---
title: "利用 Hazel 和 Automator 自动转换文件格式"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/利用 Hazel 和 Automator 自动转换文件格式.md
tags: [印象笔记]
---

# 利用 Hazel 和 Automator 自动转换文件格式

# 利用 Hazel 和 Automator 自动转换文件格式 --- 利用 Hazel 和 Automator 自动转换文件格式 ============================= [![]

---

# 利用 Hazel 和 Automator 自动转换文件格式

---

利用 Hazel 和 Automator 自动转换文件格式
=============================

[![](.evernote-content/95CE1DC3-E0DD-4424-B0C7-5B4D908BBA54/91385590-683B-4839-AF92-3F9CCECA5EF1)](https://sspai.com/user/666443)

#### [vanilla2w](https://sspai.com/user/666443)

2016年08月24日

5  [0](#)

目录

Hazel 这个之前一直不温不火的软件最近突然在少数派火了起来，究其原因，应该是缘于来自 Matrix 的一篇文章，之后来自 @JailbreakHum 的 「把你的 iOS 设备变成控制 Mac 的「遥控器」」再次将这股 Hazel 热推向了高潮。于是，好久没发文的我也来凑个热闹，希望郭老师看到后不会嫌弃我好久没写稿了。

今天，我以转换 PDF 格式为例，讲一讲如何利用 Hazel 和 Automator 自动转换文件格式。

在 iOS 上，我们常用的转换 PDF 格式的方法包括但不限于如下几个：

- 利用 Share Sheet 里 Save PDF to iBooks 这个动作；

- 利用 Workflow 里 Make PDF 这类 workflow；

- 使用 Readdle 家的 PDF Converter 这个应用。

因为我平时有很多课程的课件都是 .pptx 格式的，但是在 PowerPoint 上批注很不方便，所以我需要讲这些课件一一转换为 PDF 文件。 在我的 iPad Pro 上，我会在 PDF Expert 上将我放置课件的文件夹设置为同步文件夹，打开预先下载好的 PPT 课件后，我只需点击右上角分享菜单里的 「Convert to PDF」，这个 PPT 课件会通过 PDF Converter 自动转换为 PDF 文件并上传到与原文件相同的文件夹。所以对我来说，在 iOS 设备上转换 PDF 格式还是比较方便的。

但是在 Mac 上情况就稍显复杂了。在用 PowerPoint 打开课件后，我需要依次点击 「File」-「Export」-「File Format」-「PDF」-「Where」，然后经过点击层层文件夹选中该 PPT 课件所在的文件夹。

一次次重复无意义的操作让我感到十分不爽，于是就开始琢磨如何让这一工作流自动化。

接下来让我们以下图中的这个课件为例。

![](.evernote-content/95CE1DC3-E0DD-4424-B0C7-5B4D908BBA54/5ED2F05D-E537-49A1-88F0-18F78BF8B400)

首先，我们在 Hazel 里建立一个这样的规则。

![](.evernote-content/95CE1DC3-E0DD-4424-B0C7-5B4D908BBA54/EB929B6C-12EA-42C3-B939-4B7B662ABD31)

接着，我们需要使用 Automator 创建一个 workflow，如下图所示。

![](.evernote-content/95CE1DC3-E0DD-4424-B0C7-5B4D908BBA54/81CD5154-285F-43C4-A56A-2A22ECCD3EEF)

AppleScript 的代码如下：

![](.evernote-content/95CE1DC3-E0DD-4424-B0C7-5B4D908BBA54/635B8BEB-DEEF-4AFD-8C5D-BF71B0F0CAE3)

下载地址：<http://vanilla2wilight.d.pr/14nez>

建好后将这个 workflow 保存到本地任意位置，保存到 iCloud Drive 会导致 Hazel 无法读取。

最后，就是围绕这个 workflow 建立另外一个 Hazel 的规则了。

![](.evernote-content/95CE1DC3-E0DD-4424-B0C7-5B4D908BBA54/AF031B1A-D027-4C97-B460-ABB3BBF3C322)

最终效果就是点击下载这个课件后，这个课件储存到了 「Documents」这个文件夹， 然后通过第一个 Hazel 的规则自动归档到相应的文件夹里，接着运行第二个 Hazel 的规则，自动启动 Microsoft PowerPoint，执行导出为 PDF 这个动作，并保存到相应的文件夹。（提示：在转换时可能会提醒要求获取文件权限，点击获取即可。）

这个例子只是抛砖引玉，大家还可以通过修改 AppleScript 来完成其他格式之间的转换，也希望借此能够激发大家的灵感，踊跃讨论，并吸引更多的人参与到利用 Hazel 提高效率的实践和探索中来。

---

[🌐 原始链接](https://sspai.com/post/33808)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e54af7d2-c3a5-47e0-9cdd-a336ace3b1aa/e54af7d2-c3a5-47e0-9cdd-a336ace3b1aa/)