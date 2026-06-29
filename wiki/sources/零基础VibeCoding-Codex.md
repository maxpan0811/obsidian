---
title: 零基础也能 Vibe Coding：Codex 入门到上手全流程
type: source
created: 2026-06-08
updated: 2026-06-08
source_path: 印象笔记管理工具/零基础也能 Vibe Coding：Codex 入门到上手全流程（含设置与模板）.html
tags: [vibe-coding, ai-programming, tutorial]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "零基础也能 Vibe Coding：Codex 入门到上手全流程（含设置与模板）"
source: evernote
type: note
export_date: 2026-06-27
guid: d5d7fbb9-b119-45ba-833b-c614b1e2c720
---

# 零基础也能 Vibe Coding：Codex 入门到上手全流程（含设置与模板）

原文链接: [https://mp.weixin.qq.com/s?chksm=9602eea4a17567b27c4a5df34109b50...](https://mp.weixin.qq.com/s?chksm=9602eea4a17567b27c4a5df34109b50cf73dec47e8fc12717e5212e132011b13a8af3a295a5d&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1773840352_1&req_id=1773840352209006&scene=169&mid=2247484171&sn=e415716499a47b85d47e2164831f4336&idx=1&__biz=MzE5MTYyNjQzMg==&sessionid=1773835575&subscene=200&clicktime=1773840637&enterid=1773840637&flutter_pos=79&biz_enter_id=5&jumppath=20020_1773840528587,1104_1773840559778,30024_1773840569337,1104_1773840629687&jumppathdepth=4&ascene=56&devicetype=iOS26.3.1&version=18004533&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQCWpAW4hx7bLI2Gz2FGS5gBLVAQIE97dBBAEAAAAAAP2IB8UyzooAAAAOpnltbLcz9gKNyK89dVj0ZUWd1hCOxwUcx8uh9Qt+m5OqNcKaSwdJGdB8wrnpfHhpqhuBhW1ToIjXmxWEBzyOl1GYLvJC/4IEN2IihKpHz1ZTBV+8wC0kuPILgee8+JEvYgT4D3pgfUaApjETjMCEv2n7All86eVv1siFyCYFoOm5B+y4iNUx5UZiKiiZPnxQQ/0RmMTuRPhuYY1ktEdCNtH17vf7PqraYloipRwAKFAeFiN1QtCDB1hjrrBLwA==&pass_ticket=etUTIJVwzjPWWMmW2upYLsupiIzOAEG8yokQogvGdyAy0eW42Wv13dGEu4/fBjQE&wx_header=3)

dadaming伊捏捏的脑洞集市

## 1. 什么是 Codex？它到底解决了什么问题？

先用最人话的方式科普一下。

你可能听过 Claude Code、Clawdbot 之类的东西。 它们本质上都是：**把“编程能力 + 工程化流程”封装成一个 Agent 应用**，你用自然语言跟它协作，它负责在你的项目里改代码、跑命令、做记录。

**Codex**就是 OpenAI 对标 Anthropic 的 Claude Code 的产品： 它是一个“编程 Agent 应用”。

而且走到今天，编程 Agent 越强，其实越接近“通用 Agent”。 因为信息化 30 年，几乎一切都建立在代码之上： 你能写代码、改系统、调服务，你就能做很多“看起来不是编程”的事。

## 2. 模型怎么选？谁能用 GPT-5.3-codex？

这里说清楚，避免你踩坑：

- **GPT-5.3-codex**是编程特化模型，所以它在“事实核查、世界知识、写故事写段子”这些方面不一定强。
- OpenAI 也因此没把它塞进 ChatGPT 的常规模型列表里。
- **目前 GPT-5.3-codex 主要是在 Codex 里用。**

![](attachments/380e570b15b06671.png)

大致情况你可以这么理解（按你原文口径）：

- Plus / Pro：可以用 Codex 应用，并可用 GPT-5.3-codex
- 免费 / Go：也能用 Codex，但可能只有 GPT-5.2-codex（注意差别）

**如需升级GPT Plus可前往MUPGPT官网充值升级（月付139/年付1390）： https://mupgpt.clawdo.com/**![](attachments/36ae89eea1ea75c3.jpg)

下载也简单：打开 Codex 官网 （https://chatgpt.com/codex），点下载、安装、登录即可。

![](attachments/c7f62d9ff469481d.png)

（Windows 应用如果还没上，就先用命令行版；但我猜你主要想要“有 UI 的那个”。）

## 3. Codex 最核心的设计：文件夹 + Thread（这点决定你用得爽不爽）

Codex 里左侧那栏，看似普通，其实是它对小白最友好的地方之一。 它分两层：

### 第一层：文件夹（工作区 / 项目）

你可以理解为：一个个项目目录 / 主题盒子。 比如：AI 热点、数据抓取机器人、sandbox、tools……

### 第二层：Thread（线程 / 任务线）

点进某个文件夹后，你会看到一条条对话记录。**每一条 Thread 就是一条独立任务线**：围绕一个明确目标推进。

最接地气的比喻：

- 文件夹 = 一个项目群
- Thread = 群里某个具体话题帖

你在话题帖里聊需求，Codex 就在同一个项目上下文里改文件、跑命令、记过程。 你换一个 Thread，就相当于换了另一个话题帖，**上下文不会互相污染**。

这对小白太关键了，因为你再也不会遇到那种经典崩溃场景： 上午让它写网页，下午让它算 Excel，晚上又让它改文案，最后所有上下文搅成一锅粥，AI 开始胡编，你自己也找不到文件在哪。

我给你一个简单到离谱、但极其有效的规则：

**同一个文件夹做同一个大方向；同一个 Thread 只推进一件具体的事。**

你会明显发现：成功率更高、返工更少、心态更稳。

## 4. 我最推荐你先配好的 3 个东西

Codex 很强，但你一开始别急着狂喷需求。先把这三件事设置好，你后面会爽很多。

### 1.定时任务（自动巡检 / 自动跑活）

![](attachments/ca989c47cf2d58d4.png)

Codex 可以在特定时间做特定事。 举例：每天早上 9 点巡检服务器、发现报错就尝试修复，再把总结发到飞书/消息里。 你不懂服务器也没关系，把它当“托管管家”就行。

![](attachments/b15d4d4e01de50da.png)

### 2.Skills（最适合小白的“外挂系统”）

Skill 的价值不用多解释了。关键是：**Codex 把 Skills 做成了可视化管理界面**——你能清楚看到自己装了哪些、起什么作用、怎么编辑。

![](attachments/ddced3cbaa38de90.png)

更离谱的是它自带 Skill Creator： 你点右上角 New Skill，用嘴描述你想要什么，它就能帮你搭一个。

![](attachments/39a8698aba91030a.png)

对比某些工具：支持 skill 但构建 skill 的工具还要你自己去找、自己去装……这真的很反人类。

### 3.个性化全局规则（相当于 AGENT.md，但更直观）

你可以在个性化设置里写全局规则，让 Codex形成稳定的工作习惯。 新手直接复制下面这份就行（我帮你把格式也顺了一下）：

```
# Global rules for Codex  
## 工作原则  
- Prefer small, reviewable diffs. Avoid sweeping refactors unless explicitly requested.  
- 编辑前先明确要改哪些文件，并用 3-6 个要点说明计划。  
- Never invent APIs, configs, or file paths. If unsure, search the repo first.  
- 保持修改与现有风格和架构一致。  
  
## 安全与隐私  
- Never paste secrets, tokens, private keys, .env values, or credentials.  
- 如果需要密钥，让我用环境变量提供。  
- 不要添加埋点/遥测/网络请求，除非我明确要求。  
  
## 质量要求  
- 有测试就补测试；优先类型安全和明确错误处理。  
- 只有意图不明显时才写注释。  
  
## 运行与交付  
- 需要跑命令时，先提出“具体命令 + 为什么要跑”。  
- 可能破坏构建时，先跑最快的相关检查。  
- 输出代码变更时：给简短摘要 + 文件变更列表。  
- 调试时：给假设、实验、最小修复。  
  
## 我的偏好  
- 用中文解释；步骤要具体，可复制粘贴。
```

## 5. 真正开始 Vibe Coding：我推荐的工作流

终于到你最关心的：怎么“用起来就爽”。

我自己的习惯是：

### Step 1：先开 Plan Mode（只规划不写代码）

任何从 0 到 1 的项目（下载视频、转格式这种小活不算），我都强烈建议先用 Plan Mode。![](attachments/23b77359e4139cc0.png)

你用嘴描述需求，让它输出一个规范计划文档：目标、拆解、文件结构、步骤、风险点、验证方式。![](attachments/c7560a97817025a6.png)

计划出来后，它通常会问你要不要执行。你直接选“是”，就进入正式开发。

![](attachments/9ecce35a0db36acc.png)

### Step 2：开发阶段保持“边做边 steer”

![](attachments/f0256fb2b3f52bf5.png)

你需要它在开发中随时可被你纠偏、加需求、改方向（尤其你是小白）。 把 follow-up / 行为设置成 steer，会更舒服。

### Step 3：前端做崩了怎么办？

说实话：Codex 有时候前端确实一般。 我自己的策略是：

- Codex 负责架构、逻辑、落地
- 前端如果做成一坨💩，我会切到 Claude Code / 其他组合重制 UI
- UI OK 后再回 Codex 继续“快乐口喷”

你要记住：**工具是拿来用的，不是拿来忠诚的。**哪边强就用哪边。

### Step 4：并行 Threads（这才是效率爆炸的点）

Codex 支持你开多个 Thread 并行推进： 一个 Thread 写主逻辑，一个 Thread 修 bug，一个 Thread 写部署脚本…… 你会第一次感受到：**自己像一个小团队**。

## 6. 推理档位怎么选？我的建议很简单

你可以把它理解为：档位越高，模型在回答前会做更多推理与自检，通常更稳更全，但更慢、更贵。

我个人建议：

- **日常：High**（又稳又快）
- **大活硬活：Extra High**（成功率比省 token 重要得多）

## 最后：给所有“小白/非程序员/被命令行劝退的人”一句话

我一直觉得，Vibe Coding 对非程序员的价值可能比对程序员更大。

程序员本来就会写代码，AI 对他们是提效。 但对我们这种不会写代码的人来说，AI 是直接把一道过不去的坎给铲平了。

未来，“会用 AI 写代码”会像“会用 Excel”一样，变成基本技能。 这几乎是必然。

所以如果你曾经：

- 对 Vibe Coding 心动过
- 被封号/bug/命令行劝退过
- 被复杂 IDE 吓跑过

那我真心建议你：从今天开始，就用 Codex 试一次。 你不用先变成程序员，你只需要先**把需求说清楚**。
