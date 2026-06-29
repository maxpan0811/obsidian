---
title: macOS APFS 大小写不敏感文件系统陷阱
type: card
subtype: pitfall
created: 2026-06-29
updated: 2026-06-29
tags: [filesystem, macos, apfs, ingest, dedup]
source_path: ~/.claude/skills/LLM-Wiki管理工具/SKILL.md
---

## 问题

macOS APFS 默认大小写不敏感。`RAW/md` 和 `RAW/MD` **指向同一个物理目录**（同一 inode），但 ingested_files.json 可能以两种不同的路径引用同一文件，产生重复索引条目。

## 实例

同一文件 `LLM Wiki Schema for Technical Writer.md` 被同时以 `RAW/md/LLM Wiki Schema for Technical Writer.md` 和 `RAW/MD/LLM Wiki Schema for Technical Writer.md` 两个 key 分别入库，指向不同的 wiki 源页。

## 解决方案

1. 在 `cleanup_ingested_index.py` 中加入 lowercase dedup 逻辑
2. 新的 ingest 流程保持路径大小写一致
3. Rebuild 索引时自动去重
