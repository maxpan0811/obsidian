---
title: chromadb-hnsw-corruption-fix
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 问题

`~/.claude/data/vector_index/` 下的 ChromaDB HNSW 索引文件 `link_lists.bin` 膨胀到 **954G**，而实际向量数据 `data_level0.bin` 仅 25M。

## 根因

`ingest.py` 和 `build_index.py` 两个脚本独立写入同一 ChromaDB 实例，**没有互斥锁**。并发写入导致 HNSW 图的邻接链表（`link_lists.bin`）损坏。损坏后每次 `coll.add()` 遍历不到链表终点，持续追加新边，形成**写入自放大**循环。

发生时间：6月19日那天 ingest 运行时已飙到 954G，不是退出后自动触发。

## 修复

### 短期（已施行）

两个脚本的 ChromaDB 操作段都加了 `fcntl.flock(LOCK_EX)`：

```python
LOCKFILE = INDEX / ".index.lock"
lock_fd = open(LOCKFILE, 'w')
fcntl.flock(lock_fd.fileno(), fcntl.LOCK_EX)
try:
    # ChromaDB operations here
finally:
    fcntl.flock(lock_fd.fileno(), fcntl.LOCK_UN)
    lock_fd.close()
```

## 关联文件

- `~/.claude/scripts/build_index.py` — 已删除，合并入 ingest.py
- `~/.claude/scripts/ingest.py` — codex 写的（有 subprocess 防 segfault PDF 提取），加锁
- `~/.claude/data/vector_index/` — ChromaDB PersistentClient 数据目录
- `~/.claude/data/README.md` — codex 写的 ingest 管线文档

## 教训

两个脚本做同一件事的不同实现是设计缺陷。理想方案是合并为一个写入入口，但眼下加锁已足够防止复发。
