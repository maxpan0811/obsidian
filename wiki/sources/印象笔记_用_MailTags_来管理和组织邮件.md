---
title: "用 MailTags 来管理和组织邮件"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/用 MailTags 来管理和组织邮件.md
tags: [印象笔记]
---

# 用 MailTags 来管理和组织邮件

# 用 MailTags 来管理和组织邮件 --- ![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/4A30DAB2-F312-4

---

# 用 MailTags 来管理和组织邮件

---

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/4A30DAB2-F312-4AAC-8AF7-197D9882F8C8.jpg)

Microsoft Outlook 一直是自己处理公司邮件的首选，因为它能方便的给邮件添加日程和分类，这在处理大量邮件时尤其有用。切换到 Mac 平台后没有太好的选择，一方面是 Office for Mac 总是问题多多，另一方面又不想放弃 OS X 原生的 Mail 应用。MailTags 这款 Mail 扩展插件的出现解决的这种选择上的困扰，安装 MailTags 后 Mail 中不仅可以添加日程和标签进行分类，而且 MailTags 还完美的契合到 Mail 的各种功能体系当中，排序、搜索、边栏以及规则定义。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/C28B8723-2A7E-4BCA-94A6-16E23CF0E2A5.jpg)

整合到 Mail 的 MailTags 会体现在几个地方：

1. 边栏，MailTags 提供了三种邮件分组管理模式，关键词（Keywords）、项目（Projects）、预定日期（Tickle dates），关键词这个很好理解，安装好 MailTags 后邮件中会新增一个 Tag 栏，收到的或者新建邮件都能很方便的添加关键词标签；
2. 邮件排序，除了 Mail 原来的排序项目外，MailTags 带来了关键词（Keywords）、项目（Projects）、预定日期（Tickle dates）以及重要性（Importtance）几种排序方式；
3. 标签栏，收到或新建邮件中新增了标签栏，已添加的标签（标签栏左侧）、预定日期、优先级（标签栏右侧）都会显示在这里；
4. 搜索，可对关键词、项目、备注内容进行搜索，搜索的结果和 Mail 一样可保存为智能邮箱；
5. 详细定义，标签详细设置的入口，正文区域点击 MailTags 的图标、邮件列表的右键菜单、或者由工具栏上的图标进入。

MailTags 的功能主要是三个部分：给邮件添加「关键词」标签、设定「预定日期」、添加「备注」。所有这些功能都是基于 MailTags 实现的，发送邮件时如果勾选「Include Tags In Sent Message」，其他 MailTags 用户可以看到你设定的关键词和备注，反之，没有安装 MailTags 的邮件客户端查看或收到的邮件不会包含MailTags 创建的这些信息。

MailTags 的目的是协助用户对邮件进行类似于 GTD 的管理，通过关键词来分类和筛选邮件，通过设定日程和任务来保持对邮件事件的跟进，在自动化处理上可以利用 Mail 中的规则来定义各种条件。

关键词（Keywords）
-------------

MailTags 安装后工具栏和邮件正文中的快捷图标栏上都会新增一个标签图标，直接点击或者选中邮件后按快捷键 ⌃⌘T 都可以打开标签添加界面。标签添加窗口的内容和 MailTags 偏好设置关键词部分的内容是对应和一致的，以偏好设置中的项目为例在此做一些说明。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/523CA7A4-AE35-47C9-9E7C-4225CA2A2A42.jpg)

关键词有四个供选择的来源，自定义的 Keywords，来自邮件服务提供商的 Labels，来自系统 Finder 的 Tags，以及来自团队共享链接的文本（Hosted Keywords）。

Keywords 是 MailTags 中关键词自定义的主体，当前可用的关键词和标签都会显示在这里，设置并勾选了「Include hosted keywords from」后，Keywords 列表中还会显示来自团队共用的标签（关键词标签右侧有三个圆点表示区别）。勾选「FinderTags」后会显示来自 Finder 的标签，Labels 的标签来自与邮件服务提供商的设置，例如，Gmail 中自定义了标签 MailTags 可以读取过来显示在这里。

团队成员共享标签（Hosted Keywords），具体设置方法如下：

* 首先在 Keywords 中添加供团队使用的标签；
* 添加完成后选中这些标签，点击下方的齿轮⚙设置按钮，选择 export 导出为（仅导出选中项）一个单独的文件；
* 将导出的文件移动到 Dropbox 文件夹，右键获取「复制公共链接」；
* 在「Include hosted keywords from」中粘贴 Dropbox 公共链接，并勾选启用此项。

> MailTags 中的关键词标签是服务于邮件发起的任务管理和事项跟踪的，所以在添加关键词的时候不用有什么顾虑，可以任意添加便于记忆和检索的标签。一段时间后我们会发现很多标签随着邮件的归档和删除后变得没啥实际意义了，这时只需在 Keywords 设置中选择执行一次「Collect Keywords」（关键词收集）的操作就又变的干净清爽了，当前邮件没有采用的 Keywords 标签都会被清理（Hosted Keywords 例外）。

你或许也注意到了默认的关键词中还有 @Waiting 这样的标签，它的作用是用来跟踪邮件的后续操作的，发送一封邮件时如果你添加了 @Waiting 标签，当这封邮件被回复时 MailTags 会弹出系统通知来告知你，而且会将邮件归类到智能邮箱「Tickle Dates」的「Awaiting Reply」中，已经被回复的邮件中原来的 @Waiting 标签会被自动替换成 @reply。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/4C05E083-E027-478B-BDB7-81CC89C09331.jpg)

@Waiting 和 @reply 这两个特殊的标签是由偏好设置中指定的，当然你也可以修改成其他的特定标签。这里只是 MailTags 在自动化上的一个内置定义，其他针对邮件的自动化操作可以通过添加规则来实现，在规则的定义中，MailTags 的诸多项目都可以作为条件来进行判断。

项目（Projects）
------------

项目标签比关键词标签的层级要高，但是在作用上并没有本质的差别，可以和关键词混合使用也可以单独使用，所以项目标签下可以并列设置关键词标签或者只有项目标签，搜索时可以区分定位。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/90705494-264B-4013-A31C-51E1AA411D48.jpg)

给邮件添加项目标签主要是便于在项目管理层级上对文件、邮件等系列内容的统筹标识，所以我们在设置中看到 MailTags 支持读取 OmniFocus 项目分类就顺理成章了。外部项目名称（External Projects）的读取，除了 OmniFocus 以外还支持 The Hit List 和 Things。

预定日期（Tickle dates）
------------------

预订日期的设定可以帮助我们将邮件转化为待办事项。预定日期，也就是预定任务要被执行的日期。把它理解成添加为日程也可以，默认提供了一段时间后（如：3天）、星期几（如：周五）、某天（点击日历图标）三种选择方式。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/E676DE5A-95A8-4969-BE5E-033639342C76.jpg)

偏好设置中可以定义时间点和具体的时间周期，Tickle 的详细设置中还能基于邮件添加 Calendar 事件（Event）和任务（Task）。添加了 Tickle 的邮件不仅在时间点时会触发系统通知，而且边栏的 Tickle Dates 中也会体现出来。

为了方便操作，我们可以将边栏中的 Tickle 子项可以拖动到顶栏上，例如，Today、Awaiting Reply，这样即便在隐藏边栏的视图中也能直观的看到待办和需要跟进的邮件。

备注
--

MailTags 的备注内容只会显示在安装有 MailTags 的客户端，是关键词、标签以外对邮件的详细描述。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/EE22C761-9713-4BA3-9BE6-54F6279B22EE.jpg)

备注（Note）内容默认会以浅黄色背景的方式出现在邮件标题的下方，如果你勾选「Show note as subject」，备注还可以作为邮件的子标题出现在邮件列表当中。

邮件列表中选中邮件后，通过右键菜单「Toggle Note as Subject」，可以在 Note 和 Subject 之间切换。

颜色设置
----

MailTags 中可以给邮件单独设定颜色，或者基于项目标签、预定时间、重要性定义自动着色，以便在视觉上直观的定位邮件。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/06924F1E-D5A0-4229-B521-3D0BCB1AE906.jpg)

关键词标签添加的页面中能看到单独的一行颜色（Color）设置，这是给邮件手动进行色彩标注的一种方式，用以突出某类邮件。多数情况下，颜色用于项目的区分或者重要性的判断，这里建议大家仅用颜色来进行重要性的判断，避免颜色过多反而造成识别上的干扰。

「Use Tags to Color Message」设置中去掉 Tickle、Project 的勾选按，只保留 Importance 和默认的 Message Color（就是上面提到的手动设置 Color） 项。

其他技巧
----

1. 除了手动给邮件设置重要性以外，还可以通过规则来实现。例如，某某某发送的来的邮件，重要性标记为高。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/1B83CB3E-D988-4298-8CF2-221778F958F2.jpg)

2. 颜色和标签都是邮件管理和处理过程当中的标识产物，一段周期后我们或许不再需要它们，同样这里也可以用规则来进行清除。

![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/BBFAA9FC-149B-43A1-B389-C562A2487771.jpg)

3. 图示中选择的 MailTags 操作是「Clear MailTags Keywords」，如果你想清除所有的 MailTags 标注痕迹（标签、颜色、备注等），操作条件可以选择「Clear All MailTags」。

4. 可以直接通过拖拽的方式添加 Keywords、Projects、Tickle Dates，直接由邮件列表拖动邮件到边栏中的具体项目上即可。

MailTags 5 Beta 版已经兼容 macOS Sierra Public Beta 1，但是尚有些问题存在，例如，点击这 Calendar 中的事件（Event）和任务（Task）两项 MailTags 5 beta 会崩溃。

你可以 [前往官网](https://smallcubed.com/mt/) 下载试用或购买 MailTags。

本文档适用于：MailTags 5  
内容制作软件：Ulysses、OmniGraffle、Snagit

文章来源 [少数派](http://sspai.com) ，原作者 [scomper](http://sspai.com/author/684054) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/9D1FFECE-5D32-4197-940D-5B8FC1ADCA4D/03FD922D-24C0-40E8-8AA7-A55F4A4CC7CE.jpg)](http://www.huodongxing.com/event/7344389491800)

---

[🌐 原始链接](http://sspai.com/34889)

[📎 在印象笔记中打开](evernote:///view/207087/s1/017d2c9c-b05c-4ef7-a0eb-d314540ba8b8/017d2c9c-b05c-4ef7-a0eb-d314540ba8b8/)