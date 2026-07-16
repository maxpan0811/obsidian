---
title: 白话给团队讲明白：Loop、Harness、Agent、World Model Engineering。
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/白话给团队讲明白：Loop、Harness、Agent、World Model Engineering。.md
tags: [evernote, impression]
---

---
title: "白话给团队讲明白：Loop、Harness、Agent、World Model Engineering。"
source: evernote
type: note
export_date: 2026-06-23
guid: 2f576887-d674-4139-af97-f1ca33458793
---

# 白话给团队讲明白：Loop、Harness、Agent、World Model Engineering。

原文链接: [https://mp.weixin.qq.com/s?chksm=ce25642ff952ed39a30613d126d693a...](https://mp.weixin.qq.com/s?chksm=ce25642ff952ed39a30613d126d693ad9bff94be8e78c6dc915e2025be8ec8adf4e49da1dd99&exptype=unsubscribed_card_recommend_item_com_heat_tlfeeds&ranksessionid=1782029952_2&req_id=1782031330553375&heat_id=1&scene=169&mid=2247484559&sn=49f30258f25e2e20fd2fe16c275e4732&idx=1&__biz=Mzg2MDU4NDM5OQ==&sessionid=1782029952&subscene=200&clicktime=1782032238&enterid=1782032238&flutter_pos=16&biz_enter_id=5&jumppath=WAWebViewController_1782032213970,WAWebViewController_1782032214470,20020_1782032231051,1104_1782032232578&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQa7Q0KZIWEkL0olhb1k+bbBLTAQIE97dBBAEAAAAAAHh2OS2XmoEAAAAOpnltbLcz9gKNyK89dVj0abfZz2PDL2meSWpwuQsbUklZDzP+tentu2R0Vs4BLtPGaeXLEr/JBd5XiOVCAfhhho4to2dmwUdGRseflfmNnUVWLNalUrxK3emE5YsVCcfGFAfP3mP2VWnO2cmN03ZqQvrSJ0EvuZGehTzutM/7FdD9zvPQa7PBJEVHgYwcoh9EGWpzcFKs5/04P82TqhP7YStJZdnyiDlfqcqZx7By3prEJazehU2scrjFQfA=&pass_ticket=2s6T/mSJFiZs9yRyV5bXcYuP4VOc/tDv38WnpCIKf8HwCjpz4JIgOuhMg7tKkXcZ&wx_header=3)

Original欣逸AI欣逸AI

![](attachments/08a7b00215101169.png)

```
前几天分别给两位大领导汇报了 AI 产品和 AI 工程两个方向的一些思路后，感觉领导对 AI 的期望比我原来预估的还要高;  
我本来想着产品和工程可以一步步推进，目前看，有可能有些事不得不加快了;  
且由此看来，领导、市场、客户的期望比实际提供的东西要高啊，属于供低于求的状态了，有能力的小伙汁、小菇凉也可以趁此次机会`刷一波xz和履历了`；  
另外汇报下来后我又和几个小伙伴交流了一些东西，发现大家对不少概念还是比较混淆。所以趁这两天准备一下这篇文章。下周给团队里的小伙伴再好好讲讲。
```

本篇主要用白话和示例介绍一下： Loop Engineering、Harness Engineering、Agent Engineering、World Model Engineering 这些概念，让团队内不至于拿A当B来互相交流，偏团队科普文。

首先我对这几个概念的理解：它们是一条逐步递进的工程链路。

从 Prompt 到 Context，到 Harness，到 Loop，到 Agent，再到 World Model，本质上是在回答同一个问题：

`我们怎么把一个会生成内容的大模型，逐步变成一个能在真实业务和真实工程系统里持续干活、可验证、可追责、可改进的工作系统。这里的工作可以是写一段代码，可以是下一个订单等。`

## 一、Engineering 的演进：从会说话，到能负责一段工作

![](attachments/4abb2f03c7c7ec5c.png)

用大白话讲，大概是这样：

Prompt Engineering 解决的是：这一次怎么把话说清楚。

Context Engineering 解决的是：这一次让 AI 看见什么事实。

Harness Engineering 解决的是：把 AI 放进一个受控的工程环境里，让它能调用工具、遵守规则、接受验证。

Loop Engineering 解决的是：让系统根据目标、状态和验证结果，持续推动 AI 往前走，而不是每一步都靠人手动催。

Agent Engineering 解决的是：把 AI 设计成有角色、有目标、有工具、有记忆、有边界、能协作的工作单元。

World Model Engineering 解决的是：让 AI 不只是读文本和调用工具，而是拥有一套对业务世界、软件系统或物理环境的可计算理解，能预测行动后果，能在真实执行前做模拟和推演。 -- 其实这个概念有点早了

这几个阶段不是替代关系，而是包裹关系。

Prompt 是最内层的一次指令。

Context 是这次指令背后的事实供给。

Harness 是让 AI 可靠执行的外部支架。

Loop 是跨多步执行的流程控制。

Agent 是围绕目标和职责形成的工作主体。

World Model 是 Agent 理解和推演环境的底层模型。

所以说“Prompt Engineering 已经过时了”。Prompt 没有过时，只是它不够了。

也不要说“有了 Agent 就不需要 Harness”。恰恰相反，Agent 越强，Harness 越重要。没有 Harness 的 Agent，就像一个行动力很强但没有流程、权限、测试和审计的人，短期看起来很猛，长期一定出事。

`AI 工程的演进，不是把前一个阶段扔掉，而是把前一个阶段放进更大的工程系统里。`

**吐槽一下：不知道World Model之后又会有一个其他的什么概念出来，感觉该吹的牛皮也快到顶了，再往下吹的技术再出现一次大进步了。**

## 二、Prompt Engineering：先把一次话说清楚

![](attachments/27054b175a73cffb.png)

Prompt Engineering 是大家最早接触的阶段。

它关注的是：我怎么描述目标，模型才能给出更符合预期的回答。

比如在软件开发里，你可以这样说：

“请修复支付回调重复通知导致订单状态反复流转的问题。重点看 `payment-callback` 模块，不要改动外部 API；需要补充幂等测试；完成后运行支付相关单测，并说明影响范围。”

此Prompt里：目标清楚，范围清楚，约束清楚，完成标准也清楚。这就算是稍微标准点的prompt，所谓的调prompt，也就是如此去调。

如果把它放到 AI 软件产品里，比如一个客服 AI，Prompt Engineering 对应的就是角色设定、语气风格、回答格式和基本规则：

“你是一个面向企业客户的售后助手，回答要简洁、稳妥，不要承诺退款结果，遇到合同、发票、法律问题要转人工。”

这些东西仍然很重要。

问题是，它解决不了全部问题。

客服 AI 不能只靠一段 Prompt 就知道客户买了什么套餐、有没有欠费、历史工单是什么、合同里怎么约定、当前操作有没有权限。研发 Agent 也不能只靠一句“遵守架构规范”就知道历史设计、测试命令、模块边界和客户定制逻辑。

Prompt Engineering 最大的价值，是让一次交互不跑偏。

它最大的局限，也是只面向“一次交互”。

所以很多团队一开始会沉迷 Prompt 模板库，后来发现模板越来越长，效果越来越玄学，维护越来越痛苦。原因很简单：你把上下文、规则、工具、流程、质量门，全都塞进了一段话里。

这时候就该进入下一个阶段了。

`Prompt 是方向盘，不是整辆车。`

## 三、Context Engineering：让 AI 看见该看的事实

![](attachments/c0f3d485bae9eefd.png)

Context Engineering 解决的是：AI 到底应该看见什么。

这里的关键不是“给得越多越好”，而是“给得刚刚好”。 -- `这个真的非常非常重要，防飘的很重要的一环，也是很多AI产品、研发工程的核心之一。也是各厂商进化的核心之一。`

一个真实的软件开发任务，真正有用的上下文可能包括：

需求文档、验收标准、技术方案、ADR、接口契约、数据模型、相关代码、测试命令、线上日志、历史缺陷、客户特殊约束、最近一次 Review 意见。

但这不等于把整个代码库、所有文档、所有聊天记录全塞进去。

上下文是有限资源。内容越多，噪音越多，冲突越多，模型越容易注意力漂移。更麻烦的是，很多上下文不是缺失，而是过期。

比如支付回调这个例子，AI 如果只看到当前代码，可能会把一段看起来很丑的兼容逻辑删掉。但那段逻辑可能是两年前为了某个大客户的历史回调格式保留的。如果这个事实只在老同事脑子里，AI 就只能靠猜。

所以软件开发视角下的 Context Engineering，不只是“RAG 一下代码库”。

它至少包括几件事：

1.哪些内容是主事实源，比如 PRD、SDD、ADR、API 契约、核心测试结论。2.哪些内容是过程态，比如评审意见、临时分析、待确认问题。3.哪些内容是辅助阅读层，比如 LLM Wiki、搜索索引、会话摘要。4.哪些内容应该被 Agent 按需检索，而不是一开始全部灌进去。5.哪些上下文需要版本、审批和追溯，不能靠聊天记录硬撑。

这也是我前面几篇文章一直强调 Git 知识底座、CR、LLM Wiki 的原因。

[Docs As Code，AI 研发转型中，我们为什么把研发知识放进 Git](https://mp.weixin.qq.com/s?__biz=Mzg2MDU4NDM5OQ==&mid=2247484229&idx=1&sn=e80f6effa6e83b3c778b68d324201493&scene=21#wechat_redirect)

[AI工程论：详细拆解LLM Wiki](https://mp.weixin.qq.com/s?__biz=Mzg2MDU4NDM5OQ==&mid=2247484385&idx=1&sn=df7992eed4675a7ca14133ea92c6e919&scene=21#wechat_redirect)

AI 软件产品也是一样。

一个智能客服产品，真正的上下文不是一段客服话术，而是用户画像、订单状态、合同条款、知识库、历史工单、当前会话、权限策略、可用工具、风险等级、人工接管规则。

一个智能销售助手，真正的上下文不是“你要热情专业”，而是客户行业、商机阶段、历史沟通、竞品情况、报价规则、可承诺范围、下一步动作。

一个 AI 研发平台，真正的上下文不是“你是资深工程师”，而是代码事实、产品事实、流程状态、质量证据和组织规则。

Context Engineering 的成熟标志，不是上下文窗口越来越大。

而是团队知道什么该进上下文，什么该留在事实源，什么该按需读取，什么不该让 AI 看到。

`AI 经常不是不会做，而是看错了世界。`

## 四、Harness Engineering：让 AI 在工程环境里可靠干活

![](attachments/5eb07e92958de24e.png)

到了 Harness Engineering，问题就从“说什么、看什么”，变成了“AI 在什么环境里干活”。

它不是一个单独功能，而是一整套围绕 Agent 的外部工程系统。

它包括但不限于：

系统提示、项目规则、工具权限、沙箱、文件读写、命令执行、MCP、Skill、hooks、测试、静态检查、代码 Review、人工审批、日志审计、成本控制、失败反馈。

软件开发里，一个典型的 Harness 是这样的：

项目根目录有 `AGENTS.md`，明确项目结构、编码规范、测试命令、不能碰的目录、提交前必须跑的检查。

有 Skill 把常见任务沉淀下来，比如“如何写接口兼容性测试”“如何做支付链路回归”“如何生成发布说明”。

有 hooks 在 AI 修改文件后自动格式化、跑 lint，或者阻止它改动受保护文件。

有 MCP 连接内部知识库、任务系统、设计稿、日志平台。

有测试和静态分析作为反馈传感器，告诉 Agent 做得对不对。

有人工审批点，避免它越权执行危险命令。

这和只写 Prompt 的差别非常大。

以前我们对 AI 说：“请遵守代码规范。”

现在我们把规范放进项目文件，把检查放进命令，把权限放进沙箱，把质量门放进 CI，把常见流程做成 Skill。

AI 不再只是被“提醒”要守规矩，而是被放进一个更容易守规矩、犯错后更容易被纠正的环境里。

AI 软件产品也是一样：

比如做一个能处理退款的客服 Agent，只写一句“请谨慎退款”是没用的。它需要：

可调用的订单查询工具。

明确的退款权限边界。

不同金额的审批规则。

高风险客户的人工接管。

……

这就是 AI 产品里的 Harness。

说白了，Harness Engineering 不是让 AI 更会说，而是让 AI 在一个可控系统里更可靠地做。

`Prompt 让 AI 知道你想要什么，Harness 让 AI 不至于乱来，而这个乱来，不是仅仅在prompt中增加几句“请遵守XXX规则”就完事了。`

## 五、Loop Engineering：让系统持续推动，而不是人一直催

![](attachments/20904d56f88decd6.png)

Loop Engineering 我在第 25 篇[Loop Engineering 是噱头还是什么，它与 Harness Engineering 的关系以及在研发平台中的定位是什么？](https://mp.weixin.qq.com/s?__biz=Mzg2MDU4NDM5OQ==&mid=2247484504&idx=1&sn=65c2942152e324021b6e19df65de7cf0&scene=21#wechat_redirect)里已经专门展开过，这里就不重复写成长篇了。

核心内容：

`Loop Engineering 不是 Harness Engineering 的替代，而是站在 Harness Engineering 上面，接管“流程怎么持续往前走”这件事。`

更具体一点：

`Loop Engineering 是为 AI Agent 设计可持续运行的目标推进闭环，让系统自动完成触发、上下文装配、任务执行、结果验证、状态回写和异常升级。`

放在本文这条演进链里，Loop 只需要抓住三点。

第一，Loop 不是 while 循环，也不是自动重试。没有状态、质量门、停止条件和人工接管点的“自动继续”，只是把不确定性规模化。

第二，软件开发里的 Loop，典型形态是 CI 失败、PR Review、测试补齐、依赖升级、发布检查这些高频、可验证、可回滚的节点。系统触发 Agent，Agent 执行，质量门验证，结果写回，失败后升级给人。

第三，AI 软件产品里的 Loop，典型形态是销售跟进、工单处理、数据监控、运营巡检这类持续任务。它不再只是回答一次问题，而是围绕状态变化持续推进动作。

即：

`Harness 让 Agent 能在工程环境里可靠执行一次任务，Loop 让这个执行单元在流程里被持续调度、验证、回写和停止。`

## 六、Agent Engineering：不要把角色扮演当 Agent

![](attachments/0260a438b535cf2c.png)

Agent/Agentic Engineering 比 Loop 更进一步。 Agent/Agentic Engineering：不是只让一个执行单元循环起来，而是设计多个有职责、有工具、有记忆、有权限边界的工作主体。

**我个人对"Agent"、"Agentic"这俩的理解是有差异的，不过这里先暂时混淆一下，后面仅用Agent来讲。**

很多人把 Agent 理解成“给 AI 一个角色”，比如“你是资深架构师”“你是测试专家”“你是产品经理”。这顶多是角色 Prompt，不是完整 Agent。

一个真正的 Agent，至少要有六个要素：

- 明确职责；
- 可执行目标；
- 可用工具；
- 可访问上下文；
- 记忆和状态；
- 权限边界与责任交接。

软件开发视角下，一个团队级 Agent 体系可能长这样：

Product Agent 负责需求澄清、验收标准、用户场景和边界条件。

Architect Agent 负责方案设计、模块边界、接口契约、风险评估。

Dev Agent 负责任务拆解、代码修改、局部验证。

Review Agent 负责安全、性能、可维护性、测试覆盖检查。

Test Agent 负责测试用例补全、回归范围建议、缺陷复现脚本。

Release Agent 负责发布说明、风险确认、回滚预案和变更记录。

`PS. 不是 Agent 越多越先进。`

很多任务一个 Agent 就够了。硬拆成十个 Agent，只会增加协调成本、上下文成本和冲突概率。

Agent Engineering 真正要解决的是：哪些工作应该由哪个 Agent 负责，Agent 之间如何交接，谁能改事实源，谁只能提建议，谁可以执行命令，谁必须等人审批。

AI 软件产品里，这个问题更明显。

以 WorkBuddy 这类办公场景 Agent 为例，它的方向不是再做一个聊天框，而是让 AI 通过个人助手、专家中心、技能市场、多平台连接和远程执行，进入真实工作流。用户在微信、企微、钉钉、飞书、Slack 这类入口下达任务，Agent 可以在本地或云端环境中处理材料、生成会议纪要、准备文档、调用工具。

这已经不是普通问答。

它开始变成“数字同事”的形态。

但只要进入数字同事阶段，就必须回答一堆工程问题：

它能代表谁执行？

能读哪些文件？

能操作哪些系统？

结果由谁确认？

失败了怎么回滚？

组织如何审计？

多 Agent 同时做事时谁来协调？

这就是 Agent Engineering，而不是 Agent 命名学。

`Agent 不是一个会说话的角色，而是一个能承担一段工作的受控主体。`

## 七、World Model Engineering：让 AI 能推演世界，而不是只读材料

![](attachments/23ae1a3fc3c96ed8.png)

World Model Engineering 是这一串里最容易被讲玄幻的概念，也是目前离现实最远的一个东西 -- 我自己也还没有摸熟，但是我个人感觉，这个是现在可以开始积累，然后逐步丰富的模块，不过现在我也只能浅析。

在物理 AI、机器人、自动驾驶、游戏环境里，World Model 通常指一个能模拟世界状态变化的模型。比如 NVIDIA Cosmos、DeepMind Genie 这类方向，都是让 AI 更好地理解物理环境、生成可交互世界、预测行动后果，用于训练、评估和规划。

但我们做软件研发和企业 AI 产品，比较容易把 World Model 理解成“我要训练一个物理世界大模型”。

对大多数软件团队来说，更现实的 World Model 可能是：

一套对业务、产品、系统和用户行为的可计算表示。

它能回答的不只是“文档里写了什么”，而是：

如果我改了这个接口，哪些业务流程会受影响？

如果我关闭这个开关，哪些客户路径会断？

如果退款策略变了，订单、财务、客服、风控会发生什么连锁反应？

如果 Agent 执行了这个操作，系统状态会如何变化，风险在哪里？

如果线上指标异常，最可能是哪几类因果链路？

软件开发里的 World Model，可以从很朴素的东西开始。

比如服务依赖图、领域模型、状态机、事件流、API 契约、数据血缘、测试夹具、线上 Trace、用户路径、特性开关、监控指标、历史事故库。

这些东西如果只是散落在文档和系统里，它们只是资料。

如果被组织成 Agent 可以查询、推演、验证的结构，它们就开始接近软件世界模型。

举个例子。

一个订单系统里，订单状态从 `created` 到 `paid` 到 `fulfilled` 到 `closed`，中间涉及支付、库存、发票、履约、售后、风控。如果 Agent 只看代码，它可能知道某个字段在哪里改。如果它有订单领域状态机、事件契约和历史异常样本，它就能推演“这个状态变更会不会导致售后单无法创建”“这个补偿任务会不会重复触发发票作废”。

AI 软件产品也是一样。

一个客服 Agent 如果只有知识库，它能回答政策。

如果有工具和权限，它能执行退款。

如果有 Loop，它能跟踪整个工单。

如果有业务 World Model，它就能在操作前推演：退款会不会影响合同余额、是否触发风控、是否需要销售确认、是否会影响下月续费预测。

这才是差别。

World Model Engineering 的价值，不是让 AI 显得更高级，而是让 AI 在行动前能更接近“理解后果”。

当然，这也是最难的阶段。

因为它要求团队把业务规则、系统结构、运行数据、行为反馈、测试环境和仿真能力组织起来。没有前面的 Context、Harness、Loop、Agent，直接谈 World Model，大概率会变成概念 PPT。

`World Model 不是更大的知识库，而是可推演的世界表示。`

`到这个阶段的时候，就应该能够非常明确地感受到：有个东西或者一套东西，会同时对软件团队的研发过程产生影响，也同时影响了该软件团队对外提供的AI产品。`

## 八、当下一线 AI 产品大概处在哪个阶段

![](attachments/d95ca54a91ddc669.png)

目前看，大部分一线产品已经走的很靠前了：

大多数成熟产品已经不只是 Prompt Engineering。

大多数真正有竞争力的 AI 编程产品，正在从 Context、Harness 向 Loop、Agent 过渡阶段。

更别说 World Model Engineering了。

### Claude Code

Claude Code 已经明显不是聊天式编程助手。

Claude cowork之类的另说。

它有 `CLAUDE.md` 做项目记忆和持久上下文，有 Skills 把重复流程封装起来，有 subagents 和实验性的 agent teams 做隔离和并行，有 hooks 做生命周期控制，有 Artifacts 把会话产物变成可分享的可视化页面，有 Agent SDK 把 Claude Code 能力嵌入到可编程 agent 系统里。

所以我个人对 Claude Code 的感觉是：

- Context Engineering 很强；
- Harness Engineering 很强；
- Loop Engineering 正在产品化；
- Agent Engineering 已经有雏形，尤其是 subagents、agent teams、SDK 这类能力。

### Codex

Codex 也类似。

从当前能力看，它已经覆盖 CLI、IDE、App、Cloud、GitHub code review、AGENTS.md、MCP、Skills、subagents、automations、非交互执行、长任务执行和验证流程。

尤其是长任务实践里，计划文件、执行说明、持续文档、里程碑验证这些东西，很像我们自己做 Loop Engineering 时强调的状态、验证和回写。

所以：

- 个人研发 Harness 很强；
- 代码任务 Loop 能力越来越明显；
- 多 Agent 协作已经有产品能力。

### WorkBuddy

WorkBuddy 这类产品更偏知识工作者和办公场景。

它的特点不是代码仓库里的深度研发协作，而是跨入口、跨工具、跨设备的执行能力。比如个人助手、专家中心、技能市场、多平台连接、本地电脑远程执行、云端部署、文档和材料处理。

- 办公 Agent 产品化阶段；
- 在某些场景具备 Loop 雏形，比如持续处理材料、跨应用执行、云端或本地任务执行；
- 它的 Harness 能力取决于企业如何接入权限、文件、审批、审计和业务系统。

### 大部分 AI 产品的

如果粗略分层：

只会聊天和生成内容的产品，大多还在 Prompt 到 Context。

RAG、企业知识库、文档问答，主要在 Context Engineering。

AI 编程工具和高质量 Agent 工具，已经进入 Harness Engineering。

能持续执行任务、跑测试、自动修复、写回状态的产品，开始进入 Loop Engineering。

能定义角色、权限、工具、记忆、协作和责任边界的产品，才算进入 Agent Engineering。

World Model Engineering 目前在物理 AI、机器人、自动驾驶、科学仿真这些领域更明显。在软件研发和企业协同场景里，它还处在早期形态：更多表现为业务数字孪生、领域模型、流程仿真、影响分析、运行态反馈和测试环境的系统化建设。

所以名词有点多，比较简单的判断就是：

`一线产品正在从 Harness 向 Loop 和 Agent 过渡；World Model 是下一阶段的关键方向，但大多数团队今天还没补齐前面的地基。`

## 九、对 AI 产品研发的影响：产品不能再只做聊天框，甚至可以逐步放弃聊天框为主交互模式的形态了

![](attachments/9b58a382f68fa134.png)

第一，AI 产品的核心形态从“回答问题”变成“完成工作”。

如果产品还停留在输入框加知识库，用户会觉得它有用，但不会觉得它可靠地接管了一段工作。真正的 AI 产品要开始设计任务、状态、工具、权限、验证、异常和回写。从辅助到交付结果。

第二，产品架构从页面架构，变成工作系统架构。

以前设计一个功能，更多是页面、接口、数据表、流程状态。

现在要额外设计：（不少新推出的AI产品也在朝着这个方向走）

AI 读什么上下文。

能调用什么工具。

每一步怎么验证。

什么时候停下来等人。

失败后怎么恢复。

哪些结果写回事实源。

哪些过程只作为会话记录。

哪些行为需要审计。

第三，AI 产品的质量体系要前移。

以前我们更多看功能测试、接口测试、性能测试。

AI 产品还要看任务成功率、人工介入率、上下文缺失率、幻觉率、工具误用率、Loop 失败原因、Agent 越权风险、用户修正率、回写准确率。

这不是多加几个指标那么简单。

这意味着 QA、产品、研发、架构、运维都要重新分工。

产品经理不能只写“支持 AI 总结”。他要写清楚 AI 的目标、输入、输出、边界、失败状态和人工接管点。

架构师不能只画系统模块。他要设计 Agent 运行时、工具契约、权限边界、上下文装配和状态流转。

测试不能只测页面按钮。他要做 eval、回放、对抗样本、流程验证和真实案例集。

研发不能只接一个模型 API。他要把 AI 当成一个非确定性执行主体，放进工程系统里管理。

第四，产品路线不要跳级。

很多团队一上来就喊“我们要做企业级 Agent 平台”，但事实源没有，工具权限没有，流程状态没有，质量评估没有，审计没有，成本控制没有。

**这种 Agent 平台大概率是一个更大的聊天框。-- 尤其是那种推出各种claw的企业。**

更稳的路线应该是：

先把核心场景的上下文和事实源打通。

再把高频任务做成 Harness。

再挑低风险、验证充分的场景做 Loop。

再把角色和协作沉淀成 Agent。

最后在关键业务域上建设可推演的 World Model。

`AI 产品的高级感，不来自概念命名，而来自它能不能稳定接住一段真实工作。`

## 十、对软件工程 AI 化的影响：培训个人+改造工程系统

![](attachments/0cb56b8714d3aaec.png)

对软件工程 AI 化来说，这条链路更现实。

很多团队现在的问题不是没人用 AI，团队里已经出现了一批 AI 高手，他们用 Claude、Codex、Cursor、各种 Agent 工具，个人效率提升很明显，但团队级系统没跟上，这也是为什么现在我的工作重心之一是搞这个系统，这里就不赘述了，可以关注[AI First的研发协同平台：（一）整体设计与落地](https://mp.weixin.qq.com/s?__biz=Mzg2MDU4NDM5OQ==&mid=2247484476&idx=1&sn=d7a7e7519fb848764c36557ae6332d03&scene=21#wechat_redirect)那个系列文章，就是更新略慢（不过估计再有个把月左右会搞完）。

## 能给团队讲的判断表

![](attachments/cf908f19fb56b658.png)

最后把这几个概念压缩的话：

当你只是在优化一句话，叫 Prompt Engineering。

当你在决定 AI 应该读取哪些事实，叫 Context Engineering。

当你在设计工具、权限、测试、规则、hooks、Skill、MCP、沙箱和质量门，叫 Harness Engineering。

当你在设计触发、状态、执行、验证、回写、重试和停止条件，叫 Loop Engineering。

当你在设计有职责、有工具、有记忆、有权限、能协作的工作主体，叫 Agent Engineering。

当你在设计业务、系统或物理环境的可计算表示，让 AI 能预测行动后果和做模拟验证，叫 World Model Engineering。

AI 工程化核心是是把人的经验、流程、判断和责任，逐步外显到系统里，让 AI 能在这个系统里更稳定地工作。 -- 这里不局限在研发工程领域

所以于我所处的行业（SaaS）而言，我感觉我们的竞争力可能是：

`短期拼工具使用，中期拼 Harness 和 Loop，长期拼 Agent 体系和 World Model。`

真正能跑出来的团队，不一定是最早喊新词的团队，而是能把这些概念一层一层落到真实交付里的团队。


---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=ce25642ff952ed39a30613d126d693ad9bff94be8e78c6dc915e2025be8ec8adf4e49da1dd99&exptype=unsubscribed_card_recommend_item_com_heat_tlfeeds&ranksessionid=1782029952_2&req_id=1782031330553375&heat_id=1&scene=169&mid=2247484559&sn=49f30258f25e2e20fd2fe16c275e4732&idx=1&__biz=Mzg2MDU4NDM5OQ==&sessionid=1782029952&subscene=200&clicktime=1782032238&enterid=1782032238&flutter_pos=16&biz_enter_id=5&jumppath=WAWebViewController_1782032213970,WAWebViewController_1782032214470,20020_1782032231051,1104_1782032232578&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQa7Q0KZIWEkL0olhb1k+bbBLTAQIE97dBBAEAAAAAAHh2OS2XmoEAAAAOpnltbLcz9gKNyK89dVj0abfZz2PDL2meSWpwuQsbUklZDzP+tentu2R0Vs4BLtPGaeXLEr/JBd5XiOVCAfhhho4to2dmwUdGRseflfmNnUVWLNalUrxK3emE5YsVCcfGFAfP3mP2VWnO2cmN03ZqQvrSJ0EvuZGehTzutM/7FdD9zvPQa7PBJEVHgYwcoh9EGWpzcFKs5/04P82TqhP7YStJZdnyiDlfqcqZx7By3prEJazehU2scrjFQfA=&pass_ticket=2s6T/mSJFiZs9yRyV5bXcYuP4VOc/tDv38WnpCIKf8HwCjpz4JIgOuhMg7tKkXcZ&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/2f576887-d674-4139-af97-f1ca33458793/2f576887-d674-4139-af97-f1ca33458793/)
