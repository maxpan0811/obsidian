---
title: 刚刚 Claude Opus 4.8 发布，被实锤蒸馏了国产 DeepSeek 和千问？！附一手实测，夯还是拉？ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/刚刚 Claude Opus 4.8 发布，被实锤蒸馏了国产 DeepSeek 和千问？！附一手实测，夯还是拉？ 2.md
tags: [evernote, impression, yinxiang]
---

# 刚刚 Claude Opus 4.8 发布，被实锤蒸馏了国产 DeepSeek 和千问？！附一手实测，夯还是拉？

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI1NDczNTAwMA==&mid=224758...](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247587512&idx=1&sn=f65f1d4dfe76fca14976488e1064fc90&chksm=e889b3b3b2711ed77955e00e84febadbd5d3cf146a1e31e808f17f16cc9168fa413a7ad2b215&scene=90&xtrack=1&req_id=1780050954905528&sessionid=1780050949&subscene=93&clicktime=1780051548&enterid=1780051548&flutter_pos=4&biz_enter_id=4&ranksessionid=1780050954&jumppath=1001_1780050948168,1104_1780050949814,20020_1780050952226,1104_1780050960971&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbuofFja943nEv9vQLyiIGxLTAQIE97dBBAEAAAAAAOvwJMDz4JcAAAAOpnltbLcz9gKNyK89dVj0+61QutZHYSJg02Pa0mroxxdGwRPMLFD2iJYoN9S62nWf3Jvu1ADlB3rQHB/I6gD1+85S2UYhkkop76jP15eEQpEC99a9SEM8Na3H/SP+d4cfRbXVES8KG60jiK8XOmbKaslDdhR57y1eM91QRqXCjjjomI/Pl8wsEnj/ioMqrQx/MAmfEAcare+k3Zp/F/+uoBQjcfdYbsBVeLcgtTcnQp8OuYW0lDyvomPlE4o=&pass_ticket=Ol+/hQ2+iq685r55oLE8pkDLHf71AbwJTKqbVNntuf4QnZ9i+rM1hbKWER+qcBXu&wx_header=3)

Original程序员鱼皮 程序员鱼皮

大家好，我是程序员鱼皮。

刚刚 Anthropic 又发布了新模型 Claude Opus 4.8，从 2 月的 Opus 4.6 到 4 月的 Opus 4.7，短短 3 个月就迭代了 3 版！

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/1C08B26E-FF7E-4950-837D-9C5E0F0114D8.png)

每次大模型一更新，全网都在搬官方的跑分数据、翻译一下更新日志就完事了。

但跑分高不代表实际好用，我还是更想亲自测一测，哪怕已经发如雨下……

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/BA6C083B-A70D-4C4E-8D23-8C7184EDA49D.jpg)

正好最新的 Claude Opus 4.8 已经能在 Cursor 里用了，我干脆把 Opus 最近三代（4.6、4.7、4.8）和当红的 GPT-5.5 放到一起，用同一个提示词开发同一个全栈项目，看看到底谁最能打。

开始之前，先介绍一下本次 Opus 4.8 的更新，也请大家预测一下最终的测试结果~

Opus 4.8 更新了什么？
---------------

Opus 4.8 的定价和 Opus 4.7 一样，每百万 token 输入 5 美元、输出 25 美元，上下文依然是 100 万 tokens。

跑分这块本来我都懒得看了，反正 Opus 每次更新都是往上涨。不过和 GPT-5.5 的对比还是值得关注的，编程能力方面，SWE-bench Pro（Agent 编程能力）从 4.7 的 64.3% 提升到 69.2%，大幅领先 GPT-5.5 的 58.6%。不过在 Terminal-Bench 2.1（终端编程能力）上，GPT-5.5 以 78.2% 仍然领先 Opus 4.8 的 74.6%。

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/16405E6B-7DCE-4542-A15F-FBF3136DF924.png)

这次更新我觉得最值得关注的有 3 点：

1）动态工作流：Claude Code 里可以一次性派出几百个并行子 Agent，最多 16 个同时跑、单次上限 1000 个 Agent。适合大规模代码迁移这种硬骨头活儿。

不过大多数用户应该用不上这个功能，就好比你开了个公司，也没必要一次性雇几百个人，日常开发哪来这么大的迁移需求。

2）代码自查能力暴涨：官方说 Opus 4.8 漏检代码缺陷的概率比 4.7 降低了 4 倍。也就是说 AI 写完代码之后，自己就能发现更多 Bug，一把梭跑通的成功率更高了。

3）Fast Mode 大降价：Fast 模式可以让同样的模型处理速度翻倍，而且比之前的 Fast Mode 便宜 3 倍。

看数据是一方面，AI 编程模型好不好用，还是得拿真实项目来检验。

不过正式开测之前，先说个最近跟 Claude 有关的乐子。

有人发现用 Anthropic 官方 API（注意是 **官方 API**，不是中转站）直接调 Claude，中文问它「你是什么模型？」，它竟然一本正经地回答「我是通义千问」。据说换个问法，它还会说自己是 DeepSeek。

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/FA8E2A08-323F-40F2-A51D-597A11DB38C6.jpg)

我盲猜一个原因，API 调用没有像网页端那样的系统提示词来锚定身份，而中文互联网上「我是通义千问 / DeepSeek」的训练数据远比「我是 Claude」多得多。模型在没有身份提示的情况下，自然就输出了概率最高的那个回答。

不过也有可能，Claude 就是蒸馏了国产模型，好一个回旋镖~

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/03A604E3-9D6F-4AFE-AEBF-9601145A480E.jpg)

好了说回正题，这些顶级模型在实际编程中表现到底如何呢？

让 Cursor 自动并行测试
---------------

如果让你来做 4 个模型的编程能力对比，你会怎么做呢？手动一个一个跑么？

那也太累了，我选择直接让 AI 帮我测。

现在 Cursor 这类 AI 编程工具已经内置了「子 Agent」能力，可以并行启动多个独立的 AI 任务，而且每个任务可以指定用不同的模型。

相当于 Cursor 是一个包工头，我下一个指令，它就帮我同时调度 4 个不同的「工人」干活。

我只需要发一段提示词，Cursor 就自动帮我同时启动 4 个子 Agent，分别用 Opus 4.6、4.7、4.8 和 GPT-5.5，全部开到 High thinking 档位，用同一段提示词在各自的目录里开发同一个项目。

我让 AI 开发的项目是一个「TaskFlow 任务管理看板」全栈应用，类似简化版飞书看板，包含 7 个功能需求：用户注册登录、三列看板拖拽、任务增删改查、数据图表面板、搜索筛选、暗色 / 亮色主题切换、响应式设计。技术栈是 React + TypeScript 前端 + Python FastAPI 后端 + SQLite 数据库，前后端分离。

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/0F699DB8-67BC-4E5C-B142-35C44D1D54A7.png)

再次强调，4 个模型用的是完全一样的提示词，而且全程不做任何人工干预。我主要关注这几个指标：UI 设计水平、功能完成度、代码质量和架构合理性。

前端界面对比
------

先看登录页。

Opus 4.6 和 Opus 4.7 类似，都做了一个很干净的居中卡片式登录：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/8648FA37-E79C-4400-90F8-E6C51D63B0DA.png)

Opus 4.7 登录页

Opus 4.8 也差不多，但多了注册 / 登录 Tab 切换，还贴心地把演示账号密码直接标在了页面底部：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/920EA0F7-CC48-4AF6-8736-4EF1608A4A37.png)

Opus 4.8 登录页

GPT-5.5 的风格就完全变了，而且一看就是 GPT 的风格，左边一大块全是文案宣传，右边才是登录表单。符合我对 GPT 的刻板印象 —— 喜欢在页面上堆信息：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/DB7E02BF-9F80-4777-B193-A6393E723A0C.png)

GPT-5.5 登录页

登录之后，再来看任务看板页面。

Opus 4.6 的排版整齐，但没什么背景色，中规中矩吧：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/CD4D9211-C855-4287-8FAC-89118F05D6ED.png)

Opus 4.6 看板页

Opus 4.7 加了渐变背景色，列头有颜色区分，整体更优雅：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/4B4534EE-FCE8-4956-8464-EB232DC86044.png)

Opus 4.7 看板页

Opus 4.8 的看板跟 4.6 效果差不多，有点素：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/F520705A-FDBA-42A5-A927-F20611691729.png)

Opus 4.8 看板页

GPT-5.5 则直接把看板和数据面板合到了一个页面，上面是图表，下面是三列任务看板，用最少的页面完成最多的事。但是任务列的标题直接用了英文，细节上差了点儿意思。

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/FF59652F-C8C6-4683-BDF0-DBC1135465AD.png)

GPT-5.5 看板+数据面板

再来看看数据面板页面。

Opus 4.6 的数据面板比较简洁，三张图表排成一排，没有多余的装饰：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/5622E6A6-8F03-4134-944B-9C6114DF0238.png)

Opus 4.6 数据面板

Opus 4.7 的汇总卡片做了圆角渐变色图标，更生动了：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/03FF177D-5E6B-4EC6-A4CE-54E11D3FF1D1.png)

Opus 4.7 数据面板

Opus 4.8 的数据面板风格和 4.6 类似，不对，比 4.6 更朴素了：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/C561D5BA-E858-4464-81D3-E2F048AD8E40.png)

Opus 4.8 数据面板

再来看看深色模式，4 个模型的差距就更明显了。

Opus 4.6 的深色模式切换过来之后整体颜色还算协调，但背景和卡片的对比度偏低，看起来有点灰蒙蒙的：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/B9FF720F-29F5-467E-9EEA-F9480F4B10B7.png)

Opus 4.6 深色模式

Opus 4.7 的深色模式大不相同，渐变背景色在深色底色下显得更高级，卡片和图表的配色也很统一：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/E54758D2-D57C-4638-AB07-1A4038C4B48D.png)

Opus 4.7 深色模式

Opus 4.8 的深色模式中规中矩，没有什么惊喜，也没什么硬伤，和 4.6 比较接近：

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/4053C801-EDCB-48E0-8BF3-4B5AA2746B57.png)

Opus 4.8 深色模式

GPT-5.5 的深色模式风格有点儿像 Opus 4.6，也是一大片灰色，差点儿意思。。。

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/B7E7A98B-9C7B-4A97-95F9-92CEC12ADAFC.png)

GPT-5.5 深色模式

你们觉得谁最好看呢？

我个人投 Opus 4.7 一票，深色模式下那个渐变背景色真的很舒服。

功能实现对比
------

功能方面就不一一展示了，4 个模型全部实现了 7 个功能需求：注册登录、看板拖拽、任务管理、图表、搜索、主题切换、响应式，都能正常使用。

毕竟主流模型一把梭全栈项目已经不是什么新鲜事了，这些功能都不复杂，很难拉开区分度。

代码质量对比
------

既然功能都一样、UI 差异也是见仁见智，那真正能拉开差距的就是代码质量了。

我让 AI 帮我分析了 4 个项目的代码结构，还是能发现明显的区别的。

首先，4 个模型的项目结构出奇地一致，甚至连文件名都几乎一模一样。一方面应该是我提示词限定技术框架的原因，另一方面看来这些顶级模型的编程思路已经高度趋同了，大家都在往同一套最佳实践上靠拢。

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/11BBC7EA-A914-40C7-8086-0B400EEF1BFB.png)

看看生成的代码规模：

| 模型 | 源码文件数 | 代码行数 |
| --- | --- | --- |
| Opus 4.6 | 25 | 1,865 |
| Opus 4.7 | 32 | 2,259 |
| Opus 4.8 | 33 | 2,701 |
| GPT-5.5 | 13 | 1,221 |

显然，Opus 4.8 代码量最大，GPT-5.5 最精简。

但代码多不一定是好事，少也不代表差。关键还是看架构是否清晰、有没有明显的 Bug。下面逐个来看。

1）**Opus 4.7 的架构是最清晰的**

后端拆了 3 个 router（auth、tasks、stats），前端状态管理用独立的 store 文件，注册和登录分页面，有专门的 AppLayout 布局组件，axios 请求也做了集中封装。分层非常规整，拿去做团队项目也没问题。

2）**Opus 4.8 拆得最细**

有独立的 context 目录、FilterBar 组件、工具模块，代码量最大。另外 CORS 跨域配置直接配了 `allow_origins=["*"]`，安全意识差了点。

3）**GPT-5.5 走的是极简路线**

只用了 Opus 4.8 一半行数的代码就搞定了全部功能，但缺点是后端所有路由都写在 `main.py` 一个文件里，300 多行挤在一起。能跑是能跑，就是后面要改的话会比较头疼。

4）**Opus 4.6 功能完整，但有 2 个 Bug**

一个是缺少 React import 导致白屏，另一个是 Tailwind v4 的 CSS 层级冲突，说明 4.6 对最新框架版本的适配还不够。

综合排名
----

最终，这次测试下来 4 个模型的排名如下：

| 排名 | 模型 | 一句话评价 |
| --- | --- | --- |
| 🏅 1 | **Opus 4.7** | 架构最清晰，UI 最精致，代码零缺陷，开箱即用 |
| 🥈 2 | **Opus 4.8** | 代码量最大最详尽，但有 CORS 问题 |
| 🥉 3 | **GPT-5.5** | 1221 行极简通关，但后端单文件堆砌不利于维护 |
| 4 | **Opus 4.6** | 功能完整但有 2 个白屏 Bug，对新框架适配不足 |

看到这个结果，是不是有点意外？

最新的 Opus 4.8 竟然没拿第一，怕不是更新了个寂寞嘛？

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/0EFAFEC6-A46C-4F55-B457-05830979C7D6.png)

我的理解是，4.8 这次更新的重心不在「写更美观的代码」，而在 Agent 可靠性和长时间无人监督的任务执行上。动态工作流、代码自查能力这些特性，在大型项目和企业级场景里可能更有价值，但在「一把梭做个全栈项目」这种场景下，4.7 反而表现更稳。

**所以大家不要盲目追新，还是按自己的实际需求来选模型。**

时间有限，就先给大家分享这次测试。结合我自己的使用体感，我的建议是：

* 日常开发、一把梭小项目：选择 Opus 4.7 或 4.8 都行，4.7 的 UI 更好看，4.8 更省心（自查能力强）
* 终端操作、命令行自动化：选择 GPT-5.5，之前我做 Codex 教程的时候拿 GPT-5.5 用作办公 AI 还是很香的
* 大规模代码迁移重构：选择 Opus 4.8，它的动态工作流是杀手锏

而且我发现一个趋势，Opus 4.8 越来越像 GPT-5.5 了，都在朝着「用最务实的方式把活干完」的方向走，对 UI 美感之类的「额外加分项」反而不太上心。

不过我是真的不希望 Claude 继续朝着这个方向发展下去，大模型之间多搞些差异化，往不同的方向去强化各自的优势，给用户更多选择，我觉得才更好。

---

OK 就分享到这里，本文会收录到我免费开源的 [《AI 编程零基础入门教程》](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247581455&idx=2&sn=b7216da5331db54421750ccb5d051180&scene=21#wechat_redirect)，上千张图、几十万字，带你从 0 开始快速学会 AI 编程，做出自己的产品、跑通变现全流程，一次拿捏。

开源指路：https://github.com/liyupi/ai-guide

![](.evernote-content/C14CDAA4-CF30-4DAC-AB75-72102531B2DC/6C6BCB9B-8507-465E-B9A8-EAA7E920740E.png)

我是鱼皮，持续分享 AI 编程干货。觉得有用的话记得点赞收藏和关注~

也欢迎在评论区聊聊：你现在主力用哪个 AI 编程模型？有没有试过 Opus 4.8？

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247587512&idx=1&sn=f65f1d4dfe76fca14976488e1064fc90&chksm=e889b3b3b2711ed77955e00e84febadbd5d3cf146a1e31e808f17f16cc9168fa413a7ad2b215&scene=90&xtrack=1&req_id=1780050954905528&sessionid=1780050949&subscene=93&clicktime=1780051548&enterid=1780051548&flutter_pos=4&biz_enter_id=4&ranksessionid=1780050954&jumppath=1001_1780050948168,1104_1780050949814,20020_1780050952226,1104_1780050960971&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004935&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbuofFja943nEv9vQLyiIGxLTAQIE97dBBAEAAAAAAOvwJMDz4JcAAAAOpnltbLcz9gKNyK89dVj0+61QutZHYSJg02Pa0mroxxdGwRPMLFD2iJYoN9S62nWf3Jvu1ADlB3rQHB/I6gD1+85S2UYhkkop76jP15eEQpEC99a9SEM8Na3H/SP+d4cfRbXVES8KG60jiK8XOmbKaslDdhR57y1eM91QRqXCjjjomI/Pl8wsEnj/ioMqrQx/MAmfEAcare+k3Zp/F/+uoBQjcfdYbsBVeLcgtTcnQp8OuYW0lDyvomPlE4o=&pass_ticket=Ol+/hQ2+iq685r55oLE8pkDLHf71AbwJTKqbVNntuf4QnZ9i+rM1hbKWER+qcBXu&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3a014365-ae6e-4603-b30e-462250889854/3a014365-ae6e-4603-b30e-462250889854/)
