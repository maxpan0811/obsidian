---
title: "Mac 上隐藏了许多实用的功能，只有这样才能打开"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Mac 上隐藏了许多实用的功能，只有这样才能打开.md
tags: [印象笔记]
---

# Mac 上隐藏了许多实用的功能，只有这样才能打开

# Mac 上隐藏了许多实用的功能，只有这样才能打开 --- Mac 电脑上有一种比较另类的操作：命令行。我们不需要图形界面，只靠一句或几句命令，就能让电脑完成图形界面难以实现的功能。 ![](.ev

---

# Mac 上隐藏了许多实用的功能，只有这样才能打开

---

Mac 电脑上有一种比较另类的操作：命令行。我们不需要图形界面，只靠一句或几句命令，就能让电脑完成图形界面难以实现的功能。

![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/B2276C36-F47E-4645-92CB-C16FA5E1FB99.png)

Mac 的自带的命令行客户端是 Terminal，它的界面看上去晦涩难懂，其实使用使用起来并不复杂，许多文章中都提供了现成的命令，你只需要复制粘贴就能实现许多功能。为了更多人能够善用这一 Mac 上的利器，少数派为读者准备了专题 [轻松玩转 Mac 命令](https://sspai.com/topic/183)，你可以在其中找到许多现成、好用的命令。当然，可能你已经是一个命令行老玩家，那么本专题中也有为你准备的进阶内容，你同样可以在其中获得一些新技能。

在开始你的命令行之路前，不妨先看一下这篇文章，我（Minja）总结从入门到进阶常见的一些问题与需求，希望能助你离 Mac 高手更近一步。

从这几条命令开始
--------

第一次使用命令行必然是一头雾水，不知道从何下手。其实我们可以先试着运行一些简单的命令，解决一些普遍的需求。直接复制下面的命令到 Termnial，回车就能运行了：

1. 遇到一个生词，想知道发音？试试 `say 单词`；
2. Finder 卡死了？用 `killall Finder` 「重启」它；
3. 下载大文件时不希望电脑自动休眠，但需要关闭屏幕？用 `pmset displaysleep` ；
4. 演示 PPT、设计稿时，想让屏幕多亮一会儿：`caffeinate -t 3600`；
5. 让通知快点消失：`defaults write com.apple.notificationcenterui bannerTime 3`；
6. 使不活动的图标进入半透明状态：  
   `defaults write com.apple.dock showhidden -bool TRUE; killall Dock`  
   ![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/8E1D5835-6B0C-4846-9958-CEAAD0B88C41.gif)
7. 让 Dock 瞬间出现/消失：  
   `defaults write com.apple.dock autohide-time-modifier -int 0;killall Dock`  
   ![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/F76E4702-83A7-4B99-BC96-71946B2CA547.gif)
8. 在 Launchpad 里放下更多图标：  
   `defaults write com.apple.dock springboard-columns -int 8; defaults write com.apple.dock springboard-rows -int 7; defaults write com.apple.dock ResetLaunchPad -bool TRUE; killall Dock`  
   ![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/37BFDA90-298B-4C53-BAFC-A29803D52C12.png)命令使用前后对比

相信这些简单实用的命令可以让你很快获得成就感，并由此喜欢上命令行。

拓展阅读：

* [简单几条命令，轻松开启 macOS 系统隐藏功能 | 新手问号](https://sspai.com/post/41695)
* [视频：5 个命令放大 Dock 生产力](https://sspai.com/article/41333?series_id=9)（详细内容请阅读 [Power+](https://sspai.com/series/9)）

记不住命令，就用这几招
-----------

命令很强大，但是我们很难记住它们，其实有三个方法可以方便我们取用命令。

1. 把常用命令记在系统的文本替换中，每次打几个字母就能显示一整条命令。当然，如果你有 TextExpander 等第三方输入增强工具，也能实现文本替换。  
   ![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/ED634754-4C44-4619-BA4A-2E24E89D284E.gif)
2. 把常用命令放在 [剪贴板管理工具](https://sspai.com/post/41173) 中，随时取用。我专门在 [Copied](evernote-html-snippet://) 里建立了一个命令列表，里面都是一些难记但使用频繁的命令。  
   ![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/1406488D-0588-4830-8318-E954BAC93B7C.png)
3. 把常用命令设为壁纸，随时可以查看。你可以搜索关键词「Command Cheat Sheet」，有不少现成的壁纸，下面的壁纸来自 [这里](http://hirecollin.com/2015/08/command-line-basics-cheatsheet/)。  
   ![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/DA0890E9-9651-400F-9362-556DF101D355.png)
4. 压根不想打开 Terminal？试试 [MacPilot](http://www.koingosw.com/products/macpilot/)，这个应用把常用命令做成了图形界面，点点按钮就能实现原先需要依靠命令才能完成的操作。

![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/5D38771C-0B00-45C7-8288-3ACB14DF5604.png)

命令行的另类用法
--------

命令不仅强大，还非常灵活，我们可以在 Terminal 以外的地方运行命令。

### 更方便地运行命令

除了打开一个 Terminal 窗口，我们还可以用其他工具更方便地运行命令。[Alfred](https://www.alfredapp.com/)、[LaunchBar](https://www.obdev.at/products/launchbar/index.html) 等启动器工具都允许我们在类似 Spotlight 的搜索框里面直接输入命令。

![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/D63C9359-43FF-4B5D-88B8-73E8DBE34071.png)

拓展阅读：[LaunchBar，全方位优化你的 macOS 使用习惯的所有文章](https://sspai.com/series/28/list)。

### 用 Today Scripts 查看系统状态

这个免费的小工具平时呆在通知中心，能运行预设命令并显示结果。我们可以把查看系统状态的命令预先在 Today Scripts 里填好，需要时呼出通知中心便可以显示系统状态，看看哪些应用最占内存，或者磁盘空间还剩多少，等等。

![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/4D810E49-0458-47DF-9B7C-A3DE95FDFECC.png)显示系统状态

拓展阅读：

* [用终端命令定制你的 OS X 通知中心：Today Scripts 体验详解](https://sspai.com/post/27662)
* [让你的 Mac 通知中心变得更实用：Today Scripts](https://sspai.com/post/40169)

### 把命令「打包」

有些命令还可以「打包」成一个 App，分享给完全不懂命令行的朋友。

系统自带的 Automator 就是很棒的打包工具。我把一条压缩动图的命令打包进一个 App 里，使用时直接将图片拖到 App 图标上，就完成了压缩。这个自制的 App 我分享给了几位不懂命令行的读者，他们使用起来也没有任何障碍。

![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/758B7204-FCA0-4F7B-91CC-6BBBFF63E62B.gif)

拓展阅读：[这样压缩 GIF，体积小还效果好](https://sspai.com/post/42916)。

获取更多命令
------

Mac 自带的命令也许还不够满足你，那么是时候安装 HomeBrew 以打开新世界的大门了——HomeBrew 同样通过命令行来安装：

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

之后你就可以根据自己的需要来安装第三方的命令，实现更多功能。甚至，你还可以通过 HomeBrew 直接安装应用，就像下面这样：

![](.evernote-content/BD0F602C-F5B2-4E55-ABD9-CB23A477892D/39ED1631-F259-4B19-9185-0E30D31F5BB4.gif)

关于 HomeBrew，请浏览专题 [Homebrew，Mac 应用管家](https://sspai.com/topic/181)。

小结
--

上面介绍的命令与一些小技巧只是 Mac 命令的冰山一角，更多强大的功能，请探索专题 [轻松玩转 Mac 命令](https://sspai.com/topic/183)。

相信看完这个专题，你就能够用好命令，更加自如地使用 Mac 电脑。

---

[少数派](http://sspai.com/s/nqQk)，汇聚数字时代愿意思考的人。

---

[🌐 原始链接](http://sspai.com/post/43546)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ee777160-5a8a-402e-81cb-be155c0b0abf/ee777160-5a8a-402e-81cb-be155c0b0abf/)