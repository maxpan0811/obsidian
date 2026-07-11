# 在 Mac 上使用 Xbox 或 PS 手柄玩游戏 | 一日一技 · Mac

---

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/147BF3D7-235F-4207-857A-00307DDC7C55.jpg)

Mac 平台因为自身种种原因，对于游戏的支持不是那么太好，不管是性能方面，还是数量方面，是远远不及 Windows 的。但是这并不代表 Mac 不能愉快的进行游戏，对于一些图形处理能力要求较低的游戏，Mac 是完全可以胜任的。

作为一个主机党，在 Mac 上游玩一些游戏的过程中，键鼠的操作实在是不能让我满意。这时我就想到了手柄，能不能在 Mac 的环境下，使用手柄操作来玩游戏呢？如果你也有类似的需求，这篇文章会具体教你如何将 Xbox One、Xbox 360、PS3 或 PS4 手柄连接到 Mac。

*注：本文基于 Mac OS X El Capitan 10.11.5*

Xbox One 手柄
-----------

Xbox One 手柄无疑是 Windows 平台游戏手柄的最佳选择，但微软官方并没有针对 Mac 平台开发对应的驱动程序，欣慰的是，已经有热心的网友自制了针对 Xbox One 手柄的 Mac 驱动，让你在 Mac 上也能完全使用 Xbox One 手柄。

### 1. 下载驱动

前往[这个页面](https://github.com/FranticRain/Xone-OSX/releases)，下载名为「Xone-Driver-1.0.4.dmg」的驱动文件并安装，安装完成后会提示重启电脑。（尽管作者 Drew Mills 表示这个驱动他已经不再更新，我还是建议用 Xbox One 手柄的用户下载这个，原因稍后说明）

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/6212B176-DF58-4FEB-9EF2-FC4BB8A7FD4A.jpg)

### 2. 设置

重启完毕后，找一根普通的 Micro USB 的连接线， 通过 USB 将你的 Xbox One 手柄与 Mac 连接，如果刚刚的驱动程序安装成功的话，你应该能顺利的在系统偏好设置中看到最下面多出来了一个名为「Xone Controller」的项目。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/E5081CB6-920B-4357-B369-E3D075E48340.jpg)进入 Xone Controller，随意按手柄上的键位，观察是否与屏幕上的对应，效果如下图。没有识别出来的可以尝试重新插拔或者点击 Refresh 按钮进行刷新。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/D4A7481D-E5EC-4336-BA66-984BC4DB5C83.gif)

Xbox 360 手柄
-----------

Xbox 360 手柄的配置方法其实与 Xbox One 的类似，都是通过网友自制的第三方驱动实现支持。

### 1. 下载驱动

前往[这个页面](https://github.com/360Controller/360Controller/releases)，下载名为「360ControllerInstall\_0.16.dmg」的驱动文件并安装，安装完成后会提示重启电脑。

特别说明：此驱动其实不仅支持 Xbox 360 的手柄，同样也支持 Xbox One 手柄，但是在我测试 Xbox One 手柄的过程中发生了严重的按键延迟、连按等不正常现象，Xbox 360 手柄则一切正常。由于属于民间自制驱动，系统版本、手柄型号导致的差异很正常，这也是我不推荐 Xbox One 下载此驱动的原因。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/38F73053-375B-472B-880F-8D05EB912CB1.jpg)

### 2. 设置

注：该驱动的页面上写明了支持 Xbox 360 的无线手柄版本，但我手上并没有无线手柄版本，所以测试基于 Xbox 360 的有线版，也欢迎大家在评论区反馈适配情况。

整个的设置过程其实与 Xbox One 手柄的没什么不同，在安装并重启完成后，在系统偏好设置中会多出来名为「Xbox 360 Controllers」 的项目。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/B3B329A7-2EF2-4563-B8ED-3FC1E869DA5C.jpg)

进入 Xbox 360 Controllers，尝试测试手柄按键是否对应。如使用不正常，请尝试重新插拔。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/E69EC496-D6A2-4187-8E02-4FB7ED31B220.gif)

Playstation 4 手柄
----------------

PS4 手柄与 Mac 的连接出乎意料的简单。可能与手柄的蓝牙规格有关，PS4 手柄惊喜的原生支持Mac 系统，不通过额外驱动，通过蓝牙和有线都可以正常的进行连接。

### 通过蓝牙：

1. 进入系统偏好设置 - 蓝牙，将蓝牙打开。

2. 同时按住 PS4 手柄的 Playstation 键和 Share 键，直到手柄上方的指示灯开始快速闪动再松开，该操作会让手柄进入匹配模式。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/87E751CA-C8BA-4476-9B14-522D5C1FDC35.jpg)

3. 打开蓝牙界面，Mac 应该很快会检索到设备信息。在设备列表中应该会出现一个名为「Wireless Controller」的项目，点击「配对」。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/955FF633-C003-42E7-A467-C306063CDD11.jpg)

 4.等待 PS4 手柄成功连接之后，设备列表应该显示「已连接」，手柄上方的指示灯不再闪烁，变成常亮，代表连接成功。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/8E1E8963-4A46-48C1-B356-CEE0138B7508.jpg)

### 通过 USB 线缆：

通过 USB 连接 PS4 手柄简单程度令人发指，因为你需要做的只有两步：

1. 用一根 Micro USB 数据线把 PS4和 Mac 相连。
2. 进入相应游戏，在对应游戏设置选项更改操作方法为手柄即可。

Playstation 3 手柄
----------------

与 PS4一样，PS3 的手柄通过简单的设置也可以达到直连 Mac 的目的。

1. 打开系统偏好设置-蓝牙，打开蓝牙。

2. 通过 Mini USB 线缆连接 Mac 与手柄，这时，你的蓝牙设备列表应该会有名为「PLAYSTATION(R)3 Controller」的设备，显示「未连接」，别紧张，这是正常现象。同时，位于你手柄上方的四个指示灯会缓慢的闪烁，说明它在充电状态。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/F0A76C58-01EC-45B2-9BE0-82FA5D1E9260.jpg) 3. 拔下 USB，切断手柄与 Mac 之间的连接，按下 Playstation 键，手柄上方的四个指示灯会开始快速闪烁，说明手柄正在与 Mac 配对。

4. 你的 Mac 会要求你输入密码以完成配对，输入「0000」，点击配对。查看蓝牙状态，显示「已连接」则说明连接成功。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/EB24F09A-7DDE-4A07-8725-34D1AFA5D743.jpg)

游戏适配情况
------

经过我的测试，Steam 上标有「完全支持控制器」的游戏均可以正常识别 Xbox 手柄。除了没有手柄的震动之外，与 Windows 平台的使用体验一模一样。PS 3/4 手柄需要注意的是，进入游戏之后可能会出现无法识别的情况，这并不是手柄或电脑的问题，而是由于 Steam 上的 Windows 用户大多会购入 Xbox 手柄进行游戏，游戏开发商没有对 PS 系手柄进行适配。  
  
因为 Mac App Store 的游戏没有标注手柄支持情况，一切都取决于游戏开发者，简单来说，在 Mac 上，游戏是否支持手柄与你的购买渠道无关，与游戏本身有关。

![](.evernote-content/A562A403-645E-4081-BC79-E4DDDFBAA517/9B95919C-2F4D-4208-97D0-31E58C7718A1.jpg)

参考链接：[How to Connect a PlayStation 3 Controller to a Mac](http://theultralinx.com/2014/02/connect-playstation-3-controller-mac-os-mavericks/)

[继续阅读往期「一日一技」文章 >](http://sspai.com/search/?q=%E4%B8%80%E6%97%A5%E4%B8%80%E6%8A%80)

文章来源 [少数派](http://sspai.com) ，原作者 [一只索狗](http://sspai.com/author/682662) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/34400)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d2b19f3d-d549-4da4-9576-820fd84ba7e3/d2b19f3d-d549-4da4-9576-820fd84ba7e3/)