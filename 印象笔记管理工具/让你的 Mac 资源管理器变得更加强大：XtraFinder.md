# 让你的 Mac 资源管理器变得更加强大：XtraFinder

---

![](.evernote-content/5A254503-BD2F-4880-8DA2-FA55544ED3CC/CA6B1FFF-867E-4365-AE2D-26A5F54E05BB.jpg)

如果你和我一样刚从 Windows 迁移到 OS X 的话，可能会怀念 Windows 资源管理器中如下特性：使用 Ctrl + V 剪切文件、右键新建文件等等，因为在 OS X 下这些功能的默认操作都比较麻烦：

* 在 Finder 中，虽然可以通过先复制，再使用 Option + Command + V 的组合键进行剪切操作」，但这种实现方式实际上相当割裂，因为在 OS X 中进行文本剪切使用的组合键为 Command + X ；
* 使用 New File Menu 可以实现右键新建文档，但若勾选的新建文件类型过多的话，则多少会有些「影响市容市貌」。

实际上，通过使用 XtraFinder 这款免费的 Finder 增强应用，不仅可以实现前述功能，而且，还能做到更多。

安装及启用
-----

### 在 Yosemite（OS X 10.10）及以下系统中安装

在 Yosemite 及以下的系统中安装 XtraFinder 非常方便，

1. 前往 [XtraFinder](https://www.trankynam.com/xtrafinder/) 官网，下载最新版本；
2. 双击安装包，按照提示进行即可；
3. 安装成功后，打开 Finder，就可以看到它了。

![](.evernote-content/5A254503-BD2F-4880-8DA2-FA55544ED3CC/E3E79E95-F24C-43BF-98F4-BF52D0C872BF.jpg)

### 在 EI Captain（OS X 10.11）中安装

由于 EI Captain 中增加了一项新的保护机制 —— 系统完整性保护（ System Integrity Protection，简称 SIP）。该机制的开启，将使得 XtraFinder 在 10.11 下无法正常使用（同类应用 [TotalFinder](http://totalfinder.binaryage.com/) 亦如是）。

我并不建议大家修改或关闭 SIP 设置，因为这样会使你的 Mac 在安全性上大打折扣。不过如果你清楚其风险和后果，则可以按照以下步骤关闭 SIP 的部分功能后再安装应用：

1. 重启你的 Mac；
2. 在听到启动声后，按住 `Command + R`（⌘R） 组合键，直到出现  标志，进入恢复模式（如果担心错过时机，你也可以在状态下先按下组合键，再按开机键）;
3. 选择「以简体中文作为主要语言」（或其他语言），点击向右的箭头。在「实用工具」菜单栏中选择「终端」;
4. 输入`csrutil enable --without debug`，回车确认（你也可以输入`csrutil enable`以完全关闭 SIP，但不推荐这么做）;
5. 重启，再安装 XtraFinder 即可。

功能
--

### 为 Finder 添加多标签

在应用设置中勾选「标签页」，可以让你在一个 Finder 窗口中同时浏览多个文件夹，方便文档管理和浏览。

![](.evernote-content/5A254503-BD2F-4880-8DA2-FA55544ED3CC/BB8C9F10-A663-4BAC-92B2-56A5496E266E.jpg)

### 使用 Windows 快捷键管理文件

在「特性」菜单栏中：勾选「剪切和粘贴」可实现使用 Command + X 剪切文件的功能；勾选「按退格键返回」，则可以在 Finder 中使用 Delete 键返回先前浏览位置；勾选「在工具栏中显示返回上层目录按钮」，则将在 Finder 工具栏中增加向上按钮，点击可返回上级目录。

![](.evernote-content/5A254503-BD2F-4880-8DA2-FA55544ED3CC/F31BDFB5-B5C8-4B9E-817F-1F8A98DC5AFC.jpg)

### 为右键菜单添加「新建文件」

在「将项目添加到 Finder 菜单中」：勾选「新建文件」，点击「管理文件模板」，并自行建立需要新建的空白文档即可。需要新建文件时，右键点击「新建文件」，选择相应的文件格式并重命名，即可。

![](.evernote-content/5A254503-BD2F-4880-8DA2-FA55544ED3CC/BE5B932F-12F5-4EF4-BC6E-BD5EB7F1EC29.jpg)

### 更改 Finder 主题外观

在「Apperance」（外观）菜单栏中，勾选「显示彩色侧栏图标」，将出现如下变化。

![](.evernote-content/5A254503-BD2F-4880-8DA2-FA55544ED3CC/CF5109BE-AF0E-43AB-BD05-4AE1D48E4653.jpg)

除此之外，XtraFinder 可以实现的功能还很多，如双栏模式、拷贝路径、显示隐藏项目、永久删除等等。如果你对此感兴趣的话，不妨自行探索一番。

在启用 XtraFinder 后，访问 Finder 的速度可能会变慢，甚至会不时出现无响应的情况，此时强制退出或重启 Finder 即可。如果你想暂时关闭 XtraFinder，前往 Finder，依次点击「Finder」-「XtraFinder」-「Tools」-「重启 Finder」即可。

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

原文可获取应用下载链接：[让你的 Mac 资源管理器变得更加强大：XtraFinder](http://sspai.com/33441)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33441)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bdab0621-5474-4ab5-a52d-b8ac6e256ed3/bdab0621-5474-4ab5-a52d-b8ac6e256ed3/)