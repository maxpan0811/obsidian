---
title: "新MBP最大的秘密？ 在ARM芯片上运行iOS"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/新MBP最大的秘密？ 在ARM芯片上运行iOS.md
tags: [印象笔记]
---


![](.evernote-content/94E60A45-4F3B-4466-B0D3-BB5BF28B8351/3958C7AC-C7BE-4C15-91FC-B8E96D3BA4FB.jpg)

苹果刚刚发布了 MacBook Pro笔记本电脑，新的MacBook Pro有一个显示触摸屏。根据苹果开发者Steven Troughton-Smith深入挖掘显示触摸屏代码发现，这个触摸屏由一个单独的ARM处理器驱动，并且采用一个特殊的iOS操作系统和笔记本电脑的MacOS一起运行，但它不是你期望的那种iOS体验。这个操作系统是苹果Apple Watch智能手表WatchOS的修改版本，它本身是iOS的修改版本。这意味着MacBook Pro上的触摸显示屏独立于MacOS运行。

这个ARM处理器型号是T1，可能是苹果智能手表处理器S1的一个变种，T1在一个Ramdisk上运行特别版iOS，它通过USB接收像素缓冲区，MacOS通过USB发送帧缓冲区数据，然后T1将多点触摸事件中继回MacOS。

由于这个显示触摸屏也集成了Touch ID指纹传感器，因此需要一个安全的包围区来保护用

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->