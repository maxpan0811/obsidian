---
title: "具透 _ iOS 10.3 终于来了，这些新变化你应该知道"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/具透 _ iOS 10.3 终于来了，这些新变化你应该知道.md
tags: [印象笔记]
---

# 具透 _ iOS 10.3 终于来了，这些新变化你应该知道

# 具透 | iOS 10.3 终于来了，这些新变化你应该知道 --- 在测试版本号记录一再被刷新后，iOS 10.3 在凌晨终于正式发布了。新版 iOS 带来了新的 Apple ID 页面和 App

---

# 具透 | iOS 10.3 终于来了，这些新变化你应该知道

---

在测试版本号记录一再被刷新后，iOS 10.3 在凌晨终于正式发布了。新版 iOS 带来了新的 Apple ID 页面和 App Store 评分机制，以及包括 Find My AirPods、剧场模式和 Apple File System 在内的不少新功能。少数派第一时间为大家整理了 iOS 10.3 中值得关注的新变化。

### 新的 Apple ID 页面

更新后，打开系统设置，出现在最上方的便是新的 Apple ID 页面。你可以在这里查看和更改 Apple ID 的各项设置，管理你绑定的设备。

![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/B03F897F-C2BA-4B81-873B-535C99A2EA00.jpg)

iOS 10.3 同时带来了新的 iCloud 储存空间展示页面。在 Apple ID 中点击 iCloud 选项，你可以直观地了解 iCloud 储存空间的使用情况。

![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/C5AA0364-8C9B-4AE3-ABBC-D7733646EF52.jpg)

### 允许 App 内评分及留言

大部分的开发者都非常重视 App Store 的用户评分和评价。在 iOS 10.3 中，开发者可以利用新的 API 在 App 内通过弹窗的方式请求用户直接给出评分，不再需要前往 App Store。

![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/96231484-08E4-400E-9191-758F9C95D447.jpg)图／macstories.net

当然， 为了防止这个功能被滥用，Apple 限制每一个 App 每年只能弹窗 3 次请求 App 内评分。不过，开发者依然可以使用原来的弹窗方式请求用户到 App Store 评价。此外，在 iOS 10.3 中，开发者可以对用户在 App Store 中的评价给予回应。

[![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/F657A505-D4DA-4148-A3E8-04480C148071.png)](https://twitter.com/gruber/status/824022727870861316?ref_src=twsrc%5Etfw)

用户还可以在 App Store 中在针对某一条评论使用 3D Touch 来评价其是否有帮助。

### 

### Apple File System （APFS）

在你升级 iOS 10.3 后，如果你发现打开应用、切换后台应用时「感觉」比之前流畅了，或者发现设备的可用存储空间莫名变多了，这些都是 Apple 新引入的全新文件系统 APFS 的功劳。作为旧有文件系统 HFS+ 的替代品，基于 SSD 开发的 APFS 对 Apple 大多部分设备有更好的性能和兼容性。

对我们用户来说，升级 APFS 并不需要任何额外操作，iOS 会自动在系统升级过程中完成 APFS 升级**（仍建议在升级前做好备份）**。而之所以在升级 iOS 10.3 后设备可用空间会增加，是因为在 APFS 中，拥有同样名称的文件在系统中仅占用一次空间。例如，你将一个大小为 1GB 的文件复制 10 次，在以前的 HFS+ 中，系统会存储 10 个不同的备份，共占用 10GB 硬盘空间。而在 APFS 中，即使你复制 100 次，该文件在你的设备里也只会占用 1GB 空间。

打开和切换后台应用时会「感觉」更流畅，则是由于 APFS 在控制应用运行的优先级上有调整。

此外，APFS 比 HFS+ 拥有更好的安全性。相较于 HFS+ 在 macOS 上的硬件级加密和 iOS 上的文件级加密，APFS 采用了级别更高的系统级加密，并支持 AES-XTS 和 AES-CBC 等加密方式。

APFS 虽然有许多优势，但它也对开发者也提出了新要求。在 iOS 10.3 中，当你打开一个 32 位应用时，系统会提醒你这个应用可能在未来 iOS 版本中不再被支持，开发者需要开发 64 位应用来适配 APFS。

关于 APFS 文件系统，少数派已经专门写了另一篇文章详细讲解：[《升级 iOS 10.3 后存储空间变多了？这都是 APFS 的功劳》](https://sspai.com/post/38377)

![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/2162EAE0-85DA-40BA-9EB7-D32B79256DE5.jpg)

### Find My AirPods

作为 AirPods 用户，你是否曾遇到过找不到某一只 AirPods 的窘境？为了帮助你寻找 AirPods ，iOS 10.3 中新加入了 Find My AirPods 功能。

打开**查找 iPhone** ，你可以在设备列表里看到 AirPods 的当前位置。当你需要寻找 AirPods 时，点击**播放声音**，系统会提醒你摘下 AirPods 以避免听力受损。点击确定后 AirPods 会发出铃音，方便你确定位置。

![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/30236472-3333-4437-966F-87563EA68E6B.jpg)

### Apple Watch 中新增剧场模式

此前被曝光的剧场模式并没有被加入到 iOS 中 ，而是被放到了 watchOS 3.2 的控制中心里。

![](.evernote-content/8F5D503F-2A3A-4A3D-9D61-8B5690545689/4A598F3B-7BE3-4CEF-A5A1-B4830B6469B6.jpg)

在 Apple Watch 上打开该模式后，抬腕唤醒将被关闭。收到通知时，你需要点按屏幕或按下 Digital Crown 才能唤醒屏幕查看通知。

其他变化
----

* 播客拥有了 Widget；
* 在地图里对温度使用 3D Touch 会出现天气预报（[图](https://cdn.sspai.com/2017/03/28/5d0708611c3f95f97d91e5176cbf7fb5.jpg)）；
* 在日历里你可以删除邀请并举报为垃圾信息；
* SiriKit 允许第三方应用使用 Siri 进行支付；
* CarPlay 会在侧边栏显示最近打开的 3 个应用，音乐 App 界面被重新设计；
* 系统不再支持设置单个字符的密码，最低要求为 4 位；
* **诊断&用量**被整合到系统设置里隐私中的分析页面，新增**共享 iCloud 分享**选项；
* 打开和关闭 App 时， 动效比之前的圆角弧度更大 ；
* Safari 支持辅助功能中的减弱动态效果；
* 开发者可以随时更新 App 的图标（更换图标前需要得到用户许可），不再需要通过更新 App 实现 。
* 在系统更新时，按下电源键会出现「iPhone/iPad 将会在更新完成后重启」的提示。

---

[继续阅读少数派更多 iOS 10 详解文章 >](https://sspai.com/tag/%E5%85%B7%E9%80%8F)

---

[🌐 原始链接](https://sspai.com/post/37481)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b39a5a59-2f35-4b6b-9c3b-6b4f2f5cbabb/b39a5a59-2f35-4b6b-9c3b-6b4f2f5cbabb/)