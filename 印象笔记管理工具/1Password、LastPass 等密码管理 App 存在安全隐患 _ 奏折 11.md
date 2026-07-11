# 1Password、LastPass 等密码管理 App 存在安全隐患 | 奏折 11

---

1Password、LastPass 等密码管理 App 存在安全隐患 | 奏折 11
===========================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

本周最值得关注的新闻，是一篇和密码管理 App 相关的论文。这篇论文指出，1Password、LastPass、KeePass 等密码管理应用存在安全隐患。黑客可以通过一些手段，在电脑的内存地址上提取到用户的密码，某些情况下甚至还能获取到主密码。作为普通用户的我们，有必要为此感到恐慌吗？

本周的新鲜 App 板块有 3 款 App 介绍，分别是一款 Windows 上的窗口工具，一款即开即用的多协议下载器，和一款将 macOS 文件变成跳转链接的工具。

常规更新板块，有：老牌压缩工具 WinRAR 修复了一个存在了 19 年的漏洞，Gmail 移动客户端采用了 Material Design 设计，Day One for Mac 升级到了 3.0。

本周的工具模板板块，分享了在前几期 Power+ 文章中大受欢迎的 Windows 效率工具 Quicker 的优秀动作，你可以直接通过文章里的链接进行下载。

下面，让我们开始这期 Power+ 奏折的正文：

⭐️ 重点关注
-------

### 密码管理 App 的安全隐患

**@Fairyex：**就在上周，Independent Security Evaluators 为了检查市面上常见的密码管理应用的安全性，选择了 5 款最流行的密码管理应用（1Password 4、1Password 7、Dashlane、LastPass、KeePass），并在 Windows 10 平台上进行多场景下的模拟攻击测试。最终发表 [《Password Managers: Under the Hood of Secrets Management》](https://www.securityevaluators.com/casestudies/password-manager-hacking/)（密码管理器们：隐藏在引擎盖下的秘密）阐述了他们的发现。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/177BDEA8-00F6-41AE-BA39-FF193794A542.png)

文章引言与简介

在测试中，安全团队针对密码管理应用的三个状态 —— 未运行、已解锁（应用运行且用户已输入主密码）、锁定状态（应用运行且用户未输入密码或点击锁定按钮）进行了测试。结果发现**这些应用未运行时都能够很好地保护用户储存在本地储存的密码数据，但是在运行时（无论锁定还是解锁）安全团队都能够在它们的内存地址上提取到用户记录的密码，某些情况下甚至还能获取到主密码。**

这里有一个很关键的点，那就是，黑客是从**内存**中获取密码的。在进一步阐述它的原理之前，我觉得有必要解释一下内存是什么。因为很多人常常会把「内存」和「硬盘」搞混，比如我们常听到有人说：「我的 iPhone 内存是 128GB。」这其实是闹了笑话，内存和硬盘是完全不一样的两样东西。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/650A92AF-575F-4741-BA95-64FC0B81279B.png)

机械硬盘与内存条，图源：维基百科

大家可能都知道，我们计算机上所有的文件数据都储存在硬盘里。而我们运行系统与软件这些东西，本质上是不断地将关于它们的本地和联网获取到的数据扔给 CPU 去处理，电脑上的 CPU 是负责处理数据的，所以速度非常快（每秒上十亿次计算）。

但是相对于 CPU 的处理速度而言，硬盘的速度却很慢。如果直接让硬盘负责「传递」这些数据 CPU 就得不时停下来，等储存硬件找到数据才能继续处理，非常浪费 CPU 的性能。而且硬盘等储存硬件都有读写寿命，如果不断读取写入数据给 CPU 那么硬盘很快就会「寿终正寝」了。

这个时候我们就需要一种读写寿命近乎无限长，并且读写数据时间近乎无限短的东西 —— 于是半导体材料制作的内存（RAM）诞生了。它就是为了跟 CPU 组成伴侣而生的，由于使用半导体材料加上专门为快速读写数据优化的算法，所以它能轻松喂饱 CPU 的胃口。于是我们使用电脑的过程就变成现在这样：**运行系统 / 软件，先把相关数据从硬盘转移到内存，然后 CPU 直接存取内存上的数据。**我们开机和玩游戏的加载时间就是这么来的（想想游戏的加载时间就知道 CPU 为什么不能直接从硬盘上读取数据了）。

遗憾的是内存的半导体材料不能跟硬盘的磁性那样通过永久改变某个区域的磁性来实现长时间断电保存数据的功能（这也是内存为什么读写寿命近乎无限长的原因，硬盘每一次读写都是要磨损硬件的），一旦断电内存上的所有数据就没了。所以硬盘和内存还是只能「各司其职」。

所以简单来说材料限制的情况下，硬盘能够长久保存数据但寿命和读写数据时间有限，内存不能长久保存数据但拥有非常短的读写数据时间和非常长的工作寿命。了解了内存的基本原理，我们就能继续介绍，黑客究竟是如何从内存中盗取你的密码的？

在 1Password 4 里，如果一个用户输入主密码，自动填充了网站密码，然后锁定应用。这个时候主密码并没有从内存中清除，只是简单地用系统提供的方法加密了一下，也就是说如果你打开过 1Password 4 （不需要输入主密码）并且没有彻底退出，然后设备关机前被人偷走或者计算机被人远程控制，**那么他用系统提供的反加密方法就能从内存中提取到明文的主密码。**

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/07DE809D-9CC8-4461-AFD5-70B300A51939.png)

测试人员获取到的主密码，图源：ISE

而安全人员测试后发现 1Password 7 比起 1Password 4 更加糟糕，1Password 7 运行时会将整个密码数据库一起加载，**而且主密码和密钥（辅助加密）都是明文放在内存里的**，而不是像 1Password 4 那样只是加载用户需要的那条数据。最糟糕的是，如果这时系统发生了错误（比如死机），那么内存内容包括 1Password 的数据会被明文存储为硬盘上的调试文件。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/D9B401FE-2916-462D-81E9-DCA9C12CC46D.png)

测试人员获取到的用户所有保存的密码，图源：ISE

Dashlane、Keepass、Lastpass 在内存数据处理上也都大同小异，所以它们也能够通过上面的方法获取到用户的密码数据。

这篇文章出来后引起了外网的激烈讨论，有的人认为这篇文章提供的漏洞实现起来场景非常地有限（需要能够访问到用户的内存数据），而且如果攻击者能够做到这一点也没必要使用这种方法来获取密码，可以使用键盘监控器等其他更加容易的方法。还有的人认为密码管理应用最重要的不是安全性，而是能够管理自己记不住的一大堆密码，并且如果网站本身泄露的话一切都白搭。

1Password 官方对文章也进行了[回复](https://discussions.agilebits.com/discussion/comment/493044/#Comment_493044)，他们肯定了文章探索的内容必要性和安全性问题，但认为这个问题的现实威胁非常有限，不值得为了解决这个问题而放弃使用系统提供的内存管理方案转而自己实现一套内存管理方法（就连测试版中加上的英特尔 SGX 内存保护技术也在正式版中放弃了），这样不仅要花费过多的精力，还容易增加其他的漏洞。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/2FAFE24B-BA46-4183-91FA-3F1799C18864.png)

1Password 官方回复部分截图

那么如果密码管理应用不能完全保证安全性，那么我们应该继续使用它吗？我的观点和 Independent Security Evaluators 一致：**密码管理应用不需要做到完美，他们只需要做到比没有用密码管理应用更好就行了。**

注：感谢 [@PlatyHsu](https://sspai.com/user/714505/posts) 提供了此次事件的消息源。

新鲜工具
----

### 让 Windows 实现多标签页窗口：Multrin

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/48D1D228-6D5D-4D06-9D64-BFB0D2078396.png)

**Multrin**

[下载链接](https://github.com/sentialx/multrin/releases)

#### 应用简介

Multrin 是一款新出现的 Windows 平台的窗口管理工具，可以为多个本地窗口添加标签页支持。

#### 简单方便的窗口标签页

**@沨沄极客：**微软曾经为 Windows 画了一个饼，表示要添加一个名为 Windows Tab 的窗口多标签页功能。但实际上这个功能已经在预览版中被彻底砍掉，短期内不会再有动静了。

如果目前想在 Windows 上体验多标签页功能，可以通过 Clover 这种第三方插件，为系统的文件管理器添加标签页支持，但其他的软件窗口就没有办法了。这一款 Multrin 采用了另一种思路，它并不打算为每一个窗口添加多标签页功能，而是提供一个空白窗口，让你把需要放在一起的窗口拖进去，实现多标签页的效果。比 Station 更为简单粗暴。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/179CA3EB-1D17-42A2-9A05-51F19CAC4C86.gif)  

Multrin 使用方法

许多人为了能够及时查看消息，经常需要同时开着 QQ、微信，工作环境下也有许多本地工具。它们无法靠 Station 这类工具聚合，那就可以来试试这款 Multrin 把本地工具的窗口聚合放在一起。

不过这款工具显然还没有开发完整，还有很多优化上的问题。再加上基于 Electron 和 React，使得在实际使用时仍然会有些卡顿。不过作为一款新鲜工具，这样的表现尚可接受。你可以通过 [GitHub](https://github.com/sentialx/multrin/releases) 链接下载 Multrin。

### Motrix 下载器：即开即用的多协议下载器

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/0F400D71-3C59-4704-91D8-3B05F28D1EC2.png)

**Motrix**

[下载链接](https://motrix.app/)

#### 应用简介

**@Fairyex：** [Motrix 下载器](https://motrix.app/)是最近在 GitHub 上开源的一个个人开发的下载器，它的最大优点是封装了著名的下载工具 Aria2。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/EEAA4D99-9863-48D7-8B8B-91FFC85F9D7E.png)

多平台支持

Aria2 是一款支持多种协议的轻量级命令行下载工具。它具有占用内存小，支持平台多，功能丰富等优点。但是同时它没有用户界面，需要用命令行工具或者连接远程控制台使用，而且使用前需要手动填写配置文件里面复杂的配置，上手难度有点高。具体可以查看 [「Mac 上使用百度网盘很烦躁？花点时间配置 aria2 吧」](https://sspai.com/post/32167)。

Motrix 下载器封装了 Aria2 与默认配置并给它添加的用户界面，使得那些想要使用 Aria2 却搞不清如何配置的朋友们也能够上手即用。支持常见的 HTTP/FTP、BT 种子、磁力链接等下载协议，还可以通过 Chrome 插件支持百度云盘下载。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/17C78ED1-EF4D-4D0D-8CBC-A6C79052D27D.png)

下载界面，图源：Motrix 官网

### 统一 macOS 的文件跳转链接：Hook

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/536FB20A-BB4E-4067-933D-4C308D4A90C4.png)

**Hook**

[下载链接](https://hookproductivity.com/)

#### 应用简介

**@Minja：**URL 协议是一个神奇的东西。通过一条链接，几乎无论身在何处，都可以跳转到指定到网页、文件或者运行目标自动化动作。

iOS 上的自动化，由于系统本身的限制，很大程度上要依靠 URL Scheme 来跳转。后来 x-callback-url、Universal Link 相继登场，iOS 上的 URL 协议家族越来越庞大，以至于不了解 URL Scheme 历史的人可能会好奇，为什么 macOS 上反而没有那么好用的跳转工具。macOS 倒是也有 URL 协议，但基本只有原生应用适配这些链接格式，相比 iOS 上的 URL Scheme，使用体验实在难以望其项背。

URL Scheme 本身只是一种协议，默认的，`http://` 打头就用浏览器打开，`file://` 打头就在 Finder 显示文件…… 此外还可以自己定义。这就给了各路玩家施展的空间。之前 @OscarGong 在《[在 macOS 中制作自己的 URL Schemes](https://sspai.com/post/44425)》就介绍过自定义的方法。

**而这回介绍的文件跳转工具 [Hook](https://hookproductivity.com/)，则有望统一** 1 **macOS 上的文件 URL 跳转协议。**Hook 本质上是重新设计了 macOS 的文件 URL，用 `hook://` 开头的链接一统四分五裂的文件路径格式，从而实现几乎在任何软件里，点击 Hook 专用链接都可以跳转到真实的文件 —— **即便文件位置移动了，甚至被误放进了垃圾桶，还是可以链接上，**和它的名字（hook，钩子）很贴合。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/6513C52A-24A2-43AE-84AC-2BBBC7DD9BA1.gif)

文件被放进垃圾桶后也能「钩」上

这种跳转可以说是一种稍显霸道的「劫持」，所以你需要授权给 Hook 辅助功能权限并且保持它开启 —— 没有开启的前提下，点击 Hook 专用链接也能自动打开 Hook，这不难，@OscarGong 上面那篇文章就解释过相关原理。

Hook 的作用当然不止用默认方式打开文件，**它还可以直接设置文件的打开方式。**简单分析下面这条「在 nvalt 中打开」的 Hook 的链接，不难发现它由 3 部分组成：

1. `hook://`：表示召唤 Hook 出来
2. `nvalt/`：表示用 Byword 打开
3. 后面一串是文件的 id

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/04F81F4C-5090-449A-A422-846726036CEE.png)

设置打开方式

链接本身很简单好懂，通过自己设置中间部分，我们也可以创造自定义 URL Scheme。比较麻烦的是，Hook 里大多数打开方式都需要自己写脚本，说白了就是给了一大堆空壳让我们自己折腾。脚本是 AppleScript 写的，搜 `AppleScript open file with application` 能找到很多参考资料。具体是等 Hook 以后更新适配（它正在公测），还是自己动手做起来，就看对文件链接的需求是否够强了。

⚙️ 常规更新
-------

### WinRAR 更新：修复存在了 19 年的漏洞

**@Fairyex：** 软件安全领域网站 Check Point 最近发布了一篇[文章](https://research.checkpoint.com/extracting-code-execution-from-winrar/)，指出著名压缩软件 WinRAR 存在一个长达 19 年未被修复的漏洞。

该漏洞位于程序文件夹里面的 unacev2.dll 中，这个文件是用来使 WinRAR 支持访问与解压一个非常古老的 WinACE 压缩文件格式。

黑客只需要将正常文件与恶意文件混合利用 WinACE 压缩，并修改文件头后传给目标用户，目标用户在用 WinRAR 解压时 unacev2.dll 会扫描全盘地址以确定解压路径，漏洞会使修改的文件头里面的解压命令被执行，把恶意文件解压到黑客指定的路径（比如系统启动目录），从而实现控制用户的电脑。**因为整个过程没有明显感知，所以用户可能无法察觉到恶意文件。**

由于 unacev2.dll 并不开源且 2007 年 8 月该公司的网站已关闭，因此新版本（5.70 Brta1） 起 WinRAR 决定移除相关文件，不再支持 ACE 格式，漏洞自然也就修复了。

新版 WinRAR 下载：[官网](https://www.rarlab.com/download.htm)。当然，如果你不喜欢 WinRAR 的价格或者中国版的广告，可以尝试免费无广告且可以免费商用的 [Bandizip](http://en.bandisoft.com/bandizip/)，它包含了所有我们日常用到的压缩功能。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/9A85E62C-070A-4360-8FD7-EA595E39F2E2.png)

Bandizip 界面

或者你也可以使用大名鼎鼎的开源免费软件 [7-Zip](https://www.7-zip.org/)，简单好用，虽然不支持压缩成 RAR 文件但可以压缩成压缩率更高的 .7z 文件，并且支持包括 RAR 在内的绝大多数压缩文件格式的解压。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/0FF595FD-806F-4829-99D2-737CF670EAAA.png)

7-Zip 界面

### Gmail 客户端采用 Material Design 设计

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/A17BDCA3-7463-444A-9190-F9C6295CA87F.png)

**Gmail**

下载链接：[Android](https://play.google.com/store/apps/details?id=com.google.android.gm)、[iOS](https://itunes.apple.com/cn/app/gmail-email-by-google/id422689480?mt=8)

#### 应用简介

Gmail 是由 Google 提供的，世界上使用人数最多、表现最稳定的邮件服务之一。在主流移动平台有其客户端。

#### 值得注意的更新内容

**@文刀漢三：**Google 自从去年 9 月份[宣布](https://www.blog.google/products/gmail/inbox-signing-find-your-favorite-features-new-gmail/) Inbox 即将关闭的消息后，便把开发重点完全放到了 Gmail 上。很多 Inbox 的功能也已经被整合进了 Gmail 客户端里，比如延后电子邮件、智能推送、智能回复等。

最近，Gmail 客户端换上了 Material Design 设计，终于摆脱了以往那个「商务范」十足的形象，变得简洁、好看起来。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/6BB4164B-02E9-4501-ABAF-0F0847B5A249.png)

采用了 Material Design 设计的 Gmail 客户端

深受很多用户喜爱的 Inbox 客户端，也将在这个月底彻底停止服务。如果你正在寻找 Inbox 的替代品，不妨尝试一下 Gmail 官方客户端。

### 全新的日记本，你喜欢吗：Day One for Mac 3.0

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/F457EBBE-FDDB-4F24-ACBB-CA81C5FA9742.png)

**Day One for Mac 3.0**

[下载链接](https://itunes.apple.com/cn/app/day-one/id1055511498?mt=12)

#### 应用简介

Day One 是一款以简洁美观著称的日记应用，在同类应用中长期霸占榜首。除了最基本的用文字记录生活，还可以通过插入图片的方式快速添加当天的位置、天气等信息。良好的用户体验收获了大批好评。本次更新的是 Day One 的 macOS 版。

#### 界面大改的全新版本

**@沨沄极客：** 这次 Day One 3.0 的更新带来了大量外观上的改进：新的界面 UI 和新的工具栏，还有新的 Day One 图标、日记提示。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/705C9E88-EBFE-4EBB-BD8F-F548D8DCC76F.png)  

Day One 3.0 主界面

**Day One 的界面左侧取消了色块，整个界面变得以白色为主**。这一点和微信的策略有点像，刚开始总会让人不习惯，用的久了就会发现界面较以前更清爽。如果觉得不好看，Day One 在 Dark Mode 方面也做了进一步优化，可以先换上 Dark Mode 适应一段时间。

**Day One 此次更新还对操作逻辑做了许多调整**，最上方的工具栏变得更符合 macOS 风格，从左到右分别是侧边栏开关、筛选、切换日记本，还有搜索和 iOS 风格的四种回顾视图，整体逻辑和 iOS 的风格变得更为统一。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/560B5FC3-603B-4549-830A-35AD1279F4FA.png)  

Day One 工具栏和筛选

同时，Day One 的筛选功能变得更好用了，增加了许多直观的筛选方式，在按年份筛选时还会显示那一年写的日记数量。

新的 App 图标也变得略有一些拟物化，更像是一本蓝色的日记本了。略带倾斜的图标也和系统自带的工具们保持了相似，这样的设计要比原来直接放一个 iOS 端图标的做法要美观不少。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/6437C068-5E82-47B9-B79D-BCB1A7F7AB59.png)  

Day One 新图标

最后，本次还对英文字体进行了更新，新增支持 Whitney，Ideal Sans，Sentinel 等字体。这些字体在上次的 iOS 版客户端更新中也提到了。不过 Day One 的桌面版仍然没有支持 iOS 版的音频、绘画日记。也不支持从活动源中直接添加日记实践。所以这次更新仍然属于外观方面的大改进。

整体而言，Day One 的这次改进正在往经典的 macOS App 风格走，同时在努力消除和 iOS 版本之间的差距，尽量做到和 iOS 端的操作逻辑保持一致。

### 好用的歌单迁移 App：SongShift 4.0

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/87A72601-6FBC-47F3-88F7-486ADF1DFAE4.png)

**SongShift 4.0（2019–02–20）**

[下载链接](https://itunes.apple.com/cn/app/songshift/id1097974566?mt=8)

#### 应用简介

SongShift 是一款 iOS 上的歌单迁移应用，可以让你在多个音乐平台之间迁移歌单。支持 Apple Music、Spotify、LastFM、YouTube、Tidal 等国外服务。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/F5100850-F368-4A62-8856-48BC60283490.png)

SongShift

#### 值得注意的更新内容

**@文刀漢三：**此次更新内容主要有：

* 更好的匹配算法，会优先匹配专辑里的歌曲，而不是精选集里的歌曲；
* 新增迁移确认步骤，方便找出匹配有问题的歌曲；
* 新增了单曲和专辑的迁移方式；
* 等……

SongShift 主要是一款歌单迁移工具，一般来说在你需要迁移服务的时候使用一次就行了。但我的用法不太一样，因为我同时在用 Apple Music 和 Spotify。Spotify 是我日常听歌的主力服务，而 Apple Music 则是主要用于和 HomePod 交互，以及开通了家庭套餐，给家里的其他人使用。所以我会每隔一段时间打开 SongShift 一次，将 Spotify 的歌单同步到 Apple Music 里。

SongShift 虽然有内购，但免费版已经足够我们日常使用。如果没有特别的需求，可以不进行购买。

### BBEdit 12.6：为回归 Mac App Store 做准备

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/6C62DAA3-FB33-4ECB-A74B-26037B673EB4.png)

**BBEdit 12.6**

[下载链接](https://www.barebones.com/products/bbedit/)

#### 应用简介

BBEdit 是一款已经有 20 多年历史的 macOS 文本编辑器应用。支持 HTML 等多种编程语言的语法高亮，并且提供了丰富的自定义模块，以及强大的智能搜索、正则表达式、脚本自动化等功能。

#### 值得注意的更新内容

**@文刀漢三：**我因为偶尔需要编辑 HTML 文本，所以需要一款能对 HTML 语法进行高亮的工具。由于只是轻量级的需求，于是便挑选了更符合 macOS 设计风格的 BBEdit。

BBEdit 本身可免费使用，付费后可以获得完整的 HTML 配套工具、Text Factories 等进阶的功能。但对于我的需求来说，免费版就已经足够使用了，一般的 HTML 语法都能高亮显示，而且还能用正则表达式来进行更精确的文本替换。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/47967B75-4F70-4B2E-AB8A-684670490E63.jpg)

BBEdit

BBEdit 的这次更新，主要是为了之后回归 Mac App Store 作准备的。BBEdit 其实曾经上架过 Mac App Store，但在 2014 年却离开了 Mac App Store。当时离开的原因，[据其创始人 Rich Siegel 称](https://sixcolors.com/post/2014/10/bbedit-at-max-q/)，是由多个原因长期累积造成的。包括苹果 30% 的分成、无法维护和客户的关系（不知道谁买了你的软件，也无法获得客户的信息）、沙盒机制对功能的限制等。Rich Siegel 说，Mac App Store 会给他们带来额外的压力和困扰，这并不值得。于是便离开了 Mac App Store，只在自己的官网上出售。

后来发生的事我们也知道，在去年的 WWDC 上，苹果不仅推出了全新改版的 Mac App Store，同时也在发布会上宣布，前面提到的 BBEdit、Office 365 订阅版、摄影后期工具 Lightroom CC、FTP 文件传输工具 Transmit 等一批重量级的 app，将会陆续登陆 Mac App Store。

Office 365 和 Lightroom CC 可能是因为商业合作之类的原因才进入 Mac App Store，但 BBEdit 和 Transmit 被带回来主要原因，应该是和沙盒机制的改变有关 2 。

因为上架 Mac App Store 的软件必须遵守沙盒机制。它的目的是为了保护用户数据不被软件随意使用，当没有获得用户允许时，软件没有权限使用软件之外的任意文件。

拓展阅读：[一款软件是否来自 Mac App Store，对用户来说的四大区别](https://sspai.com/post/32204)

比如像 Markdown 编辑器 [Byword](https://itunes.apple.com/cn/app/byword/id420212497?mt=12)，如果 Markdown 文档里包含了一张存放在 Finder 本地的图片，当你想用 Byword 内置的预览功能来预览这张图片时，就需要经过用户的允许。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/EE0D1B06-7C21-4277-81CA-74AF64DC626A.gif)

用 Byword 预览外部图片时，需要经过用户允许

如果是偶尔需要用到外部文件，那么每次点击一下「允许」，也是可以接受的。但是像 BBEdit 这样的高级工具，它有很多进阶的功能需要频繁访问文件和文件夹。如果不能不受限制地访问，许多 BBEdit 中最有用的功能都会失效。

在去年 WWDC 之后，苹果也许是修改了 Mac App Store 审核的政策，允许软件询问用户的允许，来绕过沙盒机制。比如这次 BBEdit 12.6 更新后，第一次启动软件时，就会弹出一个窗口询问是否允许访问所有文件。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/F0827217-41ED-4F95-95EB-FCEF28D39F34.jpg)

第一次启动 BBEdit 时，会询问是否允许访问所有文件

[查看完整的 BBEdit 12.6 更新日志](https://www.barebones.com/support/bbedit/current_notes.html)

国外博主 Michael Tsai [提到](https://mjtsai.com/blog/2019/02/27/bbedit-12-6-to-return-to-the-mac-app-store/)，其实在 OS X 10.7 的时候，app 就已经可以询问沙盒权限了。但是从来没有这样的 app 出现过，很有可能都是被 Mac App Store 审核给拒绝了。那么这次之后，苹果会怎样应对沙盒问题的审核呢？是开放给所有 app，还是看情况决定？

Michael Tsai 认为，普通用户并不知道开放这个权限带来的后果是什么。而且，也没有一个统一的界面，能让我们看到哪些 app 获得了这个权限，以及它们访问的哪些文件夹。如果因此出现了安全问题，苹果完全可以推脱给用户 —— 这是用户自己允许过的。

我认为这也是苹果无奈的地方。一方面既想掌控系统的权威和保证系统安全，另一方面又不想失去这些 app，于是推出了一个没有明确规定的方案。具体怎么实行，只能观察 Mac App Store 接下来的变化了。

工具模板
----

### Quicker 实验室：优秀 Quicker 动作推荐

**@沨沄极客：**在前几期的《[2018 好物推荐：应用篇](https://sspai.com/post/52867)》中，我为大家介绍了这款 Windows 上的效率工具：Quicker。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/24C30151-C1E8-401C-AFF0-80FB1E08734C.png)

**由于 Quicker 提供了类似捷径（Shortcuts）和 Automator 的动作组合功能**，自由度极高，使得它远超同类的启动器应用。加上作者对软件的更新频率极高，许多软件问题可以被快速解决，我个人非常看好这款软件，**很有可能成长为 Windows 平台的捷径**。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/0CCBACA7-D8AF-430C-ABEA-1CC9EEDEB23E.png)  

复杂的组合动作

从上周开始，我会在[微博](http://weibo.com/FoxGeeker)和 [Twitter](https://twitter.com/yarinzhang) 上每天推荐一个 Quicker 动作，以我原创为主，也会推荐一些优秀的实用动作。

由于微博、Twitter 的字数限制，通常只够简单介绍动作的用法而非原理。所以我会每周在我的博客中更新这些动作的详细介绍，以及制作中的方法、问题、技巧，可以帮助大家完成更适合自己的 Quicker 动作。

这里给大家推荐两个非常实用的动作 —— 快速上传图片到 sm.ms 图床，自动分类文件。

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/682E695F-DD9E-4562-A782-4A141DB8F3C7.gif)  

一键上传到图床

「上传到 sm.ms 图床」中用到了近期更新的新特性，允许用户把选中的文件、剪贴板图片、截图上传到图床，上传完毕后自动生成 URL、HTML、Markdown 三种文字并复制到剪贴板。对于需要图床的作者而言非常便捷。

[**上传到 sm.ms 图床 - 动作下载**](https://getquicker.net/Sharedaction?code=18fdf83e-048e-46c7-185a-08d69d1d124b)

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/A152B8E7-DD79-486D-9C1C-53267E429D20.gif)  

自动分类文件

另一个动作是「为同类文件归档」，选中一些文件后运行动作，自动为同类型的文件建立文件夹，文件夹名称为文件类型。很适合用于快速整理文件。

[**为同类文件归档 - 动作下载**](https://getquicker.net/Sharedaction?code=06e1bd16-6be0-4f27-05d5-08d6960a88e5)

如果想获取各位可以按需关注[我的微博](http://weibo.com/FoxGeeker)、[Twitter](https://twitter.com/yarinzhang)，或者订阅[我的博客 RSS](http://ifoxfactory.com/feed.xml)，来获取更多的 Quicker 动作推荐。如果你尚不了解 Quicker，可以回顾一下这篇文章《[2018 好物推荐：应用篇](https://sspai.com/post/52867)》，或在 [Quicker 官网](https://getquicker.net/)下载使用。

技巧
--

### 微信技巧：将需要跟进处理的对话置顶

**@文刀漢三：**微信中有个置顶功能，一般我们会把最频繁联系的亲朋好友放到置顶里。但是，[@张扬](https://sspai.com/user/756809/posts) 在上周的 Power+ 文章《[心如止水的 Inbox Zero 状态，你也可以轻松达成](https://sspai.com/post/53025)》里，回答了一位读者的提问。其中就提到了置顶功能的另一种用法 —— 将待处理的对话置顶。

> [……] 还有另一个思路，是我在微信里会用的：主动把需要跟进处理的对话置顶，直到答复了为止。例如截稿日期前， Power+ 编辑找我催稿，在我把稿子发给他之前，我就会将他的对话置顶，直到交稿了再取消置顶。这个思路适用的对话数量同样不宜太多，因为没法区分优先级。

推荐
--

### 英伟达 AI 开源项目的遍地开花：各种 NotExist 网站

**@Fairyex：**上周奏折我们介绍了 [This person does not exist](https://thispersondoesnotexist.com/) 和它的同类网站 [This waifus does not exist](https://www.obormot.net/demos/these-waifus-do-not-exist.html)。它们都是用人工智能（AI）生成一些逼真的不存在的照片，然后评论区中有读者朋友 @薛啸宇 给出了另一个 [生成不存在的猫图片的网站](https://thiscatdoesnotexist.com/)，这勾起了我的好奇心。难道还有更多 NotExist 类网站？于是我就去仔细找了下，果然发现还有很多这样子的网站：

* [These cats do not exist](http://thesecatsdonotexist.com/)，上面读者提供的生成猫图片网站每次只能刷新一张，对于爱猫人士来讲这可远远不够。于是这个升级版的网站便出现了，它跟 This waifus does not exist 一样由好几十张自动生成的猫照片组成照片墙，充分满足爱猫人士的需求。

  ![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/2188574B-F375-41B8-9308-467159926956.png)

  有几张有点惊悚
* [This airbnb does not exist](https://thisairbnbdoesnotexist.com/)，这个网站利用了 Airbnb 的房间图片来训练以生成不存在的房间照片。不仅如此，图片下面还配上了像模像样的用户评论。

  ![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/26F0BC9A-0ED4-49F7-B904-A24A163376F6.png)

  弄得跟真的似的
* 除了简单展示外，甚至有人把 This person does not exist 做成了游戏，打开 [Which face is real](http://www.whichfaceisreal.com/) 会显示两张人脸照片，只有其中一张是由 AI 生成的。我们要做的是选择哪张照片是真实的，选完才会告诉我们答案。

  ![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/F46CC003-13F7-4E30-96BB-681771906810.png)

  猜猜哪张是真人？

更多项目可以在 [Awesome-doesnotexist](https://github.com/paubric/awesome-doesnotexist) 这个 GitHub 页面中找到。

之所以最近会出现这么多同类网站，是因为 Nvidia（也就是做显卡的那个英伟达）最近在 GitHub 上公布了自己的开源项目 [StyleGAN](https://github.com/NVlabs/stylegan)。这个开源项目是 AI 算法，利用这个算法，人们只需要使用自己的训练集及加上 tensorflow 等软硬件就能比较简单地让电脑学会生成类似的图片。Nvidia 这个开源的项目可以说大大推动了人工智能领域的普及，虽然现在才刚刚发布，但以后可以用在更加广阔的领域（比如我们每个人都非常期待的自动生成海报、PPT 甚至各种画作）。下面这个视频就展示了 StyleGAN 如何应用到汽车行业（[源地址](https://www.youtube.com/watch?v=OLZ3-ZJwSu4)）。

网站链接：

* [These cats do not exist](http://thesecatsdonotexist.com/)
* [This airbnb does not exist](https://thisairbnbdoesnotexist.com/)
* [Which face is real](http://www.whichfaceisreal.com/)
* [Awesome-doesnotexist](https://github.com/paubric/awesome-doesnotexist)

### 博客：Signal v. Noise

**@Minja**：最近 Hum 给我推荐了博客，名字很有趣，SVN，不是程序员用的那个版本控制器，而是 Signal v. Noise 的缩写。博客是 [Basecamp](https://basecamp.com/) 团队写的，专讲各种效率方面的内容，尤其是远程工作、在线协作，比较新潮。

Basecamp 国内用户可能接触不多，其实它是一个在线协作工具 3 ，在国外 App 圈里名气不小，有 19 年的历史，坐拥 300 万企业级用户（2019 年官网数据）。Basecamp 在很多工具推荐榜单里都露过脸，有些读者还可能有印象

![](.evernote-content/D58D2B28-F709-4A4D-A38C-BE6408788F69/EBD1C928-E962-459F-AF14-73B0C6E670A7.png)

Basecamp

冷知识：Basecamp 团队最早就是做咨询的，后来跑去实战一番开发了软件，现在又在出版界混得不错。

但是这样一个工具，背后却只有一个 30 多人的团队，还分散在世界各地，不得不让人好奇他们的工作方式。实际上，这帮人并不是工作狂，他们反对办公室、反对朝九晚五，还提出过「该睡就睡」的口号 4 。SVN 博客就是他们工作态度和方式的记录，你可以读到很多反对疯狂工作、快速扩张的文章：《[Busy is the new stupid](https://m.signalvnoise.com/busy-is-the-new-stupid/)》《[How about fixing the workplace rather than avoiding it at 4am?](https://m.signalvnoise.com/how-about-fixing-the-workplace-rather-than-avoiding-it-at-4am/)》《[You probably won’t make it to the top](https://m.signalvnoise.com/you-probably-wont-make-it-to-the-top/)》……

SVN 上的内容都是几乎互联网行业，遇上国内行业传统的限制，我们也许很难效仿，但是不失为一种新的工作思路。Basecamp 团队也给我们支了招，不一定要马上和上班说再见，可以试试一周里面远程几天，或者半天上班、半天远程，如果真的发现效率提高了，再试着投入远程工作的怀抱。

除了博客，他们还出了一系列畅销书，中文版比较有名的有《重来》《重来 2》，不过就像他们在书里所直言不讳的那样，这些书都是博客和日常随想的「副产品」—— 其实就是零散文章的大合集，能读原版博客的话就不用掏钱买书了。

网站链接：[Signal v. Noise](https://m.signalvnoise.com/)

RSS 订阅地址：`https://m.signalvnoise.com/feed/`

### 文章：提升 Chrome 的搜索效率

**@文刀漢三：**[第 9 期奏折](https://sspai.com/post/52902)我们推荐过的网站 [BrettTerpstra.com](http://brettterpstra.com/)，最近写了一篇如何提升 Chrome 搜索效率的文章，介绍了 Chrome 自带的关键词搜索功能。

比如我们可以输入「tb 物品名称」来直接使用淘宝网站内置的搜索功能，就像我们使用 LaunchBar 和 Alfred 等工具一样。

如果你经常使用 Chrome 的话，可以跟着文章的方法，为你经常搜索的网站设置搜索关键词。

原文链接：[Save time with Chrome custom search engines - BrettTerpstra.com](https://brettterpstra.com/2019/01/29/save-time-with-chrome-custom-search-engines/)

扩展阅读：[你每天都在用的 Chrome 地址栏，原来还藏了不少提升效率的小功能](https://sspai.com/post/44922)

1. [极少数工作方式特殊的软件可能还不适配，比如 nvALT。↩](#)
2. [Transmit 也曾上架过 Mac App Store，后来因为试用版功能的限制问题，也离开了 Mac App Store。↩](#)
3. [严格说是项目管理工具。↩](#)
4. [还把它当作了书的章节标题。↩](#)

---

[🌐 原始链接](https://sspai.com/post/53158)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8ba34822-797c-4ad7-ae75-5ceeff7363df/8ba34822-797c-4ad7-ae75-5ceeff7363df/)