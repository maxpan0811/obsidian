---
title: backup-before-modify
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


修改任何已有文件之前，**必须先备份**到 `~/.Trash/` 或加 `.bak` 后缀。

**Why：** 2026-07-18 桌面看板项目，我在没确认用户实际使用的文件名的情况下，直接把 `dashboard.html` 覆盖到了 `Dashboard 20260717.html`，导致用户之前的所有定制（标题下拉菜单、分公司标签、数据截止文案、时间按钮右置等）全部丢失，且无备份可恢复。

**How to apply：**
- 覆盖写入前：`shutil.copy(src, src + '.bak')` 或 `cp file file.bak`
- 批量操作前：先 `cp -r dir dir.bak`
- 永远不要假设"改错了可以恢复"——废纸篓不是可靠的备份机制（可能被自动清理）
- 如果用户有多个版本的文件（带日期后缀等），先确认要改的是哪个

**相关教训：** [[claude-code-deletion-protection]]
