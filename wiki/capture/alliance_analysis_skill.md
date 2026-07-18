---
title: alliance_analysis_skill
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


已创建 `四川省联盟包团分析工具` skill，位于 `/Users/panbo/.claude/skills/四川省联盟包团分析工具/`。

包含：
- `SKILL.md` — 技能定义（触发器：联盟包团/周一联盟/包团分析）
- `scripts/analyze_alliance.py` — 可复用的 Python 分析脚本

核心逻辑：按产品ID×出发日期分组，联盟门店合计人数 ≥ 10 为包团，其余为散拼。输出两个 Sheet 的 Excel。

**默认配置**：周一联盟 30 家门店、2026年欧洲数据、包团阈值 10人。
**自定义**：改脚本顶部 `ALLIANCE_FILE`/`ALLIANCE_SHEET`/`ORDERS_FILE`/`GROUP_THRESHOLD` 可适配其他联盟。

**Why:** 用户完成了周一联盟包团分析后要求保存为独立 skill，便于复用。

**How to apply:** 用户提到"联盟包团"类需求时调用此 skill。
