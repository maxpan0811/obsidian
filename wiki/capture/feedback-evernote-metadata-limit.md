---
title: feedback-evernote-metadata-limit
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


印象笔记 `findNotesMetadata(token, filter, offset, maxNotes, spec)` 有两个相关陷阱：

### 陷阱 1：默认 maxNotes=50

`findNotesMetadata()` 的 maxNotes 参数默认是 50，笔记本笔记数超过 50 时，超出部分静默不返回，导致脚本以为 "所有笔记已处理" 而跳过。

### 陷阱 2：设固定值 ≥200 仍然不够

Favorites 笔记本目前有 239 条笔记且持续增长。如果硬编码 `maxNotes=200`，超出部分同样静默丢失。**必须用分页循环**：

```python
total = ns.findNotesMetadata(token, filter, 0, 1, spec).totalNotes
all_notes = []
for offset in range(0, total, 100):
    batch = ns.findNotesMetadata(token, filter, offset, min(100, total-offset), spec)
    all_notes.extend(batch.notes)
```

注意：`findNotesMetadata` 的第 **1 个参数是 token**（不是 filter），`offset` 在第 2 位。

**Why：** 2026-06-06 发现 Obsidian 文件数（221）与印象笔记 Favorites 笔记数（239）不一致，查了 3 轮才发现是 `findNotesMetadata` 硬编码 200 的限制。这个问题不会报错，只会静默丢失数据。

**How to apply：** 任何调用 `findNotesMetadata` 的脚本，都用分页循环（offset 步长 100），不要假设 "200 够用"。已被修复在 `export_favorite_html.py`。
