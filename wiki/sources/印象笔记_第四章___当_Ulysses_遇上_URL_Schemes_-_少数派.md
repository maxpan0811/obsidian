---
title: "第四章 _ 当 Ulysses 遇上 URL Schemes - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/第四章 _ 当 Ulysses 遇上 URL Schemes - 少数派.md
tags: [印象笔记]
---


初探 Ulysses 中的 URL Schemes
=========================

有的应用所提供的 URL Schemes，根据功能不同语句的格式也有所不同。而在 Ulysses 中使用的 URL Schemes，统一按照下列的格式书写：

```
ulysses://x-callback-url/[action]?[x-callback parameters]&[parameters]
```

`ulysses://` 不必多说，自然是 URL Scheme 中的指明语句所属应用的部分。

看到句中`x-callback-url`，这意味着 Ulysses 支持在 URL Schemes 中使用 [x-callback-urls](http://x-callback-url.com/)。支持 x-callback-urls 意味着我们可以实现一些更复杂的操作，例如在应用间跳转，将多个动作串联起来。

而 Ulysses 支持 x-callback-urls 的目的不仅如此。x-callback-urls 的另一个好处，就是提供一种**标准化的 URL Sch

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->