---
title: Codex 装完别急写代码，先装这 5 个 Skill
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Codex 装完别急写代码，先装这 5 个 Skill.md
tags: [evernote, impression, yinxiang]
---

# Codex 装完别急写代码，先装这 5 个 Skill

---

原文链接: [https://mp.weixin.qq.com/s?chksm=8f35985eb8421148c3305ded4c6d862...](https://mp.weixin.qq.com/s?chksm=8f35985eb8421148c3305ded4c6d86297e82792229305e95364e9923d6ec930109181c0d3469&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782340110_2&req_id=1782342212142578&scene=169&mid=2649114292&sn=a89401fdbfbb13dd5f470c220ee13eeb&idx=1&__biz=MzIwNjA1NjMyNQ==&sessionid=1782340109&subscene=200&clicktime=1782343854&enterid=1782343854&flutter_pos=14&biz_enter_id=5&jumppath=1104_1782343837607,WAWebViewController_1782343841067,WAWebViewController_1782343842451,1104_1782343843608&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQuPB6TGmz2rgaIbZUsbh7NxLTAQIE97dBBAEAAAAAAG3+CpT30KQAAAAOpnltbLcz9gKNyK89dVj0CFQsvYpRwMbEtTWv80xFSjQgwDRLAGL+b7XEAYH4eMlPW41heVsKEzU5DwlWL94/UhxyM/e5NqoIp/s92uNoJigDhfka9dIQxvfrlT9OjgXZJgh9Pd94nBc/18ot2RrltBFFHafE8ocuaZ6QL9hGEaylkeaB4z0pei/RKB0y2FaAFTfJL20zxAAfMqnRmdKTircUwq7WHTxDmry321ovwn+7biz337bdg047jdY=&pass_ticket=pkJQBQ7U+m+6kM137nW00l05QLYMrns5O+RmeWlzTrGlRuCHBa+M1wAcqQP4kmzS&wx_header=3)

OriginalAI智闻说 AI智闻说

*Codex 装完先配 Skill 再用，跟直接上手，差别很大。社区公认的几个 Skill，能让 Codex 按规矩办事。*

装完 Codex，兴冲冲打开终端，打了第一句"帮我写个登录页面"——结果出来的代码又泛又乱，改了三遍还不对。

但你可能漏了一步：装 Skill。

Skill 就是给 Codex 装上的"岗位手册"。不装，它只靠默认行为猜你想干什么；装了，它按你定好的规矩做事。

这篇文章只回答一个问题：刚装完 Codex 的新手，应该装哪几个 Skill，怎么装，装完有什么变化。

Skill 是什么，两句话说清楚
----------------

Skill 就是一个 Markdown 文件，告诉 Codex 在特定场景下怎么做。

不装 Skill 的 Codex 就像没装任何 App 的新手机——能开机，但什么也干不好。每次你都得手动重复"先写测试再写代码""别改不相关的文件"，费劲。装了 Skill，Codex 自动遵守这些规则。

一个容易搞混的区别：AGENTS.md 是全局规则，相当于公司制度，对所有任务生效；Skill 是特定场景指令，相当于岗位手册，只在匹配到的时候才加载。后面讲 Karpathy Guidelines 的时候会再提到这个区别。

怎么装，为什么选单品 Skill
----------------

安装就一条命令的事。

两种安装位置：全局安装放在 `~/.agents/skills/`，所有项目都能用；项目级安装放在项目根目录的 `.agents/skills/`，随仓库走，团队共享。

*# 全局安装 grill-me（所有项目都能用）*npx skills add mattpocock/skills --skill grill-me -y -g*# 项目级安装（只影响当前项目）*npx skills add mattpocock/skills --skill handoff -y*# 装完验证：看目录下有没有 SKILL.md*ls ~/.agents/skills/grill-me/SKILL.md

另外 Codex 内置了 `$skill-installer`，在 Codex 里直接输入这个命令，可以交互式选择安装官方仓库的 skill。不过它只收录了 openai/skills 仓库的 skill，社区 skill 还得用 `npx skills add` 安装。

装完怎么用？两种方式：输入 `$skill-name` 显式调用，或者你的任务描述匹配到 skill 的触发条件时自动加载。

Skill 1：grill-me — 写代码前先想清楚
---------------------------

Codex 最大的毛病是带着错误假设就动手。

你跟它说"加个微信登录"，它直接开始写代码，基本不会追问你：微信登录用 OAuth2 还是扫码？用户表有 openid 字段吗？老用户怎么绑定？

grill-me 就是来治这个毛病的。它在你写代码之前，逐个问题追问你的方案，直到你和 Codex 对需求的理解一致。核心指令很简单："Interview me relentlessly about every aspect of this plan until we reach a shared understanding(这个计划的方方面面对我穷追不舍地追问，直到我们达成共识)"

*# 要给项目加微信登录，先让 Codex 追问你方案*$grill-me*# Codex 会问：# 微信登录用 OAuth2 还是扫码？# 你的用户表有 openid 字段吗？# 老用户怎么绑定微信？# ……*

Reddit 上有用户说用了 grill-me 之后，"it completely changed how I plan with Codex(它彻底改变了我使用Codex进行规划的方式)"，感觉 90% 的情况能做出自己想要的结果。这只是个人体验。

grill-me 来自 Matt Pocock 的 skills 仓库，安装量超过 15 万。

![](.evernote-content/272C5B17-B52E-4E48-9AB4-18F994E3E1C2/E32DAD64-8BAA-4F0C-AF1C-2C23816A86EF.png)

什么时候用：接到新需求、做重构、修 bug 之前——任何需要先想的场景。

npx skills add mattpocock/skills --skill grill-me -y -g

Skill 2：planning-with-files — 崩溃了也能接着干
--------------------------------------

和 Codex 聊久了，会话会崩。上下文太长之后 Codex 变糊涂，改东忘西。/compact 能压缩上下文，但压缩完还是同一个对话，结构化的进度信息丢了。

planning-with-files 把你的计划和进度写到三个文件里：task\_plan.md（要做什么）、findings.md（发现了什么）、progress.md（做到哪了）。下次开新会话，Codex 读这三个文件就能接着干，不从头来。

# task\_plan.md 示例## 目标给项目加微信登录功能## 步骤1. ✅ 调研微信开放平台 OAuth2 接入流程2. 🔄 实现后端回调接口3. ⬜ 前端扫码组件4. ⬜ 用户绑定流程

它和 handoff（下一个要讲的 skill）的区别：handoff 是"拍快照走人"，快照拍完当前会话就结束；planning-with-files 是"边做边记"，整个工作过程中持续记录，每完成一步自动更新进度。

什么时候用：任何会持续很久的任务。你改了 10 个文件、会话快到极限的时候，会庆幸之前让 Codex 做了记录。

npx skills add OthmanAdi/planning-with-files -y -g

![](.evernote-content/272C5B17-B52E-4E48-9AB4-18F994E3E1C2/313C5435-14A8-4C91-BB27-07504401C4C3.png)

Skill 3：Karpathy Guidelines — 让 Codex 少干蠢事
------------------------------------------

Codex 最常见的三个毛病：

1假设错了不问就动手

250 行能搞定非写 500 行

3顺手"改进"不相关的代码

Karpathy Guidelines 把这些行为纠正编成四条硬规则：

先想再写：有多种理解的时候列出来让你选，不偷偷选一个就跑

简单优先：200 行能写完的别写 500 行，不加你没要求的功能

手术式改动：只碰必须改的文件，不顺便"优化"旁边的代码

目标驱动：定义成功标准，写测试验证，循环直到通过

这四条规则源自 Andrej Karpathy 今年 1 月分享的 AI 编码工作流观察。开发者 forrestchang 据此改写成 CLAUDE.md 格式，multica-ai 又做了跨平台 Skill 版本，GitHub 上超过 17 万 stars。

![](.evernote-content/272C5B17-B52E-4E48-9AB4-18F994E3E1C2/DCC1DE15-8489-44C5-8886-1B196093839A.png)

前面说过 AGENTS.md 和 Skill 的区别，这里正好体现：Karpathy Guidelines 是 Skill，只在 Codex 写代码的时候才加载，不会在你让它做别的任务时跑出来多嘴。如果把同样内容写进 AGENTS.md，那就是全局生效，所有任务都受约束。

什么时候感觉最明显：改一个小 bug，结果 Codex 重构了半个文件——装了这条 Skill 之后不这么干了。

npx skills add multica-ai/andrej-karpathy-skills -y -g

Skill 4：handoff — 会话接力棒
-----------------------

Codex 会话聊到后边，越来越慢，越来越糊涂。这时候你需要开个新对话，但前面的上下文怎么办？

handoff 把当前会话压缩成一份结构化的 markdown 文档，包含目的、上下文、建议的 skill、现有文件指针。你开个新对话，把这份文档丢给它，直接接着干。

和 /compact 的区别：compact 还是在同一个对话里压缩，对话还是那个越来越长的对话；handoff 是开新对话，把工作笔记带过去，从干净的状态重新开始。

Ben Holmes 分享过一个进阶用法：在 Claude Code 里用 grill-me 做完规划，然后 handoff 给 Codex 的多个 worktree 并行实现。新手先记住"会话太长就 handoff"就够了。

npx skills add mattpocock/skills --skill handoff -y -g

Skill 5：Firecrawl — 给 Codex 连上互联网
---------------------------------

Codex 自带联网搜索，但默认走缓存，拿到的可能是几天前的内容。如果你的问题需要最新信息——比如刚发布的 API 变更、竞品最新的定价——缓存里的旧数据帮不上忙。

Firecrawl 给 Codex 装上实时联网能力：search（搜索）、scrape（抓取页面）、crawl（爬整站）、map（站点地图）、interact（操控浏览器）。不是搜缓存，是搜实时网页。

安装需要 API key，免费额度每月 1000 次，够日常用。有一点要注意：Firecrawl 的服务在国外，需要稳定的网络环境。

npx -y firecrawl-cli@latest init --all --browser

装完之后你可以这样用：

"查一下 React 19 的 migration guide，列出 breaking changes"

"搜一下掘金上最近关于 Codex Skill 的热门文章"

"爬一下这个竞品的官网，提取定价信息"

更多好用的 Skill
-----------

上面 5 个是装完就受益的"刚需"，下面这些看你的工作流按需装：

| Skill | 一句话 | 安装命令 |
| --- | --- | --- |
| mcp-builder | 引导式搭建 MCP Server | `$skill-installer mcp-builder` |
| skill-creator | 交互式问答，帮你写自己的 Skill | Codex 内置，输入 `$skill-creator` |
| agent-skill-creator | 把你的工作流一键转为可复用 Skill，17 平台兼容 | `npx skills add FrancyJGLisboa/agent-skill-creator` |

中文用户可以关注的工具
-----------

ok-skills（mxyhi）：45 个精选 skill，有中文 README——`npx skills add mxyhi/ok-skills`

claude-code-skills-zh（laolaoshiren）：200+ skill 中文合集，按场景分类

planning-with-files-zh（explainx.ai 提供的中文版）：`npx skills add https://github.com/othmanadi/planning-with-files --skill planning-with-files-zh`

skills.sh：Vercel 做的跨平台可搜索 skill 目录，网址 skills.sh

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=8f35985eb8421148c3305ded4c6d86297e82792229305e95364e9923d6ec930109181c0d3469&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782340110_2&req_id=1782342212142578&scene=169&mid=2649114292&sn=a89401fdbfbb13dd5f470c220ee13eeb&idx=1&__biz=MzIwNjA1NjMyNQ==&sessionid=1782340109&subscene=200&clicktime=1782343854&enterid=1782343854&flutter_pos=14&biz_enter_id=5&jumppath=1104_1782343837607,WAWebViewController_1782343841067,WAWebViewController_1782343842451,1104_1782343843608&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQuPB6TGmz2rgaIbZUsbh7NxLTAQIE97dBBAEAAAAAAG3+CpT30KQAAAAOpnltbLcz9gKNyK89dVj0CFQsvYpRwMbEtTWv80xFSjQgwDRLAGL+b7XEAYH4eMlPW41heVsKEzU5DwlWL94/UhxyM/e5NqoIp/s92uNoJigDhfka9dIQxvfrlT9OjgXZJgh9Pd94nBc/18ot2RrltBFFHafE8ocuaZ6QL9hGEaylkeaB4z0pei/RKB0y2FaAFTfJL20zxAAfMqnRmdKTircUwq7WHTxDmry321ovwn+7biz337bdg047jdY=&pass_ticket=pkJQBQ7U+m+6kM137nW00l05QLYMrns5O+RmeWlzTrGlRuCHBa+M1wAcqQP4kmzS&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/76979f89-c4e8-4b2f-9bfa-73b58e1e6f1e/76979f89-c4e8-4b2f-9bfa-73b58e1e6f1e/)
