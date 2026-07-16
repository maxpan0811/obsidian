---
title: 突发！Claude Opus 4.8深夜炸场，判断力大突破，梭哈Agent定了
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/突发！Claude Opus 4.8深夜炸场，判断力大突破，梭哈Agent定了.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "突发！Claude Opus 4.8深夜炸场，判断力大突破，梭哈Agent定了"
source: evernote
type: note
export_date: 2026-06-25
guid: 38d5ea78-3f1b-4f59-b1e4-0680b5305254
---

# 突发！Claude Opus 4.8深夜炸场，判断力大突破，梭哈Agent定了

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5MTg5NTU0MQ==&mid=265415...](https://mp.weixin.qq.com/s?__biz=MjM5MTg5NTU0MQ==&mid=2654156488&idx=1&sn=bab9b20fb0b7245ddc3624ee1ffe291b&chksm=bcbcd8aca83947c03de1ee4022ea18f9cc4aa798656d1ba5929944c074b9f530aee1f0cca02f&scene=90&xtrack=1&req_id=1780011033766180&sessionid=1780011028&subscene=93&clicktime=1780011406&enterid=1780011406&flutter_pos=3&biz_enter_id=4&ranksessionid=1780011033&jumppath=WAWebViewController_1780011368092,WAWebViewController_1780011368597,20020_1780011394202,1104_1780011395146&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQJq8UXcDqjThVlbLl11ksmxLTAQIE97dBBAEAAAAAAAnAOSrzWhQAAAAOpnltbLcz9gKNyK89dVj0PB7SQzNZY3LBFZW6nV8/M/2TpDpWObeAo9MBBtvX+qsgrGbDgN9cbE5Q+6g9jVDcL7SCNluKFcS1A0Egl+oVVXO+Zv4JxGMW48ZbscZfV8mgCsTDANJvaBvv9WrcQLT0UowD9rmj2/Y+vAZLO0bpKBOhMj4IzLaAq60TAmphgOh9IGpHepaLIZKkYHyGbj1J0XLQ7etFiZxO1mHXc45JqbBw77yiKkQk3Xmweas=&pass_ticket=QNKId4pYfVa9X0LXWYaRd09XvHs22tfQn/g/qn4zB6DsALNV0t7Qfh4hsq7tbjqP&wx_header=3)

Originalkkknei 雷科技

雷科技AI组 | 编辑：kkknei | 监制：罗超

千呼万唤，Cluade Opus 4.8 正式发布了。

北京时间 5 月 29 日凌晨，Anthropic 正式发布 Claude Opus 4.8，如果只看名字，Opus 4.8 很容易被理解成 Opus 4.7 后面的一次小版本更新，其实从官方释出的性能表来说，也确实如此。**比如 Terminal-Bench 2.1 上，GPT-5.5 的 78.2% 仍然高于 Opus 4.8 的 74.6%。**

![](attachments/f82781174f7a2406.jpg)

图源：Anthropic

不过，Anthropic 的真正杀招不只是 Claude Opus 4.8，而是随这个新旗舰模型一同释出，**包括 Claude.ai 的 effort control、Claude Code 的 dynamic workflows 的全新Agent能力。**

事实上，Anthropic 已经不再执着于让 Claude 变得更聪明了，而是选择让 Claude 变得更能干活了。

**判断力是Opus 4.8 的最大突破**

我们先来看看 Anthropic 这款最新旗舰模型 Claude Opus 4.8 的具体性能。

官方性能表里，Opus 4.8 在 Agentic Coding、Agentic Computer Use、Knowledge Work、Finance Agent 等多个项目上超过 Opus 4.7、GPT-5.5 和 Gemini 3.1 Pro。在 SWE-Bench Pro 上，Opus 4.8 是 69.2%，高于 Opus 4.7 的 64.3%；OSWorld-Verified 上，Opus 4.8 是 83.4%；GDPval-AA 上，Opus 4.8 得到 1890；Finance Agent v2 上，Opus 4.8 是 53.9%。

![](attachments/2247fad8f8c08ce1.jpg)

图源：Anthropic

简单来说，Opus 4.8 的核心升级是写代码、用终端、操作电脑、处理知识工作、做金融分析。更直白一点说，Opus 4.8 不是为“问答”而升级，而是为“代理执行”而升级。

过去一年，大家对 coding agent 最大的不满，并不是它完全不会写代码，而是它太自信了，比如你让它跑一个任务，它会说任务完成了，但测试没有真正跑通，还有它会把自己生成的代码缺陷放过去，甚至用很笃定的语气告诉你“一切正常”。换到问答里，那就是 AI 又一次“稳稳地接住了你”。

这类问题对聊天产品来说只是体验不太行，但对 agent 来说就是生产事故。

因为 agent 的本质不是回答，而是行动。一个会行动的模型，最可怕的不是能力不足，而是能力不足却不知道自己不足，**所以 Opus 4.8 的提升点很重要，它更愿意指出不确定性，愿意在证据不足时停下来，等待你补充完整信息再去行动。**官方甚至提到，Opus 4.8 让代码缺陷未经提醒通过的概率，比前代低了很多。

从官方早测反馈看，Cursor、Devin、Databricks、法律 AI、金融分析、浏览器 agent 等合作方也提到：

工具调用更干净，任务推进更稳，长程上下文保持更好，更适合无人值守或半无人值守的复杂工作。

另外，ClaudeDevs 官方账号对 dynamic workflows 做了连续解释：Claude Code 现在可以临时写 orchestration script，然后并行启动大量 coordinated subagents 来处理复杂任务。**官方还明确说，这类 workflow 适合 service-wide bug hunt、大型迁移、设计压力测试这类单 agent loop 很难完成的任务。**

![](attachments/bb36cd216394baca.png)

图源：Anthropic

Bun 作者 Jarred Sumner 表示， dynamic workflows 是目前可靠使用 agents 完成中大型项目的前沿方式之一，并提到 Bun 重写为 Rust 的过程中，dynamic workflows 和 adversarial code review 起到了重要作用。

不难看出，Opus 4.8 就不是一个单独拎出来很强的模型，它更重要的是在 Claude Code 这套 agent 系统里的核心执行模型。

与此同时，Anthropic 一同发布的几个新能力也很有意思，比如Claude.ai 新增的 effort control ，用户现在可以控制 Claude 在任务上“花多少力气”，有几个选项，低 effort 更快、更省；高 effort 更深、更适合复杂任务，Opus 4.8 默认的是 high effort，假如想要省一些 token，那最好手动切换回低 effort。

**5 月模型大混战：全员加速 Agent**

整个 5 月，AI 圈几乎是各家厂商各显神通。

OpenAI 继续强化 Codex，展示用 Codex 构建自改进税务智能体；Google 在 I/O 上发布一整套 AI agent 开发工具链；GitHub、Cursor、OpenAI 都在争夺企业级 AI 编程代理的位置；Replit Agent 开始和自动化 QA 结合；Luma Agents 用于规模化生成真实 UGC 广告；阿里云也在推 DataWorks AI 数据智能体和“全天候 AI 劳动力”。

国内模型侧也在继续高频迭代，比如Qwen3.7-Max 强调编程能力，智谱 GLM-5.1 高速版主打 API 速度，MiniCPM5-1B、BitCPM-CANN 继续往端侧、低比特、低成本方向推进，商汤和腾讯混元等也在快速更新迭代。

与此同时，价格战也在悄悄打响。

DeepSeek 再次降价，小米 MiMo 大模型也以极低价格入场，表面上看，这是 API 报价竞争，但实际上还是为了 Agent，因为 Agent 实在是太吃 tokens 了。

如果只是聊天，一次可能只消耗几百到几千 tokens，但 Agent 不一样，它要读上下文、拆任务、写计划、调用工具、执行代码、检查结果、修复错误，有时还要拉起多个 subagents 并行工作。**Claude Code 的 dynamic workflows 就是典型例子，官方自己也提醒它 powerful but expensive，会快速消耗大量 tokens。**

所以，token 价格战不只是为了让聊天更便宜，而是为了让 Agent 这种高消耗形态跑得起来。所以，就连 Anthropic 也不得不把 fast mode 的价格打到了前代的三分之一，来应对这样的高消耗。

![](attachments/1c0293df2322b1f8.jpg)

图源：Anthropic

**看起来，大家只是在按部就班更新模型，但似乎都遗漏了一点，那就是这些模型的核心已经不再是聊天，而是比谁更能进入真实工作流。**

**过去的大模型竞争，主战场是对话，谁回答得更自然，谁推理更强，谁上下文更长，谁多模态更好，现在主战场正在变成 agent。**

Agent 竞争的核心不是单次回答，而是连续执行，它要求模型会拆任务、会调用工具、会管理上下文、会处理权限、会控制成本、会复核输出，还要能在复杂环境中长时间不跑偏。

这也是为什么 Opus 4.8 的官方没有强调对话能力，而是把重点放在 agentic coding、computer use、knowledge work、financial analysis。因为 Anthropic 很清楚，未来最值钱的模型调用，不一定发生在聊天窗口里，而是发生在 IDE、终端、浏览器、数据平台、企业后台和各种自动化流程里。

![](attachments/140ea8fa25c8c47d.png)

图源：Anthropic

从这个角度看，dynamic workflows 可能比 Opus 4.8 本身更重要。因为它把 Claude Code 从“一个 AI 程序员”推向“一支 AI 工程队”。过去你让模型做任务，本质上是一个模型在一个上下文里循环。现在它开始能拆分任务、并行分配子代理、让不同 agent 互相验证，最后再汇总结果。

综合来看，5 月这场模型大混战，不只是“模型更强了”，而是“模型正在被允许做更多事”。

**Claude 一夜蜕变成工作流系统**

Opus 4.8 虽然在定位上是 Cludue 的旗舰模型，但还真算不上是一次“震撼全场”的模型发布。

它更像 Anthropic 给市场递出的一张路线图，这张路线图里，模型不能只追求更聪明，还要更稳；任务不能只完成一轮对话，还要能持续推进；AI 不能只给出答案，还要能解释过程、复核结果、控制成本，并且把工作流沉淀下来。这些都是未来所有大模型都要关注的点。

于是我们可以看到，Opus 4.8 负责把 Claude 的判断力和长程执行能力往前推一步，effort control 让用户可以在质量、速度和成本之间主动调节，dynamic workflows 则把 Claude Code 从单个 coding agent，推向一个可以拆任务、调度 subagents、并行执行和复核结果的工程协作系统。

**Claude 正在变成什么呢？答案已经很明显了，Claude 正在从一个聊天模型，变成一个工程协作系统。**

接下来，大模型公司的竞争也会越来越少停留在“谁更会说”，而是把目标放在更可靠地完成复杂任务、更便宜地支撑高频调用，把模型、工具、工作流、安全和成本控制，真正打包成生产力系统。

在这一方向上， Anthropic 已经交出了第一份答卷。

Opus名字来自拉丁语中的“作品”，常用来形容一位作曲家的传世之作（magnum opus，即“最伟大的作品”）。在古典音乐里，Opus 后面跟着编号，代表作曲家最重要的创作。贝多芬的《月光奏鸣曲》是 Op. 27，《命运交响曲》是 Op. 67。这不是随便写的东西，这是呕心沥血的集大成之作。

从引领加速AI产业进入工作流时代的意义来看，Cluade Opus 4.8确实堪称一个传世之作。

#AI#Claude#Agent

![](attachments/1820f3871e97a48d.png)

**End**


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5MTg5NTU0MQ==&mid=2654156488&idx=1&sn=bab9b20fb0b7245ddc3624ee1ffe291b&chksm=bcbcd8aca83947c03de1ee4022ea18f9cc4aa798656d1ba5929944c074b9f530aee1f0cca02f&scene=90&xtrack=1&req_id=1780011033766180&sessionid=1780011028&subscene=93&clicktime=1780011406&enterid=1780011406&flutter_pos=3&biz_enter_id=4&ranksessionid=1780011033&jumppath=WAWebViewController_1780011368092,WAWebViewController_1780011368597,20020_1780011394202,1104_1780011395146&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQJq8UXcDqjThVlbLl11ksmxLTAQIE97dBBAEAAAAAAAnAOSrzWhQAAAAOpnltbLcz9gKNyK89dVj0PB7SQzNZY3LBFZW6nV8/M/2TpDpWObeAo9MBBtvX+qsgrGbDgN9cbE5Q+6g9jVDcL7SCNluKFcS1A0Egl+oVVXO+Zv4JxGMW48ZbscZfV8mgCsTDANJvaBvv9WrcQLT0UowD9rmj2/Y+vAZLO0bpKBOhMj4IzLaAq60TAmphgOh9IGpHepaLIZKkYHyGbj1J0XLQ7etFiZxO1mHXc45JqbBw77yiKkQk3Xmweas=&pass_ticket=QNKId4pYfVa9X0LXWYaRd09XvHs22tfQn/g/qn4zB6DsALNV0t7Qfh4hsq7tbjqP&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/38d5ea78-3f1b-4f59-b1e4-0680b5305254/38d5ea78-3f1b-4f59-b1e4-0680b5305254/)
