---
title: /compact 指令深度解析——何时压、压什么、会丢什么
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=224748...]
source_path: 印象笔记管理工具/／compact 我用了 3 个月，今天把 Claude Code 这一个指令讲透：何时压 ／ 压什么 ／ 压完会丢什么.html
tags: [claude-code, compact, context-rot, context-management]
---

## 一句话摘要

`/compact` 不是「压缩」，是「销毁 + 接续」——95% 的人用错了时机。Claude Code 不是变慢，是悄悄丢东西，Anthropic 内部称为 **context rot（上下文腐烂）**。

## 核心机制

> 字面意思是压缩，但实际行为是：销毁旧上下文 → 用最新状态重建一个摘要 → 继续会话。

## 上下文腐烂（Context Rot）

长会话中，Claude 开始忘记自己刚刚改过什么文件、改了什么行、为什么改——这不是「我没说清楚」，是它**真的忘了**。

## 正确用法

- **何时压**：感觉 Claude 开始「忘了」上下文时
- **压什么**：销毁旧上下文，重建摘要
- **会丢什么**：微妙的历史细节、早期决策上下文、未经确认的临时结论
- **不要等**：等到明显变慢才压，已经丢了太多

## 相关页面

- [[products/Claude Code]]
- [[features/CLAUDE.md与上下文管理]]
- [[sources/CC顶级配置栈-半年调教]]
