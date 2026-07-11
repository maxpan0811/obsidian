---
title: Automator 简单介绍及入门玩法 _ Matrix 精选
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Automator 简单介绍及入门玩法 _ Matrix 精选.md
tags: [印象笔记]
---

# Automator 简单介绍及入门玩法 | Matrix 精选

---

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/E45737E4-0537-4E2D-81C9-08AAA81C26B9.jpg)

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/46189A1E-11E9-4F69-A36E-51D48A3129A1.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章对标题和排版略作修改，[原文链接](http://matrix.sspai.com/p/da7fab40)。

iOS 上大名鼎鼎的 [Workflow](http://sspai.com/tag/workflow) 在我派是深入人心，许多大神研究了很多高阶的玩法，利用 Workflow 提高了不少的效率。不得不承认，自从我开始用 Workflow 之后，也是越来越离不开他。iOS 端有 Workflow 这样的神器，那么 Mac 端呢？当然有，而且还是 macOS 系统自带的，叫 Automator ，俗称「扛炮」。他在一个很不起眼的地方，你可以通过 Spotlight 搜索来启动它。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/6D48A205-0A74-4EAF-A081-E9B39B02D578.jpg)

说实话，第一次知道 Automator 叫扛炮，我笑的停不下来。

界面介绍
----

打开 Automator ，我们新建一个文稿，然后点击工作流程，然后我们就来到了 Automator 的主界面。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/483DD745-5A32-43FA-97A7-4CE82009C3E3.jpg)

我们可以把界面分成三块，左侧的部分叫做资源库。Apple 已经贴心的在这里给我们准备了很多的动作。有系统级别的动作，也有相应 App 的一些动作。稍后我们编辑工作流程的时候，这些动作我们可以直接拖到右侧用，就像iOS 上的 Workflow 一样。右侧灰色的地方是动作编辑区，是我们制作动作流程的地方。那么编辑区下方就是流程运行的日志了，如果我们的工作流程有什么出错，就会在这里显示。

是不是会觉得和 Workflow 很像？实际上他们就是一家人。其实，[Keyboard Maestro](http://sspai.com/tag/Keyboard%20Maestro) ，Automator ，Workflow 都是同一类型的软件，都能够帮助我们这种「懒」人自动的去完成一些操作。无论是设计还是功能，三者都有着异曲同工之妙。

Automator 能做什么？
---------------

下面我们通过几个例子，来具体展示一下 Automator 的强大功能。

#### 1. 一键音频输出切换

我的桌面系统有一个 USB 连接的音箱和一个 DAC 连接的耳机。人是一种很奇怪的动物，有时候喜欢外放，有时候又喜欢独享。那么这就带来了一个问题：我们要怎么去切换输出的设备？

我当然可以拔掉一个接另一个，可是这样一点都不酷。而且这些的连接部分都藏在电线收纳盒里，每次都插拔会把人都累死。另外一种方法是按 option 点击状态栏的音量图标，可以选择输出设备。可我想要一种更懒的方法，摊在椅子上，然后我「啪」的按一下键盘，音频就切换了。如果要我坐起来按住键盘用鼠标来选，我觉得特别麻烦，由此可见，懒真是促进人类科技发展得以一个重大动力。

这个时候，Automator 就登场了。只需要一个 AppleScript ，所有问题迎刃而解。

我们在左侧的资源库搜索「运行 AppleScript」，然后把它拖到右边的编辑区，输入下面的命令：

```
on run {input, parameters}
tell application "System Preferences"
activate
set current pane to pane "com.apple.preference.sound"
end tell
tell application "System Events"
tell application process "System Preferences"
repeat until exists tab group 1 of window "声音"
end repeat
tell tab group 1 of window "声音"
click radio button "输出"
if (selected of row 4 of table 1 of scroll area 1) then
set selected of row 3 of table 1 of scroll area 1 to true
set deviceselected to "Generic USB Audio Device"
else
set selected of row 4 of table 1 of scroll area 1 to true
set deviceselected to "USB Audio DAC"
end if
end tell
end tell
end tell
tell application "System Preferences" to quit

return input
end run
```

这是从网上搜索来的一个 AppleScript ，我们只需要修改 row 后面的数字和需要切换的设备名称就可以了。其中 row 后面的数字对应输出设备在「系统偏好设置 — 声音 — 输出」的排列顺序。

我们在 Automator 运行一下这个工作流程，看看有没有报错，测试音频是否切换成功。成功之后，保存这个工作流程，给他命上一个自己喜欢的名字。然后进入「系统偏好设置 — 安全性与隐私 — 隐私」里，选择下方的辅助功能，在右侧的框里把所有的勾都勾选上。因为如果有一个应用程序没有勾选的话，你在这个应用里运行这个工作流程会报错，所以这一步一定不要忘记。

在这里插一小段，快捷键的设置不建议在「系统偏好设置 — 键盘 — 快捷键」里设置，建议用 Keyboard Maestro 。在 Keyboard Maestro 里设置一个快捷键，然后选择运行工作流程，把我们保存的这个工作流程选进去。因为系统设置的快捷键不能设置为单键，如果设置为单键，按下之后不会有反应，并且楼主在用外接键盘的时候，有时候会失灵，换成 Keyboard Maestro 之后，就从来没有出错或者失灵过了。

#### 2.从PDF文件中提取文本

对于楼主这样一个文科生来说，这是一个十分有用的工作流。它能帮助我从 PDF 文件中直接提取出文本，并且能够选择输出的方式，尽管不是特别专业的软件，但是胜在简单、不需要安装第三方软件。

我们在 Automator 中新建一个文稿，选择应用程序，然后在左侧的资源库里搜索 PDF ，然后将 提取 PDF 文本拖入到右侧的编辑区。然后我们可以选择输出的设置，例如是纯文本或者多信息文本，是否添加页眉或者页脚。如果希望根据 PDF 文稿内容询问操作，可以在动作框下面的选项处选择「工作流程运行时显示此操作」。选择后，每次提取文本时，系统都会询问此次提取的相关设置要求。最后以应用程序格式，保存这个工作流。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/EE4F502A-B139-49D2-B983-4342A4301452.jpg)

将一个 PDF 文档拖到这个程序上，就可以运行这个工作流程。如果在设置时选择了「工作流程运行时显示此操作」，Automator 就会弹出一个对话框让我们选择；否则就会按照设定好的要求自动输出。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/229E708F-3DEF-4409-96E9-41C278022421.jpg)

从输出的质量上看，效果还是很不错的。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/0FB9E9F5-2BC0-4D57-8648-0C24E130CF4A.jpg)

#### 3.批量重命名一组照片

对于喜欢摄影的人来说，把一大堆片子按日期和拍摄地点分类是一件极其痛苦的事情，索性就让它乱着。其实，借助 Automator 创建一个批量命名的工作流，就可以解决问题。

在 Automator 中新建一个文稿，选择「应用程序」，在左侧的资源库搜索「获得文件夹内容」，将它拖到右侧编辑区，然后搜索「给 Finder 项目重新命名」，同样的拖到右边。这时系统会问是否要对所变更项目做拷贝，这里可以根据需要自行选择，我这里选择的是否。

首先给照片设置一个连续的编号，在上面的动作选项卡选择「连续编号」，然后按照我的偏好设置成我想要的文件命名方法。然后，我们在拉一个「给 Finder 项目重新命名」到右侧的编辑区，选择「添加日期或时间」，继续根据个人喜好设置相关操作。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/3E04DC63-CEDE-41F1-A0DC-DFAEDD2E600D.jpg)

设置完成后，保存，这时会生成一个应用程序，我们把拍的照片拷贝到电脑的任意一个文件夹，然后把这个文件夹拖到这个应用程序上，眨眼之间，照片的命名就完成了。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/2057AC6F-1F6A-4C1F-BF28-19AE80E0F2B1.jpg)

### 4.将 WAV 文件自动转码为 Apple Lossless 并添加到 iTunes

这是一个适合我个人需求的动作流程。我习惯在网易云下载了无损音乐之后，将它转换成 Apple Lossless 放进 iTunes 里听。以前的操作是用 Permute 2 转换成 WAV之后，拖进 iTunes 里，转换并编辑歌曲信息。但是用了 Automator 之后，后面繁杂的步骤就都被省去了。

在 Automator 里，新建一个「文件夹操作」，然后依次将「导入音频文件」、「将文件导入到 iTunes 中」、「设置 iTunes 歌曲的信息」拖到右边的编辑区，之后设定好转换和添加的要求，保存并且运行就可以了。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/D92260D6-AF70-4028-A90B-67690996E066.jpg)

将下载文件夹添加到文件夹操作的目标文件夹，然后设定好 Permute 2 转换 WAV 音频的输出目录到下载即可。只要我将 flac 、ape 等文件用 Permute 2 转换好 WAV 之后，便会自动转换成 Apple Lossless 并添加到 iTunes ，然后弹出一个对话框让我输入相关的歌曲信息。唯一遗憾的一点是，不能在这个对话框里添加歌曲的专辑封面。

![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/60128744-D9C3-402F-BC96-FE99B615EC36.jpg)

总结
--

尽管它是 macOS 里自带的应用，但却被放在了 Launchpad 的「其他」文件夹里，因而导致使用它的人并不多。但这并不影响 Automator 成为一个强大的自动化工具。它可以帮助我们把日常的一些操作变成一个自动化的流程，大大的节省时间并且提高效率。不仅如此，我们还可以用它来进行批处理、运行 AppleScript 、运行 Xshell ，甚至录制动作等等。

最重要的一点是，Automator 不需要我们有高超的编程基础，仅仅靠拖动、选择点按等可视化的操作，就能创建强大的自动化流程。如同 iOS 设备上的 Workflow 一样，简单而优雅。当然，想要往更高阶的玩法走，还是需要学习一些编程语言的。

以上便是 Automator 的简单介绍和用法，适合新手和不懂编程的人。有兴趣的筒子和大神们，可以继续深究。

文章来源 [少数派](http://sspai.com) ，原作者 [JohnHarrod](http://sspai.com/author/723742) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/CABB92C1-DB36-40B6-8313-7A6E0DCE30BD/1391B848-169D-4675-91AF-56E7CDE03A59.jpg)](http://sspai.com/36650)

---

[🌐 原始链接](http://sspai.com/36667)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5f1f0261-0da8-4d1b-8ec4-0e2ebd88a84b/5f1f0261-0da8-4d1b-8ec4-0e2ebd88a84b/)
