---
title: 别再跟AI反复强调你的要求了，一个文件永久解决 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/别再跟AI反复强调你的要求了，一个文件永久解决 2.md
tags: [evernote, impression, yinxiang]
---

# 别再跟AI反复强调你的要求了，一个文件永久解决

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk2NDc0MjIyMg==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzk2NDc0MjIyMg==&mid=2247484833&idx=1&sn=0667ae2dfd2d277d65ba3a96fef394bf&chksm=c5728b706f4cf24c7cc236dad73516da6e17c96e07e51412a92fd15b35456b9c9be26014da89&scene=90&xtrack=1&req_id=1779971012725734&sessionid=1779974457&subscene=272&clicktime=1779975356&enterid=1779975356&flutter_pos=33&biz_enter_id=4&ranksessionid=1779974744&jumppath=MMSnackBarWindowViewController_1779974737077,1104_1779974737937,20020_1779974743893,1104_1779974751621&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/F6Ues6gmVpaCCj8H+CdihLHAQIE97dBBAEAAAAAAP/sJQMF05oAAAAOpnltbLcz9gKNyK89dVj0HfEWlGneV3begYj/KaAIcXpraqhdhixXcjmKg7UXfa+FXn0/AYt3mjaiOwjzywcB1JM772snqsCz6rbZ26CWl+zAyR+WNp52YeFhkgYZUGfc8oYeIjVBKmzEoKfsv/QFq8S/pYsiu4F8VNK+7nCz50r3fHeMOAdjfdqafz9wAX/0HtIHuV8iszxsZ0qbzna8Kx/qQT3SRqD70mvNmmnd1sg=&pass_ticket=ofsPmqYxTeoZaRlt2dp+v051pa29MOFp1iqeyq4831jQuW2oRBzPGe/T+CJ8o5Hx&wx_header=3)

OriginalGeekTalkAI极客聊AI

上周GitHub Trending排行榜第一名不是一个AI模型，不是一个开发框架，甚至不是一个应用程序。

是一个Markdown文件的模板。

这个仓库叫**mattpocock/skills**，一周涨了1600多个Star。排名紧随其后的**everything-claude-code**，从第14名冲到第4名。它们都指向同一件事——越来越多的开发者发现，**AI编程效率的瓶颈不在模型能力，在你怎么告诉它你的规矩**。

这个规矩的载体，就是CLAUDE.md。

---

**CLAUDE.md到底是什么？**

简单说，它是一个放在项目根目录的Markdown文件，Claude Code在每次启动时会自动读取它。你在里面写的内容，相当于给AI一份**永久生效的工作手册**——项目的技术栈是什么、代码规范是什么、哪些文件不能碰、出错了先查哪里、提交代码要遵循什么格式。

没有CLAUDE.md的时候，你每次跟Claude Code对话都像在跟一个失忆的新同事合作——每个任务都要从头解释背景。CLAUDE.md的存在让这个同事变成了一个**记住了所有项目规矩的老员工**。

这个机制不是Claude独有的。OpenAI的Codex CLI读的是AGENTS.md，Cursor读的是.cursorrules。但底层逻辑完全一样：**把你对AI的反复叮嘱固化成一个文件，让它自动加载**。

---

**我踩过的三个大坑**

用CLAUDE.md的前两周，我犯了几乎所有新手都会犯的错误。

**坑一：写成了项目说明书。** 我把README里的内容搬了一半过来——项目简介、技术架构、依赖版本、部署流程。洋洋洒洒写了两千多字。结果呢？Claude Code的回答质量没有任何变化，因为这些信息它从代码结构和package.json里自己就能推断出来。你塞给它的不是指令，是噪音。

**坑二：写得太笼统。** 我写了一句**代码要符合团队规范**。这等于什么都没说。Claude不知道你的团队规范是什么——是用Tab还是空格？函数名用驼峰还是下划线？错误处理用try-catch还是返回错误码？笼统的指令只会得到笼统的输出。

**坑三：一次性把所有规则都塞进去。** CLAUDE.md写了五十多条规则，Claude Code开始出现诡异的行为——有时候遵守这条忽略那条，有时候两条规则冲突它自己选了一个你不想要的。上下文窗口是有限的，塞太多规则会导致模型的注意力被稀释。

这三个坑的共同根源是一个认知偏差：**CLAUDE.md不是一份写给人看的文档，是一份写给AI执行的指令集**。写法完全不同。

---

**7条黄金规则**

三个月下来，我摸索出一套确实有效的写法。不敢说最优，但至少比我之前的做法好了几个量级。

**规则一：只写AI猜不到的东西。** 项目用了React？Claude从package.json就知道了。TypeScript？从tsconfig.json就知道了。CLAUDE.md里不需要重复这些信息。你要写的是**AI从代码里推断不出来但你很在意的东西**——命名习惯的特殊偏好、错误处理的固定模式、某些目录的特殊用途、不允许动的文件清单。

**规则二：用祈使句，不用描述句。****我们的项目使用了统一的错误处理模式**是描述句，**所有业务异常必须抛出BizException，包含错误码和中文描述**是祈使句。前者告诉AI一个事实，后者给AI一条可执行的指令。差别是巨大的。

**规则三：给反例比给正例更有效。** 你写**函数要保持简短**，Claude不知道你的**短**是20行还是50行。但你写**禁止出现超过40行的函数，超过时必须拆分**，这条规则就变得可执行了。再加一句**错误示范：不要把数据查询、业务逻辑、结果组装写在同一个函数里**，效果更好。AI对**不要做什么**的理解远比**要做什么**清晰。

**规则四：控制在15条以内。** 每条规则都在消耗上下文窗口的注意力。规则越多，每条规则被遵守的概率越低。我的做法是把规则压到15条以内，按重要性排序——最重要的放最前面，因为模型对靠前内容的注意力更强。

**规则五：分层管理，用Skills处理专项任务。** 通用规则放CLAUDE.md，专项规则放Skills文件夹。比如代码审查的规范、提交信息的格式、特定模块的迁移注意事项——这些只在特定场景下才需要的规则，做成独立的Skill，Claude在检测到相关任务时自动加载。这样既不污染通用上下文，又能在需要时提供精确指令。

做过银行系统代码走查的人应该理解这个分层思路——通用编码规范是一层，业务安全规范是一层，特定模块的历史包袱注意事项又是一层。不可能把所有规范揉进一个文档里让人一次看完，AI也一样。

**规则六：定期修剪，删掉AI已经学会的规则。** 有些规则写进去两周后你会发现，即使删掉Claude也能做对——因为它已经从你的代码库中学到了这个模式。这时候果断删掉，把上下文空间让给更需要强调的规则。CLAUDE.md不是写一次就不管了的，它需要跟着你的项目一起演进。

**规则七：在CLAUDE.md最前面写一句话定义AI的角色。** 不是客套话，是真正有效的角色锚定。比如**你是一个熟悉Java 17和Spring Boot 3的后端工程师，当前项目是一个金融数据处理系统，所有修改必须考虑数据一致性和审计追溯性**。这一句话能让Claude后续所有回答的基调和侧重点发生根本性的变化。

---

**一个真实的效果对比**

上个月我用Claude Code做一个批处理模块的代码审查。没有CLAUDE.md的时候，AI给出的审查意见集中在代码风格和命名规范上——这些意见没错，但不是我关心的重点。

配置了CLAUDE.md之后，同样的代码，AI的审查意见变成了：**这个批处理步骤没有做幂等性检查，如果重试会导致数据重复插入**；**异常处理没有区分可重试异常和不可重试异常，会导致整个批次因为单条数据失败而全部回滚**；**日志里缺少批次号关联，出了问题无法快速定位到具体是哪一批数据出错**。

这些才是真正有价值的审查意见。区别不在于模型变聪明了，在于我通过CLAUDE.md告诉了它**这个系统最怕的事情是什么**。

---

**Skills系统：CLAUDE.md的进化形态**

CLAUDE.md解决的是**通用记忆**的问题，Skills解决的是**专项能力**的问题。

一个Skill就是一个文件夹，里面放一个SKILL.md和可选的辅助脚本。Claude在你下达任务时，根据SKILL.md的描述判断是否需要加载这个技能。加载是动态的——不相关的Skill不会浪费上下文空间。

这个设计跟操作系统的动态链接库思路是一样的——不是启动时把所有库加载进内存，而是运行时按需加载。在上下文窗口是稀缺资源的AI时代，这个设计决策非常聪明。

GitHub上现在已经有大量社区贡献的Skills——代码审查、commit规范、文档生成、测试用例编写、数据库迁移。你不需要从零开始写，找到一个接近你需求的Skill，改一改SKILL.md里的规则就能用。

---

写CLAUDE.md这件事本身就是一次有价值的思维训练。它强迫你把那些**你知道但从未明确表达过的项目规矩**用文字写下来——哪些文件不能动、出错时的排查顺序、代码审查最关注什么。这些隐性知识平时藏在老员工的脑子里，新人要花半年才能摸索出来。

CLAUDE.md把这些隐性知识变成了显性文档。AI能用，新人也能用。

从这个角度看，CLAUDE.md最大的价值可能不是让AI写出更好的代码，而是逼你把团队的隐性知识沉淀下来。AI是工具，但它附带推动了一件本该早做但一直没做的事。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk2NDc0MjIyMg==&mid=2247484833&idx=1&sn=0667ae2dfd2d277d65ba3a96fef394bf&chksm=c5728b706f4cf24c7cc236dad73516da6e17c96e07e51412a92fd15b35456b9c9be26014da89&scene=90&xtrack=1&req_id=1779971012725734&sessionid=1779974457&subscene=272&clicktime=1779975356&enterid=1779975356&flutter_pos=33&biz_enter_id=4&ranksessionid=1779974744&jumppath=MMSnackBarWindowViewController_1779974737077,1104_1779974737937,20020_1779974743893,1104_1779974751621&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/F6Ues6gmVpaCCj8H+CdihLHAQIE97dBBAEAAAAAAP/sJQMF05oAAAAOpnltbLcz9gKNyK89dVj0HfEWlGneV3begYj/KaAIcXpraqhdhixXcjmKg7UXfa+FXn0/AYt3mjaiOwjzywcB1JM772snqsCz6rbZ26CWl+zAyR+WNp52YeFhkgYZUGfc8oYeIjVBKmzEoKfsv/QFq8S/pYsiu4F8VNK+7nCz50r3fHeMOAdjfdqafz9wAX/0HtIHuV8iszxsZ0qbzna8Kx/qQT3SRqD70mvNmmnd1sg=&pass_ticket=ofsPmqYxTeoZaRlt2dp+v051pa29MOFp1iqeyq4831jQuW2oRBzPGe/T+CJ8o5Hx&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/144470f7-7e47-4960-9ace-cfd1c49b9487/144470f7-7e47-4960-9ace-cfd1c49b9487/)
