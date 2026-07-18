---
title: feedback_selfmade_skill_chinese_name
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


自己写（创建）的 skill 一律取中文名称，比如 `每日选股分析` 而不是 `stock-analyzer`。

**Why:** 在 `.claude/skills/` 下一眼就能看出哪些是自己写的、哪些是第三方安装的，方便管理和审计。

**How to apply:** 用 `skill-creator` 创建 skill 时，在 frontmatter 的 `name:` 字段和目录名都用中文。安装第三方的 skill 不要求改名。
