# GitHub 11 万 star 的 Claude Code，5 个官方 Plugin 一行命令装完三件套（完整拆解）

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzYzMjY1OTI0MA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484527&idx=1&sn=868c6274ba480fe73b0c3e79d266bb2e&chksm=f147e3be5043d462997a51713ab66d943ddfd9cc6f1b5ede85b876f56ba0b3214de5bab9ee1b&scene=90&xtrack=1&req_id=1776482539380759&sessionid=1776482569&subscene=93&clicktime=1776482675&enterid=1776482675&flutter_pos=3&biz_enter_id=4&ranksessionid=1776482539&jumppath=20020_1776482579084,1104_1776482607447,20020_1776482612093,1104_1776482669079&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004724&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQSl454isKFaemgur8gf2M0RLBAQIE97dBBAEAAAAAAIY5Ay493m4AAAAOpnltbLcz9gKNyK89dVj04kWZUcgOFiQEdGKE3S66MBmJ58Xg6NfQUgzrqHqz18yIlCmGs2Y3uAwgjfbI/FLRKRdiiVnDGU8d7oAN0SRWiSFmewXdErKz9LHsuTe0Vlu0pprUuvuOXQf1dp2FGgn6U8U/cjI4kGoSkJkxujs2WTF+tz4RCF0b0Dh/wPG+HRcNv0/1bmlKijLOVyrHFhd2kWTTsYn69hlP6TA=&pass_ticket=IPLScXHga/mQ7CcyhE7uqmumsW2WsMVtd+gVX8kpbwoCY8zZr863k4bZZvubZtaF&wx_header=3)

Original莲花明 AI落地手记

上周我给一个新项目配 Claude Code。

先 clone 了 wshobson/agents 拿 5 个 subagent 扔到 `.claude/agents/`，然后翻 Hooks 文档配了 3 个触发器到 settings.json，再装 context7 / playwright 两个 MCP Server 到 `~/.claude/mcp.json`。

整整 2 小时过去，我看着这个新项目的 .claude 目录，突然意识到一件很蠢的事：

我这套配置在上一个项目里已经装过了，现在又手动重装一遍。

我有 20 个客户项目在并行推进。难道要在每个项目的 .claude 目录里手动重复同样的 subagent + hook + MCP 装配？

有人可能说，"你可以全放在 ~/.claude 全局目录"——对，但那只解决你自己一个人的问题。你团队里另一个同事要用同样的配置怎么办？把你整个家目录打包发给他？

那天晚上，我打开 Claude Code 敲了一行命令，发现这个问题 Anthropic 已经帮我解决了。

/plugin install feature-dev@claude-plugins-official

回车。0.5 秒后，整套特性开发流程的 subagent / hook / command 全部装完。切到下个项目？同一行命令。团队同事要用？把仓库名发给他就行。

这一篇是《Claude Code 扩展三件套》系列的收官。前三篇教你一块一块零件装，这一篇告诉你——官方已经把零件装成整机了，5 个官方整机，一行命令搞定。

---

01 / Plugin 到底是什么
-----------------

Plugin 是 Anthropic 在 Claude Code 2026-Q1 正式推出的机制，解决一个核心问题：

Subagents、Hooks、MCP、Commands、Skills 这五种扩展，怎么打包分发给别人？

以前的答案是"你自己 git clone + symlink + 改配置"，现在的答案是 `/plugin install`。

![](.evernote-content/3C9C22F0-CAC2-4239-8C8B-D6672E5E5090/FA80608D-97D4-4C4F-8730-185DC77D1CAC.jpg)

一句话：Plugin = 打包好的扩展集合。

一个 Plugin 可以同时包含：

若干个 subagent（专业员工）

若干个 hook（事件触发）

一份 .mcp.json（MCP Server 配置）

若干个斜杠命令

若干个 skill（新机制，Commands 的升级版）

默认设置 settings.json

后台监控 monitor

外壳是一个 `.claude-plugin/plugin.json` 清单文件，声明这个 Plugin 叫什么、版本多少、作者是谁。

Marketplace 机制是上面一层——一个 Git 仓库里放 N 个 Plugin，带一份 marketplace.json 清单，用户用 `/plugin marketplace add <repo>` 订阅整个仓库，再用 `/plugin install <name>@<marketplace>` 按需装单个 Plugin。

Anthropic 自己运营了一个官方 Marketplace：`anthropics/claude-plugins-official`，目前 17.2k star。

里面 80+ 个 Plugin，其中 19 个是 Anthropic 官方自建，60+ 个是合作伙伴（GitHub / Google Chrome / Microsoft / MongoDB / Figma / Notion / Linear / Cloudflare / Firebase / AWS / Vercel / Stripe ...）。

这个 marketplace 默认就在 Claude Code 里，打开 /plugin 菜单就能看到。

---

02 / 5 个 Plugin TL;DR（先看这张表）
----------------------------

下面 5 个我都在真实项目里用过一周以上，按"覆盖场景先后"排序：

#1**feature-dev（Anthropic 官方）**⭐ 17.2k

*完整特性开发工作流。内含 code-architect / code-explorer / code-reviewer 三个 subagent 协作，从需求分析到实现再到审查全覆盖。*

#2**code-review（Anthropic 官方）**⭐ 17.2k

*专做 PR / 代码审查的多智能体。调度多个 subagent 分工审查（架构 / 安全 / 可维护性 / 测试覆盖），避免主 Claude 过于"温柔"。*

#3**chrome-devtools-mcp（Google Chrome 官方）**⭐ 官方认证

*让 AI 直接控制 Chrome 浏览器。查看网络请求、控制台错误、调试 live 页面，前端开发者必装。*

#4**context7（Upstash 官方）**⭐ 52.7k

*防 LLM 幻觉神器。一句 "use context7" 实时拉任意库的最新官方文档注入上下文，版本号精准匹配。*

#5**github（GitHub 官方 MCP）**⭐ 官方认证

*直接跟 GitHub 平台对话。创 issue、开 PR、跑 actions、查代码——你在 Claude Code 里就能把 GitHub 的事全干完。*

背后数据：Claude Code 本体 115k star，官方 Plugin 目录 17.2k star，整个生态 80+ 官方认证 Plugin + 9000+ 社区 Plugin。

---

03 / #1 feature-dev（Anthropic 官方）
---------------------------------

Anthropic 工程团队自己用来开发新特性的标准工作流，现在开源给所有人。

它的特别之处在于——不是一个 subagent 干所有活，是三个 subagent 接力：

**code-explorer** — 第一步，分析现有代码库。追踪调用链、识别架构模式、记录文件依赖。相当于你让一个资深工程师先帮你 code reading。

**code-architect** — 第二步，基于 code-explorer 的分析，给出具体实现蓝图。说清楚改哪些文件、组件怎么设计、数据流向哪。相当于架构师出图纸。

**code-reviewer** — 第三步，实现完后自动做高置信度代码审查。只报真正重要的 bug / 漏洞 / 质量问题，不给你刷"代码写得真好"的废话。

三个 subagent 之间有明确的职责边界，上下游数据流也是预设好的。你一条 /feature-dev 触发，三个接力跑完，你拿到的是"分析 → 设计 → 实现 → 审查"的完整成果。

实测：一个中等复杂度特性（增加一个数据筛选面板），手写大概 3 小时，用这个 Plugin 跑下来 45 分钟，代码质量反而更稳定。

安装：

/plugin marketplace add anthropics/claude-plugins-official
/plugin install feature-dev@claude-plugins-official

两条命令，完事。

---

04 / #2 code-review（Anthropic 官方）
---------------------------------

如果说 feature-dev 是"从零开发一个新特性"，code-review 就是"把现有 PR 审严"。

痛点：你直接让 Claude 审你自己写的代码，它会"你写得真好"。

为什么？因为 Claude 的默认角色是 assistant（助手），不是 critic（评审员）。它倾向讨好你。你问"这段代码有问题吗"，它会先夸两句再挑几个小毛病，真正的大问题反而容易忽略。

code-review Plugin 把 subagent 伪装成"挑刺的同事"。内部调度多个角色：

一个 subagent 专盯架构合理性

一个 subagent 专盯安全漏洞（SQL 注入 / XSS / 权限绕过）

一个 subagent 专盯测试覆盖度

一个 subagent 专盯可维护性（命名 / 重复 / 复杂度）

每个 subagent 有自己独立的审查系统提示，不会互相影响。最后调度 agent 汇总所有审查意见，分优先级给你。

我 commit 前必跑 /code-review。有一次我写了一段看起来完全没问题的 API，安全 subagent 给我标出来："这里把用户 ID 放在 URL query 参数里，容易被第三方 CDN 缓存。"——这种问题我自己看 10 遍都看不出来。

---

05 / #3 chrome-devtools-mcp（Google Chrome 官方）
---------------------------------------------

Plugin 可以打包 MCP Server，这一个就是——Google Chrome 开发团队官方出品，把 Chrome DevTools 的能力直接开放给 AI。

效果：AI 可以直接"看见"你的浏览器。

以前你让 AI 帮你调前端 bug，对话大概是这样：

你：页面加载出错了，报错信息我发你。

你：（手动复制 console error）

你：（手动截图网络请求）

你：（手动粘贴 HTML 结构）

**AI：根据你发的信息，应该是 xxx**

现在呢：

你：页面加载出错了，打开 chrome-devtools-mcp 连接我本地 Chrome 看一下。

AI：（自己调 chrome-devtools-mcp，读 console / network / DOM / performance 全部数据）

**AI：看到了，是第 3 个 XHR 请求因为跨域预检失败触发了 retry 循环，导致主线程阻塞。修法是 ...**

前端工程师、全栈工程师、QA——这个 Plugin 装上就回不去。后端如果不碰浏览器可以跳过。

---

06 / #4 context7（Upstash 官方）
----------------------------

这个 Plugin 在 MCP 那一篇我专门拆过。放进 Plugin 系列里，是因为 Upstash 官方把它打包成了 Plugin，装起来从"改 MCP 配置"简化为"/plugin install"。

它解决的问题：Claude 的训练数据永远过时。

你让 Claude 写 Next.js 15 的代码，它可能给你 Next.js 13 的写法。你让它写 React 19，它可能给你 React 18。每次你都要手动贴最新文档，像伺候一个失忆的老板。

context7 让 Claude 自动去调外部文档服务：

你问库相关的问题时末尾加一句 "use context7"

它会实时从该库官方文档拉最新内容注入上下文

版本号精准匹配，你说 React 19 就拉 19，不会混 18

效果：库相关代码的幻觉率下降 80% 以上。

**为什么放第 4 位而不是第 1？**因为它是单一功能 Plugin（"让 Claude 查文档"），feature-dev / code-review 是多 subagent 编排 Plugin。后者对"一个人管多项目"的价值感更强，所以排在前面。但 context7 是所有 Claude Code 用户都该装的那一个。

---

07 / #5 github（GitHub 官方 MCP）
-----------------------------

GitHub 官方维护的 MCP Plugin，把 GitHub 的核心操作全开放给 Claude Code。

一句话：你可以在 Claude Code 里做 GitHub 网页版能做的几乎所有事。

具体能力：

读 / 搜 / 改仓库文件

创 / 看 / 关 issue

创 / 看 / 审 / 合 PR

查 / 触发 / 看 GitHub Actions 运行状态

管理 labels / milestones / projects

读 release / tag / commit 历史

日常用得最频的场景：

**提交 PR 后让 Claude 直接看 Actions 日志**——以前要切浏览器窗口，现在让 Claude 读 workflow 最新一次运行的失败 job。

**客户反馈新 bug**——"帮我在 repo-X 创 issue，标题是 xxx，贴这段报错上去，label 加 bug 和 p1"，一句话 3 秒搞定。

**跨仓库查历史**——"搜我们所有仓库里涉及 JWT 认证的代码，我要统一重构"，以前自己写 GitHub API 脚本，现在一句话搞定。

需要你在 GitHub 生成一个 Personal Access Token 做鉴权，配一次永久生效。

---

08 / 5 个 Plugin 一张对比表
---------------------

| Plugin | 归属 | 核心场景 | 内部打包 | 我的建议 |
| --- | --- | --- | --- | --- |
| feature-dev | Anthropic 官方 | 特性开发 | 3 subagent + commands | 必装 |
| code-review | Anthropic 官方 | 代码审查 | 多 subagent 编排 | 必装 |
| chrome-devtools-mcp | Google Chrome 官方 | 前端调试 | MCP Server | 前端必装 |
| context7 | Upstash 官方 | 防幻觉查文档 | MCP Server | 必装 |
| github | GitHub 官方 | Git 托管集成 | MCP Server + commands | 必装 |

---

09 / 我的判断：哪 3 个今晚就装
-------------------

如果你只有 5 分钟，装这 3 个，按顺序。

### 第 1 个：context7

所有人都该装。只要你写代码，每天省下来的"查库文档"时间都够 Plugin 安装成本的 100 倍。一句 "use context7"，Claude 就从"失忆的老板"变成"昨天刚读过官方文档的同事"。

### 第 2 个：github

只要你代码放在 GitHub，就装。PR / Actions / Issues 三件事每天都要做。省下的切窗口时间很快回本。有 Personal Access Token 的配置成本，一次 5 分钟，永久收益。

### 第 3 个：code-review

只要你 commit 代码，就装。它会用"挑刺"的角色审你自己写的东西，不会像默认 Claude 一样捧你。Anthropic 官方多 agent 编排，审查质量稳定在 senior reviewer 水平。

**剩下 2 个怎么办：**

**feature-dev**：前 3 个装完之后，想试"全自动开发特性"再装。适合复杂项目。

**chrome-devtools-mcp**：前端开发者装，后端跳过。

---

10 / 怎么开始
---------

Claude Code 装 Plugin 的标准 3 步：

**①** 启动 Claude Code（需要较新版本，老版本 /plugin 命令没有，先升级）

**②** 订阅官方 marketplace（只需一次）：

/plugin marketplace add anthropics/claude-plugins-official

**③** 按需装单个 Plugin：

/plugin install context7@claude-plugins-official
/plugin install github@claude-plugins-official
/plugin install code-review@claude-plugins-official

装完 `/plugin` 菜单里就能看到已启用的 Plugin 列表，`/reload-plugins` 热更新，不用重启。

进阶：团队想共享一套 Plugin 怎么办？

建一个内部 marketplace 仓库（Git 仓库根目录放一份 `.claude-plugin/marketplace.json`），把你们常用的 Plugin 列在里面，团队所有人 `/plugin marketplace add your-org/your-marketplace`，之后团队的新 Plugin 自动推给所有人。

这是 Plugin 机制最强的地方——它不是给你一个人用的工具，是给整个团队共享的基础设施。

---

一句话总结
-----

Subagents / Hooks / MCP 是零件。Plugin 是把零件装成整机的封装机制。以前 Claude Code 的扩展是"手工作坊"，现在是"标准化工厂 + 官方质检 + 一键出厂"。

这意味着什么？意味着你再也不需要每开一个项目就重新组装一次——你只要订阅一份 marketplace，你的 AI 团队可以秒速复制到任何新项目。

这是《Claude Code 扩展三件套》系列的最后一篇，也是收官：

4/13：Subagents（让 AI 分身）

4/15：Hooks（让 AI 自动触发）

4/16：MCP（让 AI 连上世界）

4/18（今天）：Plugin（把前三件套打包装进整机）

从这一篇开始，我不再叫它"三件套"了——应该叫「Claude Code 扩展四件套」。Plugin 是第四件，也是把前三件收束成一个可复用单元的最后一环。

**下一篇预告：**《Anthropic 把 Commands 合并成 Skills 了，我扒完官方 19 个自建 Skill 告诉你新范式》——Skills 是 Commands 的升级版，也是 Plugin 内部最常用的一种组件，是时候讲清楚这个新机制了。

---

关注「AI落地手记」，后续更多干货。

每周 1 篇「GitHub 上 X 个 Y」把 Claude Code 生态拆给你。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzYzMjY1OTI0MA==&mid=2247484527&idx=1&sn=868c6274ba480fe73b0c3e79d266bb2e&chksm=f147e3be5043d462997a51713ab66d943ddfd9cc6f1b5ede85b876f56ba0b3214de5bab9ee1b&scene=90&xtrack=1&req_id=1776482539380759&sessionid=1776482569&subscene=93&clicktime=1776482675&enterid=1776482675&flutter_pos=3&biz_enter_id=4&ranksessionid=1776482539&jumppath=20020_1776482579084,1104_1776482607447,20020_1776482612093,1104_1776482669079&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004724&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQSl454isKFaemgur8gf2M0RLBAQIE97dBBAEAAAAAAIY5Ay493m4AAAAOpnltbLcz9gKNyK89dVj04kWZUcgOFiQEdGKE3S66MBmJ58Xg6NfQUgzrqHqz18yIlCmGs2Y3uAwgjfbI/FLRKRdiiVnDGU8d7oAN0SRWiSFmewXdErKz9LHsuTe0Vlu0pprUuvuOXQf1dp2FGgn6U8U/cjI4kGoSkJkxujs2WTF+tz4RCF0b0Dh/wPG+HRcNv0/1bmlKijLOVyrHFhd2kWTTsYn69hlP6TA=&pass_ticket=IPLScXHga/mQ7CcyhE7uqmumsW2WsMVtd+gVX8kpbwoCY8zZr863k4bZZvubZtaF&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/56066fa5-6c39-44bf-a77e-1b0501b8f796/56066fa5-6c39-44bf-a77e-1b0501b8f796/)