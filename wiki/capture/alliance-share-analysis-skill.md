---
title: alliance-share-analysis-skill
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


已创建 `四川省联盟市占率分析工具` skill，位于 `/Users/panbo/.claude/skills/四川省联盟市占率分析工具/`。

包含：
- `SKILL.md` — 技能定义（触发器：联盟市占率/四大联盟/叮叮旅游/周一联盟/北斗联盟/悠途联盟）
- `scripts/analyze_alliance_share.py` — 812 行主分析脚本

核心逻辑：分析四川省四大门店联盟在携程欧洲渠道的预订口径双品牌市占率。
- 内置四大联盟 69 家门店清单
- 时间周期：上一个完整自然周（下单日期 Col 13 筛选）
- 三周期对比：本周 + 环比上周 + 同比去年同周
- 输出 5-Sheet Excel（1 联盟汇总对比 + 4 联盟门店明细）
- 条件格式：绿升红降（变化方向）、偶数行淡蓝、TOP1非华程浅橘

**默认配置**：欧洲板块、预订口径、自动检测最新订单文件。
**门店更新**：每季度手动修改 `ALLIANCE_STORES` 字典。

**Why:** 用户需要按自然周维度监控四大联盟的华程双品牌（华程+国旅自营）市占率趋势，要求预订口径（下单日期）而非出发口径，以便更及时地反映销售团队的当前表现。

**How to apply:** 用户说联盟市占率/四大联盟等触发词时调用此 skill，直接运行脚本即可。
