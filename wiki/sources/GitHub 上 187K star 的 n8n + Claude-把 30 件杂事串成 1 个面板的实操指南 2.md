---
title: GitHub 上 187K star 的 n8n + Claude：把 30 件杂事串成 1 个面板的实操指南 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/GitHub 上 187K star 的 n8n + Claude：把 30 件杂事串成 1 个面板的实操指南 2.md
tags: [evernote, impression, yinxiang]
---

# GitHub 上 187K star 的 n8n + Claude：把 30 件杂事串成 1 个面板的实操指南

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484893&idx=1&sn=2b5f20d2fe11343c60fd84c4ac64d691&chksm=f1af72b9ab92a8b95072108ea046bf2407d693dc5b36e47c9fcf0527fb6204e57af30afa3179&scene=90&xtrack=1&req_id=1779026707881369&sessionid=1779023840&subscene=93&clicktime=1779027071&enterid=1779027071&flutter_pos=20&biz_enter_id=4&ranksessionid=1779026707&jumppath=WAWebViewController_1779027038617,WAWebViewController_1779027039115,20020_1779027055463,1104_1779027063109&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0vuyfV5WR19GA+laJw6o9RLTAQIE97dBBAEAAAAAAKP2By+CsGgAAAAOpnltbLcz9gKNyK89dVj0Pl7vGFZlUd+Mziye3IbcAH6qyMNk9+xKM3VF3bH5iB7ETi5cakZuLSldb3lvXfNouhByzNCsN8PNbBaZ0NrduwS3BoSzVVPqdVD2sXJx1nIGaMSPKBm9pCbVZuLvKiY6qK05XwtaPSLXsaiDmYLf7W50kCfaryGsYdyEMut5qWQHhm67tsnoRTM1a5VsXGsY+8eePjYiKg3/69aAkx4cAGMsxPbD8YAH51d2C1U=&pass_ticket=BAlNRZ3FfmAf/oCDJW93Na1JWjrWl9wbnALhPhfoH/dPwuB1En70xpY8NTQkb44a&wx_header=3)

Original莲花明 AI落地手记

你打开早晨的电脑，要处理几件事？

我猜数一下不少。邮件50封，企微17条，飞书11条，git上3个项目要看PR，CI跑了8个任务，背后还有cron在拉邮件、推日报、巡服务器。

![](.evernote-content/0B435F25-23D8-4CB1-AF7A-8CBC7940E6AC/B24F4766-3E6A-452C-A1DA-FB979CFF7884.jpg)

如果你是项目经理，你的痛是这些活散在5个SaaS里，每天上班第一件事是**「先看一遍哪儿出事了」**。

如果你是开发，你的痛是10个cron加一堆shell脚本散落在crontab里，**有事报告，没事杳无音讯**，挂了你才知道。

最近两个月，我把这一堆活全塞进了一个面板。

底层是Claude当大脑负责想，n8n当手脚负责动。一对组合，把项目经理和开发两类人的日常拍扁成1张图。这篇文章把整个搭法说清楚。

---

一、为什么是Claude + n8n这对组合
----------------------

先说为什么是这俩。

Claude是大脑这部分不用我多解释。你给它一段话，它能理解你想干嘛，能拆解步骤，能写prompt，能调工具。它擅长「想清楚」。

n8n是大部分人没听过的开源工具。一句话讲：它是一个把各种SaaS、API、模型节点拖来连接的可视化面板。每个节点干一件事，节点之间连线就是数据流。一条工作流跑起来，每一步成功失败一目了然。

它擅长「动手」—— 触发、扇出、调度、可视化、出错重跑、失败告警。

单看数据。**n8n在GitHub已经187.8K star，活跃用户超过23万，Docker镜像被拉了1亿次。**这是个有人在用的真东西。

为什么两个拼一起？2026年发生了两件事，把这对组合从能用变成好用。

**第一件**，n8n官方做了Anthropic节点，Claude三个模型（Haiku 4.5 / Sonnet 4 / Opus 4）直接拖进工作流就能调。

**第二件**，开源社区做了n8n-mcp。这个东西更狠 —— 你打开Claude Code说一句「帮我写一个n8n工作流干XX事」，Claude Code直接把工作流文件生成出来导进n8n里就能跑。

Claude大脑 + n8n手脚 + MCP当神经 —— 三件套齐了。

---

二、不是我一个人在这么用
------------

### 大厂样本

外卖平台Delivery Hero（70个国家，5.3万员工），每月800个账号锁定请求要处理，原来35分钟一个全靠人手解，上n8n之后**每月省200+ 小时**。

欧洲最大招聘平台StepStone，做一个新集成从2周写代码降到2小时拖节点，**25倍提速**。

全球最大歌词平台Musixmatch，4个月省下**47天工程人力**。

### 个人玩家

Medium博主Hazel，花一个周末搭完工作流，**从此每周省20小时**。

还有个叫Mubashar Ali的，**3.17美金一个月**搭了一个n8n + Claude的销售线索机器人，每周稳定预约8到12个会议。

更夸张的是Derek Salyers，搭了**9个AI子代理**组成矩阵，整个内容业务的选题、写稿、外联、上架全自动跑，他只给方向。

### 社区生态

n8n模板库已经有**6658个AI工作流模板**，GitHub上还有个awesome-n8n-templates仓库收了280+ 免费可抄的方案。仓库地址：**github.com/enescingoz/awesome-n8n-templates**。

![](.evernote-content/0B435F25-23D8-4CB1-AF7A-8CBC7940E6AC/4C7A9894-14A5-46D3-83BF-11EC5D417B92.png)

这条路不是我一个人在走，已经被验证过了。

---

三、30件杂事，分这6大块
-------------

我把自己实际跑的工作流分成6大类 —— 你可以对着看你自己每天在干啥。

| 类别 | ① | ② | ③ | ④ | ⑤ |
| --- | --- | --- | --- | --- | --- |
| 采集 | 个人邮箱日报 | 订阅RSS | Hacker News摘要 | GitHub trending | AI圈新闻 |
| 资讯加工 | arXiv论文摘要 | 工具更新追踪 | 行业新闻精筛 | 趋势预测 | 热点合并去重 |
| 个人知识 | 笔记RAG | TODO同步 | handoff持久化 | 决策日志 | 经验沉淀 |
| 自动化执行 | 服务巡检 | 服务自愈 | SSL续费提醒 | 域名监控 | 资源回收 |
| 多AI协作 | AI调度路由 | 失败升级 | 结果回流 | 成本统计 | 效果对比 |
| 触达通知 | 企微聚合 | 邮件预览 | Telegram | Slack | 短信告警 |

表：6大类 × 5件杂事 = 30个工作流

每类挑1件展开一句：

· **采集**：早9点 / 晚6点自动拉个人订阅邮箱，50封里那5封重要的挑出来

· **资讯加工**：每天扫一遍arXiv新论文 + Hacker News + GitHub trending，按主题摘要

· **个人知识**：所有项目目录里的handoff、todo、决策日志自动归并成一个看板

· **自动化执行**：5分钟扫一次个人服务器 / VPS / VPN，挂了自动重启

· **多AI协作**：4个AI助手按任务类型自动派活

· **触达通知**：所有重要事件归并成一条企微消息，不刷屏

下面挑3个最高频的展开讲。

---

四、三个高频场景
--------

### 场景A · 个人邮箱智能分诊

我个人订阅了一堆newsletter —— OpenAI更新、Anthropic博客、HN Newsletter、几个开源项目的release。一天50封，认真看1小时，不看又怕错过。

n8n搭法：

**Schedule**（早9点触发）→ **IMAP**（拉过去24小时邮件）→ **Claude Haiku 4.5**（每封打标签：重要 / 订阅 / 广告 / 个人）→ **Switch**（按标签分流）→ **Claude Sonnet 4**（只对「重要」类做摘要）→ **企微Webhook**（推3-5条要点）。

整个工作流跑一次30秒，每月API成本不到5块钱 —— 因为90% 用Haiku，只有少数走Sonnet。

这个**双模型策略**是个关键技巧：便宜模型分类，贵模型推理。Anthropic自己也是这么建议的。

参考案例：Hazel那篇Medium用的就是同样的方案，她这套加另外两个自动化每周省20小时。

### 场景B · 自部署服务巡检自愈

我有几个个人服务器 —— 一台demo（跑测试）、一个VPS（放公众号脚本和cron）、一个VPN、几个域名 + SSL证书。

以前的痛是：东西多了散了，挂了不知道，等到要用才发现「咦怎么502」。

n8n搭法：

⏰

每5分钟

Schedule

▸

🌐

curl健康端点

HTTP Request

▸

❓

200 / 非200

IF判断

▸

📜

拉systemd日志

SSH节点

▸

🧠

Claude判定原因

AI节点

▸

🔀

重启 / 告警 / 不动

Switch分流

▸

📣

推企微通知

Webhook

图：服务巡检自愈工作流的7个节点

这套跑了快两个月。最自豪的一次是凌晨3点VPN进程挂了，n8n自己重启了，我第二天早上才在企微看到通知，没影响白天工作。

参考案例：Musixmatch 4个月省47天工程时间的方案里，类似的巡检 + 资源回收 + 告警合并占了相当大一块。

### 场景C · 多AI调度中枢

这是最近半年我玩出感觉的一块。

我同时在用Claude（复杂任务、上下文长）、Kimi（中文长文阅读）、Doubao（便宜批量翻译）、Gemini（多模态和配图）。

以前是手动派活 —— 切窗口、复制粘贴、收结果，切来切去切晕。

后来我把n8n改成调度中枢：

**Webhook入口**（接所有任务请求）→ **Doubao Lite节点**（轻量分类：执行 / 查询 / 创意 / 长文）→ **Switch**（按类型路由）→ 对应AI干活 → 失败自动升级到更强模型重跑 → 结果回流到Notion / 飞书 / 企微。

成本结构挺有意思 —— 80% 请求被路由到便宜模型，20% 复杂请求才走Claude。整体token账单比以前全用Claude **砍了70% 左右**。

参考案例：Mubashar Ali那个3.17美金一个月的销售线索机器人就是这套路的轻量版，主路由走便宜模型，关键决策才上Claude。

---

五、踩过的4个坑
--------

### 坑1：n8n默认5分钟超时

Claude Opus跑长任务很容易超过5分钟，工作流被n8n自己掐断。解法是改Workflow Settings里的Execution Timeout，调到15-30分钟。不知道你能debug半天。

### 坑2：双模型路由要前置Switch，别塞AI Agent内部

很多人想「让AI Agent自己决定调哪个模型」。听着聪明，实际debug困难 —— AI Agent节点是个黑箱，路由错了你不知道是判断错还是执行错。前置Switch明确写「重要走Sonnet，普通走Haiku」，可解释、可改、可重跑。

### 坑3：n8n-mcp比拖节点快3倍

这不是坑是隐藏招。装上n8n-mcp之后你不用拖节点了 —— 直接在Claude Code里说「帮我写个n8n workflow干XX事」，Claude Code直接吐出工作流JSON导进n8n就能跑。我对比过，**原来拖30分钟的活，8分钟搞定**。

仓库地址：**github.com/czlonkowski/n8n-mcp**。

![](.evernote-content/0B435F25-23D8-4CB1-AF7A-8CBC7940E6AC/765FEFF4-233F-48A3-B23E-13A066F5A993.png)

### 坑4：Webhook鉴权别Basic Auth

n8n默认给Webhook触发器配Basic Auth。生产环境不够安全 —— URL加token一旦泄露谁都能触发。换HMAC签名（Code节点手写验签），或者放Cloudflare Worker后面套一层。

---

六、所以你该不该上
---------

| 你的画像 | 上n8n + Claude？ |
| --- | --- |
| 项目经理 · 杂事5件以内 | 不必 |
| 项目经理 · 5-20件 + 想可视化 | 强烈建议 |
| 开发 · 5个cron以上 | 必上 |
| 已用Make或Zapier | 自部署免费可换 |

表：你该不该上的速查

---

七、写在最后
------

我以前觉得「一个人 + AI干一个团队的活」是销售话术。这一年用下来，我觉得它正在变成一种新的工作方式。

**项目经理这一类** —— 你的痛从来不是不会做事，是事太多太碎。30件杂事散在5个工具里，脑力被「调度」消耗掉了。

**开发这一类** —— 你的痛是写脚本写到最后，发现80% 在做运维和监控，真正在创造的部分越来越少。

n8n + Claude解决的就是这个问题。

它不是让AI替你干活 —— 它是把你脑子里那个隐形的「调度员」搬到了外面。Claude替你想该干啥，n8n替你动手干，**所有动作有日志、有重跑、有告警**。

你的脑力被释放出来，去做那些真正只有人能做的事。

这是2026年项目经理和开发都该装上的一对工具。

关注「AI落地手记」，不见不散。

一个人 + AI管20个项目的真实记录

原创扒一个工具，挺费功夫的。

觉得有用，点一下下面那个红色的「喜欢作者」就够了；不方便的话，转发给一个用得上的人 —— 对我一样是支持。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484893&idx=1&sn=2b5f20d2fe11343c60fd84c4ac64d691&chksm=f1af72b9ab92a8b95072108ea046bf2407d693dc5b36e47c9fcf0527fb6204e57af30afa3179&scene=90&xtrack=1&req_id=1779026707881369&sessionid=1779023840&subscene=93&clicktime=1779027071&enterid=1779027071&flutter_pos=20&biz_enter_id=4&ranksessionid=1779026707&jumppath=WAWebViewController_1779027038617,WAWebViewController_1779027039115,20020_1779027055463,1104_1779027063109&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0vuyfV5WR19GA+laJw6o9RLTAQIE97dBBAEAAAAAAKP2By+CsGgAAAAOpnltbLcz9gKNyK89dVj0Pl7vGFZlUd+Mziye3IbcAH6qyMNk9+xKM3VF3bH5iB7ETi5cakZuLSldb3lvXfNouhByzNCsN8PNbBaZ0NrduwS3BoSzVVPqdVD2sXJx1nIGaMSPKBm9pCbVZuLvKiY6qK05XwtaPSLXsaiDmYLf7W50kCfaryGsYdyEMut5qWQHhm67tsnoRTM1a5VsXGsY+8eePjYiKg3/69aAkx4cAGMsxPbD8YAH51d2C1U=&pass_ticket=BAlNRZ3FfmAf/oCDJW93Na1JWjrWl9wbnALhPhfoH/dPwuB1En70xpY8NTQkb44a&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d3640e4e-c218-4748-baa6-8b8977078d94/d3640e4e-c218-4748-baa6-8b8977078d94/)
