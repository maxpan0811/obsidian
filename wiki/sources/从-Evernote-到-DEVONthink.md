---
title: 从 Evernote 到 DEVONthink
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/从 Evernote 到 DEVONthink.md
tags: [印象笔记]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "从 Evernote 到 DEVONthink"
source: evernote
type: note
export_date: 2026-06-27
guid: f67989fb-fecf-4b61-a7bf-62d549469afe
---

# 从 Evernote 到 DEVONthink

# 从 Evernote 到 DEVONthink

2018 年 05 月 23 日

[![](attachments/5b278dcd6ffdb943.png)](https://sspai.com/user/711608/updates) 

#### [OscarGong](https://sspai.com/user/711608/updates)

目录
:   1. [痛楚](#)
    2. [上手 DEVONthink](#)
    3. [文件组织](#)
    4. [一些与 Evernote 的比较](#)
    5. [信息的收集及处理与工作流](#)
    6. [搜索](#)
    7. [DEVONthink to Go](#)
    8. [结尾](#)
    9. [参考文章](#)

本文主要讲述了三个问题：

- 我在使用 [Evernote](https://itunes.apple.com/cn/app/evernote/id281796108?mt=8&at=10lJSw "Evernote") 中遇到的问题；
- [DEVONthink](https://www.devontechnologies.com/products/devonthink/overview.html "DEVONthink") 如何覆盖解决了这些问题；
- 作为已有的 Evernote 用户如何上手熟悉 DEVONthink。

途中我比较了 Evernote 和 DEVONthink 的优势和劣势，还讨论了一些我的个人用法。

## 痛楚

我订阅 Evernote Premium 快三年了，身为 Evernote 的重度用户，我在 Evernote 里有近 1000 篇笔记，因为一些契机，最近需要在 Evernote 记一些包含代码的文档，灾难就来了：

![](attachments/dc8c39de158c6179.png)

Evernote 裁剪前后的网页对比

在使用 [Evernote Web Clipper](https://chrome.google.com/webstore/detail/pioclpoplcdbaefihamjohnefbikjilc "Evernote Web Clipper") 将网页保存到 Evernote 后，原网页中的代码块丢失了大部分格式信息，而且几乎变得不可编辑。

之所以会导致这样背后的原因也很好解释，Evernote 自己发明了一套名为 [Evernote Markup Language (ENML)](https://dev.evernote.com/doc/articles/enml.php "Evernote Markup Language (ENML) ")  的语言，而 ENML 是 HTML 的一个子集，也只是部分的支持 Javascript，所以部分格式显示不出来；一些如 依赖 `<span>` 标签实现的页面内跳转功能，在转换为 ENML 后也会失效。

一些常用的文本编辑功能，如「搜索和替换」，在 Evernote 中也一直是缺失的。之前我可以使用其他文本编辑器如 BBEdit 编辑笔记的源代码 (ENML) 来实现 Evernote 中缺失的功能。为了快速打开笔记其对应的 ENML 文件，我制作了一个 Keyboard Maestro [Macro](https://github.com/OscarGong/My-Apple-Script/blob/master/Evernote/Open%20Current%20Note's%20ENML/Open%20Current%20Note's%20ENML.scpt "Macro")。但是最近版本中，笔记的 ENML 存放位置经常发生变动，并且没有相应的文档可查询，导致每次变化时我都要花费大量的时间摸索修改这个 Macro。

如果 ENML 对 Evernote 从一而终，一直是一等公民也还好，但是 Evernote 不希望用户接触到 ENML，用户使用的 Evernote 笔记编辑器操纵的是 ENML 渲染成的富文本。同时 Evernote 的本地自动化能力有限，虽然[支持 Apple Script](https://sspai.com/post/Mac%20-%20Evernote%20Developers%0Ahttps://dev.evernote.com/doc/articles/applescript.php%0A%0A "支持 Apple Script")，但是功能十分很少：

![](attachments/4b9169341bb0e3d5.png)

二者自动化能力比较

这一切加起来使得在使用 Evernote 时，大部分时间都在点鼠标点鼠标，调整格式。如果 Evernote 能够支持 Markdown 在一定程度上可以解决这个问题，虽然 Evernote 在 2015 年就[公布](https://blog.evernote.com/blog/2015/09/22/the-future-of-writing-in-evernote/ "公布") 将开启 Markdown 内测，但是 2018 年了大家依旧没能用上。

至于 Evernote 内建的代码块功能，默认是**关闭**的，需要在 `Evernote - Preferences - Software Update` 的 `Beta Versions` 下手动开启。虽然默认不支持代码高亮，但是借助 [BBEdit](https://www.barebones.com/products/bbedit/ "BBEdit") 的 `Copy as Styled Text` 功能，将 BBEdit 处理过的代码，粘贴至 Evernote 中，除了步骤繁琐以外，效果还可以。

![](attachments/8aa969e041137064.png)

使用 BBEdit 高亮代码

不过注意，这个功能无法在 Mac App Store 版 Evernote 中开启，只有官网下载的版本才可以。而且这个功能从 [2016 年](https://discussion.evernote.com/topic/97731-code-block-in-evernote-for-mac/?do=findComment&comment=425516 "2016 年") 就可以作为测试功能可以使用了，但是到 2018 年依然在测试，官方的这种模糊不定的态度也使人感觉非常不安。

另外还有小一些问题与官方反馈过，但是并没有得到即使解决，如：编辑笔记时，我喜欢关闭主程序窗口，只保留一个弹出的笔记窗口，因为这样很清爽，但是每次从其他程序切回到 Evernote 时，主窗口都会被重新唤醒。

总的来说，如果只使用 Evernote 的内建文字工具，如这篇笔记：

![](attachments/610851fa42462599.png)

一篇无复杂格式的笔记

加上与 Evernote API 紧密结合的 IFTTT, Workflow 等工具，打拼多年的 Evernote 做的还是很不错的。但是一旦涉及到裁剪编辑复杂格式的网页，代码、LaTeX 等稍复杂的格式需求，受限于 ENML，Evernote 就变得力不从心。

### 自己的需求

每个人的工作流程、使用电脑的习惯和软件设置都不一样，所以当我要离开 Evernote 时，首先要理顺清楚我都在用 Evernote 做什么：

- 在浏览器中裁剪网页，随后进行标注等处理；
- 记录格式简单的笔记，如写作大纲；
- 记录格式复杂的笔记，如涉及代码的笔记。

格式简单的笔记不动，就留在 Evernote 内好了，如果将来某一天因为设备数的限制或者其他原因，要将他们迁移走时，也非常好处理。

对于格式复杂的笔记、涉及代码的笔记我全部都迁走使用 [Quiver](http://happenapps.com/ "Quiver") 来完成，Quiver 的 Code Cell、Markdown Cell、LaTeX Cell 等设计非常适合用来记录这些信息。在 Quiver 中编辑完成的笔记，我会导出一份到 DEVONthink 中归档。

裁剪网页这部分完全交给 DEVONthink 来处理，DEVONthink 除了能完整的记录网页上的信息，其他的特性使 DEVONthink 能够作为 research 工具，从而达到之前使用 Evernote 无法完成的事，这部分内容也是下文的重点内容。

## 上手 DEVONthink

很久以前的一个 bundle 中我就已经有了 DEVONthink，在比较官网上各个版本的 [功能区别](https://www.devontechnologies.com/products/devonthink/comparison.html "功能区别")后，发现 DEVONthink Pro 和 DEVONthink Pro Office 差别在：Office 版只是多了无纸化办公相关功能和协作功能，于是只花了 30 刀升级到了 DEVONthink Pro。

![](attachments/4114e036be02f2cf.png)

升级到 Pro

简单的比较一下：

- **DEVONthink Personal**: 基础版本，包括了 DEVONthink 的核心功能。
- **DEVONthink Pro**: 与 Personal 版相比增加了数据库、自动分组、RSS、表格功能，同时支持了 Apple Script 和 Automator。
- **DEVONthink Pro Office**: 与 Pro 版相比，增加了与办公场景相关的功能，如 OCR（字符识别）、电子邮件归档、局域网内数据共享等。

### 数据库 Database

如果你使用的是 DEVONthink Personal 版本（只支持一个数据库），在第一次启动时，会自动创建一个数据库，位于 `~/Library/Application Support`；Pro 和 Pro Office 会在第一次启动时，征询你创建一个数据库，默认位于 `~/Documents`。

一个数据库已经能够应对很多场景，但是如果想创建多个数据库，要考虑这几个要素：

- **共享**，如果你的数据是要与其他人合作编辑或者进行共享，不管是使用 Pro Office 的 Web server 服务，或者是其他方式。对 DEVONthink 来说，可操作最小的单位是数据库，因为你无法对更小层级进行访问控制。
- **组织**：对于诸如 Replicate、Duplicate（下文会提到这二者）、智能分组以及推荐等功能，默认的有效范围都是局限在当前数据库内。
- **搜索**：默认的搜索也是仅限于当前数据库，如果需要跨数据库搜索，需要使用 Search Window（`Tools - Search`）

值得注意的是，数据库属性（Database Properties）下的密码功能并不能提供真正的保护，**其在本地时**仍是未加密的，使用 Finder 直接就能访问其中的文件，属于防君子不不防小人的功能。

如果需要本地的加密功能，可以考虑在磁盘工具中，新建一个 APFS (encrypted) Volume，将 DEVONthink 数据库文件存在这个分卷中，不使用 DEVONthink 时弹出将这个分卷弹出。

### 同步

虽然 DEVONthink 是从 Mac 起家的，但是其 iOS 伴侣版本 DEVONthink to Go 在更新到 2.0 之后，可用性也非常高，所以不同设备之间的同步是必须的。

> DEVONthink Pro does not allow synchronizing databases located in a cloud folder to prevent issues related to third-party software modifying the databases.

虽然 DEVONthink 以一个个 [bundle 文件](https://developer.apple.com/library/content/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html#//apple_ref/doc/uid/10000123i-CH101-SW1 "bundle 文件") 的形式存储数据，看起来可以像 Keyboard Maestro、BetterTouchTools 等软件一样，简单的把 DEVONthink 的数据文件存到如 Dropbox、iCloud Drive 文件夹进行「外部」同步。但是 DEVONthink 维护了关于各个文件结构复杂的关系数据库，存储了像标签、已读状态、注释等信息，使用「外部」同步方法，很容易导致错误。

考虑到这个原因，以及想到我的 DEVONthink 数据可能会成长的很快，我新注册了一个 [BOX](https://www.box.com/ "BOX") 账号专门用来于 DEVONthink 进行「内部」同步，[免费](https://www.box.com/pricing/individual "免费") 的 10 GB 空间在可观的时间内应该够用了。

值得注意的是，几种内建的同步方式中，iOS DEVONthink to Go 是**不支持** iCloud Drive 同步的，非常坑：

![](attachments/d9ca02f8c57a8660.png)

Mac 与 iOS DEVONthink 的同步方式

DEVONthink 的同步还是有些令人迷惑的，在 Mac 端大致上分为三步：

- 在左面添加一个同步 Location；
- 在右边「选择」或「导入」数据库；
- 设置同步细节选项。

以 BOX 举例：

![](attachments/e63103ad90bfcadf.png)

BOX 同步

- **User Name** 与 **Password** 就是 BOX 的用户名和密码，如果使用 Dropbox 因为 Dropbox 使用 OAuth 2 验证，会弹出网页进行授权。
- **Sync Store Name** ，在云端部分 DEVONthink 数据的名字。虽然在本地，DEVONthink 的数据是以一个个 `*.dtBase2` 文件存储的；但是在云端，所有的 `dtBase2` 文件会被打包成一个 `dtCloud` 文件。当不同平台的 DEVONthink 之间同步时，使用相同的云平台，输入**相同的** `Sync Store Name`，就会同步同样的数据。

  ![](attachments/4db41a5fe6a04777.png)
- **Encryption**：建议开启，输入密钥后 DEVONthink 会对数据使用 256 位 AES 加密。

设置好了一个同步位置后右边会列出可用的数据库，在云端和在本地的都会列出来，把想同步到云端的本地数据库打钩即可。

---

5 月 24 日更新：  
[最新版本](https://blog.devontechnologies.com/2018/05/devonthink-adds-icloud/ "最新版本") DEVONthink 中（[DEVONthink 2.10](https://www.devontechnologies.com/redirect.php?id=product-dt "DEVONthink 2.10") 和 [DEVONthink To Go 2.6](https://www.devontechnologies.com/redirect.php?id=product-dttg "DEVONthink To Go 2.6") ）支持了直接使用 iCloud 同步，不再需要输入、配置复杂的同步设置。因为 iCloud 能够在后台刷新，而且考虑到 DEVONthink 是一个只能在苹果平台使用的软件，直接使用 iCloud 同步是现在的首推同步方法。

### 笔记导入

DEVONthink 支持直接导入单篇从 Evernote 导出的 `enex` 笔记文件，导入后为 Formatted Note；或者如果你打算 all-in DEVONthink，其也支持直接导入 Evernote 的整个数据库：`File - Import - Notes from Evernote…`  
同时 DEVONthink 也支持导入 Notes 的数据，方法与 Evernote 类似。

![](attachments/91128ff9baa95f11.png)

从 Evernote 导入的一个笔记本

### 偏好设置

一般来说，偏好设置的默认选项已经足够 adequate，但是也有一些我建议修改的地方：

勾选 `General - Mark duplicates and replicants in color` ，刚开始使用时，对文件进行拷贝、移动、打标签等操作时，很容易产生 duplicates 和 replicants，而这二者又是很容易使人困惑的概念，勾选这个选项会把使 duplicates 标记为蓝色，replicants 标记为红色，便于区分。（下文中重点提到这个两个概念）

**Editing**：

- `Smart copy/paste` 自动移除粘贴进的文字前后多余的空格；
- `Smart Links` 探测文本链接使其可点击；
- `Smart dashes:` 将诸如 `--` 自动转换为 `—`；
- `Data detectors:` 探测文本中的地址、时间、日期等信息；  
  这几个选项按照个人情况修改，我个人关掉了 `Data detectors:` 和 `Text replacement`。

Editing 下的 WikiLinks 也是很有用的一个功能，打开后 DEVONthink 会扫描文本，如果文本中包含笔记或文件的名字，会自动将其链接过去。至于 `Mashed Word` 和 `Names` 的区别为，Mashed Word 不接受空格。

**Colors** 下默认的 Label 和高亮颜色都充满陈旧感，我全都改掉了。

**Web** 下 `Cookie` 我修改成了 Always，方便即将提到的一个工作流。

### 一些改造

可能因为 DEVONthink 历史较长的缘故，其很多快捷键和功能安排都与一些「较新」的软件不同，我使用 Keyboard Maestro 对其进行了一些改造。

首先，无论在是 Evernote 还是 Ulysses 甚至包括 Office 中都通用的 `⌘Command - K` ，编辑超链接的快捷键，在 DEVONthink 中竟然被分配用于标记未读状态。新建一个 `⌘Command - K` 触发的 Macro，选择 DEVONthink 中的菜单项，使用正则匹配链接的两个状态，搞定。

其次，DEVONthink 的功能太多了，很多功能的快捷键和已有软件的快捷键冲突，而我又不愿意重新训练自己的习惯，于是我把这些功能都提了出来制作 Macro。

![](attachments/ce2fee6a5b04e9f0.png)

Keyboard Maestro

添加了一些个人需求的功能后，全部放在一个 Group 下，设置 Macro Group Palette 仅在 DEVONthink 中显示。

## 文件组织

当开始使用 DEVONthink 时，遇到的最大的挑战就是如何建立一套合适的管理体系，这套体系要有弹性，有包容性，又能足够契合个人的习惯。

### 「Import 导入」与「Index 索引」

除了直接使用 DEVONthink 创建的笔记之外，外部的一个文档要想能被 DEVONthink 处理，要么 Import 导入进 DEVONthink，要么 Index 索引进 DEVONthink。

选择 `File` - `Index` (`⌥⌘X`) 就能将文档「索引」到 DEVONthink 中，相当于在 DEVONthink 数据库中制作了一个源文件的「引用」，文件会维持在原处不动，DEVONthink 会对其做扫描处理，可以对其进行如打标签等进一步操作。当 Finder 中的源文件被移动或删除时，这个「引用」就丢失了其所指，尽管在 DEVONthink 中还能看到这个文档，但是已经无法预览编辑它了。

而「导入」是把文档制作一个副本，拷贝到某个 `*.dtBase2` 数据库包裹文件中。除了「索引」之外，诸如网页裁剪工具、全局 Inbox 文件夹等其他操作，都对应的「导入」动作。这部分内容会在第四节展开。

![](attachments/f4395b83bc5c7587.png)

导入与索引

#### 「导入」还是「索引」？

「索引」文件是 DEVONthink 一个有趣的特点。第二节中有提到：不建议将 DEVONthink 的数据库直接存放在 Dropbox 文件夹下；但是我们可以让 DEVONthink 索引 Dropbox 文件夹。这样做就能使文档跳出 DEVONthink 框架。

如在使用 iOS 版 PDF Expert 时，我不需要使用 Document Picker 来读取存在 DEVONthink to Go 内的 PDF 文件，直接使用 PDF Expert 内建的 Dropbox 修改其中的文件即可。保存后打开 Mac，DEVONthink 会自动将 Dropbox 中的新文件重新分析索引。

另外我已经在 Finder 中存了很多整理好的 PPT 课件、写作存档，「索引」能直接将这些已有的文件纳入 DEVONthink 体系。

另外可以使用 DEVONthink 索引 [nvALT](http://brettterpstra.com/projects/nvalt/ "nvALT")、[Scrivener](https://www.literatureandlatte.com/scrivener/overview "Scrivener") 的工作目录，甚至是 [MailMate](https://freron.com/ "MailMate") 的 Application Support 文件夹。这样便能很好的处理 DEVONthink 和其他功能有重叠 App 之间的关系，而不比为了使用 DEVONthink 摒弃掉所有其他 App。

### 「Groups 分组」与「Tags 标签」

除了数据库，Groups 和 Tags 是 DEVONthink 的第二级组织结构。

如 DEVONtechnologies 的 [Blog](https://blog.devontechnologies.com/2012/03/tuesday-tip-use-tags-efficiently/ "Blog") 中所说：

> While tags and groups are technically the same, their different way of presentation can be more flexible, especially in large DEVONthink knowledge collection spreading out in many directions. …

「标签和文件夹本质上一个东西」，只是展示形式不同（但是他这句话实际上和没说一样，一点帮助也没有）。为了更好的处理 Groups 和 Tags，对于 DEVONthink 来说，二者都只是 Labels —— 某个文件的 metadata 元数据部分的一些数据。

DEVONthink 和 Evernote 在 tag 的处理方式上有非常多的不同之处。：

1. Evernote 中，笔记本（文件夹）是第一公民，一篇笔记可以没有任何标签，但是必须依附于一个笔记本。  
   但是 DEVONthink 中，一个内容可以只依附于某个 Tag，而不必存在某个 Groups 中（当然，还是要存储某个 Database 中）。DEVONthink 有一个视图（`⌘Command - 6`）就是只列出了所有的 Tags。
2. Evernote 和 DEVONthink 中的 Tags 都可以分级，即 Tags 可分为父标签和子标签，如：「Apple - macOS - Apple Script」。Evernote 中，一篇笔记可以只标记某一个子标签，即只标记「Apple Script」这一个标签；  
   但是 DEVONthink 中，标记了一个子标签（「Apple Script」）后，会自动补全其父标签（「macOS」和「Apple」）。这从侧面也体现了 DEVONthink 中标签和文件夹本身是一个东西。

此外，DEVONthink 中有一些很独特的设计：

在 DEVONthink 中，当从 `File - Database Properties` 选项中取消勾选 `Exclude Groups from Tagging`（中文为「区别对待 Tags 和 Group」 ）后，Groups 和 Tags 就变成了完全一样的东西，Groups 的图标也会变为金色。

![](attachments/4dd045bf1837c6f8.jpg)

Exclude Groups from Tagging

这时已有的 Group 会被转换成 Tag，如果有重名的 Group 和 Tag 别担心，这个操作是可逆的，而且 DEVONthink 能把他们区分的很好。如果你倡导标签[一元论](https://zh.wikipedia.org/zh-hans/%E4%B8%80%E5%85%83%E8%AE%BA "一元论")，取消勾选这个选项，就可以像操作 Tag 一样操作 Group 了，Group 也拥有了所有 Tag 的特性，如：当为某个文件标记了一个子 Group 时，会自动标记其父 Group。

![](attachments/7515f468e74b898c.png)

Tags 为蓝色；Groups 为灰色

此时如果我按下快捷键 `⌃Control - ↩Return` 为某个文件标记了多个 Groups 后：

![](attachments/96f2e795099cc35c.png)

alter to replicant

之前 PDF 文件只有一个 Apple 标签，我又添加了 Picture 标签（实际上为 Groups），文件名称变成了红色，并且在两个 Groups 下都会显示。这是怎么回事？

#### Replicate 和 Duplicate

在任意一个文件上右键点击，会看到 `Move To`、`Replicate To` 和 `Duplicate To` 三个选项。上述情况中，那个 PDF 文件实际上是「Replicate to」到了 「Picture Groups」继而变成了 Replicant。

**Move** 其实就是剪贴、粘贴。大家都很熟悉这个概念。  
**Duplicate** 动作会在当前数据库下，创建一个一模一样的副本，每个副本之间互不干扰，修改此处，只在此处生效。  
**Replicate** 动作会创建 replicant，replicant 类似 Finder 中的 alias 概念，但是并不一样，alias 有 original 和 aliases 之分。但是 replicant 没有这个分别，replicant 也并不是复制了一份，各个 replicant 其实是一个文件，修改一处，其余也会被修改。

Replicate 是十分实用的功能，尤其是在使用 Groups 组织文件时，将同一个文件制作多个 replicant 分别放到不同的 Groups 后，这个文件就能同时在多处编辑。分散在多处的 replicant 相当于为这个文件标记了多个标签。Replicate 功能极大的提升了 DEVONthink 文件组织的灵活程度。

如「上手」部分提到的，要使得 Replicate 和 Duplicate 与普通文件有所区别，需勾选 `DEVONthink Pro - Preferences … - Mark Duplicates and Replicates in color`，之后，Duplicate DEVONthink 会用蓝色标记，Replicate DEVONthink 会用红色标记。

![](attachments/7ad00662e5171dc6.png)

Replicant 与 Duplicate

小脚注：「[replicant](https://en.wikipedia.org/wiki/Replicant "replicant")」这个来自银翼杀手的名词好难翻译啊，我较近脑汁也没想到中文语境下有类似含义的名词，或许类似：「影复件」或「影子复件」？

#### Groups 还是 Tags？

DEVONthink 的组织功能是如此强大以至于，如果不好好管理 Groups 和 Tags，时间一久肯定会使自己感到混乱。同时使用 Groups 和 Tags 或许是最佳的状态，所以要确保「groups are excluded from tagging」。

**Groups**：在大多数情况下都首先建议使用 Groups 来管理。从 Finder 中导入的文件本身就是以文件夹形式组织的。如果自己不常操作某个数据库，或者这个数据库要与他人共享，Groups 对大家都是更容易理解的。而 Tags 的设置每人都不一样，也意味着更 Tags 隐晦。

**Tags** ：一些文件 ，如从收件箱导入进来的 Gamil 邮件，本身就只有 Tag 这一个属性，对于这些文件不如单独分配一个数据库，把他们全丢进去，只使用 Tag View 来预览、管理。

一个很重要的因素是：DEVONthink 引以为傲的 AI 技术中的 Auto Group 和 Classify (`Data -> See Also & Classify`) ，只能把文档分类到不同的 Group 中，而不能对其打不同的标签 。（尽管 Auto Group 实际效果还不错，但是对我来说还是营销噱头的感觉大一些，官方甚至自己也用「AI 技术」做调侃，如[这篇四月一号的博文](https://blog.devontechnologies.com/2017/04/awareness/ "这篇四月一号的博文")。）

![](attachments/237987c75d3d0b58.png)

Classify See Also

所以这意味着对于大多数人来说，为了使 AI 引擎更好工作，也是从 [DEVONtechnologies](https://www.devontechnologies.com/ "DEVONtechnologies") 的角度来说，**最佳实践**（或许）是：使用含义清晰明确的、没有歧义的名字作为 Groups 的名字，使用私人相关的或者状态相关的情景作为标签。举个例子：在读书笔记 Group 下有数学、社会学、政治几个子 Groups，然后使用阅读中、纸质版、电子版做标签。

几个我的建议是：

- 使用 Database 作为一个大尺度上的项目分类方式，而不是只使用一个名为类似「Archive」或「电子大脑」的 Database。
- 在大多数情况下，尽量使用 Groups 来进行分类；
- 使用 Tags 时，一组 Tag 只使用于一个项目下。要用于多个项目时，要作分级。如：把 Working Tag 分为 Working-Biology 和 Working-History。

### 其他组织形式

除了也存在于 Evernote 中的 Groups 和 Tags 两种组织方式，DEVONthink 还支持更「macOS」的「Label」和「Flag」。  
Label 本质上与 Tags 是一个东西，只是视觉上更醒目；Flag 只有两个状态：未标旗和以标旗。这二者不要与 Tags 混用，Label 一般用于标记文件状态，Flag 一般用于标出重要文件。在 DEVONthink to Go 中，默认内置了可以直接筛选出 Flag、Label 的智能分组。

![](attachments/3ebe9b6456bf1bfd.jpg)

## 一些与 Evernote 的比较

DEVONthink 与 Evernote 虽然都能实现类似的目标：知识管理，但是逻辑设计和实现方式上都有很大区别。

### 同步

**Evernote** 默认同步所有的数据。与其说 Evernote 是一个软件，不如说是一个服务，很多 Evernote 的功能依靠服务端才能完成，如 PDF 文件的文字识别，意味着 Evernote 不得不将所有的数据全部上传到服务端。  
前些日子里（2016 年），Evernote 甚至[计划更改隐私条款](https://techcrunch.com/2016/12/14/evernotes-new-privacy-policy-allows-employees-to-read-your-notes/ "计划更改隐私条款")以允许其员工直接阅读用户数据以确保其深度学习功能正常运行。尽管因为反响太强，Evernote 后来[取消](https://blog.evernote.com/blog/2016/12/15/evernote-revisits-privacy-policy/ "取消")了这个计划。  
不过公平的讲，Evernote 的同步功能一级棒，逻辑简单，使用了很久几乎没有遇到过什么问题，而且速度非常快。但是敏感信息就不建议存到 Evernote 中了。

**DEVONthink** 默认不同步数据。虽然 DEVONthink 支持多种同步方式，但是与 Evernote 相比，步骤繁琐且不直观。同时这种基于本地的特性使得协作变的非常困难，Evernote 可以轻松的将笔记分享为网页或者邀请他人来编辑，但是在 DEVONthink 要实现多人协作需要很复杂的方式。Devonian Times blog 的[这篇文章](https://blog.devontechnologies.com/2015/04/tuesday-tip-use-dropbox-to-sync-with-friends/ "这篇文章")描述了一个可行的实践方式。

[\<The Power of Habit: Why We Do What We Do in Life and Business\>](https://www.amazon.com/Power-Habit-What-Life-Business/dp/081298160X "\<The Power of Habit: Why We Do What We Do in Life and Business\>") 这本书里有一些很有趣的例子，关于大公司拥有了大量数据以后，人们的自由意志是如何被操纵的。

### 笔记格式

**Evernote** 只有一种称为「笔记 (Notes)」的笔记格式，正如前面提到的，虽然其看起来是 RTFD 富文本，但是实际上是 ENML 文档。尽管 Evernote 支持视频、PDF、语音音频等作为笔记的内容，也支持把任意格式的文件当做附件，但是所有的文件都需要依附与一条笔记。

**DEVONthink** 能创建非常多种文件作为笔记：纯文本、富文本、格式化笔记、HTML、Markdown、书签等。

![](attachments/58f6bc8342f5bbcb.png)

DEVONthink Format

同时，DEVONthink 「原生的」支持 PDF、WebArchive 甚至包括 docx (Word)、Pages 等格式，存入 DEVONthink 的「原生支持」的文件都可以利用 DEVONthink 的高级功能，如搜索、词汇分析、自动分组等。对于其他格式的文件，藉由不同的 macOS Quick Look 插件，在 DEVONthink 可以预览，通过添加 metadata 信息，也可以纳入其收纳体系。

### 数据存储

Evernote 和 DEVONthink 用途都很多，都可以实现诸如：信用卡账单归档、电子邮件归档、学术研究、碎片知识管理、读书笔记等需求。DEVONthink 支持多数据库，Evernote 只能使用一个数据库。

**Evernote 的数据文件是加密的、隐藏起来的、私有格式的。**

非 MAS 版 Evernote 目前数据存储在 `/Users/Home/Library/Application Support/com.evernote.Evernote/accounts/www.evernote.com/一个数字ID/` 下，打开这个文件夹会发现这里存了一些人类几乎无法阅读的东西，上文提到的 Keyboard Maestro Macro 中我使用了 [`sqlite3`](https://linux.die.net/man/1/sqlite3 "`sqlite3`") 这个 CUI 工具来解析数据库。除了编辑源文件不方便之外，Evernote 这种存储方式还导致：

- 无法引用外部文件，Evernote 只能看见获取在数据库内部的文件，把一段文字链接到文件：`/Users/Home/Downloads/Somepdf.PDF` 是无效的。在 [另一篇文章](https://sspai.com/post/44425 "另一篇文章") 中，我讨论了一种解决方法。
- 附加在 Evernote 的文件，如果在 Evernote 未运行时使用其他工具编辑，可能会导致内容丢失。

**DEVONthink 的数据是与 Finder 文件系统相契合的。**

除了上一节中提到的：文档可以既被「导入 import」也可以被「索引 index」之外，DEVONthink 还可以使用多数据库。

多数据库的带来的好处有：

- 当我进行学术研究时，我不想看到我的信用卡账单。同理，当我 research 从网页上裁剪下的我感兴趣文章时，我也不想看到诗人头疼的学术文章。DEVONthink 的 See Also 和默认的搜索功能，都会只检索当前数据库的文件，使用多个数据库可以很好的区分开各个场景。
- 多数据库同时提升了管理的弹性。如，我发现某个数据库的体积增长非常快，占用了过多空间，我可以毫无心里负担的、不会造成任何损失的把它移动到同一局域网下的 NAS 上。

### 智能联想

Evernote 的 [Context](https://blog.evernote.com/blog/2014/10/02/context-work-enriched-smartest-minds/ "Context") 会根据当前笔记内容，联想推荐三篇相关笔记，甚至可以从 Lifehacker、Wall Street Journal、TechCrunch 等媒体上进行检索，显示相关内容。

![](attachments/01783489fb87bda5.png)

Context

尽管我有有效的 Premium 订阅，但是 Context 功能在我这失效了好久了（所以我找了一个网上的图），但是坦白的讲即使在能用的时候，Context 提供的数据对我来说帮助也不是很大…

DEVONthink 宣扬的[人工智能技术](https://www.devontechnologies.com/technology.html "人工智能技术")，说白了其实就是两个功能：

- 根据文件内容推荐适合存放的位置（Auto Group 和 Classify）；
- 在数据库中，找出其他和当前打开的文件相关的文件（See Also）。

从实际使用效果来看，当文件足够多时，Auto Group 的效果惊人的好，很难相信这个功能是来自一个只有 20 多兆的 App。在索引、存储了大量学术文件时，See Also 的效果也不错。

![](attachments/237987c75d3d0b58.png)

DEVONthink AI

### 笔记链接

Evernote 中右击笔记，选择 `Copy Note Link` 可以复制笔记链接，实现不同笔记之间的跳转，如果这篇笔记是共享的，那么这个链接在成员之间都有效。如果按住 `⌥Option` 右击笔记，选择 `Copy Classic Link`，可以复制 URL Scheme 版链接。但是笔记中的附件无法制作链接。

DEVONthink 也有类似的 `Copy Item Link` 功能，但是除了制作笔记（RTFD、PDF）链接，图片、书签、PPT 都可以制作 Item Link。**对于 PDF 文件，甚至还可以制作 Page Link（直接跳转到 PDF 文件的某页）！**（快捷键为 `⌃Control - ⇧Shift - ⌥Option - ⌘Command - C`）

对于一些不支持文件附件的场合，如 [Things](https://culturedcode.com/things/ "Things")、[Calendar](https://itunes.apple.com/cn/app/calendars-5-by-readdle/id697927927?mt=8&at=10lJSw "Calendar")，可以把文件存入 DEVONthink 然后链接到这些工具中。

Evernote 和 DEVONthink 都能生成 Table Of Content 内容目录。

### 自动化

如在第一节提到的，Evernote 在 Apple Script 支持方面同 DEVONthink 相比，几乎可以用「惨淡」来形容。通过 Script Editor 查看 Dictionary 可以发现，除了 Standard Suite 之外，Evernote Suite 所有的功能都是以「一篇笔记」为单位进行操作，如搜索、打标签、导入导出操作。

而 DEVONthink 包含了 Text Suite、DEVONthink Pro Suite、Extended Text Suite、OCR Commands Suite 五个组件。DEVONthink Pro Suite 覆盖了操纵笔记、操纵数据库等动作；Extended Text Suite 覆盖了大部分对笔记中文字进行操纵所需要的动作。

### OCR 光学字符识别

Evernote Premium 与 DEVONthink Pro Office 都有 OCR 功能，但是有所区别。在 Evernote 中，存入 Evernote 的 PDF 和图片文件在经过 Evernote 处理后，其中的字符可以被搜索到，但是无法复制下来。而在 DEVONthink 中选择「convert to searchable PDF」后，会创建一个新的文档，其中的文字不但可以搜索到，还可以复制下来。

不过 DEVONthink 的 OCR 功能是不支持中文的，中文文档的处理可以参考契丹神童的这篇文章：[通过 OCRmyPDF 实现在扫描版 PDF 中检索文字](https://sspai.com/article/44045?series_id=9 "通过 OCRmyPDF 实现在扫描版 PDF 中检索文字")

### 价格

[Evernote Premium](https://evernote.com/intl/en/get-started "Evernote Premium") 的价格为 70 美元每年，Standard 为 35 美元每年，为订阅制，有免费账户，但是限制两个设备和每月 60MB 的新上传流量。

[DEVONthink](https://shop.devontechnologies.com/order/product.php?PRODS=4556356,4556357,4556215,4556358,4558451,4559549,4556359,4556366,4556364,4556361,4556362,4556363,4556360,4574312,4575895,4620254&QTY=1,1,1,1,1,1,1,1,1,1,1,1,1,1&ORDERSTYLE=nLW45ZTPhH4&SHORT_FORM=1&SHOPURL=https%3A%2F%2Fwww.devontechnologies.com%2Fredirect.php%3Fid%3Dproducts&LANG=zh "DEVONthink") Pro 为 80 美元，DEVONthink Pro Office 为 150 美元，买断制，个人使用的话不限制设备数量。

[DEVONthink to Go](https://itunes.apple.com/app/devonthink-to-go/id395722470?mt=8 "DEVONthink to Go") 15 美元，有 8 美元的 In-app purchases，用于解锁诸如选择性同步、PDF 注释等[功能](https://www.devontechnologies.com/products/devonthink/devonthink-to-go/feature-comparison.html "功能")。

### 界面语言

Evernote 本身无论是软件界面还是文档，都支持中文，甚至还有本土运营的「印象笔记」，在本地化方面做的非常好。但是 [DEVONtechnologies](https://www.devontechnologies.com/about-us.html "DEVONtechnologies") 只是一家德国的小工作室，除了德文外软件只支持英文和法文，只要支持英文对我来说就问题不大，但是有可能对其他人产生障碍。aoaoho 制作了一份 DEVONthink 的[中文语言文件](https://github.com/aoaoho/DEVONthink-Chinese "中文语言文件")，如果有需要的话可以自行安装。

### 笔记历史管理

Evernote 支持详尽的历史版本记录，但如果想在 DEVONthink 中实现类似的功能只能诉诸于其他工具，例如使用 Keyboard Maestro 定期运行脚本将整个数据库或某个文件复制重命名到某个位置。

![](attachments/09ca6fe590e5dfb9.png)

Evernote Notes History

### 网页裁剪

与同步机制的情况类似，Evernote 的网页裁剪工具逻辑简洁，而 DEVONthink 网页裁剪工具要复杂的多，不过只要搞清楚其各个选项的作用，灵活性比 Evernote 高，下文会详细讲。

### Documentation

使用 Evernote 中遇到的大部分问题基本上都需要到其[论坛](https://discussion.evernote.com/ "论坛")中搜帖子解决；DEVONthink 有着十分详尽的[文档](https://www.devontechnologies.com/download/extras-and-manuals.html "文档")。不过祸兮福所倚，Evernote 社群十分活跃，遇到问题很容易就能产生共鸣，引起官方重视；而 DEVONthink 几乎没有社群…

## 信息的收集及处理与工作流

如上一节提到的，DEVONthink 支持的文件格式要比 Evernote 丰富很多；实际上，DEVONthink 能处理几乎所有最后呈现为文本的文件格式，PPT、Pages 都不在话下，更不用说 PDF、RTFD；此外大多数图片格式和一部分视频格式也能在 DEVONthink 中预览。

### 信息收集

一部分人使用 DEVONthink 可能基本上只是在使用导入和索引（在上一章 - 数据存储部分有详细讨论过）处理既有的文件。DEVONthink 除了导入、索引、拖拽这种直接操作文件的方式，收集信息到 DEVONthink 的方法还有很多。

#### SORTER

Sorter 是 DEVONthink 的一个小工具，类似于 [Yoink](https://eternalstorms.at/yoink/ios/ "Yoink")，会悬浮于屏幕的一侧。把文件拖入 Sorter 可以快速导入到特定的 Groups 或打上特定 Tags，双击 Sorter 内的图标可以直接在 DEVONthink 打开特定项目。Sorter 也可以用来快速创建笔记。

![](attachments/038cf774606480fe.png)

DEVONthink Sorter

Sorter 我个人使用的不多，vanilla2w 的这篇文章里覆盖了一些他的用法：[《围绕 DEVONthink 打造我的写作工作流 - 少数派》](https://sspai.com/article/43735?series_id=9 "《围绕 DEVONthink 打造我的写作工作流 - 少数派》")

#### 全局 Inbox

对于 Pro 和 Pro Office 版本，安装后会在 Finder 左侧 Favorites 部分添加 Global Inbox 文件夹，如果你的电脑上没有的话，也可以手动添加。

![](attachments/714443ac762a92ad.png)

DEVONthink Global Inbox

这个 Global Inbox 其实就是位于 `~/Library/Application Support/DEVONthink Pro 2/inbox` 的一个文件夹，等价于在 DEVONthink 左侧边栏最顶部的 Global Inbox，在 DEVONthink 运行时会变成一个蓝色的图标。

对于 DEVONthink 没有「云」属性，无法像 Evernote 可以「seamless」的存入数据这个弊端，Global Inbox 是解决的关键。如可以创建一个 IFTTT Applets，将 RSS 服务中的星标 Feed 作为 Trigger，触发动作为保存文件到 Dropbox，文件名为 `{{EntryTitle}}`，内容为 `{{EntryUrl}}`，就能自动的将我在 Inoreader 中标星的内容自动归档在 Dropbox 中，可以使用 Hazel 或 Keyboard Maestro 运行一段 Shell 脚本转换为 HTML 进行简单处理之后，就可以导入 DEVONthink Global Inbox 中以待后续处理。

Scott Granneman 的这篇文章讲述了他是如何使用 IFTTT 作为云端收集素材，Diffbot 优化格式，Hazel 运行本地 Shell，最后把文章制作成满足他需求的 Web Archive 版本。

[How to save a perfectly-scraped webpage into DEVONthink using IFTTT, Diffbot, Hazel, & several command line tools](https://www.chainsawonatireswing.com/2013/11/17/how-to-save-a-perfectly-scraped-webpage-into-devonthink/#ifttt "How to save a perfectly-scraped webpage into DEVONthink using IFTTT, Diffbot, Hazel, & several command line tools")

有一点要注意的是：Global Inbox 本质上还是 Finder 中的一个文件夹，拖拽默认为「移动」，即原本的文件会消失；可以按住 `⌘ Command` 拖拽进行拷贝，`⌘ Command ⌥ Option` 拖拽创建替身。

#### Service 和 Share Extension

Services 作为在 macOS 中历史很久远的一个特点，可以用于将当前 App 的信息分享到其他 App 之中。 作为一个非常 oldschool 的 Mac 软件，DEVONthink 当然支持 Services。

但是坦白的说，Services 应该是目前 macOS User Automation 组成中最「年久失修」的一部分（其他部分还有 Apple Script、JXA、Bridges ASObj-C 等），唯一的管理位置竟然分类在「系统偏好设置 - 键盘 - 快捷键」下。DEVONthink 的 Services 中比较有用两个：Take Rich Note 和 Capture Web Archive，二者可以把当前选中的内容本别保存为富文本或网页归档文件。但是我的主力浏览器 Chrome 对 Services 的支持很差，这两个 Services 在 Safari 工作的比较好。

另外 DEVONthink 会把自己设置为一个虚拟的打印机，可以用在所有能够打印的地方：「Print - Save PDF to DEVONthink」。

macOS 新的 App Extensions 包括 Action、Share、Content Blocker 等部分，DEVONthink 目前只能利用其中的 Share 部分，在支持 App Extensions 的软件中选择 DEVONthink 会唤出 Clip to DEVONthink 窗口，见下一小节。

### 网络信息收集

尽管上述的方法中，很多也能用于收集网络内容，但是 DEVONthink 还提供了专门用来收集网络内容的工具。

DEVONthink 本身提供了[两种方法](https://www.devontechnologies.com/download/extras-and-manuals.html "两种方法")：

- Browser extensions 浏览器扩展插件
- Bookmarklets 浏览器书签

我个人把这两种方法归纳称为「外部方法」。

#### 外部方法

![](attachments/a70129f1afa285b9.png)

DEVONthink Clipper 和 Bookmarklets

##### Browser extensions:

安装好打开浏览器插件，会看到很多选项：

**Plain Text**：纯文本文件，不必介绍。

**Rich Text**：富文本，DEVONthink 中的一等公民。纯文本文件可以随时转换成富文本（`⇧ ⌘ T`）。可以修改其中文字的字体、字号字重，添加超链接，附加图片甚至添加表格等。

**Formatted Note**：与 Rich Text 类似，都可以修改字体，添加图片、链接等。

虽然看起来 Formatted Note 的样式选项要比 Rich Text 少（如不支持表格），但是 Formatted Note 的优势是：他本质上是 XML 或者说是 HTML，使用 Sublime 打开直接就可以编辑其源代码。Formatted Note 在某种程度上讲与 Evernote 的 ENML 功能上有很多相似之处，enex 文件导入到 DEVONthink 就会被默认转换为 Formatted Note。

插入到 Formatted Note 中的图片文件都会被 encoded 进源代码中，所以可以很轻松的把 Formatted Note 上传到静态存储服务中（如 CloudApp），把获得的 URL 分享给他人，对方只需用浏览器就能打开。而 Rich Text 要想达到这个效果则需要额外工作。

**HTML Page**：本质上与 Formatted Note 是一个东西，但是因为 DEVONthink 的态度，导致二者有所区别：

- Formatted Note 的编辑器永远处于「所见即所得」状态，如果想编辑其源代码必须借助外部工具；而 HTML 文件可以点击右上角工具栏中的按钮 (`⌘ ⌥ P`) 切换为 `Text Alternative` 模式 ，直接在 DEVONthink 内编辑其源代码。  
  同时这一特点也导致了在 DEVONthink to Go 中，能预览和编辑 Formatted Note 文件；但只能预览，无法编辑 HTML 文件。
- 对 DEVONthink 来说，Rich Text 和 Formatted Note 都是其「原生」的笔记格式，而 HTML 更倾向于作为保持网页原始面貌的格式，或者说是用来归档的格式，这一点也体现在：使用网页裁剪工具保存为 Formatted Note 时可以简化格式，而保存为 HTML 时就没有这个选项。

  **Web Archive**: [Web Archive](https://developer.apple.com/documentation/webkit/webarchive#topics "Web Archive ") 是 Safari (WebKit) 发明的[一种格式](https://en.wikipedia.org/wiki/Webarchive "一种格式")，与 MHTML 类似。在 DEVONthink 中，保存为 HTML 文件时只会保存 HTML 源代码，而保存为 Web Archive 时，DEVONthink 会从远端抓取所有能用的到的资源，如图片、JS 库、CSS 等，将获取到的数据打包存储起来。与 PDF 相比，Web Archive 虽然每次打开时需要渲染，速度较慢，但是因为 Web Archive 保存了 CSS 和 JavaScript 等资源，网站的响应式布局设计不会受到影响，编辑、标注后的笔记在不同屏幕尺寸的设备上都能保持比较好的可读性。

离线时，或者随着时间的推进，保存的 HTML 文件可能因为某些服务器端数据的失效而变得面目全非；但是 Web Archive 文件能最大程度上的保持其本来面貌。（尽管苹果对 Web Archive 格式的态度很暧昧）

**PDF**：把网页保存成 PDF 格式，可以简化格式，大家也很熟悉。我个人喜欢保存为一个长的单页。

**Markdown**：一般来说，必须同时勾选「Use clutter-free layout」，将网页保存为 Markdown 才有意义，但是这个功能我用的很少，或许在某些情况下，将内容以 Markdown 格式进行处理，比直接处理 HTML 要轻松很多。

值得一提的是，DEVONthink 使用的是与 [GitHub Flavored Markdown](https://github.github.com/gfm/ "GitHub Flavored Markdown") 不同的 [MultiMarkdown](http://fletcher.github.io/MultiMarkdown-4/ "MultiMarkdown") 语法。如果想改变 DEVONthink 渲染 Markdown 时使用的 CSS 文件，可以在 md 文件开头添加语句：

<link rel="stylesheet" type="text/css" href="devon.css">  
或者将 CSS 文件存入 DEVONthink 后，在 md 开头直接这样写：  
CSS: x-devonthink-item://A8537QBF-77E0-41D9-B56B-365KDFJJOEF9

##### Bookmarklets (URL Schemes):

查看这些小书签的地址：

![](attachments/dacd0701ee5529e6.png)

小书签的代码

会发现，这些小书签只是一些简单的 JavaScript 代码，功能是获取一部分网页的属性，然后使用 URL Schemes 传入 DEVONthink。在 iOS 上有 Workflow，Mac 上有 Keyboard Maestro，小书签这个方法可以说已经完全过时了。

DEVONthink 的 URL Scheme 结构很清晰：

x-devonthink://<命令>[? < 参数 1 = 数值 1>[&< 参数 2 = 数值 2>...]]  
xdevonthink://x-callback-url / 命令 [? < 参数 1 = 数值 1>[&< 参数 2 = 数值 2>...]]

「添加」相关的几个**命令**：

- `clip`：存入 DEVONthink 并打开裁剪菜单；
- `createbookmark`：创建书签；
- `createhtml`：创建 HTML 文件；
- `createwebarchive`：创建 WebAcrchive 文件；  
  **参数**：
- `destination`: 目的地，以 UUID 形式表示。UUID 就是 Groups 的 Item Link 中的那一长串字母数字；
- `title`: 文件名；
- `location`：文件的 URL 属性；
- `source`：用于创建 HTML 文件时，后接 base64 编码的 HTML 源代码；
- `tags`: 添加标签，不同的标签直接使用逗号分隔。

所有的 URL 都要使用[百分号编码](https://zh.wikipedia.org/wiki/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81 "百分号编码")。

#### 内部方法

之所以将上面几种方法称为「外部方法」，是指「操作」是在 DEVONthink 外进行的，操作的结果只是传了一些参数进入 DEVONthink，剩下的工作是由 DEVONthink 自己完成的。

在使用上述操作收集网页内容时，最大的一个问题是，结果是我们无法预测的。带来的问题有：

- 要收集一个网页时，我经常会反复的点击浏览器拓展，切换各个格式，比较哪种格式最适合这个网页，最后只保留一个。
- 尽管 WebArchive 已经能最大限度的还原网页本来面貌，但是有一些网页内容需要动态加载，如 Disqus 评论、少数派首页；另外还有一些内容被 Pay-Wall 保护了起来，需要付费登陆后才能加载，如端传媒、少数派的付费栏目。对于这两种数据，DEVONthink 的 Clipper 处理的并不好。

DEVONthink 内包含了苹果的 WebKit 引擎，是有能力做一个浏览器的，其显示效果与当前版本的 Safari 保持一致。不同的是，DEVONthink 并不想把自己定位成普通浏览器，所以在 DEVONthink 中打开的网页是被当做一个个文档处理的，其地址栏无法用于导航，DEVONthink 的浏览功能定位是：获取、渲染、存储数据。DEVONthink 的浏览功能就是我指的「内部方法」，使用「内部方法」能很大程度上解决上述提到的问题。

![](attachments/e001041dad2bcd2a.png)

DEVONthink Web Browser

选择 `Data > New from Template > Web Browser`，就会在 Inbox 中添加 `Web Browser.html` 这个文档，这个 HTML 文件就刻用于简单浏览。注意 DEVONthink 默认的 Template 比较陈旧，一定要删掉图中的这部分用于自动添加 `http://` 的代码；另外记得按照前文「上手」部分，打开 Cookies。

遇到 Web Clipper 不能很好处理的网页，打开 `Web Browser.html`，在页面内 Capture 到 DEVONthink，一般都能获得不错的效果。

![](attachments/b276e0aa754f191b.png)

比较

要注意的是，在 Web Browser 内保存、转换成其他格式时，无论是转换为 PDF，还是 Web Archive，转换过程都会严格参照当前 View（视图）。不同的窗口大小，不同的滚动位置，都会影响最后的结果。也正是这个特点，使得这个功能尤其好用，完全**所见即所得**，结果可控。

之前我在 上说，Safari 的「Export as PDF」是效果最好的将网页保存为 PDF 的工具；现在我认为 DEVONthink 才是这个领域最好的工具。

但是每次处理网页都要先打开一个特定的文件，未免繁琐，我制作了一个 Keyboard Maestro Macro 简化了这个流程。

[> 下载地址](https://cl.ly/qtBy "> 下载地址 ")

Macro 的原理是：预先在 DEVONthink 中存入一个 HTML 文件，Macro 在每次运行时，修改 HTML 的内容，然后使用 DEVONthink 打开修改过的 HTML 文件。所以你需要预先在 DEVONthink 任意位置存入一个 HTML 文件，然后拷贝其「文件路径」和「DEVONthink Item Link」，分别替换 Macro 中的对应位置。

![](attachments/d9a2db968c58e40a.png)

Open in DEVONthink Macro

#### RSS

Pro 和 Pro Office 版 DEVONthink 可以从 RSS 源中获取文章，订阅源中的每篇文章都会被当做单独的一个文档处理，然后使用 Webkit 渲染。

出了前面提到的 Global Inbox，RSS 功能也是弥补 DEVONthink 云端属性不足的一个得力工具。将某个篇篇必读的网站的 RSS 添加到 DEVONthink 归档是一种用法，更重要的是：以 Inoreader 来说，每个文件夹、每个标签、喜欢的文章、Like 的文章，都有对应的 RSS 链接；Instapaper 的每个文件夹也能生成对应的 RSS 链接。按照自己的工作流，将这些服务的不同 RSS 链接添加进 DEVONthink 。

但是 DEVONthink 并不是一个好的 RSS 阅读器。一是 RSS Feed 中内容直接输出并不美观，从浏览器中打开再存入 DEVONthink 太繁琐。二是 DEVONthink to Go 目前并不能获取新内容，只能阅读从 Mac 端同步来的数据。

### 工作流

回到最开始的问题：Evernote 在处理格式复杂文件时表现不好；DEVONthink 几乎能完美的解决了这个问题。

对于格式简单的网页，直接使用 Clipper 简化格式，保存为 Formatted Note 或 RFTD，随后添加下划线、高亮等内容，在编辑完成后，转换为 PDF 文件存档。

对于格式较复杂的网页，保存为 Web Archive 文件，因为 Web Archive 文件完整的保留了网页所有的样式，保持着高可读性，同时还能够直接修改 Web Archive 的内容，删掉如网站的导航部分、相关推荐部分这样没用的内容，添加注释阅读完成后，如果网页没有交互部分就转换为 PDF 文件归档，有可以交互的部分就维持 Web Archive 不变。

不知道是我个人使用方法的问题还是因为软件设计所引导的，我在使用 Evernote 时，会一股脑的往里面塞东西，虽然也会对笔记做打标签等整理工作，同时也因为 Evernote 的「Switch to (`⌘Command - J`)」功能真的太好用了，导致我日后重复阅读 Evernote 中的笔记时，基本上的状态就是：读完了一篇笔记 -> 搜索 -> 读下一篇相关笔记。除非我手动的把当前项目相关的笔记都打上同样的标签，否则就是一直不停的在搜索。  
但是在使用 DEVONthink 时，存入其中的内容我都会十分严肃的处理，同时因为 DEVONthink 鼓励使用 Groups 来组织文件，慢慢的我将 DEVONthink 用成了我的 research 工具，而不仅仅是笔记工具。在做某个任务时，无论是学术上的还是仅仅个人兴趣，我会先我能搜集到的将与其相关的 PDF、HTML 等文档整理在 DEVONthink 的同一个 Group 内，在完成工作时，一旁的 DEVONthink 就成了我的文献库。而 Workspaces 功能 (Go -> Workspaces) 能将当前所有打开的 DEVONthink 窗口的大小、位置等信息保存下来，也就是可以将当前的工作状态保存下来，从而可以在不同的项目之间切换。

## 搜索

使用 DEVONthink 很大的一个动机就是为了能使用其搜索功能。使用 DEVONthink 搜索文档速度快、功能强大，你只要用一次就知道我说的是什么。

### 简单搜索

在 DEVONthink 主窗口又上角随便敲几个字符，没有其他 App 读进度条的过程，就完成了搜索。在默认设置下，搜索甚至是即时反馈的。

![](attachments/86e38da7e649505a.png)

Quick Search in DEVONthink

在 DEVONthink 中，搜索基本都是大小写不敏感的，几个搜索选项含义也非常简单：

- **Search for**：将搜索范围限定到所有信息、文档内容、来源、评论等；
- **In Selection**: 只在选定的文档内搜索；
- **Prefix while Typing**：勾选时，搜索「econ」，返回结果里会包括「economy」和「economic」；
- **Ignore Diacritics**: 勾选时，输入「dejavu」也能搜到「déjà vu 」。

除了 GUI 上的搜索条件，还可以使用控制符：

- 通配符：`?` 代替一个字符；`*` 代替多个字符；
- 布尔操作符：`AND (&, & &,+)`, `OR (|, ||)`, `XOR (^, ^^)`：和、或、异或（相斥）；
- 其他控制符：
- A `NEAR` B：A 词与 B 词之间距离在 10 个字符之内；
- A `AFTER` B：A 词紧挨着 B 词，在 B 词后。这个是我经常使用的，使 DEVONthink 能完整的搜索一个词，而不是拆开单独搜；
- A `BEFORE` B：A 词紧挨着 B 词，在 B 词前。

### 搜索窗口（⇧Shift - ⌘Command - F）和词语索引

在「文件组织」一节中提到过，DEVONthink 的简单搜索或者说快速搜索，默认的范围为当前数据库，如果需要跨数据库搜索，就要使用 `Tools - Search`。

除了简单搜索中已有的过滤条件，搜索窗口中添加了更多过滤条件：旗标、已读、锁定等。

`Tools - Concordance - Database` 可以打开 Concordance 词语索引功能，会列出当前数据库中的所有词汇按频率、长度、权重列出来，在学术环境内用处很大。

### 中文搜索

我存入 DEVONthink 中的内容大部分为英文内容，但是还是有少部分中文内容。虽然 DEVONthink 英文搜索很强大，但是因为 DEVONthink 几乎完全不能对中文进行分词，只能将中文文本在标点符号处隔开，所以其中文搜索能力非常差。

流行的解决办法为将中文词汇使用星号 `*` 分割开来，或者在每个词汇前加波浪线 `~` 强迫 DEVONthink 进行分词，可以某种程度上解决问题。

ringsaturn [写了一段 Python 脚本](https://github.com/ringsaturn/DEVONthink-Chinese-Search "写了一段 Python 脚本")，通过使用 [结巴分词](https://github.com/fxsjy/jieba "结巴分词")，在文档中提取关键词，然后填入文档元数据中的 Comment 部分。我个人对中文搜索的需求较小，所以不折腾这个方法了。另外 ringsaturn 还有 [一篇文章](https://sspai.com/post/44657 "一篇文章") 专门讨论了 DEVONthink 中文搜索的现状。

## DEVONthink to Go

DEVONthink to Go 2.0 版本发布有两年多了，从 2.0 版开始，DEVONthink to Go 默认会同步整个数据库，MobileSync 这个文件夹已经没有存在的必要了。  
DEVONthink to Go 仍在不断演进中，目前很多 Mac 操作还是只能在 Mac 上进行：

- 创建 TOC；合并、分离文档；
- 编辑 RTFD、Web Archive、HTML 文件；
- 对 PDF 文档进行 OCR 扫描、处理，转换为可复制的 PDF 文档。
- 无法使用 Auto Group, Auto Classify, See Also。换句话说，没有 AI 相关的功能。
- 无法使用 iCloud Drive 同步（尽管数据库可以存在 iCloud 中，但是仅限 Mac 版之间同步）。

所以综合来看，现在版本的 DEVONthink to Go 最佳的用途就是在移动设备上查看内容。尽管 DEVONthink to Go 也能做一些编辑操作，但是我发现经过其编辑的内容有时甚至与 Mac 版不兼容，显示效果有时会与 Mac 版不一致。

除了查看之外，DEVONthink to Go 也适合用于收集内容，我会经常把在各处看到的文章，选择 Bookmark 这个体积最小的形式存入 Global Inbox 中，随后同步至 Mac 做进一步处理。

许多 iOS 上的新特性，如 [FileProvider](https://developer.apple.com/documentation/fileprovider#overview "FileProvider"), [Drag and Drop](https://developer.apple.com/ios/drag-and-drop/ "Drag and Drop")，DEVONthink to Go 都在第一时间做了适配，我很看好未来其发展潜力。

## 结尾

从 Evernote 过渡到 DEVONthink 绝对不是一个无痛的过程，而且是一个非常痛苦的过程。DEVONthink 上手难度非常大，之所以我买回来后搁置了很久，是因为最初没有摸索清楚的那段时间，我一打开就头大，几个关键词的 Google 前几页搜索结果我几乎都读了一遍；另外也导致文章内的教程性内容写着写着就感觉要超出了我的控制。

[DEVONthink](https://www.devontechnologies.com/products/devonthink/overview.html "DEVONthink") 在学术领域有着非常广阔的前景，不止可以用作 Archive 工具，也是是非常好的 research 工具。从学生的角度来看，将从 Portal 中下载下来的 PPT、PDF 等文件 Index 到 DEVONthink 中，使用 RTFD 记笔记，随后使用 See Also 从之前 Index 好的数据中检索相关信息；另外使用 DEVONthink Index Bookends 的 attachment folder，从而使用 Bookends 管理 citation、DEVONthink 做 research，都是非常吸引人的使用场景。这篇文章的 research 工作全部是在 DEVONthink 中完成的，当所有相关文件全部存入 DEVONthink 以后，搜索真是一件美好的事情。另外能够检索 Google Scholar 等数据库的 [DEVONagent](https://www.devontechnologies.com/products/devonagent/overview.html "DEVONagent") 是无缝整合进 DEVONthink 中的，在只使用 DEVONthink 就获得了令我满意的体验情况下，我十分期待把 DEVONagent 融入工作流以后的表现。

但是既然名为「 Evernote 到 DEVONthink」，这部分就不做展开了。虽然文章以一种「踩 Evernote 捧 DEVONthink」角度展开，但是不代表我绝对的认为 DEVONthink 到处都好。上手难度大是一方面；对于纯手工输入的笔记，DEVONthink 的编辑和呈现是不如 Evernote 或者 Bear 的。现代 App 都有的「统一导航（ Evernote `⌘Command - J` 、Ulysses `⌘Command - O`、Telegram `⌘Command - K`）是我非常喜欢的功能，但是 DEVONthink 没有。DEVONthink 没有 Windows 版也是一个问题，正如 [Gabe Weatherhead](http://macdrifter.com/pages/about.html "Gabe Weatherhead") 在 [MPU #358](https://www.relay.fm/mpu/358 "MPU #358") 所说 : “The more I using Windows, the more I using iPad.” 此外 DEVONtechnologies 的动作十分缓慢，Mac 版有一些小毛病需得到改进，如：搜索高亮仅在搜索窗口中有效，文件打开后高亮就消失了；鉴于目前其开发中心基本上都集中在 DEVONthink to Go 上，DEVONthink Mac 在一段时间里估计很难获得新功能（更不敢提我想要新的 UI）。

在可预计的未来里，我会保持 Evernote 的订阅很久，只是可能慢慢的会从 Premium 降为 Standard（甚至降为 Free？）。

## 参考文章

- [Extras and Manuals - DEVONtechnologies](https://www.devontechnologies.com/download/extras-and-manuals.html "Extras and Manuals - DEVONtechnologies")
- [DEVONthink Part 4 - Duplicates, Replicants and Bookmarks — MyProductiveMac](https://sspai.com/post/[http://www.myproductivemac.com/blog/devonthink-part-4-duplicates-replicants-and-bookmarks19102015] "DEVONthink Part 4 - Duplicates, Replicants and Bookmarks — MyProductiveMac")
- [Thinking different about groups and tags in DevonThink | Arno's tech blog](https://arnostechblog.wordpress.com/2017/05/20/thinking-different-about-groups-and-tags-in-devonthink-groups-are-tags-and-tags-are-flags/ "Thinking different about groups and tags in DevonThink | Arno's tech blog")
- [iPad Diaries: DEVONthink’s New Advanced Automation – MacStories](https://www.macstories.net/ios/ipad-diaries-devonthinks-new-advanced-automation/ "iPad Diaries: DEVONthink’s New Advanced Automation – MacStories")
- [Collecting and Reading with DEVONthink - MacDrifter](http://www.macdrifter.com/2016/11/collecting-and-reading-with-devonthink.html "Collecting and Reading with DEVONthink - MacDrifter")

![](attachments/2ec6acc9ae3fc206.jpg)

#### DEVONthink To Go

iOS

[相关文章](https://sspai.com/app/DEVONthink%20To%20Go)

下载

> 拿不定主意选什么 App，下载少数派 iOS [客户端](http://sspai.com/s/nqQk "客户端")、关注 [少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，我们帮你做选择


---

[🌐 原始链接](https://sspai.com/post/44648)
[📎 在印象笔记中打开](evernote:///view/207087/s1/f67989fb-fecf-4b61-a7bf-62d549469afe/f67989fb-fecf-4b61-a7bf-62d549469afe/)
