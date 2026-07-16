---
title: "新MBP最大的秘密？ 在ARM芯片上运行iOS"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/新MBP最大的秘密？ 在ARM芯片上运行iOS.md
tags: [印象笔记]
---

# 新MBP最大的秘密？ 在ARM芯片上运行iOS

# 新MBP最大的秘密？ 在ARM芯片上运行iOS --- ![](.evernote-content/94E60A45-4F3B-4466-B0D3-BB5BF28B8351/3958C7AC-C7

---

# 新MBP最大的秘密？ 在ARM芯片上运行iOS

---

![](.evernote-content/94E60A45-4F3B-4466-B0D3-BB5BF28B8351/3958C7AC-C7BE-4C15-91FC-B8E96D3BA4FB.jpg)

苹果刚刚发布了 MacBook Pro笔记本电脑，新的MacBook Pro有一个显示触摸屏。根据苹果开发者Steven Troughton-Smith深入挖掘显示触摸屏代码发现，这个触摸屏由一个单独的ARM处理器驱动，并且采用一个特殊的iOS操作系统和笔记本电脑的MacOS一起运行，但它不是你期望的那种iOS体验。这个操作系统是苹果Apple Watch智能手表WatchOS的修改版本，它本身是iOS的修改版本。这意味着MacBook Pro上的触摸显示屏独立于MacOS运行。

这个ARM处理器型号是T1，可能是苹果智能手表处理器S1的一个变种，T1在一个Ramdisk上运行特别版iOS，它通过USB接收像素缓冲区，MacOS通过USB发送帧缓冲区数据，然后T1将多点触摸事件中继回MacOS。

由于这个显示触摸屏也集成了Touch ID指纹传感器，因此需要一个安全的包围区来保护用户付款信息。这是在苹果的T1处理器的帮助下完成。有趣的是，MacBook Pro前置摄像头出于安全原因，也连接到T1芯片

MacBook Pro这种双处理器双操作系统设计显示，苹果正在Mac上实验ARM处理器，即使这些定制芯片被降级到仅主管特定的功能，不能运行整个系统。

[阅读全文](http://www.feng.com/iPhone/news/2016-10-29/New-MBP-biggest-secret_660600.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2016-10-29/New-MBP-biggest-secret_660600.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/96ca3d82-575c-44aa-84b3-b06b22f38cb0/96ca3d82-575c-44aa-84b3-b06b22f38cb0/)