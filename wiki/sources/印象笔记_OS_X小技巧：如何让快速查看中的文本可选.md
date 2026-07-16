---
title: "OS X小技巧：如何让快速查看中的文本可选"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/OS X小技巧：如何让快速查看中的文本可选.md
tags: [印象笔记]
---

# OS X小技巧：如何让快速查看中的文本可选

# OS X小技巧：如何让快速查看中的文本可选 --- 威锋网讯，快速查看（QuickLook）是 OS X 中一项便捷的功能，它可以让我们在 Finder 中快速浏览文件，例如图片、视频、文本以及其

---

# OS X小技巧：如何让快速查看中的文本可选

---

威锋网讯，快速查看（QuickLook）是 OS X 中一项便捷的功能，它可以让我们在 Finder 中快速浏览文件，例如图片、视频、文本以及其它文件。不过遗憾的是，当我们对文本文件进行快速查看的时候，用户是无法对文本中的文字进行选定的。

庆幸的是，我们还有“终端”，终端似乎就是为突破界限而生的工具，只需要简单的终端指令，就可以让我们在快速查看中实现文本的选定。

**首先我们打开终端，并输入下列指令：**

defaults write com.apple.finder QLEnableTextSelection -bool TRUE

**点击回车后，输入：**

Killall Finder

这条指令将会使得 Finder 重启，然后就大功告成了。这样你就可以在快速查看的时候选择文本了。另外值得一提的是，当你对一个单词执行 Force Touch（又或者是 3 指点击）操作的时候是会打开词典查词的，使用了上述的终端指令后，你同样可以对词典中的文本进行选定。

如果想要取消这条指令的效果的话，只需在重新执行上述操作的时候，将第一条指令中的“TRUE”替换成“FALSE”即可。

[阅读全文](http://www.feng.com/iPhone/news/2015-12-02/OS-X-tip-how-to-make-a-quick-review-the-text-in-the-optional_631918.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2015-12-02/OS-X-tip-how-to-make-a-quick-review-the-text-in-the-optional_631918.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e4b3e6c0-06aa-44dd-aa49-d45ff8cafa33/e4b3e6c0-06aa-44dd-aa49-d45ff8cafa33/)