---
title: "Workflow：Google Fonts 字体下载 & iOS 字体安装和使用 _ Matrix 精选 - 少数派 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Workflow：Google Fonts 字体下载 & iOS 字体安装和使用 _ Matrix 精选 - 少数派 2.md
tags: [evernote, impression, yinxiang]
---

# Workflow：Google Fonts 字体下载 & iOS 字体安装和使用 | Matrix 精选 - 少数派

---

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/599F6BE9-9772-4976-998A-8B7855E792D8.jpg)

Workflow：Google Fonts 字体下载 & iOS 字体安装和使用 | Matrix 精选
====================================================

[![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/1947AC09-BFAA-4566-99B6-8E9707461265.png)](https://sspai.com/user/701048)

#### [creampie](https://sspai.com/user/701048)

2016年12月08日

23 [11](#)

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/CC3FADE5-412D-426C-BFD1-7ACFDC3F4779.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友 [参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章对标题和排版略作修改，[原文链接](http://matrix.sspai.com/p/d81ed7e0)。

---

前言
--

iOS 系统自 7.0 版本起便支持了字体文件的安装，安装后的字体将以配置描述文件的形式存储在系统中，以便文档编辑软件如 Pages、Microsoft Word 等进行调用，制作精美的文档。

用户可以通过「设置 > 通用 > 描述文件」访问它们并查阅删除：

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/9C43ECEE-9F57-460F-9F86-74DA57B0A01A.jpg)

对于字体的安装，App Store 中有专门的应用可以安装字体，比如 [AnyFont](https://itunes.apple.com/cn/app/anyfont/id821560738?mt=8)，不过需要花费 12 元购买。

而对于 Workflow 用户来说，这 12 元无非只是两个 Workflow 的事情，并且自由度更高。

Google Fonts
------------

在安装字体文件前，我们自然需要先获取字体文件，准确地说是获取可以**合法使用**的字体文件。那么像 [Google Fonts](https://fonts.google.com/) 这样拥有 800 多种字体，且都是可以自由使用的开源字体的网站，自然是我首先考虑的对象。

Google 很慷慨地提供了桌面版网站字体文件的下载途径。类似于在淘宝、Amazon 购物一样，用户往底部的小抽屉中添加心仪的字体后即可单击右上角图标打包下载。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/DDA98C3F-3902-4ADE-A4EE-2474F937A7E5.jpg)

不过在手机版网页中，该下载按钮 Google 并未提供，仅提供了将 Google 字体嵌入网页的途径。

自然，在 Workflow 面前这不是什么大不了的问题。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/4FEE72C9-5730-4151-999C-B313753328D9.png)

点击下载我制作的 [**Google Fonts Downloader**](https://workflow.is/workflows/d6c7ecb08620470fb9d47f60a238a25c)，

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/45A31701-F7FD-4816-94D1-F1A02BA899C7.png)

和 [**Install Font**](https://workflow.is/workflows/517c7b7a9a154f3ba1063fe760f2c84e)。

### Google Fonts Downloader 的使用

像在桌面端使用 Google Fonts 一样，移动端同样贴心地在底部提供了一个小抽屉供你挑选字体，点击页面上的「+」符号即可添加：

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/C9D15900-7895-436E-B1FC-246AC80FCF38.jpg)

小抽屉会在 Google Fonts 的底部出现，显示你选中的字体。

最贴心的是 Google Fonts 的后台脚本会自动把你选择的字体的名称添加到 URL 的尾部，通过正则表达式即可提取。这也方便了我制作 Google Fonts Downloader。

使用非常简单。在选完想下载的字体后，点击浏览器的分享按钮调用 Workflow 运行 Google Fonts Downloader，待下载完后将压缩包文件保存至任意文件管理应用。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/21F3D4FF-2AF7-4DBC-AD91-4C32E5541183.jpg)

使用 Install Font 安装字体
--------------------

### Install Font 的原理

**首先必须声明，这个 Workflow是我从某国外大神的成果修改而来的（[大神的Twitter](https://twitter.com/zwaldowski?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)）。**

不过这当然并不妨碍我去理解并修改这个 Workflow 以适应我的需要，以及说明它的原理。

其实原理非常简单，在苹果的 [开发者文档](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html) 中可以找到详尽的说明。配置描述文件（Configuration Profile）本质是一个 XML 文档，它可以在用户需要配置大量机器时派上用场，只要根据苹果的规定往里面填写相应的键值并导入机器即可。这些键值都可以在文档中找到说明。

从文档中可知，字体的描述文件主要有三个关键的键值需要生成：

1. <Name>：字体的名称，仅为了便于用户识别，可以是任意值；
2. <Font>：字体的数据。将 .ttf 或 .otf 字体文件进行 Base64 编码后填入即可；
3. <PayloadUUID>：即通用唯一识别码，系统以此判断配置文件的唯一性。若出现两个拥有相同 UUID 的配置文件，先导入的会被覆盖掉。

其中前两者的生成非常简单，分别对字体文件使用 **Get Name**和 **Base64 Encode**动作即可。第三者的生成稍微麻烦点，具体原理的可以参考 UUID 的相关文档，本 Workflow 中使用的是 UUID v5，基于字体文件的 SHA1 哈希值产生，这里不细说。

以上是生成配置描述文件的核心部分，将它们填入苹果提供的模板后，我们需要将其导入系统。本 Workflow 应用的是生成配置文件的 **Data URI**，并使用 **Open URLs**动作打开。**Data URI**的相关信息可在我的首篇文章 [技巧：Workflow的备份、恢复、导出、导入](https://sspai.com/p/d7e97000) 中找到。

### Install Font 的使用

在使用 Google Fonts Downloader 下载完字体压缩包并保存后，解压并对字体文件调用 **Run Workflow >**Install Font（这里我使用的文件管理器是 [Documents by Readdle](https://sspai.com/tag/Documents%20by%20Readdle))。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/1E1690B3-0399-4AF6-BBE9-E3792AFA112E.jpg)

随后 Workflow 会迅速生成配置描述文件并打开，系统将跳转至安装描述文件的页面，一步步的点安装、输入机器的解锁密码即可，不用理会未签名的警告。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/3631CF7C-BF1F-4911-831D-3B0F07F24EFC.jpg)

如此，这个字体文件就成功地安装在了你的机器上。

### 功能强化

不过当你打开我的 Install Font后，你会发现有许多看似多余的动作。

这是因为在实际使用过程中，我发现许多的字体是一整个字体家族（Font Family），也就是说含有一系列的字体。比如 Android 的系统字体 [Roboto](https://fonts.google.com/specimen/Roboto)。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/37D5C7D9-23B2-487F-BDF0-C35D324BCF44.jpg)

该 Font Family 含有 12 种风格（Style），下载下来的压缩包里有 12 个字体文件！如果要依次点击全部安装的话，工作量显然是很繁重的。

因此，最终我对 Install Font 做了一个升级，可以同时处理单个字体文件或含多个字体文件的压缩包。

使用时，首先将 Font Family 中的所有字体文件打包成 zip 压缩包，并对压缩包调用 Install Font。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/BED4E9DE-2905-4D60-A163-E802B6C9ED0E.jpg)

*这里请注意，由于 Workflow目前不能解析压缩包中的文件夹，请如图所示直接对文件打包（可以连同其它文件如文本一起打包，本 Workflow 内置了过滤动作过滤字体文件）。*

升级后的 [Install Font](https://workflow.is/workflows/517c7b7a9a154f3ba1063fe760f2c84e) 利用了 **Wait to Return**动作。在安装完一个字体文件后，请通过多任务界面返回调用 Workflow 的应用，Workflow 将继续迅速生成下一个配置文件并再次跳转至下一个字体的安装界面。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/1FBDB9FD-8F7D-4CB5-891B-2220467E7772.jpg)

如此循环往复，即使是有 12 个 Style 的 Roboto 字体家族，也可以迅速装完。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/1741705B-6921-4498-ABD1-E2DC3446360A.jpg)

字体的使用
-----

在安装完字体后，便可以重启 Microsoft Word 等文档应用，然后调用了：

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/1AFAC629-D1D4-4D4D-AF72-0CF203730506.png)

### 我的使用方式

然而我并不是一个移动端的 Word 用户。Word 也许对 iPad 使用者来说足够好用，毕竟屏幕大，操作空间大。而在 iPhone 上使用 Word、Pages 等毕竟有点局促。

而我之所以有动力制作出这两个动作的原因是，我同样可以在 Workflow 中调用字体！

本人现实中的工作是工程狮，查阅材料的性能是家常便饭，所以我制作了一个较为复杂的 Workflow 用于快速从数据库获取材料信息并排版生成 PDF 报表，便于随时随地查看和归档，以及后续的模拟工作。

这个 Worflow 我上传到了官方的 Workflow Gallery 并通过审核上架了，可以搜索下载到（虽然不是我目前自用的完全体）。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/77AA02AC-5ACE-47E9-A714-54338AF6AFA1.jpg)

由于我的 PDF 是通过先在 Workflow 中制作 HTML 文件从而生成的，我自然可以通过嵌入 CSS 样式来对 HTML 元素进行排版和应用样式。那么选择一种美观大气的字体是绝对能提高阅览体验的。

我最终选择了紧凑简洁美观的无衬线字体 [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed)。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/DDF53575-64B0-4327-9745-86A8CA189698.jpg)

在描述文件页面查看到字体的名称后，我便可以将其填入 CSS 的 font-family 属性进行应用。在此，我在自己的 Worflow 开头插入了一个 Dictionary 用于快速更改配置，包括切换字体。

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/48DE8F1B-5604-4F84-A887-9D343ABF6018.jpg)

由此生成的、应用了 [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed) 字体的报表阅读体验如下：

![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/1DA0E989-A1ED-4193-8F6B-5EB1B9F28EFB.png)

如上所示，安装了字体后，Workflow 就可以通过 CSS 调用本地字体了！然后对 HTML 文件使用 **Make Rich Text from HTML**动作即可进一步生成美观的文档。如果使用系统自带的字体，文档的排版对我而言看起来会比较糟糕，即使使用 **Helvetica**也不例外。

结语
--

当然，本文只是 Workflow 与 [配置描述文件](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html) 结合使用的一例，不足为道。

相信不远的将来能有更有趣的用法。

---

[![](.evernote-content/9AE8BAC4-6B99-46DC-911F-57042020C299/18B7FC9F-9085-4784-9DAF-43DA074E38B2.jpg)](https://sspai.com/tag/workflow)[继续阅读](https://sspai.com/tag/workflow) 中文互联网内最好的 Workflow 系列教程 >

[#Workflow](https://sspai.com/tag/Workflow)[#iOS](https://sspai.com/tag/iOS)[#技巧](https://sspai.com/tag/%E6%8A%80%E5%B7%A7)[#教程](https://sspai.com/tag/%E6%95%99%E7%A8%8B)

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

---

[🌐 原始链接](https://sspai.com/post/36457)

[📎 在印象笔记中打开](evernote:///view/207087/s1/113f8965-9f22-4e77-bcd1-ec873ee26dd8/113f8965-9f22-4e77-bcd1-ec873ee26dd8/)
