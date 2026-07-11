# 免费又强大的 macOS 自动化工具，Hammerspoon 可以让你少买很多 App

---

免费又强大的 macOS 自动化工具，Hammerspoon 可以让你少买很多 App
===========================================

1 天前

[![](.evernote-content/74D1545B-5463-40EB-98D7-87510E292EB8/AE3271B4-7253-4F7F-AB9F-C90E9BE317BE)](https://sspai.com/user/742287/updates) 

#### [涔 C](https://sspai.com/user/742287/updates)

macOS 系统最令人难以割舍的特性之一就是丰富的自动化工具支撑：内置的 AppleScript 与 Automator，还有第三方软件 Keyboard Maestro、Hazel、Alfred、LaunchBar 等。这些工具不仅仅为我们免除了许多无聊的重复工作，节省了精力和时间，也让我们时不时可以体会一些解决问题与创造工具的乐趣。今天，我们来看一款更加强大、好玩的开源软件 [Hammerspoon](https://github.com/Hammerspoon/hammerspoon)。

通过桥接操作系统与 Lua 脚本引擎，这款软件让我们能够用 Lua 脚本快速方便地与系统 API 沟通，获取各种信息或者进行控制，包括但不仅限于这些方面：窗口、键鼠、文件系统、音频、电池、屏幕、剪贴板、地理位置、Wi-Fi 等，基本上涵盖了系统中的各个方面。除此之外，创建菜单栏图标与菜单、绘制图形界面等自然也不在话下。如果这样的说明让你有些不太明白，那我们其实可将它**大致看作 macOS 平台上的 JSBox 或 Pythonista**。

阅读本文需要使用终端与 Git。少数派网站中有丰富的相关入门教程，可搜索访问。

推荐阅读：

* [玩转 Terminal 终端：入门指南及进阶技巧](https://sspai.com/post/45534)
* [Homebrew，Mac 应用管家](https://sspai.com/topic/181)
* [轻松玩转 Mac 命令](https://sspai.com/topic/183)

使用方法
----

Homebrew 用户可以使用 cask 进行安装：`brew cask install hammerspoon`，或者也可以在 [GitHub 项目页面](https://github.com/Hammerspoon/hammerspoon/releases/latest) 手动下载安装。

![](.evernote-content/74D1545B-5463-40EB-98D7-87510E292EB8/73198499-81D9-4C62-97F4-9194C39A357F.png)

偏好设置

首次打开 Hammerspoon 后，偏好设置窗口自动打开，点击上图中 **Enable Accessibility** 授予辅助功能权限。此时的 Hammerspoon 并不具备任何功能，就如同 iOS 上尚未加入任何捷径的捷径 App 一样。我们需要在 `~/.hammerspoon/init.lua` 中加入自己编写的配置脚本，并且点击 Hammerspoon 菜单栏图标并选择 **Reload Config**（重载配置），使配置生效。

推荐配置
----

在动手编写代码之前，我们先来看看其他人是怎么使用 Hammerspoon 的，也可以直接使用他们公布的成熟配置。

### 

### awesome-hammerspoon configuration

下载地址：[ashfinal/awesome-hammerspoon](https://github.com/ashfinal/awesome-hammerspoon)

这份配置实现了这些功能：

* 快捷键窗口管理
* 桌面挂件，包含时钟、日历
* 快捷键列表 Cheatsheet
* Aria2 前端，可以快速添加下载任务，查看当前下载情况
* 快捷搜索，类似于 Alfred，可搜索浏览器标签页、进程、词典、Emoji 等

![](.evernote-content/74D1545B-5463-40EB-98D7-87510E292EB8/4A72C697-8D15-4A90-9E25-1BA8E668B0F2.gif)

图片来自该配置作者介绍

其中窗口管理与常见的快捷键操作类型不同，比较有意思：按下快捷键 `⌥Option + R` 后进入管理模式

* 使用 `h/j/k/l` 移动为上下左右的半屏
* 使用 `y/u/i/o`（即 hjkl 上方按键）移动为左上 / 左下 / 右上 / 右下的四分之一窗口
* 使用 `c` 居中，按下 `=/-` 进行窗口大小缩放
* 使用 `w/s/a/d` 向上下左右移动窗口
* 使用 `H/J/K/L` 向左 / 下增减窗口大小
* 使用方向键 `上下左右` 移动到相应方向上的显示器
* 使用 `/` 撤销、重做上一次操作
* 使用 `q` 或 `Esc` 退出管理

配置使用方法：在终端中运行 `git clone https://github.com/ashfinal/awesome-hammerspoon.git ~/.hammerspoon`，然后**在 Hammerspoon 中重载配置**就可以了。

点击查看中文说明及讨论：

* [写了一份（貌似）不错的 Hammerspoon 的配置 - V2EX](https://www.v2ex.com/t/324303)
* [（自我）感觉良好的 Hammerspoon 配置，有原生 aria2 前端和类似 Alfred 的搜索了 - V2EX](https://neue.v2ex.com/t/358426)

### Hammerspoon config

下载地址：[wangshub/hammerspoon-config](https://github.com/wangshub/hammerspoon-config)

这份配置实现了这些功能：

* 菜单栏显示近日天气，包含未来一周的天气、气温与风向等
* Wi-Fi 自动脚本，通过 Wi-Fi 判断所在位置并做出相应的操作
* 窗口管理，快速切换为二分屏、三分屏
* 蓝牙耳机自动连接等

![](.evernote-content/74D1545B-5463-40EB-98D7-87510E292EB8/1EB5C40D-2383-4024-A03B-7B546FC8CDC5.gif)

图片来自该配置作者介绍

配置使用方法：在终端中运行 `git clone https://github.com/wangshub/hammerspoon-config.git ~/.hammerspoon`，然后重载配置。

点击查看中文说明及谈论：<https://www.v2ex.com/t/553241>

### HammerSpoon config file - by S1ngS1ng

下载地址：[S1ngS1ng/HammerSpoon](https://github.com/S1ngS1ng/HammerSpoon)

这份配置实现了三方面的功能，包括快捷键窗口管理、播放器 VOX 控制以及 Vim 式的光标移动快捷键。其中的窗口管理，除了常规的全屏、居中与分屏，还能够做到这些：

* 用快捷键将当前窗口移动至其它显示器，并全屏（可选）
* 用快捷键任意调整当前窗口的大小

![](.evernote-content/74D1545B-5463-40EB-98D7-87510E292EB8/5532A9C9-9921-4EED-9577-141130B57602.gif)

图片来自该配置作者介绍

详细介绍（中文）：<https://github.com/S1ngS1ng/HammerSpoon/blob/master/README-cn.md>

作者还写了一篇[相关的文章](http://singsing.io/blog/hs/HammerSpoon-1/)，除了使用说明外，也介绍了原理与所使用的 API，对于想要自己编写的读者会有些帮助。

配置使用方法：在终端中运行 `git clone https://github.com/S1ngS1ng/HammerSpoon.git ~/.hammerspoon`，然后重载配置。

### 其他配置

此外，这里也收集了一些其他配置，并列出其中的亮点功能，看看有没有你感兴趣或需要的。

|  |  |
| --- | --- |
| **配置方案** | **功能** |
| [Braden1996/BradensPoon](https://github.com/Braden1996/BradensPoon) | 划定区域打开终端、Spotify 提醒 |
| [ztomer/.hammerspoon](https://github.com/ztomer/.hammerspoon) | 番茄计时器 |
| [andrewhampton/dotfiles](https://github.com/andrewhampton/dotfiles/tree/master/hammerspoon/) | Gmail 新邮件提醒 |
| [tdlm/hammerspoon](https://gist.github.com/tdlm/60297192cbfea99bd132) | 菜单栏显示 GitHub PR |
| [TwoLeaves/hammerspoon](https://gist.github.com/TwoLeaves/a9d226ac98be5109a226) | 桌面 / Space 管理 |
| [scottcs/dot\_hammerspoon](https://github.com/scottcs/dot_hammerspoon) | 电池状态提醒、系统休眠阻止、Hazel 代替等 |
| [agzam/spacehammer](https://github.com/agzam/spacehammer) | Spacemacs 式的快捷键风格 |

你也可以访问 [Hammerspoon 官网 Wiki 页面](https://github.com/Hammerspoon/hammerspoon/wiki/Sample-Configurations) 查看更多配置方案，也可以在搜索引擎中进行搜寻。

自己动手写脚本
-------

直接用别人的配置，难以非常妥帖地符合自己的需求。那么不如参考各种配置，规划编写我们自己的配置脚本。

如果对 Lua 语言不了解，可以看看 [X 分钟速成 Y网站上的中文教程](https://learnxinyminutes.com/docs/zh-cn/lua-cn/) 快速入门。此外，Hammerspoon 官方提供了一份 [快速入门指南](https://www.hammerspoon.org/go/)，围绕多个实际应用场景介绍了相关的 API 使用，并且给出了示例代码，也可以点击查看 [完整的 API 文档](https://www.hammerspoon.org/docs/) 。

除了 Hammerspoon 自身提供的接口外，还有不少其它开发者贡献的 [扩展](https://github.com/Hammerspoon/hammerspoon/wiki/Third-Party-Extensions) 和 [插件](https://www.hammerspoon.org/Spoons)（点击查看相应列表）。扩展为 Hammerspoon 加入了额外的 API，有些还被其最终合并进去，如 [Spotify 控制](http://www.hammerspoon.org/docs/hs.spotify.html)、[利用私有 API 操作桌面（Desktop/Space）的扩展](https://github.com/asmagill/hs._asm.undocumented.spaces)。在 Hammerspoon 中插件被称为 Spoon，是使用 API 编写的较为完整的功能模块，基本上开箱即用，比如 Bingdaily 自动每天使用 bing 图片做壁纸，HSaria2 控制 Aria2 并提供一个面板可以添加任务，显示当前下载情况。

「我想玩这个，但是不会编程怎么办？」，别急，现在开始学习编程也不晚 :) 

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，让你的工作更有效率 ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

[#效率工具](https://sspai.com/tag/%E6%95%88%E7%8E%87%E5%B7%A5%E5%85%B7)[#自动化](https://sspai.com/tag/%E8%87%AA%E5%8A%A8%E5%8C%96)[#macOS](https://sspai.com/tag/macOS)

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

---

[336](#)

---

[![](.evernote-content/74D1545B-5463-40EB-98D7-87510E292EB8/6A417B50-1A84-495B-B7F3-C47BA3C0DAF2)](https://sspai.com/user/742287)

#### [涔 C](https://sspai.com/user/742287)

---

[🌐 原始链接](https://sspai.com/post/53992)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ee980da6-3964-40c3-9fb2-e8b7c5e51741/ee980da6-3964-40c3-9fb2-e8b7c5e51741/)