---
title: Claude第5代最强模型Fable 5来了！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Claude第5代最强模型Fable 5来了！ 2.md
tags: [evernote, impression, yinxiang]
---

# Claude第5代最强模型Fable 5来了！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517853&idx=1&sn=55dc9bf9310efaf329213bb44d4d5fd9&chksm=e90cf844573086ae371fcb75906f95fc0931772b6093b0183fcf6d074b838f3a3d8dd9233ca2&scene=90&xtrack=1&req_id=1781048450916100&sessionid=1781048471&subscene=93&clicktime=1781048474&enterid=1781048474&flutter_pos=0&biz_enter_id=4&ranksessionid=1781048451&jumppath=1001_1781048456739,1102_1781048457779,1001_1781048470039,1104_1781048472513&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQV4K9aCOB0GvbbIO2GrC9xRLTAQIE97dBBAEAAAAAAJStEi20epsAAAAOpnltbLcz9gKNyK89dVj0UYULx6sGaivs6wS72RTJ7np7CkuqW/X/HFtJbT/pcYvozndxX2OFpbixlhkn+0w0cv+rb8miCS7714pRdxT3PDka6NmKLUFJG/R21gkOHmS1nXz1YOXgVs5eiIhMNx6SWyST993hyRP5RbZEurnWrBOucp8psdGCp2OKAZWvBswjsez0mtzNZQhjb3vH1AbdIQMr5bPFgcTD//NTWY085s3C+kpo/dbqmkpmQjk=&pass_ticket=uujxBBANOnb1OlxHL/rKwGParJ1gx2kykx+96NfJsZ5zq4+QXxoyHKs9Vm07ReJ2&wx_header=3)

Original字节笔记本 字节笔记本

Anthropic 发布了迄今最强的模型 Claude Fable 5。

![](.evernote-content/B33900BF-22FA-4F05-9463-87415CB1C2E3/F04EBA35-E954-47C2-B334-989C33CF2100.png)

其实今天一起来的是两个东西:Fable 5 和 Mythos 5。

这两个型号是同一个底座，差别是安全防护。

Fable 5 加了一层安全分类器，面向所有人，Mythos 5 把部分领域的限制解除掉，只会给批经过审核的网络安全合作伙伴,跟美国政府一起部署。

一句话，Fable 5 就是降级版本的安全的Mythos。

**都降级了哪些东西？**

Fable 5 配了一套独立的分类器，专门盯三类请求:网络安全、生物与化学、模型蒸馏。

一旦命中，这次回答就自动交给 Opus 4.8，并告诉你发生了降级。

Anthropic给的数据是超过 95% 的会话压根不会触发，在这些会话里，Fable 5 和 Mythos 5 没区别。

![](.evernote-content/B33900BF-22FA-4F05-9463-87415CB1C2E3/D23EA08D-F431-4150-80D6-DE3EB04A02E7.jpg)

不过我测试了一下发现，即便只是搜索Fable 5相关的信息也会被通知降级到Opus。

**降级版本，但是价格到顶级。**

Fable 5 是每百万输入 10 美元、输出 50 美元，是 Sonnet 的 3 倍多。

Fable成本太过于夸张了，可以说基本上普通用户基本无缘使用，即便是Claude Code 20X额度，消耗是Opus的两倍不止，蹬两轮可能直接超限。

如果你是订阅用户，只推荐在网页端来对话尝试，Claude Code建议放弃幻想。

**Fable 5 到底有多少强呢？**

以下是官方案例：

Stripe 拿它在一个 5000 万行的 Ruby 代码库里做全库迁移，一天搞定，原本一整个团队要花两个多月。

视觉上，以前的 Claude 玩宝可梦火红版要靠一堆辅助工具才能推进，Fable 5 只用最基础的视觉接口就通关了，还能直接看着截图把一个 Web 应用的源码还原出来。

最狠的在科研侧。

蛋白质设计专家用 Mythos 5 把部分药物设计流程加速了约 10 倍，一项基因组学研究里，它几乎全自主跑了一周多，训练出的模型表现超过了发表在 Science 上的那个，体量却只有人家的百分之一。

![](.evernote-content/B33900BF-22FA-4F05-9463-87415CB1C2E3/6DFAB9E1-B9B5-4078-88BD-05BE477FD2CE.png)

也就是任务越长、越复杂，它甩开其他模型越远，这也是这代模型真正的卖点。

但真实测试下来，Fable 5 High 与 GPT-5.5 (xhigh) 相比并不那么出色。

Claude Fable 5 在 cursor 排行榜上位列 70.6，而 GPT-5.5 extra high 则为 64.3%。

GPT-5.5(xhigh) 以四分之一的成本产生类似的结果，消耗四分之一的令牌，并只需 Fable 5 的一半步骤。

所以即将发布的GPT-5.6 是完全有能力击败 Fable 5的。

![](.evernote-content/B33900BF-22FA-4F05-9463-87415CB1C2E3/688C46AC-DCEB-4153-A809-EF32BA552AEA.png)

**当然除了贵，你想用可能还用不到。**

付费的Pro、Max、Team 订阅用户可以用到6 月 22 日，之后会直接从这些计划里撤掉，想继续用得自己买API的积分。

Anthropic 说等产能够了会恢复成订阅标配，但没给时间表。走 API 和按量付费的企业用户不受影响。

**为了防止模型被蒸馏，痛下杀手。**

从 Fable 5 开始，所有 Mythos 级别模型的流量强制保留 30 天，第一方第三方平台都算在内。

Anthropic 说不会拿去训练，只用于安全监控，比如抓新型越狱和跨请求的复杂攻击，不过附加了一句最离会加入人工的审核，所有这些都是为了预防模型被恶意的蒸馏，可以说是无所不用其极，以至于违背了之前的部分条款。

因为当初有不少企业正是冲着 Anthropic 的零留存政策才选的它。

最打脸的就是上周 A/还在公开喊话，呼吁全行业一起给前沿 AI 踩刹车，这周转身就把自己最强的模型披着马甲摆上了货架。

最后是值不值得用？

Fable 5对于普通开发而言，基本上没有任何的性价比，而且增加了人工审查的环节，封号问题可能会更加的严重。

目前Fable 5的最大意义就是让GPT-5.6早点出来。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247517853&idx=1&sn=55dc9bf9310efaf329213bb44d4d5fd9&chksm=e90cf844573086ae371fcb75906f95fc0931772b6093b0183fcf6d074b838f3a3d8dd9233ca2&scene=90&xtrack=1&req_id=1781048450916100&sessionid=1781048471&subscene=93&clicktime=1781048474&enterid=1781048474&flutter_pos=0&biz_enter_id=4&ranksessionid=1781048451&jumppath=1001_1781048456739,1102_1781048457779,1001_1781048470039,1104_1781048472513&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQV4K9aCOB0GvbbIO2GrC9xRLTAQIE97dBBAEAAAAAAJStEi20epsAAAAOpnltbLcz9gKNyK89dVj0UYULx6sGaivs6wS72RTJ7np7CkuqW/X/HFtJbT/pcYvozndxX2OFpbixlhkn+0w0cv+rb8miCS7714pRdxT3PDka6NmKLUFJG/R21gkOHmS1nXz1YOXgVs5eiIhMNx6SWyST993hyRP5RbZEurnWrBOucp8psdGCp2OKAZWvBswjsez0mtzNZQhjb3vH1AbdIQMr5bPFgcTD//NTWY085s3C+kpo/dbqmkpmQjk=&pass_ticket=uujxBBANOnb1OlxHL/rKwGParJ1gx2kykx+96NfJsZ5zq4+QXxoyHKs9Vm07ReJ2&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/39032549-2bee-47b8-8bad-803afd5b75ed/39032549-2bee-47b8-8bad-803afd5b75ed/)
