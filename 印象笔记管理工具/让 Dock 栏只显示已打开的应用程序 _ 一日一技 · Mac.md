# 让 Dock 栏只显示已打开的应用程序 | 一日一技 · Mac

---

![](.evernote-content/8B58F574-E217-46FA-AA97-46A9E4F44E08/70606DF7-7759-48A4-A17C-ADDEBEB549F7.jpg)

默认情况下，Dock 栏不仅会显示用户设置为「在 Dock 中保留」的应用程序（不论打开与否）、系统项目（Finder 和废纸篓）以及堆栈，还会显示那些用户并未设置保留，却已经打开的应用程序的图标。

这种「一个不漏」的显示方式，虽然十分便于用户操作，但也容易变得讨人厌：

* 对那些已经有不少在 Dock 中保留的项目的用户来说，随着新增的应用图标和最小化窗口的挤占，Dock 栏会越变越小。这时，Dock 中不活跃的应用程序及堆栈就不仅让人分心，还影响操作效率。

![](.evernote-content/8B58F574-E217-46FA-AA97-46A9E4F44E08/B0E287E5-866C-4B19-807D-A440BBE9D8ED.jpg)

* 对那些希望截取或录制屏幕内容的用户来说，为了保持内容的相关性，常常会在截取或录制之前将不需要的项目从 Dock 栏中移除，结束后再加以恢复，十分费力。

其实，在 OS X 中，我们只需要运行一小段命令，就可以让 Dock 只显示已打开应用，从而减少不必要的干扰。

方法一
---

在「终端」（你可以通过 Spotlight 或定位至「应用程序」-「实用工具」-「终端」找到它）中输入如下命令，回车确认即可：

```
defaults write com.apple.dock static-only -boolean true; killall Dock
```

待 Dock 重启后，你就会发现，现在在 Dock 栏中只显示已打开的应用程序了！

![](.evernote-content/8B58F574-E217-46FA-AA97-46A9E4F44E08/18B3B758-E331-4DDE-BB86-F056FEB7BC9C.jpg)

如果你想恢复成默认设置，只需再次输入命令，并回车确认即可：

```
defaults delete com.apple.dock static-only; killall Dock
```

方法二
---

比起相对麻烦且容易出错的终端命令来说，利用 [OnyX](http://www.titanium.free.fr/) 这款免费的系统维护软件去设置，不仅更友好，恢复成默认的设置也更方便。

前往「参数」-「Dock」中，勾选「只显示已打开的应用程序」，并在弹出的警告窗口中点击「继续」重启 Dock 即可。

![](.evernote-content/8B58F574-E217-46FA-AA97-46A9E4F44E08/AEB923AC-2F8F-4E6E-844E-61B439606CEE.jpg)

参考链接：

* [LifeHacker: Hide Everything But Active Apps In Mac OS X](http://www.lifehacker.com.au/2015/07/hide-everything-but-active-apps-in-mac-os-x/)

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33479)

[📎 在印象笔记中打开](evernote:///view/207087/s1/480c5da0-2822-4516-ba01-01e72cacf998/480c5da0-2822-4516-ba01-01e72cacf998/)