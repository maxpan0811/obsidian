---
title: feedback-memory-system-layer
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 记忆系统分层最佳实践

来自 Anthropic 的分层记忆架构，结合我们的实践。

## 四层结构

| 层 | 适用场景 | 我们 |
|:---|:---------|:----:|
| Chat Memory Synthesis | 普通用户自动综合 | CLI 不适用 |
| Project Memory Spaces | Pro 以上项目隔离 | 暂不用 |
| **CLAUDE.md** | Claude Code 项目宪法 | ✅ 已有但有空文件 |
| **API Memory Tool** | Agent 开发者 | 暂不用（非 API）|

## 关键经验

1. **CLAUDE.md 控制在 200 行以内** — 超过后遵守度下降。`gstack` skill 的 CLAUDE.md 有 873 行，需要拆分到 `.claude/rules/` 目录。
2. **全局 CLAUDE.md** (`~/.claude/CLAUDE.md`) 目前是空文件，应该放跨项目的通用规则（语言偏好、技术栈、代码风格）。
3. **决策链条必须记"为什么"** — memory 不能只记"修复了什么"，还要记"为什么这个方案"和"排除了什么替代方案"。
4. **`/memory` 命令** — Claude Code 里可查看积累的记忆并清理过期内容。
5. **Auto Memory** — Claude Code v2.1.59+ 默认开启，Claude 可跨会话自动写记忆笔记。路径在 `~/.claude/projects/-Users-panbo/memory/`。

## Why

之前 memory 偏重记录"做了什么"，缺乏决策上下文。下次遇到类似问题，只知道结果不知道原因，还是可能走弯路。

## How to apply

- 写 memory 时至少包含一句 **"为什么选这个方案"** 和一句 **"排除了什么替代方案"**
- `~/.claude/CLAUDE.md` 补充全局偏好（语言、工具链、规则）
- 检查 gstack CLAUDE.md 是否可拆分
- 定期用 `/memory` 清理过期记忆

## 相关链接

- [[feedback_claude_md]] — 项目完成写 CLAUDE.md
- [[feedback_context_management]] — context 管理策略
- [[auto-memory]] — 当前 auto-memory 规则
