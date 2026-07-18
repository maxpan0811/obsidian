---
title: feedback_evernote_export_attachment_skip
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


印象笔记 Favorites 导出时，含文档附件（PDF、Word、Excel等）的笔记不导出到 Obsidian，只列名称给用户手动处理。图片附件（image/*）正常导出。

**重要：用白名单而非 `not image/` 过滤**
- ❌ 不要用 `not r.mime.startswith('image/')` —— 网页剪藏常有 `application/octet-stream` 二进制碎片，不是真实文档，会误杀
- ✅ 用已知文档 MIME 前缀白名单：`application/pdf`、`application/msword`、`application/vnd.openxmlformats-officedocument.*` 等
- `application/octet-stream` 视为图片正常导出（它是网页二进制碎片，不是用户附件）

**Why:** 用户明确说「图片不算附件，pdf/word文件这些才算附件」。非图片附件无法在 HTML 中渲染，同时保留供手动处理。但 `application/octet-stream` 是 Web Clipper 产生的二进制碎片，不是用户附件的文档，不应跳过。

**How to apply:** 在 `export_favorite_html.py` 中，用文档 MIME 前缀白名单检查 resources，匹配则跳过并记录到 `processed.json` 的 `skipped_attachment` 类型。用户删除附件后，改类型为 `pending_restore` 可重导出。
