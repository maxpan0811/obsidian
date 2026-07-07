---
title: 飞书出了个 CLI，我把它接进自己的 Agent，然后就回不去了
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/飞书出了个 CLI，我把它接进自己的 Agent，然后就回不去了.md
tags: [evernote, impression, yinxiang]
---

# 飞书出了个 CLI，我把它接进自己的 Agent，然后就回不去了

---

原文链接: [https://mp.weixin.qq.com/s?chksm=ce94c6bbf9e34fadc30e5e939e302f1...](https://mp.weixin.qq.com/s?chksm=ce94c6bbf9e34fadc30e5e939e302f1fcabe4f086b6a29343cc62dc754442c458e6fa1309781&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1775184109_1&req_id=1775173458256492&scene=169&mid=2247484005&sn=de06dc3c83e5ef615c2a965da2433144&idx=1&__biz=Mzg2OTkzMDQxNw==&sessionid=1775182832&subscene=200&clicktime=1775184156&enterid=1775184156&flutter_pos=88&biz_enter_id=5&jumppath=20020_1775184077221,1104_1775184083072,20020_1775184118901,1104_1775184148521&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=1800462d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQGJg6kDo0xEq2MGsXvQAX+hLTAQIE97dBBAEAAAAAAMKoAhIfFKYAAAAOpnltbLcz9gKNyK89dVj0SlAz0tX4/pjeDF0A3ezadLEZLZLzvpxnRD8nzzWfLlurh5tczA8UUaY+DgHs/OFWa9PxCy52Ta8UlQ7xGco5W0JHmoahxWk530KeOF5J8fzdB3n56cvomAIShXnAaH36INApKkS9cIoVRijXm88PbTedLi7T8sSdZXpJbkdpNOxGbTn27TQeeoeE5i8EfnvBTY5N0CSHO39fa3NuAGpJcfaVeoKLzOwWYjhiuT8=&pass_ticket=Xw9OmyaleWfCI6za8LpD61jv9t9T7ggUGRRTG/znV8LAo/6W0s2I5iApEAOKsWS7&wx_header=3)

OriginalPanda CheckPanda Check

---

飞书今天开源了一套 CLI 工具，专门为 Agent 设计。

装上之后，任何智能体都能直接调用飞书的功能——日历、文档、消息、多维表格，全部通过命令行接口控制。我把它接进了自己的个人 Agent，测了一下午。

接入之后，我让她做了几件事。查下周日程，建一个看电影的日历提醒，搜索我过去写的十几篇文档分析写作风格，顺手生成一份《写作风格指南》，最后根据这份指南加我的语音口述，把这篇文章的草稿起出来。

每个任务，一句话。

不需要打开飞书 App，不需要在对话框和文档之间来回跳。说"帮我查下周日程"，她就查了。说"帮我建个文档"，她就建了。第一次需要浏览器授权，之后全自动。

---

**单条操作只是热身**

上面说的这些，其实只是在证明链路跑得通。

真正有意思的是批量操作。在 GUI 里，你只能一个一个点——建一篇文档点一次，发一条消息点一次，改一个格式点一次，费时费力。Agent 加 CLI 完全不一样。写个循环，一百篇文档一口气建完。多维表格几百条记录批量更新，几秒钟的事。给二十个内部群同时发通知，一句话。

这类任务的效率提升，保守说是十倍起步。

还能组合其他能力一起跑。批量抓网页、批量生图、批量处理数据，跟飞书 CLI 串在一个流程里，变成一条完整的自动化链路。

单条操作证明能跑通，批量才是 CLI 真正给 Agent 的武器。

---

**飞书在做一件比工具更大的事**

飞书这次选择 MIT 开源，不只是开个接口。它在重新定义自己对用户的理解。

过去企业软件的设计逻辑，是让人用起来顺手——界面直观，点击流程短，减少人的学习成本。现在这个逻辑开始动摇了。

日程、审批、文档、项目管理，这些原本由人来发起、人来操作的业务流程，Agent 现在全都能接管。而且速度更快，出错率更低，完全不依赖界面。

软件公司迟早要想清楚一个问题——你的客户到底是谁？如果答案还是只有人类用户，你会发现越来越多的操作根本不经过你的 UI 了。

飞书出 CLI，是把自己从人与人之间的协作工具，往人与 Agent 之间的协作基础设施方向转。用户友好和 Agent 友好，两件事，飞书在同时做。

---

**企业 AI 的真实战场就在这里**

我之前写过一个判断——SaaS 的主人正在从人类变成 Agent。

很多人觉得这个说法有点夸张，但飞书 CLI 出来之后，这件事变得非常具体了。你不需要想象一个遥远的未来，今天就能把日历、文档、消息这些每天真实在跑的业务流程，交给 Agent 去管。

企业里推 AI，最难落地的往往是模型够强了，却没有地方接。飞书 CLI 补上的正是这块——给 Agent 一个插头，往企业协作软件里一插，能用的东西一下子多了一大块。

而且还是 MIT 开源，现有能力满足不了，自己提 PR 来扩。

你现在的 Agent，能接哪些内部系统？

那个答案，可能比模型本身更决定它实际能帮上多少忙。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=ce94c6bbf9e34fadc30e5e939e302f1fcabe4f086b6a29343cc62dc754442c458e6fa1309781&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1775184109_1&req_id=1775173458256492&scene=169&mid=2247484005&sn=de06dc3c83e5ef615c2a965da2433144&idx=1&__biz=Mzg2OTkzMDQxNw==&sessionid=1775182832&subscene=200&clicktime=1775184156&enterid=1775184156&flutter_pos=88&biz_enter_id=5&jumppath=20020_1775184077221,1104_1775184083072,20020_1775184118901,1104_1775184148521&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=1800462d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQGJg6kDo0xEq2MGsXvQAX+hLTAQIE97dBBAEAAAAAAMKoAhIfFKYAAAAOpnltbLcz9gKNyK89dVj0SlAz0tX4/pjeDF0A3ezadLEZLZLzvpxnRD8nzzWfLlurh5tczA8UUaY+DgHs/OFWa9PxCy52Ta8UlQ7xGco5W0JHmoahxWk530KeOF5J8fzdB3n56cvomAIShXnAaH36INApKkS9cIoVRijXm88PbTedLi7T8sSdZXpJbkdpNOxGbTn27TQeeoeE5i8EfnvBTY5N0CSHO39fa3NuAGpJcfaVeoKLzOwWYjhiuT8=&pass_ticket=Xw9OmyaleWfCI6za8LpD61jv9t9T7ggUGRRTG/znV8LAo/6W0s2I5iApEAOKsWS7&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a9887764-b4c4-4829-8dff-1b5b41d44758/a9887764-b4c4-4829-8dff-1b5b41d44758/)
