---
title: "告别封号! 人人可用的顶级Claude AI桌面端"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/告别封号! 人人可用的顶级Claude AI桌面端.md
tags: [evernote, impression, yinxiang]
---

# 告别封号! 人人可用的顶级Claude AI桌面端

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515881&idx=1&sn=5488b36de687b07bc5b92ad47c9de418&chksm=e9c0af269a57584c4a752235a30245337e5ba54691b0d68593654002348fbe20e7e2087feafb&scene=90&xtrack=1&req_id=1777513215489681&sessionid=1777513035&subscene=93&clicktime=1777513328&enterid=1777513328&flutter_pos=3&biz_enter_id=4&ranksessionid=1777513215&jumppath=WAWebViewController_1777513305455,WAWebViewController_1777513305930,20020_1777513318480,1104_1777513320096&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=1800472d&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVUxfMr8rhH/Mxvj+03gzEBLVAQIE97dBBAEAAAAAAED4D/cwtSoAAAAOpnltbLcz9gKNyK89dVj0JsVbhSKOfZ3v+DulB4udrhOg9iiyiryN2ZdHOV+OzpD+Q1n6AfpvMqmi+22t4EwyuHjPRHKhDGQMAayflPv0eMIfcpcLr5sTX22pRNHXwS9vf1yR2aYXjLP50yUlgp3OixPtzdf/dfqyGtoJmC4Go/TrSQyojoYC1rLYL9sGS75c7JyEGSbHMqgO3NaJph8eIJUexCPxU7lI7TVuQAkFtFwusVa+Ft8KFERgLIKz7g==&pass_ticket=jSjZZA3Rs4LzP97kO8+cu2ZnzauXi7PP+7KiFikewjcsxFDLGuRCQ9SFNytqoONt&wx_header=3)

Original字节笔记本 字节笔记本

相信大家都已经领取了小米发的Token大礼包[小米的MiMo 100 万亿 Token 如何免费申请？](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515862&idx=2&sn=67a9541ef4221a42ffd1631b81a447ee&scene=21#wechat_redirect)

我昨天又使用上面的方式申请到了16亿的Token额度。

。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/21D8D04B-7135-40EB-A55F-4D9C524B2F55.jpg)

小米的额度申请完成之后，强烈建议在Claude Desktop上面来使用，真的太好用了。

上次分享的[太好用了！在Claude Code Desktop 中使用第三方API的最新保姆级教程](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515780&idx=1&sn=697703ee16351f82c3ca8922e8cdef0f&scene=21#wechat_redirect)是Mac的安装方式，这次单独出一个Windows版本的。

上次的评论区有很多人留言说无法联网正常下载客户端，所以我将Mac和Windows的安装包下载下来，可以直接进行下载使用，安装包下载地址：

https://link.bytenote.net/VFjhyS

下载完成后，按照Windows普通软件的方式点击安装 。

来到Claude Desktop的初始界面。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/DB4936BA-4BE9-4859-A089-9926D0F79C78.png)

这个时候不要点击Get Started登录，点击左上角的菜单栏图标。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/995A9AD2-0664-4797-8D14-6ED6393D6E72.png)

依次点击  Help  Troubleshooting  Enable Developer Mode这三个选项，开启开发者模式。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/96CB01E7-386C-4DD2-9B8F-ABB072F11956.png)

Claude Desktop会弹出警告窗口，警告界面选择 Enable，桌面端会自动进行重启。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/4A267172-A02A-4387-B9EE-75C3D07AEE16.png)

还是原来的菜单路径，选择Developer Configure Third-Party Inference

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/0EE7361C-B732-402A-A98C-BE96BF1872C2.png)

Connection下的Gateway就可以填入第三方的接口

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/916459C3-009C-4BBF-97DB-F377AFB265B3.png)

来到小米的后台管理界面

https://platform.xiaomimimo.com/console/plan-manage

我们需要获取三样东西：

第一个是请求的地址。

需要选择兼容 Anthropic 接口协议的请求端口。

https://token-plan-ams.xiaomimimo.com/anthropic

第二个是请求的密钥。

API Key 仅在创建时可见可复制，请妥善保存，不要与他人共享你的 API Key，或将其暴露在浏览器或其他客户端代码中。

第三个是模型名称：

mimo-v2.5-pro

获取后填入到前面的Gateway界面中，具体长这样。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/477E7C4D-48F8-4A6E-B684-522082800E80.png)

填写成功后点击 Apply locally，客户端会自动重启并应用生效。

如果一切顺利就可以正常的对话了，和在命令使用Claude Code没有任务区别。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/AAB62387-03F2-456D-ABD1-A71F1CD59AD6.png)

相较于的黑漆漆的命令行，Claude Desktop的最大的优势是结构清晰，GUI的交互更加的友好。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/71D6D11E-7BA2-48AA-A68D-E67489D4A454.png)

很多在命令行无法表达的东西，比如端到端的测试截图都可以在对话内容中完整的显示。

桌面端提供了可视化的Skill和Plugin的操作，用来管理Skill更加的直观和方便。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/1FFA91FB-16E0-4855-BD1A-3558087D1D23.png)

可以直接通过Desktop提供的三种方式来创建上传使用Skill，比手动管理快捷太多了。

![](.evernote-content/00970AD7-5B1D-4003-B73A-43663E9D2761/D3BEDC21-116F-4D74-8B42-1E9E274A9FE6.png)

Claude Desktop采用了和Claude Code命令行完全一致的内核，对新手极其的友好，也可以更加方便地管理我们日常的对话内容，GUI也对CLI更加的直观好用。

接入廉价的国产模型之后不用操心网络和封号的问题，更多的发挥出Claude Code实用价值。

更多关于Claude Desktop的详细使用教程，可以关注一下字节笔记本星球的近期推送。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515881&idx=1&sn=5488b36de687b07bc5b92ad47c9de418&chksm=e9c0af269a57584c4a752235a30245337e5ba54691b0d68593654002348fbe20e7e2087feafb&scene=90&xtrack=1&req_id=1777513215489681&sessionid=1777513035&subscene=93&clicktime=1777513328&enterid=1777513328&flutter_pos=3&biz_enter_id=4&ranksessionid=1777513215&jumppath=WAWebViewController_1777513305455,WAWebViewController_1777513305930,20020_1777513318480,1104_1777513320096&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=1800472d&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVUxfMr8rhH/Mxvj+03gzEBLVAQIE97dBBAEAAAAAAED4D/cwtSoAAAAOpnltbLcz9gKNyK89dVj0JsVbhSKOfZ3v+DulB4udrhOg9iiyiryN2ZdHOV+OzpD+Q1n6AfpvMqmi+22t4EwyuHjPRHKhDGQMAayflPv0eMIfcpcLr5sTX22pRNHXwS9vf1yR2aYXjLP50yUlgp3OixPtzdf/dfqyGtoJmC4Go/TrSQyojoYC1rLYL9sGS75c7JyEGSbHMqgO3NaJph8eIJUexCPxU7lI7TVuQAkFtFwusVa+Ft8KFERgLIKz7g==&pass_ticket=jSjZZA3Rs4LzP97kO8+cu2ZnzauXi7PP+7KiFikewjcsxFDLGuRCQ9SFNytqoONt&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7a9d6932-cd48-4c25-b742-fd0f73b95aaa/7a9d6932-cd48-4c25-b742-fd0f73b95aaa/)
