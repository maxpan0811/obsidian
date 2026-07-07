---
title: "这次将 Claude Code 的 Token 使用量减少 90% 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/这次将 Claude Code 的 Token 使用量减少 90% 2.md
tags: [evernote, impression, yinxiang]
---

# 这次将 Claude Code 的 Token 使用量减少 90%

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0NDQ0ODU3MA==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547388&idx=1&sn=7146b7928a4db5653e9732c736844fab&chksm=e868ab407bcbe74ef55d934ba226c83b04b62b7c0c6394e3ee8325a54e8b66a4c163c200cf89&scene=90&xtrack=1&req_id=1777095048938308&sessionid=1777094023&subscene=93&clicktime=1777095072&enterid=1777095072&flutter_pos=6&biz_enter_id=4&ranksessionid=1777095048&jumppath=20020_1777095041531,1104_1777095042080,20020_1777095048476,1104_1777095060828&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=1800472b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmvoa1mMtZ+bLvrlRjjNn2xLVAQIE97dBBAEAAAAAAN0iKDxLQLoAAAAOpnltbLcz9gKNyK89dVj0vNDAT5LIQ8eiQqPf/135PhKmMhKwNuqxOwI7E/LvfjAdUfBae/rKqrsQy1glH7gg8izH2+7/XnanlKdYxMsNoo8S8o/17bc6MrqkjUzZvYYSYCM4UyjRACzRfeVOzuW4uNCX5rFXbRVWoxyZF2qCCOIQ0OU5XVBRBQh8Lm0WHnPZ48JzxEaBUd36otryudJqVCaKC79t5n2kbKzB2n5zFravna4AP9+9vrYA9g0MeQ==&pass_ticket=ebdFURp3sX4auOmMJjW6w16QYvpCaCG3jphf1XsNH75UsIyzmg5xb1KciA26uFHx&wx_header=3)

Originaldev 大迁世界

Claude Code 的使用量，真正吃紧的地方，往往不是你发了多少条消息。

更关键的是：每一次回复时，系统到底要重新处理多少 token。说得直白一点，你塞进去的历史越长、重复内容越多、无关上下文越庞杂，使用量就会涨得越快，而且常常是在你没察觉的时候悄悄暴涨。

好消息是，这里面的大部分消耗，其实都可以避免。只要稍微调整工作方式，Claude Code 的 token 使用量就能明显下降，很多时候甚至能砍掉非常大一部分。

1. 会话别拖太长，保持干净
--------------

长聊天线程，是最容易被忽视的 token 黑洞之一。

每当你发送一条新消息，Claude 都需要重新阅读前面的整段对话，包括旧指令、过时代码、已经解决的问题，以及那些早就不再相关的上下文。刚开始你可能没感觉，但随着对话不断变长，消耗会一点点堆起来。

更好的做法是：

切换任务时，直接开启新会话； 上下文不再需要时，使用 `/clear`； 不要把几个无关问题混在同一个线程里。

这样做的核心目的很简单：让上下文保持小而集中。上下文越干净，Claude 每次需要处理的内容就越少，token 使用量自然也会下降。

2. 别把提示词改成连续剧
-------------

很多人用 Claude Code 时，会习惯一条接一条地补充要求：

“这里再改一点。” “现在修一下那个。” “顺便把这个也调整一下。”

看起来很自然，但问题在于，每多发一次，模型就要重新处理前面的内容。你以为只是加了一句小修改，系统实际读的却是一整段越来越长的历史。

更省 token 的方式是：

尽量一次性写完整需求； 或者直接编辑原始提示词，而不是不断追加后续补丁。

这个习惯一旦改掉，浪费会少很多。尤其是在写代码、调试、重构这类任务里，减少来回补充，往往比你想象中更有效。

3. 能合并的任务，就别拆开问
---------------

把工作拆成一步一步做，听起来很有条理，但从 token 成本来看，它并不总是划算。

比如你原本可能会这样问：

先修 bug； 再重构代码； 最后补测试。

更好的方式是直接说：

“修复这个 bug，顺便重构相关代码，并补上对应测试。”

为什么这样更省？

因为模型只需要读取一次上下文，就能一次性产出完整方案。否则，每一步都要重新加载相同的背景信息，反复理解同一段代码，token 就这样被白白消耗掉了。

批量处理任务，是降低 Claude Code 使用量最简单、也最不影响质量的方法之一。

4. 给上下文要狠一点
-----------

很多 token 浪费，不是因为 Claude 不聪明，而是因为你给得太多。

常见问题包括：

只需要一个函数，却贴了整个文件； 只需要几行报错，却复制了几百行日志； 同一段代码，反复在不同消息里重新发送。

Claude 会处理你发过去的所有内容。哪怕其中大部分并没有用，它也照样会被计入上下文成本。

更好的习惯是：

只贴真正相关的代码片段； 日志先删掉无关行，再发给 Claude； 能引用文件就不要反复粘贴同一段内容。

输入越少，处理越轻，token 使用量也就越低。

5. 不是什么任务都要上最强模型
----------------

并不是每个问题，都值得动用最强模型。

一个简单判断方式是：

小任务，比如格式调整、简单改写、快速修改，用轻量模型； 一般编码任务，用中等能力模型； 复杂推理、架构设计、疑难调试，再使用最强模型。

如果所有事情都用重模型处理，很多时候并不会换来明显更好的结果，只会让 token 消耗变得更高。

真正高效的用法，不是永远选择最强，而是让任务和模型匹配。

6. 别陷进无限修正循环
------------

如果你在同一个线程里反复修改同一个回答，对话会越来越长，成本也会越来越高。

这是一种很隐蔽的浪费：你感觉自己只是在“继续优化”，但 Claude 每次都要带着前面那一长串历史继续工作。越改越乱，越乱越贵。

更好的做法是：

发现线程已经混乱时，直接重开； 把问题重新讲清楚； 一次性给出最终要求，而不是不断追加零碎修正。

重新开始并不是浪费，很多时候恰恰是在止损。干净的新上下文，通常比混乱的旧线程更省 token，也更容易得到稳定结果。

7. 提示词要简单，别写成说明书
----------------

长提示词不一定更好。

很多人为了“让 Claude 更懂”，会写一大段背景、重复要求、补充各种显而易见的细节。结果是，输出质量未必提高，token 使用量却实打实增加了。

尽量避免：

重复同一条指令； 加入与任务无关的背景； 过度解释模型本来就能理解的内容； 把简单需求包装得太复杂。

更有效的提示词通常只有三个特点：

清楚； 直接； 只保留关键内容。

你越能把问题说准，Claude 就越不需要在一堆噪音里找重点。

最后
--

把 Claude Code 的 token 使用量降低 90%，靠的不是某个神奇技巧，而是一整套更干净的工作方式。

真正有效的做法是：

保持短会话； 写清楚提示词； 把相关任务合并处理； 严格控制上下文； 选择合适模型； 避免在同一个线程里反复修补。

做到这些之后，你会发现，Claude 并不是一定要消耗那么多 token 才能完成工作。很多浪费都来自重复读取、重复解释和重复修改。

所以，省 token 的本质并不是“少用 Claude”。

而是别让 Claude 一遍又一遍地做同一件事。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547388&idx=1&sn=7146b7928a4db5653e9732c736844fab&chksm=e868ab407bcbe74ef55d934ba226c83b04b62b7c0c6394e3ee8325a54e8b66a4c163c200cf89&scene=90&xtrack=1&req_id=1777095048938308&sessionid=1777094023&subscene=93&clicktime=1777095072&enterid=1777095072&flutter_pos=6&biz_enter_id=4&ranksessionid=1777095048&jumppath=20020_1777095041531,1104_1777095042080,20020_1777095048476,1104_1777095060828&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=1800472b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmvoa1mMtZ+bLvrlRjjNn2xLVAQIE97dBBAEAAAAAAN0iKDxLQLoAAAAOpnltbLcz9gKNyK89dVj0vNDAT5LIQ8eiQqPf/135PhKmMhKwNuqxOwI7E/LvfjAdUfBae/rKqrsQy1glH7gg8izH2+7/XnanlKdYxMsNoo8S8o/17bc6MrqkjUzZvYYSYCM4UyjRACzRfeVOzuW4uNCX5rFXbRVWoxyZF2qCCOIQ0OU5XVBRBQh8Lm0WHnPZ48JzxEaBUd36otryudJqVCaKC79t5n2kbKzB2n5zFravna4AP9+9vrYA9g0MeQ==&pass_ticket=ebdFURp3sX4auOmMJjW6w16QYvpCaCG3jphf1XsNH75UsIyzmg5xb1KciA26uFHx&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8dd505a3-396e-4fe0-92e8-7dbae3def43d/8dd505a3-396e-4fe0-92e8-7dbae3def43d/)
