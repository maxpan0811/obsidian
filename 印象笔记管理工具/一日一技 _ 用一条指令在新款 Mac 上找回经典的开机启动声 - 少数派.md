# 一日一技 | 用一条指令在新款 Mac 上找回经典的开机启动声 - 少数派

---

用一条指令在新款 Mac 上找回经典的开机启动声
========================

Matrix

付费订阅

特别策划

Pi Store

官方淘宝

软件商城

Tron 计划

Tron

0

![](.evernote-content/AD776BD2-560A-423F-B8FD-47E5336146E2/A4767E68-F24E-489D-AA88-4D3DE0EC00DD)

一日一技 | 用一条指令在新款 Mac 上找回经典的开机启动声

多年使用 Mac 的老用户肯定知道，Mac 在启动时会发出一声「噔～」的启动声音，伴随着 Apple logo 在屏幕上亮起，Mac 正在安全地启动。但如果你在最近几年换了新款 Mac 电脑，你会发现这个熟悉的启动音消失不见了。

经典的 Mac 开机声音

就像 MageSafe 磁吸充电接口、会发光的 Apple logo 一样，Mac 启动音可能也代表了旧时代的设计，在 2016 年末及以后发布的大多数 Mac 电脑上，Apple 默认移除了这一特性。

好在这一启动音不是物理消失，我们只需要一条终端指令就能让它再现。打开「终端」应用，输入指令：

```
sudo nvram StartupMute=%00
```

再回车。Mac 启动音就回归了，重启就能听到。

除了经典的一声较长的提示音外，Mac 电脑在启动时还会发出其他类型的声音，不过它们通常代表 Mac 的 RAM 或 ROM 出现了问题。启动音的详细情况可以在 [Apple 支持 - 关于 Mac 的启动音](https://support.apple.com/zh-cn/HT202768) 中查看。

如果你不想 Mac 发出启动音，在终端中输入  `sudo nvram StartupMute=%01` 就能让它在启动时保持静音。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，了解更多实用小技巧 ⚙️

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

7625

本文责编：@[文刀漢三](https://sspai.com/u/eamesliu)

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

[ElijahLee](https://sspai.com/u/914r3btn/updates) ![](.evernote-content/AD776BD2-560A-423F-B8FD-47E5336146E2/088602D6-140D-4FA7-A209-D60A44B851D0.png)

多次获得「最佳作者」称号，收到多个台灯奖品。

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/59550)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9d86c81a-21c9-4ce1-bd4b-0fd93628f7e7/9d86c81a-21c9-4ce1-bd4b-0fd93628f7e7/)