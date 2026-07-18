---
title: evernote-md-export-pipeline
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**变更：** 创建 `scripts/export_favorite_md.py`，作为 Favorites→Obsidian 导出的首选方式（2026-06-22）。

**与旧 HTML 导出的差异：**
- 输出 .md 文件（YAML frontmatter + Markdown 正文）而非 HTML
- 非图片附件 → 移入 temp 笔记本（`moved_attachment`），而非跳过记录
- `markdownify` 库做 ENML→Markdown 转换
- `.env` 直接内嵌读取，无需 `source .env`

**产量：** 1030 个 .md 文件，179 条移入 temp，0 残留未处理

**遗留：** 旧 `export_favorite_html.py` 导出的 8566 个 .html 文件仍在同一目录，未清理。

**2026-06-23 重构：** `sync_favorites.py` 管线（SQLite + 两阶段写入 + GUID 级 verify）替代 `export_favorite_md.py`。详见 SKILL.md 和程序开发/印象笔记同步管线.md。

**2026-06-25 关键发现：** ENML 截断检测的 `content.endswith('</en-note>')` 对末尾带 `\n` 的笔记产生假阳性。
**2026-06-27 已修复：** 改为 `content.strip().endswith('</en-note>')`。641 条 failed 重置为 pending，首次重导后 617 条仍未处理（用户暂停工作）。

**最终对账：** .md 文件 10168 个，DB 已导出 9069 条，5 条移入 temp，714 条孤儿。

**How to apply:**
- 新导出用 `python3 sync_favorites.py`（全量）或 `--resume`（断点续传）
- ENML 截断假阳性修复：`export_note.py` 中 `content.endswith` → `content.strip().endswith`
- 后台进程若卡死（Thrift 网络挂起），kill 后 `--resume` 重启

**How to apply:** 新导出直接用 `python3 scripts/export_favorite_md.py`。导出后运行 `move_dups_to_temp.py` 处理残留重复，检查 `_1.md` 文件清理。
