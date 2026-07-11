# 菜单栏上的任意功能，你都可以用 LaunchBar 来控制 | LaunchBar 实验室

---

菜单栏上的任意功能，你都可以用 LaunchBar 来控制 | LaunchBar 实验室
=============================================

2017年05月26日

[![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/F4D1DAA0-C6A0-4B1A-9D41-6BCF4656DA1A)](https://sspai.com/user/714085)

#### [契丹神童](https://sspai.com/user/714085)

目录

我经常需要录制电脑屏幕。对此我习惯使用系统自带的 QuickTime Player。操作流程是：打开 QuickTime Player，选择菜单栏上的**文件**，再选择**新建屏幕录制**，就会出现一个**屏幕录制**窗口，再按下红色按钮或者空格键则录屏就绪：

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/14EBCC14-8610-4299-A388-21D021C5E9E6)

可是如果频繁进行这项操作时，反复的选择总会让人有点不耐烦。如果可以做一个叫作「屏幕录制」的工作流，让上面的这一串动作（「启动 QuickTime Player →选择**文件** →选择**新建屏幕录制**→等待**屏幕录制**窗口启动→按空格键」）自动进行，那我们只需要选择并启动这个「屏幕录制」，系统就可以帮我们进行后续操作，从而直接进入录屏就绪状态。

这样的工作流可以轻松实现吗？当然可以。

我们可以借助 AppleScript 实现这个需求。AppleScript 是苹果公司开发的脚本语言，和 Automator 共同作为 macOS 系统下的两大自动化作业流程工具，可以轻松简化很多平时常常出现的各种机械而繁琐的操作流程。大家不必看到「脚本」二字就皱起眉头，以为这是给程序员准备的工具。AppleScript 语法简单，极为接近人类语言，只要略懂英文，就可以轻松读懂它，并快速上手。因此，它面向的是全体 macOS 用户。

建立 AppleScript 脚本
-----------------

首先我们启动系统自带的 Script Editor 程序，新建文件，将下述代码粘贴进去，重要语句的上方都用注释进行了说明：

```
activate application "QuickTime Player"
tell application "System Events"
    tell process "QuickTime Player"
        set frontmost to true
        # 选择菜单栏上的文件「菜单」中的「新建屏幕录制」
        click menu item "新建屏幕录制" of menu "文件" of menu bar 1
        # 等待「屏幕录制」窗口出现
        repeat until exists window "屏幕录制"
        end repeat
        # 按下空格键
        tell application "System Events" to keystroke " "
    end tell
end tell
```

之后点击上面工具栏的第三个图标**运行脚本**：

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/97053483-0AFA-4FCE-A7B9-348DDB98C9A0)

上述流程就自动实现，直接进入录屏就绪状态了。

在上面的 AppleScript 代码中，最关键的步骤是  
`click menu item "新建屏幕录制" of menu "文件" of menu bar 1`  
以及  
`repeat until exists window "屏幕录制"`  
这两行。这里出现的菜单名和窗口名称要和程序中的相应文字完全一致。

即，如果你的系统是英文，需要调用的菜单名和窗口名称如下：

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/B79A74FE-60A0-4FC5-9F01-54F0EDCA8018)

则这两句就应写为：

`click menu item "New Screen Recording" of menu "File" of menu bar 1`

`repeat until exists window "Screen Recording"`

我们把这个文件保存，命名为「Record Screen with QuickTime Player」。之后也可以把它导出成一个程序，选择菜单栏上的**文件** →**导出…** ，出现的的对话框中的**文件格式**一项选为「应用程序」，即把这个脚本打包成一个程序了：

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/C40CB946-19A0-4BCB-A990-E3CBD7E3AA0D)

我们双击这个程序即可以运行。如果弹出安全提示，按提示即可完成安全授权。

与 LaunchBar 结合
--------------

如果我们再把上述脚本和 [LaunchBar](https://sspai.com/search/article?q=launchbar) 结合，做成一个 action，则可以更加高效更加优雅地实现录屏过程。

启动 Action Editor。新建动作，命名为「Record Screen with QuickTime Player」。在 **Scripts** 页面选择其使用的脚本语言为「AppleScript」，点击其右边的 **Edit** 按钮，启动 Script Editor，在其中粘贴上述代码，保存并退出。

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/9DCE1A45-9CAC-46C1-BAA3-AE3BCB338708)

下载一个自己中意的录屏图标，在 **Resources** 页面把这个图片文件添加进去：

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/14929F63-361A-454E-8DE6-100131D7CF02)

再在 **General** 页面在 **Action Icon** 填入刚才保存在 **Resources** 中的文件的名称，这个 action 就完成了。

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/3A93062C-99B7-416E-A731-EC0D9EB896E8)

在 LaunchBar 中输入 `REC`，选择 **Record Screen with QuickTime Player**，就可以直接开始屏幕的录制了。

补充：二级及多级菜单的选择
-------------

上面的 AppleScript 脚本中涉及到的只是菜单栏上的一级菜单的选择，如果想要选择二级或多级的菜单需要如何写呢？

例如，在 Safari 中，想要把当前网页通过微信分享，需要选择**文件**→**共享**→**发送到微信**：

![](.evernote-content/924223E3-937E-4C22-8ACD-B3498BBCA647/714543CF-40DA-40CB-A179-418F62E7E57F)

把这串动作写成 AppleScript，则为：

```
tell application "System Events"
    tell process "Safari"
        set frontmost to true
        # 选择 文件→共享→发送到微信
        click menu item "发送到微信" of menu of menu item "共享" of menu "文件" of menu bar 1
    end tell
end tell
```

最后
--

把 LaunchBar 和 AppleScript 结合起来，可以灵活运用在其它任意窗口应用里，操作菜单栏。针对其它各种动作或功能，都可以在网上找到大量的实例。大家可以举一反三，简化自己日常生活中经常出现的类似场景。

（*题图背景选自 [Biel Morro 的摄影作品](https://unsplash.com/photos/kcKiBcDTJt4?utm_source=Irvue&utm_medium=referral&utm_campaign=api-credit)。*）

---

[🌐 原始链接](https://sspai.com/post/39282)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4d0d6ea2-f7c6-4687-9365-2b5a664c3812/4d0d6ea2-f7c6-4687-9365-2b5a664c3812/)