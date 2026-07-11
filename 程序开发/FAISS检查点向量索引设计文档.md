# FAISS 检查点向量索引设计方案（v1，已过时）

> ⚠️ **已由 [FAISS Pipeline v2](FAISS Pipeline v2 设计文档.md) 替代（2026-07-11）。** v2 增加分块+批量编码+checkpoint+版本备份。保留此文档作为设计演进记录。

## 背景

LLM Wiki 使用 ChromaDB + bge-m3 做语义搜索。ChromaDB 的 HNSW 图索引对并发写入和批量删除极其脆弱，截至 2026-07-10 已崩溃三次：
- 两脚本无锁并发写入 → link_lists.bin 膨胀至 954G
- bulk delete 触发 compaction 失败 → 全库无法操作
- 后台残留进程 + 新进程并发写入 → segfault → 全库归零

现有修复方式（PID 文件锁）只能防并发写入，无法防 compaction 崩坏。崩了一次后必须从 wiki/sources/ 全量重建（实测 ~3-4 天，23,668 文件在 CPU 上 15-20 秒/文件）。

## 目标

1. 语义搜索必须（grep 不够）
2. 崩了不能从头重建，必须有快速恢复机制
3. 稳定的单进程构建流程

## 存储结构

### 三个文件，全部在 `wiki/vector_store/`

```
wiki/vector_store/
├── embedding_cache.pkl    ← {filename: embedding} 缓存，避免重复 embed
├── embedding.faiss        ← FAISS HNSW 索引（仅向量，搜索用）
└── metadata.pkl            ← [filename, source_path, chunk_text]，顺序对应 FAISS 索引位置
```

| 文件 | 大小估计 | 写入方式 |
|------|---------|---------|
| `embedding_cache.pkl` | ~2GB（22K × 1024维 × float32） | 追加新条目，不修改旧 |
| `embedding.faiss` | ~1MB（HNSW图索引） | 原子 rename |
| `metadata.pkl` | ~50MB | 原子 rename |

### 检查点机制

每次成功 build 后 `cp embedding.faiss embedding.faiss.bak`。build 崩溃 → `.faiss` 半截 → `.bak` 完好。查询时自动 fallback。

## Build 管线（`wiki_faiss_build.py`）

```
1. 读取 embedding_cache.pkl（已有嵌入）
2. 扫描 wiki/sources/，对比 cache 找出新文件
3. 只对新文件跑 bge-m3 embed（最慢步骤，但只对新文件）
4. 合并新旧嵌入
5. 建 FAISS HNSW 索引（22K 篇约几秒）
6. 写入 embedding.faiss（原子 rename，避免写半截）
7. 写入 metadata.pkl（原子 rename）
8. 更新 .bak 检查点
```

### 原子写入

```python
# 先写临时文件
faiss.write_index(index, "embedding.faiss.tmp")
with open("metadata.pkl.tmp", "wb") as f:
    pickle.dump(metadata, f)

# 原子 rename
os.rename("embedding.faiss.tmp", "embedding.faiss")
os.rename("metadata.pkl.tmp", "metadata.pkl")
# .tmp 文件在下次启动时清理
```

### 模式

| 模式 | 触发 | 耗时 |
|------|------|------|
| `--incremental`（默认） | ingest 后 | 仅新文件 embed + FAISS 重建（几秒） |
| `--full` | 模型升级或 cache 损坏 | 全量 re-embed（实测 ~3-4 天） |

### 和现有 ingest 配合

```
当前:  ingest 新文件 → wiki_vector_ingest.py → ChromaDB add
替换后: ingest 新文件 → wiki_faiss_build.py --incremental → 原子写 .faiss + .bak
```

`wiki_vector_ingest.py` 中 ChromaDB 相关代码保留不动（作为 fallback），但不再是主要路径。

## Query 管线

改造 `wiki_vector_query.py`，核心搜索路径改为 FAISS：

```
1. bge-m3 embed 用户问题
2. 加载 embedding.faiss（失败时自动读 .bak）
3. FAISS search（top-N，<50ms）
4. 从 metadata.pkl 取出对应文件路径和原文
5. 返回结果（格式和现有一致）
```

### 故障切换

```python
def load_index():
    for path in ["embedding.faiss", "embedding.faiss.bak"]:
        full = os.path.join(VECTOR_DIR, path)
        if os.path.exists(full):
            try:
                return faiss.read_index(full)
            except:
                continue
    raise RuntimeError("所有索引文件都不可用")
```

### 多跳模式

复用现有 `--multi-hop` 逻辑，只是向量搜索后端从 ChromaDB 换成 FAISS，上层推理逻辑不变。

## 备份与恢复

| 场景 | 操作 | 耗时 |
|------|------|------|
| build 崩溃 | 查询自动 fallback 到 .bak | 0（自动） |
| .faiss + .bak 都损坏 | `wiki_faiss_build.py --incremental` | 几秒（从 cache 重建索引） |
| cache.pkl 损坏 | `wiki_faiss_build.py --full` | ~3-4 天（全量 re-embed） |
| 硬盘故障 | 从 `wiki/sources/` 全量重建 | ~3-4 天（极端情况） |

## 依赖变化

| 依赖 | 当前（ChromaDB） | FAISS 方案 | 原因 |
|------|-----------------|------------|------|
| chromadb | ✅ | ❌ 可卸载 | 不再需要 |
| sentence_transformers | ✅ | ✅ | bge-m3 仍然用 |
| faiss-cpu | ❌ | ✅ 新增 | FAISS 索引库（~5MB，pip 装） |
| numpy | ✅（间接） | ✅ | embeddings 都是 numpy 数组 |

## 现有脚本改动范围

| 文件 | 改动 |
|------|------|
| `scripts/wiki_vector_ingest.py` | ChromaDB 写入路径保留但标记为 deprecated；新增 --faiss 模式 |
| `scripts/wiki_vector_query.py` | 搜索路径从 ChromaDB 改为 FAISS fallback chain |
| `scripts/wiki_faiss_build.py` | **新建** |
| `SKILL.md` | 更新 Build/Query 流程描述，补充 FAISS 备份恢复说明 |

## 不涉及的改动

- wiki/sources/ 内容格式：不改
- ingested_files.json：不改
- wiki/log.md 追加格式：不改
- Lint 流程：不改
- Ingest 流程（创建源页部分）：不改

---

## 2026-07-11 实践记录：FAISS 构建性能实测

> 会话 ID：`019f514b-2f35-70a1-abcc-dfcc4a43f5d2`

### 操作过程
1. 执行 `wiki_faiss_build.py --incremental --limit 500`（首次完成，缓存 2,305 文件）
2. 第二次执行同命令，在 Warp 终端跑 ~2.5 小时后手动中断
3. 中断后检查缓存——仍为 2,305 条，**本轮 ~400 个新嵌入全部丢失**

### 关键发现

| 发现 | 详情 |
|------|------|
| bge-m3 单文件速度 | CPU 上全文档 embed 约 **15-20 秒/文件**（MacBook Pro，OMP_NUM_THREADS=1） |
| 全量重建耗时 | 23,668 文件需 **3-4 天**（设计文档原估 ~2h 严重低估，已修正） |
| 缓存写入时机 | `_save_cache()` 只在 **全部文件处理完后** 调用。中途 kill 或崩溃 → 本轮新嵌入全丢 |
| 文件排序 | `sorted(os.listdir())` 按字母排序，符号/数字开头的文件排在最前 |
| 分批策略 | `--limit 500` 每次约 30-40 分钟，可在终端中分段执行 |

### 改进建议
- 脚本加增量 checkpoint：每处理 100 文件后调用 `_save_cache(cache)`，避免中断丢进度
- 或者改用 `nohup`/`tmux` 后台跑，每次 `--limit 2000`

### 当前状态
- 已缓存：2,305 / 23,668 文件（~9.7%）
- 嵌入向量维度：1024（bge-m3）
- FAISS 索引文件：embedding.faiss（9.4MB），embedding_cache.pkl（9.6MB），metadata.pkl（143KB）
