---
title: PAI - Personal AI Infrastructure（生活操作系统）
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzkwMzY1Mjg5MQ==&mid=224748...]
source_path: 印象笔记管理工具/PAI：把 Claude Code 改造成你的生活操作系统.html
tags: [claude-code, pai, personal-ai, life-os, infrastructure]
updated: 2026-06-27
---

---
title: "PAI：把 Claude Code 改造成你的生活操作系统"
source: evernote
type: note
export_date: 2026-06-25
guid: f8585006-b0c7-4648-882e-47efbb8a9ba1
---

# PAI：把 Claude Code 改造成你的生活操作系统

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkwMzY1Mjg5MQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkwMzY1Mjg5MQ==&mid=2247487243&idx=1&sn=441b83139ceab0d696bfde70ea4da714&chksm=c118a4b44283d4f2c53e002443bde195b45598e7b5fd558db8d3a2b13ca9783e86e4052c9b63&scene=90&xtrack=1&req_id=1779028645315181&sessionid=1779028622&subscene=93&clicktime=1779028938&enterid=1779028938&flutter_pos=71&biz_enter_id=4&ranksessionid=1779028645&jumppath=20020_1779028884390,1102_1779028893570,20020_1779028898061,1104_1779028901419&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQLwoiHGrXJAmHFmvgCRlcvRLTAQIE97dBBAEAAAAAAMETBO05ac8AAAAOpnltbLcz9gKNyK89dVj08XdYyfd1VQujZ5AFBk4fp3V/Jzf+6bPG1QinElB12Pu3enOZ9GQYSF26+YIzyGIf0oY2UhGQV73ng660QmopRaelCypXmKY7CygjKDjDJV3eJUWf93J0auVdaxC43Azes8zRPbUbXl1+zwpvZk03lJKQeDKxcUCtMEVnCim19ADHGH6G9Njtu3n+bC2znel9wzeq+zAR+kB4XyHh8W0plPld6kFqRsHnvLEf5NA=&pass_ticket=yMsPVMcX2mbzWZk+qFu7srQ5xxL5RHcIRVzpXcNR3e6mR8bJOIDbrKtynqF+yWye&wx_header=3)

OriginalwsleepybearGit Trend

**项目卡片**

- **项目**：Personal AI Infrastructure (PAI)[1]
- **状态**：v5.0.0 / 13.4k Star / 8 个月从 0 到万 Star
- **一句话判断**：这是目前最激进的"AI 驱动个人操作系统"实验，适合深度 Claude Code 用户，不适合想快速试水的开发者。

不是另一个 AI 提示词集合

Daniel Miessler，安全领域老兵，此前做过一个叫 Fabric 的 AI 提示词模式集合，在圈内小有名气。他做 PAI 的起点很清晰：Fabric 解决的是"问 AI 什么"，而 PAI 要解决的是"AI 怎么围绕你运转"。

PAI 全称 Personal AI Infrastructure，当前版本 v5.0.0，定位从早期的"Claude Code 脚手架"进化为**生活操作系统（Life Operating System）**。核心主张：AI 应该放大每一个人，而不只是前 1%。

这类口号我通常会先打折扣再看。但翻完仓库里的设计决策，它确实在往这个方向用力。

三层架构：PAI、Pulse、DA

PAI 的架构分三层，每一层解决一个不同的问题：

- **PAI 本体**——操作系统内核。技能系统、记忆系统、执行算法、你的身份文件，全部住在 `~/.claude/` 下面
- **Pulse**——常驻守护进程，监听端口 `31337`。它是生命仪表盘（Life Dashboard），同时承载语音通知、Hook 执行、定时任务、可观测性
- **DA（Digital Assistant）**——你的数字助手。有名字、有声音、有性格。所有交互都通过它，不是直接面对冰冷的系统

这种分层意味着：你面对的是一个有身份的 AI 同事。至少设计意图是这样。

理想状态驱动一切

PAI 和其他 Claude Code 增强方案拉开差距的地方在于一个概念：**Ideal State（理想状态）**。

具体落地形式叫 **ISA（Ideal State Artifact）**，取代了传统的 PRD。一份 ISA 文档包含 12 个固定章节：Problem → Vision → Out of Scope → Principles → Constraints → Goal → Criteria → Test Strategy → Features → Decisions → Changelog → Verification。

ISA 同时承担五种身份：理想状态的表述、测试工具、构建验证、完成条件、唯一事实来源。每个任务、每个项目，都从"当前状态"向 ISA 定义的"理想状态"推进。

我通常会怀疑"多写一层文档"的价值，但 ISA 的定位确实不同——它是 Algorithm 的直接输入，不是给人审阅的中间产物。

算法化执行：七阶段循环

![](attachments/93a8a6b5641e99c5.jpg)

PAI 的核心是一个叫 **Algorithm** 的东西，当前版本 v6.3.0。它把每一个非平凡任务推进一个七阶段循环：

**OBSERVE → THINK → PLAN → BUILD → EXECUTE → VERIFY → LEARN**

不是什么新概念，它本质上是科学方法的结构化表达。但 PAI 把它做成了强制执行的教条（doctrine）：每个阶段有明确的输入输出，验证阶段要求活探针（live-probe），高复杂度任务（E4/E5）还要做跨供应商审计。

更实际的是，PAI 内置了一个 **模式分类器**——用 Sonnet 模型判断每条用户输入应该走哪个模式：MINIMAL（简单回应）、NATIVE（原生执行）、ALGORITHM（完整算法流程）。同时分配努力等级 E1（<90 秒）到 E5（<2 小时+）。分类器结果是硬约束，不是建议。

45 个技能，但不是你想的那种

![](attachments/8d1678e6741f7561.jpg)

PAI v5.0.0 拆出了 45 个公共技能，171 个工作流，37 个 Hook。技能分类覆盖思考（Council、RedTeam、FirstPrinciples）、内容（Art、WriteStory、Fabric）、研究（Research、ArXiv）、代理（Agents、Browser、Interceptor）、构建（ISA、CreateSkill、Prompting）五大领域。

但这些技能的设计哲学值得注意：**代码优先，提示词包装代码**。技能的层级结构是：代码 → CLI 运行代码 → 工作流调用 CLI → SKILL.md 在工作流之间路由。技能是容器，SKILL.md 是入口，实际工作是真正的代码。

此外还有一个"苦丸工程"（BitterPillEngineering）技能——专门审计系统内部的过度提示，判断标准是"更聪明的模型会不会让这条规则变得多余"。随着模型变强，系统本身在缩小。

记忆系统：跨会话复利

![](attachments/2a398c9b820c1e48.jpg)

PAI 的记忆系统（v7.6）按用途分三层，全部存储在 `~/.claude/PAI/MEMORY/` 下：

- **WORK**——`MEMORY/WORK/{slug}/ISA.md`，活跃任务的 ISA，当前工作的现场
- **KNOWLEDGE**——`MEMORY/KNOWLEDGE/{People,Companies,Ideas,Research,Blogs}/`，带类型标签的知识图谱
- **LEARNING**——`MEMORY/LEARNING/`，元模式：信号、抱怨、智慧框架、反思

检索靠 BM25（MemoryRetriever.ts）+ 图遍历（KnowledgeGraph.ts）。Hook 自动将工作产出沉淀为知识——每次任务完成、满意度评分、关系记忆都被捕获并写入对应层级。

这和"每次新会话从头解释背景"的体验截然不同。PAI 的设计意图是：你用得越久，它越懂你。

隐私是结构性的，不是规范性的

v5.0.0 引入了 **Containment Zones**（隔离区）。`containment-zones.ts` 声明每个目录的隐私级别，`ContainmentGuard` Hook 在每次写入操作时检查——如果敏感内容要写到公开区域，直接拦截。

公开发布走两阶段流程：Stage（本地暂存，跑 12 道安全门禁）→ Publish（推送到 GitHub）。两步不会自动链式执行。安全门禁包括：身份信息 grep、Cloudflare ID 扫描、trufflehog 密钥检测、.env 文件残留检查等。

你的 TELOS、身份文件、记忆内容在文件系统层面就被保护了——不用靠"记得不要提交敏感文件"这种自觉性。

实际使用的前置条件

PAI 的依赖不算重，但门槛不低：

1. **Bun 运行时**——系统用 TypeScript + Bun 构建，不用 Node.js
2. **Claude Code**——PAI 是 Claude Code 原生的，不支持其他 AI 编码工具
3. **ElevenLabs API Key**——可选，语音通知功能需要；不提供则退化为桌面通知
4. **macOS 或 Linux**——Windows 不支持，社区贡献中

安装方式有两条路：

```
# 一键安装  
curl -sSL https://ourpai.ai/install.sh | bash  
  
# 手动克隆  
git clone https://github.com/danielmiessler/Personal_AI_Infrastructure.git  
cd Personal_AI_Infrastructure/Releases/v5.0.0  
cp -R .claude ~/  
cd ~/.claude && ./install.sh
```

安装后最重要的步骤是运行 `/interview`——你的 DA 会引导你填写 TELOS（使命、目标、信念、智慧、挑战、叙事）。**没有 TELOS，系统没有优化目标**。

值得警惕的地方

几个现实的考量：

**Claude Code 绑定。** PAI 深度依赖 Claude Code 的 Hook 系统、上下文管理和 Agent 架构。如果你更习惯 Cursor、Windsurf 或 Copilot，PAI 对你来说是不可用的。这不是架构选择可以弥补的——代码里大量直接调用了 Claude Code 特有的 API。

**复杂度爆炸。** 45 个技能、171 个工作流、37 个 Hook、7 阶段算法、12 章节 ISA——这套系统的学习曲线不亚于一门新框架。Daniel 自己也说"PAI 是 AI 来安装和修改的"。如果你想手动理解每一层在做什么，准备投入大量时间。

**快速迭代意味着不稳定。** 仓库从 v2.0.0 到 v5.0.0 只用了 5 个月，每次大版本都有破坏性变更。v4.x 到 v5.0.0 的迁移指南明确写道"这是不同的系统，不是补丁"。我翻 git log 时看到大量目录重组和文件重命名，这种节奏下想保持自定义配置不跑偏，需要持续跟进。

**没有 RAG，靠文件系统。** 这是一个有意的工程取舍——PAI 从 2025 年 6 月起放弃了 RAG，改用富文本交叉引用 + ripgrep 搜索。好处是透明、可审计；代价是当知识库增长到一定规模后，检索质量可能不如向量方案。

谁适合用 PAI

**适合的人：**

- 重度 Claude Code 用户，愿意投入时间配置和定制
- 有明确的个人目标体系，愿意用结构化方式管理生活和工作
- 对"AI 作为基础设施"这个方向有信仰
- 能接受快速迭代带来的不稳定性

**不适合的人：**

- 只想要一个好用的 AI 编码助手——直接用 Claude Code 就好
- 不想花时间理解 45 个技能和 37 个 Hook
- 需要跨平台支持（Windows）
- 团队协作场景（PAI 设计为个人使用）

PAI 目前还是实验性的个人项目，不是企业级解决方案。但它尝试回答的问题很实际：当 AI 能力足够强时，围绕"人"而不是"任务"来组织基础设施，是不是更合理的方向。

13k Star 至少说明，觉得这个方向值得探索的人正在变多。

---

如果这篇对你有用，建议点个关注。我会持续把 GitHub 上值得用的 AI 工具拆成「最短上手闭环 + 坑点清单 + 可复用配置」，让你少走弯路。

### 引用链接

[1]Personal AI Infrastructure (PAI): *https://github.com/danielmiessler/Personal\_AI\_Infrastructure*
