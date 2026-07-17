---
title: "如何在 iOS 和 macOS 上批量导出 Ulysses 文稿"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在 iOS 和 macOS 上批量导出 Ulysses 文稿.md
tags: [印象笔记]
---


Ulysses 转变为订阅制之后口碑反转，其中最为人不忿的是 [Ulysses 不能导出其中的文档](https://sspai.com/post/40365)，乃至出现了「作者用它产生的东西竟然不能带走！」这样的指责。

其实，Ulysses 完全是可以导出纯文本文件的，[官方推特](https://twitter.com/ulyssesapp/status/761110617281302530)在 2016 年就回答过这个问题：

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/1322D6E7-7C91-4F77-B0F7-ECFDCE645EDC.png)Ulysses 的推文

会出现 Ulysses 不能批量导出文本的误会是因为 Ulysses 本身并没有直接提供批量导出功能。但是我们可以通过外部文件夹来实现批量导出功能。

它的**原理**是：Ulysses 同时使用内置文稿库和外置文件夹**两种方式存储用户的文稿**，Ulysses 内置文稿库使用的是自己的特殊格式 `.ulysses`，而外置文件夹

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->