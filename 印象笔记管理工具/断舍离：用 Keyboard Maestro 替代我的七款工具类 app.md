# 断舍离：用 Keyboard Maestro 替代我的七款工具类 app

---

断舍离：用 Keyboard Maestro 替代我的七款工具类 app
====================================

### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

macOS 是个优秀的桌面操作系统，但作为生产力工具而言，却依然有着这样那样的短板。这里的「短板」倒不是说 macOS 系统有缺陷，而是它简洁的面貌下，反而提供了一个广阔的「可能性」—— 我们可以通过工具来对系统功能进行增强，从而定制出完全属于自己的一整套操作习惯。就像是劳动人民掌握了工具一样，生产效率自然也会大大提高。

而在这之中，能称得上「神器」的系统增强工具不多，但 Keyboard Maestro 绝对是顶得上这个名号的。为什么这么说呢？

关联阅读：[Keyboard Maestro 入门指南](https://www.sspai.com/post/36442)

第一点是它真的强大到让你难以想象。你所想要的许多扩展性功能，都可以通过它来自定义；其次就是它很轻量化，只有 24.4MB 的初始体积，完美诠释了什么叫「浓缩就是精华」；第三点，也是最重要的一点：它还能给你省不少钱。

没错，一个售价高达 36 美元（人民币付款为 267.89 元）的软件，还能给你省钱。因为一个 Keyboard Maestro 能做的可不是简单地改改键位，或者做一些复杂的流程的自动化，它更可以替代多款收费的效率 / 工具软件，一个顶几个。

改键工具（如 Karabiner）
-----------------

Karabiner 是一款在 macOS 上进行键盘映射的工具。而有了 Keyboard Maestro 之后，我们就可以通过 Macro 来对键盘进行映射和更改，实现和 Magic Keyboard 完全一样甚至是超越原生键盘的第三方键盘体验。

关联阅读：[让键盘变成你想要的样子：改键利器 Karabiner-Elements](https://www.sspai.com/post/42921)

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/48C13E0E-24E9-4C5F-96CE-03C0870B7C51.png)

例如，我目前就将自己的 IKBC DC108 机械键盘的键位改成了下面这样：

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/85C88D55-A214-4818-B04F-347639DE2847.png)

修改方法也很简单。创建一个「hot key」为触发项的 Marco，然后在 Actions 中找到「Simulate Hardware Key」拖到右侧的「No Action」中，并在下面选择你想要映射的按键即可。

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/96254242-4471-45E0-8921-F68C0AC968C4.png)

窗口管理工具（如 Mosaic / Magnet / Moom）
--------------------------------

众所周知，macOS 的窗口管理功能一直都不尽如人意，因而诞生了大量的窗口排列软件，如 Mosaic / Magnet / Moom 这些。但实际上，Keyboard Maestro 同样提供了一套窗口管理的 Action，而且还可以精确到屏幕像素的级别。

关联阅读：[为什么 Mosaic 是窗口管理的理想选择](https://www.sspai.com/post/45457)

在 Keyboard Maestro 中，你可以通过一个简单的 Marcos 来实现窗口管理。它默认提供了左右分屏、上下分屏、最大化、全屏和四角分屏，基本能涵盖绝大部分的需求。

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/F03543EE-20C2-42A6-B8E3-1AAB2EDBE8A6.png)

如果你觉得这些还不能够满足，你也可以通过「SCREEN / SCREENVISIBLE」函数来对窗口进行精确的缩放和移动控制。

**具体的教程可以戳这里：[用 Keyboard Maestro 实现窗口排列管理](https://www.sspai.com/post/55908)**

音频切换工具（如 AudioSwitcher）
-----------------------

如果你像我一样，有多个音频播放设备，那么如何进行音频切换就是一个麻烦事。好在现在 macOS 已经可以实现点击右上角的音量按钮来选择音频输出设备，不像以前一样还要按住 option 键。但不管怎样，这些操作都显得不够「优雅」。试想，只要你在键盘上按下一个按键，音频播放设备就会自动切换，原本在扬声器播放的音乐立刻就变成了从耳机输出，是不是很爽？

App Store 中，有一款叫售价 6 元的 AudioSwitcher app 虽然可以实现这个功能，但它的操作方式并不友好，还偶尔有失灵的问题。而且它还有一个最大的问题，就是它还会创建一个难以删除的音频输出选项，令强迫症无法忍受……

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/DD0248FD-49E9-4740-8B1E-8B7179418122.png)

而 Keyboard Maestro 的实现方式则要有效且优雅许多。借助 Keyboard Maestro 中的「Execute an AppleScript」，它便可以让你在触发某项条件时快速运行一个 AppleScript 脚本，从而达到目的。

首先，我们需要设置一个以快捷键为触发选项的 Macro，并在 Action 中拖入「Execute an AppleScript」，然后复制以下的音频输出切换脚本（记得删除代码里的「-- XXXX」注释文字）：

```
tell application "System Events" to tell process "SystemUIServer"

    tell (menu bar item 1 of menu bar 1 whose description contains "volume")

        click

        set target to "LG HDR 4K" -- 修改为要切换设备的名称

        set alternative to "MacBook Pro 扬声器" -- 修改为要切换设备的名称

        set retry to 1 -- 重试次数，可为 0

        set interval to 1 -- 重试间隔（秒），可为小数

        if exists (menu item 1 of menu 1 whose title is target and value of attribute "AXMenuItemMarkChar" is "✓") then

            set target to alternative

        end if

        repeat with counter from 0 to retry

            try

                click (menu item target of menu 1)

                exit repeat

            end try

            if counter < retry then

                delay (interval)

            else

                key code 53

            end if

        end repeat

    end tell

end tell
```

设置完成后，当你按下对应的按键，就可以立刻切换到另一个音频输出设备上进行播放了。

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/199AD229-5CBE-4E49-BD6F-64A8A112C6C0.png)

插个故事：一键切换音频的这个想法是在看到了王自如的 Office Tour 之后诞生的，大概是 2016 年初。当时用了 Automator（俗称「扛炮机器人」）+ Karabiner 来实现，还在 Zealer+ 论坛写了一篇很长的文章，但是后来 Zealer+ 关闭了，文章也找不回来了。现在的这个脚本是我派作者 JayQi 所写，实现的方式和数量都比我初改的要好，因此要特别感谢一下他。

在这里我也放上 JayQi 这篇文章的「传送门」：[Mac 连了多个音箱耳机想快速切换？这里有个 Geek 一点的方法](https://www.sspai.com/post/42281)

防误退出工具（如 SlowQuitApps）
----------------------

误触 Command + Q，确实是一件让人头大的事情。比如当你想要用 Command + W 关闭一个 Safari 窗口时，一不小心手抖按到了旁边的 Q，就把所有窗口都给关掉了，这种体验真的是很难受……

而且，「手抖党」似乎也不是只有我一个人，看来大家都对 Command + Q 这个按键感到了无奈，不然就不会有这么多防止误按 Command + Q 的 app 出现了吧……

关联阅读：[告别误触，防止「手抖」退出 macOS 应用：SlowQuitApps](https://www.sspai.com/post/44687)

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/C073A434-5931-42B9-BD8F-9F00FC8A936B.png)

不过有了 Keyboard Maestro，这些 app 你统统都不需要了。不仅如此，你还可以根据自己的需求，设置哪个 app 需要退出确认，哪一些则可以直接退出。

这里需要使用的就是 Keyboard Maestro 里的「IF」条件判断。创建一个叫「防手抖」的 Macro，在上面的「New Trigger」中选择「Hot Key Trigger」，并将快捷键设为 Command + Q。

然后，拖一个「If Then Else」的 Action 到右边，在下面的「New Condition」中选择「Application Condition」。接着，选择需要退出提醒的 app，并按照下图所示，在下方加入一个 Alert 给予提示，然后再在下面用「Type a Keystroke」Action 来模拟按下 Command + Q。

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/CB1FE84A-9953-4F79-B2B5-C5DD29B859F7.png)

这样一来，在你按下 Command + Q 之后，Keyboard Maestro 就会运行一次「防手抖」，如果是你选中的 app，就会提醒你确认之后再退出，而不需要确认的则会正常立刻退出。

应用切换工具（如 Manico）
----------------

macOS 也提供了一种类似 Windows 的 app 切换快捷键：Command + Tab。但是一旦 app 开启的数量较多，切换起来就变得异常麻烦，需要不停地按 Tab，不仅繁琐，效率也大打折扣。而 Manico 这类软件就是为了解决这个问题诞生的。它不仅可以快速地在打开的 app 间进行切换，如果你没有打开对应的应用，Manico 还可以帮你打开。

关联阅读：[简洁、高效、易用，Mac App 快速启动及切换工具：Manico 2.0](https://www.sspai.com/post/32457)

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/4AA034FB-957B-42C5-8E73-F4AD92F00F14.png)

不过，有了 Keyboard Maestro 之后，Manico 大概率就要失业了…… 除了有个好看的界面之外，前者在功能上基本可以替代后者。

创建一个 Marco，选择触发行为为「Hot Key Trigger」，然后输入你想要启动对应 app 的快捷键，接着在左边找到「Activate a Specific Application」并拖到右边进行设置，在「Activate」旁选择你需要切换到前台的 app，并勾选下面的两个选项，就可以通过指定的快捷键快速切换窗口。

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/ED48E722-A343-4407-8E02-BB88F604DDAD.png)

剪贴板工具（如 Paste）
--------------

Paste 是一款 macOS 上颜值相当高的剪贴板软件，但它对空间的占用却「令人发指」。其实和上面一样，Keyboard Maestro 也有一套剪贴板记录工具，除了没 Paste 好看之外，其他啥都不差。

关联阅读：[你其实需要一款 Mac 剪贴板工具，而且就是这个：Paste](https://www.sspai.com/post/31570)

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/90B370C9-2DA5-4319-BCF9-4A6F83B35A04.png)

这里的设置相当简单，只需要创建一个 Marco 并设定快捷键，然后在 Action 中选择「Activate Clipboard History Switcher」即可。用法和 Paste 类似，复制时自动记录，双击即可粘贴。

![](.evernote-content/90D6AB8B-6913-431E-A283-0F73861E6F5B/34ABE9D5-2EC3-4A5E-8988-119AB1E6524F.png)

OCR 工具（如 iText）
---------------

是的…… 你没看错，Keyboard Maestro 甚至还能替代 iText 进行 OCR 文字识别。当然了，识别的工作它干不了，但通过调用百度的 OCR API，便可以让 Keyboard Maestro 获得此等「神功」。

关联阅读：[有了 iText：你截图，腾讯 OCR 帮你识别文字](https://www.sspai.com/post/42059)

而且对比与 iText 免费版只有每月 20 次的限制，Keyboard Maestro + 百度 OCR API 每天可以免费调用 5 万次……

具体的操作方式和过程这里就不多在复述，大家可以按照 [这篇文章](https://zhuanlan.zhihu.com/p/60286600)，相信也能理解。不过要运行这个 Marco，需要两个前提条件：一是需要安装 Python 3，二是要注册百度云的 API。好在这两个并不麻烦，而且教程也写得很详细。

结语
--

其实，借助 AppleScript 和 Shell Script，Keyboard Maestro 可以替代的可不仅仅只是上面这些 app。例如使用 exiftool 或 mogrify 就可以做成一个一件清除照片 exif 的工具，干掉 Photo Zapper 这一类的 app。但限于篇幅长度，这里就不再举例，可以爬一爬 Keyboard Maestro Wiki 和对应的命令 Wiki 自己鼓捣。

总之，270 元的 Keyboard Maestro，给你换来的是无尽的想象力，毕竟「Maestro」这个名字可不是白叫的。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让你的工作更有效率 ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/56142)

[📎 在印象笔记中打开](evernote:///view/207087/s1/dea89db1-d964-4f20-9f83-16f903a1808b/dea89db1-d964-4f20-9f83-16f903a1808b/)