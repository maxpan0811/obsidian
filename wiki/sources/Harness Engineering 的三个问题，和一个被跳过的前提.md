---
title: Harness Engineering 的三个问题，和一个被跳过的前提
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Harness Engineering 的三个问题，和一个被跳过的前提.md
tags: [evernote, impression, yinxiang]
---


2026 年第一季度，OpenAI、Cursor、Anthropic 各发了一篇关于 AI 写代码的文章。技术圈立刻沸腾，所有人都开始讨论 harness engineering。

然后一片混乱。

有人说它是"让 AI 工具用得更顺"，有人说是"多个 AI agent 协作"，有人画了一堆方框和箭头说这是"agent 编排架构"。三篇文章，三种解读，三套词汇，讨论同一件事好像没有一个人在讨论同一件事。

这篇文章的起点只有一个问题，harness engineering 到底在说什么。

三家公司在解三道不同的题
============

混乱的根源很简单。三家公司用了相近的词，但实际上在解三个完全不同的工程问题。

OpenAI 解的是环境问题。他们有一个三人团队，五个月合并了约 1500 个 PR，折算下来每人每天 3.5 个。这不是靠写代码快，而是靠搭了一套让 AI 能可靠工作的基础设施——完整的文档体系、架构约束、自动化测试、可观测性工具。他们得出一个结论，agent 看不见的知识等于不存在，所以所有知识都得推进 repo，用 markdown，用结构化文档，不能留在 S

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->