---
title: delete-move-to-trash
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


所有文件删除操作一律使用 `shutil.move(fp, os.path.expanduser("~/.Trash"))`，**绝对不要用 `os.remove()`**。

**❌ 反例：** `os.remove(fp)` — 这一行让 10,743 个 .md 文件不可恢复，只能用重新导出来恢复

**✅ 正例：**
```python
import shutil, os
trash = os.path.expanduser("~/.Trash")
shutil.move(fp, os.path.join(trash, os.path.basename(fp)))
```

**Why：** 用户可能反悔。移入 Trash 给了从容恢复的窗口。永久删除意味着任何 bug（sync_favorites.py checkpoint 缺陷导致 10,820 篇误判为 orphan）都会导致不可逆损失。

**How to apply:** 凡是有文件删除操作的地方（`os.remove`, `os.unlink`），改为 `shutil.move` 到 `~/.Trash`。注意 Trash 已存在同名文件时会被静默覆盖，需要加唯一后缀或先改名。
