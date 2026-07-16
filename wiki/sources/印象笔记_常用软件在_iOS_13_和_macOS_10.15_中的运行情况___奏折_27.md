---
title: "常用软件在 iOS 13 和 macOS 10.15 中的运行情况 _ 奏折 27"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/常用软件在 iOS 13 和 macOS 10.15 中的运行情况 _ 奏折 27.md
tags: [印象笔记]
---

# 常用软件在 iOS 13 和 macOS 10.15 中的运行情况 _ 奏折 27

# 常用软件在 iOS 13 和 macOS 10.15 中的运行情况 | 奏折 27 --- 常用软件在 iOS 13 和 macOS 10.15 中的运行情况 | 奏折 27 ==========

---

# 常用软件在 iOS 13 和 macOS 10.15 中的运行情况 | 奏折 27

---

常用软件在 iOS 13 和 macOS 10.15 中的运行情况 | 奏折 27
=========================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

上周，苹果放出了 iOS 13 Beta 2 和 iPadOS Beta 2 的描述文件，让升级到新系统的步骤变得更简单了。为了给有意尝鲜升级的读者们提供参考，我们汇总了一份常见软件在 Beta 系统中的 bug 列表，你可以根据自己的使用情况进行判断。

本周的重点关注内容还有新系统中的两个新特性，包括：iOS 13 在删除 App 时会提醒取消订阅；新系统会自动在中西文之间插入空格。

新鲜工具方面：OmniFocus for Web 上线了独立订阅版；泼辣修图团队推出了视频拍摄工具「泼辣 24」。

常规更新方面：新版 Chrome 将内置更多主题自定义设置；Notion 更新至 2.6；Notability 发布 9.0；Twitterrific 发布 6.0；Microsoft To-Do 上架 Mac App Store。

新闻方面：国家出台新规定，App 不可以再随便获取个人信息；Google 推出了 Indie Games Accelerator 助力独立游戏开发者。

此外，本周还有一套 Keyboard Maestro 模板，以及一个文具测评站点推荐。

⭐️ 重点关注
-------

### 常用软件在 Beta 系统的运行情况

**@文刀漢三：**上周苹果放出了 iOS 13 等新系统的第二个开发者测试版本。此前 iOS 13 Beta 1 和 iPadOS Beta 1 由于需要下载完整固件，并且需要借助 macOS 10.15 或测试版 Xcode 才能升级，过程较为繁琐，因此挡住了不少有意尝鲜的朋友。

这次第二个测试版，苹果放出了描述文件，也就意味着升级的步骤变简单了。只需安装一个描述文件，手机和 iPad 就可以独立完成升级，无需借助其它设备。

为了给准备尝鲜的朋友们提供一些参考，我们列出了常见软件在 Beta 系统中的运行情况，你可以根据自己的使用情况进行判断。

#### iOS 13 和 iPadOS 中运行有问题的 App：

* **快捷指令（Shortcuts）：**大部分快捷指令需要调整后才能使用，并且与旧版不兼容。详见 Minja 在《[从场景自动化到自然语言支持：更易使用的 Shortcuts | WWDC 特刊](https://sspai.com/post/55205)》结尾列的 Bug 汇总。
* **提醒事项（Reminders）：**共享列表功能不可用，中文自然语言识别支持的语法不全。
* **Ulysses：**在分屏时文字会超出屏幕边界，通过返回文章列表再重新打开可解决。
* **Moke（墨客）：**回复微博评论时会闪退。
* **米家：**界面元素错乱，勉强可用。

  ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/E216C099-8B8D-40F6-884E-B48EE305BF6A.png)

  iOS 13 中的米家应用

#### macOS 10.15 中运行有问题的 App：

* **Drafts：**偶尔会出现无法和 iOS 版同步的问题，需要重启应用。
* **企业微信：**无法启动。
* **Safari：**Pocket、Evernote 等浏览器扩展失效。
* **Karabiner-Elements：**失效，临时的解决方法见[此贴](https://github.com/tekezo/Karabiner-Elements/issues/1867)（仍然会出现偶尔失效的现象）。
* **Bartender、HyperSwitch：**需在「系统偏好设置 - 安全性与隐私 - 隐私 - 屏幕录制」中给予权限。
* **MoneyWiz：**记录支出时有一定几率会闪退。
* **虾米音乐：**无法启动。
* **RegExhibit：**无法使用，因为是 32 位应用。
* **Alfred：**
  + 「Preferences - Feature」中图标部分消失（[症状参考](https://www.alfredforum.com/topic/12970-alfred-4-went-something-wrong-with-macos-1015/?tab=comments#comment-67917)）

    ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/73C81780-AC6A-40D2-9377-A2B34F35C37C.png)

    Alfred 部分图标消失
  + 无法搜索应用程序（[官方解决办法](https://www.alfredapp.com/changelog/)）
* **LaunchBar：**
  + 无法搜索应用程序。
  + 在 Action Editor 编辑动作时，动作会自动创建多个副本（重新打开 Action Editor 后会消失）。

    ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/0E5DF94B-C174-4AF2-AF54-D06AD7398E66.png)

    动作会自动创建副本
  + 使用 / 编辑自定义动作时提示 Plist 错误。
* **Keyboard Maestro：**Keyboard Maestro Engine 无法授权，点击勾选按钮无反应，多数功能无法触发。

  ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/BB32F75E-28BB-4665-B272-9B98E7D4DACC.png)

  Keyboard Maestro 引擎无法授权

这份列表会随着新 beta 系统的发布随时更新，并发布在当周的奏折中。也欢迎大家在评论中向我们提交其它软件的运行情况。

### iOS 13 在删除 App 时会提醒取消订阅

**@文刀漢三：**很多订阅制应用都会推出这样的服务：提供几天的免费试用，但是试用到期后会自动扣费。

iOS 13 beta 2 推出了一项新功能，当你删除一款正在订阅的应用时，系统会提醒你是否要取消订阅。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/4993E9E4-B632-4B61-A053-08BBC01CDCDD.jpg)

删除应用时会提示取消订阅

我身边有一位朋友就遇到了这个问题。他本身对电子产品不太熟悉，即使在用 iPhone，平时也很少用到 iCloud 相关的服务。所以他以为将一款应用删除后，这款应用就跟自己没关系了。结果他反而被自动扣费掏了腰包。

「云服务」和「账号」这些概念对于他来说是陌生的，这也跟 Apple ID 在系统中的存在感也比较低有关。有的应用甚至还会把「自动扣款」、「价格」之类的字眼藏得特别小，故意误导用户。所以有人就没有注意到备注的小字，试用结束后被扣了款，最后在 App Store 评论区等地方抱怨。

如果大家遇到了类似的问题，可以尝试通过 iTunes 退款，退款流程可以参考此文：《[如何快速申请 App 退款 | 一日一技](https://sspai.com/post/40540)》

### 新系统会自动在中西文之间插入空格

**@文刀漢三：**因为中西文书写体系的不同，中文书写是不要求空格的，而西文则需通过空格来分词。所以当两种语言混排在一起时，在中西文之间加入间距，会有利于文字在两种语言之间的平滑过渡。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/A273D6BF-017D-42CE-93E9-C10A6AA9AEFA.png)

中西混排时不加空格和加空格的区别

不过这一直没有成为行业规范，并且赞同者也分成了两派观点：一派认为，这应该是排版软件做的事情（比如 Word 就会自动调大中西文之间的间距），不应该人为在中西文之间插入空格；另一派则认为，现有的大多数网站和软件都没有对中西混排进行优化，所以愿意人为地插入空格，优化排版效果。

关于中西混排时是否要插入空格的讨论，可以参考这篇[少数派文章](https://sspai.com/post/33549)，和这条[知乎问答](https://www.zhihu.com/question/19587406)。

最近，Twitter 用户 @PLLYNYXQ [发现](https://twitter.com/PLLYNYXQ/status/1135976515248828418)苹果新系统会自动在中西文之间插入一个小于半角空格的间距。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/3F780087-DE2C-4A5E-BBFC-B1F147F406D8.jpg)

@PLLYNYXQ 的推文

也就是说，开始有大公司在操作系统层面关注中西混排的问题了。根据我的测试，这个新的排版特性在 iOS 13、iPadOS、macOS 10.15、watchOS 6 中都是有效的。

无论对于「手动空格党」，还是「非手动空格党」来说，都是一件非常值得庆祝的好消息。至少在苹果生态系统内，你见到的所有中西混排内容，都能获得更好的排版效果。我也非常希望能有更多的大公司加入到这个阵列里面。

新鲜工具
----

### OmniFocus for Web：好的工具不一定能提供好服务

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/59A043E7-2C53-455D-B9BD-C383DF1933A3.png)

**OmniFocus for Web**

[链接](https://www.omnigroup.com/omnifocus/web/)

#### 应用简介

苹果平台上久负盛名的任务管理工具，功能全面且稳定。

#### 值得注意的更新内容

**@sainho：**四月份上线了 OmniFocus 全平台订阅服务之后，官方现在又提供了[单独订阅网页版](https://www.omnigroup.com/blog/omnifocus-for-the-web-now-available)的选项。你可以选择以**每月 4.99 美元，或者全年 49.99 美元**的价格，通过官网 [Omni Store](https://store.omnigroup.com/subscribe/) 进行订阅。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/79C52D87-8DFA-4CC9-B63C-1A101EA4562D.png)

OmniFocus for Web

必须搞清楚的是，能够单独订阅网页版，并不意味着你能剩下购买本地应用的钱。网页版必须配合 Mac 或 iOS 版的 OmniFocus 使用，在网页版和本地版中登陆同一个 [Omni Account](https://accounts.omnigroup.com/?pk_vid=e2f51090e32551fb15610519756f8e99)，才能同步数据。

OmniFocus 是我用了将近四年的事项管理工具。对我这种已经购买过本地版的人来说，虽然这次的单独订阅更划算一些，但它**不是一项能让我愿意掏钱的订阅服务**。

从功能上看，目前的 OmniFocus for the Web 只能是**本地版应用的补充**。在网页版中，你可以新建和编辑项目与动作，查看「已标记」透视和管理标签。不过并没有「预测」和「检查」透视。除此之外，网页版不能查看自定义透视，也不能给动作设定重复属性和提醒。

功能的缺失可以逐步完善，OmniFocus 订阅服务的关键问题，在于**无法让我直接感知它的价值**。

订阅服务对我来说是一项支出，而非投资。既然是支出，我就会期待肉眼可见的回报。虽然我每天会频繁使用 OmniFocus，但它不会有明显直接的产出。相反如果是买断制，单次支付的钱虽然多，但我会将它视为一次投资，用于提高我的工作效率。

并不是说只有音乐、视频等形式适合订阅服务。以工具为核心的订阅服务，已有不少已经被市场接受的案例，例如 Office 365 和 1 Password。使用 Word 完成了一份报告，使用 1Password 节省回忆密码的时间，都能让我直接的体会到支出订阅费用带来的回报。

简单得说，如果订阅 OmniFocus 只是为了能够使用它，那肯定算不上值得让人买的「服务」。

编注：sainho 是《[用 OmniFocus 3 搭建任务管理系统](https://sspai.com/series/69)》教程的作者。

### 号称电影级视频拍摄工具：泼辣 24

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/18C1249D-160B-433F-A06D-30A4ACC4F80D.png)

**泼辣 24**

[下载链接](https://apps.apple.com/cn/app/%E6%B3%BC%E8%BE%A324/id1341136787?app=itunes)

#### 应用介绍

**@沨沄极客：**泼辣 24 是一款由 [Polarr Inc.](https://apps.apple.com/cn/developer/polarr-inc/id988173373) 推出的视频拍摄应用，它主打的是 **电影质感的拍摄体验**，以及可以学习色彩偏好的**智能滤镜引擎**。而名字中的 24 则是电影拍摄最常用的 24 帧 / 秒的意思。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/C5E3B325-E4D8-4B49-B3BF-F4415C99D7EC.jpg)

泼辣 24

在实际使用时，泼辣 24 确实和同类产品有许多不同，比如**滤镜的智能学习**，初次使用时会让你选择几组最喜欢的滤镜，然后生成一套适合你的滤镜方案，这个做法颇为新奇。再比如防抖功能，泼辣 24 在光学防抖的基础上又**增加了「影视级防抖」**，能够更好地减少抖动对视频的影响。还有**镜头拉伸**、**音轨编辑**等功能，对喜欢用手机拍摄视频的朋友而言应该是相当不错的应用。

目前免费用户可以使用 32 个滤镜，偶尔拍拍视频也是很够用了。泼辣 24 的订阅费用是 20 元 / 月、198 元 / 年，可以解锁上百个滤镜。这也是泼辣系列的一贯做法。**如果你已经是泼辣修图的会员，允许你直接导入泼辣修图的滤镜**（通过二维码导入，一次导入一个），对老用户而言有不小的吸引力。

⚙️ 常规更新
-------

### 新版 Chrome 浏览器将内置更多主题自定义设置

**@Fairyex：**在新版的 Chrome 开发者版上，[Techdows](https://techdows.com/2019/06/chrome-77-canary-lets-you-apply-colors-to-browser-ui.html) 发现了谷歌更新了新标签页的自定义设置，并内置了主题。该功能将会很快来到稳定版 Chrome，因为稳定版本也有相关的隐藏设置，只是开启不生效。

只要在 Chrome 开发者版上访问 `chrome://flags` 并搜索 NTP，把 `Chrome color menu` 和 `NTP customization menu version 2` 设置为 Enabled 后重启浏览器，即可开启新的自定义设置（虽然 Techdows 只提到了 Chrome Canary，但 Chrome Dev 开发者版同样适用）。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/FCDCA57C-E266-4B0D-B999-06539063C936.png)

开启设置

点击新标签页右下角的自定义，普通版只有背景的设置，新的自定义设置不仅可以更换背景，还能设置新标签页的快捷方式是自定义还是最常访问的网站，也可以隐藏所有的快捷方式。颜色和主题背景则是官方将要内置默认主题的先兆。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/AC157FCA-46A4-4552-83E4-4E73B31D94F4.png)

新增纯色背景

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/BCB440C4-1108-443E-8136-33A71F9CE47F.png)

纯色背景效果

### Notion 2.6：优化 PDF 导出，支持 Firefox 剪藏

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/8D3B0A1F-2A3D-4826-8053-8E1774C933D9.png)

**Notion 2.6**

[下载链接](https://apps.apple.com/cn/app/notion-notes-tasks-wikis/id1232780281?app=itunes)

#### 值得注意的更新内容

**@沨沄极客：**这一次的 Notion 更新带来了 5 个新功能：更好的 PDF 导出、Google Drive Embeds 优化、带 Emoji 的标注块、代码块注释、火狐浏览器的剪藏插件。

其中值得一提的是 PDF 的导出功能，Notion 以前的导出 PDF 可能会出现在「把图片分割在两页」「把一行文字分割在两页」的情况，现在导出的 PDF 已经不会再出现这个问题了。PDF 的文字也变成了相对通用的格式，能够在 PDF 中作为文字选中。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/323CB443-F448-4DEF-AC2A-E5BDCF4C2EC6.gif)

导出 PDF / 来源官网

Google Drive Embeds 方面，现在能够在 Notion 中关联 Google Drive 账号，直接选择相应的文件进行添加。同时这不会占用 Notion 的容量。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/DE2B0D68-08EB-4AED-AA54-CA89738D530B.gif)

Google Drive Embeds / 来源官网

诸如 Emoji 标注块、代码块注释等属于小修补，总的来说这次的更新力度比较小，可以在 [Notion 官方说明](https://www.notion.so/What-s-New-157765353f2c4705bd45474e5ba8b46c) 中看到更详细的说明。

### Notability 9.0：拯救歪歪扭扭的笔记

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/352EFA1A-F6D9-440E-8B70-74E34291EF70.png)

**Notability 9.0（2019–06–13）**

[下载链接](https://apps.apple.com/cn/app/notability/id360593530)

**@Minja：**手写笔记应用 Notability 每次更新被都会拿来和对手 GoodNotes 对比一番，不过这种拉锯战并不是我们今天关心的重点。对于这次的 Notability，我想说的是：它终于成了一款能放心使用的手写笔记工具。

所谓让人放心使用的手写笔记工具，必须做到两点：

1. **绘画时易于控制**，写字、画图不能像一支出墨量堪比水龙头的马克笔一样无法掌控，粗细要适当、笔迹延迟要低，等等。手写领域最出名的 Notability 和 GoodNotes 做得都还不错。
2. **画好后效果工整**：画直线就是直线、勾圆圈就是圆圈，不会生产出歪七扭八令人反胃的形状。这正是此次 Notability 更新的重点之一，而在专门的绘画应用 Procreate 中已经是主打功能了。

一言以蔽之：**又好使又好看**。Notability 引入的自动形状识别看似基础，其实这些形状同时满足了前面提到的亮点，并且利用空间很广阔，随手画个**思维导图、流程图**都变得很容易，可以直接在应用内画出相对工整的图示。而在以前的版本里，不经训练的人画出图基本上是没法看的。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/C9925FE1-F217-4122-A5EB-A0C592B92137.png)

自动识别出来的形状更加美观

当然，作为大版本更新来说只提这一个功能是不够的，橡皮擦的**局部擦除**功能同样要夸一夸。过去的 Notability 会径自把整条笔记或整个形状擦掉，不小心碰到一个图形的角落，就可能把一大块都擦没掉，这显然不符合我们手绘的习惯。想用 Notability 正经画点复杂的图示，局部消除还真是不可或缺。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/0C6B8FA4-5E9B-4944-93E2-B84A223A4D19.gif)

整体擦除和局部消除

很巧的是 iOS 13 原生备忘录也给手绘里的橡皮擦加上了局部消除功能，不会再一擦就误伤半幅画。当然，这些工具里的整体擦除功能也还在，算是电子设备区别于纸笔的一大特色，需要快速擦掉大片内容时仍然很有用。

另外说一下我自己对于手写笔记工具的态度。熟悉我的朋友可能还记得「Minja 喜欢做手账」、「Minja 经常画插画」，这次 Notability 更新后同事文刀也是第一时间想到让我来几句点评，不料「Minja 这厮竟是一个从来不用任何第三方手写笔记工具的人」。我在用且只用原生备忘录中的铅笔，原因就是只有它笔触更自然，几乎不需要勤学苦练就能达到和纸笔类似的体验（小时候有过从铅笔过渡到钢笔的经历的人，可能还记得铅笔要容易掌握得多）。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/7F4B451B-4CA1-41B6-B7DE-C125B90235DD.png)

用备忘录画的家居布局设计

换到 Notability 和 GoodNotes 这些第三方工具，就需要相当长的磨合期，从写下第一个字、画出第一个圆开始就在侵蚀你的自信心，简直是持续打击积极性。用纸笔写得一手好字的人，大半在玻璃上就是蚯蚓爬 —— 而这，也是我此次给 Notability 正面评价的原因：自动形状识别标志着它开始利用电子工具的特长简化绘制操作，而不再是单纯复刻纸笔用法。

### Twitterrific 6：新增主题，改变付费模式

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/95E6A37E-928A-4F87-97B1-1B1F0D48A6B1.png)

**Twitterrific 6.0 for iOS**

[下载链接](https://apps.apple.com/cn/app/id580311103)

#### 应用简介

苹果生态内与 Tweetbot 齐名的 Twitter 第三方客户端，也是 iPhone 上最早的 Twitter 客户端。开发团队是 Iconfactory，擅长做视觉设计，也经常帮其它应用设计图标。

#### 值得注意的更新内容

**@文刀漢三：**Twitterrific 也是一款非常老牌的 Twitter 第三方客户端了。最近它发布了 6.0 更新，主要变化有：

* **图片支持以原生比例显示：**比如有的图片是横的，有的是竖的，有的是方的，它们在 Twitterrific 内都会按照原比例显示，不需要点开图片就能看到全图。

  ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/D2B73A36-181F-4865-BDF5-E136338F156B.png)

  以原生比例显示的图片
* **支持自动播放 GIF 和视频：**如果不需要的话可以在设置中关掉。
* **支持在转推时插入图片、GIF 和视频：**我们曾在[奏折 21](https://sspai.com/post/54652) 中提过这次官方更新。
* **内置 GIF 搜索：**可以直接搜索知名 GIF 图库 GIPHY 里的图片。

  ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/69DF300B-8C4B-4950-BEB2-B6940270BFAC.png)

  内置的 GIF 搜索
* **新主题、图标、字体：**新增 5 种主题，3 个新图标，以及新字体 San Francisco Compact Rounded。

  ![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/50C49E4C-046C-4AAE-9CBB-D8978B63ED99.png)

  新增的 5 种主题（图：Twitterrific 官方博客）
* **收费模式改变：**所有功能可以免费使用，会在时间流顶部显示一条广告 banner，偶尔弹出购买提示。通过订阅可以关掉广告，订阅价格为 7 元 / 月 和 68 元 / 年，也可以直接支付 198 元终身解锁 Twitterrific 6。

其实发展了这么多年，Twitterrific 在功能上已经跟 Tweetbot 大同小异了，两者只是一些细节上的区别，选择的时候基本上就是看个人喜好。Twitterrific 的优点是设计比较讨喜，他们的团队也一直以视觉设计见长，我在 Twitter 上关注的不少设计师都选择了 Twitterrific。

Twitterrific 的广告 banner 不算很烦人，就算不付费也能正常使用。如果你曾经购买过 Twitterrific 的老版本，也有可能会获得免费解锁的权利，具体的解锁规则可以见他们的[博文介绍](https://support.iconfactory.com/kb/twitterrific/twitterrific-6-purchase-policy)。

### Microsoft To-Do ：上架 Mac App Store

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/15E5A514-6D15-4765-8FA8-D0D43336D0F6.png)

**Microsoft To-Do for macOS**

[下载链接](https://apps.apple.com/cn/app/microsoft-to-do/id1274495053?mt=12&app=itunes)

#### 值得注意的更新内容

**@沨沄极客：**Microsoft To-Do 是一款由微软推出的免费待办事项应用，它最近推出了 macOS 版本并上架了 Mac App Store。这也标志着这款应用终于实现了 iOS、Android、Windows、macOS 全平台客户端。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/CDB1519E-84B1-4314-B2DB-87E4C8984972.png)

上架 Mac App Store

Microsoft To-Do 的功能比较基础，能够实现任务提醒、重复任务、截止日期、共享列表、附加文件、子列表等功能，有「我的一天」、「重要」等多种视图，不过并不支持标签。但作为一款**大厂出品**的、**免费**的、**全平台同步**的待办事项 App，还是相当有竞争力的。

关联阅读：[「我的一天」功能，让我选择了 Microsoft To-Do | 工作日志](https://sspai.com/post/52160)

这一次上架的 macOS 版本和 Windows 版本的功能保持了高度一致，从界面也可以看出，它并不是 Todoist 那样简单的网页套壳应用，而是一个完整的 macOS 应用。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/089C8B41-44F7-4F63-847D-9ABA1CA72F3D.png)

Microsoft To-Do

观点 & 新闻
-------

### 国家新规出台：App 不可以再随便获取个人信息

**@Fairyex：**无论用户使用任何应用或者服务，它们是否在随意地采集滥用个人信息都是令人担心的问题。我们不能指望以盈利为目的的公司能够百分百约束自己，但一个有惩罚与执行力度的规范却能让人安心不少。

针对日益泛滥的应用强制获取权限，随意采集非必要个人信息等安全问题，全国信息安全标准化委员会最近公布了《网络安全实践指南 —— 移动互联网应用基本业务功能必要信息规范》。该规范以网络安全法第 41 条为基础：

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/9ABD4DAD-41CB-45CF-88F3-2FC16EC14962.png)

网络安全法第 41 条内容

该规范以实践指引为主，除了给出移动互联网应用搜集信息的原则：**权责一致，目的明确，最少够用，选择同意，公开透明，确保安全。**

还针对地图导航、网络约车、即时通讯社交、社区社交、网络支付、新闻资讯、网上购物、短视频、快递配送、餐饮外卖、交通票务、婚恋相亲、求职招聘、金融借贷、房产交易、汽车交易这 16 种业务功能获取信息的限制。

比如即时通讯社交能够获得的权限与信息就限制在以下内容：

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/58F713B8-2E3A-47E6-B858-6142621731B2.png)

即时通讯社交基本业务功能必要信息

虽然规范制定得很详细，但如果没有人遵守那就形同虚设。这次发表的规范不同于部分「纸上谈兵」的文件，在制定之初就得到了各种官方机构与华为、小米、百度、阿里等互联网巨头的支持，相信会有较大的实践力度。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/784FB67E-38EB-4799-AC4E-7FD7D999F36D.png)

技术支持单位

如果你想了解更多详细信息，可以在官网下载完整的[规范文件](https://www.tc260.org.cn/upload/2019-06-01/1559383172125092141.pdf)。

### Google 推出 Indie Games Accelerator 助力独立游戏开发者

**@Fairyex：**今年的 3 月份苹果在 Apple Special Event 上宣布了自家的游戏订阅服务 Apple Arcade。通过苹果设备庞大的游戏用户基数与按月付费的订阅制，给一些不适合通过氪金和抽卡等内购服务盈利的游戏开发者们一个良好的渠道，保证他们专注于游戏质量。

但谷歌更早就已经在致力于让游戏开发者得到更好的福利。谷歌专门为初创游戏公司推出了 Indie Games Accelerator 计划，帮助 37 个国家与地区的游戏开发者制作出质量更高的游戏。

整个计划福利包括在谷歌亚洲总部参与的两个训练营，来自游戏行业顶级专家的专业指导，免费的 Google Pixel 手机与云平台服务，参加 Google I/O、Unity Unite 等活动，优秀的游戏还能够在 Google Olay 上获得优先展示位。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/0F9FEBC4-A357-453C-9341-7C7D52A1E89B.png)

2019 年参加活动的初创公司

现在整个移动游戏平台上的游戏逐渐被氪金抽卡等内购方式所占领，以此为盈利点的游戏往往失去了游戏本来的目的 —— 有趣好玩，不仅会变成人民币玩家的游乐场，还会使游戏同质化越来越严重。但是，纯粹好玩的游戏一般来讲都不太适合加入内购，开发者会面临很大制作成本上的压力。

苹果的 Apple Arcade，谷歌的 Indie Games Accelerator 加上强推的 Stalia 云游戏，都在用自己的方法为初创游戏公司与独立开发者探索新的渠道，解决他们在成名之前面临的压力。

工具模板：用 Keyboard Maestro 模拟双击按键
------------------------------

**@Minja：**Mac 上有一种比较特殊的快捷键，即**双击单颗按键**，相信很多进阶用户都不陌生：

* 有些需要编程的人会把双击 `⇪Caps lock` 映射 `⎋Esc` 键，方便一伸小拇指就按到退出功能键。
* LaunchBar 中，双击 `⌘Command` 把文本或文件发送给自动化动作进行批量处理。
* 仿 Vim 风格的浏览器插件（例如 SVim）里，双击 `G` 可以回到网页顶部。
* ……

由于只需要按一颗键，双击操作比普通的快捷键更容易记忆和使用，在众多键位中有着很高的优先级，我们会很自然地想**用双击来触发自定义动作**。不过通常的思路是通过底层方法来改键，一般避不了写代码。直到最近我发现可以通过 Keyboard Maestro 监控键盘来曲线实现这一功能，这个问题才有了更加简单的解法。

来看一个很基础的例子：把双击 `⇧Shift` 键变成 `⎋Esc`（你完全可以对 `⇪Caps lock` 键或其他任何键下手，只是我习惯动 `⇧Shift`）。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/FD060C0A-9715-4C92-8F02-55C29B9B3FBB.png)

实现双击的触发条件

注意，触发条件没有使用常规的「This hotkey」，而是监控了「This device key」，这样能够识别的动作类型更多，双击操作（以及三击）才能被 Keyboard Maestro 认出来。之后的事情就很简单了，接上你想要的任何动作，就完成了一套双击触发的动作。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/6E95A2FE-4BAD-43DD-BF2D-EEE72C7FD945.gif)

双击模拟 ESC 键

注：由于录屏工具所限，还是会把最后模拟的 `⎋Esc` 键录进去

唯一遗憾的是，device key 要区分设备，如果你在笔记本电脑上录入快捷键，那换到外接键盘时就要再录一次，就像我的设置里面所显示那样把两个触发条件并列起来。

This device key 是比较小众的触发方式，就连 Keyboard Maestro 开发者自己起初都 [没有发现这种用法](https://forum.keyboardmaestro.com/t/multiple-actions-from-one-hotkey/7586)。这个细节也从侧面体现了 Keyboard Maestro 的潜力，愿意挖掘一番的话甚至可以开发出官方自己都没想到的用法。

推荐
--

### 网站：文具测评站点 JetPens

**@Minja：**一般的文具测评都带有很强的个人色彩，比如自来水笔，相关文章往往主打美观、流畅、握持感等等不容易量化的标准。如果你跟着这些测评去买笔，基本会大失所望。

[JetPens](https://www.jetpens.com/) 是一个与众不同的网站，它每篇博文都像做实验一样考虑周到，分类讨论、参数罗列和个人体验兼具。最近我打算添置一款便携水笔，转了一圈还是选择参考 JetPens 的横评《[The Best Mini Pens, 2019 Review](https://www.jetpens.com/blog/the-best-mini-pens/pt/388)》。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/96F5F78B-D4FD-4993-AA2F-B1E9BBEE7372.jpg)

水笔测评 图 / JetPens

这是一篇典型的 JetPens 风格测评文章，一上来就把便携水笔分成几大类，再「分擂」进行比试，这样我就只需要重点看自己最关心的「袖珍钱包笔」部分，别的完全可以跳过。文章最后还附带一张总表，呈现了参选水笔的各方面参数，没空细读正文的人也可以直接跳到最后看数据和结论。总之在这样的谋篇布局下，丰俭由人，精读还是扫一眼就决定买哪一款全看读者自己喜好。

![](.evernote-content/A4DB6B19-4B46-4DEC-90D2-342E49B9FA14/E3F293B1-6720-4728-B3DB-1288CCFDCFED.png)

文具测评的数据总表

水笔只是 JetPens 测评对象的很小一部分，各家的钢笔、圆珠笔乃至本子等文具也常常在 JetPens 里登台竞技，其中很多品牌在国内甚至听都没听过（美、日和欧洲品牌为主，应该比较全面），在看挑选标准的同时也是一个开眼界的机会。

[#奏折](https://sspai.com/tag/%E5%A5%8F%E6%8A%98)

---

[🌐 原始链接](https://sspai.com/post/55350)

[📎 在印象笔记中打开](evernote:///view/207087/s1/af504688-78f5-4f96-97c7-d3728bd34c36/af504688-78f5-4f96-97c7-d3728bd34c36/)