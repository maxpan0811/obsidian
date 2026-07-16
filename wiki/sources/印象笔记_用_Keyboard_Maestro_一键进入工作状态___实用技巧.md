---
title: "用 Keyboard Maestro 一键进入工作状态 _ 实用技巧"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/用 Keyboard Maestro 一键进入工作状态 _ 实用技巧.md
tags: [印象笔记]
---

# 用 Keyboard Maestro 一键进入工作状态 _ 实用技巧

# 用 Keyboard Maestro 一键进入工作状态 | 实用技巧 --- 用 Keyboard Maestro 一键进入工作状态 | 实用技巧 ========================

---

# 用 Keyboard Maestro 一键进入工作状态 | 实用技巧

---

用 Keyboard Maestro 一键进入工作状态 | 实用技巧
==================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/E2C6B125-B8DF-4F67-85FF-2BC4F832C461.gif)

效果展示

细心观察的话，每个人用电脑工作时都会有常用的软件，有些人甚至会将不同的软件以固定的大小和位置平铺在桌面上。

将这些软件打开，再调整到预设的位置和大小是非常适合机器去做的事。通过 Keyboard Maestro，你将能够做到设一个快捷键，将软件以你想要的大小和位置，铺在桌面。

如果你清楚 Keyboard Maestro 如何工作，可以直接查看[完整动作图示](https://cdn.sspai.com/%E7%A4%BA%E6%84%8F%E5%9B%BE.png)，或者直接[下载动作](https://cdn.sspai.com/Work%20Mode.kmmacros)。如果你想知道每一步的来由，可以看下面的教程。

首先，设定一个触发快捷键
------------

在这个动作里，这个快捷键相当于所谓的老板键。不管你屏幕上现在铺着多少窗口，只要按下这组快捷键，所有窗口都会消失，工作的软件会铺回桌面。

在 Keyboard Maestro 里，要在 `New Trigger` 里选择 `Hot Key Trigger` ，然后直接输入你想使用的快捷键。我在这里设的是 `⌘Command-⇧Shift-⌃Ctrl-W`。

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/A8A4449E-AEFC-4473-92DB-039D1C4FEE03.gif)

设置快捷键

第一步，隐藏所有其它软件
------------

Keyboard Maestro 里有内置的隐藏所有软件的动作，叫做 `Hide All Applications`。使用方法就像用 Workflow 那样，从动作库里把动作拖到动作流中即可。

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/50159D9C-7F70-4905-8892-A4917531F2F8.png)

隐藏所有软件

第二步，选择要打开软件
-----------

这一步也很容易，在动作库里找到 `Open a File, Folder or Application`，把它拖到动作流，选择要被打开的软件即可。

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/6F0B9F1F-BC03-41B3-A0DA-793AB37A14D4.png)

选择要打开的软件

第三步，调整软件窗口的大小和位置
----------------

现在我们已经可以做到用快捷键把软件打开了。接下来是核心的一步，也是相对比较难搞的一步。我们要在这一步决定窗口的大小和位置。

Keyboard Maestro 中针对窗口大小和位置当然也有现成的动作：`Move and Resize Front Window`

这个动作里首先已经内置了不少窗口的排列方式，比如常见的上下左右半屏、或者四分之一大小：

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/5F884E32-51D8-4B3E-A5B5-D94F475B764B.png)

内置的窗口排布

如果这些尺寸可以满足你的话，你只要在这一步把软件窗口的大小和位置设定好即可。如果你想做自定义，可以选择上图中 `Custom` 这个值。在这里我们就要接触到 Keyboard Maestro 中设定窗口位置和大小的语法了，Keyboard Maestro 的[官方 Wiki](https://wiki.keyboardmaestro.com/function/SCREEN) 中对这些语法有详细的说明，我在这里只介绍我们会用到的。

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/8DFEA4A6-117F-4AA2-B6D2-3E8ACAEF3EF7.png)

自定义窗口排布

* `SCREENVISIBLE`：屏幕的有效显示区域，去除了 Menu Bar 和 Dock
* `Main`：主窗口
* `Left`, `Top`, `Width`, `Height`：各自代表它们本身的意思
* `百分数`：在 `Left` 和 `Top` 的部分，百分数代表距离对面边缘有多远，计算都是从左到右从上到下。比如下面会出现一个 `SCREENVISIBLE(Main,Right)*35%` ，它代表距离屏幕**左**边缘有屏幕宽度的 35%。

Keyboard Maestro 调整窗口位置和大小时也支持绝对座标，但是考虑到不同设备有不同的分辨率，我还是比较建议用百分比来调节位置。

选择完窗口的位置和大小，还要指定该调整作用的软件（上图的最下部）。否则 Keyboard Maestro 是不知道你要调整哪个软件的窗口的。

第四步，同时调整多个软件的窗口
---------------

前三步大家搞定了如何对一个窗口一键调整大小和位置，接下来我们要完成一键让多个软件做到这一点。

我们可以先把打开软件和调整窗口这两个动作多放几个：

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/40E1848F-7E51-4352-87CA-BC7D2DF70F4D.png)

先打开软件，再排列软件窗口

按照我们人类的思维，这样做其实没什么毛病：把要打开的打开，然后再挨个排列窗口。但实际我们运行这个动作，就会发现，这个动作运行完以后，软件会打开，有的窗口会排列，有的窗口不会。问题出在哪？

问题在于，因为机器的性能不同，打开软件的快慢并不一样。而跑命令对于计算机来说都是瞬间跑完的。于是就会出现「我们还没打开某一个软件，Keyboard Maestro 却已经执行了调整它窗口的命令」这种情况，结果自然就会无效。所以我们在这里，要做的是**让命令等一等软件的启动**。

Keyboard Maestro 里有一个动作叫 `Pause Until`，它的作用就是将一个动作流暂停，等到运行情况满足了某个条件，再将动作继续。我们在这里要等的条件是：当所有要调整窗口的软件都在运行状态时，再调整它们的窗口。

![](.evernote-content/E12026E4-8A47-417D-AB9B-34CCC075A1B0/F98BA881-DA50-4134-A599-6CC3DE95DF0F.png)

在打开和排列中间，插上一个条件

所以我们要把这个动作，**插在打开窗口和调整窗口的动作之间**，把其中的条件，设为「所有要被调整窗口的软件都在运行」。

为了截图方便，只用了两个软件作为范例。如果你 Mac 的屏幕够大，运行速度够快，是想铺多少个软件就可以铺多少个的。

[⬇️ **示例动作下载**](https://cdn.sspai.com/Work%20Mode.kmmacros)（复制链接到 Mac 下载）

[> 完整动作示意图](https://cdn.sspai.com/%E7%A4%BA%E6%84%8F%E5%9B%BE.png)

[#Keyboard Maestro](https://sspai.com/tag/Keyboard%20Maestro)[#macOS](https://sspai.com/tag/macOS)[#技巧](https://sspai.com/tag/%E6%8A%80%E5%B7%A7)

---

[🌐 原始链接](https://sspai.com/post/40784)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c788d3ff-ca09-4c8d-94bc-93283d89be52/c788d3ff-ca09-4c8d-94bc-93283d89be52/)