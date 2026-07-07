---
title: 关于Agent Harness，我整理了一个最小版！
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/关于Agent Harness，我整理了一个最小版！.md
tags: [evernote, impression, yinxiang]
---

# 关于Agent Harness，我整理了一个最小版！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIyNjM2MzQyNg==&mid=224772...](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723046&idx=1&sn=427132703b45e625c9a84c50ef420fb3&chksm=e93fea0702152ebf5fb2d6385036de8b618b02b51bb72fc724cb6f2c7e7a8d602fcef4bddb66&scene=90&xtrack=1&req_id=1779767437504950&sessionid=1779766284&subscene=93&clicktime=1779768588&enterid=1779768588&flutter_pos=12&biz_enter_id=4&ranksessionid=1779767437&jumppath=30024_1779767968886,1104_1779767976198,20020_1779768247836,1104_1779768584039&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQN2eadYVNECoTVshGdVjVbRLTAQIE97dBBAEAAAAAAE4MJenzsfcAAAAOpnltbLcz9gKNyK89dVj03Yv2z+NQDwmPFmH7/dX0BlDNd2PTpEQmvVpmHize8KKJ2aFoXQTH8AUc7zAMS4quNnC+zD+cOTEd7kmgV73nhOYfQc1JaaFb1z7Dj0qXVs3VpjmCbggfGGceREWUUhaO7xre9JZFV+6SEO0kPGLsU4sAafufFmlYKK35JwRLL8Gv4WjViX3gdZ7AoALalw1oJyNYkc8ogCmjCHz/dzeDNV8v0ssGFegaxFF97h8=&pass_ticket=oriH6Dt4RR9g46tvxpSlNkeV9P1tU/imI+wmXJWdkhLdLENK/lp3Hc5E1S5NagZv&wx_header=3)

关于Agent Harness，我整理了一个最小版！
==========================

Original陈思州Datawhale

Datawhale干货   ******作者：陈思州，Datawhale成员******
============================================

前面讲 Agent 评测时，我提到：评测 Agent 不能只看最终答案，还要看它用了什么工具、拿到了什么结果、有没有按任务要求完成。那这些东西要怎么稳定记录下来？这就需要一个 harness。

现在有一个观点是 Agent = model + harness；

我会把 harness 理解成：把 Agentic model 放进一个可运行、可记录、可评分的小环境里。它不一定一开始就很复杂，只要能把任务、工具、执行过程和评分结果串起来，就已经很有价值。

这篇按 4 个问题梳理：1. 一个最 mini 的 harness 解决什么问题？2. 它最少需要哪些模块？3. 一个 eval case 可以怎么写？4.公开资料里有哪些参考？

一个最 mini 的 harness 解决什么问题

如果只是手动测试 Agent，很容易只看到最后回答。比如用户问“请判断这个项目是否支持插件系统”，Agent 回答“当前 README 没有插件系统相关说明，不能确认支持”。

这句话看起来合理，但我们还需要知道：它有没有真的读取 README？有没有读错文件？有没有调用无关工具？有没有把工具结果里没有的信息写进答案？

mini harness 要解决的就是这个问题。

它把任务放进一个固定环境里，让 Agent 使用指定工具完成任务，同时记录执行过程，最后用评分器判断结果。

这样我们看到的就不只是一句回答，而是一条完整记录：任务是什么，环境里有什么，Agent 调用了什么工具，工具返回了什么，最后为什么被判成功或失败。

mini harness 最少需要哪些模块

我会把最小结构拆成 5 个模块：

* Task：任务输入
* Environment：可操作环境
* Tools：工具接口
* Trace：执行记录
* Grader：评分器

Task 是任务本身，比如“根据 README 判断是否支持插件系统”。

Environment 是任务环境，对 coding agent 来说可能是一个代码仓库，对文档 agent 来说可能是一组文件。

Tools 是 Agent 能使用的工具，比如 read\_file、list\_files、run\_tests。

Trace 记录每一步用了什么工具、传了什么参数、返回了什么。

Grader 负责给出结果判断，第一版可以先用规则或测试脚本，比如是否读取指定文件、是否通过测试、是否写出证据里没有的结论。

这 5 个模块合起来，就能构成一个最小可用的 Agent harness。

一个 eval case 可以怎么写

一个 mini eval case 可以先写得很小，重点是任务、环境和评分规则都明确。

```
{

"id": "case_001",

"task": "判断项目是否支持插件系统",

"environment": {

"files": {

"README.md": "本项目支持本地启动、基础登录和配置管理。",

"config.md": "配置项包括 port、theme、log_level。"

}

},

"tools": ["list_files", "read_file"],

"grader": {

"must_read": ["README.md"],

"answer_should_include": "不能确认支持插件系统",

"answer_should_not_include": "支持插件系统"

}

}
```

这条 case 覆盖了几个基本点：任务目标明确，环境内容固定，工具范围清楚，评分规则也可检查。它适合用来测试 Agent 是否会基于文件内容回答，而不是根据经验补结论。

跑完后，harness 至少要记录 trace：

```
{

"case_id": "case_001",

"trace": [

{

"tool": "list_files",

"arguments": {"path": "."},

"result": ["README.md", "config.md"]

},

{

"tool": "read_file",

"arguments": {"path": "README.md"},

"result": "本项目支持本地启动、基础登录和配置管理。"

}

],

"answer": "当前 README 没有插件系统相关说明，不能确认支持插件系统。",

"grade": {

"success": true,

"reason": "读取了 README，回答没有超出文件内容。"

}

}
```

这条记录的价值在于可以定位问题。如果 Agent 没有调用 read\_file，说明工具使用有问题；如果读了 README 但仍然回答“支持插件系统”，说明结果使用有问题；如果反复读取无关文件，说明轨迹效率有问题。手动试用容易只留下主观感觉，harness 会留下可分析的执行记录。

公开资料里有哪些参考

Anthropic 的 Agent Evals 文章很适合作为主参考。它把 eval harness 和 agent harness 分得很清楚：eval harness 负责跑评测、记录步骤、评分和汇总结果；agent harness 负责让模型作为 Agent 工作，比如处理输入、编排工具调用、返回结果。它还强调，评估一个 Agent 时，评到的是模型和 harness 一起工作的效果。

SWE-agent 的重点是 Agent-Computer Interface。它说明 coding agent 的表现不只取决于模型，也取决于外部接口怎么设计。比如怎么查看文件、怎么编辑代码、怎么运行测试、怎么把错误信息反馈给模型，这些都会影响最终效果。

Terminal-Bench 的任务结构也很适合参考。一个任务通常包含 instruction、隔离环境和测试脚本。harness 负责把模型接到终端环境里，让它执行命令、安装依赖、调试错误，最后用测试脚本验证任务是否完成。

SWE-bench 则展示了 coding agent 的典型评测流程：给一个真实 issue，让模型生成 patch，再把 patch 放进环境里运行测试。这里的 harness 负责准备环境、应用 patch、执行测试、汇总结果。

这些资料放在一起看，harness 的价值在于把 Agent 的运行过程变成可以复现、可以记录、可以评分的实验。

写在最后：先把 Harness 的骨架搭出来

一个 mini Agent harness 不需要一开始做成完整平台。第一版只要能串起任务、环境、工具、执行记录和评分器，就已经能帮我们观察 Agent 到底哪里出问题。

有了这套结构，我们就不只是“试一下 Agent 好不好用”，而是能分析问题出在任务理解、工具选择、参数填写、结果读取、步骤冗余，还是评分规则本身不清楚。

封面来源｜AGI Hunt

![](.evernote-content/B5212A17-1243-416C-8F66-1A023FF87CD4/C0BEC2B0-0EB8-45DD-A520-2848CCA68EF0.png)

**一起“**点****赞”****三连**↓**

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723046&idx=1&sn=427132703b45e625c9a84c50ef420fb3&chksm=e93fea0702152ebf5fb2d6385036de8b618b02b51bb72fc724cb6f2c7e7a8d602fcef4bddb66&scene=90&xtrack=1&req_id=1779767437504950&sessionid=1779766284&subscene=93&clicktime=1779768588&enterid=1779768588&flutter_pos=12&biz_enter_id=4&ranksessionid=1779767437&jumppath=30024_1779767968886,1104_1779767976198,20020_1779768247836,1104_1779768584039&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQN2eadYVNECoTVshGdVjVbRLTAQIE97dBBAEAAAAAAE4MJenzsfcAAAAOpnltbLcz9gKNyK89dVj03Yv2z+NQDwmPFmH7/dX0BlDNd2PTpEQmvVpmHize8KKJ2aFoXQTH8AUc7zAMS4quNnC+zD+cOTEd7kmgV73nhOYfQc1JaaFb1z7Dj0qXVs3VpjmCbggfGGceREWUUhaO7xre9JZFV+6SEO0kPGLsU4sAafufFmlYKK35JwRLL8Gv4WjViX3gdZ7AoALalw1oJyNYkc8ogCmjCHz/dzeDNV8v0ssGFegaxFF97h8=&pass_ticket=oriH6Dt4RR9g46tvxpSlNkeV9P1tU/imI+wmXJWdkhLdLENK/lp3Hc5E1S5NagZv&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9251fa61-7c12-4dbe-b799-261c41124f45/9251fa61-7c12-4dbe-b799-261c41124f45/)
