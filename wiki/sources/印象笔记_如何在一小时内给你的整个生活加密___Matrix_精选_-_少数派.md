---
title: "如何在一小时内给你的整个生活加密 _ Matrix 精选 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在一小时内给你的整个生活加密 _ Matrix 精选 - 少数派.md
tags: [印象笔记]
---

# 如何在一小时内给你的整个生活加密 _ Matrix 精选 - 少数派

# 如何在一小时内给你的整个生活加密 | Matrix 精选 - 少数派 --- 如何在一小时内给你的整个生活加密 | Matrix 精选 ============================ [

---

# 如何在一小时内给你的整个生活加密 | Matrix 精选 - 少数派

---

如何在一小时内给你的整个生活加密 | Matrix 精选
============================

[Steve-Mr](http://matrix.sspai.com/user/647229)

11月19日

**

[**
21](http://sspai.com/36200#list-comment)

**
18

![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/92F9D1C3-BC73-45E5-9C28-9A5FDC65D3B9.jpg)

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/69CA90E6-D0A2-43E9-866C-48B961B2A797.png)](http://sspai.com/attachment/origin/2016/08/15/342459.png?origin)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章对标题和排版略作修改，[原文链接](http://matrix.sspai.com/p/d418e000)。

---

本文翻译自 [Quincy Larson](https://medium.freecodecamp.com/@quincylarson?source=post_header_lockup) 在 [Medium](http://sspai.com/tag/medium) 发表的文章 [How to encrypt your entire life in less than an hour](https://medium.freecodecamp.com/tor-signal-and-beyond-a-law-abiding-citizens-guide-to-privacy-1a593f2104c3#.1uc0aqj42)，建议有一定英语水平的读者直接阅读原文。此文章由 [@WayneMaa](http://matrix.sspai.com/user/690829) 同学在 2016 年 11 月 14 日的[湾区日报](http://sspai.com/tag/%E6%B9%BE%E5%8C%BA%E6%97%A5%E6%8A%A5)（第 758 期）中发现。

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/EFECFA2C-D5E3-441B-A119-BBB7971ABBCD.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/d36ff162baefdfe0d39add7ccefacbf656af7_mw_800_wm_1_wmp_3.jpg)这是 Federico Uribe 于 2012 年使用电缆在帆布上创作的作品「与过去连接」。

> “
>
> *「只有被迫害妄想症才能生存。」——Andy Grove*
>
> ”

Andy Grove 是一个从共产主义（译者注：这里的「共产主义」指当时匈牙利存在的苏联红色恐怖统治。）中逃离的匈牙利难民，随后他学习了工程学，并最终作为英特尔的首席执行官引领了个人电脑革命。他与帕金森病进行了长时间的斗争，在今年的早些时候在硅谷去世。

当世界上最有影响力的人之一建议我们去做一个被迫害妄想症患者时，或许我们应该听取。

而且在具有影响力的人中，并不是只有 Grove 一个劝我们谨慎，甚至 FBI 的局长——就是那个最近向黑客支付一百万美元以求破解一个持枪杀人者的 iPhone 的部门——都在[鼓励人们挡住他们的网络摄像头](http://thehill.com/policy/national-security/295933-fbi-director-cover-up-your-webcam)。

但你遵守法律。你又有什么可担心的呢？正如英国情报监视项目提醒我们的，「如果你没有什么可隐瞒的，那你也没有什么可害怕的。」

> “
>
> *「如果谁给我由最诚实的人画的六条线，我也能从中找出一些东西并借此把他绞死。」——黎塞留, 1641*
>
> ”

在这篇文章中，我会告诉你如何利用最先进的加密技术来保护自己。 **通过一次设置，你可以朝着让你的隐私不受危害的目标迈出一大步。**

适用于所有人的安全观
----------

首先说清楚，我所推荐的所有东西都是完全免费且合法的。如果你不为要在晚上锁门而感到困扰，那么你也不应该对于加密感到困扰。

> “
>
> *「做好准备。」——童军铭言*
>
> ”

让我们准备开始吧。

首先做一些解释。当我使用「攻击者」这个词时，我指的是任何未经许可而想要访问你的数据的人——不管那是黑客，还是一家公司，或是政府。

并且当我使用「私人」或「安全」这样的字眼时，我都指的是在合理的程度上。事实上，只要是由人设计的系统，都不是绝对私密或者绝对安全的。

只要你的手机、电脑和账户被充分保护，其中存储的内容将会保持一种「加密模块」的状态，并且任何人，无论他们多么有能力，都无法获取。

Tip #1：启用邮箱的两步验证
----------------

你的收件箱是进入你的生活的万能钥匙。如果一个攻击者掌握了你的邮箱，他们不但能阅读你的邮件，而且能重置你的许多服务的密码。这些服务包括你的社交媒体账号甚至是你的银行账户。

能让你的个人安全有一个巨大的提升的最简单的办法就是打开你的邮箱的两步验证。

一般来说，两步验证是在你登陆时保护账户安全的第二道屏障。不管你在什么时候登陆，它一般都会需要你接收一个包含一段特殊代码的信息。

两步验证极大地降低了你的邮箱被入侵的可能性。

如果你使用 Gmail，你应该[开启两步验证](https://myaccount.google.com/security#signin)。

现在就去。

我是认真的。

你回来时，我还会在这儿。

译者注：在当下的网络环境中，应该尽可能的打开各个账户的两步验证（如果提供的话）。同时这里给出 [Apple ID 的两步验证开启教程](https://support.apple.com/zh-cn/HT204152)。

Tip #2：加密你的硬盘
-------------

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/3119D30D-CDCA-4149-86C8-8C05DC8B1351.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/72c6d3cde76c9a457dcc414beca6229856af8_mw_800_wm_1_wmp_3.jpg)

[Windows](https://support.microsoft.com/zh-cn/instantanswers/e7d75dd2-29c2-16ac-f03d-20cfdf54202f/turn-on-device-encryption) 和 [macOS](https://support.apple.com/zh-cn/HT204837) 都有内建的硬盘加密。你只需要打开它。（译者注：BitLocker 仅在 Windows 专业版中提供。）

Tip #3：打开你的手机的密码保护
------------------

指纹识别比没有保护要好，但是只有它往往不够。

第五修正案（针对不能自证其罪）允许你去保密你的密码。但是法院可以强迫你用指纹解锁你的手机。

同样，当攻击者抓着你的手指的时候，你不能完全地更改你的指纹。

在你的手机彻底锁定之前，一个攻击者通常会尝试输入十次密码。所以如果你的四位密码出现在了下面的这些组合中，去改掉它。

> “
>
> 1234 9999
>
> 1111 3333
>
> 0000 5555
>
> 1212 6666
>
> 7777 1122
>
> 1004 1313
>
> 2000 8888
>
> 4444 4321
>
> 2222 2001
>
> 6969 1010
>
> ”

**更多的建议**：如果你坚持为了方便而使用指纹识别，一旦被逮捕，请立即将手机关机。这样当警方打开你的手机时，没有密码他们就无法解锁你的手机。

译者注：手机的四位解锁密码极不建议设置为自己的生日。

Tip #4：为每个不同的服务设置独立的密码
----------------------

密码本质上[是不安全的](https://medium.freecodecamp.com/360-million-reasons-to-destroy-all-passwords-9a100b2b5001)。

马克·扎克伯格把他的 [LinkedIn](https://www.linkedin.com/) 密码设置成了「dadada」。今年早些时候黑客释出了 11.7 亿邮箱密码组合，他的密码也在其中。于是黑客们接下来才能利用他的邮箱和密码来获取他的 [Twitter](https://twitter.com/) 和 [Pinterest](https://www.pinterest.com/) 账户的访问权限。

所以不要在不同的地方使用相同的密码。

当然，记住大量的密码是件麻烦事，所以不妨用一个[密码管理软件](https://en.wikipedia.org/wiki/Password_manager)。

译者注：有关密码管理软件，译者在用的是 [LastPass](http://sspai.com/tag/lastpass)，也是在看完这篇文章之后下定决心更换了所有经常使用的平台的账户密码。

同时 还有另外一款极为优秀的密码管理 App：[1Password](http://sspai.com/tag/1password). 其介绍及上手文章在这里：[iOS](http://sspai.com/26877)，[Android](http://sspai.com/28736)，[Mac](http://sspai.com/35195).

以上提及的密码管理 App 都有良好的全平台支持。

**拓展阅读：**

[全平台通吃：顶级密码管理工具 LastPass 评测（内有福利）](http://sspai.com/26418)

[是时候在 iPhone 上忘掉密码了：1Password 5.0 for iOS 上手完全指南](http://sspai.com/26877)

[填充密码比 iOS 版还方便：1Password for Android 新版体验](http://sspai.com/28736)

[1Password for Mac 使用指南](http://sspai.com/35195)

Tip #5： 使用 Signal 来发送私密信息
-------------------------

Signal 是一个广受欢迎的通讯服务，在[电子前哨基金会](https://www.eff.org/node/82654)的测试中得到了满分的成绩。所有你通过普通的信息能完成的事情都可以通过它来完成，诸如群发消息、发送照片和视频等。并且，Signal 上的一切都是被加密的。

Signal 是一个免费、开源，同时在 [iOS App Store](https://itunes.apple.com/cn/app/signal-private-messenger/id874139669?mt=8&uo=4&at=10lJSw) 和 [Google Play Store](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) 中提供的 App。我可以在短时间内把它设置好，从而安全地与我的朋友和家人通信。

#### **第一步：下载 Signal**

### 

#### 第二步：邀请朋友们下载

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/2E7DAF03-B134-4676-9E34-4541E01EF0BA.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/24d52d4de3c75dcf7e58431fc17b399c56afa_mw_800_wm_1_wmp_3.jpg)

#### 第三步：开始聊天

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/957F0A4D-A8F9-466A-B70C-E9D6FC25651B.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/f776719e9327becc1cdb045e82b8c00156afb_mw_800_wm_1_wmp_3.jpg)

恭喜你——你现在可以与你的朋友和家人谈任何你想谈的东西了，并且监听你的对话已经几乎不可能了。

你也可以用 Signal 来拨打电话以确保不会被监听。

译者注：

1. Signal 的中文名为暗号
2. 目前译者在用的安全性较好的即时通讯类 App 为 [Telegram](http://sspai.com/tag/telegram)，Telegram 的用户体验已经十分良好，功能相对丰富（Stikers 简直欲罢不能）。同时 Telegram 的 Secret Chat 的安全性与 Signal 不相上下，也是一个不错的选择。

Tip #6：浏览器的隐身模式不够私密
-------------------

即使你使用 Chrome 或者 Firefox 的「隐身模式」，这些人也能窥察到你的浏览记录：

* 网络服务提供商

* 你的学校，工作单位或者你上网的地方的网络管理员

* Google 或者是任何一个浏览器的开发商

Internet Explorer, Safari, Opera, 和其他的浏览器也不够私密。

如果你希望进行还算说得过去的网络浏览（没有任何一个系统可以做到 100% 的安全），你应该使用 Tor。

Tip #7：用 Tor 来进行隐身浏览
--------------------

Tor 指的是 「洋葱路由」，用来形容它像洋葱一样一层层的代理来对网络活动进行伪装。它是免费的，开源的并且足够易于使用。

#### 第一步：下载 [Orbot](https://play.google.com/store/apps/details?id=org.torproject.android)

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/07B20C18-FF23-4121-8357-A285DB1A7B27.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/3bb7dd8f92c2367ade57a336cef0a48b56afc_mw_800_wm_1_wmp_3.jpg)

#### 第二步：下载 [Orfox](https://play.google.com/store/apps/details?id=info.guardianproject.orfox) 浏览器

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5A03609C-3EBE-4127-8CBE-5A12475A09A2.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/8df52bbbed9ebcf2a788106de89fa64056afd_mw_800_wm_1_wmp_3.jpg)

第三步：打开 Orbot

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/334CBD26-44DA-4DA9-B08C-11F652E3625F.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/56ee9a5d2d69c5fdae76cf4d3187740156afe_mw_800_wm_1_wmp_3.jpg)

### 第四步：打开 Orfox

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/E59F053C-52B9-4C39-84F5-F290F14ACD21.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/734c543e94f38167c58d7995c6af841856aff_mw_800_wm_1_wmp_3.jpg)

### 第五步：确定 Orbox 和 Orfox 可用

访问 check.torproject.org 来确定以上所有的设置是否成功运行。恭喜——你现在可以淡定地浏览网络了，现在想在网络上追踪到你已经变得很困难了。

Tip #8：进行私密的搜索
--------------

如果 Tor 对你来说不够方便，那么你至少可以用 [DuckDuckGo](https://duckduckgo.com/) 来进行私密搜索。DuckDuckGo 是一个不会去追踪你的搜索引擎。

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/41841497-6861-460F-9610-21DC12BA7EB5.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/1abd7a59b5db2b6596ebf22586c8efb256b00_mw_800_wm_1_wmp_3.jpg)

DuckDuckGo 没有像 Google 那样的数以千计的工程师来投入大量的精力，但是当你需要使用 Google 时，它有一个快捷方式来使用加密的 Google 搜索。你只需要在你搜索的内容前加上 !google。

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/CD63F682-3A12-4A0A-842B-902E53E56EF1.jpg)](http://cdn.sspai.com/attachment/thumbnail/2016/11/17/1e7c2d5eea2f8d28f57d82946262601356b01_mw_800_wm_1_wmp_3.jpg)

如果你想要学习更多关于密码学和信息安全的知识，不妨看看这本具有深度又易于理解的书：[Cybersecurity and Cyberwar: What Everyone Needs to Know](https://www.amazon.com/Cybersecurity-Cyberwar-Everyone-Needs-Know/dp/0199918112/ref=sr_1_1?s=books&ie=UTF8&qid=1479358828&sr=1-1&keywords=Cybersecurity+and+Cyberwar%3A+What+Everyone+Needs+to+Know)

（目前尚未找到该书的中文译本，所给出的为美亚链接）

感谢你阅读这篇隐私保护指南。

由于译者最近刚刚玩了 Replica，因此对于「安全」这个问题感到更加无奈，事实上在现在的信息时代，我们的隐私已经形同虚设，我们现在能做的也就只有尽可能的保护它。同时分享一个吐槽：这样的方式足够安全，但是同样会有一个问题 ：「单单是因为这样的保密措施，我们就有理由怀疑并逮捕你。」

本文由 @SteveMeng 翻译，@WayneMaa 校对并提出修改意见。顺带这篇译文会发到由两个智障同学建的一个博客：[LAN](https://lannotwan.wordpress.com/)，欢迎各位莅临指导。

* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/6F5ED13A-3662-46AA-84A3-0C4884483E8D.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:iPhone7/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fshop%2Fbuy-iphone%2Fiphone-7)

原作者：
[Steve-Mr](http://matrix.sspai.com/p/d418e000)

文章来源：
[少数派 Matrix](http://matrix.sspai.com/p/d418e000)

**本文为转载，版权归原作者所有。

* [** Matrix 精选](http://sspai.com/tag/Matrix%20%E7%B2%BE%E9%80%89 "查看所有关于 Matrix 精选 的文章")
* [** 技巧](http://sspai.com/tag/%E6%8A%80%E5%B7%A7 "查看所有关于 技巧 的文章")
* [** 教程](http://sspai.com/tag/%E6%95%99%E7%A8%8B "查看所有关于 教程 的文章")
* [** 观点](http://sspai.com/tag/%E8%A7%82%E7%82%B9 "查看所有关于 观点 的文章")

[**

18](http://sspai.com/36200#)

* [](http://sspai.com/36200#)
* **

* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/79F79D81-872F-4DBF-BDD6-E96406CA90B9.jpg)](http://matrix.sspai.com/user/716266)
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/CD74E10B-7BF3-4FB2-892A-29B36E772338.jpg)](http://matrix.sspai.com/user/718649)
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/67CDB386-F189-4FDC-A915-CF7B8BDDD44A.jpg)](http://matrix.sspai.com/user/259815)
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/A3F55ADB-3EE9-4910-B05D-64591FCF41EB.jpg)](http://matrix.sspai.com/user/723241)
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/4C49646F-445F-40C9-A659-E469BA4E65CD.jpg)](http://matrix.sspai.com/user/725481)
* **

[![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/F379829B-CBA1-4351-896B-04FD2990EF7C.jpg)](http://matrix.sspai.com/user/647229)

[Steve-Mr](http://matrix.sspai.com/user/647229)
**
[** 查看Ta的文章](http://matrix.sspai.com/user/647229)

* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/9D4957AA-EB98-4404-8FA3-0495B33DEE59.gif)

  iPic + Typora，方便快捷地在 Markdown 中插图 | 一日一技](http://sspai.com/36275 "iPic + Typora，方便快捷地在 Markdown 中插图 | 一日一技")
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/6D0D732D-F86E-4318-ACB7-B64C3D44A3E2.jpg)

  利用 Charles Proxy 下载旧版本 iOS App | Matrix 精选](http://sspai.com/36171 "利用 Charles Proxy 下载旧版本 iOS App | Matrix 精选")
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/980EB65D-9EA4-41FC-B973-4F6FECDF42F6.jpg)

  没有新款 MacBook Pro，也能让你体验炫酷的 Touch Bar | Matrix 精选](http://sspai.com/36077 "没有新款 MacBook Pro，也能让你体验炫酷的 Touch Bar | Matrix 精选")
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/789D727E-F007-4011-90AA-83882DEFDE6F.jpg)

  macOS 内录从工具到实战 | Matrix 精选](http://sspai.com/36247 "macOS 内录从工具到实战  |  Matrix 精选")
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/D399B405-5395-443D-99DC-B1E0C5768711.jpg)

  ICONA，人人都可以设计极简 Logo | Matrix 精选](http://sspai.com/36029 "ICONA，人人都可以设计极简 Logo | Matrix 精选")
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/4B49FE10-FBB9-448C-B687-256400647350.jpg)

  关闭 macOS 的 Universal Clipboard 剪贴板同步功能 | 一日一技 · Mac](http://sspai.com/35909 "关闭 macOS 的 Universal Clipboard 剪贴板同步功能 | 一日一技 · Mac")

评论 (21)

* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/67CDB386-F189-4FDC-A915-CF7B8BDDD44A.jpg)](http://matrix.sspai.com/user/259815)

  [煮编](http://matrix.sspai.com/user/259815)

  这周刚看了【谍影重重5】，电影里面的社交网络大佬不知道映射的是谁？起步时，为了拿到投资，将用户隐私数据卖给中情局，用于监控目标人物。

  11月21日

  回复

  [](http://sspai.com/36200#)
  0
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/75F00E5C-4E43-4715-9F45-543BABA6476A.jpg)](http://matrix.sspai.com/user/726409)

  [Aquamarine](http://matrix.sspai.com/user/726409)

  IM类软件无解，这不是由个人可以决定的。

  11月20日

  回复

  [](http://sspai.com/36200#)
  0

  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/21D076C2-7D55-40CB-B9F0-D3AA1DED4B36.jpg)](http://matrix.sspai.com/user/647229)

    [Steve-Mr](http://matrix.sspai.com/user/647229)

    这个的确，目前为止我的关系链很大一部分都在腾讯系的产品上，所以想完全转移基本不可能，但是我和一位关系很好的朋友（就是文中提到的负责校对的 WayneMaa ）现在已经基本上只使用 Telegram 聊天了，我想说的其实就是如果你恰好有一个也关注有关科技方面的好友，也愿意来尝试一个不论是使用体验还是安全性都很高的 IM，那不妨和原先使用的 IM 同时使用。

    11月20日

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5D05F206-33D6-4722-A9EA-D3936E328D0F.jpg)](http://matrix.sspai.com/user/712423)

    [星宇](http://matrix.sspai.com/user/712423)
    回复 [Steve-Mr](http://matrix.sspai.com/user/647229)

    我就想用whatsapp，周围都没人用= =

    11月21日

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/21D076C2-7D55-40CB-B9F0-D3AA1DED4B36.jpg)](http://matrix.sspai.com/user/647229)

    [Steve-Mr](http://matrix.sspai.com/user/647229)
    回复 [星宇](http://matrix.sspai.com/user/712423)

    没有用过 Whatsapp, 或许可以试试结交一些国外友人？[二哈]

    11月21日

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5D05F206-33D6-4722-A9EA-D3936E328D0F.jpg)](http://matrix.sspai.com/user/726409)

    [Aquamarine](http://matrix.sspai.com/user/726409)
    回复 [星宇](http://matrix.sspai.com/user/712423)

    这个比Telegram更小众吧？

    11月21日

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5D05F206-33D6-4722-A9EA-D3936E328D0F.jpg)](http://matrix.sspai.com/user/726409)

    [Aquamarine](http://matrix.sspai.com/user/726409)
    回复 [Steve-Mr](http://matrix.sspai.com/user/647229)

    无奈绝大多数现实的联系都靠T家的，但我本人很喜欢Telegram，也一直在用，只是能够交流的人实在有限，而且都不是固定的。

    11月21日

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5D05F206-33D6-4722-A9EA-D3936E328D0F.jpg)](http://matrix.sspai.com/user/712423)

    [星宇](http://matrix.sspai.com/user/712423)
    回复 [Aquamarine](http://matrix.sspai.com/user/726409)

    布吉岛= =

    2天前

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5D05F206-33D6-4722-A9EA-D3936E328D0F.jpg)](http://matrix.sspai.com/user/712423)

    [星宇](http://matrix.sspai.com/user/712423)
    回复 [Steve-Mr](http://matrix.sspai.com/user/647229)

    鸟语不达标= =

    2天前

    回复

    **
    0
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/403544C2-9D1A-4A78-9FD4-57896E6F38D0.jpg)](http://matrix.sspai.com/user/734172)

  [闪亮](http://matrix.sspai.com/user/734172)

  曾经手贱在黑苹果设置中打开了filevault，然后。。。。。。试过的兄弟们都知道的

  11月20日

  回复

  [](http://sspai.com/36200#)
  0

  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/51FC9D1F-C6B2-4B69-9B49-C9BF82804190.jpg)](http://matrix.sspai.com/user/725941)

    [Ricky1964](http://matrix.sspai.com/user/725941)

    啥意思

    11月21日

    回复

    **
    0
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/E71B619D-3107-47B1-8FC6-3A8655EFBC4F.jpg)](http://matrix.sspai.com/user/718971)

    [ChenReason](http://matrix.sspai.com/user/718971)
    回复 [Ricky1964](http://matrix.sspai.com/user/725941)

    N个特别 慢

    11月21日

    回复

    **
    0
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/3CA66B3E-FED0-4116-B993-D7325FC2E278.jpg)](http://matrix.sspai.com/user/727178)

  [fisherlow](http://matrix.sspai.com/user/727178)

  想问问作者除了看大家的评价之外还有什么方法去判断一个IM的加密程度如何？

  11月19日

  回复

  [](http://sspai.com/36200#)
  0

  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/21D076C2-7D55-40CB-B9F0-D3AA1DED4B36.jpg)](http://matrix.sspai.com/user/647229)

    [Steve-Mr](http://matrix.sspai.com/user/647229)

    这个在文章中「电子前哨基金会」的链接里有一个对于比较主流的 IM 的加密或是安全程度的打分比较，可以看看，这个是链接 [eff.org/node/82654](https://www.eff.org/node/82654)

    11月19日

    回复

    **
    2
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/3CA66B3E-FED0-4116-B993-D7325FC2E278.jpg)](http://matrix.sspai.com/user/727178)

    [fisherlow](http://matrix.sspai.com/user/727178)
    回复 [Steve-Mr](http://matrix.sspai.com/user/647229)

    学习了。非常感谢

    11月20日

    回复

    **
    0
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/75F00E5C-4E43-4715-9F45-543BABA6476A.jpg)](http://matrix.sspai.com/user/711974)

  [oldladdy](http://matrix.sspai.com/user/711974)

  im没得选，要翻墙只能自己用

  11月19日

  回复

  [](http://sspai.com/36200#)
  0
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/4E2345CB-2287-439A-8B19-283B97811B64.jpg)](http://matrix.sspai.com/user/727128)

  [宇宇](http://matrix.sspai.com/user/727128)

  之前也做过类似的尝试，但放弃了。使用体验非常不好，例如使用Tor来浏览，速度超级慢，而且设置什么的很麻烦，用signal发消息那还要对方也用，并不是所有人都有“妄想迫害症”啊……当然密码管理什么的还是很有必要的。

  11月19日

  回复

  [](http://sspai.com/36200#)
  1

  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/21D076C2-7D55-40CB-B9F0-D3AA1DED4B36.jpg)](http://matrix.sspai.com/user/647229)

    [Steve-Mr](http://matrix.sspai.com/user/647229)

    「被迫害妄想症」这个算是一个夸张吧，主要还是至少知道怎么保护自己的隐私吧，算是一个选项吧

    11月19日

    回复

    **
    1
* [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/7E04CC14-BAAE-4FB2-9920-D6A771280C1E.jpg)](http://matrix.sspai.com/user/700912)

  [shamrol- weibo](http://matrix.sspai.com/user/700912)

  可惜国内基本没人用telegram..感觉也没什么意义

  11月19日

  回复

  [](http://sspai.com/36200#)
  0

  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/7AC60E76-01CA-4EF1-A56B-110F64B14A5D.jpg)](http://matrix.sspai.com/user/712206)

    [铝碳酸镁片](http://matrix.sspai.com/user/712206)

    是“国内基本没熟悉的人用telegram”，用电报的人还是蛮多的...

    11月19日

    回复

    **
    1
  + [![](.evernote-content/85427865-30D5-498B-8A61-8E517803072E/5D05F206-33D6-4722-A9EA-D3936E328D0F.jpg)](http://matrix.sspai.com/user/726409)

    [Aquamarine](http://matrix.sspai.com/user/726409)
    回复 [铝碳酸镁片](http://matrix.sspai.com/user/712206)

    转几个中文群组就会发现，就是那些人。

    11月20日

    回复

    **
    0

[微博登录并评论...](http://sspai.com/36200#)

---

[🌐 原始链接](http://sspai.com/36200)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e9b8ce58-952f-4864-a9de-a8391a25e79e/e9b8ce58-952f-4864-a9de-a8391a25e79e/)