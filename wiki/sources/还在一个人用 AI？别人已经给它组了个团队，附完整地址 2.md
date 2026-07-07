---
title: 还在一个人用 AI？别人已经给它组了个团队，附完整地址 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/还在一个人用 AI？别人已经给它组了个团队，附完整地址 2.md
tags: [evernote, impression, yinxiang]
---

# 还在一个人用 AI？别人已经给它组了个团队，附完整地址

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484467&idx=1&sn=2e4246081483b2ba4e11de88bd5a3ca8&chksm=f13d4cf4a90f89ee2cc903bc4b123b8ced997c80f4136bb7f869ed52daa075eb544f2335213a&scene=90&xtrack=1&req_id=1776010104394686&sessionid=1776007097&subscene=93&clicktime=1776010141&enterid=1776010141&flutter_pos=42&biz_enter_id=4&ranksessionid=1776010104&jumppath=20020_1776010094436,1104_1776010095134,20020_1776010103899,1104_1776010117439&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004635&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQYv0N+cUtGrkLBcCpS62LVBLTAQIE97dBBAEAAAAAADxsLDgNifsAAAAOpnltbLcz9gKNyK89dVj08CR4ZsMQ2GRkC5jmJxPU8m4a8DxhwXxul5ptwaXVwDPb2dPt/DKH/7KUPtUn9kjq0vrtnX4vhE1J6eg866ztXv8BfnN5jFQOHfXE1//5UBrrJdwnZ+KWIMm0anllUj2nZyz+W5u/2/nRrFI/VgmpOpjjbLrf1hrs1LlgFvSELtGXK2cx1Ij+CQKO2ndI5pCIgpgKibKKk7MLsVw3HcbqKlNblERG9M08TPbFTtw=&pass_ticket=ZA1yZ1aYyVzaq6njJC/Pf/pz6szcKWChtxnV6wnOjRd9ATUbUcGYL0IrJg2wkCnA&wx_header=3)

Original莲花明AI落地手记

一个 AI 不够用了。

上周我同时赶三个项目的 deadline，让 AI 一边写方案一边排查 bug 一边回客户消息。

结果它开始胡言乱语——方案里混进了 debug 日志，给客户的回复里夹了一段 SQL。

凌晨 2 点我想明白一件事：

你缺的不是更聪明的 AI，你缺的是一个 AI 团队。

这件事在技术圈叫 subagent。一个主 AI 负责调度，下面挂几个专业方向的“子员工”，写方案的写方案，排 bug 的排 bug，互不干扰。

![](.evernote-content/64CB20D1-B031-407F-80DA-653DDB67E078/6CA06CC2-AC87-4690-9EA6-C9F491545BB2.png)

GitHub 上已经有大佬把团队组好了，全部开源。

我翻了一圈，stars 破万的有 5 个仓库，加起来 231.7k 星。

最猛的 everything-claude-code，128k 星——28 个专业 agent + 119 个 skill，clone 下来 5 分钟装完，等于一键多了一家虚拟公司。

第二个 wshobson/agents，33.4k 星，更夸张——182 个 agent，后端架构师、安全审计师、产品经理全齐了，每个人都是一个配置文件。

awesome-claude-code 38.1k 星，不给你 agent，给你一张“去哪找 agent”的地图。遇到新场景先去它那里搜，大概率有现成方案。

VoltAgent 团队出了两个仓库：awesome-claude-code-subagents（17k 星）把 130+ agent 按 10 大类整理好，按需安装不吃重；awesome-agent-skills（15.2k 星）收了 1086 个 skill，Anthropic、Google、Vercel 官方都在贡献。

我装完跑了一周，说三个最直接的变化。

第一，上下文不再互相污染。以前切项目，AI 经常把上一个项目的东西混进来。现在每个项目配一组专属 agent，各管各的。

第二，代码质量上了一个台阶。以前提交前自己检查，现在扔给 code-reviewer，它不会像你的主 AI 那样夸你“做得真好”，它专门挑毛病。

第三，排查效率翻倍。以前翻日志靠自己，现在丢给 researcher，它先验证数据源再下结论，比我自己查靠谱。

这些仓库的作者把脏活都干完了，你只需要 clone 下来复制到自己目录。

一次 clone，用一年。

如果你现在还是一个人跟一个 AI 对话框死磕，建议今晚花半小时把团队搭起来。

区别就在于——

一个人加班到 12 点，还是一个人带团队 6 点下班。

**5 个仓库链接：**

**everything-claude-code 128k⭐**  
最全一站式方案，28 个 agent + 119 个 skill  
https://github.com/affaan-m/everything-claude-code

![](.evernote-content/64CB20D1-B031-407F-80DA-653DDB67E078/D66BE72B-B257-4D70-A2A0-367890F9CF06.png)

**awesome-claude-code 38.1k⭐**  
Claude Code 生态大索引，当词典用  
https://github.com/hesreallyhim/awesome-claude-code

![](.evernote-content/64CB20D1-B031-407F-80DA-653DDB67E078/1604AF90-2D39-4EC4-B47B-B4004ECF5723.png)

**wshobson/agents 33.4k⭐**  
规模之王，182 个 agent 全家桶  
https://github.com/wshobson/agents

![](.evernote-content/64CB20D1-B031-407F-80DA-653DDB67E078/23FA5DD6-0781-454A-80F4-98B6EF3738C5.png)

**awesome-claude-code-subagents 17k⭐**  
分类最清晰，130+ agent 按 10 大类组织  
https://github.com/VoltAgent/awesome-claude-code-subagents

![](.evernote-content/64CB20D1-B031-407F-80DA-653DDB67E078/8282D628-9415-489B-A55B-00F721B76019.png)

**awesome-agent-skills 15.2k⭐**  
1086+ skill，Anthropic/Google/Vercel 官方贡献  
https://github.com/VoltAgent/awesome-agent-skills

![](.evernote-content/64CB20D1-B031-407F-80DA-653DDB67E078/A0C9C846-B349-46BF-A0AF-2045452ED44C.png)

关注「AI 落地手记」，后续更多干活。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484467&idx=1&sn=2e4246081483b2ba4e11de88bd5a3ca8&chksm=f13d4cf4a90f89ee2cc903bc4b123b8ced997c80f4136bb7f869ed52daa075eb544f2335213a&scene=90&xtrack=1&req_id=1776010104394686&sessionid=1776007097&subscene=93&clicktime=1776010141&enterid=1776010141&flutter_pos=42&biz_enter_id=4&ranksessionid=1776010104&jumppath=20020_1776010094436,1104_1776010095134,20020_1776010103899,1104_1776010117439&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004635&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQYv0N+cUtGrkLBcCpS62LVBLTAQIE97dBBAEAAAAAADxsLDgNifsAAAAOpnltbLcz9gKNyK89dVj08CR4ZsMQ2GRkC5jmJxPU8m4a8DxhwXxul5ptwaXVwDPb2dPt/DKH/7KUPtUn9kjq0vrtnX4vhE1J6eg866ztXv8BfnN5jFQOHfXE1//5UBrrJdwnZ+KWIMm0anllUj2nZyz+W5u/2/nRrFI/VgmpOpjjbLrf1hrs1LlgFvSELtGXK2cx1Ij+CQKO2ndI5pCIgpgKibKKk7MLsVw3HcbqKlNblERG9M08TPbFTtw=&pass_ticket=ZA1yZ1aYyVzaq6njJC/Pf/pz6szcKWChtxnV6wnOjRd9ATUbUcGYL0IrJg2wkCnA&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ba229c00-48a8-4805-ba2c-b8aeb1f95cfb/ba229c00-48a8-4805-ba2c-b8aeb1f95cfb/)
