---
title: 20260710-chromadb-concurrent-write-fix
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# ChromaDB 并发写入崩坏 + PID 锁修复

## 背景
2026-07-10 进行第二批 1,000 篇印象笔记向量索引时，后台残留的内嵌 Python 脚本（session 98190，处理 2,909 篇特殊字符文件）仍在并行写入同一个 ChromaDB collection，导致 HNSW segment 状态不一致，ChromaDB 完全 segfault。

## 根因
这是同一时间两个进程并发写入同一 ChromaDB PersistentClient 目录导致的。ChromaDB 的 HNSW 索引非线程安全，并发操作会损坏内部状态。

## 修复方案
加 **PID 文件锁**，保证同一时刻只有一个进程能写入 ChromaDB：

```python
import fcntl

LOCKFILE = "/tmp/chromadb_index.lock"
with open(LOCKFILE, "w") as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)  # 阻塞等待，自动释放
    # 只有此处能执行向量索引
```

## 后果
- ChromaDB 全部归零（0 chunks），之前 1,849 个 chunk 全部丢失
- 但 wiki/sources/ 源页和 ingested_files.json 索引完整无损
- 需重新全量建立 ChromaDB 索引

## 教训
- 在 wiki_vector_ingest.py 或调用脚本中加入文件锁，不依赖人工保证串行
- 任何 ChromaDB 写入操作前先获取锁
- 查询（只读）不需要锁
