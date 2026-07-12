# 用这些方法，让 Windows 用起来更顺心 - 少数派

---

用这些方法，让 Windows 用起来更顺心
======================

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

Windows 10 中，有一些让我用起来不那么顺心的设计：小娜和「开始」中的 Bing 和 Edge、默认的快捷键、预装的应用、还有那混乱的设置面板…… 这些设计体验其实见仁见智，但如果你并不喜欢这些功能，想要摆脱它们，Windows 并没有给出调整的方法，需要借助下面这些第三方工具。

更换「开始」里的 Bing 搜索和 Edge 浏览器
--------------------------

Windows 的「开始」使用的是 Bing 搜索引擎，预览界面的链接，会强制使用 Edge 浏览器打开，偏爱其他搜索引擎和浏览器的用户往往只能选择其他启动器。

**Search Deflector** 可以实现对「开始」的搜索引擎以及浏览器的更改。从 [Microsoft Store](https://www.microsoft.com/store/productId/9P8ZJJ80RZ2K) （售价￥14）或者 [GitHub](https://github.com/spikespaz/search-deflector/releases) （免费）下载安装后，打开应用，在下拉菜单中选择浏览器为 System Default，搜索引擎根据个人习惯，我这里选择了 GitHub。

之后，打开你的设置面板，在 `应用 > 默认应用 > 按协议指定默认应用` 中，找到 `MICROSOFT-EDGE`，将后面的选项改成 `delfector.exe`，设置就完成了1。

现在，小娜以及「开始」的搜索引擎和浏览器都会被改成你所设置的选项。不过，搜索的预览界面还是 Bing，这是没有办法修改的。

相似的软件还有 **[SearchWithMyBrowser](https://github.com/sylveon/SearchWithMyBrowser)** 和 **[EdgeDeflector](https://github.com/da2x/EdgeDeflector/releases)**，这三个软件都是开源应用， Search Deflector 比较新一点，其他两个有很长一段时间没有更新了 。

更换不常用的快捷键
---------

Windows 注册了绝大多数 Win + 字母 的快捷键，这些快捷键不能再被其他应用注册使用。其中有一些，比如 Win + H 的听写功能，Win + Q、Win + S 的搜索功能可能不那么常用。想要自定义也是有办法的。

你可以使用一些软件改变按键映射，微软最近推出的 **[PowerToys](https://github.com/microsoft/PowerToys)** 就是一个不错的选择。

不过，我更推荐使用 **AutoHotKey** ，它可以在不修改系统文件的情况下覆盖掉原有的快捷键，占用内存小并且更加强大：举例来说，下面这些代码，将 Win + Q & W 改成了虚拟桌面切换功能，实现的原理是将这些按键映射成系统自带的虚拟桌面切换快捷键，代码浅显易懂：

```
 ;按下 Win + W，发送 Win + Shift + 右方向键  
   #w::  
   send #^{Right}  
   return  
 ;按下 Win + Q，发送 Win + Shift + 左方向键  
   #Q::  
   send #^{left}  
   return
```

你也可以设置按下快捷键，执行命令或者程序。例如下面这行代码，实现了当按下 Win + R 时，在 C 盘根目录启动 PowerShell：

```
 ;Powershell  
   #r::  
   Run, powershell.exe, C:\  
   return
```

AutoHotKey 的下载地址 [在这里](https://www.autohotkey.com/)，软件上手难度不大。安装后，新建 ahk 文件写入代码，保存后双击文件就能生效。

卸载预装应用
------

Windows 上有大量的预装应用，诸如电影、照片、画图3D，用起来其实还蛮顺手的，但和第三方软件比起来还是差了点意思。不过既然已经有了第三方软件，这些预装应用看起来就显得有一些多余，另外如 3D Builder 等我几乎不会用到的软件，能够彻底摆脱当然更好。

卸载它们不难。以照片应用为例，首先以管理员身份打开 PowerShell，输入以下命令，按回车，等待执行完毕就行了。修改引号中间的 Appx 包名，就能卸载其他应用2。

```
 $ Get-AppxPackage "Microsoft.Windows.Photos" | Remove-AppxPackage
```

诸如 **[iobit uninstaller](https://www.iobit.com/en/advanceduninstaller.php)** 之类的卸载工具，诸如 **[Dism++](https://www.chuyu.me/)** 之类的优化工具也都能卸载这些预装应用，并且提供了方便操作的 UI。

备份设置，让重装更简单
-----------

我每两年左右都会重装一次系统，重装后最麻烦的就是将 Windows 调教得符合个人使用习惯。Windows 拥有非常多的设置界面，在不同的面板间切换也是一件非常头疼的事情。

仔细想来，我们所做的不过是卸载预装应用、关闭各种「建议」，关掉数据上传……而这些都能够通过命令来实现，倘若再把这些命令整合起来变成可执行的脚本，以后不就可以一键完成 Windows 的初始化了吗？—— 这就是引出了**「[Win10 Initial Setup Script](https://github.com/Disassembler0/Win10-Initial-Setup-Script)」**。

Win10 Initial Setup Script 是 Windows 一键设置脚本，适合于**个人重装**后或大规模部署系统后，对 Windows 10/ Server 进行快捷设置。使用者应当完整阅读项目的说明，看得懂 PowerShell 脚本语言，了解每一个部分命令的作用。**贸然使用，会出现严重事故**。脚本的主要功能有：

1. 卸载系统所有非必要的预装 UWP 软件；
2. 禁用数据上传、禁用反馈、关闭各类「建议」，禁用任务历史3；
3. 调整系统界面和动画，使之快速、简洁；
4. 调整文件浏览器界面，禁用 F1 呼出帮助；

从[这里](https://github.com/Disassembler0/Win10-Initial-Setup-Script/releases)下载压缩包，解压后，以管理员身份运行 `Default.cmd` 即可。`Win10.psm1` 文件中，作者为每一部分命令添加了注释，并且给出了还原的方法。你也可以自己添加删除功能，使脚本符合自己的习惯。

请输入图片标题

（题图来源：[Windows 官网](https://www.microsoft.com/zh-cn/windows)）

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，了解更多 Windows 玩法

* 1Wiki 中提到软件无法生效方法，也许是多余的。我在使用这个软件的时候，必须要进行这一步设置
* 2此方法我是从 Win10 Initial Setup Script 得知的，搜索「卸载 Windows 预装应用」可以得到预装软件全部包名
* 3会导致无法进行 Insider 更新，设置面板将会出现「此设置由您的组织管理」字样

---

[🌐 原始链接](https://sspai.com/post/60894)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e8429e50-8126-48f2-8ea5-fc4dbaa05fe4/e8429e50-8126-48f2-8ea5-fc4dbaa05fe4/)