---
title: "把 iOS 上搞不定的下载远程交给 Mac：Transloader 测评 [送码]"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/把 iOS 上搞不定的下载远程交给 Mac：Transloader 测评 [送码].md
tags: [印象笔记]
---

# 把 iOS 上搞不定的下载远程交给 Mac：Transloader 测评 [送码]

# 把 iOS 上搞不定的下载远程交给 Mac：Transloader 测评 [送码] --- ![](.evernote-content/325FA23A-A0BD-43C8-8ECE-271973

---

# 把 iOS 上搞不定的下载远程交给 Mac：Transloader 测评 [送码]

---

![](.evernote-content/325FA23A-A0BD-43C8-8ECE-271973201444/33361295-DDC6-482B-888F-64BA30C180E1.jpg)

第一次接触 Transloader 的时候我误以为它是迅雷离线的进化版，能做到手机这里上传种子到离线，电脑那边离线完以后会直接下载到电脑上。上手了以后发现我错了，不过也没错太多。Transloader 虽然并不能读取种子等含有特殊协议的文件，但是只要你在 iOS 端给它一个**可下载格式**[1](http://sspai.com/31924#fn1)的文件下载链接，Mac 端那边就能帮你下载下来，比如 `.zip`, `.dmg`, `.app`, `.pdf`, `.mp4` 等等。

这就足够实用了，比如对于普通的 Mac 用户，你可能会在上下班途中阅读 RSS 的时候发现一些有意思的软件，这时候你就可以用 Transloader 让家里的电脑先帮你下载下来，回家后就可以直接安装使用。或者对于越狱的人，通过 [Workflow](http://sspai.com/tag/Workflow) 可以做到在通知中心点几下就能让家里的 Mac 开始为自己的某个设备下载最新的固件。

Transloader 基本用法
----------------

Transloader 分为 [iOS 端](https://itunes.apple.com/app/transloader/id572280994?mt=8&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw)和 [Mac 端](https://itunes.apple.com/app/transloader/id572280994?mt=8&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw)，iOS 端负责上传下载链接，通过 iCloud 将下载链接同步到 Mac 端，然后 Mac 端执行下载，将文件下载到你选择的文件夹（默认是`下载`文件夹）。

![](.evernote-content/325FA23A-A0BD-43C8-8ECE-271973201444/33157DC2-9A19-4784-A6F9-080ED1AC051A.jpg)

当在 Mac 端下载完成后，iOS 端上该文件前面会出现一个小对勾表示下载完成。

![](.evernote-content/325FA23A-A0BD-43C8-8ECE-271973201444/87AC7FB7-0BEB-471B-A1C0-1330ADA7EF00.jpg)

在 iOS 端正常添加链接的方法有两种，一是通过 App 界面右上角的 `Add` 按钮，然后把复制好的下载链接粘贴进去就好。二是通过 Sharesheet，这是在 2.1 版本中更新的新功能，很实用。

![](.evernote-content/325FA23A-A0BD-43C8-8ECE-271973201444/3CF78A5D-BED0-4327-B1BF-269B2851066C.jpg)

如图所示，当你打开一个软件的主页，这个页面如果带有下载按钮，你就可以使用 Transloader 在 Sharesheet 中的插件，直接在网页里选择你想下载的文件。整个过程，连 Transloader 这个 App 都不需要打开，你的 Mac 就能在家里将软件给你下载好。

除此之外，Transloader 还有个比较简陋的通知中心部件，方便你在通知中心查看文件是否下载完毕。

进阶用法
----

*通过 URL Schemes 跟其它效率应用或软件搭配使用，在 Mac 上直接完成文档的分类。*

Transloader 的 URL Schemes 只有两项，非常简单：

* 打开 App：`esstransloaderios://`
* 打开 App 并直接下载剪切板链接：`esstransloaderios://addfrompasteboard.at`

第二项 URL Schemes 可以让我们直接把动作放进 [Launch Center Pro](http://sspai.com/tag/Launch%20Center%20Pro) 或者 [Launcher](http://sspai.com/tag/Launcher) 这样的 App，以便我们更快地调用它。说实在的，我用了 Transloader 这么久，根本不知道它在我手机里哪一页的哪个文件夹里，都是直接用第二个 URL Schemes，把链接发过去就了事儿。一个好的工具类 App 就该这样，用得着的时候瞬间能用，用不着的时候毫无存在感。

除了临时要添加的下载任务，作为一个越狱的人，在越狱发出的时候及时下载固件也是时常会遇到的使用情境。而且固件这玩意都不小，一个多 G 的固件，到家再下和在家下好等着你区别还是很大的。我在[《征服 Workflow 中的最高峰》](http://sspai.com/30870)里详细写过如何做到这一点，其中最重要的工具当然就是 Transloader。

除此之外，如果你是一个软件媒体作者，需要经常测试各种软件，你可以在 Mac 上结合 [Hazel](https://www.noodlesoft.com/hazel.php) 来制定规则，来分类软件，比如不同的格式可以放到不同的文件夹中等等。

结语
--

Transloader 是一款典型的工具类软件，你可能不会那么常用它，它也不会来烦你，但如果哪天需要用到它，就会觉得手头有这么一样东西简直是万幸。

你可以分别在 [App Store](https://itunes.apple.com/app/transloader/id572280994?mt=8&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw) 和 [Mac App Store](https://itunes.apple.com/app/transloader/id572281534?mt=12&uo=4&at=10lJSw&uo=4&at=10lJSw) 下载 Transloader，[iOS 版](https://itunes.apple.com/app/transloader/id572280994?mt=8&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw&uo=4&at=10lJSw)免费，[Mac 版](https://itunes.apple.com/app/transloader/id572281534?mt=12&uo=4&at=10lJSw&uo=4&at=10lJSw)售价 40 元。

1. 关于可下载格式你可以这样理解，Safari 能下载的它都能下载。 [↩︎](http://sspai.com/31924#ffn1)

### *送码*

评论说说你在 iOS 或 Mac 上的下载习惯和需求，我们将于下周四（11.26）挑选出 **3** 条优秀评论，送出由开发商提供的 Transloader for Mac 兑换码，共 3 枚。

或者去少数派微博参与转发抽奖，另送 2 枚。

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[把 iOS 上搞不定的下载远程交给 Mac：Transloader 测评 [送码]](http://sspai.com/31924)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/325FA23A-A0BD-43C8-8ECE-271973201444/97E901F0-05C8-4850-8C14-2A318B81E01A.jpg)](http://aos.prf.hn/click/camref:111l75A/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fshop%2Fbuy-ipad%2Fipad-pro)

---

[🌐 原始链接](http://sspai.com/31924)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4e923036-f6bd-4b14-9866-dd46152e0bd3/4e923036-f6bd-4b14-9866-dd46152e0bd3/)