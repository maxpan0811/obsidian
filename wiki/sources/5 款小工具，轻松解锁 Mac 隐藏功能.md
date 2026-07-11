---
title: 5 款小工具，轻松解锁 Mac 隐藏功能
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/5 款小工具，轻松解锁 Mac 隐藏功能.md
tags: [印象笔记]
---

# 5 款小工具，轻松解锁 Mac 隐藏功能

---

5 款小工具，轻松解锁 Mac 隐藏功能
====================

1小时前

[![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/22804F89-5CEC-4A64-ACD0-63393964037E)](https://sspai.com/user/734392)

#### [Adventure](https://sspai.com/user/734392)

目录
:   1. [TinkerTool](https://sspai.com/post/45668#ss-H2-1531452241314)
    2. [MacPilot](https://sspai.com/post/45668#ss-H2-1531455484231)
    3. [CockTail](https://sspai.com/post/45668#ss-H2-1531457087814)
    4. [Deeper](https://sspai.com/post/45668#ss-H2-1531457094993)
    5. [OnyX](https://sspai.com/post/45668#ss-H2-1531457100373)

在 macOS 系统中，有一些默认未被开启的功能。通过有选择性地开启这些隐藏功能，可以方便我们的对 Mac 的使用。然而，这些功能和设置要么隐藏的路径较深，要么需要在终端中输入指令来开启。这对于普通用户来说有一定的门槛。本文将会介绍五款实用的小工具，用它们帮你通过点击轻松打开 Mac 的隐藏功能，让你的 Mac 更趁手好用。

TinkerTool
----------

TinkerTool 是一款专注于管理系统设置的免费应用。借助它，我们可以对 macOS 的访达、程序坞、Launchpad 等不同组件的设置进行更改。你可以在 [官网](https://www.bresink.com/osx/TinkerTool.html) 下载 TinkerTool。

打开 TinkerTool 后可以看到，它分为「Finder」、「Dock」、「Launchpad」等不同的标签页。接下来，我会分别介绍在不同标签页中我们都可以打开哪些有用的隐藏功能。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/167BA1CB-5936-47D8-91B6-095AF8EFBF5A)

应用界面

### 访达

#### 在访达的标题栏中显示文件路径

在「Finder」标签页中，勾选「Finder options」中的最后一行，「Show selected path in window title」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/F0C506B3-ED3F-4CEC-B8FB-41538582EC0D)

经过这样的设置，当我们在访达中打开文件时，标题栏会显示我们所处的路径。当文件夹层级较多时，开启这个功能可以帮你更方便地定位自己的文件。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/C7F1E906-0F12-4AFD-B719-969EC4BD0B36)

开启后效果

#### 为访达添加「Command + Q」

我们都知道，在 macOS 中，访达是唯一一个无法被退出，只能关闭窗口的应用。如果你希望让访达也可以被彻底关闭，那么可以勾选「Finer options」中的「Add “Quit” item to Finer menu」。这样，你就可以通过「Command + Q」的快捷键将访达彻底关闭。不过需要注意的是，访达关闭后，桌面上的文件也会随之不再显示。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/F7C4CF4F-8C4B-4EED-A8DE-92CEBBA783EB)

对我个人而言，开启这一选项的作用实际是方便重新启动访达。相比用「Option + Command + Esc」呼出强制重启应用窗口，选择访达再点击强制重启，直接用快捷键关闭然后打开相对而言更为方便。

需要注意的是，当你对访达的设置进行调整后，需要点击右下角的「Relaunch Finer」重新启动访达，然后设置才会生效。

### 程序坞

#### 将隐藏应用的图标「虚化」

用「Command + H」隐藏当前应用，是一个常用的快捷键操作。不过在 macOS 的默认设置中，隐藏后的应用在程序坞中的图标和其他应用没有什么区别。这样很容易让你忘记自己到底隐藏了什么应用。

在「Dock」标签页中，勾选「Dock Options」部分的第一行，「Use dimmed icons for hidden applications」，即可让被隐藏应用的图标被「虚化」，从而帮你容易地将它们区分出来。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/A348658F-E401-4F90-B23C-A09B415D34A4)

#### 取消显示程序坞的延时

很多人喜欢在「系统偏好设置-程序坞」中选择「自动显示和隐藏程序坞」，从而更好地利用屏幕空间，尤其是我这种使用 12 英寸 MacBook 的用户，屏幕空间更是寸土寸金。然而问题在于，macOS 系统在指针移到屏幕底部和程序坞之间显示设置了延时。这一明显可以感知的延时可以说令人非常不爽。借助 TinkerTool，你可以轻易将它关闭。

同样在「Dock Options」中，勾选「Disable delay when showing hidden Dock」，即可取消恼人的延时，程序坞的弹出将变得丝滑流畅。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/8E405E06-D29A-4695-AEB6-AE279B8F78EE)

#### 在程序坞右侧添加「最近使用的应用」堆栈

在 iOS 11 上，iPad 的 Dock 栏最右端会显示三个最近使用的 App，这一特性也随 macOS Mojave 来到了 macOS 平台。不过，类似 iPad 上的情况，这一栏中没有在运行中的最近打开应用不能超过三个。如果你觉得这还不够多，或是希望你的系统现在就可以获得类似的体验，可以通过 TinkerTool 在程序坞中添加相应的堆栈。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/E82FE111-B147-4197-A3D8-7E830EC07A65)

效果图

在「Stacks」部分，勾选「Add stack for recent items」，在废纸篓的左边会出现一个名为「Recent  Applications」的堆栈，最多可以存放十个应用图标。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/D9E51DBA-AE89-4C94-8E39-EDE0109E7153)

#### 开启「专注模式」

相比于 iOS 上较为受限的多窗口功能，macOS 上的多窗口更为灵活，但这也有可能对你正在进行的工作产生干扰。如果你希望暂时专注于一个应用，可以打开单窗口模式。

勾选「Single Application Mode」这一部分，即可打开单窗口模式。在该模式下，当你打开一个窗口后，其他的所有正在运行的应用窗口都会被隐藏。如果你在工作时希望不被其他窗口分神，可以考虑开启这个模式。当然，工作完成后不要忘记将它关闭。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/3279D1FF-427B-4461-920F-86540336310E)

和对访达设置时一样，在完成调整后，需要点击页面右下角的「Relaunch Dock」才能生效。

### 其他设置

#### 去掉截图命名里的截图时间

在 macOS 的默认设置中，截图会被命名为「屏幕截图+截图日期+截图时间」。然而实际上，大多数情况下，我们并不需要知道某张截图是什么时候的截图，即使有需要也可以在文件的简介中查看。此外，这一命名方式也相对没有规律，不利于我们之后对截图的使用。如果能够让截图的命名自动按数字排序，可能会更为方便。

在「General」标签页中，取消勾选「Screenshot file format」下面的「Include recording time in file name」。这样，第一张截图会被直接命名为「屏幕截图」，之后的则会是「屏幕截图1」，以此类推。这一更改将会在你下次从锁屏页登录系统后启用。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/E1E76C4E-2B8B-49F0-86C3-1DF88D817295)

#### 将崩溃报错更改为通知

当某个应用崩溃后，系统会弹出一个报错窗口，里面包含大部分普通用户看不懂的说明，以及「重新启动」、「关闭」等选项。但实际上，我们只需要知道某个应用崩溃了即可，没有必要再点选一个窗口。

在「Desktop」标签页中，勾选「When applications crash」部分的「Use Notification Center」。这样，应用崩溃后的报错就会改为显示一条通知，相比原本的设置，减少了对我们的打扰。这一更改将会在相应的应用重新启动后启用。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/705F8A7B-7BA1-45CA-A582-14BD6BC177A8)

拓展阅读：[Mac 上需要命令行才能启动的实用功能，用这个 App 就能轻松打开：TinkerTool](https://sspai.com/post/45389)

MacPilot
--------

相比 TinkerTool，[MacPilot](https://www.koingosw.com/products/macpilot/) 的功能更为丰富。它不止可以让你开关系统隐藏，还可以调整众多系统设置。不过，它那「复古」的界面，可能没有 TinkerTool 那么讨喜。你可以在 [官网](https://www.koingosw.com/products/macpilot/) 下载 MacPilot。应用需要购买或订阅，在此之前你有 14 天的试用期。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/9FD835A3-4EFF-4435-BA08-87BC8B3870E3)

应用界面

我们所需要开启的隐藏功能，都存在于「App」这个标签页中。大多数 MacPilot 可以开启的功能都和 TinkerTool 相同，对于这部分功能，下文只简单讲述开启路径。文章的笔墨则会重点放在前文没有的功能上。需要注意的是，当我们对设置进行更改时，MacPilot 会提示我们将相应部分进行重启。

#### 在访达的标题栏中显示文件路径

在「App-Finer-Appearance-General」中，勾选「Show full path  in window title bar」即可。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/04BC5471-333F-48B1-801E-312E11395BDA)

#### 为访达添加「Command + Q」

在「App-Finder-Features-General」中，勾选「Show “Quit Finer” in the “Finer” menu」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/323441C6-7F26-4DE0-B21D-377E133683E5)

#### 将隐藏应用的图标「虚化」

在「App-Dock-Appearance-General」中，勾选「Fade icons for hidden applications」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/D3559609-6A8A-4BDB-B1EA-C6B263497231)

#### 取消显示程序坞的延时

在「App-Dock-Behavior」中勾选「Automatically hide and show」，并将下一行的延时改为 0。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/63C36B05-1421-4885-885C-98CE221633F5)

#### 在程序坞右侧添加「最近使用的应用」堆栈

在「App-Dock-Behavior」中点击「Add ”Recent“ Stacks to Right」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/BCAFB365-14A8-435A-ACE7-597618682F33)

#### 开启「专注模式」

在「App-Dock-Behavior」中勾选「Single application mode」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/172EFE87-7600-45EF-80A5-5169824D02BA)

#### 去掉截图命名里的截图时间

在「App-Grab (Screenshot)」中取消勾选「Include the date and time in file name」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/F1F707A3-F467-47B9-8677-0E97BBC710E9)

#### 将崩溃报错更改为通知

在「App-System-Interface」中将「Crash reporter type」改为「Short Notice」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/1DB8D259-4DD8-4F90-AB73-AE5B966399FF)

#### 允许在 QuickLook 中进行选词

在「App-Finder-Features」中勾选「QuickLook」部分的「Allow text selection」。应用会提示我们重新启动访达。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/9E8B2F6F-EDAE-4068-9288-1A0914F5A7AD)

完成设置之后，当你用空格键或者 Force Touch 进行快速预览时，将可以在预览窗口里对文本进行选择和复制。这一功能适用于 txt、pdf、pages、doc 等格式。此外，当你使用 Force Touch 或三指点按单词进行查词时，也将可以对词典内容进行选择和复制。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/B010EAD8-449C-4EDC-835B-943D6160ADF9)

效果图

#### QuickTime Player 打开视频后自动铺满屏幕

在「App-QuickTime」中勾选「Interface」部分的「Automatically size movies to fit well on screen」。如果你已经打开了 QuickT咩 Player，则需要将其重新启动。之后，当你用它打开视频时，窗口会自动调整至铺满屏幕。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/140640DF-217F-4CD8-B6F3-C074A4599AB6)

以上介绍的两款应用，对系统版本没有非常严格的要求。而接下来将要提到的三款应用，则需要特别注意应用版本和系统版本。它们的**每一个版本都对应了 macOS 的一个大版本，也只能在该系统版本下运行**。例如，OnyX 最新的 OnyX 3.4 只能运行于 macOS High Sierra 系统。如果你在使用 macOS Mojave 的 Beta 版，那么只能等到正式版推出后，下载 OnyX 3.5 来使用。

CockTail
--------

[CockTail](http://www.maintain.se/cocktail/) 同样是一款包括了系统优化、文件删除、默认功能更改的辅助应用。你可以在 [官网](http://www.maintain.se/cocktail/) 下载对应版本的 CockTail。不过同样，它的图标也相对老旧，如果你对应用的外观比较在意，可以考虑介绍的其他应用。

打开应用后，它同样包含「 Disks」、「System」等标签页。本次我们用到的功能则集中于「Interface」中。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/0463E55A-8B24-4CD0-879F-E954547C4FE0)

应用界面

#### 在访达的标题栏中显示文件路径

在「Interface-Finer」中勾选「Show full folder path in window title」。然后，点击「Relaunch」重启访达即可生效。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/56D1E261-30A0-4C61-9579-5E06C9EA396E)

#### 为访达添加「Command + Q」

在「Interface-Finder」中勾选「Add “Quit” item to Finer menu」。同样需要点击「Relaunch」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/CD4017E0-6998-4FBF-859E-F6102598B8A0)

#### 将隐藏应用的图标「虚化」

在「Interface-Dock」中勾选「Enable transparent icons for hidden applications」。类似对访达的操作，修改完成后需要点击「Relaunch」，下面的三项设置也是这样。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/7B6875DA-81BA-45A5-BD66-95982AC7A0A2)

#### 取消显示程序坞的延时

在「Interface-Dock」页面的下方，将「Auto-show delay」调至 0。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/DC6589A8-AF5D-47D8-BB33-EC51BFE664B9)

#### 在程序坞右侧添加「最近使用的应用」堆栈

同样在「Dock」页面的下方，将「Add Recent Items stack on the」后改为「Right」，然后点击「Add」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/5943A6B9-5431-495F-83B7-7D4F5F9DA73B)

#### 开启「专注模式」

在「Interface-Dock」中勾选「Enable Single Application mode」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/22FBCE38-1D4C-4FB5-8FE8-C449726D4766)

#### 去掉截图命名里的截图时间

在「Interface-General」中，勾选页面下方的「Remove date and timestamp」。如果你希望更改截图的默认命名，还可以对「Default name」进行修改，然后点击「Apply」。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/BC81B3B6-14AA-4533-8D34-40A23C480371)

Deeper
------

类似TinkerTool，Deeper 也是一款专注于修改系统默认设置的辅助应用。相比 MacPilot 和 CockTail，它的界面和图标更贴合当前系统，而功能上也毫不逊色。更值得一提的是，Deeper 拥有中文界面。尽管一些翻译相对生硬，但也极大地降低了中文用户的使用门槛。你可以在 [官网](https://www.titanium-software.fr/en/deeper.html) 根据系统版本下载相应的应用。

#### 应用界面

#### 在访达的标题栏中显示文件路径

在「Finer」中，勾选「显示项路径在窗口标题」即可。

#### 为访达添加「Command + Q」

在「Finder」中，勾选「显示 Finer 退出项」。

#### 将隐藏应用的图标「虚化」

在「Dock」中，勾选「查看」部分的「隐藏的应用使用透明图标」。

#### 取消显示程序坞的延时

同样是在「查看」部分，勾选「自动显示和隐藏 Dock」，并勾选下一行的「关闭特效」。

#### 在程序坞右侧添加「最近使用的应用」堆栈

在「Dock」中，在「添加最近的活喜欢的项到堆栈」部分选择「往右边」。

#### 开启「专注模式」

在「Dock」的「其他选项」部分，勾选「打开单程序模式」。

#### 去掉截图命名里的截图时间

在「通用」中取消勾选「包括日期和时间捕获的名字」即可。如果你希望修改截图的默认命名方式，也可以在下方的「名称」中进行更改。

OnyX
----

严格说来，[OnyX](https://www.titanium-software.fr/en/onyx.html) 实际上并不是一个单独的应用，而是一个集成了 Deeper 和官网上另一个应用 Maintenance 在内的软件。除了 Deeper 的功能，它还可以帮你删除无用的文件、重置错误的系统文件，甚至将这一切自动化。不过也正因如此，OnyX 在开启系统隐藏功能上的方式与 OnyX 完全相同，只需要在 OnyX 的「参数」页面进行设置即可。

![](.evernote-content/878C6473-729A-47E8-B42F-1208112BF9C9/B05175E9-2F49-4BF8-B530-3A884E636D09)

应用界面

你可以在 [官网](https://www.titanium-software.fr/en/onyx.html) 根据系统版本下载 OnyX。

---

[🌐 原始链接](https://sspai.com/post/45668)

[📎 在印象笔记中打开](evernote:///view/207087/s1/438b4b00-004e-4ccf-b356-192d80b05eeb/438b4b00-004e-4ccf-b356-192d80b05eeb/)
