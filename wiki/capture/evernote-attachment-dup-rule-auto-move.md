---
title: evernote-attachment-dup-rule-auto-move
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**规则：** 每次 `local_sync.py` 运行完后，检查输出中的 `attachments`（附件跳过）和 `Collisions`（重复标题碰撞）计数。如果有，必须立即运行对应的移入 temp 脚本，不能只标记 DB 就结束。

**Why:** `local_sync.py` 是零 API 工具，只能读本地 SQLite，不能在 Evernote 端移动笔记。只改 DB 状态而不移入 temp 的话，下次 sync 时 local SQLite 仍会检测到那些笔记并重新标记，形成循环。

**执行方式：**
```bash
# 附件笔记
cd ~/.claude/skills/印象笔记管理工具 && source .env && python3 scripts/move_attachments_to_temp.py

# 重复标题（全部移入 temp，一篇不留）
cd ~/.claude/skills/印象笔记管理工具 && source .env && python3 scripts/move_duplicates_to_temp.py
```

**❌ 错误示范：** 看到 `attachments: 53` 却说"local_sync 只读不能写所以搁着" — 应该调 Thrift API 脚本移入 temp。
**✅ 正确做法：** 同步完成后立即检查输出中的附件/重复标题计数，有就移入 temp。

参考：[[icloud-obsidian-conflict-copies-fix]]
