---
title: obsidian-loading-stuck-71gb-attachments
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


Obsidian 启动一直卡在 loading 状态，排查后发现 vault 内 `印象笔记管理工具/attachments/` 目录有 **361,761 个文件，71GB**。

**根因链：** local_sync.py 之前在导出时将图片复制到 vault 内 attachments 目录 → 36 万个文件 → Obsidian 启动时遍历所有文件索引 → 加上 iCloud 同步同时处理这些文件变动 → 互锁永久 loading。

**修复：** 
1. 删除 vault 内 `attachments/` 目录（36 万文件 / 71GB）
2. 改为 `.evernote-content` 符号链接指向 Evernote 本地 content 目录
3. `--rewrite` 全量重导所有 .md，图片路径改为 `![](.evernote-content/{uuid}/{res}.ext)`
4. vault 大小从 71GB 降至 312MB

**⚠️ 未确认：** Obsidian 启动可能仍会遍历 `.evernote-content` 符号链接指向的 5 万个子目录。虽然点号开头文件在文件树中隐藏，但启动索引行为未验证。

**Why：** 之前的设计认为"本地复制图片到 vault 是标准做法"，没有意识到 36 万文件 + iCloud 同步是 Obsidian 无法承受的。修改后的策略改为"不留副本，仅引用"。

**How to apply：** local_sync.py 不再复制图片，只生成 `.evernote-content/` 相对路径。附件目录不存在 vault 内，Obsidian 启动不卡。换电脑场景需单独处理图片迁移。
