---
title: 我给3个Hermes配了个自动排班系统，现在连任务都不用我分配了！
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/我给3个Hermes配了个自动排班系统，现在连任务都不用我分配了！.md
tags: [印象笔记, 其他]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "我给3个Hermes配了个自动排班系统，现在连任务都不用我分配了！"
source: evernote
type: note
export_date: 2026-06-25
guid: cae0fbc1-ffce-4991-b863-823efdf597d4
---

# 我给3个Hermes配了个自动排班系统，现在连任务都不用我分配了！

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI1NzA2MjU0Nw==&mid=265084...](https://mp.weixin.qq.com/s?__biz=MzI1NzA2MjU0Nw==&mid=2650841525&idx=1&sn=16e7ee82187139c106cc321ecb49ba07&chksm=f0668110e28dc51684dae57d155588b629b6ce27b5ad242b3a88b018f104ea1455aceef8c8a0&scene=90&xtrack=1&req_id=1778846810408431&sessionid=1778845844&subscene=93&clicktime=1778847277&enterid=1778847277&flutter_pos=52&biz_enter_id=4&ranksessionid=1778846810&jumppath=20020_1778847232704,1104_1778847233505,20020_1778847256370,1104_1778847266552&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004929&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQMBl0OF0kL7xp7pSIO9A1mRLVAQIE97dBBAEAAAAAAM3+LfVSQkYAAAAOpnltbLcz9gKNyK89dVj0aCLbi3D4mgBHDfXyoO9EsFYCQezftj2XLXepqkQzTjN1elvKGAY8wh6dXIN4SMVle4lDf/hmYJv8/MhWszTQy+T6Oj9n3NuzPPCIv/4D4YbfVNDEouV41lYARSfjbZdpPYS2Fk4JttwASO25PXBQjELw7HIS9+rEG/wHweQS45M/V6F4p7dXdCWHeY6w0ylqzR5C/xLsTPk6kiRFSaG7PgYbr7EIkP9Vuy2ivSTbhA==&pass_ticket=lI6jtRevYsJE6+yKUWEKMq4/fBheb5VBfauz2OHDKAOL4hk8kEADdQgaqwxoDWrl&wx_header=3)

# 我给3个Hermes配了个自动排班系统，现在连任务都不用我分配了！

Original元小二2046 元小二学AI

![](attachments/14a042980c945693.jpg)

你好，我是元小二，专注分享 AI 提效、一人公司实践和个人成长。这里有 OpenClaw、Claude Code、自动化流程、虚拟产品，也有理财、思考和生活系统。

欢迎关注，也欢迎后台留言告诉我，你对哪部分内容感兴趣。

朋友们，这是一个喜大普奔的好消息：

我的AI多Agent团队，升级了。

之前我跟大家分享过，我用Hermes框架搭了三个AI员工——元小一、元小三、元小四——让他们自己开会、自己干活、自己归档。

![](attachments/6281f2b03db5335a.png)

但我最近发现了一个问题：

任务一多，就乱了。

元小一派完任务，我不知道谁在做哪个、做到第几步、有没有卡住。有时候元小三还没查完，元小四就开始自己编内容。有时候任务已经全完成了，我都不知道。

我像个不在场的老板，完全没有”公司视角”。

后来我发现Hermes自带一个功能，叫**Kanban**。

用了之后，我对以前那种”靠肉眼盯着Discord消息流”的管理方式，评价是：那根本不叫管理，那叫蒙眼飞行。

---

## 一、Kanban是什么，三句话说清楚

Kanban不是普通的待办清单。

它是一个**多Agent任务调度看板**——任务会在不同状态之间自动流转，由对应的Agent自动认领，失败了自动重试，卡住了留记录等人工介入。

你只需要告诉它”有哪些任务、谁来做、先后顺序是什么”，剩下的它自己跑。

启动只需要两条命令：

hermes kanban inithermes dashboard

`hermes dashboard`会在浏览器里打开本地控制台，默认地址是`http://127.0.0.1:9119`。

你可以把Dashboard理解成”老板视角”——哪个Agent在干活、哪个任务卡住了、哪个环节效率最低，一眼全看到。

如果你输入完命令之后，Hermes报错了，那可能是你的Hermes版本太低了，建议升级一下：

hermes update

---

## 二、看板上的6个状态，比你想的有用

Kanban看板从左到右有6列：

**Triage**：原始想法区，先把粗糙的任务扔进来，可以让LLM帮你扩写成完整规格。

**Todo**：已创建，但还不能开始——可能是有前置依赖，或者还没分配给谁。

**Ready**：准备好了，等Dispatcher调度器来领取。

**In Progress**：Agent正在执行，默认按不同Agent分组显示。

**Blocked**：任务卡住了，可能需要人工输入，或者连续失败触发了断路器。

**Done**：完成。

### 1. 最关键的那条线

从Todo到Ready的那道门，是整个Kanban的核心价值所在。

它能做到：**元小三没查完之前，元小四根本看不到任务**。

---

## 三、用`--parent`把任务串成接力棒

我之前踩过一个坑：元小一同时叫醒了元小三和元小四，元小三去查资料了，元小四没资料可用，就开始自己编。等元小三查完，两份内容完全对不上。

Kanban彻底解决了这个问题，靠一个参数：`--parent`。

比如我的内容生产流程，可以这样创建：

# 第一步：素材调研
RESEARCH=$(hermes kanban create "调研本周AI工具热点" \--assignee 元小三 --priority 2 --json | jq -r .id)
# 第二步：写稿，依赖调研完成
DRAFT=$(hermes kanban create "整理成结构化笔记" \--assignee 元小四 --parent $RESEARCH --json | jq -r .id)
# 第三步：改写，依赖写稿完成
hermes kanban create "改写为公众号推文" \--assignee 元小一 --parent $DRAFT

`--parent`的意思是：**上一个任务完成，这个任务才会进入Ready**。

一开始只有调研任务在跑，写稿和改写都在等。调研完成后，写稿自动解锁；写稿完成后，改写才启动。

这个叫依赖提升机制。

我之前靠在SOUL.md里写”严禁同时艾特多个专家”来控制时序，现在换成Kanban，时序是系统保证的，不是靠Agent自律。

可靠程度，完全不是一个量级。

---

## 四、多个Agent并行干活，是这个样子的

并行这件事，Kanban也支持，而且支持得很优雅。

比如我现在的AI自媒体流水线，设计了6个角色：

- collector：收集素材
- editor：提炼观点
- redbook：改写小红书
- wechat：改写公众号
- designer：生成配图提示词
- publisher：整理发布清单

素材收集和观点提炼是顺序的，但小红书和公众号可以并行跑。

Kanban里，我可以把redbook和wechat都设为editor任务的子任务，editor一完成，两个改写任务**同时进入Ready，各自被对应Agent领走**。

然后启动网关：

hermes gateway start

不同Agent会各自领取属于自己的任务，互不干扰，在Dashboard里看，In Progress那一列按profile分组，一眼就是”谁在做什么”。

我之前自己做这套流程，一篇内容从素材到发布清单要花3个多小时。

现在我只需要把素材丢进Kanban，去睡一觉，醒来所有内容都在对应文件夹里了。

---

## 五、任务失败了，不会悄无声息地消失

这个点，是我觉得Kanban最有价值的地方之一。

传统的多Agent系统，任务失败了你通常只会看到”没有反应”。你不知道是Agent挂了、还是任务没派到、还是前置依赖没完成。

Kanban会记录每一次执行的结果：

- `spawn_failed`：Worker启动失败
- `gave_up`：连续失败3次，触发断路器，进入Blocked
- `crashed`：进程中途挂掉，自动释放任务，等下一次重新派发
- `completed`：完成

可以用这个命令查看某个任务的执行历史：

hermes kanban runs <task\_id>

连续失败3次后进入Blocked，不会无限重试，必须人工解锁——这叫断路器机制。

遇到这种情况，在Dashboard里点Unblock，或者直接：

hermes kanban unblock <task\_id>

第二次执行时，Worker会看到第一次被阻塞的原因，所以它知道要改什么，不需要从头猜。

---

## 六、最被低估的功能：结构化交接

Kanban好不好用，很大程度上取决于你有没有让Agent**写好交接信息**。

Worker完成任务时，要写清楚：做了什么、改了哪些文件、做了哪些决策、下一步怎么接。

kanban\_complete(summary="完成小红书标题和正文改写，保留原文核心观点，增强痛点和行动感",metadata={"output\_files": ["redbook\_draft.md"],"decisions": ["标题采用痛点型", "正文采用清单结构", "结尾加入互动提问"],"next\_step": "交给designer生成封面图提示词"
})

这样下一个Agent接手时，不需要翻聊天记录，直接知道：前面的人做了什么、为什么这么做、自己从哪里开始。

普通待办清单只记录”现在做到哪了”。

Hermes Kanban记录的是”之前怎么失败的、为什么失败、这次怎么改”。

这，才叫AI团队的协作记忆。

---

把Kanban接进Hermes，整个多Agent系统从”能跑”变成了”真正可管理”。

我对没有看板的多Agent系统的评价是：那不叫团队，那叫一群AI在乱跑。

先把素材收集、观点提炼、小红书、公众号、配图、发布检查这6个节点用`--parent`串起来，跑通一遍，你会发现：**原来AI团队可以这么安静地工作**。

---

## 七、Hermes和OpenClaw，到底有什么区别？

用Hermes用了一段时间，最常被朋友问到的一个问题是：

“我之前在用OpenClaw，这俩有啥不一样，我要不要换？”

我来说清楚，不绕弯子。

**Hermes：任务板驱动的多Profile协作型。**

它的多Agent核心是Kanban。每个任务是一行数据库记录，每次交接是一行记录，每个Worker是一个有自己身份的完整进程。你可以把它想成：**给AI团队用的Jira**——任务状态、依赖关系、失败历史、交接备注，全都有。

**OpenClaw：网关路由+多命名Agent+Sub-Agents型。**

它的核心不是任务板，是”入口”。Telegram、飞书、微信——哪个IM进来的消息，路由给哪个Agent处理。它也支持Sub-Agents，可以后台非阻塞地spawn一个子Agent去干活，完成后把结果announce回来。

![](attachments/33f4f13d9933ccc4.png)

### 1. 最关键的一个区别

我之前以为OpenClaw不支持并行，后来翻了官方文档才发现：这是我理解错了。

OpenClaw的Sub-Agents是非阻塞的，spawn完立刻返回run id，子Agent在自己的session里跑，跑完自动把结果推回来。

**它是支持并行的。**

真正的区别在于：Hermes有原生任务状态机、run history、断路器——失败了记录、失败3次锁住、解锁后带着上次失败原因重试；OpenClaw没有这一套，它的多Agent协作更偏”消息和会话层”，不是”任务板层”。

### 2. 两者的隔离性，其实差不多

Hermes的Profile，独立config、memory、sessions、skills——但文件系统不隔离，仍然是当前用户权限。

OpenClaw的Agent，独立workspace、agentDir、session store——但同样，不是硬沙箱，绝对路径照样能访问其他位置。

要说哪个更安全，两边都需要额外配沙箱。这点上别被”隔离性强”的说法带跑了。

### 3. 我的真实使用场景拆分

我自己现在是这样用的：

**批量内容生产、工程流水线、长期任务追踪**——用Hermes Kanban。素材调研→整理笔记→改写推文这条流水线，依赖关系清晰，需要审计追踪，Hermes Kanban一把搞定。

**Telegram群里的快速响应、多角色聊天、个人自动化**——用OpenClaw。有人在群里@一个Agent要查资料、另一个人要起标题，OpenClaw的网关路由处理这种场景很顺手（TG升级了bot-to-bot的能力）。

两个一起用，其实比单独选一个更好使。

我对”Hermes和OpenClaw只能二选一”这种说法的评价是：这是个假命题。

![](attachments/1c4c9cc90371813f.png)

---

赶快去试试吧，期待你的反馈，我的朋友。

人生是一场无限游戏，乾坤未定，你我均是黑马。

---

【元小二学AI】👇公众号后台回复关键词【**hermes**】，领取从小白到高手的Hermes全套教程。


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI1NzA2MjU0Nw==&mid=2650841525&idx=1&sn=16e7ee82187139c106cc321ecb49ba07&chksm=f0668110e28dc51684dae57d155588b629b6ce27b5ad242b3a88b018f104ea1455aceef8c8a0&scene=90&xtrack=1&req_id=1778846810408431&sessionid=1778845844&subscene=93&clicktime=1778847277&enterid=1778847277&flutter_pos=52&biz_enter_id=4&ranksessionid=1778846810&jumppath=20020_1778847232704,1104_1778847233505,20020_1778847256370,1104_1778847266552&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004929&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQMBl0OF0kL7xp7pSIO9A1mRLVAQIE97dBBAEAAAAAAM3+LfVSQkYAAAAOpnltbLcz9gKNyK89dVj0aCLbi3D4mgBHDfXyoO9EsFYCQezftj2XLXepqkQzTjN1elvKGAY8wh6dXIN4SMVle4lDf/hmYJv8/MhWszTQy+T6Oj9n3NuzPPCIv/4D4YbfVNDEouV41lYARSfjbZdpPYS2Fk4JttwASO25PXBQjELw7HIS9+rEG/wHweQS45M/V6F4p7dXdCWHeY6w0ylqzR5C/xLsTPk6kiRFSaG7PgYbr7EIkP9Vuy2ivSTbhA==&pass_ticket=lI6jtRevYsJE6+yKUWEKMq4/fBheb5VBfauz2OHDKAOL4hk8kEADdQgaqwxoDWrl&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/cae0fbc1-ffce-4991-b863-823efdf597d4/cae0fbc1-ffce-4991-b863-823efdf597d4/)
