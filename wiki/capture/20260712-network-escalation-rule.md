---
title: 20260712-network-escalation-rule
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


运行 local_sync.py 从其他笔记本批量移入 Favorites 的笔记后，需要分别处理：
1. 附件笔记（PDF/Word/Excel 等）→ 移入 temp 笔记本（不用导出 .md）
2. 重复标题笔记 → 全部移入 temp，一条不留
3. stuck 笔记（DB 标记 moved_to_temp 但实际仍在 Favorites）→ 单独修复

关键发现：多次分段清理时，DB 在 API 调用成功前就更新了 status，导致百余篇笔记 DB 显示已移入 temp 但实际还在 Favorites。需单独检查并修复。
