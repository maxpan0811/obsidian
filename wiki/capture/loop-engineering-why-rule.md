---
title: loop-engineering-why-rule
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-20 讨论了循环工程（loop engineering）的概念和当前体系的成熟度。

## 核心输出

**所有 skill 必须有 Why 规则正式确立**，写入全局 CLAUDE.md。

## 背景

用户分享了关于循环工程的文章，分析了其核心六件套（自动触发、隔离工作区、技能文件、MCP 连接器、子代理对抗审查、外存状态持久化）。发现了用户的体系已有 5/6 件套，缺自动触发层。

在此基础上讨论了意图债（Intent Debt）问题：不含 Why 的 skill 3 个月后只能用"以前就是这么做的"解释。用户确立规则：所有 skill 必须记录关键决策的 Why。

**Why:** 追溯成本比记录成本高 10 倍。技能文件会累积到 76 个，未来更多。不记 Why，系统会丢失商业判断和业务验证。

**How to apply:**
1. 创建新 skill → SKILL.md 写完 What 后，花 30 秒加关键决策的 Why
2. 修改已有 skill → 如果改了口径/行为/阈值，同时更新对应 Why
3. 正好被 skill-creator 引用时自动触发该规则
