---
title: "在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac - 少数派.md
tags: [印象笔记]
---

# 在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac - 少数派

# 在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac - 少数派 --- 在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac ========================

---

# 在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac - 少数派

---

在 Mac 上快速查看指定应用的所有窗口丨一日一技 · Mac
===============================

[![](.evernote-content/307365E2-E8CD-4522-B048-4FC5381BBE11/1FE8ECFD-F708-491B-B80C-1ABF0EE39C99.jpg)](http://matrix.sspai.com/user/713414 "luiyezheng ")

[luiyezheng](http://matrix.sspai.com/user/713414)

15分钟前

** [Mac](http://sspai.com/tag/Mac)

[** 3](http://sspai.com/33389#list-comment)

** 2

使用 Mac 时，我们可以通过按下 F3 键将所有活跃窗口排列在屏幕上，这对于窗口管理有着很大的帮助。然而，由于所有应用的窗口都同时显示，当我们开启了比较多的应用程序和窗口时，界面就会显得杂乱无章，找到需要的窗口并不容易。

[![](.evernote-content/307365E2-E8CD-4522-B048-4FC5381BBE11/E8CFC12C-406C-479A-ACFA-A98CEC5CFD5B.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/20/458e076935520c81fe6f9dd3915d7d314d81b_mw_800_wm_1_wmp_3.jpg)

其实，你可以通过双指滑动 Dock 中应用的图标，来查看这个应用当前开启的窗口。这样一来，搜索范围从所有应用程序缩小到一个应用程序，就能更快找到想要的窗口。

OSX 中默认关闭了这一操作，我们需要通过终端命令将它开启，下面我们就来看看具体如何操作。

操作方法
----

首先，你可以在 LaunchPad 或应用程序文件夹内打开终端，或者直接在 Spotlight 中搜索「终端」。

[![](.evernote-content/307365E2-E8CD-4522-B048-4FC5381BBE11/88DB3391-DCDC-4DF7-886B-B1649F97AAB4.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/20/a3a1cf7bb3ffa629aa45f0439045cd3d4d81e_mw_800_wm_1_wmp_3.jpg)

[![](.evernote-content/307365E2-E8CD-4522-B048-4FC5381BBE11/DC58F877-861D-46A4-B96D-D3C4E20F47D2.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/20/15dfd372ec5f6035da09db1a713aef594d81d_mw_800_wm_1_wmp_3.jpg)

找到并打开终端后，输入下面的指令：

`defaults write com.apple.dock scroll-to-open -bool true &&\killall Dock`

来看看效果，例如这里我们想找到文本编辑器的某个窗口，那么就在文本编辑的 Dock 图标上双指滑动：

[![](.evernote-content/307365E2-E8CD-4522-B048-4FC5381BBE11/1883E7EA-6967-4595-94F5-E7B3E347F5E0.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/03/20/02d8c9e1c86af6c32f998c49d5ae19194d81a_mw_800_wm_1_wmp_3.jpg)

可以看到，屏幕上只显示了文本编辑器的三个窗口。活跃的窗口显示在屏幕的中央，而最小化窗口以缩略图的形式显示在底部。

如果你想要关闭这一操作，只需要输入下面的指令：

`defaults write com.apple.dock scroll-to-open -bool false &&\killall Dock`

好了，以上就是开启双指滑动显示窗口，从而提高窗口管理效率的方法。如果你有任何疑问，或是有其他更好的方法，欢迎在下面的评论区与我们交流。

---

[🌐 原始链接](http://sspai.com/33389)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b714c3b6-2e16-4b34-8e08-78e2b9eaf00d/b714c3b6-2e16-4b34-8e08-78e2b9eaf00d/)