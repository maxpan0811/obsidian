# 在 Windows 上如何管理 Hosts？这里有 3 款小工具推荐给你

---

在 Windows 上如何管理 Hosts？这里有 3 款小工具推荐给你
====================================

[![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/908FA46B-E803-47E0-9E4B-6AB1DE8150C0.png)](https://sspai.com/user/724096)

#### [Eric\_hong](https://sspai.com/user/724096)

02月14日

99  [10](#)

用户在浏览器地址栏输入访问的网址域名时，需要转换成 IP 地址才能让计算机理解要找到哪个服务器，而 DNS 服务器的作用就是将网址转换为 IP 地址。在查询 DNS 服务器时，可能需要消耗一定的时间，或者由于某些原因遭到 DNS 污染或者劫持，导致网络访问出现问题。

系统里有一份名为 Hosts 的文件，用于储存计算机网络中各节点信息，负责将主机名称映射到 IP 地址，系统会在 DNS 请求查询之前，系统首先查询本地 Hosts 文件是否存在这个地址映射关系，如果有就直接调用，没有的话再向 DNS 服务器查询域名解析。从这个角度来看，Hosts 文件可以用来提高解析效率。

手动修改 Hosts 文件
-------------

Windows 系统中 Hosts 文件的具体路径位于 `C:\Windows\System32\drivers\etc\hosts`，用户可添加或者修改类似 `IP + 空格 + 域名` 的形式正确改变 Hosts 文件内容。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/2457A914-6F6F-4C1E-AD65-16D21811D4EA.jpg)

常见的系统 Hosts 文件内容

打开命令行窗口，输入以下命令，使本地的 Hosts 文件生效：

```
ipconfig /displaydns //显示DNS缓存内容

ipconfig /flushdns //删除DNS缓存内容
```

不过，与手动更改 Hosts 文件相比，如果借助第三方工具的话，可以实现更好用的功能：

* 快速备份 Hosts 文件；
* 一键切换不同的 Hosts 规则；
* 本地和远程调用 Hosts 文件。

SwitchHosts!
------------

[SwitchHosts!](https://oldj.github.io/SwitchHosts/#cn) 是一个管理、切换多个 hosts 方案的工具。由于 Hosts 文件的特殊性，所以用户使用 SwitchHosts! 工具时需要以管理员身份运行才能更好实现软件的功能。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/734D9E26-E7AF-4819-A6D1-F0DAB77EA689.jpg)

SwitchHosts! 主界面

SwitchHosts! 支持 Windows、Linux、macOS 平台，经过一段时间的体验，软件有以下几大特点：

**语法高亮**：Hosts 文件内容本身就是依据语法编写的解析规则，用户使用系统内置的笔记本应用也可以打开 Hosts 文件，但如果存在太多地址映射解析的规则，整个文档会显得混乱。SwitchHosts! 支持了语法高亮特性，方便用户区分和更好地阅读 Hosts 文件内容。

**方案允许多选**：SwitchHosts! 一大特色就是支持建立多个 Hosts 文件方案，软件默认会自动生成名为 「My hosts」、「backup」两个 Hosts 文件，「backup」就是用户系统原本的 Hosts 文件内容。通过单独的开关设置，让用户一键切换不同的 Hosts 方案，或者同时打开多个方案。SwitchHosts! 会将多个方案自动合并到位于左边栏的「系统 Hosts」文件里，并且在任务栏里弹出消息提醒。**点击行号快速切换注释**：Hosts 文件中可以在开头使用 `#` 注释，使某条地址解析失效。SwitchHosts! 则支持点击代码阅读的行号来快速实现注释的效果，无需再手动敲打 `#`。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/47A32E90-83B9-4C0B-8CD1-678E5847F1C4.gif)

点击行号注释规则

**系统托盘快速切换**：鼠标右键点击 SwitchHosts! 在系统托盘的应用图标，用户即可通过弹出选项中快速切换预设好的 Hosts 方案。

**本地/远程方案**：SwitchHosts! 支持本地和远程地址两种方式添加 Hosts 文件方案。当然，用户还可以通过导入/导出功能，实现备份和恢复不同的 Hosts 文件。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/933A9CFC-B528-4C3E-8611-F8E45E540BBE.gif)

添加本地/远程方案

SwitchHosts! 的 macOS 版本里，还支持 Alfred 快速调用。你可以在[作者网站主页](https://sspai.com/post/(https://blog.oldj.net/2017/04/03/switchhosts-with-alfred/))了解更多软件支持 Alfred 背后的开发故事。在一键切换、Hosts 规则显示高亮和最小化到系统托盘上，SwitchHosts! 均提供了不错的支持功能，尤其在一键快速切换功能上，简单的操作方便了开发者在做本地开发时需绑定特定的 Hosts 方案。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/1D1AF72C-F96E-4A23-AA7F-626EAF64BB79.png)

#### SwitchHosts!

Windows

[相关文章](https://sspai.com/app/SwitchHosts!)

下载

Multiple-host
-------------

[Multiple-host](https://github.com/liyangready/multiple-host) 更多是为了解决程序猿开发过程中需要频繁切换 Hosts 的问题，软件在以下几个方面为开发和测试提供了便利：

**唤起使用虚拟 Hosts 环境的浏览器**。在 Multiple-host 开始使用的标签页中，软件支持唤起使用虚拟 Hosts 环境的浏览器，分别有 Chrome、Firefox、IE 三大浏览器，如果用户系统中安装对应的浏览器不在其默认的 C 盘文件路径中，则可以在「设置 - chrome 启动路径/firefox 启动路径」选项中进行修改。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/A682ED8F-3AEB-414E-9791-02D09274DF4A.jpg)

唤起虚拟 host 的浏览器

被唤起的浏览器只受虚拟 hosts 规则影响，并且不会加载任何的第三方扩展插件，而用户还可以正常使用浏览器。这样的好处在于方便测试不同的 Hosts 规则产生的效果。

**一键启用代理 Hosts**。在代理 host 标签中，用户可以通过「新增环境」来建立一个全新的 Hosts 文件，双击环境名称进入编辑界面，用户可以自定义不同的规则，Multiple-host 会在保存之后自动筛选出生成的 Hosts 规则和注释，方便用户做进一步的开关操作。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/D601263E-0BCF-40EB-A72A-5C79158965DC.gif)

代理 host

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/37BFAECE-B8C0-47E2-BBDE-4B346A6BB63A.png)

#### Multiple-host

Windows

[相关文章](https://sspai.com/app/Multiple-host)

下载

Hozz
----

[Hozz](http://blog.zhangruipeng.me/Hozz/) 使用了 Javascripts 语言编写，支持 Windows、macOS、Linux 平台，作者在软件官网注明了软件分别在各自的系统版本中进行了测试使用。不过我下载 Windows 10 64位的软件版本，出现未能成功启动软件的问题，换用 Windows 7 版本则不会出现问题，感兴趣的用户需要注意这一点。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/76DAE8F2-3294-414B-877A-8790F3CC9A20.gif)

开关切换

Hozz 内置了简单的开关键功能，支持不同 Hosts 文件快速切换，拖拽文件至边栏实现快速导入 Hosts 文件。用户还可以加载远程地址来获得在线 Hosts。由于我在体验过程中，Hozz 设置页面未能成功弹出，按照官方说明，软件的设置页面，提供了导入导出 zip 文件以及生成 Surge 的配置文件。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/B23410F3-68D9-4B92-AAE8-CA2A531970A9.jpg)

新建 Hosts 界面

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/1BD7ECE5-8BBF-43C5-B8DA-7057396CF5C4.png)

#### Hozz

Mac

[相关文章](https://sspai.com/app/Hozz)

下载

打造个人的同步在线 Hosts 文件
------------------

前面体验了三款快速切换 Hosts 的工具，其中有软件支持远程调用 Hosts 文件的功能，所以在这部分简单介绍如何打造属于自己的同步在线 Hosts 文件。

在这里，我使用了「Github 网站 + SwitchHosts!」，具体步骤：

在 Github 上新建项目 new repository，填写好项目的名称、是否公开、是否创建说明文档等信息；

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/DD1B611D-5D91-48BD-8577-8F61CC12CABB.jpg)

New repository

创建好项目之后，点击「create new file」创建一个新文件，比如创建一个名为 hosts 的文件；

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/094F3F08-6806-4DC2-9620-F3B84EF68B5F.jpg)

Create new file

在代码编辑窗口里，按照 `IP + 空格 + 域名` 的形式创建好规则，确认后点击「Commit new file」；

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/7A4CA694-89E3-4532-A522-7A390A0BB435.jpg)

Commit new file

接着就需要获取 hosts 文件的在线更新地址，点击「Raw」即可转换为在线更新地址；

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/4754EEF7-312C-4D85-9DE7-356FCBFECFFB.jpg)

Raw

最后打开软件 SwitchHosts!，进入「添加 - 远程」，将第四步得到的在线地址填写在 URL 地址里，设置好自动更新的时间，点击确认完成打造个人的同步在线 Hosts 文件。

![](.evernote-content/C82D0914-E0D8-4A71-8D42-B2B7556C71E6/6AFCE221-3C83-404F-B860-314DE01E2862.jpg)

使用 SwitchHosts! 远程方式添加规则

灵活管理 Hosts 文件
-------------

由于 Hosts 文件在系统中有着提升网址域名解析效率的作用，灵活管理好 Hosts 文件方便了做开发调试工作，网上有开发者还共享了去广告和特殊功能的 Hosts 文件。而借助第三方工具，便于备份文件，快速切换不同的 Hosts 文件，甚至是启用远程共享的 Hosts 规则。考虑到 Hosts 文件在系统中有特殊作用，其安全性也应该引起大家重视，不随便添加网上的规则，同时做好 Hosts 文件的备份工作。

DNS 设置选项参考少数派分享文：[网速变慢？你可能需要先设置好 DNS | 科普](https://sspai.com/post/42125)

---

[🌐 原始链接](https://sspai.com/post/43248)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4e7ee255-1394-4a4a-989d-4666a1d8b9c6/4e7ee255-1394-4a4a-989d-4666a1d8b9c6/)