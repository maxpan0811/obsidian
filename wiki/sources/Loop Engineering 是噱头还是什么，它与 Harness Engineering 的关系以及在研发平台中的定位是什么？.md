---
title: Loop Engineering 是噱头还是什么，它与 Harness Engineering 的关系以及在研发平台中的定位是什么？
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/Loop Engineering 是噱头还是什么，它与 Harness Engineering 的关系以及在研发平台中的定位是什么？.md
tags: [evernote, impression]
---

---
title: "Loop Engineering 是噱头还是什么，它与 Harness Engineering 的关系以及在研发平台中的定位是什么？"
source: evernote
type: note
export_date: 2026-06-22
guid: c1d34651-cd79-4cf2-82f2-d3903c48a8f8
---

# Loop Engineering 是噱头还是什么，它与 Harness Engineering 的关系以及在研发平台中的定位是什么？

原文链接: [https://mp.weixin.qq.com/s?chksm=ce2564f8f952edeeb9f6cefe41cdf66...](https://mp.weixin.qq.com/s?chksm=ce2564f8f952edeeb9f6cefe41cdf66a2ec01eb914ca5d970850afefc08b9cf6373146627e43&exptype=unsubscribed_card_recommend_item_com_heat_tlfeeds&ranksessionid=1782032740_2&req_id=1782032746321263&heat_id=1&scene=169&mid=2247484504&sn=65c2942152e324021b6e19df65de7cf0&idx=1&__biz=Mzg2MDU4NDM5OQ==&sessionid=1782032739&subscene=200&clicktime=1782034167&enterid=1782034167&flutter_pos=16&biz_enter_id=5&jumppath=20020_1782034113452,1101_1782034113824,20020_1782034147956,1104_1782034162798&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQR6TznLyaSNWxnvHqpfov1xLTAQIE97dBBAEAAAAAAKoMBtlgnzUAAAAOpnltbLcz9gKNyK89dVj0Ry+P1ti1pYw1WMsglIMizt+p4UTjJ26qsqK4+YCGs2ISUJ9vKy6X85NiE9NAn76C2JLiMUROsi18uTFuj64cifhkQ5YVmDDwiiPtYVqjmaSfHNwIH9RIhCmQ5XbUnO8nvoKuMhavpHH6oLJXkPDs3MBpsqW3ElwqYl6fOM+T8VccEYzwT1vjJq+dU5vdO9tavskwWHzIvumEERAPrCk1L5Ch46dP86XUIfz3ZLU=&pass_ticket=zeTQjl4oZxIcMGijxyzUtzr2Ax7jzrlFYdtiq6BtLCgaiAqNaDW//tRAm9PkiYxr&wx_header=3)

Original欣逸AI欣逸AI

![](attachments/c34341574d463a5d.png)

最近看到 Loop Engineering 这个词又热起来了...也是服气大家的造词能力。

不是因为它没有价值，而是因为这类新词一旦被喊热，很容易被理解成“下一代银弹”：Prompt Engineering 过时了，Context Engineering 过时了，Harness Engineering 也过时了，现在大家都要搞 Loop Engineering。

这就有点离谱。

我的判断比较简单：

`Loop Engineering 不是噱头，但也不是一个独立于 Prompt、Context、Harness 之外的新神坛。它真正有价值的地方，是把过去人手动反复推动 Agent 的动作，变成可触发、可验证、可追踪、可停止的研发流程控制层。`

如果只是写一个 while 循环，不断调用大模型，那不叫 Loop Engineering，那叫自动化烧 token。

如果只是让 Agent “你自己一直干到完成”，没有状态、没有质量门、没有停止条件、没有人工接管点，那也不叫 Loop Engineering，那叫把不确定性规模化。

但如果我们把它放回真实软件研发里看，尤其放进我前面写的《AI First 的研发协同平台的整体设计与落地》那套系统里看，它确实是一个非常关键的拼图。

它不是替代 Harness Engineering，而是站在 Harness Engineering 上面，开始接管“流程怎么持续往前走”这件事。

## 一、Loop Engineering 到底是什么

![](attachments/76e2de5c88fb73df.png)

以前我们使用 coding agent，大多数时候是人坐在驾驶位。

人提出目标，人补上下文，人看执行结果，人发现测试失败，人再输入一句“继续修”，人看到 review 问题，人再让 Agent 改。Agent 看起来很自动，但真正的循环控制器其实是人。

Loop Engineering 关注的正是这个变化：

过去是人不断 prompt Agent。

现在是系统根据目标、状态和验证结果，持续 prompt Agent。

这个“系统”可以很轻，也可以很重。轻一点，是一个本地脚本加状态文件。重一点，是研发平台里的 Pipeline、任务状态机、Agent 执行平面和质量门。关键不是形态，而是它至少要有几个基本部件：

1.触发器：什么时候启动，比如 CI 失败、PR 创建、需求评审通过、定时巡检、线上告警。2.目标：这一轮到底要完成什么，什么不算完成。3.上下文：Agent 读取哪些事实、代码、文档、日志、评审意见和历史尝试。4.执行器：调用哪个 Agent、哪个 Skill、哪个工具、在哪个 worktree 或 sandbox 里执行。5.验证器：跑哪些测试、检查哪些质量门、谁来 review、哪些证据必须回写。6.状态：当前到了哪一步，试过什么，失败原因是什么，下一步是什么。7.停止规则：成功、失败、重试次数耗尽、风险过高、需要人工介入。

少了前几项，它只是 prompt。

少了验证和停止条件，它就是风险。

少了状态，它就只能靠聊天上下文硬撑，跑久了必然失忆、漂移、重复犯错。

所以我更愿意把 Loop Engineering 定义成：

`为 AI Agent 设计可持续运行的目标推进闭环，让系统自动完成触发、上下文装配、任务执行、结果验证、状态回写和异常升级。`

它不是某个工具按钮，也不是某个模型能力。

它是研发协作系统里的控制逻辑。

## 二、它和 Prompt、Context、Harness 是什么关系

![](attachments/af4191b60ea4dbd6.png)

这几个词最近堆在一起，特别容易讲乱。

我自己的分法是这样的。

Prompt Engineering 解决的是：这一次怎么把话说清楚。

比如“请修复这个 bug，并保证不改变现有接口行为”。这仍然重要，但它只是单次交互层。

Context Engineering 解决的是：这一次让模型看见什么。

比如 PRD、SDD、接口契约、历史 ADR、相关代码、测试命令、日志、客户约束。很多 Agent 做错，不是模型不会，而是上下文缺了、错了、过期了。

Harness Engineering 解决的是：让 Agent 在工程环境里可靠执行一次任务。

它包括系统提示、项目规则、工具权限、文件操作、命令执行、沙箱、hooks、MCP、Skill、subagent、测试反馈、会话记录和人工审批。说白了，Harness 是把一个会聊天的大模型，包成一个能在研发现场干活的工程协作者。

Loop Engineering 解决的是：如何让一个或多个 Agent 沿着目标持续推进，直到完成、失败或交给人。

它不只关心“这一次怎么干”，而是关心“这一组工作怎么被发现、拆解、执行、验证、回写、重试和升级”。

放成一条链路，大概是：

Prompt 是一次指令。

Context 是这次工作的事实输入。

Harness 是 Agent 的工程运行环境。

Loop 是跨多轮、多任务、多 Agent 的流程控制系统。

所以，Loop Engineering 不是 Harness Engineering 的替代品。

更准确地说：

`Harness 让 Agent 能干活，Loop 让 Agent 持续、可控、可验证地推进活。`

没有 Harness 的 Loop，只是在反复调用一个不稳定的聊天机器人。

没有 Loop 的 Harness，也能提高个人或单任务效率，但很多工作仍然要靠人不断推动。

这也是为什么外部工具的发展很值得看。

Claude Code 已经把 `CLAUDE.md`、Skills、subagents、hooks、MCP、plugins 这些能力做成 extension layer。它们本质上是在增强 Harness，也在给 Loop 提供积木：项目上下文、可复用流程、生命周期钩子、工具连接、隔离子任务。

Codex 也类似。`AGENTS.md` 负责项目级指导，`codex exec` 让 Agent 进入脚本和 CI，Automations 支持周期性任务，GitHub code review 和 GitHub Action 把 Agent 放进 PR 与流水线里。它们已经不是单纯聊天工具，而是在把 Agent 嵌入研发流程。

这些外部实践说明了一件事：Loop Engineering 不是凭空造词。工具形态已经开始往这个方向长。

但注意，这些能力更多是产品级积木，不是企业级 Loop 的开箱即用版本。真正进入研发主流程，还要补事实源、权限、质量门、组织状态和责任边界。换句话说，工具可以提供部件，但组织级闭环仍然要自己设计。

## 三、Loop Engineering 在软件研发工程里的定位

![](attachments/c7bd380d8e52b211.png)

如果把软件研发拆成几层，Loop Engineering 最适合落在“研发流程层”和“工程平台层”的交界处。

它不应该主要待在单个 prompt 里，也不应该只待在个人 IDE 里。个人 IDE 或 CLI 里的 Loop 很有价值，比如“改代码、跑测试、看报错、继续修”，但这更像个人短循环。

团队级 Loop Engineering 真正要解决的是流程问题：哪些节点可以自动推进，哪些节点必须人工判断，失败后重试还是升级，成功后哪些产物必须回写。

这些问题都不是单个模型能单独决定的。Loop 更像流程编排层：向下调用被 Harness 包好的 Agent 工作单元，向上接受状态机、质量门、权限和度量系统约束。

它一般会以几种工具形态出现。

第一种，是本地短循环。

比如开发者在 Codex、Claude Code、Cursor、Aider 里给出目标，Agent 修改代码、运行测试、根据错误继续修。这个层面适合个人效率，不适合承担团队治理。

第二种，是 CI/CD 里的 Agent Step。

比如 CI 失败后，Agent 自动读取日志，生成失败摘要，尝试在独立 worktree 中修复，跑最小测试集，成功后推 PR，失败后把原因写回。这个场景很适合，因为验证机制天然存在。

第三种，是 PR Bot 或 GitHub App之类的。

PR 创建后自动 review，发现高优先级问题后触发修复任务，修复后再次 review。这里 Loop 的关键不是“AI 审一次”，而是 review、修复、验证、再 review 的闭环。

第四种，是 Workflow Engine 或 Agent Orchestrator之类的。

当任务变成长周期、多角色、多阶段以后，就不能靠一个脚本硬扛了。需要状态机、任务队列、事件流、重试策略、人工审批、审计日志和成本控制。Temporal、Airflow、Dagster、LangGraph、自研 Pipeline 引擎，或者研发协同平台里的流程引擎，都可能承载这件事。

第五种，是 AI First 研发协同平台。

这也是我最关心的方向。因为对大型 SaaS 团队来说，真正的挑战不是让一个 Agent 写出一段代码，而是让需求、设计、开发、测试、发布、复盘这些节点，在 AI 参与后仍然可控、可追溯、可改进。

`Loop Engineering 在团队级软件工程里的核心定位，不是 Agent 能力，而是研发流程控制层。`

这句话很重要。

如果一个场景没有明确触发器、没有可靠上下文、没有可执行动作、没有可信验证、没有停止条件，就先别急着搞 Loop。

否则它会把团队原来靠人兜底的混乱，变成系统自动运行的混乱。

## 四、它是不是噱头，取决于有没有工程约束

![](attachments/b7e848c949b016f1.png)

很多新概念变成噱头，通常不是概念本身有问题，而是落地时偷懒。

Loop Engineering 最容易被偷懒成三种东西。

第一种，自动重试。

Agent 失败了，再来一次；再失败，再来一次。看起来很自动，实际上没有改变上下文、策略和验证，只是在赌下一次模型发挥好一点。

第二种，自动派活。

系统看到 issue，就让 Agent 去做。问题是 issue 质量不够、验收标准不清、影响范围不明、测试证据不足，Agent 做得越快，风险越大。

第三种，自动评论。

PR、CI、告警下面多了一堆 AI 评论，团队一开始觉得新鲜，过几周就开始忽略。因为它没有真正进入决策节点，也没有减少人的负担。

这三种都容易让 Loop Engineering 变成噱头。

真正有价值的 Loop，一定带着工程约束：

目标要足够小。

上下文要有事实源。

执行要隔离环境。

验证要自动化优先。

失败要可解释。

状态要持久化。

重试要有上限。

高风险动作要人工审批。

结果要回写到研发系统，而不是只留在聊天记录里。

这里我特别想强调“状态”。

很多人以为 Agent 失败是因为模型不够聪明。但在长任务里，真正麻烦的是状态管理。它上次做了什么，为什么失败，哪些路径已经排除，哪个测试还没跑，哪个人卡了审批，如果这些信息只在上下文窗口里，迟早会丢。

所以 Loop Engineering 不能只依赖对话上下文。

它需要外部状态。

这个状态可以是 Markdown，可以是任务系统，可以是 PR comment，可以是 traceability 文件，可以是数据库里的执行记录。关键是它必须在单次会话之外存在。

`Agent 会忘，研发系统不能忘。`

## 五、放进 AI First 研发协同平台，它应该落在哪里

![](attachments/a97d540c0b4c70fe.png)

前面那篇

《AI First 的研发协同平台的整体设计与落地》

欣逸AI，公众号：欣逸AI[AI First的研发协同平台：（一）整体设计与落地](https://mp.weixin.qq.com/s/AaqutKGOoa9hU2bV5VQl0g)

里，我把平台拆成几个核心能力：可信知识底座、超级个体协同层、流程状态机、Agent/Skill 与受控工具、质量门与度量系统、场景工坊。

而Loop Engineering 不会被做成一个独立模块，然后在菜单里叫“Loop 管理”。那样大概率没人用。

它更应该嵌进这些能力之间，成为平台的流程运行机制。

第一，可信知识底座要承接 Loop 状态。

Loop 不能只把过程留在聊天记录里。一次 CR 从需求到发布，需求澄清、设计评审、任务拆分、测试覆盖、风险关闭，都应该回写到 `change-requests/`、`delivery/`、`traceability` 或 review annotations 里。LLM Wiki 可以负责读、搜、问、解释，但关键状态和交付证据必须回到主事实源。

第二，超级个体协同层要沉淀 Loop 模板。

过去团队沉淀 Prompt、Skill、检查清单和脚本。进入 Loop Engineering 后，更值得沉淀的是“可复用工作闭环”：触发器是什么、读哪些上下文、调用哪个 Agent、能用哪些工具、质量门是什么、失败几次升级给人。

这里要分风险等级。CI 修复、测试补全、依赖升级偏自动执行型；需求澄清、PR 风险审查、发布前检查偏辅助判断型；线上问题初步排查默认只读，不能自动操作生产环境。不同风险等级的 Loop，权限和停止条件必须不一样。

第三，流程状态机负责给 Loop 画轨道。

状态机定义 `drafting`、`requirement-approved`、`tech-designing`、`developing`、`code-reviewing`、`writing-back` 这些流程位置。Loop 只适合驱动其中高频、可验证、可恢复的节点，不应该把每个状态都自动化。

比如开发阶段可以让 dev-agent 在独立 worktree 里改代码、跑测试、失败重试、提交 PR；Review 阶段可以让 reviewer-agent 生成风险摘要、收敛 P0/P1 问题；但需求评审、架构取舍、发布审批这类节点，仍然应该 Agent 辅助、人来判断。

第四，Harness 是 Loop 的执行平面。

Loop 不应该直接“控制模型”，而应该编排已经被 Harness 包好的工作单元。不同 Agent 有自己的上下文、权限和输出格式，MCP、受控 Command、CI、Git 和 traceability 工具，则是它可以调用的执行接口。

第五，质量门和度量系统决定 Loop 有没有价值。

不要只看 Loop 执行了多少次，要看成功率、重试次数、人工介入率、失败原因、质量风险和 token 成本。没有质量门的 Loop，会同时制造质量债和 token 账单。

第六，场景工坊负责把 Loop 产品化。

用户不需要看到一堆抽象概念：Loop、Harness、Context、MCP、State。他应该看到具体工作流，比如“修复 CI 失败”“补 traceability”“识别重复失败任务”。产品上不一定叫 Loop，但必须可触发、可观察、可接管、可复盘。

## 六、最后的观点

![](attachments/59ff57ee1ded4987.png)

Loop Engineering 不是噱头。

但它也不是一个可以盖过 Prompt、Context、Harness 的新概念。

它更像是 AI First 软件工程继续往前走后，必然出现的一层流程能力：当 Agent 不再只是单次工具，而开始参与持续交付时，我们必须设计循环、状态、验证、重试、升级和回写。

放回 AI First 研发协同平台里，它的位置很清楚：事实源提供可信上下文，Harness 提供 Agent 执行环境，状态机定义流程轨道，质量门定义完成条件，Loop 负责驱动其中可自动化的节点持续推进。

没有 Harness，Loop 只是危险的自动化。

没有事实源和质量门，Loop 跑得越快，团队越危险。

没有状态机和外部状态，Loop 跑久了就会变成一段失忆的长对话。

所以最后给一个决策规则：

`不要为了追概念而建设 Loop Engineering。只有当一个研发场景已经具备清晰触发器、可信上下文、受控执行器、可验证结果和明确停止条件时，才值得把它做成 Loop。`

这时候，它才不是噱头，而是 AI First 研发平台从“能调用 Agent”，走向“能稳定交付”的关键一步。
