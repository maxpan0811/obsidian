---
title: claude-code-best-practice：Claude Code 工作流指南
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://github.com/shanraisshan/claude-code-best-practice]
source_path: 印象笔记管理工具/1.7万星，claude-code-best-practice：Claude Code 工作流指南.html
tags: [claude-code, workflow, best-practice, command, skill, agent]
---

## 一句话摘要

不是教你几条 Claude Code 小技巧，而是教你把 Claude Code 组织成一套可复用、可协作、可持续迭代的工作流——核心在于**给能力分层、划清职责边界**。

## 核心内容

### 分层分工体系

| 层 | 工具 | 职责 | 适合放什么 |
|---|------|------|-----------|
| 入口 | **command** | 一句话拉起一套动作 | 触发词、固定流程包装 |
| 执行 | **agent / subagent** | 重任务、长任务、独立上下文 | 不要把复杂活塞在主会话里 |
| 复用 | **skill** | 可复用的方法、步骤、判断标准 | 会反复用到的经验 |
| 稳定配置 | **settings** | 稳定规则和全局偏好 | 长期希望模型遵守的约束 |
| 长期记忆 | **memory** | 持续性背景和长期记忆 | 以后也得记得的事 |
| 外部能力 | **MCP** | 接入外部工具、数据源和系统能力 | 进入日常流程的外部工具 |

### 三个常见问题

1. **上下文混乱**：所有规则、背景、临时需求都塞进一个会话，越聊越钝
2. **职责混乱**：command/skill/agent/settings/memory/MCP 各自该干什么没有边界
3. **流程失控**：同样一类任务每次都重讲一遍，无法复用，也很难协作

### 最短上手闭环

1. 选一个经常重复的任务
2. 把入口收成 command
3. 把会重复解释的方法写成 skill
4. 把又长又重的执行切给 subagent
5. 把稳定规则放进 settings/memory
6. 把外部能力接到 MCP

### 适合谁

- 已经在用 Claude Code，但遇到上下文/职责/流程「三乱」的人
- 想把 Claude Code 从「会用」推进到「能稳定用于真实项目」的人
- 希望把自己的经验整理成 command/skill/agent 分工的人

## 相关页面

- [[products/Claude Code]] — Claude Code 产品概览
- [[sources/Claude Code教程-二-核心操作]] — 核心操作教程
- [[sources/从会话管理到知识库-四层进阶指南]] — 会话分层体系
- [[features/工作模式与权限]] — 工作模式
- [[features/CLAUDE.md与上下文管理]] — 上下文管理
- [[features/Skills]] — Skills 封装
- [[features/MCP]] — MCP 外部工具
- [[features/Subagent]] — Subagent 分身
