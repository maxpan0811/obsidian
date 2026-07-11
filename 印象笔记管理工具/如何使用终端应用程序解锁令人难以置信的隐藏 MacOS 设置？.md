# 如何使用终端应用程序解锁令人难以置信的隐藏 MacOS 设置？

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0MzU5NzQ4Mw==&mid=224749...](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247490241&idx=1&sn=c2a524f030df3013d8d08c91167b3a1a&chksm=c2401ff45cc7fef5069246790bcca764232c4187838204fd283246cde12969cebaddc278728d&mpshare=1&scene=24&srcid=07022TAQAlT7KMxDAkQfExB7&sharer_shareinfo=192748ad1d7c06f8251b3631d39a9e24&sharer_shareinfo_first=192748ad1d7c06f8251b3631d39a9e24&clicktime=1783048833&enterid=1783048833&ascene=14&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0/w6pkRRdNBF3oxFKIEtpBLAAQIE97dBBAEAAAAAAERPK+lzPO4AAAAOpnltbLcz9gKNyK89dVj0O98mvh845yi1YfBBFnWnnpDt59/60pBU68cdxUXXYL5OF2e5+SjjFHCAIxil6dNuQc9GmMDaYj8Rbp4bp/fH8QsqV2RUF29lzdhzFdI+spU8u+dinrn87GtwoRrJa6i2DpWicMNCqLRCCme6OXc0xTRU7dB0EHa3mofzYD7uIlc30+SE05GJb5BkFLs+0+krVYmXzvuFsGYzGA==&pass_ticket=y08nPth9XSQJUiBrvZZA66iqK+hNDY74TAxvyOxvL4QkZZ9SbLRj0rVdY2XQHwf4&wx_header=3)

如何使用终端应用程序解锁令人难以置信的隐藏 MacOS 设置？
===============================

Original点蓝色字关注👉 程序员echo

MacOS 有许多实用的自定义选项，😭这些选项并不直接出现在系统设置中。要修改这些选项，你需要通过一个额外的步骤——使用 `defaults` 命令。

如果你希望将 Mac 的使用体验调整得更加符合自己的需求，远超 Apple 默认的设置，那这篇文章对你来说非常有帮助。

![](.evernote-content/EE01A611-247B-46A5-B7DA-C7E4E4AC7E50/417403EB-6643-40BA-93D3-76A0EA602731.png)

让我们深入了解一下。

### 介绍

如果你对编程不熟悉，不要担心，这个过程只是将不同的命令文本复制并粘贴到一个特殊的窗口中。

首先，打开 Spotlight，搜索并打开“终端”应用。

如何打开 Spotlight
--------------

你可以按下 CMD + 空格键，或者点击导航栏顶部的搜索🔍图标。

终端界面看起来应该是这样的，或者稍微有所不同：

![](.evernote-content/EE01A611-247B-46A5-B7DA-C7E4E4AC7E50/7F01A5DE-5947-4DD7-9397-DCF263F5C77D.jpg)

终端界面：
-----

这就是我们将粘贴所有命令的地方。现在，让我们深入探讨一下我们将要做的事情。

![](.evernote-content/EE01A611-247B-46A5-B7DA-C7E4E4AC7E50/42340899-69D4-4B60-B197-E64A26825FB8.jpg)

### 什么是 `defaults` 命令？

`defaults` 命令允许你通过终端读取、写入和删除 macOS 的偏好设置。

这条命令的基本格式是：

defaults write <domain> <key> <value>

* `<domain>`: 应用程序的捆绑标识符，例如 `com.apple.finder` 用来修改 Finder 或 `NSGlobalDomain` 系统范围的设置。
* `<key>`: 你正在修改的具体偏好设置。
* `<value>`: 你要分配的值，可以是字符串、布尔值（true 或 false）、整数等。

一些更改会立即生效，而其他更改可能需要通过以下命令重新启动受影响的应用：

killall Finder

有时你可能会被提示输入 Mac 密码。

这是完全正常的，因为你正在修改设置，要求输入密码是一种验证方式，确保修改不是恶意程序在执行。

### 为什么使用 `defaults` 命令？

通过 `defaults` 命令，你可以获得对 macOS 环境的完全控制，从而获得更加个性化的体验。

以下是它带来的一些好处：

* 个性化系统行为
* 解锁实验性或隐藏的功能
* 加速动画和交互
* 配置开发者工具或优化工作流程

但不再废话了，接下来让我们深入了解一些真正能够改变你使用 MacOS 方式的 `defaults` 命令。

这些命令有些是提升质量的功能，而另一些则是彻底改变游戏规则的优化。

### 主要的 `defaults` 命令

这些命令按类别组织，每个命令后面都会附带一个小段落，告诉你如何还原到原来的设置，以防你以后想要恢复。

![](.evernote-content/EE01A611-247B-46A5-B7DA-C7E4E4AC7E50/8AE6D28A-5AD6-4299-A797-D951DE797A92.png)

#### 界面与动画

* **改变最小化动画效果**（改变应用程序最小化的行为）

defaults write com.apple.dock mineffect -string "suck"; killall Dock

恢复：`defaults write com.apple.dock mineffect -string "genie"; killall Dock`

* **禁用窗口动画**

defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false

恢复：将 `false` 改为 `true`。

* **禁用橡皮筋滚动**

defaults write -g NSScrollViewRubberbanding -int 0

恢复：将 `0` 改为 `1`。

#### Finder 调整

* **默认显示隐藏文件**

defaults write com.apple.finder AppleShowAllFiles -bool true; killall Finder

恢复：将 `true` 改为 `false`。

* **在 Finder 标题中显示完整文件路径**

defaults write com.apple.finder \_FXShowPosixPathInTitle -bool true; killall Finder

恢复：将 `true` 改为 `false`。

* **启用 Finder 的退出选项**

defaults write com.apple.finder QuitMenuItem -bool true; killall Finder

恢复：将 `true` 改为 `false`。

* **隐藏桌面上的所有图标**

defaults write com.apple.finder CreateDesktop -bool false; killall Finder

恢复：将 `false` 改为 `true`。

#### Dock 与任务控制

* **移除 Dock 自动隐藏延迟**

defaults write com.apple.dock autohide-delay -float 0; killall Dock

恢复：`defaults delete com.apple.dock autohide-delay; killall Dock`

* **加速任务控制动画**

defaults write com.apple.dock expose-animation-duration -float 0.1; killall Dock

恢复：`defaults delete com.apple.dock expose-animation-duration; killall Dock`

* **只显示正在运行的应用程序**

defaults write com.apple.dock static-only -bool true; killall Dock

恢复：将 `true` 改为 `false`。

* **在 Dock 中添加隐形间隔**

defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="spacer-tile";}'; killall Dock

恢复：从 Dock 中拖出间隔条即可删除。

#### 系统便捷功能

* **始终展开“保存”对话框**

defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode2 -bool true

恢复：将 `true` 改为 `false`。

* **始终展开“打印”对话框**

defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true
defaults write NSGlobalDomain PMPrintingExpandedStateForPrint2 -bool true

恢复：将 `true` 改为 `false`。

* **默认将文件保存在本地（而非 iCloud）**

defaults write NSGlobalDomain NSDocumentSaveNewDocumentsToCloud -bool false

恢复：将 `false` 改为 `true`。

* **重新启用键盘重复（禁用重音符号菜单）**

defaults write -g ApplePressAndHoldEnabled -bool false

恢复：将 `false` 改为 `true`。

#### 隐私与工作流

* **防止照片自动打开**

defaults -currentHost write com.apple.ImageCapture disableHotPlug -bool true

恢复：`defaults -currentHost delete com.apple.ImageCapture disableHotPlug`

* **停止在网络驱动器上创建**`.DS_Store`**文件**

defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true

恢复：将 `true` 改为 `false`。

* **禁用“从互联网下载”警告**

defaults write com.apple.LaunchServices LSQuarantine -bool false

恢复：将 `false` 改为 `true`。

#### 截图与显示

* **将截图文件格式更改为 JPEG**

defaults write com.apple.screencapture type -string "jpg"; killall SystemUIServer

恢复：将 `jpg` 改为 `png`。

* **更改默认截图保存位置**

defaults write com.apple.screencapture location -string "$HOME/Pictures/Screenshots"; killall SystemUIServer

恢复：`defaults delete com.apple.screencapture location; killall SystemUIServer`

* **禁用截图阴影**

defaults write com.apple.screencapture disable-shadow -bool true; killall SystemUIServer

恢复：将 `true` 改为 `false`。

* **禁用浮动缩略图预览**

defaults write com.apple.screencapture show-thumbnail -bool false; killall SystemUIServer

恢复：将 `false` 改为 `true`。

* **从截图文件名中移除日期/时间**

defaults write com.apple.screencapture include-date -bool false; killall SystemUIServer

恢复：将 `false` 改为 `true`。

* **改善非 Retina 显示器上的字体平滑效果**

defaults write -g CGFontRenderingFontSmoothingDisabled -bool false

恢复：将 `false` 改为 `true`。 到此，😊本期的分享到这了，下期我们再见！！！🚀

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247490241&idx=1&sn=c2a524f030df3013d8d08c91167b3a1a&chksm=c2401ff45cc7fef5069246790bcca764232c4187838204fd283246cde12969cebaddc278728d&mpshare=1&scene=24&srcid=07022TAQAlT7KMxDAkQfExB7&sharer_shareinfo=192748ad1d7c06f8251b3631d39a9e24&sharer_shareinfo_first=192748ad1d7c06f8251b3631d39a9e24&clicktime=1783048833&enterid=1783048833&ascene=14&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0/w6pkRRdNBF3oxFKIEtpBLAAQIE97dBBAEAAAAAAERPK+lzPO4AAAAOpnltbLcz9gKNyK89dVj0O98mvh845yi1YfBBFnWnnpDt59/60pBU68cdxUXXYL5OF2e5+SjjFHCAIxil6dNuQc9GmMDaYj8Rbp4bp/fH8QsqV2RUF29lzdhzFdI+spU8u+dinrn87GtwoRrJa6i2DpWicMNCqLRCCme6OXc0xTRU7dB0EHa3mofzYD7uIlc30+SE05GJb5BkFLs+0+krVYmXzvuFsGYzGA==&pass_ticket=y08nPth9XSQJUiBrvZZA66iqK+hNDY74TAxvyOxvL4QkZZ9SbLRj0rVdY2XQHwf4&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/24cf4e06-d9b5-4ebe-aca1-0a011df807b7/24cf4e06-d9b5-4ebe-aca1-0a011df807b7/)