---
title: "Karpathy 说 Claude Tag 是 LLM 交互的第三种范式"
type: source
created: 2026-06-28
updated: 2026-06-28
source_path: 印象笔记管理工具/Karpathy 说 Claude Tag 是 LLM 交互的第三种范式.md
tags: [evernote, impression]
---
---
title: "Karpathy 说 Claude Tag 是 LLM 交互的第三种范式"
source: evernote
type: note
export_date: 2026-06-28
guid: 7da4b5e6-f350-4fa5-9739-c71530dacb74
---

# Karpathy 说 Claude Tag 是 LLM 交互的第三种范式

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI2NTI4MDczMA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzI2NTI4MDczMA==&mid=2247490144&idx=1&sn=89e65b3173086e71dcd9f141d08132ca&chksm=eb61155b4a9cd7832f4fbe9c58c08905368865898143acfac070acee3fe2309bcbcbbca9fd0c&scene=90&xtrack=1&req_id=1782308689420484&sessionid=1782304295&subscene=93&clicktime=1782313795&enterid=1782313795&flutter_pos=26&biz_enter_id=4&ranksessionid=1782308689&jumppath=20020_1782308697536,1104_1782308698184,20020_1782308701857,1104_1782313774806&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQjYUb7K6fUOn2QvrKefNT1BLOAQIE97dBBAEAAAAAAIEpKL7r8KQAAAAOpnltbLcz9gKNyK89dVj0tKJjIXyuC9r0dLZ6esd0Z/FcX4HYDPFM5F24mCV5liPJA/nz4lo65XZ8OcFPZNlNDMfwnQ8ZnrLVcVIODNbiz1k9XlenVGOt9AvENcqayGwjpwqfTgEmoC7ykIZieizDkR08LVy+m1kcmUINbfIUn6NpdxPTnUA0wnSt9CD5FNqcTrVKpfLCDpfhqRNxeJu+BCXbA8X2mRIL5SytB0XD3mR7PEFzQl7C&pass_ticket=nEQyXJW5QyLfeOVzaj+khlRsOns4yckHQDj7el7WQoPoFGInTGf3a6DoRW4+zn7H&wx_header=3)

OriginalPeng Peng的AI日常

昨天，Anthropic 官宣发布 Claude Tag，“Claude 可以作为一个团队成员加入你的 Slack 工作区”，并且“频道里任何人 @Claude，就能把活派给它”。

产品负责人 Cat Wu 说：Claude Code 团队全年都在用 Claude Tag 内部交付。现在产品团队 65% 的代码由它产出，包括 Claude Tag 自身的大部分代码也是它写的。

Karpathy 给出如下评论，而且评价着实不低：

Imo this is the 3rd major redesign of LLM UIUX. The first paradigm was that the LLM is a website you go to, the second was that it is an app you download to your computer. This third one is that it is a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans.

在我看来，这是 LLM 用户界面和用户体验的第三次重大重新设计。第一种范式是 LLM 是一个你访问的网站，第二种是它是一个你下载到电脑上的应用。这种第三种范式是它是一个自包含的、持久的、异步的实体，拥有全组织的工具和上下文，与人类团队并肩工作。

## 第一种范式的例子，比如 ChatGPT，第二种我理解指的是 Claude Code 或者 Codex 这种 Agent 产品，那 Claude Tag 真得称得上是第三种吗？

## Claude Code 能做什么？

Claude Code 创始人 Boris 说：我每天 @Claude 好多次：写 PR、处理用户反馈、排查事故、做数据分析、总结信息等等。把它当成公司的搜索引擎用。"X 项目什么状态？""这个服务谁负责？"它直接给你答案，不是甩一堆链接。

**一个例子**

|  |  |
| --- | --- |
|  |  |

不是 IM 机器人

Boris 说：在 Slack 里 @Claude，它就在频道里跟你一起干活。主动、多人协作、有自己的身份和记忆。但它不只是个 Slack 机器人。

为什么？Claude Tag 和 IM 聊天机器人有啥不同？

### 懂协作：一个频道里就一个 Claude，像同事一样跟大家配合，随时能接上对话。

### 会学习：它会持续留意频道里的对话，慢慢摸清背景，不用你每次都从头解释。

### 干活主动：能主动推送你可能需要的消息，还会跟进那些沉了没人管的任务。

### 知道如何干活：给它派个活，它就能自己进行规划，安排时间，独立把项目推下去。

## 应用场景

既然 Cladue Tag 在 Claude 内容已经运行了很久，是经过实践验证的，那么，它的应用场景有哪些呢？

Cat Wu 总结了内部使用 Claude Tag 的六种场景：

**事故响应**

告警一响，Claude 进事故线程。拉图表、diff 部署、回来时根因和责任人已经 @ 出来了。团队在线程里确认。Claude 开 fix、合进去、盯指标恢复、关闭告警。

**Bug 分诊**

把 Claude 放在反馈频道里，自动捡 bug 报告。它找到对应代码路径、复现、git blame 定位作者、写 fix、@ owner。剩下的事只有 code review，然后 Claude 自己合 PR。

被阻塞的活

把那些卡在别人身上的工作丢给 Claude，比如等后端上线后对接前端。它会等着、盯着，几天后带着 PR 回来，review 过程中的变动它自己适配好了。

线程变复盘

事故收尾时 @Claude 写复盘。它回溯整个线程、重建时间线、把 postmortem 写进文档、action items 开成 issue。

后台盯梢

给 Claude 设阈值，不用盯面板。比如 CI 红太久就通知。平时不出声，阈值一过自动发消息，附带失败测试和 culprit commit。让它直接从同一个线程里出 fix。

帮你盯上线和指标

把 Claude 指向一个 A/B 测试，告诉它指标和 guardrail。guardrail 一波动它就报警，团队中途修正，结果显著时它带着 rollout PR 回来通知你。

### tips

**怎么给 Claude Tag 派活？**

在任何 Claude 所在的频道里 @ 它，不用装任何东西。

**Claude Tag 擅长干什么？**

编码、数据、事故、GTM 等场景。

**怎么拿到好结果？**

界定任务范围和 review 产出的好习惯。

**Claude Tag 记住了什么？**

频道记忆、工作区共享内容、谁能看到什么。

**Claude Tag 能定时跑任务吗？**

定时任务、频道盯梢、触发器。

一张图总结

![](attachments/38823737f3f8a4ba.png)

参考：Anthropic 官网Claude Tag 官方文档
