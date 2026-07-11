---
title: Alfred Workflow 从使用到创造 - 少数派
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Alfred Workflow 从使用到创造 - 少数派.md
tags: [印象笔记]
---

# Alfred Workflow 从使用到创造 - 少数派

---

Alfred Workflow 从使用到创造
======================

macOS 内置的 Spotlight（聚焦） 功能让我们可以方便地搜索文件、启动应用、查询单词，我还记得刚使用时感到的那份惊艳。直到遇见了 Alfred，在稍作把玩后我就用 Alfred 取而代之。这其中的原因除了 Alfred 在搜索文件与应用等基础方面的优化增强，很大程度上也是由于 Alfred 中的 workflow 功能。

关联阅读：[一站式文件处理中心：Alfred 文件搜索 & 处理详解](https://sspai.com/post/56175)

少数派的读者应该对于 Alfred workflow 都不陌生，毕竟我派发过不少相关文章。它让用户可以像搭积木一样，自己动手实现各种功能，扩充到 Alfred 中，类似于 iOS 中的快捷指令、Android 上的 Tasker。

快捷指令、Tasker 等发展多年后，各路高手玩得不亦乐乎的同时，也越来越多地惠及普通用户。Alfred workflow 也不例外，许多优质的作品被分享出来，种类繁多，五花八门，比如汇率计算、定时器等小工具类型，针对 GitHub、Twitter 等网站的交互搜索型，控制蓝牙、外观模式等系统功能增强型，还有就是连接印象笔记、DEVONthink、Mweb 等第三方应用，通过 Alfred 控制它们，改善使用体验。众多 Workflow 经过长时间的使用和更新迭代，相当成熟稳定。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/CEA2DCAC-2075-4F5C-B9F2-0CFCF6D9F863.png)

Object 展示

学会使用 workflow 的必要性不用再多说，学习编写也非常推荐。除了自己动手丰衣足食的乐趣，更重要的是这两方面原因：一，别人的 Workflow 不一定完全契合自己的需求，也可能已经年久失修，掌握编写方法就可以尝试修改它们；二，解决小问题的简单 Workflow 很少会被大费周章地发布出来，而日常碰到的有些临时问题用 Workflow 解决却是非常合适。

所以，本文首先介绍 Workflow 使用的方方面面，包括导入、配置、管理等，并列出了一些推荐的优质作品、合集仓库。然后，按照入门、进阶的路径，配合实例，带领大家循序渐进地学习如何编写。

为避免混淆，这里先明确下本文中所使用的词语。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/F5159031-59B8-4339-927B-79A0897002C7.png)

文中用语图示

注：本文介绍的功能需要激活 PowerPack。

Workflow 使用
-----------

Alfred 发展至今，解决常见需求的 Workflow 基本都能在网络上找到，所以我们先来看如何使用。这里我选择了 [Menu Bar Search](https://github.com/BenziAhamed/Menu-Bar-Search) Workflow 作为示例。它的功能简单实用，就是在 Alfred 内输入 `m 搜索词` 搜索当前应用菜单栏中的菜单项，回车执行。实际的使用感受却是出人意料的方便，不必再用鼠标在菜单栏中层层穿梭，也省去了记忆很多快捷键的烦恼。尤其是，它会将用过的菜单项排在结果列表前面，可以直接回车运行，非常贴心方便。我常用来搜索执行 Ulysses 中粘贴 Markdown 格式文本、预览（Preview）中显示目录侧边栏，以及在浏览器中打开书签等。[点击这里下载](https://github.com/BenziAhamed/Menu-Bar-Search/raw/master/Menu%20Bar%20Search.alfredworkflow)

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/A653B1B9-6C55-41E9-944E-CABB7CD4521F.gif)

menu search 对比

### 导入安装

Workflow 下载后得到的是一个后缀名为 `alfredworkflow` 的文件，直接双击打开，Alfred 显示导入界面：

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/9DB717C3-7743-492C-9FCE-F2255A1337F5.jpg)

Workflow 导入界面

我们来具体看看，左侧上方是基本信息，由上到下依次为名称、简介、类别、作者、网站、版本号。其中的类别可以选择。下方的变量列表，用来做自定义配置，**相当于应用的偏好设置**。对想要设置的变量，可以双击变量名称左侧的空白区域，显示输入框而后填写。至于各变量的作用，可以看右侧的 workflow 详细说明。但并不是每个 Workflow 制作者都会填写或保持更新右侧的说明区域，所以应该**以 Workflow 的发布网页为准**。

此处，根据说明，我们知道这四个变量的含义：

* `-max-children`：单个菜单中菜单项数量显示上限，默认为 40。
* `-max-depth`：菜单层级深度上限，默认为 10。
* `-show-apple-menu`：是否显示  菜单，默认为不显示。
* `-show-disabled`：是否显示当前不可用的菜单项，默认为不显示。

实际上，大多数时候我们都可以直接略过变量配置，保持默认。

视线继续下移，界面最下方还有一行英文小字，意思是**Workflow 内的快捷键与快捷短语在导入时会被忽略**，也就是说需要用户自己主动设置后才能使用。大概是因为每个人在这两方面的配置习惯差异较大，并且容易因为重复而造成冲突。后面会说如何设置。

最后，点击右下角的「Import」导入即可。

### 配置与使用

导入后先别着急上手，可能还需要简单配置下。现在可以看到，Workflow 被添加到窗口左侧的列表中，右侧的编辑区则是用来配置修改列表中选择的 Workflow。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/8E3321F5-F4E9-4A93-8A01-5C46F0E7DFBE.png)

Workflow 导入后

是否配置以及如何配置因 Workflow 而异，依旧是**以发布网页为准**。如果 Workflow 功能非常简单以至于作者根本没有写任何说明，那么我们可以直接看编辑区。

如图所示，Workflow 由一个个 Object （官方用语，可以理解为**模块**或**组件**）组成，并通过之间的连线形成运行链路，确定运行顺序和数据流向。每个 Object **下方标有它的种类名称**，如图中我标记为 1 号的是个 `Hotkey`（快捷键） Object、2 号是个 Script Filter Object。对于 Menu Bar Search，如果使用快捷键（对应标号为 1 的 Object），就会按照 1→2→3 的顺序运行，如果使用关键词（标号为 2 的 Object），运行顺序则是 2→3。位于链路前端的 Object 就像个「启动装置」。后面的编写部分会有更深入的剖析。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/D43036E2-5ECC-4BDD-8F51-D147455FC02F.png)

Workflow 结构

**需要我们配置的正是这些启动装置**，主要包含关键词（最常见）、快捷键、快捷短语（最少见）三方面，分别对应于下面这些种类的 Object。关键词类比较特殊，多种 Object 都涉及到关键词的设置使用。设置过后，关键词、快捷键、快捷短语会显示在 Object 图标的上方，如下图中关键词 `ke`、快捷键 `⌃⌥⇧⌘D`、快捷短语 `ddate`。

* 关键词：Keyword 与 File Filter、List Filter、Dictionary Filter、Script Filter
* 快捷键：Hotkey
* 快捷短语：Snippet

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/B40C480E-3CF6-48C6-BB81-DCD03526B5F9.png)

Object 图标

前文中已经提到，快捷键与快捷短语需要用户配置后才能使用，关键词可以根据需要调整为自己习惯的字符。配置过程大同小异。双击标号 1 的快捷键 Object 就可以打开它的配置窗口，此时窗口内的快捷键设置项 Hotkey 已经自动选中，直接按下要设置的快捷键，然后点击右下角的「Save」保存，也可以用快捷键 `⌘Command-S`。设置的快捷键就会显示在 Object 图标上。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/B351B07A-7598-49EE-93F3-C92ADB2C009A.png)

Hotkey 配置窗口

关键词的修改，来看标号为 2、4 的 Script Filter Object，**图标上方显示的 `m`、`ms` 就是它们各自的关键词**。修改方法，与快捷键别无二致，打开配置窗口在 Keyword 文本框中修改就可以了。快捷短语也是修改配置窗口中的 Keyword 项。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/02389442-BF9A-4B2D-AF7C-4B4BA298F200.png)

修改关键词

另外，导入阶段看到的**环境变量**配置项，导入后仍然可以修改。点击编辑区右上角 `[]` 图标，弹出窗口的右侧就是变量列表，双击后填写，右下角「Save」保存。顺便提一句，之所以一个 Workflow 会使用环境变量，是因为这些用户可能需要自定义配置的数据，这样修改最方便。如果直接放在 Object 配置或者代码中，会给用户的使用造成不便和麻烦。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/7CEFB67A-675B-4E3F-B86F-3C7F8C6075E5.png)

变量修改窗口

如何使用一个具体的 Workflow 当然还是要查看它的发布网页。而对于没有说明的简单 Workflow，可以根据这些启动装置 Object 推测使用方法。就拿 Menu Bar Search 来说，它的功能是搜索菜单栏，从编辑区又可以看到有 `m`、`ms` 两个关键词，那么用法无非就是在 Alfred 中输入 `m 菜单项名称` 或 `ms 菜单项名称`，试试便知。存在快捷键、快捷短语 Object 的 Workflow，设置好后使用下也就知道效果了。

### 管理与更新

Alfred 在 Workflow 管理方面提供的功能不多，毕竟平时使用中我们面对的都是 Alfred 输入框，也就只有偶尔导入和调整配置时才会打开 Workflow 列表窗口。

**禁用与隐藏暂时不用的 Workflow**：在窗口右侧的 Workflow 列表中，右键菜单中的第一项 「Enabled」可以用来切换**启用 / 禁用**状态。去掉勾选「Enabled」即是禁用，之后这个 Workflow 就无法运行了，还会在列表中暗色显示。

建议禁用暂时用不到的 Workflow，这样可以减少 Alfred 结果列表中无用项，也能避免干扰其他 Workflow。此外，Workflow 列表上方的齿轮 ⚙️️ 图标菜单中，选择第三部分第一项「Only Show Enabled」可以隐藏列表中已禁用的 Workflow。我过去编写的一些 Workflow，现在用不到了但舍不得删除，就会禁用并隐藏起来。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/217F3BFF-6D44-4C43-A2CF-3AF7991388B6.png)

Workflow 列表右键菜单

**分类管理 Workflow**：前面我们知道了在导入时如何设置分类。导入后，还可以在 Workflow 列表中右键点击，在「Category」子菜单里选择分类。默认的分类有三种：Tools（工具）、Internet（网络）、Productivity（效率）。它们在我看来区别并不大，经常不知道该把一个 Workflow 归于哪一类。后来索性把几个默认的类别都删了，完全按照自己的需要分类，比如把自己编写的 Workflow 收为一类，把正在制作的分为一类。大家可以根据自己的情况灵活处置。

类别的删除与添加窗口，在齿轮图标菜单中点击「Edit Categories…」打开。如果需要一次为多个 Workflow 设置分类，只需要按住 `⇧Shift` 或 `⌘Command` 键点击选中多个 Workflow，然后同样是在右键菜单中设置。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/8E7F2360-D966-4E65-A2DF-EF68D15E2E96.jpg)

列表上方的齿轮图标菜单

齿轮图标菜单中，除了前面提到的「Only Show Enabled」隐藏已禁用、「Edit Categories…」编辑类别，还包括仅显示某个类别 Workflow、调整列表排序、设置是否显示 Workflow 作者之类的信息等功能选项。

最后是关于**更新 Workflow**。绝大部分的 Workflow 都没有提供检查更新的功能，所以需要我们**主动**到发布的网站上查看有没有更新，将更新的文件下载下来。双击文件打开的更新窗口界面，与导入界面基本一样，只不过左下角多了个「Migrate my settings（合并我的设置）」选项，勾选（默认）就是会保留我们设置的快捷键、关键词、变量等。如果去掉勾选这一项，就相当于全新安装 Workflow，所以一般直接点击右下角的「Update」更新就可以了。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/26AE8AE4-C4E7-41CB-A2E3-3766451C005A.png)

Workflow 更新窗口

### Workflow 推荐

优秀的 Workflow 成百上千，这里分享一些我自己经常使用的 workflow。

首先是系统功能增强类：

* [Recent Documents / Apps](https://github.com/mpco/AlfredWorkflow-Recent-Documents)：快捷获取各种最近打开的文档、文件夹、应用。最近几天处理的工作文档用它一键打开，刚刚关闭又需要的文件也可以在这里找到，不用再去文件夹中翻找。[介绍文章](https://sspai.com/post/47063)
* [Bluetooth manager](https://github.com/bmunoz89/alfred-wf-bluetooth-manager)：控制 macOS 系统蓝牙功能，打开 / 关闭、连接 / 断开。我用来连接 AirPods、音响等。
* [App Language Switcher](https://github.com/mpco/AlfredWorkflow-App-Language-Switcher)：让应用临时以指定语言启动，或者修改应用的默认语言。英文系统下，偶尔需要中文截图可以快捷切换，或者看看应用的某个功能在其他语言下是什么名称。
* [Menu Bar Search](https://github.com/BenziAhamed/Menu-Bar-Search)：搜索菜单栏回车执行，将菜单栏中的功能也纳入 Alfred 的工作流中。
* [Search Notes.app](https://github.com/sballin/alfred-search-notes-app)：搜索 macOS 内置应用 Notes 中的笔记和文件夹，快捷打开。显然比打开 Notes 然后再找到需要的笔记方便多了。

然后是一些与第三方应用协作的：

* [Spotify Mini Player](http://alfred-spotify-mini-player.com/)：全能型 Spotify 播放控制器，可以控制播放，搜索歌曲、歌单、歌手，编辑播放列表等等，功能全面。
* [Evernote Workflow](https://www.alfredforum.com/topic/840-evernote-workflow-9-beta-4-alfred-4/)：Evernote 笔记搜索、打开、创建等，不支持印象笔记。
* [Alfred Maestro](https://github.com/iansinnott/alfred-maestro)：搜索 Keyboard Maestro 中 macro，回车运行，`⌘Command-Enter` 编辑。算是一种额外的触发方式。
* [DEVONthink Search](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search)：搜索 DEVONthink 文档，根据搜索匹配度排序结果。
* [Calibre Search](https://github.com/mpco/AlfredWorkflow-Calibre-Search)：根据名称和标签搜索 Calibre 中书籍，快捷打开，查看评分、标签等。
* [Ariafred](https://github.com/Wildog/Ariafred)：Aria2 下载控制器，添加、浏览下载任务。

还有几个 GitHub 上的 Workflow 合集仓库，内容丰富，值得翻一翻：

现在多数持续更新的 Workflow 项目都存储在 GitHub 网站上，如果你不太熟悉如何使用 GitHub，尤其是如何下载上面的 workflow ，那么可以看这篇文章 [《搜索资源、跟踪更新、交流反馈…… 掌握这些技巧你也能找到 GitHub 上的好资源 - 少数派》](https://beta.sspai.com/post/54990)。另外，你还可以到 [Alfred 论坛](https://alfredforum.com/)、[第三方 Workflow 分享网站 Packal](http://www.packal.org/)以及 [GitHub](https://github.com/) 中按需搜索。

编写入门
----

各路高手制作的 Workflow 固然好用，但是自己时不时出现的各种需求不能总指望别人给解决，何况制作 Workflow 也是一种乐趣。这一节就带大家从最简单的 Workflow 编写开始学习，请放心内容不涉及代码编程 :)

下面的几节比较基础，依次介绍如何新建 Workflow、添加与连接 Object 等。有编写经验的读者，可以根据各小节的标题判断是否需要阅读。

### 新建 Workflow

点击 Workflow 列表下方的加号 ➕️ 图标，选择「Blank Workflow（空白 Workflow）」以打开新建窗口。这里需要填写一些基本信息，如 Name（名称）、Description（简介）、Category（类别）、Bundle ID、Created By（作者）、Website（网站）以及图标等，请按照上图填写。其中，只有 Name 必须填写，其他可选。我们接下来重点看下 Bundle ID 和图标。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/5D9056C2-98BD-4C89-9D7B-DCCD7B779FA9.png)

Workflow 新建窗口

**Bundle ID** 可以理解为 Workflow 的身份证编号，用来辨识和区分。没有 ID 不影响使用，但是在更新 Workflow 时，Alfred 就不知道下载的新版本对应于哪个已经安装的 Workflow。Bundle ID 的格式一般为 `com.作者名字.Workflow名称`，分为由点分隔的三部分。第二部分也可以是作者的网络 ID。如果作者有个人网站，那么前两部分通常是网站域名的逆序写法，如个人网站 `example.net` 写为 `net.example`。前文介绍的 Menu Bar Search 的 ID 是 `com.folded-paper.menu-bar-search`，`com.folded-paper` 对应作者的个人网站 `folded-paper.com`。

**图标** 的设置很有必要，合适好看的图标不仅可以提高辨识度，在 Alfred 结果列表中一眼认出，而且也赏心悦目。图标有这么两种：

* 图片文件，直接拖拽到图标框中就设置好了。我们可以在网络上找到各种图标图片，比如编写了一个文件操作类的 Workflow，可以在图片搜索引擎中用关键词 `文件 图标` 搜索。
* 应用图标，比如这一节我准备编写个文件相关的 workflow，那么可以用 Finder 的图标，在 Alfred 中搜索 Finder App 拖拽到图标框中就行了。现在尝试下吧。

需要删除图标时，点击选择图标框，按下 `Backspace（退格键）`即可。

填写完毕后，点击右下角的「Create」或者使用快捷键 `⌘Command-S`，我们就得到了一个新 Workflow。之后需要修改这些信息时，可以在 Workflow 列表中双击，或者右键单击后选择「Edit Details」。

### 开始编写

编辑区中右键点击，菜单前五项分别是 Triggers（触发）、Inputs（输入）、Actions（动作）、Utilities（工具）、Outputs（输出）等 Object 类别。添加 Object 就在这里，点击任意一项就会放置在光标位置，并自动弹出配置窗口。填写完毕后同样是点击「Save」或使用快捷键 `⌘Command-S` 保存。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/03B973A2-0E82-433B-B5A8-423779046B1B.png)

Object 类别

不同的 Object，配置项当然也不一样，但配置窗口也有几个通用一致的地方。下方左侧的**问号图标**，点击可以打开 Alfred 官网中关于当前 Object 的帮助文档，还附有必要的图示和 workflow 示例。有啥不懂就看文档，一定没错。

窗口右下方「Cancel」按钮旁边的**白色方形图标**，用来打开当前 Workflow 的资源文件夹，里面存有配置文件 `info.plist`、图标文件、脚本文件等。一般在需要编辑处理这些文件时会用到。另外，我们下载到的 `alfredworkflow` 文件，其实就是这种文件夹的压缩包。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/17CD1B7F-F158-4153-81DC-7B8B972BF248.png)

Object 配置窗口

接下来，回归正题。

首先，选择右键菜单中「Trigger - Hotkey」，添加一个用来设置快捷键的 Object。配置窗口中，点击选中 Hotkey 配置框，按下想要设置的快捷键，比如 `⌃Control-⇧Shift-⌥Option-⌘Command-K`。这里出于临时演示需要，设置一个复杂的快捷键，避免和已有的快捷键发生冲突，你也可以设置为其他的。窗口的其他配置项暂时不用管，直接保存。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/A6600CCD-C3F1-4426-B381-282C1B8F2CB3.png)

Hotkey 配置窗口

然后，选择「Input - Keyword」添加一个关键词 Object，按照下面这样设置后保存：

* Keyword 关键词，设为 `aa`，没什么特殊含义，顺手而已。一般使用英文字母，毕竟中文输入需要按下更多次按键。
* Argument 参数，也就是之前所说的「搜索词」，设为「No Argument」不需要搜索词，这样在 Alfred 中输入关键词 `aa` 后可以直接回车运行。
* Title 标题，设为 `打开文件`。标题只是用来显示在 Alfred 结果列表中作为标识，不影响功能与使用。
* Subtext 副标题，也就是结果列表中标题下方的一行小字，补充额外的信息，设为 `学习 Workflow 中`。
* 图标，是否设置都可以。**如果不设置就直接继承 Workflow 的图标**。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/7E1F554B-7304-428B-9789-1D5E29138E6B.jpg)

Keyword 配置窗口

然后，选择「Actions - Open File」添加一个用来打开文件的 Object。不做设置的默认情况下，它会打开前一个 Object 传来的文件。我们现在先设置个固定的文件用来打开，随便拖拽一个文件到左侧的框中就可以了。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/C5E8015A-EAF7-4763-9A40-47BFF73F2752.jpg)

Open File 配置窗口

最后，需要在 Object 之间建立连接。如图所示，光标移动到一个 Object 的尾部，拖拽突出的尾巴，到后一个 Object 前面突出的脑袋上。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/739DFD68-DC27-4C66-A503-49C4A87EAC21.gif)

Object 建立链接

这样，我们的第一个 Workflow 就做好了。使用快捷键`⌃Control-⇧Shift-⌥Option-⌘Command-K` 或者在 Alfred 中输入关键词 `aa` 选择「打开文件」后回车，就可以打开前面设置的那个文件。

这一节，我们知道了如何添加、配置与连接 Object。但做的 Workflow 确实太简单了，只是用来打开固定的文件，没什么用。不过这只是第一步，让我们继续，把它升级为一个实用的 Workflow。

### 继续完善

我们来把上面的 Workflow 改造下，让它具备这样的功能：用快捷键或关键词运行 Workflow 后，在**固定**的文件夹及其子文件夹中搜索并打开文件。它用来搜索我们高频使用的文件夹相当好用，比如「下载」、「桌面」、素材文件夹等。在工作时，不必打开 Finder 层层寻找，也不必用 Alfred 默认的文件搜索功能大海捞针。搜索范围限定为若干个文件夹减少了干扰项，让搜索更加精准。

首先，添加一个「Input - File Filter」，这是个可以在指定文件夹中搜索指定类型文件的 Object，自然也是本 Workflow 的核心。配置窗口按照下面这样依次设置后保存：

* Keyword 关键词，依旧设为 `aa`，与之前的关键词一致。
* with Space，关键词与搜索词之间是否需要空格。这一项对于实际使用基本没有影响，保持默认即可。你也可以分别试试。
* Placeholder Title，占位符标题，设为`打开文件`。和之前设置的标题没什么区别，之所以称为「占位符」标题，是为了强调这是在 File Filter 列出搜索结果前展示的临时标题。
* Placeholder Subtext，占位符副标题，不如设为`这是 File Filter 的副标题`。
* File types，文件类型列表，比如分别拖拽一个 JPG 和 PNG 图片文件到这里，那么这个 Workflow 就只能搜索这两种文件了。需要删除时可以点击选中后按下 `Backspace（退格键）`。为了让编写的 Workflow 能够搜索所有文件类型，这里暂且不设置。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/009490DC-29FB-4760-85CF-A695C4830C1B.jpg)

File Filter 配置窗口

接着，点击窗口上方的「Scope」，这个面板用于设置文件搜索范围。设置的方法，除了拖拽文件夹到列表中，也可以点击右下角的加号➕ 按钮，手动输入文件夹路径。这里，我是将「下载」文件夹拖入其中，你也可以设置为自己高频使用的其他文件夹。记得保存。

现在唤出 Alfred 输入框，输入 `aa` 会发现有两个「打开文件」，分别对应于前后设置的 Keyword 和 File Filter 两个 Object。显然，File Filter 内含 Keyword 功能，不需要 Keyword Object 了。应该将重复的 Keyword Object 删除，点击选中后按下 `Backspace（退格键）` 键就可以了。同时可以看到，与之相连的两条连线也没有了。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/96BCFAEA-D9D4-4702-B351-7F6ECDBE1E2C.jpg)

Keyword 功能重复

然后，分别连接 Hotkey 到 File Filter，File Filter 到 Open File。这个 Workflow 算是初步完成，可以按下设置的快捷键，输入任意文字，搜索「下载」文件夹中的文件，回车打开。也可以在 Alfred 中输入 `aa 搜索词` 搜索。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/210AAD9B-CFF0-4E41-9311-189DF9771190.jpg)

在 Alfred 中输入关键词进行搜索

但是，好像列出的文件并没有按照什么顺序排列。对于「下载」文件夹，我们经常需要刚刚下载的那个文件，那么怎么让这个 Workflow 在敲下两个空格后将最新的文件放在最前呢呢？双击 File Filter 打开配置窗口，选择「Limit and Sort」面板，可以看到第三个设置项「Sort by」，用来控制结果排序。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/E99FD3DB-EF7A-4B12-ADEA-F6CCB7269869.jpg)

File Filter 的 Sort by 配置

「Sort by」的默认设置是「Alfred’s Knowledge」，意思是根据 Alfred 已知的信息智能排序，将你可能需要的文件放在最前。然而，「智能」很多时候不够智能，猜不透用户的心思。除了默认项，还有「Creation Date（按照创建日期排序）」与「Last Modified Date（按照修改日期排序）」，我认为设置为后者比较合适。举个例子，依次创建 A、B、C 三个文件，而后修改了 B，如果选择「Creation Date」，那么结果列表中的顺序会是 C、B、A。而选择「Last Modified Date」会是 B、C、A。你可以分别试试，选择自己更习惯的。如此配置后，再运行这个 Workflow 并敲下两个空格，就会在结果列表中首先显示最新的文件，省去了很多时候手动选择的步骤。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/2D10C4DF-ACB3-4515-A7A5-9F2B77F654FC.jpg)

在 Alfred 中显示最新的文件

### 分支的使用

这一节，我们来学习分支的使用。分支可以用来同时执行多个操作，比如同时使用多个搜索引擎进行搜索；也可以给用户提供多个功能选项，就像我们使用 Alfred 搜索应用时，按下回车是运行，按下 `⌘Command-回车` 打开所在文件夹，按下 `⌥Option-回车` 在 Finder 中搜索。下面的例子就属于后一种。

继续改进上面的 Workflow，选择「Action - Reveal in Finder」添加一个用来在 Finder 中显示文件的 Object，并从「File Filter」连接到它。然后，我们再试试利用这个 Workflow 搜索文件，回车就不仅仅是打开文件，还会同时打开所在文件夹。也就是说，File Filter 之后的两条分支同时运行了。这显示是分支的第一种用法，但不适合这里。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/A4F272FA-EF06-41C1-8A0C-43E8FA7B6042.jpg)

连线配置

双击 File Filter 与 Reveal in Finder 之间的连线，同样会弹出一个配置窗口，用来调整这条连线的行为。其中，第一项「Action Modifier」动作修饰键，比如勾选「Command」后保存，那么就只有按下`⌘Command-回车`才能通过这条连线，后面的 Object 才会运行，也就是打开所在的文件夹。

第二项「Modifier subtext」是修饰键按下时显示的副标题，用来提示不同按键的作用。这里填写为「打开所在文件夹」，之后使用时按下 `⌘Command` 键就能看到，不松开 `⌘Command` 直接再按下 `回车` 键就可以打开文件夹。

第三项「Window Behaviour」的应用场景比较特殊，暂且不表。总之，第一项勾选「Command」，第二项填入「打开所在文件夹」，然后保存。需要注意的是，**附有圆点的连线才能编辑**。

至此，一个实用的 Workflow 就做好了，再来试试吧。选择结果列表中某个文件后，按下 `回车` 是打开，按下 `⌘Command` 会看到副标题变成了「打开所在文件夹」，按下`⌘Command-回车`则是打开所在文件夹。你可以尝试添加更多的分支，也可以在 File Filter 中「File types」拖入文件以设置搜索的文件类型，「Scope」搜索范围中加入多个常用的文件夹。而且，我们也可以使用`右方向键`打开 Alfred 内置的 Action 列表。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/6C3ED721-50CE-42CB-8E90-85740BB15ACF.gif)

打开文件

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/80451DB1-539C-4C5D-AB86-C046DD23674B.gif)

打开文件夹

### 分享自己的 Workflow

将自己编写的 Workflow 分享给朋友或发布到网络上，想来也是非常不错的。点击编辑区右上角四个图标中的右侧第二个导出图标，或者在 Workflow 列表中右键点击并选择「Export…」可以打开导出窗口。这里用来检查和补充名称、版本号、变量、介绍等各种信息，让使用者更好地上手，避免一头雾水，也能在一定程度上保护版权。此处对信息的修改，在点击右下角的「Export」导出时也会保存在我们自己的 Workflow 中，而不只是存在导出的文件内。填写完毕后，导出保存就可以得到 Alfred Workflow 文件。发送给朋友后如何导入使用，前文已经详细介绍过了。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/FFC78621-2A18-4D2F-B712-2EF6940C5AC8.png)

导出 Workflow

### 辅助编写设施

最后补充介绍下 Alfred 为编写 Workflow 提供的一些辅助设施。 Workflow 列表下方的加号➕️ 图标菜单中，之前只是使用最后一项「Blank Workflow」新建 Workflow，我们来看剩下的几个。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/87EB6056-6E9F-458F-B5C5-1E6E4D69FDD4.png)

第一项「Workflow Defaults」，顾名思义就是用来设置 Workflow 默认信息的，毕竟作者之类的每次都一样。设置后再新建 Workflow 时会自动填入这些默认信息。弹出窗口中有四项，分别是 Bundle ID、Created By（作者）、Website（网站）、Readme（使用说明）。其中，Bundle ID，这里填写的是 `com.作者名字.` 部分，等到新建 Workflow 时补上后面的 Workflow 名称。填写并保存后，新建个 Workflow 试试看。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/3EB48E63-8600-4DB8-9DD3-361DEDA26C63.jpg)

Workflow 默认设置

第二项「Getting Started」新手入门，以 Workflow 示例加注释的形式讲解关键词、快捷键、剪贴板、变量等主题，按照从易到难的顺序排列。比如，列表第一项是关于最常用的 Keywords，介绍如何添加和使用关键词，点击后导入一个 Workflow 并弹出一段说明文字，点击「Continue」后可以看到 Workflow 内容。这些导入的 Workflow 可以运行观察实际效果，其中的 Object 也大都注有关于使用和配置的说明文字，还可以双击 Object 查看学习配置。注释文字的编辑窗口，可以通过 Object 右键菜单中选择「Edit Note」打开。如果你的英文尚可，那么这里是学习编写 Workflow 的好地方，建议把这个列表过一遍。英文阅读吃力的话，也可以借助各种翻译工具。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/59AF9505-D291-461C-88B4-4C6A3B31DA6A.png)

Workflow 入门

第三项「Examples」含有 6 个实用的 Workflow 示例。其中，「Should I watch this movie」 用来一键搜索三个网站查看观影建议；「Simple Folder Search」与「Dynamic File Search」 分别能够仅搜索文件夹、在任意的指定文件夹内搜索文件；「Simple To-do List」 实现简单的待办事项清单功能；「Google Suggest」 与 「Amazon Suggest」在输入时提供搜索建议。这些 Workflow 都可以直接使用、修改、学习原理。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/ACBB97B6-4976-4844-AE7D-4F53415BA7E5.jpg)

Examples

第四项「Templates」包含分为七类的数十个 Workflow 模板。模版的命名很直白，例如其中的「Templates - Essentials - Keyword to Script to Notification」，看着名字就知道是用关键词触发运行脚本并发送通知消息。点击后，不再是导入 Workflow，而是弹出新建窗口。修改名称、Bundle ID 等信息并保存后，可以看到已经添加 Object 并做好连接。我们需要做的是，在其基础上调整修改配置。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/8AF8663A-A33B-4F04-87D1-E8CBC10872F2.jpg)

Alfred Templates

编写进阶
----

前面，我们学习了 Workflow 新建、编写、导出等整个流程。现在，是时候深入核心看一看了，这也是制作复杂强大 Workflow 的前提。那么什么是核心呢？在我看来就是**数据的流通过程**。 数据之于 Workflow，就如同材料之于流水线。只有弄明白数据在 Workflow 中怎么被一个个 Object 传递、使用、修改，才能理解 Workflow 的运转机制，编写时得心应手。

这一节，我们以「Examples - Simple To-Do List」一个简单的待办事项列表 Workflow 为对象，逐步理清在功能运转之下的「数据暗流」。考虑到部分读者可能对英文阅读比较头疼，这里提供一个[翻译后的版本](https://github.com/mpco/Alfred-Workflow-Tutorial/raw/master/Simple%20To-Do%20List%EF%BC%88%E7%BF%BB%E8%AF%91%E7%89%88%EF%BC%89.alfredworkflow)，下文也以此版本为基础进行讲解。在看文章的同时，点开 Object 查看配置细节可以更好地理解文章。导入时，注意有个 `path` 变量，后文中会涉及到。

首先，在导入 Simple To-Do List 后试用体验下它的功能。在 Alfred 中输入 `todo 买杯咖啡` 并回车，接着 Alfred 会显示三项结果：家庭、工作、稍后，这是三个待办列表的名称，选择「家庭」后回车就会将「买杯咖啡」添加到其中。此时，注意屏幕右上角，会出现一个通知「已将事情添加至 home」。以上是添加事情的功能部分。再次唤出 Alfred 输入框，敲下 `vtodo`，立即显示上面的三个列表名称，输入文字筛选或者用方向键进行选择，回车会打开相应的存储文件，用来查看已经添加的事情。当然，如果还没有添加过，那也就没有相应的存储文件供打开了。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/140BD601-0C40-498B-8B46-31D93196E7ED.jpg)

Simple To-do List 使用流程

功能体验过后，我们来分析下这个 Workflow 是如何实现的。这里需要先引入两个知识点：

**知识点 1 - 输入与输出**：每个 Object 都会接收前面 Object 传递的数据作为`输入`，并向后面的 Object 发送 `输出数据`。输入与输出的数据，在 Workflow 中被称为 `Argument（参数）`。在 Object 内部的配置窗口中用 `{query}` 指代所接收的输入数据。如果你在 Alfred 中添加过搜索引擎，那么应该对 `{query}` 并不陌生。

**知识点 2 - 变量**：Workflow 中，除了输入与输出，还可以使用**变量**存储、传递数据。与输入输出不同之处在于，变量在 Object 中被创建后，连线上后面的每个 Object 都可以读取、修改它。而输入输出仅仅是两个 Object 之间的数据传递。变量用 `{var:变量名称}` 指代它的值。

另外，**环境变量**比较特殊，它是在 Workflow 配置中创建的，每个 Object 都可以读取。一般用于存储 Workflow 的偏好设置类数据，就像 Simple To-Do List 中的 `path` 用来让用户方便地设置待办事项列表文件的存储位置。毕竟如果用户需要扒开 Object 配置窗口或者代码文件去修改的话，就太不友好了。

做个比喻帮助大家理解。假设 ABCD 四个人（对应于四个 Object）在按顺序排队，A 向后面的 B 说了一句「你好」，那么「你好」对于 A 来说就是**输出数据**，对于 B 来说就是**输入数据**，仅限于两者之间，后面的 CD 两人不知道。**变量**则像是，B 向后面传了一张纸条，标题「AH」内容为「地震高冈，一脉溪水千古秀」，后面的每个人都可以看到、修改、甚至销毁。另外，墙上贴着一张纸，标题「注意」内容为「保持安静」，这就属于**环境变量**，这个空间（对应于 Workflow）里的每个人都可以看到。现在应该明白了吧。

接下来，我会详细分析下 Simple To-Do List 的原理及其数据流通过程，每一步都会专门注明输入输出、变量等数据。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/9EB9E7FC-7076-4C64-A37A-6746620562EA.jpg)

Simple To-do List

**知识点 1：Keyword Object**

这种 Object 我们已经比较熟悉了。打开配置窗口，注意右上角的配置项「Argument Required」，用来设置是否需要 Argument（为了避免这种陌生术语，之前将其称为「搜索词」），可以选择「Argument Required（必须有）」、「Argument Optional（有无都行）」以及「No Argument（不能有）」。此处设置为「Argument Required」，所以在关键词 `todo` 之后需要继续输入文字（如「买杯咖啡」）才能回车运行。你可以试试只输入 todo，选择「添加事项」后回车，是不是无法进入下一步。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/25FF4D41-B350-44B9-A0CB-79985C5FAB2A.jpg)

Keyword 配置窗口

另外，配置窗口中可以看到 Title 被设置为`添加事项：{query}`。根据知识点 1，`{query}` 被用来指代接收的输入数据 Argument，此处就是 `买杯咖啡`。所以在 Alfred 中输入 `todo 买杯咖啡`时，标题显示为 `添加事项：买杯咖啡`。

Keyword Object 会在按下回车时，将输入数据直接发送给下一步。

* 输入：买杯咖啡
* 输出：买杯咖啡
* 变量：`path`（值：`~/Documents/Alfred/todos/`）

**知识点 2：Arg and Vars Object**

一个之前未见过的新 Object，属于 Utilities 类别，用来配置 Argument 和 Variables（变量）。它的配置窗口分为上下两项。上方的 Argument 用来设置发给下个 Object 的输出数据，此处为空，也就是没有输出。下方的 Variables 是用来创建、修改变量，这里将接收的输入 `{query}` （也就是 `买杯咖啡`）填入 `task` 变量中。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/B068ED80-CA69-4361-AAC3-45CDF485482D.jpg)

Arg and Vars 配置窗口

* 输入：买杯咖啡
* 输出：无
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）

**知识点 3：List Filter object**

新 Object，属于 Inputs 类别，功能是让用户在预先设置的列表中选择一个。配置窗口中，可以看到它也能够设置 Keyword，实际上 Inputs 类别的 Object 都可以。窗口上方的常规设置项就不说了。下方左侧列表中，是预先填入的三项数据：家庭、工作、稍后。点击其中的「家庭」，窗口右侧显示出对应的数据：Title（标题）、Subtitle（副标题）、Arg（Argument 缩写）。当用户选择列表中的某项时，List Filter 会输出对应的 Arg 数据。比如选择「家庭」，则输出「home」。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/25513405-19CA-46FA-8629-DF181E2D1C90.jpg)

List Filter 运行结果与配置窗口

* 输入：无
* 输出：home（假设我们在使用时选择了「家庭」）
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）

这里还有个有意思的细节，为什么上一个 Object **故意**将 Argument 设置为空，也就是不输出数据到这一步的 Object 呢？我们可以打开上一个 Arg and Vars Object 的配置窗口，在 Argument 中填入 `{query}` （这是未修改 Arg and Vars 时的默认值）并保存。然后唤出 Alfred，输入 `todo 买杯咖啡` 后回车，奇怪的事情发生了：Alfred 输入框中显示着「买杯咖啡」，而原本应该出现的三个结果（家庭、工作、稍后）却没有了。按退格键删除「买杯咖啡」，三个结果就又出现了。

为什么会这样呢？因为 Arg and Vars Object 的 Argument 配置项是用来设置输出到下一步的数据，其中填入的 `{query}`，代表接收自第一步 Keyword object 的输入数据 `买杯咖啡`。所以就将接收自第一步的 `买杯咖啡`原封不动地输出到了第三步 List Filter Object。而 List Filter Object 会将接收的输入数据显示在 Alfred 输入框中。也就干扰了「家庭、工作、稍后」的显示和选择，所以需要在 Arg and Vars Object 中将 Argument 设为空。

实际上，Inputs 类别的 Object 都会像 List Filter 一样，将前一个 Object 发来的输入数据显示在 Alfred 输入框中。

**知识点 4：Arg and Vars Object**

配置窗口中，Argument 保持默认值 `{query}` ，将接收的输入数据直接原样输出。Variables 列表中创建了新变量 `filename`，并为其赋值 `{query}`。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/9B4BCF5D-6270-4D92-81A2-71A384923DAE.jpg)

Arg and Vars 配置窗口

* 输入：home
* 输出：home
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）、`filename`（值：`home`）

**知识点 5：Conditional Object**

一个根据条件选择后面分支的 Object，属于 Utilities 类别。这里设置的条件是：如果 `task` 变量的值不等于空白，就执行`追加`分支，否则执行`打开文件`分支。打开配置窗口，If 后紧跟着三个输入框。第一个填写的 `{var:task}` 指代 `task` 变量。第二个「is not equal to（不等于）」是设置第一、三项之间的关系，可以选择等于、不等于、 大于、小于、正则匹配等五种。第三个未填写，空白。之后的 「ignoring case」指在条件判断中是否忽略大小写。最左侧的 `追加`、 `打开文件` 用来标记不同的分支以方便连线，非必需。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/56A9BE7E-47FC-4ACF-9F5F-B5EEAE262333.jpg)

Conditional 配置窗口

我们来分析下 `task` 变量的情况。当使用 `todo` 关键词添加事情时，运行到第二个 Object，事情被填入 `task` 变量中。然后运行到条件判断这一步，`task` 变量不等于空白，所以执行后面`追加`分支。而当使用 `vtodo` 关键词选择打开某个待办事项列表文件时，由于跳过了前两个 object，没有建立 `task` 变量，也就不符合「task 变量不等于空白」条件，所以执行 `打开文件` 分支。以上正好符合之前我们使用这个 Workflow 时的情况。

* 输入：home
* 输出：home（Conditional object 直接将输入数据向后传递）
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）、`filename`（值：`home`）

**知识点 6：Write Text File Object**

用来写入文本文件，属于 Outputs 类别。配置窗口中，第一行的 Filename 用来设置文本文件的路径，此处是 `{var:path}/{var:filename}.txt`，含有两个变量。环境变量 `path` 的值是 `~/Documents/Alfred/todos/`。`filename` 在第四步被创建，假如之前选择了「家庭」列表，那么此处的值就是 `home`。所以文件路径就是 `~/Documents/Alfred/todos/home.txt`。接着，看第一行的右侧 `if exists`，意思是如果文件已经存在怎么办，可以选择三种处理方式：「Skip」跳过，「Overwrite」覆盖、「Append」追加。再看下方的大文本框，是向文件中写入的内容 `- {var:task}`，相信你已经明白，就是 `- 买杯咖啡`。

总结下，这一步的作用是将待办事项 `- 买杯咖啡` 添加到 `~/Documents/Alfred/todos/{var:filename}.txt` 文件中。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/3B078C4E-EDD2-4C34-AC59-760689178786.jpg)

Write Text File 配置窗口

* 输入：home
* 输出：`~/Documents/Alfred/todos/home.txt`（Write Text File Object 默认输出文件路径）
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）、`filename`（值：`home`）

**知识点 7：Post Notification Object**

发出通知消息，属于 Outputs 类别。配置很简单，不用再说明了。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/D07DCB35-521A-46A3-80F1-DDFF7F449477.jpg)

Post Notification 运行结果与配置窗口

* 输入：`~/Documents/Alfred/todos/home.txt`
* 输出：`~/Documents/Alfred/todos/home.txt`（Post Notification Object 直接将输入数据向后传递）
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）、`filename`（值：`home`）

**知识点 8：Open File Object**

打开文件，属于 Actions 类别。配置中只有个路径信息 `{var:path}/{var:filename}.txt`，也很简单。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/A891A1EF-F98C-48E8-BFDA-5AECC14540FF.jpg)

Open File 配置窗口

* 输入：home
* 输出：`~/Documents/Alfred/todos/home.txt`（Open File Object 输出文件路径）
* 变量：`path`（值：`~/Documents/Alfred/todos/`） 、`task`（值：`买杯咖啡`）、`filename`（值：`home`）

至此，Simple To-Do List 就解析完毕了，Workflow 中数据的传输原理也借此学习了一遍。

### 用调试模式看数据

读到这里，或许你会有些疑问：怎么知道一个 Object 的输入输出与变量数据呢？毕竟只有这样，我们才能准确地配置 Object，让编写的 Workflow 按照预期运行。这一节就告诉大家怎么做。

点击编辑区右上角的蜘蛛图标，或者使用快捷键 `⌘Command-D` ，调试模式区域就会出现在编辑区下方。我们再次使用 `todo 买杯咖啡` 运行 Workflow，添加至「家庭」列表中。注意调试区域，随着 Workflow 的运行会生成一系列信息。

第一行「Logging Started…」表明记录开始，其余行的构成是这样的：时间、Workflow 名称、Object 名称、信息内容。而且，每个 Object 会生成两行信息，其中第一行「Processing complete」表明该 Object 运行完成，第二行「Passing output ‘XXX’ to YYY」是说明输出信息 XXX 到 YYY Object。另外，这里的 Object 名称都被蓝色高亮显示，试着点击下，会发现编辑区中对应的 Object 被选中并凸显出来。如此一来，就可以直接找到一行调试信息对应的 Object。在查找问题，尤其是 Object 比较多时非常方便。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/25313014-5949-4792-9E19-E0B920966BCF.jpg)

调试区域上方还有一行选项和按钮，用来控制调试信息显示范围，方便聚焦。左侧第一项「Sow All information」配置显示的信息内容，可以选择「All information（所有信息）」、「Interesting information（有趣信息）」，**所谓的「有趣信息」就是异常的、出错的、需要我们注意的信息**。第二项「for this Workflow」，用来选择「this Workflow」只显示当前 Workflow 的调试信息或「all Workflows」显示所有 Workflow 的信息。你可以选择「all Workflows」然后运行其他 Workflow 试试。第三项「Only selected object (s)」很简单，勾选就只显示在编辑区内选中 Object 的调试信息。右侧还有两个按钮，分别是「Copy」一键复制所有调试信息，「Clear」清空。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/6C34CD68-6A77-4726-85E2-621BD34D372A.jpg)

Debug 选项

然而，有没有发现我们目前得到的调试信息，只有输入输出数据（前一个的输出就是后一个的输入），变量数据从哪儿能找到呢？这就需要用到「Utilities - Debug」这个 Object 了。在编辑区中添加一个「Utilities - Debug」，配置窗口中默认填写着 `'{query}', {allvars}` 也就是接收的输入数据和所有变量，不用修改直接保存。然后将需要获取输出和变量数据的 Object 连接到「Debug」，可以像图中那样将第三个 Object「List Filter」与第四个「Arg and Vars」都连接至「Debug」。现在，再次输入 `todo 买杯咖啡` 运行 Workflow，添加至「家庭」列表中，看看调试信息有什么不同。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/D2591197-275C-4FA0-94F4-817C3832C8B2.jpg)

添加、连接 Debug

我们会发现，相比之前多了两行「Debug」的信息，分别对应与之相连的两个 Object。以对应「List Filter」的前一行为例，信息内容部分中 `home` 是「List Filter」的输出数据，其后花括号内是「List Filter」向后传递的变量数据。如果嫌调试信息比较杂乱，可以试试选择「Show Interesting information」或者在编辑区中选中 Debug 后勾选「Only selected object (s)」，两者在当前效果是一样的。

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/AE3D64D9-7ACE-4E9E-9611-3DBE60AEE1A8.jpg)

添加 Debug Object 后的调试信息

![](.evernote-content/2F0EFF74-58F6-494A-AECD-B4AE2FFAF1B6/B132FE4D-8278-47DC-915E-2E0A13A98027.jpg)

精简后的调试信息

结语
--

现在，你可以缓口气了。我们从新建 Workflow 说起，一路上历经添加与配置 Object、使用分支扩展功能、导出分享自己的作品，到最后的挖掘 Workflow 数据流通原理、查看调试信息，信息量确实有点大。Workflow 编写的绝大部分原理与知识，都已经在这里了。

不过，还有一点点关键的高阶内容，主要是涉及「Inputs - Script Filter」和「Utilities - JSON Config」两个 Object。前者在我们安装的很多 Workflow 中都可以看到，是构建强大 Workflow 的核心。后者则是用来动态配置各种 Object，比如在运行 Workflow 时现场指定「File Filter」的搜索范围，各位可以在「Examples - Dynamic File Search」这个示例中体验到。由于这部分内容涉及代码与编程，有一定的学习门槛，所以放到正在筹备的 Alfred 教程中。

这篇文章涉及的概念、术语、配置细节比较多。在电脑前一边阅读，一边实际操作才能更好理解。如果有什么不明白的地方，欢迎留言反馈。

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57648)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ee4fbe4d-cc12-4146-b04e-1f021d98eeb0/ee4fbe4d-cc12-4146-b04e-1f021d98eeb0/)
