---
title: "无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」.md
tags: [印象笔记]
---


![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/5DA50858-EB10-4846-8875-C899A74C01F4.jpg)

一个月前 [JailbreakHum](http://matrix.sspai.com/user/681230) 同学写了一篇[《把你的 iOS 设备变成控制 Mac 的「遥控器」》](http://sspai.com/35242)。碰巧我当时也想要写一篇类似的文章，当这标题映入眼帘，我心里便是咯噔一下，脑海里闪过 N 个加粗大字：「该死，我想写的东西居然被抢先了！」。

不过，仔细一读，发现虽然晚了一步，但自己的方法还是有可取之处的，简单来讲，我的方法和 JailbreakHum 那篇文章实现的效果相同，都利用了 AppleScript，但是我不需要用 Hazel，事实上无需任何第三方应用，就可以实现通过 iPhone 来控制 Mac。

原理
--

想要遥控 Mac，关键就在于 Mac 上要有一个能根据手机上的指令自动触发 AppleScript 的后台程序。但是，我们有没有必要

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->