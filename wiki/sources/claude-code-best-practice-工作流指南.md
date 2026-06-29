---
title: claude-code-best-practice：Claude Code 工作流指南
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://github.com/shanraisshan/claude-code-best-practice]
source_path: 印象笔记管理工具/1.7万星，claude-code-best-practice：Claude Code 工作流指南.html
tags: [claude-code, workflow, best-practice, command, skill, agent]
updated: 2026-06-27
---

---
title: "1.7万星，claude-code-best-practice：Claude Code 工作流指南"
source: evernote
type: note
export_date: 2026-06-26
guid: 0bb52732-3a47-422a-83eb-e1f1250d2583
---

# 1.7万星，claude-code-best-practice：Claude Code 工作流指南

原文链接: [https://mp.weixin.qq.com/s?chksm=c093b6d1f7e43fc7a72f9219110fbf8...](https://mp.weixin.qq.com/s?chksm=c093b6d1f7e43fc7a72f9219110fbf86380813a25fe0674a5b56beb55b75b476fc1a43b1b708&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1774916204_1&req_id=1774911368136129&scene=169&mid=2247484837&sn=c51c38f6cb8e49fd6e4e406753e055d0&idx=1&__biz=MzkwMzY1Mjg5MQ==&sessionid=1774917255&subscene=200&clicktime=1774919662&enterid=1774919662&flutter_pos=15&biz_enter_id=5&jumppath=20020_1774919637376,1104_1774919637725,20020_1774919647736,1104_1774919653165&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004629&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQFnnAhqgaRVtmUQY3q2yUfBLTAQIE97dBBAEAAAAAAFOzA4TIKNgAAAAOpnltbLcz9gKNyK89dVj0qcQY7CYpC/l7sPA3v0tIePddb4i0QsdoWYRrXre2CpJ4cE/vpege9gND29TcmSLk3gTID9fscHREHfG68wUhMUyAeQeQ8WaLkUgA+7bh958j3N0Bt49UgCd5NM7G13ECaGg/B92tu53pbG7umtLXSgVWOQElm0CSJdmnkRclEC45C1Ncf5lpOTbi1Kfu/9mZOVuYS7Rf58Y+62n9KvjCZg/RWdYRNXuIwa9zWgE=&pass_ticket=Opn93icMsraxEfb26kcMPBXdIVYlKjc7VWFojCU9JPuTp9IlVDignUmUOOi4ukPp&wx_header=3)

OriginalwsleepybearGit Trend

**项目卡片**

- **项目名**：claude-code-best-practice
- **GitHub**：https://github.com/shanraisshan/claude-code-best-practice[1]
- **一句话判断**：**这不是教你几条 Claude Code 小技巧的仓库，而是教你怎么把 Claude Code 组织成一套可复用、可协作、可持续迭代的工作流。**

如果你已经在用 Claude Code，但一进真实项目就开始乱：对话越来越长，规则越堆越多，哪些事该放 command、哪些该沉淀成 skill、哪些该交给 subagent，越做越分不清——**这个仓库解决的正是“会用 Claude Code，但不会把它组织成稳定流程”这个问题。**

![](attachments/4c8d94a034236f7c.png)

*这张图基本概括了仓库的核心：入口层是 command，执行层是 agent / subagent，复用层是 skill、settings、memory 和 MCP。*

这个仓库到底是干什么的

先把结论说透：**claude-code-best-practice 的核心用途，不是教你怎么下命令，而是教你怎么设计 Claude Code 的工作流和分工。**

很多人真正卡住，不是不会用 Claude Code，而是进入真实项目后马上遇到三个问题：

- **上下文混乱**：所有规则、背景、临时需求都塞进一个会话，越聊越钝。
- **职责混乱**：command、skill、agent、settings、memory、MCP 各自该干什么，没有边界。
- **流程失控**：同样一类任务每次都重讲一遍，无法复用，也很难协作。

**这个仓库做的事，就是把这些能力一层层拆开，告诉你该把什么放在哪里。**

它最重要的价值：把分工讲明白

这套仓库最值得读的，不是“又多了几个技巧”，而是它把 Claude Code 里最容易混掉的几类能力讲出了边界。

- **command**：适合做**入口、触发词、固定流程包装**。你希望一句话拉起一套动作，就放这里。
- **skill**：适合放**可复用的方法、步骤、判断标准**。凡是以后还会反复用到的经验，都应该沉淀成 skill。
- **agent / subagent**：适合处理**重任务、长任务、需要独立上下文的任务**。不要把所有复杂活都塞在主会话里。
- **settings**：适合放**稳定规则和全局偏好**。比如你长期希望模型遵守的约束，不必每次重讲。
- **memory**：适合放**持续性背景和长期记忆**。它解决的是“这件事以后也得记得”。
- **MCP**：适合接入**外部工具、数据源和系统能力**。重点不是“连上了没有”，而是有没有进入你的日常流程。

**这套分工一旦清楚，Claude Code 才会从“能聊”变成“能跑流程”。**

适合谁，不适合谁

**适合的人**：

- **已经在用 Claude Code，但开始遇到上下文混乱、职责混乱、流程失控的人**
- **想把 Claude Code 从“会用”推进到“能稳定用于真实项目”的人**
- **希望把自己的经验整理成 command / skill / agent 分工的人**

**不太适合的人**：

- **只是想看基础命令和快速入门的人**
- **还没进入真实项目、暂时不需要流程设计的人**
- **当前只想偶尔让 AI 改个小 bug，并不关心复用和协作的人**

所以读这个仓库，最好的预期不是“再学几个招”，而是**建立一套判断：什么留在主会话，什么做成 command，什么沉淀成 skill，什么切给 subagent，什么放进长期配置。**

最短上手闭环，可以怎么走

如果你现在就想把它用起来，最短闭环其实很简单：

1. **先挑一个你经常重复的任务**，不要一上来就重构全部流程。
2. **把任务入口收成一个 command**，让触发方式固定下来。
3. **把会重复解释的方法写成 skill**，别每次重新讲背景和步骤。
4. **把又长又重的执行过程切给 subagent**，把主会话留给判断和调度。
5. **把稳定规则放进 settings / memory**，把外部能力接到 MCP 里。

**做到这一步，你就已经不是“在和 Claude Code 聊天”，而是在搭一个能持续复用的工作流。**

最后一句

如果你现在的状态是“Claude Code 已经会用，但越用越乱”，那这个仓库最值得看的价值就一句话：**它在教你怎样给 Claude Code 做分工、做组织、做工作流，而不只是补几个技巧。**

当这件事理顺以后，Claude Code 才更有机会从一个偶尔好用的助手，变成**能长期参与真实项目的协作系统**。

---

如果这篇对你有用，建议点个关注。我会持续把 GitHub 上值得用的 AI 工具拆成「最短上手闭环 + 坑点清单 + 可复用配置」，让你少走弯路。

### 引用链接

[1]*https://github.com/shanraisshan/claude-code-best-practice*
