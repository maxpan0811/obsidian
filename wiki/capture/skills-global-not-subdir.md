---
title: skills-global-not-subdir
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


Claude Code 官方建议是大型 monorepo 场景按子目录放 skill，但对于**多项目松散工作区**（`~/` 下十几个独立目录各自为政），走到哪个目录才加载哪些 skill 反而容易忘。这次试了 6 个 skill 分散到子目录后立即发现不现实，全移回了全局 `~/.claude/skills/`。

**Why：** 用户的工作习惯是从 `~` 启动 Claude Code，不固定某个项目目录。子目录 skill 只在对应目录激活，换目录启动就丢了，用户记不住每次从哪进。

**How to apply：** 除非是单一 monorepo + 每天只进那一个目录，否则 skill 全部放全局 `~/.claude/skills/`，平等对待。分层 CLUDE.md 已经够用，skill 不需要再分。
