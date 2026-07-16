---
title: "操控浏览器选 agent-browser 还是 Playwright？CLI 和 MCP 两条路"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/操控浏览器选 agent-browser 还是 Playwright？CLI 和 MCP 两条路.md
tags: [印象笔记]
---

# 操控浏览器选 agent-browser 还是 Playwright？CLI 和 MCP 两条路

# 操控浏览器选 agent-browser 还是 Playwright？CLI 和 MCP 两条路 --- 原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI

---

# 操控浏览器选 agent-browser 还是 Playwright？CLI 和 MCP 两条路

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwNjA1NjMyNQ==&mid=264911...](https://mp.weixin.qq.com/s?__biz=MzIwNjA1NjMyNQ==&mid=2649114435&idx=1&sn=81f3b6ff7386e73ca401d8f1bf94e158&chksm=8ebb4ab35da3beee1722d13c2b61f1a7f0e0d89e5b4e4b3b58514da8e48a7fba23de4e6f8ccf&mpshare=1&scene=24&srcid=0630SRoUUVwMcoyoso08iO8M&sharer_shareinfo=66661dfde4e36e6fd4121b1e34fc9617&sharer_shareinfo_first=66661dfde4e36e6fd4121b1e34fc9617&clicktime=1782898560&enterid=1782898560&ascene=14&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbR/v5nXL+OijyVR/UmGlBxLTAQIE97dBBAEAAAAAAPGOE5RTZcMAAAAOpnltbLcz9gKNyK89dVj0/SU9ThAcmQ/AphroLUrkaoDxbxL++4VKBQb+fH/NhjDtpGZaxlfjRG5NfqyQnP3XP2KNJJN5+HNPEljOvt2EIMMSGT5TYd1sRxkJ8IcaLrPB4UU+g2PGjKt936KOQwb0t+HuSzp+lg07CtsjjwMve8N0yH5K/jB53DZ2rlJio3LOZXaHz1tML2Oadug+XQ9+6IzjxO5Osr9BqeQX1Lu1bSgqWfTO3TAL0ISBBKg=&pass_ticket=Lc8BzSFyARCCXcpxHbd+tGWV7Rg1ah2HUJYi5pOGRiUCCfDPq0lSBJ/hr+bT4L7Y&wx_header=3)

OriginalAI智闻说 AI智闻说

你让 AI 写代码，它能写。你让它上网查个实时数据，它就傻了：模型知识有截止日期，今天的热搜它不知道，刚发布的 API 文档它没见过。

想让 AI 自己打开浏览器、看网页、点按钮、抓信息？目前最火的三个工具：agent-browser（近 4 万 star）、Playwright MCP（3.4 万 star）、Playwright CLI（1.2 万 star）。前两个名气大，但很多人不知道微软还出了个 Playwright CLI，定位和 agent-browser 一样：给 coding agent 用的浏览器 CLI。选错工具，轻则多花 token，重则效率很低。

这三个东西到底是什么
----------

agent-browser，Vercel Labs 出的命令行工具，Rust 原生二进制，CLI 冷启动快。设计思路很简单：给 AI 一条命令行，让它像人操作终端一样操控浏览器。

Playwright CLI，微软出的，刚才说的那个容易被忽略的。它跟 Playwright MCP 是同一团队的产品，但走的 CLI + Skills 路线，专门给 coding agent 用的。底层用 Playwright 引擎。

Playwright MCP，微软出的 MCP 服务器（MCP server）。把 Playwright 的浏览器自动化能力包装成 MCP 协议，让 Claude Desktop、Cursor、VS Code 这类客户端直接调用。

一句话区分：agent-browser 和 Playwright CLI 都是命令行工具，互相竞品；Playwright MCP 是协议服务，跟它俩不在一个赛道。前两个在终端敲命令，第三个在客户端里调接口。

先选路线：CLI 还是 MCP
---------------

在选具体工具之前，得先搞清楚一件事：你用的是什么环境？

用 Claude Code / Codex / Copilot CLI 这类 coding agent，走 CLI 路线。coding agent 天然在终端里工作，调一个命令行工具比走 MCP 少一层协议开销，token 消耗低得多。

用 Claude Desktop / Cursor / VS Code 这类 MCP 客户端，走 MCP 路线。MCP 的优势在客户端自动发现工具、维护会话状态，鼠标点两下就配好了。

Playwright 官方 README 里有段对比：

*Modern coding agents increasingly favor CLI-based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose accessibility trees into the model context.*

翻译过来：现代 coding agent 越来越倾向于用 CLI + Skills 而不是 MCP，因为 CLI 调用更省 token，不用把大段工具描述和冗长的无障碍树塞进上下文。

CLI 路线：agent-browser vs Playwright CLI
--------------------------------------

既然 agent-browser 和 Playwright CLI 是正面对手，那就认真比一下。

### 怎么装

agent-browser

三种方式任选：

*# 方式一：npm（需要 Node.js）*npm install -g agent-browseragent-browser install   *# 下载 Chrome for Testing# 方式二：Homebrew（macOS）*brew install agent-browseragent-browser install*# 方式三：Cargo（Rust）*cargo install agent-browseragent-browser install

`agent-browser install` 会从 Google 官方的 Chrome for Testing 通道下载一个 Chromium，不污染你本地的 Chrome。装完直接用。

Playwright CLI

npm install -g @playwright/cli@latestplaywright-cli install --skills *# 安装 Skills（给 coding agent 用）*

两步搞定。Playwright 自带浏览器管理，不需要额外下载 Chrome。

### 核心差异表

|  | agent-browser | Playwright CLI |
| --- | --- | --- |
| 出品方 | Vercel Labs | Microsoft |
| 语言 | Rust 原生二进制 | TypeScript（Node.js） |
| 浏览器引擎 | Chrome for Testing | Playwright 引擎（Chromium/Firefox/WebKit） |
| 需要 Node.js | npm 安装需要；brew/cargo 不需要 | 需要 18+ |
| Skills 支持 | 通过 skills.sh 自动注册（coding agent 自动识别可用命令） | 通过 `install --skills` 注册 |
| 会话管理 | 后台常驻模式，`-s` 切换会话 | `-s` 会话参数，`--persistent` 持久化 |
| token 效率 | 高，每次只返回命令结果 | 高，不把页面数据强制塞进 LLM 上下文 |
| 可视化监控 | 无 | `playwright-cli show` 打开实时仪表板 |

几个关键差异展开说：

浏览器引擎。agent-browser 只有 Chrome；Playwright CLI 支持 Chromium / Firefox / WebKit 三个引擎，加 `--browser=firefox` 就能切换。需要跨浏览器测试的，Playwright CLI 省事。

可视化仪表板。这是 Playwright CLI 的独有功能：`playwright-cli show` 打开一个实时仪表板，能看到所有活跃浏览器会话的直播画面，点击任一会话还能直接接管鼠标键盘。coding agent 在后台跑浏览器操作的时候，你可以在仪表板上观察进度、随时介入。agent-browser 没有等价功能。

token 效率。两者都是 CLI，都比 MCP 省 token。Playwright CLI 的 README 直接标注了 "Token-efficient"，即不把页面数据强塞进 LLM 上下文。agent-browser 也是同样的思路：每条命令只返回精简结果，不往上下文里塞冗长的无障碍树。

### 实测：同一任务，两种写法

打开掘金首页，搜"AI Agent"。

agent-browser

agent-browser open juejin.cnagent-browser snapshotagent-browser fill @e3 "AI Agent"agent-browser click @e12

Playwright CLI

playwright-cli open https://juejin.cnplaywright-cli snapshotplaywright-cli fill e3 "AI Agent"playwright-cli click e12

命令几乎一模一样。`snapshot` 都返回带 ref 标记的无障碍树，AI 靠 ref 编号精准定位元素。唯一差别：agent-browser 用 `@e3` 格式，Playwright CLI 用 `e3` 格式。

![](.evernote-content/71F95337-0C19-49A8-8E74-28EA58189D26/01DDD1F6-06F3-4CEA-860A-E01B259C0E91.png)

### agent-browser 独有功能

`read` 命令。不启动浏览器，直接 HTTP 请求抓页面，输出干净的 Markdown 文本，还支持 `--filter` 过滤章节、`--outline` 只看标题结构、`--llms` 查找文档索引：

agent-browser read https://juejin.cn/post/7abc123

这是 agent-browser 的杀手功能。很多时候你不需要"操控"浏览器，你只是想"读"一个网页。比如查 API 文档、读一篇文章、拉一份 llms.txt。agent-browser 把「读网页」和「操控浏览器」拆成了两件事：`read` 负责读，`snapshot` + `click` 负责操控。Playwright CLI 和 Playwright MCP 都只有操控这一条路，读网页也得先把浏览器打开。

`batch` 批量执行。一条命令跑多步操作：

agent-browser batch "open https://juejin.cn""snapshot -i""click @e1"

`chat` 自然语言操控：

agent-browser chat "打开掘金，搜索 AI Agent，点击第一个结果"

`cookies --curl` 导入。从浏览器「复制为 cURL」直接导入 cookie：

agent-browser cookies set --curl ./curl-dump.txt

### Playwright CLI 独有功能

`show` 实时仪表板。能看到所有活跃会话的直播画面，点击可以接管操作：

playwright-cli show

Playwright 全家桶。codegen 录制、trace 查看、截图对比、视频录制，测试领域的能力全覆盖。如果同时还需要跑自动化测试，Playwright CLI 能和测试流程无缝衔接。

多浏览器引擎。加 `--browser=firefox` 或 `--browser=webkit` 就能切换：

playwright-cli open https://juejin.cn --browser=firefox

MCP 路线：Playwright MCP
---------------------

MCP 路线目前就一个主流选项：Playwright MCP。

用 Claude Code 加一行命令：

claude mcp add playwright npx @playwright/mcp@latest

用 Cursor / VS Code / Claude Desktop，写一段 JSON 配置：

{"mcpServers":{"playwright":{"command":"npx","args":["@playwright/mcp@latest"]}}}

重启客户端就生效。15+ 客户端一键接入：VS Code、Cursor、Claude Desktop、Cline、Copilot、Gemini CLI、Goose、Junie……配置一行 JSON 就能跑。

MCP 的优势是生态好、接入门槛低、会话有状态——登录态、cookie 之类跨调用自动保持，不用每次重新登录。劣势是 token 消耗高——工具 schema 常驻上下文，无障碍树也比较冗长。频繁操作页面的时候，上下文会被撑得很大。

![](.evernote-content/71F95337-0C19-49A8-8E74-28EA58189D26/DDE11797-7457-4BB7-BC26-4101A9C5D2DD.png)

选型决策表
-----

| 你的场景 | agent-browser | Playwright CLI | Playwright MCP |
| --- | --- | --- | --- |
| 用 Claude Code / Codex / Copilot CLI | ✅ 装完即用 | ✅ 装完即用 | ⚠️ 也能用，但多一步配置 |
| 用 Claude Desktop / Cursor / VS Code | ⚠️ 得手动调 | ⚠️ 得手动调 | ✅ 一行配置搞定 |
| 只想读网页文本，不想启动浏览器 | ✅ read 命令 | ❌ 做不到 | ❌ 做不到 |
| 需要跨浏览器测试 Firefox/WebKit | ❌ 只有 Chrome | ✅ 三引擎 | ✅ 三引擎 |
| 想实时观察 agent 的浏览器操作 | ❌ 无仪表板 | ✅ 仪表板直出 | ⚠️ 取决于客户端是否提供浏览器预览 |
| 需要批量执行 / 脚本化 | ✅ batch 命令 | ⚠️ 无 batch 命令，需 shell 脚本串联 | ❌ 依赖客户端调度 |
| 想要开箱即用的客户端生态 | ⚠️ 需自己集成 | ⚠️ 需自己集成 | ✅ 15+ 客户端原生支持 |
| 追求 token 效率 | ✅ CLI 天然省 | ✅ CLI 天然省 | ❌ schema 常驻上下文 |

更直白地说：coding agent 用户在 agent-browser 和 Playwright CLI 之间选，核心看你要不要 `read` 命令和跨浏览器；MCP 客户端用户直接选 Playwright MCP，这赛道没别的选。

![](.evernote-content/71F95337-0C19-49A8-8E74-28EA58189D26/6E6208C1-EF2B-4A59-A61E-0F115276A3CD.png)

现在的边界
-----

三个工具各有卡点。

agent-browser 有 545 个 open issue，迭代快但稳定性还有风险。只支持 Chrome，想做跨浏览器验证得找别的工具。

Playwright CLI 只有 1.2 万 star，社区热度比 agent-browser 低不少，文档也相对少。需要 Node.js 运行时，不像 agent-browser 有 Rust 原生二进制可选。

Playwright MCP 的 token 消耗是硬伤，尤其做频繁页面操作的时候，上下文会被无障碍树撑得很大。MCP 协议本身还在快速演变，不同客户端的支持程度参差不齐。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIwNjA1NjMyNQ==&mid=2649114435&idx=1&sn=81f3b6ff7386e73ca401d8f1bf94e158&chksm=8ebb4ab35da3beee1722d13c2b61f1a7f0e0d89e5b4e4b3b58514da8e48a7fba23de4e6f8ccf&mpshare=1&scene=24&srcid=0630SRoUUVwMcoyoso08iO8M&sharer_shareinfo=66661dfde4e36e6fd4121b1e34fc9617&sharer_shareinfo_first=66661dfde4e36e6fd4121b1e34fc9617&clicktime=1782898560&enterid=1782898560&ascene=14&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQbR/v5nXL+OijyVR/UmGlBxLTAQIE97dBBAEAAAAAAPGOE5RTZcMAAAAOpnltbLcz9gKNyK89dVj0/SU9ThAcmQ/AphroLUrkaoDxbxL++4VKBQb+fH/NhjDtpGZaxlfjRG5NfqyQnP3XP2KNJJN5+HNPEljOvt2EIMMSGT5TYd1sRxkJ8IcaLrPB4UU+g2PGjKt936KOQwb0t+HuSzp+lg07CtsjjwMve8N0yH5K/jB53DZ2rlJio3LOZXaHz1tML2Oadug+XQ9+6IzjxO5Osr9BqeQX1Lu1bSgqWfTO3TAL0ISBBKg=&pass_ticket=Lc8BzSFyARCCXcpxHbd+tGWV7Rg1ah2HUJYi5pOGRiUCCfDPq0lSBJ/hr+bT4L7Y&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5a584ad4-4aa9-42b7-8d8c-b80d36cb20df/5a584ad4-4aa9-42b7-8d8c-b80d36cb20df/)