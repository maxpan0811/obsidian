---
title: Claude Opus 4.8上线：Dynamic Workflows+650亿美元融资
type: source
created: 2026-05-29
updated: 2026-05-29
sources: [刚刚，Claude Opus 4.8 上线，张口就说自己是 DeepSeek、Qwen.html]
source_path: 印象笔记管理工具/刚刚，Claude Opus 4.8 上线，张口就说自己是 DeepSeek、Qwen.html
tags: [anthropic, claude, opus, funding, dynamic-workflows]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "刚刚，Claude Opus 4.8 上线，张口就说自己是 DeepSeek、Qwen"
source: evernote
type: note
export_date: 2026-06-27
guid: e743bcf0-aeef-4f00-966d-68f7d96001f4
---

# 刚刚，Claude Opus 4.8 上线，张口就说自己是 DeepSeek、Qwen

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5MjAyNDUyMA==&mid=265109...](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=2651092743&idx=1&sn=a13ba312db7e689c31174815bb7147ff&chksm=bcee52b8be191bc64edfb63ec7522ac0487b7d5d93d4779c718224073f6775f77b9362538d1c&scene=90&xtrack=1&req_id=1780011025347057&sessionid=1780011028&subscene=93&clicktime=1780011211&enterid=1780011211&flutter_pos=1&biz_enter_id=4&ranksessionid=1780011025&jumppath=1001_1780009610876,1104_1780011029353,20020_1780011032812,1104_1780011203267&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAhwAjq8IJ+QgNaIerkNlxhLTAQIE97dBBAEAAAAAAFRUOHYP7ZkAAAAOpnltbLcz9gKNyK89dVj0fI/9peOtkHe49TzNjPD3ZTau+zEiHIVk4avtdsGxVy8Jne450haUfUqJipSFR69C/fBkASrbEybk21+PXHQkZ+Uiba0RJT3UtsAhXPNXhcGYzyvLqtPMO/3yu/HUapMnXhX1YU+LX3hacVc2E8S/WD0HWOZlDZLkfq8z1R2PjeHtRjYcpZDx6IykzsbUvAMy5WdshPcg09wJwiR/TuOhJwx52/VeCZ7vCYGxRLA=&pass_ticket=oKJsAinTPt4QC+T0/yGxLxwTimlfBOyE+vTtbdzJW1HP/JwdT9RYLBv2y8krhKsd&wx_header=3)

Original发现明日产品的 APPSO

伴随着 IPO 预期升温，Anthropic 产品模型的节奏也愈发加快。就在刚刚，Anthropic 接连发布两条重磅消息：一是将旗舰模型升级为 Claude Opus 4.8，二是完成 650 亿美元的 H 轮融资，投后估值达到 9650 亿美元，已逼近万亿美元关口。

![](attachments/ca256997e16cabb5.png)

对于一家估值已经逼近万亿美元的 AI 公司来说，市场要看的也不再只是模型跑分，而是它能否把智能、工具、开发环境、云平台和算力资源变成一套可规模化交付的基础设施。换句话说，Anthropic 必须从一家交付好模型的公司，逐渐转向为一家试图重塑企业 AI 工作方式的公司。加量不加价，Claude Opus 4.8 正式登场此次发布的 Claude Opus 4.8，是 Anthropic 对旗舰模型 Opus 系列的一次升级。照目前这个模型发布节奏，用网友调侃的话来说，我们大概率能在 GTA 6 发布(不跳票的话，11 月)之前，率先看到 Claude Opus 6。Anthropic 称，Opus 4.8 建立在 Opus 4.7 基础上，在编码、智能体任务、推理和知识工作等方面均有提升，并且已经面向用户开放，标准使用价格保持不变，仍为每百万输入 token 5 美元、每百万输出 token 25 美元。开发者也可以通过 Claude API 使用 claude-opus-4-8。

![](attachments/3e0f91dfb76f49ae.png)

API 价格对比🔗 https://platform.claude.com/docs/en/about-claude/models/overview从官方披露的信息看，Opus 4.8 的改进覆盖编码、智能体能力、推理能力和实际知识工作任务。Anthropic 在发布材料中用一张对比表展示了 Opus 4.8 与前代 Opus 4.7 以及其他模型在多项测试中的表现，当然，比起单次回答质量，模型的升级重点还是在长任务和复杂协作中的表现。

![](attachments/9de911827a9c34b6.jpg)

真实工作流里，模型往往需要连续处理多步任务，调用工具，检查中间结果，并根据反馈继续推进。Anthropic 表示，早期测试者认为 Opus 4.8 在执行智能体任务时更可靠，判断也更清晰。Opus 4.8 在诚实性上的提升是一大亮点。AI 模型常见的问题，是在证据不足时过早下判断，并自信声称已经取得进展。Anthropic 称，Opus 4.8 更愿意说明工作中的不确定性，也更少作出缺乏支撑的判断。代码任务尤其能体现这种变化。内部评估显示，Opus 4.8 让自己写出的代码缺陷未经说明地通过的概率，约为前代的四分之一。也就是说，新模型在发现风险时更可能提醒用户，而不是把问题留到后续测试或生产环境中。

![](attachments/7eaf341b63d4cb99.jpg)

在对齐和安全方面，Anthropic 延续了自己的核心叙事。Opus 4.8 在欺骗、配合滥用等不对齐行为上的发生率明显低于 Opus 4.7，并接近目前对齐表现最好的模型之一 Claude Mythos Preview。安全、可靠、可控，仍然是 Anthropic 用来区分自身的一组关键词。随着 Claude 更深地进入企业流程，这些关键词也开始承担更多商业意义。不过有意思的是，Opus 4.8 发布后，就被网友发现有些不对劲。

![](attachments/f5ead8d1e736eebc.png)

🔗https://x.com/realNyarime/status/2060059543820963975不少网友测试发现，当他们追问 Opus 4.8 的模型身份时，它给出的答案并不总是 Claude。

![](attachments/58c1f241a21bd921.png)

有时它会把自己认成 Qwen，有时又会报出 DeepSeek 的名字，疑似存在蒸馏的行为。

![](attachments/4324e59884a229b8.png)

而当网友在 Claude 官方客户端里提出同样问题时，这类回答通常又不容易复现。原因大概率在于，客户端里的系统提示词和产品层约束更完整。

![](attachments/fea38ba42db6a290.png)

动态工作流上线，Claude Code 走向多 agents 协作伴随 Claude Opus 4.8 一同上线的，还有多项产品和开发者功能。其中，最直接影响 Claude 用户体验的当属 effort control，也就是思考强度调节。控制项位于模型选择器旁边，顾名思义，用户可以决定 Claude 在一次任务中投入多少推理算力。较高强度下，Claude 会进行更多推理，以换取更好的回答质量；较低强度下，Claude 响应更快，使用额度消耗也更慢。

![](attachments/c6287b23a4e06b05.png)

Anthropic 表示，Opus 4.8 默认采用 high effort，用户还可以选择 extra，在 Claude Code 中对应 xhigh，或者选择 max，让模型投入更多 token。Anthropic 建议，困难任务和长时间运行的异步工作流更适合使用 extra。真正影响 Claude Code 产品形态的，是 dynamic workflows。该功能目前处于 research preview，目标是让 Claude Code 处理过去需要更长工程周期的大规模任务。以往按季度规划的工作，现在甚至有机会在数天内完成。

![](attachments/e3ae2cefbf307ced.png)

dynamic workflows 的核心机制是，Claude 会根据用户任务动态编写 orchestration scripts，并在单个会话中运行数十到数百个并行 subagents。模型会先规划任务，再分配给多个 subagents，随后检查返回结果，最后向用户汇报。Opus 4.8 上线后，这些 agents 还可以运行更长时间。

![](attachments/87455866b55783b1.png)

该功能主要面向复杂、庞大或历史包袱较重的代码库。典型场景包括全服务范围内查找 bug、性能优化审计、安全审计、大型代码库迁移、框架替换、API 废弃迁移、语言移植，以及对关键方案进行多角度验证。

![](attachments/46da804a110d6355.jpg)

使用方式上，Anthropic 建议在 dynamic workflows 中打开 auto mode。用户可以直接要求 Claude 创建 workflow，也可以在 Claude Code 中打开 ultracode。ultracode 会把思考强度设为 xhigh，并让 Claude 自动判断当前任务是否适合使用 workflow。dynamic workflows 当前已经在 Claude Code CLI、Desktop 和 VS Code extension 中开放，面向 Max、Team 和 Enterprise 套餐。其中 Enterprise 在发布时默认关闭，需要管理员在 Claude Code 设置中启用。该功能也可用于 Claude API、Amazon Bedrock、Vertex AI 和 Microsoft Foundry。对于 Max、Team 用户，以及通过 API 使用 Claude Code 的用户，dynamic workflows 默认开启。

![](attachments/4042923a0d6b8203.png)

Anthropic 用 Bun 迁移案例展示了 dynamic workflows 的上限。Jarred Sumner 使用该功能将 Bun 从 Zig 移植到 Rust，最终生成约 75 万行 Rust 代码，现有测试套件通过率达到 99.8%，从首次提交到合并约用了 11 天。整个迁移过程由多个 workflow 完成：先为 Zig 代码库中的 struct 字段映射 Rust lifetime，再为每个 .zig 文件生成行为一致的 .rs 文件，数百个 agents 并行工作，每个文件都有两个 reviewer。之后，fix loop 持续运行 build 和 test suite，直到构建和测试通过。迁移完成后，又有 overnight workflow 处理不必要的数据复制问题，并为每类问题打开 PR，供最终审查。

![](attachments/56e17afa73c87698.gif)

除了 Claude Code，Anthropic 还更新了 Messages API。现在，Messages API 可以在 messages array 内接受 system entries。开发者可以在任务执行过程中更新 Claude 的指令，同时不破坏 prompt cache，也不必通过 user turn 传递更新。这一能力可用于 agent 运行时更新权限、token 预算或环境上下文。下一步，Anthropic 还计划推出一个比 Opus 智能水平更高的新模型类别。没错就是那个强的可怕的 Claude Mythos Preview，预计未来数周内可以把 Mythos class models 带给所有客户。到时候，我们也将第一时间尝尝咸淡。

![](attachments/7eaf341b63d4cb99.jpg)

近万亿美元估值背后，Claude 需要更大的算力底座与 Claude Opus 4.8 同日发布的另一条消息，是 Anthropic 完成 650 亿美元 H 轮融资。本轮由 Altimeter Capital、Dragoneer、Greenoaks 和 Sequoia Capital 领投，投后估值达到 9650 亿美元。

![](attachments/d89d2beffe1be080.png)

本轮融资还包括 hyperscalers 的 150 亿美元既有承诺投资，其中包括亚马逊的 50 亿美元。Micron、Samsung、SK hynix 等战略基础设施伙伴也加入其中。Anthropic 称，这些公司在全球 memory、storage 和 logic chips 供应中具有关键作用，能帮助其随着 Claude 需求增长扩大计算能力。算力扩张是本轮融资背后的关键背景。Anthropic 披露了多项基础设施协议：与亚马逊签署协议，获得最高 5 吉瓦新增容量；与 Google 和 Broadcom 签署协议，获得 5 吉瓦下一代 TPU 容量；与 SpaceX 达成协议，可使用 Colossus 1 和 Colossus 2 中的 GPU 容量。

![](attachments/157f950c3ec0b639.png)

Anthropic 还强调，Claude 是首个同时进入 AWS、Google Cloud 和 Microsoft Azure 三大云平台的前沿模型。不过，AWS 仍是 Anthropic 的主要云服务商和训练合作伙伴。融资的背后，其实是 Anthropic 商业定位的变化。早期大模型公司比拼的是模型能力和通用聊天体验，而现在企业客户更关心的是 AI 能否进入核心流程，能否处理复杂任务，能否被接入开发环境、云平台和内部系统。Claude Code、Cowork、effort control、dynamic workflows 和 Messages API 更新，都在围绕这个方向展开。

![](attachments/dbef1a8d3ca7d4c6.gif)

把产品发布和融资放在一起看，Anthropic 正在同时扩张三类能力。第一是模型能力，Opus 4.8 提高了编码、推理、智能体任务和知识工作表现，并强化了对不确定性的表达。第二是工作流能力，dynamic workflows 让 Claude Code 从单次代码辅助走向更复杂的工程执行和审查。第三是基础设施能力，650 亿美元融资、超大规模云厂商承诺投资、内存和芯片伙伴加入，以及与 Amazon、Google、Broadcom、SpaceX 的算力协议，为后续模型训练和推理需求提供资源。

![](attachments/65e9a567127029b2.jpg)

这也是 Anthropic 估值逼近万亿美元的核心逻辑。Claude 不再只是一个 AI 聊天窗口，而是正在成为连接模型、代码、企业流程、云平台和算力基础设施的工作系统。Opus 4.8 是这套系统中的最新模型底座，dynamic workflows 是面向复杂工程任务的产品形态，650 亿美元融资和算力扩张则是继续把这套系统推向更大规模客户的前提条件。AI 的潮水把 Anthropic 推到了浪尖，站在这个高度，往前是乘风，往后是沉船落水，没有第三种姿势。*\*封面由 AI 生成*
