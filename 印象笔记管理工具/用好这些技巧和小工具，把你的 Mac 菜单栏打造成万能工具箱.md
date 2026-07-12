# 用好这些技巧和小工具，把你的 Mac 菜单栏打造成万能工具箱

---

macOS 上有一个兵家必争之地，那就是菜单栏。我们经常会发现，一个应用

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/3E8FC342-08C9-4732-83FB-D99C3E3FF10C.gif)刚启动，就在菜单栏里给自己占了一个位置。的确，菜单栏可以随时呼出，用来显示系统状态、放置一些常用小工具再方便不过。

但是你有没有想过，我们可以自己定义菜单栏、把它变得更趁手？我们总结了一些菜单栏整理的技巧，还收集了一批优秀的菜单栏小工具，希望能和你一起把菜单栏打造成随叫随到的工具箱。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/D696F630-AF12-4DB0-96AA-A86EFBED231A.gif)更多技巧，还可以关注专题 [「把 Mac 菜单栏变成万能工具箱」](https://sspai.com/topic/191)。

这些工具值得放在菜单栏上
------------

所谓巧妇难为无米之炊，要充分发挥菜单栏的功能，我们需要用更多的 App 来武装这一方小天地。

### 隐藏多余图标，就用这两个工具

挑选喜欢的菜单栏工具前，我们不妨先准备几个整理工具，不然你的菜单栏可是很容易就被图标挤满的。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/3BA498FA-CE90-4164-A453-DAA963BE4247.png)被挤满的菜单栏

[Bartender 3](https://www.macbartender.com/) 是名气最大的菜单栏工具之一，它可以把不常用的菜单栏图标「折叠」起来，要用的时候再展开，可以为你腾出不少的空间。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/D696F630-AF12-4DB0-96AA-A86EFBED231A.gif)Bartender 3

不过，Bartender 3 是一个付费工具，如果你暂时不想花钱，可以试试另一个工具 [Vanilla](http://matthewpalmer.net/vanilla/)，核心的收纳功能它也可以事先。但是想要自动隐藏、开机启动等高级功能，还是要升级到专业版。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/1D442B41-3B17-46B9-965F-BCEE664FB743.gif)Vanilla

### 随取随用，就用这些工具

菜单栏其实是一个很好的「公告栏」，在全屏模式下也能查看。我们可以把常用的信息放在这个区域，便于随时检查。

除了看时间，大家最常看的恐怕就是日历了，知名工具 Fantastical 就提供了菜单栏插件，但是为了这个功能而买 Fantastical 似乎不是很划算。如果你需要替代品，可以考虑一下免费的 [Itsycal](https://www.mowglii.com/itsycal/)。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/DED99AD4-E5DA-43C8-BFF1-7E94605061C6.jpg)Itsycal 界面，图片来自 vanilla2w 的文章

> 延伸阅读：[Fantastical 太贵了？试试免费的菜单栏日历工具：Itsycal](https://sspai.com/post/42848)

想随时提醒自己的话，你还可以把便笺和待办清单放进菜单栏，定价任性的 [Thought Train](https://www.thoughttrain.cc/?ref=producthunt)——想付多少就付多少——是个不错的选择。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/3E8FC342-08C9-4732-83FB-D99C3E3FF10C.gif)随手添加待办事项

除了上面的小工具，在我派的一场 [群分享](https://sspai.com/post/41470) 中，派友们还分享了更多好用的菜单栏小工具，读者们可以再去淘一淘宝。

> 延伸阅读：[哪些 macOS 菜单栏小工具很实用？看看少数派作者们的推荐 | 群分享](https://sspai.com/post/41470)

延伸阅读：

* [不仅要能藏，还要藏得优雅，Mac 菜单栏简化工具 Bartender 3 更新](https://sspai.com/post/40832)
* [Vanilla，精简 Mac 菜单栏应用图标，小巧轻量还免费丨App+1](https://sspai.com/post/39036)

用 LaunchBar 控制菜单栏
-----------------

菜单栏里面图标、功能太多，要用的时候慢吞吞地把光标移过去实在不方便。如果你用的还是 iMac 或者外接显示器，相信你的体会一定更深刻……如果你是一个效率控，这种体验想必难以忍受的，那么可以试试 [LaunchBar](https://www.obdev.at/products/launchbar/index.html) 这个第三方工具。

在 macOS 中，几乎所有菜单栏功能都可以通过系统自带的 AppleScript 脚本语言来控制，而 LaunchBar 就可以把这些脚本打包起来，快速取用。虽说写脚本也是一种高级玩法，但 AppleScript 足够简单，不信的话，拿一个快速开启 QuickTime 录屏功能的例子，你自己感受一下：

activate application "QuickTime Player"

# 叫醒 QuickTime

tell application "System Events"

# 让系统起来干活

tell process "QuickTime Player"

# 让系统去监督 QuickTime

set frontmost to true

click menu item "新建屏幕录制" of menu "文件" of menu bar 1

# 点击「菜单栏 - 文件 - 新建屏幕录制」

repeat until exists window "屏幕录制"

# 等待「屏幕录制」窗口出现

end repeat

tell application "System Events" to keystroke " "

# 按一下空格键开始录制

end tell

end tell

这一串脚本其实是很直白的指令，派系统去干活、完成一套点击操作。接下来把它们打包进 LaunchBar，就可以快速启用菜单栏中的「新建屏幕录制」功能了。

![](.evernote-content/7E58C91D-EBF5-40DD-8FAA-C896A6E5FE79/6E49875A-967E-44F5-8285-336D02E4E675.png)控制菜单栏里的功能，图片来自 契丹神童 的文章

> 延伸阅读：[菜单栏上的任意功能，你都可以用 LaunchBar 来控制 | LaunchBar 实验室](https://sspai.com/post/39282)。

macOS 的菜单栏还有更多使用技巧，我们也能找到更多好用的第三方小工具。想继续强化你的 Mac 菜单栏，欢迎关注少数派的专题 [把 Mac 菜单栏变成万能工具箱](https://sspai.com/topic/191)。

---

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用 ⚡️

---

[🌐 原始链接](http://sspai.com/post/44692)

[📎 在印象笔记中打开](evernote:///view/207087/s1/91e28958-cd3a-42fc-938a-248774201ea1/91e28958-cd3a-42fc-938a-248774201ea1/)