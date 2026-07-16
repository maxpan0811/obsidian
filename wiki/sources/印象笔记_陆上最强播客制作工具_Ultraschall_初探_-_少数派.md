---
title: "陆上最强播客制作工具 Ultraschall 初探 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/陆上最强播客制作工具 Ultraschall 初探 - 少数派.md
tags: [印象笔记]
---

# 陆上最强播客制作工具 Ultraschall 初探 - 少数派

# 陆上最强播客制作工具 Ultraschall 初探 - 少数派 --- 陆上最强播客制作工具 Ultraschall 初探 ========================= ### Matrix

---

# 陆上最强播客制作工具 Ultraschall 初探 - 少数派

---

陆上最强播客制作工具 Ultraschall 初探
=========================

### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

在收听播客愈发流行的当下，创作播客也成为了一种越来越普遍的表达方式。但是在今天，播客的制作仍然面临着一个有些尴尬的局面 —— 现有的用于播客制作的软件工具通常来自一些传统的专业行业，例如音乐制作、音效制作、广播电台、电影工业，乃至企业音频会议方案等，这些工具虽然功能全面，但是大多数并非针对个人用户开发和销售，因此普遍存在价格昂贵、学习曲线陡峭等问题。许多播客创作者可能用着盗版的昂贵的工业级数字音频工作站（Digital Audio Workstation，简称 DAW），但实际上仅仅用到了一些简单的剪辑功能，对于更加进阶的声音处理，可能既不了解，也不知道从何入手。

我作为两档独立播客（[告别摄影](http://byebye.photography/) 和 [洋泾浜](https://www.yangjingbang.fm/)）制作的参与者，在创作的过程中也踩过各种各样的坑，几乎尝试过市面上所有的播客相关的软件工具。最近，我试图为我的播客添加章节标记，发现这个近年较为流行的功能却严重缺少相关工具的支持，虽然章节标记的 ID3 标准是开源的，也已经推出了许多年，但是现在市面上几乎所有的 DAW 都仍不支持此功能，只有 [Podcast Chapters](https://chaptersapp.com/) 和 [Forecast](https://overcast.fm/forecast) 两个成型的独立软件可用，而前者虽然功能完善，但 $19.99 的售价对于许多独立播客制作者来说并不便宜，后者虽然目前免费，但是仍然处于 bug 较多的 beta 状态，并且只支持导入 .wav 格式，导出几种固定码率的 .mp3 文件，对于希望对音质有更精确把控的创作者来说并不算友好。在这个搜寻的过程中，我发现了 [Ultraschall](https://ultraschall.fm/)。

Ultraschall 是什么？
----------------

Ultraschall 是一个专门为播客创作而定制的 [Reaper](https://www.reaper.fm/) 插件。Reaper 是我目前制作播客的主力 DAW 软件，它功能非常全面，非常轻量且价格低廉，并且提供事实上无限期的免费试用，应该是目前最适合个人音频创作者的工具之一，Nick 在少数派写的[《播客制作入门指南》](https://sspai.com/post/56285)中对它也做过简短的介绍。

但为什么我觉得一个插件值得单独来介绍？Ultraschall 不只是一个普通的插件，它对 Reaper 进行了深度的定制，完全改造了 Reaper 原有的界面和操作，增加了一些对于播客创作者来说非常实用的小工具，同时又保留了 Reaper 原有的强大的可定制性和可扩展性。可以说，安装了 Ultraschall 之后的 Reaper 已经完全变成了另一个专门针对播客创作者的音频工作站了。

很有趣的一点是，Ultraschall 是一个完全由德国的播客爱好者开发和维护的插件，在他的早期版本中甚至只提供德文的 changelog，并且至今也不提供官方的英文文档。这导致它即使在英文世界中的知名度也并不高。但是不用担心，Ultraschall 的软件界面是 100% 英文的，而且操作也很简单，只要是用过常见 DAW 的人，上手都不会有什么障碍。Ultraschall 是完全免费和非盈利的，但制作之精良、功能之丰富让我对德国的播客生态产生了一些好奇。

安装与配置
-----

虽然官方网站只有德文，但 Ultraschall 的安装包里提供了完整的英文安装说明，简单概括如下：

* 安装特定版本的 Reaper。由于定制程度非常深，所以 Ultraschall 推荐安装特定版本的 Reaper 而不是当前的最新版作为软件主体，参考安装包中的目前最新的版本对应的是 Reaper 5.70，可以在 Reaper 官网的 [历史版本下载页面](https://www.reaper.fm/download-old.php) 找到对应的 Windows 或者 Mac 版。

+ 如果你之前就已经安装并且在使用 Reaper，建议对当前版本进行备份或将之 [转换为便携版](https://www.lacinato.com/cm/blog/25-reaperportable)，因为 Ultaschall 很可能会跟既有的插件起冲突。好在 Reaper 只要是便携安装就可以支持多个版本同时存在，所以这个过程并不复杂。

* 安装 Ultraschall。最新的安装包可以在 [官网](https://ultraschall.fm/install/) 获得。
* 安装程序运行完毕之后，启动 Reaper，这时候你会看到一个主题文件缺失的警告，没有关系，点下一步进入程序主界面。
* 进入主界面之后，将安装包里的 `Ultraschall_3.1.ReaperConfigZip` 拖入主界面。Reaper 会弹出提示询问是否要导入配置，一路选是即可。
* 到这一步安装已经完成了，可以重新启动软件，如果没有弹出警告并且出现下方的画面就说明安装成功了。

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/F895C03C-D812-45D6-847E-EDDE27282DDB.gif)

导入配置

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/B06A4D94-01F1-46C2-BAFF-21D6C4DD9924.png)

启动画面

界面与基本逻辑 —— 为播客而生的 DAW 应该是什么样？
-----------------------------

Ultraschall 在 Reaper 基础上，为了播客制作增加了许多贴心的设定，对于与常规 DAW 相同的剪辑功能，本文不再赘述，主要挑选几点对于播客制作较为实用的进行介绍。

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/E98835A3-6280-4367-A7BB-48DC6DEE1C2F.png)

基本界面构成

### 贴心的菜单设计

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/23194AF8-D1E7-4BAA-891C-1820C88CE408.png)

Untraschall 的菜单栏

Reaper 原本的界面中附带了非常复杂的按钮设置，Ultraschall
则只留下了一组对于播客特别实用的，并且配上了定制的图标。图中的按钮从上至下，从左至右依次是：

* 缩放至显示完整的项目。
* 开启 / 关闭音轨窗口跟随播放进度滚动。
* 开启 / 关闭单音轨 ripple edit1 。
* 开启 / 关闭所有音轨 ripple edit。
* 插入章节标记。
* 插入章节标记并同时编辑内容。
* 在光标处分割音频。
* 切换鼠标左键拖动行为：选取 / 移动。
* 以 ripple edit 的方式删去所选的内容。
* 在当前音轨启用静音包络线 2 。

如果你曾经进行过播客剪辑，你会感受到这个按钮的布局一定是懂行的人做的，不多也不少。

### 强大而实用的工具

在 Reaper 原本的功能之外，Ultraschall 自己添加了一些针对播客制作的小功能，这些功能在其它的 DAW 软件中通常都难以实现，或是需要第三方的插件。例如：

#### 响度分析

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/3D28A08C-6814-4BB4-BC88-17F6E43FF513.png)

响度分析窗口

在剪辑视图中，在底部调音台窗口的旁边有一个 Loudness 的选项，可以方便的对项目中任意一个音轨（或是片段）进行响度分析，得到它的平均响度和动态范围等。这对与多音轨录音的播客剪辑有着极大的帮助，再也不用靠耳朵听来估计不同嘉宾的音量大小了。在传统 DAW 中，这个功能通常需要用第三方插件来实现，专业的音频分析插件非常昂贵（例如售价 $199 的 [iZotope Insight 2](https://www.izotope.com/en/products/insight.html)），而且其中大多数的功能可能播客创作者完全用不上，但这个小工具却把这个问题一键解决了。

#### Project Bay

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/BB3B4C03-5061-485D-86E8-A81EB9BC16E3.png)

Project Bay 窗口

在审阅（故事板）视图中，界面的右侧会出现一个 Project Bay 窗口，可以在其中看到项目中所用到的所有源文件和所有音频片段的列表。配合 Reaper 自带的 Media Explorer 功能，让录音文件和音效的管理变得格外便捷。如果你在 DAW 之外对某条音轨进行了单独的降噪和后期处理，你可以在这个窗口中方便地替换它。如果你使用了一些重复出现的音效，也可以直接从这个窗口中通过拖拽来将它放到音轨中。

#### Ultraschall Dynamics 插件

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/A1B07DA0-83AE-49BB-920A-11741BB3F5FA.png)

Ultraschall Dynamics 插件界面

Ultraschall 自己开发了一个叫作 Ultraschall Dynamics 的音频插件。虽然看起来不起眼，但它同时提供了播客常用的三大音频处理：限制器（limiter）、动态压缩（dynamic compression），和噪声门（noise gate）。这个插件只有三个参数，Target 规定了音轨的目标响度，Noisefloor 规定了噪音范围的上限，Noisegate 则规定了噪音范围的下限。简而言之，它可以做到：音量高于 Noisefloor 的声音会被压缩至接近 Target，而低于 Noisefloor 的声音会被压低，低于 Noisegate 的声音则会静音。具体的曲线则是自动计算的。这个插件提供了一个非常简洁但实用的音频处理操作，对于录音质量尚可的音频，你可能只需要用它就可以完成后期处理的部分了。5

导出章节标记一键完成
----------

Ultraschall 最直击我的痛点的功能当属它完善的导出系统。作为一个 DAW 软件，Reaper 自带的渲染菜单已经是非常强大了，支持几乎所有常见的音频格式，并且支持分段、分音轨导出。然而，正如开头所说，播客制作中的一些特有的需求，例如添加节目的单集封面和章节标记，目前仍然需要求助于第三方软件来完成。而 Ultraschall 的导出功能将这些需求集成到了 Reaper 中，成为了目前唯二可以直接在 DAW 中实现章节标记的方案之一 3 。

![](.evernote-content/DFE47466-26A9-449F-8B74-0FBDB5CA3BED/DB3DF063-6625-4CAA-A76A-6F7C0C997B7F.png)

导出窗口

* 点击主界面左下角的 Export Assistant 就可以呼出播客导出窗口，只要按照他提供的几个步骤，你就可以得到一个包含了完整的章节、封面、标题、作者名等元数据（metadata）的 .mp3 或 .m4a 文件。
* 第一步是调用 Reaper 原生的渲染功能，你可以选择你想要的码率和格式，将节目导出成 .mp3/.m4a 文件（目前这两种格式是唯二支持播客章节功能的音频格式）。
* Ultraschall 使用 Reaper 原生的 marker 功能来生成播客章节标记，因此如果你在剪辑时已经通过 marker 标记了章节，第二步就已经完成了，你可以点击第二步中的 View Chapters 来查看章节列表 4 。
* 第三步是编辑节目的元数据，你可以在这里填入节目的标题和作者。
* 第四步是插入单集封面，你只需要将封面的图片重命名为 cover.jpg (/jpeg/png)，再将其放到工程文件所在的文件夹中即可。
* 在这些步骤都完成之后，点击 Finalize MP3/m4a，选择你在第一步中所导出的音频文件，这些元数据就会被写入音频文件中。

总结
--

总而言之，对于播客创作者来说，Ultraschall 是一个难得的强大且趁手的工具，但由于语言的关系，成为了常见的推荐和选择中的遗珠。如果你已经在使用 Reaper 制作播客，或者正在寻找一个理想的工具，我强烈推荐你尝试 Ultraschall。它可以让新手更快更好地着手播客创作，对于老手也是有许多功能上的惊喜，Reaper 本体 $60 的售价加上无限期试用也比大多数的 DAW 软件要便宜。

Ultraschall 的官网上对自己的定位是 High-end Podcasting，我认为它的体验可以担得上这个名号。

[張奕源 Nick](https://sspai.com/u/nicholaszhang) 对本文亦有贡献。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57334)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7939910b-db31-4f0a-817b-aa3f3b9bad61/7939910b-db31-4f0a-817b-aa3f3b9bad61/)