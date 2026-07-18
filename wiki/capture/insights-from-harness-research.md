---
title: insights-from-harness-research
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


用户 2026-06-20 分享了一篇长篇调研笔记：为解决 AI"黑箱操作"问题（不知道 AI 刚才做了什么、为什么做、下一步打算做什么），筛了 100+ 仓库后筛选出 10 个工具。

## 核心模式提炼

### 1. 「仪表盘全黑」问题 = 运行时不可见性

用户描述：**"不开自动驾驶但仪表盘全黑，你只能坐着祈祷别撞墙"**。

映射到当前体系：
- ✅ 输入侧很好（CLAUDE.md、skills、memory、rules 全面）
- ❓ 运行时侧缺乏 visibility — 当前没有机制能回答"这轮 AI 做了什么/为什么做/下一步打算"。
- ECC 的核心卖点（instincts 系统 + 周报多 Agent review）实际上填补的是这个空白。

### 2. Instincts > Rules

ECC 最值钱的概念：**不是让 AI 记住规则，而是让 AI 在生成代码之前就知道这个场景下不该这么干**。

当前体系里大部分是 rule（"必须 XXX"、"不要 XXX"），少数 skill 有 instinct（"这个场景应该先想 XXX"）。差距：rule 是事后约束，instinct 是事前引导。

### 3. Superpowers 的「慢」是值得的

用户自己验证了：**"太慢了，每次改个小功能都要写 plan，烦得不行... 但上周改了一个涉及三个微服务的功能，全程没出一个低级错误"**。

用户已有的 writing-plans + executing-plans + TDD 链路就是同样的模式。需要有意识地接受这个 tradeoff。

### 4. 技能冲突：静默覆盖最坑

"两个都叫 code-review 的 skill，后装的会覆盖先装的——这种静默覆盖最坑，你根本不知道哪儿出了问题"。

当前 76 个 skill，有定期 audit（skills-context-tax-audit 框架）但缺**运行时冲突检测**。

### 5. Karpathy 规则：别过度抽象

"AI 喜欢写 helper function 但人类不这么干"——用户已有类似规则（最小改动、不穿透多层调用链），但分布在多个文件中（CLAUDE.md + AGENTS.md + 具体 skill）。

## 对当前体系的可操作改进

1. **增加「运行时透明性」**：可以考虑在每个 skill 结束或关键节点，自动输出一份"做了什么 + 为什么这么选 + 下一步计划"的结构化日志。减少用户的"黑箱焦虑"。

2. **Instincts 审计**：在下次 skills audit 时，检查高频 skill 有多少是 rule 驱动（必须/不要）vs instinct 驱动（这个场景应该先想 XX）。差距大的 skill 可以补 instincts 段。

3. **技能冲突检查**：list skills 时顺便检查同名 skill，作为 audit checklist 新增项。

**关联记忆：** [[all-skills-must-have-why]] [[skills-context-tax-audit]]
