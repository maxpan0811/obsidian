# 为 OS X （EI Captain）创建可引导安装器

---

为 OS X 创建可引导安装器
===============

有了 OS X El Capitan、Yosemite 或 Mavericks，您就可以将 USB 闪存驱动器或其他可移动介质用作从中安装 OS X 的启动磁盘。

以下高级步骤主要适用于系统管理员以及熟悉命令行的其他人员。

sudo /Applications/Install\ macOS\ Sierra.app/Contents/Resources/createinstallmedia --volume /Volumes/install --applicationpath /Applications/Install\ macOS\ Sierra.app --nointeraction

在“终端”中使用“createinstallmedia”命令
------------------------------

1. 从 Mac App Store 下载 OS X 安装器。如果下载完成后安装器自动打开，请退出。安装器将位于您的“应用程序”文件夹中。
2. 装载 USB 闪存驱动器或其他宗卷。您也可以使用内部备用分区。
3. 打开“终端”应用，它位于“应用程序”文件夹的“实用工具”文件夹中。
4. 在“终端”中使用“`createinstallmedia`”来创建可引导安装器。有关该命令的示例请见[下一部分](https://support.apple.com/zh-cn/HT201372#examples)。有关详细的使用说明，请确保相应的“安装 OS X”应用位于您的“应用程序”文件夹中，然后在“终端”中输入以下任一路径：

El Capitan 的路径：

```
/Applications/Install\ OS\ X\ El\ Capitan.app/Contents/Resources/createinstallmedia
```

Yosemite 的路径：

```
/Applications/Install\ OS\ X\ Yosemite.app/Contents/Resources/createinstallmedia
```

Mavericks 的路径：

```
/Applications/Install\ OS\ X\ Mavericks.app/Contents/Resources/createinstallmedia
```

示例
--

以下是这个命令的基本语法。将“volumepath”替换为您的 USB 闪存驱动器或其他宗卷的相应路径，并将“installerpath”替换为“安装 OS X”应用的相应路径。

```
createinstallmedia --volume volumepath --applicationpath installerpath
```

以下示例均假设 OS X 安装器已位于您的“应用程序”文件夹中，并且您的 USB 闪存驱动器或其他宗卷的名称为“abc”：

El Capitan 的示例：

```
sudo /Applications/安装\ OS\ X\ EI\ Capitan.app/Contents/Resources/createinstallmedia --volume /Volumes/abc --applicationpath /Applications/安装\ OS\ X\ EI\ Capitan.app
```

Yosemite 的示例：

```
sudo /Applications/Install\ OS\ X\ Yosemite.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume --applicationpath /Applications/Install\ OS\ X\ Yosemite.app
```

Mavericks 的示例：

```
sudo /Applications/Install\ OS\ X\ Mavericks.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume --applicationpath /Applications/Install\ OS\ X\ Mavericks.app
```

上次修改时间： 2015-10-27

---

[🌐 原始链接](https://support.apple.com/zh-cn/HT201372)

[📎 在印象笔记中打开](evernote:///view/207087/s1/dc72caed-2a8d-4560-af9a-9614ea642d8a/dc72caed-2a8d-4560-af9a-9614ea642d8a/)