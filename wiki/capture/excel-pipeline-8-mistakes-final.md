---
title: excel-pipeline-8-mistakes-final
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-22
created: 2026-07-22
---


# Excel → 看板数据管线 8 大常见错误（最终版）

从 Excel 源表重建数据看板时必犯的系统性错误。2026-07-21~22 门店管理看板拆分任务全部验证通过。

## 1. 时间字段：默认用「下单日期」❌ → 应用「出发日期」✅
- **反例**：华西欧洲全年用下单日期=3.30亿，用出发日期=3.45亿
- **Why**：旅游行业产量口径按出发日期（出行时间）

## 2. 双品牌口径：默认用「供应商名称」❌ → 应用「订单归属」排除法 ✅
- **正确**：`订单归属` ≠ `'其他供应商订单'`

## 3. 产品分类：默认用「目的地国家_归属业务板块」❌ → 应用「考核区域」✅
- **Why**：考核区域不含目的地参团

## 4. 产品映射二次查表：key 已是映射值，别再查 PRODUCT_MAP
- **反例**：`PRODUCT_MAP.get("美洲")` = None → 全归零

## 5. 省份产品汇总：大区汇总只用 Top10 → 丢长尾
- **正确**：加 `prov_product` 全量字段

## 6. 门店/旅顾分开统计
- 门店数 = 非「旅行顾问」前缀、旅顾数 = startswith('旅行顾问')
- 产量含旅顾，Top10 排除旅顾

## 7. CSS 缺失：从模板提取 CSS 时漏掉业务样式
- **反例**：`template.html` 不含 `.low-share`，零产量标红不生效
- **正确**：`build_html()` 中补上 `.low-share { color: #a02020; background: #ffe0e0; }` 等业务 CSS
- **How**：不要假设 template.html 的 CSS 是完整的——它是给原始大看板用的

## 8. JS 函数遗漏：新增 onclick 属性但忘记定义对应函数
- **反例**：加了 `selType` 按钮但没有 `function selType(t)` → 按钮按不动
- **How**：每新增一个 `onclick="selXxx(...)"` 都必须同步新增 `function selXxx(...)` 并在 render() 链中正确调用

**Why**：每次 Excel 管线都跳相同思维捷径。

**How to apply**：每次「从 Excel 构建看板」任务前，逐条过这 8 条。
**验证数据**：华西 25年欧洲 3.45亿、美洲总 5,030万/双品 814万（用户一致确认）。
