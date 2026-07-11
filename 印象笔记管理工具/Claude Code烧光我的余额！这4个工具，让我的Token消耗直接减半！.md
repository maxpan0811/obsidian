# Claude Code烧光我的余额！这4个工具，让我的Token消耗直接减半！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI1NzA2MjU0Nw==&mid=265084...](https://mp.weixin.qq.com/s?__biz=MzI1NzA2MjU0Nw==&mid=2650841636&idx=1&sn=7dba97def925644c336b47fe3e2bb971&chksm=f0e405a7e003004ecddddcbbe0471255852b477a03b08bf3791ce9de50853f83929275e4a0f8&scene=90&xtrack=1&req_id=1779855503926408&sessionid=1779855552&subscene=93&clicktime=1779855555&enterid=1779855555&flutter_pos=0&biz_enter_id=4&ranksessionid=1779855503&jumppath=1001_1779855546489,1102_1779855549381,1001_1779855551799,1104_1779855553236&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004934&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQlrmUzQDuYDXheA8Fe4U2SRLTAQIE97dBBAEAAAAAAFWlA0ITAHYAAAAOpnltbLcz9gKNyK89dVj08GqrzdL+aGveqfZpudDZITTVhpslwspJO+eoTyPR1Q77mbGboKVIbwvTIMG5r9MrSvRLJYxftlhG4lochliBmnPemFlSQlfsHC8BrMvGFOoerwNyu3z1RWwCSm1Yn1iBigJsXsbrKHkWjh9X2Y9ylAYQy5q7iVbIRqZTxaaJoLpYgCXT9IY05xNLTcVFDEQCQhk+1jIkjtFKtBwiGRjSj5jqdBsmSQfQvSWF388=&pass_ticket=p5GkFC3NqluZsgEKCZJeo0FzciMS5ijlHXRa0RJ6seuwZNfodnVzmawre3MGY1PZ&wx_header=3)

Original元小二2046 元小二学AI

你好，我是元小二，专注分享 AI 提效、一人公司实践和个人成长。这里有 OpenClaw、Claude Code、自动化流程、虚拟产品，也有理财、思考和生活系统。

欢迎关注，也欢迎后台留言告诉我，你对哪部分内容感兴趣。

朋友们，这篇写给每天靠Claude Code吃饭的人。

前几天，我一个做独立开发的朋友跟我说——

“小二，我Claude Code的费用已经超过我吃饭的钱了。”

我当时的第一反应是：你不会是在跟Claude聊家常吧？

但仔细一问，发现他的问题根本不是”问太多”，而是被一些根本没注意到的地方悄悄吃掉了。

比如跑一次测试，终端吐出几百行日志。

比如查一次Git状态，一堆分隔符、路径、无用提示信息全进了上下文。

比如接了Playwright、GitHub MCP、数据库MCP，工具一返回就是一大坨DOM、JSON、日志、表格。

Claude真正需要的可能只有那几行关键信息，但上下文里塞进去的，往往是一整包原始噪音。

**这才是Claude Code真正烧token的原因：它看得太多，很多还没必要。**

今天这篇，我就按场景介绍4个工具，帮你把Claude Code的上下文瘦下来。

---

一、RTK：终端输出太吵？用它一刀砍干净
--------------------

第一个工具叫 **RTK**，全名可以理解为 Rust Token Killer。

它解决的问题很具体：终端输出太嘈。

你在Claude Code里经常会让它跑这些命令：

cargo test
npm test
git statuspytestgrep / find / ls

这些命令本身没问题，但输出经常臃肿到离谱。

有时候Claude只是想知道测试失败在哪里，结果终端甩给它几百行进度条、路径、分隔符、无效状态。

我之前跑一个Rust项目的测试，Claude读了半天终端输出，结果把一个显眼的报错位置漏掉了。我重新描述了一遍需求，让它只看失败行，才顺利修完。

RTK就是把这件事自动化：

它夹在Claude Code和终端命令中间，把无效噪音过滤掉，只把更干净、更短的结果交给Claude。

项目方给出的测试数据是，**部分命令场景可以节省60%到90%的token。**

别把这个数字理解成所有项目都能省这么多，更准确地说——

如果你经常跑测试、查日志、查文件、跑Git命令，RTK会非常有用。尤其是 Go、Rust、Node、Python 这类项目，测试和构建输出一多，效果很容易感受到。

### 1. 安装方式

macOS 直接：

brew install rtk-ai/tap/rtkrtk init -g   # 初始化全局 hook

装完重启Claude Code，用 `rtk gain` 查看节省统计。

### 2. Windows 用户注意

如果你是Windows原生环境，hook体验可能没那么完整。建议先从几个高频命令手动试起：

rtk git statusrtk cargo test
rtk npm test

别一上来就期待完全无感，先跑几个命令感受一下再决定要不要深度配置。

---

二、Context Mode：MCP重度用户，这个才是你的菜
------------------------------

如果你只是用Claude Code改本地代码，RTK就已经够香了。

但如果你接了大量MCP工具——Playwright、GitHub、数据库、网页抓取、文件系统——那 **Context Mode** 更值得你优先关注。

它解决的问题是：**MCP工具返回的信息太大了。**

举个真实例子。

Playwright跑完一个页面操作，可能返回很长的DOM结构。

GitHub MCP查一个issue列表，可能返回一大坨JSON。

数据库工具查一次表，可能返回几百行原始数据。

这些内容直接怼进Claude上下文，会话窗口瞬间变肥，而且大量内容Claude根本用不上。

![](.evernote-content/4ADBD803-8FB6-452F-99F4-67572A90E8A9/DCD7F94E-BA21-43E5-9CDF-D5C0024E2612.png)

### 1. Context Mode的解法

把大体积工具输出先放进本地沙箱和SQLite数据库里，再给Claude一个压缩后的摘要。Claude后面真需要细节，再去检索。

它还用了SQLite FTS5全文索引和BM25排序，历史记录、工具输出、错误信息、文件编辑记录，都可以被重新搜索。

这对长会话特别有价值。

你肯定有过这种体验：前面聊得好好的，改了很多东西，后来上下文太长被压缩，Claude开始忘细节，乱改代码。

Context Mode想解决的就是这个。

项目方公布的基准测试里，**Playwright快照、GitHub issue列表、日志、CSV这类大体积输出，特定场景下可以压缩95%以上。**

### 2. 安装方式

走Claude Code插件市场，命令类似：

/plugin marketplace add mksglu/context-mode/plugin install context-mode@context-mode

安装前建议先看项目说明，确认你的Claude Code版本和插件市场配置没问题。

**如果你基本不用MCP，优先级可以放后面。如果你每天都让Claude Code操作网页、查GitHub、跑数据库，那Context Mode值得第一时间测。**

![](.evernote-content/4ADBD803-8FB6-452F-99F4-67572A90E8A9/A0400E27-16DA-4DE9-A9B1-593CAC038EA5.png)

---

三、Caveman Claude：最便宜最快见效，今天就能用
------------------------------

第三个工具很有意思，叫 **Caveman Claude**。

Caveman是”穴居人”的意思。

核心思路超级简单：**让Claude少说废话。**

你肯定见过Claude这种回复：

“好的，我理解你的需求了。接下来我将从几个方面帮你分析这个问题，并给出一个完整的方案……”

这种话听起来很礼貌，但在日常开发里，它就是纯纯的token浪费。

Caveman的做法是通过CLAUDE.md或Claude Code skill，直接告诉Claude：

* 少寒暄
* 少解释
* 少复述
* 少铺垫
* 直接给结果
* 优先工具调用
* 输出尽量短

项目方测试显示，它可以让**输出token平均减少约65%。**

我对Caveman Claude的评价是：**成本为零，立竿见影。**

你可以直接在项目的CLAUDE.md里加几条规则，今天下午就能感受到效果。

### 1. 适合什么人？

适合日常改Bug、跑命令、调小功能的人。

适合觉得Claude太啰嗦、只想要结果的人。

### 2. 一个重要提醒

别把Claude压得太死。

如果你在做复杂架构设计、方案权衡、技术选型，太短的回复会影响解释质量，到时候反而要反复追问，浪费更多token。

我的建议是——

日常修Bug、跑命令、改小功能：开Caveman风格。

复杂决策、重构设计、技术选型：别压太狠。

安装方式：终端直接运行👇

claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman

---

四、code-review-graph：代码库越大，它越值钱
------------------------------

第四个工具叫 **code-review-graph**。

它解决的问题和前面几个不一样。

前面几个主要压缩运行时输出。

code-review-graph关注的是：**别让Claude乱读代码。**

大型项目里，Claude经常会读一堆无关文件。

![](.evernote-content/4ADBD803-8FB6-452F-99F4-67572A90E8A9/DB12A7E8-5FB2-4D59-BF46-5C87F9592D31.png)

尤其是monorepo、后端服务、前端大仓库，一不小心就把上下文塞满，而且读的文件很多都和这次改动没关系。

### 1. 它怎么工作的？

它在本地构建代码知识图谱。

通过Tree-sitter解析代码结构，建立函数、类、模块、调用关系、依赖关系、测试覆盖等索引。

这样Claude做代码审查时，可以优先看和改动真正相关的文件，而不是漫无目的地乱读。

项目方公布的数据：**代码审查平均token减少约6.8倍，部分大型仓库最高达到49倍。**

### 2. 适合什么场景？

适合代码量超过几万行的项目。

适合大型monorepo。

适合经常让Claude Code做代码审查、影响范围分析、依赖追踪的人。

如果你只有一个几十个文件的小项目，先别急着上，RTK和Caveman就够了。

**只有当Claude动不动就读几十个无关文件时，code-review-graph才真正有价值。**

安装方式如下：

pip install code-review-graph
code-review-graph install --platform claude-code

---

五、怎么组合用？
--------

不用一口气全装，按你的实际场景选就行。

我建议的上手顺序是这样的：

**第一步，先用Caveman，今天就能减少废话输出。**

**第二步，装RTK，把终端噪音压干净。**

**第三步，如果你用MCP，再上Context Mode。**

**第四步，如果项目很大，再考虑code-review-graph。**

这样最稳，每步都能感受到效果，不会搞到最后不知道是哪个工具起作用。

---

六、几个通用好习惯，工具之外更重要
-----------------

工具装完，这几个习惯也值得养起来。

**第一，开工前先看上下文。**

Claude Code里用 `/context` 查看当前上下文情况。看到上下文已经很肥，就别继续往里塞大输出——新开一个会话吧。

**第二，一个任务结束就开新会话。**

不要让上一个任务的日志、报错、探索过程继续拖累下一个任务。旧会话是历史包袱，能甩就甩。

**第三，探索性工作尽量放子任务。**

让Claude试错、查资料、跑大量命令，别污染主会话。主会话负责决策和验收，子任务负责探索。

**第四，别把整仓库扔给Claude。**

先让它看目录结构，再让它判断需要读哪些文件。”少读无关文件”本身就是省token，而且效果比你想象的好。

**第五，敏感项目先看清楚权限。**

这些工具会接触命令输出、代码结构、MCP返回内容。公司项目、客户代码、私有仓库里使用前，要先看清楚许可证、数据是否本地处理、有没有遥测。

别为了省token，引入新的安全风险，那就得不偿失了。

---

七、最后说一句
-------

Claude Code烧token，很多时候不是因为你问太多。

更常见的原因是：终端输出太吵，MCP返回太大，历史上下文太肥，代码读取太散。

所以真正有效的优化思路也很清楚：**让Claude少看噪音，多看关键信息。**

Caveman Claude今天就能试。

RTK装完下午就能看到节省统计。

Context Mode适合MCP重度用户。

code-review-graph适合大型代码库。

如果你每天都在用Claude Code写代码，这几个工具值得认真测一轮——

不只是为了省那一点钱，更重要的是，让Claude的上下文更干净，回答更聚焦，长会话不再跑偏。

赶快去试试吧，我的朋友。

人生是一场无限游戏，乾坤未定，你我均是黑马。

---

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI1NzA2MjU0Nw==&mid=2650841636&idx=1&sn=7dba97def925644c336b47fe3e2bb971&chksm=f0e405a7e003004ecddddcbbe0471255852b477a03b08bf3791ce9de50853f83929275e4a0f8&scene=90&xtrack=1&req_id=1779855503926408&sessionid=1779855552&subscene=93&clicktime=1779855555&enterid=1779855555&flutter_pos=0&biz_enter_id=4&ranksessionid=1779855503&jumppath=1001_1779855546489,1102_1779855549381,1001_1779855551799,1104_1779855553236&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004934&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQlrmUzQDuYDXheA8Fe4U2SRLTAQIE97dBBAEAAAAAAFWlA0ITAHYAAAAOpnltbLcz9gKNyK89dVj08GqrzdL+aGveqfZpudDZITTVhpslwspJO+eoTyPR1Q77mbGboKVIbwvTIMG5r9MrSvRLJYxftlhG4lochliBmnPemFlSQlfsHC8BrMvGFOoerwNyu3z1RWwCSm1Yn1iBigJsXsbrKHkWjh9X2Y9ylAYQy5q7iVbIRqZTxaaJoLpYgCXT9IY05xNLTcVFDEQCQhk+1jIkjtFKtBwiGRjSj5jqdBsmSQfQvSWF388=&pass_ticket=p5GkFC3NqluZsgEKCZJeo0FzciMS5ijlHXRa0RJ6seuwZNfodnVzmawre3MGY1PZ&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3c5852ad-ddd9-4283-a670-2d9c612a4a37/3c5852ad-ddd9-4283-a670-2d9c612a4a37/)