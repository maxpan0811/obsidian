---
title: evernote-local-sync-aligned-20260708
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


local_sync.py 重建 DB（--rewrite 全量导出后事故恢复），DB exported_file 统一对齐到 safe_title 最新版 `|`→`_` 规则，清理 90 篇碰撞副本 + 20 篇无对应残留。`reconcile.py` 的 List Checkpoint 断点续传 bug 再次触发（从 batch=175 续传仅抓 7,040 条，漏大批数据，导致 10,910 条正常导出笔记被误标 orphan_removed）。解决方法：恢复 orphan_removed → exported，然后用 `--scan` 配合本地 Evernote DB 重建完整映射。

最终三方对齐：磁盘 24,549 .md = Favorites 24,549 条 = DB exported 24,628（差 79 处 attachment/orphan 是正常）。OB 行为：不可用点号开头以外的 symlink（会导致渲染白屏），OUTPUT_DIR 已改到本地 `/Users/panbo/Obsidian/` 而非 iCloud 路径。

**Why:** 本地+API 两管线共用同一个 `state.db`，DB schema 不一致（local_sync 写 local_uuid/local_updated，sync_favorites 只有 updated 列），导致导入时频繁因列名报错。

### reconcile.py 删除

### 重要提醒：本地 SQLite 没有 ≠ 云端已删

本地 SQLite 只是同步缓存。笔记在云端 Favorites 但未下载到本地时，SQLite 查不到但实际在云端存在。应等 Mac 客户端同步后再用 `local_sync.py` 导出，或手动删除再恢复触发同步。

### reconcile.py 删除（2026-07-08）

`reconcile.py` 已于 2026-07-08 删除（移入 ~/.Trash）。致命原因：
- List Checkpoint 断点续传 bug（`resume_from = done * 100`），两次同模式事故各误标 ~10,900 条
- `sync_favorites.py` 和 `fast_export.py` 的导入入口改为打印提示
- 功能完全被 `local_sync.py` 覆盖

### 附件+重复笔记自动移入 temp

`local_sync.py` 的 `run()` 末尾集成 `move_attachments_to_temp()` 和 `move_duplicates_to_temp()`。同步完成后自动检测 DB 中 `status='attachment'` 和同标题 ≥ 2 篇的笔记，通过 Thrift API `getNote()` + `updateNote(notebookGuid=temp)` 移入 temp。雲端已删笔记标记 orphan。无需再手动运行 `move_attachments_to_temp.py` / `move_duplicates_to_temp.py`。

**Why:** 用户要求"把这个功能加入 local_sync 里，不要我每次提醒"。
**How to apply:** 只用 `local_sync.py` 做增量/全量同步，不再碰 `reconcile.py` / `sync_favorites.py`。增量运行直接 `python3 local_sync.py`。

**关于不能改本地 DB 的原因：** 印象笔记本地 SQLite 只是云端缓存的只读副本。同步引擎以云端时间戳为准，直接改本地 `ZNOTEBOOK` 字段会被下次同步覆盖。`updateNote(notebookGuid=temp)` 必须通过 Thrift API 写入云端。

### .env 加载 bug（2026-07-08）

`local_sync.py` 原来未加载 `.env`，自动清理调 Thrift API 时拿不到 token。新增文件头部 `.env` 读取。

### 最终完全对齐（2026-07-08）

```
Favorites 29,660 - Disk 29,660 = 0 ✅ 完全一致
```

### 关键教训：.notes 导出文件加密 vs 本地缓存明文

`.notes` 导出文件正文是 AES 加密（`base64:aes`），图片是明文的可提取。本地缓存 `~/Library/Application Support/com.yinxiang.Mac/.../content/{uuid}/content.enml` 是明文 XML，`local_sync.py` 可直接读取。

### 第四次同步：新增 5,630 篇后完全对齐（2026-07-09）

```
Favorites 34,909 - Disk 34,909 = 0 ✅
```

单次 sync 处理 5,630 篇新增笔记，50 秒完成。自动清理：284 附件 + 260 重复标题 + 172 孤儿文件。多轮 sync 补齐未同步的 content.enml 后自然对齐。

**关键教训：** 新增大量笔记时，部分 content.enml 可能尚未同步到本地（本地 SQLite 有记录，但 content 目录无文件）。持续运行 `local_sync.py` 即可逐步补全。
**How to apply:** 日常增量同步 `python3 local_sync.py` 即可。同步完成后自动清理附件和重复笔记。

"不是留学生的问题"这篇笔记第一次检查时说"云端已删"是误判——实际是 Mac 客户端尚未同步到本地。删除再恢复触发了同步，本地有了 content.enml 后 `local_sync` 正常导出。

### 杂项清理（2026-07-09）

清理 `/Users/panbo/` 下 Claude Code 产生的无用残留：
- `.claude.json.tmp.*`（8 个）— 崩溃恢复残留的状态文件
- `"` 目录（引号字符名）— 路径引号配对错误的产物
- `~` 目录（波浪号字符名）— shell `~` 展开失败的产物

**Why:** 了解 Claude Code 会在哪些路径产生意外目录有助于定期清理。
**How to apply:** 清理规则——home 目录下出现引号/特殊字符命名的空目录可安全删除。`.claude.json.tmp.*` 是旧 session 崩溃残留，当前 `.claude.json` 正常即可删除。

**Why:** 认为"本地 SQLite 没有 = 云端已删"是错误推断——本地只是缓存，可能只是未同步。

### 碰撞副本清理规则（2026-07-08）

文件名末尾带 `_[a-f0-9]{8}`（8 位十六进制随机码）的 `.md` 是 safe_title 碰撞产生的副本。规则：
- ✅ 原文件存在时 → 碰撞副本可安全删除
- ⚠️ 原文件不存在时 → 碰撞副本是唯一版本，需保留

用户 2026-07-08 手动确认 50 篇可删 + 10 篇因原文件缺失需保留。记忆文件 `evernote-collision-copy-cleanup-rule.md`。
