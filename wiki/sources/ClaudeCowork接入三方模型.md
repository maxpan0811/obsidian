---
title: Claude Cowork 接入三方模型 3 分钟教程
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=245386...]
source_path: 印象笔记管理工具/必看！3分钟学会Claude Cowork接入三方模型.html
tags: [claude, cowork, third-party-model, knowledge-worker]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "必看！3分钟学会Claude Cowork接入三方模型"
source: evernote
type: note
export_date: 2026-06-24
guid: c696aac0-8e1a-4d37-a6d4-b86543be35d2
---

# 必看！3分钟学会Claude Cowork接入三方模型

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA4NjEwMTQ1NA==&mid=245386...](https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=2453865384&idx=1&sn=e09e40efd1300b42365043c9d5afb500&chksm=8935371dc206546a4c95c46dd888c5c97dfd440fafab3ce7a4f6fe4def1bb3dd1274fffb016a&scene=90&xtrack=1&req_id=1777376805048154&sessionid=1777376981&subscene=93&clicktime=1777377260&enterid=1777377260&flutter_pos=1&biz_enter_id=4&ranksessionid=1777376805&jumppath=20020_1777377192088,1104_1777377195036,20020_1777377198933,1104_1777377246891&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=1800472d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQxsscX8rm4iVZ0rp654rU9hLVAQIE97dBBAEAAAAAAELDATl/hg4AAAAOpnltbLcz9gKNyK89dVj07kUTW9KMf4L98i/sgggEwbas5ZAIU7nJQmlH7PldrFS9KTYd01J7J35Ue9l0kT6b5nysMQ8o34uevz/76qXAGqvgASdyS55GguFYxDBcBUaemp7lW+/ZnTGHzRciQub8u3JgZ1XBJVwtc9tGwL7r/uMp1gkS7/FjlAWySxQoMMRYcoJILgBY21a/IyLPJIKjjxXH3zJewPbJscjA56P44bUllknwulZoIXrmKT09Qw==&pass_ticket=6lCk7JbppnYsBHxbJA4xo231v+EpuEB0YhLMQbVDIgRP300cd4Utcz6yEC6GVgli&wx_header=3)

![](attachments/1fb3d9f804349788.jpg)![](attachments/56d36f764fd16f2d.jpg)![](attachments/99194183c298acb7.jpg)![](attachments/0f31f6d927781196.jpg)![](attachments/757bde0966c589a3.jpg)![](attachments/9a0b2e690d7e64a2.jpg)

作为Anthropic年初推的桌面端Agent，Cowork专门面向不会写代码的知识工作者。授权一个本地文件夹，用大白话告诉它要做什么，它自己读文件、做计划、调用子Agent，最后把成品写回文件夹。

比起命令行的Claude Code，Cowork对普通人友好太多。

Claude Code好歹还能随意接入三方模型使用，但Cowork一直有个门槛：必须用Anthropic自家账号登录才能用。账号注册不上、订阅买不了、或者哪天号没了，这款软件就成了一块砖。

这两天我折腾时无意中发现，Claude桌面版已经悄悄开放了第三方模型支持。我把完整流程踩过一遍，分享下来。

1️⃣ 第一步，打开开发者模式

打开Claude Desktop，登录界面先放着不动。点顶部菜单栏的Help，进Troubleshooting，里面有一个Enable Developer Mode。点它，按提示重启。

重启之后，菜单栏会多出来一个Developer选项。点进去，选Configure Third-Party Inference，配置面板就出来了。

2️⃣ 第二步，填API订阅地址

这里是整个流程最容易踩坑的一步，我也是踩过才搞明白的。

面板里要填三样东西：Gateway类型、Gateway base URL、API Key。

注意Claude客户端只接受Anthropic自家Messages API协议，直接填DeepSeek的官方地址，它会请求一个根本不存在的端点，怎么试都报错。正确做法是中间加一层协议翻译。

3️⃣ 第三步，应用并重启

填好之后点Apply locally，按提示完全退出App再打开（不是关窗口，是Cmd+Q）。

重新启动后，登录界面会被替换成一个新的引导页，选第一个Local配置模式。进去就是Claude Desktop的主界面了，左上角可以切换Cowork和Code两种模式，可选的模型列表里能看到你网关后面接的那些第三方模型。

我自己现在主力已经换成DeepSeek V4的方案了，干起活来真是便宜又好用。

⚠️ 几个真实使用感受

Cowork在隔离虚拟机里跑代码，所有任务都不会动你本地系统的其他东西，文件和网络访问受控。这一点和Claude Code、CodeX直接操作你整台电脑的工具完全不一样，Cowork面向的是没开发背景的人，安全防护是产品基因。

它内置的AskUserQuestion机制也很好用，背景信息不够时会主动给几个选项让你补全上下文。这种知道自己不知道的能力，是普通AI工具最缺的。

🎯 一句话总结

Cowork这种好东西不该被Anthropic账号绑死。A厂自己留了后门让你接别家模型，开关藏得深但是真的有用。会折腾的人永远比规则跑得快一点。

#claude#Cowork#claudecode#AI编程#VibeCoding
