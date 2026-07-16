---
title: "Mac App Store「调试」菜单和 Safari 「开发」菜单的用处 _ 一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Mac App Store「调试」菜单和 Safari 「开发」菜单的用处 _ 一日一技 · Mac.md
tags: [印象笔记]
---

# Mac App Store「调试」菜单和 Safari 「开发」菜单的用处 _ 一日一技 · Mac

# Mac App Store「调试」菜单和 Safari 「开发」菜单的用处 | 一日一技 · Mac --- ![](.evernote-content/5E2B67DA-00C1-41C5-86

---

# Mac App Store「调试」菜单和 Safari 「开发」菜单的用处 | 一日一技 · Mac

---

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/65A4485F-2935-4797-B2DC-AD0730656266.jpg)

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

在 OS X 中，苹果隐藏了部分针对开发者的菜单，例如 Mac App Store （下文简称 MAS ）的「调试」（Debug）菜单和 Safari 的「开发」菜单。不过，其中也有着不少普通用户不太关注却又用得着的东西，例如播放视频发热或无法安装、更新应用程序等。

当你开启前述隐藏菜单后，并兴致勃勃地想要「一探究竟」时，或许会感到相当沮丧，因为你可能根本就看不懂！不过这没关系，因为你只需关注其中少数几个选项及其可实现的功能即可。

Mac App Store 的调试菜单
-------------------

### 开启方法

退出 MAS（如果已经打开了的话），在「终端」（你可以通过 Spotlight 或定位至「应用程序」-「实用工具」-「终端」找到它）中输入如下命令，回车确认，并重启 MAS，即可显示隐藏的「Debug」菜单栏：

`defaults write com.apple.appstore ShowDebugMenu -bool true`

若希望再次隐藏它，则取消勾选「Enable Debug Menu」，并重启 MAS 即可；或者通过在终端中运行如下命令实现：

`defaults write com.apple.appstore ShowDebugMenu -bool false`

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/9A4BB9D1-EF10-4760-8CF3-20C2D6DB1381.jpg)

### 需要关注的功能

* **Show Downloads Folder：**显示下载文件夹。如果在安装或更新应用程序的过程中出错，不妨进入 MAS 的下载文件夹中将其删除，随后再重新安装或更新。
* **Clear Cookies & Reset Application：**清除 Cookies 和重置应用。这或许是「调试」菜单中最有用的两个选项了，先后点击「Clear Cookies」和「Reset Applications」，将清除下载文件夹中的所有文件，并将 Mac App Store 重置为默认状态。这样或许就能够解决一些在购买、安装或更新应用程序之中遇到的一些古怪问题。

Safari 的开发菜单
------------

### 开启方法

打开 Safari，前往「偏好设置」-「高级」中，勾选底部的「在菜单栏中显示“开发”菜单」，即可显示「开发」菜单，取消勾选则为关闭。

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/F3F8BA3C-AA4C-40B2-B28F-8C37A896E71A.jpg)

如果你不习惯上述方式的话，则可以通过 [OnyX](http://www.titanium.free.fr/) 这款免费的系统维护软件去开启/关闭：

* 前往「参数」-「程序」中，勾选勾选「显示 App Store 调试菜单」，即可开启 MAS 的「Debug」菜单；
* 前往「参数」-「Safari」中，勾选「打开开发菜单」，即可开启 Safari 的「开发」菜单。

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/18B727C7-22E7-482F-BB4A-67F722A8F8EF.jpg)

### 需要关注的功能

**打开网页的浏览器**：若使用 Safari 打开某些网页出现问题的话，该选项能够让你使用其他已经安装的浏览器打开当前页面，从而省去复制粘贴网址的步骤。

**用户代理：**当你浏览一个网页时，浏览器会向所访问网站的服务器发送用户代理（User Agent）字符串 —— 该字符串通常会标明你使用的浏览器和版本号，以及操作系统和版本等信息，并利用这些信息向你提供合适的内容。

例如，我在「用户代理」-「其他」中查看到的字符串为：

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17
```

如果将「用户代理」更改为`Safari-iOS 9.3-iPad`（或其他 iOS 代理），则可以将伪装成 Safari Mobile。

这样一来，在浏览乐视、优酷等视频网站时，视频就将以 HTML 5 这种更为省电的方式播放，从而减缓 Mac 风扇狂转、温度骤升的恼人局面。

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/D1CB549D-570B-40C8-A83A-349A9BDF9027.jpg)

**显示页面资源：**可以方便地查看当前页面中的脚本、图像、样式表、字体等等。通过查看「图像」，我们可以方便地找到网站的 Logo 图片等 :-D

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/787B94CF-BCD3-49E2-8787-C33A3F8A1FD3.jpg)

**清空缓存：**出于加快加载速度的考量，Safari 会缓存最近访问页面中的元素，例如图片、文本信息等。但时间一长，这些缓存可能会过旧或不再被需要。通过清空缓存能够帮助我们清理掉一些无用的缓存文件以处理错误的页面显示、释放一部分存储空间或者是清除部分隐私数据，等等。

Bonus：开启 Safari 隐藏的「Debug」菜单
----------------------------

退出 Safari，在「终端」中输入如下命令，回车确认，并重启 Safari，即可显示隐藏的「Debug」菜单：

`defaults write com.apple.Safari IncludeInternalDebugMenu 1`

若希望再次隐藏它，在终端中运行如下命令即可：

`defaults write com.apple.Safari IncludeInternalDebugMenu 0`

![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/83BB49F1-4976-4C98-A015-516D4A5BBC35.jpg)

注意
--

1. 如果你并不十分清楚「调试」菜单中选项的具体含义的话，请勿随意点击或修改其中的选项。
2. 由于 OnyX 中功能面板复杂而众多，因此在使用前，最好使用 Time Machine 或第三方的工具备份您的系统和用户数据。并且，不建议你在并不熟悉其具体含义前，随意开启或关闭某些功能项。

参考链接：

1. [CNET: Make use of the Mac App Store debug menu](http://www.cnet.com/news/make-use-of-the-mac-app-store-debug-menu/)
2. [王飞 -《OS X Mountain Lion 高手进阶》](http://www.ibuick.com/products/ML_masters/index.html)
3. [Macs About: How to Enable Safari's Develop Menu](http://macs.about.com/od/usingyourmac/qt/safaridevelop.htm)

[![](.evernote-content/5E2B67DA-00C1-41C5-86A3-BEDD973F4D93/9283128D-A283-407F-B5E3-D9C7C007F3BB.jpg)](http://sspai.com/su/22p1)如果你希望通过赞助方式支持更多优质内容，请[联系我们](mailto:will@zookr.net)。

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33420)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5775b247-13e0-4bba-bacb-ec94d2704a22/5775b247-13e0-4bba-bacb-ec94d2704a22/)