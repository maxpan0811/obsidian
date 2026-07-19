---
title: data-summary-cross-validate
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-19
created: 2026-07-19
---


数据汇总时必须交叉校验，防止列错位导致张冠李戴。

**Why:** 2026-07-19 做华程预算指标汇总时，从`收入毛利预算表_汇总.xlsx`的`预算单元汇总`sheet取值，因表头行与数据行空列错位（col7=合计，col8起=各公司），把上海公司的78,800错误填到北京公司下。原始文件北京公司=54,000，上海公司=78,800，两个sheet数据一致但我取错了列。

**How to apply:**
1. **交叉校验** — 从汇总表取某公司数值后，必须打开该公司的详细sheet比对annual total，不一致立即报错
2. **列映射显式化** — 打印 `(col_index, header_name)` 对照表确认映射，不从表头行猜列号
3. **合计勾稽** — 汇总后各分项加总 = 合计行，不等就停下来排查
4. ❌ 禁止直接从汇总表批量取值而不回源验证
