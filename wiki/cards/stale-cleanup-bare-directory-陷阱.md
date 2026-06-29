---
title: Stale 清理漏掉 bare-directory 条目
type: card
subtype: pitfall
created: 2026-06-29
updated: 2026-06-29
tags: [ingested_files, stale, cleanup, pitfall]
source_path: ~/.claude/skills/LLM-Wiki管理工具/SKILL.md
---

## 问题

`ingested_files.json` 中可能存在 bare-directory 条目（key 以 `/` 结尾，没有实际文件名），如 `RAW/Excel/`。

旧版 `cleanup_ingested_index.py` 用 `os.path.exists(path)` 检查文件是否存在——但目录本身存在时 `os.path.exists()` 返回 `True`，导致这类条目未被清理。

## 实例

`RAW/Excel/` → 考核报表与环线游数据分析-2026年.md

该条目的 source_path 不是一个文件，而是指向目录本身。修正后 123 个文件 ↔ 123 个条目完全匹配。

## 解决方案

检查路径时，增加 `path.endswith('/')` 判断：

```python
if path.endswith('/'):
    continue  # bare directory, skip
```
