---
title: 清除 macOS Finder 的「前往」(⌘ - shift - G) 记录 - 少数派
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/清除 macOS Finder 的「前往」(⌘ - shift - G) 记录 - 少数派.md
tags: [印象笔记]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "清除 macOS Finder 的「前往」(⌘ - shift - G) 记录 - 少数派"
source: evernote
type: note
export_date: 2026-06-25
guid: fcde85ea-3946-4632-a8a3-2cce0510b593
---

# 清除 macOS Finder 的「前往」(⌘ - shift - G) 记录 - 少数派

# 清除 macOS Finder 的「前往」(⌘

![](attachments/20a81d3617ffbc38.png)

清除 macOS Finder 的「前往」(⌘ - shift - G) 记录

作为一个强迫症患者，我最近发现 macOS 的访达会记录所有「前往」(⌘ - shift - G) 过的文件夹，而且「前往」的记录无法很方便地删除。不过，借助万能的搜索引擎，我还是找到了删除「前往」记录的办法，记录如下。

为了方便编辑 plist 文件，我们需要先在 Mac App Store 中下载 **Xcode**。

1. 打开 Xcode，在菜单栏中选择 File > Open…，然后按 ⌘ - shift - G，输入 `~/Library/Preferences/`，点击 Go

![](attachments/d147c9f72a4e9ade.png)

前往～/Library/Preferences/ 文件夹

2. 找到 `com.apple.finder.plist`，点击 Open

![](attachments/93412b4bfcf6b5ae.png)

打开访达配置文件

3. 清空 `GoToField` 的键值，删除 `GoToFieldHistory` 下的所有子项，按 ⌘ - S 保存，随后退出 Xcode

![](attachments/fdaa24292125bb7f.png)

清除 plist 文件中的「前往」记录

4. 点击左上角的 Apple 菜单 () > Force Quit… > Finder > Relaunch，重启访达

![](attachments/b5f5b4e177e96c1c.png)

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
