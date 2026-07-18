---
title: claude-code-hooks-sound
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


用 macOS 内置系统音效，搭配 settings.json hooks 实现事件音效：
- `Stop` hook → 任务完成 → `Hero.aiff`（英雄号角）
- `Notification` hook → 等待输入 → `Glass.aiff`（玻璃碎声）

路径直接用 `/System/Library/Sounds/`，无需额外生成音效文件。

所有内置音效：Basso / Blow / Bottle / Frog / Funk / Glass / Hero / Morse / Ping / Pop / Purr / Sosumi / Submarine / Tink
