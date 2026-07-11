# 在 Mac 上便捷无痛升级 app 的全新姿势 —— MacUpdater - 少数派

---

在 Mac 上便捷无痛升级 app 的全新姿势 —— MacUpdater
=====================================

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/74E60B1A-5595-4799-A813-6756367D40D8)

在 Mac 上便捷无痛升级 app 的全新姿势 —— MacUpdater

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

在更新了 macOS Catalina 之后，有大量无法兼容的 app 出现了崩溃闪退或是卡死的现象。虽然在这些 app 都在短时间里发布了更新升级，逐渐兼容了新版本的 macOS。但这个更新的过程，却带给了我极其割裂的体验。

在这些 app 中，有一些是 Mac App Store 安装的，需要通过 Mac App Store 来升级。虽然体验很好，但也只是小部分；更多的则是通过 dmg 文件直接拖到应用程序或是 pkg 格式的安装包安装的，这类 App 就只能一个一个点开查询更新，特别繁琐；而还有一些如 Adobe 全家桶这类 app，则是要通过自家的应用管理器来升级……

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/BD06EA62-C3BD-41D0-9B40-BB2AD755206E.png)

这就让我思考一个问题：有没有一个能够管理所有 app 升级的工具，能让我实现在一个 app 内完成 app 下载和更新？

答案是有的。

**CleanMyMac X**
----------------

在之前发布的全新 CleanMyMac X 中，有一个「更新程序」的功能，可以通过它实现对部分 app 的一键升级。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/3981F7AD-7DE2-49CD-967D-D83DEC6CB714.png)

用法和 Mac App Store 类似，CleanMyMac X 会自动搜索可以更新的 app，然后点击自己需要更新的 app，再点击下方的更新按钮，CleanMyMac X 就会自动帮你完成升级。

加上 CleanMyMac X 优秀的 UI 设计，使用体验上来说还是很「惬意」的。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/EB69DBA1-22BE-4B8D-A728-703348EE5AA6.png)

但是在使用中，我却发现了一个致命问题：它并不能更新系统内所有的 app。

通过万能的 Google 搜索之后我发现，CleanMyMac X 仅支持来自 Mac App Store、自家的 Setapp 以及基于 Sparkle 的 app，对于其它来源的 app 则无能为力。

那么，什么是 Sparkle？按照其官方网站的介绍，Sparkle 是一个用于 macOS app 中的开源软件更新框架，可以实现真正的自主后台静默更新。然而梦想很美好，现实却很残酷。这种主动需要开发者去适配的框架，必然不能顾及到所有的 app。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/13D73AC9-F8C7-4A4E-BD87-95680506BBE6.png)

而且 CleanMyMac X 极高的售价，相信也让一些人望而却步（虽说「附带」了一个清理功能）。那么，有没有一款更好用的 app 管理升级呢？

**MacUpdater**
--------------

[MacUpdater](https://www.corecode.io/macupdater/)，堪称 Mac 上管理 app 更新的「瑞士军刀」。

它不仅没有上面 CleanMyMac X 的局限，而且在使用体验上也极为优秀。如果偏要找什么缺点的话，那只能说 UI 没有 CleanMyMac X 好看，以及图标还是复古的「拟物风」吧。

首先，MacUpdater 会每天定时扫描你所有的 app，查询他们是否有更新。如果你觉得每天扫描太频繁，你还可以根据自己的需求，选择每两天、每周、每两周或每个月扫描一次。当然，不想让 MacUpdater 自动扫描的话，还可以选择从不自动扫描。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/2A157654-A3BE-40A5-9929-BF193C6B7017.png)

扫描完毕，可以更新的 app 会出现在「Outdated Apps」里，你可以通过旁边的分类查看这些需要更新的 app。下方的列表，就是所有可更新的 app 列表。

MacUpdater 会列出你当前 app 的版本，以及发现的最新版本，点击最右侧的升级，就能一键升级对应的 app 了。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/EA019BDA-849E-436B-BBAF-0E4774364741.png)

点击升级旁边的「i」，还可以查看详细的更新信息，包括软件的更新说明、开发者、甚至是软件主页和安装来源。如果你发现 MacUpdater 有信息错误或是更新问题，还可以点击「Report App Feedback」给他们发送反馈。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/2705F657-E4CF-4B82-A26D-B79646382C2D.png)

另外，你也可以通过右键，来对 app 的更新进行详细操作。例如忽略此次更新，或是完全忽略这个 app 的所有更新，以及打开 app 所在位置、重新扫描等。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/E1D43BFF-6586-4E2E-ACC3-474D5DA5A3DE.png)

在最下方还有一些相关的信息，比如你的 Mac 里共安装了多少款 app，有多少款是最新版本，有多少是需要更新的，以及上一次扫描和下一次扫描的时间。

需要提醒的是，如果是 MAS 来源的 app，MacUpdater 能够扫描出来，但无法再 app 内升级，需要跳转到 MAS 进行操作。而对于非 MAS 的 app，就可以在 MacUpdater 一键无痛升级。

来到设置界面之后，你会发现，MacUpdater 的自定义程度极高，能够覆盖不同人群的各种使用偏好。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/37F887F0-FFE0-4223-BB98-80A22DD5BAAD.png)

在这里我就不具体详述每一个细节，着重介绍其中一个：升级备份。

一般来说，app 更新之后都会有新功能或 bug 修复，但有些 app 并不是升级到最新就是最好的，甚至会出现新 bug 或是不兼容的问题。

MacUpdater 也考虑到了这点，因此提供了升级前备份的功能。在设置页面下的「Scanning & Updating」的选项卡里，有一个「Keep Safety Backups」的选项，勾选之后就可以开启这项功能。你不仅可以自定义存储几个版本的 app，还可以自定义备份的位置，又或者是将更新下载的 app 也备份一份。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/383D79B6-CA31-4ED1-BAED-DECB388C18A0.png)

实测后发现，MacUpdater 最多能备份 99 个旧版本以及 99 个新版本的内容，简直令人震惊……

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/AE53958D-ED31-493A-AF54-78F82F0790DE.png)

对了，MacUpdater 很让我佩服的一点是，有一些 app 更名或是更改了升级策略之后，它都能够扫出来。例如之前我在用 WindowTidy 2.1.5 版本的时候，MacUpdater 就找到了一个 1.2.6 版本的升级，我就很奇怪，怎么还会「降级」呢？

点了一下升级发现，它警告我这可能是一个重大个 app 更新版本，因此更新后或许需要一个新的许可。另外 MacUpdater 还提示，WindowTidy 已经停止更新，而且被一款全新的 app Mosaic 所取代。

![](.evernote-content/BEC8B165-F9FA-4482-90A0-F21CDBB588F2/1325649B-0657-4ECE-AC62-CEF63E954F03.png)

需要说明的是，[MacUpdater](https://www.corecode.io/macupdater/) 虽然并不是一款免费的软件，但也提供了免费试用。在试用期间，你可以升级 10 款 app，超过之后就需要购买了。

如果你也是一个「更新强迫党」，那我还是很推荐这款 app 的，售价 9.99 美元（约合人民币 71 元），买断制而非订阅制。

反正买一个也不贵，按照 Apple 现在的写 bug 速度，每年秋天肯定都是能派上大用场的嘛。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，解锁更多应用与技巧

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57846)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d5d36301-a46f-4517-8eba-608416d0a604/d5d36301-a46f-4517-8eba-608416d0a604/)