---
title: Harness Engineering 的三个问题，和一个被跳过的前提
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Harness Engineering 的三个问题，和一个被跳过的前提.md
tags: [evernote, impression, yinxiang]
---

# Harness Engineering 的三个问题，和一个被跳过的前提

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg2OTkzMDQxNw==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzg2OTkzMDQxNw==&mid=2247484021&idx=1&sn=4499c6e0019b30ada061de62d790b308&chksm=cf003f114789cd8e45c82a923d0d28c384e6e065faab48c40fd4023189cb1365542df81aa9f7&scene=90&xtrack=1&req_id=1775310094334408&sessionid=1775305459&subscene=93&clicktime=1775310630&enterid=1775310630&flutter_pos=32&biz_enter_id=4&ranksessionid=1775310094&jumppath=20020_1775310560931,1104_1775310561439,20020_1775310565350,1104_1775310624213&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004630&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ45DPOIkB6MHpRGYjP/uMhRLTAQIE97dBBAEAAAAAAHEEGhIquIUAAAAOpnltbLcz9gKNyK89dVj0sDssbEIAh/hSFlj26qjOmxMSTKC1O/FQ6fjWjqtzNTD6lDG0GSVX2N6sYW741nXtNghP8pzYd83ySssd2k/NLcBHlCKbwALroG19ZudnEZlL9YbVHjvbQyavTaSlfiKzIcCBv1cOHa6047YPTm3porOhM499Yb7KzigP5rzDaQqQZpfP7ETk8NTYI5GR7ikDlk4IsnLoSXqyorwEJzUhNLekIvWFd8jqK37U224=&pass_ticket=9J2GYBtAt/wv62m7yIGW/qGtI7f34fnMkpJ5Xskg9Mm/hBj/oZPVEEuWOcWu3Fqi&wx_header=3)

OriginalPanda CheckPanda Check

2026 年第一季度，OpenAI、Cursor、Anthropic 各发了一篇关于 AI 写代码的文章。技术圈立刻沸腾，所有人都开始讨论 harness engineering。

然后一片混乱。

有人说它是"让 AI 工具用得更顺"，有人说是"多个 AI agent 协作"，有人画了一堆方框和箭头说这是"agent 编排架构"。三篇文章，三种解读，三套词汇，讨论同一件事好像没有一个人在讨论同一件事。

这篇文章的起点只有一个问题，harness engineering 到底在说什么。

三家公司在解三道不同的题
============

混乱的根源很简单。三家公司用了相近的词，但实际上在解三个完全不同的工程问题。

OpenAI 解的是环境问题。他们有一个三人团队，五个月合并了约 1500 个 PR，折算下来每人每天 3.5 个。这不是靠写代码快，而是靠搭了一套让 AI 能可靠工作的基础设施——完整的文档体系、架构约束、自动化测试、可观测性工具。他们得出一个结论，agent 看不见的知识等于不存在，所以所有知识都得推进 repo，用 markdown，用结构化文档，不能留在 Slack 或者团队成员的脑子里。

Cursor 解的是并行问题。他们把"用 Rust 从零写一个浏览器引擎"当测试任务，数百个 agent 同时跑了一周，生成超过一百万行代码，峰值吞吐量约每小时 1000 个 commit。这不是靠单个 agent 更聪明，而是靠摸索出了一套能让几百个 agent 协同不打架的架构——经历了四次失败迭代之后。

Anthropic 解的是时间问题。一个 agent 连续运行几个小时，会出现两类失败。第一类是方向漂移，随着上下文变长，模型开始偏离最初的目标，细节越陷越深。第二类是自评失真，agent 发现了自己工作里的问题，然后说服自己这些问题可以接受，给出通过判断。他们的解法是引入一个独立的 evaluator 角色，用真实运行的应用做验证，和执行 agent 完全隔离、互不共享状态。

一个在讲环境，一个在讲并行协调，一个在讲运行时纠偏。这就是为什么大量二手讨论摸不着头脑。

三家达成了四条共识
=========

在展开分歧之前，三家的共识部分更值得认真看。这四条判断，是当前 AI 工程讨论里最没有争议、也最有行动指导价值的内容。

人类的核心工作变了。从直接写代码，变成设计 agent 能可靠工作的环境和条件。代码由 agent 产出，人的杠杆点在于环境设计、架构约束、反馈回路、评估机制。三家从不同方向得出了同一个判断。

约束比指令有效。"禁止提交未完成的实现"比"记得把实现写完"管用得多，因为约束是可执行的、确定性的，指令是可解释的、模糊的。在数百个 agent 同时工作的场景下，一句模糊的指令被并行放大的后果比人类团队里严重得多。

知识必须存在于 repo 里。Slack 上的对齐、Google Docs 里的讨论、团队成员脑子里的隐含经验，对 agent 统统是空白。这不是建议，是硬约束。

完美主义是吞吐量的敌人。在 agent 产出速度远超人类注意力的场景下，要求每次 commit 接近完美会让整个系统停滞。三家都接受了"纠错比等待便宜"的权衡。

一个被三家同时跳过的前提
============

读完三篇文章，有一个问题始终没有被认真回答。

他们在讨论怎么 scale，但没有讨论 scale 向哪里，以及为什么是这个方向。

Anthropic 的 evaluator 在纠偏，但纠偏是朝哪个方向纠。sprint contract 谁来定义，什么叫好结果，这个判断从哪里来。文章没说清楚。Cursor 接受了一个稳定的错误率让系统自然修复，但什么样的错误率是可接受的，可接受性由谁定义，也没有答案。

这个被跳过的前提是价值函数——这套系统究竟在优化什么。

没有价值函数，所有纠偏都只是形式化动作。几百个 agent 每小时 1000 个 commit，如果方向本身就偏了，吞吐量只是把错误加速放大。Evaluator 评估的是提前定义好的目标，如果那个目标本身就有问题，evaluator 的独立性也救不了结果。

还有一个被轻描淡写的问题，context infrastructure。三篇文章里说得最直白的是 OpenAI 那句：agent 看不见的知识等于不存在。但"知识存在于 repo 里"和"知识是高质量的、结构化的、能支撑真实判断的"，是两件完全不同的事。

同样的模型、同样的工具、同样的 harness，接入一套经过长期积累和精炼的知识体系，和接入一堆七零八落的文档，产出的性质会完全不同。前者是有判断力的分析，后者是正确的废话。

Harness 决定 agent 能否高效工作，context 决定 agent 是否值得工作。这两件事的重要性其实是倒过来的，但三篇文章的重心都放在前者。

对在做 AI 项目的企业，真正值得检查的顺序
======================

这三个 scaling 维度，对 OpenAI、Cursor、Anthropic 这类在 AI 能力边界做探索的机构有直接价值。但对更广泛的企业来说，数百个 agent 并行、单个 agent 连续六小时、全自动 ticket 驱动执行，大多数 AI 项目根本走不到那一步，也不需要走到那一步。

一家正在用 AI 做合规审核的公司，真正卡住的问题往往不是 agent 跑不够久，而是审核标准没有写清楚；不是并行度不够，而是历史案例数据太分散 agent 找不到；不是人机交互效率低，而是连"什么样的审核结果算合格"都没有人说得清楚。

在这个阶段谈 harness engineering 的三个 scaling 维度，很容易用高级框架包装了一个还没想清楚的项目。

更实用的检查顺序是这样的。

先把价值函数说清楚。什么叫好结果，这个标准谁来负责，能不能写成一个 evaluator 真正可以执行的 contract，而不只是一句语气词堆叠的要求。

然后检查 context 的质量。agent 能访问的知识，够不够结构化、够不够准确、覆不覆盖任务实际会碰到的情况。这比把知识推进 repo 更难，但更关键。

最后才是 harness 本身。你的任务复杂度，真的需要多个 agent 协作、长时间运行，还是一个设计得当的单次调用就够了。

Anthropic 在文章里有一个很值得借鉴的习惯，他们把每个 harness 组件都看作基于"当前模型能力边界"的暂时假设，随着模型变强，会主动去移除不再需要的组件，而不是不断叠加。这个思路不只适用于 harness 组件，对整个 AI 项目的复杂度设计都适用——定期问自己，这里的复杂度还有必要吗。

三家顶尖 AI 实验室把一年的工程实践浓缩进三篇文章，当前 AI 工程讨论里最接近一手资料的东西就是这些了。框架值得理解，共识部分可以直接拿来用。

但在你把这套框架搬进自己的项目之前，那个被跳过的前提先想清楚。

你知道你这套系统在优化什么吗？

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg2OTkzMDQxNw==&mid=2247484021&idx=1&sn=4499c6e0019b30ada061de62d790b308&chksm=cf003f114789cd8e45c82a923d0d28c384e6e065faab48c40fd4023189cb1365542df81aa9f7&scene=90&xtrack=1&req_id=1775310094334408&sessionid=1775305459&subscene=93&clicktime=1775310630&enterid=1775310630&flutter_pos=32&biz_enter_id=4&ranksessionid=1775310094&jumppath=20020_1775310560931,1104_1775310561439,20020_1775310565350,1104_1775310624213&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004630&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ45DPOIkB6MHpRGYjP/uMhRLTAQIE97dBBAEAAAAAAHEEGhIquIUAAAAOpnltbLcz9gKNyK89dVj0sDssbEIAh/hSFlj26qjOmxMSTKC1O/FQ6fjWjqtzNTD6lDG0GSVX2N6sYW741nXtNghP8pzYd83ySssd2k/NLcBHlCKbwALroG19ZudnEZlL9YbVHjvbQyavTaSlfiKzIcCBv1cOHa6047YPTm3porOhM499Yb7KzigP5rzDaQqQZpfP7ETk8NTYI5GR7ikDlk4IsnLoSXqyorwEJzUhNLekIvWFd8jqK37U224=&pass_ticket=9J2GYBtAt/wv62m7yIGW/qGtI7f34fnMkpJ5Xskg9Mm/hBj/oZPVEEuWOcWu3Fqi&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b9aa11b1-0f3f-4281-b644-09118d1663e1/b9aa11b1-0f3f-4281-b644-09118d1663e1/)
