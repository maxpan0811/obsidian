---
title: reading-to-system-pipeline
type: capture
tags: [auto-capture, process]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-20 完成了一次完整的"读文章→提炼→落地"闭环。4 篇文章 + 7 项产出。

## 管线模式

1. **读文章** — 用户分享行业文章
2. **提炼核心** — 交叉验证：哪些已验证、哪些是缝隙、哪些可操作
3. **落地** — 直接改写 CLAUDE.md / rules / skills / memory，而不是停留在讨论
4. **存经验** — 每项落地写 memory，更新 MEMORY.md 索引

## 本次的 7 项产出

| 来源 | 产出 | 类型 |
|------|------|------|
| 循环工程文章 | 运行时日志格式（⚙️） | CLAUDE.md 规则 |
| 循环工程讨论 | 所有 skill 必须有 Why | CLAUDE.md 规则 + memory + skill-creator |
| CLAUDE.md 最佳实践 | 反例优先于正例 | CLAUDE.md 规则 + skill-creator |
| CLAUDE.md 最佳实践 | 审计加第5问（规则能删吗） | 技能审计 SKILL.md |
| Harness 6 components 文章 | 6 components 思维框架 | CLAUDE.md 规则 |
| Harness 6 components 文章 | 多步脚本 checkpoint 习惯 | CLAUDE.md 规则 |
| 用户调研笔记 | Instincts > Rules 模式识别 | memory |

## 已补充 Why + 反例的 skill

- 产品市占率分析工具（10 条 Why + 5 个反例）
- 四川省联盟包团分析工具（7 条 Why + 3 个反例）
- 微信读书管理工具（5 条 Why）

其余 skill 使用时顺手补。

## 关键原则

- **不从零发明**：每项改动都能追溯到具体文章/讨论/踩坑
- **不改不动**：用户明确说"可以"才落地，说"后面用的时候再加"就停
- **改完验证**：每次改动后验证语法/引用/一致性
- **存完收口**：落地后写 memory + 更新索引，不留悬挂改动

**关联记忆：** [[all-skills-must-have-why]] [[runtime-log-format]] [[why-plus-counterexample-pattern]] [[harness-6-components-framework]]
