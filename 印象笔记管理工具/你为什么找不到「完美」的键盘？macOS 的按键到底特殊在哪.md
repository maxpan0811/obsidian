# 你为什么找不到「完美」的键盘？macOS 的按键到底特殊在哪

---

智能摘要

Windows系统引用的正是这套标准，也才有了Windows系统上的复制黏贴键。macOS为了解决用户使用键盘的矛盾，增加了修饰键修改功能，你可以根据不同的键盘，调整按键映射。为了验证自己的猜测，QMK团队的成员，重写了提供供应商ID，还有产品ID的接口，把第三方键盘伪装成了原装键盘。方面没有明确的回答我的问题，只是确认了它们有向第三方键盘品牌提供过付费的技术服务。希望用户能通过按键，显示当前所有正在运行的窗口，以及显示当前系统中所有可见的app。

原文约 3244  字  | 图片 16 张 | 建议阅读 7 分钟 | [评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2023-05-10&nu=925c3d6e-633f-4f64-bdb4-1adaa1d364fa&fr=myyxbj&ud=328ef&v=2&sig=A0AB38EE86CB6F8816FDCEB469E3AB75)

你为什么找不到「完美」的键盘？macOS 的按键到底特殊在哪
==============================

原创 七骑士托马斯 少数派

作为 macOS 用户与键盘博主，我对适配 macOS 的键盘总有一种别样的执着。打开 Apple 商店，搜索键盘，没有一把是机械键盘，也没有那么多的配列供我选择，价格也不便宜。而部分第三方厂商生产的键盘，总会宣传自己的键盘适配 macOS，体验起来就会发现实际效果大打折扣。

macOS 下的键盘到底有什么特殊、为什么特殊呢？让我们从 50 年前，Apple 电脑上的 Command 键说起。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/F99BA5EA-404B-4226-95E4-0CCF45FF02DC.jpg)

**▍****macOS 的键盘为什么特殊？**

拉里·特斯勒（Larry Tesler）是一名计算机科学家。1973 年，他加入了施乐帕克研究中心，参与研发世界上的第一台基于用户图形界面的个人电脑 Xerox Alto，发明了电脑上的复制和黏贴功能。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/3CEBA31E-DB60-4B60-9B47-EDE0F8FEFE5E.jpg)

Xerox Alto 图片来自维基百科

1979 年，史蒂夫·乔布斯参观施乐帕克研究中心，正好是劳瑞本人给史蒂夫·乔布斯演示的 Xerox Alto。用鼠标控制的图形界面，让乔布斯看到了个人电脑的未来。而此时的施乐帕克研究中心，对于图形化的操作系统并不是那么的重视。所谓道不同不相为谋，劳瑞在之后一年，就加入了苹果公司。1983 年，第一款拥有图形界面的商品化个人电脑 Apple Lisa 发布，第一次为这些功能设置了一套快捷键方案：Command 加字母键。而 Apple Lisa 自带的键盘上，Command 键就已经放在空格的旁边了。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/1A5FB914-F7FB-48B1-A7C0-ECAF872B7129.jpg)

Apple Lisa 1 图片来自维基百科

随着苹果电脑的热销，用组合键进行复制黏贴操作受到了消费者的好评。1985 年，一代经典 IBM Model M 增强版键盘发布，标准的全尺寸键盘从此时诞生。该键盘的空格键的旁边只有 Alt 键和 Ctrl 键。为了集百家之所长，IBM 在 1987 年把这些快捷键正式纳入公共用户访问标准。Windows 系统引用的正是这套标准，也才有了 Windows 系统上的复制黏贴键。而当时 Windows 系统没有 Command 键，就用 Ctrl 键代替，大家最熟悉的 Ctrl+C 和 Ctrl+V 从此诞生。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/3D5ECE1B-8AAC-47DC-AC46-F80EB1404F86.jpg)

至今 Linus 对这个键盘的赞誉还让人历历在目。称其为最伟大的键盘

在 IBM Model M 这把键盘当中，Ctrl 和 Alt 键之间，是没有按键的。一部分 Unix 系统的电脑，在适配的键盘中加了一个 Super 键（也有一部分使用 Meta 键），放在 Ctrl 和 Alt 之间。1994 年 9 月，微软发布了自己的第一代人体工学键盘，为了 Windows 95 操作系统，他们也新增了两个按键：Windows 键，还有 Menu 键。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/4413DE72-F89B-4118-A353-12B8A69644CF.jpg)

Microsoft Natural Keyboard Gen1/V1 图片来自维基百科

反倒这个时候苹果就犯了难——Command 键的前身，其实就是「苹果键」，因为乔布斯不喜欢苹果的 logo 被滥用，而改成了现在的图案。从内涵上，Command 键和 Windows 键相同（都是 GUI 键的不同表现）；从功能上看，Command 键和 Ctrl 键相同；从人们的操作习惯上，Command 键又和 Alt 键相同。尤其是 Windows 操作系统保有量更大的今天，原本是先来的苹果反而成了小众，无论怎么适配，都会让一部分人难以理解。

**▍****Command、Option、Control**

当一把第三方键盘接入 macOS，macOS 会对 Ctrl、Windows、Alt 三个按键，做简单的映射：Command 键对应 Windows，Control 键对应 Ctrl 键，Option 键对应 Alt 键。

我也是从 Windows 系统用到 macOS 的。一开始，我也不理解苹果为啥要拷打我的肌肉记忆。但用着用着，我就慢慢喜欢上 macOS 的这套布局了。想要使用修饰键中频率最高的 Command 键，仅需挪动下大拇指就可以够到了。不用工学键盘，也能让大拇指起到更多作用。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/A198F3F6-F089-40BA-B398-AB57899EC95B.jpg)

同时，macOS 为了解决用户使用键盘的矛盾，增加了修饰键修改功能，你可以根据不同的键盘，调整按键映射。你要喜欢的话，还能把 MacBook Pro 上的按键改成 Windows 习惯的。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/45114A0F-E958-4D5F-88A2-94332B33F650.png)

你用过了吗？真的很好用

很多第三方厂商所谓的适配 macOS，其实就是做了下这三个按键的映射。确实，对于绝大部分用户来说，这就够了。问题就是，macOS 上现在需要适配的按键，可不止这三个。

**▍****Fn 与 Globe，macOS 上的大麻烦**

你有多久没有用过 MacBook 上的 Fn 键了呢？

第三方键盘的 Fn 和苹果官方键盘的 Fn 是有本质的区别的。第三方键盘的 Fn 键，绝大多数只能控制键盘自身的功能，比如调整 RGB 灯效、调整无线连接模式、切换不同的按键层级等。对于电脑来说，第三方键盘的 Fn 键是**不存在的按键**。而 macOS 的 Fn 键是一个全新的修饰键，绑定了很多系统级别的功能。因此，绝大部分键盘 macOS 上的 Fn 兼容情况很差。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/003895C6-73A7-498E-924E-D033AE510930.png)

开源键盘固件 QMK 团队内的成员，曾经试图解决 Fn 键的兼容性问题。他们发现，无论是单独向 macOS 发送 Fn 的键值，还是直接截获 Mac 键盘上发出的信号，复制一遍，再由第三方键盘重新发送一次，macOS 对第三方键盘的发出的 Fn 键信号都是没有响应的。于是 QMK 团队的成员就开始怀疑，macOS 内部对键盘是有白名单限制的。

那 macOS 怎么知道，连接的键盘是不是自己人呢？键盘的本质就是个 USB 设备，在每个 USB 设备当中都有会有一个供应商 ID，还有产品 ID。供应商 ID 是需要通过 USB 联盟付费获得的，认证费用不高。并且这些 ID 是公开透明的，任何一个电脑都能查到所连接的 USB 设备的供应商 ID。比如 Apple 的供应商 ID 就是 0x05AC。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/85EBC83B-4FE7-4AA3-9BB4-3DCEB437C3FF.png)

为了验证自己的猜测，QMK 团队的成员，重写了提供供应商 ID，还有产品 ID 的接口，把第三方键盘伪装成了原装键盘。macOS 的 Fn 键，终于可以在第三方键盘上按出来了。并且，修改成不同的产品 ID，一些按键的功能也会发生变化。

QMK 团队成员在帖子中发布警告，通过盗用其他公司的供应商 ID 和产品 ID 来做 macOS 的适配，是会产生法律问题的。这篇帖子是 2017 年写的。但是六年后的今天，还真有在售的键盘，在采用这种非法的行为去适配 macOS。

针对 macOS 内部的白名单机制，我也特意咨询了 Apple 的技术顾问。Apple 方面没有明确的回答我的问题，只是确认了它们有向第三方键盘品牌提供过付费的技术服务。我作为个人，Apple 方面不方便告知付费技术服务的具体内容和收费方式。

**▍****F 区的特殊系统功能**

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/C7872BC6-7EBF-4709-BC25-88ECEACA3F31.png)

如果有你打开过 macOS 中的系统报告，会发现有一部分第三方的机械键盘，没有设置供应商 ID 和产品 ID，却依然能实现一部分 macOS F 区按键的系统功能。这些厂家是怎么做到的呢？

这还真离不开 USB 联盟旗下，人体学接入设备（HID）标准的建立。HID 标准容纳了鼠标、键盘、游戏手柄、耳机等设备的通用标准，供各大外设厂商免费合法地使用。

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/D96302E5-D660-47A4-BEB1-135148D9C3DC.png)

我们以 Magic Keyboard 上的 F1 和 F2 举例。它们的默认功能是调整亮度。早年有 Mac 用户反馈，自己的 Windows 键盘接入 Mac 之后，按下 Scroll Lock 键，竟然能调整屏幕亮度。这其中的原因是，在 macOS 的世界中，是没有 Windows 键盘里的 Print Screen、Scroll Lock、Pause 键的，而是采用了 F13、F14、F15。并且在老版本的 macOS 中，F14 和 F15 赋予的正是调整屏幕亮度的快捷键。好处就是这给了第三方键盘厂商一个适配的方案。坏处就是小白用户觉得无法理解。在最新的 macOS 中，这组快捷键仍有保留，但是默认处于禁用状态。而且这个时候，HID 标准中已经增加了调整亮度的代码，F1 和 F2 的问题就解决了。

同时被解决的，还有 F7 到 F12 这六个多媒体按键。原理是相同的。

F5 和 F6 比较特殊。在 MacBook 上，F5 和 F6 是调整键盘的背光灯亮度。Apple 自己的外接键盘不存在背光灯，F5 和 F6 在默认状态按下，不会触发系统级功能，所以可以不用适配。

那 F3 键的调度中心，还有 F4 的启动台功能怎么办呢？

2017 年 10 月 6 号，USB 联盟收到了来自 Apple 员工 gopu 的提案。希望用户能通过按键，显示当前所有正在运行的窗口，以及显示当前系统中所有可见的 app。正好对应了 macOS 中的调度中心和启动台功能。gopu 还非常贴心地给了 USB 联盟建议，具体要加什么键值进去合适。提案提上去了，需要投票表决，才能通过。有投票资格的竟然是英伟达，Wacom，还有微软。投票很顺利地通过，并且加入了 HID 标准当中。感谢 gopu，你简直就是天使。至此，所有的 F 区按键，都已经有合法的方案去适配了

……吗？

**▍****谁也保不准的未来**

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/A7F72117-B479-468D-BAAF-D840ACE3FB8E.png)

很遗憾，我认为，就目前情况而言，可能永远不会有完美兼容 macOS 的第三方键盘——因为在第三方键盘品牌想方设法，寻找老按键兼容方法的同时，Apple 也在想法设法地添加新的按键。

比如在 Apple 官网上架的「带有触控 ID 的妙控键盘」，相比老版本，它增加了聚焦搜索按键、听写按键，还有专注模式按键。可以预见的是，只要 Apple 还在更新系统，并且为了让用户用最快的方式体验它们的最新功能，就有可能把新的按键加在键盘上。再加上 Apple 的白名单机制，更新版本越多，造成的混乱注定越大。

而对于第三方键盘厂商来说，供应商所提供的兼容 macOS 的解决方案，看上去都一样，且都无法确认这些兼容方案的合法性。所以，它们宁愿放弃 macOS 用户，也不想碰到不必要的麻烦。

针对 Apple 设定的白名单，还有所谓的付费技术服务，我是这样看待的。首先，它是有必要存在的，比如说最新版妙控键盘上的 Touch ID，它就应该启用最严格的保护措施，只有 Apple 自己才可以使用，才能真正保护用户的隐私安全。至于付费技术服务，与其只提供某些按键的使用权限，更应该提供的是，在与 Mac 电脑交互过程中更强大的无线抗干扰能力、无线信号加密技术、无线传输速度优化等技术上的支持。macOS 用户不该被局限于千篇一律的 Magic Keyboard，他们值得和 Windows 用户一样，轻轻松松就能用上更好的键盘。

原文链接：

https://sspai.com/post/79608?utm\_source=wechat&utm\_medium=social

作者：七骑士托马斯

责编：北鸮

******/****更多热门文章****/******

[![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/6E173F34-7BCC-4035-9DD0-26E53D84EA88.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247554014&idx=1&sn=849c717036086783e0841789eb9c137c&chksm=fdb3e6b4cac46fa2bd21aa5339a65057c599dc52fbcc3a4ed60067cd6920b137814ef7457fa5&scene=21#wechat_redirect)

[![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/F7153904-8855-4953-9D28-B8DD79556B37.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247553963&idx=1&sn=7d20277477cfbcfecb3a5ba6d0ec39aa&chksm=fdb3e6c1cac46fd70f9677179740c697b933d475a27c3e7182e6124c3d74f578a57632b58dec&scene=21#wechat_redirect)

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/C4CE2B99-7C0E-4224-A135-948DC97CDA47.gif)

![](.evernote-content/312ADCEF-2C11-45A9-8403-653A3E4D41C5/F0085EC3-98FF-42A3-B20E-2AA6CFEF1366.gif)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247554057&idx=1&sn=d9387ad436b8a968ce9adcd87cedfcf0&chksm=fdb3e163cac46875ce2fbb9b2ae992c16edf9fbdd41e720b4a3d7d1063cdd07de478e9e2a63e&mpshare=1&scene=24&srcid=0510j5uxnk9NLjiTbT9f0MqI&sharer_sharetime=1683715724220&sharer_shareid=ee47b9411760e9070f0b59d8d8655fa1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a905bebb-6e35-4072-9951-9293caa09599/a905bebb-6e35-4072-9951-9293caa09599/)