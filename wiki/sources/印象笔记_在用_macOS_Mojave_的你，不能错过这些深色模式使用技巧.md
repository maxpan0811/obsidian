---
title: "在用 macOS Mojave 的你，不能错过这些深色模式使用技巧"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/在用 macOS Mojave 的你，不能错过这些深色模式使用技巧.md
tags: [印象笔记]
---

# 在用 macOS Mojave 的你，不能错过这些深色模式使用技巧

# 在用 macOS Mojave 的你，不能错过这些深色模式使用技巧 --- 在用 macOS Mojave 的你，不能错过这些深色模式使用技巧 ==========================

---

# 在用 macOS Mojave 的你，不能错过这些深色模式使用技巧

---

在用 macOS Mojave 的你，不能错过这些深色模式使用技巧
=================================

1天前

[![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/4DA55AB1-A106-4AF6-96BE-9E2F55E32178)](https://sspai.com/user/647483)

#### [ElijahLee](https://sspai.com/user/647483)

目录
:   1. [只让菜单栏和 Dock 栏变为深色模式](https://sspai.com/post/47813#ss-H2-1541476006194)
    2. [让某个应用始终显示深色模式](https://sspai.com/post/47813#ss-H2-1541476021629)
    3. [定时自动切换深色模式](https://sspai.com/post/47813#ss-H2-1541476025206)
    4. [和深色模式更搭的动态壁纸](https://sspai.com/post/47813#ss-H2-1541476029689)

macOS 原生支持黑暗模式是一直以来 Mac 用户呼唤已久的功能。虽然这一功能已经在 macOS Mojave 上实现，但是只能在深浅两种模式之间进行简单的全局性切换，仍然不能满足许多用户的需求：有人希望只让菜单栏和 Dock 栏变成黑色，有人想在浅色模式下也能用上黑色的地图，还有人想让 macOS 在天黑时自动变成黑色。于是各种应用和方法层出不穷，将 macOS Mojave 深色模式的各个效果剥离开，单独设置让它变得更合口味。

本文帮你整理了一些在 macOS Mojave 上使用深色模式的技巧，希望能帮助你更好地利用深色模式这一功能，获得更好的 Mac 使用体验。

只让菜单栏和 Dock 栏变为深色模式
-------------------

macOS Mojave 推出深色模式之后，系统偏好设置中原有的「使用深色菜单栏和程序坞」功能不再提供了。你只能接受菜单栏、程序坞，和各个应用界面的外观**一起**变深变浅。

不过，一条额外的终端指令，可以让你只将菜单栏和程序坞使用深色模式，而其他保持浅色模式不变。

1. 在「系统偏好设置 - 通用」中将外观切换成「浅色」。
2. 打开终端，输入指令：`defaults write -g NSRequiresAquaSystemAppearance -bool Yes`
3. 注销并重新登录。这一步会关闭当前所有打开的应用，因此需要提前保存好所有文稿。
4. 在「系统偏好设置 - 通用」中将外观切换成「深色」。
5. 如果你想恢复成系统的深色模式，那么在终端输入`defaults delete -g NSRequiresAquaSystemAppearance`，再执行第 3 步即可。

**关联阅读：**[让 macOS Mojave 在深色主题下依然显示浅色窗口 | 一日一技](https://sspai.com/post/47265)

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/0A653DD0-A226-4ADD-AF5F-5D9BF05EEA88.png)

让某个应用始终显示深色模式
-------------

有些应用天生就适合深色模式，比如照片、地图等；有些应用却只能用浅色模式，比如 Safari（因为绝大部分网页采用的是白色背景）。下面这几款软件就能让你自主选择哪些应用始终保持深色模式，哪些始终采用浅色模式。

打开 Gray，选择想要控制的应用图标，像按下开关一样点击它，应用就会自动退出并重启，并变黑或者变白。应用图标的背景颜色以及下方一行小字，指示了它将保持在哪种外观模式。如果想要让它恢复成跟随系统变化，右键选择 reset 即可。你可以在 [GitHub](https://github.com/zenangst/Gray)下载 Gray。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/0124EF69-49D6-43AF-9C01-F1162B87303C.jpg)

Gray 还有另外一项功能是可以一键切换深浅模式，而不必在系统偏好设置里切换。除了它以外，我们之前还介绍过用 [NightOwl](https://nightowl.kramser.xyz/)、Alfred、Automator、Keyboard Maestro 等软件实现一键打开深色模式的功能，感兴趣也可以通过[之前的文章](https://sspai.com/post/45857)进行了解。

**关联阅读：**[不想让应用跟随 macOS Mojave 变换深色模式？你可以试试这款工具：Gray](https://sspai.com/post/47465)

**关联阅读：**[4 种方法，一键打开 macOS Mojave 的黑暗模式](https://sspai.com/post/45857)

定时自动切换深色模式
----------

### f.lux

f.lux 可以让 macOS 的显示色温随着日出日落进行调节，让屏幕光线对眼睛更加健康。在 macOS Mojave 推出后，f.lux 现在支持日出日落调节色温的**同时**，切换系统外观的深浅模式。还有一款 [Shifty 夜览管家](https://shifty.natethompson.io/zh-cn/) 也可以实现类似的功能。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/C8C19950-997A-4A78-96EB-3BD0AC80C31F.png)

**关联阅读：**[我为何放弃 Night ⇧Shift，重新拥抱 f.lux](https://sspai.com/post/39240)

### NightOwl

如果你只想让深色模式能够随着日出日落自动切换，但又不想系统色温也发生变化，那么你可以使用 [NightOwl](https://nightowl.kramser.xyz/)，它等于是剥离了色温调节功能的 f.lux。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/95CE5E57-C194-4F1A-BB28-34662099745B.png)

### Shifty

[Shifty](https://shifty.natethompson.io/zh-cn/) 这款应用跟 f.lux 类似，都是帮你快速调节电脑色温或者快速开关夜览模式 (Night Shift)。这款软件也提供了根据夜览模式的开关时间配合开启系统深色模式的功能，如果你同时在用夜览模式，免费开源的 Shifty 会是你切换深色模式的一个不错的选择。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/8C198587-086E-4CA3-A501-11BE294144D2.png)

**关联阅读：**[Shifty：让 macOS 的夜间模式更懂你 | App+1](https://sspai.com/post/40765)

### Keyboard Maestro

我们之前在[《4 种方法，一键打开 macOS Mojave 的黑暗模式》](https://sspai.com/post/45857)介绍过，通过 Keyboard Maestro 这款自动化工具，你也可以实现定时切换 macOS 颜色模式的功能。你可以直接下载[这个脚本](https://cdn.sspai.com/%E5%88%87%E6%8D%A2%E5%A4%96%E8%A7%82%E6%A8%A1%E5%BC%8F-Keyboard%20Maestro.kmmacros.zip)并修改里面的代码，来让 macOS 在自己需要的时候自动切换深、浅色模式。

和深色模式更搭的动态壁纸
------------

macOS Mojave 外观的配色模式可以根据日出日落自动切换了，同时系统自带的动态壁纸也会根据太阳高度自动切换。到了晚间，深色模式和深色的 Mojave 沙漠相得益彰。当然除了 Mojave 沙漠之外，还有很多和深色模式更搭的动态壁纸。

[24 Hour Wallpaper](https://www.jetsoncreative.com/24hourwallpaper/) 是基于 [Hal Bergman](http://halbergman.com/) 和 [Josh Michaels](http://joshjet.net/) 两位摄影师的摄影作品开发的壁纸软件。从 2011 年起，他们就花了大量时间进行 24 小时不间断摄影，并制作成了 macOS Mojave 动态壁纸。共计 58 款包括自然风光、城市摄影在内的动态壁纸，其中蓝天白云和繁星点点都会随着日出日落变化，美妙至极。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/6E8130D5-F6A5-4258-BEAF-96AF0E7D71A4.jpg)

其中我最喜欢的水彩系列动态桌面壁纸,由摄影作品通过图像处理变成水彩画而来。这一系列的动态壁纸随时间变化既带有科技感，水彩风格又让壁纸带上艺术气息，把它们设为 macOS Mojave 桌面壁纸非常新颖别致。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/6FC34ED5-D8F3-4F93-93DD-E69F0207EE12.gif)

你可以在 [Mac App Store](https://itunes.apple.com/cn/app/24-hour-wallpaper/id1226087575?mt=12) 下载 24 Hour Wallpaper，应用售价 45 元。

从 Apple TV 脱胎而来的 Aerial 屏保，也适配了深色模式，它会在日落后播放夜间屏保，在日出后播放白天的屏保。

![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/443EC09B-1242-4345-AC74-35EAFE808B07.png)

**关联阅读：**[macOS Mojave 的动态桌面，可不只是「定时换壁纸」这么简单](https://sspai.com/post/47390)

**关联阅读：**[新增国际空间站航拍视频，还能配合深色模式显示屏保：Aerial 更新汇总](https://sspai.com/post/47629)

关于 macOS Mojave，你还有哪些和深色模式有关的新鲜玩法，欢迎在评论区和我们分享。

> 获取特惠、正版、高品质软件，尽在 [少数派数字商城·正版软件](https://sspai.com/mall)

[#系统增强](https://sspai.com/tag/%e7%b3%bb%e7%bb%9f%e5%a2%9e%e5%bc%ba) [#macOS](https://sspai.com/tag/macOS) [#应用推荐](https://sspai.com/tag/%e5%ba%94%e7%94%a8%e6%8e%a8%e8%8d%90)

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

---

[74](#)

---

[![](.evernote-content/5AAF83F9-8F45-4249-9770-9697DC168BFC/1766701A-5083-4FD8-8A78-519AD7217369)](https://sspai.com/user/647483)

#### 

#### [ElijahLee](https://sspai.com/user/647483)

---

[🌐 原始链接](https://sspai.com/post/47813)

[📎 在印象笔记中打开](evernote:///view/207087/s1/db896a9a-fb94-4432-93b2-a04f810942ee/db896a9a-fb94-4432-93b2-a04f810942ee/)