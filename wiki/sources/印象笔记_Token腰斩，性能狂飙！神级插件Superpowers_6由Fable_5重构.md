---
title: "Token腰斩，性能狂飙！神级插件Superpowers 6由Fable 5重构"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Token腰斩，性能狂飙！神级插件Superpowers 6由Fable 5重构.md
tags: [印象笔记]
---

# Token腰斩，性能狂飙！神级插件Superpowers 6由Fable 5重构

# Token腰斩，性能狂飙！神级插件Superpowers 6由Fable 5重构 --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzU

---

# Token腰斩，性能狂飙！神级插件Superpowers 6由Fable 5重构

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518630&idx=1&sn=19cbff8dbba7535b4e38340607940113&chksm=e9aee37c93c4350694e8f9fdf761db1cc0707d164e1d4692aa2c3bcac385c05ba8a2b42bed03&scene=90&xtrack=1&req_id=1783228433927669&sessionid=1783227213&subscene=93&clicktime=1783228547&enterid=1783228547&flutter_pos=3&biz_enter_id=4&ranksessionid=1783228434&jumppath=20020_1783227219363,1104_1783228431511,20020_1783228433450,1104_1783228483591&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b31&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ82k9dU7W5PsvvqlFD6hyNRLLAQIE97dBBAEAAAAAACrbLNtoBUcAAAAOpnltbLcz9gKNyK89dVj0WbIhxTSPYyk5Nbt4w5q1ohW4FTVg41zx1T3DazY7VK+bamyoxLiQyC9nzUFdW8g8vml40OZdvxRB/EI4PvlE34b258qxc1UmibE5+3HXy+MWq5WAqkAcVU1ofhRcmCQOt1laFzxdbyGQz7Jdfa46oXj88zkxWuiDZVB3YqS8BDB7usqSsc73wISdM73Dz6E9w517RIAicr5W3FWf5i6L7HVfYqR8&pass_ticket=4fgjBf7wbXK2RW+k+RD0fydKja+3YDTLER+QHuXb8kdsmvZtMmxeoawsItcrh/p8&wx_header=3)

Original字节笔记本字节笔记本

![](.evernote-content/13FE8453-4494-4843-9FE8-55444CECA4CC/9B28CBC7-D545-4719-8067-872CD9B925F4.png)

Superpowers 6 新的版本由Fable 5进行了重构，构建耗时降低约 50%，token 消耗降低约 60%。

Superpowers作为Code Agent的神级插件，相信大家都已经不陌生。

它是一套给编码 Agent 用的完整开发方法论，建立在一组可组合的技能之上，逼着 Claude Code、Codex 这些工具在写代码前先问清楚需求，再拆任务，再派子代理干活，最后两阶段审查。

没有 Superpowers 之前，AI 编码直接需求模糊就直接开写，写完发现跟你想的不是一回事，要么是不写测试或者测试补得很敷衍，整个过程没有计划，做到哪算哪。

有了 Superpowers 就是给 AI 配一套流程。

先用 brainstorming 技能把模糊需求逼问成清晰的 spec,分段展示给你确认。

确认后用 writing-plans 把工作拆成一个个 2 到 5 分钟能做完的小任务，每个任务都写清楚要改哪些文件、完整代码、怎么验证。

最后进入 subagent-driven-development，每个任务派发一个全新的子代理去执行，再走两阶段审查，先查是否符合 spec，再查代码质量。

这套工作流目前已经成为了 AI 编程的标配。

这次重构使用了 Fable 5，[我自己使用Fable 5 做了一个英文点读机的例子](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518592&idx=1&sn=0cfdbe281175d09819344f03809aa334&scene=21#wechat_redirect)。

Superpowers开源作者Jesse一开始对 Fable 5 的期待并不很高，能省 15% 的 token 就够了。

结果三轮改动下来，完全不是这么回事。

第一轮，Fable 5 把 reviewer 查代码变更的方式从"自己跑 git 命令去查"改成"预先打包好格式化 diff 直接喂进去"。

这次下来省了大概 10% 的时间和 token。

第二轮更有意思。Jesse 自己琢磨出一个方案，把两个各自独立跑的 reviewer，其中一个查 spec 是否符合,一个查代码质量合并成一个。

结果第二天醒来，发现 Fable 5 已经自己想到、实现、验证了同一个方案。

人和 AI 同时收敛到了同一个答案，这种巧合读起来有点毛骨悚然，和我之前写的那个 Fable 5 的案例的感受如出一辙。

第三轮是重头戏。

Fable 5 自己发起了一个 autoresearch loop，用 Opus 当协调者，预先登记假设，批量跑了 25 组以上的实验，持续 36 小时,烧掉相当于 650 美元的算力。

跑出来几个反直觉的结论:

精简 reviewer 的指令能让输出压缩 41%，判断质量不受影响，给流程步骤加旁白说明能再省 54%,而且几乎零方差。

过程当中按任务复杂度动态分配模型：

简单任务用更便宜的 haiku，能省钱，系统还能在发现任务其实不简单时自动拒绝降级，不会因为省钱牺牲质量。

三轮下来，最终效果是构建耗时降低约 50%，token 消耗降低约 60%。

6.0 这次还顺手做了一轮去 Claude Code 方言化的改写。

早期版本的技能描述用的是 Claude Code 的说法,比如"用 Task 工具""写进 CLAUDE.md"，这次统一改成了更通用的表达，比如"派发一个子代理""你的指令文件"，并给每个 harness 单独配了一份工具映射参考文件。

同时新增了 Kimi Code、Pi、Antigravity 三个新 harness 的支持，brainstorming 的可视化配套功能也换了个更安全的实现方式。

算是高度契合了我的使用方式 [6月工具模型使用排行！我的主力现在是这几个](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518548&idx=1&sn=874aaac6488a090331563fd5cd3a50a5&scene=21#wechat_redirect)

新版本的安装方式没有任何的改变。

Claude Code走官方插件市场，依次执行:

/plugin marketplace add obra/superpowers-marketplace  
/plugin install superpowers@superpowers-marketplace

装完退出重启 Claude Code，用 /skills 确认技能已经加载。

如果想手动装,也可以直接 clone 到本地技能目录:

mkdir -p ~/.claude/skills  
git clone https://github.com/obra/superpowers.git ~/.claude/skills/superpowers

如果想按项目单独配置，方便团队共享同一套设置,在项目根目录下再放一份:

mkdir -p .claude/skills  
cp -r ~/.claude/skills/superpowers .claude/skills/

装好之后不需要额外敲命令，brainstorming 技能会在你开始描述需求时自动激活，通过提问帮你把想法澄清清楚。

Codex App 里 Superpowers 已经被收录进官方插件市场，不需要自己加 marketplace 源。

操作是打开 Codex App,点侧边栏的 Plugins，在 Coding 分类下找到 Superpowers，点旁边的 + 号,跟着弹出的提示走完流程，比 Claude Code 简单。

这套方案如果用在远程上也非常好用，可以搭配我现在用的方案[我目前使用的两套远程Vibe Coding的方案](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518611&idx=1&sn=08857091b5996c8e27bc516e7920d85e&scene=21#wechat_redirect)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518630&idx=1&sn=19cbff8dbba7535b4e38340607940113&chksm=e9aee37c93c4350694e8f9fdf761db1cc0707d164e1d4692aa2c3bcac385c05ba8a2b42bed03&scene=90&xtrack=1&req_id=1783228433927669&sessionid=1783227213&subscene=93&clicktime=1783228547&enterid=1783228547&flutter_pos=3&biz_enter_id=4&ranksessionid=1783228434&jumppath=20020_1783227219363,1104_1783228431511,20020_1783228433450,1104_1783228483591&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b31&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ82k9dU7W5PsvvqlFD6hyNRLLAQIE97dBBAEAAAAAACrbLNtoBUcAAAAOpnltbLcz9gKNyK89dVj0WbIhxTSPYyk5Nbt4w5q1ohW4FTVg41zx1T3DazY7VK+bamyoxLiQyC9nzUFdW8g8vml40OZdvxRB/EI4PvlE34b258qxc1UmibE5+3HXy+MWq5WAqkAcVU1ofhRcmCQOt1laFzxdbyGQz7Jdfa46oXj88zkxWuiDZVB3YqS8BDB7usqSsc73wISdM73Dz6E9w517RIAicr5W3FWf5i6L7HVfYqR8&pass_ticket=4fgjBf7wbXK2RW+k+RD0fydKja+3YDTLER+QHuXb8kdsmvZtMmxeoawsItcrh/p8&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ec9ba22a-a6c7-4be5-8f5b-4c26430a2785/ec9ba22a-a6c7-4be5-8f5b-4c26430a2785/)