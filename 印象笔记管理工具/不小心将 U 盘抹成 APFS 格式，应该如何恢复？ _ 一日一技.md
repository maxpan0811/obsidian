# 不小心将 U 盘抹成 APFS 格式，应该如何恢复？ | 一日一技

---

不小心将 U 盘抹成 APFS 格式，应该如何恢复？ | 一日一技
=================================

15 小时前

[![](.evernote-content/E40AC2CA-F4C7-4DEC-8AF6-3B9443F89B89/6B5B794F-5111-48D5-A908-3F63271FBB17)](https://sspai.com/user/666443/updates) 

#### [Vanilla](https://sspai.com/user/666443/updates)

很多 Mac 用户在升级系统到 macOS Mojave 版本后发现，APFS 格式的 U 盘在系统自带的磁盘工具 app 中无法抹成其它的通用格式，只有孤零零的 4 个「APFS」选项，让人心生绝望。

![](.evernote-content/E40AC2CA-F4C7-4DEC-8AF6-3B9443F89B89/7F7DB071-5ECE-42EB-9F6A-ED84C30B74FA.jpg)

那么，如何在 Mac 上找回磁盘工具 app 原来的通用格式（包括 MS-DOS (FAT)、ExFAT 等）支持呢？思路就是让 APFS 格式的 U 盘变成 Mac OS 扩展格式，这样它就能像之前那样支持完整格式的抹掉了。

第一步，把 U 盘插到电脑上，然后打开终端 app，输入指令 `diskutil list`。这时候，你就能在终端 app 中看到你电脑上所有内置和外置的磁盘信息。仔细阅读后，从中选择你想要抹掉的磁盘，记下「IDENTIFIER」信息。一般情况下，如果你只在电脑上插了一个 U 盘，那么它的「IDENTIFIER」为「disk2s2」。

![](.evernote-content/E40AC2CA-F4C7-4DEC-8AF6-3B9443F89B89/F4F74C79-A191-465A-A36B-74222E1784CF.jpg)

第二步，在终端 app 中输入指令 `sudo diskutil apfs deleteContainer /dev/IDENTIFIER`，将其中的 `IDENTIFIER` 替换为你在上一步记录下的信息，一般情况下为 `disk2s2`。这时候，终端 app 会提醒你输入管理员密码，按要求输入后「回车」即可。

![](.evernote-content/E40AC2CA-F4C7-4DEC-8AF6-3B9443F89B89/E99C9429-64B5-4F6A-9117-3071C30F465B.jpg)

重新回到磁盘工具 app，你会发现原来 APFS 格式的 U 盘已经被格式化为 Mac OS 扩展格式，当你想要抹掉它的时候，又可以开心地选择其它通用的格式了。

![](.evernote-content/E40AC2CA-F4C7-4DEC-8AF6-3B9443F89B89/0E37AE9B-0D1B-4B68-AE86-9998F1EEB790.jpg)

更多实用的 Mac 技巧：

* [让 macOS Mojave 在深色主题下依然显示浅色窗口 | 一日一技](https://beta.sspai.com/post/47265)
* [一条命令轻松解决 Mac 上「应用程序 “xxx” 不能打开」的问题 | 一日一技](https://beta.sspai.com/post/52828)
* [如何在 Safari 中长截图？| 一日一技](https://beta.sspai.com/post/44965)

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，了解更多 Mac 使用小技巧

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

---

[🌐 原始链接](https://sspai.com/post/55703)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7979ef6f-6f7d-4009-8cb2-39cd69641372/7979ef6f-6f7d-4009-8cb2-39cd69641372/)