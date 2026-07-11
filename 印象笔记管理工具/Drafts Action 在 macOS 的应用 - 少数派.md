# Drafts Action 在 macOS 的应用 - 少数派

---

Drafts Action 在 macOS 的应用
=========================

[Drafts](https://sspai.com/post/44113) 是 Power+ 文章里的常客，也是我们奏折里的重点关注对象。它的定位是笔记应用，追求的是快速记录，然后再考虑进一步的处理。所以存在 Drafts 里的笔记，往往都是随手记下的未经打磨的草稿，它们有的会成为日后的文章素材，有的会变成社交网络上的一段话，有的会发送到日历和任务管理等软件里。

Drafts for iOS 长期以来的卖点之一 1，是它的 Action 功能，这是 Drafts 的自动化模块，可以帮助我们缩减处理草稿的流程。最简单的，比如将笔记发送到 Evernote 的摘抄笔记本里，并且附加到文末，减少中间的复制、查找、翻页、粘贴等操作；Action 也可以像快捷指令那样，将多步动作串联到一起形成工作流，比如摘抄保存到 Evernote 之后，还能继续作为文本发送到社交网络里。

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/9F06BDA1-1CE3-42C9-9BCC-7223641F49ED.png)

Drafts 的 Action 功能

在即将发布的 Drafts 16 中，Action 功能终于被移植到了 Drafts for macOS：

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/9FE19ED5-D01A-4F0C-A6A4-4C7C6E6F9A15.jpg)

Drafts for macOS 的 Action 功能

Drafts 刚传出准备开发 macOS 版时，我是持怀疑态度的，因为我难以想象 Drafts 要如何迁移 Action。它里面很复杂，有系统服务，有第三方服务，有 URL Schemes，有 JavaScript，还能互相嵌套；我也很怀疑 Action 对于 macOS 的意义，因为 macOS 上已经有很多自动化工具了，似乎不缺 Drafts 这一块。PhilGu 在《[Drafts for Mac 测评：草稿处理的无缝衔接](https://sspai.com/post/53761)》这篇文章里也表达过类似的担忧。

但是我错了，Drafts 16 for macOS 的 Action 功能是一次很完整的搬运，而且在自动化工具云集的 macOS 平台，Drafts Action 也有它存在的意义。

注：Drafts 16 for macOS 正在公测中，如果你是 Drafts 订阅用户，可以通过[官网](https://docs.getdrafts.com/beta/)下载 Beta 版本。

近乎完整的 Action 移植
---------------

这次的 Action 移植很完整，不论是从位置上，还是从功能上。

位置上，Drafts Action 的展示与 iOS 版逻辑一致，Action 会分组显示在右边侧边栏上，自定义按键则显示在草稿的底部（对应 iOS 的键盘上方）：

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/F5D18BC7-3D01-4141-BA46-8B46281B04C1.jpg)

侧边栏和自定义按键

功能上它和 iOS 版实现的别无二致，可以新建、修改、删除 Action，并且会在两个平台互相同步。macOS 版也提供了更灵活的编辑方式，有了单独的 Action 管理器，可以分窗口分标签显示，方便对比和批量移动 Action：

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/30C25CF4-3D79-47EA-BFB9-01D7BE210786.jpg)

macOS 版的 Action 编辑页面

过去 Action 能做的它几乎都可以做，包括系统服务（比如处理剪贴板、发送邮件短信、添加日历任务等）、第三方服务（比如 Twitter、Todoist、Dropbox 等）、插入自定义本文（比如插入 Markdown 语法、插入常用模板）、URL Schemes 功能（比如发送到 Ulysses）、JavaScript 功能（比如编码解码文字）。

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/6F1C012A-A003-4282-81EC-F6F0039074CC.jpg)

Drafts Action for macOS 支持的服务

但之所以说「近乎完整」，是因为目前还有两项功能没有被实现：

1. **第三方服务不支持 Evernote ：**这是 Evernote 的锅，因为 Evernote 没有提供标准的跨平台 API，而是在不同平台上使用单独的 SDK2 。Evernote 的 iOS 版有一套 SDK，是 Drafts 正在使用的；而 Mac 上的 Evernote SDK 则年久失修，已经无法使用。
2. **邮件动作不支持 HTML：**只能发送纯文本的邮件，不支持发送带有 HTML 格式的邮件，也是因为 macOS 上没有提供相应的 API，开发者表示仍在寻找解决方案。

Drafts Action 在 macOS 上的应用
--------------------------

乍看之下，Drafts Action 的这些功能似乎并不独特，macOS 上也有大量能常驻后台的自动化工具可以选择，比如 Keyboard Maestro、TextExpander、BetterTouchTool 等，Drafts Action 在这里面的位置是什么呢？

我实际使用了一段时间之后，发现 Drafts Action 确实有它自己的价值。

### URL Schemes 仍有存在意义

首先是体现了 URL Schemes 的价值。通过 URL Schemes 和其它应用交互的操作仍然很有必要，它大于简单的复制粘贴。因为我们已经预置了文本应该去的位置，而且不必等候应用打开，也不必查找新文本在应用里应在的位置，这既减少了操作，也能避免应用内部的其它元素对我们造成干扰。

我在 Drafts 里有两个发送到 Ulysses 的 Action：

**一个是发送文本到 Ulysses 的收件箱。** 因为 Drafts 有全局的速记功能，在任何界面都快速调用，所以有时候图快就随手在 Drafts 里记下一两句想法，过后想扩展成完整的文章了，再通过这个动作发送到 Ulysses 里进一步完善。

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/A1AFD70C-B8C7-40AD-A6D5-1C6CE223AF30.jpg)

用 URL Schemes 发送文本到 Ulysses

**另一个 Action 的作用是收集奏折素材。**因为 Ulysses 自带文档库同步，所以我会基于项目来整理里面的文章，奏折就被我放在了「Power+ 2.0」文件夹下的「奏折」文件夹里。如果靠手动层层点进这个文件夹再复制粘贴，那未免太麻烦了。这个 Action 就预先填好了文件夹位置，点一下就能发布过去。

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/E8D788CD-B4F6-4B84-AB4D-BDBB187825BE.jpg)

在 URL Schemes 里预设文件夹位置

这两个 Action 都是借助了 URL Schemes，实现的效果是往往应用还没打开，文本就已经传过去了。不过需要注意的是，**并不是所有应用在 iOS 和 macOS 上都提供了通用的 URL Schemes**，比如 Evernote 和 Fantastical 虽然在 iOS 有完善的 URL Schemes 支持，但在 macOS 上却几乎不可用；而 OmniFocus、Things、Day One、Ulysses 这几款应用，则在两个平台都提供了完善的 URL Schemes 支持。

由于 Drafts 的笔记属性，所以它的 URL Schemes 用法大多基于文本处理，但 URL Schemes 在 macOS 上其实还有更多的用处，比如快速调整、制作成超链接等，具体可以看 OscarGong 写的《[在 macOS 中使用 URL Schemes](https://sspai.com/post/55130)》。

### 和第三方服务的结合

Drafts 中通过 API 实现的操作，同样可以比其它方式都更快地实现我们想做的事。比如我在 Drafts 中有一个发送任务到 Todoist 的 Action，用于批量添加会议产生的任务。有时候开选题会的过程中会逐渐产生很多任务，我会将这些任务以及会议中产生的想法记录到 Drafts 里，会后稍加整理，再通过这个 Action 批量发送到 Todoist，每一行就是一个新任务。

**[⏬ 下载「+Todoist」动作](https://actions.getdrafts.com/a/11i)**

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/A29069A6-D21B-4D29-8782-B7BBCBCECFE7.jpg)

批量添加任务

这个 Action 基于 Todoist 的 API，好处是不用打开 Todoist 的 app，自动就能将数据同步到云端。而且它还支持 Todoist 的自然语言输入，比如「打印资料 tom #My-Job p2」这样的文本，就会被识别成「任务名称为『打印资料』，截止时间是『明天』，项目为『My-Job』，优先级为『第二优先级』」，方便我们在 Drafts 里直接对任务的属性进行预设。

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/197384BE-C465-468A-9BC4-D6B6681CD209.jpg)

自然语言输入

像 Drafts 这样内置了图形界面的第三方 API 服务，在前面提到的那批自动化工具里并不多见，它们往往需要更复杂的步骤才能实现相同的功能，而 Drafts 用简单的图形界面就能搞定，可以节省掉很多查询 API 文档、填 URL、填 API Key 等参数的步骤。

### JavaScript 小工具

Drafts 中通过 JavaScript 实现的功能，会直接让一些 macOS 的小工具丧失意义。比如 Drafts 用户 @nahumck 制作了一个文本处理动作，结合了「编码」「解码」「全大写」「全小写」「Title case」「小型大写字母」3「加连字符」「加圆圈」等多项功能，以往这些小需求都是通过第三方 app 或者搜索网页应用解决的，但这一个 Drafts 动作就能全部搞定。我把它放在了自定义键盘中，按下后弹出一个列表，让我选择想要的处理效果。

**[⏬ 下载「Text Modifier…」动作](https://actions.getdrafts.com/a/110)**（我稍微优化了显示方式，去掉了几个不常用的功能）

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/9473DBF2-E026-413F-A38E-D346E124A4C4.jpg)

文本处理动作合集

类似的 JavaScript 小工具还有：

* 将 Markdown 文本转换为 HTML 格式，并复制到剪贴板里：**[⏬ 下载「✪ > Rich Text」动作](https://actions.getdrafts.com/a/119)**
* 按照中文习惯统计字数（由 Minja 制作）：**[⏬ 下载「Word Counter」动作](https://actions.getdrafts.com/a/11a)**

但是，不可否认的是，在 iOS 上非常有用的「复制」「粘贴」「撤销」「缩进」等键盘上方的快捷键丧失了意义，因为很明显，在 macOS 上我们会用实体快捷键来做这些事，而 iOS（尤其是 iPhone）长按屏幕后再从菜单里选取的操作则没有自定义按键来得快。此外还有一些用 Drafts 内置标签实现的 Markdown 语法，比如在自定义按键中放一个 `#` 的快捷键，就是为了快速输入 Markdown 里的标题符号 `#`，在 macOS 上也失去了意义。

不过，如果你把这些动作都换成 JavaScript 版本的话，不仅功能上有所增强，还能在 macOS 上焕发新生。比如同样是插入标题符号的动作，如果你用「插入文本（Insert Text）」模块实现的话，只能在当前光标位置插入符号；而 JavaScript 版本不需要将光标移动到行首，就能插入 `#` 符号，按多几下还能继续增加标题层级。

**[⏬ 下载「Markdown Header (#)」动作](https://actions.getdrafts.com/a/11b)**

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/13DD93A4-B020-4B3F-B59A-8D66A974117B.gif)

JavaScript 版本的 Markdown 动作

这类 JavaScript 动作不需要自己制作，基本都能在 Drafts 的[官方库](https://actions.getdrafts.com/)中搜到，类似的还有：

* **[插入 Markdown 列表符号（-）](https://actions.getdrafts.com/a/11c)**：同样不需要将光标移动到行首，还支持对多行文本进行操作；
* **[插入 Markdown 引用符号（>）](https://actions.getdrafts.com/a/11d)**：同上；
* **[插入 Markdown 加粗符号（\*\*）](https://actions.getdrafts.com/a/11e)**：选中要加粗的文本，按下快捷键后就能在文本的两端插入加粗符号，不需要来回移动光标。

根据 macOS 习惯调整
-------------

如果你刚在 macOS 上升级到 Drafts 16，可能会发现一些 Action 和自定义按键意义不大，比如前面提到的「复制」「粘贴」「撤销」等，所以你需要调整自己的 Action 的排布，让自己在 iOS 和 macOS 上使用 Drafts 时都更得心应手。

考虑到两个平台的操作习惯不同，Drafts 16 也很贴心地在 Action 设置里提供了是否在 iOS 和 macOS 显示的开关，你可以先通过这个开关来进行初始调整：

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/820265E7-A6F1-4B03-9897-8C59881694FA.jpg)

设置平台的开关

自定义按键由于会一直常驻显示，所以我分别制作了两组自定义按键，一组专门在 iOS 上使用，另一组专门在 macOS 上使用。macOS 组去掉了「复制」「粘贴」「撤销」这些 macOS 上用不到的按键，留下了「Markdown 列表符号」「Markdown 引用符号」这些可以批量操作的按键，以及文本处理、插入 TaskPaper 任务符号等功能按键。

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/95AD42E6-5744-4F4A-8292-D4C72769D1CE.jpg)

iOS 和 macOS 分别有不同的自定义按键

而 Action 功能，我则不建议让它一直常驻显示在侧边栏里。因为 Drafts 作为笔记应用，我更倾向于让它的应用窗口保持小巧，不占用过多屏幕空间。如果让 Drafts 同时显示标签、列表、Action，再加上笔记本身这一栏，整个窗口就会显得过于冗杂，而且 Action 栏关闭后窗口还不会缩回原来的大小，非常烦人。4

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/E35D1BD7-7F02-43FF-A81D-2F9D07461831.jpg)

关闭 Action 栏后不会自动缩小窗口，一直显示又过于占用空间

我更推荐的使用 Action 栏的方法是：**对 Action 进行编码，然后使用系统顶部的菜单栏，再借助 macOS 上的「快捷键之王」来启动。**

Drafts 的开发者很懂 macOS，绝大部分的 Drafts 功能都能在菜单栏中找到，包括 Action 栏里所有的 Action。这样做的好处是用户[可以任意为它们赋予快捷键](https://sspai.com/post/38664)，并且快捷键会显示在菜单栏里，方便你加强记忆。不过这里我要讲的不是为每个 Action 赋予快捷键，而是通过一个统一的快捷键来检索它们，这个快捷键是 `⇧Shift-⌘Command-/`，被 Hum 称为「[macOS 上的快捷键之王](https://sspai.com/post/38403)」。它的作用就是让你输入文字，然后检索菜单栏里所有的选项。比如输入「Markdown」，就能搜到很多和 Markdown 相关的选项：

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/EF0F1704-24B2-41D8-95C5-A93050000ED3.gif)

快捷键之王

那么如何更快地搜到这些 Action 呢，我这里也借鉴了 Hum 的[标签编码方法](https://sspai.com/post/40742)，对每个 Action 进行编码，这样我只需要在按下 `⇧Shift-⌘Command-/` 之后，输入「01」「02」等数字，就能快速找到这些 Action：

![](.evernote-content/BFD9B00F-248C-4068-91AE-150C3BEFE292/6FCD8695-0CBF-44EC-9DFC-4916ADE1B27F.jpg)

通过编码快速找到 Action

结语
--

Drafts 是采用订阅制软件里的好榜样，它有勤快的更新节奏，也真正做到了每个版本都有惊喜。[不用再憋大招放到大版本更新](https://sspai.com/post/57602)，可以把用户急需的新功能、开发者想到的新点子，更快速地迭代到现有版本上。

虽然 macOS 平台的自动化工具很丰富，但 Drafts 的 Action 功能凭借其易用的内置模块，以及可以由用户提交的官方 Action 库，仍能在这些软件堆里找到自己的位置。

致谢
--

感谢 Hum 提供了本文的选题，以及他对 Drafts Action 和自动化的一些独特见解。说起来很巧，我第一次读 Hum 的文章就是他以前在越狱指南写的 [Drafts 系列](https://jbguide.me/tags/drafts)，那也是我第一次注意到 Drafts 这款应用，并且看完文章后当时就决定了要买下它。

* 1 另外两个卖点分别是打开即写和键盘上方的自定义按键，后者本质上也可以看作 Action。
* 2 简单理解 API 和 SDK 区别：API 是数据接口；SDK 是一套打包好的可以直接下载的工具包，里面包含了 API。
* 3 不太规范的用法，原理是替换成 Unicode 中的特殊字符。
* 4 标签栏和列表栏由于具备整理分类的功能，所以我更愿意让它们常驻显示。

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57721)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1414c8cd-3bb9-4d5c-b54e-c71b4ca2a288/1414c8cd-3bb9-4d5c-b54e-c71b4ca2a288/)