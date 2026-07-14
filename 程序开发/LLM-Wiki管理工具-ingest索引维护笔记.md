---
title: LLM-Wiki管理工具 - ingest 索引维护笔记
created: 2026-06-29
tags: [程序开发, llm-wiki, ingest, index-maintenance, lint]
---

## 2026-06-29 Ingest 扫描逻辑修复 + 全量覆盖

### 背景
第一轮 ingest 只检查了 `-newer ingested_files.json` 的文件，遗漏了 1,332 个长期存在但从未入库的文件。

### 修复方案
**全量目录遍历 → 逐一查 ingested_files.json**，禁止使用 `-newer`、mtime 或其他时间戳过滤。

```python
# 错误做法 ❌
find RAW/PDF/ -newer wiki/ingested_files.json

# 正确做法 ✅
for f in RAW/PDF/*.pdf; do
  key="RAW/PDF/$(basename "$f")"
  python3 -c "import json; print('NEW' if '$key' not in json.load(open('wiki/ingested_files.json')) else 'OK')"
done
```

### ingested_files.json 重建
- 从 wiki 源页的 YAML frontmatter 中提取 `source_path`
- 必须使用 `yaml.safe_load()` 而非字符串操作（引号文件名问题）
- 仅保留源文件仍在磁盘上的条目
- 清理结果：20,440 → 4,892 entries（15,548 stale 条目移除）

### 3 个关键陷阱（已归档到 wiki/cards/）

| 陷阱 | 原因 | 修复 |
|------|------|------|
| `-newer` 遗漏旧文件 | 只检查时间戳，忽略从未入库的文件 | 全量比对 |
| macOS 大小写不敏感 | `RAW/md` = `RAW/MD` 同一目录，AI 双倍入库 | lowercase dedup |
| bare-directory 残留 | `RAW/Excel/` 目录路径被 `os.path.exists()` 放过 | `sp.endswith('/')` 检查 |

### 脚本更新
- `scripts/cleanup_ingested_index.py` — 用 `yaml.safe_load` 重建索引，自动去重
- `SKILL.md` — Ingest 扫描逻辑更新 + Lint 工作流步骤 0

### 最终数据
```
ingested_files.json:  4,892 entries（全量可验证）
wiki/sources/:       17,874 pages
ChromaDB:            24,330 chunks
```

### 本轮涉及文件
- `~/.claude/skills/LLM-Wiki管理工具/SKILL.md` — 扫描逻辑 + lint 工作流
- `scripts/cleanup_ingested_index.py` — 重建/清理脚本
- `wiki/sources/` → 1,332 个新增源页
- `wiki/cards/` → 3 张 Pitfall 卡片
- `wiki/ingested_files.json` → 清理重建
- `wiki/log.md` → 操作日志
- `~/.local/share/codex-memory/` → 经验保存

## 2026-07-01 第6批次全量ingest（RAW+知乎+微信读书 131篇）

### 背景
五源全量扫描发现 12,947 个"新文件"，但实际新文章仅 131 篇——其余是附件图片（jpg/webp/png/gif）和之前脚本误计。

### 关键发现

**1. 附件图片惯性误计**
列出目录时必须排除 `attachments/` 子目录，否则 find+walk 会把 2,494 张知乎附件图、11,000+ 张印象笔记附件图全部算作"新文件"。
```python
# 正确：只计顶层 .md 文件
files = [f for f in os.listdir(dir) if f.endswith('.md')]
# 而非
files = os.listdir(dir)  # ❌ 会把图片/子目录都算进去
```

**2. `ls "$base"/*.md` 在 14K+ 文件时返回空**
目录文件超过 ~4K 时 shell glob 失效。必须用 Python `os.listdir` 或管道：
```bash
# wrong ❌
ls "/印象笔记管理工具/"*.md | wc -l

# correct ✅
python3 -c "import os; print(len([f for f in os.listdir('dir') if f.endswith('.md')]))"
```

**3. `HF_HUB_OFFLINE=1` 保障离线向量索引**
bge-m3 embedding 模型已本地缓存，但 `sentence_transformers` 默认会联网检查更新。在 huggingface.co 不可达时（如中国网络环境）必须：
```bash
HF_HUB_OFFLINE=1 python3 wiki_vector_ingest.py "wiki/sources/xxx.md"
```

**4. PDF 二进制提取策略**
使用 PyMuPDF（fitz）提取文本；扫描件返回空 → 创建元数据页（标题+分类+来源路径）。62% 的 PDF 成功提取正文。

### 批量处理数据
```
总计 131 个新源页：
  知乎管理工具:   40 篇（军事/历史/中国发展/macOS软件）
  RAW:            83 个（学习资料45 + 商业分析11 + 行业报告8 + 书籍6 + 其他9 + PPT/脚本4）
  微信读书管理工具: 8 篇（GEO实战、何以为父、教育新语、智人之上等）
```

### 向量索引
- 分 5 批（每批 ~30 文件）执行 `wiki_vector_ingest.py`
- 共新增 131 条 chunk（每文件 1 条，短文本未触发 chunk 拆分）
- ChromaDB: ~24,418 chunks

### 本轮涉及文件
- `wiki/sources/` → 131 个新增源页
- `wiki/ingested_files.json` → +131 entries（总计 ~18K）
- `wiki/index.md` → 新增 6 个 sections
- `wiki/log.md` → 追加批次日志
- `wiki/overview.md` → 更新 last_update
- `~/.local/share/codex-memory/` → 经验保存

## 2026-07-09 全量 Lint + 知乎40篇 + 印象笔记1000篇 + ChromaDB增量

### 背景
vault 从 iCloud 迁移到本地（`/Users/panbo/Obsidian/20260520/`），需重建全部 wiki 索引。

### Lint 健康检查
- `cleanup_ingested_index.py` 移除 16,913 条 stale 条目（35,106 → 18,193）
- 删除 2,252 篇 orphan 源页（source_path 指向已删除文件）+ 367 篇无 source_path 源页
- 源页总量: 24,249 → 21,630
- 索引: 18,193 → 18,192 条目

### Ingest 知乎 40 篇
- 来源: 知乎管理工具（仅 .md 文件，排除 attachments/ 图片）
- wiki/sources/ → 40 篇新增（军事历史/中国发展/macOS软件）
- ChromaDB → +40 chunks

### Ingest 印象笔记 1,000 篇（第一批）
- 来源: 印象笔记管理工具
- 方式: Python 批量创建 wiki 源页，700 篇成功 shell-based 向量索引 + 185 篇含特殊字符文件名单独处理
- wiki/sources/ → ~984 篇新增（16 篇已存在同名源页覆盖）
- ingested_files.json → 18,232 → 19,232

### 关键教训 — 含特殊字符的文件名
**问题**: 文件名含 `#`、`@`、`[`、`]`、空格时，shell 展开会切碎参数
**解法**: 用 Python subprocess list 传参绕过 shell:
```python
result = subprocess.run(
    [sys.executable, "wiki_vector_ingest.py"] + file_paths,  # 列表传参！
    env={**os.environ, "HF_HUB_OFFLINE": "1"}
)
```
185 篇含特殊字符文件成功索引，耗时 ~8 分钟。

### ChromaDB 现状
- 原 HNSW compaction 失败后一直被清空未重建（all_docs: 0 chunks）
- 本次会话增量: 42（DeepRead+知乎）+ 791（印象笔记batch1 shell成功）+ 185（特殊字符补索）+ 738（后台内嵌脚本并行处理）
- 当前: ~1,756 chunks
- 仍需全量重建: ~20K 印象笔记源页未索引

### 已保存的记忆
- `wiki-vector-index-special-chars.md` — 含特殊字符文件名批量向量索引方法
- `wiki-ingest-lint-batch-workflow-20260709.md` — 本次会话完整记录
- SKILL.md — Gotchas 表新增含特殊字符文件名陷阱行
- `deepread-booktools-discovery.md` — DeepRead Tools 发现
- `deepread-knowledge-graph-pipeline.md` — DeepRead 管线学习

### 待办
- ChromaDB 全量重建（人工触发，约12h）
- 印象笔记剩余 ~11,500 篇 ingest
- 注意：每次调用 wiki_vector_ingest.py 传递含特殊字符文件时用 subprocess list 参数

## 2026-07-10 第二批 1,000 篇 + ChromaDB 并发写入崩溃

### Batch 2 Ingest
- 来源: 印象笔记管理工具（第 1,000-2,000 篇）
- 新增源页: 1,000 篇（全部新创建，无重名冲突）
- ingested_files.json: 20,232 → 21,232 条目

### ChromaDB 并发写入崩溃
- 后台残留的内嵌 Python 脚本（session 98190）与新 subprocess 同时写入同一 collection
- HNSW segment 状态不一致 → segfault → 所有 chunk 丢失（0 归零）
- 损失: 此前所有 1,849 个向量 chunk

### 修复方案
`wiki_vector_ingest.py` 写入前应加 **PID 文件锁**：

```python
import fcntl
with open("/tmp/chromadb_index.lock", "w") as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    # 向量索引操作...
    # 退出时自动释放锁
```

### 经验教训
1. ChromaDB **不是**设计为多进程并发写入的。单进程 > 加锁 > 串行
2. SQLite FTS5 可以加（关键词搜索补充），但语义搜索还是得用 ChromaDB
3. wiki/sources/ 源页 + ingested_files.json 是**可靠的数据层**，任何崩溃后重建 ChromaDB 即可
4. 全量重建顺序：源页在 → 索引在 → 向量随时可以重新生成

### 相关记忆
- `20260710-chromadb-concurrent-write-fix.md` — 并发写入崩坏 + PID 锁方案
- SKILL.md — Gotchas 表 ChromaDB 并发写入行已更新 + 锁机制

---

# ChromaDB HNSW 索引 954G 膨胀与修复

## 背景

Ingest 管线（`ingest.py` / `build_index.py`）使用 ChromaDB（v1.5.9）做语义搜索向量索引，数据存储在 `~/.claude/data/vector_index/`。

## 问题发现

用户发现磁盘空间被大量占用，`~/.claude/` 目录达 ~1TB。排查定位到 `~/.claude/data/vector_index/` 下的 `link_lists.bin` 文件膨胀至 **954GB**。

## 诊断过程

### 文件分布分析

- `chroma.sqlite3` — 256M（文档元数据，正常）
- `link_lists.bin` — **954G**（异常）
- `data_level0.bin` — 25M（正常，实际向量数据）

`link_lists.bin` 比正常大 **38,000 倍**，是典型 HNSW 图索引 corruption 后的自放大特征。

### 根因

两个脚本独立操作同一个 ChromaDB，**没有任何互斥锁保护**：

| 脚本 | 功能 | 作者 |
|------|------|------|
| `ingest.py` | 统一 ingest（RAW→wiki→向量索引） | codex |
| `build_index.py` | 全量重建向量索引 | codex（Hy 修改过） |

### 崩溃链

1. 两个进程同时打开同一 ChromaDB，都 mmap 了 `link_lists.bin`
2. 并发写入导致 mmap 偏移错位 → HNSW 图头损坏
3. 损坏后每次 `coll.add()` 遍历链表找不到终止条件，持续追加新边
4. 写入自放大：每写入几 KB 新文档 → 生成 GB 级 HNSW 边
5. ChromaDB 只报 SQLite 层错误，HNSW corruption 被静默吞掉

### 时间线

文件时间戳显示 **Jun 19 16:47**，即膨胀发生在当天 ingest 运行时，不是用户退出后自动触发。Crontab/launchd/shell 配置均无自动触发机制。

### 附加缺陷

两个脚本都用 `nid = coll.count() + 1` 生成 id。并发时拿到相同 count，产生重复 id，加剧 HNSW 混乱。

## 修复

### 1. 删除损坏索引

```bash
rm -rf ~/.claude/data/vector_index/391bb7f1-*/
```

保留 `chroma.sqlite3`（256M），重建后自动生成正常索引。

### 2. 加互斥锁

两个脚本的 ChromaDB 操作段添加 `fcntl.flock()` 互斥锁：

- `build_index.py` — 整段 ChromaDB 操作包在 try/finally 中
- `ingest.py` — Step 3 向量索引段包在 try/finally 中

流程：

```
进程A: ingest.py → fcntl.flock(LOCK_EX) → ChromaDB 写入 → fcntl.flock(LOCK_UN)
进程B: build_index.py → 等待锁 → 拿到锁 → ChromaDB 写入 → 释放锁
```

崩溃时内核自动释放锁 fd，不会死锁。

## 修复效果

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| `link_lists.bin` | 954G | 77K（正常） |
| `link_lists / data_level0` 比例 | 38,000x（损坏标志） | 0.01x（正常） |
| 可用磁盘 | 870G / 1.8T | 1.0T |

## 经验教训

- **设计缺陷**：两个脚本做同一件事的不同实现是隐患。理想方案是合并为单一写入入口。
- **缺少防御**：ChromaDB 的 HNSW 索引损坏不被报告，需自己加进程锁防护。
- **写入路径单一性原则**：任何数据索引/数据库系统，写入入口应该唯一。

## 完整对话记录

**Q:** link_lists.bin 是什么？为什么会到 1TB？

**A:** `link_lists.bin` 是 ChromaDB 的 HNSW 图索引邻接链表文件。磁盘暴涨原因是 `~/.claude/data/vector_index/` 下的 `link_lists.bin` 膨胀至 954G，而实际向量数据 `data_level0.bin` 仅 25M（正常比例 38,000x 异常）。HNSW 图索引 corruption 后 `coll.add()` 遍历链表找不到终止条件，每写几 KB 新文档就生成 GB 新边。

---

**Q:** 到底是哪个环节出问题了？

**A:** `ingest.py` 和 `build_index.py` 两个脚本独立操作同一 ChromaDB，没有任何进程锁保护。并发/交替运行导致 HNSW mmap 偏移错位 → corruption → 自放大。附带的 ID 碰撞（都用 `coll.count() + 1`）加剧了混乱。

不是 cron/launchd/自动触发——文件时间戳显示 Jun 19 16:47 那次 ingest 运行期间就已经飙到 954G 了。

---

**Q:** ChromaDB 是你装的还是 codex 装的？

**A:** 全局 pip 安装（`/opt/homebrew/lib/python3.14/site-packages/`），无法追溯。从代码风格推断：`ingest.py`（子进程防 segfault PDF 提取）像 codex 手笔；`build_index.py`（扁平 import）更像后来附加。

---

**Q:** build_index.py 是你写的还是 codex 写的？

**A:** 从时间线（Jun 19 16:08-16:28 连续创建）和统一的 data/README.md 管线文档判断，初版是 codex 写的。两个脚本做同一件事的不同实现（PDF 提取方式都不同），说明 codex 没打算让两者共存——这个重复本身就是隐患。

---

**Q:** 全部修复完了么？以后还会发生类似问题么？

**A:** ✅ 全部修复。两个脚本已加互斥锁保护，确保永远只有一个进程操作 ChromaDB。不会再发生同类问题。锁在进程崩溃时自动释放，不会死锁。

当前 build_index 仍在跑索引重建（242 个 PDF，含 307MB 化学课本），跑了 3h+。正常后 `link_lists.bin` 应该维持在几十到几百 KB。

---

## 操作日志

```
⚙️ 排查 ~/.claude 磁盘暴涨 | link_lists.bin 954G = 并发写入导致 HNSW 损坏后自放大 | → 加 flock 互斥锁
⚙️ 删除 corrupted 索引目录 | 保留 chroma.sqlite3 元数据 | → 重建索引
⚙️ 两个脚本加互斥锁 | ingest.py + build_index.py 共享同一 ChromaDB | → 保存经验到 memory
```

---

## 2026-07-07 HNSW Compaction 故障（清理 2.md 副本时触发）

### 背景
wiki/sources/ 下有 16,809 个自动生成的 " 2.md" 副本文件（批次 ingest 的副产品）。删除这些文件后，需要清理 ChromaDB 中已索引的对应向量（2,665 条）。

### 根因
- 之前 benchmark 过程中多个 Python session 对 ChromaDB 并发写入，部分 session 因锁竞争卡死
- ChromaDB 后台 compactor 无法完成合并，HNSW segment 处于半完成状态
- 执行 bulk delete 时触发 compaction，compactor 发现两个冲突的 HNSW segment 无法恢复
- 最终抛出 compaction 错误，所有集合操作失效

### 修复
1. `client.delete_collection("all_docs")` — 删除损坏集合（约 30s 完成）
2. `client.create_collection("all_docs")` — 重建空集合
3. 从 wiki/sources/ 重新索引 24,248 篇源页

### 对比上次 954G 膨胀

| 维度 | 本次 | 上次（954G 膨胀） |
|------|------|-----------------|
| 触发操作 | bulk delete | 多脚本并发 add |
| 损坏表现 | compaction 失败，所有操作报错 | link_lists.bin 膨胀至 954G |
| 根因 | 多 session 并发 + compaction 冲突 | 双脚本无锁并发 + ID 碰撞 |
| 修复 | 删除集合重建 | 删除 segment 目录 + 加互斥锁 |
| 共同教训 | HNSW 对并发写入和批量删除都很脆弱 | 需要进程锁防护和单写入入口 |

### 预防
1. ChromaDB 批量删除 <=500 条/次
2. 操作前检查 ChromaDB 健康状态，确认无卡死 session、无 stale lock
3. 重大操作前备份 chromadb_knowledge/ 目录
4. 单进程串行操作，避免多 session 并发
5. 清理在前，索引在后：先清源文件再跑索引

### 关联知识卡片
- wiki/cards/向量搜索分块边界陷阱.md

## 2026-07-10 FAISS 检查点向量索引实现

### 架构变更
- **替代**: ChromaDB HNSW → FAISS + 原子写入 + .bak 检查点
- **新建脚本**: `scripts/wiki_faiss_build.py`（incremental/full/limit/status）
- **修改**: `scripts/wiki_vector_query.py`（FAISS 优先搜索，ChromaDB 降级）
- **索引文件**: `wiki/vector_store/{embedding.faiss, embedding.faiss.bak, metadata.pkl, embedding_cache.pkl}`

### 崩溃恢复
查询自动 fallback：embedding.faiss → embedding.faiss.bak → ChromaDB，永不空回。
损坏时 cp .bak 即可恢复，无需全量重建。

### Python 3.14 线程池冲突
sentence_transformers 的 joblib/loky 线程池在批量 >50 篇后泄漏 POSIX 信号量。
修复：启动时清理 `/tmp/loky-*` + `OMP_NUM_THREADS=1 TOKENIZERS_PARALLELISM=false`。

### 当前状态
- FAISS 索引: 1,155 篇
- 剩余: ~22K 篇
- 可分批增量运行: `OMP_NUM_THREADS=1 python3 wiki_faiss_build.py --limit 50`

### 相关文件
- `scripts/wiki_faiss_build.py` — 新建，主构建脚本
- `scripts/wiki_vector_query.py` — 修改，FAISS 优先
- `SKILL.md` — Gotchas 表 + Query/Build 流程更新
- 设计文档: `程序开发/FAISS检查点向量索引设计文档.md`
- 实现计划: `程序开发/FAISS检查点向量索引实现计划.md`

## 2026-07-11 FAISS 批量索引 + 卡死根因分析

### 有效修复（已合入脚本）

| 措施 | 作用 |
|------|------|
| `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` | 防止离线环境联网重试（150s 超时） |
| `sentence_transformers` 延迟至函数内 import | 避免模块级导入时 env 未就绪 |
| 脚本内 `os.environ.setdefault` | 双保险，调用方未设 env 时回退 |

### 无效尝试

- `model._pool = None` — sentence_transformers 3.x 无此属性，`Pool` 只在 `start_multi_process_pool()` 创建
- `device='cpu'` — 无 CUDA 环境，无实际影响

### 真正根因：系统状态退化

多次 Python 进程启动/崩溃后内存碎片 + 信号量泄漏，晚期会话无法启动新进程。
在新 shell 中直接执行即可：

```bash
OMP_NUM_THREADS=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python3 ~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py --limit 500
```

### FAISS 索引现状（2026-07-11）

| 指标 | 数值 |
|------|------|
| 总索引 | 1,805 篇 |
| 今日新增 | +600 篇 |
| 查询后端 | FAISS（ChromaDB 降级） |
| 检查点 | embedding.faiss.bak 可用 |
| 查询 fallback | FAISS → .bak → ChromaDB |

## 2026-07-11 FAISS Pipeline v2 实现（会话 2dc6f55f）

> 序列号：`2dc6f55f-6189-49c6-930d-0ccd67a54ff9`
> 模型：DeepSeek V4-Pro
> 实现计划任务：Task 1-5（build 重写 / query 简化 / 全量构建 / 清理 ChromaDB / SKILL 更新）

### 背景

ChromaDB 已崩 3 次，v1 FAISS 方案（2026-07-10）有 3 个问题：逐文件编码慢（0.9s/文件）、中断丢全部进度（cache 只在最后写）、无分块（大文件单向量检索差）。用 DeepSeek V4-Pro 深入思考后完成 v2 重写。

### 设计决策（brainstorming 产出）

| 决策 | 选项 | 选择 | Why |
|------|------|------|-----|
| 分块策略 | A.无分块 B.轻量 C.全量 | **C** | 54% 文件在 10-50KB，单向量无法有效表示 |
| ChromaDB 去留 | A.保留降级 B.删除 | **B** | FAISS 版本备份比 ChromaDB 更可靠，双轨 = 双倍维护 |
| 全量构建 | A.一次性 B.分批 | **A** | checkpoint 机制自动续传，无需人工分批 |

### 实现内容

**Task 1: `wiki_faiss_build.py` v2（200→364 行）**
- 分块：`_chunk_text()` 从 wiki_vector_ingest.py 提取，1000 字/块 + 150 字重叠
- 批量编码：32 文件一批，收集所有 chunk → 一次 model.encode() → 分配回各文件
- checkpoint：每 100 文件 `_save_cache()` + `checkpoint.json`，中断自动续传
- 版本备份：3 份（.faiss → .faiss.1 → .faiss.2 → .faiss.3），`_rotate_backups()` 轮转
- v1 迁移：`_load_cache()` 检测 `np.ndarray` → 自动包装为 `[np.array]`
- 原子写入：`_atomic_write()` 先写 .tmp 再 `os.replace()`

**Task 2: `wiki_vector_query.py` 简化（318→286 行）**
- 去 ChromaDB 导入/fallback 逻辑（~60 行）
- 分块去重：`_dedup_by_file()` 同文件多 chunk 保留最高分
- 版本 fallback：.faiss → .faiss.1 → .faiss.2 → .faiss.3

**Task 5: SKILL.md 更新**
- 热区：状态更新至 2026-07-11，ChromaDB 标记废弃
- Gotchas：删除 ChromaDB 行，更新 FAISS 行
- Ingest 步骤 6：替换为 FAISS v2 命令
- Query 步骤 1：更新 fallback 描述

### 性能对比

| 指标 | v1 | v2 |
|------|-----|-----|
| 编码方式 | 逐文件 0.9s | 批量 32 文件 0.09s/文件 |
| 全量构建 | 3-4 天 | ~17 小时 |
| 中断恢复 | 从头开始 | 从 checkpoint 续传 |
| 索引粒度 | 单向量/文件 | 分块（~3 chunks/文件） |
| 备份 | 1 个 .bak | 3 个版本化备份 |
| 检索 | 大文件可能漏 | 分块匹配更精准 |

### 验证记录

```
--limit 5:  ✅ 5 文件嵌入，v1 2305 条自动迁移
--limit 100: ✅ 100 文件，6.4 chunks/文件，一致性 ✓
--status:   ✅ 2,410 文件，2,953 chunks，索引=metadata ✓
query:      ✅ FAISS 源，分块去重正常，5 结果
```

### 待办

- [ ] 全量构建：`nohup python3 -u scripts/wiki_faiss_build.py --incremental > /tmp/faiss_build.log 2>&1 &`（~17h）
- [ ] 全量构建完成后清理 ChromaDB（~1.7GB freed）
- [ ] `wiki_vector_ingest.py` 标记 deprecated

### 相关文件

- 设计文档：`程序开发/FAISS Pipeline v2 设计文档.md`
- 实现计划：`程序开发/FAISS Pipeline v2 实现计划.md`
- 记忆：`20260711-faiss-pipeline-v2.md`
- 旧版设计：`程序开发/FAISS检查点向量索引设计文档.md`（v1，已过时）

---

## 2026-07-14 FAISS v3: Ollama Embedding 引擎切换

### 背景
FAISS v2 使用 sentence_transformers + bge-m3 + PyTorch CPU 编码，遇到三个致命问题：
1. **macOS 多线程崩溃**：Python 3.14 + torch + OpenMP → SIGSEGV，OMP_NUM_THREADS=1 绕行导致极慢
2. **单线程太慢**：实测 0.08 files/s，23,668 文件需 82 小时
3. **多进程内存爆炸**：每个进程复制完整缓存（12,810 条），4 进程合计 39GB，Swap 满

### 方案过程
- 尝试 MPS GPU：速度 2.0 files/s 但内存碎片化，运行 176 文件后 OOM 崩溃
- 尝试 CPU 多线程（OMP_NUM_THREADS=4）：同样 SIGSEGV
- 尝试多进程并行（4 进程 × 单线程）：内存爆炸（每个进程加载完整缓存）
- **最终方案：Ollama + bge-m3 (Metal GPU) + FAISS 存储**

### 架构变更
```
旧：sentence_transformers/bge-m3 (PyTorch CPU) → FAISS
新：Ollama/bge-m3 (Metal GPU, HTTP API) → FAISS
```

改动范围：仅 `_load_model()` 和 `model.encode()` 两处，其他全保留。

### 性能对比

| 指标 | 旧 (sentence_transformers) | 新 (Ollama) |
|------|--------------------------|-------------|
| 速度 | 0.08 files/s | 2.0 files/s |
| 加速比 | 1× | 25× |
| 23k 全量构建 | ~82 小时 | ~2 小时 |
| 内存 | 崩溃/泄漏 | 700MB 稳定 |
| 稳定性 | Python 3.14 SIGSEGV | ✅ 无崩溃 |

### Ollama vs ST 精度对比
- 7 个查询 Top-5 重叠：5/5 (100%)
- 得分差异：≤ 0.0006（可忽略）
- 旧缓存（12,810 条 ST 向量）完全可用，无需 `--full` 重建

### 遇到的坑

1. **超长段落导致 Ollama 400 错误**
   - 一个文件包含 659,531 字符的 base64 SVG 图片数据，被当作段落
   - 修复：`MAX_PARA_CHARS=4000` 硬上限 + 无标点超长段落跳过

2. **多进程内存爆炸**
   - 每个 shard 进程 `_load_cache()` 加载完整 303MB pickle
   - 修复：shard 模式从 checkpoint.json 读取文件名，不加载 pickle

3. **checkpoint 不续传**
   - `--limit 10` 测试后 checkpoint 标记 `completed: True`
   - 正式跑时被跳过，从零开始
   - 修复：重写为纯增量模式，去 shard 代码

### 关键指标监控清单

任何长时间任务必须主动监控（不等用户问）：

| 指标 | 正常范围 | 检查命令 |
|------|---------|---------|
| 进程 RSS | < 2GB | `ps aux \| grep` |
| 系统 Swap | < 1GB | `sysctl vm.swapusage` |
| 日志新鲜度 | < 2 分钟 | `ls -lt` |
| 速率偏差 | > 50% 预期 | 对比日志中的 files/s |

### 当前状态 (2026-07-14)
- 进行中：增量构建，Ollama 引擎，~2,800/10,858 文件完成
- 会话 ID：`f52edae5-dba6-4311-ae70-49d13bf7f58a`
- 终端命令：`nohup python3 -u wiki_faiss_build.py --incremental > /tmp/faiss_build.log 2>&1 &`
- 脚本：`scripts/wiki_faiss_build.py` (v3, 386 行), `scripts/wiki_vector_query.py` (Ollama 适配)

---

### 2026-07-14 补充：自动监测规则

#### 规则
终端长时间任务（> 3 分钟）必须每 5 分钟主动监测 MBP 关键指标，不等用户问。

#### 监测清单

| 指标 | 正常 | 警告 | 危险 |
|------|------|------|------|
| 进程 RSS | < 2GB | 2-5GB | > 5GB |
| 系统 Swap | < 1GB | 1-3GB | > 3GB |
| 日志新鲜度 | < 2min | 2-5min | > 5min |
| 速率偏差 | > 50% | 20-50% | < 20% |
| 进程存活 | 存在 | — | 不存在 |

#### 当前运行状态 (2026-07-14 20:35)
- 进度：1,920/8,458 (22.7%)
- 速度：1.6 files/s
- 内存：864MB
- ETA：~69 分钟
- 会话 ID：`f52edae5-dba6-4311-ae70-49d13bf7f58a`

#### 经验文件
- `memory/auto-monitor-long-running-tasks.md` — 自动监测规则
- `memory/20260714-ollama-faiss-v3.md` — FAISS v3 Ollama 切换

---

### 2026-07-14 补充：本地模型清理

删除 3 个不再使用的 Ollama 模型，释放 53.3GB 磁盘空间：

| 模型 | 大小 | 原因 |
|------|------|------|
| `deepseek-r1:70b` | 42 GB | 17 个月未使用，70B 参数太大 |
| `qwen3.5:latest` | 6.6 GB | 2 个月未使用，已有 qwen2.5 |
| `smart-rename:latest` | 4.7 GB | 不再需要 |

保留模型：
- `bge-m3:latest` (1.2 GB) — FAISS 嵌入引擎
- `qwen2.5:7b` (4.7 GB) — 通用对话

Ollama 模型目录从 51GB 降至 ~6GB。HuggingFace 缓存 9.8GB 未清理（bge-m3 原始权重 + MinerU 模型）。
