# 人人都有Fable 5：用agentfw把DeepSeek+Kimi+Qwen融合成Fable 5平替模型

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c14fbbe3f63832f5fe49b8fdd88964f...](https://mp.weixin.qq.com/s?chksm=c14fbbe3f63832f5fe49b8fdd88964f3c9ca8ffccfd6482bca76b78c4fa35c48228c250ab4fe&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_1&req_id=1782031330553375&scene=169&mid=2247485582&sn=29c9dbe26c6d6663986b33b90449a88d&idx=1&__biz=MzkxNjQ5NzkyMg==&sessionid=1782032739&subscene=200&clicktime=1782033702&enterid=1782033702&flutter_pos=12&biz_enter_id=5&jumppath=WAWebViewController_1782033678959,WAWebViewController_1782033679461,20020_1782033700857,1104_1782033701389&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQyDuCNoE/veQwa3WrkK2pRBLTAQIE97dBBAEAAAAAAHhQBv4ScKUAAAAOpnltbLcz9gKNyK89dVj0cNOkRyaMXOUoXlfWTHoy15lK7z59u2VaxEeiVmfkAxe6gnLb1BqJkfdjtHOIgkKwjzwS6Ff5bim7x4M72GPuZWzcwPHQUB2EKyUrR3Hhmc84s/fosqwkOxVbg8Jv3B9CKp2rg2H5OuUtjpFRZgR13uTOdPY+tnpYmVK0iYdBpKEagWVUvbsYqkzhH4k8xBCwGCG+CxHvQXOsU3LKk9vcr2alDwul8Jy05fMm+oo=&pass_ticket=dZRdfa/wV693GMzaulSUsTzwL4E/bxT+b3Mykwzg1IfzBdkC+F+4zoZdeQ0wNKUW&wx_header=3)

Original值得关注的象信AI

![](.evernote-content/662B6A80-A91B-4A22-9D10-BD937A9ACAA5/F790E53D-3DC4-414D-A18A-B99F62133E99.jpg)

过去半年，大模型的竞争一直在往“更大、更贵、更强”走。

Fable 5 这类前沿模型当然强，但问题也很现实：价格高、调用成本高、在团队或高频 agent 场景里，长期用下来是一笔不小的开支。

OpenRouter 最近做了一个很有意思的实验：不再只问“哪个单模型最强”，而是让多个模型组成一个 Panel（专家小组），并行回答，再由一个 judge / synthesizer 把答案融合成最终结果。

结果很直接：

单个模型不是终点。

多个模型合体，很多时候比单模型更强。

OpenRouter 的结论：Fusion 能逼近甚至超过前沿模型
---------------------------------

OpenRouter 在 DRACO 深度研究基准上测试了 Fusion（融合模型）。

DRACO 是 Perplexity AI 提出的深度研究评测集，包含 100 个复杂任务，覆盖学术、金融、法律、医疗、技术、UX、产品比较等 10 个领域。它不是简单考记忆，而是考模型能不能搜索、理解、综合、引用，并产出真正有用的研究答案。

OpenRouter 的关键发现有三点：

1. 多模型 Panel 稳定强于单模型。
2. 前沿模型组队后，可以超过单个前沿模型。
3. 平价模型组队后，也能接近 Fable 5 这类顶级模型。

![](.evernote-content/662B6A80-A91B-4A22-9D10-BD937A9ACAA5/F6FE7DE2-0AF1-4F3B-9B1D-C8AE8BB13EEF.png)

DRACO benchmark scores for Fusion and solo configurations

原文数据里，Claude Fable 5 单跑的标准化得分是 65.3%。

而 Gemini 3 Flash + Kimi K2.6 + DeepSeek V4 Pro 的 Fusion 组合，得分达到 64.7%。

差距只有 0.6 个百分点。

更重要的是，OpenRouter 还指出，这组预算模型 Panel 的单任务成本大约只有 Fable 5 的一半。

![](.evernote-content/662B6A80-A91B-4A22-9D10-BD937A9ACAA5/AFE9AB81-D920-457A-B18A-05AA20A74921.png)

Score vs cost per task for Fusion and solo configurations

这件事给我们的启发很大：

Fable 5 不是一个只能“买更贵模型”才能获得的能力。

它也可以被拆成一套本地可控的协作流程。

开源的agentfw：把 Fusion 放到本地
------------------------

OpenRouter 的 Fusion 是云端服务。你调用 `openrouter/fusion`，它在服务端把请求分发给多个模型，再融合答案。

但对 agent 场景来说，我们更希望这个能力发生在本地。

原因很简单：

模型可以换。

供应商可以换。

路由策略可以改。

安全策略必须握在自己手里。

这正是 agentfw 适合做的事。

开源地址：**https://github.com/openguardrails/agentfw**

agentfw 是一个本地 AI agent firewall，站在 agent 和模型服务之间。它能看到请求、路由模型、保护敏感信息，并在本地对 agent 的模型调用做编排。

所以，Fusion 不一定非要长在云端。

它可以长在 agentfw 这一层。

![](.evernote-content/662B6A80-A91B-4A22-9D10-BD937A9ACAA5/38C55794-FC43-456B-A5EC-F335EA32D1D5.png)

本地 Fable 5 平替：DeepSeek V4 Pro + Kimi K2.6 + Qwen3.6
---------------------------------------------------

agentfw 推荐的本地 Fusion 阵容是：

**Qwen3.6 + Kimi K2.6 + DeepSeek V4 Pro**

这是一套偏工程实用的组合。

DeepSeek V4 Pro：负责推理、问题拆解、低成本高强度思考。

Kimi K2.6：负责代码、长上下文、中文理解、材料归纳和复杂文档消化。

Qwen3.6：负责稳定输出、结构化和多模态任务。

这三个模型不是简单轮流调用，而是分工协作：

同一个任务，agentfw 在本地并行发给三个模型。

三个模型各自给出答案、推理路径或候选方案。

本地 judge 对答案进行交叉检查：找共识、找冲突、找遗漏。

最后 synthesizer 生成一个统一答案。

这就是本地版 Model Fusion。

用户体感上，还是只调用一个“模型”。

但背后其实是三个开源模型在协作。

为什么 Fusion 会变强？
---------------

因为复杂任务往往不是单一能力问题。

一个模型可能事实覆盖更好，但表达一般。

一个模型可能推理更强，但容易漏掉边界条件。

一个模型可能中文更自然，但技术细节不够硬。

单模型回答时，这些弱点会直接暴露。

Fusion 的价值在于，它不是投票，而是综合。

它会把多个模型的答案拆开看：

哪些观点一致？

哪些地方互相矛盾？

谁补充了别人没看到的信息？

哪个答案看似自信但证据不足？

最终答案应该保留什么、删掉什么、修正什么？

这一步本质上是在给模型输出做“二次审稿”。

OpenRouter 原文里还有一个很有意思的现象：同一个模型和自己做 Fusion，也能涨分。Opus 4.8 与自己组成两模型 Panel 后，得分从单体 58.8% 提升到 65.5%。

这说明增益不只来自模型多样性，也来自“多次生成 + 综合裁决”这个流程本身。

agentfw 怎么做这件事？
---------------

在传统调用方式里，agent 只知道一个模型。

例如：

Claude Code 调 Fable 5。

Codex 调 GPT。

OpenClaw 调某个默认模型。

agentfw 介入后，模型调用会先经过本地防火墙层。

在这里，我们可以把“一个模型”替换成“一个 Fusion 策略”。

比如定义一个本地虚拟模型：

![](.evernote-content/662B6A80-A91B-4A22-9D10-BD937A9ACAA5/75E81C70-ABD9-4F5C-9F3E-E414E2C056BB.png)

agent 仍然以为自己在调用一个模型。

但 agentfw 会在本地完成：

请求复制。

并行分发。

结果收集。

冲突分析。

最终融合。

敏感信息保护。

调用轨迹记录。

这就把“模型能力”从单点变成了组合能力。

人人都有 Fable 5，不是人人都买 Fable 5
---------------------------

这里的重点不是说某个组合在所有场景都 100% 等于 Fable 5。

真正重要的是：

很多实际工作，不需要每次都调用最贵的单模型。

调研、代码 review、方案设计、长文归纳、产品分析、投研摘要、法律条款初筛，这些任务更需要的是多视角、可复核、低幻觉和稳定产出。

Fusion 正好适合这些场景。

用 agentfw 做本地 Fusion 后，团队可以把高价模型调用从“默认选项”变成“兜底选项”。

日常任务走 Qwen3.6 + Kimi K2.6 + DeepSeek V4 Pro。

高风险任务再升级到 Fable 5。

模型故障时自动切换。

敏感信息在本地先被 agentfw 处理。

所有调用路径都有迹可查。

这比单纯追逐最强模型，更像一套真正可落地的 AI 基础设施。

最后
--

OpenRouter 的 Fusion 实验说明了一件事：

未来的大模型能力，不一定只来自“更大的单模型”。

它也可能来自“更好的模型协作系统”。

Fable 5 很强。

但 Fable 5 不是唯一答案。

当 Qwen3.6、Kimi K2.6、DeepSeek V4 Pro 这样的开源模型被 agentfw 在本地组织起来，每个人都可以拥有一套自己的“Fable 5 平替”。

不是云端给你的黑盒能力。

而是跑在你本地、可路由、可审计、可保护、可替换的 AI agent firewall。

这才是象信AI想做的事情：

让强模型能力变得更开放。

让 agent 的控制权回到用户手里。

让人人都有自己的 Fable 5。

开源地址：**https://github.com/openguardrails/agentfw**

参考来源
----

OpenRouter Blog: Surpassing Frontier Performance with Fusion  
https://openrouter.ai/blog/announcements/fusion-beats-frontier/

DRACO paper  
https://arxiv.org/abs/2602.11685

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c14fbbe3f63832f5fe49b8fdd88964f3c9ca8ffccfd6482bca76b78c4fa35c48228c250ab4fe&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_1&req_id=1782031330553375&scene=169&mid=2247485582&sn=29c9dbe26c6d6663986b33b90449a88d&idx=1&__biz=MzkxNjQ5NzkyMg==&sessionid=1782032739&subscene=200&clicktime=1782033702&enterid=1782033702&flutter_pos=12&biz_enter_id=5&jumppath=WAWebViewController_1782033678959,WAWebViewController_1782033679461,20020_1782033700857,1104_1782033701389&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQyDuCNoE/veQwa3WrkK2pRBLTAQIE97dBBAEAAAAAAHhQBv4ScKUAAAAOpnltbLcz9gKNyK89dVj0cNOkRyaMXOUoXlfWTHoy15lK7z59u2VaxEeiVmfkAxe6gnLb1BqJkfdjtHOIgkKwjzwS6Ff5bim7x4M72GPuZWzcwPHQUB2EKyUrR3Hhmc84s/fosqwkOxVbg8Jv3B9CKp2rg2H5OuUtjpFRZgR13uTOdPY+tnpYmVK0iYdBpKEagWVUvbsYqkzhH4k8xBCwGCG+CxHvQXOsU3LKk9vcr2alDwul8Jy05fMm+oo=&pass_ticket=dZRdfa/wV693GMzaulSUsTzwL4E/bxT+b3Mykwzg1IfzBdkC+F+4zoZdeQ0wNKUW&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/45b96ae3-1ff1-4b38-a4db-83e0a26f7a53/45b96ae3-1ff1-4b38-a4db-83e0a26f7a53/)