---
title: "你还没把 Claude 用得足够有野心：别只让它做杂活，要让它接管高杠杆工作"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/你还没把 Claude 用得足够有野心：别只让它做杂活，要让它接管高杠杆工作.md
tags: [印象笔记]
---

# 你还没把 Claude 用得足够有野心：别只让它做杂活，要让它接管高杠杆工作

# 你还没把 Claude 用得足够有野心：别只让它做杂活，要让它接管高杠杆工作 --- 很多人觉得自己已经“会用 AI”了。 会让它总结文章、整理会议纪要、润色文案、写点脚本，已经比大多数人强不少。

---

# 你还没把 Claude 用得足够有野心：别只让它做杂活，要让它接管高杠杆工作

---

很多人觉得自己已经“会用 AI”了。

会让它总结文章、整理会议纪要、润色文案、写点脚本，已经比大多数人强不少。

但 Christine Zhu 这篇文章真正戳人的地方在于：

你生产力真正跃迁的那一刻，往往不是把杂事自动化，而是开始把那些高杠杆、过去你不敢交出去的工作，也交给 Claude。

她说自己过去几个月，一直在用 Claude 清理“多巴胺积压”。

所谓多巴胺积压，就是那些你特别容易立刻去做、做完还会产生一种“我今天很有效率”的幻觉的小事。它们很爽，但未必重要。

把这些事情自动化之后，时间的确被释放出来了。

但真正的大跃迁，发生在下一步：

她开始逼 Claude 去做更难、更关键、更高杠杆的工作。

结果不是小幅提效，而是她对工作节奏、承载能力和流畅感的整体提升。

把 Claude 用到产品工作的 3 个层级

文章借用了 @shreyas 提出的产品工作三层框架：

* • optics：让进展被看见、被理解、被同步
* • execution：推动执行、协调流程、把事情落地
* • impact：真正高杠杆的判断、策略、叙事和方向选择

很多人会很自然地让 Claude 处理前两层里的零碎劳动，却把第三层留给自己。

我们会下意识相信：

“判断力”才是最该由人类保留的护城河。

但 Christine 的经验恰恰相反。

她认为，只要给足上下文，Claude 不只是能做“助理型工作”，它甚至能在很多高难度任务上，提供比你预期更快、更好的初稿、拆解和判断辅助。

Notion 一项覆盖 10 个市场、6000 名职场人士的调研也说明了类似趋势：大多数组织还只是把 AI 当成聊天机器人或思维伙伴，真正把它推到更高阶使用方式的公司仍然很少。

也就是说，机会还非常大。

作为平台 PM，Christine 需要理解并协同整个产品组织的路线图，面对的是成千上万 PM 和开发者构成的系统复杂度。她的做法，不是更拼命，而是把 Claude 分别用进这三个层级里。

![](.evernote-content/0941C4AE-43C8-40A1-AB20-7CAFD3075647/D8E9B6A9-BAA4-4244-ACED-925FF2175482)

第一层：Optics 工作，能自动化就别手工做

所谓 optics，不是作秀，而是把团队的进展准确地呈现给对的人、放到对的场景里。

这类工作常常看起来琐碎，却非常吃时间：

* • 更新状态表
* • 汇总不同项目线的进展
* • 按不同受众改写版本
* • 在多个场合重复同步同一批信息

Christine 的做法非常直接：

她设了一个每周跑两次的定时任务，从 Slack、日历、会议笔记、Git 等关键源拉上下文，然后把每条工作流的最新更新写进 Google Sheet 模板，再自动发一条精简 Slack DM 给自己。

这个状态板对团队公开，很多问题不需要再专门来问她。

换句话说，她并不是让 Claude 帮她“写得更快”，而是让 Claude 接管整段生产流程。

她甚至判断，这一类工作未来很可能会直接被产品化进 Claude 本身。

![](.evernote-content/0941C4AE-43C8-40A1-AB20-7CAFD3075647/26FBA8DB-4583-442D-9F63-EDCA9AA121B2)

这部分最有参考价值的，是她公开了一个定时任务指令模板。因为它本来就是可以直接改造复用的，我保留英文原文：

You are updating the [your status sheet] for [name]. Your job is to gather the latest updates from Slack channels, a Google Sheet tracker, and the PM journal, then write a JSON update file to a Google Drive inbox folder (which an Apps Script time trigger picks up and applies to the sheet), and send [name] a compact Slack DM.

## STEP 1: Read current sheet state

[use google connector here]

## STEP 2: Gather signals (last 3 days)

### 2a. Slack channels

Read these channels using slack\_read\_channel (oldest = 3 days ago unix timestamp):

[insert your slack channels]

### 2b. PM Journal

Read the last 3 days of journal entries from the [folder]. These are local files at:

[insert filepath]

Read the 3 most recent .md files (by filename date). Journal entries contain to-dos, decisions, meeting notes, and context that may not appear in Slack. Treat journal entries as a first-party source alongside Slack messages.

## STEP 3: Determine changes

For each track and detail row, identify ONLY items with verifiable changes:

- Status changed? (e.g., “◉ In Dev” → “Complete”)

- New items shipped?

- Next milestone updated?

- New or resolved risks?

- Notes worth updating?

Be factual. Only report changes backed by [your sources]

## STEP 4: Push updates to the sheet via Drive inbox

Create a JSON file in the Drive inbox folder. The Apps Script time trigger (runs hourly) will pick it up and apply the changes to the sheet.

[work with claude on JSON payload]

## STEP 5: DM Christine

Send a Slack DM to [yourslackID] with a compact summary. Format:

At-a-Glance sheet updated — [date]

[N] changes pushed:

• [Track]: [one-line summary of what changed]

• [Track]: [one-line summary]

Heads up: [1-2 sentences on anything notable that doesn’t map to a sheet row — new risks, scope changes, staffing, cross-team signals]

If nothing changed across all tracks, send: “At-a-Glance sheet checked — [date]. No changes detected across any tracks.”

## GUIDELINES

- Be factual. No inferences or speculation.

- Use the sheet’s own terminology: “◉ In Dev”, “○ Planned”, “Complete”, “On Track”, “At Risk”, “In design”

- If a Slack channel has no relevant messages, skip it silently.

- Keep the DM under 500 characters. Christine wants glanceable, not comprehensive.

她的核心判断我很认同：

最该无情自动化的，往往就是这些看起来“必要但没创造性”的信息生产与同步劳动。

因为它们最容易吞掉你的专注力，又最容易制造“我今天忙了一整天”的错觉。

第二层：Execution 工作，让 Claude 从总结员变成副驾

在执行层，Christine 每周一会跑一个叫 context-dump 的技能。

这个技能会读取她过去一周的 Slack、日历、笔记和 repo 活动，分析她的效率与模式，给出优先级建议，还会直接提出具体可以开始做的工作。

![](.evernote-content/0941C4AE-43C8-40A1-AB20-7CAFD3075647/69304AF6-30C0-466A-9E62-45760A390ACB)

她特别强调，这类输出读起来不该只是“总结”，而更像一个真的在观察你工作模式的教练。

比如其中一个洞察是：

杠杆型工作占比跌破了大约 70% 的目标，不是因为零碎事务增加了，而是因为对齐和仪式性会议占用了太多时间，挤压了真正产出书面成果的深度工作。

这就不是“帮我总结一下本周做了什么”了。

这是在做更高阶的判断：

* • 你的时间到底花在哪
* • 哪些流程开始挤压你的高价值产出
* • 你下一步应该优先调整什么

她还会让 Claude 去检查 Jira 和 roadmap，判断团队进度、安排下一步，再进一步把 PRD 拆成 tickets，甚至直接帮她完成 Jira 更新。

她的态度很明确：

别把 Claude 只当成摘要器。要敢于向它索取判断。

此外，她还会每月跑一次定时任务，分析客户支持频道，归纳主题、判断趋势，并推荐最值得优先处理的请求与问题。这样她就能更持续地贴近用户，而不是等问题堆积后再回头补课。

第三层：Impact 工作，把最难开始的高杠杆任务也交给它

真正最有意思的是第三层。

这也是大多数人最舍不得放手的一层：

* • 想新产品方向
* • 写高风险汇报或关键叙事
* • 用业务上下文检验策略
* • 为重要讨论做观点组织

Christine 说，她已经不再等“完美条件”出现，比如一定要有完整的两小时深度工作块，才肯启动这类任务。

现在哪怕只有 10 分钟空档，她也会直接在装好了上下文的 Claude 项目里，先做一次语音 dump，让模型在高配推理模式下陪她 spar，快速产出一个很糟但能推进思考的初稿。

这件事以前可能要拖好几天。

她强调了一个很关键的前提：

你得先认真“onboard” Claude。

也就是把足够多的上下文交给它，例如：

* • 现有产品 deck
* • roadmap
* • 代码库概要
* • 团队和产品背景
* • 目标与指标
* • 关键利益相关者及其关注点
* • 你自己想提升的能力

这样一来，无论是在 Cowork 项目里，还是在 Claude Code 里，它都能在你工作的过程中持续吃到正确上下文，并随着你的工作继续更新。

![](.evernote-content/0941C4AE-43C8-40A1-AB20-7CAFD3075647/13CF2FBD-4C73-4331-BE01-55231979956B)

她对“判断力”的定义也很值得记住：

所谓判断力，本质上往往就是对上下文做模式匹配。

平台 PM 需要同时处理 5 到 10 条工作流，每一条背后都有不同团队、不同时间线、不同范围。人脑能 hold 的上下文是有限的，但模型能同时握住更多上下文，因此当然可能给出有价值的判断辅助。

当然，它也有边界。

比如没写下来的团队关系、真实激励、组织政治、责任归属，它都不真正拥有。

但即便如此，它已经足够强，可以成为高杠杆思考的启动器和加速器。

她还提到另一个很实用的技巧：

让 Claude 把输出直接生成为 HTML artifact，而不是一堵 markdown 文字墙。

这样你会更快看懂它的结构，也更容易在脑内形成视觉化观点。虽然她不会直接分享这些 HTML，因为它不够协作、像另一个额外链接、也显得太“AI 味”，但它非常适合拿来做自己的中间稿。

AI 不只是在替你工作，也在训练你成长

这篇文章后半段还有两个很好的观察。

1. 技术 fluency 会被快速拉高

Christine 本人没有 CS 学位，但她会用 Claude Code 去理解代码库结构、生成架构概览、辅助讨论 PRD 与路线图，甚至已经开始提交小型 PR。

重点不是“让 PM 去写更多代码”，而是：

它让原本不熟悉技术细节的人，能更快地进入工程语境，做出更有质量的判断。

通过读 Claude Code 的 plan、看它如何拆问题、如何评估可行性，一个人能非常快地提升自己的技术理解力。

2. 它还能成为诚实的职业教练

她每周跑的 context-dump，随着时间累积，其实也变成了一份很难得的成长记录：

* • 你做了什么
* • 遇到了什么挑战
* • 做成了什么成果
* • 哪些人际动态在反复出现

每隔几个月，她就会让 Claude 读取这份滚动历史，反过来评估自己新发展出的能力、存在的盲点，以及为了进入下一个层级，最值得刻意训练的方向。

它几乎像一个持续在线的职业教练，也非常适合拿来辅助写月报和年终总结。

最后那个提醒，比 setup 更重要

Christine 还专门提醒了一个陷阱：

不要把“搭最完美的自动化系统”本身，又变成新的多巴胺积压。

也就是说，别沉迷在 setup 里，最后把真正重要的工作继续往后拖。

她自己的基础配置包括：

* • Obsidian：记录每日笔记与会议摘要
* • Claude Code in VSCode：理解代码库、写 PRD、做可视化、连接内部 MCP
* • Claude desktop / Cowork：跑定时任务、做写作与头脑风暴
* • Connectors：Slack、Google Drive、Outlook、Jira、GitHub、HeyMarvin
* • PM folders：沉淀长期上下文，如写作风格、会议记录、年度目标、模板与框架

但她认为，这部分反而是“最不重要”的。

真正关键的是：

别再只把模型当成处理边角料的工具。

模型过去几个月的进步，已经足以让它在越来越多困难任务上，做得比我们预期更好。最值得做的，不是继续守着“这个还是得我自己来”的心理防线，而是不断拿更高预期去测试它。

她给出的最终建议很简单，也很锋利：

挑一个你一直拖着、但其实最有杠杆的任务。把它需要的上下文、你现在的判断、你担心的点，一次性交给 Claude。然后直接问它：

我还漏掉了什么？

很多时候，你缺的不是更多勤奋，而是更大胆地使用你已经手里的模型。

[原文链接](https://mp.weixin.qq.com/s/CSMP2Kb1UwrIuSBL0Ji0Rg)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2c57ef70-5814-4050-bb0d-c6017bbfeda9/2c57ef70-5814-4050-bb0d-c6017bbfeda9/)