# 如何自动化你的 Mac？更智能办公的初学者指南

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0MzU5NzQ4Mw==&mid=224749...](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247490896&idx=1&sn=3a17903a589544c55c87723dbe373a92&chksm=c2d7547d954a84112dc0d194702d88e7a05388ec9a08b5bf4a42fb76a8ec58f0be8085a43070&scene=90&xtrack=1&sessionid=1745229156&subscene=93&clicktime=1745229573&enterid=1745229573&flutter_pos=8&biz_enter_id=4&ranksessionid=1745229406&jumppath=20020_1745229406172,1104_1745229478021,20020_1745229486567,1104_1745229568728&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003a25&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjhw9uMdlTiR2wnmJjDBeoBLYAQIE97dBBAEAAAAAAN6+MRiWVGAAAAAOpnltbLcz9gKNyK89dVj0h5wmST2B1+UZgCM+I5FfNPEqTIevNT6qBi/RN7+Xl8G/61ExAeazid40Ojgvi0+AEsMRFDIp4AalSvQnmsEXt66myo6BUmgpvX0WNTvFInKHJaRJCMPJkyxN5HEOgFfewdWF/pkIP5JH4aEFFrwZQA8dRnv3tXqHA0bhH59SqY61ERdMjy5IEqRNi3DZmHt1JGwBLG85W59sg/TRBQpSg+Yy/oe0Aac4sTjYA5ApUyi0UA==&pass_ticket=Z6HNqAbhPMoE+uohVkJjwXBUpnj6sfkhQ9hS0INWH6DpctOMO+aewW4inrwbX7uj&wx_header=3)

原创 点蓝色字关注👉 程序员echo

每天，我们在 Mac 上执行无数任务，甚至不需要思考。这些小动作——重命名文件、打开常用应用程序、整理下载文件——都在无形中增加了工作流的摩擦。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/7B673AE9-93DF-48F8-A935-09FA027BCD77.png)

你是否注意到，一个本来只需要 30 秒的小任务，会让你从专注的项目中分心？

其实你不需要成为专家，也不需要懂任何编程——学习自动化，完全可以利用 macOS 上已有的工具。

最简单的入门方式
--------

*Shortcuts*（快捷指令）是最适合初学者的自动化工具之一，而且每台 Mac 上都默认安装了这个应用。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/44744179-4BF0-4614-A529-5EF1C0E752CF.png)

这个应用的概念非常简单——将多个操作链接在一起，方便从一个地方启动。它使用简单的拖放界面，就像 LEGO 积木一样。

这些快捷指令可以很简单，也可以很复杂。

有些指令的链条可能只是一起启动应用程序、批量重命名文件、设置焦点模式、将文本转换成语音，或者其他一些简单的操作。

但是，Shortcuts 还能做更多事情。我们先从简单的开始。

学习使用 Shortcuts
--------------

**步骤 1：** 打开 Spotlight（按下 Command + 空格键），输入 "Shortcuts"，然后按回车。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/8B1DA0E8-6FFA-46D8-A420-259E38E0CCC2.jpg)

**步骤 2：** 点击右上角搜索栏旁的小加号图标。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/D96699A6-1E15-46E4-8378-1FB55157ED55.png)

你现在创建了一个空白的快捷指令。

下面是一个例子，但我们将从零开始创建一个简单的快捷指令。在这个界面中，注意右侧有许多可以执行的操作——这些是我们想要自动化的动作。

我们可以将它们拖到左侧，像拼积木一样组成我们想要的自动化动作。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/7DCB4B29-9FD7-4D83-B8BD-CB3B71DBC2B4.png)

选择一个操作，并设置相关参数，创建一个动作链。

一起来试试！
------

我的目标是创建一个简单的链条，打开 Spotify，并将其调整为适合屏幕的大小。

首先，搜索 "打开应用程序"（Open App）操作，将其拖到左侧面板。然后，从下拉菜单中选择你想要打开的应用——在这里选择 Spotify。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/21EC90B3-89BA-4042-94C4-3EA1A266F7DC.png)

接下来，要调整窗口大小，可以使用 "调整窗口大小"（Resize Window）操作，将其拖到 "打开 Spotify" 操作的下方。

你会注意到两个操作之间有一条白色的线，表示这两个动作已经连接在一起。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/D2D1E38E-5818-4F76-ADEF-4F183BFE257B.png)

就这样！现在只需要给快捷指令起个名字，像 "打开 Spotify"。你也可以自定义图标。既然 Spotify 是一个音乐应用，图标是绿色的，我也给快捷指令设置了一个类似的绿色图标。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/1F35A569-50F9-4646-B161-CE97097A01D2.png)

当我们将这些指令结合起来，设置好合适的大小调整操作，效果会非常美丽且满足：

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/030294AD-F609-416A-89F1-1F0960F0DA8D.png)

冰山一角
----

打开和调整应用程序的大小，算是最简单的操作了。

但 Shortcuts 的功能远不止这些。它与第三方软件集成，可以操作日历和待办事项，打电话、运行 shell 命令，甚至将一个快捷指令嵌套在另一个指令中。

理论上，可能性是无限的。

高效使用 Shortcuts
--------------

为了更高效地使用这些快捷指令，有三种主要方式：

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/559F907D-B1FE-4C32-908D-580EB5F677BE.jpg)

1. 使用 Spotlight（Command + 空格）快速查找并运行快捷指令。
2. 将快捷指令作为桌面小部件添加。
3. 或者手动在 Shortcuts 应用中使用它们（不推荐）。

#### 使用 Spotlight

这是最简单的方法。

只需按 Command + 空格，输入 "打开 Spotify"，然后按回车键。

#### 将 Shortcuts 添加到桌面小部件

右键点击桌面，选择 "编辑小部件"。在弹出的菜单中，搜索 Shortcuts 应用，并选择你喜欢的小部件大小。

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/5059BDC0-F447-49C7-B360-3E1A46391117.png)

然后，将其拖放到桌面上。

现在，只需点击桌面上的小部件，你的快捷指令就能运行啦！

进一步资源
-----

掌握这种工具可能需要一些时间。

幸运的是，你不必从零开始，因为很多人已经为你做了这些，并乐于分享他们的快捷指令。以下是一些资源：

* **RoutineHub**：这几乎是 Shortcuts 的 GitHub，用户在这里发布、版本控制和更新他们的快捷指令。你可以按照类别（生产力、实用工具、媒体等）浏览。
* **MacStories Shortcuts Archive**：由 Federico Viticci 创建，这是苹果界非常受尊敬的博主之一。他为 iOS 和 macOS 设计了许多先进且文档详细的快捷指令。
* **Reddit — r/shortcuts**：一个发现小众或有趣自动化的好地方，你可以在这里寻求帮助和反馈。

结语：让你的 Mac 为你服务
---------------

到目前为止，你应该对如何通过几个巧妙的工具将你的 Mac 从一个被动的设备变成一个积极的助手——几乎像一个日常工作的副驾驶——有了一个不错的了解。

如果你不想从头开始构建快捷指令，也可以随时在线搜索别人已经创建好的快捷指令。本期的分享到这了，下期我们再见！！！🚀

![](.evernote-content/9DE57FF7-CF6F-4429-B1FA-F400A6AC0BEE/074782B1-6EE7-4120-97BC-519B8C7EE5DA.gif)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247490896&idx=1&sn=3a17903a589544c55c87723dbe373a92&chksm=c2d7547d954a84112dc0d194702d88e7a05388ec9a08b5bf4a42fb76a8ec58f0be8085a43070&scene=90&xtrack=1&sessionid=1745229156&subscene=93&clicktime=1745229573&enterid=1745229573&flutter_pos=8&biz_enter_id=4&ranksessionid=1745229406&jumppath=20020_1745229406172,1104_1745229478021,20020_1745229486567,1104_1745229568728&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003a25&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjhw9uMdlTiR2wnmJjDBeoBLYAQIE97dBBAEAAAAAAN6+MRiWVGAAAAAOpnltbLcz9gKNyK89dVj0h5wmST2B1+UZgCM+I5FfNPEqTIevNT6qBi/RN7+Xl8G/61ExAeazid40Ojgvi0+AEsMRFDIp4AalSvQnmsEXt66myo6BUmgpvX0WNTvFInKHJaRJCMPJkyxN5HEOgFfewdWF/pkIP5JH4aEFFrwZQA8dRnv3tXqHA0bhH59SqY61ERdMjy5IEqRNi3DZmHt1JGwBLG85W59sg/TRBQpSg+Yy/oe0Aac4sTjYA5ApUyi0UA==&pass_ticket=Z6HNqAbhPMoE+uohVkJjwXBUpnj6sfkhQ9hS0INWH6DpctOMO+aewW4inrwbX7uj&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/507de9e9-fec7-43bb-8355-f5d63b194322/507de9e9-fec7-43bb-8355-f5d63b194322/)