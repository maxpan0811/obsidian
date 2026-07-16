---
title: "技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作.md
tags: [印象笔记]
---

# 技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作

# 技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作 --- ![](.evernote-content/F1FC01CF-97DE-43A9-BA9F-85BADCC39BE8/2A

---

# 技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作

---

![](.evernote-content/F1FC01CF-97DE-43A9-BA9F-85BADCC39BE8/2AEAB9F9-F205-49F8-B980-8F8A5EA36574.jpg)

MacID 是一款让你可以通过指纹识别、触控板手势等方法解锁 Mac 的应用。在少数派[此前的文章](http://sspai.com/32055)中，已和大家详细介绍过 MacID 的主要功能和使用方法。

你可能不知道的是，在 MacID 1.3 中，我们可以通过 AppleScript 对 MacID 进行扩展了。具体来说，你可以让 MacID 在 Mac 睡眠、唤醒、锁屏、解锁时，运行预先定义好的 AppleScript 脚本文件。举个例子，你可以让 Mac 锁屏时自动暂停 itunes 音乐播放，之后解锁 Mac 时再接着播放。

首先，什么是 AppleScript 呢？简单来说，AppleScript 是苹果开发的一种简单的脚本语言，可以用来控制运行于 Mac OS 上的部分程序，也可以写成独立运行的程序文件。

你可能会问，「我不知道如何写 AppleScript 脚本怎么办？」不用担心，AppleScript 实现基本功能的代码非常简单，此外，我会在本文提供一些常用的代码，你也可以直接拿去用。

方法
--

打开 Finder，在菜单栏中选择「前往」，然后点击「前往文件夹」选项（或使用快捷键Shift+Command+G），在弹出的对话框中输入路径`~Library/Application/Support/MacID` 并按下回车。

在打开的文件夹中，可以看到四个子文件夹，分别是 *onSleep*（睡眠）、*onWake*（唤醒）、*onUnlock*（锁屏）以及 *onLock*（解锁）。当我们把 AppleScript 脚本文件放入特定的子文件夹中后，MacID 就会在对应的 Mac 状态下执行脚本。

![](.evernote-content/F1FC01CF-97DE-43A9-BA9F-85BADCC39BE8/339D1FA7-688C-4060-9A49-799C29DBC275.jpg)

知道了文件夹在哪里，下面就要开始编写 AppleScript 脚本了。先看一个简单的暂停 iTunes 的例子：

```
tell app "iTunes" to pause
```

1. 打开 Mac 自带的「脚本编辑器」并新建一个文件，将上面这行代码复制粘贴。然后从菜单栏「文件」-「导出」，注意一定要选择「文本」作为文件保存的格式。  
   ![](.evernote-content/F1FC01CF-97DE-43A9-BA9F-85BADCC39BE8/26F30C2C-A542-4F64-B5FB-371295E7EB11.jpg)
2. 将导出的文件拖动至 *onLock* 文件夹中。
3. 打开 iTunes 播放一首歌，然后让你的 Mac 通过 MacID 锁屏。一小会儿之后，音乐就会暂停了。

暂停了音乐，接下来我们需要让 MacID 解锁电脑时继续播放 iTunes，脚本代码如下：

```
tell app "iTunes" to play
```

重复上面的步骤，这次将代码文件放入到 *onUnlock* 文件夹即可。

更多玩法
----

### 将系统静音

```
set volume output volume 0
```

（这里的 0 也可以修改成其他你需要的音量数值）

### 暂停或继续 MplayerX 视频播放

```
tell app "MplayerX" to pause/play
```

### 启动迅雷并开始下载

让这段代码在 Mac 睡眠时执行，就可以在你不使用电脑的时候自动下载文件了。注意要勾选迅雷设置中的「启动后自动开始未完成任务」。

```
tell app "Thunder" to launch
```

如果你还有更多好点子，但不会使用 AppleScript，可以在下方评论告诉我你的想法，我会试试看能否通过 AppleScript 实现，并告诉你方法。

比较遗憾的是，MacID 目前只能通过 AppleScript 对应用程序执行一次操作，因此一些复杂的程序就无法实现了，若之后的版本能有所改进，那这个功能一定会发挥更大作用。

目前你可以在 App Store 下载 MacID（￥25），或在[官网下载](https://macid.co/) Mac 版（免费）。

**继续阅读：**[《优雅解锁 Mac 的 MacID》](http://sspai.com/32055)

文章来源 [少数派](http://sspai.com) ，原作者 [luiyezheng](http://sspai.com/author/713414) ，转载请注明原文链接

原文可获取应用下载链接：[技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作](http://sspai.com/32828)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/F1FC01CF-97DE-43A9-BA9F-85BADCC39BE8/ACC53B74-96E1-4979-A905-85E38E5B806B.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:buyAW/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fwatch%2Fbuy%2F)

---

[🌐 原始链接](http://sspai.com/32828)

[📎 在印象笔记中打开](evernote:///view/207087/s1/cf0b4048-1add-4a07-95e6-cfdb68f38a95/cf0b4048-1add-4a07-95e6-cfdb68f38a95/)