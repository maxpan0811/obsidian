---
title: "技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/技巧：通过 MacID，让 Mac 在锁屏或解锁时自动执行某操作.md
tags: [印象笔记]
---


![](.evernote-content/F1FC01CF-97DE-43A9-BA9F-85BADCC39BE8/2AEAB9F9-F205-49F8-B980-8F8A5EA36574.jpg)

MacID 是一款让你可以通过指纹识别、触控板手势等方法解锁 Mac 的应用。在少数派[此前的文章](http://sspai.com/32055)中，已和大家详细介绍过 MacID 的主要功能和使用方法。

你可能不知道的是，在 MacID 1.3 中，我们可以通过 AppleScript 对 MacID 进行扩展了。具体来说，你可以让 MacID 在 Mac 睡眠、唤醒、锁屏、解锁时，运行预先定义好的 AppleScript 脚本文件。举个例子，你可以让 Mac 锁屏时自动暂停 itunes 音乐播放，之后解锁 Mac 时再接着播放。

首先，什么是 AppleScript 呢？简单来说，AppleScript 是苹果开发的一种简单的脚本语言，可以用来控制运行于 Mac OS 上的部分程序，也可以写成独立运行的程序文件。

你可能会问，「我不知道如何写 AppleScript 脚本

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->