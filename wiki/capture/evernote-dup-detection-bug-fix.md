---
title: evernote-dup-detection-bug-fix
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**问题：** `reconcile.py` 的重复检测 `true_dup_titles` 来自 `scripts/note_cache.json`（2026-06-22 导出的 9636 条缓存）。当 Favorites 增长到 14,000+ 条后，缓存过期，重复检测全部失效。

**根因：** 设计时假设 `note_cache.json` 会定期更新，但实际从未更新过。2026-06-22 后新增 +1,500 条笔记中的重复未被检出。同时 batch_notes（在内存中实时拉取）包含了全量 14,000+ 条，却未被用于重复检测。

**第二个漏洞：** 移入 temp 的条件用了 `exported_file`（已导出的 .md 文件名）分组，而非 `title` 分组。未导出的重复笔记永远不会被检测到。

**第三个漏洞：** `export_note.py` 的 export_one 没有做标题级重复检测。如果一篇新笔记和已导出的笔记标题相同（新副本），会被直接导出为同名 .md（覆盖原文件）而不产生报警。

**修复 (reconcile.py):**
1. 删除 `note_cache.json` 依赖，改为从 `batch_notes` 实时数据检测
2. 新增 `make_safe_title` 归一化文件名级去重（标题相似但标点不同的情况）
3. 使用 `title` 分组（非 exported_file）确定要移入 temp 的副本

**Why:** 离线缓存在增量的数据管道中是已知陷阱。任何依赖"全量数据"的策略必须从实时源获取，不能假设缓存会及时更新。

**How to apply:**
- 任何检测类逻辑（重复、缺失、异常）必须从**最新的实时数据源**获取，而非离线缓存
- 数据管线的"list"步骤拉取的是全量快照 → 后续步骤应使用这个快照，不再依赖外部缓存文件
- 当数据量增长超过缓存量时，缓存失效是静默的——不报错，只产生错误结果
