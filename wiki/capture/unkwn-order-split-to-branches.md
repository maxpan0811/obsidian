---
title: unkwn-order-split-to-branches
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-23
created: 2026-07-23
---


# unkwn 订单拆分 + national_overview 按月重建

## unkwn 订单归属

融合订单表中 `订单销售公司` = `unkwn` 的订单全部是携程平台线上产量。

**拆分规则**：按 `新架构团公司` 字段分配到 6 分公司：
- 北京公司→华北、上海公司→华东、广州公司→华南、成都公司→华西、武汉公司→华中、厦门公司→福建

❌ 不能用 `门店省份` 分（线上业务省份不反映分公司归属）
✅ `订单来源` 判断携程/非携程 + `新架构团公司` 判断分公司

## 产品分类字段

❌ `目的地归属区域`（col B）——有西欧/南欧/英爱等子类
✅ `目的地归属业务板块`（col A）——只有欧洲/中东非/北美洲/澳新/中亚+高加索+蒙古/中南美 6 个值

## national_overview 在 periods 中有 19 份副本

看板的 `periods.month.data[0-11]`、`quarter.data[0-2]`、`half.data[0-1]`、`year.data[0]` 及顶层共 **19 处** 都有 `national_overview` 副本。必须按月从 Excel 聚合然后分别填入。

❌ 只更新顶层 → periods 中旧值未改
❌ 用暴力替换覆盖全部 → 丢失月度差异
✅ 按月聚合 + 按季/半年/年汇总 + 逐 period 填入

**How to apply**：更新渠道管理看板任何数据时，先确认该字段在 periods 中有多少副本，一律从 Excel 按原始维度聚合。

## JSON 编辑避坑

❌ `content.find(';\n', idx)` 找结尾 → JSON 字符串内部有 `;` 会截断
✅ 大括号深度计数定位 JSON 边界
✅ 保留 `before[JSON_START]` 完整 HTML `<head>` 不丢失
