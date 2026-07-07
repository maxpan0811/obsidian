---
title: "满血版DeepSeek-R1，五大平台白嫖攻略！ 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/满血版DeepSeek-R1，五大平台白嫖攻略！ 2.md
tags: [evernote, impression, yinxiang]
---

# 满血版DeepSeek-R1，五大平台白嫖攻略！

---

原文链接: [https://mp.weixin.qq.com/s?chksm=b16d1b6e861a927878e5eba1f0ea1e0...](https://mp.weixin.qq.com/s?chksm=b16d1b6e861a927878e5eba1f0ea1e082f1deff47534dc6838ce1a06afde5950717660d464a0&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738510260_4&scene=169&mid=2452242857&sn=a08c99aeb3ac1776c3a5bb99cc1567d9&idx=1&__biz=MjM5MTU0MzIwOA==&sessionid=1738509696&subscene=200&clicktime=1738544530&enterid=1738544530&flutter_pos=38&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQUQTrffdlN23tt1/TcUM8ghLWAQIE97dBBAEAAAAAAMMNKK3uzCcAAAAOpnltbLcz9gKNyK89dVj0sPPvcjpJyMeEtHDpZGexa2spTtvtRaYDoXJLRz5Hqrq+PAGmbCo1Z3ksmaZcZp/XGzs05nc9VFUELdfc+h5aJss3PZmemUwDDhBwLph7JqU1Azt7haUnmXTeQJtHOMN7v1O873emcWBzMeHkebMF2HespAF2XehkEiyMJFadRE+Dn0Fx88koX6yhjMipX3uxYcYGjy36J3a+zzrm4QpIzdAhMxfCfjKh9DFaRat+4YY=&pass_ticket=h79rPyrIZvEA533Ua3PKWyw+HMcvNarpeemeefG4ivLixcGeqBIRj9XYR7Y0jbwE&wx_header=3)

原创 王抖抖 王抖抖

因为访问量过大以及遭受网络攻击，DeepSeek官网和APP这几天时好时坏，API也没法用。

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/EE826920-1B56-4530-BE95-0BD3CDA3EC16.png)

此前我们已分享了本地部署DeepSeek-R1的方法（参见[**DeepSeek-R1本地部署**](https://mp.weixin.qq.com/s?__biz=MjM5MTU0MzIwOA==&mid=2452242802&idx=1&sn=6b51532fa05384e517f236f79f27a715&scene=21#wechat_redirect)），但普通用户限于硬件配置，连70b模型也很难跑起来，更别说671b的全量模型了。

幸好各大平台都接入了DeepSeek-R1，大家可以尝试作为平替。

---

**一、英伟达NIM微服务**

网址：  
https://build.nvidia.com/deepseek-ai/deepseek-r1

英伟达部署了全量参数671B的DeepSeek-R1模型，网页版直接使用，点进去就能看到聊天窗口：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/09E04F0D-E400-4CE9-A919-2BD263BA7F06.png)

同时右侧也列出了代码页：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/A1FC0EA2-15A3-4ECF-8AEC-045A387CE0A2.png)

简单测试一下：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/EE9F15CE-D6DB-45AB-94FD-F863F0A6B96B.png)

聊天框下方，还可以开启一些参数项（多数情况下可默认）：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/09E23EE2-9E47-471E-AFE8-765A79D5FBB6.png)

这些选项的大概意思和功能如下：

*Temperature（温度）：  
数值越高，输出更随机，可能生成更具创造性的回答*

*Top P（核采样）：  
数值越高，保留更多概率质量的token，生成更具多样性*

*Frequency Penalty（词频惩罚）：  
数值越高，越多地惩罚高频词，减少啰嗦或重复*

*Presence Penalty（出现惩罚）：  
数值越高，越倾向于让模型尝试新词*

*Max Tokens（最大生成长度）：  
数值越高，回答潜在的篇幅越长*

*Stop（停止条件）：  
生成到某些特定字符或序列时，停止输出，防止生成过长或跑题*

目前，由于白嫖的人越来越多（看下图的排队人数），NIM部分时段会出现卡顿：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/B2D1F7CC-50BE-4367-8C3A-4964D5A5D552.png)

难道英伟达也缺显卡？

NIM微服务还支持API调用DeepSeek-R1，但你需要用邮箱注册账号：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/FAFE5D2A-6E5A-4AFA-A36A-3C6AD430D90B.png)

注册过程比较简单，只用邮箱验证：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/95FB0360-3CC0-4E6F-9F7E-4E1877F88437.png)

注册好之后，可以点击聊天界面右上方的“Build with this NIM”生成API KEY，目前注册就送1000点数（互动1000次），白嫖党可以用完再换个新邮箱再注册。

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/6A1B1E69-2245-41E3-9914-B7D8119B1695.png)

NIM微服务平台也提供其他许多模型的使用：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/8E966B13-8F63-45CC-8EC5-45C53A7162C9.png)

---

**二、微软Azure**

网址：  
https://ai.azure.com

微软Azure可以通过聊天操场，创建一个聊天机器人，并与模型交互。

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/1521E18B-1F79-4447-8FE1-935E485093D0.jpg)

Azure的注册麻烦许多，首先你要创建一个微软账户（如果已经有了就直接登录）：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/057E35D9-8268-4BB1-AFE3-FCCB784F7C2B.jpg)

创建账户也需要邮箱验证：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/36B08A8B-421F-4F88-8885-6D6AB71F7911.jpg)

完了要证明自己是人类，连续回答10道阴间问题：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/6F4AF98F-DC33-4145-89F6-41BBD0901F07.jpg)

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/B95BD6E4-D102-4F93-85F3-17F2DEF44944.jpg)

到这里还不够，还得创建订阅：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/7BAB7EEB-739D-4321-9E0C-18921060AEF1.jpg)

验证手机号码以及银行账号等信息：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/9F3EEFA6-7F2B-4D52-A03B-0873BCF5B1E4.jpg)

接下来选择“无任何技术支援”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/E907410E-5C83-43B5-B7D2-D6C65ED0A239.jpg)

到这里就可以开始云部署了，在“模型目录”可以看到显眼的DeepSeek-R1模型：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/3550E0ED-F173-4DEA-A66B-43CA172BEB21.jpg)

点击之后，在下一个页面点击“部署”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/59CAD67B-5C2E-4A99-A5F0-096D7A01F423.jpg)

接下来要选择“创建新项目”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/EAC7EDB5-94E0-441D-89ED-0EF1CE54681A.jpg)

然后全部默认，点击“下一个”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/B8F70F2D-BA93-4110-A8B9-A7E4ED8A41DF.jpg)

接下来点击“创建”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/19130A96-CDFA-4386-A84D-FD1F2F67532E.jpg)

在这个页面下创建就开始了，需要等待一段时间：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/D57CDC27-23E1-4C9A-AB5E-E3A05CA6F658.jpg)

完成后来到这个页面，你可以点击“部署”，进入下一步：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/E5B0B13E-9CAE-460B-8757-6B71584F33AB.jpg)

也可以查看上方面的“定价和条款”，可以看到是免费使用：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/ED6C0F9D-A843-4891-A8D5-BF8F08B3B583.jpg)

继续点击“部署”进入这个页面，可以点击“在操场中打开”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/655220EB-4F2B-44F7-BA74-459282E637BC.jpg)

然后就可以开始对话：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/9AB451ED-DD62-40E8-B831-5D6A7C090237.jpg)

Azure也有类似NIM的参数调节可选：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/68FF9C52-E40A-4591-BD24-B9602BB3935E.png)

作为平台，有许多模型可以部署：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/2B04453E-49AA-4EC7-A824-E1B0291B2199.png)

对于已经部署的模型，今后通过左边菜单的“操场”或“模型+终结点”就可以快速访问：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/C3C25180-7D70-485A-AB46-E291BC900BD4.png)

---

**三、亚马逊AWS**

网址：  
https://aws.amazon.com/cn/blogs/aws/deepseek-r1-models-now-available-on-aws

DeepSeek-R1同样在显眼位置，排面。

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/3BB1DA1E-6B0B-468A-97CA-178E71EE09E7.png)

亚马逊AWS注册过程和微软Azure差不多麻烦，都要填写付款方式，还要电话验证+语音验证，这里就不再详细描述：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/666D1705-707B-4A4B-B625-76ADB8F4AAEA.png)

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/A5720595-B91F-4DC3-B42C-E19CA6EED5EC.png)

具体部署过程和微软Azure也是大同小异：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/18EF5514-B5A3-4F3C-924C-727645E7622F.png)

---

**四、Cerebras（需科学上网）**

网址：  
https://cerebras.ai

和几家大型平台不同，Cerebras使用的是70b模型，宣称“比GPU方案快57倍”：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/17370C3D-87E4-4ED5-BFEC-999AC97B04CD.png)

邮箱注册进入后，上方的下拉菜单可以选择DeepSeek-R1：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/BF013080-B02B-40B4-890A-4A5286590384.png)

实测速度确实比较快，虽然没有宣称的夸张：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/61631E46-30DC-41A8-9052-061BEA81609B.png)

---

**五、Groq（需科学上网）**

网址：  
https://groq.com/groqcloud-makes-deepseek-r1-distill-llama-70b-available

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/3A1BF4B2-A2B3-4B0F-9133-91C98C00E015.png)

邮箱注册进入后，也是可以选择模型：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/032175BB-7C82-4B38-AC4C-775E2A978896.png)

速度也很快，但同样是70b，感觉比Cerebras的要弱智一点？

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/30EC724C-7B7C-4E6F-9412-1B38DBD00353.png)

注意，登录状态下可以直接访问聊天界面：  
https://console.groq.com/playground?model=deepseek-r1-distill-llama-70b

希望大家玩得开心，也希望DeepSeek早日恢复正常！

---

这是本公众号第六十六篇推文，今后将长期分享AI聊天、AI绘画、AI资讯，欢迎大家交流！

也可长按下方图片，关注我在其它社交网站的帐号：

![](.evernote-content/E5BF46D1-FE86-41BB-8C73-6F781323AC68/FFD52DD0-3DDE-451D-9ABB-4A73658CBBAB.jpg)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=b16d1b6e861a927878e5eba1f0ea1e082f1deff47534dc6838ce1a06afde5950717660d464a0&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738510260_4&scene=169&mid=2452242857&sn=a08c99aeb3ac1776c3a5bb99cc1567d9&idx=1&__biz=MjM5MTU0MzIwOA==&sessionid=1738509696&subscene=200&clicktime=1738544530&enterid=1738544530&flutter_pos=38&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQUQTrffdlN23tt1/TcUM8ghLWAQIE97dBBAEAAAAAAMMNKK3uzCcAAAAOpnltbLcz9gKNyK89dVj0sPPvcjpJyMeEtHDpZGexa2spTtvtRaYDoXJLRz5Hqrq+PAGmbCo1Z3ksmaZcZp/XGzs05nc9VFUELdfc+h5aJss3PZmemUwDDhBwLph7JqU1Azt7haUnmXTeQJtHOMN7v1O873emcWBzMeHkebMF2HespAF2XehkEiyMJFadRE+Dn0Fx88koX6yhjMipX3uxYcYGjy36J3a+zzrm4QpIzdAhMxfCfjKh9DFaRat+4YY=&pass_ticket=h79rPyrIZvEA533Ua3PKWyw+HMcvNarpeemeefG4ivLixcGeqBIRj9XYR7Y0jbwE&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2dc5b7a8-1752-4623-aa55-77ffc7d41a74/2dc5b7a8-1752-4623-aa55-77ffc7d41a74/)
