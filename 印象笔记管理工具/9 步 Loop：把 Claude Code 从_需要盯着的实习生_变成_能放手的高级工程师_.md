# 9 步 Loop：把 Claude Code 从"需要盯着的实习生"变成"能放手的高级工程师"

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c47661faf301e8ec56295b726203dab...](https://mp.weixin.qq.com/s?chksm=c47661faf301e8ec56295b726203dab3ba6a89ace9756f5a1fd6579b50725c89e89d5125af90&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_5&req_id=1782035209366580&scene=169&mid=2247483768&sn=cf51e9a68e6248c1069398ae2872ec89&idx=1&__biz=Mzk2NDE5Njg0NQ==&sessionid=1782032739&subscene=200&clicktime=1782035856&enterid=1782035856&flutter_pos=49&biz_enter_id=5&jumppath=MMWebViewController_1782035832744,1104_1782035842280,20020_1782035845029,1104_1782035853143&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQxGqCzuSiMa4qHKt65jbVRRLTAQIE97dBBAEAAAAAAE9nNMpkPwYAAAAOpnltbLcz9gKNyK89dVj0DerhxseB5Wo7h29wrgAW8wh/ddWRwWT47tgATrY/WyYBP+1wGBnjZmmgjgBLkFW+uIpwuQQukeFjsE4qNGqASsgfmjf7o8iC5A+e6RI4u3XPZdXNSiytZZJfo3zIkuTWTUZ5HhFur6X/93tsxR0rZv2GHwM0SL0cAI3hoxy2B4LPw+cWM//anY0Qy/zDLHpzxKdheUaB3NYxc3ajNrrAhxusTqnsw6zacvDNI88=&pass_ticket=nZ6QRdJsifTqzrdaj/+O68xmqgBBCsflxfy2YitueqcxcxffcD/naWp+eukAX5UL&wx_header=3)

9 步 Loop：把 Claude Code 从"需要盯着的实习生"变成"能放手的高级工程师"
===============================================

OriginalAI 极未来AI 极未来

快速小结：大多数人用 Claude Code 的方式是：打一段指令、看它改文件、肉眼检查、再打下一段。这能用，但这是把一个能自主工作的 Agent 当人肉问答机在用。一个高级工程师不是这样干活的——他先读代码理解现状，做方案让你审批，小步实现，自动跑测试，让别人 review，改完再跑一轮，确认没问题才提交。这整个流程完全可以用 Claude Code 自带的功能搭建成一个可重复的自动化 loop。搭一次，以后每个任务都走同样的纪律。

正文开始

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/79A96222-E51C-43E9-B7E4-F775C4D6E111.png)

Claude Code 自带了搭建这个 loop 需要的所有原语：Plan 模式、Subagent、Hook、CLAUDE.md、Slash 命令。"初级"和"高级"之间的差距不是模型能力——是你有没有把这些东西串成一个 loop。

第 1 步：先理解，再动手
-------------

新手一上来就让 Claude 开始改代码。高级做法是先让它理解代码库。

Claude Code 有内置的 Explore subagent——在独立上下文窗口里只读你的代码，不改任何东西，不污染主会话。

```
先探索认证模块在这个代码库里怎么工作的。  
画出涉及的文件、数据流、和任何看起来脆弱的地方。  
先别改任何东西。
```

理解了再动手，和不理解就开干，产出质量天差地别。

第 2 步：Plan 模式出方案
----------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/728603F7-0473-4BD1-98EF-ECDFE31DE5F8.png)

Plan 模式让 Claude 在不执行任何操作的情况下思考完整方案。它会产出一个逐步计划，你可以读、改、批准，然后才开始动手。

```
进入 plan 模式：详细说明怎么给 API 加限流。  
列出要碰哪些文件、改的顺序、可能的风险。  
等我批准后再写代码。
```

在这一步抓住错误方向的成本是零——因为还没写任何代码。等写了一半再推翻，成本巨大。

第 3 步：CLAUDE.md 写入你的团队标准
------------------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/360FEC12-2122-4F95-9DD9-BB06884436A4.png)

CLAUDE.md 是 Agent 每次启动都读的"团队规范手册"。你的约定、命令、模式写一次，每个会话自动生效。

```
# 项目规范  
## 约定  
- TypeScript 严格模式，不允许 any  
- 函数优先于类  
- 每个新函数必须有测试  
  
## 命令  
- 测试：npm run test  
- Lint：npm run lint  
  
## 规则  
- 不要编辑 /generated 目录  
- 先匹配现有文件的风格再加代码
```

**重要的细微差别**：CLAUDE.md 的指令是建议性的——Claude 大部分时候遵守，但不是 100%。绝对不能违反的规则，需要第 5 步的 Hook 来强制执行。CLAUDE.md 设默认值，Hook 执行非谈判项。

第 4 步：小步实现，可审查的粒度
-----------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/96717AFA-756C-4392-B572-CE95833CF2C2.png)

方案批准了、标准加载了，实现步骤反而变得很无聊——这正是目的。

```
只实现计划的第 1 步。保持改动小且自包含。  
遵循 CLAUDE.md 的约定。  
完成第 1 步后停下来让我验证，再继续下一步。
```

小改动容易验证、容易回滚。一个 600 行的 diff 你根本审不了。

第 5 步：Hook 强制执行非谈判项
-------------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/2C1BE8A7-CDB2-4277-B8CE-E52F0050D546.png)

这一步是区分"看起来高级"和"真正高级"的分水岭。

Hook 是在 Claude Code 生命周期特定节点触发的 shell 命令。和 CLAUDE.md 不同，Hook **每次都确定性地执行**——“每次编辑后跑 lint”、"测试没全过不允许 commit"这些变成了保证而非建议。

```
{  
"hooks":{  
"PostToolUse":[{  
"matcher":"Edit|Write",  
"command":"npm run lint && npm run test"  
}]  
}  
}
```

Claude 不可能"忘记"跑检查——Hook 100% 触发。

第 6 步：让它证明改动有效
--------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/8511A616-3492-4718-BC18-72EAA6491406.png)

高级工程师不信任没测试过的代码——包括自己写的。

```
为这个改动写测试，包括 token 过期的边界情况。  
跑完整测试套件，给我看结果。  
如果有任何失败，修好了再继续。
```

搭配第 5 步的 Hook，测试套件在每次代码改动后自动运行。"做完了"意味着测试真的通过了，而不是 diff 看起来合理。

第 7 步：让第二个 Agent 审查第一个
----------------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/B6A99465-DF2D-4676-B89D-B1E46CEA3DB4.png)

代码审查之所以有效，是因为审查者没有写那段代码。你可以复制这个机制——开一个审查 subagent，在干净的上下文窗口里，唯一任务就是挑毛病。

```
启动一个审查 subagent。它的任务：以一个怀疑论的高级工程师身份  
审查我刚才的 diff。检查安全问题、遗漏的边界情况、  
任何违反 CLAUDE.md 的地方。只报告问题，不要修。
```

因为它有自己的上下文且带着批判者的任务，它能抓住写代码的那个 Claude 自己说服自己忽略的问题。

第 8 步：修了再检查，循环到干净
-----------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/6F7CDB47-9A76-4F1F-9EE6-A97F56DD11D9.png)

这一步是它从"流水线"变成"循环"的地方。审查发现问题 → Agent 修复 → 检查和审查再跑一遍 → 直到没有新问题。

```
处理审查者提出的每个问题。修完后，  
重新跑测试，并再次启动审查 subagent 审查更新后的 diff。  
循环直到审查返回干净。给我看最终审查结论。
```

跟高级工程师处理 code review 评论一模一样——不是确认收到就完了，是修了、验了、再审了。

第 9 步：封装成一个命令
-------------

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/C641B136-61F9-4A2A-BFA6-AA38ED29A8B6.png)

改动干净了，commit、开 PR。最后一步是把整个 9 步循环封装成一个 slash 命令，以后永远不需要手动拼装。

```
# .claude/commands/ship.md  
# /ship：运行完整的高级工程师 loop  
1. 探索相关代码（Explore subagent）  
2. 出方案并等待我的批准  
3. 按 CLAUDE.md 小步实现  
4. 写测试并运行（Hook 强制执行）  
5. 启动审查 subagent 审查 diff  
6. 修复问题、重新测试、重新审查直到干净  
7. 用清晰的信息 commit 并开 PR
```

一个命令 `/ship`，整个流水线跑起来。

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/3D8BD49D-23F7-4540-B9D2-28E41C3A553B.png)

为什么这有效
------

这九步没有一步是 trick。它们就是一个高级工程师对每个任务都会走的纪律，映射到了 Claude Code 已经自带的功能上：

* • **探索**意味着它先理解再编辑——像高级工程师先读代码
* • **Plan 模式**意味着坏方案在零成本时就被拦住
* • **CLAUDE.md + Hook**意味着标准加载了、关键规则被强制执行
* • **测试 + 独立审查**意味着"做完了"是挣来的不是宣称的
* • **Slash 命令**意味着你搭建一次、永远运行

**老实说**：这不会让 Claude Code 完美无缺——没有什么能。但"需要盯着的实习生"和"可以信任交给任务的高级工程师"之间的差距不是更好的模型，是你有没有搭建这个 loop。搭一次，每个任务都走它。

![](.evernote-content/38DBC7F4-5B96-480B-8CEE-268268A84FB2/9A2C8308-37DF-4981-9DB8-03167701FADF.png)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c47661faf301e8ec56295b726203dab3ba6a89ace9756f5a1fd6579b50725c89e89d5125af90&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_5&req_id=1782035209366580&scene=169&mid=2247483768&sn=cf51e9a68e6248c1069398ae2872ec89&idx=1&__biz=Mzk2NDE5Njg0NQ==&sessionid=1782032739&subscene=200&clicktime=1782035856&enterid=1782035856&flutter_pos=49&biz_enter_id=5&jumppath=MMWebViewController_1782035832744,1104_1782035842280,20020_1782035845029,1104_1782035853143&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQxGqCzuSiMa4qHKt65jbVRRLTAQIE97dBBAEAAAAAAE9nNMpkPwYAAAAOpnltbLcz9gKNyK89dVj0DerhxseB5Wo7h29wrgAW8wh/ddWRwWT47tgATrY/WyYBP+1wGBnjZmmgjgBLkFW+uIpwuQQukeFjsE4qNGqASsgfmjf7o8iC5A+e6RI4u3XPZdXNSiytZZJfo3zIkuTWTUZ5HhFur6X/93tsxR0rZv2GHwM0SL0cAI3hoxy2B4LPw+cWM//anY0Qy/zDLHpzxKdheUaB3NYxc3ajNrrAhxusTqnsw6zacvDNI88=&pass_ticket=nZ6QRdJsifTqzrdaj/+O68xmqgBBCsflxfy2YitueqcxcxffcD/naWp+eukAX5UL&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8be8656c-1e27-42e5-bba0-44cc8d1daa20/8be8656c-1e27-42e5-bba0-44cc8d1daa20/)