---
name: claude-code-ch8-subagent
type: source
tags: [claude-code, tutorial]
source_path: 印象笔记管理工具/法律人的Claude Code教程（八）（教不会我吃民法典！）：Subagent—让 Claude Code学会分身术.md

updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "法律人的Claude Code教程（八）（教不会我吃民法典！）：Subagent—让 Claude Code学会分身术"
source: evernote
type: note
export_date: 2026-06-27
guid: 83ec8932-6c20-4ff0-8d2c-aa8e6c566d69
---

# 法律人的Claude Code教程（八）（教不会我吃民法典！）：Subagent—让 Claude Code学会分身术

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485884&idx=1&sn=7fa4c3caf83f5e75a8d89a4125d859fd&chksm=c2547a61f523f3776c54b06ce5a4c1eebd39b000027ab6b281fd0bd009830b170b411cf71451&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDPRGr+U8Z5R8G73gKRtMFBLVAQIE97dBBAEAAAAAACSFJfsuxDwAAAAOpnltbLcz9gKNyK89dVj0m+L8/4f/gtwq1LjZLyfmgpqQVz8s606iezPUDzSYWM2AH+DSRdWcB3WHbpUgxKxhfCYfUZZS/UJvTfczNwOkYr433fjD8KMw+jBRXE0SR5idhMP2tyVUOfF20RA3HsTnWnDrloYRtFhMdSyyNRBI6lfQbCclWtR69abk7PXXW6Rg12utAlq5GbtIM0EdYR38VFuEfPg4z5FcXkxTIkkY2A5sdU9dfZSLJnJVe0fNMQ==&pass_ticket=VKIM36tq/aVuq0CbzUOJe3P4qM6UnLRxVgrotVvKZ/ci4lV9AJkZJNpBuLgqPmIy&wx_header=3)

# 法律人的Claude Code教程（八）（教不会我吃民法典！）：Subagent—让 Claude Code学会分身术

Original两眼一睁就是学呀 智律积成

经过了前几篇的学习，你已经掌握了一套完整的工作方法体系：

教程五=MCP → 教Claude Code使用外部工具

教程六 = Skills → 教 Claude Code按你的方式做事

教程七 = Hooks → 设规则让 Claude Code自动执行

但到目前为止，你的 Claude Code 还只是"一个人"在干活。

**问题是**：一个人的精力是有限的。

- 审查一份大型合同，要查主体、看条款、核法条、检索类案……一个人忙不过来
- 尽职调查要同时查股权、查诉讼、查资质、查许可证……一个个来太慢
- 批量处理几十份文书，一个人从头做到尾，效率上不去

***这时候，你需要的不只是一个助手，而是一个助手团队。***

---

## 什么是 Subagent？

先说一句人话版结论：

**Subagent 就是在主对话中派生出的独立 AI 助手。**

每个 Subagent 有自己的：

- 独立上下文 — 不占用主对话的"脑容量"
- 独立工具权限 — 可以只读、只写、或只用特定工具
- 独立系统提示 — 可以有自己的"人设"和专长
- 独立模型选择 — 简单任务用便宜的 Haiku，复杂任务用 Opus

用个类比来说：你是一个律所合伙人，Claude Code 是你的 junior 律师。以前你只有一个 junior，现在你可以派生出多个专门化的 junior，各司其职。

![](attachments/c1e3db270f0bc3bf.png)

那这东西到底能解决什么问题？

| 问题 | 没有 Subagent | 有 Subagent |
| --- | --- | --- |
| 尽职调查要查好几件事 | 一个个来，耗时长 | 派多个 Agent 并行查 |
| 审查合同时要搜索大量文件 | 主对话上下文爆了 | 用只读 Agent 搜索，结果返回 |
| 简单任务也用 Opus | 成本高 | 简单任务路由到 Haiku，省钱 |
| 需要固定工作流的审查 | 每次都要重新说一遍 | 写成一个 Agent，一键调用 |

---

## 先看一个实际效果

我们先不讲怎么创建，先看 Subagent 跑起来是什么样的。

场景：一份 200 页的合同，需要全面审查。我提前创建了三个审查 Agent，分别负责主体信息、业务条款和法律条款。

![](attachments/a14a782eee8c70d8.png)

相当于三个人（Agents）一起做一个工作，如果是一个人（Agent）来做这个工作，上下文很有可能不精准，最终导致交付效果不好。现实中也是这样，一个律师独立负责一个大型任务，耗时更长，质量不一定好，而团队协作通常是更好的选择。

我只需要说一句话。

然后三个 Agent 同时工作，各看各的部分。

![](attachments/08b5f10296275212.png)

最终由主Agent向我汇报结果。

![](attachments/5debbb7a0409d2e1.png)

效果对比：

| 维度 | 不用 Subagent | 用 Subagent |
| --- | --- | --- |
| 时间 | 时间较长 | 节约时间 |
| 上下文 | 主对话爆了 | 各自独立 |
| 漏项风险 | 高（疲劳漏看） | 低（分工明确） |

看到效果了，我们来看怎么做到的。

---

## 内置的 Subagent

其实你不需要创建任何东西，Claude Code 自带几个开箱即用的 Subagent，输入“/agent”可以查看：

| Agent | 模型 | 工具权限 | 用途 |
| --- | --- | --- | --- |
| **Explore** | Haiku（快速） | 只读 | 搜索文件、探索代码库 |
| **Plan** | 继承主对话 | 只读 | Plan Mode 下的研究与规划 |
| **General-purpose** | 继承主对话 | 全部工具 | 复杂研究、多步操作、代码修改 |

![](attachments/aa216e37f5ee40a7.png)

使用起来很简单：

你：用 Explore agent 搜索这个项目中的所有合同
Claude：(自动派生 Explore，用 Haiku 快速搜索)
       → 搜索完成，把结果返回给你

![](attachments/0644d0537b370437.png)

这些内置 Agent 已经能满足很多基础需求。

但真正发挥 Subagent 威力的，是**创建你自己专门的 Agent**。

---

## 创建你的第一个 Subagent

有三种方式，我按推荐程度排序。

### 方式一：交互式创建（推荐）

1. 在 Claude Code 中输入 `/agents`

![](attachments/3c9d0ea3d92c6c46.png)

2. 选择 **Create new agent**

![](attachments/e01275eb41eed0cd.png)

3. 选择作用域：

- **User-level** → 所有项目都能用（保存到 `~/.claude/agents/`）
- **Project-level** → 仅当前项目能用（保存到 `.claude/agents/`）

4. 选择 **Generate with Claude**，用自然语言描述你想要的 Agent

![](attachments/fbf3d9562d5e951e.png)

5. 选择工具权限

![](attachments/ffc4befdf858b124.png)


6. 选择模型（Haiku / Sonnet / Opus）

![](attachments/fdc7a5a49a4ec03f.png)


6. 选择背景色（用于区分）

![](attachments/b6c1bbe86060117a.png)


6. 配置 memory

![](attachments/56a7502df0cb2958.png)


6. 保存

![](attachments/69d0ce7f7e85dc10.png)

整个过程是交互式的，你不需要记住任何技术细节。

### 方式二：手动创建（Markdown 文件）

我们在刚刚的方式中，就创建了一个 Agent，体现为一个 md 文档。

![](attachments/7a80266e58eb22f3.png)![](attachments/96cd1845b3494716.png)

我们之前对话中的很多内容，都会体现在这个 md 文档中。但是，还是有很多内容需要调整，具体需要如何调整，可以看下一节的配置详解。

或者，我们也可以手动在 `~/.claude/agents/` 目录下创建一个 `.md` 文件：

markdown

---
name: contract-reviewer
description: 审查合同的法律风险，标注高/中/低风险等级
tools: Read, Grep, Glob
model: sonnet
---
你是一个合同审查专家。审查合同时：
1. 检查主体资格是否有效
2. 检查权利义务是否对等
3. 检查违约责任是否平衡
4. 每个问题标注风险等级（高/中/低）
5. 给出具体的修改建议

**文件结构**：

- YAML frontmatter（`---` 包围的部分）→ 配置
- 正文内容 → 系统提示（system prompt）

具体含义后面会进一步解释。

### 方式三：CLI 内联定义（临时使用）

如果你不想创建文件，也不想走交互式流程，可以直接在启动 Claude Code 时定义一个临时 Agent：

bash

claude --agents '{
  "快速审查员": {
    "description": "快速审查合同风险",
    "prompt": "你是合同审查专家...",
    "tools": ["Read", "Grep"],
    "model": "haiku"
  }
}'

这个 Agent 只在当前会话中有效，关闭就没了。适合临时需要一个专门助手，但又不值得专门创建文件的场景。

建议知道就行，不学～

---

## 配置详解：两个关键设置

Subagent 的配置项不少，但真正需要你关心的，就两个：**工具权限**和**模型选择**。

### 工具权限控制

| 配置 | 含义 | 适用场景 |
| --- | --- | --- |
| `tools: Read, Grep` | 白名单：只能用 Read 和 Grep | 审查类任务（只读不改） |
| `disallowedTools: Write, Edit` | 黑名单：除 Write、Edit 外都能用 | 大部分工作，但禁止改文件 |
| 省略 `tools` 字段 | 继承主对话的全部工具 | 信任 Agent 的任务 |

需要你根据这个agent具体的工作来选择。

或者我建议，你可以直接与Claude Code对话，与它讨论出具体的工具权限。

### 模型选择

| 值 | 说明 | 适合场景 | 成本 |
| --- | --- | --- | --- |
| `haiku` | 最快最便宜 | 搜索、分类、简单提取 | 低 |
| `sonnet` | 平衡 | 大多数任务 | 中 |
| `opus` | 最强 | 复杂推理、疑难案件分析 | 高 |
| `inherit` | 继承主对话 | 默认 | 跟随主对话 |

**成本优化建议**：简单查询类任务用 Haiku，够用；复杂分析类任务用 Sonnet 或 Opus，别省。

### 完整配置参考

上面说的是最常用的两项。如果你用手动创建方式（Markdown 文件），完整的配置模板如下：

yaml

---
name:my-agent*# 必填。唯一标识符（小写字母+连字符）*
description:...*# 必填。什么时候应该调用这个 Agent*
tools:Read,Glob,Grep*# 可选。允许的工具列表（省略=继承全部）*
disallowedTools:Write,Edit*# 可选。禁止的工具列表*
model:sonnet*# 可选。sonnet / opus / haiku / inherit（默认）*
permissionMode:default*# 可选。权限模式*
maxTurns:20*# 可选。最大对话轮次*
skills:*# 可选。预加载的 Skill 列表*
-api-conventions
-error-handling-patterns
mcpServers:*# 可选。MCP 服务器配置*
-server-name
hooks:*# 可选。生命周期 Hook*
PreToolUse:...
PostToolUse:...
memory:user*# 可选。持久记忆范围*
background:true*# 可选。是否始终作为后台任务运行*
isolation:worktree*# 可选。设为 worktree 可隔离 git 工作区*
---
这里是系统提示内容（systemprompt）。
可以写多行，支持Markdown格式。

大部分时候，你只需要填写前面几个字段就够了，后面的都是高级选项。

仅作为参考，希望这个不要把你劝退。

---

## 前台 vs 后台

Subagent 可以在前台运行，也可以在后台运行。

**前台运行（默认）**：阻塞主对话，等 Subagent 完成。适合需要立即看结果的任务。

**后台运行**：不阻塞主对话，可以同时做其他事。适合耗时长、不需要交互的任务。

操作很简单：当你派生一个 Agent 去做耗时任务（比如批量处理文件），随时可以按 **Ctrl+B** 把它转到后台，自己继续做别的事。

---

## 还能用在哪些场景？

开头展示的合同分模块审查只是一个例子。Subagent 在法律工作中还有很多用法：

| 场景 | 怎么做 | 说明 |
| --- | --- | --- |
| **尽职调查** | 派4个 Agent 并行查（工商、司法、资产、资质） | 以前一天的活，现在半小时 |
| **批量文书格式统一** | 派多个后台 Agent 并行处理 | 50 份起诉状同时整理 |
| **证据目录生成** | 派 Agent 阅读证据文件 | 自动提取关键信息，生成目录 |
| **案件材料梳理** | 派 Plan 模式 Agent | 新案卷快速输出结构化摘要 |
| **类案并行检索** | 派多个查询 Agent | 不同性质类案同时查 |
| **合同新旧版本比对** | 派 Agent 逐条比对 | 标注所有修改，判断有利/不利/中性 |
| **合同一页纸摘要** | 派 Haiku Agent | 合伙人没时间看全文，一页纸搞定 |

创建思路很简单，先想清楚"要做什么"，然后选对工具权限。

具体如何配置，法律人最好的方式就是与Claude Code对话。

## 如何设计Agent：几种常见的模式

设计 Agent 不只是设计单个 Agent，更是设计**它们如何协作**。

以下是 Subagent 最常用的三种协作模式，都是 Claude Code 现成支持的。

---

### 模式一：并行执行

**场景**：一份 200 页的合同，需要同时审查主体、业务、法律三个模块。

**设计思路**：派三个 Agent 同时干活，各看各的，最后汇总。

主对话
  │
  ├── 主体审查员 (entity-reviewer)
  ├── 业务审查员 (business-reviewer)
  └── 法律审查员 (legal-reviewer)
  │
  └── 汇总结果

**怎么用**：

这份合同太长，派三个审查员并行审查

**适用**：任务可以拆分、互相独立、不需要等待彼此。

---

### 模式二：流水线

**场景**：先检索类案，再提取裁判观点，最后生成代理词。

**设计思路**：上一个 Agent 的输出是下一个 Agent 的输入，顺序执行。

类案检索 Agent → 观点提取 Agent → 代理词生成 Agent
   (输出案例)      (输出观点)        (输出文书)

**怎么用**：

1. 先检索相关案例
2. 基于这些案例提取裁判观点
3. 根据观点生成代理词

**适用**：任务有明确先后顺序，每一步的输出是下一步的输入。

---

### 模式三：分支选择

**场景**：案件进来，先判断是民事/刑事/行政，再分发给专门的 Agent。

**设计思路**：根据条件把任务分发给不同的"执行者"。

案件分类 Agent (调度员)
  │
  ├── 民事 → 民事 Agent
  ├── 刑事 → 刑事 Agent
  └── 行政 → 行政 Agent

**怎么用**：

先判断案件类型，然后分给对应的专业 Agent 处理

**适用**：任务有多种类型，每种类型需要不同的处理方式。

---

### 选择决策树

不知道用哪种模式？按这个流程来：

任务可以同时进行吗？
├─ 可以 → 并行执行
└─ 不可以 → 有明确顺序吗？
            ├─ 有 → 流水线
            └─ 没有 → 分支选择

---

### 更复杂的协作？

如果任务需要多个 Agent 互相商量、共享信息，那就进入 **Agent Teams** 的领域了。

大多数法律场景，这三种模式就够用了。

---

## Agent Teams：从"助手"到"团队"

前面讲的 Subagent，本质上还是"你指挥，Agent 干活，结果汇报给你"。

Agent Teams 更进一步：**多个 Agent 之间可以直接互相通信、协商、分工**。

*Agent Teams 目前是实验性功能，默认禁用。*

### 和 Subagent 有什么区别？

| 维度 | Subagent | Agent Teams |
| --- | --- | --- |
| **通信** | 只向你汇报 | 队友之间可以直接通信 |
| **协调** | 你管理所有工作 | 共享任务列表，自协调 |
| **适合** | 聚焦任务，只要结果 | 复杂工作，需要讨论协商 |
| **成本** | 较低 | 较高 |

大多数场景下，Subagent 就够用了。Agent Teams 适合特别复杂的任务，比如模拟法庭辩论、多方交易博弈这类需要不同"立场"互相碰撞的场景。

借用官方的图来解释：

![](attachments/356db988ba0127fc.png)

### 怎么启用？

跟 Claude Code 说一句话就行：

帮我在 settings 里启用 AgentTeams

或者手动在 `~/.claude/settings.json` 中添加：

json

{
"env":{
"CLAUDE\_CODE\_EXPERIMENTAL\_AGENT\_TEAMS":"1"
}
}

### 怎么用？

自然语言描述角色和任务就行：

你：创建一个模拟法庭团队，3个队友
  分配角色：
- 队友A 扮演原告律师
- 队友B 扮演被告律师
- 队友C 扮演法官
  让他们就这个案件进行辩论，最后给出裁判意见

以下是部分过程展示：

![](attachments/73787d3790de7f2b.png)![](attachments/fb15cfbd2b4ebf05.png)![](attachments/aa64840c1aa08624.png)![](attachments/70a3097b2a0ad3e4.png)![](attachments/8c0991319e7f7eed.png)![](attachments/a7c97bf97d13ad9a.png)![](attachments/5b46b0fe065f82b8.png)

### 什么时候值得用？

大多数场景 Subagent 就够了。Agent Teams 适合这类任务：

| 场景 | 为什么用 Teams |
| --- | --- |
| **模拟法庭辩论** | 原/被告/法官三种立场互相对抗 |
| **复杂并购尽调** | 财务/法务/业务/税务并行交叉验证 |
| **多方争议调解** | 不同利益方各自主张，需要协商 |
| **竞品策略分析** | 多个竞争对手，分头研究再比对 |

判断标准：**需要不同"立场"互相碰撞**。

### 当前限制

毕竟是实验性功能，有些限制要知道：

| 限制 | 影响 |
| --- | --- |
| **成本较高** | 每个队友独立计费，token 消耗翻倍 |
| **稳定性** | 实验性功能，可能有 bug |

*如果只是简单的并行执行（像开头的合同审查），Subagent 更划算。*

---

## 何时用什么：一张图搞清楚

学完前几篇，你手头有好几个工具了。什么时候用什么？

需要"一直记住" → CLAUDE.md（岗位说明书）
需要"外部工具" → MCP（神兵利器）
需要"一键调用" → Skill（招式手册）
需要"自动执行" → Hook（规章制度）
需要"分身干活" → Subagent（分身术）
需要"团队协作" → Agent Teams（团队）

---

## 高级话题（了解即可）

有两个话题，大多数法律人用不上，了解一下就行。

**Headless 模式**（`-p` 参数）：不打开交互界面，直接用命令行处理。

**Agent SDK**：把 Claude Code 的能力嵌入到你自己的程序中。适合有编程需求的场景。

---

## 小结

| 要点 | 说明 |
| --- | --- |
| **Subagent = 派生专门助手** | 独立上下文、独立工具、独立模型 |
| **内置 Agent 直接用** | Explore、Plan、General-purpose |
| **自定义 Agent 三种方式** | `/agents` 交互式、Markdown 文件、CLI 参数 |
| **工具权限要控制** | 只读 Agent 用于审查，全权限用于执行 |
| **前后台切换** | Ctrl+B 转后台 |
| **Agent Teams 实验性** | 多 Agent 协作，适合复杂任务 |

真正让 Subagent 发挥价值的，不是技术细节，而是**工作方式的变化**。以前你是一个人从头做到尾，现在你可以分工协作，把不同模块交给不同的专门助手，自己只管最终的判断和决策。

---

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485884&idx=1&sn=7fa4c3caf83f5e75a8d89a4125d859fd&chksm=c2547a61f523f3776c54b06ce5a4c1eebd39b000027ab6b281fd0bd009830b170b411cf71451&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQDPRGr+U8Z5R8G73gKRtMFBLVAQIE97dBBAEAAAAAACSFJfsuxDwAAAAOpnltbLcz9gKNyK89dVj0m+L8/4f/gtwq1LjZLyfmgpqQVz8s606iezPUDzSYWM2AH+DSRdWcB3WHbpUgxKxhfCYfUZZS/UJvTfczNwOkYr433fjD8KMw+jBRXE0SR5idhMP2tyVUOfF20RA3HsTnWnDrloYRtFhMdSyyNRBI6lfQbCclWtR69abk7PXXW6Rg12utAlq5GbtIM0EdYR38VFuEfPg4z5FcXkxTIkkY2A5sdU9dfZSLJnJVe0fNMQ==&pass_ticket=VKIM36tq/aVuq0CbzUOJe3P4qM6UnLRxVgrotVvKZ/ci4lV9AJkZJNpBuLgqPmIy&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/83ec8932-6c20-4ff0-8d2c-aa8e6c566d69/83ec8932-6c20-4ff0-8d2c-aa8e6c566d69/)
