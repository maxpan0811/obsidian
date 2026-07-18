---
title: faiss-v3-oom-fix
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 问题
FAISS v3 增量构建（wiki_faiss_build.py）在处理 47,819 个新文件时，跑至 8,128/47,819（17%）被 macOS Jetsam SIGKILL（OOM）。

**根因：** `BATCH_SIZE=32` 下 batch embedding 峰值内存过高。系统 64GB RAM 占用 ~56GB，Swap 6GB 近满。

## 修复（2026-07-15）
在 `/Users/panbo/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py` 中：

| 改动 | 旧值 | 新值 | 原因 |
|------|------|------|------|
| `BATCH_SIZE` | 32 | **8** | 单次 batch 峰值内存降至 1/4 |
| `CHECKPOINT_EVERY` | 100 | **50** | 更频繁存盘，减少丢失 |
| 每批后 `gc.collect()` | 无 | **有** | 显式释放 Python 循环中的废弃对象 |
| 每批后 `time.sleep(0.5)` | 无 | **有** | 给 Ollama/Metal 留 GPU 内存释放时间 |

**提权经验：** 纯 `del` 变量不够——必须显式 `gc.collect()` + `time.sleep()`，因为 Metal GPU 内存释放是异步的。

**Why:** 首次跑时 ~4.3 files/s 的 ETA 162min，OOM 在 17% 被杀。调参后虽然单文件速度略降（~3.0 files/s），但消除了 OOM 风险，能跑完全程。

## 相关文件
- 脚本: `~/.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py`
- 构建日志: `/tmp/faiss_build.log`
