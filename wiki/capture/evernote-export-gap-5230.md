---
title: evernote-export-gap-5230
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**发现**: 印象笔记 Favorites 笔记本实际有 **5230 条笔记**，但 `印象笔记管理工具/` 管线目录仅导出 2298 个 HTML 文件。processed.json 记录 2321 条，中间缺了约 3000 条。

**原因**: 印象笔记 Favorites 是全量收藏，但 export_favorite_html.py 是按 GUID 增量导出的——之前各批次导出之间有大量未覆盖的笔记。

**当前状态**: 剩余约 2607 条未导出。但印象笔记 API 限流严重（errorCode=19，rateLimitDuration 3-5分钟），约 60% 的请求会触发限流。

**修复**: 在 export_favorite_html.py 的 except 块中增加了专门的 rate limit 处理逻辑：自动解析 rateLimitDuration + 30s 缓冲等待，失败笔记排到队列末尾重试。同时将每篇间延迟从 0.5s 提到 3s。

**Note**: 导出进程在用户中断时仍在后台运行中（nohup）。

**Why**: 批量导出 2607 篇带图片的 Evernote 笔记是费时的后台操作，不在当前项目的核心路径上。
**How to apply**: 下次需要继续导出时，先检查 `/tmp/evernote_export.log` 看进度，`ps aux | grep export_favorite` 确认进程是否还在运行。
