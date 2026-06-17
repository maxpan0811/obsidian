---
name: Subagent
type: feature
tags: [claude-code, subagent]
---

# Subagent

所属产品：[[products/Claude Code|Claude Code]]

## 概述

Subagent = 从主对话派生出的独立 AI 助手。每个 Subagent 有独立上下文、工具权限、系统提示和模型选择。

类比：律所合伙人 → junior 律师 → 多个专门化 junior 各司其职。

## 内置 Agent

| Agent | 模型 | 工具权限 | 用途 |
|-------|------|---------|------|
| Explore | Haiku | 只读 | 搜索文件、探索代码库 |
| Plan | 继承主对话 | 只读 | 研究与规划 |
| General-purpose | 继承主对话 | 全部工具 | 复杂研究、多步操作 |

## 创建方式

1. **`/agents` 交互式**（推荐）：选择作用域 → 描述需求 → 选择权限和模型 → 保存
2. **手动创建**：`~/.claude/agents/<name>.md`
3. **CLI 内联**：`claude --agents '{"name":{...}}'`（临时）

## 两种关键设置

- **工具权限**：`tools: [Read, Grep]`（白名单）或 `disallowedTools: [Write, Edit]`（黑名单）
- **模型选择**：Haiku（搜索/分类）→ Sonnet（日常）→ Opus（复杂推理）

## 三种协作模式

- **并行**：多个 Agent 同时独立干活（如合同分模块审查）
- **流水线**：上一个输出是下一个的输入（检索类案 → 提取观点 → 生成代理词）
- **分支选择**：根据条件分发给不同专业 Agent（民事/刑事/行政分流）

## Agent Teams（实验性）

多个 Agent 之间可直接通信、协商、分工。适合模拟法庭辩论、复杂并购尽调等需多立场碰撞的场景。

来源：[[sources/Claude Code教程-八-Subagent]]
