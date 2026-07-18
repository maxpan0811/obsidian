---
title: runtime-log-format
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-20 确立运行时日志规则：每个响应末尾附带操作日志，格式为 `⚙️ [已完成] | [关键决策] | → [下一步]`。

**Why:** 用户反馈"不知道 AI 刚才做了什么、为什么这么做、下一步打算怎么做"，像开了自动驾驶但仪表盘全黑。运行时日志弥补了输入侧（CLAUDE.md + skills + memory）强大但运行时不可见的缺口。

**How to apply:**
1. 复杂任务分段输出时，每段末尾带日志；简单任务一次性输出
2. 日志字段：已完成（1-15字）、关键决策（10-30字，含口径/依据）、下一步（5-15字）
3. 不含决策点的单步操作可省略「关键决策」
4. 格式与 Caveman 模式兼容——结构化的简短脚注，不破坏正文简洁

**关联记忆：** [[all-skills-must-have-why]] [[insights-from-harness-research]]
