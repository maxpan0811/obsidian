---
title: 20260710-faiss-impl-loky-fix
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# FAISS 检查点向量索引实现

## 架构

替换 ChromaDB 为 FAISS + 原子写入 + .bak 检查点。

**存储文件（wiki/vector_store/）：**
- `embedding_cache.pkl` — {filename: embedding} 缓存，避免重复 embed
- `embedding.faiss` — FAISS HNSW 索引
- `embedding.faiss.bak` — 成功构建的检查点
- `metadata.pkl` — [filename, ...] 列表，顺序对应 FAISS 索引位置

**Build 流程（wiki_faiss_build.py）：**
- `--incremental`（默认）— 仅新文件 embed，重建索引
- `--full` — 全量重建
- `--limit N` — 限制嵌入数（分批用）
- `--status` — 查看索引状态

**Query 流程（wiki_vector_query.py）：**
FAISS 优先 → 自动 fallback .bak → ChromaDB 兜底

## 关键坑：Python 3.14 + loky 线程池泄漏

**现象：** 批量嵌入 >50 篇时进程永久挂起，无输出，不响应 SIGTERM。

**根因：** sentence_transformers 内部用 joblib → loky 管理并行池。loky 在 `/tmp/` 下创建 POSIX 信号量文件协调子进程。某次 crash 后信号量未清理，下次运行 loky 发现陈旧信号量以为还有进程，永久等待。

**修复（已合入脚本顶部）：**
```python
import glob
for f in glob.glob("/tmp/loky-*"):
    try: os.unlink(f)
    except: pass
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
```

## 性能

| 批次 | 耗时 | 备注 |
|------|------|------|
| 5 篇 | ~7s | 首次，含模型加载 |
| 50 篇 | ~2m40s | 含模型加载 ~30s |
| 1,000 篇 | ~31m | 含模型加载，后台稳定运行 |

## 当前状态（2026-07-10）
- FAISS 索引已建：1,155 篇
- 剩余未嵌入：~22K 篇
- 脚本改造完成，可分批增量运行
