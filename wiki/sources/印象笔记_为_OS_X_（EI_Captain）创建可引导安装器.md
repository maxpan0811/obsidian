---
title: "为 OS X （EI Captain）创建可引导安装器"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/为 OS X （EI Captain）创建可引导安装器.md
tags: [印象笔记]
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

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->