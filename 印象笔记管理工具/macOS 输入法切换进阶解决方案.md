# macOS 输入法切换进阶解决方案

---

macOS 输入法切换进阶解决方案
=================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

macOS 的输入法切换起来并不顺畅。

默认系统下，比较快的方式是通过 `⌃Control-⌘Command`（或别的快捷键）在几个输入法里面打转，不幸的是，每换一次输入方案，整个输入法菜单顺序就会重新洗牌，这种反直觉的设计让人切个输入法都要小心翼翼，无法做到不假思索的盲操作 1 。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/C065CE7F-DCD2-4D83-8B0F-AFB8A5D68D0D.png)

频频被打乱顺序的输入法菜单

在这个背景下，不少高手都提出过优化输入法切换体验的思路，但是很少有能够兼顾切换速度和精确度的。对比很多方案后，我重写了一段流传多年的 AppleScript 代码，最后给出一套比较理想的解决方案：

1. **指哪打哪**，精确切换输入法。
2. **快速无痕**，输入法图标一闪的功夫就完成切换。
3. **灵活自定义**，可以和各种自动化工具结合，实现快捷键绑定或者视应用自动切换。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/924D9094-94EB-402A-A28A-A50DAA334888.gif)

通过快捷键切换到指定输入法

这一次，希望能彻底解决 macOS 输入法切换顽疾。

两套切换方式
------

切换输入法的核心是一段 AppleScript 代码，通过套在不同的自动化工具和动作中，可以带来两种不同的切换方式：

1. 通过快捷键手动切换
2. 根据当前应用自动切换

不管最后你用哪个自动化动作，最后起切换作用的部分是一样的，这里在给出 Keyboard Maestro 版（设置起来最简单）的同时也会放出 AppleScript 脚本的地址，方便其他工具的用户取用。

* [手动切换下载（Keyboard Maestro）](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Switch%20Input%20Source%20Auto%20Macros.kmmacros.zip)
* [自动切换下载（Keyboard Maestro）](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Switch%20Input%20Source%20Macros.kmmacros.zip)
* [AppleScript 脚本下载](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/Switch%20Input%20Source.scpt.zip)

### 快捷键手动切换

手动切换是最常见的方式，快捷键在稍加使用后又是最符合直觉的。我提供的 Keyboard Maestro 动作组中预设了中文拼音、美式键盘和日文假名 3 组键盘的切换动作，如果你是英文系统可开箱即用 2 ：

* `⌃Control-⌥Option-⌘Command-1`：切到日文假名
* `⌃Control-⌥Option-⌘Command-2`：切到中文全拼
* `⌃Control-⌥Option-⌘Command-3`：切到美式键盘

这样一来，按哪组快捷键就能调出指定的输入法，不用被顺序动不动就变乱的切换菜单耽误。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/1BBD5842-596E-4AB8-BD99-D875092F40AA.gif)

用快捷键切换输入法

使用中文系统或者需要添加其他输入法的读者可以自己动手。任意打开其中一个 Keyboard Maestro 动作，可以看到其由触发条件 Trigger 和具体动作 Action 组成。首先找到动作中 AppleScript 脚本的最后一行，把**括号里的输入法名称换成你所需要的**，同时记得保留两边的引号。输入法名称可以在菜单栏中找到 3 ，不同语言的操作系统显示出来不一样，需要严格按照所显示的名字修改脚本。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/42F77213-391B-4458-AC5D-51DBBD7EB82D.png)

修改手动切换的动作

之后给动作设置顺手的快捷键，一个切换输入法的 Keyboard Maestro 动作就自定义完成了。诚然有些输入法自带了切换快捷键（比如日文输入法的假名和罗马字两种模式），但是这些键位容易和其他应用冲突、又不能轻易改，我个人更喜欢通过 Keyboard Maestro 来设置长长的快捷键，避免键位打架，大家也可以设置更简短易按的组合方式。

### 按应用自动切换

除了手动切输入法，有些比较固定的场景下也可以自动开启特定输入方案。最典型的就是在终端中开启美式键盘，以待后续直接输英文命令。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/CE81CB94-DC9C-4EAC-987F-31A60A89697E.gif)

根据应用自动切换输入法

这个需求同样可以在 Keyboard Maestro 中完成，而且还能在用完应用离开后再切回正常输入法。这回的触发条件需要变成**「This application」**，视是否处于具体应用中**（Active 或 Deactive）**来触发切换动作。脚本部分的修改方式和手动切换一样，此处不赘。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/100F3341-3A0D-4DB1-B87B-935AAF065FCC.png)

自动切换的 Keyboard Maestro 设置

自动切换的情景不限于终端，你所下载的动作组里还包含了脚本编辑器场景下的自动切换，当然其他工具也能搭配上专属输入法。使用指南部分到此为止，后面我们来看一下这一系列动作是怎样实现的。主要涉及的知识点有：

1. 如何用 AppleScript 模拟点击菜单栏
2. 如何让 AppleScript 在暗地里点击，不显示操作过程

这些内容在各种和菜单栏工具交互的时候都可能派上用场，有折腾想法的读者不妨一读。

原理简析
----

通过自动化工具精确切换输入法并不是一个新鲜的想法。早在 2013 年，编程论坛 Stackoverflow 上就有人进行过相关的 [讨论](https://superuser.com/questions/588534/switch-to-a-specific-input-source-in-os-x)，本文方案正是脱胎于其中的一段古早代码。

切换的核心是**借助 AppleScript 模拟鼠标运动，从而点击菜单栏（Menu bar）中的指定输入法选项**。但是最初的代码运行起来并不算理想，每次切换时都会展开整个输入法菜单，有碍观瞻。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/9C0A8BD7-CFC7-4975-9260-E5701BAEEA6E.gif)

最初的方案需要展开菜单才能工作

我早在几年前就了解到 AppleScript 切输入法的方案，但苦于运行过程粗糙，一直不敢向人推荐。后来读到 @Nanana《[一键切换 macOS 输入法的多种方案](https://sspai.com/post/52964)》一文，深感 Karabiner-Elements 方案的轻快无痕 4 ，便又起了捣鼓的劲儿。

一番改良之后，终将 AppleScript 方案中悬了几年的心结悉数解开，遂有此文。

### 模拟点击菜单栏

如果要手动切换输入法，我们需要做两件事：

1. 点击菜单栏中的输入法图标
2. 点中所需的输入法选项

这套操作，早年间的高手们就用 AppleScript 实现了。AppleScript 胜在语法直白，但福兮祸倚，坊间流传的代码中夹杂了 `something's` 这样典型的英文所有格来表示菜单栏控件 —— 雪上加霜的是，后面还跟着一个 `whose` 从句，让人想改写也无从下手。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/3F8783FB-DAF0-4124-A033-F3DA3D63B6EC.png)

过长的单行代码

改良的第一步就是把 AppleScript 改成更容易理解和修改的形式，我比较推荐的是**「套娃式」**。@帕特里柯基 在《[AppleScript 入门：探索 macOS 自动化](https://sspai.com/post/46912)》一文中已经介绍过这种层层嵌套的 AppleScript 语法结构。

原先的代码结构堪比一段用上各种高级语法结构不带喘气的炫技中考英文作文 5 ，很难搞懂每部分对应的各个系统控件。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/0749ED9E-84CA-4FCE-9BCF-DD4B14F5329F.png)

原先的代码比较难理解

一旦拆开来写，尽管代码变得冗长了，但是好识别很多，也能很快将代码和菜单栏中的控件对应起来。

1. **System Events**：所有模拟键鼠的行为都需要交给 System Events 来执行，最先出场的就是它。
2. **SystemUIServer**：菜单栏中的输入法图标隶属 SystemUIServer 管辖，因此第二步就靠 SystemUIServer 传达。
3. 剩余组件部分从大到小依次类推，分别是：
   1. **menu bar 1**：表示菜单栏，注意控制多数应用时会用 `menu bar 2` 来和左侧的菜单区分，SystemUIServer 属于特例。
   2. **menu bar item 某某**：可以数字来表示要点击菜单中归 SystemUIServer 管的第几个图标，如果图标数量比较多而且位置经常变动，可以在指定完位置后再添上具体称谓： `whose description is "名称"`
   3. **menu 某某**：同样使用数字指定第几个子菜单。菜单栏中有用作分隔的几条细线，它们划出来的就是子菜单了。
   4. **menu item 某某**：最后具体要点击的选项，通常添上选项名字即可。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/5F742246-F821-4D29-87F4-5370AB7791E1.png)

层层深入的组件

不难发现，切换输入法其实是控制菜单栏的特殊情况（也是最复杂的情况之一），普通应用既没有那么多选项，也没有那么多图标，代码往往会更简洁。最后还是看一眼拆开重写的切换代码，这只套娃还有很大的改进空间。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/F34EEB33-3000-42DA-BF58-C80F30254F6E.png)

层层嵌套的代码

参考资料：

* [Mac Automation Scripting Guide: Automating the User Interface](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html)
* [AppleScript: Graphic User Interface (GUI) Scripting](http://www.macosxautomation.com/applescript/uiscripting/index.html)

### 优化到「无痕操作」

至此为止，我们的改进似乎都只限于代码形式，不过你可以运行上面的代码试试（记得把假名输入法 `Hiragana` 改成其他你在用的输入方案），奇怪的事情发生了：菜单栏没有展开，输入法也没有切过去；此时点一下输入法图标一看究竟，结果发现切换又是正常的 —— 似乎输入法在「等」我们点它一下。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/02F205AF-7C4E-45D8-9687-F60992BE674D.gif)

点一下才能切输入法

注意，上面整个过程中菜单栏都没有展开。这就是我们实现无痕操作的关键 —— **改变点击顺序**，先点输入法选项，再点菜单栏，这样就能让 AppleScript 全程在幕后工作。落地到代码就简单了，把刚才的套娃拆出一部分，保留到点击菜单栏为止，复制到原代码下方即可完成两次点击。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/53A2E37B-D6B2-4ECE-B31A-9620783413CD.png)

避免展开菜单栏的代码

接下去就是一些例行的套壳过程，中间还要套一层 AppleScript 函数，不过这部分不影响本文动作主要功能，暂时不讲；大致明白整体实现思路后，习惯 Automator、Keyboard Maestro 等不同工具的读者就可以各取所需进行移植。我日常用的是 Keyboard Maestro，为几个常用输入法设置了不同的 `Hyper-数字键` 启动方式。

* `Hyper-1`：切到日文，这一键位其实有点偏，所以我分配给了用得最少的日文假名输入法。
* `Hyper-2`：切到双拼，这个键位比较居中，我给了最常用的中文双拼。
* `Hyper-3`：切到美式键盘，有些古董网站的登录框需要用到。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/070D5D4A-8125-4FBC-885A-ECD267A17CB8.png)

Keyboard Maestro 步骤

所谓 Hyper 键其实是按键不够用的产物，上世纪的键盘中就有这颗实体键，现在可以把 `⌃Control、⌥Option` 和 `⌘Command` 一起按下模拟 Hyper。这些快捷键的分配思路在此只是简要一提，感兴趣的读者可以参考《[快捷键终极使用指南 | 效率思维](https://sspai.com/article/52239?series_id=70)》。

来试试 Keyboard Maestro 的切换效果，已经能够同时实现精确指定输入法和无痕操作。由于核心是 AppleScript，换到其他自动化工具后切换效果也一样，不同的只是我们的操作方式。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/0274ED5E-6CAC-4E9A-B656-BFA17775F19F.gif)

通过快捷键切换输入法

完成手动切换操作后，我们最后看一下如何**根据应用自动切换输入法**。很多情况下，能够自动切换输入法会让文字输入变得更自然，不至于打几个字才发现出不了字。

* **开启终端时**，切到英文状态，等待输入命令
* **退出终端时**，切回中文状态，方便正常打字
* **离开脚本编辑器后**，换回中文输入法，重新回到正常打字状态
* ……

某些第三方输入法（比如鼠须管、落格）自身支持自动切换，但不用这些输入法的读者就享受不了。而通过 Keyboard Maestro，可以脱离输入法本身的限制进行自动切换。

Keyboard Maestro 中有个「This application」的触发方式（Trigger），可以根据自己需要把应用开启和退出设置成输入法切换的触发条件。比如开终端时自动开打英文输入，可以这样设置。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/19216869-9028-4716-81A9-CFFAE2C4F242.png)

设置应用为触发条件

打开终端试试，不出意料就能自动切换到英文。同样为中文输入设置一个自动开启条件，就能在退出终端后再换回来。

![](.evernote-content/5AF1A6C4-7781-44DC-A6B1-0CCF2CCD9A93/CE81CB94-DC9C-4EAC-987F-31A60A89697E.gif)

根据应用自动切换应用

小结
--

输入法切换是一件小事，但不表示我们必须长期忍受默认的低效切换方式。事实上，已经有不少开发者和自动化高玩就这个问题给出了自己的方案，我不过是在它们的工作上再提出了一种比较开放的选择。

除了文中提到的快捷键切换和自动切换，各位也可以结合自己趁手的工具进行改装，总之让动作适合自己最重要。如果能够帮到同样因输入法切换问题而心烦的读者，便算是一种荣幸了。

1. [除非在必有的美式键盘以外，你只用一个输入法↩](#)
2. [效果类似 Kawa，但本文方案可以配合 Keyboard Maestro 实现自动切换↩](#)
3. [所以你需要现在输入法设置中开启菜单栏图标，这可能是本文方案的唯一瑕疵↩](#)
4. [而且可以直接改键盘，按一颗键就实现切换，这是本文方案很难做到的↩](#)
5. [就像这句话一样让人让人读得上气不接下气↩](#)

---

[🌐 原始链接](https://sspai.com/post/54685)

[📎 在印象笔记中打开](evernote:///view/207087/s1/365d412c-329b-43c3-9786-e50f64ebad18/365d412c-329b-43c3-9786-e50f64ebad18/)