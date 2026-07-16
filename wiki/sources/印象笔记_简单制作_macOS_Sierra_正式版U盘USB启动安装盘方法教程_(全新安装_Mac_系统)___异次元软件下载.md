---
title: "简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) _ 异次元软件下载"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) _ 异次元软件下载.md
tags: [印象笔记]
---

# 简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) _ 异次元软件下载

# 简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) | 异次元软件下载 --- 简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教

---

# 简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) | 异次元软件下载

---

简单制作 macOS Sierra 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统)
=================================================

** [备份恢复](http://www.iplaysoft.com/category/backup-restore), [系统工具](http://www.iplaysoft.com/category/system)  **  [Mac](http://www.iplaysoft.com/os/mac-platform)  ** 2016-09-25

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/09D3EE06-458F-4786-AB9A-0BC6D0A7D278.jpg)

243,894

微博 腾讯 空间 微信      68.

0

随着苹果 [macOS Sierra 正式版](http://www.iplaysoft.com/macos-sierra.html)发布，很多[使用 Mac 电脑](http://www.iplaysoft.com/go/mac)的同学都已升级到最新版系统了。但如果你对系统有洁癖或原本系统已凌乱不堪，那么可能还是希望能格式化「**全新安装 macOS Sierra**」的。

不过由于[苹果官方](http://www.iplaysoft.com/go/apple)只提供了 macOS Sierra 的[升级](http://www.iplaysoft.com/tag/%E5%8D%87%E7%BA%A7)程序，而没提供完整的镜像，想要全新安装的话，只能自己制作一个 macOS Sierra 的U盘启动盘/安装盘了。今天异次元就给大家提供一个简单的制作[教程](http://www.iplaysoft.com/tag/%E6%95%99%E7%A8%8B)，这样以后给 Mac 重装系统、在没网络的情况下给多台机器[装机](http://www.iplaysoft.com/tag/%E8%A3%85%E6%9C%BA)都方便许多……

[**访问：Apple 中国官网](http://www.iplaysoft.com/go/apple)

相关阅读：[简单几步制作 Windows 10 USB 启动安装盘图文教程](http://www.iplaysoft.com/windows-10-udisk-install.html)

### 方法一：使用命令行创建制作 macOS Sierra 正式版 USB 安装盘

制作 **macOS Sierra** 正式版 [USB](http://www.iplaysoft.com/tag/usb) 启动盘的方法有很多，用户可以选择使用命令行来创建，也可以选择第三方U盘制作工具来制作，大家可以根据自己的喜好选择。

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/2819C3AC-B99A-44D2-9DC3-C9705A72DD16.jpg)

本教程首先介绍命令行的方式，因为这是苹果官方系统内置的命令，优点是稳妥而且没有兼容性问题，只是需要通过命令行操作，对新手来说可能看似有点复杂，但其实步骤还是非常简单的。

1. 首先，准备一个 [8GB 或更大容量的 U盘](http://www.iplaysoft.com/go/upan)，并[备份](http://www.iplaysoft.com/tag/%E5%A4%87%E4%BB%BD)好里面的所有资料。
2. [下载好 macOS Sierra 正式版的安装程序](http://www.iplaysoft.com/macos-sierra.html)
3. 打开 “应用程序 → 实用工具 → 磁盘工具”，将U盘「抹掉」(格式化) 成「Mac OS X 扩展（日志式）」格式、GUID 分区图，并将U盘命名为「Sierra」。(注意：这个盘符名称将会与后面的命令一一对应，如果你改了这盘符的名字，必须保证后面的命令里的名称也要一致。)  
   ![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/F4DFAED9-CED3-4482-939E-E3F2EA5CB333.jpg)
4. 打开 “应用程序→实用工具→终端”，将下面的一段命令复制并粘贴进去：  
   sudo /Applications/Install\ macOS\ Sierra.app/Contents/Resources/createinstallmedia --volume /Volumes/Sierra --applicationpath /Applications/Install\ macOS\ Sierra.app --nointeraction
5. 回车并执行该命令，这时会提示让你输入管理员密码，便会开始制作过程了：  
   ![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/9B5ED4EA-983B-4320-BFD8-53BA69B6FA5A.jpg)
6. 如上图，这时系统已经在制作中了，请耐心等待直到屏幕最后出现 Done. 字样即表示大功告成了！然后，就带着[U盘](http://www.iplaysoft.com/tag/U%E7%9B%98)出去浪吧……

### 方法二：使用 DiskMaker X 启动盘制作工具：

如果你不喜欢任何[代码](http://www.iplaysoft.com/tag/%E4%BB%A3%E7%A0%81)、命令之类的操作，那么除了上面使用命令行来制作 macOS 的启动/安装盘的方法外，我们也有更加傻瓜直观一点的方法，那就是通过 **DiskMaker X** 工具来制作 macOS 安装U盘。

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/9768822C-72AB-4BF1-B629-C141B2674F6A.jpg)

[Diskmaker X](http://www.iplaysoft.com/macos-usb-install-drive.html) 是一款免费的 **macOS USB 启动盘制作软件**，当然前提也是要先[下载好 macOS Sierra 正式版的安装程序](http://www.iplaysoft.com/macos-sierra.html)。DiskMakerX 支持制作 macOS Sierra / OS X Yosemite / El Capitan 等不同版本的系统安装盘，启动后会让你选择，这里我们选择 macOS Sierra (10.12)。

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/456F3E3A-DE7A-472D-8E72-508B0F852487.png)

如果你已经下载好 macOS 的安装程序，那么正常情况下，Diskmaker X 会自动帮你找到其路径的，点击 Use This Copy 继续下一步：

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/716C9F89-71B5-4BB2-B25E-682D96DF5677.png)

之后，DiskMaker X 会提示你需要一个至少 [8GB 容量的U盘](http://www.iplaysoft.com/go/upan)，将 U 盘插入 Mac 之后，点击 “An 8 GB USB thumb drive” 按钮下一步

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/777D5063-6BEF-4D14-A324-5318ACF6025B.png)

这时会出现选择 U 盘盘符的窗口（请注意千万不要选错盘符哦！！）：

![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/772E4DD2-9F57-4978-9193-1C7A46CC18F5.jpg)

确认格式化并抹除 U盘 (Erase then create the disk)，然后就开始一条龙制作过程了。

### 通过 U 盘安装 macOS Sierra / 格式化重装 (抹盘全新安装系统) 方法

当你制作好 macOS Sierra 的安装盘 U 盘之后，你就可以利用它来给 [Mac 电脑](http://www.iplaysoft.com/go/mac)格式化重装 (抹盘安装)了。操作的方法非常简单：

1. 当然还是要想办法[备份](http://www.iplaysoft.com/tag/%E5%A4%87%E4%BB%BD)好 Mac 里所有的重要数据了。
2. 插上制作好的安装U盘，如果系统能识别出来即可，这时我们先关机了。
3. 按下电源键开机，当听到“噹”的一声时，按住 Option 键不放，直到出现启动菜单选项：  
   ![](.evernote-content/1056882B-7DA4-4FBD-977C-20FF32D6C36D/33C6B47E-78AF-4D91-A976-87D75610A4C3.jpg)
4. 这时选择安装U盘 (黄色图标) 并回车，就可以开始安装了，在过程中你可以通过“磁盘工具”对 Mac 的磁盘式化或者重新分区等操作。
5. 之后就是一步一步的安装直到完成了。

### 相关文件下载地址：

官方网站：[访问](http://www.iplaysoft.com/go/apple)  
软件性质：免费

[下载 DiskMaker X 启动盘制作工具 (Mac)](http://dl.iplaysoft.com/files/3948.html)  |  [下载 macOS Sierra](http://www.iplaysoft.com/macos-sierra.html)  |  [更多 Mac 相关](http://www.iplaysoft.com/os/mac-platform)

---

[🌐 原始链接](http://www.iplaysoft.com/macos-usb-install-drive.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/dcf09945-da0c-401a-aab3-bd5321aa2a1b/dcf09945-da0c-401a-aab3-bd5321aa2a1b/)