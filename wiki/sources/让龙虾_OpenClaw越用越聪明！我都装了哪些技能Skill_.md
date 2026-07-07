---
title: 让龙虾_OpenClaw越用越聪明！我都装了哪些技能Skill_
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/让龙虾_OpenClaw越用越聪明！我都装了哪些技能Skill_.md
tags: [evernote, impression, yinxiang]
---

# 让龙虾/OpenClaw越用越聪明！我都装了哪些技能Skill?

---

来源：[打开原文](https://mp.weixin.qq.com/s/GAZUgM0ntmNenEYUC29uBg)

先声明一下，这里的龙虾可以是大龙虾也可以是小龙虾，既可以是 OpenClaw 也可以是 NanoClaw，因为技能 Skill对于所有的龙虾都是通用的，仅仅只是一个文档目录而已。

我目前使用的是NanoClaw。卸载 OpenClaw！拥抱NanoClaw，你如果使用的是OpenClaw，也不影响下面技能的使用。

我们知道龙虾/OpenClaw能够跑起来主要基于两点：

1. 模型：模型当然是越贵越好了，好的模型龙虾能力自然也就越强。

2. 技能：最终决定每个人的龙虾能力大小或使用边界的还是技能Skill。

我们可以把Skill技能看作是手机上一个一个的APP，我们要实现某项功能，就可以在OpenClaw上去下载这些APP，进而增强原来龙虾没有的能力。

下面就是整理我当前使用整理出来的基础和扩展Skill。

搜索
--

搜索几乎成为龙虾的第一个要安装的技能，这样它就才能自由地获取外部的知识库信息。

没有搜索的话，龙虾就是又聋又瞎。

OpenClaw默认选项提供调用 Brave Search API 进行网页搜索和内容提取，Brave Search轻量无需浏览器，不过需申请 BRAVE\_API\_KEY，价格不低，每千次搜索需要5美金。

![](.evernote-content/DEA89EB1-0C08-4F36-8F27-21DE0EC24BA2/12A091C7-4007-450E-BC30-158A723F1A24.png)

所以我目前使用的是我自己写的一个免费的全网搜索工具：GLM Coding Plan 太抠了！重写了一个联网搜索Skill

搜索基本不限量 ，搜索效果也不错，而且支持模型友好的多结构化信息。

agent-browser
-------------

基于Rust 的无头浏览器 CLI工具，支持页面导航、点击、填表、截图，用于网页自动化交互。

除了常规的网页自动化交互，agent-browser 最大的作用是直接复用已登录的 Chrome 浏览器。

尤其是那种反爬很严格，还有复杂验证的网站，我们可以提前可以先在本地 Chrome 手动登录，导出 cookies，再导入到自动化流程中。

后续复用以避免重复登录，我要绕过它的限制，比如我就登录推特，然后来获取一些官方的推文信息：

![](.evernote-content/DEA89EB1-0C08-4F36-8F27-21DE0EC24BA2/FF87C94A-412B-40E6-8B88-6FAC4B14947D.jpg)

适合抖音或者小红书、推特这些需要登录才能操作的场景。

capability-evolver
------------------

AI 自我进化引擎。

允许 Agent 自主审查自身的会话日志并随时间改进行为，是 ClawHub 下载量最高的 Skill，遥遥领先第二名。

![](.evernote-content/DEA89EB1-0C08-4F36-8F27-21DE0EC24BA2/B7B50897-E4B8-4D6D-81DD-8A3DE73286FE.png)

安装：

clawhub install capability-evolver

安装后capability-evolver 会分析运行时历史，识别可优化的模式，在协议约束内自动应用进化策略，让 Agent 越用越聪明，无需人工干预。

byterover
---------

ByteRover可以看作是龙虾的第二大脑。

使用上下文树管理项目知识，提供知识检索和知识存储，当用户请求信息查找、模式发现或知识持久化时触发。

ByteRover 本质上是给 OpenClaw Agent 装了一个工程项目维基，不是聊天历史，而是结构化的、可版本控制的、跨会话持久的项目知识库。

适合长期运行的开发项目，越用积累的上下文越多，Agent 越来越"懂"你的项目。

clawhub install byterover

gog
---

深度打通Google生态。

如果你也在用 Google 全家桶，gog 是覆盖最完整的选择。

Google Workspace 完整 CLI 集成，覆盖 Gmail、日历、Drive、联系人、Sheets 和 Docs， 龙虾一键直达。

安装

clawhub install gog

summarize
---------

输入 URL、播客或 YouTube 视频即可提取关键内容。

适用于内容调研、快速浏览长文章，以及在决定是否完整观看前先了解视频要点。

![](.evernote-content/DEA89EB1-0C08-4F36-8F27-21DE0EC24BA2/8BAF28F5-073E-440A-8B2B-0716662379EF.png)

支持 PDF、网页、音频等多种格式，使用对应模型的 API Key，具体可以看它的安装说明文档。

之后我们可以输入网址链接，让它来总结B站以及YouTube上的视频。

github
------

通过 gh CLI 与 GitHub 交互。

管理 Issue、Pull Request、Workflow Run 和高级 API 查询，支持 gh issue、gh pr、gh run、gh api 等完整命令集。

我使用这个Skill最多的场景就是给它一个GitHub源码地址，然后让龙虾自己读取项目的说明，进行全自动化的安装和部署。

clawhub install github

weather
-------

OpenClaw 自带的官方 Skill。

免费，无需 API Key，直接从 wttr.in 拉取天气数据。

简单实用，集成进早晨定时简报 cron 任务中，每天9点自动播报天气。

![](.evernote-content/DEA89EB1-0C08-4F36-8F27-21DE0EC24BA2/D1189190-DE15-4D6B-B11B-73056E2765CC.jpg)

clawhub install weather

free-ride
---------

管理 OpenRouter 上的免费 AI 模型。

自动按质量对模型排名，配置降级 fallback 以应对限速，并更新 openclaw.json。

羊毛党的必备，使用这个技能可以免费获取Openrouter提供的免费模型，并且集成了模型切换、速率限制的功能。

Openclawskills 一键配置最优免费模型。

clawhub install free-ride

find-skills
-----------

万事不绝，可以用 find-skills，它是skilll的skill，元skill。

如果你不想抓破脑袋到处搜索Skills的话，直接使用这个Skill的Skills来找到相对应的Skills就可以。

比如询问"如何做某件事"或"找一个能做 X 的 Skill"时自动触发，它会自动发现和安装合适的 ClawHub Skill。

clawhub install find-skills

obsidian
--------

通过 obsidian-cli 管理 Obsidian Vault

支持搜索笔记名称/内容、创建新笔记、移动或重命名等操作。

Obsidian Skill 直接操作的是本地文件，所以可能之后的话，Obsidian的客户端你都不需要打开了。

集成进龙虾之后，你可以实时地修改、检索、管理Obsidian里面所有的笔记内容，甚至可以直接把它附加到龙虾的上下文当中使用。

clawhub install obsidian

nano-banana-pro
---------------

这个技能其实可以当成是音视频生成的一个通用技能代表。

nano-banana-pro是我目前做文章配图常用的一个Skill，调用 Google Gemini 3 Pro Image生成或编辑图像。

以上这些都是我当前应用的比较多的几个Skills，但也只是冰山一角而已，更多的还是自己定制的Skill，为此我还专门写了一个编辑器来管理它Typora 收费？来，写一个！

OpenClaw这些龙虾Agent其实并不是万能的，就像你买了苹果手机，还需要去安装和购买各类专业型的软件来处理实际的业务。

龙虾本质上只是龙虾壳而已，真正用好龙虾，不在龙虾，更多的在于如何去打磨和优化自己的业务工作流技能。

如果你也有自己想分享的Skill，可以在下方留言！

[📎 在印象笔记中打开](evernote:///view/207087/s1/e5ebe785-3876-4be6-b1fd-8384942c5dc0/e5ebe785-3876-4be6-b1fd-8384942c5dc0/)
