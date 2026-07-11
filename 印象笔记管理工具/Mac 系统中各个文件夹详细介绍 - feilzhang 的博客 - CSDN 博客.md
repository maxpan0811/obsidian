# Mac 系统中各个文件夹详细介绍 - feilzhang 的博客 - CSDN 博客

---

Mac 系统中各个文件夹详细介绍
================

Mac OS X 系统以 Unix 作为核心，根目录为 /

打开 Macintosh HD 你会发现内中有四个文件夹分别为：**应用程序 (Applications)**、 **系统 (System)**、 **用户 (User)**、 **资料库 (Library)** 下面为大家详细介绍下其含义

**Mac OS X**，这是一个基于 UNIX 核心的系统，增强了系统的稳定性、性能以及响应能力。它能通过对称多处理技术充分发挥双处理器的优势，提供无与伦比的 2D、3D 和多媒体图形性能以及广泛的字体支持和集成的 PDA 功能。MAC OSX 通过 Classic 环境几乎可以支持所有的 MacOS9 应用程序，直观的 Aqua 用户界面使 Mac intosh 的易用性又达到了一个全新的水平。

[MAC 硬盘中各个文件夹 \*](https://www.jianshu.com/p/fd80006844c1)

打开 Macintosh HD 你会发现内中有四个文件夹

分别有 —— 应用程序 (Applications)、系统 (System)、用户 (User)、资料库 (Library)。四个文件夹中又分别各有若干数量的文件夹存在。

[1.Applications](https://www.jianshu.com/p/fd80006844c1)

这个当然就是存放各种软件的位置了。

[2.System](https://www.jianshu.com/p/fd80006844c1)

包含由 Apple 安装的系统软件。这此资源是系统正常运行所必须的，位于启动卷宗中

/System/Library/CFMSupport CFM, Code Fragment Manager, 等同旧 Mac OS 应用程序都会使用的共有程式库。以确保 Mac OS 环境的一致性。当中储存有一个在 OS X 中极为重要的档桉 —CarbonLib, 是执行炭火软件时必不可欠的档桉。此外还有 DiscRecordingLib (CD/R-RW 用的程式库), OpenGLLib (OpenGL), stbCLib (c 语言)

/System/Library/DTDs 作为存放系统所使用的各种 XML 档桉，并为其格式定义之档桉. Mac OS X Data 形式製成的文书，分别由三个档桉管理，分别是 PropertyList.dtd,KeyboardLayout.dtd 及 sdef.dtd 三个档桉所组成。而 DTD, 全名为 Document Type Definition. 此外，.plist 档桉亦是由 XML 撰写出来的.

/System/Library/Extensions 其实这裡就是用作存放硬件驱动的地方，苹果不称驱动程序为 driver, 而是称为 Extension.

/System/Library/Filesystems 主要就是用以存放 OS X 对应及支持何种档桉格式的资料。例同标准的 AppleShare (苹果档桉分享标准), ISO 9660/FTP/HFS 及至网络上用的如 Samba 等

/System/Library/HelpViewer 一切和 Mac OS Help 有关的档桉及文件都存放于此

/System/Library/Find 就是搜寻机能了。是对应多国语言的.

/System/Library/OpenSSL 全名为 Secure Sockets Layer. 是一套通讯加密技术，一般用于 Web 服务器上，会将密码传送时以加密的暗号处理，从而减低第三方成功盗 取资料的可能。一般应用于以 https 开首的 URL 上. Mac OS X 内置的 WebServer—Apache, 亦包含这个服务.

/System/Library/CoreServices/Dock 这是 OS X 的特徵之一，这部份是有关 Dock 的资料

/System/Library/CoreServices/Finder.app 这个比较特别，因为这是一个应用而非一个档桉夹，Finder.app 可说是负责掌控整个 OS 上的一切资源.

/System/Library/CoreServices/Kerberos 由 MIT (麻省理工大学) 开发的网络认证技术。能够很简单地以单一 ID 登入系统的检证技术. Mac OS X 支援其版本 4 的 Kerberos. 所谓 Kerberos, 在希腊神话中是一头住在冥界，拥三头，蛇尾的地狱守门犬

/System/Library/CoreServices/Menu ExtrasStatus bar 上面所有系统自带工具的原文件，双击打开可以直接在 status bar 上添加相应文件

/System/Library/CoreServices/Setup Assistant 所有有关设定助理的资料都存放于此.

/System/Library/CoreServices/Software Update 这裡就是负责 Software update 的地方

[3.Library](https://www.jianshu.com/p/fd80006844c1)

系统资源库。

比如字体、ColorSync 配置、偏好设置以及插件都应该安装在 Library 目录下适当的子目录中。

Application Support 包含了应用相关的数据以及支持文件，比如第三方的插件，帮助应用，模板以及应用使用到但是并不需要用来支持运行的额外资源文件。按照惯例，所有这些内容都会被存储在以应用名称命名的子目录当中。

Assistants 包含了帮助用户进行配置或者其它任务的程序。

ColorPickers 包含了用来选择色彩的资源，它们根据某种模型，比如 HLS (色彩角、饱和度、亮度) 选择器或者 RGB 选择器。

ColorSync 包含了 ColorSync 配置和脚本。

Components 包含了系统包和扩展。

Contextual Menu Items 包含了用于扩展系统级菜单的插件。

Dictionaries 包含了系统自带的字典文件。

Desktop Pictures 桌面图片目录。

Documentation 包含了供计算机用户和管理员参考的文档文件和 Apple 帮助包。(Apple 帮助包在 Help 子目录当中。) 在本地域中，这个目录包含了 Apple 公司发布的帮助包 (不包括开发者文档)。

Extensions 包含了设备驱动和其它内核扩展。(只存在于系统域当中。)

Favorites 包含了指向经常访问的文件夹、文件或者网站的别名。(仅仅存在于用户域当中。)

Fonts 包含了用于显示和打印的字体文件。

Java 包含了 Java 运行环境。

StartupItems 包含了在系统导入时刻运行的系统以及第三方脚本和程序。 (更多有关系统导入时刻启动步骤的信息请参考系统启动程序主题)

[4.User](https://www.jianshu.com/p/fd80006844c1)

包含了某个用户专有的资源。这里也有一个 Library 文件夹，不同与上边的那个 Library，是专为你的帐号服务，里面放的是你自己的个性化字体、配置文件等

Applications 包含仅仅当前用户可用的应用。

Desktop 包含了 Finder 在当前登录用户桌面上显示的桌面项。

Documents 包含了用户的个人文档。

Download 包含了下载的各种文档。

Library 包含了应用设置、偏好设置一起其他用户专有的系统资源

Documentation 包含了供计算机用户和管理员参考的文档文件和 Apple 帮助包。(Apple 帮助包在 Help 子目录当中。) 在本地域中，这个目录包含了 Apple 公司发布的帮助包 (不包括开发者文档)。

Extensions 包含了设备驱动和其它内核扩展。(只存在于系统域当中。)

[硬盘中还有几个隐藏文件夹](https://www.jianshu.com/p/fd80006844c1)

1) bin——— 储存有基本的 UNIX 指令

2) sbin——–UNIX 系统指令的储存地方，是比较进阶的指令

3) etc——— 系统设定档桉储存地方

4) var——— 改动频繁的档桉，都置放于此，例如各 log 档桉

5) tmp——–系统的暂存档

6) usr———UNIX 的使用者专用档桉夹

Mac OS X 新建文件夹的方法：从「档案」(File) 选单中选取「新建文件夹」(New Folder) 即可

---

[🌐 原始链接](https://blog.csdn.net/feilzhang/article/details/89485406)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1e4b7b18-ebff-47a1-9c9b-881104b4d8e0/1e4b7b18-ebff-47a1-9c9b-881104b4d8e0/)