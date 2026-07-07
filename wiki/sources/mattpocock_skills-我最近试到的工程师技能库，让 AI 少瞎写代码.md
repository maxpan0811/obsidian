---
title: mattpocock_skills：我最近试到的工程师技能库，让 AI 少瞎写代码
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/mattpocock_skills：我最近试到的工程师技能库，让 AI 少瞎写代码.md
tags: [evernote, impression, yinxiang]
---

# mattpocock/skills：我最近试到的工程师技能库，让 AI 少瞎写代码

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c25b9e91f52c1787bbebc064af6e82f...](https://mp.weixin.qq.com/s?chksm=c25b9e91f52c1787bbebc064af6e82f3355559e81cd4e65df527759058b3813af1642934dee1&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782032740_2&req_id=1782031330553375&scene=169&mid=2247483740&sn=0b5445988e94da1b86065effd623b1b8&idx=1&__biz=MzkzMjQ5ODA4Mg==&sessionid=1782032739&subscene=200&clicktime=1782034343&enterid=1782034343&flutter_pos=20&biz_enter_id=5&jumppath=20020_1782034289272,1104_1782034305455,20020_1782034310435,1104_1782034341682&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQFOnr1NLiUw/4ljCjFqUxQRLTAQIE97dBBAEAAAAAACfGDxg1kCIAAAAOpnltbLcz9gKNyK89dVj0yt1cUkSK+K+tzk0igNoqaxLXaSHxEFBxgzXnZIb3zXiO+2a96pR8zgvskUCMwHqswXazbbTcokPvgIcgQ0hFHmpNxPc+oNgAQ0XCzGOeeA9bsufbUEgju3/mPXtRxwfxdZymyA/R7ynemhjVisBISlL1o39idJ+cOsA+/oF2H4b34ff0T/krbEQVqGcqXBFhOOgRd7aWYQ2cb9yAT8GGfRFwlfmoqHi8HZIpWyw=&pass_ticket=LWag0ZdyuBotQS8LHTG4sMFI64s6n0QMPUsWycM+bqAplWIT7bUt6IEuqP975v/i&wx_header=3)

mattpocock/skills：我最近试到的工程师技能库，让 AI 少瞎写代码
=========================================

Original吃瓜的小VVibe With Agents

最近我发现了一个非常好用的工程师 Skills 仓库:https://github.com/mattpocock/skills![](.evernote-content/655B51E2-E4AB-437C-A9E1-0CB10D992AEC/39169C58-C312-4550-AEED-705B82B5E369.png)

它不是那种“让 AI 表演一下十年架构师”的 Prompt 合集，而是一个围绕**开发设计、需求澄清、代码反馈、测试验证**组织起来的工程师技能库。

我最近在项目里试了一段时间，最大的感受是：它能明显减少 AI 瞎写代码的概率。甚至有些场景里，一个 Skill 顶得上我之前好几个 Skill 的组合。

这个仓库来自 Matt Pocock，仓库名也很直接：**Skills for Real Engineers**。

翻译得不那么客气一点就是：别整那些只会喊口号的 AI 咒语了，真正做工程，要靠流程、反馈、测试、设计和上下文。

我对它的第一印象是：这不像一个“技能大礼包”，更像一个老工程师把自己日常避免踩坑的方法，拆成了一套 AI 能执行的工作习惯。

它最打动我的地方，不是某个 Skill 看起来多炫，而是它非常克制：

* 每个 Skill 都很小；
* 每个 Skill 都解决一个具体失败模式；
* 不试图接管你的整个研发流程；
* 不把 AI 当魔法棒，而是把 AI 拉回工程常识。

如果你经常用 Claude Code、Codex、Cursor 这类 Coding Agent，你大概率遇到过这些问题：

* 需求没讲清楚，AI 做出来一个“看似对，其实偏了十万八千里”的东西；
* AI 输出太啰嗦，解释很多，但项目里的核心术语它并没有真正理解；
* 代码跑起来了，但测试不扎实，重构一次就开始漏水；
* Bug 修得很快，但修完以后你不知道它到底为什么坏；
* 项目越做越复杂，AI 写代码的速度变快了，屎山堆积速度也变快了。

mattpocock/skills解决的就是这些问题。

一句话概括：

**它不是让 Agent 写更多代码，而是让 Agent 按真正工程师的方式工作。**

---

先装起来：30 秒安装步骤
-------------

这个仓库的安装方式很简单，官方推荐通过 `skills.sh` 安装。

第一步，在终端执行：

```
npx skills@latest add mattpocock/skills
```

第二步，安装器会让你选择要安装哪些 Skills，以及安装到哪些 Coding Agent 上。

这里有一个重点：

**一定要选/setup-matt-pocock-skills。**

第三步，打开你的 Coding Agent，在项目里运行：

```
/setup-matt-pocock-skills
```

它会问你几个初始化问题：

```
你使用什么 Issue Tracker：GitHub、Linear，还是本地文件；

/triage

用哪些标签来表示

needs-info、

ready-for-agent 等状态；

PRD、ADR、

CONTEXT.md 这些项目文档要保存在哪里；

当前项目是单仓库单上下文，还是 monorepo / 多上下文。
```

配置完以后，就可以开始使用其它 Skills 了。

我的建议是：第一次不要贪多，先安装和使用这几个：

```
/setup-matt-pocock-skills

/grill-with-docs

/to-prd

/to-issues

tdd

diagnosing-bugs

domain-modeling

codebase-design
```

如果你的目标是“让 AI 不瞎写代码”，这几个已经能形成一条很完整的工程链路：

**先问清楚 → 再写 PRD → 再拆 Issue → 再用测试和调试反馈交付。**

这比一上来丢一句“帮我实现某某功能”要稳得多。

---

一、这个仓库的核心思想：小 Skill，可组合，保留人的控制权
-------------------------------

很多 AI 工程化方案喜欢做成“大流程”：

从需求到设计，从开发到测试，从发布到复盘，全都塞进一个超级系统里。

好处是看起来很完整，坏处也明显：一旦中间某一步偏了，你很难知道是哪里坏了。

Matt 这套 Skills 的思路相反：

**不要造一个巨大的 AI 研发机器，而是把工程师真正需要的能力拆成小而清楚的 Skill。**

它把 Skill 分成两类：

| 类型 | 谁来触发 | 作用 |
| --- | --- | --- |
| User-invoked | 人手动输入，比如 `/grill-with-docs` | 编排流程，启动一个明确任务 |
| Model-invoked | Agent 根据任务自动调用 | 提供通用纪律，比如 TDD、调试、领域建模 |

这个分类很关键。

有些能力必须由人来决定什么时候启动，比如“把这段讨论整理成 PRD”。  
有些能力则应该成为 Agent 的工作习惯，比如“调试前先构造反馈循环”。

前者是流程入口。  
后者是工程纪律。

这就像一个团队里：

* 产品经理决定什么时候立项；
* 工程师决定怎么测试；
* 技术负责人决定模块边界；
* QA 决定怎么复现问题。

而不是所有人抢一个键盘，对着代码一起念咒。

---

二、推荐工作流：从想法到可执行任务
-----------------

![](.evernote-content/655B51E2-E4AB-437C-A9E1-0CB10D992AEC/A3AB986E-787A-4937-A4BB-ECE1EFC26182.png)

如果你要用这套 Skills，我建议先理解它的主流程：

![](.evernote-content/655B51E2-E4AB-437C-A9E1-0CB10D992AEC/FB2EED44-4D7C-4C73-A9B9-637962F17D83.png)

这套流程的价值在于，它没有一上来就让 AI 写代码。

它先问：

* 你到底要什么？
* 项目里的术语叫什么？
* 哪些东西应该写进 `CONTEXT.md`？
* 哪些决策应该记成 ADR？
* 这个需求能不能拆成独立可交付的垂直切片？
* 每个切片是否能被测试验证？

这才是工程。

会写代码只是其中一环，甚至不是最难的一环。

---

三、Engineering Skills：主菜，真正写代码的人最该看
----------------------------------

![](.evernote-content/655B51E2-E4AB-437C-A9E1-0CB10D992AEC/6DC1C903-C130-47FF-85BE-DA220DE4D1EA.png)

### 1. /ask-matt：不知道用哪个 Skill？先问路

**定位**

**ask-matt** 是一个路由 Skill。它不直接帮你写功能，而是告诉你当前情况应该走哪条流程。

**适合场景**

* 你打开仓库，看到一堆 Skill，不知道先用哪个；
* 你有一个需求，但不知道该先问清楚、写 PRD、拆 Issue，还是直接实现；
* 团队刚引入 Skills，需要一个“入口导航”。

**实际效果**

它像一个经验丰富的工程负责人，先帮你判断：

* 这是一个新需求，应该从 `/grill-with-docs` 开始；
* 这是积压 Issue，应该先 `/triage`；
* 这是上下文太长，应该 `/handoff`；
* 这是代码架构变差，应该 `/improve-codebase-architecture`。

**直观例子**

你说：

“我要做一个订单退款功能，不知道应该直接让 Claude 写还是先整理需求。”

普通 AI 可能马上开始生成代码。  
`ask-matt` 的思路是：先进入 `/grill-with-docs`，把退款边界、订单状态、异常场景、领域术语都问清楚。

这就很像真实团队里，靠谱工程师不会听到“做退款”三个字就开始建表。

---

### 2./grill-with-docs：把需求拷问清楚，还顺手沉淀项目语言

**定位**

这是仓库里非常重要的 Skill。它会对你的计划或设计进行连续追问，同时结合 `domain-modeling`，把领域术语、关键决策写入项目文档。

**适合场景**

* 有代码仓库；
* 要做新功能或大改动；
* 需求里有很多含糊词，比如“状态”“账户”“可用”“完成”“取消”；
* 你希望 AI 不是只听你一句话，而是真的理解业务。

**实际效果**

它会逼你把需求讲清楚。

不是那种“请补充需求”的废话，而是沿着设计树追问：

* 这个状态能不能回退？
* 用户撤销和系统取消是不是同一个概念？
* 这个操作失败后，数据应该保持什么样？
* 这个术语在 `CONTEXT.md` 里已经有定义吗？
* 这次决策是否值得写成 ADR？

**场景例子**

你说：

“给课程系统加一个发布功能。”

它可能会追问：

* 发布是把草稿变成正式内容，还是把文件写入某个目录？
* 发布失败能否重试？
* 已发布内容能否撤回？
* 发布过程是同步还是异步？
* 用户看到的是发布结果，还是发布任务进度？

问完以后，AI 不只是知道“要做发布”，而是知道你们项目里“发布”这个词到底是什么意思。

这就是它厉害的地方。

---

### 3./triage：把混乱 Issue 变成 Agent 能接的工单

**定位**

`triage` 用来处理 Issue 或外部 PR，把它们放进一个清晰状态机：

* bug；
* enhancement；
* needs-triage；
* needs-info；
* ready-for-agent；
* ready-for-human；
* wontfix。

**适合场景**

* GitHub Issues 里堆了一堆 bug 和需求；
* 用户报错信息很散；
* 你想让 Agent 帮忙做，但 Issue 还不够清楚；
* 开源项目或团队项目需要一个“入口分诊台”。

**实际效果**

它不会看到 Issue 就上手改。

它会先：

* 读 Issue 正文和评论；
* 看标签和历史状态；
* 结合代码库验证问题是否存在；
* 判断是否已有类似实现；
* 如果信息不足，生成明确问题；
* 如果足够清楚，写出 Agent-ready brief。

**场景例子**

用户提了个 Issue：

“上传文件经常失败。”

普通处理方式可能是：开发先猜网络问题，再猜权限问题，再猜文件大小问题。

`triage` 的方式是：

* 先问失败文件类型、大小、浏览器、错误截图；
* 查代码里上传限制；
* 验证是否能复现；
* 如果复现不了，标记 `needs-info`；
* 如果复现了，写成 Agent 可以接手的修复 brief。

这就是“把抱怨变成工程任务”。

---

### 4. /improve-codebase-architecture：给屎山做体检，不是上来就重构

**定位**

这个 Skill 用来扫描代码库，找出架构摩擦点，并生成可视化 HTML 报告。它关注的是“deep module”：用小接口承载更多行为，让代码更容易测试、更容易被 Agent 理解。

**适合场景**

* 项目越来越难改；
* Agent 每次改代码都要绕很多文件；
* 测试不好写；
* 模块接口很大，但里面没多少真正行为；
* 你怀疑系统里有一堆浅模块、转发层、假抽象。

**实际效果**

它不是简单说：

“建议优化架构。”

而是会列出候选改造点：

* 涉及哪些文件；
* 当前问题是什么；
* 为什么它造成理解成本；
* 如何通过更深的模块改善 locality 和 leverage；
* 改完后测试会怎么变简单；
* 哪个候选最值得先做。

**场景例子**

一个订单校验逻辑分散在：

* Controller；
* Service；
* Repository；
* 前端表单；
* 定时任务；
* 测试 helper。

每次改规则都要全项目搜索。

这个 Skill 会引导你思考：是不是应该把“订单可提交性判断”做成一个深模块，把复杂规则藏在一个稳定接口后面？

注意，它不是为了“代码看起来更优雅”。  
它是为了让未来每一次修改都更便宜。

---

### 5. `/setup-matt-pocock-skills`：第一次使用前的项目配置

**定位**

这是初始化 Skill。它会配置当前仓库如何使用这套工程 Skills。

**适合场景**

* 第一次把这套 Skills 放进项目；
* 项目要明确 Issue 放哪里；
* 团队要确定 triage 标签怎么映射；
* 项目要确定 `CONTEXT.md` 和 ADR 的位置。

**实际效果**

它会引导你配置三件事：

* Issue tracker：GitHub、GitLab、本地 Markdown 或其他；
* Triage labels：哪些标签表示 `needs-info`、`ready-for-agent` 等状态；
* Domain docs：项目是单上下文，还是 monorepo 多上下文。

**场景例子**

你的项目用 GitHub Issues，但标签叫：

* `status: needs info`
* `status: ready for ai`
* `status: wontfix`

而不是仓库默认的标签名。

这个 Skill 会把映射记录下来，后续 `/triage` 和 `/to-issues` 才不会乱贴标签。

---

### 6. `/to-prd`：把已经聊清楚的内容整理成 PRD

**定位**

`to-prd` 不负责继续采访你。它的职责是把当前对话和代码理解综合成 PRD，并发布到 Issue tracker。

**适合场景**

* 已经通过一轮讨论把需求讲清楚；
* 想把临时对话沉淀成可追踪文档；
* 想让后续 Agent 根据 PRD 开工，而不是根据聊天记录猜。

**实际效果**

它会整理：

* Problem Statement；
* Solution；
* User Stories；
* Implementation Decisions；
* Testing Decisions；
* Out of Scope；
* Further Notes。

尤其重要的是，它会关注“测试 seam”。也就是说，功能应该通过哪个接口被验证。

**场景例子**

你和 Agent 聊了 40 分钟退款功能。  
如果直接让它写，后面很可能丢上下文。

`to-prd` 会把这 40 分钟整理成一个稳定文档。之后无论换哪个 Agent，都能从 PRD 接着干。

---

### 7. `/to-issues`：把 PRD 拆成真正可交付的垂直切片

**定位**

`to-issues` 把计划、规格或 PRD 拆成独立可领取的 Issue。它强调 tracer bullet，也就是垂直切片。

**适合场景**

* 功能太大，不能一次让 Agent 全做；
* 希望每个 Issue 都能独立验证；
* 多个 Agent 或多次会话并行推进；
* 不想按“先数据库、再接口、再前端”这种横切方式拆任务。

**实际效果**

它会把功能拆成端到端小闭环：

* 一个切片可能同时包含 schema、API、UI、测试；
* 每个切片完成后都能演示或验证；
* Issue 之间依赖清楚；
* 每个 Issue 都能被新的 Agent 会话独立接手。

**场景例子**

做“退款功能”时，不要拆成：

1. 建表；
2. 写接口；
3. 写页面；
4. 写测试。

更好的拆法可能是：

1. 支持后台查看可退款订单；
2. 支持提交单笔退款请求；
3. 支持退款失败后的错误展示；
4. 支持退款结果通知和审计记录。

每个都是用户能感知的完整路径。

这就是它比普通任务拆分强的地方。

---

### 8. `/prototype`：用可丢弃原型回答不确定问题

**定位**

`prototype` 的核心思想是：原型不是小号生产代码，而是用来回答问题的临时实验。

**适合场景**

* 状态机在脑子里绕不清；
* 业务逻辑有很多分支；
* UI 方案要看了才知道；
* 争论“这样行不行”已经超过 10 分钟。

**实际效果**

它会根据问题选择两种路线：

* 逻辑问题：做一个可运行的终端小程序；
* UI 问题：做几个差异明显的 UI 版本，能切换对比。

并且它明确要求：

* 原型从第一天就标记为可丢弃；
* 一个命令就能跑；
* 默认不做持久化；
* 不追求优雅；
* 问题回答完就删除或吸收到正式代码里。

**场景例子**

你不确定订单状态应该怎么流转：

`draft -> submitted -> paid -> cancelled -> refunded`

里面有撤销、部分退款、超时关闭等情况。

与其让 AI 直接写生产代码，不如先让它做一个终端状态机原型。你通过几个操作走一遍，就能看出规则是否合理。

这很工程师：用最便宜的东西回答最贵的问题。

---

### 9. `diagnosing-bugs`：调试前先构造反馈循环

**定位**

这是我非常喜欢的一个 Skill。它把调试拆成严谨流程：

复现 → 最小化 → 假设 → 探针 → 修复 → 回归测试 → 复盘。

**适合场景**

* Bug 很难复现；
* 性能突然变慢；
* 用户说“偶现”；
* AI 想直接猜原因；
* 开发已经看代码看麻了。

**实际效果**

它最重要的原则是：

**没有能变红的反馈循环，就不要开始猜。**

也就是说，你得先有一个命令、脚本、测试、curl、浏览器脚本或回放用例，能稳定触发这个 Bug。

然后再：

* 缩小复现范围；
* 生成 3 到 5 个可证伪假设；
* 每次只验证一个变量；
* 加带唯一前缀的临时日志；
* 修复后删除调试痕迹；
* 把正确原因写进提交说明或 PR。

**场景例子**

线上用户说：

“保存表单偶尔失败。”

坏的 Agent 会直接猜：

“可能是 token 过期，我来改一下鉴权。”

好的 Agent 会先做：

* 收集真实请求；
* 用 curl 或 Playwright 复现；
* 构造一个能失败的最小用例；
* 判断是前端重复提交、后端并发、数据库约束，还是超时重试；
* 最后把复现用例变成回归测试。

这就是职业调试和玄学调试的区别。

---

### 10. `tdd`：不是“先写一堆测试”，而是一条一条打穿

**定位**

`tdd` 用于测试驱动开发，但它反对一种常见误区：先把所有测试写完，再统一写实现。

它强调垂直切片：

一个测试 → 一个实现 → 再下一个测试。

**适合场景**

* 新功能；
* 修 Bug；
* 复杂业务逻辑；
* 希望测试能抗重构；
* 不想让 Agent 写一堆看似覆盖很高、其实没用的测试。

**实际效果**

它强调好测试应该验证行为，而不是实现细节。

好测试像规格说明：

“用户可以用有效购物车结账。”

坏测试像监控内部零件：

“某个私有函数被调用了三次。”

前者能承受重构。  
后者一改内部结构就炸。

**场景例子**

你要做优惠券功能。

坏的做法：

* 先写 20 个测试；
* 测各种函数名、参数、mock 调用；
* 再让 AI 填代码。

好的做法：

1. 先写“有效优惠券能抵扣订单金额”；
2. 写最小实现让它过；
3. 再写“过期优惠券不可用”；
4. 再写“优惠券不能重复使用”；
5. 最后在全绿后重构。

它让 AI 的开发过程有节奏，不是一路狂奔。

---

### 11. `domain-modeling`：让 AI 学会项目里的“人话”

**定位**

`domain-modeling` 用来建立和维护项目领域模型。它不是读 `CONTEXT.md`，而是主动更新项目里的领域语言。

**适合场景**

* 项目术语混乱；
* 同一个词在不同人嘴里含义不同；
* AI 经常把业务概念搞混；
* 新功能涉及关键领域概念；
* 你希望代码命名更贴近业务语言。

**实际效果**

它会做几件事：

* 挑战含糊词；
* 发现术语冲突；
* 用具体场景压测概念边界；
* 检查代码和口头描述是否一致；
* 把确定下来的术语写入 `CONTEXT.md`；
* 对重要决策谨慎写 ADR。

**场景例子**

你说：

“账号冻结后不能操作。”

它可能追问：

* 账号是 User，还是 Customer？
* 冻结是禁止登录，还是禁止交易？
* 管理员能否解冻？
* 冻结期间定时任务还能否扣费？

这些问题听起来麻烦，但比上线后发现“客服说的冻结”和“风控说的冻结”不是一个东西要便宜得多。

---

### 12. `codebase-design`：设计深模块，让代码对人和 AI 都更友好

**定位**

`codebase-design` 提供一套设计词汇，用来讨论模块、接口、seam、adapter、depth、locality、leverage。

**适合场景**

* 想设计或改造模块接口；
* 代码难测试；
* 模块太浅，只是转发；
* Agent 找不到合适修改点；
* 团队讨论架构时词汇混乱。

**实际效果**

它会让你关注一个核心问题：

**这个模块是否用较小的接口，承载了足够多的行为？**

深模块的好处是：

* 调用者学更少；
* 改动集中；
* 测试通过公共接口覆盖更多行为；
* Agent 更容易理解应该在哪里修改。

**场景例子**

你有一堆函数：

* `validateUserName`
* `validateUserEmail`
* `validateUserPhone`
* `validateUserAddress`
* `validateUserStatus`

每个地方都自己组合调用。

这可能是浅模块。  
更深的设计可能是提供一个 `validateCustomerProfile()`，把规则、顺序、错误聚合都藏进去。

这不是为了少写几个函数。  
这是为了让复杂度待在它该待的位置。

---

四、Productivity Skills：不只写代码，也管知识和会话
-----------------------------------

13. `/grill-me`：没有代码仓库时，也能把想法问清楚
--------------------------------

`grill-me` 是 `grill-with-docs` 的轻量版。区别是它不依赖代码仓库，也不写 `CONTEXT.md` 或 ADR。

适合：

* 写产品想法；
* 整理文章结构；
* 设计一个流程；
* 做一个还没进仓库的功能方案。

它的价值很朴素：

**在开干之前，把模糊变清楚。**

---

### 14. `/handoff`：把长对话交接给下一个 Agent

AI 会话最大的现实问题之一，是上下文会变长、变糊、变贵。

`handoff` 的作用是把当前会话压缩成一个交接文档，让新会话接着干。

它不是简单总结，而是会：

* 记录当前目标；
* 记录已经做出的决定；
* 引用已有 PRD、ADR、Issue、文件路径；
* 建议下一个 Agent 使用哪些 Skills；
* 避免重复写已经沉淀在其他文档里的内容；
* 删除敏感信息。

适合长任务、跨会话任务、需要换 Agent 接力的任务。

---

### 15. `/teach`：把当前目录变成一个长期学习空间

`teach` 很特别，它不是写代码，而是把当前目录当成一个教学工作区。

它会维护：

* `MISSION.md`：为什么要学；
* `RESOURCES.md`：可信资源；
* `lessons/*.html`：一节节课程；
* `reference/*.html`：速查资料；
* `learning-records/*.md`：学习记录。

它适合长期学习某个概念，比如：

* TypeScript 类型体操；
* TDD；
* DDD；
* React Server Components；
* AI Agent 工作流。

我喜欢它的原因是：它把“学习”也工程化了。

不是今天收藏一篇，明天忘掉一篇，而是有使命、有课程、有复习、有记录。

---

### 16. `/writing-great-skills`：教你怎么写一个好 Skill

如果你想自己写 Skill，这个一定要看。

它的核心观点是：

**Skill 的目标不是让输出完全固定，而是让过程稳定。**

它会讨论：

* model-invoked 和 user-invoked 的取舍；
* Skill 描述怎么写才容易触发；
* 哪些内容应该留在 `SKILL.md`；
* 哪些内容应该下放到外部参考；
* 如何避免重复、沉积、无效句子；
* 如何用更强的 leading word 稳定 Agent 行为。

场景例子：

你想写一个“上线检查 Skill”。

差的写法是：

“请认真检查代码质量，确保没有问题。”

好的写法是：

* 什么情况下触发；
* 第一步检查分支；
* 第二步检查测试；
* 第三步检查配置差异；
* 第四步检查回滚方案；
* 每一步的完成标准是什么；
* 哪些参考文件按需加载。

这就是 Prompt 和 Skill 的区别。

---

### 17. `grilling`：追问能力的底层发动机

`grilling` 是很多 Skill 背后的底层能力。

它做一件事：

**一题一题地追问，直到计划或设计的每个分支都被解决。**

注意，是一题一题，不是一口气扔给你 12 个问题。

这点非常重要。很多 AI 问需求时喜欢这样：

“请告诉我目标用户、业务流程、异常场景、权限规则、验收标准、技术栈、数据结构、接口形式……”

看完只想关电脑。

`grilling` 的思路更像一个会推进会议的工程师：

先问最关键的一个问题。  
等你回答后，再问下一个依赖这个答案的问题。

这才是真正的需求澄清。

---

五、Misc Skills：偏工具化，但很实用
-----------------------

18. `git-guardrails-claude-code`：先把危险 Git 命令拦住
----------------------------------------------

这个 Skill 用 Claude Code hooks 拦截危险 Git 命令，比如：

* `git push`
* `git reset --hard`
* `git clean -f`
* `git branch -D`
* `git checkout .`

适合：

* 担心 Agent 误删代码；
* 团队不希望 AI 自己推送；
* 想给 Claude Code 加一道本地安全阀。

这东西听起来朴素，但很现实。

AI 写代码可以快，删代码也可以很快。  
有些快，我们不一定承受得起。

---

### 19. `migrate-to-shoehorn`：把测试里的 TypeScript 断言迁移得更安全

这个 Skill 很具体：把测试文件里的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。

适合 TypeScript 测试里经常遇到这种问题：

* 测试只关心对象的一两个字段；
* 但类型要求你构造完整大对象；
* 于是到处写 `as Request` 或 `as unknown as Type`。

它会用：

* `fromPartial()` 处理部分对象；
* `fromAny()` 处理故意错误类型；
* `fromExact()` 强制完整对象。

这不是大众 Skill，但很 Matt Pocock：精准、实际、专治 TypeScript 测试里的小痛点。

---

### 20. `scaffold-exercises`：给课程和练习生成规范目录

这个 Skill 用于创建课程练习目录，比如：

* section；
* exercise；
* problem；
* solution；
* explainer；
* readme。

适合做教学内容、代码课程、训练营的人。

它的重点不是“生成文件夹”这么简单，而是保证结构能通过既定 lint 规则。

---

### 21. `setup-pre-commit`：给项目加提交前质量门禁

这个 Skill 会设置：

* Husky；
* lint-staged；
* Prettier；
* typecheck；
* test。

适合：

* 项目还没有 pre-commit；
* 团队想减少低级格式问题；
* 想让 AI 改代码后，在提交前自动跑一轮质量门禁。

这类工具不性感，但非常管用。

因为工程质量很多时候不是靠觉悟，而是靠门禁。

---

六、我最推荐优先学的 5 个 Skill
--------------------

如果你不想一次看完全部，我建议按这个顺序入手：

| 优先级 | Skill | 为什么先学 |
| --- | --- | --- |
| 1 | `/grill-with-docs` | 解决“AI 没听懂需求”的根问题 |
| 2 | `tdd` | 给 AI 稳定反馈，不让它闭眼写 |
| 3 | `diagnosing-bugs` | 修 Bug 前先建立可复现循环 |
| 4 | `domain-modeling` | 让 AI 学会项目里的业务语言 |
| 5 | `codebase-design` | 让代码对人和 Agent 都更容易维护 |

这 5 个连起来，其实就是一个很强的工程闭环：

![](.evernote-content/655B51E2-E4AB-437C-A9E1-0CB10D992AEC/45552232-5706-400C-9F14-732D3FEE09E5.png)

这不是“AI 代替工程师”。  
这是“AI 被工程师的工作方法约束住”。

---

七、给读者的一个真实场景：做一个“退款功能”
----------------------

假设你要做一个退款功能。

不用 Skills 的做法：

> “帮我做一个退款功能，前后端都写一下。”

AI 很开心，开始生成：

* refund 表；
* refund API；
* refund 页面；
* refund service；
* 一些看起来很努力的测试。

然后上线后你发现：

* 部分退款没考虑；
* 已关闭订单还能退款；
* 重复点击会生成两笔退款；
* 客服和财务对“退款成功”的定义不同；
* 测试全绿，但用户流程漏了一半。

用这套 Skills 的做法：

1. `/grill-with-docs`：先问清楚退款状态、角色、异常流程；
2. `domain-modeling`：把“退款请求”“退款完成”“退款失败”“冲正”等术语写进 `CONTEXT.md`；
3. `/prototype`：如果状态机复杂，先做一个可丢弃状态机原型；
4. `/to-prd`：把讨论整理成 PRD；
5. `/to-issues`：拆成端到端垂直切片；
6. `tdd`：每个切片一条行为一条行为打穿；
7. `diagnosing-bugs`：如果发现线上问题，先构造复现循环，再修；
8. `codebase-design`：如果发现退款逻辑散得到处都是，再考虑深模块改造。

你看，AI 还是那个 AI。

变化的是工作方式。

---

八、为什么我说它是真正工程师技能
----------------

因为这个仓库不断强调几个朴素但重要的工程原则：

* 需求要先对齐；
* 领域语言要沉淀；
* 反馈循环要够紧；
* 测试要验证行为；
* Bug 要先复现再修；
* 模块要有深度；
* 原型要可丢弃；
* 上下文要能交接；
* 危险操作要有护栏。

这些东西没有一个是 AI 时代才发明的。

恰恰相反，它们都是老派工程师早就知道的常识。

但 AI 让一个问题变得更严重：

**以前不懂工程，最多写得慢；现在不懂工程，AI 可以帮你更快地制造混乱。**

所以这类 Skills 的价值不是“让你少写 Prompt”。

真正价值是：

**把工程师的判断、节奏、反馈和边界，变成 Agent 可以反复执行的工作方式。**

---

结尾
--

如果你只把 Coding Agent 当成一个“代码生成器”，那你会很快进入一个状态：

看起来每天都在交付，实际上每天都在欠债。

`mattpocock/skills` 这类仓库提醒我们：

AI 编程不是把手从键盘上拿开。  
AI 编程是把真正重要的工程动作变得更明确、更稳定、更可复用。

说人话就是：

**别急着让 AI 干活，先教它怎么像个工程师一样干活。**

这才是 Skills 最值得分享的地方。

![](.evernote-content/655B51E2-E4AB-437C-A9E1-0CB10D992AEC/02918F1F-1DD0-4C2C-9712-1960581EBA84.png)

---

资料来源
----

* GitHub 仓库：  
  https://github.com/mattpocock/skills
* README：  
  https://raw.githubusercontent.com/mattpocock/skills/main/README.md
* Engineering Skills 示例：  
  https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/tdd/SKILL.md  
  https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/diagnosing-bugs/SKILL.md  
  https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/codebase-design/SKILL.md  
  https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/domain-modeling/SKILL.md

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c25b9e91f52c1787bbebc064af6e82f3355559e81cd4e65df527759058b3813af1642934dee1&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1782032740_2&req_id=1782031330553375&scene=169&mid=2247483740&sn=0b5445988e94da1b86065effd623b1b8&idx=1&__biz=MzkzMjQ5ODA4Mg==&sessionid=1782032739&subscene=200&clicktime=1782034343&enterid=1782034343&flutter_pos=20&biz_enter_id=5&jumppath=20020_1782034289272,1104_1782034305455,20020_1782034310435,1104_1782034341682&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQFOnr1NLiUw/4ljCjFqUxQRLTAQIE97dBBAEAAAAAACfGDxg1kCIAAAAOpnltbLcz9gKNyK89dVj0yt1cUkSK+K+tzk0igNoqaxLXaSHxEFBxgzXnZIb3zXiO+2a96pR8zgvskUCMwHqswXazbbTcokPvgIcgQ0hFHmpNxPc+oNgAQ0XCzGOeeA9bsufbUEgju3/mPXtRxwfxdZymyA/R7ynemhjVisBISlL1o39idJ+cOsA+/oF2H4b34ff0T/krbEQVqGcqXBFhOOgRd7aWYQ2cb9yAT8GGfRFwlfmoqHi8HZIpWyw=&pass_ticket=LWag0ZdyuBotQS8LHTG4sMFI64s6n0QMPUsWycM+bqAplWIT7bUt6IEuqP975v/i&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/506967d8-7cc6-4d48-99d1-e82fcb5fafae/506967d8-7cc6-4d48-99d1-e82fcb5fafae/)
