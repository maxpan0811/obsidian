---
title: "OS X新手技巧：改变Launchpad的应用布局"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/OS X新手技巧：改变Launchpad的应用布局.md
tags: [印象笔记]
---

# OS X新手技巧：改变Launchpad的应用布局

# OS X新手技巧：改变Launchpad的应用布局 --- [![](.evernote-content/0B49DD2F-F89A-44F4-8510-78756320C6C2/E11C3618

---

# OS X新手技巧：改变Launchpad的应用布局

---

[![](.evernote-content/0B49DD2F-F89A-44F4-8510-78756320C6C2/E11C3618-DCF1-49CA-B3C6-B86711230259.png)](http://www.feng.com/iPhone/news/2016-03-15/OS-X-novice-skills-change-the-Launchpad-application-layout_641453.shtml)

　威锋网讯，Launchpad 是 OS X 中的一个应用集合中心，位于 Dock 的它给用户一种 iOS 主屏的即视感。默认情况下，Launchpad 的应用显示布局为 7 列 5 行，如果你对于这种排列不满意的话，那么我们可以通过 OS X 的终端指令来对它的布局进行修改。

![](.evernote-content/0B49DD2F-F89A-44F4-8510-78756320C6C2/E11C3618-DCF1-49CA-B3C6-B86711230259.png)

通过本文，我们将向你介绍如何修改 Launchpad 的应用布局，资深用户可略过。

1.打开终端应用，并输入下列指令：

defaults write com.apple.dock springboard-columns -int X;defaults write com.apple.dock springboard-rows -int X;defaults write com.apple.dock ResetLaunchPad -bool TRUE;killall Dock

注意将上述指令中的X替换为数字，第一个 X 代表列，第二个 X 代表行。例如你要将应用布局设置为 5 列 3 行,则输入下列指令：

![](.evernote-content/0B49DD2F-F89A-44F4-8510-78756320C6C2/E50FBE8F-117A-4122-9400-0E4C7346A2B8.png)

defaults write com.apple.dock springboard-columns -int 5;defaults write com.apple.dock springboard-rows -int 3;defaults write com.apple.dock ResetLaunchPad -bool TRUE;killall Dock

2.点击回车并等待 Dock 和 Launchpad 重启

3.重新打开 Launchpad 就可以看到变化了

![](.evernote-content/0B49DD2F-F89A-44F4-8510-78756320C6C2/40270D41-FC04-41FD-8015-9D033DB04602.png)

如果你希望恢复到默认设置，只需将列和行的数字改回和原先一致即可。根据屏幕尺寸和屏幕分辨率的不同，默认的布局也有可能不同。

[阅读全文](http://www.feng.com/iPhone/news/2016-03-15/OS-X-novice-skills-change-the-Launchpad-application-layout_641453.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2016-03-15/OS-X-novice-skills-change-the-Launchpad-application-layout_641453.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/abe494a5-2901-4537-a586-6e7c618ea6da/abe494a5-2901-4537-a586-6e7c618ea6da/)