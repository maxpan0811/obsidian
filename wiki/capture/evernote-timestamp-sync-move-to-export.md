---
title: evernote-timestamp-sync-move-to-export
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


印象笔记 sync_pipeline 中，`batch_update_timestamps`（同步 batch_notes.updated → notes.updated）必须放在 **export 步骤之后**，绝不能放在 reconcile 步骤中。

**Why：** 2026-06-30 发生了一次规则变更事故——AI 误删了 reconcile 中的 `updated` 时间戳检测逻辑。此时 `batch_update_timestamps` 在 reconcile 末尾依然运行，把所有 14,064 条笔记的时间戳都同步了，导致差异永久抹除，后续即使恢复检测逻辑也无法找回遗漏的更新。损失：所有在事故期间更新过的印象笔记文章都没能同步到 Obsidian。

**How to apply：**
- 时间戳同步（`batch_update_timestamps`）放在 `sync_favorites.py` 的 `step_export()` 末尾
- reconcile 步骤（`reconcile.py:reconcile()`）末尾**不要调用** `batch_update_timestamps`
- 理由：reconcile 是**检测**阶段，export 是**执行**阶段。检测阶段的逻辑可能因规则变更而出错，如果同时在检测阶段把差异抹掉，错误就不可逆了。执行阶段同步才是安全的——只有确认导出成功后，才认为"这个版本已经同步过了"

**相关文件：**
- `sync_favorites.py` — `step_export()` 末尾调用 `batch_update_timestamps`
- `reconcile.py` — 已删除对 `batch_update_timestamps` 的调用，只做检测不做同步
- 这条规则在 2026-06-30 SKILL.md 更新中记录
