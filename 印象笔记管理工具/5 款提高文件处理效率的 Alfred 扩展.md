# 5 款提高文件处理效率的 Alfred 扩展

---

通过简单的指令即可实现原本很复杂的操作，作为 Alfred 的核心功能，各种各样的「扩展」（Workflow）在实际操作中给我们带来了极大的方便，也使得这款应用变成了名副其实的效率工具，深受效率达人的喜爱。

在[此前的文章](http://sspai.com/32281)中，曾经和大家分享了 4 款在本地快速查看常用网站内容的扩展，今天介绍的这 5 款 Alfred 扩展，都是能够极大提高文件处理效率、简化文件处理的流程的，如果你平时需要经常对文件进行管理操作，它们多半会是你想要的。

快速在当前 Finder 窗口创建新文件
--------------------

OS X 不像 Windows 那样可以直接鼠标右键创建新文件，不得不说是个小小的缺憾。**NewFlie** 这款插件则完美解决了这个问题。

Alfred 中输入关键词「nfo + 空格+文件名.后缀」，即可在当前 Finder 窗口下新建并打开一个文件，支持的文件格式包括 text、html、markdown 等。「nf + 空格 + 文件名.后缀」则是只新建文件但不打开。多个文件之间用「/」分隔。

如果当前没有打开的 Finder 窗口，则默认在桌面上新建你指定的文件。

[点此下载该扩展 >](http://www.packal.org/workflow/newfile)

![](.evernote-content/89CA2EB5-2092-420C-AD51-F6EF4B099B93/2342535F-79D8-49A4-A833-31AFAFC425B5.gif)

快速调整图片尺寸
--------

我在写博客的时候，经常需要对图片大小调整后才能上传，于是每次都要将图片一张张打开，实在是非常麻烦。如果你有和我类似的困扰，**Resize Image** 这款扩展或许很适合你。

它可以帮你快速调整图片尺寸，而无需打开图片。

使用方法很简单，选中你需要调整尺寸的图片，然后调出 Alfred，输入关键词「rimage + px」并按下回车即可（px是图片的宽度）。Resize Image 不会改变图片原本的长宽比。

[点此下载该扩展 >](http://www.packal.org/workflow/resize-image)

![](.evernote-content/89CA2EB5-2092-420C-AD51-F6EF4B099B93/B2A74831-783E-4438-9CA7-C67CB90E02FD.gif)

快速切换终端路径
--------

如果你经常用到终端，切换终端路径（cd）会是一件麻烦的事儿，你得把文件夹路径复制到终端中。**Terminalfinder** 这款插件可以帮你解决烦恼。

Alfred 输入关键词「ft」，即可以当前 Finder 窗口路径作为默认路径打开 terminal。关键词「tf」，则是打开当前 terminal 所在路径对应的文件夹。

除了 Finder 和 Terminal 之外，这款插件还支持 iterm 以及 Path Finder。

[点此下载该扩展 >](http://www.packal.org/workflow/terminalfinder)

![](.evernote-content/89CA2EB5-2092-420C-AD51-F6EF4B099B93/6E813639-3F1D-4045-839B-C7DCE60DAF28.gif)

查看最近使用文件
--------

有些文件或文件夹是你最近使用过的，现在你又要用到它了，怎么才能快速得找到它们？

配合 **Recent Documents** 扩展，你只需在 Alfred 窗口中输入「recent」，即可查看最近使用过的文件或文件夹。个人认为这款扩展可以一定程度上取代 [Dropzone](http://sspai.com/tag/Dropzone) 或者 [Yoink](http://sspai.com/tag/Yoink) 之类的应用了。

[点此下载该扩展 >](http://www.packal.org/workflow/recent-documents)

![](.evernote-content/89CA2EB5-2092-420C-AD51-F6EF4B099B93/7CF67B3D-1DC4-4949-A120-9E457FBA69F2.jpg)

让 Alfred 中的 Snip 也拥有文本展开的功能
---------------------------

[TextExpander](http://sspai.com/tag/TextExpander) 是一款强大的文本快捷输入工具，但它的价格实在有些贵。如果你只是想使用其中的文本展开功能，那么 **BetterSnip** 这款扩展也许就足够了。

在 Alfred 中添加一个类似下面格式的 Snip：

*我是{Name},我生活在{country}*

*<<<{Name},{City}>>>*

下次使用时，按照以下步骤：

1. 在 Alfred 窗口中选择这条 snip，复制到剪贴板。
2. 在 Alfred 窗口中输入 「bsnip luiyezheng;中国」回车。
3. 按下「command + V」 粘贴，即可输入 「我是luiyezheng，我住在中国」。

[点此下载该扩展 >](https://github.com/luiyezheng/Alfred-workflow/tree/master/BetterSnip)

![](.evernote-content/89CA2EB5-2092-420C-AD51-F6EF4B099B93/18E91488-DE19-4A5C-B54B-CF7D0142CBD4.gif)

以上就是今天要向大家推荐的五款 Alfred 扩展，希望你们喜欢。同时大家也可以去 [Alfred 社区](http://www.alfredforum.com)、 [Workflows 平台](http://www.alfredworkflow.com/)等网站查看和下载自己需要的扩展。

**关联阅读：**

* [4 款「本地化」的 Alfred 扩展分享](http://sspai.com/32281)
* [OS X 效率启动器 Alfred 详解与使用技巧](http://sspai.com/27900)
* [OS X 效率启动器 Alfred 的 5 个实用扩展推荐（一）](http://sspai.com/27854)
* [OS X 效率启动器 Alfred 的 5 个实用扩展推荐（二）](http://sspai.com/27929)
* [OS X 效率启动器 Alfred 的最佳伴侣：Alfred Remote for iOS 上手详解](http://sspai.com/28137)

文章来源 [少数派](http://sspai.com) ，原作者 [luiyezheng](http://sspai.com/author/713414) ，转载请注明原文链接

原文可获取应用下载链接：[5 款提高文件处理效率的 Alfred 扩展](http://sspai.com/32680)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/89CA2EB5-2092-420C-AD51-F6EF4B099B93/4036019E-033B-46A3-A501-BC9FB700007C.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:buyAW/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fwatch%2Fbuy%2F)

---

[🌐 原始链接](http://sspai.com/32680)

[📎 在印象笔记中打开](evernote:///view/207087/s1/42f23753-b932-4900-af6c-5c5cb5f3b3e8/42f23753-b932-4900-af6c-5c5cb5f3b3e8/)