# Homebrew 技巧：使用 Mackup 快速备份 Mac 软件的配置文件

---

![](.evernote-content/029136F8-67FC-4AC1-A39E-2E6886B0A2B6/0A0179D6-31D9-41FB-82A2-EEFAE21E9C57.jpg)

Mac 上备份数据资料，你会怎么做？想必很多人的选择都是使用系统内建的 Time Machine 来进行数据的备份与恢复。不过要知道，Time Machine 备份恢复的时间往往比较长，在这过程中还不一定会出什么意外。

如果你只需要备份 Mac 软件的配置文件，除了 Time Machine，你还可以试试 Github 上的开源项目 [Mackup](https://github.com/lra/mackup) ，它拥有足够轻量与快速的备份恢复操作，更重要的是，它不需要另外安装，通过 [Homebrew](http://sspai.com/32857) 与几行简单的命令就可以完成操作。

关于 Homebrew 的教程，请阅读：[《借助 Homebrew Cask，教你快速下载安装 Mac App 新姿势》](http://sspai.com/32857)

关于 Mackup
---------

[Mackup](https://github.com/lra/mackup) 是 Github 上的一个开源项目，旨在帮助你快速方便地备份恢复软件的配置文件，Mackup 已经支持了包括 iTunes Applescripts 在内的一系列常用的软件程序，可以在它的项目首页进行更多了解。

除了开头介绍它是由命令行完成备份恢复操作之外，由 Mackup 备份的配置文件全部会存储在你的个人云端文件夹中，不会占用你的本地空间。目前 Mackup 支持的云端存储服务商有以下几种：

* Dropbox
* Google Drive
* Copy
* iCloud
* Box

如果你不想用这些云服务的话，也可以用 Git 或其它在线工具存储。

安装 Mackup
---------

### 1. 安装 Homebrew

上文提到了，Mackup 的安装可以通过 Homebrew 来完成，不了解 Homebrew 的朋友可以再看看[之前的文章](http://sspai.com/32857)。

简言之，你需要在终端中输入下列代码安装 Homebrew，如果你已经装过可忽略这一步：

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### 2. 安装 Mackup

输入下面的命令安装 Mackup：

`brew install mackup`

### 3. 选择你的同步文件夹

Mackup 默认会将配置文件备份到你的 Dropbox 本地存储文件夹，前提是你的电脑上已经安装了 Dropbox。如果你不想存储到 Dropbox 中，那就需要稍微配置一下。

这里以 iCloud 为例，介绍 Mackup 的备份路径配置方法。

首先，在终端输入命令：

`vi ~/.mackup.cfg`

执行完上述命令之后，你会看到下面的界面：

![](.evernote-content/029136F8-67FC-4AC1-A39E-2E6886B0A2B6/9C67FCDB-2E7A-467F-8288-692EA846376F.jpg)

不要慌张，继续在窗口中输入以下文字：

```
[storage]  
engine = dropbox
```

这样，你就已经设置好你的 Mackup 同步文件夹为 iCloud 了，剩下要做的就是保存这份配置文件：

按下「ESC」按键并输入 `:wq` 然后回车，至此，Mackup 的同步文件夹就已设置完成。

![](.evernote-content/029136F8-67FC-4AC1-A39E-2E6886B0A2B6/2C43C9C0-DB80-4979-A3D5-A1F71D460C03.jpg)

Mackup 的操作
----------

关于 Mackup 的操作其实非常简单，这里列出 Mackup 的常用操作命令：

* `mackup backup` 使用 Mackup 进行备份操作
* `mackup restore` 使用 Mackup 进行数据的恢复
* `mackup list` 查看 Mackup 支持的软件列表
* `mackup -h` Mackup 的帮助命令
* `mackup uninstall` 将配置文件拷贝回原来的系统目录

如果你想卸载 Mackup，输入以下命令即可：

`brew uninstall mackup`

文章来源 [少数派](http://sspai.com) ，原作者 [waychane](http://sspai.com/author/703114) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/029136F8-67FC-4AC1-A39E-2E6886B0A2B6/F94EC49B-4254-4ED0-894D-2F025E1DDE6B.jpg)](http://sspai.com/33084)

---

[🌐 原始链接](http://sspai.com/32933)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b0ae8e91-e465-43e9-9516-10f89ee5dc41/b0ae8e91-e465-43e9-9516-10f89ee5dc41/)