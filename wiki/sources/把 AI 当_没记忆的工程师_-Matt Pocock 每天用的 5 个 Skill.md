---
title: 把 AI 当_没记忆的工程师_：Matt Pocock 每天用的 5 个 Skill
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/把 AI 当_没记忆的工程师_：Matt Pocock 每天用的 5 个 Skill.md
tags: [evernote, impression, yinxiang]
---

# 把 AI 当"没记忆的工程师"：Matt Pocock 每天用的 5 个 Skill

---

原文链接: [https://mp.weixin.qq.com/s?chksm=8851163dbf269f2b138a47c19ed3365...](https://mp.weixin.qq.com/s?chksm=8851163dbf269f2b138a47c19ed336509052ae6ca63f98c595f710ccb978f7440083a33eb413&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782032740_1&req_id=1782031330553375&scene=169&mid=2453073571&sn=a9173c38854ccda23864a92e7611ef66&idx=2&__biz=MzA4MTU0Nzc2MQ==&sessionid=1782032739&subscene=200&clicktime=1782032771&enterid=1782032771&flutter_pos=4&biz_enter_id=5&jumppath=1001_1782032731413,1104_1782032740937,MMFlutterViewController_1782032741731,1104_1782032742561&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQHUuHie7ZQ1oE/eL6GKbQtBLTAQIE97dBBAEAAAAAAMqiESuwNMQAAAAOpnltbLcz9gKNyK89dVj07oU7+NrtRUDjzcDbYFgWkCg53K+cchs3h7JtnZsSLJqbuFqpmPlUXEsLTSS14QENShOgKw1Lg4FAdeBJp47TP4chhy9LS3FCQs+qLiZ7l9Sw/ehujbeSyo6cu+WCnbKCm1ab0QJFHPBHcFSXqszfC7oSQ6T/msyaSDJOeuaRbVql481dv5HNRUrk5mUzKFZlTQUQtcGoi188i2MwvkPE6c2h8/2iqOJcelIFhng=&pass_ticket=4BAgCLqxVFun2J58TSMGDiYx+5QIzJ3TMnJfYwQQJ5qcb//7UJdeQAADkvdBwue7&wx_header=3)

橙研所

作者是谁**Matt Pocock** 是 TypeScript 圈非常知名的教育者——*Total TypeScript* 系列课程作者、*aihero.dev* 创办人，在 X（@mattpocockuk）上有大量关注，以把复杂工程概念讲得极其清楚著称。这一两年他把重心转向「怎么用 AI 写出高质量代码」，本文就是其中一篇。

太长不读Matt Pocock 的核心判断很反直觉：**AI 写出来的代码质量，主要不取决于 AI 多聪明，而取决于你把工程流程编码得多严。**他把"想清楚 → 写 PRD → 拆任务 → TDD → 改架构"整条链，做成 5 个能一键调用的 Skill。下面逐个说，最后讲那条贯穿始终的哲学。

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/153F5584-60E5-4C1B-A12F-8A28B391A109.png)

图 1 · 5 个 Skill 串成一条从想法到落地的流水线（橙研所据原文梳理）

01/grill-me：先把你自己烤熟
-------------------

最反常识的一个。它不让 AI 急着出方案，而是**反过来拷问你**——用"设计树"一路追问，把你脑子里没想清楚的地方挖出来。作者提到有过一次 50 多个问题的 session。

他有句话我很认同：*Skill 不必长才有用*（"Skills don't have to be long to be impactful"）。`/grill-me` 本身很短，但它改变的是"人先想清楚再让 AI 动手"的顺序。这其实就是 Claude Code 的 Plan Mode 精神——**探索和执行分开，错误假设别带着往下跑。**

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/2D644290-756B-4D17-B4B6-4B6C5CE2C87A.png)

02/to-prd：把讨论焊成文档
-----------------

聊清楚之后，一键把对话变成一份 PRD（带用户故事的 GitHub Issue）。意义在于：**共识不留在聊天记录里，而是沉淀成可追溯的文档。**下一轮 AI 接手时不靠"它还记不记得"，而是读这份文档——和上一篇 Tw93 文章里 HANDOFF.md 的思路一模一样。

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/81FA159E-AF45-48E2-BB41-D131115E7143.png)

03/to-issues：垂直切，不要横着切
----------------------

把目标拆成能独立干完的任务。关键招式是*垂直切片*而不是水平切片，并标好任务之间的阻塞关系。

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/391E95DE-094E-499F-9211-69E47B5110B0.png)

图 2 · 垂直切片：每个任务都是一条能独立验证的端到端薄片

为什么对 AI 尤其重要？因为**能独立验证的任务，AI 才"做没做对"是可判定的**。横着切出来的半成品，没法验证，也就没法让 agent 自己跑。

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/6E388C7E-BF60-4201-B8F0-4E5E5762B18F.png)

04/tdd：红 → 绿 → 重构
-----------------

到了写代码这步，作者用 TDD 的红-绿-重构循环，并称它是*"最一致的改进方式"*。道理也和验证闭环一脉相承：先写一个会失败的测试（红），让 AI 写到它通过（绿），再回头重构。**测试就是 agent 的"做对了没有"的硬标准**，不靠你肉眼看。

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/465458B5-2CAF-43BB-9B1E-44C25CDF613B.png)

05/improve-codebase-architecture：地基烂，AI 也烂
------------------------------------------

最后一个是养护代码地基。作者的原话很直白：*"垃圾代码库里，AI 也只会产出垃圾"*（"garbage code base, the AI will produce garbage within that code base"）。

这点常被忽略：大家总想着"怎么把 prompt 写得更好"，但**AI 是在你的代码库里干活的，地基的整洁度直接决定它能走多远**。所以要持续花精力让架构对 agent 友好——清晰的边界、好导航的结构。

![](.evernote-content/35891F40-72EC-486E-897B-EB73D0444EB3/CF54496C-14F9-4291-A9A3-15E7FC3B63C6.png)

06真正的那条线：AI 是个没记忆的工程师
---------------------

把 5 个 skill 串起来看，作者真正在说的是一件事：**把 AI 当成一个能力很强、但每次都失忆的工程师**。对这样的人，你不会指望他"自己悟"，而会给他一套极严的流程——想清楚、写下来、拆成可验证的小块、用测试卡住、保持地基干净。

流程编码得越严，AI 的输出越稳。放大 AI 的不是更聪明的模型，是更扎实的工程纪律。

这条线和橙研所一直在聊的 harness 方法论是同一个东西：**不靠 agent 自觉，靠把约束和验证焊进流程**。Matt 是用 5 个 GitHub 流的 skill 落地，你也可以用自己的方式落地——重点是那套纪律，不是具体哪个 skill。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=8851163dbf269f2b138a47c19ed336509052ae6ca63f98c595f710ccb978f7440083a33eb413&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782032740_1&req_id=1782031330553375&scene=169&mid=2453073571&sn=a9173c38854ccda23864a92e7611ef66&idx=2&__biz=MzA4MTU0Nzc2MQ==&sessionid=1782032739&subscene=200&clicktime=1782032771&enterid=1782032771&flutter_pos=4&biz_enter_id=5&jumppath=1001_1782032731413,1104_1782032740937,MMFlutterViewController_1782032741731,1104_1782032742561&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQHUuHie7ZQ1oE/eL6GKbQtBLTAQIE97dBBAEAAAAAAMqiESuwNMQAAAAOpnltbLcz9gKNyK89dVj07oU7+NrtRUDjzcDbYFgWkCg53K+cchs3h7JtnZsSLJqbuFqpmPlUXEsLTSS14QENShOgKw1Lg4FAdeBJp47TP4chhy9LS3FCQs+qLiZ7l9Sw/ehujbeSyo6cu+WCnbKCm1ab0QJFHPBHcFSXqszfC7oSQ6T/msyaSDJOeuaRbVql481dv5HNRUrk5mUzKFZlTQUQtcGoi188i2MwvkPE6c2h8/2iqOJcelIFhng=&pass_ticket=4BAgCLqxVFun2J58TSMGDiYx+5QIzJ3TMnJfYwQQJ5qcb//7UJdeQAADkvdBwue7&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b6e75ffe-15e1-48a2-abd6-ba2c36e7aa7f/b6e75ffe-15e1-48a2-abd6-ba2c36e7aa7f/)
