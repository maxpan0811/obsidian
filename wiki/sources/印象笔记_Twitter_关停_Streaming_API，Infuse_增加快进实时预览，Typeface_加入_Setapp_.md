---
title: "Twitter 关停 Streaming API，Infuse 增加快进实时预览，Typeface 加入 Setapp _ App 奏折 050"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Twitter 关停 Streaming API，Infuse 增加快进实时预览，Typeface 加入 Setapp _ App 奏折 050.md
tags: [印象笔记]
---

# Twitter 关停 Streaming API，Infuse 增加快进实时预览，Typeface 加入 Setapp _ App 奏折 050

# Twitter 关停 Streaming API，Infuse 增加快进实时预览，Typeface 加入 Setapp | App 奏折 050 --- Twitter 关停 Streaming 

---

# Twitter 关停 Streaming API，Infuse 增加快进实时预览，Typeface 加入 Setapp | App 奏折 050

---

Twitter 关停 Streaming API，Infuse 增加快进实时预览，Typeface 加入 Setapp | App 奏折 050
========================================================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

本周 Twitter 搞了一个大新闻，另外值得关注的应用更新有：

* Infuse 增加了快进快退缩略图，这曾是它和 nPlayer 相比的唯一短板。
* Todoist 重新设计了 3D Touch 功能和「安排」界面，添加任务更效率，界面更现代。
* [Setapp](https://setapp.sjv.io/c/1249877/344537/5114) 加入了 Typeface，一款字体管理工具，弥补了原生字体工具在汉字预览方面的缺失。

下为详情。

Twitter 关停 Streaming API
------------------------

**@Hum：**从昨天（8 月 16 日）起，Twitter 正式结束了对 Streaming API 的支持。这对第三方 Twitter 客户端的最大影响是它们不能再通过 Streaming API 接收即时的信息流。

这导致的最大问题是第三方客户端不再能使用以下两项功能：

1. 推送通知
2. 时间线实时刷新

全平台，所有第三方客户端，无一例外。

Tweetbot 4 的[主要更新](https://sspai.com/post/31703) —— 它的 Activity 界面，因为受到 API 改动的影响，被迫整个移除。这几乎相当于直接把它打回到了 Tweetbot 3……

如果第三方客户端想要恢复通知和自动刷新时间线的功能，就必须使用 Twitter 新推出的 [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview)。可问题是，免费版（或者更准确地说是测试版）的 API 只能提供给 15 个 Twitter 用户使用。

目前给出价位中，下一档的价格直接跃升到了「每 250 个用户花费 2899 美元」。算上各种其它成本，第三方开发者想要收支平衡，就要收每个月收每个用户 16 美元。

今天（8 月 17 日）早上，Twitter 的产品 Rob Johnson 在 Twitter 上公开了他发给团队的[邮件](https://twitter.com/robjohnson)（[文字版本](https://d.pr/f/MTC1Uz)）。但这封邮件没有很好地解释为什么他们做出这样的选择。

其中有一句含糊其辞的：

> In 2011, we told developers (in an email) not to build apps that mimic the core Twitter experience.

似乎在暗指第三方开发者模仿 Twitter。但实际上，Twiiter 的第一个 iOS 客户端和 Mac 客户端都是第三方客户端，甚至小鸟的图标都来自于 Twitterric。

在 Twitter 官方发布的另一篇 [blog](https://blog.twitter.com/developer/en_us/topics/tools/2018/new-developer-requirements-to-protect-our-platform.html) 里，Twitter 提到以后要**验证**开发者，不会再任意发放 API。虽然不知道具体什么时候会强制实施，但到时候应该还会有一场小风波。

从这次公开的团队邮件来看，Twitter 之后的态度也许会更硬，超过 250 用户的 API 订阅费大概也只会更贵。

很多人因此判断 Twitter 第三方客户端的时代即将（已经）结束，可我却没有这么悲观。其实我设备上的 Twitter 客户端一直都有两个 —— 一个官方，一个 Tweetbot（文刀也是这样）。而且为了避免干扰，我从不开通知，苹果发布会之外也没有用过实时更新。我留下官方客户端，也主要是因为它的时间线算法和 Highlight 功能，可以帮我在更短的时间里找到更需要注意的信息（虽然代价是我都不知道其它的信息是啥）。

所以这件事，Twitter 做得确实缺乏解释，很不地道。但似乎也不必过于指责和悲观。

Infuse：快进 / 快退时预览画面
-------------------

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/91B8BC05-0129-4819-90FF-E3412FD5DDAD.png)

**Infuse 5.8（2018-08-16）**

[下载链接](https://itunes.apple.com/cn/app/infuse-5/id1136220934?mt=8&ign-mpt=uo%3D4&at=10lJSw)

#### **应用简介**

Infuse 是一款功能与设计兼具的 iOS 视频播放应用。它最大的特点是可以帮你匹配视频库，自动添加电影 / 电视剧封面、导演、演员、简介等信息，无需手动整理。Infuse 还可以与 Trakt.tv 关联，同步你的追剧进度。此外 Infuse 对视频格式、音频格式、字幕、手势操作、串流等功能也都有完善的支持。

#### **值得注意的更新内容**

**@文刀漢三：**Hum 曾在《[iOS 播放器界的双雄对比测评 | Best Of](https://sspai.com/article/40663?series_id=9)》中提到 nPlayer 的一项特色功能 —— 快进 / 快退时预览画面：

> 在 nPlayer 上，当使用左右划来快进 / 快退时，**每过一秒就可以看到那一秒视频的画面**，这样你可以清楚地知道自己是不是想把视频快进 / 快退到这一刻。但 Infuse 做不到这点，你只能猜，猜你是不是快进 / 快退到你想去的位置了，没猜对就得来回调节。

Infuse 在最新的 5.8 版本里，终于加入了这项功能，这也让 Infuse 跟 nPlayer 相比的唯一短板消失了。现在二选一的话，我们会更推荐 Infuse。

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/0DE76699-99FA-4ED7-9F14-3C44E8E65B88.jpg)

快进 / 快退时预览画面（图 / Infuse）

Infuse 有两个版本，分别是订阅制的 [Infuse](https://itunes.apple.com/cn/app/infuse-5/id1136220934?mt=8&ign-mpt=uo%3D4&at=10lJSw) 和买断制的 [Infuse Pro](https://itunes.apple.com/cn/app/infuse-pro-5/id1136220915?mt=8&ign-mpt=uo%3D4&at=10lJSw)，大家可以按需选择。

Todoist：3D Touch 后用自然语言添加任务、「安排」页面新设计
-------------------------------------

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/660E25E2-2E0B-4F83-AD41-D6ABB043C973.png)

**Todoist 11.8（2018-08-13）**

[下载链接](https://itunes.apple.com/cn/app/id572688855?mt=8&ign-mpt=uo%3D4&at=10lJSw)

#### **应用简介**

Todoist 是全平台的任务管理工具，以其易上手、云属性、自然语义、过滤功能著称。Hum 在少数派为其写过一套付费教程 ——《[用更现代的方式做任务管理](https://sspai.com/series/1)》

#### **值得注意的更新内容**

**@文刀漢三：**自然语言输入是 Todoist 的特色功能之一，但从 Todoist 的图标上 3D Touch 选择「添加任务」进去，会直接进到单个任务的编辑页面，无法使用自然语言输入，这是一个很不合理的设计。

新版终于把这项设计改了过来，从图标上 3D Touch 进入后，打开的是快速添加（Quick Add）页面，可以愉快地使用自然语言来添加任务。

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/86F11CE0-121F-4B46-8055-99051E64D459.jpg)

3D Touch 后可以用自然语言来添加任务

Todoist 11.8 还重新设计了「安排（Schedule）」界面。新设计有更明确的时间指示，我们可以直接看到推迟后的结果具体是星期几。另外新设计也把日历表放到界面底部，相比旧设计可以少点一下。

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/0786490D-F29F-4603-B03E-60A4D6781B4B.jpg)

旧 / 新设计的「安排」界面

此外撤销按钮、清空的收件箱 / 项目 / 今天页面也一些设计上的改变：

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/05F7BA3E-85E9-46C0-835F-D7C7FDCDDD32.jpg)

旧 / 新设计的撤销按钮

字体管理工具 Typeface 加入 [Setapp](https://setapp.sjv.io/c/1249877/344537/5114)
------------------------------------------------------------------------

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/E015386A-527F-45A5-8B10-1BCCC44953C3.png)

**Typeface 2.1.0**

[下载链接](https://typefaceapp.com/)

#### **应用简介**

Typeface 是一款字体管理工具，可以按组、风格来管理电脑上已安装的字体。Typeface 最大的特色是字体预览功能，支持对比字体高度、间距，并且能够直接显示中文字体的效果。

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/71A9F94B-C481-4E4C-959A-6EEAAD33825F.png)

Typeface（左）能直接显示中文字体效果，系统字体簿只能显示英文（右）

#### **普通用户也需要字体管理工具**

**@Minja：**我们需要一个字体管理工具吗？

字体管理工具，听上去好像只有专业设计师才用得上，和普通用户有什么关系？当然有关，因为我们都喜欢**好看**的东西，字体也不例外。几乎少数派每发一篇 Kindle 自定义字体的文章，最后都会成为爆文，从这一点就能看出，在意字体的人不在少数。不过，想自定义字体的话，问题也随之而来：

* 怎样预览字体效果，尤其是中文字体？
* 怎样查看某个字体适不适合中英混排？
* 看到一个好看的英文字体，怎么知道它支不支持中文？
* ……

这些关于「看字体」的问题，就需要一个字体管理工具来解决了。macOS 自带了一个字体簿，不过它智能进行简单的字体安装、卸载，想要直接预览字体的显示效果，还得用第三方工具。而 Typeface，就让「看字体」这件事变得很轻松。

上一小节里，我们已经展示过 Typeface 直接查看中文字体的效果。我在大学期间修过平面设计，身边不少同学就是直接去 Photoshop 或者 Sketch 里看字体的最终效果，有点牛鼎烹鸡的味道。如果是个不搞设计的普通用户，还得专门下一个庞大的修图工具来看效果，想想就麻烦。

查看单个字符是最基础的需求，在此之上，我们还会想知道**中英混排**的效果，毕竟现在不少中文书里也夹杂着英文，偶尔看到一个效果敷衍的英文字体，会跟吃到一颗坏瓜子一样令人扫兴。Typeface 里面可以直接输入文字查看混排效果，如果某个字体压根不支持中文或英文，就会暴露无遗（右）。

![](.evernote-content/BE221A43-C33E-4BFE-9F5D-4038BAB0571C/C145A2BC-3A7E-4394-A88A-2810F0FD53C1.png)

查看中英混排效果

更多的功能，你不妨下载 [试用](https://dcdn.typefaceapp.com/latest) 版本来体验，很可能用完你就发现，自己真的需要一个字体管理工具。Typeface 的价格不低，需要一百多块钱，如果你有需要的话，可以考虑订阅 [Setapp](https://setapp.sjv.io/c/1249877/344537/5114) 来获取 Typeface。

---

[🌐 原始链接](https://sspai.com/post/46195)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a9ebf396-27e0-40d2-a3d8-5fbeec66fe5a/a9ebf396-27e0-40d2-a3d8-5fbeec66fe5a/)