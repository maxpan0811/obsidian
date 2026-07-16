---
title: "如何在Parallels Desktop for Mac中安装Parallels Tools"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在Parallels Desktop for Mac中安装Parallels Tools.md
tags: [印象笔记]
---

# 如何在Parallels Desktop for Mac中安装Parallels Tools

# 如何在Parallels Desktop for Mac中安装Parallels Tools --- 如何在Parallels Desktop for Mac中安装Parallels Tools 

---

# 如何在Parallels Desktop for Mac中安装Parallels Tools

---

如何在Parallels Desktop for Mac中安装Parallels Tools
----------------------------------------------

*2017-04-21*[Parallels](http://mp.weixin.qq.com/s?__biz=MzA5MDQwMjgxOQ==&mid=2649551170&idx=1&sn=6c8efb1e24f155088e094bc50839ae1e&chksm=8814682ebf63e1382d7042c33a8fe227bf3c5b772a61f7288a6213c9c4023c0e9fba3389250d&mpshare=1&scene=1&srcid=04214v4Quku34Q0tFX0KRZHr##)

![](.evernote-content/BB7F15CE-566C-43F1-AEE9-B822EB639777/7D65B7C2-C193-4360-BB53-FB006CCC9A36.jpg)

当你在Parallels Desktop for Mac中第一次设置虚拟机时，你可能会发现Parallels Tools被自动安装上了。是不是有那么一瞬间觉得这又是什么无良的捆绑软件，想要马上卸载掉它呢？小编可要为它喊冤啦，且听我慢慢介绍一下Parallels Tools到底是什么，为什么它对于Parallels Desktop中的Windows/Linux/Mac虚拟机而言如此重要？它为什么能自动安装？如何知道它已经安装完毕？以及万万不要轻易卸载哟~

**丨Parallels Tools是什么？**

Parallels Tools是一组安装在虚拟机中的客户机操作系统驱动程序(这是什么奇奇怪怪的名字) ，简单来说，它能帮助你轻松、高效地使用虚拟系统。

有了它，你就可以在虚拟机与Mac桌面之间流畅地移动鼠标，可以通过调整窗口大小来更改虚拟机屏幕分辨率，还能同步你的虚拟机时间和日期设置。与此同时，你的虚拟机还可以共享Mac的磁盘及文件夹，或者直接在Mac OS和虚拟机之间拖拽移动文件等等。

**丨没有安装Parallels Tools又会怎样？**

当然不会怎样了，你仍然可以顺利使用操作系统，但是智慧如你，怎么会错过这么好用又容易操作的工具呢~

**丨我如何知道是否已经安装了Parallels Tools？**

当Parallels Tools安装成功后，你可以在虚拟机与Mac设备之间自由移动光标；同时鼠标与键盘可以根据你的操作自动释放。还有一个简便方法就是启动你的虚拟机查看窗口状态栏。如果虚拟机窗口状态栏出现提示：“同时按住 Ctrl + Alt 来释放鼠标和键盘”，这意味着目前尚未安装Parallels Tools。也意味着你是不是应该做些什么了。

**丨Parallels Tools在Mac中的位置**

虽然多数情况下你不需要手动为Windows虚拟机定位Parallels Tools镜像，但如果出于某些不可抗因素而未能完成自动安装，那你或许需要知道Linux与Mac OS的镜像存放位置。以下是这些镜像的样子：

* prl-tools-win.iso——面向Windows客户机操作系统的Parallels Tools镜像
* prl-tools-lin.iso——面向Linux客户机操作系统的Parallels Tools镜像
* prl-tools-mac.iso——面向Mac OS X的Parallels Tools镜像

这些镜像可以在Mac设备的以下位置找到：

/Applications/Parallels Desktop.app/Contents/Resources/Tools

虽然你可能已经在虚拟机设置阶段安装了Parallels Tools，但还是让小编我为你逐一介绍一下需要执行的设置，以防它没有顺利安装到你的操作系统之中。

**丨如何在Windows虚拟机内安装Parallels Tools？**

1.启动你的虚拟机，并登录到Windows。

2.当Windows启动后，点击屏幕上方的Actions菜单（Parallels Desktop 10及之后版本），或者Virtual Machine菜单（Parallels Desktop 9及之后版本），并选择Install Parallels Tools。

![](.evernote-content/BB7F15CE-566C-43F1-AEE9-B822EB639777/F1317A42-F1AC-415A-9600-A9EABFE9EF5D.jpg)

3.打开CD-ROM，点击Parallels Tools，开始自动安装。

![](.evernote-content/BB7F15CE-566C-43F1-AEE9-B822EB639777/3C012EF6-1CA8-4A05-BA4D-F2EDF77DDEE2.jpg)

4.安装完成后，你的虚拟机将自动重启。

![](.evernote-content/BB7F15CE-566C-43F1-AEE9-B822EB639777/BB3F6F46-50DE-419B-A9AA-34E910572F42.jpg)

**丨如何在Linux虚拟机内安装Parallels Tools？**

1.启动Linux并打开Terminal窗口。

2. 获得管理员/root权限：

*sudo su or su*

3. 确保Linux虚拟机内的Make sure the DVD驱动器处于弹开状态：

*eject /dev/cdrom*

4.找到Parallels Desktop菜单栏>**Devices**>**CD/DVD**>**Connect image****…**

导航至*/Applications/Parallels Desktop/Contents/Resources/Tools.*

点击**prl-tools-lin.iso**然后点击**Open**.

5.将ParallelsTools镜像安装至Linux虚拟机：

*mkdir /media/cdrom*

*mount /dev/cdrom /media/cdrom*

6.确保磁盘镜像已经成功安装：

*ls /media/cdrom*

它应列出磁盘中的文件：

*install\*  installer/ install-gui\*  kmods/  tools/ version*

7.转到Parallels Tools镜像，并运行安装包：

*cd /media/cdrom*

*./install*

**丨如何在Mac OS虚拟机内安装Parallels Tools？**

1.启动虚拟机，并登录到客户机操作系统。

2.客户机操作系统启动后，通过屏幕上方的**Actions**菜单（ParallelsDesktop 10及以后版本）或者**Virtual Machine**菜单（Parallels Desktop 9及以后版本）选择**Install Parallels Tools**，连接Parallels Tools .iso镜像文件。

3.在虚拟机中，打开Parallels Tools并双击**Install**，开始安装。

4.在欢迎窗口中，点击**Continue**，并跟随安装向导提示。

5.当安装完成时，点击**Restart**退出助手，并重新启动你的虚拟机。

怎么样，对于Parallels Tools的认识是不是焕然一新，小编可是从功能介绍到安装指导为你提供了全方位立体化的服务，就算再不相信，也要给人家一个机会尝试下嘛。

长按二维码关注我们

![](.evernote-content/BB7F15CE-566C-43F1-AEE9-B822EB639777/CF59FE1E-9F65-4C9A-AC90-8C9AA605FC88.jpg)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzA5MDQwMjgxOQ==&mid=2649551170&idx=1&sn=6c8efb1e24f155088e094bc50839ae1e&chksm=8814682ebf63e1382d7042c33a8fe227bf3c5b772a61f7288a6213c9c4023c0e9fba3389250d&mpshare=1&scene=1&srcid=04214v4Quku34Q0tFX0KRZHr#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/387e4b4f-0045-4158-af2d-efdf42a9dce6/387e4b4f-0045-4158-af2d-efdf42a9dce6/)