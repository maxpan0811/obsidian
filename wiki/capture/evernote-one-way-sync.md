---
title: evernote-one-way-sync
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


印象笔记 Favorites → Obsidian 同步规则：

- **方向是单向的**：只从印象笔记导出到 Obsidian，绝不从 Obsidian 写回印象笔记
- **源端修改会覆盖**：印象笔记里的笔记修改后（updated 时间戳变化），`reconcile` 会识别并重新导出覆盖 Obsidian 的版本
- ⚠️ 曾误解为"修改过的笔记不覆盖"(2026-06-30)。用户修正：印象笔记改了就该覆盖 Obsidian，这才是预期行为

**Why：** 印象笔记是权威源，Obsidian 是只读镜像。源改了镜像就该同步更新，但反向绝对不行。

**相关文件：**
- `reconcile.py` — 保留 `updated` 时间戳检测：`if updated and n.get('updated', 0) != updated: queue.append((guid, 'updated'))`
- `sync_favorites.py` — `batch_update_timestamps` 只放在 export 步骤末尾，不在 reconcile 中（2026-06-30 新增安全规则）
