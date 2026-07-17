---
title: 谷歌Gemini 的新升级简直疯狂！
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/谷歌Gemini 的新升级简直疯狂！.md
tags: [evernote, impression, yinxiang]
---


我打开新版Gemini的那一刻，第一反应是："是不是页面加载坏了？"

按下回车，回答几乎是瞬间出现的。**整整快了3倍**，没有夸张。

我连续一周把Google这次放出的5个更新一个个测过去——速度、NotebookLM、API、Webhook、还有AI上电视——越测越觉得，这次Google根本不是在补功能，**它在悄悄改写AI产品的底层规则**。

今天把我踩过的每一个细节，包括那些让我"WTF"的瞬间，全部讲透。

![](.evernote-content/E0665EFC-911C-4A3D-9D45-E816CF6C066C/495E1FB9-AA20-4EAC-8A26-3932B514D7FD.png)

Gemini 4速度暴涨3倍，我打开页面以为加载坏了
--------------------------

这次升级背后有个技术词叫"多Token预测"（Multi-Token Prediction）。听起来玄，原理超简单。

**老AI是这样工作的**：选一个词，再选下一个词，再选下一个词……一个一个吐字，慢得像挤牙膏。

**新Gemini不一样**：它能同时

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->