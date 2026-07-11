# Code is not cheap：Matt Pocock 给 vibe coder 的 5 条提醒

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0MTY4MjE4OA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=Mzk0MTY4MjE4OA==&mid=2247490889&idx=1&sn=d757f3ea2e31b7cbb90076729b1331aa&chksm=c3a7415351adade84ea2afadd9ed865b065dd27d922d14a86fac4cdadf57d1040f46397b0593&mpshare=1&scene=1&srcid=0428Esd8ry2ZlVrSTESNliyk&sharer_shareinfo=ebe799b54da745247ca8f9dcbe29d321&sharer_shareinfo_first=cee7be365afb89b74608c19844a48fd1&from=groupmessage&isappinstalled=0&clicktime=1777376816&enterid=1777376816&ascene=1&devicetype=iOS26.4.2&version=1800472d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQenNfRUN1tREs4lxsLsvm8BLpAQIE97dBBAEAAAAAANjhKh77c2gAAAAOpnltbLcz9gKNyK89dVj0U8Q4fibCDDevDDXSOyhz3HycOwG2nEnNnUo3sB2USW9wT0ACmwDE+fl9lGI5WuDCGI0SMozBaIDKRQmEH1W79yLrGH6M6IksEEyfCkNds6oDRFuzs0Uno0mHDOmNrKjw8NUWaq0w6OS1in5mO7muFrfOk888+dqqO30YZmF9gRpjFqaqPh3aTuz1+CB+CuduqZyomCCm/Cv2OLA/ju2THlJPMtuf9Q4A6RuTgttlyNZRT4chWSWmdyfbn7ATxZD2nHln&pass_ticket=F8DBv36XkWB6wQ1I+tRYNnDlalpPIKc7yh5I9j6ezZFD87dpOP1QJPO8rdB0LzsI&wx_header=3)

Original蔡荔蔡荔谈AI

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/3E866F81-35F1-460B-A1AE-1BFE51516187.png)

前几天 Matt Pocock 把自己在 AI Engineer Europe 上的演讲录像放到了 YouTube，标题叫 It Ain't Broke: Why Software Fundamentals Matter More Than Ever。五天时间，接近 30 万播放。

他想说的事情其实就一句：Code is not cheap。

过去一年开发者圈子流行另一种叙事——代码反正是 AI 生成的，写规格（spec）就行了，剩下交给 AI，Code is cheap。

Pocock 在伦敦那场会上系统地把这个判断翻了过来。但他不是在反对 vibe coding——他自己就在 AI Hero 教 Claude Code for Real Engineers，他的 GitHub 仓库 mattpocock/skills 现在有 32.4 k stars。

他要说的是：vibe coding 想做好，得先承认代码不便宜，然后回到软件工程基本功上。

如果你不认识 Matt Pocock：他是 Total TypeScript 的作者，前 Vercel 工程师。这场演讲他给 vibe coder 留下了 5 条很具体的实操建议，下面拆开讲。

一、 为什么"Specs to Code"会越跑越糟
==========================

Pocock 自己试过 Specs to Code 这种工作流——你只反复修改需求文档，每次让 AI 据此重新生成代码，自己不去手改代码本身。听起来很美，对吧？把程序员变成产品经理，AI 来兜底。他的实战记录是这样的：

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/B5F0D088-022C-4D5E-8DE4-87C6A3EF71A9.png)

Specs → Code → Worse Code → Even Worse Code → Garbage

为什么会这样？因为 AI 不在乎"软件熵增"——这是软件行业一个老观察：代码就像一栋老房子，每一次草率的修补都让它离倒塌更近一点。AI 没办法对抗这个倾向，反而在加速它。AI 写出来的代码能跑，但"能跑"和"好"是两回事。

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/09C38EFD-B4B8-4BFA-B682-B7544693D726.png)

Pocock 因此抛出三个判断，全部和"AI 让代码变廉价"叙事相反：

第一，Code is not cheap——代码不便宜。 第二，坏代码现在比以往任何时候都贵——它会让你的 AI 投入打水漂。 第三，好的代码库前所未有地重要。

这个逻辑链可能对 vibe coder 来说会难以接受。你以为你在用 AI 加速开发，实际上你在用 AI 加速积累技术债。

Armin Ronacher（Flask 作者）在同一场会议上的说法更狠：AI 工具骗你以为自己更高效了，但只是让你来不及思考——代码审查全靠"放行"，因为 AI 写代码的速度已经比人审的速度快了。

二、 AI 不是 bug，是放大器：6 种翻车场景
=========================

Pocock 把 AI 编程实战中的失败模式总结成 6 类：

1. 意图偏离（The AI didn't do what I want）。AI 没理解你真正想要的——但更深层的问题是，你自己也没完全想清楚自己想要什么。
2. 极度冗长（The AI is way too verbose）。AI 写出大段啰嗦、面面俱到、毫无锋利度的代码。
3. 代码失效（Code That Doesn't Work）。生成的代码根本跑不起来。
4. 过度执行（Doing way too much）。你让它修一个 bug，它顺手重构了三个模块。
5. 看不懂你的代码库（AI Doesn't Understand My Code）。架构混乱、模块零散，AI 在你的代码里迷路。
6. 认知过载（My Brain Hurts）。AI 倒了一堆代码给你，你 review 不过来，大脑罢工。

Pocock 的诊断戳到了痛点——这些不是 AI 的 bug，而是你自己软件工程实践的短板被 AI 放大了。需求模糊、没有共享语言、缺架构纪律，这些问题原本就在，AI 只是把它们暴露并加速了。

三、 5 条实操建议：人做战略家，AI 做执行官
========================

针对这 6 种翻车，Pocock 给出了 5 个实操建议，每一个背后都对应一个软件工程的经典思想。

3.1 Tip 1：写代码之前，先达成"共享设计概念"（Shared Design Concept）
--------------------------------------------------

这是他认为最重要的一条。具体方法是用一个叫 /grill-me 的 skills —— 意思是"拷问我"——让 AI 像面试官一样把你的设计思路从头到尾问一遍，每个分支、每个依赖关系都问到位，直到你和 AI 对要做什么有完全一致的理解。

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/9001A8D7-33E5-4118-8862-C2F5FB7F55AD.png)

他的原文是：Interview me relentlessly about every aspect of this plan until we reach a shared understanding.

为什么这一招比 AI 自带的"规划模式"强？因为规划模式是 AI 给你出方案，grill-me 是 AI 逼你把脑子里模糊的东西讲清楚。两者方向相反。

3.2 Tip 2：和 AI 建立"共享语言"（Ubiquitous Language）
--------------------------------------------

这是从领域驱动设计（Domain Driven Development）借来的概念。在你的代码库里维护一份术语表（一个 Markdown 文件就够），把业务里的核心词汇定义清楚——什么叫"客户"，什么叫"订单"，每个术语对应的边界是什么。AI 在思考和命名时会自动对齐到这套语言，沟通成本骤降。

3.3 Tip 3：强制 TDD（Test-Driven Development）
-----------------------------------------

这条对资深工程师不新鲜，但对 vibe coder 来说是当头一棒。Pocock 说 TDD 强迫 AI 小步快跑——你能验证多快，才能跑多快。测试是 AI 必须通过的硬约束，是 vibe coding 最缺的那个外部锚点。

3.4 Tip 4：深化模块架构，追求 Deep Modules
--------------------------------

这一条来自 John Ousterhout 的 A Philosophy of Software Design。他对比了两种代码组织形态：

* 浅模块：一堆碎小、相互依赖的文件，每个只做一点点事，AI 在里面找不到北。
* 深模块：简单的接口，藏在背后的复杂实现。

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/11548D0F-0D42-4BE8-9655-7A5BC03D4E37.png)

Pocock 指出，AI 特别擅长生成浅模块——它倾向于把一个功能拆成 N 个小文件。结果是你的代码库里全是零散、互相依赖的小块，AI 自己都看不懂自己写的代码。

修复方法是用他的 improve-codebase-architecture skill，让 AI 帮你把零散逻辑收拢到边界清晰的大模块里。

3.5 Tip 5：Design the interface, delegate the implementation
-----------------------------------------------------------

直译：设计接口，委托实现。这是整场 18 分钟演讲里我认为最值得记住的一句话——前面 4 个 Tip 都是手段，这一句是这套方法论的内核。

具体说就是：人类做战略家，AI 做战术执行官。你只专注在高层——这个模块该做什么、不该做什么、对外长什么样；具体怎么写交给 AI；最后用测试来验证 AI 写得对不对。

为什么这句话是精华？因为它一刀切清楚了人和 AI 的协作边界。前面 4 个 Tip——拷问设计、共享语言、强制 TDD、追求深模块——本质都是在为这个边界服务，保证人专注在"该自己想清楚的那一层"，不被 AI 拖进具体实现的泥潭。Pocock 引用 Kent Beck 在 Extreme Programming Explained 里的一句话作为整场收尾：

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/A8A78B76-3B57-41C4-AFB7-DD1C090D7A1D.png)

Invest in the design of the system every day.

每天为系统设计做投入——这是给 AI 时代工程师的最朴素一句话。

四、 一个 vibe coder 看完这场演讲该想什么
===========================

4.1 第一，"vibe coding"和"real engineering"正在加速分化
---------------------------------------------

过去半年大家把 Cursor、Claude Code、Codex 一股脑叫做 AI coding。但 Pocock 这一派开始明确划界：你是写一次性 prototype 的 vibe coder，还是在维护一个会活几年的代码库的 real engineer？前者怎么糙都行，后者必须有工程纪律。

Apple 在 4 月份送约 200 名 Siri 工程师去参加多周的 AI 编程训练营，是同一个信号——大厂已经意识到，问题不是"还要不要工程师"，而是"能不能把工程师和 AI 工具配合好"。

4.2 第二，Pocock 的 skills 仓库本身就是一个范本
---------------------------------

32.4 k stars 不是没有理由的——他把"先拷问设计"、"先写测试"、"重构成深模块"这些抽象方法论，全部封装成了一行 npx 就能装的 Claude Code skill。这是当前 Claude Code 生态里最值得抄的实践之一。

![](.evernote-content/CCE84F44-8EBD-4E2F-862C-795B56201C68/2EB9EB8C-F01D-44B2-9EAA-C1551E8D1EEC.png)

4.3 第三，最实用的一条不是 TDD，而是 Tip 1
----------------------------

TDD 和模块架构都有学习曲线，但 grill-me 这一招几乎零成本：让 AI 写代码之前，先逼它把你的需求拷问一遍。我自己做过一些项目复盘，代码出问题的地方，回溯下来很多都是 spec 阶段没想清楚——而这一步是源头。

4.4 第四，区分什么时候不需要这套
------------------

一次性脚本、demo、个人小项目，Pocock 这套你可以略过——杀鸡用牛刀。但只要你做的是会上线的产品、会有别人接手的代码库、会跑超过三个月的项目，工程纪律就不是可选项。最简起步动作就一个：在项目根目录建 CONTEXT.md，把业务领域核心术语写下来——Tip 2 的最简版，五分钟能做。

4.5 第五，这场演讲背后是一个更大的产业风向
-----------------------

这次 AI Engineer Europe 上，Pocock、Armin Ronacher、Mario Zechner（libGDX 作者）几个人不约而同在讲同一件事——AI agent 在加速积累技术债，开源项目被无意义的 AI 生成 PR 淹没，agent 写出的代码"能跑但没法维护"。这不是反 AI 派的怀旧，是工程师社区开始集体意识到：光有代码生成能力是不够的，必须配套工程纪律。

回到 Pocock 那句话：Code is not cheap。AI 没让代码变便宜，它让坏代码变得更贵。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0MTY4MjE4OA==&mid=2247490889&idx=1&sn=d757f3ea2e31b7cbb90076729b1331aa&chksm=c3a7415351adade84ea2afadd9ed865b065dd27d922d14a86fac4cdadf57d1040f46397b0593&mpshare=1&scene=1&srcid=0428Esd8ry2ZlVrSTESNliyk&sharer_shareinfo=ebe799b54da745247ca8f9dcbe29d321&sharer_shareinfo_first=cee7be365afb89b74608c19844a48fd1&from=groupmessage&isappinstalled=0&clicktime=1777376816&enterid=1777376816&ascene=1&devicetype=iOS26.4.2&version=1800472d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQenNfRUN1tREs4lxsLsvm8BLpAQIE97dBBAEAAAAAANjhKh77c2gAAAAOpnltbLcz9gKNyK89dVj0U8Q4fibCDDevDDXSOyhz3HycOwG2nEnNnUo3sB2USW9wT0ACmwDE+fl9lGI5WuDCGI0SMozBaIDKRQmEH1W79yLrGH6M6IksEEyfCkNds6oDRFuzs0Uno0mHDOmNrKjw8NUWaq0w6OS1in5mO7muFrfOk888+dqqO30YZmF9gRpjFqaqPh3aTuz1+CB+CuduqZyomCCm/Cv2OLA/ju2THlJPMtuf9Q4A6RuTgttlyNZRT4chWSWmdyfbn7ATxZD2nHln&pass_ticket=F8DBv36XkWB6wQ1I+tRYNnDlalpPIKc7yh5I9j6ezZFD87dpOP1QJPO8rdB0LzsI&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/87dd2924-c667-4a39-8d34-f637ef9841dd/87dd2924-c667-4a39-8d34-f637ef9841dd/)