---
title: safe-title-underscore-ordering-fix
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**问题：** Obsidian vault 中 97 个文件以 `_` 开头（如 `_ 特朗普注定解决不了美国重新工业化问题.md`），即使 `safe_title` 有 `lstrip('_')` 也没去掉。

**根因：** `safe_title` 的执行顺序是 `lstrip('_')` → 正则替换 `|`→`_`。部分 Evernote 标题以 `|` 开头（如 `| 特朗普...`），`lstrip('_')` 对 `|` 无效，随后正则把 `|` 替换为 `_`，但这时 `lstrip` 已经跑过了，文件以 `_` 开头被写出。

**修复：** 改为先正则替换特殊字符为 `_`，再 `lstrip('_')`：
```python
# 错误顺序：
s = title.strip().strip('. ').lstrip('_')
s = re.sub(r'[<>:"/\\|?*]', '_', s)

# 正确顺序：
s = title.strip().strip('. ')
s = re.sub(r'[<>:"/\\|?*]', '_', s)
s = s.lstrip('_')
```

**执行：** 清空 93 个下划线文件 → `--rewrite` 全量重导 → 0 个下划线文件残留 ✅

**经验：** `lstrip` 在正则之前执行会漏掉被正则转化为目标字符的字符。先转换、再剥离。

**重要：** 增量同步逻辑已确认正确——`should_skip_via_db` 比较 `ZDATEUPDATED > local_updated`，更新过的笔记自动重导，无需 `--rewrite`。

参考：[[icloud-obsidian-conflict-copies-fix]]
