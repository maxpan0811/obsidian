# 让你在 Windows 上也能实现高效操作：AutoHotkey

---

作为 Windows 上的一款自动化工具，AutoHotkey 常常是被用来管理快捷键的。AutoHotkey 是一种 Windows 上的脚本语言。你可以通过 **编写脚本** 来实现你想要的功能，同时提高操作 Windows 的效率。

相信不少朋友对于 AutoHotkey 还不是很了解，什么是 AutoHotkey？

> AutoHotkey 是面向普通电脑用户的自由开源的自动化软件工具，它让用户能够快捷或自动执行重复性任务。——中文维基百科

可是由于 AutoHotkey 没有 Automater 那样可视化流程的操作，普通用户根本不知道 AutoHotkey 是如何开始的，更加无法深入学习编程。其实，只要稍微了解一下 AutoHotkey 的功能定位，你也就可以用它在 Windows 上实现高效操作。

你可以先在 [AutoHotkey 官网](https://www.autohotkey.com/) 下载安装后继续阅读。

用 AHK 自定义快捷键
------------

AutoHotkey 的功能很丰富，能够实现轻松打开 Windows 上的程序、网页、文档、文件夹、窗口，更支持调用到 Windows 系统级别的 API 来实现某些功能。但是，对于普通用户来说，设置热键实现快速启动，才是最简单方便地使用 AutoHotkey 的方法，我们就先从快捷键开始讲起。

使用快捷键能让你 **在操作电脑时变得简便快捷，手指不需要再在键盘和鼠标之间切换**。例如，当你在浏览器里想要新建一个窗口时，不需要再点击 + 号，只需要按下 Ctrl+N 就能实现；再比如切换程序窗口，只要按下 Alt+Tab。

![](.evernote-content/61177597-7AB5-4369-B55A-684F5ED23A1B/76A758E2-0A90-4083-ADAA-C5B4E722DF6F.gif)

软件自带的快捷键

除了使用系统和程序里预设好的快捷键外，我们也可以 **自定义快捷键和组合快捷键**。这时候，就要用 AutoHotkey 来编写脚本帮助我们快速地实现。通过它编写的快捷键设置脚本，能够替换掉 Windows 的默认快捷键，因此我们仅需要一个 AHK 脚本就能很方便的管理电脑上的所有快捷键。

### 编写代码，自定义快捷键

设置快捷键很容易，在编辑脚本里输入几行命令即可。你可以试试把下面这几段代码复制进记事本，然后保存为 .AHK 格式。打开后按下快捷键，试试看效果。

Win+S，打开少数派首页——

```
#s::Run https://sspai.com ;win+s 打开少数派网站
```

Win+G，运行 CMD——

```
#g:: ;win+g 运行CMD              
Run Cmd.exe
Return
```

Win+1，将剪切板上的内容粘贴到 Notepad 并保存——

```
#1:: ;win+1 将剪切板上的内容粘贴到 Notepad 并保存
IfWinExist, Untitled - Notepad
{
WinActive
}
else
{
Run,  Notepad
WinWait, Untitled - Notepad
WinActive
}
sleep, 500
send, {enter}{enter}^v
return
```

可以看到，在 AutoHotkey 中设置热键要用到的语法很简单，跟 Javascript 一样很好理解。

效果展示：

![](.evernote-content/61177597-7AB5-4369-B55A-684F5ED23A1B/7E68BB77-36A8-4763-ACE6-D6628F7B9439.gif)

快速打开少数派官网

### 怎样合理设置快捷键

设置快捷键的步骤并不复杂，令人头疼的点反而是快捷键太多、不方便记忆、使用频率降低。我建议是，**不要设置很多的快捷键，将常用的快捷键写在 AHK 脚本内就好**。

原则上，**快捷键用的键位的选择也要方便记忆**，比如上面我设置的「打开少数派的网站」这一快捷键组合是 Win+s，s又是少数派的首字母，所以就可以将快捷键要实现的功能和键位联想记忆。

这时候，还可以用到一个 [Show your key-presses on screen](https://github.com/TaranVH/2nd-keyboard/blob/master/Taran%27s%20Windows%20Mods/KEYSTROKE%20VIZ.ahk) 的 AHK 脚本，轻松帮助你回忆起快捷键内容。

### 更多快捷键相关功能

AutoHotkey 不仅支持把单键、组合键设置为热键，还 **支持把鼠标、游戏杆按钮等外设设为热键**。

如果你有外接机械键盘，就可以用它来 **修改键位**。例如，把多余的 Fn 键设置为特殊的快捷键来使用。如果需要避开常用的 Fn 键，键盘上还有多余的键位，那就可以设置为一些特殊的功能。如果在使用 PR 剪辑视频时，有 F13 可以用作渲染导出的组合快捷键，剪辑的效率能得到大大地提高。

用 AHK 自定义文本替换
-------------

少数派上有一篇 @Yigang 写的有关 [Windows 下的文本替换](https://sspai.com/post/39737)的文章，他就是利用 AutoHotkey 的热字符串来实现文本替换的功能。文本替换的确很方便，将缩写替换为全写，所以在聊天使用输入法时，能够快捷地输入一些常用的词语、地址、邮箱、号码。

格式类似于下面这种形式——

```
::sspai::少数派
```

```
::ahk::AutoHotkey
```

同样的，利用热字符串，也可以用在编辑文稿或者编写代码时，用来查找并替换某些特殊的字符。我在 Github 上搜索 AHK 时发现了有很多相似的实现脚本，比如这个[写 PHP 用的常规文本替换脚本](https://github.com/hanshou101/AHK-Scripts/blob/master/sss%24.ahk)。

![](.evernote-content/61177597-7AB5-4369-B55A-684F5ED23A1B/3A8D9777-2003-4CF6-97D6-DC6AFC90BECB.png)

PHP&AHK

用 AHK 实现「按键精灵」的功能
-----------------

用 AutoHotkey 发送键击几乎可以自动化全部的操作。是不是可以实现跟「按键精灵」相似的功能？可以，而且要比「按键精灵」强大许多。比如说，玩 MOBA 游戏都是需要很多次的鼠标点击，如果用 AutoHotkey 辅助，再也不用怕自己「手残」不能打游戏了。

所谓的「按键精灵」本质上就是不断的循环，程序在做这样的事情要比人有效率。抢购的经历总是让人难忘，你是不是还在为点破鼠标还没抢到而气愤？

```
#1:: ;循环点击示例
loop, 10
{
click
sleep 200
}
return
```

这个动作中每次按下 Win+1，就可以每隔 0.2 秒单击一次鼠标，反复点击十次。实现自动键击。不必要浪费太多的力气，就能「刷到」想要的东西。

![](.evernote-content/61177597-7AB5-4369-B55A-684F5ED23A1B/0DA01D9A-704D-4451-998F-B51824A5F98E.gif)

相当于双击 5 次

AHK 还能做这些事

此外，Windows 系统管理相关的工作，AutoHotkey 也能够处理。最简单的有「查看系统信息」「查看网络连接状态」「监控后台运行的程序」「防止屏幕变暗」等等，在此就不一一列举，如果感兴趣可以自行查找。

有趣的是，我在查找 AutoHotkey Script 的过程里，发现不少小工具。它们没有特别复杂的功能，往往只是解决一个需求。比如，这个 [QQ.ahk](https://github.com/health901/AHK/blob/master/QQ.ahk) 就是禁止其他 QQ 号使用 QQ 软件。还有生成随机字符串、加时间戳、图片转换、翻译这些，俨然是一个个「小」程序。

的确，AutoHotkey 体积小，运行起来又特别轻量，比起其他的程序，我也更愿意用 AutoHotkey 造一些实用小工具。最近吃鸡游戏大火，就有人用 AutoHotkey 专门写了[绝地求生按键脚本](https://github.com/fuckpubg/AHK)，以此提升自己的游戏体验（并不属于外挂的范畴）。

如果你对它感兴趣，可以在这些地方学习更多相关知识。

* [AutoHotkey 官网](https://www.autohotkey.com/)
* [AutoHotkey 中文文档](https://wyagd001.github.io/zh-cn/docs/AutoHotkey.htm)

总结
--

AutoHotkey 确实是 Windows 上强大的自动化软件工具，它能够很好地实现 **热键、热字符串、文本替换，也能模拟鼠标、游戏杆的点击和监控调整系统状态** 等功能。

但是术业有专攻，除了以上这些，要想在 Windows 实现其他更加复杂的工作，AutoHotkey 就不如 Python 这种脚本语言。所以，作为普通用户，你在使用 AutoHotkey 的过程里，对「自动化」有了新的想法才是最有价值的。

每个人都应该打造属于自己的工作流。现在我再使用 AutoHotkey 就不光光管理 Windows 下的快捷键，而是结合我要在电脑上写稿、剪辑视频、上网页的工作流，把其中的某些步骤进行自动化，让工作流变得更加流畅快捷。比如说，在使用 PR 剪辑时就运行 pr.ahk，里面包含了一系列的快捷键和组合快捷键，还能实现批量处理。

要知道，说起自动化软件，人们总是会说 iOS 有 workflow，MacOS 上有 Automater，那 Windows 上会有这样的软件吗？

AutoHotkey 就是这样一款能够在 Windows 上实现自动化的软件。

---

[🌐 原始链接](http://sspai.com/post/43305)

[📎 在印象笔记中打开](evernote:///view/207087/s1/cfa2ec65-5ee5-404c-bcb4-09396339b3b2/cfa2ec65-5ee5-404c-bcb4-09396339b3b2/)