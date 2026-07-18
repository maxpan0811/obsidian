---
title: claude-dot-md-best-practices
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-20 用户分享原极客聊AI文章关于CLAUDE.md的7条黄金规则、3个大坑、Skills系统。与当前体系交叉验证。

## 已验证（当前体系已覆盖）

| 文章说的 | 当前体系 | 状态 |
|----------|---------|------|
| 三层：CLAUDE.md + Skills + 项目级文件 | 全局→Workspace→项目三级分层 | ✅ 已覆盖且更强（含rules/） |
| 祈使句不用描述句 | CLAUDE.md 全祈使句 | ✅ 已覆盖 |
| Skills = 动态加载专项规则 | 76 skills 按触发条件加载 | ✅ 已覆盖 |
| 只写AI猜不到的东西 | CLAUDE.md 收全局未覆盖的 | ✅ 已覆盖且更强（+上下文分级Tier 1-3） |
| 角色锚定在最前面 | 全局CLAUDE.md开头配置 | ✅ 已覆盖 |

## 有价值的补充

### 1. 反例 > 正例（值得推广到已有skill）

文章核心观察：**AI对"不要做什么"的理解远比"要做什么"清晰**。

当前体系里绝大多数是"必须/不要"的正向约束（rule），缺少配套的反例说明。比如现在写"包团占比用营收口径"——更好的写法是

> **包团/散拼占比统一按营收计算**，不以人数计算。错误示范：不要用人数做占比，人数口径会高估低价大团的占比，扭曲分析结论。

**可操作改进：** 在以后的skill Why段里，给关键的threshold/规则加一条"反例"或"不要"。

### 2. 定期修剪（当前体系没做）

"有些规则写进去两周后你会发现，删掉Claude也能做对——因为它已经学会了。这时候果断删掉"。

当前有skills audit（skills-context-tax-audit），但audit检查的是**overlap/conflict/token cost**，不检查"这规则AI已经学会了吗，可以删了吗"。

**可操作改进：** audit checklist 新增一条 `❏ 规则是否已被AI学会？可删？`

### 3. 规则数量的警戒线（当前没显式标）

文章建议15条以内。当前全局CLAUDE.md ~128行，规则部分约30条（含工作方式约定的18-20条具体规则 + 其他），实际上超出15条且分散在各节。

但当前体系是分层加载的（Tier 1-3 + Skills按需），不是所有规则同时出现在AI视野里。所以15条警戒线主要适用于**单层、单文件的CLAUDE.md用户**。对分层体系来说，更应该检查的是**每个skill/skill的规则数**——单个skill超过15条就该拆分。

**关联记忆：** [[all-skills-must-have-why]] [[skills-context-tax-audit]] [[runtime-log-format]]
