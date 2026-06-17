---
title: Claude Code Superpowers：14个技能完整拆解
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?chksm=f0bb4e2bc7ccc73d3a20223b3e5f042...]
source_path: 印象笔记管理工具/Claude Code最佳搭档Superpowers：14个技能完整拆解，装上就是另一个AI.html
tags: [claude-code, superpowers, skill, workflow, plugin]
---

## 一句话摘要

Superpowers 是一个 Claude Code 开源插件，装上后 AI 多了 14 个「职业技能」——从需求分析到收尾形成完整开发流水线，每个技能都有**不可绕过的铁律**。

## 14 个技能的完整流水线

```
需求进来
  → 1 using-superpowers (路由：该调哪个技能？)
  → 2 brainstorming (需求分析：问问题、出方案、确认)
  → 3 writing-plans (写实施计划：拆成小任务)
  → 4 using-git-worktrees (开隔离环境)
  → 5 executing-plans / 6 subagent-driven-development (执行)
  → 7 dispatching-parallel-agents (并行派遣)
  → 8 test-driven-development (先测试后写码)
  → 9 systematic-debugging (四阶段排查 bug)
  → 10 verification-before-completion (验证才能说完成)
  → 11 requesting-code-review / 12 receiving-code-review (审查)
  → 13 writing-skills (封装新技能)
  → 14 finishing-a-development-branch (收尾)
```

## 设计哲学

1. **反合理化**：内置「反合理化」表，堵住 AI 想偷懒跳过技能的每一条借口（"这个问题很简单"→"查技能"）
2. **铁律不可绕**：违反就停，不是建议，是强制规则
3. **流水线而非散装**：14 个技能形成一条完整链路

## 相关页面

- [[products/Claude Code]]
- [[features/Skills]]
- [[sources/Everything Claude Code完整上手攻略]]
- [[sources/claude-code-best-practice-工作流指南]]
