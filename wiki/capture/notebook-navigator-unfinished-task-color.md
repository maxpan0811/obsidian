---
title: notebook-navigator-unfinished-task-color
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 现象

Obsidian 中部分 `.md` 文件在文件列表显示粉紫色，重启/重建索引不消失。

## 根因

Notebook Navigator 插件 v2.5+ 的 **"Unfinished task background"** 功能：文件内容包含 `- [ ]`（未勾选待办列表项）时，文件在列表面板自动显示特殊颜色。

## 修复

插件设置 → List → Notes → **Unfinished task background** → 关掉

或把 `- [ ]` 改为普通列表 `-`。

**Why:** 不是文件损坏或着色，是插件自动标记"含有待完成任务的文件"。2026-06-29 Hy 定位。
