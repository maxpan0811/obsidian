---
title: "知名开发者带你分析苹果APFS文件系统 (一)"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/知名开发者带你分析苹果APFS文件系统 (一).md
tags: [印象笔记]
---


在今年的 WWDC 大会上，苹果公布了一个为旗下所有 OS 打造的全新文件系统 APFS。尽管它在消费者眼中并不显眼，但作为取代现有 HFS+ 的方案，APFS 的出现势必会产生深远影响。曾经参与 ZFS 文件系统开发的 Delphix 公司 CTO Adam Leventhal 以一个开发者的角度来评价 APFS，分析我们即将会迎来什么：  
  
　**前言**

![](.evernote-content/9308E20E-6A41-4B0E-B7DB-66FAA38C18B5/43BCC2A4-D646-4225-8697-E06563D7CE07.jpg)

APFS，也就是 Apple File System（苹果文件系统），它的开发从 2014 年开始，Dominic Giampaolo 为首席工程师。APFS 不基于已有的东西，而是苹果从头打造的一个独立的系统。当 Giampaolo 被问到他有没有从 BSD 的 HAMMER，Linux 的 btrfs 或 OpenZFS 这些现代文件系统那里得到设计灵感时 —— 毕竟 APFS 想要实现的和它们的部分功能很相似 ——

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->