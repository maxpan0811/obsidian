---
title: Claude Code 七层约束（2）：Hook+Skill+CLAUDE.md 分层设计
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzIwMDcwMjYwNg==&mid=224748...]
source_path: 印象笔记管理工具/Claude Code 七层约束（2）：任务开始前的准备／Hook+Skill+CLAUDE.md 分层设计全拆解.html
tags: [claude-code, harness-engineering, hook, skill, claude-dot-md, constraint-system]
---

## 一句话摘要

Claude Code 长期项目质量退化的根本原因在于**结构性的**——用自然语言指令约束概率生成系统，指令必然被稀释。真正的解法是 Harness Engineering：不改变模型，而是在输入端设计行为边界，让约束在模型处理任务之前就已就位。

## 核心洞察

> 用自然语言指令约束一个概率生成系统，等于把防线建在这个系统内部。指令在长对话中必然被稀释。有效的约束必须在模型的概率处理之外。

## 三个输入端机制

### 第1层：Hook — 事件注入（上下文劫持）

- **核心思路**：不是让模型「记住」规则，而是每次处理用户消息前**强制注入**规则
- **关键事件**：`UserPromptSubmit`（用户发消息后模型处理前）、`Stop`（会话结束时触发归档）
- **注入方式**：脚本 stdout 输出特定 JSON 格式的 `additionalContext`，出现在系统提示层
- **优势**：系统级强制介入，不依赖模型记忆力
- **支持的 31 个事件**：覆盖会话生命周期、用户输入、工具调用、子代理、任务管理、文件环境、上下文压缩等 9 大类

### 第2层：Skill — 流程锁定

- **安装**：`enabledPlugins` 配置
- **自动激活机制**：安装后自动生效
- **三类使用场景**：约束型 Skill、工具型 Skill、知识型 Skill
- **验证**：检查是否已生效

### 第3层：CLAUDE.md — 分级规则体系

- **三级加载**：全局 → 项目 → 子目录，逐层覆盖
- **每级职责**：全局（稳定规则和偏好）、项目（项目背景和约束）、子目录（模块级约定）
- **冲突处理**：下层覆盖上层

## 三层协同逻辑

```
CAUTION.md（全局偏好）
  ↓
CLAUDE.md（项目规则）
  ↓
Hook 注入（运行时强制）
  ↓
Skill 锁定（流程封装）
```

## 关联阅读

- 七层约束系列第 1 篇：让 Claude Code 成为稳定协作者

## 相关页面

- [[products/Claude Code]]
- [[features/Hooks]]
- [[features/Skills]]
- [[features/CLAUDE.md与上下文管理]]
- [[sources/claude-code-best-practice-工作流指南]]
- [[sources/Everything Claude Code完整上手攻略]]
