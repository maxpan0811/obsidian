---
title: duckdb-excel-all-varchar
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# DuckDB 读 Excel 必须 all_varchar=true

**规则：** 所有 `read_xlsx()` 调用必须加 `all_varchar=true` 参数。

❌ 错误示范：`SELECT * FROM read_xlsx('order.xlsx')` — DuckDB 默认推断列类型，遇到数字列里混了字符串（如订单号前缀 `'`、备注等）直接报 `Failed to parse cell: Could not convert string to DOUBLE`。

✅ 正确写法：
```sql
SELECT * FROM read_xlsx('file.xlsx', all_varchar=true)
```
数值字段需要时显式 CAST：`CAST("成交人头" AS INT)`, `CAST("成交销售额" AS DOUBLE)`

**Why:** 用户的 Excel 几乎都有混合类型列（55K 行订单表、102K 行渠道明细都踩过这个坑）。DuckDB 类型推断过于激进，不处理必崩。

**How to apply:** 任何 DuckDB 读 Excel 的场景（CLI、Python、skill），默认加 `all_varchar=true`，不等报错再加。
