---
title: evernote-old-pipeline-removed
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**操作：** 2026-06-29 删除老管线 3 个文件：`scripts/export_favorite_html.py`、`run_export.py`、`run_until_done.py`

**原因：** 用户要求删除老管线。老管线执行 `export_favorite_html.py`（HTML 输出），已被 `sync_favorites.py`（Markdown 输出，SQLite 事务 + 两阶段写入 + GUID 级验证）取代。

**同步执行了什么：**
1. 删除 3 个老管线文件 ✅
2. 更新 CLAUDE.md/SKILL.md 去除老管线引用 ✅
3. 运行 `sync_favorites.py --list --reconcile --export` 同步 Favorites 笔记 ✅
4. 重复标题检测：3 组 6 条笔记移入 temp + 3 个 .md 删除 ✅
5. 非图片附件笔记导出时自动处理：已看到 1 条 `转发: 旅游业务11月份经营情况` 移入 temp ✅
6. 创建新脚本 `scripts/scan_and_move_to_temp.py` 用于一次性全量扫描 ✅

**Why：** 老管线已无人维护，每次引用 `export_favorite_html.py` 会误导用户选择过时路径。同步删除 `run_export.py` 和 `run_until_done.py`（均硬编码引用该文件）。

**当前状态：** 导出至 255/474 触发限流（1485s ~25min），后台自动续传中。
