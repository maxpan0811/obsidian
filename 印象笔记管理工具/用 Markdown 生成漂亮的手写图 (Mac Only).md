---
tags: [★★★★★]
---

# 用 Markdown 生成漂亮的手写图 (Mac Only)

---

用 Markdown 生成漂亮的手写图 (Mac Only)
==============================

2018年12月28日

[![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/CD7F4EDD-7CF0-4E7A-9DA2-6D9542E7AEE6)](https://sspai.com/user/723660)

#### [Hepo](https://sspai.com/user/723660)

之前我在 [这篇文章](https://sspai.com/post/47823) 中看到了聪明工作课的大纲图片，样式比较美观，我就想能不能拆出 MarkEditor 中 Text to Image 这项功能，制作一个通用的工具，让更多的人都能通过这个工具轻松做出同样板式甚至更加美观的图片，而不需要麻烦设计师多次进行修改。

于是，我做了 Text2Image 这款 macOS 上的小工具，它能够为你将 Markdown 语法文本自动进行图文排版，生成样式美观的图片。

![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/06B7D206-9FCD-4BBC-A4CB-CA2F289B6992.png)

通过 Text2Image 自动生成的图片

用 Markdown 语法对文字进行排版
--------------------

就如同 Markdown 语法需要通过 CSS 进行样式渲染，Text2Image 需要对应的模板才能对文字进行渲染，完成指定样式的图文排版。

Text2Image 的模板语法采用的是 [Jinja2](http://jinja.pocoo.org/docs/)，软件的排版引擎还会对 Markdown 语法解析后的结果再做分解，比如，即使你将下图中文本与插图语法进行上下次序的调整，也不会影响我们最后得到的结果。

![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/16A69688-E0DF-41B6-A329-DB8512599A38.png)

右图为渲染之后得到的结果

Text2Image 中的模版
---------------

### 由少数派的聪明工作课受到启发

在少数派的 [《告别低效，人人必备的聪明工作法》](https://study.163.com/course/introduction.htm?courseId=1006216001&share=2&shareId=400000000627114) 课程介绍里，页尾的课程大纲图文排版令人印象深刻，这也启发了我去开发 Text2Image 这款工具，并实现了大纲图片的图文排版样式。

你可以在 Text2Image 中找到名为「SSPAI Chapter」的模版并应用它，之后在软件的输入框中填写必要的文字信息，即可生成下图样式的图片。

![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/29A47F38-EADB-4DF2-AA3D-19F927EE016A.png)

左图为 Markdown 文本，右图为渲染后得到的结果

在 Text2Image 中，模板就是一个 HTML 文件，我们还可以在 HTML 的 header 部分调整生成器的界面，界面参数中的 Title、Signature 等元素也都可以通过输入 HTML 代码进行定制。有了这套模版，之后如果有文字改动或者需要复用这套样式的情况，就不用麻烦设计师重新出图了。

需要注意的是，当你用 Text2Image 将自己的设计写成固定模板的时候，也需要考虑**书写体验、效率、设计效果**等多方面因素的融合。比如「SSPAI Chapter」这个模板为了配合最终图片的排版，在对书写体验基本没影响的前提下，巧妙地在二级标题 (H2) 内增加了 `B` 的 HTML 标记，来实现最终图片修饰性的排版。

### 制作逼真的手写体

在 [《决定「下一步行动」，真正让待办清单为你所用》](https://sspai.com/post/51972) 这篇文章里有几张非常逼真的手写体插图，让这篇文章几乎成为有史以来最「跑偏」的评论聚集地，读者几乎都在问: 这个配图是怎么做到的？

我也将其做成了一个模板，你可以在 Text2Image 中找到名为「CN Handwrite」的模版并使用它。

![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/759EE9B5-279D-48F7-A558-E41739CE8D21.png)

右图为「CN Handwrite」渲染出的图片样式

这里分享一个小的技巧，就是巧用 Markdown 中 `pre` 的语法，这样可以保证空格的效果。这套模板用的是纯 CSS 规则生成，包括纸张的网格以及图片背景中的噪点效果，后者是通过 [NoisePNG](http://noisepng.com/) 直接生成作为复合背景实现的。

由于苹果自己的 Webkit (可以简单理解为 Safari) 并不支持 `filter: blur(0.35px)` 这种小于 1 像素的模糊效果，而恰恰是这种微小而又不会产生实质上模糊的效果会让最终生成的图片更逼真一些。这让我灵感一现，采用了一种可以被前端工程师「挂城墙」的做法来模拟手写劲道产生的细微压痕：将 HTML 内的 DOM 元素视为类似图层的逻辑，复制、叠加一个，然后再进行 (高斯) 模糊，类似传统意义上 Photoshop 最简单的「磨皮」手法。

![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/B7232AA4-E93E-4358-A62A-E8EDB04B06EE.jpg)

放大后看一看，「手写」效果还是蛮逼真的…

### 方便的导出功能

用 Text2Image 导出图片也很方便，软件支持三种形式的导出：

1. 另存为图片文件
2. 复制图片到粘贴板中
3. 直接发送到微信中

如果你需要使用发送到微信的功能，你需要先在 macOS 系统系统偏好设置的扩展设置内启用微信的共享菜单选项。

![](.evernote-content/E9992823-AC87-48FA-9153-9492102D1F81/3DFB945C-2FE9-4101-A58E-C6FE5556476F.png)

勾选微信的共享菜单选项

最后
--

Text2Image 是从 MarkEditor for Mac 中独立出来的免费 App，在 MarkEditor 中这一功能叫做 Text to Image，是 Pro 版本中的一个小功能。当然，从书写体验和文本管理的角度来说，MarkEditor 内的 Text to Image 功能体验会好不少。

除了 Text2Image，我还做了 Markdow 转脑图工具 MarkRemap、支持图床的图片素材管理工具 ImageBox 等小工具，它们都是从 MarkEditor for Mac 中拆分出来的免费工具，你可以在 [YiGe.app](https://yige.app/) 下载它们。

最后，感谢带给我灵感的少数派设计师嘉君。

---

**编注：**MarkEditor for Mac 2.0 也已上架少数派正版软件商城，除了本文提到的 Text2Image、ImageBox 等功能，MarkEditor 还支持一键同步文章至博客、少数派等平台，并拥有微信公众号样式排版、幻灯片演示以及 MarkEditor 云服务等更多高级功能。

如果你感兴趣，可以阅读由 sainho 写作的[《MarkEditor 2.0：让文字变成你想要的样子》](https://sspai.com/post/47616)一文，了解更多有关 MarkEditor 的功能和用法，或者在少数派正版软件商城直接 [购买 MarkEditor](https://sspai.com/item/43)。

---

[🌐 原始链接](https://sspai.com/post/52190)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f07b2c01-7608-4a0c-a2bd-c2a8f4df8146/f07b2c01-7608-4a0c-a2bd-c2a8f4df8146/)