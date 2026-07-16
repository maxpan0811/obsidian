---
title: "Workflow 1.5 更新详解"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Workflow 1.5 更新详解.md
tags: [印象笔记]
---

# Workflow 1.5 更新详解

# Workflow 1.5 更新详解 --- ![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/FF8E0181-47F8-462

---

# Workflow 1.5 更新详解

---

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/FF8E0181-47F8-4626-9507-07040E28E85D.jpg)

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/C374E6FA-AE76-424C-BC9B-091E230B4018.png)

[Workflow](http://sspai.com/tag/workflow) 是个空前的应用，它像一个工作台，一个机床。我们既可以做出某些我们需要长期使用的自动化工具，比如下载[微博里的秒拍视频](http://cl.ly/gJ6f)、[下载 Twitter 里的视频与 GIF](http://cl.ly/gL2g)、[查看某款 App 的价格变更历史](http://cl.ly/gIiu)或者[把 Evernote 的笔记变为 PDF 分享给别人](http://cl.ly/gImT)；也可以在有某个临时的需求的时候做出来一个小工具来应对，比如想[把某人的 Instagram 图片都下载下来](http://cl.ly/gJCg)或者[获取某个应用的 Icon](http://cl.ly/gIlX)。[1](http://sspai.com/34448#fn1)

Workflow 的适应力之强，使它可以很快地适配其它 App 的变化，针对不同的应用或服务制定特殊的动作。除了这一点，从这次更新我们还可以看出，Workflow 现在除了把活做出来，还想把活做得更精，把过程做得更「傻瓜」。

iTunes Store 相关动作
-----------------

[@三块五毛](http://www.weibo.com/steyuanxing) 曾经在一个[获取应用预览图的 Workflow 动作](http://cl.ly/gLXb)的基础上发展出搜索 App 链接的 Workflow 动作，可以直接在通知中心运行。这个动作运用了 iTunes Search API，所以非常复杂（你可以[下载](http://cl.ly/gLG0)下来看看），一般玩家无能为力，能做的恐怕也少有人愿意做如此冗长的 Workflow。

但是这次的更新，Workflow 直接把复杂的 API 调用转为了一个与 App Store 相关的动作——`Search App Store`。

这个改动让和 App Store 相关的动作的制作门槛大幅降低。配上此前就有的动作 `Get Details of App Store App` 使得搜索 App Store 内容，以及直接获取应用作者、价格、描述、截图、图标等相关信息变得容易许多。

同时，加上 `Show in iTunes Store` 这个动作，就可以在运行中的 Workflow 显示 App 卡片。所以如果你通过 Workflow 找到了心仪的 App，在运行中的 Workflow 中就可以直接购买或下载。

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/88014CC1-7E5F-4D6B-BF71-A4E5B08C65E1.jpg)

我做好了一个比较[初始的 Workflow 动作](http://cl.ly/gIeq)，功能是搜索 App （可以自行输入，也可以直接获取剪切版内容），并在 Workflow 中弹出下载界面。在这个动作的基础上，你可以针对自己的需求尽情发挥。

除了 App Store 以外，Workflow 这次也添加了不少 iTunes Store 的动作，用法和 App Store 动作类似，比如这个[分享正在听的音乐的链接的动作](http://cl.ly/gLIk)，所以你可以自行在以上动作的基础上举一反三。

Apple Music 相关动作
----------------

这次 Workflow 更新添加的关于 Apple Music 的新动作解决了我一个大难题。

一个人的歌多了，就会分为全曲库随机时听到了会觉得「我靠我竟然有这么好听的歌「，和随机到了会觉得「当初我怎么买了这首歌「这两种。我曾经一首一首地过我的曲库，想把那些随机到了愿意听下去的歌放在一起，这个播放列表起名就叫 `My Tastes`。而这个任务着实不容易完成，因为每听到一首喜欢的歌，我就得手动地点好几下才能把它加到那个播放列表，如果加错了，不仅要再加，还要把加错的删了，非常耗人。

而这次 Workflow 更新了两个关于 Apple Music 的动作：

* Add to Playlist（添加到播放列表）
* Create Playlist（创建播放列表）

通过第一个动作，我直接做了一个 Workflow，[这个 Workflow](http://cl.ly/gLVW) 完全解决了我的问题。而且它也非常简单——获取当前歌曲，然后添加到 `My Tastes` 这个播放列表。这样的 Workflow 可以直接在通知中心运行。

而关于第二个创建列表的动作，我的用法是这样：我们的音乐，都有它所属的类别和歌手。对于某个歌手或某个类别的歌曲，肯定也都有更喜欢的和感觉一般的。比如说，我想把我喜欢的 Coldplay 的歌曲全总结出来，一般的方法是：先在 Apple Music 里做一个列表叫 `Bests of Coldplay`，然后用 `Get Current Song` 和 `Add to Playlist` 等个动作把你听到的 Coldplay 的歌加到那个列表里。这个方法的问题在于不聪明，因为你每次有一个新的歌手想整理，就得跑去建个列表。说不定你以后都忘了你有没有建过某个艺术家或音乐类别的列表了。

但是利用第二个动作，你可以把这件事完成得聪明很多。首先你不必预先创作某个类别或某个歌手的列表，你可以让 Workflow 去获取音乐的信息，然后自行为你创建这个列表。一旦列表创建，Workflow 会自动把音乐加到这个列表。Workflow 帮你分类、Workflow 帮你整理，你要做的就是在通知中心拉出来按一下这个动作。

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/C39FBD3E-8AE0-418E-ACD8-DE6CD8538E77.gif)

动作下载：[Best Songs of XXX](http://cl.ly/gL25)，你可以根据你自己的需求进行修改。

Trello 相关动作
-----------

Trello 与 Workflow 的互动并不是通过 URL Schemes，而是通过 API，这样的好处在于 Workflow 运行的时不需要离开正在运行的应用。从客观上说，节省了跳转的时间，而且对于惯用「返回上一个 App「这一功能的人来说是个好消息；从主观上来说，不跳转体验要好很多，注意力也不会太分散。

Trello 是个团队协作的知名工具，它的概念是将办公室的黑白板的体验移动到云端。因为我们 Checked [2](http://sspai.com/34448#fn2)在讨论和执行的时候也在使用 Trello，所以我对这次针对 Trello 的更新内容还是很喜欢的。

Workflow 这次针对 Trello 更新了 5 个动作：

* Add Trello Card（添加到 Card）；
* Create Trello List（新建 List）；
* Create Trello Board（新建 Board）；
* Get Trello Items（获取 Trello 项目）；
* Get Details of Trello Items（获取 Trello 项目的具体信息）；

其中最实用的我想是 `Get Troll Items（获取 Trello 项目）` 和 `Add Trello Card（添加到 Card）`。

`Get Troll Items` 可以让我们以文本形式获取某个 List 中的所有 Card，在和同事讨论进度的时候可以直接把这个 List 的内容发送给对方。Checked 准备节目的时候，我们会把以往头脑风暴后想到的话题拿出来参考，过去我们或是打开 Evernote、或是打开 Trello 的列表来讨论，总之需要在目前讨论的应用之外再开一个应用去看这个话题列表。现在我可以使用一个通知中心动作，将话题直接发送到对应的 Slack 频道中：

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/3B0AC604-BE83-4B5D-9C14-D0E3966CA7CA.jpg)

动作下载：[Checked Topics](http://cl.ly/gLSe)

*（你可以在这个 Workflow 修改，使之适合你的团队工作模式）*

`Add Trello Card` 可以让你直接把具体内容添加到预设好的卡片，所以我们可以在 Drafts 等**在选中文字后的菜单中会显示「分享「这个选项**的应用里直接写好想添加的内容，然后通过 Workflow 直接在不离开应用的情况下，把内容发送到 Trello。

比如当我想到新话题，我可以在 Drafts 中先写好话题名和描述，然后运行 Workflow，将话题和描述分别发送到 Trello 的相应位置。

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/73DF4E12-6B2F-4BB2-9484-A8ED30E62B69.gif)

[这个 Workflow 动作](http://cl.ly/gLUB)依然只是雏形，动作中 Board、List、Due 等等都可以在选中后设为其它变量，而不必是预设的内容，也就是说你可以根据雏形完全自定义这个动作里所有的参数。

Omnifocus 相关动作
--------------

Workflow 里很早就有一个 Omnifocus 的动作，因为那时 URL Schemes 的限制，所以只支持添加任务和备注。但在上次更新，Omnifocus 彻底给 iOS 版[武装上了整套的 URL Schemes](http://sspai.com/33969)，Workflow 也马上跟进支持了这套 URL Schemes。

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/C5B490AB-349B-4B2E-AF47-8CDD6CB3FBCD.jpg)

我此前在 Omnifocus 刚更新的时候根据它的 URL Schemes 做过一个动作，用来把在阅读读中遇到的需要下载的软件保存到 Omnifocus 中[3](http://sspai.com/34448#fn3)。这个动作用到的 URL 是：

```
omnifocus://x-callback-url/add?name=Title&note=URL&project=软件下载&x-success=pocket://
```

懂的人看起来没有问题，但是对于入门者，这段 URL 就不如上面的图看着舒服。URL Schemes 的不好上手的原因之一就是不好读，Workflow 有不少动作其实都是把 URL Schemes 的各段分开然后给图形化，让新手更容易接受。

除此之外，这次更新也出现了新添加的动作——`Add TaskPaper to Omnifocus`，这一项可以用于一次性批量添加任务。在这一点上，从 Omnifocus 更新了 URL Schemes 后我就想做这样一个东西，想实现：1. 批量添加任务；2. 给需要加旗标的加旗标。本来打算用 Drafts 的自定义键盘实现。但是要新写 JavaScript。而用 Workflow 实现得特别优雅，点的次数夜要比 Drafts 自定义键盘少很多。

动作下载：[Tasks To Omnifocus](http://cl.ly/gKIH)

Ulysses 相关动作
------------

因为我不用 Ulysses，所以这部分没有办法为大家带来原创的内容，所以简单地编译一下[官网提供的三个动作及其说明](http://ulyssesapp.com/blog/2016/06/workflow/)。

**动作 1：[将网页发送到 Ulysses](https://workflow.is/workflows/920cc9a7867040f9b3c079777bf58506)**

储存时可以选择格式（文本、Markdown 或 HTML）。也可以选择位置，默认是存到 Inbox，你也可以自行选择 Group。

**动作 2：[为 Ulysses 文件添加内容](https://workflow.is/workflows/0fa38d4649b74bf29779998032262f4c)**

添加文本到已有的 Ulysses 文本中，需要使用到 [Sheet Identifier](http://ulyssesapp.com/kb/x-callback-url/#identifier) 来指定固定的文本。

**动作 3：[发送剪切板内容到 Ulysses](https://workflow.is/workflows/89a6db3209e74864af381a15bacec5ce)**

在 Ulysses 中创建新文档，然后将剪切板作为其内容。

其它新增动作
------

* `Get Group from Matched Text`: 在匹配过的文本中获取其中的某一部分。
* `Format File Size`: 将文件的大小转化成合适的单位。
* `Show Web Page`: 在 Workflow 内部显示网页。

这些动作都不难懂，只简单介绍一个对于普通用户比较陌生但却很有用的功能——`Get Group from Matched Text`。

用正则表达式的人对这个动作可能向往已久了，以前要实现这个功能也是要费一番周折。普通人对这个动作也并不是说完全用不上，因为它所作的事情是从一段文字中，获取符合匹配结果的某一部分：

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/1852CBDE-B5FC-4969-A226-EC47CB69C3F7.jpg)

工作中需要处理列表的人应该会很需要这个动作。而且正则表达式也并不难学，事实上它都不需要系统学，对于非程序员，在你用的时候搜一下规则稍微折腾一下就能应用。

支持外接键盘
------

Workflow 这次更新支持了一些快捷键：

* ⌘R 运行 Workflow
* ⌘. 停止 Workflow
* ⌘F 搜索动作
* ⌘Z 撤销
* ⌘⇧Z 重做
* ⌘W 关闭 Workflow 窗口

其它
--

Workflow 这次也修复了几个让老用户颇为头疼的问题，我个人感受最深的是以下这几个：

1. **支持 If、Repeat、Choose from Menu 这样的框架类动作的拖拽**。以前的 Workflow，If 等可以内包动作的框架一旦填入内容就不能移动，这样修一个含有框架的长动作极其痛苦。现在你移动这些框架类动作的时候，无论它们内部有没有放入动作，都会缩成一个动作条，当你把它放到合适的位置以后会再展开。
2. **支持搜索动作。**[Checked 第十期](http://Checked.fm/10)里我们吐槽了 Workflow 的分类难，几个 Workflow 的 Power User 都有超过 50 个 Workflow，找一个不容易，小瓶手机上一行只有俩 Workflow，从上拖到下都得好久。而现在能搜索了，从某种程度上解决了找 Workflow 的这个问题。
3. 据官方说 Workflow 的加载速度更快了😜。

还有一个中文输入法的 Bug：

![](.evernote-content/F3727DD9-1EEE-4735-ABDC-15F5E0F097DF/AF194C47-47F3-43ED-8B73-50D7D2C70B89.gif)

结语
--

本来只想像 1.3 版的更新时那样写简评，结果又写成了一篇长文。原因不仅在于这次更新出的动作的实用性，更是在于 App Store 那几个动作让我第一次出现了很强烈的感受——Workflow 把累活替我们做了。关于 iTunes Store 和 App Store 的动作本身都可以用 Workflow 对 API 的支持来完成，而新的动作将几十个动作块的串联合而为一。

我总是觉得对 Workflow 的赞誉是很没有必要的，因为 Workflow 已经属于为赞誉坐镇的那类应用。举例来说，去年年末出现的各路 App 榜单里，但凡是评「最佳应用「或者与效率有关的应用的，没有 Workflow 的话，只能说这个榜单不入流。所以如果你还从未见识过它的威力，你最好尽早试试。

我在少数派写过[一系列教程](http://sspai.com/tag/workflow)，你也可以下载本文中提供的 Workflow 来感受一下这款非凡的应用。

你可以在 [App Store](https://itunes.apple.com/cn/app/id915249334?mt=8&uo=4&at=10lJSw) 下载 Workflow。

1. [下载微博里的秒拍视频](http://cl.ly/gJ6f)出自[@三块五毛](http://www.weibo.com/steyuanxing)；[下载 Twitter 里的视频与 GIF](http://cl.ly/gL2g)出自[@OscarGong](http://www.weibo.com/u/1947026242)；[查看某款 App 的价格变更历史](http://cl.ly/gIiu)和[把某人的 Instagram 图片都下载下来](http://cl.ly/gJCg)出自[@T\_Bryan](http://www.weibo.com/517225734)，以上三位都是 iOS Power User Telegram 群内的成员。 [↩︎](http://sspai.com/34448#ffn1)
2. Checked 是由[我](http://www.weibo.com/jailbreakhum)、[文刀](http://sspai.com/weibo.com/wendaohansan)、[千千](http://sspai.com/weibo.com/gabriellanjrc)三人共同主持的关于效率和应用的播客。 [↩︎](http://sspai.com/34448#ffn2)
3. 关于这个动作的具体用法和情境请看[《用 GTD 的方法结束稍后读》](http://sspai.com/33933)。 [↩︎](http://sspai.com/34448#ffn3)

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[Workflow 1.5 更新详解](http://sspai.com/34448)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/34448)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bbbdaa6a-65e3-4e70-86a4-4e2e7f4dd488/bbbdaa6a-65e3-4e70-86a4-4e2e7f4dd488/)