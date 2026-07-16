---
title: "终端教程：删除动画使自动隐藏Dock更快"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/终端教程：删除动画使自动隐藏Dock更快.md
tags: [印象笔记]
---

# 终端教程：删除动画使自动隐藏Dock更快

# 终端教程：删除动画使自动隐藏Dock更快 --- 威锋网讯，如果您在全屏模式下使用 macOS 应用，或者设置了光标移开的时候 Dock 会自动隐藏，那么您应该注意到尝试访问 Dock 时会发生的

---

# 终端教程：删除动画使自动隐藏Dock更快

---

威锋网讯，如果您在全屏模式下使用 macOS 应用，或者设置了光标移开的时候 Dock 会自动隐藏，那么您应该注意到尝试访问 Dock 时会发生的延迟。这些延迟是由附加到 Dock 的动画所产生的。每当您尝试通过将光标移动到 Mac 屏幕底部的 Dock 时，macOS 就会启动这个动画。

![](.evernote-content/5F789DB1-CB79-4463-8C5B-526C37C169B9/4EED5C35-FB4F-4EFB-8FC1-2D1EFA92567D.jpg)

这个动画对于保持 macOS 的美感至关重要，但这增加了您使用 Dock 的时间。如果您想摆脱这个动画，我们就可以借助完美的终端命令。使用这个终端命令的唯一缺点可能是在初期的时候您会感到一些不习惯。但是如果您可以坚持下来，那么您就可以更快地访问 Dock。

![](.evernote-content/5F789DB1-CB79-4463-8C5B-526C37C169B9/8FD6FDA9-963E-4C85-A15F-C89DF893A5A2.gif)

**删除动画使自动隐藏 Dock 更快**

如果还没有打开自动隐藏 Dock 的选项，最好先执行这个操作。您可以通过打开系统偏好设置> Dock 并选中“自动显示和隐藏 Dock”选项。

现在只需打开终端应用并复制粘贴以下命令：

defaults write com.apple.dock autohide-time-modifier -int 0;killal

使用此终端命令，Dock 动画将会被完全移除，从而让用户更快速地访问。

[阅读全文](http://www.feng.com/iPhone/news/2017-05-19/Terminal-tutorial-to-automatically-delete-animation-hidden-Dock-faster_678644.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2017-05-19/Terminal-tutorial-to-automatically-delete-animation-hidden-Dock-faster_678644.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c50472ca-79fa-4569-9c3a-eaab1ec3857e/c50472ca-79fa-4569-9c3a-eaab1ec3857e/)