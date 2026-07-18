---
title: icloud-obsidian-conflict-copies-fix
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**问题：** Obsidian vault 放在 iCloud Obsidian 同步路径下 (`Library/Mobile Documents/iCloud~md~obsidian/Documents/`)，local_sync.py 写入 17K .md 文件时，Obsidian 也在实时索引这些文件，macOS 文件协调系统判定为并发冲突，产生大量 ` 2.md` 副本。7月6日清理了16K后，再次同步又生成回来。

**修复方案（已实施 v2）：** local_sync.py 主流程前后增加三阶段保护：

1. **写入前** → `quit_obsidian()`：AppleScript 优雅退出 Obsidian
2. **等待 30s**（每 0.5s 确认一次进程是否退出）— 超时 escalate：`pkill -x` → 等 5s → `pkill -9`
3. **写入后** → `cleanup_conflict_copies()`：仅当存在同名原始文件时才删除 ` 2.md` 副本（避免误杀"奏折 10.md"等合法标题）
4. **全部完成** → `open_obsidian()` 重新打开

**Why:** iCloud 冲突只在多进程并发写同一目录时产生。清理步骤匹配原始文件存在才删，避免误杀合法数字结尾笔记。

### `find_evernote_db()` 无 WAL 时返回 None 修复

**问题：** 初始 `w > sz`（sz=0），Evernote 干净关闭（无 -wal 文件）时 `0 > 0` 为 False → 返回 None。改 `>=` 后备份 DB 因 WAL 更大被选中而非主 DB，导致 `--cleanup` 使用空 active 集全员判孤儿。

**修复：** 初始 sz=`-1`，`0 > -1` 为 True，首个存在的 DB 即入选。`>` 确保多候选时选 WAL 最大的。

### `step_cleanup` 全员误判事故

**经过：** `find_evernote_db` 返回备份 DB（非主 DB），`step_cleanup` 的 active 集为空，19,986 个 .md 全员判 orphan 移入废纸篓。`find ~/.Trash -name "*.md" -exec mv {} ... \;` 全量救回。

### `move_duplicates_to_temp.py` 变量名踩坑

循环变量 `ns` 覆盖了外层 `ns = client.get_note_store()`，报 `'list' object has no attribute 'getNote'`。修复：改用 `items`。

### 最终对账 19957=19957

所有修复后，Favorites 19,957 = .md 19,957，完全对齐。

参考：[[local-sync-reconcile-complete-20260706]]
