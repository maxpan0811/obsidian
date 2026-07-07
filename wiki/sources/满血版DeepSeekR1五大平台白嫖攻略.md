---
title: 满血版DeepSeek-R1，五大平台白嫖攻略！
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/满血版DeepSeek-R1，五大平台白嫖攻略！.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "满血版DeepSeek-R1，五大平台白嫖攻略！"
source: evernote
type: note
export_date: 2026-06-27
guid: 2dc5b7a8-1752-4623-aa55-77ffc7d41a74
---

# 满血版DeepSeek-R1，五大平台白嫖攻略！

原文链接: [https://mp.weixin.qq.com/s?chksm=b16d1b6e861a927878e5eba1f0ea1e0...](https://mp.weixin.qq.com/s?chksm=b16d1b6e861a927878e5eba1f0ea1e082f1deff47534dc6838ce1a06afde5950717660d464a0&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738510260_4&scene=169&mid=2452242857&sn=a08c99aeb3ac1776c3a5bb99cc1567d9&idx=1&__biz=MjM5MTU0MzIwOA==&sessionid=1738509696&subscene=200&clicktime=1738544530&enterid=1738544530&flutter_pos=38&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQUQTrffdlN23tt1/TcUM8ghLWAQIE97dBBAEAAAAAAMMNKK3uzCcAAAAOpnltbLcz9gKNyK89dVj0sPPvcjpJyMeEtHDpZGexa2spTtvtRaYDoXJLRz5Hqrq+PAGmbCo1Z3ksmaZcZp/XGzs05nc9VFUELdfc+h5aJss3PZmemUwDDhBwLph7JqU1Azt7haUnmXTeQJtHOMN7v1O873emcWBzMeHkebMF2HespAF2XehkEiyMJFadRE+Dn0Fx88koX6yhjMipX3uxYcYGjy36J3a+zzrm4QpIzdAhMxfCfjKh9DFaRat+4YY=&pass_ticket=h79rPyrIZvEA533Ua3PKWyw+HMcvNarpeemeefG4ivLixcGeqBIRj9XYR7Y0jbwE&wx_header=3)

原创 王抖抖 王抖抖

因为访问量过大以及遭受网络攻击，DeepSeek官网和APP这几天时好时坏，API也没法用。

![](attachments/861ac5ffa90e1efb.png)

此前我们已分享了本地部署DeepSeek-R1的方法（参见[**DeepSeek-R1本地部署**](https://mp.weixin.qq.com/s?__biz=MjM5MTU0MzIwOA==&mid=2452242802&idx=1&sn=6b51532fa05384e517f236f79f27a715&scene=21#wechat_redirect)），但普通用户限于硬件配置，连70b模型也很难跑起来，更别说671b的全量模型了。

幸好各大平台都接入了DeepSeek-R1，大家可以尝试作为平替。

---

**一、英伟达NIM微服务**

网址：  
https://build.nvidia.com/deepseek-ai/deepseek-r1

英伟达部署了全量参数671B的DeepSeek-R1模型，网页版直接使用，点进去就能看到聊天窗口：

![](attachments/da6bdce95fdb48d7.png)

同时右侧也列出了代码页：

![](attachments/e62b7eea1061f79b.png)

简单测试一下：

![](attachments/e03bdbca30394e74.png)

聊天框下方，还可以开启一些参数项（多数情况下可默认）：

![](attachments/433d62eaa67aed1c.png)

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

![](attachments/deb45a48d1a9e30b.png)

难道英伟达也缺显卡？

NIM微服务还支持API调用DeepSeek-R1，但你需要用邮箱注册账号：

![](attachments/39afa044ef6d6532.png)

注册过程比较简单，只用邮箱验证：

![](attachments/c7b2daf7dd52fd8a.png)

注册好之后，可以点击聊天界面右上方的“Build with this NIM”生成API KEY，目前注册就送1000点数（互动1000次），白嫖党可以用完再换个新邮箱再注册。

![](attachments/50914215bfe950f1.png)

NIM微服务平台也提供其他许多模型的使用：

![](attachments/900dacb01953ec0e.png)

---

**二、微软Azure**

网址：  
https://ai.azure.com

微软Azure可以通过聊天操场，创建一个聊天机器人，并与模型交互。

![](attachments/d18b06a5d6b82868.jpg)

Azure的注册麻烦许多，首先你要创建一个微软账户（如果已经有了就直接登录）：

![](attachments/367fd60aac5c4179.jpg)

创建账户也需要邮箱验证：

![](attachments/ec058df7e40542bb.jpg)

完了要证明自己是人类，连续回答10道阴间问题：

![](attachments/96899e4a28647957.jpg)

![](attachments/9eb1c4c70336ad1f.jpg)

到这里还不够，还得创建订阅：

![](attachments/deb67e9f1e53b2e1.jpg)

验证手机号码以及银行账号等信息：

![](attachments/7e2acc4e9a63d8be.jpg)

接下来选择“无任何技术支援”：

![](attachments/24c6b7110581e7c3.jpg)

到这里就可以开始云部署了，在“模型目录”可以看到显眼的DeepSeek-R1模型：

![](attachments/523a3536dfc47006.jpg)

点击之后，在下一个页面点击“部署”：

![](attachments/c0e5dfde2f191cb4.jpg)

接下来要选择“创建新项目”：

![](attachments/5ffc3c140103b497.jpg)

然后全部默认，点击“下一个”：

![](attachments/1dd121404c1396c4.jpg)

接下来点击“创建”：

![](attachments/e6f289bec5946629.jpg)

在这个页面下创建就开始了，需要等待一段时间：

![](attachments/78b4cbc69db2644e.jpg)

完成后来到这个页面，你可以点击“部署”，进入下一步：

![](attachments/a4b07c9970f22812.jpg)

也可以查看上方面的“定价和条款”，可以看到是免费使用：

![](attachments/7769f895c530b75d.jpg)

继续点击“部署”进入这个页面，可以点击“在操场中打开”：

![](attachments/f46859aa5b027611.jpg)

然后就可以开始对话：

![](attachments/cc839829c9d2fbfe.jpg)

Azure也有类似NIM的参数调节可选：

![](attachments/c70ba84d61eb8ba2.png)

作为平台，有许多模型可以部署：

![](attachments/7abdd3c4a9bcd188.png)

对于已经部署的模型，今后通过左边菜单的“操场”或“模型+终结点”就可以快速访问：

![](attachments/c4453b3477f49b4a.png)

---

**三、亚马逊AWS**

网址：  
https://aws.amazon.com/cn/blogs/aws/deepseek-r1-models-now-available-on-aws

DeepSeek-R1同样在显眼位置，排面。

![](attachments/02bc706282ea195d.png)

亚马逊AWS注册过程和微软Azure差不多麻烦，都要填写付款方式，还要电话验证+语音验证，这里就不再详细描述：

![](attachments/7dcb440e02954e55.png)

![](attachments/2ff594cfd38270fd.png)

具体部署过程和微软Azure也是大同小异：

![](attachments/d773d1eb86501aba.png)

---

**四、Cerebras（需科学上网）**

网址：  
https://cerebras.ai

和几家大型平台不同，Cerebras使用的是70b模型，宣称“比GPU方案快57倍”：

![](attachments/d66573acd8e79b32.png)

邮箱注册进入后，上方的下拉菜单可以选择DeepSeek-R1：

![](attachments/7e6809d399064c49.png)

实测速度确实比较快，虽然没有宣称的夸张：

![](attachments/5ff2f1369124ff5b.png)

---

**五、Groq（需科学上网）**

网址：  
https://groq.com/groqcloud-makes-deepseek-r1-distill-llama-70b-available

![](attachments/1c925a93e8791643.png)

邮箱注册进入后，也是可以选择模型：

![](attachments/dbb8044457573026.png)

速度也很快，但同样是70b，感觉比Cerebras的要弱智一点？

![](attachments/df9013307780dd55.png)

注意，登录状态下可以直接访问聊天界面：  
https://console.groq.com/playground?model=deepseek-r1-distill-llama-70b

希望大家玩得开心，也希望DeepSeek早日恢复正常！

---

这是本公众号第六十六篇推文，今后将长期分享AI聊天、AI绘画、AI资讯，欢迎大家交流！

也可长按下方图片，关注我在其它社交网站的帐号：

![](attachments/e5e520df133f651c.jpg)
