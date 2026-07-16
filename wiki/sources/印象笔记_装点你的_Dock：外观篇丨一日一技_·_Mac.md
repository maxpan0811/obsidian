---
title: "装点你的 Dock：外观篇丨一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/装点你的 Dock：外观篇丨一日一技 · Mac.md
tags: [印象笔记]
---

# 装点你的 Dock：外观篇丨一日一技 · Mac

# 装点你的 Dock：外观篇丨一日一技 · Mac --- ![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/115DFF4D-E

---

# 装点你的 Dock：外观篇丨一日一技 · Mac

---

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/115DFF4D-EED7-44D5-BED1-7C80E58770F1.jpg)

Dock 栏是 OS X 的标志性设计，也是用户与 OS X 交互的最重要的方式。利用 Dcok 栏，我们可以将自己最为常用的应用程序、文稿和文件夹添加到 Dock 栏中。

通过「系统偏好设置」，就可以对 Dock 进行一些基础性设置，但借助于终端命令（或第三方系统增强应用），则可以让我们对 Dock 栏做更进一步地「装点」，让它变得更顺手，更赏心悦目。

说明
--

* 在本文中，所有的设置，均以 Dock 栏放置在屏幕底部为例进行说明。
* 为了简化说明，在本文中，笔者将 Dock 分隔线左侧的区域称为「应用区」，将右侧区域称为「堆栈区」（Stack）。
* 文中绝大多数功能之实现，都倚赖于终端命令。你可以通过 Spotlight 搜索「终端」，也可以定位到「应用程序」-「实用工具」-「终端」找到它。为了避免出错，建议你直接复制并粘贴到「终端」。
* 除了需要在终端中输入修改默认设置的命令以外，还需要执行 `Killall Dock`命令（请注意大小写），重启 Dock，以使更改生效。不过在本文中，笔者将命令做了整合，只需要执行一次即可立刻生效：

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/F624E8C9-1D50-4393-BBC7-FFB5C473205F.jpg)￼

外观调整
----

### 1. 快速调整 Dock 基本设置

在「系统偏好设置」的「Dock」面板中，有很多细致的设置项。但如果你希望快速调整一下 Dock 设置的话，则不妨将光标放置在 Dock 栏的分隔线上，右键，就可以在弹出菜单中进行设置了，例如启用 Dock 隐藏和放大，调整 Dock 在屏幕中的位置等，十分方便。

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/3A0AB631-422A-4F91-B8B0-1FAA4C07173B.jpg)

### 2. 增加空白占位符

通过在 Dock 中添加空白占位符（Spacer）的方式，可以帮助我们对应用程序和堆栈进行分类。

在「应用区」添加空白占位符：

`defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'; Killall Dock`

在「堆栈区」添加空白占位符：

`defaults write com.apple.dock persistent-others -array-add '{tile-data={}; tile-type="spacer-tile";}'; Killall Dock`

重复执行上述命令，就可添加多个占位符。点按并移动，可以调整其位置。如果你想移除它们，右键点击「从 Dock 中移除」即可。

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/591E6975-8213-4ECA-ACBD-FA167C775275.jpg)

### 3. 隐藏应用使用透明图标显示

默认情况下，使用 ⌘M 最小化的窗口会在右侧以缩略窗口展示，非常容易区分。但是，使用 ⌘H 隐藏的应用程序窗口，既不在 Mission Control 中显示，也没有明显的标志能够标明其包含隐藏的应用程序窗口。到头来，你要么记得，要么主动查看，非常不便。

通过如下命令，可以让那些包含隐藏窗口的应用程序图标变暗，从而方便我们区分：

`defaults write com.apple.dock showhidden -bool true; Killall Dock`

恢复为默认设置：

`defaults delete com.apple.Dock showhidden; Killall Dock`

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/60107A35-0064-4B82-808D-70DEE83BBED6.jpg)

### 4. 设置最小化窗口效果为「吸入」效果

在「系统偏好设置」-「Dock」面板中，可以设置最小化窗口效果 —— 神奇效果（Genie）和缩放效果（Scale）。但实际上，系统还隐藏了一种吸入效果（Suck，请不要想歪）。

开启命令：

`defaults write com.apple.dock mineffect suck; Killall Dock`

如果希望恢复成默认效果，前往「系统偏好设置」-「Dock」中修改即可。

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/0147AB4B-14A0-4F2F-A758-CCADBF27A214.gif)

### 5. 让 Dock 只显示已打开的应用程序

默认情况下，Dock 栏不仅会显示用户设置为「在 Dock 中保留」的应用程序（不论打开与否）、系统项目（Finder 和废纸篓）以及堆栈，还会显示那些用户并未设置保留，却已经打开的应用程序的图标。

这种「一个不漏」的显示方式，虽然十分用户操作，但也十分容易变得讨人厌：

* 对那些已经有不少在 Dock 中保留的项目的用户来说，随着新增的应用图标和最小化窗口的挤占，Dock 栏会越变越小。这时，Dock 中不活跃的应用程序及堆栈就不仅让人分心，还影响操作效率。

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/F5168C16-7D84-4DA6-84F2-070B61E0B868.jpg)

* 对那些希望截取或录制屏幕内容的用户来说，为了保持内容的相关性，常常会在截取或录制之前将不需要的项目从 Dock 栏中移除，结束后再加以恢复，十分费力。

通过执行如下命令，其实就可以让 Dock 只显示已打开应用，从而减少不必要的干扰：

`defaults write com.apple.dock static-only -boolean true; killall Dock`

恢复为默认设置：

`defaults delete com.apple.dock static-only; killall Dock`

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/EFC763EA-D033-4AEF-84E3-2E6F1A34DF14.jpg)

### 启用堆栈高亮效果

默认情况下，当文件堆栈设置「显示内容为」「网格」视图时，光标经过图标并不会高亮显示（在其他视图则不然）。为了方便我们更准确地选择对象，不妨通过如下命令启用「网格」视图下的高亮效果（OS X 的这种区别对待，还真是令人琢磨不透 == ）：

启用图标高亮：

`defaults write com.apple.dock mouse-over-hilite-stack -bool TRUE;killall Dock`

恢复为默认效果：

`defaults delete com.apple.dock mouse-over-hilite-stack;killall Dock`

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/1CF8DBBD-2BA3-496F-983C-646B9716BC3E.jpg)

Bonus：
------

比起相对麻烦且容易出错的终端命令来说，利用 [OnyX](http://www.titanium.free.fr/) 这款免费的系统维护软件去设置，不仅更友好，恢复成默认的设置也更方便。

具体设置，如下图所示：

![](.evernote-content/CC839A61-F05A-490C-8F1D-4DED618B1DEB/F6AC36E0-BBA9-4920-8F9E-6ABE15C9A911.jpg)

参考链接：

1. [TekRevue: The Complete Guide to Customizing the Mac OS X Dock](http://www.tekrevue.com/tip/the-complete-guide-to-customizing-mac-os-xs-dock-with-terminal/)
2. [知乎：OS X 中应如何布局 Dock 上的图标？](https://www.zhihu.com/question/21678287)
3. [Scomper：从 Windows 到 Mac](http://www.jianshu.com/p/00b21f0696db)

想要获得更多简单实用的小技巧？*[查看往期「一日一技」>](http://sspai.com/tag/%E4%B8%80%E6%97%A5%E4%B8%80%E6%8A%80)*

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33493)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8b3e60bf-46e9-44d3-9595-2fc6773c9722/8b3e60bf-46e9-44d3-9595-2fc6773c9722/)