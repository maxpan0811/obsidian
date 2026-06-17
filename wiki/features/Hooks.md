---
name: Hooks
type: feature
tags: [claude-code, hooks]
---

# Hooks

所属产品：[[products/Claude Code|Claude Code]]

## 概述

Hook 是自动触发的规则。CLAUDE.md 可能忘、Skill 可能跳步，**Hook 是立铁律**——触发了就自动执行，没有商量余地。

核心思想：从"希望 AI 做对"到**用规则创造确定性**。

## 核心概念：上下文劫持

Hook 的设计思路与常规提示不同：**不是让模型「记住」规则，而是每次处理用户消息前强制注入规则**。注入发生在模型开始生成回复之前，是系统级的强制介入，不依赖模型的「记忆力」。

> 用自然语言指令约束一个概率生成系统，指令必然被稀释。有效的约束必须在模型的概率处理之外。—— Harness Engineering

## 四种动作类型

| 类型 | 说明 | 示例 |
|------|------|------|
| 执行命令 | 在电脑上跑一条指令 | 播放提示音、写日志 |
| 发送请求 | 把信息发到一个网址 | 任务完成通知协作平台 |
| 让 AI 判断 | 让 Claude 做一次独立评估 | "这次审核是否覆盖了所有必查项？" |
| 派出子代理 | 派小助手去检查文件 | "检查输出的审核意见格式是否规范" |

## 支持的事件（31个）

Claude Code 支持 31 个 hook 事件（截至 2026年5月），核心事件：

| 事件 | 触发时机 | 用途 |
|------|---------|------|
| `UserPromptSubmit` | 用户发消息后、模型处理前 | **核心**：强制注入纪律提醒和状态 |
| `PreToolUse` | 任意工具调用执行前 | 文件写入前拦截 |
| `PostToolUse` | 工具调用成功返回后 | 注入校验结果 |
| `PostToolUseFailure` | 工具调用失败后 | 错误处理 |
| `Stop` | 模型完成本轮回复时 | 会话归档 |
| `SessionStart` | 会话启动或恢复时 | 初始化检查 |
| `PreCompact/PostCompact` | 上下文压缩前/后 | 压缩感知 |

## Hook 脚本输出格式

`UserPromptSubmit` 事件的注入格式（stdout）：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "这里是要注入到模型上下文的内容"
  }
}
```

`additionalContext` 的内容会出现在模型的系统提示层，在用户消息之前被处理。无论用户发什么，模型在处理它之前都会先读到这段内容。

## 配置方式

### settings.json（推荐直接编辑）

Hook 配置写在 `~/.claude/settings.json`（全局生效）或 `<项目>/.claude/settings.json`（仅当前项目）。两个位置可以同时存在，Claude Code 会合并加载。

```json
{
  "hooks": {
    "UserPromptSubmit": [
      { "hooks": [ { "type": "command", "command": "node ~/.claude/scripts/hook-discipline.js", "shell": "bash" } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python '~/.claude/scripts/export_chat.py'", "shell": "bash" } ] }
    ]
  }
}
```

### 对话式配置（轻量）

直接跟 Claude Code 说需求：
- "配置一个**全局** hook：完成任务时自动播放提示音"
- "给**这个项目**配置审计 hook：每次修改文件记录修改前后内容"

## 全局 vs 项目级

- 全局（`~/.claude/settings.json`）：所有项目生效
- 项目级（`.claude/settings.json`）：仅当前项目生效

## 三层约束体系中的位置

```
CLAUDE.md（静态规则，对话中被稀释）
  ↓
Hook（运行时强制注入，每次消息前生效）
  ↓
Skill（流程锁定，封装工作流）
```

Hook 层是三层输入端机制中**最底层、最强制**的一层。

来源：[[sources/Claude Code教程-七-Hooks]] · [[sources/Claude Code七层约束-Hook-Skill-CLAUDE]]
