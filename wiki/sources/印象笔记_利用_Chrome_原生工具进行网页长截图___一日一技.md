---
title: "利用 Chrome 原生工具进行网页长截图 _ 一日一技"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/利用 Chrome 原生工具进行网页长截图 _ 一日一技.md
tags: [印象笔记]
---

# 利用 Chrome 原生工具进行网页长截图 _ 一日一技

# 利用 Chrome 原生工具进行网页长截图 | 一日一技 --- 利用 Chrome 原生工具进行网页长截图 | 一日一技 ============================ [![](.e

---

# 利用 Chrome 原生工具进行网页长截图 | 一日一技

---

利用 Chrome 原生工具进行网页长截图 | 一日一技
============================

[![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/F4AAC013-CE85-4500-BD06-2BF616670070.jpg)](https://sspai.com/user/713147)

#### [Umi](https://sspai.com/user/713147)

12月08日

128  [24](#)

之前试用 Firefox Quantum 时，我最喜欢的特性之一就是其自带的截图功能。它不仅可以自动检测网页元素边界，还能轻松保存整个网页，十分方便。

后来由于扩展及习惯等原因，我又换回了 Chrome，但还是对该功能念念不忘。尽管商店里也有许多截图增强扩展，但在截取一些比较复杂的网页时，往往会出现元素错位、重复的现象。经过一番探索，我发现 Chrome 开发者工具中其实自带了截图命令，效果也令人满意，在这里分享给大家。

要想使用截图功能，你需要首先确保 Chrome 已升级至 59 或更高版本。在想要截图的网页中，首先按下 `⌘Command + ⌥Option + I`（Windows 为 `F12`）快捷键，召唤出调试界面。

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/6E96BF40-3CD8-43CD-8375-CDAFF7705C1E.png)

  
随后，按下 `⌘Command + ⇧Shift + P`（Windows 为 `Ctrl + Shift + P`），输入命令 `Capture full size screenshot`（只输前几个字母就能找到），敲下回车，Chrome 就会自动截取整个网页内容并保存至本地。由于是渲染引擎直接输出，其比普通扩展速度更快，分辨率也更高。  

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/1D105DBC-772F-4382-8606-55095C5D55B3.png)

  

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/32A46A3A-8A5A-4C2D-B12B-D5E8DA820078.png)

  
除了普通长截图以外，你还可以利用这一功能截取手机版网页长图。只需要按下 `⌘Command + ⇧Shift + M` （Windows 为 `Ctrl + Shift + M`）模拟移动设备，再按刚才的方法运行命令就可以了。在顶部的工具栏中，你可以选择要模拟的设备和分辨率等设置。  

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/20474664-EC99-4D57-9054-B1C0414A5892.png)

  

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/89C3B049-7958-4451-BD8A-8450DEBADA7C.png)

  
如果你想准确截取网页的某一部分，可以按下 `⌘Command + ⇧Shift + C`（Windows 为 Ctrl + Shift + C）嗅探元素。选中想要的部分后，再运行 `Capture node screenshot` 命令，一张完美的选区截图就诞生了。  

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/9F38B956-3B6A-4D99-8473-313F065A9B20.png)

  

![](.evernote-content/A8943775-0018-4D37-90D0-B6374423CA87/0D72EF72-1472-4EB4-9CE8-091FD942704D.png)

  
此外，`Capture screenshot` 命令可以让你截取当前网页的可视部分。我也会继续发掘 Chrome 开发者工具的其它好玩用法，到时推荐给大家

---

[🌐 原始链接](https://sspai.com/post/42193)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f2d29b7c-5557-4fe4-ab93-332d76fdfbe9/f2d29b7c-5557-4fe4-ab93-332d76fdfbe9/)