---
title: feedback_evernote_duplicate_handle
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


印象笔记 Favorites 导出时检测到同名重复笔记，采用 B 方案（跳过 + 报告）：
1. 脚本导出前检查 note_cache.json 统计真正同名标题
2. 同名笔记跳过导出，记录到 processed.json（type: skipped_dup_title）
3. 运行结束时列出全部重复笔记，提示用户处理
4. 用户手工将重复笔记移到 temp 笔记本（不可直接删除，必须等用户指令）

**全部副本都要移动，不能只移被跳过的部分**——用户需要同时看到保留版和删除版才能判断哪篇更好。

**Why:** 用户明确说不能擅自从 Evernote 删除任何笔记。且如果只移一条，用户无法对比判断哪条更好。

**How to apply:** 用 scripts/note_cache.json 按标题分组，找出所有同名笔记的 GUID（包括被保留和跳过的），用 note_store.getNote → updateNote(notebookGuid=TEMP) 全部移动到 temp。移动后清除 processed.json 中 type=skipped_dup_title 的记录，重新导出。
