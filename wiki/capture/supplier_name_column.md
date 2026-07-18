---
title: supplier_name_column
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


供应商排名分析必须使用"供应商名称"（Col 39）字段，而非"订单归属"（Col 58）。

**Why:** 订单归属字段把大量真实供应商笼统归为"其他供应商订单"（如JUPITER LEGEND CORPORATION、四川全球通等都被合并），掩盖了真实竞争格局。使用供应商名称才能看到真正的Top供应商。

**How to apply:** 分析供应商维度时，读取 Col 39（供应商名称）。华程相关订单（含各地华程、账号订单）合并为一家"华程"；国旅订单合并为"国旅"；其他供应商按实际名称各自独立。品牌分类（华程/自营）仍基于订单归属字段（Col 58）判断。
