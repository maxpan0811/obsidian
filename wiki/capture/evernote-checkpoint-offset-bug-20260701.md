---
title: evernote-checkpoint-offset-bug-20260701
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-07-01 严重 bug：`sync_favorites.py` 的 `list` 步骤从 checkpoint（batch=141, offset=14100）恢复，只拉了 Favorites 最后 3,321 篇笔记。后续 `reconcile` 发现 DB 中 10,820 篇笔记不在 batch_notes 中 → 误判为 orphan → 全部 `os.remove` 永久删除。

**根因：** `reconcile.py:list_notes()` 的 `get_checkpoint('list')` 返回上次的 batch 值，`resume_from = done * 100` 从偏移量恢复。当 `pageSize=100`，batch=141 时从 offset 14100 开始拉，17,421 篇中只拉了最后 3,321 篇。

**Why：** 断点续传机制本身没问题，但 recovery 路径缺少"从 0 开始全量拉取"的选项。checkpoint 应该有个 `--reset` 或用 `--force` 跳过断点。

**How to apply:** 修改代码时需要注意：
1. `get_checkpoint('list')` 返回的 batch 值可能非常大（每次运行增加），下次运行如无 `--force` 标志应默认从 0 全量拉取，或提供 `--reset-list` 选项。
2. Orphan 检测必须满足 batch_notes 是**全量实时数据**的条件。如果 list 步骤只拉了部分笔记，后续的所有检测（orphan、重复标题、更新时间戳对比）全部无效。
3. 交叉验证：每次 reconcile 前增加"batch_notes 条数 = 85%+ Evernote 实际数"的断言（17,421 × 85% ≈ 14,800），低于阈值直接报警不执行孤儿删除。

**验证方法：** 调用 `findNotesMetadata` 不带 offset，返回的 `totalNotes` 与 `len(batch_notes)` 比较，差异超过 15% 则预警。
