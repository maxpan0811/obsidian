---
title: feedback_revenue_share_caliber
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


分析包团/散拼占比时，统一按 **营收** 口径计算，不使用人数口径。

**Why:** 包团产品客单价通常高于散拼，按人数占比会低估包团的业务比重。用户明确要求用营收来反映真实业务结构。
**How to apply:** 在写包团占比/散拼占比时，用 `g_rev / total_rev` 而非 `g_peo / total_peo`。人数占比仅用于单独列示。
