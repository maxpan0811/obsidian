---
title: "Redis之父下场，给DeepSeek V4单独造了一台推理引擎"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Redis之父下场，给DeepSeek V4单独造了一台推理引擎.md
tags: [印象笔记]
---


来源：[打开原文](https://mp.weixin.qq.com/s/9X0bcfUGZYxoXuQwt89zkQ)

henry 发自 凹非寺量子位 | 公众号 QbitAI

DeepSeek V4，已经开始逼着海外开发者为它修专属高速公路了。

发布才两周，开源圈里，第一批V4原生基础设施已经冒了出来。

而且，不是那种在现有框架上套一层壳的“小修小补”。

不是通用GGUF加载器；不是llama.cpp的wrapper；甚至压根不支持别的模型。

它只干一件事：

把DeepSeek V4 Flash，在Mac上跑到极致。

![](.evernote-content/1BC9BAC6-A8E7-4776-9098-C50DA8E8F659/61AD01B2-BB54-46ED-ABFB-54B5C9FE6655.png)

这条“专属高速公路”，叫ds4.c。而把修出来的人，分量有点吓人——

Salvatore Sanfilippo，程序员圈更熟悉他的另一个名字：antirez。

他一手创造了 Redis（GitHub 7.4 万 Star），并亲自主导这个全球最流行

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->