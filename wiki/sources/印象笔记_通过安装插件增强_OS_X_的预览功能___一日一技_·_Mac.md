---
title: "通过安装插件增强 OS X 的预览功能 _ 一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/通过安装插件增强 OS X 的预览功能 _ 一日一技 · Mac.md
tags: [印象笔记]
---

# 通过安装插件增强 OS X 的预览功能 _ 一日一技 · Mac

# 通过安装插件增强 OS X 的预览功能 | 一日一技 · Mac --- ![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/E0

---

# 通过安装插件增强 OS X 的预览功能 | 一日一技 · Mac

---

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/E020B0C0-097C-41F7-BB96-1EC5EE6960DC.jpg)

「预览」（Preview）作为 OS X 系统内置的图片、PDF 查看和编辑软件，功能异常强大和易用，以致于有人戏称在 OS X 中最好用的软件是 —— 空格键！

「预览」原生支持的文件格式其实已经相当丰富，例如 PNG、PSD、PDF、RAW 等；在安装了第三方应用程序后，可预览的文件格式会进一步增加，例如 .scriv、.graffle 等。但即便如此，也还有很多文件格式是「预览」处理不了的，例如日渐流行的 .md 格式文件。

不过好在我们可以通过各种开源的预览插件，让「预览」支持更多格式的文件，令其「如虎添翼」。

安装、启用和卸载
--------

### 1. HomeBrew Cask

如果你习惯于使用 HomeBrew Cask 安装和卸载软件的话，只需要在「终端」中执行相应格式命令即可：

* 安装：brew cask install （+ 文件名）
* 卸载：brew cask uninstall （+ 文件名）

例如，如果你希望安装或卸载 QLMarkdown（Markdown 预览插件），则只需要将前述 （package name）替换为 qlmarkdown 即可，例如：

`brew cask install qlmarkdown`

### 2. 手动方式

**安装：**

1. 下载对应的预览插件，解压得到后缀名为 .qlgenerator 的插件文件；
2. 打开 Finder，依次点击「前往」-「前往文件夹」，在弹出窗口中输入 ~/Library/QuickLook，回车确认，打开文件夹。如果显示没有该文件夹的话，则改为输入 ~/Library，回车确认，打开「资源库」文件夹，并在其中手动新建名为 QuickLook 的文件夹。
3. 将 .qlgenerator 文件复制到前述 QuickLook 文件夹中。
4. 在「终端」中执行命令`qlmanage -r`，刷新以生效

**注：**如果将插件文件放入 ~/Library/QuickLook，则将仅为自己所在的用户安装；如果放入 /Library/QuickLook，则将为所有用户安装。

**卸载：**

如果你希望卸载相应的预览插件，只需将其从 QuickLook 文件夹中删除即可。

预览插件
----

在 [QuickLook Plugins](http://www.quicklookplugins.com/) 的网站上，有着相当数量处理不同文件格式的预览增强插件，例如 Camera Raw、 JSON 等。

在下文中，我将仅介绍几个针对普通用户的实用插件。如果你对预览插件有进一步的兴趣，不妨自行探索一番 :-D

点击文中提到的 6 款插件名的超链接，可跳转至 GitHub 下载。如遇问题，你也可以 [点此](http://7xqgno.com1.z0.glb.clouddn.com/%E3%80%8C%E9%A2%84%E8%A7%88%E3%80%8D%E6%8F%92%E4%BB%B6.zip) 下载打包文件。

### 1. [QLMarkdown](https://github.com/toland/qlmarkdown)

预览 Markdown 格式文件插件。

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/86058070-A6B2-4FC5-92A0-2A0F12B4C816.jpg)

需要特别指出的是：如果你使用的是 10.10 及以下系统版本的话，还可以通过在「终端」中执行如下命令，启用「在预览中选择文本」的功能：

`defaults write com.apple.finder QLEnableTextSelection -bool TRUE; killall Finder`

### 2. [QLStephen](https://github.com/whomwah/qlstephen)

预览无拓展名的纯文本文件插件。

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/571EF3FE-E87B-4B23-8E1E-0F52A10B764F.jpg)

### 3. [BetterZipQL](https://macitbetter.com/BetterZip-Quick-Look-Generator/)

预览压缩包内容插件，可以让我们非常方便地查看压缩包中所包含的内容。目前支持的格式包括：ZIP、RAR、7-Zip、TAR、TGZ、TBZ、TXZ、DMG 等等。

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/E8D07D13-7247-4D9C-AFA4-AF285BC31BEE.jpg)

### 4. [QLImageSize](https://github.com/Nyx0uf/qlImageSize)

安装后，将在预览窗口的标题栏中显示图片分辨率及文件大小（左图），并在 Finder 中显示图片的格式（右图）。

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/2F0CD1FF-6699-4C78-80DE-E4A0FE9C8C83.jpg)

除了常规的图片格式外，它还支持 bpg、Portable Pixmap、WebP 格式。

需要指出的是：该插件的安装文件为 .pkg 文件，双击安装即可；如果需要卸载，则需要在「终端」中运行如下命令，回车确认，并输入管理员密码：

`sudo rm -rf "/Library/Application Support/qlimagesize" "/Library/QuickLook/qlImageSize.qlgenerator" "/Library/Spotlight/mdImageSize.mdimporter"`

### 5. [Suspicious Package](http://www.mothersruin.com/software/SuspiciousPackage/)

预览标准的 Apple 安装包文件（.pkg 后缀文件）内容插件，该插件的安装和卸载和普通的应用安装相同，将 .app 文件拖入「应用程序」即可安装，从中删除即可卸载。

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/B502D813-C583-4B54-826C-4E2FDA1EB54D.jpg)

### 6. [QuickLookCSV](https://github.com/p2/quicklook-csv)

预览 CSV 文件插件。

![](.evernote-content/3F2DE1F3-0483-47AB-A8C4-1E42078DC055/E6FF8F0B-5B04-456D-8388-714A540E7B3C.jpg)

**参考链接：**

1. [SwiftGG 交流分享：Mac 上鲜为人知的使用技巧](http://www.jianshu.com/p/6c08f0ca23c4)
2. [GitHub: quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins)
3. [Apple：Mac 基础知识：通过「预览」app 查看和编辑图像和 PDF](https://support.apple.com/zh-cn/HT201740)
4. [Wikipedia: Preview (Mac OS)](https://en.wikipedia.org/wiki/Preview_(Mac_OS))

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33674)

[📎 在印象笔记中打开](evernote:///view/207087/s1/93532190-77d8-41e0-8059-4d8076524c8a/93532190-77d8-41e0-8059-4d8076524c8a/)