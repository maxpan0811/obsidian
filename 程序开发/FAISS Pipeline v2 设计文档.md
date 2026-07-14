# FAISS Pipeline v2 设计文档

> 替代 ChromaDB，解决知识库向量索引的稳定性、速度和备份问题。
> 设计日期：2026-07-11

## 背景

LLM Wiki 使用 ChromaDB + bge-m3 做语义搜索，ChromaDB 的 HNSW 图索引对并发写入和批量删除极其脆弱，已崩溃三次：

| 日期         | 原因                           | 结果                      |
| ---------- | ---------------------------- | ----------------------- |
| 2026-06-19 | 两脚本无锁并发写入                    | link_lists.bin 膨胀至 954G |
| 2026-07-07 | bulk delete 触发 compaction 失败 | 全库无法操作                  |
| 2026-07-10 | 后台残留进程 + 新进程并发写入             | segfault → 全库归零         |

v1 FAISS 方案（2026-07-10）已替代 ChromaDB 写入路径，但仍有三个问题：

| 问题 | 现状 | 根因 |
|------|------|------|
| 慢 | 2,305/23,668 文件已索引 | 逐文件编码，未用 batch（0.9s vs 0.09s/文件） |
| 易崩 | 中断丢全部进度 | `_save_cache()` 只在全部完成后调用 |
| 检索质量差 | 大文件（54% 在 10-50KB）只用一个向量 | 无分块（ChromaDB 有分块但不稳定） |

## 设计决策

### Why FAISS 而非其他方案

| 方案 | 为什么不选 |
|------|-----------|
| 继续用 ChromaDB | 已崩 3 次，HNSW 对并发写入和批量删除脆弱 |
| SQLite FTS5 | 只能关键词搜索，不支持语义搜索 |
| Milvus/Qdrant | 需要 Docker/服务端，过重 |
| FAISS | 纯 Python 库，无后台进程，无 compaction，原子写入天然安全 |

FAISS 的 FlatIP 索引只是一个 numpy 数组 + 内积运算，没有 HNSW 图、没有后台合并、没有 mmap 并发冲突。崩了就是文件损坏，恢复就是读 .bak。

### Why 分块（C 方案）

- 54% 的源文件在 10-50KB，单向量无法有效表示
- 复用 ChromaDB 已有分块逻辑（1000 字/块 + 150 字重叠），已验证有效
- 全量构建 ~1.8 小时，可接受

### Why 一次性全量构建（A 方案）

- checkpoint 机制每 100 文件存一次，中断可从断点续传
- 不需要人工分批触发，减少操作负担

### Why 删除 ChromaDB

- FAISS 有自己的 .bak 版本化备份，比 ChromaDB 更可靠
- 保留双轨 = 维护两套代码 + 两套数据 + 两套 fallback 逻辑
- ChromaDB 作为"降级方案"不可靠（它崩的时候你正需要它）

## 存储结构

```
wiki/vector_store/
├── embedding_cache.pkl       ← {filename: [emb1, emb2, ...]}  每文件 N 个 chunk 向量
├── embedding.faiss           ← FlatIP 索引，当前活跃
├── embedding.faiss.1         ← 版本化备份（最近 3 次成功构建）
├── embedding.faiss.2
├── embedding.faiss.3
├── metadata.pkl              ← [(filename, chunk_idx, preview), ...] 对齐 FAISS 位置
├── metadata.pkl.1/.2/.3      ← 对应版本的元数据备份
└── checkpoint.json           ← {last_file, files_done, total_files, timestamp}
```

| 文件 | 预估大小 | 说明 |
|------|---------|------|
| embedding_cache.pkl | ~290MB | 71K chunks × 1024维 × float32 |
| embedding.faiss | ~290MB | FlatIP 索引 |
| metadata.pkl | ~14MB | chunk → 文件映射 |
| 3 个版本备份 | ~900MB | 版本化回滚 |
| **合计** | **~1.5GB** | |

## Build 管线

### 入口参数

```
--incremental   增量（默认，仅新文件）
--full          全量重建（清空 cache）
--limit N       限制处理文件数（测试用）
--status        查看索引状态
```

### 主流程

```
1. 加载状态
   ├── 读 checkpoint.json → 检测是否中断续传
   ├── 读 embedding_cache.pkl → 已有嵌入
   └── 扫描 wiki/sources/ → 找出新文件列表

2. 分块 + 批量编码（核心循环）
   for batch in chunks(files, 32):
       ├── 对每个文件：读文本 → 去 YAML frontmatter → 分块
       ├── 收集所有 chunk 文本 → model.encode(batch_texts)
       ├── 存入 cache[name] = [emb1, emb2, ...]
       └── 每 100 文件：_save_cache() + 写 checkpoint.json

3. 建 FAISS 索引
   ├── 遍历 cache，展开所有 chunk → (emb, metadata)
   ├── faiss.IndexFlatIP(dim=1024).add(embs)
   └── 写 metadata.pkl

4. 原子写入 + 版本轮转
   ├── _atomic_write(index, "embedding.faiss")
   ├── _atomic_write(metadata, "metadata.pkl")
   └── 轮转备份：del .3, .2→.3, .1→.2, .faiss→.1

5. 更新 checkpoint.json（标记完成）
```

### 分块逻辑

复用现有 ChromaDB 的分块代码（已验证有效）：

- 按段落 `\n\n` 拆分
- 合并至 1000 字/块
- 相邻块 150 字重叠（防止实体-值对跨块断裂）
- 文件 < 1000 字 → 1 个 chunk

### 关键安全措施

- **原子写入**：先写 `.tmp`，再 `os.replace()`（POSIX 保证原子性）
- **checkpoint 每 100 文件**：中断最多丢 100 个文件的嵌入进度
- **索引写入失败**：`.bak` 仍然完好，查询不受影响
- **版本轮转**：保留最近 3 次成功构建，可回滚至任意版本

### 时间估算

| 场景 | 耗时 |
|------|------|
| 全量重建 23,668 文件（~71K chunks） | ~1.8 小时 |
| 增量 100 新文件 | ~10 秒 |
| 中断后续传（从 checkpoint） | 从中断点继续，不重做 |

## Query 管线

### 流程

```
1. bge-m3 embed 用户问题（单条，带 prefix）
2. 加载 FAISS 索引（.faiss → .faiss.1 → .faiss.2 → .faiss.3）
3. FAISS search（top-N × 2，< 50ms）
4. 按 metadata 取出 (filename, chunk_idx, preview)
5. 同文件多 chunk 命中 → 合并取最高分
6. 返回结果（格式与现有兼容）
```

### 故障切换链

```python
def load_index():
    for path in ["embedding.faiss", "embedding.faiss.1", 
                 "embedding.faiss.2", "embedding.faiss.3"]:
        if os.path.exists(path):
            try:
                return faiss.read_index(path)
            except:
                continue
    raise RuntimeError("所有索引文件都不可用，请运行 wiki_faiss_build.py")
```

### 代码简化

- 去掉 ChromaDB 导入和 fallback 逻辑（~60 行）
- 去掉 `query_fulltext()` 中 ChromaDB 分支
- 去掉重复的 model 加载
- 预计：318 行 → ~180 行

## 备份与恢复

| 场景 | 操作 | 耗时 |
|------|------|------|
| build 崩溃 | 运行 `--incremental`，从 checkpoint 续传 | 从中断点继续 |
| .faiss 损坏 | 查询自动 fallback 到 .faiss.1/.2/.3 | 0（自动） |
| 所有 faiss 都损坏 | `wiki_faiss_build.py --incremental` | 几秒（从 cache 重建索引） |
| cache.pkl 损坏 | `wiki_faiss_build.py --full` | ~1.8 小时（全量 re-embed） |
| 硬盘故障 | 从 `wiki/sources/` + `ingested_files.json` 全量重建 | ~1.8 小时 |

## 依赖变化

| 依赖 | 当前 | v2 | 原因 |
|------|------|-----|------|
| chromadb | ✅ | ❌ 删除 | 不再需要 |
| sentence_transformers | ✅ | ✅ | bge-m3 仍然用 |
| faiss-cpu | ✅ | ✅ | FAISS 索引 |
| numpy | ✅ | ✅ | embeddings 数组 |

## 文件改动范围

| 文件 | 改动 |
|------|------|
| `scripts/wiki_faiss_build.py` | **重写**（200 → ~250 行），加分块、批量编码、checkpoint、版本备份 |
| `scripts/wiki_vector_query.py` | **简化**（318 → ~180 行），去 ChromaDB 降级逻辑 |
| `scripts/wiki_vector_ingest.py` | 保留不动，标记 deprecated |
| `SKILL.md` | 更新 Build/Query 流程描述，去 ChromaDB 引用 |

## 不涉及的改动

- wiki/sources/ 内容格式：不改
- ingested_files.json：不改
- wiki/log.md 追加格式：不改
- Lint 流程：不改
- Ingest 流程（创建源页部分）：不改

## 迁移路径

```
1. 重写 wiki_faiss_build.py → 跑 --limit 100 验证
2. 简化 wiki_vector_query.py → 验证查询结果
3. 跑全量 --incremental（~1.8h，从当前 cache 续传）
4. 验证查询正常
5. 删除 ChromaDB 数据（~1.7GB）
6. 更新 SKILL.md
```

## 风险

| 风险 | 概率 | 缓解 |
|------|------|------|
| 批量编码内存溢出 | 低 | 32 文件一批，~100MB 内存 |
| FlatIP 索引检索慢 | 低 | 71K × 1024 维，内积 < 50ms |
| Python 3.14 loky 信号量泄漏 | 中 | 启动时清理 `/tmp/loky-*` + `OMP_NUM_THREADS=1` |
| 分块后查询结果与 ChromaDB 不一致 | 低 | 分块逻辑完全复用 ChromaDB 代码 |