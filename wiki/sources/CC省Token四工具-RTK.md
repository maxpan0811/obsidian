---
title: Claude Code 省 Token 四工具
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzI1NzA2MjU0Nw==&mid=265084...]
source_path: 印象笔记管理工具/Claude Code烧光我的余额！这4个工具，让我的Token消耗直接减半！.html
tags: [claude-code, token, cost-optimization, tool-recommendation]
---

## 一句话摘要

Claude Code 真正烧 token 的原因不是问太多，而是上下文里塞进了大量**终端输出噪音**（测试日志、Git 状态、工具返回的 DOM/JSON），四种工具针对不同场景做上下文瘦身。

## 四大省 Token 工具

| 工具 | 场景 | 效果 |
|------|------|------|
| **RTK** (Rust Token Killer) | 终端输出太吵（测试、Git、构建） | 部分命令场景可省 **60%-90%** token |
| （其余工具待原文补充） | | |

## 核心观点

> Claude Code 真正烧 token 的原因：它看得太多，很多还没必要。跑一次测试，终端几百行日志全进上下文；接 MCP，工具返回一大坨 DOM/JSON 都塞进去。

## 相关页面

- [[products/Claude Code]]
- [[sources/Claude Code十大必装MCP推荐]]
- [[sources/claude-code-best-practice-工作流指南]]
