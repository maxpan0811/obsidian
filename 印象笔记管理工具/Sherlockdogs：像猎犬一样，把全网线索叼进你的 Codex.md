# Sherlockdogs：像猎犬一样，把全网线索叼进你的 Codex

---

来源：[打开原文](https://mp.weixin.qq.com/s/wRw3RD_dvT8r9pEGjBn3Xg)

Sherlockdogs：像猎犬一样，把全网线索叼进你的 Codex
----------------------------------

你只管发给微信自己，剩下交给它

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/63D5A415-CF8F-4172-A0FB-A566A6594B39.jpg)

全网线索叼进 Codex
------------

先把爽点一次说透。

你看到任何有用的东西——一篇公众号文章、一个网页、一条小红书或 X 线索、一个抖音/B站/YouTube 视频、一份 PDF——顺手发给微信里的"文件传输助手"或你自己。剩下的不用你管。

它会自动落成 Obsidian 能打开的本地 Markdown 资料包，同时变成 Codex 可直接处理的上下文。你说一句"帮我拆观点""写成一篇稿"，Codex 已经拿着原文、链接和图片在干活了。

零复制、零截图、零补背景。

这就是 Sherlockdogs 想做的唯一一件事：把"发给自己"这个你早就有的动作，直接接到 Codex 的对话框里。

为什么"发给自己"是个黑洞
-------------

"发给自己"几乎是每个人的临时收件箱。看到好东西，先发给自己，回头再说。

问题是，它只负责收，不负责处理。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/3E02F3AE-0EDA-41BC-A26A-3A1D1BB28F80.png)

发给自己，收了就沉底
----------

等你真要用的时候，麻烦才开始：翻微信找那条消息、复制链接、把图片一张张存下来、打开 Obsidian、再打开 Codex，从头跟它解释这篇文章是什么、我要干嘛。

等你把这些搬运做完，最初那个"我想拆一下这篇的观点"的念头，早就凉了。

Sherlockdogs 接的就是这段断掉的路：发给自己的那一刻，处理就已经开始了。

一句话定位
-----

你在各个平台看到的内容，发给微信自己，Sherlockdogs 自动整理成本地 Markdown，直接送进 Codex 对话处理。

它不是云端剪藏，不是机器人账号，也不是"又一个收藏夹"。

它也不是把整个 Obsidian 乱丢给 AI，而是只把你主动发来的资料，整理成可追溯、可阅读、可交给 Codex 的本地包。

它是一个本地优先的入口：手机随手发 → 电脑本地整理 → Obsidian 可读 → Codex 直接接着干。

而且——你的内容全程不上传。

这一点我要说在最前面，因为下面会讲到它要读取本机的微信数据。你可能会担心安全，所以先讲清楚：数据一步都不离开你的电脑。不上传、不过任何服务器、不存云端。Sherlockdogs 只在你自己的机器上，读你发给自己的那条消息，整理成本地文件。仅此而已。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/547E00E4-86B4-4852-A809-E0DBDCCA55A1.jpg)

本地优先，全程不上传
----------

它到底长什么样
-------

讲再多概念，不如看一眼真实流程：一条内容从"发给微信自己"，到"在 Codex 对话里被处理"，中间我什么都没做。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/EC8290BB-C9DD-4C55-AF3D-5E02BD703558.png)

发给自己后，Codex 直接拿着原文开始处理
----------------------

关键在于：Codex 拿到的不是一段孤零零的文字，而是一份带来源的完整资料——原文、链接、标题、图片、附件、你发送的时间，都在。

所以你不用再交代背景，直接开口要结果就行。

这才是"让 Obsidian 给 AI 用"的正确形态：不是把整座库开放给模型，而是把新进来的资料先变成结构清楚、来源清楚、任务清楚的本地 Markdown。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/F87C0210-6B67-4DE9-96B6-991B6268D1E4.png)

文章带着完整上下文进入 Codex
-----------------

支持哪些渠道
------

一句话：来源不限，统一发给微信的自己。

• 公众号文章

• 网页链接

• 小红书、X（推特）线索

• 抖音、B站、YouTube 视频链接（先存标题、链接、封面、时长等线索，需要深解析时再进 Codex 任务）

• 临时文字笔记、想法

• 图片、PDF、文件

不管你平时混哪个平台，动作都一样：看到 → 发给自己。

能实现哪些功能
-------

内容进来之后，你能拿到两层东西。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/FEF3803D-EACC-4E64-B30A-B8FBA0F648CE.png)

产品功能一览
------

第一层，落成 Obsidian 友好的本地资料库：

• 自动生成本地 Markdown（raw.md、metadata.json、README.md和附件目录）

• 保留完整来源证据：从哪来、原文链接、图片、附件，全部留底，可追溯

• Obsidian 可以打开、搜索和沉淀；Codex 可以按原文继续处理；但本质仍是普通本地文件，不强绑定任何 App

第二层，直接进 Codex 对话开干：

发送时带一个简单标记（比如 #或 #2），这条内容就不只是被保存，而会生成一个 Codex-ready 任务。然后你在对话里可以直接让它：

• 摘要：基于原文和来源生成可追溯摘要，不是泛泛总结

• 拆观点：把里面的判断、论据、数据、案例拆开

• 找选题：从一条线索继续追问"我能写什么"

• 写草稿：把原始资料变成你自己的文章骨架、公众号初稿或素材卡

• 做资料库：把有长期价值的事实、图片、链接沉淀下来

Mac 和 Windows 都能用
-----------------

这一版，Mac 和 Windows 都已经跑通，而且走的是同一条主路径：读取本机微信数据库，识别你"发给自己"的那条消息，再在本地整理成资料和任务。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/4EB121FB-7431-4994-82B9-E196325F248A.png)

Mac / Windows 同一条主路径
--------------------

再强调一次，因为这关系到你敢不敢用：读的是你自己电脑上的微信数据，全程不上传、不过服务器、不存云端。Sherlockdogs 只读你发给自己的内容，落成本地文件，别的什么都不碰。

除了微信自聊这条主路径，还有一条不依赖微信数据的备用入口：iOS 快捷指令 / Inbox。从 iPhone 分享面板把链接、文本、图片、PDF 发送到 Sherlockdogs，同步进本地 Inbox 就能入库。适合想从浏览器、相册直接分享，或暂时不想走微信路径的场景。

第一次怎么用
------

不用研究太多，三步走。

1. 启动本机服务（双击启动程序，Mac / Windows 各有对应入口）

2. 连接微信自聊（双击连接程序，授权读取本机微信）

3. 发一条测试：手机微信给自己发一条带 #2的内容

看到本地 Markdown 生成，或看到 Codex 卡片出现，就说明主链路通了。之后日常使用，你只需要继续把东西发给自己。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/EAE0B6AF-E3F5-48A0-BBD4-0CFF256A28B2.png)

三步走
---

如果内容没进来，先别重装，跑一次自带的一键修复就好（具体命令见文末附录）。

这版的真实边界
-------

我不想把一个 public beta 吹成万能工具，边界讲清楚：

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/C2002709-8832-4DF9-A589-96FD8B9E9678.jpg)

公测阶段的真实边界
---------

• 本机微信数据库受微信版本、账号、路径和系统权限影响，不承诺每台机器都一次成功；遇到问题可以用一键修复和反馈工具回传线索。

• 视频链接当前以保存线索为主，深度解析需要按指令进入 Codex 任务。

• iOS 快捷指令 / Inbox 是正经的第二入口，不是废线——对不想碰微信数据的人很重要。

• Obsidian 是推荐阅读器，不是强依赖；最终产物是普通 Markdown 文件。

• 当前免费：public beta 阶段免费试用。

怎么下载
----

GitHub：

github.com/SherlockRobo/sherlockdogs

先看 Release 页面里的 START\_HERE.md，按上面说的三步走。第一次启动可能要等几分钟，先用一条最简单的内容测试：手机微信给自己发一个链接。

![](.evernote-content/FCEC9AF2-BEDF-4CA5-8525-AF0C61218541/319D0837-DC39-4F3C-9573-BAB4BE1B07DB.jpg)

GitHub 下载页
----------

最后
--

Sherlockdogs 做的不是"收藏更多"。

它做的是：把你已经随手发给自己的东西，叼回你自己的电脑，变成 Obsidian 可读、Codex 可处理的本地资料入口。

看到 → 发给自己 → Codex 直接开干。

这就是 1.0 public beta 想先跑通的事。如果你平时也常把文章、链接、想法发给自己，这一版应该会很快让你明白它爽在哪。

附录：技术细节（给愿意折腾的人）
----------------

Mac 操作入口

启动：Sherlockdogs Start.app  
连接微信：Sherlockdogs Connect WeChat.app  
查看结果：Sherlockdogs Open Output.app  
一键修复：Sherlockdogs OneTouchRepair.app（或 Repair Sherlockdogs.command）

Windows 操作入口

启动：Sherlockdogs Start.cmd（或 1 OneClick Install.cmd）  
连接微信：Sherlockdogs Connect WeChat.cmd（或 2 OneClick Configure.cmd）  
冒烟测试：Run Windows WeChat Smoke.cmd  
查看结果：Open Sherlockdogs Output.cmd  
诊断：Doctor Sherlockdogs.cmd（或 3 OneClick Repair.cmd）  
导出证据：Export Windows Evidence.cmd（或 4 OneClick Report.cmd）

iOS 快捷指令 / Inbox（跨平台备用入口）

iPhone 分享面板 -> 发送到 Sherlockdogs  
-> 同步到本地 Inbox  
-> 本机 Sherlockdogs 监听并入库  
-> 生成 Markdown / Codex 任务

下载目录

Mac：releases/1.0-public-beta/macos/  
Windows：releases/1.0-public-beta/windows/

反馈时最好带四样东西：Mac 还是 Windows；走微信自聊还是 iOS Shortcut；微信版本和系统版本；Doctor / Evidence 的结果。这样能快速判断问题卡在数据发现、数据读取、消息接收、任务生成，还是 Codex runner。

内部备注 · 标题备选（发布前删除本块）
--------------------

• 全渠道收藏，发给微信的自己，直接进 Codex 对话开干

• Sherlockdogs 发布：把公众号、小红书、抖音视频等收藏直接送进 Codex

• 看到 → 发给自己 → Codex 开干：Sherlockdogs 1.0 公测

• 不是收藏夹，是多平台信息到 Codex 的本地入口

• Mac / Windows 都能用：发给微信自己，自动进 Codex

[📎 在印象笔记中打开](evernote:///view/207087/s1/fdf4bbd3-de09-4ad4-a36d-2d367031e08d/fdf4bbd3-de09-4ad4-a36d-2d367031e08d/)