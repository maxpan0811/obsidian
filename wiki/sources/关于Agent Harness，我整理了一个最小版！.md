---
title: 关于Agent Harness，我整理了一个最小版！
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/关于Agent Harness，我整理了一个最小版！.md
tags: [evernote, impression, yinxiang]
---


关于Agent Harness，我整理了一个最小版！
==========================

Original陈思州Datawhale

Datawhale干货   ******作者：陈思州，Datawhale成员******
============================================

前面讲 Agent 评测时，我提到：评测 Agent 不能只看最终答案，还要看它用了什么工具、拿到了什么结果、有没有按任务要求完成。那这些东西要怎么稳定记录下来？这就需要一个 harness。

现在有一个观点是 Agent = model + harness；

我会把 harness 理解成：把 Agentic model 放进一个可运行、可记录、可评分的小环境里。它不一定一开始就很复杂，只要能把任务、工具、执行过程和评分结果串起来，就已经很有价值。

这篇按 4 个问题梳理：1. 一个最 mini 的 harness 解决什么问题？2. 它最少需要哪些模块？3. 一个 eval case 可以怎么写？4.公开资料里有哪些参考？

一个最 mini 的

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->