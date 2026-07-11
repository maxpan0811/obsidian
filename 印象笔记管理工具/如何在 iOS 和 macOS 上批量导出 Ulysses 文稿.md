# 如何在 iOS 和 macOS 上批量导出 Ulysses 文稿

---

Ulysses 转变为订阅制之后口碑反转，其中最为人不忿的是 [Ulysses 不能导出其中的文档](https://sspai.com/post/40365)，乃至出现了「作者用它产生的东西竟然不能带走！」这样的指责。

其实，Ulysses 完全是可以导出纯文本文件的，[官方推特](https://twitter.com/ulyssesapp/status/761110617281302530)在 2016 年就回答过这个问题：

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/1322D6E7-7C91-4F77-B0F7-ECFDCE645EDC.png)Ulysses 的推文

会出现 Ulysses 不能批量导出文本的误会是因为 Ulysses 本身并没有直接提供批量导出功能。但是我们可以通过外部文件夹来实现批量导出功能。

它的**原理**是：Ulysses 同时使用内置文稿库和外置文件夹**两种方式存储用户的文稿**，Ulysses 内置文稿库使用的是自己的特殊格式 `.ulysses`，而外置文件夹则使用的是 `.md` 格式。所以我们需要做的是把文稿迁移到外置文件夹即可，操作非常简单。

下面，我们来看在 macOS 和 iOS 上分别如何导出 Ulysses 文档。

在 macOS 上导出文稿
-------------

在 macOS 上可以在左边栏选择添加外置文件夹。

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/84858928-D63B-4049-952B-3FE434EC7EB5.jpg)新建外置文件夹

￼之后选择想要导出的文件夹并拖拽到外置文件夹。Ulysses 会弹出一个提示，选择右侧的「继续」。

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/8B9F2908-41F0-43CC-A1C8-4596B95CB9A4.jpg)Ulysses 弹出的提示

这样导出就完成了。所有的文稿都会以标准的 Markdown 格式被导出为一个个 `.md` 文件。

在 iOS 上导出文稿
-----------

在 iOS 上导出文稿限制则是更多一些。首先点击在左边栏右下角的「管理」处，选择添加 Dropbox 文件夹。

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/C3EEDAAD-F35F-4D11-A884-9E2CBD052394.jpg)新建外置文件夹

之后需要对于每一个主文件夹左划选择「Details」，并把父文件夹改为 Dropbox 的文件夹。

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/CC129957-35A8-41A3-B3AD-74C9634CF5A2.jpg)把文稿移动到外置文件夹

Ulysses 会弹出一个提示询问是否继续，选择「继续」。然后会有一个弹框问你是「移动」还是「复制」，这里选择「复制」更好，可以保留内置库中的原文稿。

![](.evernote-content/E1B0EF3C-5656-4AD5-AFE8-688EB134CDA6/69CD937E-5311-45F4-8CF4-660F38D96CBB.jpg)Ulysses 弹出的提示

**相关阅读：**

* 如果你想换别的 Markdown 编辑器，可以看看这篇文章：《[想试试其它写作工具？11 款好用的 Markdown 编辑器推荐](https://sspai.com/post/40358)》
* 我还写了一篇使用 Workflow 做到批量导出 Ulysses 的文章，这篇文章更多是一种使用 Workflow 的尝试，感兴趣的话可以读一下：《[使用 Workflow 批量导出 Ulysses 文稿](https://sspai.com/post/40417)》

---

[🌐 原始链接](https://sspai.com/post/40479)

[📎 在印象笔记中打开](evernote:///view/207087/s1/71876887-fcf6-44a1-8233-382632c55688/71876887-fcf6-44a1-8233-382632c55688/)