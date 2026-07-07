---
title: Claude装太多，只会更废 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Claude装太多，只会更废 2.md
tags: [evernote, impression, yinxiang]
---

# Claude装太多，只会更废

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0NDQ0ODU3MA==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547725&idx=1&sn=c7e7ac5c2fabe1a6f33112308079980e&chksm=e862761340c0910654a03fe88db97f2bde2402630e2af06f31bde37f5dd97b71a60dc0ce7c24&scene=90&xtrack=1&req_id=1779798125604975&sessionid=1779796388&subscene=93&clicktime=1779798662&enterid=1779798662&flutter_pos=11&biz_enter_id=4&ranksessionid=1779798125&jumppath=30024_1779798381461,1104_1779798416563,20020_1779798581562,1104_1779798659337&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8xavmdZFXkh28X9uM7krnxLTAQIE97dBBAEAAAAAAN62OQ6VFA8AAAAOpnltbLcz9gKNyK89dVj0jxhnqnyr1yPlX5H2akSrd53UVJt1DkNrLPwRz3oMvXLrVrICH4/GlK02opf1QBXafGMTDu904aw0nxFBQUlrPZQjnU2JFC+DuxbYAo6VX90TpzLKytafptFUlopfmtrUx6cqUIvV7MPRY6buZ8QYZpyEmkL2n6mJSUlo8sLYaxJ/aBYPGAP+zl/6NaSutXkoUXLh0gF4dtcNldMe37qG7k8+c48BZ5v1laR+Pk0=&pass_ticket=u7uQ3FKlN5i6GQmOLVqqQ6cw2hqdwDT8gf2o9yb/GOt4KedCn9+cdkzTgWndZAVd&wx_header=3)

Claude装太多，只会更废
==============

Originalde 大迁世界

上个月刚开始时，我的 Claude Code 里装了 31 个 skills。

一个月后，只剩下 8 个。

被我删掉的那 23 个，并不是坏了，也不是不能用。问题是：我根本没怎么用它们。很多 skill 都是六周前看到社交媒体帖子、Top 10 推荐清单后顺手装上的。装完之后，它们就安静地躺在那里。

可问题是，它们并不是“躺着不动就不消耗”。

每一个 skill 的 description，都会在每一轮对话里继续占据我的 context window。无论我有没有触发它，它都在消耗 token。Anthropic 自己的 playbook 里也提到过，skills 数量最好控制在 8 到 12 个以内。一旦超过这个范围，成本就开始显现。

超过之后，每一行多余描述，都是 context tax。

也就是说，这是模型必须支付的 token 成本，不管这个 skill 最后有没有真正帮上忙。

这次 audit 之后，我才看清一个差距：高级 Claude Code 配置，通常是 8 个经过审计的 skills；初级配置，则是装 30 个，然后把它叫作“技术栈”。

下面这 8 个，就是我最后留下来的。里面 6 个是官方的，2 个是社区构建的。每一个留下来，都有自己的理由。更有意思的是，其中 3 个其实早就在你的机器上了，只是你可能从来没意识到它们也是 skills。

Context Window 的机械现实
--------------------

当你在 Claude Code CLI 里输入一个 prompt 时，引擎发送给模型的，并不只是你输入的那句话。

它还会读取本地 `.claude/skills/` 目录，并把所有已安装 skill 的 description 编译进 system prompt 里。它必须这么做，因为模型需要知道自己可以调用哪些工具来解决问题。

如果你装了 30 个 skills，就等于强迫模型在看你的代码库之前，先读完一小本“工具说明书”。

你会为此付出两个代价：延迟和准确率。

模型会被一堆无关选项分散注意力。你只是让它格式化一个 markdown 文件，它可能却开始考虑要不要使用数据库迁移 skill。

Anthropic 在官方指南中明确提醒过这个问题。他们给 skill descriptions 分配了非常严格的 1% context budget。每个 description 的上限是 1,536 个字符。

当你把这个预算塞满从来不用的工具时，你实际上是在挤压 Agent 理解代码所需要的工作记忆。

audit，就是修复这个问题的机制。

你要看清自己到底在用什么，然后把剩下的全部剥掉。

![](.evernote-content/9DE7B622-9B4D-4F6D-8862-54CB00562839/1257847C-279D-4310-9D6C-C75A87D8BE4D.png)

Anthropic 自己的 Meta-Skill，必须放第一位
-------------------------------

Anthropic 官方的 `skill-creator`，是这个列表里所有其他 skill 的前置条件。

包括那些后来被我删掉的。

这个 skill 支持新 skill 的 YAML frontmatter 和执行逻辑。它更像是一个 description 字段的调优助手。

而 description，恰恰是一个 skill 最重要的部分。

因为模型判断要不要触发某个 skill，看的就是 description。如果你的描述太模糊，模型会忽略它；如果你的描述太宽泛，模型又会频繁触发它，白白浪费你的 API 预算。

---
name: review-pr
description: Review the current PR diff and flag risks. Use before commit.
allowed-tools: Bash(git diff \*) Bash(gh pr \*)
---

它能同时暴露三个问题：

第一，多个 skills 之间的 description 是否互相重叠。 第二，你预期它应该触发的 prompt，是否触发得足够稳定。 第三，这件事到底该不该做成 skill，还是其实只应该写进 CLAUDE.md 里当作一次性规则。

真正大量使用 skills 的工程师，最后都会把 `skill-creator` 放在第一位，原因就在这里。

初级用法，是看到别人推荐什么就装什么。

高级用法，是用 `skill-creator` 为自己的仓库构建小而具体的工具，并在项目结束后及时清理。

我这次 audit 时，就用它把三个写得很差的 git helper skills，合并成了一个更可靠的 prompt。

![](.evernote-content/9DE7B622-9B4D-4F6D-8862-54CB00562839/D9638661-4C6E-4142-8C91-47A6EF911872.png)

文档处理套装
------

Anthropic 提供了一个叫 `document-skills` 的 bundle，可以用一条命令处理 PDF、XLSX、DOCX 和 PPTX 的生成。

它是通过 Plugin Set 分发的。Plugin Set 是 Anthropic 对“一条命令安装多个相关 skills”的叫法，这些 skills 装在一起后，可以自然地串联工作。

/plugin install document-skills@anthropic-agent-skills

如果你没装这个 bundle，却直接让模型“创建一个 PDF”，大概率得到的只是一个顶部写着 PDF 的 markdown 文本。

因为语言模型本质上生成的是文本，不是二进制文件格式。

装上这个 bundle 后，Agent 才能真正产出一个 `.pdf` 或 `.xlsx` 文件，让工程以外的人也能打开、阅读和使用。

在很多配置里，这个 bundle 可以替代 4 个单独的 MCP servers。

MCP 是一个开放标准，用来把 AI 模型连接到外部数据源。过去，如果开发者想解析 Excel，可能得跑一个本地 MCP server；想生成 PDF，又得再跑另一个。

现在，把这些逻辑迁移到本地 skills 后，总体 context tax 会更低。你不再需要加载一堆外部 server 的 JSON schemas。skill 只需要执行本地 Python 脚本或原生命令，就能完成文件转换。

需要注意的是，document skills 是 source-available 的参考实现，不是 open source。Anthropic 公开它们，是为了让你看到文件操作底层是怎么工作的。

你应该通过 Plugin Set 系统安装它们，而不是手动复制粘贴代码。

强制确定设计方向
--------

有两个社区插件，在插件市场里排名很靠前，而且它们应该被当作一个能力块来看待：`frontend-design` 和 `theme-factory`。

这两个 skills 会改变 Agent 写 UI 的方式。

如果你经常使用 AI coding assistant，你很快就会识别出那种默认审美：中性色、Inter 字体、浅灰渐变。最后，每一个内部工具、每一个 dashboard，看起来都像同一个模板里复制出来的。

/plugin marketplace add anthropics/claude-code
/plugin install frontend-design@anthropics/claude-code
*# theme-factory lives in the anthropics/skills repo:*
/plugin install theme-factory@anthropic-agent-skills

与其接受这种千篇一律的 AI 默认审美，不如一开始就强制它确定设计方向。

你可以要求 Agent 在写第一行 CSS 之前，就先锁定 brutalist layout、retro-futuristic aesthetic，或者 clean editorial style。

`theme-factory` 会基于这个方向，生成完整的 CSS variables 和 Tailwind 配置，确保整个应用的视觉风格保持一致。

我在 audit 时删掉了 5 个不同的 UI component generators，因为这对组合在“控制审美方向”这件事上做得更好。

它们通过在代码生成之前，把严格的 design token schema 注入上下文，来覆盖模型默认的审美权重。

把 Playwright 放进 Skill 里
-----------------------

把 Playwright 放进 skill，是一个很小的变化。

但它能把“我手动点了点，好像能用”，变成真正的 smoke test。

`webapp-testing` skill 可以直接从命令行编排一个本地 headless browser session。

/plugin install webapp-testing@anthropic-agent-skills
/webapp-testing http://localhost:3000 "verify login flow and dashboard render"

这个 slash command 接收目标 URL，以及一句自然语言描述，告诉它你想验证什么。

调用后，Claude 会启动开发服务器，访问本地 URL，然后开始和页面交互。它会填表单、点按钮、截图。

接着，它会提取 DOM accessibility tree。

也就是屏幕阅读器用来理解页面结构的那张结构图。

这个步骤，才是它从“截图测试”升级成“Agent 可行动验证”的关键。

比如，Claude 写了一个新的登录表单，但提交按钮不小心被透明 div 层盖住了。它读取 DOM tree 后，会意识到这个元素不可点击，然后重写 CSS 的 z-index 来修复问题。

你不需要每次生成 diff 后再手动点一遍页面。你运行命令，Agent 会带着真实浏览器验证结果回来报告。

它不会替代你的 CI suite。

但它可以替代你提交代码前那种临时、随手、靠感觉的人工点击检查。

Press enter or click to view image in full size

你早就在用的内置 Skills
---------------

很多开发者第一次意识到自己早就在用 skills，是看到 `/simplify` 的时候。

*# Already installed. Type it after any diff:*
/simplify
*# Sibling bundled skills: /debug /batch /loop /claude-api*

Anthropic 会把几个核心命令直接打包进 Claude Code 安装里。

当你在生成一个大 diff 后输入 `/simplify`，引擎其实调用的是 Simplify Skill。它会读取当前 diff，并把代码改得更干净、更容易维护。

它还有几个兄弟命令：

`/debug` 用来处理 stack traces。`/batch` 用来跨文件 fan-out。`/loop` 用来 run-until-condition。`/claude-api` 用来向 Anthropic API 发起子任务查询。

这些命令在特定场景下都有用。

但没有一个像 `/simplify` 一样，值得成为日常必用项。

初级模式，是接受 Agent 第一次生成的结果。

但语言模型生成的代码，经常会包含重复逻辑，或者过度复杂的抽象。

高级模式，是每次 commit 前都跑一遍 `/simplify`，强制模型用“降低复杂度”这个明确目标重新审视自己的输出。

知道这些命令本质上是 skills，也能帮你理解 compaction budget 是怎么工作的。

Claude Code 会保留一块 25K-token allowance，用来确保对话被总结后，已调用的 skills 仍然可以继续使用。

当你调用 `/simplify` 时，系统会压缩之前的对话历史，好让这个 skill 有足够的工作记忆来执行特定的重构任务。

Skills 和 MCP 之间的桥
-----------------

当 skill 抽象不够用，因为 Agent 需要真正操作外部系统时，你就需要一座桥。

`mcp-builder` skill 解决的正是本地逻辑和外部状态之间的断层。

Skills 处理的是 thinking layer。

它们告诉 Agent 应该如何理解一个系统，或者应该遵循什么架构模式。

MCP servers 处理的是 doing layer。

它们负责实时数据、持久状态、OAuth 流程和外部 API 调用。

当你需要连接一个新的内部 billing API 时，`mcp-builder` 可以根据一句自然语言描述，生成所需的 MCP server。

/plugin install mcp-builder@anthropic-agent-skills

---
name: build-internal-billing-mcp
description: Support an MCP server for the internal billing API.
---

Use mcp-builder to generate tools for: list\_invoices, refund\_charge,
get\_subscription\_status. Use OAuth from .env.local.

builder 会读取这段指令，并自动支持 authentication boilerplate，这样你就不需要手动把所有东西接起来。

初级模式，是把开源 registry 上能找到的 MCP server 全部装一遍。

于是 Jira、Slack、GitHub、Postgres 全部一起加载，prompt 还没开始，就先把 50,000 tokens 的 JSON schema 塞进 context window。

今年早些时候，很多协议早期使用者已经记录过这种失败模式，并提醒大家不要加载过大的 schema，因为它会挤掉真正有用的上下文。

高级模式，是 skills-first。

凡是本地 skill 能解决的，就先用 skill。只有当 skill 真的无法覆盖需求时，才使用 MCP。

`mcp-builder` 让这个模式变得可行，因为你可以为自己的真实需求构建一个很小、很专用的 server，而不是去找一个巨大臃肿的现成方案。

Press enter or click to view image in full size

抓住那些能 grep 出来的漏洞
----------------

把 CodeQL 和 Semgrep 包成 skill，可以抓住常见漏洞中最容易被模式匹配发现的那 80%。

而最近的一些研究也证明，这个安装位是值得的。

语言模型并不擅长在一堆样板代码里识别微妙的安全漏洞。它可能很自信地写出一个认证流程，但里面却漏掉 CSRF token，因为从结构上看，那段逻辑似乎是正确的。

/plugin marketplace add trailofbits/skills
/plugin install static-analysis@trailofbits

安全团队在测试 AI 生成应用时，已经多次发现：那些通过了随手人工 review 的代码里，仍然可能存在两位数级别的漏洞，其中甚至包括 critical 级别的问题。

这个 security skill 会标记 SQL injection 模式、硬编码 secrets、不安全的反序列化，以及缺失的授权检查。

它会在后台运行 Semgrep，格式化输出结果，然后只把存在漏洞的代码块送回 Claude 的 context window，让 Agent 可以继续修复。

初级模式，是直接发版，然后祈祷安全没问题，等客户发现漏洞后再处理。

高级模式，是在打开任何 pull request 之前，先跑 `/security-review`。

skill 会抓出明显错误，工程师再 review 修复结果。剩下那 20% 更隐蔽的业务逻辑漏洞，则继续交给团队的人类 review 流程。

它能抓模式。

但它不理解你的领域特定授权规则。

隔离执行环境
------

只要你把本地文件系统的执行权限交给自主 Agent 足够久，它迟早会犯一次破坏性错误。

解决办法是隔离。

`agent-sandbox` 提供的正是这个能力。

*# Install (community skill from disler/agent-sandbox-skill, GitHub-hosted):*
git clone https://github.com/disler/agent-sandbox-skill.git \
  ~/.claude/skills/agent-sandbox
*# Then in any Claude Code session — the skill drives these under the hood:*
uv run sbx init --timeout 1800            *# create sandbox (returns sandbox\_id)*
uv run sbx exec <sandbox\_id> "npm test"   *# run commands in the sandbox*
uv run sbx sandbox kill <sandbox\_id>      *# tear down*

如果你把本地文件系统的钥匙交给它，最后一定会知道它会犯哪一种错：

在错误目录里递归删除文件。 不小心提交 `.env`。 往 dev database 里灌一堆垃圾测试数据，把应用搞坏。

这个 skill 会使用 E2B 启动一个隔离环境。E2B 是一个 cloud-sandbox provider，提供临时计算环境。

Claude 可以在里面构建、托管和测试 full-stack 应用，而不会碰你的本地机器。

每一个 full-stack 实验，都先在 fork 出来的云沙箱里跑。只有真正值得保留的 diff，才会被搬回本地仓库。

我在 audit 时差点删掉这个 skill，因为它触发频率不高。

但后来我想起其中一次，它抓住了一个会清空我 dev database 某张表的 deploy script。

所以，它必须留下。

每月 Audit 框架
-----------

上面这 8 个 skills，只是我这次 audit 后的结果。

你的 8 个，可能会完全不同，这取决于你的技术栈。

真正重要的交付物，不是这份名单，而是这个 audit 框架。

它只需要 10 分钟，但你应该每 30 天跑一次。

打开你的 `.claude/skills/` 目录，然后对每个文件问自己四个问题。

第一，过去 30 天，我触发过这个 skill 吗？

如果答案是否，那就删掉。以后需要还能重新安装。没有理由为了一个你不主动使用的工具，持续支付 context tax。

第二，它的 description 是否和另一个 skill 抢同样的触发短语？

如果两个 skills 都说自己可以处理 database migrations，模型就会浪费时间在它们之间做选择。更糟的是，它可能会幻觉出一个两者混合的工具。

你必须合并它们，或者砍掉弱的那个。

第三，这件事能不能只是一个 one-shot prompt，而不是 recurring skill？

并不是所有重复需求都需要做成 skill。

如果你只是想让 Agent 按某种格式写 commit message，把规则放进 CLAUDE.md 就够了。

Skills 应该用来执行逻辑和串联工具。

Prompts 则应该用来设定规则。

第四，它的安装体积配得上它占用的 token 吗？

看一下 supporting files 的大小。

如果一个 skill 需要 Python 脚本和密集的 YAML 配置文件，那它最好真的能帮你省下几个小时。

如果它只是包了一条简单 bash 命令，那你还不如自己手动输入 bash。

你跑完这套 checklist。

删掉死重，优化留下来的 descriptions。

Press enter or click to view image in full size

如果你能看到这里，下面是一次性安装这 8 个能力块的命令。

没有 `/plugin` 命令。

它适用于 Desktop、Web、CLI、Cursor，以及任何 Claude Code 会读取 `~/.claude/skills/` 的地方。

git clone https://github.com/anthropics/skills.git /tmp/anthropic-skills
git clone https://github.com/anthropics/claude-code.git /tmp/claude-code
git clone https://github.com/trailofbits/skills.git /tmp/tob-skills
git clone https://github.com/disler/agent-sandbox-skill.git /tmp/agent-sandbox
mkdir -p ~/.claude/skills
cp -r /tmp/anthropic-skills/skills/skill-creator    ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/pdf              ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/docx             ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/xlsx             ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/pptx             ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/theme-factory    ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/webapp-testing   ~/.claude/skills/
cp -r /tmp/anthropic-skills/skills/mcp-builder      ~/.claude/skills/
cp -r /tmp/claude-code/plugins/frontend-design/skills/frontend-design ~/.claude/skills/
cp -r /tmp/tob-skills/plugins/static-analysis       ~/.claude/skills/
cp -r /tmp/agent-sandbox/.claude/skills/agent-sandboxes ~/.claude/skills/agent-sandbox
rm -rf /tmp/anthropic-skills /tmp/claude-code /tmp/tob-skills /tmp/agent-sandbox
ls ~/.claude/skills/

最后那条 `ls` 应该打印出 11 个文件夹：

`skill-creator`、`pdf`、`docx`、`xlsx`、`pptx`、`frontend-design`、`theme-factory`、`webapp-testing`、`mcp-builder`、`static-analysis`、`agent-sandbox`。

Claude Code 会实时监听这个目录，不需要重启。

打开任意 session，问一句：

What skills are available?

就能确认它们是否已经加载。

现在，你已经拥有了和我这次 audit 相同的配置。

30 天后，跑一次你自己的 audit。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547725&idx=1&sn=c7e7ac5c2fabe1a6f33112308079980e&chksm=e862761340c0910654a03fe88db97f2bde2402630e2af06f31bde37f5dd97b71a60dc0ce7c24&scene=90&xtrack=1&req_id=1779798125604975&sessionid=1779796388&subscene=93&clicktime=1779798662&enterid=1779798662&flutter_pos=11&biz_enter_id=4&ranksessionid=1779798125&jumppath=30024_1779798381461,1104_1779798416563,20020_1779798581562,1104_1779798659337&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8xavmdZFXkh28X9uM7krnxLTAQIE97dBBAEAAAAAAN62OQ6VFA8AAAAOpnltbLcz9gKNyK89dVj0jxhnqnyr1yPlX5H2akSrd53UVJt1DkNrLPwRz3oMvXLrVrICH4/GlK02opf1QBXafGMTDu904aw0nxFBQUlrPZQjnU2JFC+DuxbYAo6VX90TpzLKytafptFUlopfmtrUx6cqUIvV7MPRY6buZ8QYZpyEmkL2n6mJSUlo8sLYaxJ/aBYPGAP+zl/6NaSutXkoUXLh0gF4dtcNldMe37qG7k8+c48BZ5v1laR+Pk0=&pass_ticket=u7uQ3FKlN5i6GQmOLVqqQ6cw2hqdwDT8gf2o9yb/GOt4KedCn9+cdkzTgWndZAVd&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d6e288f0-8359-4993-9259-bc034c297d9e/d6e288f0-8359-4993-9259-bc034c297d9e/)
