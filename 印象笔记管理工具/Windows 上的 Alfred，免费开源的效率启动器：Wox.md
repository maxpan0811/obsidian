# Windows 上的 Alfred，免费开源的效率启动器：Wox

---

Windows 上的 Alfred，免费开源的效率启动器：Wox
================================

2016年03月28日

[![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/8BBB6BDB-186B-482E-81BD-E6471E5BA30E)](https://sspai.com/user/693646)

#### [MakicLin](https://sspai.com/user/693646)

目录

没听说过 Alfred？
------------

[Alfred](https://sspai.com/post/tag/alfred) 是 Mac 平台上无可争议的效率启动神器，它是增强版的 Spotlight，除了快速执行启动应用、计算公式、搜索一切之外，还有强大的可扩展性，拥有众多的功能扩展插件。

少数派此前已对 Alfred 作过多篇文章介绍，[点此阅读](https://sspai.com/post/tag/alfred)。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/2AA9163B-7E99-4F8B-8B1F-2754481722C3)

在 Windows 上也有类似的效率软件，名叫 Wox，它拥有和 Alfred 相同的使用方式和逻辑。

Hello，Wox！
----------

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/4E4FEE89-8206-4A74-9CED-08440E6E325A)

[下载 Wox](http://www.getwox.com/)，无需安装，解压出来的文件夹就是软件目录，打开文件夹中的 Wox.exe 即可开启 Wox。和 Alfred 相似，按下 Alt+Space 输入「chrome」，你就可以通过 Wox 快速启动 Chrome。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/8948FFB4-B7EA-4247-B413-FE711C5E4B7D)

需要注意的是，由于 Wox 1.2.0 自带了 Everything 插件，Wox 会启动 [Everything](https://www.voidtools.com/)（一个 Windows 上的本地文件搜索引擎），不影响实际使用。

Alt+Space，然后呢？
--------------

此时，你已手握「神器」，但可能不知从何下手。除了启动软件，搜索文件之外，Wox 还可以做很多事情，下面介绍几种 Wox 的实用用法。

和 Alfred 一样，Wox 除了自带的基础功能之外，也支持扩展插件。基础功能在呼出 Wox 之后可以直接使用，比如计算器，直接输入数学式即可。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/6B1119F7-7C7D-4B08-BDFF-607541750292)而插件功能则需要输入「触发关键词」，比如货币换算是输入「cc」触发。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/5B232744-D819-426D-BEC3-B6E0BAC41EF9)

### 插件安装

通过安装插件，Wox 的功能得以延展。你可以前往 [官网插件页面](http://www.getwox.com/plugin) 找到 Wox 已有的插件列表。安装方式是输入触发关键字「wpm install + 插件名」。以安装有道翻译插件为例，安装命令为：`wpm install youdao`。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/D7D8CB0D-32EF-411B-9789-03DB930D3143)

### 查看天气

你可以通过 Wox 快速查看各地天气，触发关键字为 *weather*，安装命令：`wpm install weather`。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/7D76DF23-6717-466C-9319-ED95494D492E)

### 剪贴板历史

Wox 也可以记住复制过的内容并可随时调用，只需要安装 ClipBoard History 插件即可实现，触发关键词「cb」，安装命令：`wpm install Clipboard History`。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/8F2EC5CC-0E82-440D-8773-492D3C53944F)

### 弹出 USB 设备

Remove USB 插件让我们可以通过 Wox 快速的移除 U 盘等 USB 设备，触发关键字「reu」，安装命令：`wpm install Remove USB`。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/7ED56491-5249-44D3-A11F-1E3D711C2519)

### 网页搜索、添加搜索引擎

搜索引擎是 Wox 不可或缺的功能。呼出 Wox 之后输入触发关键字「g」便可调出谷歌搜索，而维基百科的触发关键字为「wiki」。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/9F3B5DD8-63B7-4C41-9B92-FD933A22FCDC)如果需要使用百度或其他搜索引擎该怎么办呢？我们需要动手添加搜索引擎。打开「设置菜单→ 插件」中的「网页搜索」，点击「添加」即可。以百度为例，配置如图：

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/B7368C45-1F0F-4812-9A8C-C0366E3CE23F)

触发关键词按自己喜好设置，图标可在类似 [*Easyicon.net*](http://easyicon.net/) 图标搜索引擎中取得。其中的 URL 是重要内容，百度的 URL是：`https://www.baidu.com/s?wd={q}`。这个 URL 并非凭空得来，根据下面的方法可以得出各种搜索引擎的 URL：

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/17B0293E-EB0D-492D-975F-CA251634EB21)

依此方法，我们也可以得到的知乎搜索引擎 URL：`http://www.zhihu.com/search?type=content&q={q}` 。

### 命令行

如果你是靠命令行使用电脑的进阶用户，Wox 也可以方便地实现 *Win+R* 的功能。你只需要输入符号「>」，Wox 就和 Win+R 一样了。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/142640DE-FB70-4649-A8CC-854DD5E09946)

需要注意的是，安装 Wox 之后，*Win+R* 的快捷键会被 Wox 接管，可以到「Wox 设置菜单 → 插件 → 命令行」中恢复。

除此之外，通过安装插件，Wox 还可以实现更多功能，各位可以前往 [官网插件页面](http://www.getwox.com/plugin) 和 GitHub 上寻找更多插件。

更合我意的 Wox
---------

对 Wox 进行一些简单的设置，可以让它更合我们的心意。

### 主题外观

我们可以在 Wox 的设置菜单的「主题」选项下选择内置的主题，也可以到 [官网主题页面](http://www.getwox.com/theme/builder) 在线定制主题。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/0F9D0D56-BE37-41C2-AC4D-5B644ABBCD4E)

### 热键自定义

举个例子，为了快速调用剪贴板历史，我们可以将 *Alt+C* 映射为关键词「cb」，当你之后按下 *Alt+C* 的时候，Wox 会呼出并自动输入「cb」。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/03FFEE9D-7E8E-4AAE-8932-B496F5D7A3FF)

### 更合理的触发关键词

有些插件的触发关键词可能不太好记，大家可以在「设置菜单 → 插件」中自定义每个插件触发的关键词。

如果需要管理插件，可以输入关键词 *wpm* 触发插件管理。

![](.evernote-content/BB14EB86-9E93-4A0E-B34C-EF9FA0912BB1/23BA0513-BE0F-4ABF-B29F-F0D07FD8FACD)

结尾
--

虽然 Wox 相比 Alfred 在插件和具体设置上还相差较远，但其核心体验已经非常接近，已经可以算是 Windows 上的效率启动利器了。

你可以在 [Wox 官网](http://www.getwox.com/) 免费下载 Wox。同时，Wox 也是一个开源项目，你可以在 [Github 页面](https://github.com/Wox-launcher/Wox) 了解详情。

[启动器应用](https://sspai.com/tag/%e5%90%af%e5%8a%a8%e5%99%a8%e5%ba%94%e7%94%a8) [Windows](https://sspai.com/tag/Windows) [效率工具](https://sspai.com/tag/%e6%95%88%e7%8e%87%e5%b7%a5%e5%85%b7)

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

---

[🌐 原始链接](https://sspai.com/post/33460)

[📎 在印象笔记中打开](evernote:///view/207087/s1/49cf80cc-090a-44f8-8530-62b769148f6e/49cf80cc-090a-44f8-8530-62b769148f6e/)