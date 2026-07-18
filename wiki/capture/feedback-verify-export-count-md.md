---
title: feedback-verify-export-count-md
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


导出（Favorites→Obsidian HTML、或类似操作）完成后，必须核对两边的数量：

1. 源端（印象笔Favorites）有多少条
2. 目标端（Obsidian HTML文件）有多少条
3. 如果是增量导出，找出未处理的 diff

**Why：** 用户发数量不一致（本次221条 vs  226条），直接报"完成"是不行的

**How to apply：** 任务输出后，先打印两端数量比对，不一致就逐条排查原因（去重、命名冲突、之前的脚本bug、Token问题等），把问题解决了再汇报

**验证脚本：** `/tmp/verify_favorites.py` — 自动化比对 Evernote Favorites 与 Obsidian 的逐条一致性。每次导出完成后运行，确认 `Missing from Obsidian: 0` 和 `Extra in Obsidian: 0`。
