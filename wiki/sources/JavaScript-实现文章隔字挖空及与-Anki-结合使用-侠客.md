---
title: JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客.md
tags: [印象笔记]
updated: 2026-06-27
---


title: "JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客"
source: evernote
type: note
export_date: 2026-06-24
guid: 1d6a8bfb-26c0-4ae5-afd6-b9e0defd10a1
---

# JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客

# JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客

好久没写博客了，好开心。还是在自己的博客写文章更舒服。

不知不觉已经过去这么久了，我即将成为一名大二的学生，哈哈哈哈哈哈哈哈容我先笑一会儿。想想也很神奇，我竟然会去学 “数学与应用数学”。好久没写过代码了，其实我也没写过什么像样的代码。

### 文章隔字挖空

还是称其为 “隔字替换” 吧，就是每隔一个单词，把后面的单词替换为一个小方块，把标点符号留着。

我先实现了一个段落的隔字替换。html 示例像这样：

```
<p id="first">Our vicar is always raising money for one caus

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->