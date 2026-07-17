---
title: 本地小模型的Claude Code来了，拆解它的完整 Harness！
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/本地小模型的Claude Code来了，拆解它的完整 Harness！.md
tags: [evernote, impression, yinxiang]
---


来源：[打开原文](https://mp.weixin.qq.com/s/iiTmgbtrYHMMjQ7dn7CDrg)

Datawhale干货   
  
作者：陈思州，Datawhale 成员

最近 Agent 圈一直在讨论 Harness 和 Loop。

Claude Code 之父 Boris Cherny 在访谈里提到，他现在不再只是手动提示 Claude，而是让一堆 loops 持续运行；这些 loops 会去提示 Claude，并判断下一步该做什么。他的工作，正在变成"写循环"。

OpenClaw 之父 Peter Steinberger 也表达过类似观点：未来使用编程 Agent，不应该只是给 Agent 写 prompt，而是设计一套循环机制，让这些循环去提示 Agent、观察结果、决定下一步。

在过去，Prompt Engineering 关注的是：这一轮怎么提示模型。Loop Engineering 关注的是：模型如何一轮轮观察、行动、接收反馈。Harness Engineering 关注的是：这些循环运行在什么系统里，如何长期稳定、可控、低成本地工作。

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->