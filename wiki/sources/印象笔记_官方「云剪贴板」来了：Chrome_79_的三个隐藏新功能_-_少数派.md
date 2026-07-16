---
title: "官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能 - 少数派.md
tags: [印象笔记]
---

# 官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能 - 少数派

# 官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能 - 少数派 --- 官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能 ============================

---

# 官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能 - 少数派

---

官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能
=============================

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/F6721FDE-07D6-46FD-8933-D358EE941357)

官方「云剪贴板」来了：Chrome 79 的三个隐藏新功能

本周，Chrome 79 正式版开始向 Windows、Mac、Linux、Chrome OS 以及移动设备全面推送，此前在其它测试版本中的一些实用功能，包括跨设备共享剪贴板、标签页冻结等等，在这次更新后也终于来到了稳定版当中。

在这篇文章中，我们就来一起看一看 Chrome 79 正式版最实用的三个新功能。

和 Android 设备共享剪贴板
-----------------

更新到 Chrome 79 正式版后 Google 为我们带来了官方版本的「云剪贴板」。

要开启这个云剪贴板，我们首先需要保证移动端和桌面端 Chrome 均更新至 Chrome 79 正式版本，同时移动端和桌面端 Chrome 登录同一 Google 账号即可。在此前提下，如果在桌面端浏览网页并选中特定文字，右键菜单顶部应该就会出现「复制到您的设备」选项（如下图）。

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/7C9C047B-1980-45B9-AF6D-3B3B70BB266D.png)

如果你没有看到类似的选项，就需要在 chrome://flags 页面中搜索关键词「**clipboard**」并开启下面这三个功能标签：

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/805ECAD0-6B77-4DCE-802B-D1C737522669.png)

对移动端而言云剪贴板的开启方式类似，不过需要注意的是我们只需要在移动端的 chrome://flags 中搜索同样的关键字并开启以下两个功能标签即可：

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/B480FFCE-093C-4E15-87F3-971095F5AA3E.png)

另外，在 Android 平台上的操作也与我们日常的文本复制方式略有区别。为了和系统自带的剪贴板内容进行区分，在移动端选中需要发送到桌面端的文本后我们只能选择打开 Android 系统的「分享」菜单，然后找到 Chrome 浏览器的「发送文本到您的设备」才能呼出跨设备复制选单。

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/C71B8662-B426-42BA-9183-4B5AFC2D4CDB.png)

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/76DCC2C0-1727-4ECC-A37A-FBEFB13E6C92.png)

实际使用效果上来看，移动端发送文本到桌面端的操作显然是相对有些繁琐的，但云端跨设备复制过程过程的提示倒是十分清晰。另外和 [剪纸云](https://sspai.com/post/52305) 走 FCM 推送的方式不同，Chrome 这个功能经测试走的是 Chrome 账户同步服务器，换句话说，**它对网络条件的要求有些苛刻**（虽然对主力 Chrome 用户来说这方面应该也都没问题吧）。

另外，我们经过测试也发现，这个功能目前仅支持 Android 和 Windows 平台的 Chrome 浏览器。

「冻结」非活动标签页，省电省资源
----------------

一直以来 Chrome 浏览器都有着对系统资源占用较大的问题，随便打开几个标签页内存很可能就会占用超过 4GB 以上，如果打开标签页较多的话，就会让整个系统都会异常卡顿。

而 Google 在 Chrome 79 稳定版当中引入了一项名为「标签页冻结」的新功能，其作用是如果打开的标签页有五分钟以上没有活动，那么该标签页的资源将会被冻结，并释放 CPU 和内存资源。当用户再次切换回该标签页时，则会自动刷新重载。

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/C2811F21-C678-4439-8F00-9BFCE1022753.png)

当然这个功能会排除掉一些特殊的情景，比如说如果非活动标签页正在播放音视频内容，那么标签页即便是超过五分钟没有活动也不会被释放资源，这样避免在收听内容时出现中断。

目前该功能虽然已经出现在 Chrome 79 但尚未默认开启，你可以在 chrome://flags 中找到 `#proactive-tab-freeze` 进行开启。

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/09486B94-3128-45C6-90F2-A7213CB27F7C.png)

新的标签页分组样式

另外，标签页分组样式在这个 Chrome 79 中相比之前也略有调整，感兴趣的读者不妨参阅我们之前的文章。

**关联阅读：**[用好这些隐藏「小开关」，让 Chrome 浏览器更好用](https://sspai.com/post/57430)

密码泄露风险提醒
--------

此前 Google 曾经上线了在线版本的密码检查服务，通过授权登录形式可以检查账户下的密码是否存在泄露的风险，同时在此之前 Google 也专门开发了一款「密码安全检查扩展程序」，当用户在网页上输入密码时将会得到提示，以确定是否存在泄露风险。

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/5BFF615B-468B-4FD9-A731-690F3B7DE206.png)

而从 Chrome 79 开始，这项功能被完全集成到 Chrome 浏览器中，无需安装扩展软件，当你在网页中使用密码服务时将会自动分析你输入的密码，根据 Google 分享的工作原理，用户输入的密码信息将会被加密并发送给 Google 进行分析，在保证安全的同时还做到了用户名保持匿名。最后 Google 将会对给出相应的解决方案和建议。

![](.evernote-content/CF6D6A50-D65A-4943-BC25-F8EA9EEB25E5/18947332-314D-4A49-A7E7-98295BD4703C.png)

目前该功能尚未在 Chrome 79 全量上线，即便在 chrome://flags 中开启了相关的功能标签（`chrome://flags/#password-leak-detection`）选项也无法直接激活相关设置，因此我们推测这可能是一项服务器端更新。

其它新特性
-----

除了本文介绍的这三个实用功能，Chrome 79 正式版也带来了更好的 WebXR 支持（可以改善网页 VR、AR 内容的体验），更好的网页浏览安全性（默认启用 [DoH](https://sspai.com/post/56783)、弃用 TSL 1.0 和 TSL 1.1、默认屏蔽更多危险的「[混合内容](https://www.howtogeek.com/443032/what-is-mixed-content-and-why-is-chrome-blocking-it/)」）以及 Web 应用蓝牙扫描支持等等新特性。

此前部分仅存在于 Beta、Canary 等测试版本中的 feature flags 同时也下放到了 Chrome 79 正式版本，包括通过缓存页面来加速前进、后退操作的 `#back-forward-cache`，感兴趣的话你也可以前往 chrome://flags 搜索并开启。

### 参考资料

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，找到更多 Chrome 使用小技巧、实用插件

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57839)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0a3ff564-3e18-4138-a043-c4cadbecc90f/0a3ff564-3e18-4138-a043-c4cadbecc90f/)