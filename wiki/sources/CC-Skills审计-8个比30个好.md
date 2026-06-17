---
title: Claude Code Skills 审计：8 个比 30 个好
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=224754...]
source_path: 印象笔记管理工具/Claude装太多，只会更废.html
tags: [claude-code, skill, audit, context-window, optimization]
---

## 一句话摘要

一个月从 31 个 skills 删到 8 个的经验——每个 skill 的 description 都在每一轮对话中占据 context window，不管有没有被触发，都在消耗 token。**高级配置是 8 个经过审计的 skills，初级配置是装 30 个然后叫它「技术栈」**。

## 核心事实

- **Context Tax**：每个 skill 的 description 会被编译进 system prompt，模型每次对话都得读完
- **Anthropic 官方建议**：skills 数量最好控制在 **8-12 个**以内
- **Description 上限**：每个 1,536 字符，1% context budget
- **两个代价**：延迟（模型读完一堆无关选项）+ 准确率（被无关选项分散注意力）
- **关键意识**：装完不用的 skill 不是「躺着不动」，它们**每轮对话都在收费**

## 相关页面

- [[products/Claude Code]]
- [[features/Skills]]
- [[sources/Everything Claude Code完整上手攻略]]
- [[sources/CC省Token四工具-RTK]]
