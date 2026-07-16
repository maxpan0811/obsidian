---
title: "Shortcuts 和苹果的布局"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Shortcuts 和苹果的布局.md
tags: [印象笔记]
---

# Shortcuts 和苹果的布局

# Shortcuts 和苹果的布局 --- Shortcuts 和苹果的布局 ================ | 本文为付费栏目文章，您已订阅，可阅读全文 | 相信很多关注少数派的读者都和我一样，

---

# Shortcuts 和苹果的布局

---

Shortcuts 和苹果的布局
================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

相信很多关注少数派的读者都和我一样，当 WWDC 舞台上出现了 Shortcuts 时，瞬间两眼放光：「咦？这不是 [Workflow](https://itunes.apple.com/cn/app/workflow/id915249334?mt=8&uo=4&at=10lJSw) 吗！」

Workflow 于 [2017 年 3 月被苹果收购](https://sspai.com/post/38438)，应用本身以及四位开发者都加入了苹果。此后 Workflow 有过几次更新，但都算不上太大的变化。外界一直都在猜想 Workflow 将会以怎样的方式融入 iOS，会带给这个生态怎样的变化。

直到今年 WWDC，我们终于见到了脱胎换骨的 Workflow——Shortcuts。Shortcuts 很明显是 Workflow 在 iOS 中整合后的成果，两款应用的界面极其相似，包括模块化的功能、拖拽式的交互方式、通知中心小部件、以及提供直接下载的 Gallery 页面。

![](.evernote-content/E0EA2314-76ED-4A93-8263-E9BA8B089C51/9926479C-1556-46D2-AEA2-B2747D2204CB.jpg)

Shortcuts 应用的界面

这里我们先明确一下几个名词的意思，首先是 **Shortcuts**：

1. 这是苹果会在今年秋天推出一个独立的应用，叫做 Shortcuts（你可以理解为改名后的 Workflow），后文称作「**Shortcuts 应用**」；
2. 另外，Shortcuts 应用中每个可以运行的动作也叫做 Shortcuts（对比 Workflow 应用中的 Workflow 动作），后文称作「**Shortcuts 动作**」；
3. 每个 Shortcuts 动作都可以由多个步骤（Step）组成，步骤可以是系统自带的，也可以是由第三方应用提供的快捷操作，然后这个快捷操作也叫 Shortcuts（就问你晕不晕），后文称作「**Shortcuts 模块**」。

Shortcuts 动作除了可以在 Shortcuts 应用中运行，还可以在通知中心小部件运行，暂不明确能否在分享菜单（Share Sheet）中运行。它和 Workflow 不同的地方是，整合了 Siri 功能，你可以在「设置 - Siri 与搜索 - Shortcuts」找到这些 Shortcuts，然后设置自定义短语。当你使用自定义短语——也就是 Siri 语音运行 Shortcuts 时，它才被称作 **Siri Shortcuts**。

此外，Shortcuts 动作还可以通过 **Siri 建议** 来运行：当手机检测到合适的时间、地点或者运动状态时，就会在锁屏界面、Spotlight、或者 watchOS 的 Siri 表盘中进行提醒，让你可以点击后直接运行 Shortcuts 动作。

![](.evernote-content/E0EA2314-76ED-4A93-8263-E9BA8B089C51/14B911D2-861B-45EF-B8D2-042854E67185.jpg)

Shortcut 和 Siri 相关的启动方式

总结一下就是，Shortcuts 动作的使用途径可以分成三种：Shortcuts 应用、自定义短语（Siri 语音）、Siri 建议。

所以你可以看得出来，苹果收购 Workflow 并不是简单地把功能加进 iOS 系统里，而是在 Workflow 原有的基础上，开拓出一个新的方向：Siri。

苹果收购 Workflow 的目的之一是强化 Siri
---------------------------

这次的 WWDC，让我意识到：苹果收购 Workflow 除了提升 iOS 自身的自动化能力，另一个目的很可能就是为了强化 Siri。

从发布会上其实就看得出苹果很重视 Siri，Shortcuts 应用的所有功能展示，几乎都是围绕着 Siri 的使用场景展开的。在 WWDC 主会之外，有两场 Sessions 的演讲者都是原 Workflow 团队的开发者，一位是 Ari Weinstein，另一位是 Ayaka Nonaka1 。我有特别注意到，他们两位都隶属 Siri 部门，这就更加说明了苹果收购 Workflow 的目的——奔着融入 Siri 去的，两位都直接加入了 Siri 部门。

![](.evernote-content/E0EA2314-76ED-4A93-8263-E9BA8B089C51/C695E2E3-4B7C-47AE-A82E-8D7DFEAB3478.jpg)

Ari Weinstein 和 Ayaka Nonaka 在 WWDC Sessions 上

Siri 作为智能语音助手的角色，一直以来走的都是**自然语言处理**的路子，也就是分析用户说的每句话的语法结构，每个词每个字是什么意思，并且尝试去理解同一句话的不同表达方式。而亚马逊的 Alexa 走的则是另一个路子，它非常开放，允许第三方应用定义命令，并且用户也可以借助 IFTTT 自定义短语。换句话说，很多时候 Alexa 并没有听懂你说了什么，它只是识别到你说了一句提醒设定好的短语，然后根据设定去执行而已，如果你换个表达方式，它就会执行失败。

在前年的 [The Talk Show Live From WWDC 2016](https://youtu.be/vpCQk1pYFco?t=55m) 上，苹果软件高级副总裁 Craig Federighi 谈到他们努力让 Siri 明白用户的多种表述方式，以及他们会自己完善开发 Siri 在各个领域的语言处理能力，然后再由开发者接入进来，而不是直接把理解用户命令的任务丢给开发者。Craig 甚至还有些不齿这样的做法，他说如果仅凭关键词（Trigger Word）来触发命令的话，那其实对于苹果公司来说非常简单。

> It would have been really super easy for us to say, “Hey, just tell us a trigger word, or the name of your app, and we’ll hand you a string.” — Craig Federighi

但他们没有选择这么做的原因是，这会让 Siri 的体验非常不统一。苹果营销高级副总裁 Phil Schiller 还说到，他们对 Siri 的愿景是：对所有事情**同等的**聪明。

> We need Siri to be equally smart at all the things we do. — Phil Schiller

但现实是什么呢，Amazon Alexa 在市场上获得了大量的好评，而 Siri 则是普遍地不看好，甚至不看好到产生偏见。比如每次少数派首页上发布了一篇 Siri 相关的文章，底下评论中一定会有「可是 Siri 就是个智障」式的抖机灵，并且附和的人还不少，完全不顾文章中的技巧是否真的有用。

最后苹果还是动摇了。这次 WWDC 之后，你可以看出 Siri 的发展路线除了自然语言处理，还新增了让用户自定义短语的 Siri Shortcuts。自定义短语虽然并不像苹果公司理解的那种「智能」，但它至少能解决实际问题，因为一旦设定好了，它就不容易出错。

在 [Building for Voice with Siri Shortcuts](https://developer.apple.com/wwdc18/214) 这场 WWDC Session 上，苹果对自定义短语的建议是使用简短的、容易记住的短语。他们举了一个例子，当你想用 Siri Shortcuts 订一份海鲜汤外卖时，既不应该用「Hey Siri, please place an order, thank you」这种指向不明的句子，也不应该用「Order a clam chowder to my office」这种稍显冗长的句子，而是应该用「Chowder time」这种简短直接的短语。

![](.evernote-content/E0EA2314-76ED-4A93-8263-E9BA8B089C51/1CC44BB1-FA86-4F69-A228-5C5AF8931D31.jpg)

Siri Shortcuts 的自定义短语应该尽量简短直接

甚至，你还可以设置更短的短语。比如，Hum 曾经在 Power+ 的 Slack 群中分享过一个在 iPad 上用键盘就能快速翻译网页的 Workflow 动作（[点此下载](https://workflow.is/workflows/0a1d8a3c886545d1bf4526e62a50d616)），我把这个动作的 Siri Shortcuts 短语设置为「GT」，然后又因为我的 iPad Pro 长时间连着外接键盘，因此也开启了 [Type to Siri](https://sspai.com/article/43440?series_id=9) 功能。每当我需要翻译网页时，只需先复制网页链接，然后长按 Home 键唤出 Type to Siri，再输入「GT」，就能自动运行 Google 翻译的 Workflow 动作，比之前的步骤也要稍许简单一些。

用 Siri Shortcuts 允许 Google 翻译网页的 Workflow 动作

有了 Shortcuts 的帮助，反而让我开始觉得 Siri 有戏。当然 Siri 在自然语言识别、搜索结果整合等方面还是要继续提高，但能够使用自定义短语这一点就足够让我感到兴奋。因为自定义短语与智能无关，而是一种有标准答案的交互方式，它虽然简单粗暴，但足够实用，而且还可以配合 HomePod。想象一下，如果 IFTTT 也适配 Shortcuts 动作，那么用 Siri 控制非 HomeKit 智能家居是不是就轻而易举了？

Shortcuts 会是 iOS 自动化的 3.0 时代
----------------------------

苹果收购 Workflow 的另一个目的——是众多 Power User 关心的，也是 Workflow 本来就在做的事情——让 iOS 设备的自动化更强大。

Workflow 原本的模式是：除了需要将 iOS 系统提供的 API 封装成一个个的模块，还需要主动去适配第三方应用的 API 和 URL Schemes，把第三方应用的功能也封装成一个个模块，最后再让用户自己拼装成完整的动作。

主动适配第三方其实是劳动量很大的工作，因此在 Workflow 应用中你也看得到，支持的第三方应用并不算多，大部分都是国外比较知名的效率应用，而且有些支持的功能并不算丰富，其它类型的应用就更少了。

现在，当 Workflow 进化为 Shortcuts 之后，**不再需要主动去适配第三方应用，而是由第三方应用主动来适配 Shortcuts。**

首先，第三方开发者可以使用苹果提供的 Shortcuts API，为自己的 App 设计 Shortcuts 动作。Shortcuts API 有两种：

1. 第一种叫 NSUserActivity，可以实现比较简单的动作，比如直接打开 App 里面的某个界面，或者打开已经在 Spotlight 里可以索引的、已经提供给 Handoff 的功能2 。Drafts 开发者就利用 NSUserActivity 实现了直接打开应用的语音转文字功能：
2. 第二种叫 Intents，可以实现不打开 App 在当前界面运行结果，并且开发者还可以自定义 UI 和回复内容。比如 JSBox 的开发者钟颖就做了这么一个动作：当他喊出「回家」短语后，JSBox 会自动抓取实时的公交数据，并以他设计好的 UI 返回到 Siri 页面上：

当开发者定义过 Shortcuts 动作之后，它们就会自动出现在 Shortcuts 应用里，作为一个个可以组装的模块。也就是说，每一个应用都可以为 Shortcuts 应用提供模块。

![](.evernote-content/E0EA2314-76ED-4A93-8263-E9BA8B089C51/5BE37864-7D47-4D97-A579-ED8E18D11319.png)

在 Shortcuts 应用里使用第三方 Shortcuts 动作

当我和 Hum 讨论到这一点的时候，他提到了一个大胆的猜想：**苹果想将软件功能模块化**。因为这就像把所有 App 的功能都打碎了，然后放到 Shortcuts 里，有一点打破了沙盒的感觉，App 和 App 之间可以互相使用对方的功能。但其实整个程序还是在沙盒的保护之中，因为所有的操作都是需要经过你的允许并且由你主动组装和运行。

我们不妨顺着这个猜想继续往下延展，也许日后我们可以自己「做 App」，用不同 App 提供的 Shortcuts 模块拼装成一个「新的 App」，比如我们可以做一个每日小报的 Shortcuts 动作。运行之后，会展示今天的日历安排、还剩哪些待办事项、天气如何、今天有哪些大新闻、支付宝里购买的基金涨赔、汇率变动等信息。

在这之前，要把这些信息全都汇总到一起，其实是相对比较麻烦的。因为有些 App 内部的信息你是无法获取的，另外你可能也得懂 API 的用法，再通过一些公开的服务把数据抓取下来。Shortcuts 推出之后，以后可能都会有开发者替你把这些事情做好，我们只需要简单地进行组装就行了。也许再过一段时间，对 Shortcuts 支持的完善程度，以及功能模块拆得是否够散，也会变成好 App 的新标杆。

当然这些只是根据已有信息以及开发文档进行的猜想，实际效果还得等 Shortcuts 应用的正式发布。另外我也稍微有些担心 Shortcuts 应用发布后的第一个版本能否达到 Workflow 的完成程度，比如变量模块、`Get Contents of URL` 等和 API 相关的模块是否会继续提供，模块之间的输入输出处理是否正常，原有内置的第三方模块是否会被移除，这些问题都需要关注。但总体而言，Shortcuts 应用的回归，以及苹果赋予它未来发展的方向，都是更值得我们去期待的。

[URL Schemes](https://sspai.com/post/31500) 是 iOS 自动化的 1.0 时代，让多个 App 串联到一起成为了可能；Workflow 是 iOS 自动化的 2.0 时代，融入了模块化编程的思想，让不懂代码的用户也能轻松做出属于自己的工作流；或许以后，Shortcuts 将会是 iOS 自动化的 3.0 时代，打破 App 的边界，把 iOS 自动化提升到了一个新的高度。

1. [Workflow 原团队一共四位成员，另外两位是 Conrad Kramer 和 Nick Frey。↩](#)
2. [部分应用因为之前适配过 Spotlight 索引和 Handoff 功能，所以当升级到 iOS 12 之后，即使这些应用没有特地去适配，也能自动支持 Shortcuts 功能。此处需感谢在意空气开发者张斌对这个问题的解答。 ↩](#)

[#Workflow](https://sspai.com/tag/Workflow)[#捷径](https://sspai.com/tag/%E6%8D%B7%E5%BE%84)

---

[🌐 原始链接](https://sspai.com/post/45298)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1334b669-10b8-419d-941e-a3abe95e7661/1334b669-10b8-419d-941e-a3abe95e7661/)