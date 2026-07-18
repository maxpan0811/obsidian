---
title: 20260714-ollama-faiss-v3
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# FAISS v3: Ollama Embedding 引擎切换 (2026-07-14)

## 背景
FAISS v2 使用 sentence_transformers + bge-m3 + PyTorch CPU 编码，遇到三个致命问题：
1. macOS 多线程 SIGSEGV（Python 3.14 + torch + OpenMP 冲突）
2. 单线程太慢（0.08 files/s，23k 文件需 82 小时）
3. 多进程内存爆炸（每个进程复制完整缓存，4 进程 39GB）

## 关键决策

| 决策 | Why |
|------|-----|
| 换 Ollama 替代 sentence_transformers | Ollama 用 Metal GPU 推理，不依赖 PyTorch，稳定不崩，25× 加速 |
| 保留 FAISS 存储层 | ChromaDB 崩过 3 次，FAISS v2 版本备份 + checkpoint 已成熟 |
| 不换 ChromaDB | compaction 崩溃是 ChromaDB 自身 bug，不可修复 |
| 超长段落处理 | 659KB base64 SVG 数据被当作段落 → 加 MAX_PARA_CHARS=4000 硬上限 + 数据跳过 |

## 性能

| 指标 | 旧 (sentence_transformers) | 新 (Ollama) |
|------|--------------------------|-------------|
| 速度 | 0.08 files/s | 2.0 files/s |
| 加速比 | 1× | 25× |
| 23k 全量 | ~82 小时 | ~2 小时 |
| 内存 | 崩溃/泄漏 | 700MB 稳定 |
| 稳定性 | Python 3.14 SIGSEGV | ✅ 无崩溃 |

## Ollama vs ST 精度对比
- 同一查询 Top-5 重叠：5/5 (100%)
- 得分差异：≤ 0.0006（可忽略）
- 旧缓存完全可用，无需 `--full` 重建

## 关键教训
- 启动长时间任务后必须主动监控 RSS、Swap、日志新鲜度、速率偏差
- 超长段落（无标点）需跳过，否则 Ollama 返回 400
- 多进程方案是死路——每个进程加载完整缓存 = 内存爆炸
- checkpoint 在 `completed: True` 时会被跳过，`--limit` 测试后需清理 checkpoint

## 相关文件
- 脚本：`scripts/wiki_faiss_build.py` (v3, Ollama), `scripts/wiki_vector_query.py`
- 维护笔记：`程序开发/LLM-Wiki管理工具-ingest索引维护笔记.md`
- 会话：`f52edae5-dba6-4311-ae70-49d13bf7f58a` (2026-07-14)

## 如何应用
- 构建：`python3 wiki_faiss_build.py --incremental`
- 查询：`python3 wiki_vector_query.py "<query>"`
- 中断后重跑同命令，自动续传（每 100 文件 checkpoint）
- 需要 Ollama 服务运行：`ollama serve`
