---
title: "简单制作 OS X Yosemite 10.10 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) _ 异次元软件下载"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/简单制作 OS X Yosemite 10.10 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) _ 异次元软件下载.md
tags: [印象笔记]
---

# 简单制作 OS X Yosemite 10.10 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) _ 异次元软件下载

# 简单制作 OS X Yosemite 10.10 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) | 异次元软件下载 --- 简单制作 OS X Yosemite 10.10 正式

---

# 简单制作 OS X Yosemite 10.10 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统) | 异次元软件下载

---

简单制作 OS X Yosemite 10.10 正式版U盘USB启动安装盘方法教程 (全新安装 Mac 系统)
========================================================

[ [技术教程](http://www.iplaysoft.com/category/tutorial) - [Mac](http://www.iplaysoft.com/os/mac-platform) // 2014-10-19 ]![](.evernote-content/7BA38E38-CE61-4F70-A5D4-9B9974AE1CD9/7F102CE6-C574-49CE-867E-B3DAC0A07CEB.jpg)

638,773

微博 腾讯 空间 微信      291.

186

伴随着 [iMac 5K Retina](http://www.iplaysoft.com/go/imacretina) 和新的 [Mac mini](http://www.iplaysoft.com/go/macmini) 等硬件的发布，[苹果](http://www.iplaysoft.com/tag/apple)终于都推出了 OS X Yosemite 系统正式版了！相信很多人都已经用上。不过对于一些不想升级，而是打算「全新安装」系统的朋友却遇到一个小问题。

那就是怎样制作 [OS X Yosemite 正式版](http://www.iplaysoft.com/osx-yosemite.html) 的U盘启动安装盘？其实方法比较简单，下面我们就给大家带来一个**制作 Yosemite U盘启动盘/安装盘的教程**吧。这样以后想给 [Mac](http://www.iplaysoft.com/os/mac-platform) 重装系统、在没有网络的情况下或者帮多台机器安装系统都方便得多……

### 简单制作 Mac OS X Yosemite 正式版 USB 启动盘的方法教程：

其实**制作 OS X Yosemite 正式版 USB 启动盘的方法**有很多，譬如使用命令行的，也有使用第三方工具的。这个[教程](http://www.iplaysoft.com/tag/%E6%95%99%E7%A8%8B)主要介绍前者，因为这是目前我了解到的最稳妥、简单，而且没有兼容性问题的方法了。

![](.evernote-content/7BA38E38-CE61-4F70-A5D4-9B9974AE1CD9/4195B912-19CE-427B-86B9-A36B1867C12B.jpg)

不过大家可别被「命令行」三个字吓到，其实你只需按步骤来，复制粘贴命令即可快速完成，事实上是很简单的。

### 一、准备工作：

1. 准备一个 8GB 或以上容量的 [U 盘](http://www.iplaysoft.com/go/upan)，确保里面的数据已经妥善[备份](http://www.iplaysoft.com/tag/%E5%A4%87%E4%BB%BD)好（该过程会抹掉 U 盘全部数据）
2. 从这里[下载苹果官方 OS X Yosemite 正式版的安装程序](http://www.iplaysoft.com/osx-yosemite.html) (可选 AppSotre 或网盘下载)
3. 如果你是从 Mac AppStore 下载的，下载完成后安装程序可能自动开始，这时先退出安装
4. 如从网盘下载的，请将解压后获得的 "Install OS X Yosemite.app" (显示为 "安装 OS X Yosemite.app") 移动到「应用程序」文件夹里面

### 二、格式化 U 盘：

插入你的 [U 盘](http://www.iplaysoft.com/tag/u%E7%9B%98)，然后在「应用程序」->「实用工具」里面找到并打开「磁盘工具」，或者直接用 Spotlight [搜索](http://www.iplaysoft.com/tag/%E6%90%9C%E7%B4%A2) “磁盘工具” 打开，如下图。

![](.evernote-content/7BA38E38-CE61-4F70-A5D4-9B9974AE1CD9/4FABB98C-994E-4B1F-A51E-C3DF283D3CB4.jpg)

* 1 - 在左方列表中找到 [U 盘](http://www.iplaysoft.com/go/upan)的名称并点击
* 右边顶部选择 2 -「分区」，然后在 3 -「分区布局」选择「1个分区」
* 在分区信息中的 4 -「名称」输入「iPlaySoft」 (由于后面的命令中会用到此名称，如果你要修改成其他(英文)，请务必对应修改后面的命令)
* 在「格式」中选择 5 -「Mac OS 扩展 (日志式)」
* 这时，先别急着点“应用”，还要先在 6 -「选项」里面，如下图

![](.evernote-content/7BA38E38-CE61-4F70-A5D4-9B9974AE1CD9/58A00D67-7E2E-49C6-A1D6-528A0DFC5144.jpg)

* 选择「GUID 分区表」，然后点击「好」
* 最后再点「应用」开始对 U 盘进行格式化。

### 三、输入终端命令开始制作启动盘：

* 请再次确保名为 “安装 OS X Yosemite” 的文件是保存在「应用程序」的目录中
* 在「应用程序」->「实用工具」里面找到「终端」并打开。也可以直接通过 Spotlight 搜索「终端」打开
* 复制下面的命令，并粘贴到「终端」里，按回车运行：

> sudo /Applications/Install\ OS\ X\ Yosemite.app/Contents/Resources/createinstallmedia --volume /Volumes/iPlaySoft --applicationpath /Applications/Install\ OS\ X\ Yosemite.app --nointeraction

回车后，系统会提示你输入管理员密码，接下来就是等待系统开始制作启动盘了。这时，命令执行中你会陆续看到类似以下的信息：

> Erasing Disk: 0%... 10%... 20%... 30%...100%...  
> Copying installer files to disk...  
> Copy complete.  
> Making disk bootable...  
> Copying boot files...  
> Copy complete.  
> Done.

当你看到最后有 「Copy complete」和「Done」 字样出现就是表示启动盘已经制作完成了！

### 四、U 盘启动安装 OS X Yosemite 的方法：

当你插入制作完成的 **OS X Yosemite U盘启动盘**之后，桌面出现「Install OS X Yosemite」的盘符那么就表示启动盘是正常的了。那么怎样通过 [USB](http://www.iplaysoft.com/tag/usb) 启动进行全新的系统安装呢？

其实很简单，先在目标电脑上插上 U 盘，然后重启你的 [Mac](http://www.iplaysoft.com/go/mac)，然后一直按住「option」(alt) 按键不放，直到屏幕显示多出一个 USB 启动盘的选项，如下图。

![](.evernote-content/7BA38E38-CE61-4F70-A5D4-9B9974AE1CD9/A5FCAA36-5849-4C3A-B55E-4A3C5F3479A1.jpg)

这时选择 U 盘的图标回车，即可通过 U 盘来安装 Yosemite 了！这时，你可以直接覆盖安装系统(升级)，也可以在磁盘工具里面格式化抹掉整个[硬盘](http://www.iplaysoft.com/tag/%E7%A1%AC%E7%9B%98)，或者重新分区等实现全新的干净的安装。

---

[🌐 原始链接](http://www.iplaysoft.com/osx-yosemite-usb-install-drive.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0f84ddba-1be1-4101-a6f2-becc08b775d6/0f84ddba-1be1-4101-a6f2-becc08b775d6/)