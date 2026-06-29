---
title: 文献管理利器 Zotero 设置技巧 - 少数派
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/文献管理利器 Zotero 设置技巧 - 少数派.html
tags: [印象笔记]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "文献管理利器 Zotero 设置技巧 - 少数派"
source: evernote
type: note
export_date: 2026-06-26
guid: ce0a3ca9-7538-4c32-96a1-4c7f2b75fec1
---

# 文献管理利器 Zotero 设置技巧 - 少数派

# 文献管理利器 Zotero 设置技巧

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

在之前的 
[文章](https://tomben.me/posts/2019/10/06/suggestions-for-writing-thesis.html#endnote) 中，我提到文献管理软件多如牛毛 —— [EndNote](https://endnote.com/)、[Papers](https://www.papersapp.com/)、[Mendeley](https://www.mendeley.com/)、[Citavi](https://www.citavi.com/en)、[NoteExpress](http://www.inoteexpress.com/aegean/) 等等，并演示了结合 EndNote 和 Word 实现参考文献自动化的操作步骤。但实际上，我一直没有深入使用过任何一款文献管理工具 1 ，主观上有两方面的原因：一是我的文献数目较少，人工管理也还可以，二是文献条目输出需求不高，因为我一般都是直接上数据库网站或者 Google Scholar 下载 BibTeX 文件 2 。

客观上，我之前使用过的文献管理软件确实不太好用 —— 说的就是你，EndNote。不知道什么原因，EndNote 在 macOS 上总是很卡顿，从 Mojave 10.14 开始就与系统显得格格不入，最受不了的一点是它会把导入的 PDF 附件复制一份到自己的数据库中，命名方式还不够友好，强迫症表示不能接受。macOS Catalina 
[不再支持 32 位应用程序](https://support.apple.com/zh-cn/HT208436) 之后，EndNote 作为电脑中少数几个 32 位应用，就被我「名正言顺」地抛弃掉了 3 。

由于不使用文献管理工具，我的文献管理得很不好，常常散落在四处：iCloud、Dropbox、坚果云、本地磁盘..... 到处都是，并且分类混乱，阅读与查找起来很不方便。

最近着手写作毕业论文，参考文献数目激增，我意识到不能再像以前那样「自由放任」地管理文献了。因此我想要寻找一个文献管理工具 —— 既没有 EndNote 的毛病，又能帮助我高效管理文献。幸运的是，我找到了，它就是 
[Zotero](https://www.zotero.org/)！

## Zotero 简介

![](attachments/e556cab37ab2ae73.png)

正如 
[Zotero 官网](https://www.zotero.org/) 介绍的一样，Zotero 是一个免费、易用的个人研究助手，可以帮助你收集、组织、引用和分享文献。与此同时，Zotero 是一个 [开源软件](https://github.com/zotero)，很多人为 Zotero 开发了各种各样的 [插件](https://www.zotero.org/support/plugins)，使得 Zotero 功能丰富，探索潜力无穷。网络上关于 Zotero 的教程可以说是汗牛充栋，因此，本文不会介绍 Zotero 的基本使用，而会介绍一些 Zotero 的特色功能和不太常见的设置技巧。

## 添加文献

添加文献是文献管理的第一步，而 Zotero 添加文献的方式可以说是它的一大特色，让人眼前一亮。在下载 Zotero 的时候，
[Zotero 的下载页面](https://www.zotero.org/download/) 会提示我们下载两个部分 —— Zotero 软件本体和浏览器插件 Zotero Connector，其中 Zotero Connector 支持 Chrome、Firefox，暂不支持 Safari，但是目前的 [Zotero Beta](https://forums.zotero.org/discussion/80255/available-for-beta-testing-zotero-connector-for-safari-13/p1) 版本包含 Zotero Connector for Safari，相信不久之后的正式版就可以在 Safari 中使用 Zotero Connector 了。

![](attachments/d0bc0c89d5b4e338.png)

当我们浏览数据库时，Zotero Connector 会自动读取当前页面的信息，图标也会随着内容进行变化。比如，打开中国知网之后，点击 Chrome 浏览器右上角的 Zotero Connector 图标，就会自动将该页面的数据保存到 Zotero 中
4 ，如果有下载全文的权限，还会将 PDF 附件一同保存下来。

![](attachments/65e84fde5b946feb.png)

然后打开 Zotero，会发现文献信息连同 PDF 一起保存了下来，并且光标自动定位到了刚刚保存的这条文献条目上。

![](attachments/77b5bca0a5a02946.png)

一般来说，Zotero 会识别常用数据库，正确地保存文献信息。并且不止学术网站，像 
[豆瓣](https://www.douban.com/) 这样的网站也是可以识别的，你可以在 [这里](https://github.com/zotero/translators/tree/b80ec528f6ac8c17523354b91893e3772d7ff715) 找到 Zotero Connector 支持的全部网站，不得不说开源的力量确实很强大！

值得注意的是，我们应该等待网页加载完成之后再点击 Zotero Connector 图标，否则文献数据可能无法被正确地识别，而仅仅被保存为「网页」。

除了利用 Zotero Connector 添加文献，Zotero 还支持通过输入 ISBN 或 DOI、直接拖拽 PDF 或其他附件、RSS 订阅导入、从其他文献管理工具导入等方式添加文献。可以这样说，添加文献在 Zotero 面前简直就是小菜一碟。

## 同步设置

刚接触 Zotero 的时候，它的同步机制是让我比较困惑的地方，网上的大部分教程似乎也没有说得非常清楚。几经折腾，我终于明白了 Zotero 的同步机制：数据同步是通过 Zotero 的服务器进行的，同步的是条目信息，文件同步可以选择 Zotero 或 WebDAV 协议进行同步，同步的是附件。

![](attachments/b7d341ad8f38c492.png)

Zotero 免费账户提供了 300MB 空间用于同步，可通过付费扩容，套餐价格如下表所示。

| Storage Amount | Annual Price (USD) |
| --- | --- |
| 300 MB | Free |
| 2 GB | $20 |
| 6 GB | $60 |
| Unlimited | $120 |

不得不说这个价格还是非常昂贵的，幸好 Zotero 提供 WebDAV 协议来同步附件，也就是非常占用空间的 PDF 等附件。
[坚果云](https://www.jianguoyun.com/) 作为国内唯一支持 WebDAV 协议的网盘，成为很多 Zotero 教程用到的同步工具，就连坚果云官方也进行了介绍，你可以前往 [坚果云帮助中心](http://help.jianguoyun.com/?p=3168) 查看。

然而，通过坚果云的 WebDAV 同步之后，得到的附件会如下图所示 —— 文件夹命名不规则，难以区分。如果在 iPad 上阅读，想要找到需要查看的文章，简直就是一场噩梦。

![](attachments/9d08666c306e25b1.png)

那么应该怎么做？得益于 Zotero 丰富的插件，我们可以利用 
[Zotfile](http://zotfile.com/) 来避免文件乱命名的问题，更加高效地管理附件。

## 附件设置

在 
[这里](https://github.com/jlegewie/zotfile/releases) 下载以 `.xpi` 结尾的 Zotfile 插件之后，在 Zotero 中安装，然后进行相关设置。

首先打开 Zotero 的偏好设置，前往 
`高级 -> 文件和文件夹`，查看数据存储位置，默认是 `~/Username/Zotero`，这是存放文献条目数据的文件夹目录 5 。我为了将其同步，选择的是坚果云中的一个同步文件夹 `~/Username/Nutstore Files/Zotero/Zotero`。

然后点击 Zotero 上方 
`工具 -> Zotfile Preferences`，打开 Zotfile 的偏好设置。将 `Source Folder for Attaching New Files` 的路径设置为 Zotero 数据文件夹下的 `storage`，这是为了让 Zotfile 监控 Zotero 默认的附件存放目录，从而对附件进行重命名、移动等操作。比如我设置的就是 `~/Username/Nutstore Files/Zotero/Zotero/storage`。

最后将 
`Location of Files` 下的 `Custome Location` 设置为 `~/Username/Nutstore Files/Zotero/Attachments`，因此，我的坚果云同步文件夹中就存放了所有的 Zotero 数据，目录结构如下：

```
Zotero
├── Zotero  # Zotero 数据库文件夹
	│   ......
	├── Attachments   # 附件文件夹
	│   ├── Journal
	│     ├── Year
	│       ├── Attachment-1
	│   ├── Publisher
	│     ├── Year
	│       ├── Attachment-2
	│   ├── ......
```

### 删除多余附件

通过 Zotfile 管理附件存在一个问题：在 Zotero 中删除的文献条目，不会使附件文件夹中对应的附件自动删除，这也是 
[很多 Zotfile 用户](https://github.com/jlegewie/zotfile/issues/96) 希望增加的功能，尽管 Zotfile 目前还不支持，但有用户提供了一个 [变通方法](https://github.com/jlegewie/zotfile/issues/96#issuecomment-505084568)：

1. 关闭 Zotero 附件同步，这里假设附件目录为 `~/Username/Nutstore Files/Zotero/Attachments`。
2. 将 Zotfile 文件夹更改为任何一个其他的目录，比如 `~/Username/Desktop/Zotero`。
3. 在 Zotero 中选择所有条目，点击右键，选择 `Manage Attachments -> Rename Attachments`，然后 Zotfile 会自动将 Zotero 数据库中存在的条目对应的附件移动到新文件夹中，也就是 `~/Username/Desktop/Zotero`。
4. 将最初的文件夹中的所有内容删除，在删除前最好同步一下，避免可能产生冲突。
5. 将 Zotfile 文件夹更改为最初的目录 `~/Username/Nutstore Files/Zotero/Attachments`。
6. 在 Zotero 中选择所有文件，点击右键 `Manage Attachments -> Rename Attachments`，所有的附件就移动到最初的文件夹中了。

因此，确定删除某一篇文献之前，首先应该在 Zotero 中选择它，点击右键，选择 
`打开文件位置`，删除附件，然后再在 Zotero 中删除文献条目。

### 删除重复附件

由于各种原因，有时候同一个文献条目可能对应多个相同的附件，为了解决这个问题，我找到一个还算凑合的方法：

- 安装 [tree](http://mama.indstate.edu/users/ice/tree/)，macOS 上可以使用 Homebrew 快速安装：

```
brew install tree
```

- 进入附件目录，执行 tree 命令：

```
cd Attachments
tree -N
```

在输出结果中，搜寻同一个文件夹下文件名称非常接近的文件，进入相应文件夹，确认无误后，删除多余的即可。这一步有点考眼力劲儿，不过还是很容易发现的，瞧！下图就是我找到的 。

![](attachments/72b6f281f4d3d713.png)

由于 Windows 无法安装 tree（可能有其他功能相似的命令行工具），你可以使用 Visual Studio Code 打开 Attachments 文件夹，在左侧边栏查看当前目录结构，找到重复的附件。

![](attachments/d7a6d16d27d9089f.png)

### 移动或重命名附件

我们存放附件的目录不会一直不变化，可能需要根据情况或对附件文件夹进行重命名或移动，然而一旦我们重命名或移动附件文件夹，Zotero 就无法找到了。当然，你可以点击 
`定位......`，手动让 Zotero 知道对应附件所在的位置，但这样一个一个地操作，效率实在是太低了，特别是在文献条目成百上千的情况下。

![](attachments/e2c14137785fb324.png)

由于附件是由 Zotfile 管理的，如果我们直接修改附件文件夹，就会出现附件找不到的情况。因此，我们应该遵循一个原则：
始终让 Zotfile 知道附件文件夹的位置（这听起来像是一句废话 ）。

假设我要将附件文件夹从 
`Attachment` 重命名为 `Attachments`，那么应该这样操作：

1. 在 `Attachment` 文件夹的同级目录下新建一个空文件夹 `Attachments`，比如我将这两个文件夹都放置在 `~/Username/Nutstore Files/Zotero` 下。
2. 点击 Zotero 上方 `工具 -> Zotfile Preferences`，打开 Zotfile 的偏好设置。将 `Location of Files` 的 `Custome Location` 设置为 `~/Username/Nutstore Files/Zotero/Attachments`。
3. 在 Zotero 中选择所有条目，点击右键，选择 `Manage Attachments -> Rename Attachments`。然后 Zotfile 自动将 `Attachment` 中的所有文件移动到 `Attachments` 中。
4. 删除 `Attachment`，完成 ✌️

由于不可预测的原因，可能路径移动错误（比如手抖点错了，我在测试的时候就抖了一下 ），导致全部附件都无法找到，也不必担心。我们可以利用 
[Zutilo](https://github.com/willsALMANJ/Zutilo) 这个插件，来批量修改附件路径。

前往 
[这里](https://github.com/willsALMANJ/Zutilo/releases) 下载 `zutilo.xpi` 这个文件，在 Zotero 中安装。重启 Zotero，然后在 Zutilo 首选项中将「修改附件」选择为 `Zotero 上下文菜单` 或 `Zutilo 上下文菜单`。

![](attachments/4f6c9de00443d1e8.png)

接下来在 Zotero 中全选所有条目，点击右键，选择 
`Zutilo -> 修改附件路径`。首先填写「要替换的附件目录旧部分路径」，比如 `/Attachment`，然后填写「替换匹配旧部分路径的附件所使用的新部分路径」，比如 `/Attachments`，就可以将全部文献路径修改正确。

![](attachments/31e1650ec71b7a4c.png)

## 小结

Zotero 功能强大，可以高度自定义，多加探索还会发现不少的彩蛋，大幅提高我们的文献管理效率。我接触 Zotero 的时间不长，还有很多技巧或设置没有涉及到，如果你有什么问题或经验，欢迎留言交流与指教。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，找到数字时代更好的生活方式

> 分享你提升效率的种种心得，参加  [征文活动](https://sspai.com/s/JR4j) 还能赢取效率工具 ️

Measure

Measure
