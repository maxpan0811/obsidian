---

name: claude-code-ch8-subagent
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（八）（教不会我吃民法典！）：Subagent—让 Claude Code学会分身术.html

---

# 法律人的 Claude Code 教程（八）：Subagent — 让 Claude Code 学会分身术

> 来源：智律积成（微信公众号）

## 核心概念

- **Subagent** = 从主对话派生出的独立 AI 助手
- 每个 Subagent 有独立上下文、工具权限、系统提示、模型选择

## 内置 Agent

| Agent | 模型 | 权限 | 用途 |
|-------|------|------|------|
| Explore | Haiku | 只读 | 搜索文件、探索代码库 |
| Plan | 继承主对话 | 只读 | 研究与规划 |
| General-purpose | 继承主对话 | 全部工具 | 复杂研究、多步操作 |

## 创建方式

1. **推荐**：`/agents` 交互式创建
2. **手动**：在 `~/.claude/agents/` 下创建 `.md` 文件
3. **CLI**：`claude --agents '{"name":{...}}'`（临时）

## 三种协作模式

- **并行**：多个 Agent 同时干活，各自独立
- **流水线**：上一个 Agent 输出是下一个的输入
- **分支选择**：根据条件分发给不同专业 Agent

## Agent Teams（实验性）

多个 Agent 之间可以直接互相通信、协商、分工。适合模拟法庭辩论、复杂并购尽调等需多立场碰撞的场景。

[Related: [[features/Subagent]]]
