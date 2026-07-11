# App+1 | 体验最接近「原生」，免费开源的老牌 RSS 阅读器：NetNewsWire - 少数派

---

体验最接近「原生」，免费开源的老牌 RSS 阅读器：NetNewsWire
=====================================

![](.evernote-content/5F217C72-0CA5-49DB-9819-D06F6F9438A1/37AD3FCA-C785-497E-9359-B596F307DD7C)

App+1 | 体验最接近「原生」，免费开源的老牌 RSS 阅读器：NetNewsWire

RSS 并没有随着 2013 年关闭的 Google Reader 逐渐消失，事实上，至今还有很多人在继续使用，也有很多产品在持续迭代。例如，较为熟知的 Feedly、Inoreader 等 RSS 抓取服务，以及 [Reeder](https://sspai.com/post/54241)、[Unread](https://sspai.com/post/59130) 等 RSS 客户端。

今天介绍的 NetNewsWire 是一款支持 Mac 和 iOS 双平台的 RSS 客户端，其首发于 2002 年。去年 8 月，NetNewsWire 5 正式发布，而今年 3 月首次支持 iOS 和 iPadOS。

设计
--

NetNewsWire 的 Mac 和 iOS 应用均使用 Swift 开发，是一款彻底的原生应用。开发者毫不谦虚地说，NetNewsWire 应该是用 Swift 编写的最大的开源项目之一，几乎是第一。同时，NetNewsWire 使用 [MIT License](https://github.com/Ranchero-Software/NetNewsWire/blob/master/LICENSE) 开源了 [整个项目](https://github.com/Ranchero-Software/NetNewsWire)，供所有 Swift 开发者学习使用。

NetNewsWire 整体使用了简洁明晰 Apple UI 设计语言，同时应用支持 Dark Mode 暗黑模式。

![](.evernote-content/5F217C72-0CA5-49DB-9819-D06F6F9438A1/378308BD-75F3-48B4-8CC1-847B6D279793.png)

同时，其 iOS 应用和 Mac 应用具有高度的一致性，iPad 版本采用了与 Mac 相似的三栏样式。而在 iPad 多任务处理中，悬浮窗口呈现的 NetNewsWire 几乎和 iPhone 应用一模一样。

![](.evernote-content/5F217C72-0CA5-49DB-9819-D06F6F9438A1/66DC9A83-A7BB-49F0-8FE9-5E06FF3C7CB3.png)

与 iOS 平台上另外两个旗舰 RSS 应用 Reeder 和 Unread 相比，NetNewsWire 的设计感稍显不足。但是，其接近系统应用的设计风格，虽算不上惊艳，但十分耐看。我个人甚至很喜欢这种接近于系统应用的设计风格。

功能
--

NetNewsWire 支持一个默认的本地 RSS 账户，以及绑定 Feedly 和 Feedbin 服务。 目前，其并不支持 Inoreader 和 NewsBlur 等更多的 RSS 服务账户，我认为这一点亟待改进。

![](.evernote-content/5F217C72-0CA5-49DB-9819-D06F6F9438A1/CF58AFFE-5F32-43E3-BBAC-31E5B2483032.jpg)

此外，作为一款只支持 Mac 和 iOS 的应用，NetNewsWire 完全可以使用 iCloud 同步本地账户，而不需要用户在各个设备上都单独添加一遍自己订阅的站点。对于上述 2 个问题，开发者也承诺会在后续版本中改进。

NetNewsWire 提供了智能视图，你可以快速筛选出今天、未读和收藏的内容。其中，今天包含了过去 24 小时的文章。这个细节我很喜欢，如果只包含真正意义上「今天」的文章，那些午夜发表的内容就很可能会被忽略。

![](.evernote-content/5F217C72-0CA5-49DB-9819-D06F6F9438A1/4C7214EA-40A1-4616-93A8-7777C25668E7.png)

此外，NetNewsWire 提供了获取全文的功能，该功能适用于一些仅在 RSS 中包含摘要信息的订阅源。目前，NetNewsWire 并不支持调整文章的字体样式和大小，只能使用官方默认的渲染样式，这一点对自定义要求高的用户可能稍显遗憾。

NetNewsWire 快捷键支持值得一提，iPad 版本上的所有操作基本都有快捷键，快速浏览标记文章的体验非常好。

![](.evernote-content/5F217C72-0CA5-49DB-9819-D06F6F9438A1/EDC0F1FF-34C4-40CF-A570-AC0BEC7A5D83.jpg)

同样，Mac 版本也支持大量的快捷键操作，你甚至只需要使用上下左右方向键就可以完成在不同的资讯源和文章之间的跳跃。细节做得很好，例如当你一不小心删除或已读某篇文章后，你可以直接使用标准快捷键 Command + Z 还原，也可以在 iOS 设备上使用摇一摇来撤回操作。

哲学
--

无论是设计还是功能，NetNewsWire 似乎没有太多的「亮点」，一切都显得中规中矩，但这不意味着 NetNewsWire 乏善可陈。

NetNewsWire 的创造者分享了他们的开发哲学：

> 我们认为 NetNewsWire 绝不应该崩溃，应该是没有 BUG 的。它应该足够快，并且比空气还轻。我们相信 NetNewsWire 的质量比单纯地增加功能更为重要，质量本来就应该是最重要的功能，可以让用户一次又一次放心地使用它。NetNewsWire 功能的更新，绝不应该以牺牲可靠性和速度为代价。

得益于开发者对于轻量、稳定的追求，NetNewsWire 的 Mac 程序包解压后不到 10 MB，而 iOS 应用大小仅 7 MB 左右。同时，NetNewsWire 的刷新速度真的很快，我使用了这么久也的确没有遇到崩溃的情况。

最后，请不要忘记 NetNewsWire 最值得称道的特点：开源且免费。目前为止，其他能够拥有相似功能和体验的 RSS 客户端无一例外都是收费的。

你可以在 [App Store](https://apps.apple.com/cn/app/netnewswire-rss-reader/id1480640210) 或 [官网](https://ranchero.com/netnewswire/) 下载 NetNewsWire 的 iOS 及 macOS 版本。

**拓展阅读**

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e) ，发现更多新酷应用

7746

设计

功能

哲学

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/59482)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1e90375f-9834-476a-849f-bf2e5585ab5c/1e90375f-9834-476a-849f-bf2e5585ab5c/)