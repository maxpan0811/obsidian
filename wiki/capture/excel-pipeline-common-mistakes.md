---
title: excel-pipeline-common-mistakes
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-21
created: 2026-07-21
---


# Excel → 看板数据管线常见错误清单

每次从 Excel 源表重建数据看板时，最容易犯以下系统性错误：

## 1. 时间字段：默认用「下单日期」❌ → 应确认用「出发日期」✅
- **反例**：华西欧洲全年数据用下单日期算 = 3.30亿，用出发日期 = 3.45亿
- **Why**：旅游行业的产量口径通常按出发日期（实际出行），而非下单日期（预定时间）
- **How to apply**：每次做数据管线，先问「时间口径是下单还是出发」

## 2. 产品形态过滤：不要自作主张加 `产品形态 = '跟团游'`
- **反例**：用户明确说「半自助游属于跟团游，不要剔除」
- **Why**：半自助游在业务上归跟团游大类，`产品形态` 字段区分只是为了内部统计
- **How to apply**：不要按 `产品形态` 字段过滤，除非用户明确要求排除半自助

## 3. JS onclick 引号转义：Python f-string 生成的 JS 字符串里容易搞错
- **反例**：`onclick="selRegion(''全部'')"` 或 `onclick="selRegion(\\'全部\\')"` 都不对
- **正确**：生成的 HTML 中应为 `onclick="selRegion('全部')"`（双引号属性内单引号不需要转义）

## 4. Excel 日期序列号：openpyxl 读出来是 datetime 对象，不是整数
- **反例**：用 `int(float(str(val)))` 处理 datetime 对象会报错
- **正确**：先判断 `hasattr(dt_val, 'date')`，再用 `(dt_val.date() - date(1899,12,30)).days`
- **Why**：openpyxl 的 `data_only=True` 模式下日期列返回 datetime，不是原始序列号

## 5. 大区汇总不能只用 Top10 门店数据
- **反例**：产品筛选时的大区汇总只聚合 Top10，丢掉了长尾 75% 的数据
- **正确**：省份层加 `prov_product` 全量字段，大区汇总用它而非遍历门店

**Why**：这些错误每次都一模一样——因为我在遇到 Excel 数据管线任务时，会跳进相同的思维捷径。

**How to apply**：每次「从 Excel 构建看板」任务开始时，先过一遍这 5 条清单。
