---
title: evernote-md-export-dup-bug
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**问题：** `export_favorite_md.py` 的重复检测条件为 `true_dup_titles and os.path.exists(md_path)`。首次批量导出时 .md 目录为空，条件不成立，所有重复笔记都被正常导出为 `title.md` + `title_1.md`。

**后果：** 21 组重复笔记（42 条）被导出为 21 对重复 .md 文件，而非移入 temp。

**修复方向：** 重复检测不应依赖 `os.path.exists()`。首条记录正常导出，后续同标题一律移入 temp。

**当前 workaround：** 导出后用 `move_dups_to_temp.py` 将 Favorites 残留重复移入 temp，手动删除 `_1.md` 文件。

**Key files:** `scripts/export_favorite_md.py`, `move_dups_to_temp.py`

**Why:** 脚本内重复检测在 main loop 之前执行，那时还没有任何 .md 文件生成，所以全部漏检。

**How to apply:** 修改 `export_favorite_md.py` 中 main loop 前的 duplicate check，加入运行时跟踪：记录已在本轮导出的标题，而非依赖文件系统存在性。
