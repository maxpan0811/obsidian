# 用 Mac 抹掉的 U 盘在 PC 上不能用？试试这个方法 | 一日一技

---

用 Mac 抹掉的 U 盘在 PC 上不能用？试试这个方法 | 一日一技
====================================

[![](.evernote-content/FDD9480B-43FE-406C-80F3-C5519EDE869D/67FC10B7-F64F-4995-9278-689B8D703B24.jpg)](https://sspai.com/user/707024)

#### [Megabits](https://sspai.com/user/707024)

12月03日

91  [20](#)

不知道你有没有遇到过这样的问题：平时用的 U 盘太乱了，想要重新来过，于是用 Mac 自带的磁盘工具抹掉了。你本以为一切 OK，存好要用的文件就去楼下打印店了。到了之后打印店的人却问你这盘显示不出来，是不是坏了。

你回来又好好看了一下，没毛病啊。主引导记录（MBR），好好的 FAT 格式，为什么就显示不出来呢？

出现问题的原因
-------

这其实是一个 Mac 分区表的结构问题。有些时候明明设置了 MBR 分区表和 FAT 分区，弄出来的盘依然会在 Windows 中无法显示。Windows 10 在某一版本的更新里修复了这个问题，但是你不能保证别人的电脑是不是这个最新版本，这个问题依然有很大可能性出现。有时候本来要给别人传个文件，好不容易复制到盘里了，结果在别人电脑上插进去没显示，特别耽误事。

而且由于是分区表问题，你并不能通过在能读这玩意的 Windows 里面格式化一遍来解决。

解决办法
----

一般来讲要在 Mac 上解决这个问题要么你在终端里折腾一阵，要么就要花钱买好贵的分区工具，我这里有一个比较有趣还不用花钱的解决方案。

有一款叫做 [ApplePi-Baker](https://www.tweaking4all.com/software/macosx-software/macosx-apple-pi-baker/) 的软件，这玩意本来是拿来搞树莓派的，但是也可以拿来抹掉你的 U 盘。操作方法非常简单，把盘插到你的 Mac 上，打开这款软件。在左边的列表中选中你的 U 盘，点击 Prep for NOOBS，等待运行完成即可。

![](.evernote-content/FDD9480B-43FE-406C-80F3-C5519EDE869D/CB8F312D-F4B1-4A07-92BD-6D019BFF0711.png)

之后你就可以把卷标改回自己想叫的名字，正常使用了。我推荐你把这款软件留在电脑上，之后任何可能要拿出去在别人电脑上用的 U 盘，都可以用这个来格式化以防万一。

这个功能本来是拿来抹掉给树莓派用的 SD 卡的。树莓派一般使用的就是最基础的 MBR 分区表的 FAT32 分区，不管在什么系统上都是用的了的。而且其抹盘的流程和磁盘工具不同，可以写出「正常」的 MBR 分区表。

你还可以在 Windows 上使用 [Rufus](https://rufus.akeo.ie/?locale=zh_CN) 来干同样的事情。按照下图选好各种选项，处理一次就没问题了。

![](.evernote-content/FDD9480B-43FE-406C-80F3-C5519EDE869D/282FB7C1-7A19-41CF-84EB-F9D0C4426BB5.png)

下载地址：

* [ApplePi-Baker](https://www.tweaking4all.com/software/macosx-software/macosx-apple-pi-baker/)（[直接下载压缩包](https://www.tweaking4all.com/?wpfb_dl=94)）
* [Rufus](https://rufus.akeo.ie/?locale=zh_CN)

---

[🌐 原始链接](https://sspai.com/post/42108)

[📎 在印象笔记中打开](evernote:///view/207087/s1/eb9dcb65-a4b0-446a-9822-c2fce77ce6b1/eb9dcb65-a4b0-446a-9822-c2fce77ce6b1/)