---
title: feedback_thousand_sep_merge
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


每次生成 Excel 报表时，数值必须用千分号分隔且无小数位（Python f-string `:,` 格式），百分数无小数位（`:.1f%`）。

生成 `openpyxl` 报表时，**每个子标题行**（如"包团产品×日期汇总"、"供应商贡献比例分析"等）必须调用 `ws.merge_cells()` 跨所有数据列合并，否则标题只占 A1 一格，视觉效果差。

违反这两个规则会重复踩坑，需要在写入前逐项核对。

**Why:** 用户已多次指出这两个问题，且写入 `feedback_excel_format.md` 和此前反馈中仍会遗漏。
**How to apply:** Sheet 写入完成后，先检查所有数值是否用了 `f"{v:,}"`，再检查每个标题行是否调用了 `merge_cells()`。
