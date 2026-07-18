---
title: feedback_evernote_export_auto
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


"导出Favorites"（步骤1）和"导出后验证"（步骤2）必须自动连续执行，不询问用户。

**Why:** 用户明确说"以后1、2全部执行，不要问我"，说明这是一个固定的管线操作，不需要每次确认。

**How to apply:** 每次被触发执行印象笔记导出时，先导出（python3 scripts/export_favorite_html.py），导出完成后立即跑两个验证脚本（Evernote vs HTML 数量比对 + 重复标题检测），一次性输出所有结果。
