---
title: 刚刚，飞书 CLI 开源了，我用 Claude Code 玩转几大企业级场景，绝了！
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/刚刚，飞书 CLI 开源了，我用 Claude Code 玩转几大企业级场景，绝了！.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "刚刚，飞书 CLI 开源了，我用 Claude Code 玩转几大企业级场景，绝了！"
source: evernote
type: note
export_date: 2026-06-27
guid: 1b58a7f3-9541-428f-b542-6625c458b9c4
---

# 刚刚，飞书 CLI 开源了，我用 Claude Code 玩转几大企业级场景，绝了！

原文链接: [https://mp.weixin.qq.com/s?chksm=c14d940ff63a1d1985f9d3b6d9f0dcb...](https://mp.weixin.qq.com/s?chksm=c14d940ff63a1d1985f9d3b6d9f0dcbe3fa2e414f130fd1e31090afd00d9f2fcf68c9c7f0561&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1776482104_1&req_id=1776477378630175&scene=169&mid=2247491446&sn=708496f70f54dc8dde451845fcd9fe34&idx=1&__biz=MzkxNjY0MzM1MA==&sessionid=1776482569&subscene=200&clicktime=1776484052&enterid=1776484052&flutter_pos=24&biz_enter_id=5&jumppath=WAWebViewController_1776483809203,20020_1776483822349,BrandSubHistoryFlutterViewController_1776483824143,1104_1776483950390&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004724&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ+o8SVBlu46ZufCVpmA41EhLVAQIE97dBBAEAAAAAANniJThsPDsAAAAOpnltbLcz9gKNyK89dVj0DezA5nf4h9A5pibSsdGiAH8K6qoYKeGotfbkisX135tBjQqn5hnaUREp14HtVhG10HZCW0y1TO4yyhHonuB5opxrZbBgmCvjo4i7kHLYBx+zvc16Pyt710trSf1Ut1JNGJ09URwUo6WETsmr12INl3fvuCGULRjTDulgq7s/FIsO/BaBcYQPJqhaIFbX3Uc5PD0vUmQMbG5JDRwVxyuue2fBhyQ1u+XGeagaH0Uxaw==&pass_ticket=//zznkkkaGCwFAQE5YP3PAJT20Ki/iGJeF2EDYYnBFjPIaWSnnEkQNT6EULm4ikr&wx_header=3)

Original甲木Zuiyn 甲木未来派

"

从今天开始，你的每一个AI Agent，都能直接操作你的飞书了。

—— 飞书 CLI，正式开源

大家好啊，我是甲木。

今天，**飞书 CLI，正式开源了。**

![](attachments/8220859b56ae5af9.jpg)

— 飞书 CLI GitHub 页面

一句话说清楚意味着什么：**从今天开始，你的每一个 AI Agent，都能直接操作你的飞书了。**

肯定很多朋友已经在用 Claude Code、CodeX 或者其他的 Agent 去做各种各样的事了，写代码，做分析，搞内容，AI 越来越聪明。

但是如果我们本身在用飞书，直接让 AI 检查我们日历有没有冲突的会议，方案发到群里，直接新建个多维表格、文档等等，它都做不到..

「AI 再聪明，看不到你的数据，就只能跟你干聊。」

之前我在写各家 OpenClaw 文章的时候，我们只能通过小龙虾来接入飞书插件，现在，飞书直接把 CLI 开源了，这意味着 Claude Code、Codex、Trae，或者任何一个能跑命令行的 Agent，都可以原生接入飞书。

无需登记，无需审核，GitHub 直接下载。

3 月 19 日飞书春季发布会说十天内开源，今天 3 月 28 日，准时上线。说到做到。

接下来，就给大家看看接上了飞书 CLI 之后，都能帮我们干啥。

📌 本文看点

01

CLI 是什么？跟你有什么关系

02

一段话完成安装配置

03

4 个真实场景实战演示

01

BASICS

### 简单科普下 CLI 是什么..

大家可能一听 CLI（命令行工具）就觉得是程序员的东西，跟自己没关系。

但你每天用电脑，其实一直在跟电脑"对话"。只不过你用的是鼠标——双击打开文件，拖拽移动，右键复制粘贴。

![](attachments/febe7e33f104b223.jpg)

但电脑还有另一种对话方式：**命令行**。

打一行mkdir 工作报告，文件夹就建好了。打一行open 周报.docx，文件就打开了。不用找图标，不用点菜单，一行字，一个动作。

「用命令行（或者说打字）跟电脑对话的方式，就叫 CLI。」

其实我们都在间接用它了：你让 Siri 定闹钟，Siri 背后就是在用命令调用你手机的时钟 App；你让 Claude Code 帮你搜文件、跑代码，它背后也是在用命令行操作你的电脑。

![](attachments/bac3db33a82b1bd8.jpg)

你负责说人话，AI 负责"打字"执行。

以前的问题是：飞书没有加入这个群聊。AI 再聪明，跟飞书之间没有沟通渠道，所以只能给你建议，不能帮你干活。

「飞书 CLI 就是把飞书拉进了这个群聊。」

装上之后，AI 终于能直接跟飞书对话了，帮你查日历、发消息、写文档、建多维表格、搜知识库、发邮件。

![](attachments/28da8fc43a24d5f1.jpg)

所以 CLI 跟你的关系是：**你完全不需要学它，甚至不需要知道它存在。**你只管用自然语言跟 AI 说话，AI 会自己用 CLI 去操作飞书。

安装一次，然后忘了它就好。

02

SETUP

### 怎么安装使用？

你除了可以在你的终端按照 GitHub 上的指引npm install -g @larksuite/cli去安装，

![](attachments/33fea1f52d87c6ff.jpg)

你还可以直接通过👇🏻这种方式：

Step一段话完成安装

复制以下内容，发送给你的 AI（Claude Code、Codex、Trae、Cursor 都行）：

💻 安装命令

帮我通过以下命令安装 lark-cli

npm install -g @larksuite/cli

然后通过以下命令安装相关 skills

npx skills add https://github.com/larksuite/cli -y -g

安装完成后，请给我发送应用配置链接，引导我完成应用的配置

![](attachments/d66ae7f96d312c0c.png)

就这么简单。你不需要手动配置任何东西，AI 会一步步引导你完成，简单方便，非常AI 友好的设计！

![](attachments/a4d8dbb59ca47380.png)

— 扫码授权

Auth让 Agent 以你的身份操作

飞书 CLI 支持两种模式：

·**不授权，直接用**：AI 可以帮你发消息、创建文档等操作，但看不到你的个人数据（日程、私信、收件箱）。

·**授权后，完全打通**：AI 可以访问你的日历、消息、文档，并以你的名义执行操作。

授权只需要一行命令：

lark-cli auth login --recommend

![](attachments/d3897f02ec2dbb78.jpg)

打开弹出的链接，在飞书里确认一下就行。如果你暂时跳过也没事，后续 AI 在需要访问你个人数据的时候，会自动弹出授权提示。

安装配置完成，接下来是正餐。

💡 如果你是 OpenClaw 用户：飞书即将上线内置全部 CLI 能力的官方插件，升级后无需单独安装 CLI，直接用就行。

03

IN ACTION

### 场景实战：Agent + 飞书能做什么

我用 Claude Code + 飞书 CLI 跑了几个真实场景，给大家看看这套组合拳的实际效果。

场景 1我的个人说明书

先来个简单的，当作你的"第一个任务"。

一句话，让 Agent 读取你在飞书上的各种信息，直接创建一篇"关于你的个人使用说明书"：

根据我的所在部门、飞书消息、飞书云文档、本周日历上的日程等信息，帮我创建一篇飞书云文档，写一篇关于我个人这周的说明书。

![](attachments/f3bbf64a46ff86f0.png)

— 自动加载 lark 的 skills

Agent 自动搜索你的飞书数据，提取关键信息，然后直接在飞书里创建了一篇文档。

![](attachments/1b59c7ae252f3f59.png)

— 把我这周的日程全扒出来了....

注意这里的关键点：**你拿到的不是一段需要复制粘贴的文字，而是一个飞书文档链接，**打开就能看、能编辑、能分享给同事。

![](attachments/df88e4600d16a0d6.png)

— 涉及到太多细节了...所以只能打码了

包括我觉得信息太隐私了，不方便给大家展示，然后直接跟它说，

![](attachments/3a12456220dc91fb.png)

最后看看效果：

![](attachments/2e819ed06e7da925.gif)

「这就是 CLI 最本质的能力，AI 不只是给你写了一段内容，而是帮你把事情办了。」

场景 2内容创作全流程：从选题到成稿

这个场景是我自己日常最高频的需求。

做内容的人都知道，写一篇文章的流程大概是：找选题 ->列大纲 ->写初稿 ->反复修改。中间要在 AI 工具和飞书文档之间来回切换、复制粘贴，效率很低。

现在这整条链路可以全部在飞书里跑通。

Step 1让 Agent 帮你找选题

帮我搜索一下最近飞书群聊和文档中，以及你可以看看最近热门的网站关于 AI Agent 落地应用的讨论内容，整理成 5 个选题方向，每个附上理由和切入角度，写入一篇新的飞书文档。

![](attachments/f4c298aa9c08af07.jpg)

Agent 搜索我的群聊和文档，同时还从网上看看最新新闻，提炼讨论热点，5 个选题带理由，直接写进飞书文档。

Step 2确认选题，写框架

就第 3 个选题展开，结合我过往的写作风格，创建一篇飞书文档，帮我想想整体的逻辑框架应该如何来设计？

Agent 根据你选定的方向，创建一篇新的飞书文档，直接在里面写好框架。

![](attachments/0a0e59a362f1d14e.png)

Step 3评论协作：人和 AI 在文档里对话

这一步最有意思。

![](attachments/859090ae796c0f38.png)

框架写完后，我直接在飞书文档里用**划词评论**提修改意见，之前给同事意见的时候都是这么提的...然后让 Agent 读取评论，自动修改正文：

{{文档链接}} 根据我的评论修改文档，修改后用划词评论标识出修改点。

Agent 读取你的每条评论，逐一修改对应段落，还会在修改处加上评论说明改了什么。你不满意？继续在评论区提意见，它继续改。

![](attachments/8f5d28aa8071f4fd.png)

「以前我们都是写完复制给 AI 看，AI 改完我们再复制回来。现在我跟 Agent 可以直接在同一篇飞书文档里"对话"。」

修改意见就是评论，修改结果就是正文。

![](attachments/5cb28c5bea479d04.gif)

整个过程不需要离开界面。

场景 3群聊消息总结 + 待办提取

这个场景应该是所有人都能共鸣的。

我们肯定都有这种经历：好几个项目群，每天几百条消息，翻都翻不完。更头疼的是，群里有人说了个事，你当时没记下来，后来就忘了。

现在一句话搞定：

帮我搜索一下「XX项目群」最近三天的消息，总结讨论要点，提取出跟我相关的待办事项，然后把待办创建成飞书任务，提醒时间设为明天上午 10 点。

Agent 搜索群聊消息 ->结构化总结讨论内容 ->识别出跟你相关的待办 ->直接创建飞书任务并设好提醒。

![](attachments/ebeb56548b04cdb4.png)

你不用翻聊天记录，也不用自己记待办。

如果你想更进一步，还可以让 Agent 把总结发回群里，让大家确认：

把总结和待办发到群里，@所有相关人确认一下是否准确。

![](attachments/d3c2ba1ae53b961e.png)

这个场景看起来简单，但它背后串联了飞书 CLI 的三个核心能力：**消息搜索、任务创建、消息发送**。

以前我们做这件事，得自己翻聊天记录、手动记笔记、手动建任务，至少花 20 分钟。现在一句话，30 秒。

场景 4多维表格 + 仪表盘——让数据自己说话

最后来一个视觉冲击力比较强的。

我平时写了不少内容，也给企业做过一些 AI 培训，资料散落在飞书的各个角落。一直想整理一下，但每次打开云空间看到一堆文件就放弃了。

现在让 Agent 帮我干这件事：

帮我搜索飞书云空间里我创建的所有文档，按类型（文章/方案/培训资料/笔记）分类，记录每篇文档的标题、创建时间、字数，全部写入一个多维表格，然后做一个仪表盘，我要看这段时间的内容创作分布和工作节奏。

![](attachments/eb228777e8ef18bd.png)

— 太强了....

Agent 自动拉取文档列表，分类打标签，写入多维表格，然后生成仪表盘。

![](attachments/75b7bdd0d5d1b4cd.jpg)

饼图看内容类型占比，时间线看创作节奏，一张仪表盘让你看清自己的内容资产全貌。

多维表格是飞书的杀手级功能。以前 Agent 只能帮你"说"应该怎么整理数据，现在它能直接帮你**建表、填数据、建视图、生成仪表盘**，一条龙全部搞定。

这就是飞书的实力和速度，永远为了你的 Agent 更好用而努力..

![](attachments/c7e53cb4835d9884.jpg)

而且，飞书还开放了一个许愿池。你想让 CLI 支持什么新能力？直接提交需求，也可以给别人的需求 +1 投票，票数高的优先安排。

![](attachments/14e1953681037e3e.png)

我提交了一个，**自动化生成多维表格字段，然后直接一体化打通 AI 工作流。**不用手动输入「字段捷径」，相信大家都知道飞书多维表格的实力吧...

∞

FINAL THOUGHTS

### 结语

「构建企业级 Agent 的难点，从来不是模型能力，而是能不能在真实系统里跑通。」

对于之前很多在使用飞书的企业来说，其实他们很希望自己的 AI Agent 能够跟飞书的生态进行结合与打通。

今天飞书 CLI 开源，显著降低了构建企业级 AI Agent 的门槛，提供了官方的最佳实践和完整的能力覆盖。

回看 AI Agent 这两年的路线图，基本上就是以"能动手实现结果"为主。

以前是你操作飞书，现在是 AI 操作飞书，你只管拍板。

作为一个重度飞书用户，我也有几点期待，希望官方尽快落实..

比如未来 CLI 能支持多维表格更细粒度的字段操作（自动创建字段类型、公式字段），支持捷径和快捷指令的创建（让 Agent 在飞书里设置自动化触发器），以及妙记的深度集成（不只是读逐字稿，还能自动标注关键时刻、生成行动项）。

甚至可以想象一下审批流的接入，让 Agent 能发起审批、追踪进度，那企业级的 AI 工作流就真正闭环了。

这些就交给许愿池吧。

以上。

END

我是甲木，热衷于分享一些 AI 干货内容，同时也会分享 AI 在各行业的落地应用。#Agent

如果你觉得今天这篇有收获，欢迎**点赞、在看、转发**三连，我们下期再见 👋🏻


---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c14d940ff63a1d1985f9d3b6d9f0dcbe3fa2e414f130fd1e31090afd00d9f2fcf68c9c7f0561&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1776482104_1&req_id=1776477378630175&scene=169&mid=2247491446&sn=708496f70f54dc8dde451845fcd9fe34&idx=1&__biz=MzkxNjY0MzM1MA==&sessionid=1776482569&subscene=200&clicktime=1776484052&enterid=1776484052&flutter_pos=24&biz_enter_id=5&jumppath=WAWebViewController_1776483809203,20020_1776483822349,BrandSubHistoryFlutterViewController_1776483824143,1104_1776483950390&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004724&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ+o8SVBlu46ZufCVpmA41EhLVAQIE97dBBAEAAAAAANniJThsPDsAAAAOpnltbLcz9gKNyK89dVj0DezA5nf4h9A5pibSsdGiAH8K6qoYKeGotfbkisX135tBjQqn5hnaUREp14HtVhG10HZCW0y1TO4yyhHonuB5opxrZbBgmCvjo4i7kHLYBx+zvc16Pyt710trSf1Ut1JNGJ09URwUo6WETsmr12INl3fvuCGULRjTDulgq7s/FIsO/BaBcYQPJqhaIFbX3Uc5PD0vUmQMbG5JDRwVxyuue2fBhyQ1u+XGeagaH0Uxaw==&pass_ticket=//zznkkkaGCwFAQE5YP3PAJT20Ki/iGJeF2EDYYnBFjPIaWSnnEkQNT6EULm4ikr&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/1b58a7f3-9541-428f-b542-6625c458b9c4/1b58a7f3-9541-428f-b542-6625c458b9c4/)
