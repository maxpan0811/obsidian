---
title: Alfred真正的大杀器：Workflows_领客专栏·Pinapps
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Alfred真正的大杀器：Workflows_领客专栏·Pinapps.md
tags: [印象笔记]
---

# Alfred真正的大杀器：Workflows|领客专栏·Pinapps

---

Alfred 真正的大杀器：Workflows | 领客专栏·Pinapps
--------------------------------------

*2015-03-26*
*精品应用尽在*
appsolution
appsolution

**appsolution**
![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/E0DC8F69-CA4B-4168-AE05-C80CEB2C6E65.sgml)

appsolution

专注于推荐新酷精华应用。主打 iOS/Android 平台，是国内最早、用户最多的 App 推荐认证公众号。支持自定义菜单及机器人查询。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/DAE2EA20-9F5D-4DBC-B86C-39662E9B83E8.png)

感谢大家上周对「如何用 Alfred 大幅提升搜索效率」的支持，我们这期接着聊。

接下来介绍一下 Workflows，这也是 Alfred 升级 V2 的核心功能。

相对于 Workflows，前面提到的自定义搜索只是小儿科了。Alfred 允许用户通过脚本语言来控制 OS X 及其平台上的各类第三方应用。V2 推出的时候，好多程序员朋友们都异常激动。而对于像我们这样的普通用户来说，你就当它是一个超级插件中心吧。

首先，它长下面这个样子。左边都是我添加过的各种 Workflows。利用它们我们能做些什么呢？还是举一些我在使用的 Workflows 做例子吧。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/250B271F-A3B0-44E6-AFFA-F3B4D5204260.jpg)

在我使用的 Workflows 中大概分为按需个性需求类和功能类。前者大部分都是按照自己的需要来配置，后者更多是从论坛中找来针对某些应用功能的扩展。

首先我们先来看看 Workflows 能提供些什么。由于我不是开发，所以只能从普通用户的角度出发来介绍一下。

简单来说，在 Alfred 应用自身当中它提供了触发、执行、反馈这样一条操作链路。在这条链路中我们可以「任意」设置来帮助我们完成一系列的操作。

以下方这个「Cod」操作为例。通过它能够帮助快速进入开发模式，激活后输入关键词「cod」，Alfred 将帮我把 Xampp、Espresso、LiveReload、调试页面全部激活，打开本地开发环境来折腾下我的网站。执行完成后给我返回一个通知，告诉我所有事件执行完成。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/A26FC944-C3E5-45FE-8659-9F7744E483EE.jpg)

**首先，是操作的触发方式。**

Workflows 提供了非常多的选择。你可以通过快捷键、关键词、甚至是 Alfred 新近发布的 iOS 应用 Remote 来进行触发。

**然后，是触发后执行的操作。**

通过右上角的加号可以添加三个应用的打开、URL 在 Chrome 中的激活。在这里 Workflows 可以做以下操作，如果懂开发你会发现 Workflows 可以帮你干非常多的活，只要你能想到。

* Open file
* Reveal File in Finder
* Browse in Alfred
* Launch Apps / Files
* Default Web Search
* Open URL
* System Command
* iTunes Command
* Run Script
* Run NSAppleScript
* Terminal Command

**最后，输出。**

我增加了一条输出通知来告诉我所有的工作已经准备好。除此之外 Workflows 还可以输出到剪贴板或者再次激活允许 Script。在所有的节点建立完成后，记得要将它们连起来。这样才能保证他们能一步步的运作起来。

比如为了让开机速度更快，我去掉了所有的默认启动项，单独建立了一条命令来激活所有需要开机启动的应用。「Cod」这个激活、打开应用的链路其实能解决我们很多问题，大家完全可以去自己尝试着配置以下，慢慢你就能搭建出适合自己的 Workflows 了。

除了关键词之外，Workflows 同样支持快捷键做激活。比如我就用「Command + E」来激活 Finder。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/C9D6CDDD-58A6-4404-977A-5BA14CA4D9DF.jpg)

接下来要说说功能类的 Workflows 了。这部分大多都是针对一些应用的功能增强，主要目的还是补足原有应用功能上的不足、提升操作效率。

比如我曾经在 Pinapps 中推荐过的屏幕休眠管理应用 Caffeine，每次想要激活它只有去顶部菜单栏里找，有时眼神不好得瞅半天。有了这个小插件，只需要激活 Alfred 输入 caf（可自行定义）就搞定了。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/7DA320C5-0F3E-4D10-9A59-9B6AC10133AA.jpg)

是不是有点意思了？接着往下看看我平时常用的 Workflows：

**Dianping**

点评搜索。其实我们上周介绍的自定义搜索功能中也能达到类似功效，而 Workflows 的好处就是能够及时的回传数据显示。比如我想找海底捞，输入「dp 海底捞」选择我想去的分店回车就可以在浏览器中打开该餐馆的介绍详情页面了。这比自定义搜索更加方便，需要注意的是有些网站提供的数据接口速度较慢，建议还是使用自定义搜索。比如 App Store。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/29F08293-565B-46D5-954C-102B304129C6.jpg)

**Dropbox Toggler**

Dropbox 同步开关。和前面提到的 Caffeine 一样。不用去顶部菜单栏找瞎了。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/9ABCC7AC-8BD8-4E93-81FC-5EFAFC1B74F1.jpg)  
**Fantastical**

Fantastical 的语义化输入，添加事件也可以在这里搞定。同样不用去顶部菜单栏找瞎了。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/1633C5C2-943C-426E-881D-32BA7CF31ECA.jpg)  
**GoagentX**

GoagentX 的快捷开关，各位懂的。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/4C897A10-DF8D-4DB3-A299-52798330BC86.jpg)  
**iMessage**

iMessage 快速启动，输入名字或者手机号进入 iMessage 对话框。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/7839B2DD-1766-4A8E-8939-EEA39F33B884.jpg)  
**Kill Process**

快速杀掉进程，这是个好东西。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/010AF695-8C92-454B-AC52-5D710BA2ECE9.jpg)  
**Mail.app Search**

Mail 邮箱的快速搜索，找邮件不用再打开邮箱了。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/3ABE68BE-A595-4277-A0D4-DBA46BF21E6B.jpg)  
**App Store**

Mac App Store 和 App Store 搜索。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/B62E9B73-211B-4508-8CB5-618433FE1A6B.jpg)  
**Open in Dropshelf**

还记得曾经给大家介绍过的 Dropshelf 吗？选择文件进行快捷键操作，当前文件就会暂存到 Dropshelf 中了。省去了拖拽的操作。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/422E22AE-4AAA-420F-AC4F-E58A97963ED4.jpg)  
**Open URL in…**

将 URL 在指定浏览器中打开，前端同学们最爱。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/B5E884EB-F121-450C-B18B-EE11ACDE412E.jpg)  
**PinAdd**

如果你是 Pinboard 的用户，这个功能你不能错过。关键词激活后可以直接将当前浏览器中当前 tab 收藏到 Pinboard 中。空格再加关键词为 URL 打 tag。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/4FAA0CCD-BACA-4CD6-832F-27DF3023EC4D.jpg)  
**Transmit ftp**

Transmit 是我常用的 FTP 工具，关键词输入后可以选择 ftp 直接连接。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/2C789E2F-D700-466A-B4D1-CE09BD43B679.jpg)  
**Tweetbot**

Tweetbot 快捷入口

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/1657C5D8-11D4-4D12-BD71-C606C2E833A7.jpg)  
**Wi-Fi 开关**

在这里可以直接打开或关闭 Wi-Fi，同时你也可以查看到目前所处 Wi-Fi 情况。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/6600C5F6-364F-417B-88DB-64D597F91A85.jpg)  
**有道翻译**

直接输入后翻译。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/BCDC1BBE-5206-4AC4-9E78-C86DDF487A3B.jpg)  
**About This Mac**

关于本机信息，想不起来也不用去点小苹果了。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/C1FE3DC2-BC42-4033-BE43-9A6114EF746B.jpg)

以上就是从我常用的 Workflows 中精选出来的一些，相信已经基本能说清楚 Workflows 的强大之处了。任何一个操作都可以帮我们至少省下十秒的时间。

如果你想要获得更多 Workflows，有两个办法。要么你使用「想要增强的 app 名称 + Workflow(s)」去搜索引擎里找；或者登陆 Alfred 官方论坛的 Workflows 版块找寻自己喜欢的东西。

下面是我使用 Alfred 的一些数据：从 2.0 发布到现在我已经使用了 5w 多次，平均一天 74 次。其实正常的工作日基本都是快 200 次的样子了，可见现在我是多么地依赖它。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/6938C146-54A6-44F7-90C6-68DD36C35F07.jpg)

1.0 版本的 Alfred 已经让人爱不释手，2.0 版本增加 Workflows 更是让我就毫不犹豫地购买了终生账户。甚至还给老妈的电脑买了 Family License，节日的时候给团队同学送礼物也是 Alfred Powerpack（使用 Workflows 需要购买 Powerpack 服务）。

像此类能大幅提升效率的工具非常值得大家付费购买，毕竟现在时间可比金钱贵多了。你甚至可以和身边的朋友合买 Family Licenses，这样也会更加的合算。这个「坑」不会入错！

OK，关于 Alfred 的介绍结尾了。我只是从一个使用者的角度给大家分享了一下为什么值得买，Alfred 真正厉害的东西我还远没有摸透。我倒是很想找一位开发同学来从技术角度再来介绍一下 Alfred，不知是否有人接档呢？

最后，也欢迎大家关注我开设的公众号「Pinapps」，我会在这里给大家推荐一些有态度的 iOS/Mac 应用。

![](.evernote-content/FE88D4A4-727D-480E-B240-66FA8827C463/9ED1686F-3FB4-4F3E-8D25-8C34A7FEEF9B.jpg)

阅读原文

阅读

  
举报

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=205434919&idx=1&sn=ccc211a88d3c1be5ee19f7acb45e7e3a&scene=1#rd)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&amp;mid=205434919&amp;idx=1&amp;sn=ccc211a88d3c1be5ee19f7acb45e7e3a&amp;scene=1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/cdf3beaa-10af-41d0-89cf-53b74d7f984a/cdf3beaa-10af-41d0-89cf-53b74d7f984a/)
