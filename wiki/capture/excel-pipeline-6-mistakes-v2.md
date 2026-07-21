---
title: excel-pipeline-6-mistakes-v2
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-21
created: 2026-07-21
---


# Excel → 看板数据管线 6 大常见错误 v2

每次从 Excel 源表重建数据看板时必犯的系统性错误。2026-07-21 门店管理看板拆分任务中全部触发了一遍。

## 1. 时间字段：默认用「下单日期」❌ → 应确认用「出发日期」✅
- **反例**：华西欧洲全年用下单日期=3.30亿，用出发日期=3.45亿
- **Why**：旅游行业产量口径按出发日期（实际出行），非下单日期
- **How to apply**：先问「时间口径是下单还是出发」

## 2. 双品牌口径：默认用「供应商名称」LIKE ❌ → 应用「订单归属」≠ '其他供应商订单' ✅
- **反例**：用供应商名称 LIKE '%华程%' 会漏掉部分订单、误包含其他旅行社
- **正确**：`订单归属` 有明确分类（北京华程/上海华程/国旅/其他供应商等），排除法精准
- **How to apply**：先看 `订单归属` DISTINCT 值，排除法替代包含法

## 3. 产品分类：默认用「目的地国家_归属业务板块」❌ → 应用「考核区域」✅
- **反例**：归属业务板块含「目的地参团业务部」= 目的地参团，不算跟团游
- **Why**：考核区域已正确做了分类，不含目的地参团
- **How to apply**：直接问用户用哪个字段做产品分类

## 4. 产品映射二次查表：key 已是映射值，别再查 PRODUCT_MAP
- **反例**：`PRODUCT_MAP.get(k) == pn`，k 已是"美洲"，PRODUCT_MAP 只有"北美洲"/"中南美" → 美洲全归零
- **正确**：`k == pn`
- **Why**：第一步已映射存为 key，后续不能再查原映射表

## 5. 省份产品汇总：大区汇总只用 Top10 门店 → 丢长尾 75%
- **反例**：产品筛选时遍历门店 product_data 聚合，非 Top10 被丢掉
- **正确**：省份加 `prov_product` 全量字段，大区汇总用省份级数据

## 6. JS onclick 转义 + Excel datetime 处理（技术细节）
- onclick：Python 生成 JS 时 `onclick="selRegion(\'' + r + '\')"` 才对
- datetime：openpyxl `hasattr(val, 'date')` → `(val.date() - date(1899,12,30)).days`

**Why**：这些错误根因相同——每次遇到 Excel 管线任务会跳进相同思维捷径。下次先过这 6 条。

**How to apply**：每次「从 Excel 构建看板」任务开始前，逐条确认。
