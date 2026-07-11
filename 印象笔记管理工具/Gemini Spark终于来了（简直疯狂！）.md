# Gemini Spark终于来了（简直疯狂！）

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjMzODE4NA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzYzMjMzODE4NA==&mid=2247491059&idx=1&sn=e9b0277740c6ee97851543f9b1ca587e&chksm=f14a43d7d252a920b73e4837a793600c4599ac323c98faf8a932c96db9e28ecf3b94ddd2d421&scene=90&xtrack=1&req_id=1779427849672904&sessionid=1779427875&subscene=93&clicktime=1779427899&enterid=1779427899&flutter_pos=1&biz_enter_id=4&ranksessionid=1779427849&jumppath=1001_1779427873189,1104_1779427876705,20020_1779427880028,1104_1779427891784&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004930&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzUW6WXPelvxDl0vCuYiUixLTAQIE97dBBAEAAAAAALcWFMVqsMQAAAAOpnltbLcz9gKNyK89dVj0abwfu+5dfdbIymXZn/xe8WrguPJ9Vy0OtoT9ETB6YRp/Wu0gRUHjv6UTYj6m30adVzaJDTsezyrPkVQZ9mPp0+ZPrIHY/BQs0hVqp6v5jZOLNuaV8dVRiyrETNBD8tf3qLEQBdnC0gp912CcUW+jzW5JFH9UaTkq+w+QwrdUXqytw4brpj4whh2DCk7gsZ9LrRP0EpyjabAD+3zxAzkHPpdqDMBjYGQhjmXazWc=&pass_ticket=ZuGLUN2+BxC+q1si9rB8sr8LBHFdxBqUCgBFZd3G2bYsEPZaHv42drzIaFT70sAC&wx_header=3)

Original老刘的笔记本 老刘的笔记本

---

我把笔记本合上了。

Spark在Google Cloud的虚拟机上继续替我跑活——这是我用AI两年来，**第一次真切体会到"代办"两个字的含义**。

不是"AI回答了我的问题"，是"**我布置了任务，AI在我睡觉时替我做完了**"。

一周下来，我有**8条心得**想分享。但在那之前，我先讲清楚Spark到底是什么——以及它和你想象中的"AI助手"，差在哪里。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/994E7C14-FD0D-4B1F-8264-142611C91F31.png)

一、Spark不是聊天机器人，是"一个会上班的虚拟员工"
----------------------------

我们先做一个翻译。

**ChatGPT / Claude / 旧版Gemini = 聊天**——你输入，它响应，会话结束。

**Gemini Spark = 上班**——你布置任务，它在Google Cloud的专属虚拟机上**连续工作几小时甚至几天**，过程中**你的电脑不必开机**。

Spark的硬件配方是这样的：

* • **大脑**：Gemini 3.5 Flash（我前几天评测过的那个"吊打Pro"的Flash）；
* • **执行器**：Google Antigravity Harness（专门为agent训练的工具调用框架）；
* • **身体**：Google Cloud的专属虚拟机，**24/7在线**。

关键差异：**普通AI跑几秒就停，Spark跑几小时甚至几天**——Google管这个叫"**long-horizon execution**"（长时程执行）。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/6E2FCCE7-23DB-47E0-AAF7-BA3FE420BDB5.png)

二、三根支柱：Tasks、Skills、Schedules
-----------------------------

Spark的整个产品形态可以用三根支柱概括。

**第一根：Tasks（任务）** —— 一次性活儿。

例：扫描我的Google Drive，把过去30天最重要的文件归类整理到一张表里。

我布置后关掉电脑，**等它做完会给我推送**。

**第二根：Skills（技能）** —— 训练一次，永久记住。

例：读我过去50封邮件，提炼成一份"语气风格指南"，命名为"Ghostwriter"。以后每次我让你起草邮件，**都按这个风格写**。

这是我玩到第三天才意识到威力的功能——**详见下面第三节**。

**第三根：Schedules（定时计划）** —— 时间触发。

例：每周一早9:00，扫上周收件箱，生成本周优先级to-do，**在我的日历上锁定深度工作时间块**。

这三根支柱合起来，Spark就从"工具"变成了**真正会持续工作的"虚拟员工"**。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/0A3D4DA9-D960-4002-92A7-84A658B2D262.png)

三、Skills才是杀手锏：我训了一个"我"
----------------------

让我先讲清楚Skills为什么重要。

**过去我用AI写邮件最大的痛点**：起草的版本永远"不像我说话"。要么太正式，要么不够直接，**每封都得改20-40分钟**。

我用Spark做的第一件事就是建一个Skill：

1. 1. 把我过去50封发件邮件喂给它；
2. 2. 让它分析我的句式、用词、节奏；
3. 3. 命名为"**Ghostwriter**"。

从那以后——**它每次起草，都是我的语气**。

我不再改主语、不再删客套、不再调整长短句节奏。**40分钟的活儿压缩到5分钟review**。

Skills的本质：**训一次，用一辈子**。一次性投入 vs 终身复利——这是agent经济和chat经济的根本差异。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/994E7C14-FD0D-4B1F-8264-142611C91F31.png)

四、Schedules：我的周一早晨彻底变了
----------------------

第二个让我上瘾的是Schedules。

我设了一条**周一8:55触发**的Schedule，内容：

1. 1. 扫描上周收件箱所有邮件；
2. 2. 提取必须本周回复的，按紧急度排序；
3. 3. 生成一份"本周优先级to-do"；
4. 4. **在我的Google Calendar上自动锁定深度工作时间块**——避开会议时间。

每周一早9:00我打开电脑，**所有"思考"已经做完**，剩下的只有"执行"。

我的判断：**这种"被动接收"的工作流**，比任何效率App都更接近"真正的助理"。它不是替你做事，它是**替你做好了准备**——你只负责确认和执行。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/6E2FCCE7-23DB-47E0-AAF7-BA3FE420BDB5.png)

五、它跑的不是Google圈：MCP打通整个数字世界
--------------------------

这是大多数人会忽略的一个点。

Spark默认接入**所有Google全家桶**：Gmail、Calendar、Drive、Docs、Sheets、Slides、YouTube、Maps。

**但真正的杀招在MCP**——**Model Context Protocol**。

通过MCP，Spark可以调用：

* • **Notion** —— 自动写入和读取我的工作笔记；
* • **GitHub** —— 创建Issue、跟踪PR；
* • **Slack** —— 监控频道、回复消息；
* • **Canva** —— 自动生成设计稿；
* • **OpenTable / Instacart** —— 预订餐厅、下生鲜单。

**这意味着Spark不再被困在Google生态里**——它能在你的**全部数字世界**里跑活。

一周下来我最深的感受：**Spark不是Google的工具，它是我个人的"操作系统"**。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/0A3D4DA9-D960-4002-92A7-84A658B2D262.png)

六、它会停下来问你：危险操作前必须人工确认
---------------------

我特意挑了一个测试场景：让Spark**自动给一个客户发会议确认邮件**。

它走完了所有准备步骤——查日历、起草邮件、确定收件人、生成主题——**然后停下来等我确认**。

弹窗里写着：**"Ready to send email to X. Confirm?"**

类似的还有：

* • 花钱前问：**"Confirm purchase of $X?"**；
* • 发到对外渠道前问；
* • 调用第三方服务前问。

这是Google做对的一件事——**所有"会产生不可逆后果"的动作，必须人工二次确认**。你才是老板，Spark是助理。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/994E7C14-FD0D-4B1F-8264-142611C91F31.png)

七、可用性：先给Ultra订阅者
----------------

直说硬条件：

* • **美国地区**先开放；
* • **Google AI Ultra订阅者**（新增的100美元/月档位，或下调到200美元的最高档）；
* • **18岁以上**；
* • **Gemini Enterprise**企业用户同步开放；
* • "**接下来几周扩展更多区域**"——Google官方原话。

如果你在中国大陆，**目前还要等**——但我建议**现在就开始研究**，等开放时就能立刻上手。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/6E2FCCE7-23DB-47E0-AAF7-BA3FE420BDB5.png)

八、我从一周实战里提炼的8条心得
----------------

这8条是我**踩过坑后**总结的，**直接照搬就能少走弯路**：

1. 1. **先列"每周重复浪费时间"的事**——那是Spark最该接管的清单；
2. 2. **别一上来全自动化**——挑1个Skill训练，跑通再加下一个；
3. 3. **重复性的事统统挂Schedule**——每周/每月节奏的任务最适合；
4. 4. **任何"发出去"和"花钱"操作，必须人工Review**——别图省事；
5. 5. **训Skills时，给"样本"而不是"描述"**——50封旧邮件比一段风格说明强10倍；
6. 6. **任务prompt当成员工JD写**——具体输入、具体输出、具体边界；
7. 7. **把Spark的虚拟机当"远程同事"**——你的角色是项目经理，不是执行者；
8. 8. **每周回顾一次Skills和Schedules**——删掉用不上的，避免变成噪音。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/0A3D4DA9-D960-4002-92A7-84A658B2D262.png)

九、最深的判断：AI竞赛已经从"聊天"卷到"上班"
-------------------------

写到这里我意识到一件事——

**Spark的发布不是一个产品发布，是整个行业方向的一次正式宣告**。

过去两年，所有AI产品都在比"谁的对话更聪明"。今天起，所有人都在比"**谁的agent更会替你打工**"。

这是两条完全不同的赛道：

* • **聊天**比拼的是模型本身的智能；
* • **上班**比拼的是**模型+工具调用+长时程规划+人机接力**整套系统。

我的判断：**6个月后，会用agent的人和不会用agent的人，会被分到两个完全不同的世界**。差距类似"会用Excel"vs"会写Excel公式"——但放大10倍。

![](.evernote-content/FF5AB524-8768-40EA-AA6A-CB52DD65E47C/994E7C14-FD0D-4B1F-8264-142611C91F31.png)

写在最后：你今晚就该做的一件事
---------------

如果你是Google AI Ultra订阅者——

**今晚就打开Spark**。**只做一件事**：**训一个Ghostwriter Skill**——把你过去发出的20封邮件喂给它，命名保存。

明天起草下一封邮件时，你会理解我为什么写这篇文章。

如果你还没订阅——

**这是我连续写4篇Gemini文章里第一次劝你掏钱**：每月100美元，**省下的时间远值这个数**。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjMzODE4NA==&mid=2247491059&idx=1&sn=e9b0277740c6ee97851543f9b1ca587e&chksm=f14a43d7d252a920b73e4837a793600c4599ac323c98faf8a932c96db9e28ecf3b94ddd2d421&scene=90&xtrack=1&req_id=1779427849672904&sessionid=1779427875&subscene=93&clicktime=1779427899&enterid=1779427899&flutter_pos=1&biz_enter_id=4&ranksessionid=1779427849&jumppath=1001_1779427873189,1104_1779427876705,20020_1779427880028,1104_1779427891784&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004930&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzUW6WXPelvxDl0vCuYiUixLTAQIE97dBBAEAAAAAALcWFMVqsMQAAAAOpnltbLcz9gKNyK89dVj0abwfu+5dfdbIymXZn/xe8WrguPJ9Vy0OtoT9ETB6YRp/Wu0gRUHjv6UTYj6m30adVzaJDTsezyrPkVQZ9mPp0+ZPrIHY/BQs0hVqp6v5jZOLNuaV8dVRiyrETNBD8tf3qLEQBdnC0gp912CcUW+jzW5JFH9UaTkq+w+QwrdUXqytw4brpj4whh2DCk7gsZ9LrRP0EpyjabAD+3zxAzkHPpdqDMBjYGQhjmXazWc=&pass_ticket=ZuGLUN2+BxC+q1si9rB8sr8LBHFdxBqUCgBFZd3G2bYsEPZaHv42drzIaFT70sAC&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d98cd1f1-c834-494b-9d97-af145bab7cc3/d98cd1f1-c834-494b-9d97-af145bab7cc3/)