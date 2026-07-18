---
title: evernote-dup-title-all-to-temp
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 重复标题笔记处理策略变更

**变更日期**: 2026-06-24
**触发**: 用户在导管线重构讨论中发现 reconcile 阶段对重复标题的处理不安全

**旧逻辑**: 第 1 篇正常导出 .md，第 2+ 篇移入 temp
**问题**: 用户无法判断 temp 中笔记对应哪篇、内容是否完整，也无法确定第一篇是否应该保留

**新逻辑**: 所有同标题笔记全部移入 temp，已导出的 .md 文件一并删除。用户去 temp 手工筛选，再把要留的那篇移回 Favorites。下次 `--reconcile` 检测为 `new` 重新导出。

**Why**: 让用户做的是"选哪个保留"的确认操作，而不是"从 temp 捡回可能缺失的笔记"的排查操作。前者比后者安全 10 倍。

**How to apply**: 涉及 `reconcile.py` 的 repeat title 处理逻辑和完成后清理 .md 文件。

**Related**: [[evernote-md-export-dup-bug]]
