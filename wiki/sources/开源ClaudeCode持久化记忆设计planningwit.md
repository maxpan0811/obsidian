---
title: 开源 Claude Code 持久化记忆设计：planning-with-files 技能详解
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/开源 Claude Code 持久化记忆设计：planning-with-files 技能详解.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "开源 Claude Code 持久化记忆设计：planning-with-files 技能详解"
source: evernote
type: note
export_date: 2026-06-27
guid: 3a926faa-f9ed-4227-b78d-f74005aa54cb
---

# 开源 Claude Code 持久化记忆设计：planning-with-files 技能详解

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5NzA1NzMyOQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ==&mid=2247486649&idx=1&sn=8b083e5bf234869fe886c20836951095&chksm=a706edcee9c440d28e205d35b8aa26fc8d71bf385b056be610ab9f9362632131956878b77c32&mpshare=1&scene=24&srcid=0607jxR8CkJpDIpaLDGKKTZm&sharer_shareinfo=09131461e48c0dbde5b5486cab0914d3&sharer_shareinfo_first=09131461e48c0dbde5b5486cab0914d3&clicktime=1780824610&enterid=1780824610&ascene=14&devicetype=iOS26.5&version=18004a29&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQGoOc6F3zzWFpLL35na7UTBLTAQIE97dBBAEAAAAAAN3kMQVIAW4AAAAOpnltbLcz9gKNyK89dVj0CrRHeUm+a5+l+3cU6vIGxdaTRbr8l57gGV45XmKF4PHaP23iiUPydW+teGJuLFSnbB5LewzpM+m84ZaC167P3QEMp8b+ND/i4Ua1LZGmjUk69mNxqo83ZeX95Ep6Rwwa9RoWuEA6B2yEILCFhaWRp+nmxfUrImHA38+ud+8c7X29oVZnICtrCTwrJt38SrawjZnyK/pa70Og2HfSHvPtY0PUrAGZ7hnYNBSqZ0E=&pass_ticket=rpWzfJE/tXG9S5FauYjuqnGaULdYdJ9LECy6dbpTm6ay9zmU2wQhIuUzfgB/1lxc&wx_header=3)

# 开源 Claude Code 持久化记忆设计：planning-with-files 技能详解

Original兔兔AGI 技术极简主义

 

如果你用 Claude Code 做过稍微复杂一点的开发，大概率都遇到过这些问题：上下文一重置，`TodoWrite` 就消失；工具调用一多，目标开始漂移；错误没有被持续记录，最后上下文越来越重，但真正有用的信息却越来越少。

这些问题并不是使用方式不对，而是当前 AI 编程的结构性痛点。

**planning-with-files** 提供了一条可行的解法：把关键状态写进文件，而不是依赖上下文记忆。

**planning-with-files** 是一个 Claude Code 插件，借鉴了 **Manus** 的设计思路，用持久化的 **Markdown** 文件来做规划、进度跟踪和知识存储。它关注的不是模型能力，而是把文件系统当作稳定的**工作记忆**来使用。

## 核心概念

**planning-with-files** 的核心做法是为每个复杂任务维护**三个文件**：

task\_plan.md      → 拆分任务、规划阶段、追踪进度
findings.md       → 记录调研结果、关键发现与设计决策
progress.md       → 保存会话日志、实验记录和测试结果

### **task\_plan.md：任务主线与控制面板**

这是整个任务中最关键的文件，相当于项目的主控面板，用于明确方向、约束范围，并持续记录关键决策。通常包含以下内容：

- • **目标定义**：明确要解决的问题和预期结果，避免任务范围不断膨胀
- • **阶段拆分（3–7 个）**：将复杂任务拆解为可执行阶段，并为每个阶段维护状态
- • **关键问题清单**：列出当前尚未解决、会影响整体推进的核心问题
- • **决策记录**：记录已做出的技术选择及其理由，便于回溯和复盘
- • **失败尝试记录**：明确哪些方案已经验证不可行，避免重复踩坑

**阶段状态通过复选框维护**：

- • `[ ]` 未开始
- • `[-]` 进行中
- • `[x]` 已完成

### **findings.md：信息与结论的集中存放处**

`findings.md` 用来存放所有阶段性研究结果和客观信息。当你通过 `view`、`browser` 等工具查看代码、网页或文档时，和任务相关的重要内容都应该整理到这里，而不是只存在于上下文里。

通常包括：

- • **需求整理**：从用户描述、Issue 或文档中提炼出的明确需求
- • **研究结论**：对代码结构、架构设计、API 行为等的分析结果
- • **技术选择依据**：为什么选某个方案、放弃另一个方案
- • **问题与对应解决方式**：调试过程中遇到的具体问题及处理方法
- • **参考资源**：相关文档、规范、示例、教程链接
- • **界面 / 页面观察记录**：对网页结构、UI 行为的分析结论（必要时附截图说明）

这里记录的是已经确认过的信息和结论，而不是推测或待办事项。

### **progress.md：会话与操作记录**

`progress.md` 用来记录每一次会话中实际发生了什么，相当于一份连续的开发日志。它关注的是过程，而不是规划或结论。

通常会记录这些内容：

- • **当前阶段**：当时处在哪个阶段，阶段状态是否发生变化
- • **已执行的操作**：具体做了哪些 `Write`、`Edit`、`Bash` 等操作
- • **文件变更记录**：新建、修改或删除了哪些文件
- • **测试与运行结果**：测试、构建、运行、部署的输出结果
- • **错误与异常**：出现过的报错、失败信息及当时的上下文
- • **5-Question 重启检查**：在会话中断或恢复时，用于快速对齐当前状态

**这个文件的核心价值是可追溯性**。当你隔几天再回来，或者换一个会话继续推进时，只要翻一下 `progress.md`，就能快速搞清楚：

之前做到哪一步、为什么停在这里、有哪些问题已经踩过坑。

### 三文件协作机制

在 **planning-with-files** 中，三个文件各自承担不同角色：

- • **task\_plan.md**：定义任务目标和阶段进度，指明「下一步做什么」
- • **findings.md**：存储研究结果、技术决策和发现，回答「已掌握哪些信息」
- • **progress.md**：记录操作日志和测试结果，回答「之前具体做了什么」

通过这种分工，信息组织更高效，也避免了单一文件过于杂乱。

## 工作原理

**planning-with-files** 的核心在于一套自动触发的 Hook 机制。这些 Hook 会在关键节点介入，把原本容易遗漏的步骤自动补齐，减少对人工记忆的依赖。

### 工作循环图解

任务开始 → 创建 task\_plan.md → 创建 findings.md + progress.md
↓
进入工作循环：
  PreToolUse Hook → 读取 task\_plan.md → 刷新目标
  → 执行具体工作
  → PostToolUse Hook → 提醒更新阶段状态
  → 每 2 次查看操作 → 同步更新 findings.md
  → 阶段完成 → 更新 task\_plan.md + progress.md
  → 出现错误 → 记录到两个文件
↓
Stop Hook → 验证完成 → 任务结束

### Hooks 机制说明

| Hook | 触发时机 | 作用 |
| --- | --- | --- |
| **SessionStart** | 会话开始 | 提示插件已生效 |
| **PreToolUse** | 执行 Write / Edit / Bash 前 | 读取 `task_plan.md`，确认当前目标 |
| **PostToolUse** | 执行 Write / Edit 后 | 提醒更新阶段进度 |
| **Stop** | 会话即将结束 | 检查是否还有未完成阶段 |

#### PreToolUse Hook：保持目标一致

这是最关键的一个 Hook。在每次执行 `Write`、`Edit` 或 `Bash` 之前，它都会先读取 `task_plan.md`，把当前任务目标重新同步进上下文。

这样一来，即使工具调用次数很多，AI 也不容易偏离最初的目标，从根本上缓解了「目标漂移」的问题。

#### PostToolUse Hook：阶段状态提醒

在完成 `Write` 或 `Edit` 操作后，这个 Hook 会提醒你检查当前阶段是否已经完成，并在必要时更新 `task_plan.md` 中对应的状态标记。

#### Stop Hook：任务完成验证

在结束工作前，Stop Hook 会检查 `task_plan.md` 中所有阶段是否都标记为完成。如果发现有未完成的阶段，它会提醒你继续处理，确保没有遗漏。

### 2-Action 规则

每进行**两次查看类操作**（view / browser / search）后，必须把发现更新到 `findings.md`。

操作1: WebSearch → 记录结果
操作2: WebFetch → 立即更新 findings.md
操作3: Read file → 记录发现
操作4: Grep search → 立即更新 findings.md

**为什么每两次**？因为查看类操作产生的信息很多，如果不及时保存，容易被上下文覆盖。通过每两次操作强制同步，可以保证所有重要发现都被记录。

这种规则配合 Hooks 使用，形成了一个自动化工作流，让你专注做任务，而不必担心遗漏重要信息。

### **Manus 原则**

**planning-with-files** 的设计体现了 **Manus** 的五大核心原则：

| 原则 | 实现 |
| --- | --- |
| **文件系统即记忆** | 所有重要信息存储在三个 Markdown 文件中，而不是依赖易失的上下文 |
| **注意力操作** | 每次操作前，PreToolUse Hook 会重新读取任务计划 |
| **错误持久化** | `task_plan.md` 中记录每次失败尝试，避免重复犯错 |
| **目标追踪** | 通用复选框实时显示各阶段进度，确保任务清晰可控 |
| **完成验证** | Stop Hook 会在任务结束时检查所有阶段是否完成 |

总的来说，这套设计就是把易失的上下文信息变成**可追踪、持久的文件系统记忆**。

## 快速上手

安装很简单，不需要额外的配置，也没有复杂的依赖。

整个过程在 Claude Code 里完成，只要两步。

### 步骤一：把插件加入市场

在 Claude Code 的终端中执行：

/plugin marketplace add OthmanAdi/planning-with-files

### 步骤二：安装插件

/plugin install planning-with-files@planning-with-files

安装完成后，重启 Claude Code，就可以使用了。

![](attachments/16c701434184432e.png)

## 实战示例

下面通过一个完整示例，展示 **planning-with-files** 在实际项目中的使用方式。

### 任务描述

构建一个简单的Python命令行todo应用，支持添加、列出和删除任务。

### Phase 1：初始化规划

运行 `/planning-with-files:plan` + 任务描述

![](attachments/2f619eee971f67da.png)

首先生成 `task_plan.md`，用于定义任务目标和阶段划分。

![](attachments/17f8d01ebacccf0c.png)

同时创建 `findings.md` 和 `progress.md`，分别用于记录研究发现和执行过程。

### Phase 2：研究与发现

进入研究阶段后，开始调研 Python CLI 的常见实现方式，并在每完成两次查看操作后，将关键信息整理并写入 `findings.md`。

![](attachments/b0051bba09bfde04.png)

同时更新 `task_plan.md` 的阶段状态：Phase 1 和 Phase 2 标记为 [x]，Phase 3 标记为 [-]，用于反映当前进度。

### Phase 3：实施与错误处理

在实现过程中，所有错误和调试过程都会记录在 `progress.md` 中，包括具体操作和失败原因。

![](attachments/a498821a349c3be2.png)

这种做法可以保留完整的执行轨迹，避免问题被遗忘或重复出现，也方便后续排查和迭代。

### Phase 4：完成验证

当所有阶段完成后，`task_plan.md` 中的复选框都会标记为 [x]。

![](attachments/29e4f4e263a37d57.png)

此时，Stop Hook 会检查各阶段状态，确认任务已全部完成，作为本次工作的结束条件。

![](attachments/bd6565d1a360c880.png)

### 文件演变总结

- • **task\_plan.md**：复选框从 `[ ]` 到 `[x]`，清晰展示任务推进过程
- • **findings.md**：从空白逐步积累为完整的研究和决策记录
- • **progress.md**：持续补充测试结果和错误日志，完整还原执行过程

这个示例展示了三文件模式如何让复杂任务变得**可控、可追踪、可恢复**，从而让整个开发过程更加透明、高效。

## **适用场景与最佳实践**

### 什么时候使用？

**✅ 推荐使用的场景**：

- • **多步骤任务**：任务包含三个或更多阶段
- • **研究型任务**：需要查阅文档、调研或对比方案
- • **构建项目**：从零搭建系统或功能模块
- • **频繁工具调用**：涉及大量 `Read`、`Write`、`Edit` 操作
- • **跨会话任务**：需要在多个会话中持续推进的长期任务

**❌ 不适用的场景**：

- • **简单问答**：只需快速得到答案的问题
- • **单文件编辑**：仅修改一个文件的情况
- • **快速查找**：简单搜索或浏览信息

### 关键规则

1. 1. **先创建 task\_plan.md**：这是整个流程的核心，绝不可跳过
2. 2. **严格执行 2-Action 规则**：每两次查看操作后，必须立即更新 `findings.md`
3. 3. **记录所有错误**：无论错误是否已解决，都要保留，避免重复犯错
4. 4. **避免重复失败**：对每次失败尝试做详细记录，下次使用不同方案

### 会话恢复机制

上下文窗口有限。大量工具调用后，窗口可能被填满，这时需要运行 `/clear` 命令来清空上下文，以便继续工作。

#### 问题场景

传统使用 `/clear` 时，如果工作内容未同步，所有上下文都会丢失，AI 会忘记之前做了什么，你需要重新说明背景。

**planning-with-files** 提供了会话恢复机制，可以保留关键信息，避免重复工作。

#### 恢复机制

再次运行 `/planning-with-files` 时，技能会自动处理之前的会话数据：

1. 1. **检测上一次会话**：查找 `~/.claude/projects/` 中的会话信息
2. 2. **定位规划文件**：获取 `task_plan.md`、`findings.md`、`progress.md` 的最后更新时间
3. 3. **提取丢失上下文**：抓取规划文件更新后的对话内容
4. 4. **显示追赶报告**：列出自上次更新后的所有活动

即便上下文窗口已满、规划文件未及时更新，技能也能在下一次会话中自动恢复丢失的信息。

#### 最佳实践工作流

为了充分利用会话恢复功能，推荐以下流程：

1. 禁用 auto-compact，以使用完整上下文窗口
2. 启动新会话
3. 运行 /planning-with-files
4. 持续工作直到上下文填满（Claude 会发出警告）
5. 运行 /clear 清空上下文
6. 再次运行 /planning-with-files → 自动恢复之前的状态

#### 禁用 Auto-Compact 配置

为了充分利用上下文窗口，建议关闭自动压缩功能：

// .claude/settings.json
{
  "autoCompact": false
}

关闭后，你可以手动决定何时清空上下文，不必担心信息丢失，**planning-with-files** 会自动恢复尚未同步的工作内容。

## 总结与展望

**planning-with-files** 将任务状态和关键信息持久化到文件系统，为解决 AI 编程中的上下文管理问题提供了可行方案，同时针对常见痛点提出了具体改进。

- • **上下文易失** → 关键信息落盘，避免随会话丢失
- • **目标漂移** → 持续对齐任务计划，保持执行方向
- • **错误重复** → 保留失败记录，减少重复试错
- • **上下文浪费** → 上下文只承载当前必要信息

在复杂或长期项目中，这种方式可以明显提升任务的可控性和可追溯性。

**既然看到这里了，如果觉得有启发，随手点个赞、推荐、转发三连吧，你的支持是我持续分享干货的动力。**

推荐阅读：[开源 Claude Code 编程宝藏搭档 Oh My Claude Code 完整上手攻略](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ==&mid=2247486606&idx=1&sn=1b132d9e0db262123da1a0ac868af6de&scene=21#wechat_redirect)


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ==&mid=2247486649&idx=1&sn=8b083e5bf234869fe886c20836951095&chksm=a706edcee9c440d28e205d35b8aa26fc8d71bf385b056be610ab9f9362632131956878b77c32&mpshare=1&scene=24&srcid=0607jxR8CkJpDIpaLDGKKTZm&sharer_shareinfo=09131461e48c0dbde5b5486cab0914d3&sharer_shareinfo_first=09131461e48c0dbde5b5486cab0914d3&clicktime=1780824610&enterid=1780824610&ascene=14&devicetype=iOS26.5&version=18004a29&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQGoOc6F3zzWFpLL35na7UTBLTAQIE97dBBAEAAAAAAN3kMQVIAW4AAAAOpnltbLcz9gKNyK89dVj0CrRHeUm+a5+l+3cU6vIGxdaTRbr8l57gGV45XmKF4PHaP23iiUPydW+teGJuLFSnbB5LewzpM+m84ZaC167P3QEMp8b+ND/i4Ua1LZGmjUk69mNxqo83ZeX95Ep6Rwwa9RoWuEA6B2yEILCFhaWRp+nmxfUrImHA38+ud+8c7X29oVZnICtrCTwrJt38SrawjZnyK/pa70Og2HfSHvPtY0PUrAGZ7hnYNBSqZ0E=&pass_ticket=rpWzfJE/tXG9S5FauYjuqnGaULdYdJ9LECy6dbpTm6ay9zmU2wQhIuUzfgB/1lxc&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/3a926faa-f9ed-4227-b78d-f74005aa54cb/3a926faa-f9ed-4227-b78d-f74005aa54cb/)
