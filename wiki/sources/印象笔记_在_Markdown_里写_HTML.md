---
title: "在 Markdown 里写 HTML"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/在 Markdown 里写 HTML.md
tags: [印象笔记]
---

# 在 Markdown 里写 HTML

# 在 Markdown 里写 HTML --- 在 Markdown 里写 HTML ================== | 本文为付费栏目文章，您已订阅，可阅读全文 | Markdown 在科技

---

# 在 Markdown 里写 HTML

---

在 Markdown 里写 HTML
==================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

Markdown 在科技圈已经风靡很久了，但很多人一提 Markdown 就是：「再也不用 Word 了」、「轻松搞定排版」。这其实是对 Markdown 的误解，Markdown 不是为了替代 Word，也不是为了完成排版工作。

Markdown 主要的目的是为了在写作网络文章时，有一套简洁的书写方式，容易写，同时也容易读。而排版本身，并不是由 Markdown 来决定的，**Markdown 只决定内容的属性，不决定内容的样式**。比如下面这段文字：

```
# Markdown 是什么

Markdown 是一门轻量级标记语言。
```

通过 Markdown 编辑器（以 Byword 为例）预览后，是这个样子的：

![](.evernote-content/3CA4C32F-6A55-4DEF-9543-E67A5207AF80/0162DE60-3E84-46D8-B907-5921DA408DAC.jpg)

在 Byword 中预览 Markdown 语法

Markdown 语法定义了「Markdown 是什么」这一行是标题，但标题应该用什么字体、显示多大的字号、采用什么字重、居中还是左对齐，这些通通都不是由 Markdown 决定的。那为什么我们会看到上面这张图里的效果呢？

因为 Byword 会将 Markdown 语法转换成 HTML，像下面这样：

```
<h1>Markdown 是什么</h1>

<p>Markdown 是一门轻量级标记语言。</p>
```

最后再由 Byword 软件内置的 CSS 进行渲染，才得到我们看到的样子。我们平时所说的 Markdown 编辑器或者支持 Markdown 的网页编辑器（比如少数派），也就是内置了转换 Markdown 语法功能的编辑器。

也就是说，Markdown 语法最终都会变成 HTML。因此，如果我们直接在 Markdown 中插入 HTML 代码，HTML 代码就会被保留。也就是说，我们可以在 Markdown 里写 HTML 代码。

在 Markdown 中写 HTML 代码
---------------------

**Markdown 虽然基于 HTML，但不是为了取代 HTML，而是辅助 HTML。**由于 Markdown 的目的是要保持简洁，所以在功能上，它并没有 HTML 那么丰富。可以说它是 HTML 的子集，只拥有部分 HTML 的功能。

如果需要用到更丰富的功能，那么还是得借助 HTML 代码。很多 Markdown 编辑器都支持直接写 HTML 代码，比如 Byword、MWeb、MarkEditor、Day One、nvALT、Sublime Text、Ulysses 等。

注意：由于 Ulysses 采用的是自己改进过的 Markdown XL 语法，它不能对写在文中的 HTML 代码直接进行解析，而是需要在代码两边插入 `~`，或者在段首插入 `~~`，就能在预览或导出时转换成正常的 HTML 代码。

在 Markdown 里写 HTML，主要是为了展示和输出的时候有更丰富的样式，比如发布到网页上，或者导出成 PDF。自己平时写作的时候，并不需要用到这种方法，而且我也不建议过度使用 HTML，因为样式应该由网站或编辑器的 CSS 来决定。但是当你无法改变 CSS 的时候，我们就可以尝试用少量 HTML 代码来改进我们文章的排版。

需要注意的是，在 HTML 的区块元素中（比如 `<p>`、`<div>`、`<table>`、`<pre>` 等标签），是无法使用 Markdown 语法的。比如：

```
<p>这是**一句话**。</p>
```

里面的「一句话」三个字不会被加粗。而 `<span>`、`<del>` 等区段标签则可以用在 Markdown 段落中。

由于 HTML 的语法很多，我无法列出所有的使用场景，而且本文的目的也不是为了介绍 HTML 本身，所以下面我会简单举几个例子给大家参考。

### 改文字颜色

比如文章中的某一句话需要特别引起别人的注意，类似于「这个商品需凭序列号购买」这种重要信息，我们就可以把这句话改成更能吸引注意力的颜色，写成：

```
这个商品需凭<span style="color: red">序列号</span>购买。
```

显示效果就会变成这样：

这个商品需凭序列号购买。

当然红色比较夸张，你可以挑一个稍微顺眼的颜色，并辅以加粗效果。

### 改背景颜色

我们 Power+ 每周的读者反馈中，会包含有编辑写的内容和读者反馈的内容，而且有时候读者反馈的内容量也比较长，在少数派默认的引用样式下效果不佳。所以我们为了区分编辑内容和读者内容，采用了增加背景色的效果。具体写成：

```
<div style="background-color: #D8EAF2; color: #497091; margin-bottom: 10px; padding: 2% 3% 2% 3%; border-radius: 6px;">  
读者反馈内容。  
</div>
```

显示效果如下：

读者反馈内容。

### 强行居中

很多编辑器的默认标题样式都是左对齐，但有时候我会更偏向居中的对齐方式，尤其是在标题底下紧接着图片的时候。比如之前我们在制作 Checked 播客的微博长图时，最顶部是大标题，紧接着往下就是 Logo 图片。

![](.evernote-content/3CA4C32F-6A55-4DEF-9543-E67A5207AF80/7E45CCF3-DA39-4D97-8F40-70DD92CC3053.jpg)

居中的大标题

考虑到有时候标题会比较短，如果和正文左对齐的话，会显得图片有些失衡，所以我们就直接将标题写成：

```
<center><h1>#41: 专访顾伶磊：视觉障碍者如何无障碍地「看」世界 </h1></center>
```

实现了标题居中，对齐了接下来的 Logo 图。

### 插入 Font Awesome 图标

少数派作者 @契丹神童 也曾写过一篇文章介绍他如何用 Font Awesome 图标来丰富 Markdown 文档里的内容，达到如下图的效果：

![](.evernote-content/3CA4C32F-6A55-4DEF-9543-E67A5207AF80/1D6DC8B4-E5FB-4611-AF11-489A435BA98C.gif)

Font Awesome 图标

原理也是将 HTML 代码插入 Markdown 文中，稍微不同的是需要在文档任意位置插入一段 `<head>` 元素，具体方法大家可以 [点此](https://sspai.com/post/45217) 看原文介绍。

总结
--

相信看完此文，你会更加理解 Markdown 和 HTML 之间的关系，它们不是互斥的敌人，而是相辅相成的好朋友。写作时用 Markdown，简洁的标注可以让我们专注在内容本身。发布排版时用 HTML，有更强大灵活的样式支持。像 WordPress 这种提供搭建博客的网站，还会允许你将 HTML 转换为富文本，调整起来也更直观。

其实 Markdown 的排版能力很弱，但这正是它的优点。Markdown 本来就不是为了替代任何排版工具而存在的，它的目的就是用少量最常用的标记符号，比如标题、加粗、列表等，让我们在写作过程中实现最基础的排版需求，不用担心文章最终的呈现效果。

另外 Markdown 的源文件也很易读，大部分的标记符号都很简单，而且看起来也直观，用 Markdown 创始人 John Gruber 的原话说就是「Markdown 的列表看起来像是，嗯，列表。」

易写与易读，构成了 Markdown 的两大特点，这也正是广大被 HTML 折磨过的程序员们喜欢 Markdown 的原因。

[#文字编辑](https://sspai.com/tag/%E6%96%87%E5%AD%97%E7%BC%96%E8%BE%91)

---

[🌐 原始链接](https://sspai.com/post/45748)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d65dfb97-c25d-479b-916a-141e4d5bd7f4/d65dfb97-c25d-479b-916a-141e4d5bd7f4/)