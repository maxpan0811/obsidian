---
title: expense-report-first-use-20260710
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-07-10 首次使用"差旅报销工具" skill。从 QQ 邮箱下载附件 → 三引擎提取金额 → 构建城市时间线 → 生成 Excel。

### 技术要点

**携程发票提取：** 金额在 `¥XX.00` 行（PDF L44），行程在备注栏「携程订单」行。PDF 没有出发时间，只有日期和航班号。

**12306 提取：** 票价在 `票价:` 后 `¥XXX.00`（L24），时间在 `HH:MM开`（L22），区间在 L33-34。

**滴滴提取：** 用 PyMuPDF `get_text("dict")` 获取 text blocks 的 y/x 坐标：
- y=237 行：出行日期(x~191)、出发地(x~258)、到达地(x~373)
- y=293 行：金额
- 出发时间从对应的「滴滴出行行程报销单」提取（y=372）

**城市归因：** 大交通→目的地城市，当天滴滴全归该城市。6/18 成都→上海有原票和改签两笔（¥850+¥314），均计入。

**rm -rf 事故：** 误用 `rm -rf old/` 永久删除 3 张发票，无法恢复。已写入全局 CLAUDE.md + settings.json deny 规则。

**Why:** 差旅报销需要提取 PDF 中的金额、日期、出发地/到达地，按城市归因。
**How to apply:** 下载 QQ 邮箱附件 → PyMuPDF 提取 → 构建时间轴 → 生成 Excel。禁止 rm -rf，只用 shutil.move 到 Trash。
