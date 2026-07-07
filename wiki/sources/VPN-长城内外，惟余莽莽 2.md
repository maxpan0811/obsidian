---
title: "VPN-长城内外，惟余莽莽 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/VPN-长城内外，惟余莽莽 2.md
tags: [evernote, impression, yinxiang]
---

# VPN-长城内外，惟余莽莽

---

VPN - 长城内外，惟余莽莽
---------------

*2014-02-18*
MacTalk By 池建强
MacTalk By 池建强

**MacTalk By 池建强**
![](.evernote-content/FA8CEF0C-6897-4568-B828-AEFB52C78203/FDE6BE99-85AE-4CB2-A0CA-51E7F30CCE13.sgml)

sagacity-mac

帐号开通于2012年末，内容起于 Mac 而不止 Mac，讲述技术与人文的故事，释放编程与写作的力量。行文采用了一种技术和人生感悟相结合的风格，文字简单、内容有趣，诸君可各取所需。相关畅销书《MacTalk·人生元编程》。

![](.evernote-content/FA8CEF0C-6897-4568-B828-AEFB52C78203/3516E21E-E7BE-42F7-82E6-20A8C2D8D1BC.jpg)

由于众所周知的原因，VPN 在国内是一个很好的业务服务，据我所知，无数程序员为了访问 Twitter、Facebook 和各种不知名的外国网站，不得不借助 VPN 的力量翻上翻下。

在我春节期间推荐过一次 VPN 服务之后，很多人就反馈，VPN 是好用，挂上之后国外的网站是能访问了，但原来国内正常访问嘻唰唰的网站立刻变得慢吞吞了，怎么破？这是个问题。如果连了 VPN 没做任何设置的话，会导致所有网络都是通过 VPN 访问，缺点有二：  
1、VPN 的流量问题，严重的话还可能导致被 VPN 提供商封杀（比如没事就去下载动作片）。  
2、嘻唰唰变慢吞吞的问题。

我当时的回复是设置一下路由表即可。估计很多朋友没明白是肿么回事，这事就过去了。

今天小道君在朋友圈碎碎念：「使用 VPN 翻越长城的问题在于，启用 VPN 的时候国内网站速度巨慢，而绝大多数人要同时访问国内和国外的服务，这个时候很纠结啊，就好比一个人一会儿脱裤衩，一会儿再穿上，这能舒服么？」

我看到之后，陷入了深深的思考，这个 VPN 已经上升到了裤衩的高度，问题似乎变得有些严重了，所以我决定今天写点什么……

下面就给大家介绍一下如何通过修改路由的方式，让用户在使用 VPN 作为默认网关时，不用 VPN 访问国内网站，减少 VPN 的网络流量消耗，增加国内网站的访问速度，促进人民群众的安定团结，推动社会的长治久安。

为了简单起见，我只讲步骤不讲原理，并只针对 Mac 用户（Windows 用户请找 WinTalk，谢谢）。

1、自行搭建 VPN 服务器或购买 VPN 提供商的服务。  
2、打开系统偏好设置—>网络，增加 VPN 设置，VPN 类型选择PPTP，根据提示设置用户名密码等信息即可。  
3、下载 chnroutes.py，相关网址：https://code.google.com/p/chnroutes/downloads/list  
4、打开终端进入下载文件的目录，执行：python chnroutes.py -p mac，该目录下会生成两个文件「ip-up」和「ip-down」。  
5、把这两个文件复制到 /etc/ppp 下，然后进入该目录执行：sudo chmod a+x ip-up ip-down  
6、没有5了，已经全搞定了。

测试一下，在终端执行：netstat -nr，检查路由表的输出信息。连接 VPN，然后再次执行：netstat -nr，你会发现路由表已经发生了变化。这时再去访问国内的网站，你发现他们又变得嘻唰唰了，同时还能访问 Twitter 和 Facebook！

就到这里，晚安。

点击【阅读原文】，阅读其他操作系统和 VPN 类型的解决方案（不用 Mac 也管哈）。

今日题图：GreatWall，来自National Geographic

阅读原文

阅读

  
举报

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&mid=200062863&idx=1&sn=ecd28282f9d500db4fdb8df39f3726b2&scene=1#rd)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&amp;mid=200062863&amp;idx=1&amp;sn=ecd28282f9d500db4fdb8df39f3726b2&amp;scene=1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/387b345c-2618-44e7-a780-ea5072fd2bec/387b345c-2618-44e7-a780-ea5072fd2bec/)
