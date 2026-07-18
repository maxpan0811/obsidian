---
title: local-sync-symlink-image-pattern
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**变更：** local_sync.py 的图片策略从"复制到 attachments/"改为"通过 .evernote-content 符号链接引用"。

**具体改动：**
1. 删除了 `ATTACH_DIR` 常量，新增 `SYMLINK_NAME = '.evernote-content'`
2. 新增 `ensure_symlink()` 方法：创建 `.evernote-content` → Evernote 本地 content 目录的符号链接
3. `copy_res()` 替换为 `res_ref()`：不复制文件，只返回相对路径 `{SYMLINK_NAME}/{lu}/{rl}{ext}`
4. `build_md()` 不变，图片路径通过 repl 回调自动写入
5. 目录清理：`_pending`, `attachments` 残留已删除

**性能：** 17,285 篇笔记，3.2 分钟，0 失败。比之前的 5 分钟略快（减少了图片复制开销）。

**状态：** vault 从 71GB / 36 万文件 → 312MB / 17,220 个 .md 文件。

**⚠️ 未完成：**
- Obsidian 仍可能因为 symlink 指向的 5 万子目录导致启动慢（待验证）
- 65 篇含非图片附件的笔记未移入 temp（updateNote 缺 title 字段，需完整 Note 对象）
- ZSOURCEURL 链接已加（94% 的笔记有链接）

参考：[[obsidian-loading-stuck-71gb-attachments]]
