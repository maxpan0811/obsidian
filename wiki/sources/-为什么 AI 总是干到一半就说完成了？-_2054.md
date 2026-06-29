---
title: "为什么 AI 总是干到一半就说完成了？"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/为什么 AI 总是干到一半就说完成了？.md
tags: [evernote, impression]
---

---
title: "为什么 AI 总是干到一半就说完成了？"
source: evernote
type: note
export_date: 2026-06-22
guid: 245c7d13-1105-44ce-8597-ac6f2e92efbb
---

# 为什么 AI 总是干到一半就说完成了？

原文链接: [https://mp.weixin.qq.com/s?chksm=f0932ec9c7e4a7df6c61bc3d9174537...](https://mp.weixin.qq.com/s?chksm=f0932ec9c7e4a7df6c61bc3d9174537490a9cfbd09e58eb85c069e182f207490c9a9cb1f30eb&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782029952_1&req_id=1782029952718987&scene=169&mid=2247484030&sn=80cdf26669dc65ed74295552d7f83515&idx=1&__biz=MzYzNTI1NjI4MA==&sessionid=1782029952&subscene=200&clicktime=1782031333&enterid=1782031333&flutter_pos=7&biz_enter_id=5&jumppath=WAWebViewController_1782031263989,WAWebViewController_1782031264526,20020_1782031327730,1104_1782031328342&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQj+kpMJ9FMyI04nOMjxw4VxLTAQIE97dBBAEAAAAAAIluCSVv+K0AAAAOpnltbLcz9gKNyK89dVj0BFEgk0zwc3tM1E5H8T6ebQv07v9MsBZ3WFigJESA+7Y548J6yHTk2FZCNn/AhBrOjRxX2+h/DrUXZUNFYnGVQdpbP4oselitR/zdSyfzYGVBfeeVzOwird0IUzdVeBkANclLUfCAa4MpPqebIFWzu9YFlOQN3ueowhps0MZNllSj6VG29FArA1YJc8TMesxz+qcR/DMystXvJ0otDPPXtDPMOkivHZXouFnHCL0=&pass_ticket=hAgqdGQ2Kmgvhi5z8Sa9TsFZStTK5vtWkxehOmCRmRf/ejxecNpXmZkFYzGUJxQC&wx_header=3)

Original小时智讯AI 干货拆解

AI NATIVE CODER

# 为什么 AI 总是干到一半就说完成了？

Claude Code 这次把 Agent 的老毛病讲透了

复杂任务里，AI 的问题不只是「不会做」，而是经常做不完整、验证不可靠、目标会漂移。

你应该遇到过这种情况。

你给 AI 一个复杂任务。

它先分析得头头是道，计划列得很完整，语气也很自信。

然后干到一半，突然告诉你：

「已经完成。」

你一检查，发现 50 个问题只处理了 20 个，代码改了一部分，验证没跑完，边界条件也漏了。

这不是你一个人的错觉。

在 Claude Code 最新的 dynamic workflows 文章里，Anthropic 工程师把这个问题讲得很直白：复杂任务里，AI Agent 有几个稳定的老毛病。

它会偷懒。

它会偏爱自己的结论。

它会在长上下文里慢慢跑题。

这篇文章有意思的地方，不只是介绍了一个新功能，而是把 Agent 为什么会失控、以及该怎么用工程结构把它管住，讲清楚了。

## 一、AI 并不是不会做，而是经常「做不完整」

Claude Code 这次发布的东西叫 dynamic workflows。

简单说，就是 Claude Code 不再只靠默认的 coding harness 做所有任务。

它可以根据当前任务，临时写一个 JavaScript workflow，也就是一个任务专用的执行框架。

这个 workflow 可以调度多个子 agent。

每个子 agent 可以有自己的上下文窗口，可以在自己的 worktree 里干活，可以负责不同的任务，也可以专门负责检查别人。

这听起来像是「多 Agent」。

但我觉得更准确的说法是：

它不是让 AI 多几个分身，而是让 AI 学会给任务搭一个临时项目组。

普通 prompt 是你对一个人说：「把这件事做好。」

workflow 是你先搭好结构：谁负责提出假设，谁负责查证据，谁负责执行，谁负责挑错，谁负责最后合并，什么时候算完成，什么时候必须继续循环。

这才是它真正重要的地方。

## 二、第一个老毛病：干到一半就交差

原文里用了一个很准确的词：Agentic laziness。

不是说模型真的懒。

而是它在复杂、多步骤、长时间任务里，经常会提前停止，然后把局部进展包装成最终结果。

比如你让它做一次安全审查，里面有 50 个待检查项。

它可能认真处理了前 20 个，然后因为上下文变长、任务变复杂、反馈变稀疏，就开始收尾。

最后它会说：

「我已经完成了安全审查。」

但实际上，它只是完成了安全审查的一部分。

原文里的例子很典型：

「这个测试大概 50 次才失败 1 次。设置一个 workflow 去复现它，形成理论，并在 worktrees 里对抗性测试这些理论。用 /goal，直到有一个理论成立之前不要停。」

这句话的重点不是 flaky test。

重点是「不要停」不能只写在 prompt 里。

你需要一个结构，让任务真的不断循环，直到满足停止条件。

## 三、第二个老毛病：AI 太相信自己

第二个问题叫 self-preferential bias。

也就是 AI 倾向于偏爱自己的发现和结论。

这个问题在「让 AI 自己检查自己」的时候尤其明显。

你让它写一段代码，再让它检查这段代码有没有问题。

它当然能发现一些明显 bug。

但它很容易站在自己的思路里继续推理。

它会下意识维护自己的设计，而不是像一个真正独立的 reviewer 那样，从反方向拆它。

原文给了几个很好的 workflow 场景。

• 让不同 agent 从投资人、客户、竞争对手三个视角去拆一份商业计划。

• 让一个 agent 写方案，再让另一个 agent 按 rubric 做对抗验证。

• 给一个 CLI 工具命名，让多个 agent 提不同方案，再用 tournament 方式两两比较，选出前三名。

这背后的原则很朴素：

判断和生成最好分开。

如果一个 agent 既是选手，又是裁判，它就很难完全公正。

所以 dynamic workflows 里很重要的模式叫 adversarial verification：一个 agent 负责产出，另一个 agent 负责怀疑。

## 四、第三个老毛病：做着做着就跑题

第三个问题叫 goal drift。

目标漂移。

这在长任务里特别常见。

一开始你给 AI 的要求很清楚：不要改公共 API，不要引入新依赖，先验证再合并，保留原来的文风。

但对话越来越长，中间经历多次总结、压缩、续写，这些细节就会慢慢丢失。

原文里说得很直接：每一次 compaction 都是有损的。

最容易丢的，往往不是大目标，而是那些边界条件。

比如「不要做 X」。

比如「必须覆盖某个 edge case」。

比如「只改这个目录，不碰其他模块」。

workflow 的解法不是让一个上下文死撑到底。

而是把任务切开，让不同子 agent 带着更小、更明确的目标去工作，最后再由 synthesize 步骤合并结构化结果。

## 五、最有价值的不是功能，而是 6 个工作模式

原文里总结了几个 dynamic workflows 常见模式，我觉得值得单独记下来。

**第一，Classify-and-act。**先判断任务类型，再路由到不同处理方式。

**第二，Fan-out-and-synthesize。**把任务拆成很多小块，并行交给多个 agent，最后统一综合。

**第三，Adversarial verification。**每个产出都让另一个 agent 专门验证。

**第四，Generate-and-filter。**先生成大量候选，再按标准过滤、去重、验证。

**第五，Tournament。**不做绝对评分，而是多个方案两两比较。

**第六，Loop until done。**不是跑固定轮次，而是循环到停止条件成立。

这就是 AI 工作流和普通 prompt 的区别。

普通 prompt 依赖模型自觉。workflow 把自觉变成结构。

## 六、最适合用 workflow 的，其实不只是写代码

这篇文章还有一个点容易被忽略。

作者说，workflows 有时候在非技术任务里更有用。

因为原文里的例子并不全是代码。

• 从过去 50 次会话里，挖出你反复纠正 Claude 的地方，再提炼成 CLAUDE.md 规则。

• 在 Slack incidents 频道里，回看过去 6 个月事故，找出没人建 ticket 的重复根因。

• 给 80 份简历排序，先问你岗位 rubric，再筛选后端候选人，并复核前 10 名。

• 分析为什么 3 月销售下滑，这同样需要拆证据、提假设、找反例、做验证。

所以这次更新真正指向的，不只是「Claude Code 更会写代码了」。

而是很多复杂知识工作，都可以被改写成：任务拆解、并行执行、独立验证、结构化合并、循环直到完成。

## 七、但别滥用，多 Agent 不是万能药

原文最后也提醒了一个很重要的点：

dynamic workflows 不是所有任务都需要。

它会消耗更多 token，也会增加流程复杂度。

普通小改动，不需要 5 个 reviewer。

一个简单 bug，不一定要拉起一整套 agent team。

真正值得用 workflow 的，是这几类任务：

• 任务很长，容易半途而废。

• 任务可以并行拆分。

• 结果必须被独立验证。

• 目标容易在长上下文里漂移。

• 需要处理大量相似对象。

• 停止条件不是固定轮次，而是「直到没有新问题」。

workflow 不是为了显得高级。它是为了把复杂任务里最容易失控的部分，用结构管起来。

## 八、会用 AI 的人，下一步要学会设计工作流

过去一年，很多人都在学 prompt。

怎么写角色，怎么写上下文，怎么写输出格式，怎么让模型一步步思考。

这些当然还有用。

但如果任务复杂到一定程度，prompt 就不够了。

你不能只靠一句「请务必完整完成」解决 Agentic laziness。

你不能只靠一句「请客观评价」解决 self-preferential bias。

你不能只靠一句「不要忘记目标」解决 goal drift。

这些不是文案问题。

这是系统设计问题。

AI Native 的工作方式，正在从「会不会提问」进入「会不会组织工作」。

低阶用法是让 AI 帮你做事。

高阶用法是让 AI 先搭一个适合这件事的工作系统，再在系统里做事。

它可以是一个临时研究团队，可以是一个代码迁移小组，可以是一个事实核验流水线，也可以是一个事故复盘小组。

这才是 Agent 真正开始变得有用的地方。

不是因为它突然像人一样自觉。

而是我们终于开始承认：

复杂任务不能只靠自觉。

复杂任务需要结构。

参考来源

Thariq Shihipar, A harness for every task: dynamic workflows in Claude Code, 2026-06-03

Claude Blog, A harness for every task: dynamic workflows in Claude Code
