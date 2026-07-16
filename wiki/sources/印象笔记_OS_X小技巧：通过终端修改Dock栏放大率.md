---
title: "OS X小技巧：通过终端修改Dock栏放大率"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/OS X小技巧：通过终端修改Dock栏放大率.md
tags: [印象笔记]
---

# OS X小技巧：通过终端修改Dock栏放大率

# OS X小技巧：通过终端修改Dock栏放大率 --- [![](.evernote-content/CB2FA458-B339-4862-8518-BEFCB873A816/6118193E-75

---

# OS X小技巧：通过终端修改Dock栏放大率

---

[![](.evernote-content/CB2FA458-B339-4862-8518-BEFCB873A816/6118193E-75FB-457D-B9A2-4D9C20ADFBD8.jpg)](http://www.feng.com/iPhone/news/2015-10-26/OS-X-tip-through-the-terminal-to-modify-the-Dock-bar-magnification_628198.shtml)

　威锋网讯，“终端”是 OS X 平台上一个非常快捷的指令工具，今天我们要为大家介绍的是如何利用终端来更改 Dock 的放大率，有朋友会问，在系统偏好设置中进行修改不是更加简单快捷吗？

![](.evernote-content/CB2FA458-B339-4862-8518-BEFCB873A816/0F56984C-29DB-4BC8-8DCE-78991168C3C4.jpg)  
  
![](.evernote-content/CB2FA458-B339-4862-8518-BEFCB873A816/6118193E-75FB-457D-B9A2-4D9C20ADFBD8.jpg)

首先是终端也可以很高效，因为利用终端可以直接修改放大率的数值。其次，终端可以比系统中默认设置的最大放大率还高出 4 倍。最后，终端就是为爱折腾爱动手的用户而设的。

要更改 Dock 栏的放大率，首先打开终端，并输入以下指令：

defaults write com.apple.dock largesize -int 128; killall Dock

在你进行“回车”之前，你可以对“128”这个数值进行修改，只要不超过“512”，其它数值都是有效的。需要指出的是，不要使用负数。

回车确认后，Dock 栏便会重启并生效。如果不成功的话，那么肯定是有某个步骤出了错。

![](.evernote-content/CB2FA458-B339-4862-8518-BEFCB873A816/2385C872-35F1-4EAA-AE0E-337FD0926965.jpg)

如果你还知道其它的终端指令，不妨和我们分享。

[阅读全文](http://www.feng.com/iPhone/news/2015-10-26/OS-X-tip-through-the-terminal-to-modify-the-Dock-bar-magnification_628198.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2015-10-26/OS-X-tip-through-the-terminal-to-modify-the-Dock-bar-magnification_628198.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7aec49c8-910a-4756-80c1-0691384a1af6/7aec49c8-910a-4756-80c1-0691384a1af6/)