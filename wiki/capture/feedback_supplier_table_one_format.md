---
title: feedback_supplier_table_one_format
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2025/2026年 Sheet1 的供应商分析部分，统一为**一个表**格式：
- 标题：包团供应商贡献比例分析（按包团营收降序）
- 列：排名 | 供应商名称 | 参与包团数 | 包团营收 | 包团营收占比 | 包团人数 | 包团人数占比 | 包团人均卖价（元/人）
- 尾部三行汇总：包团整体平均（黄底）、散拼整体平均（粉底）、全部订单整体平均（黄底）
- 前5名供应商用绿色底色标注
- 不拆分成"贡献比例"和"平均卖价"两个表

**Why:** 用户明确要求对齐2026年的格式模板，拆成两个表会显得冗余且增加查阅负担。
**How to apply:** 用 analyze_alliance.py 生成时，用 create_sheet_summary 里的单一供应商表结构，不要拆表。
