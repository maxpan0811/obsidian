# 在 Windows 10 上安装软件，你现在可以用微软的包管理工具了：WinGet - 少数派

---

在 Windows 10 上安装软件，你现在可以用微软的包管理工具了：WinGet
=========================================

Matrix

付费订阅

特别策划

Pi Store

官方淘宝

软件商城

Tron 计划

Tron

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/CDF4C7D4-85E4-4DBB-9323-9C9BEDBC14CA)

在 Windows 10 上安装软件，你现在可以用微软的包管理工具了：WinGet

软件包管理工具，是电脑中自动安装、配置、卸载和升级软件包的工具。基于命令行的包管理工具已经在 \*NIX 世界中被广泛使用，不论是 macOS 的 Homebrew，还是 Linux 各大发行版自己的包管理（APT、Yum、Pacman……），它们都不仅有着完善的使用机制，还有丰富的软件包生态，是 \*NIX 系统安装、管理软件包的不二之选。

Windows 在「包管理工具」方面则一直乏善可陈。社区的努力让 Windows 有了 Chocolatey 以及[我曾经极力推荐的 Scoop](https://sspai.com/post/52496)，Windows 自己在历史上也曾经推出过具有「包管理工具」类似功能的 OneGet 和 NuGet。但是前二者一直依赖社区维护者的用爱发电，后二者则更强调开发环境的软件安装，没有提供日常用户所使用的软件，都不尽完美。

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/4E3359BC-273D-45D0-9562-7C46D0C61D39.png)

WinGet —— Windows 官方的包管理工具

在刚刚结束的 [Microsoft Build 2020](https://mybuild.microsoft.com/) 上，微软终于发布了面向广大 Windows 普通用户的 Windows 官方「包管理工具」—— Windows Package Manager，也就是 WinGet。有了 WinGet，Windows 用户终于可以**通过官方途径**来在命令行环境下管理软件了。

下载安装
----

WinGet 支持 Windows 10 1709 及以上版本，现在使用 Windows 10 的同学们就可以直接下载安装。官方提供了下面的几种安装方法：

### 通过 Microsoft Store 下载

目前 WinGet 还在 Preview 阶段，因此如果你想用官方的渠道安装 WinGet，那么你需要：

* 或是加入 [Windows 10 Insider](https://insider.windows.com/)，并下载安装 Windows Insider 版本的系统
* 或是通过[官方注册通道](http://aka.ms/winget-InsiderProgram)来将自己加入 WinGet Preview flight ring

之后，你的系统上面就应该出现（命令行环境下的）WinGet 本体，并可以通过 Microsoft Store 同步更新。

### 通过 GitHub Release 手动安装

另外，你也可以直接去 [WinGet 的官方 GitHub 仓库](https://github.com/microsoft/winget-cli)，[在 Release 页面](https://github.com/microsoft/winget-cli/releases)手动下载 WinGet 的安装程序进行手动安装。

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/ABD5EECD-D7A9-4A28-B057-467E174F3315.png)

在 WinGet 的 GitHub Release 页面手动下载安装

令人熟悉的 WinGet 操作和命令
------------------

安装好 WinGet 之后，我们就可以在 PowerShell 或者 CMD 中用 `winget` 命令调用它了。

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/8E5A520F-D21D-4EA7-A56E-70EFDE63E6AE.png)

WinGet：微软官方开发的 Windows 包管理工具

直接运行命令 `winget`，WinGet 会给我们展示自己的一些基础操作，包括安装软件、显示软件信息、显示应用源、搜索软件、验证安装程序等等。我自己在日常使用 Windows 时，是经常使用 Scoop 进行软件安装管理的，这里我将 WinGet 和 Scoop 直接面对面，进行命令的对比，看看常用的几个功能（安装软件、显示信息、搜索软件）之中 WinGet 和 Scoop 之间的区别。

### 安装软件

安装软件大家都一样，同样都是 `winget install {软件名称}` 和 `scoop install {软件名称}`。比如这里，我分别使用 WinGet 和 Scoop 下载安装 Postman：

```
# 使用 WinGet 安装一遍
winget install postman

# 卸载，再用 Scoop 安装一遍
scoop install postman
```

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/48DBE178-79D0-4708-AFD8-18AB66C4E1A1.png)

使用 WinGet 和 Scoop 下载安装 Postman

安装过程大概都是类似的，WinGet 安装的是 `exe` 文件，而 Scoop 安装了 NuGet 的 `.nupkg` 文件。二者都是 Windows 上常见的软件安装文件。界面上，WinGet 的下载进度条比较酷炫，而 Scoop 使用的依旧是「字符进度条」，简单淳朴。

另外，WinGet 还有一个比较骚的进度条，在刚刚安装命令之后加上 `--rainbow` 的参数，即可解锁彩虹进度条！（ 净搞这些有的没的 (/▽＼)）

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/88D7A7C3-818E-4AB3-91CD-68A8396BB6AD.gif)

使用 WinGet 下载安装程序的彩虹进度条与下载全过程

### 显示软件详细信息

同样的，WinGet 和 Scoop 都有支持显示某一个软件的详细信息。这里，WinGet 使用的命令是：

```
winget show postman
```

而 Scoop 与之对应的命令为：

```
scoop info postman
```

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/39DE42D9-4C00-467F-B6E8-F67EAC934C21.png)

显示待安装软件的详细信息

二者都显示了当前准备安装软件的版本信息、官方网站、原地址、下载链接等等信息，比较类似。

### 搜索特定软件

WinGet 和 Scoop 也一样支持搜索某一软件。使用的是相同的 `search {软件名称}` 的命令。比如，搜索 Steam：

```
# WinGet 搜索 Steam
winget search steam

# Scoop 搜索 Steam
scoop search steam
```

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/70834A73-AB72-4E09-90EF-EA0D8DC8F3A9.png)

WinGet 和 Scoop 搜索特定软件

当然，WinGet 和 Scoop 都是关键词匹配搜索，由于 Scoop 目前的软件库比较丰富，因此搜索到的东西也比 WinGet 多一些。另外，我发现 WinGet 搜索速度要比 Scoop 快一些，可能是由于 Scoop 需要联网遍历整个软件 bucket，导致搜索速度没有那么快。

除了上面介绍的三个命令以外，WinGet 还有方便 WinGet 软件源开发管理人员使用的 `validate` 命令和 `hash` 命令等等。

WinGet 安装和管理软件的原理
-----------------

尚处于 Preview 阶段的 WinGet 目前是利用 Manifest 清单文件来管理与安装不同的软件，这一设计理念和 Scoop 是高度相似的。为了让各位彻底理解这一过程，我们先介绍 WinGet 和 Scoop 这类 Windows 软件包管理工具在安装软件过程中具体是怎样工作的。

WinGet 是典型的「Windows 思路」包管理工具，由于 Windows 本身的设计，软件的安装几乎都伴随着「软件安装器」的使用。因此，WinGet 一类「包管理工具」，包括 Scoop 在内，实际上都是代替我们：

* 寻找软件官方发布地址
* 下载我们设定版本的软件
* 运行软件安装器来安装下载得到的软件
* 并进行环境上的准备、安装后的善后工作等

而 WinGet 这类包管理是怎样知道去哪里寻找软件、下载软件和进行安装的呢？答案就是通过读取软件对应的 Manifest 清单文件。

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/7351E1AE-FFED-4B9A-9881-811AB1336D90.png)

WinGet 安装软件的工作原理

就如图中描述的过程一样，WinGet 和 Scoop 在安装软件过程，都是先去各自维护的软件 Manifest 库，寻找相应的软件安装 Manifest 清单文件，这一文件就像说明书一样指导软件包管理工具安装软件的具体过程。WinGet 和 Scoop 等 Windows 包管理工具就会依据软件相应的 Manifest 文件：准备、下载、安装、善后。

可以发现，在这一过程中，最为重要的一步就是找到「软件 Manifest 库」，并从中请求得到待安装软件相应的「Manifest 文件」。对于 WinGet 来说，微软官方目前维护了一个在 GitHub 上面开源的 [microsoft/winget-pkgs](https://github.com/microsoft/winget-pkgs) 仓库，用于让 WinGet 来寻找软件相应的 Manifest 文件。

![](.evernote-content/1E2C8D08-01A8-40C3-B86B-7F25996BF33D/662DC29A-270F-4EDB-BBE3-71586456E3D2.png)

GitHub 上面 Postman 的软件 Manifest 文件

与之相应的，Scoop 是通过 bucket 的机制实现的这一功能特点。在之前的文章[「给 Scoop 加上这些软件仓库，让它变成强大的 Windows 软件管理器」](https://sspai.com/post/52710)中，我就介绍过 Scoop 不同的软件仓库、如何添加自定义软件仓库以及如何从第三方软件仓库中下载安装软件等等。在 WinGet 中，我们同样也有相应的方法。

WinGet 提供了一个 `source` 的命令，利用 `winget source <command>`，我们就可以方便地管理不同的 WinGet 软件 Manifest 仓库（WinGet 官方称之为「软件源」），比如：

* `winget source add <软件源>`：添加新的软件源
* `winget source list`：列出当前已添加的软件源
* `winget source update`：更新当前全部添加的软件源
* `winget source remove`：移除当前使用的软件源
* ……

当然，由于 WinGet 也才问世几天，所以还没有出现除了官方仓库外可用的软件仓库。

小结
--

WinGet 在我看来，和 Windows Terminal 一样，都是 Windows 团队让 Windows 系统更加「开发者友好」的又一努力。不过，WinGet 现在着实仅是一个半成品，**其半成品最重要的体现在于：仅支持安装软件，不支持卸载软件。**

同时，WinGet 也并没有逃脱 Windows 类包管理工具的通病 —— 「软件安装器」并非真正意义上的「软件包管理工具」。目前来看，WinGet 也仅仅是和社区优秀作品 Chocolatey、Scoop 等 Windows 包管理工具原理完全一致的一个工具，并没有因为微软自己的加入而有新的花样。

希望未来随着不断迭代，WinGet 能够变得不是为了造轮子而造轮子，成为真正意义上的「Windows 包管理工具」，让开发者朋友们像看 Windows Terminal 一样高呼「真香」。感谢阅读。

**关联阅读：**

> 下载少数派 [客户端](https://sspai.com/page/client) 、关注 [少数派公众号](https://sspai.com/s/J71e) ，第一时间掌握 Chrome 更新动态与技巧 ✨

---

[🌐 原始链接](https://sspai.com/post/60592)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f3fd5a8e-cdbe-4562-879a-c6686a181025/f3fd5a8e-cdbe-4562-879a-c6686a181025/)