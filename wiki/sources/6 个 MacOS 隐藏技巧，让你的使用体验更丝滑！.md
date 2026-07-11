---
title: 6 个 MacOS 隐藏技巧，让你的使用体验更丝滑！
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/6 个 MacOS 隐藏技巧，让你的使用体验更丝滑！.md
tags: [印象笔记]
---

# 6 个 MacOS 隐藏技巧，让你的使用体验更丝滑！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU4Njc3NjQ1Nw==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzU4Njc3NjQ1Nw==&mid=2247488337&idx=1&sn=f090c0c5b5f472af91164062a36c52e6&chksm=fc4c22b5cc189f5b4d502b20ab049b57e84b834d3a59a94ecd609da1c8a537063200660f6bd9&scene=90&xtrack=1&sessionid=1742717341&subscene=93&clicktime=1742717776&enterid=1742717776&flutter_pos=5&biz_enter_id=4&ranksessionid=1742717351&ascene=56&devicetype=iOS18.3.2&version=1800383b&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ+fMuwVdzZe3jBltHA7ej1xLYAQIE97dBBAEAAAAAAKjKDUEmbD8AAAAOpnltbLcz9gKNyK89dVj0443m8Hdi1Rf98ksRzROZtdPTn9r0ViFh8/kn8rnvQg4p4XNSYfm9a9EKFZTjvkoLy5OQFC4pOyzu6RTCohpt/drpoEloVyCQQs5nLrrStMm0y4BBqYYrw6QQ4J4zETR1pwncPm2PAGA3/qCNsvTJX6N9rPxly/zyHCmZEpILeGhSpTlSmJ09JiZMJA0wkOhcCvA/wvXdsxes6aYRGCz33DzMH4+rLT7kF1eA02PVeCXPAw==&pass_ticket=ZhCHLcxn7xlq1/NXTua8PlkQocdCRrezqx/iDW3IFtIxdynYijHPHas2o29gQ1GZ&wx_header=3)

6 个 MacOS 隐藏技巧，让你的使用体验更丝滑！
==========================

原创 点蓝色字关注👉  程序员黎明

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/122841A5-C9F8-450B-BD58-A54A94E982DA.gif)

MacOS 的设计简洁直观，几乎谁都能轻松上手，这确实是苹果的一大优势。但与此同时，也有不少实用功能被深藏在系统设置里，不仔细挖掘还真不容易发现。

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/CDF6FF4E-FC63-48A8-A090-5597EAEA2E01.png)

今天就来聊聊 6 个 MacOS 上非常实用但容易被忽略的小技巧，希望能帮到你！

---

1. 让 Spotlight 发挥最大价值 🔍✨
------------------------

Spotlight 不只是个应用启动器，它还有很多隐藏功能，比如：

* **直接计算**：输入算式就能出结果，回车就能看到答案。

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/7D5703FF-823A-43E8-BA47-DFF77E793CB6.png)

* **快速换算**：输入后，它会直接告诉你结果。长度、体积、重量等单位都能换算，省得上网查了。

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/89EBC948-2A62-44F3-B62A-BD87C00DCE0E.png)

* **秒查文件路径**：找到某个文件后，按住 `Command` 键，就能看到它在 Finder 里的完整路径。

---

2. 定制 Dock，让它更顺手 🖥️🎨
--------------------

Mac 的 Dock 默认占据不少屏幕空间，而且可能不够高效。想让它更简洁？可以这样设置：

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/EE09AF76-ADB8-4BF5-8FFE-98899408727D.png)

* **隐藏 Dock**：打开 **系统设置 → 桌面与 Dock → 自动隐藏和显示 Dock**，这样 Dock 只在鼠标移到屏幕底部时才出现。

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/82CBDF50-A2FF-49A4-BD4D-745C6F102F5E.png)

* **加速 Dock 动画**：默认 Dock 的隐藏和显示动画较慢，我们可以用终端命令加速：

  defaults write com.apple.dock autohide-time-modifier -float 0.15;killall Dock

  这样 Dock 只需要 0.15 秒就能出现，既快又不失美感。想恢复默认速度？用这条命令：

  defaults delete com.apple.dock autohide-time-modifier;killall Dock

---

3. 截图神器，让你效率翻倍 📸⚡
-----------------

Mac 自带的截图功能很强大，但很多人可能只知道 `Command + Shift + 3`（全屏截图）。其实还有这些技巧：

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/677F6DAF-9FD9-499F-8365-B5BC558DCA7E.png)

* `Command + Shift + 4`：选取屏幕的某个区域截图。
* `Command + Shift + 4` → 按 `空格键`：可以直接截图某个窗口，而且带漂亮的阴影效果。
* `Command + Shift + 5`：呼出截图菜单，可以录屏、定时截图，还能设置截图保存位置。
* **小技巧**：在截图时按住 `Control`，截图就会直接复制到剪贴板，而不是生成文件，方便粘贴到其他地方。

---

4. 神奇的通用剪贴板
-----------

苹果的 **通用剪贴板** 是个神奇的功能，它允许你在 iPhone 上复制内容，然后直接在 Mac 上粘贴（反之亦然）。设置方法如下：

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/71BD63C3-3FC5-4239-AA91-AD373CBDBE10.png)

**系统设置 → 通用 → 隔空投送与接力**，确保 **“允许在这台 Mac 和 iCloud 设备之间接力”** 已开启。

现在你可以在 iPhone 里复制一段文字，回到 Mac 上直接 `Command + V` 粘贴，无需额外操作，超方便！

---

5. 强制退出卡死的应用 🔌💻
---------------

Mac 很稳定，但偶尔应用还是会崩溃。遇到卡死的程序，不用重启 Mac，试试这些方法：

* **强制退出应用**：按 `Command + Option + Escape`，选择卡住的应用，点 **强制退出**。

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/0D0D247C-A591-47A0-96A0-9C59A9F0A1A2.png)

* **强制关机**：如果整个 Mac 都卡死了，可以长按 **电源键** 10 秒，直接关机（不推荐，非必要别用）。
* **尝试温和重启**：按 `Control + 电源键`，会弹出一个关机/重启菜单，优先试试这个，比强制关机更安全。

---

6. 这些快捷键让你操作更高效 ⌨️🚀
-------------------

学会这些快捷键，Mac 用起来能快一大截：

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/5E11CDF1-5862-46F2-B699-A8AF07EEB634.png)

* `Command + Tab`：切换不同的应用。
* `Command + ~`（波浪号）：在同一应用的多个窗口之间切换。
* `Command + W`：关闭当前窗口。
* `Command + Q`：退出当前应用。
* `Command + L`：浏览器里快速选中地址栏。

---

最后
--

这些小技巧虽然隐藏得比较深，但掌握后真的能让 Mac 用起来更顺手。

![](.evernote-content/034B2A81-685D-40D6-819D-DF2D252B85B2/A9ABC1F7-178B-4F76-9330-256C78778550.png)

如果你有更好用的 Mac 技巧，欢迎分享！好的，本期我们就到这里啦，感谢观看！我们下期再见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU4Njc3NjQ1Nw==&mid=2247488337&idx=1&sn=f090c0c5b5f472af91164062a36c52e6&chksm=fc4c22b5cc189f5b4d502b20ab049b57e84b834d3a59a94ecd609da1c8a537063200660f6bd9&scene=90&xtrack=1&sessionid=1742717341&subscene=93&clicktime=1742717776&enterid=1742717776&flutter_pos=5&biz_enter_id=4&ranksessionid=1742717351&ascene=56&devicetype=iOS18.3.2&version=1800383b&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ+fMuwVdzZe3jBltHA7ej1xLYAQIE97dBBAEAAAAAAKjKDUEmbD8AAAAOpnltbLcz9gKNyK89dVj0443m8Hdi1Rf98ksRzROZtdPTn9r0ViFh8/kn8rnvQg4p4XNSYfm9a9EKFZTjvkoLy5OQFC4pOyzu6RTCohpt/drpoEloVyCQQs5nLrrStMm0y4BBqYYrw6QQ4J4zETR1pwncPm2PAGA3/qCNsvTJX6N9rPxly/zyHCmZEpILeGhSpTlSmJ09JiZMJA0wkOhcCvA/wvXdsxes6aYRGCz33DzMH4+rLT7kF1eA02PVeCXPAw==&pass_ticket=ZhCHLcxn7xlq1/NXTua8PlkQocdCRrezqx/iDW3IFtIxdynYijHPHas2o29gQ1GZ&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e71da176-dd36-41ce-8f3d-71969547eed3/e71da176-dd36-41ce-8f3d-71969547eed3/)
