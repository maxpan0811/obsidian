---
title: Claude Dynamic Workflows 完整教程
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzE5MTYyNjQzMg==&mid=224748...]
source_path: 印象笔记管理工具/Anthropic 最强功能：Claude Dynamic Workflows 完整教程（含提示词）.html
tags: [claude, dynamic-workflows, subagent, orchestration]
updated: 2026-06-27
---

---
title: "Anthropic 最强功能：Claude Dynamic Workflows 完整教程（含提示词）"
source: evernote
type: note
export_date: 2026-06-26
guid: 0aa3ecf1-a38a-4f15-8992-8abc8ece6097
---

# Anthropic 最强功能：Claude Dynamic Workflows 完整教程（含提示词）

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzE5MTYyNjQzMg==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzE5MTYyNjQzMg==&mid=2247486683&idx=1&sn=fa02d74e8f4ad736003999c4b87516fe&chksm=97251557f83bc7b47bbb6f0c7175d69bbb187b8b42f84a4df5b2de2da2399d9fd81e7c6b45e4&scene=90&xtrack=1&req_id=1780583475209848&sessionid=1780583470&subscene=93&clicktime=1780583886&enterid=1780583886&flutter_pos=36&biz_enter_id=4&ranksessionid=1780583475&jumppath=1001_1780583469117,1104_1780583471046,20020_1780583474665,1104_1780583799552&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a26&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ6x9UnKluZbO4lPL/U81ayBLTAQIE97dBBAEAAAAAALFTL6ukK2EAAAAOpnltbLcz9gKNyK89dVj0If/1rMgTS8auZXz9GH5lC61SHAEFvJSNzWO6ZKatic2CHa4q+pNV/UerHlse95l3u0OUNVuqbTC2Zd+grCAJlGDPmsETZddLhxTGIU5bmKx4zo2LdkLWW/4vR97trkLVdV/sYMNv+Cj8TogWK5sp4CViS7sV70Gtulxl5BWsyf4Gj6lTjYjUK/qWL7I5+nZyrOusZimskhxTdUO1glXXVcGKEEnqWY99KkCSsGY=&pass_ticket=zevPIj1nXti//KffJGUokn3Co3KegbZ2rbjuXuLUgqEJ7K6HJDReIlOUGrckQlWh&wx_header=3)

CNMAI 伊捏捏的脑洞集市

很多人刷到 Claude 4.8 更新就直接划走了——因为 Opus 4.8 的 benchmark 太亮眼了。

但真正能让你的 **Claude Code 生产力起飞 5-10 倍** 的，是这个被大多数人忽略的 **Dynamic Workflows**（动态工作流）。

它是让 Claude **自己编写 JavaScript 编排脚本**，在后台并行调用数十到数百个子代理（subagents），互相交叉验证、自我纠错，还能把整个流程保存成可复用的斜杠命令。

本文基于 Anthropic 最新 Claude Code 功能和真实使用经验，给你最完整的技术原理、启动方式、监控保存全流程，以及内容创作者实用的提示词模板。读完就能上手。

## **目录**

一、Dynamic Workflows 到底是什么？核心原理

二、三种启动方式（最新触发技巧）

三、实时监控与保存复用（必学操作）

四、实战案例 + 可直接复制的提示词

五、5 个高级技巧和避坑指南

六、总结和行动建议

### 一、Dynamic Workflows 到底是什么？核心原理

![](attachments/60956ca9e32eb9cf.png)

Anthropic 官方定义：

❝

A dynamic workflow is a JavaScript script that orchestrates subagents at scale. Claude writes the script for the task you describe, and a runtime executes it in the background while your session stays responsive.

**解释**：

Claude 会根据你的任务描述，自动生成一个 JS 脚本。这个脚本把大任务拆成多个阶段，分配给不同的子代理并行执行。代理之间可以互相”挑刺“（ adversarial review ），结果不一致就重新验证。

整个过程在后台运行，你的会话界面保持响应，还支持中途暂停和恢复。

![](attachments/c47ca1f2d2527b9d.png)

**它能做到但传统方式做不到的 4 件事**：

1. **并行扇出（Fan Out）**：一个任务拆成 10-100+ 个子任务同时跑，而不是串行等待。
2. **自我验证机制**：代理互相交叉验证，大幅降低幻觉和错误。
3. **可恢复（Resumable）**：长任务（几小时甚至几天）可以暂停，之后继续。
4. **可复用编排**：优秀的 workflow 可以保存成 `/your-command`，下次直接调用相同逻辑。

**与 Skills、MCP/Connectors 的本质区别**（很重要）：

- **Skills**：教 Claude「怎么做」它已经会的事（SOP 化）。
- **MCP / Connectors**：给 Claude 接入外部工具和实时数据。
- **Dynamic Workflows**：**协调整个团队**去完成单次对话或单技能搞不定的大规模复杂任务。

例如你写一篇深度研究报告。

Skills 负责结构和润色，Connectors 拉取最新数据，而 Dynamic Workflows 可以同时调用几十个来源搜索、多个代理交叉验证事实、过滤噪声，最后输出带引用、高可信度的报告。

### 二、三种启动 Dynamic Workflows 的方式

**方式1：手动触发（最灵活，推荐新手先用这个）**

在 prompt 中直接包含 **workflow** 关键词（或根据最新更新，使用 `use a workflow for this` / `create a workflow`）。

Claude 会立即切换到编排模式：

- 分析任务并生成阶段计划
- 展示给你看，请求批准
- 后台启动多个代理并行执行

**小贴士**：如果不想每次都触发，可在 `/config` 里关闭 Workflow keyword trigger，或按 **Alt + W** 临时忽略。

**方式2：使用内置**`/deep-research`**（最推荐入门）**

直接输入：

`/deep-research [你的研究问题]`

它会自动并行搜索多个来源、交叉验证每个主张、过滤不可靠信息，最后输出带引用来源的结构化报告。适合每天做市场情报、竞品分析、AI 工具研究。

**方式3：Ultracode 自动模式（最强大）**

运行：

`/effort ultracode`

开启后，Claude 会为每个有实质性的任务**自动规划并执行 workflow + 高推理努力**。

注意：token 消耗会明显增加，适合重要任务。

❝

推荐一个自用的 Claude Pro 订阅升级服务(稳定正规，操作简单)：**cnmClaude.com**

### 三、实时监控与保存复用（最核心的操作）

工作流启动后，输入：

`/workflows`

打开实时进度面板，可看到：

- 每个阶段（phase）
- 当前运行的代理数量
- Token 消耗情况
- 已用时间

**面板内快捷键**（非常实用）：

- `p`：暂停 / 恢复
- `x`：停止选中代理或整个 workflow
- `r`：重启某个代理
- `s`：**保存当前脚本为可复用命令**（最重要！）
- `Enter`：深入查看某个代理的 prompt、工具调用和结果

**保存 workflow**：按 `s` 后可保存到项目库或个人库。以后在任何对话输入 `/saved-workflow-name` 就能复用相同编排逻辑。这才是把重复工作真正变成 SOP 的关键。

### 四、实战案例 + 可直接复制提示词（内容创作者最爱）

**案例1：公众号爆款内容生产全流程工作流**（强烈推荐）

把一个 X 帖子或想法，自动完成从选题到成文的全流程。

**提示词模板**（直接复制修改使用）：

使用 Dynamic Workflow 为我的微信公众号创建一个完整的内容生产流水线。
任务：基于这个 X 帖子 [粘贴链接或内容]，产出一篇 3000-4000 字的技术干货公众号文章。
工作流阶段要求：
1. 内容角度挖掘与爆款标题变体生成（至少 5 个高点击标题）
2. 深度研究与事实交叉验证（使用多个来源）
3. 文章结构规划 + 钩子/结尾设计
4. 正文撰写（技术干货风格，带实操步骤和提示词）
5. 视觉生成提示词优化（封面 + 配图）
6. SEO 优化 + 互动引导语
7. 最终排版建议和发布 checklist
请先展示完整计划，得到我批准后再执行。使用并行代理和交叉验证确保质量。

运行后在 `/workflows` 实时监督进度。

**案例2：深度研究报告**

直接用：

`/deep-research Claude Dynamic Workflows 最新技术细节、限制、最佳实践和真实用户案例，交叉验证官方文档与社区反馈`

**案例3：大型代码审计 / 重构**（开发者向）

适合代码库级别的 bug hunting、安全审计、迁移重构等。多个代理可以互相 review 代码。

### 五、5 个高级技巧和避坑指南（技术干货核心）

1. **模型选择决定成本**

   大型 workflow 前先输入 `/model` 查看当前模型。Opus 4.8 跑几十上百个代理费用会很高，建议先用 Sonnet 测试逻辑，确认后再切强模型。
2. **提前连接好 MCPs / Connectors**

   做研究类 workflow 前，先把 Notion、Drive、网页搜索、特定 API 等工具连好。来源越多，交叉验证越强。
3. **与现有 Skills 深度结合**

   如果你已经有写钩子、润色、视觉提示等 Skills，可以在 workflow prompt 里指定调用它们，形成「技能包 + 编排」组合。
4. **成本与停止条件意识**

   长任务一定要利用 resumable 特性，设置合理 stop conditions。时刻监控 `/workflows` 的 token 面板，及时干预。
5. **最佳实践流程**

- 小任务先手动测试 workflow 逻辑
- 保存高质量的 workflow 形成个人AI 团队标准作业程序
- 迷茫时直接问 Claude：`基于你对我的了解，我应该构建哪些 workflows？`

### 六、总结和行动建议

Dynamic Workflows 把复杂、重复、高价值的工作，从我手动一步步催变成了我设计一次，团队自动跑。

对于公众号运营者、内容创作者、研究员、开发者来说，这可能是 2026 年最值得深度掌握的 Claude 技能之一。

**现在就行动起来**：

1. 打开 Claude Code，试试输入 `workflow` 或 `/deep-research` 一个你当前的任务
2. 把你最常做的重复流程做成一个 workflow 并保存下来
