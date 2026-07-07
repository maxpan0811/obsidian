---
title: "LLM 是最小那块 · Multi-Agent Harness 才是真护城河 · DeepSeek 9 子代理拆 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/LLM 是最小那块 · Multi-Agent Harness 才是真护城河 · DeepSeek 9 子代理拆 2.md
tags: [evernote, impression, yinxiang]
---

# LLM 是最小那块 · Multi-Agent Harness 才是真护城河 · DeepSeek 9 子代理拆

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247485296&idx=1&sn=7fd1a69f4dc819926464aa623c3a4dc7&chksm=f118c6af2309bca977e62563376367ac513156910bfe6bfe8b65aa170008c4516c7b68ecf728&scene=90&xtrack=1&req_id=1780011798927897&sessionid=1780011028&subscene=93&clicktime=1780011970&enterid=1780011970&flutter_pos=14&biz_enter_id=4&ranksessionid=1780011798&jumppath=1122_1780011850174,20020_1780011857275,1122_1780011951938,1104_1780011954010&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQRfy5h3mt8CUaKPZZZs9pdhLTAQIE97dBBAEAAAAAADVaKZGtA0EAAAAOpnltbLcz9gKNyK89dVj0uggVA1ZIKCu9YKRpdn0VU4l5dt6EbJ783OI4FPi3lHyyfec56EY7X1Q5pAIHiUIlPcwJamXhimQcdUfOxLMAzfX7EE0vmcG1kW1CsbqpqaNuvz8epD/4ooa8KQFfuuSi+WKmO4uhNugftYAse3zGcZdXbYdfkV+xo2eX1duluJLqxGhBISvWTmnVw8Sr8Gh/QkHzK1yKeEif4Al8ie9B/JWk4VZo6k0MIKW/qMo=&pass_ticket=FLVZ/Gaw+/UDNe3l72mI35vw6QJ2ByTpy1i2Gd8t3p+KtMUA/PrUzRkAEo0ngYYd&wx_header=3)

Original莲花明 AI落地手记

2026大模型圈的最大错觉
-------------

2026年AI圈最大的错觉:大家都觉得自己在卷模型。

GPT-5.5、Claude Opus 4.7、DeepSeek V3.2、Gemini 3 Pro、Kimi K3 ... 表面看是**模型军备竞赛**。

但5月以来,一连串事件透露真相:

· **5/16** · PwC选Claude Code整合Finance Business Group

· **5/19** · KPMG 27万员工部署Claude · Cowork + Managed Agents嵌入Digital Gateway

· **5/19** · Karpathy加入Anthropic · 不写代码 · 用Claude加速训Claude

· **5/20** · DeepSeek北京招聘组建「**Harness**」团队 · 直接对标Claude Code

· **5/26 Fortune**:四大AI噩梦 + 同一答案 = Claude嵌入平台

· **5/27 Simon Willison**:Anthropic + OpenAI终于找到PMF

从模型到部署到组织,一个新关键词反复浮现:**Harness**。

英文「束具 / 缰绳」· 在AI圈里特指**包在LLM外面的工程框架**。

真信号是:**大模型时代的真护城河不是模型 · 是harness**。这篇讲清楚这件事

§ 1 · 5/20 DeepSeek那条招聘启事的真正分量

━━━ KEY SIGNAL · 2026-05-20 ━━━

DeepSeek北京招聘 · 组建Harness团队

研究员Deli Chen招聘启事(节选)

"招产品经理 + 研发工程师 · 加入Harness团队 · 北京 · 目标:打造首方代码代理 · 对标Anthropic Claude Code / OpenAI Codex / Cursor"

Harness2026行业新核心概念 · 包在LLM外面的工程层

46%906工程师调研中Claude Code 「最爱」占比(2026 Q1)

40%Gartner预言:2026年底企业应用含AI Agent占比

110+Agent Harness学术论文(2026综述统计)

图1 · 5/20 DeepSeek招聘 + 关键背景数字

### 1.1招聘JD里藏着行业拐点

DeepSeek 5/20这条招聘启事,中文圈很多公众号简单当「DeepSeek想做Claude Code替代品」转发。

深一层看:**DeepSeek这家以模型起家的公司,公开承认「光做模型不够」**。

而DeepSeek是行业里最不需要「证明模型强」的公司之一 —— V3.2 + R1在多个基准测试持平甚至超GPT-4o。

一家「模型最强」的公司主动招产品 + 工程团队搞harness · 说明:

*"****从模型战转向工程战****是行业共识 · 不是某家公司的战术选择 · 是所有头部都意识到了的方向。"*

### 1.2同一时间发生的其他信号

· **2026 Q1调研**:906软件工程师参与 · **Claude Code 46% most loved** · 第二名Cursor 27%

· **Gartner预言**:2026年底**40% 企业应用**含task-specific AI agent

这些数据合起来,是一个明确指向:**harness不是噱头 · 是2026的新基础设施**。

---

§ 2 · Multi-Agent Harness到底是什么 · 学术定义
-------------------------------------

「Harness」中文翻译有几种 —— 「束具」「缰绳」「装具」。AI圈里没有特别好的中文译法 · 业界一般直接用英文。

简单说:**Harness = 包在LLM外面的工程框架 · 让LLM能完成真实任务而不止于聊天**。

🧩 Agent Harness 6 Components · 学术定义(E/T/C/S/L/V)

E Execution Loop · 执行循环

Plan → Act → Observe → Reflect · 让LLM闭环跑事

T Tools · 工具层

文件读写 / Shell / API调用 / MCP等扩展能力

C Context · 上下文管理

记忆 / 知识库 / 历史会话 / Skills加载

S State · 状态管理

任务状态 / 检查点 / 回滚 / 子任务协调

L Limits · 权限边界

敏感操作守护 / 写权限沙盒 / 速率限制

V Verification · 验证层

执行结果验证 / 测试 / Lint / 安全扫描

💡 **缺任何一个component · 都不算「生产级harness」** · 这是110+ 学术论文综述结论

图2 · Agent Harness 6 components · 缺一不可的工程框架

### 2.1 6个components各自的意义

**E · Execution Loop** · 执行循环

LLM默认是一问一答。Agent需要的是「连续多步骤」 —— 规划 → 行动 → 观察结果 → 反思 → 继续。这个循环就是E。Claude Code的task / Cursor的Composer / OpenAI的Agent SDK都在做这件事。

**T · Tools** · 工具层

让LLM能调用真实世界的能力 —— 读写文件、跑shell命令、调API、查数据库。2024-2025业界统一标准是**MCP(Model Context Protocol)**,Anthropic推出后业界全部跟进。

**C · Context** · 上下文管理

Agent跨多次会话要记得「我之前做过什么」· 跨项目要带「公司规则」 —— 这就是Skills(团队最佳实践)+ CLAUDE.md(项目级规则)+ Memory(跨会话记忆)。

**S · State** · 状态管理

多步骤任务里,每一步的状态(成功 / 失败 / 待重试 / 子任务派发)需要被显式管理。SubAgents设计 / 检查点 / 回滚都属于S。

**L · Limits** · 权限边界

agent默认会乱搞 —— 删错文件 / 调外网API烧钱 / 把客户数据传出去。Limits是给LLM套缰绳,常见做法是Hooks(Anthropic)/ Permissions(各家)/ Sandbox(OpenAI Codex云端)。

**V · Verification** · 验证层

agent跑完一步要验证「真的对吗」 —— 跑测试、跑Lint、跑安全扫描、跑PR review。这是从「demo跑通」到「生产可信」最难的一步。

### 2.2缺一不可 · 为什么

⚠️ **缺E**:agent只能一问一答 · 不能多步骤

⚠️ **缺T**:agent只能聊天 · 不能真做事

⚠️ **缺C**:agent每次都失忆 · 跨会话没记忆

⚠️ **缺S**:多步骤任务中间失败就崩 · 没法重试

⚠️ **缺L**:agent会乱搞 · 删错文件 / 烧钱 / 数据泄露

⚠️ **缺V**:跑完不知道对不对 · 错误链式累积

**所以业界共识:缺任何一个 · 都不是「生产级harness」**

---

§ 3 · 一句话 · LLM是最小的那块
---------------------

📊 MongoDB 5月Medium那篇原话 · 重新看Agent系统

*"****The LLM is the smallest part of your agent system.****"*

译:LLM是你Agent系统里最小的那块。

🎯 一个生产级Agent系统 · 工作量分布(经验估算)

10-15% · LLM本身(选哪个模型 / 提示词)

30-40% · Tools + Context + State(E/T/C/S)

25-35% · Verification + Limits(V/L · 真正难的地方)

15-20% · 集成 + Observability + 持续优化

图3 · Agent系统工作量 · LLM是占比最小的那块

MongoDB工程团队5月发了一篇深度博客 · 标题就是上面那句:

「**The LLM is the smallest part of your agent system.**」

这句话很多人乍听以为是PR话术 —— 不就是想推自己MongoDB Atlas Vector嘛?

但仔细看他们的论证,确实有道理:

### 3.1真实生产agent系统工作量分布

· LLM本身(选模型 + 提示词) · **10-15%**

· Tools + Context + State(E/T/C/S) · **30-40%**

· Verification + Limits(V/L · 最难的部分) · **25-35%**

· 集成 + Observability + 持续优化 · **15-20%**

换算:**85-90% 的工作量在LLM之外**。

而且LLM本身这10-15% 的工作量 · 90% 的时间是在**测哪个模型最适合自己的场景** · 不是在「调模型」。

### 3.2为什么这件事改变一切

🎯 **关键认知**

如果LLM只占15% · 那么换一个模型 · 系统能力天花板只升5-10%

但如果harness占85% · 升级harness · 系统能力天花板能升50-200%

**这就是为什么Claude 4.5 → 4.7体感升级有限**

**但用上Skills + Hooks + Subagents后体感升级巨大**

差别不在模型 · 在harness。

---

§ 4 · DeepSeek Harness 9子代理拆解
-----------------------------

DeepSeek 5/20的招聘JD + 后续业界根据V3.2开源工具栈推测 · 基本能拼出一个9子代理的雏形:

🤖 DeepSeek Harness 9子代理拆解(业界推测版)

🧠 Planner

拆解任务为可执行子目标

⌨️ Coder

写代码 / 改代码 / 文件操作

🔍 Searcher

代码搜索 / 文档检索 / RAG

🧪 Tester

跑单元测试 / 集成测试 / 报错收集

👁 Reviewer

代码review / 风格检查 / 提建议

🐛 Debugger

复现 / 假设 / 验证 / 修复

📝 Documenter

写docstring / 更新README / 生成changelog

⚡ Optimizer

性能优化 / 重构建议 / 复杂度降低

🛡 Guardian

权限守护 / 敏感操作拦截 / 安全扫描

💡 9个子代理是**业界根据DeepSeek招聘JD + 开源V3.2工具栈推测** · 不是官方公开架构

图4 · DeepSeek 9子代理 · 国产Claude Code雏形

### 4.1对比Claude Code的设计哲学差异

Claude Code的设计:**一个主代理 + Subagents按需启动**。

主代理读CLAUDE.md + Skills后,根据任务自己决定要不要起subagent。subagent跑完返回结果给主代理 · 主代理继续。

DeepSeek Harness的(推测)设计:**9个角色化子代理 · 按角色明确分工**。

这两种哲学各有优势:

· Claude Code 「主-从」结构:灵活 · 适合不确定任务 · 但调度复杂

· DeepSeek 「角色化」结构:明确 · 适合可预测任务 · 但灵活度低

从2024-2025业界总结来看 · 这两种结构最后都会演化成「**动态主-从 + 角色化补充**」的混合。AutoGPT 2024走纯角色化 · Claude Code 2025走纯主从 · 2026看上去要往中间走。

### 4.2 DeepSeek Harness真出来后的影响

两个直接影响:

**① 国内AI Coding工具生态升级**:目前国内首选是通义灵码 + Cursor中国版 · DeepSeek Harness真出 · 会成第三个主力。性价比和合规优势对国企 / 政企特别有吸引力。

**② 国际工具开始重视「角色化」**:Claude Code / Cursor / Codex接下来6-12月会重新看「9子代理 = 是否值得吸收」 · 类似2024年Cursor看Cline加入Composer类设计。

---

§ 5 · 6大Multi-Agent Harness横评
-----------------------------

国外3强 + 国内3跟 · 各有定位 · 选型看场景:

🛠 6大Multi-Agent Harness横评(2026 Q2)

Claude Code · Anthropic

综合成熟度★★★★★

💡 Skills + MCP + Hooks · CLI编排 · 商业最成熟

OpenAI Codex · OpenAI

综合成熟度★★★★

💡 云端沙盒 + 并行任务 · GPT-5.5加持 · 适合大规模重构

Cursor · Anysphere

综合成熟度★★★★

💡 IDE内嵌 · Composer + Background Agent · 日常编码最顺

DeepSeek Harness · DeepSeek

综合成熟度★★★(预)

💡 招聘期 · 9子代理推测 · 国内合规优势 · 性价比待打

通义灵码Lingma · 阿里通义

综合成熟度★★★

💡 VSCode插件 + CLI · @ 工作空间感知 · 国内大厂背书

Aider · 开源社区

综合成熟度★★★

💡 纯CLI开源 · Git原生集成 · 个人开发者首选

🎯 国外3强(Claude / Codex / Cursor) · 国内3跟(DeepSeek / 灵码 / + 后续Kimi) · **下半年国内会出更多**

图5 · 6大Harness横评 · 国外成熟国内追赶

### 5.1选型决策树

🎯 **简化选型逻辑**

· **个人 / 小团队 + 海外业务** · Claude Code(综合最成熟) + Cursor(日常编码) 组合

· **个人 / 小团队 + 国内业务** · 通义灵码 + DeepSeek API · 性价比最高

· **大企业 + 海外** · Claude Code(主力) + OpenAI Codex(并行重构)

· **大企业 + 国内 / 政企** · 等Q3 DeepSeek Harness正式版 · 或现在用通义灵码企业版

· **开源 / 自托管 / 极致省钱** · Aider + 自托管DeepSeek V3.2

---

§ 6 · 三圈信号 · 不只是开发者新闻
---------------------

🎯 三圈通吃 · 开发者 / CTO / 中小企业 各自路径

👨‍💻 AI开发者

01别只学prompt · 学搭harness(用Claude Skills / MCP / Hooks是入门门槛)

02练「6 components思维」· 拿到一个agent需求先想E/T/C/S/L/V都有没有

03开源awesome-harness-engineering仓库刷一遍 · 选3个深度阅读

04自己跑通一个mini-harness项目(50-200行)· 比看100篇文章值钱

05面试时讲「我搭过的harness是什么样」· 比讲「我会用Claude」高级3个级别

💼 企业CTO / 技术老板

01评估供应商 / 工具:不只看「用了什么LLM」· 看「harness 6 components各打几分」

02团队建设KPI:从「能用AI写代码的开发者」转向「能搭mini-harness的开发者」

03国产vs国际选型:Q3-Q4看DeepSeek Harness是否真出 · 性价比和合规优势可能改写决策

🏢 中小企业 / 个体开发者

01不用等DeepSeek Harness · 现在用Claude Code + MCP + Skills已能搭mini-harness

02选1个具体业务场景(客户咨询 / 内容生成 / 数据分析)做闭环 · 别贪大

03本文 § 6给5步可抄路径 · 含工具栈 + 真实账本 · 3个月跑通

图6 · 三圈信号 · 开发者5 / CTO 3 / 中小企业3可抄

### 6.1 AI开发者 · 别只学prompt

如果你是AI开发者 · 接下来12个月最值得练的不是「写更好的prompt」· 是「**搭一个mini-harness**」。

过去2年prompt工程师 / AI编排师这种岗位招聘大量出现 · 但工资差异巨大:

· 只会写prompt的 · 月薪1.5-3万

· 会搭harness的(用Skills / MCP / Hooks跑通真实业务) · 月薪4-10万

· 能设计企业级multi-agent架构的 · 月薪10-30万 + 期权

差别就在**有没有6 components的工程化思维**。

### 6.2 CTO / 老板 · 评估维度要更新

如果你是技术CTO或老板 · 接下来评估两件事:

**① 选工具时不只看LLM**

过去18个月CTO选AI工具最常问的:「用了哪个模型?GPT-5还是Claude?」

未来12个月该问:「**harness 6 components各打几分**?」「Skills生态有多大?」「MCP兼容度?」「Hooks灵活度?」「Verification怎么做?」

**② 团队建设KPI转向**

过去KPI:团队里有多少开发者用上了AI工具(席位数)。

未来KPI:团队里有多少开发者**搭过自家mini-harness** · 业务流程能被agent跑通的比例。

### 6.3中小企业 · 现在就能开干

看到「Multi-Agent Harness」「6 components」「9子代理」这些词 · 中小企业老板第一反应可能是:「太高级 · 跟我没关系」。

错。**现在用Claude Code + MCP + Skills · 已经能搭一个mini-harness跑通真实业务**。

不用等DeepSeek出 · 不用等谁出。具体怎么搭 · § 7给。

---

§ 7 · 中小企业5步搭mini-harness · 用Claude Code跑通
------------------------------------------

📋 中小企业5步搭mini-harness · 用Claude Code跑通

STEP 1选场景 + 定6 components

选一个具体业务(客户咨询 / 内容生成 / 数据分析)· 列出E/T/C/S/L/V各自要做啥

▼

STEP 2 Tools层

MCP servers(知识库 / 数据库 / API)· 5-10个工具够用 · 别贪多

▼

STEP 3 Context层

Skills(团队最佳实践markdown文件夹)+ CLAUDE.md(项目规则)+ 知识库RAG

▼

STEP 4 Verification + Limits

Hooks拦截敏感操作 · 自动跑测试 / Lint · 写权限沙盒

▼

STEP 5 Observability + 闭环

记录每次agent跑的step · 周复盘 · 不断打磨prompt + skills

💰 一个虚构案例账本(20人SaaS创业公司)

配置:Claude API月成本 ¥6,000 + Qdrant自托管 ¥800 + 5个MCP服务器 + 12个skills · 一次性集成 ¥3万

团队效率:研发交付速度**2.5×** · 客服响应时间**2小时** → **10分钟**

商业指标:同样20人 · ARR从 ¥600万涨到 ¥1500万 · 净利率 +20pt · 3个月部署 + 6个月磨合

图7 · 中小企业5步mini-harness + 虚构账本

### 7.1为什么是这5步 · 顺序很重要

看到5步可能觉得「就是装个Claude Code嘛」 · 但顺序和重点不一样。

**STEP 1选场景 + 定6 components**

选具体场景之前 · 先在纸上画一张表:E / T / C / S / L / V各自要做啥。如果你画不出来 · 说明场景没想清楚 · 别开干。

举例:做一个「客户咨询自动响应」 agent —

· E:收到客户问题 → 检索知识库 → 生成回答 → 客户确认 → 归档

· T:企微消息读写 + RAG检索 + 客户档案查询 + 工单创建

· C:历史咨询(Memory) + FAQ(Skills) + 客户档案(Context)

· S:每个对话的状态(待回复 / 已回复 / 转人工)

· L:敏感操作(打折 / 退款承诺)必须转人工 · 不允许agent直接回

· V:回答前必查「是否有客户专属合同条款冲突」

这张表画清楚 · 后面4步基本是体力活。

### 7.2 STEP 2-3 · Tools + Context · 工具栈推荐

🛠 **2026中小企业mini-harness推荐栈**

· **Harness主体**:Claude Code(CLI编排 · Skills + MCP + Hooks全套)

· **LLM**:Claude(高质量)+ DeepSeek API(国内合规 / 便宜)双路

· **向量库**:Qdrant自托管(高性能)/ Milvus云版(国内)

· **MCP Servers**:开源市场已200+ · 找5-10个匹配业务的即可

· **Skills**:团队最佳实践markdown · 跨项目复用 · 一次写多次用

· **集成**:钉钉 / 飞书 / 企微 + Webhook接Claude Code入工作流

### 7.3 STEP 4-5 · Verification + Observability · 闭环关键

搭完前3步只是demo · 4-5步才是「敢上生产」。

**STEP 4 Verification + Limits**:Hooks拦敏感操作(打折 / 退款 / 删除客户数据) · 写权限沙盒(不让agent直接改生产库) · 自动跑测试 / Lint。

**STEP 5 Observability + 闭环**:每次agent跑完记录step trace · 周复盘看「哪些step频繁失败」 · 反推改prompt / 改skills / 改tools。

### 7.4真实账本(虚构 · 基于业界普遍数据反推)

20人SaaS创业公司 · 6个月跑通后:

· Claude API月成本 ¥6,000(主推理)+ DeepSeek API ¥1,500(国内合规备份)

· Qdrant自托管月成本 ¥800(2台32GB阿里云ECS)

· 一次性集成开发 ¥3万(2个工程师6周)

· 团队效率:研发交付速度**2.5×** · 客服响应**2h → 10min**

· 商业指标:ARR **¥600万 → ¥1500万** · 净利率**+20pt**

---

收尾 · 5/20招聘启事的真信号
-----------------

回到一开始的事件。

DeepSeek 5/20的招聘启事,表面上看是「中国AI公司想做Claude Code替代品」。

深一层看,是**整个行业从「模型战」正式转向「工程战」**的拐点。

再深一层看,是**2026年AI Coding / AI Agent的真护城河 · 不在模型 · 在Multi-Agent Harness**的产业共识形成。

最深一层看,是**未来12-36个月 · 谁能搭出最好的harness · 谁吃下AI应用层的大部分价值**的开始。

🎯 **一句话总结**

不是「DeepSeek学Claude Code的新闻」

是「**大模型时代真护城河浮现 · 从模型转向工程**」

AI开发者要练「搭mini-harness」

CTO / 老板要更新「评估维度 + 团队KPI」

中小企业5步可抄路径 · 3个月跑通mini-harness

同一件事 · 三圈通吃。

今天先看清这件事的真实意义。具体怎么动 · § 6三圈 / § 7 5步都已经给到了。

剩下的是 —— **这周你能开始画的那张E/T/C/S/L/V表是什么**。

— END —

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247485296&idx=1&sn=7fd1a69f4dc819926464aa623c3a4dc7&chksm=f118c6af2309bca977e62563376367ac513156910bfe6bfe8b65aa170008c4516c7b68ecf728&scene=90&xtrack=1&req_id=1780011798927897&sessionid=1780011028&subscene=93&clicktime=1780011970&enterid=1780011970&flutter_pos=14&biz_enter_id=4&ranksessionid=1780011798&jumppath=1122_1780011850174,20020_1780011857275,1122_1780011951938,1104_1780011954010&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQRfy5h3mt8CUaKPZZZs9pdhLTAQIE97dBBAEAAAAAADVaKZGtA0EAAAAOpnltbLcz9gKNyK89dVj0uggVA1ZIKCu9YKRpdn0VU4l5dt6EbJ783OI4FPi3lHyyfec56EY7X1Q5pAIHiUIlPcwJamXhimQcdUfOxLMAzfX7EE0vmcG1kW1CsbqpqaNuvz8epD/4ooa8KQFfuuSi+WKmO4uhNugftYAse3zGcZdXbYdfkV+xo2eX1duluJLqxGhBISvWTmnVw8Sr8Gh/QkHzK1yKeEif4Al8ie9B/JWk4VZo6k0MIKW/qMo=&pass_ticket=FLVZ/Gaw+/UDNe3l72mI35vw6QJ2ByTpy1i2Gd8t3p+KtMUA/PrUzRkAEo0ngYYd&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b748317b-bc73-48e1-9b84-17fb11484e82/b748317b-bc73-48e1-9b84-17fb11484e82/)
