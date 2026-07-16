---
title: "懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。.md
tags: [印象笔记]
---

# 懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。

# 懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。 --- 懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。 --------------------------- 原创 *2016-0

---

# 懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。

---

懒得整理混乱的桌面？让 Hazel 来帮你自动化管理。
---------------------------

原创
*2016-03-24*
*5key*
[Pinapps](#)

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/AA009C71-DDE1-450C-A788-406AE93CFAE9.webp)

我看过团队里很多人电脑，大家的桌面就像上面这张图一样布满了各种文件夹和文档。作为靠电脑吃饭的这样一群人每天都要处理大量各种文档，桌面上乱七八糟的其实很正常。但乱的结果就是找什么都不方便，还让电脑无谓的增加了很多垃圾信息。

也许你会考虑每隔一段时间进行一次整理，该挪的挪该删的删。时间久了你就会发现其实有很多操作是有规律的，是完全可以用机器来代替的。

以我自己的桌面管理为例，在工作中接触最多的无外乎是文档、设计稿、各种安装包压缩包以及各类图片等文件，因为赶时间可能都直接扔在桌面上。我希望电脑能帮我将它们归归类，不需要的直接删掉（如下图）。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/449DA464-7D43-453C-A212-20DA42C8A419.webp)

所以我需要一款工具能帮我根据文件的类型、添加的时间来进行一些自动化的操作。而着一些的操作我们可以借助今天的主角 Hazel 来完成。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/817019A4-D002-4CDE-A9D2-022D9F9B4647.webp)

如果大家尝试过在邮箱中设置收件规则，那么你对 Hazel 的操作很快就能上手。简单来说就是 Hazel 监控整个 Mac 硬盘，根据不同的规则匹配来自动化完成操作「If xxx then yyy」。

Hazel 依附在 OS X 的系统设置面板中，所有规则的建立都需要在这里完成。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/C0B8AE5F-C14E-47B7-B58D-9213E315C091.webp)

Hazel 的界面非常简单，左侧蓝色区域是规则所覆盖的文件夹范围；右侧黄色区域是具体规则及相应操作。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/FE72EF70-76CE-4FD5-BC51-DD780CF7D0C2.webp)

首先在左边选择一个需要自动化管理的文件夹，在这里以「桌面」为例进行讲解。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/7726ED47-5C5B-45C1-BE52-D3C6AC711032.webp)

然后在右侧开始添加执行规则，我在这里为「桌面」添加了5条不同的规则。每当桌面上出现一个新的文件时，Hazel 都会用这5条规则去扫一遍这个文件，一旦满足某一条系统将会自动执行相应的操作。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/CB04656B-6690-4188-9056-D2AC57E2C55F.webp)

先从一条简单文档归类开始。在「if」条件区域选择如果文件类型是 PDF，那么久将这个文件移动到桌面的「PDF」文件夹中。这样每次保存一个新的 PDF 文件到桌面时，Hazel 都会自动帮你归入「PDF」文件夹。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/5B50DCDA-6555-4F91-8F72-6FCABABC7F6D.webp)

保存之后我们可以点击窗口下方的预览 icon（小眼睛），Hazel 会告诉你目前桌面上那些文件是符合规则匹配的。规则在保存后很快就会执行，所以如果想先进行调试需要先将 rules 进行暂停。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/F38D4E25-F182-4BD5-85F3-E138176ACFD6.webp)

接下来我们可以再进一步（以 sketch 文档为例），如果我们不想立刻将文档归入相应的文件夹我们还可以增加一个时间条件（最后一次打开是在四天前）。这样 Hazel 就只会将最后一次打开是四天前的 sketch 文档归入相应的文件夹。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/AE0301B6-3EFA-4031-BCD7-B97A8DF4F9D8.webp)

附上一些我常用的规则。「move others type files to doc」将 dmg、sketch、pdf 之外的文件，三天内没有打开过的文件移入「doc」文件夹。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/71224076-0F7C-495E-A41C-72923C5C2F78.webp)

「upzip and move to trash」将新下载的 zip 文件解压，同时将压缩包移入垃圾箱。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/369AC947-9427-42C7-9FEA-CD7279013E03.webp)

将 OS X 的 app 安装文件移入 dmg 文件夹。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/7A822263-931D-4979-A2A4-D99D61125BC4.webp)

同时自动挂载安装包，并在一周后将安装包移入垃圾箱。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/B3F897F5-3B2E-42A2-B70D-2B6E92509CB3.webp)

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/070B3200-AC4E-4C21-B467-2D8374D8D513.webp)

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/2CF535BF-74AE-4EAC-9FD7-2B05D702E386.webp)

Hazel 在规则设置上的支持还是非常强大的，大家完全可以按照自己的需求进行定制。在配置好相应的规则后系统能自动将桌面上的文件管理得紧紧有条，我们只需要定期对文件夹里文档做整理就行了。

![](.evernote-content/56B2D009-1939-4E19-8D9A-EE0B1073CCBE/C6149469-F5AF-4DBC-B0D6-8244647E31F3.webp)

Hazel 是一款收费应用，售价29美金。售价不算便宜，但和它帮我们节省的时间比起来它还是非常的划算的。当然，你也可以到 Hazel 的官网下载试用版先进行一些尝试。

**试用版下载地址****：**

> https://www.noodlesoft.com/hazel.php

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&mid=402225457&idx=1&sn=c482221503b959da683566c0b53a4b10&scene=0&key=710a5d99946419d912dfd4e3c9268db4006965ceeaa7d7555a933ff0ba8ed921a762f6e523701c814d1d7f316b34b187&ascene=0&uin=MjM1ODc3OTE1&devicetype=iMac+MacBookPro11%2C1+OSX+OSX+10.11.4+build(15E65)&version=11020201&pass_ticket=mRhM59Yf8tFQhx%2FP2%2FFHEBeGoW2WRfXxCD1bMYkvLcw%3D)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3555d968-417c-4a4f-b631-36ac23e78aff/3555d968-417c-4a4f-b631-36ac23e78aff/)