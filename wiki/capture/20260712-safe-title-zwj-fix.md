---
title: 20260712-safe-title-zwj-fix
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


safe_title() 中增加 s.replace('\u200b', '') 剥离零宽空格（U+200B）。

一致性清理流程：
1. 还原被误移的 32 篇笔记从 temp 到 Favorites
2. 禁用重复标题自动清理（move_duplicates_to_temp）
3. 删除 44 个含零宽字符的残留 .md 文件 + 1 个碰撞副本
4. 删除 286 个孤儿 .md 文件（笔记已不在 Favorites）
5. safe_title 增加零宽字符剥离
