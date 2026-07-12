# 定制你的浏览器新标签页，让常用功能触手可及：Steward

---

作为浏览器用户，你也许对启动器不太了解，但相信你对新标签页扩展并不陌生，如 [Speed Dial 2](https://speeddial2.com "Speed Dial 2")、[Momentum](https://momentumdash.com "Momentum")、[Infinity](https://chrome.google.com/webstore/detail/infinity-new-tab/dbfmnekepjoapopniengjbcpnbljalfg "Infinity") 等热门扩展，让你可以在新标签页快速记录、查看天气、更换壁纸、打开常用网址等等。

为了让更多人更好地体验到启动器的强大，我为 [Steward](http://oksteward.com/ "Steward") 加上了新标签页模式，使之立刻就拥有新标签页扩展的常用功能，甚至更多，同时还兼具其它扩展没有的强大自定义以及启动器快捷高效的操作方式。

Steward 免费开源，你可以选择需要的版本下载：

* [Chrome 版下载🔗](https://chrome.google.com/webstore/detail/dnkhdiodfglfckibnfcjbgddcgjgkacd "Chrome 版下载🔗")
* [Firefox 版下载 🔗](https://addons.mozilla.org/zh-CN/firefox/addon/steward-a-command-launcher/?src=userprofile "Firefox 版下载 🔗")

自定义外观
-----

新标签的打开相当频繁，因而它的外观也是很重要的，不管是美观还是自定义。美观通常是主观的，如果你有更好的外观建议也可以反馈给我。

### 壁纸

相信很难有其它扩展比 Steward 更方便的管理壁纸了，往下看你就知道。

#### 壁纸操作

**`wp` 命令**

`wp` 命令操作如下图，包括保存、刷新、复制壁纸链接等操作。需要说明的是「上传到图床并保存」这一项，由于 Steward 壁纸外部来源要么是动态链接(保存的壁纸可能失效)，要么可能加载缓慢，因此通过图床不只可以转为固定链接，还能起到加速的作用，这个图床目前是微博的，日后也可能替换或自定义为其它图床，比如七牛云。

![](.evernote-content/F58E3761-5ACD-42E2-B87D-C8D4E9AC9FA6/81805012-3E08-4D21-8924-ED3690E3E46D.png)wp 命令操作列表

另外，保存、刷新在新标签页页面底部也有按钮可以完成操作。

**Wallpaper 面板**

在这里可以选择应用/删除某张壁纸，也可以手动添加壁纸链接。

![](.evernote-content/F58E3761-5ACD-42E2-B87D-C8D4E9AC9FA6/82DB3995-A0A0-443C-B1DB-4460FB2C937E.png)Wallpaper 设置面板

**`wps` 命令**

对于想要快速切换收藏的壁纸的你，使用 `wps` 命令会有惊喜哦。

#### 壁纸来源

分为外部来源以及个人收藏，外部来源包括 Bing、Unsplash、Nasa 以及 Desktoppr。你可以保存某张壁纸，或通过 wp 命令以及在设置页面的 wallpaper 面板手动添加壁纸链接，这些都将进入你的个人收藏。

Steward 默认的来源只包含个人收藏以及质量相对最高的 Bing，你可以在**设置页面 - General 面板**的壁纸来源自行设置。

外部来源会随着 Steward 的持续迭代而不断增加，如果你有好的来源建议可以告诉我哦，我会很高兴将它添加进去的。

### 样式

#### 自定义

![](.evernote-content/F58E3761-5ACD-42E2-B87D-C8D4E9AC9FA6/F1676152-7A51-457E-8407-0F443A495159.png)Appearance 面板自定义新标签页外观

### 其它

通过 `nt` 命令可以对新标签页进行一些额外的设置。

![](.evernote-content/F58E3761-5ACD-42E2-B87D-C8D4E9AC9FA6/B7CAB905-7F48-40EA-847C-6A95A6393EC2.png)nt 命令操作列表

#### 功能区显示/隐藏

默认为显示，当设置为隐藏时，新打开新标签页时 Steward 功能区将不可见，当按下 Tab 键或点击页面以获得焦点后，功能区将显示出来。

#### 毛玻璃效果

由于存在某些壁纸的色值导致 Steward 功能区显示不清，开启毛玻璃效果后会得到改善。

添加常用功能
------

花了较大篇幅介绍了外观的设置，然而功能上的考虑才是新标签页模式设计的初衷，也是它的精髓所在。

### 固定应用一个命令

我们常常看到这些需求：

* A: 我想打开新标签页就能看到待办事项 todolist
* B: 我想看到的是习惯打卡 times
* C: 我想通过新标签页提醒我及时查看处理 pocket 文章

对于 A，使用 `custom todo` 命令

对于 B，使用 `custom ts` 命令

对于 C，使用 `custom po` 命令

格式为 `custom 命令+空格`，注意通常都不能省略末尾的空格哦。

### 多个命令随机应用

我常用的命令很多，但 `cusotm` 命令只能设置一个，怎么办？

使用 `random` 命令即可，比如以下几条命令，可以让你的新标签页在每次打开时，随机从中选择一条应用，如此你的新标签页就兼具了书签、todolist、天气、常用网址的功能。

```
random bm 
random todo 
random tq 
random site
```

![](.evernote-content/F58E3761-5ACD-42E2-B87D-C8D4E9AC9FA6/0B80D7B5-F475-4F8C-A4EC-E6525D1A49FF.png)random 图示，与以上命令不是完全对应的

### 自定义新标签页的标题

既然新标签页内容可以自定义，那它的标题要能自定义就更好了。

通过 `ntm` 命令可以为新标签页设置一组标题，每次打开将随机从中选择一条显示。  
![](.evernote-content/F58E3761-5ACD-42E2-B87D-C8D4E9AC9FA6/A165B8F0-520F-4543-8F9E-849AA2F1E0C0.png)ntm 命令图示

占用新标签页的其它考虑
-----------

Steward 开发之初只有 [Popup](http://oksteward.com/steward-document-zh/%E4%B8%89%E5%A4%A7%E6%A8%A1%E5%BC%8F/Popup%E6%A8%A1%E5%BC%8F.html "Popup") 一种模式，至于为什么会加上新标签页模式，除了降低使用门槛以外，主要还有以下两方面考虑。

### 默认新标签页替代容易

默认新标签页只有搜索框以及常用网址。由于地址栏本身就是搜索框，而常用网址可以用 Steward 的 `site` 命令取代，后者还更加便捷，可以说，替代默认新标签页毫无压力。

### 更好的利用新标签页

随着 Steward 的插件越来越多，结合对 Mac 上 Alfred 的日常使用，发现类似的命令启动器的一大天然缺陷或不便，即对于高频功能的使用操作上有些繁琐——首先需要通过快捷键唤起主应用，再输入指定命令才能进一步查看或操作。

所以将 Steward 的功能区放置在新标签页上就可以在某种程度上解决这个问题，同时，Steward 对新标签页的设计也是外观与功能兼顾的。

**小技巧：如果你不想使用新标签页**

看完新标签页的介绍，你应该有了对它的全新认识。如果你还是想关闭它的话，可以使用 Browser Alfred([Chrome 应用商店](https://chrome.google.com/webstore/detail/browser-alfred-a-command/jglmompgeddkbcdamdknmebaimldkkbl "Chrome 应用商店") / [Firefox 附加组件](https://addons.mozilla.org/zh-CN/firefox/addon/browser-alfred-%E6%B5%8F%E8%A7%88%E5%99%A8%E5%91%BD%E4%BB%A4%E5%90%AF%E5%8A%A8%E5%99%A8/?src=userprofile "Firefox 附加组件"))，它除了不占用新标签页以外，其它功能完全跟 Steward 同步。

拓展阅读：

* [在 Chrome 里用「Alfred」是什么体验？Steward 把效率启动器带进了浏览器](https://sspai.com/post/42048 "在 Chrome 里用「Alfred」是什么体验？Steward 把效率启动器带进了浏览器")
* [Chrome 命令启动器 Steward 攻略 -- 三种模式各有神通](https://sspai.com/post/42121 "Chrome 命令启动器 Steward 攻略 -- 三种模式各有神通")

> 让你的 Chrome 浏览器更强大，就在专题 [无扩展，不 Chrome](https://sspai.com/topic/102 "无扩展，不 Chrome") ⚡️

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk "少数派 iOS 客户端")、关注 [少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，让智能设备更好用 ⚡️

---

[🌐 原始链接](http://sspai.com/post/42273)

[📎 在印象笔记中打开](evernote:///view/207087/s1/157c043a-8f77-4e5a-b545-16ebbf87b1de/157c043a-8f77-4e5a-b545-16ebbf87b1de/)