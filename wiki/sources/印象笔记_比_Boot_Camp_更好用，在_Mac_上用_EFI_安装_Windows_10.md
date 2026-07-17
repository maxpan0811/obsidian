---
title: "比 Boot Camp 更好用，在 Mac 上用 EFI 安装 Windows 10"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/比 Boot Camp 更好用，在 Mac 上用 EFI 安装 Windows 10.md
tags: [印象笔记]
---


**特别提醒：数据无价！请务必在动手前做好数据备份工作！**

为什么要使用 EFI 安装？
--------------

1、Boot Camp 会模拟旧电脑的 BIOS 环境（即 Legacy 模式）来引导 Windows ，这或多或少会造成性能损失。而大多数 Mac 以及 Windows 10 都是支持 EFI 启动的。（难道 Apple 是为了防止用户装 Windows ？）

2、使用 macOS 自带的 Boot Camp 助理安装 Windows 10 时，系统会把磁盘的分区表类型转换为 GPT+MBR 混合型（仅限 2015 年之前推出的 Mac ）。然而很多分区工具都无法识别这种 GPT+MBR 混合型分区表，在分区之后会导致分区表损坏，从而导致分区数据丢失。这是最致命的问题。使用 EFI 安装 Windows 10 之后，分区表类型不会被修改，因此可以在 Windows 10 下自由分区。

3、使用 EFI 安装 Windows 10 之后可以使用快速启动功能。

4、玩外接显卡的朋友应该知道，使用 Boot Camp 引导由于有 32 位寻址的限制从而使显卡出

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->