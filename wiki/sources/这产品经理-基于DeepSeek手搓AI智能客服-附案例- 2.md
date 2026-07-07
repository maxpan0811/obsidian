---
title: 这产品经理：基于DeepSeek手搓AI智能客服（附案例） 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/这产品经理：基于DeepSeek手搓AI智能客服（附案例） 2.md
tags: [evernote, impression, yinxiang]
---

# 这产品经理：基于DeepSeek手搓AI智能客服（附案例）

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIxMzM1ODA2NA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzIxMzM1ODA2NA==&mid=2247487225&idx=1&sn=0163e678fbd94325724d91ab23e13e18&chksm=9680e0820e6bde4d0c36c2571d7ab1227a1f210c9d2853ad14d8a2ba4caa84d95d1327e6eafd&mpshare=1&scene=1&srcid=022429Pfrb5VRdKzqYjU6h34&sharer_shareinfo=982702e611776a46e5fb99e569ea7954&sharer_shareinfo_first=982702e611776a46e5fb99e569ea7954&from=groupmessage&isappinstalled=0&clicktime=1740386992&enterid=1740386992&ascene=1&devicetype=iOS18.3.1&version=18003833&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQCdtCwNy/L4t8PQURDrV/RRLsAQIE97dBBAEAAAAAAEuOFG6j9ZEAAAAOpnltbLcz9gKNyK89dVj0hYeA4ySa1hh0w6U3w0hNTYZoglfkTz7DuC1onpzulAPYBU2q5E/DGULKNs59ft7vKIdp22SW/zRKkXuMPK+zE1mj4zzsHYxRnxOolg3oQQRO2aHvrpkQiXD6OswDWAIesmAuBLN2NjdiXvGGs2NZghpaEMFbf7uL0IGN+ojbg29ER9N0lPDNkzEFgrpWT/d1D9+nwBaeAd1BuByRZcNxfEUYkIqSEdPKF3MuHfy6M5B6x2/rbgkAyTJ0+HliVNrkuUDV7u7w&pass_ticket=sM06spzbeCkKs5Eqt7v2ieo5WSalPc/gdwNmpHKNGjc7zve/vJAvyiWCPW1oZFBo&wx_header=3)

这产品经理：基于DeepSeek手搓AI智能客服（附案例）
=============================

原创道叁鄙人道三

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/7FD0BAF5-9369-4D07-AA97-BDB8591F55BE.png)

智能客服想必大家并不陌生吧，一个可以007且全年无休的任劳任怨的牛马！

你也不曾想过自己有一天也能手搓、调教一个AI智能客服！

对于非技术人员，想要搭建一个AI智能客服，想都不敢想；那你们接着往下文看，不仅敢想，而且还想动手，等着老板给你升职加薪吧。

首先，本文会从以下几个方面进行介绍如何手搓AI智能客服

● 介绍coze（使用里面的DeepSeek模型）；

● AI智能客服工作流搭建过程；

● 如何应用落地（技术可行性分析）；

1.  介绍coze

coze（中文名称：扣子）是一个 AI 应用开发平台，字节跳动旗下的AI产品。coze提供了友好的可视化设计和编排工具，无论你是否具备编程能力，都可以通过低代码方式拖拖拽拽，然后基于自己业务或者需求快速搭建出基于大模型的各类AI项目；

同时支持将AI 应用发布到各个社交平台、通讯软件，也可以通过 API 或 SDK 将 AI 应用集成到你的业务系统中。

本文介绍的智能客服是采用智能体搭建的，AI大模型采用的是内置DeepSeek模型；

关于coze详细内容在这里不过多介绍，大家可以去官网查看；国内版https://www.coze.cn；国外版https://www.coze.com

两者在大模型是有差异的：国内版主要使用大厂自研的大模型（豆包、deepseek、KIMI等），国外版主要是GPT-4等大模型；

2.  AI智能客服搭建过程

搭建过程大概分为四步骤：创建售前问答库、创建智能库、创建智能体、调试智能体；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/A14EC562-BBCC-4CAF-87E1-712CDD89CC01.png)

2.1 创建售前问答库

首先，通过deepseek.com生成一份SaaS软件售前问答30条，表格展示，表头包含问题、答案、关键词，然后复制到excel上备用；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/3DAFF97C-9B25-49FC-87A8-5FB647D40DDE.png)

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/B641C778-4990-412E-BF72-90630617067D.png)

其次，进入coze后台中工作空间点击+资源后，我们会发现添加资源库支持多种格式，这里上传准备好的售后问答excel即可。

然后傻瓜式下一步下一步就搞定了，下图就是上传成功后的excel中数据；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/FDC289BB-D35D-4AB0-8676-CCEE71C43BC5.png)

2.2 创建智能体

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/318CF95C-A13F-4848-B8B0-96BE496D5434.png)

（AI智能客服工作流）

在创建智能体后，选择单Agent的工作流模式，工作流模式是由多个节点构成的标准化步骤，用来完成特定的任务和达到预期的目标。

通过将复杂的任务拆成多个子任务，可以避免单个模型能力的限制，确保内容输出的准确性，同时整个流程会更加可控。

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/77DA6699-731A-4062-8C46-A79803B97FC6.png)

接下来详细介绍如何搭建AI智能客户工作流的过程

2.2.1 开始节点和结束节点

工作流这两个节点是无删除的，开始节点输入的是客户询问的问题，结束节点是Agent经过deepseek大模型处理后的答案；

2.2.2 意识识别节点

主要用于用户输入的意图识别，并将其与预设意图选项进行匹配。

在实际客服咨询业务过程，会存在大量的与售卖产品问题，为了防止Agent不知所措引入了“意识识别”节点，避免Agent回复一些牛头不对马嘴的答案。

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/F68440F0-AD4F-4B87-992D-1A2DDD273B44.png)

2.2.3 问题处理节点

当意图识别为产品外的问题，通过DeepSeek模型进行智能回答，为了使得回答健康且始终围绕产品本身，需要填写对应的提示词。

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/E8AEA4B5-B7D1-40B4-AC04-5A4A9CE5A7F2.png)

当客户提出产品相关的问题，Agent也需要对问题应进行归纳总结且需要结合上下文，来充分理解用户的问题；这里DeepSeek模型也需要配置相关提示词；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/8F02D36D-C8CB-4214-86E6-8E95AACB303C.png)

2.2.4 知识库节点

将 “2.1创建售前问答库” 步骤创建好的文档，上传到知识库节点中，供Agent读取、调用；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/E130E677-37AF-4F91-9EF5-5BD270F52EF2.png)

2.2.5 回答处理阶段

当Agent根据“2.2.3 问题处理节点”步骤得到处理后的客户问题，就能在知识库中检索对应的回答；

得到答案后，需要通过DeepSeek模型将答案进行修饰再输出给客户；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/9246FD81-29C6-41A2-AA8A-F4CBD6814FF7.png)

2.3 调试AI智能客服

咨询非产品的问题，回答基本上比较靠谱、健康；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/FF309107-CD5F-4878-A58E-0A0B8D49E163.png)

问了两个售前问题（不完全和售前问题一样），智能客服的回答与excel的答案基本符合我们的预期，相当nice！！

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/304D0C42-E192-46FE-87BD-3890CC7039C1.png)

下面是问答库对应的问题，可以对比一下客服的回答差异点，效果还是不错的；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/C3EF790C-484E-40FC-BF9A-4CEB058ACA84.png)

2.4 发布智能体

完成AI智能体可以点击页面右上角“发布”按钮，大家可根据业务情况选择不同的平台，比如抖音、微信的小程序/公众号、api方式等等；

![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/BFDCAC2A-BD8F-4500-ACC0-19279FD90C38.png)

3.如何应用落地或业务中

最近公司官网正在筹备，后期有计划把AI智能客服放到官网；

为了避免让技术调研AI智能客服如何应用到业务中而嗷嗷瞎叫，索性好人做到底帮技术做个可行性验证，这更能体现出你能力价值，够他们仰望半生了![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/7B12613B-6EF1-4AC7-9523-286A27CBAD74.png)![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/7B12613B-6EF1-4AC7-9523-286A27CBAD74.png)![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/7B12613B-6EF1-4AC7-9523-286A27CBAD74.png)。

官方文档：https://www.coze.cn/docs/developer\_guides/chat\_v3#70a1d1bd

接口地址：https://api.coze.cn/v3/chat

在线postman：https://www.sojson.com/http/test.html

```
请求头

Content-Type:"application/json;charset=UTF-8"

Authorization:"Bearer pat_fYhFov*****KO86aE****MbiPbz5MWY"
```

```
请求参数

{

"bot_id": "744235748****337",

"user_id": "111", // 这里可以上传设备ID

"stream": true,

"auto_save_history":true,

"additional_messages":[

{

"role":"user",

"content":"SaaS 软件能解决什么痛点？",

"content_type":"text"

}

]

}
```

```
返回的回答数据，很完美，技术会给你举起大大的👍

event: conversation.message.completeddata: {

"id": "7446483412615217202",

"conversation_id": "7446483406814232585",

"bot_id": "7442357489300963337",

"role": "assistant",

"type": "answer",

"content": "SaaS 软件能解决以下痛点：优化业务流程，通过自动化数据处理减少人工操作失误；提升团队协作效率，打破部门信息壁垒；提供精准数据分析，助力决策制定。",

"content_type": "text",

"chat_id": "7446483406814248969",

"section_id": "7446483406814232585",

"created_at": 1733769528---回答时间戳单位秒

}
```

好了，最后接口调用没问题，证明技术上完全可行，有疑问的可以留咨询![](.evernote-content/48015EE0-92D5-4839-900D-7545493D3619/3EA08EE4-0F7E-4F53-9D1E-C66EA2FCE72A.png)；

最后分享一些关于学习deepseek相关的多篇文档，感兴趣小伙伴可以点击下方链接获取；

DeepSeek从入门到精通.pdf

DeepSeek 7大场景+50大案例+全套提示词+实操案例.pfd

DeepSeek如何赋能职场应用--从提示语技巧到多场景应用.pdf

200条Deepseek润色指令.pdf

个人观点，仅供参考

阅读原文

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIxMzM1ODA2NA==&mid=2247487225&idx=1&sn=0163e678fbd94325724d91ab23e13e18&chksm=9680e0820e6bde4d0c36c2571d7ab1227a1f210c9d2853ad14d8a2ba4caa84d95d1327e6eafd&mpshare=1&scene=1&srcid=022429Pfrb5VRdKzqYjU6h34&sharer_shareinfo=982702e611776a46e5fb99e569ea7954&sharer_shareinfo_first=982702e611776a46e5fb99e569ea7954&from=groupmessage&isappinstalled=0&clicktime=1740386992&enterid=1740386992&ascene=1&devicetype=iOS18.3.1&version=18003833&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQCdtCwNy/L4t8PQURDrV/RRLsAQIE97dBBAEAAAAAAEuOFG6j9ZEAAAAOpnltbLcz9gKNyK89dVj0hYeA4ySa1hh0w6U3w0hNTYZoglfkTz7DuC1onpzulAPYBU2q5E/DGULKNs59ft7vKIdp22SW/zRKkXuMPK+zE1mj4zzsHYxRnxOolg3oQQRO2aHvrpkQiXD6OswDWAIesmAuBLN2NjdiXvGGs2NZghpaEMFbf7uL0IGN+ojbg29ER9N0lPDNkzEFgrpWT/d1D9+nwBaeAd1BuByRZcNxfEUYkIqSEdPKF3MuHfy6M5B6x2/rbgkAyTJ0+HliVNrkuUDV7u7w&pass_ticket=sM06spzbeCkKs5Eqt7v2ieo5WSalPc/gdwNmpHKNGjc7zve/vJAvyiWCPW1oZFBo&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/92cd0310-8993-4d61-b2b2-f3e1a67b506b/92cd0310-8993-4d61-b2b2-f3e1a67b506b/)
