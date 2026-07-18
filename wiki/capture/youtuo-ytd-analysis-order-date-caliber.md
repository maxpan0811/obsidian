---
title: youtuo-ytd-analysis-order-date-caliber
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-30 完成悠途联盟门店 YTD 分析，修正了口径问题。

**教训：** "2025年1-12月" 文件里实际包含 2024 年 Q4 遗留订单（约 5248 行），**不能按 year==2025 过滤**，应该从文件读取所有欧洲订单。历史参考文件也是这么做的。

**口径确认：** 悠途联盟 YTD 报表使用**下单日期**口径（Col 13），与参考文件 `四川省悠途联盟门店分析20260609.xlsx` 一致。不能用出发日期。

**How to apply:**
- 任何年份标签为 "1-12月" 的 Excel 文件，实际数据可能覆盖前后年份的遗留订单
- 分析 YTD 数据时，不要用 `order_dt.year == year` 过滤
- 门店数据按子串匹配（短名 in 全名），特殊映射如 `名山县门市` → `雅安携程名山区名山门市`

**2026年关键数据：** 224单 505人 1,225.4万营收 | 双品牌占比 31.28%（华程370.0万+国旅13.3万）

[[alliance-analysis-reference]]
