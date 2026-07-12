# 自定义 Touch Bar 功能，让「鸡肋」也能发光发热：BetterTouchTool

---

自 2016 年 Touch Bar 在 MacBook Pro 上问世以来，对其最大的争议就是它并不能很好地提高用户的工作效率：Touch Bar 提供的大多数功能很容易使用键盘快捷键来实现，并且有些时候使用快捷键更加方便、符合直觉。

一年多的时间过去了，虽然越来越多的应用程序添加了 Touch Bar 支持，然而能够用它实现的功能还是十分有限。不过幸好，我们可以通过 BetterTouchTool 这款程序对 TouchBar 进行深度自定义，做到真正提高工作效率。

[BetterTouchTool](https://www.boastr.net/) 是一款著名的触控板增强工具，用户可以使用它来为触控板创建自定义手势，从而大大提高其实用性，Touch Bar 问世之后，BetterTouchTool 也为之添加了自定义功能，本文就将介绍该功能的使用方法。

下载安装之后，BetterTouchTool 的按钮默认就会出现在 Touch Bar 的 Control Strip 区域，点击即可呼出用户的自定义菜单：

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/C298114E-755A-4BD6-A2F4-7902344C284E.jpg)BetterTouchTool 的 Touch Bar 按钮

然而软件并没有内置任何自定义功能，用户需要根据自己的需求在软件里面自行添加。

在 BetterTouchTool 中为 Touch Bar 添加自定义功能非常简单，进入软件主界面之后切换到 Touch Bar 标签页，然后点击「+ TouchBar Button（新增 Touch Bar 按钮）」按钮即可在 BetterTouchTool 的 Touch Bar 菜单中新建一个按钮。

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/FC291B59-6F1E-43D1-B508-0510450939A0.png)创建自定义按钮

新建之后，在列表中选择我们需要编辑的按钮，即可在界面下方依次更改该按钮的图标、名称、点击后触发的键盘快捷键，或者是触发的其他动作。

我们先随意创建一个按钮，选中之后点击「Predefined Action（预置动作）」处，可以看到 BetterTouchTool 内置了许多动作供我们使用，包括模拟鼠标移动与点击、模拟键盘按键、模拟触控板手势、屏幕截图、窗口缩放与位移、系统控制等等……

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/F49FC7E1-AD86-45EC-9A3C-991F1333DD83.png)BetterTouchTool 的内置动作

如果你从未使用过 BetterTouchTool，那么有可能对这么多动作感到无所适从，下面我们就将通过几个范例来介绍如何使用这些动作，制作出你需要的自定义功能。

一键显示隐藏文件
--------

由于 macOS 并未在系统设置中提供显示隐藏文件的开关，每次需要显示隐藏文件时都要在终端中输入一长串指令，想要恢复为隐藏状态又要重新输入一长串指令，十分麻烦。我们可以通过建立一个自定义按钮，来一键显示、隐藏文件，从而解决这一问题。

根据上文介绍的方法，首先点击「+ TouchBar Button」在 Touch Bar 上新建一个按钮，在「Touch Bar Button Name（Touch Bar 按钮名称）」一栏填写按钮的名称，每个自定义按钮都必须有一个名称，否则不会在 Touch Bar 上显示。名称支持 Emoji，可以点击文本框右边的 Emoji 图标选择，这里以「🙈显示」为例作为按钮名称。

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/08E7A13D-FD91-4DCC-BFE3-F28A85CACE15.png)BetterTouchTool 软件设置（左）与 Touch Bar 上的显示效果（右）

此时我们已经可以在 Touch Bar 上找到我们刚刚创建的按钮了，然而点击它却没有任何反应，这是因为我们还没有为其设置任何动作。

BetterTouchTool 中已经集成了显示 / 隐藏隐藏文件的动作，我们在「Predefined Actions - Utility Actions」菜单中将其选中即可：

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/3F44FC35-8A07-4F9A-B75F-F5B044D9C030.png)BetterTouchTool 内置的显示 / 隐藏隐藏文件功能

至此，按钮的全部设置已经完成，点击这个按钮就可以更改隐藏文件的显示状态了。

一键发微博
-----

如果你的系统中装有 Maipo 微博客户端，那么可以通过以下方法使用 BetterTouchTool 在 Touch Bar 上对其进行调用从而撰写微博。

使用与上文同样的方法新建一个按钮，为了美观起见，我找到了新浪微博的 logo，并拖拽到了软件下方的空白处，这样我们的 Touch Bar 按钮就有了图标，接下来在「Touch Bar Button Name」处填写按钮名称，这里以「撰写」为例。填写完之后 Touch Bar 按钮的外观就已经设定完成了。

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/2171B4F7-4978-46DA-ACF0-6BB6CC56D829.png)BetterTouchTool 软件设置（左）与 Touch Bar 上的显示效果（右）

使用 Maipo 客户端发微博的思路为：

1. 先运行 Maipo 应用程序；
2. 向 Maipo 发送「Command + N」快捷键新建一条微博。

确定了实现方法之后我们就可以为按钮添加动作了。

点击软件右下角「Predefined Action」处的按钮，在「Controlling Other Application（控制其他程序）」子菜单中选择「Open Application / File / Apple Script...（打开程序 / 文件 / Apple Script）」这一项，在弹出的窗口中选择「Maipo.app」程序。这样设置之后，每次点击按钮就会启动 Maipo 客户端。然而这样还不够，我们还需要为它发送一个「Command + N」快捷键。

点击 BetterTouchTool 软件下方的「Attach Additional Action（添加后续动作）」按钮，为我们的按钮添加一个后续动作：

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/84BC8C7A-C2AB-4E5E-854F-23D46F97E68C.png)Attach Additional Action

在列表中选择我们创建的后续动作，然后在「Predefined Action」处选择「Controlling Other Applications - Send Shortcut to Specific App（为特定程序发送快捷键）」一项。

在弹出的选项窗口中，将「Shortcut to Send」一项设置为 Maipo 撰写新微博的快捷键「Command + N」，点击「Select Application to Send Shortcut to（选择将快捷键发送至的程序）」，在弹出的打开文件对话框中选择「Maipo.app」程序，并勾选「Bring app to front before sending the shortcut（发送快捷键前将应用转到前台）」选项，否则可能导致发送失败，最终结果如下：

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/948FE33F-21E9-48D0-8D54-19FE2037E852.png)发送快捷键设置（上）与按钮总体动作（下）

点击按钮测试一下：

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/C96CDF1B-438A-49FC-85BA-88CB882F407A.gif)测试

一键弹出所有外置硬盘
----------

我经常会给笔记本接上多块外置硬盘，需要移动电脑时则需要将它们一个个手动弹出，非常麻烦，于是就有了制作一个一键弹出所有外置硬盘按钮的想法。

BetterTouchTool 虽然没有内置弹出设备的动作，但是它支持运行 Apple Script：在「Predefined Action - Controlling Other Application」中选择「Run Apple Script in background」一项，该动作可以在后台运行指定的 Apple Script 脚本，在弹出的窗口中输入（其实我并不会编写 Apple Script 脚本，这一段是在国外的论坛里找到的）：

```
tell application "Finder" to eject (every disk whose ejectable is true and local volume is true and free space is not equal to 0)
```

![](.evernote-content/460B01A6-FD1E-4CBE-8D75-11B217138DD4/FE57BC46-039B-4E1F-B111-C8E98D364473.png)Apple Script 编辑器

写完之后点击「Save」保存，以后每次点击按钮，BetterTouchTool 就会执行这段脚本，将所有外置硬盘自动弹出。

更多
--

本文只是介绍了 BetterTouchTool 对 Touch Bar 的几种自定义方法，希望能给大家提供一个思路，BetterTouchTool 还有许许多多内置的动作与方法，大家可以根据自己的需要，来对 Touch Bar 进行定制，从而真正提供工作效率。

---

[🌐 原始链接](https://sspai.com/post/40787)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2efec489-4950-4762-9775-5eeafd2e8b2c/2efec489-4950-4762-9775-5eeafd2e8b2c/)