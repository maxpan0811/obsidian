---
title: Keyboard Maestro 在窗口管理上的应用 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Keyboard Maestro 在窗口管理上的应用 2.md
tags: [evernote, impression, yinxiang]
---

# Keyboard Maestro 在窗口管理上的应用

---

Keyboard Maestro 在窗口管理上的应用
==========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

窗口管理不只是调整窗口的大小和位置，在实际的使用上，像是切换窗口内的标签页、切换窗口所在虚拟桌面等操作，都属于窗口管理的一部分。

对于调整窗口的位置和大小，已经有了不少现成的工具，在《[macOS 窗口管理工具 | Best Of](https://sspai.com/post/55470)》一文中我们就能找到不错的选择。但是标签页管理以及调整窗口所在虚拟桌面这两个问题，市面上还没什么提供直接解决方案的工具。

这就是 Keyboard Maestro 发挥威力的时候了。除了常规的窗口位置、大小调整之外，我们还可以用 Keyboard Maestro解决窗口内的标签页、窗口所在桌面管理问题。比如把多个窗口合并到同一个标签页：

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/EB6D685E-1DC7-47E8-8402-9F7CD7B65E35.gif)

合并窗口

以及，把窗口移动到指定桌面：

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/AF039B22-304A-4081-BB4D-DF7D55A6BDE3.gif)

移动窗口到指定桌面

可以说，Keyboard Maestro 可以全面覆盖你的窗口管理需求，在这篇文章中，我将提供 7 个动作，和你分享 Keyboard Maestro 在窗口管理上的实践。

注：本文有小部分动作不是我制作的，或者我没做出主要贡献，故不方便放到自己的 GitHub 仓库中，仅提供直链下载。这些动作请大家关注原作者的消息。

窗口管理系列
------

狭义上的窗口管理指的只是窗口本身大小、位置的调整，最常见的左半屏、右半屏已经成为窗口管理工具的基础功能，除此之外，这节还会介绍还原窗口大小和滚动切换窗口两种动作。

由于涉及到控制系统部件（窗口、标签页、模拟点击之类），部分动作运行时可能会要求权限。反正这些动作都是开源的，大家不用担心安全问题。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/94F41698-80AE-4D9D-AC67-5A0470289A42.png)

授予 Keyboard Maestro 控制 App 的权限

### 滚动切换窗口

Finder 里有一个很让其他应用羡慕的功能，即按 `` ⌘Command-` `` 在几个窗口间按顺序切换，效果有点像用 `⌘Command-⇥Tab` 滚动切应用。早几年时候其他原生应用也能用上这一功能，不过最新系统上似乎都不再奏效。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/579C3BC4-B65D-49B8-A3F9-C3CE5B5FF73D.gif)

滚动切换窗口

滚动切换的原理其实是计算当前应用的窗口数量，然后按编号挨个换过去，于是就 [有人](https://macscripter.net/viewtopic.php?id=29904) 用 AppleScript 重新实现了一遍。原作者只提供了一段 Safari 专用的代码，我把它改写后移植到了 Keyboard Maestro 里，使其在大多数应用里都可以使用（测试了一批原生和第三方应用，暂时没出现失效的情况）。快捷键和 Finder 一样都是 `` ⌘Command-` ``，而且和 Finder 自带的不冲突。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/5DFF72C7-AC80-47C2-B447-C5CD0C1D034E.png)

Finder 支持在窗口间滚动切换

[> 动作下载](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Window%20Manager/Window%20Roll.kmmacros.zip)

这个动作我在 Safari 里用得最多。Safari 没有给标签页分组的功能，有时候页面开多了就只能再分到几个不同窗口里（不然会挤得横跨整个屏幕都塞不下），比如查个资料，可能几个 GitHub 仓库放一窗口、几篇 Stack Overflow 问答塞一个窗口，再单开一个窗口来搜索，这时候就可以通过窗口切换的 Keyboard Maestro 动作快速定位，而不用像原来那样去标签页里闷头乱翻。

### 左半屏和右半屏

以左半屏和右半屏这对窗口排布为代表，各种**分屏布局**是最抢手的功能，在各家应用宣传页面上整个窗口忽而向左、忽而朝右的 GIF 看上去也很有动感。

左右对半开的排布用得最多，习惯的用法是左边放文件夹、右边开编辑器，或者一侧搁参考页面、一侧对付文章草稿。我提供的动作也是左右开，具体的排布方式和快捷键也可以自己设置。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/2F44754F-0D22-4079-A6BD-271B00521B26.gif)

让窗口占据左半屏或右半屏

* [动作下载](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Window%20Manager/Window%20Half%20Screen.kmmacros.zip)
* 默认键位：

+ 左半屏：`⌃Control-⌥Option-⌘Command-<`
+ 右半屏：`⌃Control-⌥Option-⌘Command->`

Keyboard Maestro 已经内置了最常见的分屏布局方案，使用频率最高的全屏、半屏乃至四角 1/4 布局都有现成的选项可用，其他尺寸也能在「Move and Resize Window」这一模块中自行设置。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/3B9EDFA5-DEFD-4472-8720-9170C2A679D0.png)

靠左或靠右占据半个屏幕的设置

这组动作在改变布局前还会记录下窗口大小和位置，以便稍后通过另一个动作还原改动前的窗口样式。

### 还原窗口大小和位置

左半屏和右半屏等都是比较极端的窗口布局，往往只在我们进入 Work Mode 时开一下（而且一般会把界面压缩得很奇怪，本质上只是窗口太小时的折衷方案）。进一步的问题就是怎样把它们变回去，回到常规的窗口大小。但是很多管理工具只管变形，不管恢复，这就有点让人懊恼。

我们还是用 Keyboard Maestro 来解决这个问题。区别于很多自动化工具，Keyboard Maestro 有比较完善的**变量**特性，可以长期储存一些数据 —— 在这里指的当然就是窗口原位置和尺寸了。通过上一节的动作移动窗口后，运行下面的 Keyboard Maestro 动作就能回到更改前的窗口状态。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/DAA898A6-9D51-49A2-AE4C-03CA0F93D505.gif)

还原变动前的窗口大小

[> 动作下载](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Window%20Manager/Window%20Back.kmmacros.zip)

键位上我设计的是 `⌃Control-⌥Option-⌘Command-?`，正好跟在 `<` 和 `>` 键后面成组使用。前两个动作运作时记录下的窗口状态，在运行还原动作后就会重新赋予给当前窗口。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/D413084A-6E40-4139-B83A-9A1D1F65CB13.png)

还原窗口的设置

有些时候工作得无聊可能会左左右右分屏玩（就像 Windows 用户右键刷新桌面一样），后悔把窗口搞乱的话也可以运行这个动作救急。不过还原动作只能搭配其他 Keyboard Maestro 动作用，和另外的窗口管理工具是不能打配合的。

标签页管理系列
-------

做窗口管理的工具何其多，但是涉足标签页管理的工具就屈指可数了。标签页不想窗口那样需要频繁调整大小，但是基础的左右切换等功能还是有必要存在。自己实现这些功能时发现并不简单，针对标签页似乎没有统一的系统控件可用，最后用了一些比较取巧的方案。

### 合并所有窗口成标签页

第一个功能还是和窗口有关，即把一个应用的**窗口合并为到一起**，变成多个标签页。窗口泛滥是常有的事情，有些应用本身新建标签页的快捷键就与众不同而容易导致按错，比如脚本编辑器就不按常理出牌，习惯性按下 `⌘Command-T` 结果会出来一个字体 Type 的弹窗 —— 总之，挺多时候不知不觉开了一堆窗口，嫌杂乱的话就可以把它们一键收纳起来。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/EB6D685E-1DC7-47E8-8402-9F7CD7B65E35.gif)

[> 动作下载](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Window%20Manager/Tab%20Merge%20from%20windows.kmmacros.zip)

实现这一动作依靠的是「Select or Show a Menu Item」模块，不过和常规用法不同，这次要跳过具体应用、直接指定点击「Window」菜单下的「Merge All Windows」选项，如此一来 Keyboard Maestro 便会在当前应用的菜单栏里寻找这一选项，从而在绝大多数应用里面正常工作。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/3FCF82F8-17C9-4DB9-84EA-FE605F09EB2C.png)

### 全局适用的标签左右切换

讲窗口管理的时候我们中 Finder 里借鉴了一个 `` ⌘Command-` `` 快捷键来滚动切换窗口，这次换作从 Safari 偷师一回，把**左右切换标签页**的操作带到各个应用中去。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/68E64818-E8CC-49E2-8B72-37720D028EA4.gif)

使用统一的快捷键切换标签页

[> 动作下载](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Window%20Manager/Tab%20Next:Previous.kmmacros.zip)

切换标签页这个基础操作在各个应用中快捷键是不一样的，特别是第三方工具，往往自成一派，很不方便记忆键位。考虑到浏览器是最常用的工具之一，在 Safari 里切标签页也几乎练出了肌肉记忆，我的做法就是把大家的键位都照着 Safari 统一起来，这样便不用为每个应用额外记忆一次。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/C147F730-AD07-4636-8E4F-0D111263F9A4.png)

各个应用切换标签页的快捷键不同

实现原理就比较奇特了，因为每个应用切换标签页的菜单栏选项名字都少有不同 —— 比如往后切一个，Safari 本身是「Show Next Tab」，而我常用的脚本编辑器 CodeRunner 是「Select Next Tab」—— 导致没法把动作写死，于是我换成用 AppleScript 脚本来寻找应用的菜单栏，点击其中名字包含（`whose name contains`）「Next Tab」的项目，基本一打一个准。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/5126471F-44AD-4DC3-B687-6FAA1C00A823.png)

左右移动一个标签页的动作设置

当然，这个脚本不能直接用到中文界面的应用中，需要大家自己改写。一个应用或许没有中文界面，但几乎不可能不提供英文界面，为了通用性考虑我只提供英文下的解决方案。

虚拟桌面切换
------

虚拟桌面是许多 macOS 用户的常用工具。如果一个桌面还不够你堆放窗口，最简单的方法就是再开几个桌面来扩大施展空间。桌面开多了之后，在几个桌面间移动窗口就会变得比较麻烦。

桌面在 macOS 下的标准称呼是 Desktop，不过呼其俗称的人不在少数，用「Space」「Workspace」「Screen」的都大有人在，简单起见我们约定一下只用「桌面」。

本节动作作者是 Keyboard Maestro 论坛的 Tom，他非常精炼地把 8 个动作压缩在一个 Keyboard Maestro 动作里，对于新手来说可能有点难搞懂，所以我进行了分拆。原讨论贴的地址在 [这里](https://forum.keyboardmaestro.com/t/move-frontmost-window-to-a-different-space/10512)，有能力的读者建议试试原版动作。

### 将窗口左右移动一个桌面

macOS 里一直都有一套左右移动桌面的快捷键（默认是 `⌃Control-←` 和 `⌃Control-→`），但这是切换整个桌面，而不能移动单个窗口到其他桌面上。折腾窗口移动的自动化玩家可以说是前仆后继，但因为苹果没有开放相应的接口，很多人空有一身代码功夫却无处施展。

直到 Keyboard Maestro 论坛上有几位高手利用 KM 来模拟键鼠操作，才巧妙解决了这一窗口移动问题。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/163379C9-7AD7-4F93-884C-C49C91362343.gif)

将窗口移到其他桌面

[> 动作直链下载](https://cdn.sspai.com/minja/Window%20to%20Space.kmmacros.zip)

在手动切换的情况下，通常我们会想到开启 Mission Control 界面再把窗口拖到目标桌面，其实还有更加流程化的移动方式：

1. 用光标按住一个窗口的顶栏
2. 按快捷键 `⌃Control-←` 或 `⌃Control-→` 向左 / 右切换一个桌面
3. 松开光标，窗口也会跟着移动到新的桌面

这串操作只涉及了鼠标和键盘的常规点按操作，完全可以在 Keyboard Maestro 模拟一遍。唯一需要注意的是，在 Mojave 系统中 Keyboard Maestro 模拟的快捷键 `⌃Control-→` 和系统存在冲突，需要把系统的桌面切换快捷键改掉（KM 里相应的也要改一下）。原作者推荐的键位是下面这长长两串：

* 向左移动一个桌面：`⇧Shift-⌃Control-⌥Option-⌘Command-Q`
* 向右移动一个桌面：`⇧Shift-⌃Control-⌥Option-⌘Command-W`

虽然长到不可思议，但也能有效避免撞快捷键。随之而来的一个问题是系统自带的切换组合键变得难用了，介意这一点的读者可以通过 [这组](https://cdn.sspai.com/minja/Space%20Next:Previous.kmmacros.zip) Keyboard Maestro 动作模拟原有的短键位。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/4C085B90-7573-41A6-95A2-8813B72D0841.png)

左右移动一个桌面的设置

### 将窗口移到指定桌面

理解了左右移动的实现方式后，把窗口切到指定桌面的动作就比较好懂了。这套 Keyboard Maestro 动作原理仍然是模拟键鼠操作，只是把快捷键换成了系统自带的 `⌃Control-数字键`（用于切换指定桌面）。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/AF039B22-304A-4081-BB4D-DF7D55A6BDE3.gif)

移动窗口到指定桌面

[> 动作直链下载](https://cdn.sspai.com/minja/Window%20to%20Specific%20Space.kmmacros.zip)

和方向键不同，数字键暂时没出现和系统冲突的问题，所以这回不需要改动系统快捷键。不过在使用前记得要去系统键盘设置中勾选切换桌面的快捷键，如果没有看到 `⌃Control-数字键` 系列键位，可能是因为当前只有一个桌面，多开几个虚拟桌面就能看到这些键位如期现形。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/169F434F-985E-4ECA-8C48-B58921389BA9.png)

移动到指定桌面的设置

对于习惯一个桌面做一套工作的人而言，指定桌面来切换窗口的动作是比较实用的，可以把桌面 1 设置成工作区，桌面 2 拿来查资料，桌面 3 放置聊天软件的窗口。提示一下，为了防止 macOS 自作聪明改换桌面顺序（这就让指定桌面编号来切桌面的意义大打折扣），需要在系统 Mission Control 设置中取消勾选第一项桌面自动重排设置。

![](.evernote-content/1D6327D7-E402-4C2E-975B-FAB76319C7C0/98C50446-6CD3-4139-8B1D-CD08D4CA430D.png)

避免桌面自动重排

小结
--

Keyboard Maestro 虽然属于全能选手，但是已经在使用其他窗口管理工具的读者不用全盘迁移到 Keyboard Maestro，毕竟已有现成功能的话，实在没必要自己重头折腾。大家可以根据工具的具体短板，用 Keyboard Maestro 进行弥补和辅助，让各个工具协作起来完善 macOS 窗口管理。

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/55852)

[📎 在印象笔记中打开](evernote:///view/207087/s1/314d255f-728d-4673-b6dc-9ad6ddd906e9/314d255f-728d-4673-b6dc-9ad6ddd906e9/)
