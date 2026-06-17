---
title: Hermes Agent 深度拆解：与OpenClaw对比
type: source
created: 2026-05-29
updated: 2026-05-29
sources: [Hermes Agent 深度拆解：它强在哪，跟 OpenClaw 有什么区别.html]
source_path: 印象笔记管理工具/Hermes Agent 深度拆解：它强在哪，跟 OpenClaw 有什么区别.html
tags: [hermes, openclaw, agent, platform, comparison]
---

# Hermes Agent 深度拆解

> 来源：Original超级猛

## 一句话
Hermes Agent定位为"Agent平台层"，比OpenClaw更系统化——双入口、学习闭环、模型无锁定、完整自动化能力。

## 核心能力（6层）

1. **多入口Agent系统**：CLI + Messaging Gateway（Telegram/Discord/Slack/WhatsApp/Signal/Email）
2. **学习闭环**：Persistent Memory (MEMORY.md/USER.md) + Skills System + Session Search
3. **强执行路线**：terminal/file/browser/code/MCP/cron/delegation
4. **模型无锁定**：Nous Portal/OpenRouter/OpenAI/Anthropic/Gemini/GLM/Kimi/Minimax
5. **多Agent协作**：spawn subagents + parallel workstreams + RPC
6. **内置cron调度**：定时任务+结果分发

## 与OpenClaw对比

| 维度 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| 产品定位 | Agent平台层 / 长期运行框架 | 早期Agent Bot体系 |
| 主入口 | CLI + Messaging 双入口 | 更偏Bot/消息化 |
| 记忆系统 | Persistent Memory + Session Search + 外部Provider | 有memory，层次不够清晰 |
| Skills | 标准化、按需加载、支持Hub和自建 | 有，系统化程度较弱 |
| 执行能力 | terminal/file/browser/MCP/cron/delegation | 能力存在，整合度不如 |
| 模型支持 | provider-agnostic | 多provider，生态承接方向弱 |
| 自动化 | 内置cron/profiles/sessions/insights | 更偏agent/bot使用 |

**关键判断**：Hermes明确做了从OpenClaw的完整迁移路径（SOUL.md/MEMORY/USER/skills等），把自己放在"OpenClaw下一代承接者"的位置。

## 相关页面

- [[features/CLAUDE.md与上下文管理]]
- [[products/Claude Code]]
- [[sources/Claude永久大脑双模记忆Conway]]
