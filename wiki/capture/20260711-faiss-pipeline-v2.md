---
title: 20260711-faiss-pipeline-v2
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## FAISS Pipeline v2 实现（2026-07-11）

### 背景
ChromaDB 崩过 3 次（954G 膨胀、compaction 失败、segfault 归零），v1 FAISS 方案有 3 个问题：逐文件编码慢（0.9s/文件）、中断丢进度、无分块。DeepSeek V4-Pro 模型下完成 v2 重写。

### 关键决策

| 决策 | Why |
|------|-----|
| 分块（C 方案）| 54% 文件在 10-50KB，单向量无法有效表示；复用 ChromaDB 已验证的分块逻辑 |
| 批量编码 32 文件一批 | 0.09s/文件 vs 0.9s/文件，10x 提速 |
| checkpoint 每 100 文件 | 中断最多丢 100 个文件的进度，自动续传 |
| 版本化备份 3 份 | .faiss → .faiss.1 → .faiss.2 → .faiss.3，查询自动 fallback |
| 删除 ChromaDB | FAISS 有版本备份比 ChromaDB 更可靠；保留双轨 = 维护两套代码 |

### 实现细节

**`wiki_faiss_build.py` v2（364 行）：**
- 分块：`_chunk_text()` 从 wiki_vector_ingest.py 提取，1000 字/块 + 150 字重叠
- 批量：攒 32 个文件的所有 chunk → 一次 model.encode() → 分配回各文件
- checkpoint：每 100 文件 `_save_cache()` + `checkpoint.json`
- 版本轮转：`_rotate_backups()` 删除 .3 → .2→.3 → .1→.2 → 当前→.1
- v1 迁移：`_load_cache()` 检测 `np.ndarray` → 自动包装为 `[np.array]`
- 原子写入：`_atomic_write()` 先写 .tmp 再 `os.replace()`

**`wiki_vector_query.py`（286 行，-32 行）：**
- 去 ChromaDB 导入/fallback 逻辑
- 分块去重：`_dedup_by_file()` 同文件多 chunk 保留最高分
- 版本 fallback：.faiss → .faiss.1 → .faiss.2 → .faiss.3

**`SKILL.md`：**
- 热区、Gotchas、Ingest、Query 全部更新

### 性能

| 指标 | v1 | v2 |
|------|-----|-----|
| 编码速度 | 0.9s/文件 | 0.3 files/s（含分块+编码） |
| 全量构建 | 3-4 天 | ~17 小时 |
| 中断恢复 | 从头开始 | 从 checkpoint 续传 |
| 索引粒度 | 单向量/文件 | 分块（~3 chunks/文件） |
| 备份 | 1 个 .bak | 3 个版本化备份 |

### 当前状态（2026-07-12）
- FAISS 索引：3,210 文件，8,947 chunks（cache），2,953 chunks（FAISS 索引文件，待 rebuild）
- 全量构建进行中：Warp 终端运行，从 checkpoint 续传（已处理 800/21,258 新文件）
- 系统更新中断过一次（2026-07-12 凌晨），checkpoint 机制已续传
- ChromaDB 待全量构建完成后清理（1.7GB）
- v2 构建脚本（364 行）+ 查询脚本（286 行）已就绪
- 相关会话：`2dc6f55f-6189-49c6-930d-0ccd67a54ff9`（设计+实现）、`f52edae5-dba6-4311-ae70-49d13bf7f58a`（续传+进度检查）

### 相关文件
- 设计文档：`程序开发/FAISS Pipeline v2 设计文档.md`
- 实现计划：`程序开发/FAISS Pipeline v2 实现计划.md`
- 维护笔记：`程序开发/LLM-Wiki管理工具-ingest索引维护笔记.md`
- 脚本：`scripts/wiki_faiss_build.py`, `scripts/wiki_vector_query.py`

### 如何应用
- 每次 ingest 后跑 `wiki_faiss_build.py --incremental`
- 中断后重跑同命令，自动续传
- 查询自动 fallback 版本备份，永不空回
- 全量构建命令：`OMP_NUM_THREADS=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python3 -u scripts/wiki_faiss_build.py --incremental > /tmp/faiss_build.log 2>&1 &`
