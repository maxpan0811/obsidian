---
title: 20260716-faiss-400-handling
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# FAISS 增量构建 Ollama 400 错误与修复（2026-07-16）

## 背景
FAISS v3 增量构建（`--incremental`）在 2026-07-16 晚重新跑剩余 ~19,000 新文件时遇到两个问题：

### 1. Print 被 nohup 缓冲吞掉
nohup 重定向到 `/tmp/faiss_build.log` 后 Python stdout 缓冲，日志文件始终 0 字节。
**修复**：脚本顶部加 `print = functools.partial(print, flush=True)`，所有 print 实时输出。

### 2. Ollama 400 错误崩溃
Ollama 对某些文本返回 HTTP 400（非连接断开），脚本直接退出。
**修复**：`_ollama_embed()` 增加逐条编码 fallback——遇到 batch 400 时拆成单条，问题文本降级为 1024 维零向量跳过，不中断构建。

### 3. Vault 实际文件数修正
之前记录的总文件数为 52,209 已过时。当前 Obsidian vault 实际有 **100,004 个 .md 文件**。
已缓存 81,068 文件（436,622 chunks），待嵌入 ~19,000 文件。

## 当前状态（2026-07-16 18:30）
- `--status`: 81,068 files cached, 436,622 chunks
- 索引落后（374,342 chunks vs 436,622 cache）→ 嵌入完成后自动重建
- 备份文件占 ~4GB（3 份旧 faiss + 3 份旧 metadata + chroma.sqlite3）→ 待清理
- 两次中断（Ollama 升级 + 400 错误），进度在 61.7% 停住

## 关键经验
- nohup + Python print → `flush=True` 或 `functools.partial(print, flush=True)`
- Ollama 400 不是不可恢复的错误——降级为逐条编码 + 零向量跳过即可
- 嵌入完成前不要手动清理 embedding_cache.pkl（否则得重新嵌入）

**Why:** 处理和记录边界情况修复，避免下次遇到同样问题再花时间排查。
