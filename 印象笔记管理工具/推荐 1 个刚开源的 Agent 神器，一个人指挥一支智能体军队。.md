# 推荐 1 个刚开源的 Agent 神器，一个人指挥一支智能体军队。

---

原文链接: [https://mp.weixin.qq.com/s?chksm=f9a295d0ced51cc6e1a7d5f3b8e5f3f...](https://mp.weixin.qq.com/s?chksm=f9a295d0ced51cc6e1a7d5f3b8e5f3f28ecb24af452785872d4b6c1691ade997c515826ed6bb&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_3&req_id=1782034214604406&scene=169&mid=2247534105&sn=dd39c1fa41782f732bbfcd129e1d135e&idx=1&__biz=MzUxNjg4NDEzNA==&sessionid=1782032739&subscene=200&clicktime=1782034678&enterid=1782034678&flutter_pos=25&biz_enter_id=5&jumppath=WAWebViewController_1782034645425,WAWebViewController_1782034645925,20020_1782034668175,1104_1782034669239&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmjkGRZ/m9HdZ+06e3vn5pBLTAQIE97dBBAEAAAAAAPw4DYcl1k8AAAAOpnltbLcz9gKNyK89dVj0b3g5OrFTeVzY5T/sRJa3Sp9oqBA9eNBbbwpKjh0+oEG3+1SrILK/hMbGk/y73OyA+GH364r6Z3LYqOdaWwoubs74++HrfuhXmColFMRMclOGp0+VJwp3hWJMSE3HQ/FTBZ35rfXcnL/JK9CW354etOd/Rm5V22oUDvYX/ua5Peaas77XiOXqSEljCxbWMdypMoLvifCrU/TT4QPPyLY4XpDV7UQb6Efiqhyfy68=&pass_ticket=G77JohRV41BPVWGEIcVuszmTYqYbM30Sh5/BQPTW/0DubBQ9f5q1Glv1XCk7tk3X&wx_header=3)

Original逛逛逛逛GitHub

今天逛 GitHub 的时候，发现了一个刚刚开源的项目。

有点意思。

但如果你再找一个多项目并行互不干扰、离开电脑活还能推进、花的每一分钱都知道去哪了、AI 记错了你能打开它脑子改过来：

可以试试这个刚开源的 PilotDeck。

**一个人，一个 PilotDeck，一支智能体军队。**

**PilotDeck 是由清华大学 THUNLP 实验室、面壁智能、OpenBMB 与 AI9stars 联合研发并开源，面向通用场景、适用于多任务。**

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/D4FFA5D7-E311-4792-8719-8AC671D68BBD.png)

01

**开源项目简介**

**这个开源项目的理念，就是让你一个人就能指挥一支智能体军队的开源操作系统。**

在 PilotDeck 里，每个项目都有一个独立的工作舱 WorkSpace。

注意，这个 WorkSpace 可不是你在 IDE 里打开的一个文件夹哦，它是一个完整的智能体生存环境。

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/5AFFE2BA-50B7-4722-85B6-E3460190C882.png)

```
GitHub 链接：https://github.com/OpenBMB/PilotDeck  
官方网站链接：https://pilotdeck.openbmb.cn/
```

**每一个工作区有如下专属的东西，还挺有趣的。****专属文件系统：每个项目可操作的文件范围清晰划定，AI 生成的文件自动标识****专属记忆：Project Memory 记住项目目标、进度、限制；Feedback Memory 记住你的偏好和要求****专属技能：技能商店一键安装到对应 WorkSpace，随任务增长自动沉淀能力**

像是给 AI 造一个家。

### 我后面打算基于这个平台，同时运营多个平台：小红书、抖音、公众号、B 站、X 平台。

### 开 5 个 WorkSpace，每一个都是关于特定任务的经验。

一个人，五支队伍，互不干扰。

02

**几个超能力**

在这个基础上，PilotDeck 有三个让我眼前一亮的超能力。

① Always-on：你睡了，它还在干活
---------------------

Always-on 是 **Agent 主动发现值得做的事，自己干，干完把成果落地成文件，等你来看。**

比如搞小宇宙播客的博主，录制了一期中文播客，睡前跟 PilotDeck 说："帮我把这期翻译成英、日、韩、法、德、西、葡、阿拉伯、俄语，注意文化适配。"

然后安心睡觉。

Always-on 模式启动。

Agent 自动拆分任务，调度子 Agent 分别执行各语种翻译。

智能路由判断：简单语种走便宜模型，需要文化意译的部分走强模型。

第二天早上，9 个翻译版本整整齐齐躺在 WorkSpace 里。

日语版把"有点东西"翻译成了「なかなかやるな」（颇具实力），而不是直译成"有些东西"。

Token 花费不到一杯星巴克。

### 下面这些都是使用 PilotDeck 跑出来的，而且是 20B 级别的模型，效果还是挺顶的。

### ② 凌晨 3 点的 Dream 模式

PilotDeck 有个很浪漫的功能叫 **Dream（梦境）**。

Agent 在空闲时段自动回顾、整理和优化自身记忆，就像人类在睡眠中整理白天的记忆一样。

哪些经验值得沉淀、哪些记忆可以压缩、哪些任务进度需要更新，它自己搞定。

③ 智能路由，简单任务不配用最贵的脑子
-------------------

用 AI Agent 搞日常工作，月 token 费用可能都比工资还高。

大多数工具默认所有任务都用同一个最贵的模型。就像一个公司里所有活都让总监干，从写战略规划到订外卖都是同一个人。

PilotDeck 的智能路由会自动判断任务复杂度：

简单任务，比如文案生成、格式调整 → 自动走便宜模型，省钱 70%~90%中等任务，比如邮件撰写、数据分析 → 匹配中等模型复杂任务，比如策略规划、深度研究 → 走强模型

### 实测数据：

**小红书种草文案场景：**

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/8A26DEF2-AA14-41B7-A4DF-E6391C62F79D.png)

**同样的效果，省了约 70%。**

**复杂任务场景（播客多语言推送、论文综述、金融分析等）：**

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/1FC75B19-B39B-4CBB-BD64-98B7FE820388.png)

**1/6 的成本，效果超过 Claude Sonnet 4.6 单 Agent。**

而且每个 WorkSpace 独立算账的，"写自媒体文章一共花了 80 元，邮件花了 120 元，日报花了 300 元"，每一分钱都有去处。

你可以看到每一个任务的发费，好处是能够通过此来探索找到成本最低，效果最稳定的一条路。

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/132D47EC-B811-4123-9D80-5B7652BB9572.png)

④ 白盒记忆
------

AI 记错了，可以打开它脑子改改。PilotDeck 把记忆变成了白盒：
------------------------------------

**PilotDeck 下，打开某一个项目的 WorkSpace，可以直接查看它的 Memory。**

**发现不对的地方直接改就行了。**

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/A17F5226-F05A-4912-8936-500CFD45466D.png)

### 更酷的是：它真的越用越懂你。

每次你纠正 Agent 的偏好，它都记在 Feedback Memory 里。三个月后，Agent 像一个磨合了十年的搭档，你说半句话，它就知道你要什么。

而这一切都在你的掌控中：觉得最近谐音梗太多了，打开 Feedback Memory，找到偏好谐音梗这条记忆，改成偶尔用，立刻生效。

**而且很重要的一点是 **PilotDeck 专注在 Project Memory 和这个 Feedback Memory 上。****

****不会很随便的把各种对话的流水账转成记忆，因为流水账式的信息对你后续的使用其实意义不大。****

03

**点击下方卡片，关注逛逛 GitHub**

这个公众号历史发布过很多有趣的开源项目，如果你懒得翻文章一个个找，你直接关注微信公众号：逛逛 GitHub ，后台对话聊天就行了：

![](.evernote-content/AB7D7FC0-3680-4211-8F44-74262C1C4277/A2A14B65-535C-416B-9DCD-1489CC7E8DAA.png)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=f9a295d0ced51cc6e1a7d5f3b8e5f3f28ecb24af452785872d4b6c1691ade997c515826ed6bb&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_3&req_id=1782034214604406&scene=169&mid=2247534105&sn=dd39c1fa41782f732bbfcd129e1d135e&idx=1&__biz=MzUxNjg4NDEzNA==&sessionid=1782032739&subscene=200&clicktime=1782034678&enterid=1782034678&flutter_pos=25&biz_enter_id=5&jumppath=WAWebViewController_1782034645425,WAWebViewController_1782034645925,20020_1782034668175,1104_1782034669239&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmjkGRZ/m9HdZ+06e3vn5pBLTAQIE97dBBAEAAAAAAPw4DYcl1k8AAAAOpnltbLcz9gKNyK89dVj0b3g5OrFTeVzY5T/sRJa3Sp9oqBA9eNBbbwpKjh0+oEG3+1SrILK/hMbGk/y73OyA+GH364r6Z3LYqOdaWwoubs74++HrfuhXmColFMRMclOGp0+VJwp3hWJMSE3HQ/FTBZ35rfXcnL/JK9CW354etOd/Rm5V22oUDvYX/ua5Peaas77XiOXqSEljCxbWMdypMoLvifCrU/TT4QPPyLY4XpDV7UQb6Efiqhyfy68=&pass_ticket=G77JohRV41BPVWGEIcVuszmTYqYbM30Sh5/BQPTW/0DubBQ9f5q1Glv1XCk7tk3X&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/257b51ca-6bc2-4321-8e2c-0c5334286f03/257b51ca-6bc2-4321-8e2c-0c5334286f03/)