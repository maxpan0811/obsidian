---
title: _compact 我用了 3 个月，今天把 Claude Code 这一个指令讲透：何时压 _ 压什么 _ 压完会丢什么 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/_compact 我用了 3 个月，今天把 Claude Code 这一个指令讲透：何时压 _ 压什么 _ 压完会丢什么 2.md
tags: [evernote, impression, yinxiang]
---

# /compact 我用了 3 个月，今天把 Claude Code 这一个指令讲透：何时压 / 压什么 / 压完会丢什么

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247485096&idx=1&sn=0a2acf35f4606c44e6fee584e7bc8aed&chksm=f1054576cd49cc7a553b93ceae604f63ed56518655902be51caeff5b098a198b58e396477a48&scene=90&xtrack=1&req_id=1779862685576322&sessionid=1779862930&subscene=93&clicktime=1779862936&enterid=1779862936&flutter_pos=9&biz_enter_id=4&ranksessionid=1779862890&jumppath=1001_1779862909089,1101_1779862911446,1001_1779862927108,1104_1779862930941&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004934&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQswDvOKmTefljcpPo7p+AeBLTAQIE97dBBAEAAAAAAIfxE9yS+U8AAAAOpnltbLcz9gKNyK89dVj03MWIwc/lN2pqrY58a0nKAZMJRGO9TE7Urum+6XTYZlDM3Eqv+eJ+X05CylS4v73LwhHbhihSwdoWSMEp8KngAt8p/XNe9a7PXoVYe2nfiSoEdXVGoVbQpkzHOwBCDtWYZGrmYDFlZH6IYkFyH/eQPRF5n7NzFvP5lZ2TCa7FYPps8t9H+WU6Ri+Xqspn0Gixa9m9ttZGZCgD63Xb1ws2wTvXgzZgiKFgYpRWwxA=&pass_ticket=lcG9tKNpoDy7BOJUxZO/GElRUYKSFyE1pvW7Sll3IwO/NqlCiEj60DiHt1REZ54k&wx_header=3)

Original莲花明 AI落地手记

一、那天我以为只是变慢了
------------

上周我让Claude Code改一个Python服务里的鉴权中间件。从早上10点写到下午4点，中间过了5次方案、改了3个测试用例、推翻了1个我自己拍板的方案。

下午4点12分，我让它把最终方案写成commit message。它问我：「这次改了哪几个文件？」

我盯着屏幕，心里咯噔一下。

那是它从早上开始一直在改的文件。文件名、相对路径、改了什么行、为什么改 —— 这些它本来应该完全知道。这不是"我没说清楚"，是它**真的忘了**。

Claude Code不是变慢，是悄悄丢东西。这种现象在Anthropic内部有个专门的词，叫**context rot** —— 上下文腐烂。

解药就一个指令：**/compact**。

但这个指令95% 的人都用错了时机。我用了3个月才搞懂它的机制，今天讲透。

---

二、/compact不是「压缩」，是「销毁 + 接续」
---------------------------

字面意思是压缩。但你看完它的实际行为就会发现，"压缩"这个词反而误导人。

真实机制是这样：

旧窗口（销毁）

120轮对话

180k tokens

含早期决策 / 文件路径 / 修过的bug

→

LLM摘要

单独一次调用

~1分钟 + 烧tokens

生成结构化summary

→

新窗口（接续）

摘要 + 最近几轮

~30k tokens

会话ID不变

图1 · /compact不是压缩，是销毁旧窗口 + 摘要传递 + 新窗口接续

三步：

**① 销毁**：当前会话窗口（可能已经有180k tokens、120轮对话），整个被丢弃。

**② LLM调用**：单独发起一次LLM请求，把刚才那180k tokens喂进去，让模型写一份结构化摘要。这一步要烧时间（~1分钟）和tokens。

**③ 接续**：新窗口里放的是【那份摘要 + 最近几轮真实对话】，可能只剩30k tokens。会话ID不变，你感觉上没换会话，但模型记忆已经被换过芯。

所以"压缩"是误导，准确说法是**蒸馏式重启**。蒸馏的过程必然丢东西 —— 早期文件路径、临时变量名、你纠正过的写法、被否决的方案理由 —— 全都可能在摘要里被裁掉。

**API层面的实证**：Anthropic Claude API在2026-01-12上线了compact测试版，header是`compact-2026-01-12`。压缩触发后，API自动删除compaction块之前的所有message blocks。这是**不可逆的**。

---

三、三档时机：60% 是黄金，95% 已经晚了
-----------------------

Claude Code CLI左下角会显示context使用率。这个百分比就是你判断要不要 /compact的核心数据。

0%

25%

50%

75%

100%

**0-60% · 别压**

**60-75% · 主动压（最佳窗口）**

**75-95% · 必须压（再不动就晚）**

**95%+ · auto-compact被动触发**

图2 · /compact时机选择 · 60-75% 是最佳手动窗口

### 3.1 0-60%：别压

这个区间任何 /compact都是亏的。摘要本身要烧tokens和1分钟时间，换来的东西你根本用不到。

### 3.2 60-75%：主动压（这是黄金窗口）

原因有两个：

**① 摘要质量最高**：要压缩的内容总量适中，模型有余力把"关键决策"和"无关闲聊"分清楚。等到90% 才压，模型自己都在context饥荒里，摘要会瞎裁。

**② 不打断当前任务**：你主动 /compact时通常处在任务节点之间。auto触发是随机的，可能正好卡在你写到一半。

### 3.3 75-95%：必须压

再不动就要被动了。但这个区间你还能加instructions控制：

/compact Focus on: 鉴权中间件改造 · 已修文件路径 · 测试用例 / 砍掉: 早期方案讨论 · 闲聊

这一行指令能让摘要质量再上一档。Anthropic官方建议「5-10项instructions最佳」。

### 3.4 95%+：auto-compact自动触发（但你已经失控）

Claude Code默认在 ~95% 时自动compact。听起来很贴心，实际上有3个代价：

· 触发时机你不挑，可能正好卡在你跑测试中间

· instructions你给不上，模型自己决定保留啥

· auto-compact还会**预留22.5% 的buffer**（约45k tokens）—— 这部分context你从一开始就用不上

---

四、auto-compact偷掉的那22.5% buffer
------------------------------

这是最反直觉的设计。

Claude Code的context窗口是200k tokens。但你打开任何一个新会话，左下角永远从 ~22.5% 开始（约45k tokens已用）—— 这部分就是auto-compact预留的"逃生通道"，让它能在95% 触发时还有空间写摘要。

换句话说：**200k上下文里，你能用的实际上只有155k**。这45k不是你的，是auto-compact自己留着用的。

**性能反例**：GitHub issue #13112报告auto-compact触发后，Claude Code出现明显的推理质量下降。已修过的bug又复发、之前纠正过的命名又用错。Anthropic官方在2026年3月承认这是已知的退化问题。

解药有两个：

**方案A · 关掉auto-compact**：CLI命令`/auto-compact off`。代价是要自己盯context%，一过70% 就主动压。

**方案B · 提前手动压**：保留auto但永远不要让它触发。这是我的选择 —— 65% 时主动 /compact，永远把它扼杀在自动触发之前。

---

五、手动 /compact的3个正确姿势
--------------------

### 5.1永远带instructions

裸 /compact的摘要质量是给"通用场景"准备的 —— 它假设你是新手，把一切都简单总结一遍。但你不是新手，你正在做**一件具体的事**。

正确的写法：

/compact 保留:

- 当前在改的文件路径列表

- 已通过的测试 case 编号

- 用户最后一次纠正的命名约定

砍掉:

- 早期讨论过但被否决的方案

- 你 explain 给我听的库 API 用法（我后面会自己查）

这一段instructions给得越具体，摘要越能贴合任务。

### 5.2在「任务节点之间」压，不在执行中压

压在哪一个具体时刻，比压不压更重要。最佳时机：

· 跑完一组测试 / 合并完一个PR / 改完一个文件 → 安全

· LLM正在生成代码 / 跑测试中 / 调外部API → **禁压**

在执行中压，相当于把"还没说完的话"也喂进摘要LLM。模型不知道你下一句要补什么，可能直接误判任务已结束。

### 5.3压完立即verify

/compact完成后第一件事不是继续干活，是**验记忆**。问一句：

刚才我们在改哪几个文件？已经过的测试用例是什么？

最后一次你被纠正的写法是什么？

如果它答得上来 → 摘要质量合格，继续干。

如果它答错了任何一条 → 立即Esc+Esc回滚到 /compact之前，重新加instructions再压。

**我的实操配置**：在 ~/.claude/commands/ 目录下做一个自定义slash command，叫`/cc`（compact-careful的缩写），内置我的instructions模板 + verify问句。需要时一个命令搞定。

---

六、5个真实踩坑（全部有GitHub issue实证）
---------------------------

社区报告的compact相关bug不少。下面5个是我自己踩过 + GitHub有公开issue的：

| 坑 | 症状 | 来源 |
| --- | --- | --- |
| 忘文件 | compact后Claude不记得在改哪个文件，要重新Read | GH #13112 |
| 重犯老错 | 你早就纠正过的命名 / 写法，compact后又犯一遍 | GH #13112 |
| Context low误报 | 明明还剩86% context，CLI弹警告 + /compact直接失败 | GH #6616 |
| 5% 时彻底崩 | context剩5% 才想压，API直接500，10次重试全失败 | GH #3274 |
| 手动compact fail | auto-compact关了之后，逼近上限手动压触发error卡死 | GH #25620 |

图3 · 5个有GitHub issue实证的真实踩坑

### 6.1忘文件 + 重犯老错（issue #13112）

最常见。compact后Claude不记得在改哪个文件，要重新Read。更恼火的是早就纠正过的命名 / 写法，compact完又犯一遍。

**解药**：在instructions里显式列出「当前在改的文件路径」和「你已经被纠正过的3条规则」。

### 6.2 Context low误报（issue #6616）

明明左下角还显示86% 可用，CLI却弹「Context low」警告，并且 /compact命令本身直接报错失败。

**解药**：这是CLI显示bug。重启CLI，重新 --resume这个session即可恢复。

### 6.3 5% 时彻底崩（issue #3274）

Context还剩5% 才想起来要压，已经晚了。这时API调用会返回500错误，10次重试全失败，CLI进入死循环。

**解药**：永远不要等到95%+ 才compact。这条铁律比任何instructions都重要。

### 6.4关掉auto后手动fail（issue #25620）

一些用户嫌auto-compact干扰，关闭后手动 /compact反而触发error卡死。

**解药**：要么auto开着 + 65% 主动压；要么auto关掉 + 设置严格的「context监控提醒」（比如自己写一个hook，到60% 时桌面通知）。不要中间态。

---

七、我的实战SOP：长任务的4段式管理
-------------------

做一个工作日的长任务（比如改造一个有30个文件的服务）时，我现在固定走这个流程：

### 阶段1：会话开始（0-30% context）

什么都不管，专心干活。这一段context烧的全是有效信息，不要碰 /compact。

### 阶段2：30-60% context

开始留意「任务节点」。每完成一个独立模块（一个文件改完 + 测试通过），在心里打一个checkpoint。

### 阶段3：60-75% context（黄金压缩窗）

选择最近一个checkpoint作为「压缩点」。运行：

/compact 保留:

- 项目目标 + 已确认的架构决策

- 当前 in-progress 的文件路径

- 用户给过的 3 条具体偏好（命名 / 测试 / commit 格式）

砍掉:

- 已合并 PR 的具体 diff 细节

- 早期方案对比

压完立即跑verify问句。合格 → 进入阶段4。

### 阶段4：75-90% context（如果还在work）

再压一次。这一次的instructions要更激进，只保留「当前正在改的那一个文件 + 当前测试用例」。

如果到这一步还没完成任务 → 大概率任务规划过大，应该 /clear拆分成2-3个独立会话来做。

**反直觉认知**：好的Claude Code使用者，单会话很少超过90% context。一旦你发现自己经常打到95%，说明**任务拆分有问题**，不是compact没用对。

---

八、上下文三指令的决策表
------------

Claude Code管理context的核心命令有3个 —— /compact、/clear、/rewind（或Esc+Esc）。什么时候用哪个，一张表说清楚：

| 场景 | 指令 | 为什么 |
| --- | --- | --- |
| 当前任务做到一半，想继续 | /compact + 自定义指令 | 保留任务上下文，砍掉无关历史 |
| 当前任务彻底完成，要切新主题 | /clear | 纯空白重启，最快 |
| Claude刚做错一步，想撤回 | Esc+Esc或 /rewind | 回到上一个checkpoint，不动context |
| 不知道任务完没完 | 先 /clear再说 | 默认 /clear比默认 /compact安全 |
| 做长任务怕忘 | 提前 /compact at 60% | 主动比被动好 |

图4 · 上下文管理三指令决策表 · 收藏备用

一句话总结：

**/clear是默认**（任务切换最干净）/ **/compact是续命**（同一任务要继续才用）/ **Esc+Esc是反悔**（刚做错就回退，比compact便宜）。

三个都不会用，只会让auto-compact兜底 —— 那就别怪Claude越来越笨。

---

**写在最后**：这一篇是Claude Code单指令深挖系列的第一篇。后续会拆 /clear、/rewind、/btw、worktree —— 这些都是业界标配但80% 用户不会用的指令。

如果觉得有用，把它转给你身边那个还在95% 才compact的同事，他会感谢你。

关注「AI落地手记」

一个人 + AI管20个项目的AI编排师

工具拆解 · 实战踩坑 · 不画饼只讲落地

写得对你有用，**点喜欢作者**或**转发**给同样在用Claude Code的朋友。

— AI落地手记 —

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247485096&idx=1&sn=0a2acf35f4606c44e6fee584e7bc8aed&chksm=f1054576cd49cc7a553b93ceae604f63ed56518655902be51caeff5b098a198b58e396477a48&scene=90&xtrack=1&req_id=1779862685576322&sessionid=1779862930&subscene=93&clicktime=1779862936&enterid=1779862936&flutter_pos=9&biz_enter_id=4&ranksessionid=1779862890&jumppath=1001_1779862909089,1101_1779862911446,1001_1779862927108,1104_1779862930941&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004934&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQswDvOKmTefljcpPo7p+AeBLTAQIE97dBBAEAAAAAAIfxE9yS+U8AAAAOpnltbLcz9gKNyK89dVj03MWIwc/lN2pqrY58a0nKAZMJRGO9TE7Urum+6XTYZlDM3Eqv+eJ+X05CylS4v73LwhHbhihSwdoWSMEp8KngAt8p/XNe9a7PXoVYe2nfiSoEdXVGoVbQpkzHOwBCDtWYZGrmYDFlZH6IYkFyH/eQPRF5n7NzFvP5lZ2TCa7FYPps8t9H+WU6Ri+Xqspn0Gixa9m9ttZGZCgD63Xb1ws2wTvXgzZgiKFgYpRWwxA=&pass_ticket=lcG9tKNpoDy7BOJUxZO/GElRUYKSFyE1pvW7Sll3IwO/NqlCiEj60DiHt1REZ54k&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/170d99a9-a605-4389-9487-c08cd0016468/170d99a9-a605-4389-9487-c08cd0016468/)
