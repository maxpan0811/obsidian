---
title: huacheng_product_type_dimension
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


华程直采融合订单数据表中 `下单时产品类型形态名称`（col43）包含三种产品类型：
- **出发地参团**: 56,807人 / 84.3% — 占绝大多数
- **定制包团**: 10,058人 / 14.9% — 集团欧洲事业部为主
- **目的地参团**: 535人 / 0.8% — 集团欧洲事业部为主

报表新增第5个 Sheet `{区域}-产品类型`，包含两段：
1. 产品形态汇总（人数/营收/订单数/人均/占比）
2. 各公司/事业部 × 产品类型明细（含小计）

**Why:** 用户要求补充产品类型维度，展示各公司的业务结构差异（如集团欧洲事业部以目的地参团+定制包团为主，6大分公司以出发地参团为主）。

**How to apply:** 在数据读取循环中增加 `pt_et`（产品类型级汇总）和 `pt_et_entity`（实体×产品类型级明细）两个 defaultdict，使用 `row[42]`（col43）获取产品类型名称。注意 `defaultdict` 嵌套结构为 `defaultdict(lambda: {'h':0,'r':0.0,'o':0})` 而非 `defaultdict(defaultdict(...))`，否则类型不匹配。
