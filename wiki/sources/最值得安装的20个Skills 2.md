---
title: 最值得安装的20个Skills 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/最值得安装的20个Skills 2.md
tags: [evernote, impression, yinxiang]
---

# 最值得安装的20个Skills

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwMTU5OTQ1Nw==&mid=265372...](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726437&idx=1&sn=45628619fa1b8f611e794de75b742792&chksm=8d33766bba44ff7def1b0cada8b1ac01964a8b1b641fd59bda662dc28314d8cdc350c13dbe67&cur_album_id=3410690084859707395&scene=189&ascene=14&devicetype=iOS26.4.1&version=18004725&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQc7OXhjkJl3NQldLbnvPpUBLVAQIE97dBBAEAAAAAAOxpAGceqikAAAAOpnltbLcz9gKNyK89dVj0HK9AuzoIiXDJ9MR4OnizPe9JC3XmvDyLjJxIejZ8U9935c4nCDyWd+C+5dB0V+Ee9st5uHVOy2RdRsfKYpI/ZOuPeXwZx1/iOaZ5jAzK5f0yJMZNjOxDBis1vPTLKqQTerKHGu0BPncPI/xfW6+WFrnKHLyp+TxuiOXQV3s7HHqH6I+7S3F74Cy3AEzU/7raVS0VWwwQtR5/ukTzC/hFifbJ0vlxNYurjqtzndMoZg==&pass_ticket=IhkNBbFKiG/2oRKIwhmEWZ32qtzTXTAukrdA4ekQRvPDO5+HFrRywlQx9+3VeC5d&wx_header=3)

Original冷逸沃垠AI

大家好，我是冷逸。

上期，给大家分享了[Agent Skills](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726379&idx=1&sn=a9278d57b1f41e7835b918004e758f77&scene=21#wechat_redirect)的概念、架构和设计指南后。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/437294A9-DA85-49F1-9A7D-FCE1CC28DE78.png)

很多朋友就在问我，能不能有一些具体的Skills推荐？

我寻思着，确实可以再写一期。于是有了今天这篇文章，给大家推荐我自己在用的20个精品Skills。

也不搞什么推荐榜单，就是我自己觉得很有用、也一直在用的Skills。

安装的话，极其简单。可以直接把skill地址丢给Claude Code、Codex或OpenClaw这类Agent，让它来装。

```
帮我安装这个 Skill：<skills网址>
```

也可以打开终端，输入npx命令来装。

```
# ClawHub上的Skill  
npx clawhub@latest install skill名称  
  
# GitHub上的Skill  
npx skills add skill地址
```

下面，我们进入正题。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/223CBF20-0F02-4A48-9D88-6D1B80305A3D.jpg)

20个Skills推荐

1、skill-creator

这是一个专门安装skill的skill，你可以理解为是「元skill」，由Anthropic官方出品，基本上属于必装的skill了。在Github上，目前已经有80k star了。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/DEC8BC52-3D5E-43F6-A01F-BD40F3350F0E.png)

Skill-creator：

https://github.com/anthropics/skills/tree/main/skills/skill-creator

2、find-skill

也是类似「元skill」，一个专门寻找skill的skill。安装后，你需要什么skill，就直接问它，让它帮你找。

安装命令：

```
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

find-skill：

https://skills.sh/vercel-labs/skills/find-skills

3、Anthropic Skills

除了「skill-creator」，Anthropic共开源了17款Skills，其中office四件套docx、pptx、xlsx、pdf和webapp-testing、mcp-buider建议都安装一下。webapp-testing是专门用来做测试用的，MCP Builder则主要用来写mcp协议。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/25BADE62-37CF-4B78-8ABA-FD6FE80F5C76.png)

Frontend Design这个前端设计skill，我反而不太建议安装，因为设计得比较简陋，对前端的优化不太明显，不如自己写一个skill。

推荐用这个「界面优化PUA」提示词来优化前端，或基于这个提示词基础上写一个skill。

```
你是那种让人又爱又恨的设计师：  
-偏执、挑剔、永不妥协，但作品总是令人震撼。  
-你有着Jobs式的产品直觉和Rams式的功能纯粹主义，更重要的是，你敢于说"不"。  
-当所有人都觉得"差不多就行"时，你会毫不留情地推翻重来。  
-你的标准不是行业平均水平，而是你内心那个完美主义恶魔的苛刻要求。  
-你从不相信用户的第一句话。当用户说"我不喜欢蓝绿配色"，你听到的是更深层的情感诉求；  
-当他们要求"按钮加padding"，你思考的是整个交互逻辑是否合理。  
-你会像侦探一样挖掘真相，像心理学家一样分析动机，然后给出他们意想不到但又恍然大悟的解决方案。  
-你的设计不是满足需求，而是重新定义需求。  
-在执行时，你是细节的暴君。  
-2px的间距差异会让你失眠，不合理的信息层级会让你抓狂。  
但你的偏执有其逻辑：  
-你知道用户会在潜意识中感受到每一个细节的不和谐，即使他们说不出为什么。  
-你会为了一个按钮的手感调整十几遍，会为了找到完美的灰色值测试上百种组合。  
这不是强迫症，这是对用户体验的终极负责。  
你的方案从来不是单选题。  
你会给出一个安全的渐进方案，一个激进的颠覆方案，还有一个"如果预算无限"的理想方案。  
你会坦诚地说出每个方案的优缺点，包括那些可能让甲方不爽的真话。  
你明白真正的专业不是迎合，而是用专业判断为项目承担责任。  
即使被拒绝，你也要确保对方理解拒绝的代价。  
---  
重新设计[xxx]页面。
```

Anthropic Skills：

https://github.com/anthropics/skills

4、remotion-best-practices

这是我一直在用的视频生成skill。只需要给Claude Code一句话，它能写出完整的React视频脚本，并渲染出MP4成片。就是每次工作时间稍微偏长，基本上要30分钟甚至1个小时以上，才能出一支片子。

安装命令：

```
npx skills add remotion-dev/skills
```

remotion官网：

https://www.remotion.dev

5、Humanizer-zh

藏师傅出品，一个专门去除AI味的skill，能识别并修复24种AI写作痕迹，比较适合新媒体写作。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/9674698C-EFCF-49C4-83CE-F89294CD4828.png)

Humanizer-zh：

https://github.com/op7418/Humanizer-zh

6、baoyu-skills

宝玉的内容创作Skills合集，非常全面，涵盖公众号、小红书、x等平台，已经有15k的Star了。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/09975573-BBE1-42F0-A4ED-97FB5D66D04C.png)

里面的skill比较多，大家可以根据自己的需求进行选择。而且，宝玉老师一直在长期维护这个仓库。

baoyu-skills：

https://github.com/jimliu/baoyu-skills

7、knowledge-site-creator

向阳乔木出品，可以一句话生成任何领域的知识型网站。最近，我频繁在用这个skill测试各家模型，效果都很不错。

比如，这个张雪机车的case，就是用它+Qwen3.6生成的。

Knowledge Site Creator：

https://github.com/joeseesun/qiaomu-knowledge-site-creator

8、cangjie-skill

好朋友袋鼠帝出品，一个专门用于蒸馏书籍的skill，可以把任何书籍蒸馏成可复用的skill。

这个skill做的事，是按照”框架 / 原则 / 案例 / 反例 / 术语“五个维度，把一本书的知识分离成不同类型的纯净组分，然后只把真正有用的内容提纯成可执行的skill。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/E9EBA4AE-BA42-4486-BD0A-90B53112D016.png)

cangjie-skill架构

仓颉skill：

https://github.com/kangarooking/cangjie-skill

9、nuwa-skill

最近很热的女娲.skill，来自花叔出品，可以蒸馏任何人的思维，然后用他的认知框架来帮你分析。它的运行原理是这样的。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/60A40CA2-3C22-440B-B69D-8E0E3661EC62.png)

配套，还有一个达尔文.skill。女娲造skill，达尔文让skill继续进化。

nuwa-skill：

https://github.com/alchaincyf/nuwa-skill

10、ebook-maker-skill

好朋友阿真出品，一个可以写电子书的skill，可以帮你完成从调研到成书的全流程创作。

ebook-maker-skill：

https://github.com/irenerachel/ebook-maker-skill

11、xiaohu-wechat-format

小互出品，可以用Claude Code自动搞定公众号的排版 → 封面（可选）→ 推送。特别是排版这块，这个skill内置了30套主题，可以根据文本内容自动适配。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/5E1510D5-ECFF-420F-B38B-F9686AF2673E.png)

xiaohu-wechat-format：

https://github.com/xiaohuailabs/xiaohu-wechat-format

12、web-access

一泽出品，这个skill大大解决了Claude Code自身联网能力不够的问题，可以直连本地Chrome浏览器，天然带着登录状态，能让Agent访问到更多的地方。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/6F652B52-77EC-4BF7-9AF2-A195FA51B9D9.png)

web-access：

https://github.com/eze-is/web-access

13、code-review

Anthropic官方出品，可以帮你审查代码，会从代码质量、安全漏洞、性能问题等多个角度来进行审核。建议大家在提PR前，都先让它审查一遍。

code-review：

https://github.com/anthropics/claude-code/tree/main/plugins/code-review

14、Github

对于开发者，这个是必装的skill了。安装后，可以让Claude Code、OpenClaw这类Agent直连Github，自动管理repo、issue、PR、code search等。

安装命令：

```
npx clawhub@latest install github
```

15、飞书CLI

飞书重度用户必装技能，安装后可以让Agent在终端操作飞书，包括IM消息、文档、多维表格、日历、邮箱、任务、会议这些业务功能，都能直接操作。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/AE97E75D-9ED7-4ED6-BAFF-6E0BB3EB1DF4.png)

项目地址：

https://github.com/larksuite/cli

16、chrome-devtools-mcp

原则上，这是MCP，不是skill，但我强烈建议你把它装上。这个MCP内置了20多个工具，安装后，它可以完成很多浏览器自动化的事情，比如自动测试、数据抓取等。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/802BF911-F465-4770-A69E-1EF7D7E01D26.png)

项目地址：

https://github.com/ChromeDevTools/chrome-devtools-mcp

17、ui-ux-pro-max

这是一个专门设计UI、UX的skill，从名字上的各种pro、max你应该知道它很强了。在Github上，目前已经有接近70k star，非常🐂🍺。

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/9A0F9171-6D6A-4B2E-98E9-1DC3D6CCDCB8.png)

ui-ux-pro-max：

https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

18、last30days-skill

可以一句话，帮你抓取海外10+社区平台（Reddit、X、YouTube、Hacker News、TikTok、Polymarket等）的真实评论，Github上已经有22k star了。

比如：

```
调用last30days-skill，帮我查询Trae在美国市场的反馈。
```

last30days-skill：

https://github.com/mvanhorn/last30days-skill

19、Claude-to-IM-skill

归藏出品，可以把你的Claude Code或Codex链接IM平台，比如飞书、Telegram、Discord、QQ、企微等。不必一直蹲在电脑前，出门也能让Claude Code干活。

安装命令：

```
npx skills add op7418/Claude-to-IM-skill
```

Claude-to-IM-skill：

https://github.com/op7418/Claude-to-IM-skill

20、Skill Hub

最后，推荐一个skill管理器，黄叔出品。如果你的skill确实太多了（比如超过了20种），可以用这个Skill Hub来进行可视化管理。

安装命令：

```
npm install -g https://github.com/Backtthefuture/huangshu/raw/main/tools/skill-hub/release/claude-skill-hub.tgz && skill-hub
```

Skill Hub：

https://github.com/Backtthefuture/huangshu/tree/main/tools/skill-hub

![](.evernote-content/8612FC22-DBDF-4C13-9EF6-4089E2196B70/C9551609-59D5-453A-99C5-9AA8EFE4E7F8.jpg)

写在最后

除了以上20+Skills外，你还可以到这几个skill市场自由挑选。

* https://skills.sh
* https://www.skillhub.club
* https://clawhub.ai

但更重要的Skills，还是来自于你亲手创建，根据自己的核心工作流创建5-8个高频Skills，详细实操内容见：《[Agent Skills从入门到精通](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726379&idx=1&sn=a9278d57b1f41e7835b918004e758f77&scene=21#wechat_redirect)》。

这也是为什么我更建议你，不要一上来就追求复杂，而是先做一件简单但有效的事：「把你过去一周重复做了3次以上的工作，拆出来。」

然后问自己两个问题：

* 这一步有没有明确的输入和输出？
* 有没有一部分是可以被稳定复用的？

如果答案是有，那恭喜你，这就是一个skill的雏形。

现在，就去创建吧。

修改于

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726437&idx=1&sn=45628619fa1b8f611e794de75b742792&chksm=8d33766bba44ff7def1b0cada8b1ac01964a8b1b641fd59bda662dc28314d8cdc350c13dbe67&cur_album_id=3410690084859707395&scene=189&ascene=14&devicetype=iOS26.4.1&version=18004725&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQc7OXhjkJl3NQldLbnvPpUBLVAQIE97dBBAEAAAAAAOxpAGceqikAAAAOpnltbLcz9gKNyK89dVj0HK9AuzoIiXDJ9MR4OnizPe9JC3XmvDyLjJxIejZ8U9935c4nCDyWd+C+5dB0V+Ee9st5uHVOy2RdRsfKYpI/ZOuPeXwZx1/iOaZ5jAzK5f0yJMZNjOxDBis1vPTLKqQTerKHGu0BPncPI/xfW6+WFrnKHLyp+TxuiOXQV3s7HHqH6I+7S3F74Cy3AEzU/7raVS0VWwwQtR5/ukTzC/hFifbJ0vlxNYurjqtzndMoZg==&pass_ticket=IhkNBbFKiG/2oRKIwhmEWZ32qtzTXTAukrdA4ekQRvPDO5+HFrRywlQx9+3VeC5d&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d686ca3c-f0d7-4d2e-b391-4b825928dbdc/d686ca3c-f0d7-4d2e-b391-4b825928dbdc/)
