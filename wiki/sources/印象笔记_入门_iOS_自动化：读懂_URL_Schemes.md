---
title: "入门 iOS 自动化：读懂 URL Schemes"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/入门 iOS 自动化：读懂 URL Schemes.md
tags: [印象笔记]
---


之前我写过一篇《[URL Schemes 使用详解](https://sspai.com/post/31500)》，其中把 URL Schemes 从功能上分为了 4 种：

1. **基础 URL Schemes**：用于启动应用，比如：<drafts4://>；
2. **复杂 URL Schemes**：用于直接打开应用的具体功能，比如：<drafts4://dictate>；
3. **变形 URL Schemes**：用于输入内容，含有第三方应用的特殊语法，比如：在 Launch Center Pro 里用这一条 `drafts4://create?text=[prompt]`；
4. **x-callback-URL：**前面的 URL Schemes 只能执行一个动作，而 x-callback-URL 可以根据根据前一段 URL Schemes 的执行情况决定进一步的行动。

作为补充，在这篇文章，我来介绍一下 URL Schemes 正式的读法。包括每个部分是什么、符号都是什么意思，以及阅读文档时该从哪些地方入手，注意哪些细节。

订阅 [Power+](http://

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->