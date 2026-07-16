---
title: "重新想像 Excel 该有的样子：Airtable 评测"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/重新想像 Excel 该有的样子：Airtable 评测.md
tags: [印象笔记]
---

# 重新想像 Excel 该有的样子：Airtable 评测

# 重新想像 Excel 该有的样子：Airtable 评测 --- ![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/524D4D

---

# 重新想像 Excel 该有的样子：Airtable 评测

---

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/524D4D06-B1B1-4441-A2A7-DF15CC9ED0B9.jpg)

Office 的三件套：Word、Excel、PowerPoint 已经成为了从学生到职场人士都不可或缺的生产力工具。然而，这三者毕竟是软件时代的产物，像 Excel 最早的版本，Excel for Macintosh，发布于 1985 年，距今已经 31 年了。

31 年后的今天，移动设备替代了以前的桌面台式机，成为了个人数字中心，在覆盖的用户数量和单个用户的使用时间上，都是过去的 PC 所无法匹敌的。同时，网络正以我们意想不到的速度连接一切，软件从一个个孤立的个体存在，正在被改造成一个个相连接的服务……在这些变化的背后，31 岁高龄的 Excel 多多少少显得有些老旧了，这种老旧是它在诞生之初所烙下的基因，在这个时代中已经显得过时。

如果让我们重新设计 Excel，它会是什么样子？[Google Docs](https://docs.google.com) 系列只是把微软的 Office 系列从本地软件改造成了 Web Apps，这是一次技术改造，却不是一次重新设计。更恰当的类比，可能是 Quip 之于 Word，前者向我们展示了在这个时代里，重新设计的一款现代化文字编辑服务，应该是什么样的。

那么今天要介绍的 [Airtable](https://airtable.com) 之于 Excel，可能正如同 [Quip](https://quip.com) 之于 Word。

一个现代化的网络服务，应该是怎么样的？
-------------------

在具体谈 Airtable 之前，我们不妨想一想，作为一款现代化的网络服务，应该具备哪些特质？我可以列举出很多关键词：跨设备、随时可用、交互友好、开放 API、多人协同……但在这些你经常看到的宣传语背后，我们的使用方式和开发者的设计理念，究竟发生了什么变化，才催生了这些特性？

从传统软件到现代化的网络服务，背后蕴含的变革实质，其实是这三点：

#### 数据是流动的

在传统软件时代，我们认为「人 - 设备 - 软件」三者是一个不可分割的实体，数据只不过是三者不可分割的一部分。没错，那时候我们可能需要花费高昂的价格去购买一套软件的授权，安装在某一台设备上。在网络还不发达的上世纪八九十年代，个人数据在设备之间的转移都不是一件容易的事情。

而现在，许多数据已经彻底从「人 - 设备 - 软件」中分离出来，不再依附从属于具体的人、设备或者软件。得益于网络连接，数据可以在人和人之间、设备和设备之间、服务和服务之间自由流通，而这种流通性创造了许多不一样的可能。人和人之间的数据促生了协同办公，设备和设备之间的数据让一切随时随地可用，服务与服务之间的数据更是打破了传统软件的壁垒，API 的普及与标准化使得自动工作流成为可能。

#### 面向使用场景设计

传统软件的设计，很多时候并不是面向最终用户的。特别是企业级别的软件，诸如 SAP 之类的公司，肯定是面向雇主，而不是面向雇员的。相对应的，这样的设计思路下，一款软件的确可以实现某些目的，完成特定的功能，却对于使用者来说，往往最后成为了生产力的束缚。

现在的网络服务，在设计之初，就更面向普通大众的实际使用场景。你会发现这一类产品同样可以走入企业级市场，最典型的例子莫过于 Slack。实现了同样的目的，却在一定程度上替换了企业内部难用的沟通邮件平台，带来了更好的使用体验，这只有在面向使用场景设计的思路下，才得以实现。

#### 交互高于功能

打开 Word 或者 Excel，里面你常用的功能有多少？但你却不得不发现，它们在界面上很可能占据着同样的重要度，在一些操作流程上打断你，弹出让人费解的提示框……

实际上，现在大家已经越来越清楚地认识到，要让更多人使用，很多时候并非只是不断地添加功能，而是要让产品本身更容易使用，降低上手难度。这也是现在业内常说的关注用户体验，在使用过程中让人感到愉悦。

这种愉悦是多方面的，可能是保留最常用的 80% 的功能，而在功能上做减法，以减少技术上的复杂程度和用户的认知学习成本；可能是在不同的设备、不同的屏幕分辨率上，实现自动适应，改变内容的组织形态……

在接下来对 Airtable 的介绍中，希望你能带着这些思路，一起看看 Airtable 相比于 Excel，有哪些不同，多做了哪些，又少做了哪些。

认识 Airtable
-----------

在介绍 Airtable 之前，我不得不先强调：Airtable 当然不可能完全取代 Excel，在数据透视、函数处理、宏等方面，Airtable 可能永远都不会像 Excel 那么强大。但是，在很多简单的日常应用上，杀鸡焉用牛刀，Airtable 带着现代化的设计思路，反而可能是更好用的选择。

Airtable 本质是一个表格化的数据编辑工具。这里最重要的是表格化，不同于文字或幻灯片，表格着意味着数据的规整化，而在规整化的数据上，则可以孕育出无限可能。最典型的例子莫过于关系型数据库，从某种程度上来看，每一张 Excel 表格，就是一个小型的关系型数据库。在规整的数据结构上，你在少数派看到的每一篇文章、你的注册信息、网站的作者介绍，在背后其实都是一张张表格里，在不同字段下填入了相应的信息，然后通过特定的方式展现了出来。

Airtable 也是一样的道理，为了更方便说明，我们先把 Airtable 中定义的一些术语，和 Excel 做一个对应：

* **Base：**在 Airtable 中，你可以创建任意多个 Base，每一个 Base 其实就类似一个单独的 .xlsx 文件。Airtable 准备了许多默认的模板，涵盖了个人、销售、人力、任务管理等多个类别，不同的模板为你准备好了一些在使用中常用的字段和一些示例说明，方便你快速开始使用。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/AF55BC76-085D-44F5-82EF-82A5B84B08C6.jpg)

* **Tables：**每一个 Base 都可以包含多个 Tables，也就是 Excel 中下方的工作表。
* **Views：**Views 是 Airtable 所特有的一个功能，你可以把 Views 理解成一个 Table 的不同展现形态，而共享同一个 Table 的数据源。每一个 View 都可以单独记录自己的行列展示、筛选条件等等。而更高级的，记住我们所说过的表格只是规整化数据的原始形态，在这个基础上，Views 还支持以日历、表格、图集、看板的形式展现。例如，想要租房的时候，自己感兴趣的每一个房源，除了表格形式（左）外，你还可以按自己的打分，切换到以打分归类的看板形式（右）。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/BE288D91-4709-48C0-A6F5-54FA692F5D2A.jpg)

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/3418F406-3849-4D79-A313-8166DECD402C.jpg)

* **Fields 和 Records：**这两个也很好理解，Fields 相当于 Excel 中的列（Column），而 Records 则是每一条记录，相当于 Excel 中的行（Row）。不过，Airtable 中的 Fields 支持更多的数据类型和展现形式，这个我们稍后会提到。

简单来说，Airtable 中的 Base 就是一个 .xlsx 文件，里面可以有好多张 Tables（工作表），每张 Table 都由列（Fields）和行（Records）组成，而 Table 本身又可以有多个展现形式（Views），不同的 Views 使用的是同一张 Table 下的数据源。

下面，我们来看看，Airtable 中的数据从何而来，如何展现，又去往哪里。这个过程中，可能不会把 Airtable 所有的功能都面面俱到，但希望通过接下来的介绍，在你理解了 Airtable 是什么的基础上，对 Airtable 怎么用有一个初步的认识。

Airtable 中的数据从何而来
-----------------

先问问你自己，Excel 中的数据从何而来？除了你自己手动输入、复制粘贴和接收别人的文件外，Excel 中的功能是这样体现的：

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/76924FC7-A8CC-494C-AA0D-EF13EA9484C1.jpg)还记得前文里提到的，一款软件诞生之初的基因烙印吗？这可能就是最好的体现。那么，Airtable 中的数据，除了自己手工编辑外，有哪些方式填入呢？

#### 从 API 中来

Airtable 支持大量的第三方平台，通过 API 的形式互传数据。一个简单的例子，可能就是少数派之前的 [技巧文章](http://sspai.com/36100) 中，有人分享了利用豆瓣和 Airtable 的 API，通过 Workflow，将豆瓣上的书籍/影剧信息，记录到 Airtable 中。

Airtable 自建有一套完整的 [API](https://airtable.com/api)，并通过 [Zapier](https://zapier.com/zapbook/airtable/)，支持和 450 多个网站或 app 互通数据，包含 Dropbox、[Evernote](http://sspai.com/tag/%E5%8D%B0%E8%B1%A1%E7%AC%94%E8%AE%B0)、Gmail、Instagram、[奇妙清单](http://sspai.com/tag/%E5%A5%87%E5%A6%99%E6%B8%85%E5%8D%95) 等等。例如，你可以把 [Pocket](http://sspai.com/tag/Pocket) 上归档的历史文章信息同步到 Airtable 中保存，可以记录下文字、链接和摘要。对于 Pocket 这样对搜索不友好的服务，Airtable 可能更适合于查找过往的归档历史文章。又比如，Airtable 可以自动记录下你发过或收藏过的 Twitter，可以作为一种很不错的备份方式。

#### 制成表单，让别人填写

还记得面向使用场景的设计理念吗？表格只是以规整的形式记录源数据，但实际上通过这套规整的数据，可以有无数种展现形式。

结合我们之前提到的 View，Airtable 可以将一张表格以表单（Form）的形式展现。回到之前举的租房的例子，你可以制成一张房源表单信息发布到网上，让有房源的人填写相应的信息。在这里，你可以定义表单的标题和介绍，并展现哪些列（Fields）信息供他人填写，例如，我想让有房源的人告诉我租金、街道、面积等基本信息，但我自己对房源的评级、感想等字段则可以隐藏。

当你发布这份表单后，会生成一个链接，别人可以直接访问并提交表单内容，这些信息会自动记录在你的表格里。你可以访问 [这个链接](https://airtable.com/shrJR9WjfeL3hffVn) 试试。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/3F7B0FEC-4EFA-4A80-8977-56AC573C2CAF.jpg)

Airtable 中的数据如何展示
-----------------

在 Excel 中，一切表格中的数据，可以简单理解成都是基于字符的：不管是文本、数字、日期还是链接等等，其实都是一段文本字符。

而在 Airtable 中，每一列（Fields）都可以有一个特定的类型，而且这个类型出奇得丰富，除了常规的文本外，你还可以设置为附件、勾选框、单/多选框、二维码等等。例如附件类型，你可以直接上传图片，图片会以缩略图的形式直接展现。而如果是多选框，Airtable 还会以标签的形式，展现你选中的选项。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/B2BC1401-24B7-461A-B3BF-F6EE07B2F90F.jpg)另一点和 Excel 不同的是，如果你想使用 Airtable 进行单元格关联、运算等操作，也需要单独设置成相应的类型，而不是像 Excel 中那样输入等号。Airtable 目前提供了公式、汇总、计数、查询、自动序号等几种类型。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/098F744B-445C-49AA-A520-61A510E8C45F.jpg)

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/3B572994-E03A-49C4-97AC-3A401DAC53C2.jpg)

另外，Airtable 还提供了灵活的编辑方式。不想在那么窄窄的一个单元格里添加图片？你完全可以把一行（Record）展开成一个悬浮窗，可以直接编辑这一行中的所有信息。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/A1EED295-CDCE-44D5-8E9E-F9ACDADA50EF.jpg)

类似的设计思路更体现在了移动端。想想 Excel for iOS 是怎么做的？基本上就是把表格照搬到了手机上，操作起来特别麻烦，目前这个阶段，可能也就只能在手机上查看一些文件，真要想编辑，估计没人会这么折磨自己吧？

而 Airtable 则在移动端做了相应的优化，它提供的思路不是一种改良，而是真正符合设备特性的改造。每一条记录（Record）与其说是死板的表格，在移动端更像是长条形的卡片，在真正编辑时，点击任一单元格，会将整条记录展开并定位到相应的编辑位置。而且每个不同类型的字段也都对移动端做出了相应的优化，例如多选框会再弹出下拉选择，勾选框则直接使用了系统样式的开关按钮。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/7C56B94F-EA93-4801-A449-5A5B64FB1D48.jpg)

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/C0B0E1DA-5CAE-431B-BD3D-EFF5619A98E8.jpg)

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/94BD40EC-ED90-49BD-B8B2-D4BFFA1E714E.jpg)

Airtable 中的数据去往哪里
-----------------

Airtable 是一个对分享极度友好的服务，这意味着它不仅支持多人协作编辑，还支持将你的表格直接分享出去。记住，除了分享整个 Base 外，你的分享实际上是基于 Airtable 的 View 的。

还记得 Airtable 提供的多种 View 的展现形式吗？这意味着除了[表格的查看方式](https://airtable.com/shrFbRPWd6VHo8mLy/tblOOsLw48TwNQOjg)之外，还可以直接做成漂亮的[图集](https://airtable.com/shr9Wfhuz0uKXnUsN)或[看板](https://airtable.com/shrCrky6tp5JfHZYH)的形式，分享给他人。

![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/AC2BAC72-CCCA-41CC-8276-52E7298B0B4F.jpg)

* [查看表格形式>>](https://airtable.com/shrFbRPWd6VHo8mLy/tblOOsLw48TwNQOjg)
* [查看图集形式>>](https://airtable.com/shr9Wfhuz0uKXnUsN)
* [查看看板形式>>](https://airtable.com/shrCrky6tp5JfHZYH)

最棒的是，你甚至还可以把 Airtable 中的内容，直接嵌入到现有的网页，比如像下面这样：

好了，到现在你应该已经对 Airtable 有了一个基本的认识，你不妨在电脑上亲自上手试一试：[点此访问](https://airtable.com/invite/qrmMSWjM) 网页，或在手机上下载 [iOS](https://itunes.apple.com/cn/app/airtable-flexible-database/id914172636?mt=8&uo=4&at=10lJSw) 或 [Android](https://play.google.com/store/apps/details?id=com.formagrid.airtable&hl=en) 应用。

如果你有兴趣，也欢迎在评论中和我们分享你对 Airtable 的使用体验，或者有哪些陈旧的软件服务，你觉得应该被改造？

文章来源 [少数派](http://sspai.com) ，原作者 [子不语Rex](http://sspai.com/author/648292) ，转载请注明原文链接

原文可获取应用下载链接：[重新想像 Excel 该有的样子：Airtable 评测](http://sspai.com/36402)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/68BFAA07-C85D-45CB-9D85-8D697BD237D5/7E84BF5B-357B-4DF0-A914-DF257BAA543B.jpg)](http://sspai.com/36393)

---

[🌐 原始链接](http://sspai.com/36402)

[📎 在印象笔记中打开](evernote:///view/207087/s1/68f45b18-aa40-471a-89b7-de12284aa65e/68f45b18-aa40-471a-89b7-de12284aa65e/)