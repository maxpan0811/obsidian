---
title: local-sync-inline-images-rewrite
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**做了什么：**
1. `local_sync.py`: 将 `<en-media>` 在 ENML 阶段直接替换为 `<img src="attachments/...">`，再经 markdownify 转为 `![](附件)`，图片按原文位置穿插
2. `local_sync.py`: 新增 `--rewrite` 参数，跳过"已存在"检测，强制删除旧 .md 后全量重导出
3. `safe_title()`: 增加 `lstrip('_')`，去掉笔记标题开头的下划线

**性能：** 17,186 篇（含 15,808 篇图片笔记），3.1 分钟完成，0 失败。

**注意：** `sync_favorites.py` 的 SQLite DB 不跟踪 `local_sync.py` 的导出状态。重跑后 verify 会报大量"缺失/hash 不匹配"——那是在比对旧 DB 记录，不是真正的问题。
