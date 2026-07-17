---
title: "macOS 效率进阶，学习如何用 AppleScript 实现自动化"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/macOS 效率进阶，学习如何用 AppleScript 实现自动化.md
tags: [印象笔记]
---


听 [Yvesss](https://sspai.com/user/63) 老师的建议修改了标题，原标题：「快速上手 macOS GUI Scripting: 基于 UI 元素的系统自动化控制」。

GUI Scripting 可以帮助你实现如下图一样的效果：打开记账软件，并在其中进行复杂繁琐的自动化录入操作——几乎所有点击操作都在瞬间完成。过程中，我实际进行的操作只有：激活这个脚本、输入消费金额和消费内容而已。

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/6F0465D6-4F1F-4E27-B8D5-2C53902F9F3E.gif)在 Money Pro 中录入一次消费

GUI Scripting 的原理很简单，就是利用脚本语言模拟鼠标键盘操作，进而控制系统 UI 元素。比如说，点击窗口中的某个按钮、在某个文本框里输入信息、以及获取窗口内特定区域的文本等等。这些可能单调繁琐的工作，你都可以用 GUI Scripting 来解放双手，实现无延迟的自动化。

本文介绍的是 macOS 下的 GUI Scri

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->