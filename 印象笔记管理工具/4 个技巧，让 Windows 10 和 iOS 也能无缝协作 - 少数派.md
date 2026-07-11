# 4 个技巧，让 Windows 10 和 iOS 也能无缝协作 - 少数派

---

4 个技巧，让 Windows 10 和 iOS 也能无缝协作
===============================

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/3F9814FB-2D62-4B4B-BA66-9A43B979364B)

4 个技巧，让 Windows 10 和 iOS 也能无缝协作

苹果生态的设备协作一直是它的优势，[隔空投送](https://support.apple.com/zh-cn/HT204144)（AirDrop） 配合 [接力](https://support.apple.com/zh-cn/HT209455)（Handoff）让你可以在 Mac 和 iOS 上轻松地进行传输文件、发送网址和同步剪切板等操作。但假如你用的是一台 Windows 10 电脑和一台 iPhone，有没有办法获得类似的体验呢？

作为一个双平台的用户，在这篇文章里我将分享几个实用的小技巧，想办法让你的 Windows 10 和 iOS 实现「无缝协作」。

文件传输：Windows 和 iOS 也有「隔空投送」
---------------------------

隔空投送是苹果设备之间无线传输文件的一个实用功能。而到了 Windows 10 和 iOS 上，许多人会使用微信、QQ 等 IM 工具来发送文件。这个方法固然简单，但操作起来终究不像隔空投送一键发送这样方便。

隔空投送之所以好用，是因为它可以在手机与电脑的任何地方直接发送，在手机上用分享菜单，在电脑上直接右键点击，这种不需要跳转的方式效率无疑是最高的。

现在市面上有很多第三方的文件传输工具，少数派之前也介绍了不少。我在尝试了几乎所有 Windows 和 iOS 平台间的传输文件工具后，最终选择了 [Send Anywhere](https://send-anywhere.com/)。

[> 拓展阅读：手机和电脑之间如何高效传文件？10 款跨平台传输应用和服务横评](https://sspai.com/post/53889)

使用 Send Anywhere 需要在 iOS 和 Windows 上安装相应的客户端。在 iOS 上，Send Anywhere 不需要打开客户端导入文件，直接利用分享菜单就能发送。以相册为例，第一次使用时，选择希望分享的照片，然后在分享菜单里找到 Send Anywhere，点击后 Send Anywhere 会生成一个 6 位的分享码，然后在电脑上输入后配对传输。之后 Send Anywhere 会记住你选择的设备，就不需要每次都输入分享码了。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/10255013-0803-46F3-B605-FB59FBA6225B.jpg)

Windows 上同样也非常简单，右键点击希望分享的文件，然后点击「Share with Send Anywhere」（或直接选择希望分享的设备）。手机会收到通知，点击通知接收文件即可。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/7C896D94-AF27-4B61-AAB9-BF77579D3FEE.png)

许多同类工具虽然有类似的功能，但都需要在分享菜单中选择「在 XXX 中打开」导入文件发送。而 Send Anywhere 能够实现类似隔空投送的效果，一键发送。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/D882699C-1DB5-4DBC-AA5E-28D51D4560E8.jpg)

其他同类工具很多都需要打开后再传输

需要注意的是，当你使用 6 位分享码传输时，Send Anywhere 采用的是局域网点对点传输，文件将直接发送到对应的设备上。而如果你在传输时选择了设备或采用链接分享，那么文件将上传到 Send Anywhere 的服务器中保存 48 小时（之后会自动删除）。

不过，假如你有大量传输文件的需要，或者需要传输体积较大的文件，更推荐使用 iOS 文件 App 里连接 SMB 服务的方式进行传输 。这种方法需要一定的动手能力，在 Windows 上设置好共享文件夹后，当两台设备处于同一局域网时，就可以直接进行传输。少数派 Power+ 付费栏目对此有一篇详细的介绍，感兴趣的话可以阅读一下。

[> 付费栏目：媲美 AirDrop，如何让 iOS 与 Windows 便捷地互传文档](https://sspai.com/post/57286)

发送网址：让 Safari 和 Edge 也能「接力」
---------------------------

Windows 10 上默认的浏览器是 [Microsoft Edge](https://sspai.com/post/58490)，iOS 上的默认浏览器是 Safari，要把手机上查看的网页发送到电脑上，除了复制粘贴到聊天工具，还有更快一步的方法。

在 App Store 里搜索下载「[Continue on PC](https://apps.apple.com/cn/app/continue-on-pc/id1254607852)」，这是微软开发的一款用来共享网页的小工具。

在 Safari 里打开想要分享的网页，在分享菜单里选择 Continue on PC，登录你在 Windows 10 电脑上登录的微软账号，选择你的电脑，分享成功后电脑端就会自动用 Edge 打开你分享的网页。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/B5035354-C99B-4EC8-9B5C-22AF5AFAAE7B.jpg)

除了 Edge，Chrome 和 Firefox 也都支持类似的功能。不过你需要在 iOS 上下载 Chrome 和 Firefox 浏览器，并且在电脑和手机上都要登录一样的 Google 和 Firefox 账号。相比 Edge，两者除了支持从手机发送到电脑，还支持从电脑发送到手机。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/02AA09D9-09BA-476D-8F74-6F63B693DAA3.jpg)

剪切板同步：Windows 也能有「通用剪切板」
------------------------

支持 Windows 和 iOS 同步的剪切板同步工具，之前少数派介绍过 [几款](https://sspai.com/post/43775)，另外一些国产的输入法也都支持云剪切板功能。这些方法的问题在于你不能像苹果的通用剪切板一样在 Windows 上复制后直接到手机上粘贴内容，还是需要进入 App 或切换输入法来粘贴。

如果你想在 Windows 和 iOS 上实现类似「通用剪切板」的效果，推荐你试试 [Bark](https://sspai.com/post/53090)。利用 iOS 的推送通知，它可以把你在 Windows 上复制的文字内容推送到你的手机上，并自动帮你复制到剪切板中。整个过程只需要在 iOS 上下载 Bark 的客户端，然后在 Windows 上下载一个 [脚本](https://github.com/authorTp/Handoff4Windows)，进行简单的配置后即可使用。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/7B7E9116-B8F6-472B-9A06-638BAF62DCD3.gif)

具体的操作方法，请参考少数派之前的 Bark 介绍文章：

[> 拓展阅读：定制推送内容、同步 Windows 剪贴板…… 把 iOS 推送通知玩出花：Bark](https://sspai.com/post/53090)

如果你需要双向的剪切板传送，那 MFiles 这款工具可以帮到你。它是一个支持多平台文件传输的小工具，还拥有剪切板同步的功能。

首先你需要在 [Windows](http://mfiles.maokebing.com/)和 iOS （￥18）上下载应用，并进行配对。从电脑或手机上复制一段文字，点击 Windows 客户端里的「传送粘贴板」或 iOS 客户端上的「传送 - 传送剪切板」，即可传送剪切板中的内容，直接在另一台设备上粘贴就行了。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/282355ED-205F-4C5D-A4F3-2F6E3950532A.png)

[> 拓展阅读：让 Android 用上隔空投送，你可以试试全平台的 MFiles](https://sspai.com/post/53192)

Office 文件接力：在电脑上继续编辑手机上的文档
--------------------------

工作里经常需要跟 Office 三件套打交道的人不在少数。现在很多人都习惯用手机查看别人发过来的 Word、Excel 或 PowerPoint 文件，但假如需要编辑文档，还是电脑更方便一些。如果你有将 iOS 上打开的 Office 文件同步到 Windows 上继续编辑的需求，下面这个技巧可以帮到你。

在 iOS 的 App Store 里下载新版 [Office](https://sspai.com/post/57281)应用，它可以帮你 iOS 上打开和编辑 Word、Excel 或 PowerPoint 文件。用它打开你需要编辑的 Office 文档，然后将它保存到你的 OneDrive 上（Office 365 用户拥有 1TB 的 OneDrive 空间，另外每个 Windows 账号则都会附赠 5GB 的 OneDrive 免费空间）。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/64E9AD51-47A0-41C1-A024-EF30876A79A6.jpg)

回到你的 Windows 电脑，打开系统设置，在「隐私」中找到「活动历史记录」，开启里面的选项。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/E5F19898-A7CE-43C6-9D1D-63C5172CB097.png)

然后按下 Win+TAB，打开任务视图。这时候你会发现在下面出现了一条时间线，在这里能够看到你最近保存和打开过的文件。之后你只要在手机上打开或编辑过 OneDrive 里的 Office 文件，你都能在这里看到记录。点击时间线里的文档就可以继续在电脑上进行编辑。相比文件传输或者使用其他网盘，这种方式更加接近「接力」的使用体验，两边都会自动同步你的修改记录，保证你随时随地都可以开始工作。

![](.evernote-content/88AD7623-D676-4256-942B-952169A5E9FE/04529D4C-7070-47A5-B271-FA58BB42C6F0.png)

以上就是我经常使用的 4 个 iOS 和 Windows 10 协作的技巧。除此之外，一些电脑厂商还会提供专门的同步工具来帮你进行协作，比如 Dell 的 [Dell Mobile Connect](https://www.dell.com/en-us/shop/dell-mobile-connect/ab/dell-mobile-connect) 就可以让你在 Windows 电脑上查看 iPhone 的通知、短信，还能直接在电脑上用手机打电话，如果有需要的话不妨试试看。

> 更多实用的 Windows 10 小知识，尽在「[真正好用的 Windows 10，从这里开始](https://go.sspai.com/topic/270)」专题

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，了解更多 iOS 和 Windows 使用技巧 ‍

27363

文件传输：Windows 和 iOS 也有「隔空投送」

发送网址：让 Safari 和 Edge 也能「接力」

剪切板同步：Windows 也能有「通用剪切板」

Office 文件接力：在电脑上继续编辑手机上的文档

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/59329)

[📎 在印象笔记中打开](evernote:///view/207087/s1/476857ba-fac3-4f28-bd42-6a7e874ac038/476857ba-fac3-4f28-bd42-6a7e874ac038/)