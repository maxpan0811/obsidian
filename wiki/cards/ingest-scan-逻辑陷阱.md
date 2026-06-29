---
title: Ingest 扫描逻辑：-newer 陷阱与全量比对
type: card
subtype: pitfall
created: 2026-06-29
updated: 2026-06-29
tags: [ingest, scanning, filesystem, pitfall, macos]
source_path: ~/.claude/skills/LLM-Wiki管理工具/SKILL.md
---

## 问题

`ingest` 扫描新文件时，用 `find -newer ingested_files.json` 来替代全量目录比对。这只能找到**修改时间比索引新**的文件，而**一直存在却从未入过库**的文件被完全遗漏。

## 直接后果

2026-06-29 的 ingest 会话中，漏掉了 **1,332 个文件**：
- 印象笔记管理工具 1,264 个 .md
- RAW/PDF/Word/PPT/Excel 68 个

这些文件已存在了数天到数月，只是从未经过 ingest 流程。

## 解决方案

**永远用全量目录遍历 → 逐一查 ingested_files.json**，禁止使用 `-newer`、mtime 或其他时间戳过滤：

```bash
# 错误做法 ❌
find RAW/PDF/ -newer wiki/ingested_files.json

# 正确做法 ✅
for f in RAW/PDF/*.pdf; do
  key="RAW/PDF/$(basename "$f")"
  python3 -c "import json; idx=json.load(open('wiki/ingested_files.json')); print('NEW' if '$key' not in idx else 'OK')"
done
```

## 相关 Pitfalls

- [[cards/filesystem-case-insensitive-陷阱]]
- [[cards/stale-cleanup-bare-directory-陷阱]]
