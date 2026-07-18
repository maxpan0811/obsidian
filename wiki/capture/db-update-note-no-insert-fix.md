---
title: db-update-note-no-insert-fix
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**问题：** `sync_favorites.py` 管线中 `update_note()` 只执行 `UPDATE notes SET ... WHERE guid=?`。当导出队列中包含不在 notes 表的新 GUID 时，.md 文件成功写入磁盘但 DB 状态未更新。

**根因：** `db.py:93` — `update_note` 设计时假设调用前 GUID 已在 notes 表中（由 migrate_from_json.py 或 reconcile 预创建），但 reconcile 仅创建 export_queue，不创建 notes 表记录。`export_one()` 调用 `update_note(guid, status='exported', ...)` 对新 GUID 静默不做事。

**影响：** 474 条新笔记的 .md 文件成功导出但未被 DB 追踪，verify 时显示 493 条 on-disk-not-in-DB。

**修复：** 在 UPDATE 前检查记录存在性，不存在则 INSERT：

```python
def update_note(guid, **kwargs):
    with _get_conn() as conn:
        existing = conn.execute("SELECT guid FROM notes WHERE guid=?", (guid,)).fetchone()
        if existing:
            fields = [f"{k}=?" for k in kwargs]
            values = list(kwargs.values()) + [guid]
            conn.execute(f"UPDATE notes SET {', '.join(fields)} WHERE guid=?", values)
        else:
            fields = {'guid': guid, **kwargs}
            placeholders = ', '.join(fields.keys())
            values_placeholder = ', '.join('?' for _ in fields)
            conn.execute(
                f"INSERT INTO notes ({placeholders}) VALUES ({values_placeholder})",
                list(fields.values())
            )
```

**Why:** 任何 DB CRUD 函数都需考虑记录不存在的情况。`update_note` 在 sync_favorites.py 的 export 流程中被 `export_one()` 调用处理新笔记，但该函数从未预期处理新 GUID。

**How to apply:**
- 每次创建 `update_*` 或 `save_*` 函数时，默认使用 INSERT OR REPLACE 语义，或在 UPDATE 前做存在性检查
- 调用链验证：追踪 `update_note` 的所有调用方，确保每个调用路径都能处理"记录不存在"
