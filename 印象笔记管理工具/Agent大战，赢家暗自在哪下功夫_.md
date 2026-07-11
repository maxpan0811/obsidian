# Agent大战，赢家暗自在哪下功夫?

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU1OTEwNDkwNw==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw==&mid=2247492927&idx=1&sn=2af47928c4607429b5c89f80314115f8&chksm=fc1ef3dbcb697acd1d7096d418b4502e5402d3eb064ad3f4287aa7ec62b8f36ede84442379a7&exptype=timeline_unsubscribed_social_card&force_enter_love_page=1&req_id=1779345616279185&scene=90&ascene=56&devicetype=iOS26.5&version=1800492f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQXtig4LSK8iun6447HOIIkxLTAQIE97dBBAEAAAAAAOxtAbsHWrIAAAAOpnltbLcz9gKNyK89dVj0aQm7azKLfA17CAAR7+72npcEBJdnqK/LQPCJmcfVoDrFamaep4CLuy/kRx3tx8V3rtiQEdbSUBwUjN4sMJRHqvSgukmK3X5yiwQWasD70pL/taRFHO2RH76r+r94zILhHt2I9S11+ww+n7ohSsV09AJKWCR2BVGLNkw4lX2XAzhKmXatKHbfQvzOHCY5ih3FH12pEs5T8SKm7+9PiFuhtpZRwP9bcezueeJFmds=&pass_ticket=jbeCe2jaBOffqhxEcHe5n1y91Q9QmRvKpej1QFsY4oI89+hrZKMDqFeL9skgcCTB&wx_header=3)

Original亲爱的数据 亲爱的数据

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/76571FC2-01FE-49D7-B685-C9EE67C09E48.jpg)![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/299968C9-008C-4848-BE25-836323018E9D.jpg)![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/D3C28C44-0B31-43E1-BADF-B30B65898B6B.png)

（一）日子都不好过
---------

OpenAI和Anthropic在release note节奏上，

证明了一件事：

他们有实力两周抬一次模型能力线。

其威力，足以消灭掉一批创业公司。

这事不展开，共识。

在这一波里，别说小公司，

大厂也压力山大，日子都不好过。

谷歌虽然全栈发力，但至今未能稳赢，

微软再也不强势地领先了，

AWS没有好模型，

Meta不仅没有好模型，还没有好芯片；

苹果虽然没有好模型，但只剩好硬件；

阿里有好模型好芯片，但没有Top1的APP；

字节有好APP，但只有视频模型领先；

腾讯的模型在大力提高广告营收。

百度有好芯片，但此前落后太多。

看完这一圈，你会发现一件事：

模型本身的牌桌，几乎定型了。

但这些大厂并没有躺平。

每一家都在悄悄做一件事：

绕道模型背后，搭一层别的东西。

Anthropic自己也在做。

它2026年4月推出CMA，突出API服务，

阿里云4月也推出了JVS Crew，

把企业级Agent平台架在已有云基础设施上，

Meta想花20亿买下MANUS但被拦下了。

以上每一个动作，都不是在抬模型能力。

而是，模型之外，Agent之下，那一层infra。

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/DE6EEF59-67F7-4A57-8AB8-005EC12F08F5.png)

（二）“运行时”是地基
-----------

很多人只焦虑模型吃应用，其实不止，

我和朋友挨踢小茶聊天，

他总结了一句，非常到位：

模型变强，吃Infra，吃Agent，

吃Harness，吃应用。

这一看，谁都不安全，怎么才安全？

我观察两种活得好的Agent，

总结除一个规律：

都自己做一些Agent基础设施的工作

第一，先看通用Agent赛道的两大标本，

都是"端到端把活干完的产品形态"，

可不绑定任何优秀模型。

MANUS的卖点是，

一个Agent在云端虚拟机里干完活。

Genspark的卖点是，多个模型互相校验，

合成一个产品级交付物，

自研模型路由和多个Agent协同系统。

第二，垂直Agent有两个代表性智能体，

Kosmos和Hippocratic，典型vertical Agent。

首先，它们都选对小众市场，

占据稀缺资源的垂直智能体。

其次也都在Agent基础设施下了硬功夫。

科学发现赛道上，Kosmos是教科书级别的示范。

团队为了让Agent能在科研场景下，

连续跑十几个小时，读上千万token，

专门做出来的一套基础设施。

没办法，科研的研究背景庞大（上下文更长），

传统做法是全塞进去，科研这样处理不行，

就会有注意力衰减，研究目标越跑越偏。

于是，他们在Agent外面单独搭了一层数据库，

去解决了模型本身解决不了的问题：

长程任务的状态管理。

其次，医疗智能体Hippocratic，

它护城河是1.8亿次医疗交互，

且把对话过程做成“可控，可验证，可审计”，

这可不是什么“附加功能”，

而是直接嵌在运行时（Runtime）里的。

不难发现，虽然有通用和垂直两种活法，

但是狠招都一样，都在Agent基础设施里下功夫。

而其中，Agent基础设施里最核心，

莫过于"运行时"。

但运行时是地基，没有它，其他都建不起来。

想玩好运行时，有两个选择：

选择一：自己搭。

选择二：用别人的。

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/2081F3B9-6EC8-44C8-A8FE-1ADC00123D95.png)

（三）路线对比
-------

在系统设计里，"任务真正被执行的地方"，

就叫运行时。

写一个Agent framework不难。

GitHub上几百个framework项目，

大部分是一个人一个周末写出来的。

但写一个生产级的运行时极难。

当下，Agent是一个长程过程：

它要调工具，要存中间结果，

要根据反馈继续干，要维持多轮上下文，

要处理工具调用失败，要在出错时重试或回滚。

这些事全部发生在模型之外，

全部发生在运行时里。

Claude模型本身，

不知道你的文件系统长什么样，

不知道你之前那次工具调用返回了什么，

不知道这个session已经跑了6小时该不该继续。

这些状态全部由运行时维护。

我找了四个厂商，

分两条完全不同的运行时路线对比。

“自己搭”这个流派： 

Kimi Agent和Multica

“别人的”这个流派：

Anthropic的CMA和阿里云JVS Crew。

讲清楚它们，你就明白这一层赛道的格局了。

这两个流派，完全是两套语言。

一，Kimi Agent运行时：交给模型。

Kimi Agent不是一个独立的系统，

而是被训练进了模型的权重里，

模型本身就是一个多Agent编排器。

Kimi K2.6用新训练方法，

让模型学会自主把一个复杂任务，

拆解成300个并行子任务，

动态实例化子Agent去执行，最多协调4000步。

没有预定义的工作流，没有手写的编排框架，

完全由模型自己决定。

一个13小时的工作流，

通过swarm并行可压缩80%时间。

这是截至目前最激进的路线，

把别人写在框架里的编排逻辑，直接训进模型。

如果赢了，所有外置的Agent framework，

都失去存在理由。

官方文档链接：

https：//www.kimi.com/blog/kimi-k2-5

二，Multica的运行时：

为指挥别的Agent而设计。

Multica做的是多个Agent之上的一层，

一个团队调度层。

观察这个Agent，得从Multica的视角看，

Multica它不干活，只指挥。

它是"调度层"，不是"执行层"，

自己决定"这个任务派给谁"，

"几个Agent怎么协作"。

而Coding Agent，去写代码、

改文件、跑命令、调工具，是干活的。

意外的是，这些Coding Agent不是"用户入口"，是"后端"，

是执行任务的那块。

Multica赌的是，

一个开发团队未来会同时用多家厂商的Agent，

但缺一个统一的协作和调度层。

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/46B988C8-034E-4FA5-9EF8-0DC8FA5AAB73.jpg)

它的核心判断很硬，单个Agent已经够强了，

问题不在Agent能力，在协作开销。

十个Agent各自为战，

产出还不如三个能协作的Agent。

所以缺的不是更强的Agent，是协作基础设施。

官方文档链接：

https：//multica.ai

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/A48DA021-AE86-44E4-B089-4C19A8256BA3.png)![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/88CA13D6-5B00-4F13-BEB6-A8606C9CC339.jpg)

（四）企业的Agent痛点在哪？
----------------

这里有必要再强调下，

个人Agent和企业Agent的差距，

比猫和熊猫的差别还大，

除了Agent专业能力高超之外，

企业智能体天然还有几个要求，

规模化，稳定，安全可控。

公司有1000人，这1000个员工能不能同时用，

这要分布式基座，不是单机。

公司要有人担责，要看出问题谁负责、

怎么审计、能不能回溯，

这要全链路可观测和审计追溯。

公司最关心A部门数据不能被B部门看到，

这是要多租户的逻辑隔离+物理沙箱。

还有成本怎么核算、预算怎么管控、

超支怎么报警，

这要按使用量计费+配额管理。

上面几件事，手脑一体的本地架构都做不了。

我最看好的两个品牌，和我的想法很一致。

不怕说句得罪人的话，这种个人Agent的架构，

我不看好魔改，无论改龙虾，

还是改爱马仕（Hermes），

无论是头部厂商改，还是中腰部厂商魔改。

改不好的根本原因就是，

虽然运行时的部署是从本地电脑到云端都可以，

但是，选项再多也是给个人用的，服务一个用户。

企业要的是反过来：同时服务一千个员工，

每人一套独立环境，互不干扰。

这个需求翻译过来，在工程上，

就是一件事：运行时和环境彻底解耦。

不好改的原因是，那种个人Agent架构是一锅烩，

因为一锅烩就够了，没必要分开，

Agent怎么想、工具怎么调、

文件存哪里、出错怎么办，

全塞在一个进程里。一处改，处处要跟着动。

企业级Agent就不行，

需要重新规定它们怎么通信、

怎么协作、怎么互相不踩。

这种改法，改完之后，

原来的代码基本没什么能留下的。

工作量是从头写一遍的级别。

所以，最实在的一句话，

领导如果你是在喜欢龙虾，

又痛下决心改手脑分离，

不如让团队直接重写一套Agent infra，

让暴击来的直接点。

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/9372B20F-748B-4018-A984-E88CF486ED56.png)

（五）Anthropic的CMA和阿里云JVS Crew
----------------------------

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/BCB8C4D8-F97E-40E8-87B9-94813BC26D79.jpg)

一，CMA的运行时：把运行时本身做成API

Anthropic直接做一套生产级的，

拿出来卖。

它的方法是运行时被定义成，

一个标准化的API服务，

你调API创建一个Agent，

再调API创建一个Environment，

再调API启动Session，然后开始用。

中间所有的工程细节，你都不用管，

调API成了干活“前奏”，

运行时是个工程上极难做好的事。

每一项都是分布式系统的硬骨头。

让每个开发者自己造轮子，大部分人做不出来，

做出来也不安全、不稳。

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/09040E61-A487-4028-9F2F-6A8F27C3EDB1.jpg)

但是，你观察，CMA四大件里，

没有任何一个等于"运行时"，

如果非要从这四个里挑一个最像运行时的，

是Environment。

但严格说，Environment是运行时的"配置模板"，

真正在运行的是Session。

这正是Anthropic抽象水平高的地方，

直接叫"运行时"太粗了，会把这些事混在一起

于是，拆成了四个更精确的概念。

Anthropic赌"运行时会变成基础设施的标配API"。

另外，把OpenClaw改成CMA这种结构，

就是要把一锅烩拆成几层，

重新规定层间通信、层间状态、层间容错，

这件事的工作量，和重写一套Agent infra，

也是同一个级别的。

官方文档链接：

https：//platform.claude.com/docs/en/managed-Agents/overview

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/485A43BB-6F6E-47D0-8AE5-99F8220BF2BA.jpg)

二：JVS Crew的运行时：和环境隔离并解耦

JVS Crew是阿里云推出的，

企业级Agent量产基座，

我认为，国内最好的Agent infra，

或许没有之一。

这个东西也是我挖到的，

甚至拉一位CTO搞一篇测评，

毕竟，我在阿里还是能要到优惠劵的。

表面上，阿里云JVS Crew和CMA，

来路完全不同，

一个云大厂，一个模型公司：

但在架构设计上，有诸多共识。

其中最重要的是，

两边都选择把运行时和环境分开。

我认为，这不是偶然，

是企业级Agent基础设施的第一性原理，

被两条独立的路径同时验证。

或者换个角度，JVS Crew重点设计了两件事：

怎么算钱、怎么落地。

两件事都跪在手脑分离上。

第一，算钱：按使用量后付费，

席位制SaaS在Agent时代不灵了。

Agent用量和"员工在不在线"无关，

和"干了多少活"有关，

按席位算钱永远错配，

预付制采购流程两三个月，

估算错了又得重走。

JVS Crew按使用量后付费1积分=0.05元。

零门槛启动、秒级统计、月末出账。

模型推理，沙箱执行，外部API三类消耗，

分开计费清清楚楚。

第二，落地：权限和隔离

企业上Agent有两件事不解决就上不了线。

首先，权限不能出错。

Agent替张三干活时，

系统给它戴上张三的身份令牌，

它调任何工具，访问任何数据令牌，

一路跟着传，每一次都校验一次。

张三能干的它就能干，

张三不能干的一步都迈不出去。

其次，一个出问题不能连锁炸。

每一只手是独立的沙箱容器，

互相不通气、不可逃逸。

1000个Agent，一个Agent抽风，

平台层秒级把那个容器干掉，

其他999个Agent没感觉。

算钱、权限和隔离这三件事，

都跪在同一件事上——手脑分离。

脑、手、外部工具是三个独立层，

消耗才能分开计量，

身份才能层间传递，容器才能各自隔离。

手脑一体的架构里这三件物理上做不到。

其他能力——多租户、合规、可观测，

这是云向agent的自然延伸。

阿里云做了十几年接进Agent这层是顺带的。

官方链接：

https://help.aliyun.com/zh/jvs/getting-started/quickly-build-an-agent-using-jvs-crew-and-integrate-it-with-the-client?spm=a2c4g.11186623.help-menu-3028257.d\_1\_1.62e9771cW2qCoY

![](.evernote-content/2668747D-B39F-4D9A-9584-64D84A6539BE/720A9E64-5AB3-43EF-9DA8-E5F824EBA66C.png)

Agent大战，赢家暗自在Agent基础设施下功夫。

这设施一天不成熟，

产品公司就一天得自己搭，

运行时、做沙箱、写状态管理，

干本不该他们干的累活。

这层一旦成熟，产品层才能腾出手来，

干产品该干的事：

钻客户、搞行业、抠数据。

头部模型一下子攻不破。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw==&mid=2247492927&idx=1&sn=2af47928c4607429b5c89f80314115f8&chksm=fc1ef3dbcb697acd1d7096d418b4502e5402d3eb064ad3f4287aa7ec62b8f36ede84442379a7&exptype=timeline_unsubscribed_social_card&force_enter_love_page=1&req_id=1779345616279185&scene=90&ascene=56&devicetype=iOS26.5&version=1800492f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQXtig4LSK8iun6447HOIIkxLTAQIE97dBBAEAAAAAAOxtAbsHWrIAAAAOpnltbLcz9gKNyK89dVj0aQm7azKLfA17CAAR7+72npcEBJdnqK/LQPCJmcfVoDrFamaep4CLuy/kRx3tx8V3rtiQEdbSUBwUjN4sMJRHqvSgukmK3X5yiwQWasD70pL/taRFHO2RH76r+r94zILhHt2I9S11+ww+n7ohSsV09AJKWCR2BVGLNkw4lX2XAzhKmXatKHbfQvzOHCY5ih3FH12pEs5T8SKm7+9PiFuhtpZRwP9bcezueeJFmds=&pass_ticket=jbeCe2jaBOffqhxEcHe5n1y91Q9QmRvKpej1QFsY4oI89+hrZKMDqFeL9skgcCTB&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b4bb7374-8ceb-4dca-9e11-b7f0585212ec/b4bb7374-8ceb-4dca-9e11-b7f0585212ec/)