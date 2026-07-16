---
title: "Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活.md
tags: [印象笔记]
---

# Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活

# Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活 --- ![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AF

---

# Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活

---

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/D7888F58-6EA2-4C1B-A4F3-7158A033791A.jpg)

### *「2016 与我的数字生活」年度征文入围作品*

今年，我们在  [2016 年度盘点](http://sspai.com/topic/2016/) 中举办了一次大型年度征文活动，鼓励大家围绕「数字生活」为主题，回顾刚刚过去的 2016 年。我们给予最开放的选题、最自由的投稿方式、有史以来最丰厚的 [奖品](http://cdn.sspai.com/attachment/thumbnail/2016/12/26/faeb3befe1e2d8c138a027f0b72d30675810b_mw_800_wm_1_wmp_3.jpg)，以及跨越春节的两个月充足时间，等你参与。你可以 [点此查看](http://sspai.com/36695) 活动规则和奖品清单。

本文是「2016 与我的数字生活」征文活动的**第 34 篇**入围作品，我们会在两个月的活动期内，不定期从收到的投稿中挑选发布优秀的文章，你可以 [点此查看](http://sspai.com/topic/2016/) 之前的入围文章。所有经此发布的文章，即为已入围征文活动。本文仅代表作者本人观点，少数派仅对标题和排版略作调整。

> 2016 年在 App 上最大的收获就是入手 Keyboard Maestro 并应用到我的工作中了。在体会到 Keyboard Maestro 的强大之处后，正好赶上搞活动，5.6 折 20 刀拿下 ，这绝对是我 2016 年购买的最值的 App。

前言
--

Keyboard Maestro 其实很早就有所了解，但是在看过很多教程和实例后仍对它所能实现的功能有些迷茫，可能是并非是自身的需求，所以不能切身感受到其强大的功能， 直到在工作中使用 Keyboard Maestro 才真正意识到。少数派里有很多优秀的介绍文章，如[《Keyboard Maestro 入门指南》](http://sspai.com/36442)、[《懒的前提是要足够高效： Mac 效率工具 Keyboard Maestro 详解》](http://sspai.com/28721)，我这里只是分享下我的用法，工具都是经过量身定制才能真正发挥其作用，才能体现其价值 😁。

初识 Keyboard Maestro
-------------------

> 在 OmniFocus 身上尝到了 AppleScript 的甜头后，就对 AppleScript 产生了浓厚的兴趣，然后开始尝试其他场景和操作能否使用 AppleScript 去完成。

真正开始接触 Keyboard Maestro 是因为当初想使用 THL（[The Hit List](https://itunes.apple.com/cn/app/the-hit-list-simply-powerful-tasks/id432764806?l=en&mt=12&uo=4&at=10lJSw)），THL 不像 [OmniFocus](http://sspai.com/tag/OmniFocus) 那样提供了脚本的工具栏空间，所以脚本需要以其他方式运行，比如 Menu Bar 里的脚本菜单、设置快捷键并记住、App 的「服务」里等，让人感觉很不直观，各种论坛对脚本的执行都推崇使用 Keyboard Maestro ，遂尝试之。

我现在使用 Keyboard Maestro 的场景主要就是以下三个：

1. OmniFocus
2. Finder
3. Word

最开始使用 Keyboard Maestro 的时候只是当作 AppleScript 的启动器，然后开始慢慢改造，才发现 Keyboard Maestro 是如此的方便，很多数据可以经 Keyboard Maestro 处理后交给 AppleScript 去执行，减少了编写 AppleScript 的工作。

OmniFocus
---------

> 使用 Keyboard Maestro 的方式有很多，其他教程都有介绍，我一直使用 Shrink Palette（因为懒得记快捷键）。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/25C90C26-5C2B-466B-B20C-92204BF92FA8.jpg)

如图设置会在指定 App 激活时才出现该组的悬浮窗，对于项目的排序也有很丰富的设置，这里不做过多表述。

### Template for OmniFocus

在 OmniFocus 里我主要是针对「模板脚本」，在[《帮我打造 OmniFocus 工作流的得力助手：「模板脚本」的使用分享 | 2016 与我的数字生活》](http://sspai.com/36927)也介绍过，原始的脚本在变量多的时候需要逐一对变量赋值，如果出现录入错误就需要全部重来 😳，通过 Keyboard Maestro 我们可以实现对变量的批量赋值，然后执行 AppleScript ，这就大大的提高了录入数据的准确率和效率。

该 Macro 使用了以下 Action ：

1. Execute AppleScript - 运行一段录入多行文本变量的脚本；
2. Set Variable to Text - 设置行号变量，初始值 0 ；
3. For Each - 根据行数循环，将每一行的文本赋值给一相应的变量；
4. Prompt for User Input - 将所有变量信息在一组输入框内显示，有错误可以进行修改；
5. Switch - 处理下拉框「审限」变量；
6. Execute AppleScript - 运行改造过的 OmniFocus 的「模板脚本」，开始依据模板生成任务；
7. Execute Macro - 运行一个删除本次运行生成的变量的 Macro，如果在 Keyboard Maestro 新建过变量的，官方都建议在 Macro 最后删除所生成的变量，已减少内存空间的占用（貌似），该 Macro 在官方 Wiki 有。

Finder
------

Finder 作为 macOS 下的文件管理器，其强大的 Tag 和 Smart Folder 让文档管理又清晰又快捷，作为系统内置的 App 自然也提供了丰富的 AppleScript 接口，使用 KM 来执行脚本就更方便了。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/9A6ECBDD-223C-4FA9-BD88-9B0F55F81A44.gif)

### 拷贝文件

法律文书都有固定格式，所以每次都需要拷贝模板文件到特定案件的文件夹里，时间长了就很烦，对于这种重复又麻烦的操作使用 AppleScript 来处理是再合适不过了。

该 Macro 其实就是简单的执行一个 AppleScript 脚本，拷贝模板文件到当前文件夹，其实 macOS 自带的 Automator 也能做到，Keyboard Maestro 也有执行 Automator Workflow 的 Action ，这个以后再说。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/3EE8EC9E-A1E1-4382-8476-DCF11C0E3236.jpg)

### 改文件名

模板文件拷贝过来以后，为了便于管理和检索，将所在文件夹的名称中所含的案号添加到文件名中，以后在 Spotlight 或者 Alfred 等里搜索案号就可以直接定位相关文书了。

该 Macro 使用了以下 Action ：

1. Execute AppleScript - 执行 AppleScript 脚本，获取当前文件夹的名称；
2. Search Variable Using Regular Expression - 利用正则表达式搜索「案号」，并赋值变量；
3. Execute AppleScript - 执行 AppleScript 脚本，变更文件名；
4. Execute Macro - 执行删除本次生成的变量的 Macro。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/35616EA7-1A21-4BD7-B670-BCB6600ADC16.jpg)

Word
----

Word 是我工作的必备工具，为了保证文书的兼容性，必须使用 MS Word （谁让 WPS 不出 Mac 版呢 😂），正好 MS Office 提供了极其丰富的 AppleScrip 接口，比 Apple 的 iWorks 都丰富，MS 真的是 Apple 的好基友 😂。有了这么多接口必然要用 AppleScript 好好调教调教啦 ✌️。

### 打开 Finder

不知道你们有没有这样的经历，在一个文件夹打开一个 Doc 后，随手就关闭了 Finder ，然后在编写的时候发现需要打开同一文件夹里的另一个文件，这是就得打开 Finder 挨个路径点一遍，好了，现在有 Keyboard Maestro 帮助你。

该 Macro 也仅仅执行一个段 AppleScript 代码而已。就是获取当前文档所在路径，并告诉 Finder 打开即可。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/79EDD274-773D-43D7-82D0-51A3C2AC1FA1.jpg)

### 替换关键词

每个案件都会有很多文档，而这些文档又会有很多信息是共同的，比如案号、案由、当事人等，如果每个文档都如此录入一遍相当麻烦，即便是拷贝粘贴也是个体力活，没关系，我们用 Keyboard Maestro 一键搞定。

该类 Macro 使用了以下 Action ：

1. Execute AppleScript - 执行脚本，获取当前文件夹名称及在 OmniFocus 中录入的相关信息；
2. Search Variable Using Regular Expression - 利用正则表达式对提取的变量进行处理，比如将文件夹名称（该名称在[前文](http://sspai.com/36927)中利用脚本所建立）拆分为「案号」、「当事人及案由」、「案由」，Keyboard Maestro 的正则表达式正好弥补了 AppleScript 的短板，可以很简单的就拆分变量；
3. Type the ⌘A Keystroke - 全选文档，Word 的 replace 命令是在选择的范围内进行；
4. Execute AppleScript - 执行替换 Word 关键词的脚本；
5. Execute Macro - 删除本次生成的变量。

在一些特定的文档上，可以加入 「Prompt for User Input」Action 允许修改和另行输入相关信息用以替换 。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/D59744B8-B68D-485D-9C85-000913302CE8.jpg)

### 处理文本顺序

得益于 Keyboard Maestro 易用的正则表达式，让我们更容易的去处理一些特定的文本，比如对原审判决的表述，完全可以由原审文书头部换个顺序得来。

该 Macro 使用了以下 Action ：

1. Filter Clipboard with Remove Styles - 我们首先复制原审文书的头部到剪贴板，然后移除剪贴板的格式；
2. Search and Replace Clipboard With String Matching - 使用正则表达式移除剪贴板里的空格；
3. Set Variable & For Each Item in a Collection Execute Actions - 处理剪贴板的数据，一行文本赋值给一个变量，主要拆分成「原审法院」、「原审案号」、「文书类型」；
4. Set Clipboard to Text - 设置剪贴板内容为「原审法院」+「原审案号」+「文书类型」的顺序文本；
5. Execute Macro - 删除所用变量。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/5DBA0423-FBE1-4858-835B-34B981AF3F07.jpg)

### 短语输入

Keyboard Maestro 使用「This string is typed」Trigger 可以实现 TextExpander 的类似功能，再结合 Keyboard Maestro 的变量处理，完美的处理「发回重审」的规范输入。

该 Macro 以如下流程运行：

1. Search Clipboard Using Regular Expression - 将上节处理好的剪贴板内容直接用正则表达式拆分成「原审法院」、「原审文书」；
2. Insert Text - 设置制式文本，并将上述两变量插入到相应位置；
3. Execute Macro - 删除使用的变量。

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/B8A798B1-AF87-4C2C-82AD-9B52A44BA396.jpg)

![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/9F9EA82F-A947-4316-9975-8E09FFBB48DD.gif)

总结
--

我使用 Keyboard Maestro 主要就以下几个步骤：

1. 先用 Keyboard Maestro 处理变量，利用 Keyboard Maestro 强大的正则表达式拆分组合文本，在正则表达式里将需要单独提出的变量加上（）就行，测试的时候会很直观的显示变量的结果，相当方便，对于刚接触正则表达式的我帮助颇大。![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/7D05E8D8-3CFE-4F1A-A77C-D913E5A1B768.jpg)
2. 然后将变量传递给 AppleScript 用以执行，也可以是使用 AppleScript 获取变量后再传递给 Keyboard Maestro 处理，Keyboard Maestro 与脚本直接的变量传递也极大的降低了脚本的编写难度。
3. 最后官方论坛强烈建议在每次 Macro 执行完毕后都养成清理变量的好习惯，便于内存的释放吧，官方论坛提供了一个通用的 Macro ：[[KM] DELETE List of KM Variables [SUB-MACRO]](https://forum.keyboardmaestro.com/t/km-delete-list-of-km-variables-sub-macro/3435)，调用该 Macro ，填入需要删除的变量名即可。

通过上文介绍，是不是发现 Keyboard Maestro 简直无所不能，Keyboard Maestro 其实可以作为 Automator 的增强版，自身提供了大量的 Action，很简单的就能搭建一个自己的 Macro，而且提供了更便捷的执行入口，其对各种脚本的支持更是扩展了无限可能，很多需要使用 Shell 命令开关的系统功能，都可以使用 Keyboard Maestro 既便于存放又便于执行。

在你迷茫 Keyboard Maestro 如何使用的时候，不妨就执行几个简单的命令，等你习惯后自然会开发更深的用法了，希望本文能让你更好地认识 Keyboard Maestro 并更好的利用它来提高效率。

（如果你喜欢这篇文章，我们鼓励你在文末点赞和评论，这会成为 [征文活动](http://sspai.com/36695) 最后评奖的参考之一，你可以 [点此查看](http://sspai.com/topic/2016/) 之前的入围文章。 ）

文章来源 [少数派](http://sspai.com) ，原作者 [Janner Chang](http://sspai.com/author/735387) ，转载请注明原文链接

原文可获取应用下载链接：[Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活](http://sspai.com/37708)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/91000A4E-BB3D-4035-B01C-9482AFD02CDB/3F6B180F-6CF1-4BA6-83FF-92E6B38A911C.jpg)](http://click.dji.com/ABURuoReMxaFL_0m6mfp?pm=custom)

---

[🌐 原始链接](http://sspai.com/37708)

[📎 在印象笔记中打开](evernote:///view/207087/s1/16317e4b-32cc-4de4-97d5-b95c8eb5ef73/16317e4b-32cc-4de4-97d5-b95c8eb5ef73/)