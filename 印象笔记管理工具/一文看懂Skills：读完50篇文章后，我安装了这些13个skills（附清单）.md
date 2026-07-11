# 一文看懂Skills：读完50篇文章后，我安装了这些13个skills（附清单）

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzU4NDUyNTUwMQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzU4NDUyNTUwMQ==&mid=2247485344&idx=1&sn=14be057f819bcb3a41553127dd9c5852&chksm=fc5837ce693190fbb2ee105ca5ea2b3b1ccaea6c32923922af9a6d8c05dd8579071093fd23c8&scene=126&sessionid=0&clicktime=1773237758&enterid=1773237758&ascene=3&devicetype=iOS26.3.1&version=1800452f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQnxruoOXjxIImLGDU1vuzhRLVAQIE97dBBAEAAAAAAJJFE9NgmB4AAAAOpnltbLcz9gKNyK89dVj0m4As6OzM0B8iQu3UfcR8LS6gSVnZhKKGfOC4/n0KZeF9Nat4LjXwL5ICI8fpP+VodO9vJhjhueAQ68S4xJY+lLSh5r5BKjq5BGDlur/9+95c49YJRCxP9o8n3VckdV3t1WoGGn558/dmGHh5s4vPuGjflwBzAzCZZBmLll8AwDWd9UgpW2pWYlBT3AhJGEkfvpSWLmBVqmF3iYrMYiT3XXjdvptpXTN0fUL7UyaFMQ==&pass_ticket=2xtx8mYo8Af4PGHuhWJL4xRy5s88qyKnPyfX8q8C44g9vA12znnqC4XBTtrpFCVO&wx_header=3)

Original闻思修AI手记 闻思修AI手记

![](.evernote-content/A4021677-78D3-4FA0-BA32-F1474152F0EF/134226A4-E30E-48F3-903E-0140DD8DD352.png)

Claude Skills这东西，火了好几个月了。

全网都在喊“Skills改变生产力”“Skills让效率起飞”，但我一直没动。主要是感觉时候没到。

我的习惯是：一项技术刚出来的时候不追，等它成熟到能比现有工具强十倍，再一次性研究透。

这可能会错过热点流量，不过没关系。追新工具这件事，太容易把自己累死了。

最近觉得时候到了。我把过去几个月收藏的50多篇文章翻出来，筛出20+篇精华，用Gemini、Claude、GPT、Manus分别跑了一轮Deep Research，综合成了一份完整报告。

这篇文章，就是研究之后的全部收获。

Skills 到底是什么
------------

一句话：**把你的流程性知识，变成可复用的能力包，让Agent随叫随到，稳定发挥。**

Skills本质就是一个文件夹。

文件夹里装的东西很清楚，如果你是职场人士：

* `SKILL.md` 相当于告诉你这个岗位是做什么的
* `scripts/` 是常用到的工具软件
* `references/` 是业务流程涉及的知识库
* `assets/` 是工作模板库

把这些东西打包放好后，让Claude干活的时候自己去查、去用、去执行。

你不用每次开新对话都从头交代一遍“我要什么格式”“我的风格”“按什么流程处理"等等。只需要调用这个skills就行。

这里有一个很容易被忽略的好处：**省Token**。

以往，在大模型的交互中，对话越长，模型越笨。且越耗费Token。

Token确实又寸土寸金（尤其像claude这种）。

而Skills呢把大量背景知识从对话中抽离出来。需要时按需调取，主对话窗口始终保持干净。这就间接省了不少Token。

![](.evernote-content/A4021677-78D3-4FA0-BA32-F1474152F0EF/3965C550-8EE0-457E-B6F0-F6551C1BB919.png)

什么时候该用 Skills
-------------

有一条判断标准特别好用：**任何你不想一遍遍重新解释的东西，都值得写成Skill。**

官方给了三类典型场景：

**第一类，组织级工作流。**品牌规范、法务合规流程、标准化文档模板。这些东西公司里每个人都要遵守，但每次找AI帮忙都得重新说一遍。此时写成Skill就能一劳永逸。

**第二类，专业领域经验。比如**Excel公式套路、数据分析流程、PDF处理方法、代码 标准、安全审计清单等。类似这些是你在某个领域摸爬滚打攒下来的经验。

**第三类，个人偏好和习惯。**你的笔记结构、代码风格、研究方法论。每个人干活都有自己的一套讲究，Skill能让AI记住你的偏好和风格。

根据这几个标准。我盘点了自己的习惯，并安装上了claude官方出的几个与自身工作贴近的skills。同时根据自己需求，又自制了几个skills。

怎么安装和创建 Skills
--------------

1、安装很简单，两种方式。

第一种，命令行直接装。直接告诉Claude："帮我安装这个skill，skill项目地址为 xxx"，它自己就能搞定。

第二种，把Skills文件夹拖到本地目录 `~/.claude/skills`，手动放进去。

2、创建Skills也不复杂。如果你不是程序员（比如我），最省事的办法是直接跟Claude说：

"我要创建 skill，一步步引导我"，它就会一步步带你走完流程，最后生成一个zip 包，上传安装即可。

进阶一点的做法是先安装官方出的`skill-creator`，当你提出需求的时候，让它调用这个skill帮你做设计。这样出来的Skill结构既规范又稳定。

把 GitHub 项目打包成 Skill：一个被低估的用法
-----------------------------

这个思路来自卡兹克，我觉得是整个Skills生态里最值得关注的玩法。

**Skills最正确的用法，是将整个GitHub项目压缩成你自己的超级技能库。**

比如yt-dlp这个视频下载工具，打包成Skill之后，你只需要丢一个视频链接过去，Claude自动帮你下载。

比如Pake这个项目，可以把Web应用打包成轻量级桌面 APP。这些原本需要你去读文档、装环境、跑命令的事情，变成了一句话的事。

操作步骤并不复杂：

1. 复制目标 GitHub 项目链接
2. 给Claude Code提需求：“帮我把这个开源工具 https://... 打包成一个 Skill，实现xxx功能”
3. 先让claude开启计划模式做规划，再写Skill，稳定性会好很多
4. 如果一个skill在使用过程中遇到问题。你解决掉这个问题之后，记得告诉 claude：“把这些经验更新到这个skill里”。

第四步是关键。每次踩坑、每次修复，都喂回给Skill，它就会越来越好用。这就成为一个持续进化的skills了。

如果对这个部分感兴趣，可以搜索卡兹克这篇文章：《Skills的最正确用法，是将整个Github压缩成你自己的超级技能库》，应该会受到一些启发。

![](.evernote-content/A4021677-78D3-4FA0-BA32-F1474152F0EF/8A8557E1-10C7-4A4B-BC92-269763FC99DE.png)

Skills 不只是文档，还能跑代码
------------------

很多人以为Skills只是一堆提示词文件，其实不是。

Skills里还可以包含可执行脚本，比如Python脚本。

AI生成代码有个老问题：不稳定。

每次解决问题，它调用的库可能不一样。比如今天它用 `requests` 库，明天可能换成 `axios。`

又比如，同一个任务每次生成的代码也都不一样，调试成本很高。

但Skill里的脚本是你写好的、验证过的，逻辑固定，结果可预期。

同时，大量参考资料可以放在 `references/` 目录里，Claude 需要的时候自己去查，不占主对话的上下文。

这就像给员工配了一个资料柜，不用把所有文件都摊在桌面上。

五步框架：把工作流变成可进化的 Skill
---------------------

这个方法论来自宝玉AI，观点比较激进但很有说服力：

**几乎所有能用workflow完成的AI任务，都可以用Agent + Skills实现。**

**我很认可这个观点。连lenny's newsletter里面赠送的n8n（一种搭建流程的AI工具）**我都转手出去了。因为真的不需要了（[Lenny's Newsletter白送18个AI工具，我只激活了4个](https://mp.weixin.qq.com/s?__biz=MzU4NDUyNTUwMQ==&mid=2247485208&idx=1&sn=23a5b35f34e766127739a391cbfe99ff&scene=21#wechat_redirect)）。

### 第一步：拆分

把工作流拆成单一职责的skill或subagent。每个模块只做一件事，做好一件事。

### 第二步：编排

在主skill里用自然语言描述整个流程。不需要写代码，像给同事交代任务一样说清楚就行。一个skill可以调用另一个skill，组合出复杂工作流。

### 第三步：存储

所有中间结果都保存成本地文件，而不是留在内存或上下文里。

### 第四步：分摊

Subagent之间只传文件路径，不传内容。这条规则很重要。直接把一大段内容塞给 subagent，上下文窗口很快就撑满了。

传路径的话，subagent会自己去读文件，上下文保持得很干净。

### 第五步：迭代

这是Agent + Skills相比传统workflow最大的优势——可以持续进化。

当skill的提示词你觉得不好的时候，可以让Claude帮你改。它甚至可以自己迭代 subagent的system prompt，实现自我进化。

这五步看似简单，但贯穿了一个核心思想：**拆得开、存得住、传得轻、改得动。**

![](.evernote-content/A4021677-78D3-4FA0-BA32-F1474152F0EF/02342532-4705-464E-8878-7DBE36090445.png)

实战案例
----

网络上实战案例太多了。看了一篇来自AI blew my mind的文章。整理了来自23个创作者的36个Skills应用场景。有兴趣可以按照下面标题搜索找来看。

![](.evernote-content/A4021677-78D3-4FA0-BA32-F1474152F0EF/413ED2CB-E349-49C0-A2D5-A2669AB839BD.png)

一条最重要的认知
--------

研究了这么多，最想说的其实是这一句：

**Skills一定是你本身实践过或者沉淀好的工作流，只是把它自动化。不是让AI帮你从零发明流程，而是把你已经验证过的流程固化下来。**

好的组织，会把经验变成可复用的 skill。好的个人，也一样。

这也是为什么同样用 Skills，有人效率翻倍，有人折腾半天没效果。差距不在工具，在于你自己有没有值得固化的东西。

最后我安装了哪些skills呢？
----------------

最终探索后安装了以下13个skills。供参考。这仅仅是第一次尝试装skills。后续应该会沉淀更多。欢迎交流。

1. `podcast-reader`：英文播客文字稿 → 结构化中文大纲（自制）
2. `github-to-skills`：自动将 GitHub 仓库转换为 AI Skills
3. `skill-manager`：Skills 生命周期管理
4. `obsidian-markdown`：Obsidian 风格 Markdown 创建与编辑（来自obsidian官网）
5. `pdf`：PDF 文件处理（读取、合并、分割、旋转）
6. `skill-evolution-manager`：根据反馈优化迭代现有 Skills
7. `skill-creator`：创建 Skills 的官方指南
8. `pptx`：PowerPoint 文件处理
9. `obsidian-bases`：Obsidian Bases 文件创建与编辑
10. `video-transcribe`：录制并转写视频音频为文字（自制）
11. `frontend-design`：生产级前端界面创建
12. `mcp-builder`：创建高质量 MCP（Model Context Protocol）服务器的指南
13. `json-canvas`：JSON Canvas 文件创建与编辑（来自obsidian官网）

    以上5、7、8、11、12均来自anthropic官网；2、3、6来自卡兹克文章，文末资源清单附有有仓库链接

![](.evernote-content/A4021677-78D3-4FA0-BA32-F1474152F0EF/28742190-C593-4332-ABB4-B16891E89E21.jpg)

1. 图：我调用询问claude code现在安装了哪些skills。有些并不是真实的skills。总共是13个。

资源清单
----

最后整理一份实用资源，方便直接取用。

**Skills 资源站：**

* **skills.sh**：精选 Skills 网站，支持 Claude Code、Cursor、GitHub Copilot、Windsurf、Codex、Gemini 等 16 种以上 AI 编程工具，一行命令即插即用
* **Anthropic 官方 GitHub**：github.com/anthropics/skills，学 Skills 从官方样例开始最靠谱
* **Skills Marketplace（SkillsMP）**：Claude、Codex、ChatGPT 的 Skills 市场

**Skills 管理三件套（卡兹克出品）：**

* `skill-creator` + `skill-evolution-manager` + `skill-manager`
* 解决 Skills 库的增删改查和迭代升级，实现全自动化管理
* 下载地址：github.com/KKKKhazix/Khazix-Skills

**官方延伸阅读：**

* *The Complete Guide to Building Skills for Claude*（Anthropic 官方权威指南）
* *Agent Skills - Claude API Docs*（开发者技术文档）
* agentskills.io（Agent Skills 开放标准官方网站）
* *36 Claude Skills Examples to Transform How You Work*（大量真实案例）

Tavily-search

Tavily Search 是 OpenClaw 生态中最核心的联网搜索技能，专为 AI 智能体优化，能让您的 OpenClaw 助手实时获取网络最新信息，突破大语言模型的知识截止日期限制。

### 🎯 核心定位：AI 专属的搜索引擎

与返回杂乱 HTML 的传统搜索引擎不同，Tavily 专为 LLM 消费设计：

* **输出优化**：返回**结构化摘要**、相关性评分（0-1分）、来源链接，而非原始网页。
* **智能降噪**：自动过滤广告、导航栏、SEO 噪音，提取纯净核心内容。
* **多源聚合**：单次 API 调用聚合多达 **20+ 权威数据源**，提供综合答案。

### 🔧 核心功能一览

| 功能模块 | 具体能力 | 适用场景 |
| --- | --- | --- |
| **智能搜索** | 基础/高级两种深度模式，支持中英文查询 | 日常信息查询、技术问题解答 |
| **新闻搜索** | 专用 `--topic news`模式，支持按天/周/月时间过滤 | 追踪行业动态、监控热点事件 |
| **深度研究** | `advanced`模式进行多源综合分析，质量更高 | 学术研究、竞品分析、市场调研 |
| **内容提取** | 从指定 URL 提取完整正文，清理无关元素 | RAG 知识库构建、资料归档 |
| **域名过滤** | `--include-domains`/ `--exclude-domains`控制来源 | 确保信息来自权威站点 |

### 📦 安装与配置（三步完成）

步骤1：获取 API Key

1. 访问 [tavily.com](https://tavily.com/)注册账号（支持邮箱/GitHub登录）。
2. 在 Dashboard 中复制以 `tvly-`开头的 API Key。
3. **免费额度**：每月 **1,000 次搜索**，个人使用完全足够。

步骤2：安装技能

# 推荐方式：通过 ClawHub 安装
clawhub install tavily-search
# 或使用完整命令
npx clawhub@latest install tavily-search

步骤3：配置 API Key

# 方法一：设置环境变量（推荐）
export TAVILY\_API\_KEY="tvly-你的密钥"
# 方法二：在 OpenClaw 中直接配置
# 对 OpenClaw 说：“将 Tavily 的 API Key 设置为 [tvly-xxxxxx]”

### 🚀 基础使用示例

在 OpenClaw 中直接对话使用：

* “**使用 tavily 搜索一下今天的头条新闻**”
* “**帮我搜一下微信接入 OpenClaw 的最新消息**”
* “**用 tavily 查一下 Next.js 最新版本是什么**”

**命令行直接调用**（安装后技能位于 `~/.openclaw/skills/tavily-search/`）：

# 基础搜索
node skills/tavily-search/scripts/search.mjs "Python 异步编程"
# 新闻搜索（最近7天）
node .../search.mjs "AI 最新进展" --topic news
# 高级深度研究
node .../search.mjs "机器学习最佳实践" --deep

### ⚖️ 与 Brave Search 对比

| 维度 | Tavily Search | Brave Search |
| --- | --- | --- |
| **优化目标** | AI 消费（结构化摘要） | 人类阅读（原始链接） |
| **免费额度** | 1,000 次/月 | 2,000 次/月 |
| **搜索深度** | 4档可调（basic/advanced等） | 固定深度 |
| **新闻搜索** | ✅ 专用 news 模式 | ❌ 无专用模式 |
| **域名过滤** | ✅ 支持包含/排除特定域名 | ❌ 不支持 |
| **响应速度** | ⚡ 极快（basic 模式1秒内） | ⚡ 快速 |

建议：两者都安装配置，按需使用：

* **日常简单搜索** → Brave Search（免费额度更多）
* **深度研究/新闻** → Tavily Search（质量更优）

### 💡 高级使用技巧

1. **组合技能**：与 **Summarize**（文章摘要）、**DeepWiki**（代码文档研究）等技能搭配，构建完整的研究工作流。
2. **自动化任务**：让 OpenClaw Agent 每天早8点自动搜索指定关键词，生成简报并发送到 Telegram/邮箱。
3. **事实核查**：对 AI 生成的内容进行实时验证，确保信息准确性。

### ⚠️ 注意事项

1. **API Key 安全**：不要将密钥提交到公开仓库，建议使用环境变量管理。
2. **配额监控**：免费版每月 1,000 次搜索，超出需升级付费计划。
3. **搜索深度选择**：`basic`模式适合日常查询（速度快），`advanced`模式适合深度研究（消耗配额翻倍）。

总结：Tavily Search 是 OpenClaw 必装的核心技能之一，它让您的 AI 助手真正“联网”，能够回答实时问题、进行深度研究、追踪最新动态。安装配置简单，免费额度充足，是提升 OpenClaw 实用性的关键工具。

Skills的协同工作技能

在 OpenClaw 中，当您安装了多个功能相似的技能时，系统会通过一套优先级规则和协调机制来决定如何调用，而不是简单地“调用功能最强的那个”或“各自调用一部分”。其核心设计目标是避免冲突、确保任务顺利完成。

### 🎯 核心机制：优先级与匹配规则

当您发出一个指令时，OpenClaw 会按以下流程处理：

1. **触发词匹配**：系统扫描所有已安装技能的 [`SKILL.md`](http://SKILL.md)中的 `trigger`描述，找出所有可能匹配的技能。
2. **按优先级排序**：如果匹配到多个技能，系统会按照**从高到低的优先级**进行排序：

* **第1级：用户显式指定** - 例如您明确说“**用 tavily 搜索...**”，则优先调用 `tavily-search`技能。
* **第2级：精准匹配** - 触发词与指令语义完全吻合的技能。
* **第3级：模糊匹配** - 语义相近的技能。
* **第4级：默认** - 没有匹配时，AI 使用自身知识回复。

3. **路径优先级（同名冲突时）**：如果存在同名技能，系统按以下路径优先级加载（高优先级覆盖低优先级）：

   `/skills`(工作区) > `/.agents/skills`(项目) > `~/.agents/skills`(个人) > `~/.openclaw/skills`(全局) > 内置技能。

### 🔧 两种协同模式：单激活 vs. 多激活

根据任务复杂度和技能设计，OpenClaw 支持两种协同模式：

| 模式 | 工作原理 | 适用场景 |
| --- | --- | --- |
| **单激活模式** | 只激活**优先级最高**的那个匹配技能。 | 简单查询，避免多个相似技能同时响应造成冲突或冗余。 |
| **多激活模式** | **同时激活**所有匹配的技能，并行或按顺序执行。 | 复杂指令需要多个技能协作完成（例如：“查天气并画图表”）。 |

**例如**：如果您同时安装了 `tavily-search`和 `brave-search`，当您说“搜索AI新闻”时：

* 若两者触发词都匹配，系统会根据优先级（如精准度）选择其中一个执行。
* 但如果您说“**用 tavily 和 brave 都搜一下...**”，系统可以理解并尝试协调两者共同工作。

### 🤖 协同工作原理

多技能协作通常通过 “智能体工作流” 实现：

1. **主智能体**解析您的指令，识别出需要多个技能的子任务。
2. **规划与调度**：根据技能描述，决定执行顺序（串行）或并发执行。
3. **结果整合**：将各技能的输出汇总，形成最终回复。

例如，指令“帮我总结今天关于OpenClaw的新闻，并生成一个趋势图”可能触发：

* `tavily-search`执行新闻搜索。
* `summarize`技能对搜索结果进行摘要。
* `design-doc-mermaid`或 `chart-generator`生成趋势图。

### 💡 给您的实践建议

1. **显式指定**：最可靠的方式是在指令中直接指明技能名，如“**用 design-doc-mermaid 画一个架构图**”。
2. **查看技能文档**：安装后查看技能的 [`SKILL.md`](http://SKILL.md)，了解其准确的触发词和适用范围，避免意外匹配。
3. **技能管理**：如果不需要某个技能，可将其从技能目录中移除，或通过配置禁用。
4. **利用工作区技能**：对于特定项目，可将专用技能放在项目工作区的 `/skills`目录下，它会获得最高优先级，避免与全局技能冲突。

总结：OpenClaw 的技能调用不是“民主投票”，而是基于优先级规则的智能调度。您可以通过显式指定技能名来精确控制，系统也具备在复杂任务中协调多技能协同工作的能力。理解这套机制，可以帮助您更高效地组织和管理您的技能生态。

---

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzU4NDUyNTUwMQ==&mid=2247485344&idx=1&sn=14be057f819bcb3a41553127dd9c5852&chksm=fc5837ce693190fbb2ee105ca5ea2b3b1ccaea6c32923922af9a6d8c05dd8579071093fd23c8&scene=126&sessionid=0&clicktime=1773237758&enterid=1773237758&ascene=3&devicetype=iOS26.3.1&version=1800452f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQnxruoOXjxIImLGDU1vuzhRLVAQIE97dBBAEAAAAAAJJFE9NgmB4AAAAOpnltbLcz9gKNyK89dVj0m4As6OzM0B8iQu3UfcR8LS6gSVnZhKKGfOC4/n0KZeF9Nat4LjXwL5ICI8fpP+VodO9vJhjhueAQ68S4xJY+lLSh5r5BKjq5BGDlur/9+95c49YJRCxP9o8n3VckdV3t1WoGGn558/dmGHh5s4vPuGjflwBzAzCZZBmLll8AwDWd9UgpW2pWYlBT3AhJGEkfvpSWLmBVqmF3iYrMYiT3XXjdvptpXTN0fUL7UyaFMQ==&pass_ticket=2xtx8mYo8Af4PGHuhWJL4xRy5s88qyKnPyfX8q8C44g9vA12znnqC4XBTtrpFCVO&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/35b665f1-0f3a-4ede-92a0-96119da1492a/35b665f1-0f3a-4ede-92a0-96119da1492a/)