---
title: "装点你的 Dock：添加篇 _ 一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/装点你的 Dock：添加篇 _ 一日一技 · Mac.md
tags: [印象笔记]
---

# 装点你的 Dock：添加篇 _ 一日一技 · Mac

# 装点你的 Dock：添加篇 | 一日一技 · Mac --- ![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/ED07A62F

---

# 装点你的 Dock：添加篇 | 一日一技 · Mac

---

![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/ED07A62F-6F8F-49B5-8D69-A9FA0FDCA6F8.jpg)

Dock 栏是 OS X 的标志性设计，也是用户与 OS X 交互的最重要的方式。利用 Dcok 栏，我们可以将自己最为常用的应用程序、文稿和文件夹添加到 Dock 栏中。

通过「系统偏好设置」，就可以对 Dock 进行一些基础性设置，但借助于终端命令（或第三方系统增强应用），则可以让我们对 Dock 栏做更进一步地「装点」，让它变得更顺手，更赏心悦目。

* **上期回顾：**[《装点你的 Dock：外观篇》](http://sspai.com/33493)

玩转 Dock 添加项
-----------

### 1. 添加应用到 Dock 中的另类技巧

一个有意思的技巧是：如果你想要一个已经打开的应用程序在 Dock 中保留，移动一下它的位置，OS X 就会自动将其设置为「在 Dock 中保留」。

### 2. 在「堆栈区」添加网址

除了添加文件堆栈以外，你还也可以直接将浏览器中的常用网址拖拖入「堆栈区」即可，以便快速访问。

### 3. 在「应用区」添加文件夹

一般来说，在分隔线的左侧只允许添加应用程序，但通过变通的办法，实际上也可以在该区域放添加文件夹。

这样做的好处是：

1. 充当 Finder 替身：由于 Finder 图标位置「偏居一隅」，使得我们有时不得不跨越大半个屏幕去点击它，十分不便；
2. 快速访问指定文件夹。有一些文件夹是我们经常需要访问的，如「下载」、「屏幕截图」等 —— 把它们放在桌面上？这样虽然最简单，但你最好设置个「触发角」，同时忍受不时的误触发的烦恼；建立个文件堆栈？文件堆栈虽然可以快速打开文件，但如果我想要查看文件夹，那就得按住 ⌘ 键才行；通过 Alfred？这样好是好，但是也还是不如直接在 Dock 中放置一个文件夹方便。

**步骤一：**在 Finder 中找到目标文件夹，并在其原文件名后增加「.app」后缀。修改后，文件夹图标将变为「无效」状图标。

**步骤二：**点按并拖拽，将其添加到应用程序区域。

**步骤三：**删除原文件夹的「.app」后缀，随后文件夹图标将恢复正常。

**步骤四：**在 Dock 中单击添加的文件夹，图标恢复正常。

![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/F2F15D94-A186-47D8-9BB7-8E46FA72600E.jpg)

### 4. 在「堆栈区」添加应用程序

一般来说，「堆栈区」只允许添加文件夹堆栈和网址，但实际上，通过终端命令，也可以在该区域添加应用程序。

需要输入的命令格式为：

`defaults write com.apple.dock persistent-others -array-add 'tile-datafile-data_CFURLString/Applications/应用名.app_CFURLStringType0'; Killall Dock`

其中的引用路径 /Applications/应用名.app 的内容，我们可以通过以下方式查询：

**步骤一：**在 Finder 的「应用程序」中，定位到想要添加的应用程序，例如「预览」或「终端」。

**步骤二：**按住 Option（⌥）键，右键选择「将『预览.app』拷贝为路径名称」，粘贴到文本工具中，显示为 `/Applications/Preview.app`（「终端」对应的路径为 `/Applications/Utilities/Terminal.app`）。

![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/57536D97-E75A-44C5-8C95-64B70E2022D1.jpg)  
步骤三：使用上述路径替换掉前述引用路径 `/Applications/应用名.app`，输入「终端」即可。

![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/DB2565E2-A247-4BD3-B3A2-5235B1BD73AC.jpg)

### 5. 添加「不常用应用程序」堆栈

对于小屏幕的 Mac 用户来说，Dock 栏常常会被挤得满满当当的（别忘了，最小化窗口也会挤占 Dock 空间），这对使用 Spotlight 或是 Alfred 来启动应用程序的用户倒也还好。不过，为了缓解 Dock 空间不足的尴尬，也可以将那些并非「每日必备」的应用程放入「堆栈区」，以便不时之需。

**步骤一：**在「应用程序」中，找到希望添加的目标应用，点击鼠标右键，选择「制作替身」。

**步骤二：**新建一个文件夹（不妨取名为「应用堆栈」），并将替身文件剪切到该文件夹中。

**步骤三：**将「应用堆栈」文件夹，拖入「堆栈区」即可。

![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/54DAFCB3-42E9-4DFE-AFA0-286C0B0B3E44.jpg)￼

### 6. 添加「最近使用项目」文件堆栈

通过点击  -「最近使用的项目」，可以很方便地查看到最近使用的应用程序、文稿、服务器等。但除此之外，我们还可以通过如下命令，将其添加到「堆栈区」中去。

添加到堆栈右侧：

`defaults write com.apple.dock persistent-others -array-add '{ "tile-data" = { "list-type" = 1; }; "tile-type" = "recents-tile"; }'; Killall Dock`

添加到堆栈左侧：

`defaults write com.apple.dock persistent-apps -array-add '{ "tile-data" = { "list-type" = 1; }; "tile-type" = "recents-tile"; }'; Killall Dock`

![](.evernote-content/D8C6669C-47CD-4A6A-8BFC-859794A86ED2/5F30034E-9BAF-408A-880B-C1BDC87A8CA8.jpg)

参考链接：

1. [TekRevue: The Complete Guide to Customizing the Mac OS X Dock](http://www.tekrevue.com/tip/the-complete-guide-to-customizing-mac-os-xs-dock-with-terminal/)
2. [知乎：OS X 中应如何布局 Dock 上的图标？](https://www.zhihu.com/question/21678287)
3. [Scomper：从 Windows 到 Mac](http://www.jianshu.com/p/00b21f0696db)

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

想要获得更多简单实用的小技巧？*[继续阅读往期「一日一技」文章>](http://sspai.com/tag/%E4%B8%80%E6%97%A5%E4%B8%80%E6%8A%80)*

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33496)

[📎 在印象笔记中打开](evernote:///view/207087/s1/10fa5133-6cdd-4fd9-95f3-831e9077a608/10fa5133-6cdd-4fd9-95f3-831e9077a608/)