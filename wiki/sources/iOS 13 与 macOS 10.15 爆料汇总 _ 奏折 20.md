---
title: iOS 13 与 macOS 10.15 爆料汇总 _ 奏折 20
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/iOS 13 与 macOS 10.15 爆料汇总 _ 奏折 20.md
tags: [evernote, impression, yinxiang]
---

# iOS 13 与 macOS 10.15 爆料汇总 | 奏折 20

---

iOS 13 与 macOS 10.15 爆料汇总 | 奏折 20
=================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

五一小长假过后，很快就是振奋人心的微软 Build 2019、Google I/O 2019 和 WWDC 2019，相信关注科技新闻的你们一定不会错过。到时候 Power+ 也会针对这些大会推出特别内容，敬请期待。

本周的重点关注和 WWDC 2019 相关，iOS 13 和 macOS 10.15 最近接连被爆出一系列的新消息，包括 Mac 版捷径、iPad 操作逻辑变化、以及 Marzipan 跨平台应用等等。种种迹象表明，今年的 WWDC 将会是一个「大年」。

新鲜工具方面：阿里巴巴推出免费商用字体；看《复联 4》时应该在什么时候上厕所？这款叫 RunPee 的应用能告诉你。

常规更新方面：DEVONthink 发布 3.0 公测版；Overcast 发布重磅新功能，可以方便分享播客片段；时间记录工具 Toggl 发布 iPad 版等。

此外，还有 Drafts 工具模板推荐，以及通过图案欺骗 AI 算法，高通修复芯片严重安全漏洞等内容。

下面，让我们开始这期奏折的正文：

⭐️ 重点关注：iOS 13 与 macOS 10.15 爆料汇总
---------------------------------

国外知名新闻网站 [9to5Mac](https://9to5mac.com/) 的一位作者 [Guilherme Rambo](https://9to5mac.com/author/guirambobr/) 最近接连爆料了一系列 iOS 13 与 macOS 10.15 的消息，并且提及了很多具体的功能细节。

这周的重点关注，我们就来汇总一下这些爆料的内容，并且说说我们对这些新功能的看法。

### macOS 的捷径会是什么样子

**@Minja：**macOS 版的捷径可能是新系统中最吸引人的特性之一。从 9to5Mac 的[爆料](https://9to5mac.com/2019/04/19/siri-shortcuts-screen-time-mac/)来看，基本可以确定这款「已经开发两年」的新自动化工具是呼之欲出。这回可能开启新时代的 macOS 原生自动化工具改动，主要有两种可能：

1. 直接升级现有的 Automator。
2. 借助 Marzipan，将 iOS 版捷径移植到 macOS 上。

但不论是哪一种情况，都免不了和以脚本为杀手锏的 Automator 狭路相逢。比起 Marzipan 在交互上可能出现的代差，更值得关心的是新工具和目前自动化生态的**兼容问题**。

现在的 Automator 简单之处几近简陋，复杂之处近乎繁琐，对于新手和老手都不算友好。图形化模块的粗糙自不必多言，甚至没有一个文本框供你存储信息；复杂的方面，也走向了另一个极端。这是 Automator 发展历程中留下的债务，我们展望下一个自动化时代前，有必要简单回顾一下 macOS 自动化的历史。

1. 二十世纪九十年代，Jobs 回归苹果。彼时自动化还主要依赖 Unix / 类 Unix 系统的「遗产」，典型代表是 **Shell 和 Python**。
2. 近似自然语言的 AppleScript 问世，macOS 大量汲取 BeOS、NeXT 等等系统和软件的成果，使得包括 Finder、Safari、iPhoto 在内的多数原生软件都实现了**脚本化**，并支持调用 Unix 系脚本。

   ![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/0C808629-B16E-466D-B2D0-51B3B61408E6.png)

   AppleScript 编辑器
3. 同时期，作家、自动化高手 Soghoian1 入职苹果，拉开 Automator 开发的序幕。
4. 2005 年，Automator 发布，macOS 自动化生态进入**图形化**时代，同时支持调用 AppleScript 和 Unix 脚本。

   ![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/CB4506A3-C27D-496C-AD70-CA9B659B5AFD.png)

   Automator 界面
5. 以苹果原生软件为标杆，许多第三方应用开始支持 AppleScript 和 Automator，其中甚至包括早期版本的 Office。

不难看出，macOS 自动化生态的演化并不是一个更新换代的过程，而是一个**不断积累**的过程。直到二十一世纪，我们还在使用 Unix 时代的工具，这就导致了一定程度上的复杂乃至混乱。我在《[如何批量导出 Safari 书签和阅读列表 | 实用技巧](https://sspai.com/article/52565?series_id=70)》分享过一个 Safari 书签导出动作，功能简单，但是为其编写的 Automator 脚本非常复杂，结构仿佛俄罗斯套娃：

* 首先，Automator 中嵌入了 Shell
* 然后，Shell 中嵌入了 Python
* 接着，Python 中嵌入了 AppleScript
* 然后，AppleScript 中嵌入了 Shell
* ……

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/332A225B-3EC6-491A-BB58-8DC2C5962494.png)

复杂的代码嵌套

窥一斑而见全豹，这个动作很能体现 macOS 自动化生态在当下的窘境：**积累的语言和工具多，每个又无法独当一面，只能互相搀扶着前进。**于是我们看到的很多自动化动作，繁复程度直逼亭台楼阁上的榫卯构造，遑论改良，就是看懂结构都很困难。

如果简单推出一个 Marzipan 版的捷径、通过 Siri 打通 Automator ，情况不会有太多好转，毕竟 Marzipan 有希望带来的任何新模块都不可能一举颠覆 Shell、Python、AppleScript 和 JavaScript 江山。当得知 Marzipan App 将出现之后，期待的情绪在我脑中没能持续一秒，担心就接踵而至：很难想象，以前的套娃式自动化动作在 macOS 10.15 中可能「发福」到怎样夸张的层级。不过换个角度想，自动化生态也不会就此恶化，不喜欢 Siri 的人不用就行，原来的功能有很大希望会被保留。简而言之，**Marzipan 版捷径倒是一个比较实际的选择。**

而直接将 Automator 升级为 macOS 版捷径，就要冒着面对几十年「债务」的风险，如何处理 AppleScript 甚至 Unix 脚本都是一个问题。关于这一可能性的讨论是比较消极的，国外玩家圈里一片「这是屠杀」的抱怨，甚至有很多用户做好了完全放弃原生自动化工具的打算。

此外，周五早晨 Scriptable 开发者在 Twitter 上展示了应用的 Marzipan 版，似乎给 Marzipan 版捷径提供了一些想象素材。不过主界面究竟如何并不是最值得关心的，毕竟没多少人愿意全天候开着 Automator（或捷径）点按钮，最后还是回到经典的快捷键、快速操作、语音指令等更便捷的方式下，界面改动对实际使用的影响并不明显（除非苹果把原有的触发方式悉数砍掉，但这实在危言耸听）。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/30869F1F-B25D-463C-B448-27273E1AA885.jpg)

Scriptable 的 Marzipan 版

总的来说，在大批重量级工具 ——Evernote、Office、Photoshop、DEVONthink—— 都支持 Automator 和 AppleScript 的今天，在 Automator、AppleScript 和 Unix 脚本已经紧密联系的今天，苹果所做的工作最可能是小修小补换换 UI、加个 Siri 锦上添花，但也不排除大刀阔斧改动 Automator 和 AppleScript 的可能。但是，如果苹果再犯 iWork 09 的错误 —— 放弃脚本 ——macOS 的自动化生态可能就不会乐观了。

### iPad 操作逻辑变化

**@沨沄极客：**根据爆料，iOS 13 为 iPad 带来了操作逻辑上的变化，在窗口管理方面有两点改进：

1. **同一个应用现在可以打开两个窗口**：就像在 macOS 上拖动 Safari 的选项卡拖到窗口外，就能分成两个 Safari 窗口一样。这项功能可能会随着 iOS 13 来到 iPad 上。
2. **允许应用中显示悬浮窗口**：这项功能类似于一个开源项目 [PanelKit](https://github.com/louisdh/panelkit) 的效果，应用中可以显示多个子窗口，这些「卡片」可以任意拖动，像调色板一样悬浮在应用上方。还能实现堆叠，通过景深表现卡片的位置。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/E8623262-28CD-44D7-88F0-F9A029ABC7AF.gif)

与开源项目 PanelKit 类似

这两个窗口逻辑变化，说明苹果希望让 iPad 进一步提升多任务处理能力。比如同一个应用拆分功能还能用在文档、表格文件上，大幅提高文档处理效率。

悬浮窗口能让大尺寸 iPad 获得更多的操作空间。这项功能不同于 macOS 的窗口化，而是类似 Photoshop 的调色板，属于应用内的操作逻辑优化。这样的改动，让我们有望在 iOS 13 上看到更多接近桌面体验的生产力应用。

在改进操作逻辑之余，**iPad 还将支持撤销手势**，通过「三指单击 - 向左滑动」实现撤销，「三指单击 - 向右滑动」实现重做。由于这样的操作并不直观，苹果可能会在初次弹出键盘时出现引导动画。将来如果想撤销一步，终于不必再摇一摇 iPad 了。

以上三点已经有多家外媒进行了报道，可信度较高。剩下的信息以传闻居多，无法确定是否会在 iOS 13 上实装。

[Federico Viticci 在播客 Connected 中爆料](https://www.relay.fm/connected/239?_ga=2.204938768.1670066500.1556862083-779937119.1556636106)，**称苹果将会在 iOS 13 中添加外部指针设备支持**。这里的「外部指针设备」主要就是指鼠标和触摸板。Viticci 还提到，这项功能默认关闭，需要在辅助功能中手动开启。

如果真的官方支持了鼠标，iPad 的使用效率确实能得到进一步的提升。苹果也需要考虑启用鼠标指针的后果，这会让 iOS 的应用逻辑出现分歧，给开发者和用户双方都带来一些误导，毕竟手指操作和鼠标操作是两回事。

[9to5Mac 的 Gui Rambo 表示](https://www.imore.com/ios-13)，iOS 13 会推出**更强的多选功能（Multi-select Support）**，不仅可以选中多个图标、选中可以拖动的内容，还能拖动列表项目和视图这种复杂的结构（Items in list and collection views）。

[The Verge 的一篇短报道提到](https://www.theverge.com/2019/1/30/18204230/apple-ios-13-dark-mode-ipad-home-screen-features-rumors)，iOS 13 可能会**带来一个全新的 iPad 主屏幕**，还会给 File 和其他应用添加多标签页功能。但目前没有更详细的消息。

### Marzipan：不能以高质量应用的标准去要求它

**@文刀漢三：**Marzipan 是苹果内部的一项开发代号，其目的是提供一套开发工具，让开发者以更小的成本进行跨平台（iPhone、iPad、Mac）开发。在去年 WWDC 上，苹果曾经简单预览过这个项目，并且放出了四款已经通过 Marzipan 移植后的 macOS 应用：新闻、股市、语音备忘录、家庭。

根据 9to5Mac [爆料](https://9to5mac.com/guides/macos-10-15/)，在今年的 WWDC 上，苹果将会推出独立的音乐、播客、TV 应用，并且都是采用 Marzipan 技术进行移植。此外还会有重新设计的图书应用以及捷径（Shortcuts）的 Mac 版，但不确定是否采用 Marzipan 技术。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/5E1D6D88-764F-4EFE-97DA-84031A48D9F7.png)

iTunes、播客、TV、图书（来源：9to5Mac）

苹果推出这个项目，很有可能是为了**拯救 macOS 应用生态的颓势**。近几年，macOS 上新出现的高质量应用越来越少，各大厂商的开发重点也都是以移动平台和网页版为主，桌面端应用永远被排到了最后。这是由两个原因导致的：一方面，用户的主要使用场景慢慢往移动平台迁移，macOS 受到的关注也就随之降低；另一方面，开发并持续维护一款 macOS 应用的成本不低，和开发 iOS 应用完全是两码事，两者的代码并不能互通。因此，我们可以看到开发者们越来越倾向于转向网页版应用（比如 Twitter），或者使用 [Electron](https://electronjs.org/) 这样的跨平台开发框架（比如 Notion、Slack、Trello）。

Marzipan 项目主要解决的就是第二个问题，降低跨平台开发的成本。不过这里又出现了一个新的问题，开发成本到底会降到多低呢？虽然苹果目前没有披露更多的细节，但我们仍能从一些侧面来一窥究竟。

简单来说，**这取决于你对应用质量的要求**。

Twitter 上的爆料达人 [Steve Troughton-Smith](https://twitter.com/stroughtonsmith) 开发了一款命令行工具 [marzipanify](https://github.com/steventroughtonsmith/marzipanify)，让你可以将模拟器中的 iOS 应用，转换成运行在 UIKit 上的 macOS 版应用。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/4D3B5CA5-D8C5-453B-9BD0-77F20DAD1C7E.jpg)

使用 marzipanify 移植的 Overcast for macOS（来源：Steve Troughton-Smith）

如果你的需求只是将 iOS 应用直接运行在 macOS 上，那么一条命令行就可以搞定。但如果你想让移植后的应用[有更合理的应用界面](https://www.highcaffeinecontent.com/blog/20190302-Making-Marzipan-Apps-Sing)、[支持「服务」和 AppleScript](https://www.highcaffeinecontent.com/blog/20190307-Deeper-Integration-with-Marzipan)，那么显然要付出更多的成本来适配和优化。

就比如 iPhone 和 iPad 都是 iOS 系统，它们的交互模式和开发框架够通用吧？但即便如此，iPhone 应用如果要推出一款高质量的 iPad 应用，仍需花上很多努力。比如支持分屏、支持快捷键、支持多指操作、支持 Drag and Drop 等。

苹果目前已经发布的几款 Marzipan 应用，都遭到了大量的用户吐槽。Benjamin Mayo 专门写了一篇[博文](http://benjaminmayo.co.uk/marzipan)，悉数 Marzipan 应用的诸多问题。比如所有应用都不支持多窗口；家庭应用内部出现了照搬 iOS 的设置界面，同时还无法点击设置界面外的内容（macOS 风格的设置界面是单独的窗口，和主应用分离）；在搜索栏输入内容后，按下 Esc 键会清除搜索栏的内容，但是侧边栏里的搜索结果不会被重置；快捷键支持不完善；此外还有页面的滚动动画不一致、缩放窗口时没有实时响应等问题。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/B2885592-F286-4B86-BA75-467BE1E8613D.jpg)

macOS 版家庭应用中直接照搬了 iOS 版的设置界面

虽然在 9to5Mac 的另外一篇[爆料文章](https://9to5mac.com/2019/04/22/wwdc-developers-siri-marzipan/)里，提到今年苹果将为 Marzipan 加入更多新的 API，包括支持 Mac 菜单栏、更丰富的快捷键、Touch Bar、多窗口功能等。但这些仍是非常基础的 macOS 功能，离一款真正的精品应用还远得很。至少在 Marzipan 推出的初期阶段，用我们平时看待应用的标准去评判它的话，很可能会失望。

### 其它新功能

**@Fairyex：**除了上面提到的重点功能，macOS 10.15 与 iOS 13 还可能会有以下这些新功能与新特性：

* **macOS 10.15：**

  + 屏幕时间：拥有和 iOS 版类似的功能，比如设置应用限额和超时锁定应用等，有可能可以和手机上的屏幕时间联动。
  + 可能会从 iTunes 中拆分出独立的音乐和播客应用，但 iTunes 仍会保留，用于同步管理手机数据。
  + 借鉴更多 iPad 界面，可能会有与其类似的通知中心与控制中心界面。
  + 更多 iMessage 特效。
* **iOS 13：**

  + iPad 版 Safari 支持自动访问桌面版网页，比如打开 YouTube 会自动提醒用户是否切换到桌面版本的网站。
  + 邮件应用更新：支持自动分类邮件，能将邮件分为市场营销、购物、旅行、不重要等类别，并支持类别搜索，还可以将邮件添加到稍后读。
  + 全新的 Reminders 应用，iOS 和 macOS 都有。
  + 增加字体管理功能，开发者可以调用系统提供的字体选择组件，并且用户打开缺少字体文档的时候可以自动在线补全。
  + 为第三方应用设计文档共享功能。
  + 允许第三方应用直接访问外部储存照片。
  + 合并 Find My Phone 和查找朋友。

新鲜工具
----

### 看《复联 4》应该在什么时候上厕所？

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/F0F3405C-FB5B-4512-AE6C-2C026A0BCD92.png)

**RunPee**

[下载链接](https://itunes.apple.com/cn/app/runpee/id450326239?mt=8)

**@文刀漢三：**最近《复仇者联盟 4：终局之战》正在火热上映，剧情精彩的同时，电影时长也让观众很满足，有足足 3 小时 2 分钟。

看这么长的电影，相信很多人的膀胱都受到了挑战。既想在影片中途上个厕所，又担心在上厕所的时候错过了重要剧情。

前几天 [Lifehacker](https://lifehacker.com/how-to-know-when-to-go-pee-during-avengers-endgame-1834364906) 推荐了一款很有趣的应用，叫做 [RunPee](https://itunes.apple.com/cn/app/runpee/id450326239?mt=8)。它会在你看电影的时候，提醒你什么时间点是一个上厕所的好时机。

比如《复联 4》中，它就推荐了 3 个「尿点」，并且会附上每个「尿点」的准确时间，以及触发「尿点」的台词或场景。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/117C2F85-E49A-4C87-ACA7-8647345311C5.png)

《复联 4》中的 3 个「尿点」

配合 RunPee 的闹钟功能，当你开始看电影的时候，同时按下闹钟。它就会在「尿点」来临的时候发出震动提醒你。当你上完厕所回来后，点开选项，它还会向你总结刚才错过的这段剧情发生了什么，非常贴心 。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/D4587DF6-CE81-4D8E-9295-701650721C09.jpg)

闹钟提醒 & 剧情总结

每看一部电影，就需要在 RunPee 里花费一枚「尿币（Peecoins ‍♂️）」。新注册的用户可以免费获得两枚，此外还可以通过内购或者观看广告的方式来获取。

### 免费商用字体：阿里巴巴普惠体

**@沨沄极客：**随着视觉中国的版权纷争告一段落，大家对版权意识有了新的认识。在字体领域，设计师同样需要警惕字体版权带来的问题。

近日，阿里巴巴发布了一款名为「阿里巴巴普惠体」的字体。阿里官方给这款字体的定义是「这是一款由中国企业首次发布的可面向全场景使用的免费商用正文字体」。实际收录了中文 27533 个汉字，5 种字重；西文 683 字，11 种字重。字符覆盖率很高。有部分设计师对整体字形提出了一些看法，但整体来看赞美远多于批评。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/EF475586-EC37-4A86-9513-2E316BEDD442.png)

阿里巴巴普惠体

**阿里巴巴普惠体允许任何个人和企业免费使用，包括商业用途。** 部分网友质疑这款字体是否会出现「先免费后收费」的情况，我拜托 Fairyex 调查了一下，确认这款字体是可以免费使用的，即使阿里宣布收费，之前使用也不必付费。这款字体也是阿里希望提升自己的品牌做出的努力，一般也不会做出这种事。

你可以通过 [Alibaba ICS](https://ics.alibaba.com/project/Hn8mXx) 使用淘宝账号登陆后免费下载阿里巴巴普惠体。

⚙️ 常规更新
-------

### 早该如此的 DEVONthink 3

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/00715F51-0990-49EF-810E-6D1E2FBC122D.png)

**DEVONthink 3.0 公测版**

[下载链接](https://www.devontechnologies.com/blog/devonthink-30b1)

**@Minja：**上周 DEVONthink 3 开启公测，中文检索 2 、中文 OCR 识别、黑暗模式等新特性都为大家津津乐道，在奏折里也没必要再写一遍。

我想说的是，**在对元数据的处理上，DEVONthink 终于赶上并超越了 Finder**。得承认这话有点得罪人，毕竟在用户心目中 DEVONthink 已经和「元数据」「破除文件夹条条框框」划上了等号，「赶超」一说又从何而来？实际上，只要是一个真正用过 DEVONthink 2 的人，管理文件时都会处处碰钉子：

* **智能文件夹不智能**：条件非常有限，比如可以创建一个「少数派文章」文件夹，却不能排除其中的非付费文章。
* **搜索语法不够细**：不能在搜索框中直接按标签、作者等元数据来找文件。
* **常用文件夹、智能文件夹不能放在主界面边栏**，必须前往数据库才能找到，不够方便。
* ……

要命的是，这些问题在 Finder 中根本不存在，只是藏得有点深。这里只展示一下我的 Finder 智能文件夹，具体用法碍于篇幅只能在以后的文章里细说。下图是我在 Google Photo 数据库里的几个智能文件夹，细致到可以根据颜色属性揪出所有 Mac 截图，无论是方便地插入侧边栏还是灵活指定或排除某个条件，都是旧版 DEVONthink 很难做到的。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/44D97B0A-5282-4CEA-9336-B0A406973440.png)

用 Finder 的智能文件夹找出 Mac 截图

作为 DEVONthink 用户，这些文件管理进阶功能的缺失一直让我憋着一口气。终于在 DEVONthink 3 中，上述问题一口气全部被解决。

具体说，「赶上」有两方面，功能上是**智能文件夹**的增强、**搜索语法**的拓展，界面上是**侧边栏支持存放常用文件夹**。「超越」，则体现在**自定义元数据**的加入，突破了 Finder 框架下的可能性边界。

1. 智能文件夹：可以排除某个关键词，或者指定开头、结尾，用于过滤网站、作者、标题等元数据非常精确。

   ![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/7BA204AB-B288-4977-B54B-C4E34C53A8DE.png)

   DEVONthink 3 的智能文件夹条件更全面
2. 搜索语法：支持 `元数据:关键词` 的搜索，比如用 `tag:edc` 找出所有带 `tag` 的文件。

   ![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/E70E2A44-0C05-47EA-B882-64A268C4E86A.png)

   新增的搜索语法
3. 侧边栏：可以将常用文件夹直接放在侧边栏，方便取用。

   ![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/FF27EE49-9466-42D4-95F4-7FB8E88F15EB.png)

   更便捷的侧边栏

DEVONthink 的智能文件夹、搜索语法一出现，我在 Finder 里摸索出来的那些文件管理技巧马上都能迁移过去，元数据的用途当然不限于这段简评所提及的搜索功能，包括自定义元数据等更多场景在后续的单篇文章中会和大家见面。

对元数据的灵活使用是 DEVONthink 的根本，也是任何一个完整的文件管理工具的根本。作为和 Finder 有一定替代作用的文件管理工具，评价 DEVONthink 更应该站在元数据的层面上去看。其他问题 —— 比如 OCR，买个引擎可以曲线解决 3 ；中文搜索，直接开 Spotlight 或写个 LaunchBar 动作也能凑合用 —— 都是可以解决的，唯独元数据是完全仰赖 DEVONthink 本身。

幸运的是，这次 DEVONthink 没让我们失望。

### Overcast 重磅新功能：分享播客片段

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/1396A078-B90A-4AAE-A699-7E254073E5CB.png)

**Overcast 2019.4**

[下载链接](https://itunes.apple.com/cn/app/overcast-podcast-player/id888422857)

#### 应用简介

知名开发者 Marco Arment 开发的播客客户端，主打 Smart Speed 和 Voice Boost 两个特色功能，前者可以智能缩短节目的沉默时间，后者可以均衡节目的音量。

#### 值得注意的更新内容

**@文刀漢三：**Overcast 最近推出了一项重磅功能，可以分享播客的片段，解决了播客分享不方便的问题。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/91783C9A-0BD6-42C8-8907-AC9CD7C72229.png)

分享播客片段

Overcast 新版相当于在应用里内置了一套视频剪辑工具，让你挑选片段的起始和截止时间，最长为一分钟，然后输出为音频或者视频。其中视频的画面会自动包含播客的封面、标题、节目名等信息，甚至它的进度条还会跟着视频播放而走动。

测试最终导出的效果

Overcast 本身其实已经具备很完善的分享功能了，包括有网页版，可以免下载直接播放；分享时候可以带有时间戳，不需要手动快进。

不过新推出片段分享功能，则会让 Overcast 的分享更加强大，也会让用户更加容易接受。像这样的短视频片段，尤其适合分享到微博、Twitter、Instagram 等社交平台，用户不需要离开当前应用，就能直接收听你分享的内容。

### 时间记录工具 Toggl 发布 iPad 版

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/8FB6ABB6-3577-4307-98FC-20172C109FB2.png)

**Toggl for iPad（2019–04–30）**

[下载链接](https://itunes.apple.com/cn/app/toggl/id1291898086)

#### 应用简介

Toggl 是一个记录时间的工具，可以帮助你追踪时间用在了哪里。

#### 值得注意的更新内容

**@Minja：**Toggl 可以说是 Power+ 奏折的老朋友，从两年前第一个 iOS 重启版开始（之前还有个更古老的版本，已经停更）就频频在奏折中出场。在重写了 iOS App、更新桌面客户端后，Toggl 终于在这周发布了 iPad 版。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/BE63111C-4022-4B03-B0C4-1718D121D2AB.png)

iPad 版 Toggl

iPad 上的 Toggl 和手机版功能完全一致，主要有**计时、查看报表、检视日程**三大板块，对于以前就用过 Toggl 的人来说非常好上手。估计是第一版的缘故，iPad 版 Toggl 对屏幕空间的利用率并不高，基本只是一个拉宽版本的手机 App，更多时候我还是愿意从屏幕侧边划出 Toggl 小窗口进行计时，而不是开一个全屏 App。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/C549C206-C508-4CC1-ABC9-137EA775929A.gif)

划出 Toggl 进行计时

由于我们小组是远程工作，支持在线协作的 Toggl 的就成了首选的时间记录工具。之前没有 iPad 版时，我们通过捷径间接使用 Toggl，不过我个人的情况是常常忘了关计时器，导致从表单上看是「劳动模范」，很影响数据有效性。刚推出的 iPad 客户端可能还有点粗糙，但是从无到有已经迈了很大一步。根据 Toggl 曾连登几周奏折的更新频率看，iPad 版的未来更新也值得期待。

### 更原生的文件体验：群晖 Drive for iOS

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/892B35EF-31E7-4D8F-BC7A-F6BD66ACC7D8.png)

**Synology Drive**

[下载链接](https://itunes.apple.com/cn/app/synology-drive/id1267275421?mt=8)

#### 值得注意的更新内容

**@沨沄极客：**Synology Drive 是一款群晖 NAS 专用的文件存储 App，能够通过 IP 和 QuickConnect 码连接 NAS。

最近的一次更新中，Drive 终于支持了 iOS 自带的 File（文件应用），不用再打开额外的窗口就能访问 NAS 中的文件了。**支持文件应用，意味着你可以直接用本地的程序直接打开 NAS 的文件进行编辑。**

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/48FB1C05-307C-4407-9AA8-E8C69178E3A8.png)

直接在 File 中打开文档

我目前的主力同步工具就是群晖 NAS，由于在 Drive 应用中需要「发送文件到其他应用 - 编辑文件 - 导出文件到 Drive」，非常麻烦，远不如 iCloud Drive。所以我原先采用的方法是 Documents + WebDAV 的方法访问 NAS 文件，然后直接用 Documents 来编辑文件。这方面的内容在《[用好 WebDAV，我是如何在 Windows 和手机之间传输文件的 | 工作日志](https://sspai.com/post/53942)》 有详细的说明。

现在 Drive 支持 File 后就方便了很多，**我可以直接在 File 中打开需要编辑的文档，自动跳转到 Ulysses 进行编辑，编辑完成后自动保存**。这和 iCloud Drive 的体验已经非常接近了。由于 NAS 的存储空间远大于 iCloud Drive，所以那些舍不得放在 iCloud Drive 里的大文件都可以选择放进 NAS 里。

工具模板
----

### 用 Drafts 发送 GitHub Issue

**@Minja：**用 GitHub 进行协作的人，可能经常需要提建议、设任务，不过 GitHub 客户端是众所周知的重量级工具，一些使用频繁的功能点起来不是很方便。如果只是想发一条 issue，我更推荐一个 Drafts 动作。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/AC2F3EFE-8A5D-48A7-B7D6-94372F712DC7.png)

填写 token 和选择 repo

[> 动作下载（作者 @ Tyler Hall）](https://actions.getdrafts.com/a/1Vj)

这一动作借助 GitHub API 来提 issue，可以自动查找近期活跃的 repo（仓库），并把当前草稿作为 issue 内容发上去。使用前需要在 [GitHub](https://github.com/settings/tokens) 上生成 token，第一次允许动作时根据提示填入 token 即可正常工作。这一 token 是不分 repo，所以权限要给得谨慎，最好别给删除 repo 的权限。

从用户们陆续开发各种小工具也可以看出，GitHub 的客户端实在有很多不如意之处（上期奏折介绍的 hub 就是为了摆脱 GitHub 图形界面而设计的）。好在 GitHub 的 API 给得比较足，大家也有充分的自定义空间。

观点 & 新闻
-------

### 通过图案欺骗 AI 算法：人工智能的攻与防

**@Fairyex：**经过这么多年的发展，AI 已经逐渐融入我们周围的生活中，甚至在我们无法察觉的时候 AI 当我们做了很多事情，就像[帮鞋匠做鞋子的小精灵](https://www.grimmstories.com/zh/grimm_tonghua/liang_ge_shenmi_de_xiao_xiejiang)那样。相对的，当 AI 被滥用，他对我们隐私和安全造成的威胁往往也无法察觉。

有很多相关人员已经注意到这种问题，他们正在往与主流方向相反的方向研究 —— 如何对抗 AI 算法。比如在最近比利时大学生 Simen Thys 等人发表的[论文](https://arxiv.org/pdf/1904.08653.pdf)中，就展示了如何利用一幅图片让自己从人体识别算法中「隐身」：

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/BAB9B678-4A34-4B68-91CA-D2AF83EDCC21.png)

隐身效果

这意味着如果你拿着这张图片或者穿有印有这张图片的衣服，就可以从监视摄像头的人工智能识别中消失。虽然他们的研究只是针对了 YOLOv2 这种应用比较广的目标检测算法，但是原理是通用的，并且它展示了**机器学习算法并非 100% 精准与可靠**。

Jiawei Su 等人的[单像素攻击研究](https://arxiv.org/abs/1710.08864)则更进一步，只需要改动图片里面的**一个像素**，就能让常见的人脸识别算法与物体识别算法识别不出包括人脸在内的所有物体，同时图片本身几乎没有变化。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/E4040382-F7C5-47BD-B8CC-65F9D07A79C5.png)

攻击效果

更有趣的是，这种对抗算法也是通过人工智能智能训练出来的。简单来说就是设计两种算法，以人脸识别为例，一种算法专门用来识别人脸，一种算法专门用来生成干扰。

两种算法都不知道对方的存在，只能知道对方实现的结果（人脸识别率，干扰程度以及对图片的影响程度）。两种算法互相对抗，在很长时间后研究人员就能得到两种很好的算法 —— 抗干扰能力强的人脸识别算法与对图片影响小的干扰人脸识别算法。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/D6171891-C6DE-4125-93A1-EDDFC22253DE.png)

算法原理

虽然干扰算法能够更好地保护我们的安全与隐私，但同时它也是一把双刃剑 —— 想象一下如果用这种算法对抗自动驾驶算法，那么黑客只需要在公路上画一个图案就能攻击自动驾驶的汽车了。不管如何，算法与对抗算法跟矛与盾一样，会一直博弈下去。

### 高通修复约 40 款芯片的严重安全漏洞

**@Fairyex：**NCC Group 在去年[曝光](https://www.nccgroup.trust/us/our-research/private-key-extraction-qualcomm-keystore/)了代号 CVE–2018–11976 的高通芯片旁路漏洞，这一漏洞可以让黑客从高通芯片硬件安全模块中监听出用于各种加密算法的根密钥。

该漏洞出现的地方位于高通芯片的 TrustZone，一块与普通内核隔离的专门用于实现安全算法的芯片区域。在 Android 等系统上涉及到安全加密等操作都在这个区域[独立完成](https://source.android.com/security/keystore)，即使黑客取得了手机系统的完全控制权也无法获取到这一区域上面的任何信息（因为芯片拒绝任何类型的密钥提取），但是漏洞使黑客能够通过分支预测和内存缓存的不同频率「推测」出芯片里面的部分内容。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/36F03E4D-F77F-4EA2-9FF0-5CEE2848F268.png)

推测过程

该漏洞影响到包括常见的骁龙 6xx、8xx 手机芯片系列在内的约 40 款芯片，高通直到今年 4 月份才会正式修补这个漏洞。如果你的手机芯片在下面，这个受影响列表里面，请尽快把安全补丁打到 4 月份之后。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/0679934E-03C4-4C84-8E10-5D2391D73C37.png)

影响芯片列表

推荐
--

### 网站：菜单栏 App 合集

**@沨沄极客：**有不少应用会在 Mac 上方的菜单栏添加一个快捷图标，来实现快捷操作。

macOS 的菜单栏到底能实现多少种功能？本期推荐的网站 [Mac Menu Bar Apps](https://macmenubar.com/) 给出了答案，Mac Menu Bar 收集了 230 多种菜单栏应用。包含电池类、日历类、清理类、剪贴板类等 20 个分类。满足对菜单栏定制的一切需求。

![](.evernote-content/C45B2584-76BB-440E-B79D-A7F576CFAB12/B24CB79D-79BD-4E5A-A854-153C07BE51F5.png)

Mac Menu Bar

并不是每一个支持菜单栏快捷图标的工具都能上榜的，网站收录的应用大多都有一些独特的功能点。每个应用都有一句简单介绍和这款应用的官网链接，一部分还附上了官方视频。

如果你想找一些好用的工具丰富一下 Mac 菜单栏，可以访问 [Mac Menu Bar Apps](https://macmenubar.com/)。

1. [现供职于 Omni Group。↩](#)
2. [严格说是东亚文字。↩](#)
3. [DEVONthink 3 Pro 价格贵也就贵在 OCR 引擎。↩](#)

---

[🌐 原始链接](https://sspai.com/post/54561)

[📎 在印象笔记中打开](evernote:///view/207087/s1/85a00ba3-4a1b-4bc6-864c-51cb2fecad7f/85a00ba3-4a1b-4bc6-864c-51cb2fecad7f/)
