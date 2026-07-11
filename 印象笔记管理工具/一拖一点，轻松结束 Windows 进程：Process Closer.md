# 一拖一点，轻松结束 Windows 进程：Process Closer

---

相信你在使用 Windows 电脑时也遇到过这些问题：机器忽然发热变卡、CPU 突然被某个进程占满、蹦出一个明明已经关闭了的弹窗……

关闭软件后硬要留几个驻留后台进程占坑已经成为一些「毒瘤」软件的正常操作了，而这些在后台不知道干啥的进程就是导致前面几种情况的「幕后元凶」。通过 `Ctrl+Alt+Del` 组合键打开进程管理器杀死进程可以解决这些问题，但是：

* 每次想要彻底退出软件都需要打开进程管理器，很麻烦；
* 某些软件比较「狡猾」，将自己的后台进程起一个和软件无关，通常还和系统进程很像的名字，让你不知道从何下手。

而今天推荐的轻量级应用 [Process Closer](http://www.adminscope.com/downloads/process-closer/) 能轻松解决上面的问题，并且它使用起来只需拖拽、点击这样简单的动作。

Process Closer 是一款方便的进程结束软件。从某种意义上说，它算是任务管理器单一功能的高级版本，因为你允许用户通过使用「拖放」的方式结束进程和进程树。另外，如果有时候进程卡住了或者无响应，它还能提醒你即使关闭相关进程。 ​ 在 [官网](http://www.adminscope.com/downloads/process-closer/) 下载完毕后，你可以安装或者直接使用绿色版。Process Closer 不会在后台运行，需要你手动打开（当然可以设置开机启动），手动运行后它会默默地出现在系统托盘上。 ​

![](.evernote-content/EF9B756B-766C-4A1A-B50E-176DF942A3AA/D440D1A7-8D19-400C-8A02-4A8BBF5348EA.png)运行后出现在托盘上

我们以迅雷为例，当你下载完文件不想它没完没了后台弹窗的时候，点击右下角的蓝色图标。接着一个「Drag & Kill」的小窗口会出现，在上面按住鼠标右键，将出现的十字光标拖动到迅雷上，在弹出的确认窗口里面选择「All processes with same name（相同名字的所有进程）」然后点击「yes」即可轻松彻底地干掉进程。 ​

![](.evernote-content/EF9B756B-766C-4A1A-B50E-176DF942A3AA/F6EFD1B9-D5C6-4D07-B444-1B39262F2148.gif)

如果检测到无应答程序，则在右下角会显示一个单独的「未检测到响应过程」窗口。所有拖到这个窗口的程序都会立即被杀死。不过在我这里有时候即使选择忽略也会经常弹出来，比较烦人（虽然设置里可以关掉）。 ​

![](.evernote-content/EF9B756B-766C-4A1A-B50E-176DF942A3AA/4E57C968-F1EA-4E23-BA2B-9F612AE91001.png)

右键选择设置还有更多高级的调整，图片下面的列表就是从上到下的选项翻译，你可以根据自己的需要进行勾选：

![](.evernote-content/EF9B756B-766C-4A1A-B50E-176DF942A3AA/2DB9C3C0-1E02-4E64-BF2D-09C4F48FF041.png)

结束进程选项：

* ​结束进程（默认） 子选项：询问杀死所有相同名字的进程
* 结束进程和子进程
* 正常方式关闭进程
* 检测无响应的进程子选项：检测时间间隔，默认 30 秒
* 无需确认直接结束进程 ​

其他选项：

* 开机启动
* 快捷键 ​

虽然 Process Closer 的界面设计还比较古老，当它仍然可以在最新的 Windows 10 系统上使用，而且支持结束 UWP 应用和内核级别的进程。另外，它还是一个绿色免安装版的应用，即开即用，可以放在 U 盘里备用。

你可以从 [这里](http://www.adminscope.com/downloads/process-closer/) 免费下载 Process Closer，用于私人和商业用途，需要微软的 [.NET4 框架](https://support.microsoft.com/zh-cn/help/2858728/the-net-framework-4-5-1-offline-installer-and-net-framework-4-5-1-lang)。推荐经常需要使用管理多个程序和正在被各种弹窗后台占用困扰的派友使用。

---

> 更多好工具，就在 [Windows 上的好应用](https://sspai.com/topic/170) 🔨

> 下载少数派 iOS [客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，不再错过任何一款好用的 App 📱

---

[🌐 原始链接](http://sspai.com/post/44608)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8a5b7f37-e673-4c64-bc42-1717350f28e3/8a5b7f37-e673-4c64-bc42-1717350f28e3/)