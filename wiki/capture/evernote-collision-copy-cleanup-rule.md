---
title: evernote-collision-copy-cleanup-rule
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


文件名末尾带 `_[a-f0-9]{8}`（8 位十六进制随机码）的 `.md` 文件是 `local_sync.py` 的 safe_title 碰撞处理产生的副本。当两篇不同笔记的 safe_title 相同时，第二篇会加 GUID 前 8 位后缀去重。

**规则：**
- ✅ 同名原文件（不带随机码的 `.md`）存在时 → 碰撞副本可安全删除
- ⚠️ 同名原文件不存在时 → 碰撞副本是唯一版本，需保留

`local_sync.py` 的 `cleanup_conflict_copies()` 只处理 iCloud 冲突副本（` 2.md`），不处理 GUID 后缀碰撞副本。后者是服务的正常行为，保持原样更安全。手动清理时遵循上述规则判断。

**Why:** 碰撞副本由 safe_title 去重产生，不是 iCloud 冲突，不应由 cleanup 自动处理。手动清理时需检查原文件存活状态避免误删。用户 2026-07-08 手动确认 50 篇可删 + 10 篇因原文件缺失需保留。
