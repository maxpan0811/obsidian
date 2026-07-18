---
title: feedback-scan-full-table
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 分析 Excel 必须先扫全表

处理 Excel 时，不能只看前几行样本就建立处理逻辑。

**Why:** 这次写华北众信脚本时只看了前8行（北京→陕西），没翻到第10-14行还有甘肃、宁夏、青海、山西、内蒙古，导致 PROVINCE_MAP 漏了5个省份。用户发现后才补上。

**How to apply:** 处理 Excel 的第一步永远是 `ws.max_row` 获取总行数，然后用循环把所有非空行的第一列（或 key 列）打印出来确认完整范围，再写处理逻辑。
