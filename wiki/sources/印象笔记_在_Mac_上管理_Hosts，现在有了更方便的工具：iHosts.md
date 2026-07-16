---
title: "在 Mac 上管理 Hosts，现在有了更方便的工具：iHosts"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/在 Mac 上管理 Hosts，现在有了更方便的工具：iHosts.md
tags: [印象笔记]
---

# 在 Mac 上管理 Hosts，现在有了更方便的工具：iHosts

# 在 Mac 上管理 Hosts，现在有了更方便的工具：iHosts --- ![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/5

---

# 在 Mac 上管理 Hosts，现在有了更方便的工具：iHosts

---

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/55C3E24E-F656-4385-ADCB-37683B40C509.jpg)

少数派之前在《[技巧：利用 AppleDNS 项目加速 Apple 服务](http://sspai.com/33481)》一文中介绍了通过修改系统 Hosts 文件来加速 Apple 服务的方法。不过，这一方法需要使用终端程序来进行，对于一部分用户来说显得不够友好。

如果你是 Mac 用户，你有一个更好的选择来修改系统 Hosts 文件，那就是使用 Hosts 编辑管理工具－－[iHosts](http://h.ihosts.toolinbox.net/cn/)。

Hosts 是什么？iHosts 是什么？
---------------------

对于 Hosts 的原理这里不作深入介绍，[维基百科](https://zh.wikipedia.org/wiki/Hosts%E6%96%87%E4%BB%B6)上是这么介绍 Hosts 的：

> Hosts 文件是一个用于储存计算机网络中各节点信息的计算机文件。这个文件负责将主机名称映射到相应的 IP 地址。Hosts 文件通常用于补充或取代网络中DNS 的功能。

而今天的主角 iHosts 则是 OS X 平台上一款方便我们编辑、管理 Hosts 的软件。相较于通过终端修改系统 Hosts 文件的方法来说，iHosts 可视化图形界面的操作方式显得更为方便、简单。

iHosts 怎么用？
-----------

接下来，我就以 [AppleDNS](http://sspai.com/33481) 项目为例，介绍一下 iHosts 的用法。

在开始前要提醒大家的是，iHosts 仅仅是一个系统 Hosts 的修改以及管理工具，它并不能生成 AppleDNS 的相应配置参数，因此，生成 AppleDNS 配置参数的步骤仍然需要使用终端程序来进行。如果你已经清楚了这一前提，那么，开始吧。

### 1. 生成 AppleDNS 的相应 Hosts 配置参数

[AppleDNS](https://github.com/gongjianhui/AppleDNS) 是 GitHub 上针对 Apple 服务进行加速的一个项目。通过在终端程序中运行相应的脚本文件，我们可以得到对应形式（比如 Hosts）的配置参数。你可以阅读《[技巧：利用 AppleDNS 项目加速 Apple 服务](http://sspai.com/33481)》这篇文章来了解具体方法。

### 2. 修改 Hosts

在生成 Hosts 文件对应的 AppleDNS 参数之后，我们可以通过 iHosts 来进行配置。

打开 iHosts，我们可以通过 Menubar 或者快捷键 ⌘ ＋ E 来打开 Hosts 编辑窗口。点击左下角的加号，我们可以新增一个名为「AppleDNS 」的 Hosts 分组，之后，只要将之前在终端中生成的参数复制粘贴到右侧编辑窗口，即可完成一组 Hosts 的编辑。

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/1A04D289-8912-4B4F-A724-F24A54D0A8D9.jpg)

### 3. 使用 Hosts 分组功能

同样地，我会以配置 AppleDNS 的思路来介绍分组的用法。

现实生活中，很多人会需要在家庭还有办公室等环境中切换网络环境，而 AppleDNS 项目的配置参数又是针对特定网络运营商来生成的，这就对于有频繁切换网络环境的用户造成了不便。利用 iHosts，我们可以很轻松地解决这个问题。

iHosts 支持通过分组管理 Hosts 配置，这里引用一下软件官网的相应介绍：

> 使用分组管理 Hosts 是 iHosts 的一大特色。一般的 Hosts 管理工具都是将 Hosts 文件进行整体替换；而 iHosts 管理的粒度更小，可以仅仅更新其中的一部分，分组则是其中重要的环节。

因此，不管是在移动、联通还是电信的网络环境下，我们可以很方便地通过切换 Hosts 分组的方式来切换相应的 AppleDNS 配置。这里要多提一句，虽然 iHosts 是一款免费软件，不过最多只能添加 4 个 Hosts 节点。你可以通过内购来添加更多节点：

* 升级至 iHost Plus（$2.99），最多添加 10 个 Hosts 节点
* 升级至 iHost Pro（$4.99），最多添加 50 个 Hosts 节点

比如，我们可以通过增加一个名为「Apple-CMCC」分组来完成对于家庭中网络环境下 AppleDNS 的设置，之后，我们可以再设置一个名为「Apple-Unicom」分组来完成办公室环境下的设置，只需要通过 Menubar，我们就可以很方便地切换相应的 Hosts。

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/39FE8FCD-EAEC-49B9-995E-D419059A859C.jpg)

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/2C41BEC6-4E5B-4C6F-86AA-AA78BA5E1918.jpg)

### 4. 实时查看 Hosts

在编辑 Hosts、或开发过程中，很可能需要查看当前的 `/etc/hosts` 内容是什么，这时候就需要用到实时查看 Hosts 这一功能。

点击系统菜单栏中 iHosts 的托盘图标，在弹出的菜单中点击查看「Hosts」，或者通过 ⌘ ＋ V 快捷键，即可打开 Hosts 查看窗口。并且，当 Hosts 发生变化时，这里也会实时更新。

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/8904CF33-B83D-41CA-9E72-8AF0AC351FF8.jpg)

关于沙盒与权限
-------

出于安全的考虑、以及上架 Mac App Store 的条件，iHosts 运行在沙盒模式中，默认不能访问沙盒外的任何文件。如果需要编辑 Hosts，就需要您在首次切换 Hosts 时，允许 iHosts 访问 /etc/hosts 文件。

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/F64DBE0D-E2A7-4DD2-B6AF-745C68FD8962.jpg)

第一次运行 iHosts 时，软件会有弹窗提示我们允许当前用户修改 Hosts，我们只需要接着在终端窗口内粘贴剪贴板内命令并运行即可。

![](.evernote-content/3743F990-51CE-40D8-A800-62506BA4F55E/9AB63683-EA2A-4557-82C4-D0A7EF402671.jpg)

以上步骤看似繁琐，但实际上仅仅设置一次即可，之后则是无痛透明的。另外，这也带来的很大的安全性。毕竟 iHosts 从不以管理员权限运行，也就从根本上保证 iHosts 对您的系统是安全的。所以，为了安全，稍微复杂的操作也是值得的。

你可以在 [Mac App Store](https://itunes.apple.com/app/id1102004240?ls=1&mt=12&uo=4&at=10lJSw) 免费下载 iHosts。应用免费，如需添加 4 组 iHosts 分组则要付费升级。

**参考链接：**[iHosts 使用手册](http://h.ihosts.toolinbox.net/cn/)

文章来源 [少数派](http://sspai.com) ，原作者 [waychane](http://sspai.com/author/703114) ，转载请注明原文链接

原文可获取应用下载链接：[在 Mac 上管理 Hosts，现在有了更方便的工具：iHosts](http://sspai.com/34142)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/34142)

[📎 在印象笔记中打开](evernote:///view/207087/s1/80895a4b-bf5d-4bf0-8680-60ed64fc8818/80895a4b-bf5d-4bf0-8680-60ed64fc8818/)