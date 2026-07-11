# 加强你的「一指禅」：Mac OS X QuickLook 兼容性扩展教程

---

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/6B4D72A1-F319-498F-A46D-2FFBD5A069D4.jpg)

什么是 QuickLook
-------------

QuickLook（快速预览）首次出现在 Mac OS X 10.5 中，用户可以在不开启外部软件的情况下按下空格键快速预览文件，属于 Mac OS X 的优秀特性，它的简单和高效得到很多 Mac OS X 用户的认可。它还有个更传神的名字——「一指禅」。

为什么要扩展 QuickLook 的兼容性
---------------------

当我只是想查看而不修改文件的时候，QuickLook 一直是我的最佳选择。比如查看一个 .psd 文件，只需要选中文件并按下空格键就可以立即弹出，要比打开 Photoshop 快得多。使用过程中，我们也发现 QuickLook 也并非是万能的，有一些文件格式它是打不开的，比如 .markdown, .mkv 等常用格式。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/E4B10652-32B4-4A3B-93F7-FF6A42B7169E.jpg)

还好我们可以通过安装插件的形式扩展 QuickLook 的兼容性。另外，QuickLook 插件不仅可以让它兼容更多格式，还可以让已经兼容的格式呈现出更全面的信息。接下来我们一起了解一下具体步骤：

如何安装/卸载 QuickLook 插件
--------------------

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/4651AA74-33E1-4AA2-9784-140910433C43.jpg)

由于不是苹果官方制作，也没有统一的发行平台，有些开发者会将插件打包成 `.pkg` 安装包，安装较为简单；但有些插件是以单个文件的形式出现，后缀名为 `.qlgenerator`，安装比较繁琐，下面的教程来告诉大家如何安装 `.qlgenerator` 格式的插件，以兼容 [Markdown](http://sspai.com/tag/Markdown) 为例：

**1. 下载插件：**能让 QuickLook 兼容 markdown 的插件不止一个，我从 Github 上面找到 *qlmarkdown* 这个插件。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/3B99C190-27F0-42D8-8BB7-56B225C361CF.jpg)**2. 将插件移动到 `/Library/QuickLook` 目录下：**打开 Finder ，使用「前往文件夹」（菜单栏位置：前往 - 前往文件夹；快捷键：⇧shift + ⌘cmd + G）前往 `/Library/QuickLook`，将刚才下载的插件移动到这里（此处需要输入密码）。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/9435FA09-ADAD-4524-917F-50B2B232FEDA.jpg)

3.使用「终端」重启 QuickLook：我们可以在 LaunchPad 或 Spotlight 中找到 *终端（Terminal）*。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/83B0A83E-BA18-4FB2-8EEB-C409CAB9FEDE.jpg)![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/02BEC584-9F87-44AD-B49B-C9D7D6846466.jpg)

输入 `qlmanage -r` 并回车。看到上面的命令就说明重启成功，这时候我们使用「一指禅」预览 Markdown 文件就不是一片空白了。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/95A907C7-C841-46E1-BE47-0361BE7A4C98.jpg)

更多你可能用得上的 QuickLook 扩展插件
------------------------

### QuickLook Video

这款插件可以让 QuickLook 兼容 .mkv 等非原生支持的视频格式，但并不能正常播放，只能显示出一些视频的缩略图和信息。

* [下载地址（Github）](https://github.com/Marginal/QLVideo/releases/tag/rel-184)

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/B7496E41-C526-4C98-A74C-1D5D67C7CA6C.jpg)

### 程序员系列插件

QLColorCode, QuickLookJSON, QLPrettyPatch 这三款插件分别可以高亮查看代码，JSON 文件以及 Patch 文件。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/CC838128-4E1F-4432-9C11-E9969A7BCE12.jpg)

[QLColorCode 下载](https://qlcolorcode.googlecode.com/files/QLColorCode-2.0.2.tgz) (需翻墙)

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/CDE3143A-77F6-49EF-AEE9-24DA8E3865BF.jpg)

[QuickLook JSON 下载](http://www.sagtau.com/media/QuickLookJSON.qlgenerator.zip)

### BetterZipQL

BetterZipQL 这款插件可以让用户直接使用 QuickLook 查看 Zip 压缩文件的信息以及文件目录。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/68A22D37-5DEB-4CA9-BA0B-FA50EDA06C05.jpg)

[BetterZipQL 下载](http://macitbetter.com/BetterZipQL.zip)

### qllmageSize

这款插件可以在标题栏的位置显示图片文件的分辨率以及文件大小。

![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/FDEFD05B-7E55-44B9-93AE-8010E7773D2C.jpg)[qllmageSize 下载（Github）](https://github.com/Nyx0uf/qlImageSize#installation)

QuickLook 的可扩展性不止于此，更多的插件大家可以去 [QuickLookPlugins.com](http://www.quicklookplugins.com/) 寻找，或 Google 搜索关键词 `QuickLook plugins`。

文章来源 [少数派](http://sspai.com) ，原作者 [MakicLin费浩林](http://sspai.com/author/693646) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/33663051-7EBA-4A7A-AC1B-500C0594037E/D2B884BC-7828-412E-9C5C-23F7949643DF.jpg)](http://aos.prf.hn/click/camref:111l75A/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fshop%2Fbuy-ipad%2Fipad-pro)

---

[🌐 原始链接](http://sspai.com/31927)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c9e5ac43-85cc-4917-8c8e-d1e6bb42ef58/c9e5ac43-85cc-4917-8c8e-d1e6bb42ef58/)