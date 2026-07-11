# 清除 macOS Finder 的「前往」(⌘ - shift - G) 记录 - 少数派

---

清除 macOS Finder 的「前往」(⌘
=======================

![](.evernote-content/6A60A124-E27D-4927-B156-85CD0E7B0579/F507BB00-1B4A-48AC-AE2E-16F9A6048AB7)

清除 macOS Finder 的「前往」(⌘ - shift - G) 记录

作为一个强迫症患者，我最近发现 macOS 的访达会记录所有「前往」(⌘ - shift - G) 过的文件夹，而且「前往」的记录无法很方便地删除。不过，借助万能的搜索引擎，我还是找到了删除「前往」记录的办法，记录如下。

为了方便编辑 plist 文件，我们需要先在 Mac App Store 中下载 **Xcode**。

1. 打开 Xcode，在菜单栏中选择 File > Open…，然后按 ⌘ - shift - G，输入 `~/Library/Preferences/`，点击 Go

![](.evernote-content/6A60A124-E27D-4927-B156-85CD0E7B0579/08AE2207-2B99-4447-9CCC-672CA9C25F2D.png)

前往～/Library/Preferences/ 文件夹

2. 找到 `com.apple.finder.plist`，点击 Open

![](.evernote-content/6A60A124-E27D-4927-B156-85CD0E7B0579/076460BD-3EED-47DE-878D-594BBEFA1FBA.png)

打开访达配置文件

3. 清空 `GoToField` 的键值，删除 `GoToFieldHistory` 下的所有子项，按 ⌘ - S 保存，随后退出 Xcode

![](.evernote-content/6A60A124-E27D-4927-B156-85CD0E7B0579/6FF6752A-5059-4B24-B5E7-E95E48F87586.png)

清除 plist 文件中的「前往」记录

4. 点击左上角的 Apple 菜单 () > Force Quit… > Finder > Relaunch，重启访达

![](.evernote-content/6A60A124-E27D-4927-B156-85CD0E7B0579/9A4758E3-0F3C-4A40-8802-5247CAB3CB22.png)

重启访达

这时打开访达就可以发现，「前往」记录被成功清除了。

12

1

[路中南](https://sspai.com/u/LuZhNan/updates) 等 1 人为本文章充电

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/57560)

[📎 在印象笔记中打开](evernote:///view/207087/s1/fcde85ea-3946-4632-a8a3-2cce0510b593/fcde85ea-3946-4632-a8a3-2cce0510b593/)