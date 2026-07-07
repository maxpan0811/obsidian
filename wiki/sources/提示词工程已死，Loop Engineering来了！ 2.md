---
title: 提示词工程已死，Loop Engineering来了！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/提示词工程已死，Loop Engineering来了！ 2.md
tags: [evernote, impression, yinxiang]
---

# 提示词工程已死，Loop Engineering来了！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIyNjM2MzQyNg==&mid=224772...](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723482&idx=1&sn=52522523fc778c878f71c1d9061535e3&chksm=e99d8dcb28c56142a0a1b409964970caa7f5d0a522dcd7639ebb8b6f16bb9185e5d7bba00910&scene=90&xtrack=1&req_id=1781481180240491&sessionid=1781481346&subscene=93&clicktime=1781481356&enterid=1781481356&flutter_pos=1&biz_enter_id=4&ranksessionid=1781481180&jumppath=1001_1781481329913,1104_1781481347188,20020_1781481349673,1104_1781481354016&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQHGH12cKK+CAMN1iy82FMkBLTAQIE97dBBAEAAAAAAFSgE67IwOMAAAAOpnltbLcz9gKNyK89dVj0V3nK4EEjV6kNwukHSwEhkjYXRzBjkTnCu1MdTprajM3qZD0I04xpoYoEDh9y9EM7tyl3hFgn0iN20KVW0ZcPgZK0mtzCnsznDyMIF263OZMwwPbj4fuF0CuqFkCq1TWxap1ItEWEecU6/ViepVhme55nedU0ay5Wxt7uAVHbLj2AyloSim3W3SHhbLoiUhVopaEu1fiZsw4l3ARS8f9rxvD1W628/tZ1U/ipafk=&pass_ticket=KGug9bo/3RHMfWuG8NGJzGBGKD8E4JW070IspUpc37oFkxathCquI9sNk5vZsunh&wx_header=3)

OriginalDatawhale Datawhale

 Datawhale干货 

**作者：Addy Osmani，谷歌云 AI 总监**

一个能帮你写代码的 AI，到底让活变轻松了，还是变难了?

大部分人第一反应是：这下轻松了。以前一行行敲代码，现在动动嘴；以前自己 debug，现在丢给 Agent。但谷歌云 AI 总监 Addy Osmani 最近一篇刷屏长文,结论正相反：想把这东西真用明白，比过去写提示词还难。

![](.evernote-content/D3FCF7CA-5389-4F29-A4E9-2BEEDF6926E6/275521C0-2BC9-4F78-A1E3-096EC6F0BB97.png)

他还打了个比方：你可以让自己当个全程在场的工程师，也可以当个只管按启动键的人。这种新的干活方式，AI 圈最近给它起了个名字：Loop Engineering，循环工程。

这件事的起点，是 Claude Code 负责人 Boris Cherny 说，自己现在基本不直接给 AI 下指令了，而是写好一个个 loop，让 loop 去驱动 AI。用他的原话说:「我的工作就是写循环。」

![](.evernote-content/D3FCF7CA-5389-4F29-A4E9-2BEEDF6926E6/BF4656A2-6FB9-4388-A573-83F8251D65B3.png)

一个大厂核心产品的负责人，说自己主要的工作就是写 loop；一个大厂 AI 总监，说这事比写提示词还难。

问题就来了：这个让一圈大佬都改了干活方式的 loop，到底是什么？它凭什么被说得这么重要，又难在哪？

### 一、从写提示词，到 Loop Engineering

先看看大家平时是怎么用 Agent 的。

你说一句，它做一点，你看一眼，不对再补一句，它再改，你再看。上下文不够，你还得重新交代背景、提醒它别动哪里。AI 是在干活，但一直盯着进度、一步步往前推的人，还是你。

所以那个阶段，大家最在意的是提示词怎么写：怎么把第一句话说得准、说得全。

但用久了会碰到另一个问题：真正花时间的，往往不是第一句提示词，而是后面那一长串重复动作。发现问题、拆任务、并行处理、回头检查、记录这轮做到哪、决定是继续还是交还给人。这些动作每天都在发生，加起来才是大头。

于是重点变了。以前是“怎么写一句好提示词”，现在变成“怎么把这一串反复发生的动作，设计成一个能自己转起来的 loop”。

这就是 Loop Engineering 想做的事。它把提示词定义成了一个零件，而真正决定结果的，变成了那个 loop。

二、Loop Engineering 到底是什么
------------------------

用一句不绕的话讲：Loop Engineering，就是你不再亲自一轮一轮指挥 Agent，而是把“发现问题、执行、检查、记录、继续下一步”这条链路，做成一个能自动运转的小系统。

重点不在“自动”，在“闭环”。

有人会把 loop 理解成定时跑个任务。定时只是开始。一个真正能用的 loop，至少要做到这几件事：它能自己启动，知道去哪找信息，做完一轮知道怎么检查结果，失败了知道要不要重试，每轮知道把进展记到哪，也知道什么时候该停下来交给人。

这本质还是一套工作流。

Addy 在原文里的说法是：loop 不是你去给 Agent 写提示词，而是你设计一个系统，让这个系统替你去写。人的位置往后退了一层，从执行者，变成了调度者。

三、一个完整的 loop 长什么样

Addy 把它拆成“五个积木，加一个记忆机制”。换成更直白的问法，一个 loop 得同时回答六个问题。

**第一，谁来把它叫醒？**不会自己启动的，不叫 loop，只能算“你手动点一次”。所以第一件事是调度：定时、按事件触发，或者跑到目标完成才停。比如每天扫一遍昨晚失败的 CI，每半小时看一次新 issue，测试不过就一直改。这一层决定的，是你在用工具，还是在运行系统。

**第二，多个 Agent 一起干活，怎么解决并行问题？** 只要并行，就迟早会出现改同一处文件、彼此覆盖的情况。所以要隔离。代码场景里这就是 worktree：给每个 Agent 一个独立工作空间，各改各的，最后再合并。没有隔离的并行，常常不是提效，而是批量制造冲突。

**第三，AI 怎么知道你们平时怎么干活？**这是 skill，或者说项目知识。模型每次开工，都很容易重新变回一个不熟悉你项目的新同事。所以得把知识写到外面：项目怎么启动、哪些目录别碰、命名规范是什么、踩过哪些坑。提示词是当场的临时指令，skill 是长期的固定规则。没有这层规则，loop 每转一圈都要重新认识你一遍。

**第四，它能不能碰到本地资料？**只能看本地文件的 Agent，还是半封闭的，它能给建议，但推不动真正的工作。有用的 loop 往往要接出去：issue 系统、数据库、CI、测试环境、PR、通知工具。这一步决定了 AI 是“说”还是“做”——是告诉你“这里可能有 bug，建议这么改”，还是直接开分支、跑测试、开 PR、关联工单，把结果丢进你的待审列表。

**第五，谁来检查它，进行结果的验收？**写代码的 Agent 往往高估自己的答案，它写完再问自己“行吗”，答案大概率是“行”。所以越来越多 loop 把执行和验证拆开：一个负责做，一个专门挑错，必要时换不同模型、不同视角来查。道理跟团队里那条老规矩一样——写代码的人，最好别自己给自己 review。在无人盯着的 loop 里，这条更要紧，因为它一旦犯错，会顺着 loop 越跑越远。

**第六，它怎么记住昨天做到哪了？**这是最不起眼、却几乎所有长期 loop 都离不开的部件：记忆。可能只是一个 markdown 文件、一张看板、一份外部记录，但它必须存在。Agent 最大的麻烦之一，是每次启动都太像重新来过：昨天验证过的结论今天再查一遍，上周否掉的方案这周又端上来。所以得有个对话之外的载体，记下做过什么、失败过什么、哪些已确认、哪些还得人来处理。Addy 在原文里有句话适合做总结：模型会忘，但仓库不会忘。

四、Loop Engineering 的成本和边界
-------------------------

Addy 原文里没有把 Loop Engineering 讲成一个无脑乐观的方案，他一直在提醒两件事：成本，和边界。

先说成本。loop 一旦跑起来，就不是问一次答一次的计费方式了。它会反复读上下文、反复试错、反复验证，有时还拉好几个 Agent 一起干，token 消耗可能非常大。如果任务不值得反复跑、没有稳定的反馈，或者只是一次性的小事，loop 很可能还没帮你省时间，先把成本烧光了。

再说边界。loop 能替你推进流程，但不能替你担责任。AI 说“完成了”，不等于真没问题；说“测试通过了”，也不等于业务逻辑对。一个没人盯着的 loop，也会没人盯着地犯错。还有一个更隐蔽的代价：AI 干得越多，人越容易不再去看过程，时间一长，代码越堆越多，自己真正理解的却越来越少。

所以 loop 的用法，从来不是把人拿掉，而是把人从重复劳动里抽出来，但把判断、验收和刹车这三样权力留在自己手里。

五、哪些工作适合用 loop
--------------

代码是 loop 最先爆发的地方，因为它天然有反馈：测试过没过、程序跑不跑、日志报不报错，都能直接验证。但把这个思路抽象一下，它适合的工作远不止编程。

比如内容选题。一个 loop 可以这样跑：每天定时去扫新闻源、X、博客、论文站，先挑出值得看的，补上来源、摘出核心观点、标出有争议的地方，资料不够的地方标红，最后把一份选题清单交给编辑。运营、研究、客服、产品分析也类似，很多流程都满足同一个条件：任务会重复、流程相对稳定、结果有一部分能检查。满足这几点，loop 就有落地空间。

写在最后：人和 AI 的协作方式已经升级
--------------------

把 Loop Engineering 当成一个新词，它很快会被下一个词替代。但它背后的人与 AI 的协作模式是很多大佬在思考的：当 AI 能够处理更长链路的任务时，人和 AI 的协作方式，也得从一轮一轮的对话，升级成一个能自己运转的闭环。

过去大家比的是谁的提示词写得好。接下来比的可能是谁的 loop 设计得好：怎么调度、怎么验证、怎么记录、什么时候该停。

回到开头 Addy 那句话：这件事不会让你的工作变简单，它只是把发力点挪了个位置。你可以选择做那个始终在场、清楚每一步在发生什么的工程师，也可以做那个只负责按下开始键、然后看着代码越堆越多的人。

***一起“******点赞******”三连****↓*

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247723482&idx=1&sn=52522523fc778c878f71c1d9061535e3&chksm=e99d8dcb28c56142a0a1b409964970caa7f5d0a522dcd7639ebb8b6f16bb9185e5d7bba00910&scene=90&xtrack=1&req_id=1781481180240491&sessionid=1781481346&subscene=93&clicktime=1781481356&enterid=1781481356&flutter_pos=1&biz_enter_id=4&ranksessionid=1781481180&jumppath=1001_1781481329913,1104_1781481347188,20020_1781481349673,1104_1781481354016&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQHGH12cKK+CAMN1iy82FMkBLTAQIE97dBBAEAAAAAAFSgE67IwOMAAAAOpnltbLcz9gKNyK89dVj0V3nK4EEjV6kNwukHSwEhkjYXRzBjkTnCu1MdTprajM3qZD0I04xpoYoEDh9y9EM7tyl3hFgn0iN20KVW0ZcPgZK0mtzCnsznDyMIF263OZMwwPbj4fuF0CuqFkCq1TWxap1ItEWEecU6/ViepVhme55nedU0ay5Wxt7uAVHbLj2AyloSim3W3SHhbLoiUhVopaEu1fiZsw4l3ARS8f9rxvD1W628/tZ1U/ipafk=&pass_ticket=KGug9bo/3RHMfWuG8NGJzGBGKD8E4JW070IspUpc37oFkxathCquI9sNk5vZsunh&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/306d63ca-2c54-42ab-8d0f-3440e1041e84/306d63ca-2c54-42ab-8d0f-3440e1041e84/)
