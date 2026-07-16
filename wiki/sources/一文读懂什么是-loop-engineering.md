---
title: 一文读懂什么是 loop engineering
type: source
created: 2026-06-20
updated: 2026-06-20
source_path: 印象笔记管理工具/一文读懂什么是 loop engineering.md
tags: [编程, AI]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "一文读懂什么是 loop engineering"
source: evernote
type: note
export_date: 2026-06-25
guid: 9a7b5b0b-d417-4608-9d2a-48d7f3dbc402
---

# 一文读懂什么是 loop engineering

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIyODcxODg0NQ==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzIyODcxODg0NQ==&mid=2247495258&idx=1&sn=cfbb67089742da26663a332f902fa83c&chksm=e925d432f51b0795009409271c9df4306d23a358fe468931aa366b41512f8a8cf5a02d49e214&scene=90&xtrack=1&req_id=1781529985837818&sessionid=1781527535&subscene=93&clicktime=1781530188&enterid=1781530188&flutter_pos=32&biz_enter_id=4&ranksessionid=1781529985&jumppath=20020_1781529985222,1104_1781530011512,20020_1781530025975,1104_1781530086618&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAsdebsLVXQ/2AdMPZz16vRLTAQIE97dBBAEAAAAAAP7nAICyRYYAAAAOpnltbLcz9gKNyK89dVj08C+kKuEXp2DYMRKIFn7Yd44IBM5he0r/ud0rjs+Spl5nSxjlrK8t6fxlfu5u9QsP5/JwaQBtJac/SmTD0QN1wnKei8O6h58K4pR+tBcTx08OQQihbK6lWU9Vwyzs21bedvZCIxMjueDbHrLj0RoLZIRwn2n1+yFcFgvJojy7SI3RHBO+3t1thn4jPFA7DIpyR0DIcF0C+yxheRYNdwkYAm33vfDTGur6E4PZPSQ=&pass_ticket=NnJzgtg9eCvydEc6wLS2z5egAd7+XuZt61M1uTHYT7s+wmmpSbgl8A6GThtJC/NU&wx_header=3)

Original青椒大个青椒

继“提示词工程”“上下文工程”之后，2026 年 6 月又冒出一个词：循环工程（loop engineering）。

先是 Claude Code 创造者说自己已经不再搞什么提示词，而是专注 loop engineering，然后是Peter Steinberger 在 X 上发布类似内容的贴文。

循环工程的核心是：不再一句句给 AI 下指令，而是设计一个能让 AI 自己转起来的循环。

## 它到底是什么

旧做法是你逐条 prompt：你说一句，AI 干一步，你看结果，再说下一句。各种针对 Claude Code 设计的小键盘，让人类只负责按 Yes 和 No，核心原因都是这个。AI 是聪明，但它会一直问问题，你得坐在电脑前等着回答。

每次我这么干的时候都会想，这么简单的问题真的需要我坐在这里耗时间吗？

循环工程替代掉的正是这个交互。Steinberger 的说法是，人不该再去给代理发提示词，而该去设计一个能自动给代理发提示词的系统。人从“一句句指挥”挪到“设计一个让 AI 自己转的循环”。

业界的演进路线分三段：先是提示词工程，控制输入给模型的文字；再是上下文工程，控制喂给模型的知识；然后是运行框架工程（harness），管模型之外的执行、隔离、错误回传。循环被放在 harness 之内或之上的一层，Osmani 称它“比 harness 高一层”。

harness 有一句常被引的公式：Agent = Model + Harness。代理等于模型加上围着模型的那层运行框架。做循环需要的代码量更高。

一个能工作的循环框架，真正占住代码量的是模型外面那一圈：触发、隔离、回传、状态。有了这些代码，AI 才能够在框架内循环往复完成工作。

## 一个“循环”长什么样

一个基本的循环由六组零件组成，每一组都是“人退到循环外面”之后打的补丁。

自动触发：靠 Cron 定时任务或事件钩子（比如仓库收到新合并请求）把活自动送进来，人不用每天手动唤醒。

隔离工作区：用 Git Worktree 给每个并行的代理一个独立的克隆环境，互相不踩。

技能文件：把项目约束和标准流程写成机器能读的文件灌进上下文，对治模型每开一个新会话就忘事。

MCP 连接器：通过模型上下文协议（MCP）接到外部系统，读任务看板、查数据库、调脚本。

子代理对抗审查：拆成规划、执行、验证三个角色，让生成代码的模型不自己审自己，验证代理专门挑刺（Planner / Executor / Verifier）。

外存状态持久化：这一组叫 Ralph Loop。最基本的形式是一个 while 循环，每轮都开全新上下文，状态全靠 git 历史、progress.txt、AGENTS.md 这类外部文件。

这六组里，每一个单独拿出来都是真实的工程实践。

这套方法论最早来自 2022 年 10 月，普林斯顿（Shunyu Yao、Karthik Narasimhan）和谷歌研究院的论文 ReAct（arXiv:2210.03629，ICLR 2023），机制是“想、做、观察”三步循环。

2023 年 3 月 30 日，Toran Bruce Richards 发布 AutoGPT，13 天破 3 万星、数周破 10 万星，是循环最早的出圈尝试。

想做到成功的循环不容易。循环自己判不清活干完没有，就会一直转下去，每转一圈都在花钱。各种护栏的目的正是为了让烧钱可控。

## 适用场景

循环工程本质上还是适合商业体，在那里，它的价值最明显。

Mindtrip 是一个真实运营的消费级 AI 旅行平台，2026 年 5 月 6 日上线了 Mindtrip Flights，基于 Sabre Mosaic、用 PayPal 收款。平台实现了一整套循环方案，通过获取航班取消通知，让 AI 在几分钟之内推出针对每个旅客的退改签方案，效率极高。

以往需要人来做的事，现在把标准交给 AI，由 AI 来做即可。

简单的说，循环工程解决的是 7X24 牛马工作的问题。用无需休眠的 AI 来替代人类，在同样时间内完成工作，花钱买时间。

如果你的工作没那么着急，慢慢来即可。AI 在这里的价值依然是，替代人。AI 是拥抱 996，007 的圣体。

我在我的新内容产品里已经打造了一条尚未彻底闭环的 loop 雏形，选题—写稿—审核—修改—再审—复审。其中审核和修改是闭环循环，标准是蒸馏出来的我的品味。未来它将会根据阅读数据做成全自动循环，不断优化内容。

目前看，效果不错。人的注意力是稀缺资源，AI 能帮我解决这个问题。

## 四、代价

任何便利都有代价。循环工程把人抽出去，用 AI 替代。它的代价有三种。

第一种是技术债，代码写乱了、依赖缠成一团。这种债是显性的，AI 能替你还，可以重构

第二种是理解债。代码可能整洁、测试全绿，但团队里没人能从底层说清系统是怎么转的。这是“人退到循环外面”的直接副产品：使用者如果没参与生成的每一步，结果就成了一个能用却看不透的黑箱。

把判断提炼出来交给 AI，做成循环，本质上是外包思考。长期外包的思考，一旦出错或者修改，需要人类重新介入。

第三种是意图债，Addy Osmani 提出（《The Intent Debt》）。一个功能“为什么这么设计”的理由，如果没显式写进文档（比如架构决策记录 ADR），AI 代理就会拿它的推理能力脑补一个看似合理的理由，再照着这个假理由去重构系统。让意图债变危险的，恰恰是 AI 最被称道的那项本事：会推理。

技术债 AI 能还，理解债 AI 帮着还（但它的解释反而可能加深你的依赖），到意图债这儿，AI 彻底还不了。意图不是从代码里能推出来的东西，它只能来自人真实的业务诉求。你能外包执行，外包不了“想要什么”。回顾每个环节的决策步骤和原因，不是一件轻松的事。

微软的 Mark Russinovich（Azure CTO）和 Scott Hanselman 在 CACM（2026 年 4 月）的文章里说，agentic 助手给资深的是“AI boost”、给初级的是“AI drag”，他们叫它“收窄的金字塔”假说：同一个循环，资深的拿它放大判断，初级的拿它替代判断。

哈佛的报告：22 到 25 岁、AI 暴露高的岗位降了约 13%；斯坦福调查：2025 年 7 月，22 到 25 岁的软件开发者就业比 2022 年底的峰值降了约 20%，入门岗在 2022 到 2024 年间降了约 60%。循环替掉的多是初级活，可初级活正是人练出判断、日后能还意图债的台阶。

当然，也不是所有人都同意这个判断。AWS 的 CEO Matt Garman，认为“用 AI 替代初级开发者”是他听过最蠢的事之一。

## 结论

所以循环工程的核心是定义护栏、立验收标准、规划代理之间怎么沟通，并且把“为什么这么设计”的意图记下来。

harness 提供 AI 框架，loop 让 AI 在框架内跑起来，就这么简单。


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIyODcxODg0NQ==&mid=2247495258&idx=1&sn=cfbb67089742da26663a332f902fa83c&chksm=e925d432f51b0795009409271c9df4306d23a358fe468931aa366b41512f8a8cf5a02d49e214&scene=90&xtrack=1&req_id=1781529985837818&sessionid=1781527535&subscene=93&clicktime=1781530188&enterid=1781530188&flutter_pos=32&biz_enter_id=4&ranksessionid=1781529985&jumppath=20020_1781529985222,1104_1781530011512,20020_1781530025975,1104_1781530086618&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAsdebsLVXQ/2AdMPZz16vRLTAQIE97dBBAEAAAAAAP7nAICyRYYAAAAOpnltbLcz9gKNyK89dVj08C+kKuEXp2DYMRKIFn7Yd44IBM5he0r/ud0rjs+Spl5nSxjlrK8t6fxlfu5u9QsP5/JwaQBtJac/SmTD0QN1wnKei8O6h58K4pR+tBcTx08OQQihbK6lWU9Vwyzs21bedvZCIxMjueDbHrLj0RoLZIRwn2n1+yFcFgvJojy7SI3RHBO+3t1thn4jPFA7DIpyR0DIcF0C+yxheRYNdwkYAm33vfDTGur6E4PZPSQ=&pass_ticket=NnJzgtg9eCvydEc6wLS2z5egAd7+XuZt61M1uTHYT7s+wmmpSbgl8A6GThtJC/NU&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/9a7b5b0b-d417-4608-9d2a-48d7f3dbc402/9a7b5b0b-d417-4608-9d2a-48d7f3dbc402/)
