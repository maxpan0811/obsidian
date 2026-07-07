---
title: 如何在使用 Claude Code 时避免出现“已达到限制”的错误 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/如何在使用 Claude Code 时避免出现“已达到限制”的错误 2.md
tags: [evernote, impression, yinxiang]
---

# 如何在使用 Claude Code 时避免出现“已达到限制”的错误

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0NDQ0ODU3MA==&mid=224754...](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547242&idx=1&sn=cbee41e231f5459d976b0cdfb70f5a4c&chksm=e8d41bc42891cfbab5935b8d0df8348b2f71c4d27f58243ae210e08a594112106c321ab8bfb2&scene=90&xtrack=1&req_id=1776475821342739&sessionid=1776482569&subscene=272&clicktime=1776483194&enterid=1776483194&flutter_pos=59&biz_enter_id=4&ranksessionid=1776482836&jumppath=30024_1776482890971,1104_1776482893374,30024_1776482896077,1104_1776482904324&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004724&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2/wtn3Gto08/5ML4vA5QRhLVAQIE97dBBAEAAAAAAAVKMtfye9cAAAAOpnltbLcz9gKNyK89dVj0Swbtz8Y8eCcBltjsp9TNe1cSD1SkcHqUgoQdVxQ5NFx1AOSPAviYQ2YW4VsrWs7mRseu7XW9RfY40Ub1tlFmp771hVZ5KzXJl3PrOe0DQcblG5OlxEC33ohAknbLd/E7/RsJw5sAA12JpEHoZp52mSML4zZM0duymIeNVuelKQGAbEZgAtj8ailiU1vJwzMPvoiwLuqVhStOnxGUF7GucBh9/Yt2ndYQ2offH8sHRg==&pass_ticket=H97gMCi4RBpB5wrK32r+0YLhhqGQwIfrMXlt1Pjulji+uNzFFbGxeL7L62ZY16J0&wx_header=3)

Originaldev 大迁世界

工作一忙起来，Claude Code 突然弹出一句 “You’ve hit your limit”，真的很让人抓狂。尤其是你正赶进度、正想一口气把事情做完时，这种中断感，简直像临门一脚被人拽住。

这篇文章，我想分享 6 个很实用的方法，帮你尽量降低在 Claude Code 里撞上使用限额的概率。

Claude Code 里，其实有两种不同的限制
------------------------

在和 Claude 交互时，你通常会遇到两类限制，而且它们的运行逻辑并不一样：**使用限额**和**长度限额**。

### 使用限额

它控制的是：在某一段时间内，你到底能和 Claude 互动多少次。说白了，就是你在一天内可支配的“对话额度”。

你可以把它理解成一笔“交流预算”——它决定了你还能给 Claude 发多少条消息，还能在 Claude Code 里持续工作多久，超过之后，就只能等额度恢复。

一旦这部分额度被用光，系统就会提示你类似 “You hit your limit” 这样的信息，同时告诉你，下次重置要等到什么时候。

Claude Code 目前有两套和使用相关的限制：**5 小时滚动限制**（也就是日常使用限制）以及 **7 天维度的周限制**。举个例子，如果你看到系统显示“resets 5pm”，那通常意味着你已经触发了日限额，需要再等一个新的 5 小时窗口。

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/D3282E49-C70F-4212-B538-7033978E06CF.png)

### 长度限额

另一类限制，和 Claude 的上下文窗口有关，也就是它在单次聊天中，最多能同时处理多少信息。

你可以把上下文窗口想成 Claude 的“工作记忆”。这块空间越充足，它越能理解前因后果，也越能在连续任务中保持稳定。

长度限额会直接影响输出质量；不过，它和使用限额不同——即使你快碰到长度边界，通常也不会立刻让你彻底停工。

所以，优化上下文窗口的使用，不只是为了避免撞上长度限制；更重要的是，它会直接决定 Claude 产出结果的质量高低。

真撞上使用限额后，会发生什么
--------------

答案其实很现实：**要么等，要么花钱。**

你可以等当前套餐的额度重新刷新——Claude Code 一般会明确告诉你，还要多久才能恢复使用；或者，你也可以选择额外购买配额，但这部分需要你自己另外付费。

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/D46294A5-CD20-4F2C-9E02-0B512AE8A299.png)

额外的使用额度，是可以单独购买的。

6 个实用方法，帮你尽量别再撞上限额
------------------

### 1. 实时盯住你的使用情况

Claude Code 其实提供了几种查看限额的方法。要是你用的是桌面版，可以进入 **Settings → Usage**，在那里查看当前套餐的使用情况。

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/86668D18-C1A1-4D83-A4F6-7E792F55534F.png)

Claude Code 桌面版中的套餐使用信息。

这个入口当然能用，但老实说，并不算高效。因为 Usage 被放在设置里，你每次都得专门点进去看，不太适合频繁监控。相比之下，后面几种方式更顺手，也更适合日常使用。

Claude Code 还有一个内置提醒：当你的额度用到 **90%** 左右时，Chat 模式输入框上方会出现一条警告信息。

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/7D39E3AD-52B6-462C-B0E7-CE0478527B45.png)

输入框上方出现的“Usage limit reached”提示。

很多时候，**90% 比 100% 还让人焦虑**。因为当它还没彻底断掉时，你反而会一直担心：眼下这项任务，到底还能不能撑到做完？

随着 Opus 4.7 发布，Anthropic 也顺手重做了 Claude Code 的桌面端界面，并加入了更直观的实时监控。现在，你只需要点击输入框右下角的图标，就能看到上下文窗口和套餐用量。

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/99A571EC-FCC3-4193-B911-ADFC70A9DBCC.png)

如果你用的是 Claude Code CLI，也可以自定义状态栏。在命令行里输入：

`/statusline show model name, usage limits and length limits with progress bars`

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/1BF4BE60-42F9-472F-80B8-5D010ABAB9C5.png)

在 Claude Code CLI 中提交 `/statusline` 指令来自定义状态栏。

设置完成后，Claude Code 会展示这些信息：

* **ctx**：当前上下文使用情况，也就是长度限额相关信息；
* **daily / weekly**：每日与每周的使用额度，并通过独立进度条显示出来。

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/DE71B465-8EBC-4532-BDDA-B8C6C1EEE84B.png)

Claude Code CLI 中的自定义状态栏效果。

### 2. 任务不同，模型也别乱选

Claude Code 提供了不止一种模型。很多人一上来就切到 Opus，毕竟它最强，也最擅长深度推理。但问题在于，这个模型通常也意味着：

* 单次请求消耗更多算力；
* 输出往往更长、更重。

于是结果很直接：即便消息条数不算多，也更容易更早触发限制。

更稳妥的做法，不是默认选“最强”，而是**按任务匹配模型**。我自己通常这样分：

* **Haiku**：速度极快，负担很轻，特别省额度。适合处理简单提问、快速确认，不需要查资料也不需要深度分析的任务。
* **Sonnet**：中等体量，但 token 利用效率很高。适合执行类工作，比如写代码、改内容、反复迭代。
* **Opus**：能力最强，但也最“贵”。更适合复杂规划、棘手排障，或者架构层面的审查与判断。

切换模型时，可以直接输入这个命令：

`/model`

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/2595AB03-275C-430B-880E-B8F97494F2FD.png)

Claude Code CLI 会话中的模型选择界面。

### 3. 先进入计划模式，再动手执行

很多人最容易踩的坑，就是一上来就让 Claude 直接开改。这样做往往会带来大量不必要的来回沟通：你改一句，它回一段；你补一句，它又延伸一堆。回合数一多，额度自然飞快往下掉。

所以，与其立刻让它生成结果，不如先让它把路想清楚。因为**迭代次数越少，消息消耗通常也越少**。

Claude Code 最近新增了一个非常强的规划模式——**Ultraplan**。它可以围绕你的任务，先生成一份相当完整、相当细致的执行方案：

`/ultraplan [explain the task you want Claude Code to plan]`

The Best Way To Plan Work With Claude Code /ultraplan for making the most of Claude Code uxplanet.org

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/2E36CE62-6823-4B47-B931-81B520A4AD5B.png)

Claude Code 生成的详细执行计划。

### 4. 大任务别硬扛，拆开做才聪明

大任务最容易把你拖进两个坑：**上下文越来越长，交互轮次越来越多**。而这两件事叠在一起，基本就等于：离撞限额不远了。

所以，更好的方式是把工作拆成彼此独立的小模块、子任务，一个个处理。每完成一段，就用下面这条命令清空上下文：

`/clear`

Start a new session with empty context
--------------------------------------

这样做的好处很直接：上下文保持干净，Claude 不会背着一大堆旧信息前进，响应会更轻，消耗也更可控。

与其死磕一场超长会话，不如养成模块化工作流。对使用限额如此，对长度限额也是一样——**分块处理，往往比一次性猛冲更省、更稳，也更容易得到清晰结果。**

### 5. 把“少说废话”讲明白

Claude 天生就比较爱展开，尤其在你没有明确要求时，它很容易给出一大段解释。

可问题是，你很多时候根本不需要那么多。你只想让它执行，只想拿代码，只想看结论。那就别让它自己猜，直接在提示词里写清楚，比如：

* concise output
* code only

输出越短，每一轮消耗的 token 往往就越少。因此，同样一个任务，你把要求说得越明确，成本通常越低。

### 6. 少开 MCP，少背无谓的工具包袱

MCP 服务器——尤其是像 Figma 这一类——会在你没怎么察觉的时候，悄悄吞掉大量额度。

原因并不复杂：MCP 会显著占用上下文窗口；而且，一旦你同时挂了多个 MCP，它们很可能直接成为项目里最大的 token 消耗源。最容易把 Claude token 烧光的方式之一，就是在项目里让所有 MCP 长期开着。

因为每当你发送一条消息，所有已连接的 MCP 服务器，都会把自己的工具信息一起带进上下文——哪怕你这次任务压根用不到它们。

第一步，也是最重要的一步，就是：**把当前没在用的 MCP 断开。**

![](.evernote-content/BEF02260-9793-423B-A3BE-7713E6F1D183/4A9C6A68-DC87-41B4-BC25-4F5404B48DFC.png)

断开暂时不用的 MCP。

第二，能直接调 API 的时候，尽量直接调 API，而不是层层套 MCP。这样做不仅更安全，而且在 token 消耗上也更可预期。最后，尽量别反复传输体积很大的设计文件——这种隐形成本，累积起来往往比你想象中更夸张。

顺带说一句，我对 MCP 在正式设计生产流程里的表现，一直保留一点怀疑。它在灵感探索、想法发散阶段，确实很灵活、很好用；然而，一旦你开始推进真正可交付、可落地的生产级方案，它反而很容易变成阻力，而不是助力。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=2247547242&idx=1&sn=cbee41e231f5459d976b0cdfb70f5a4c&chksm=e8d41bc42891cfbab5935b8d0df8348b2f71c4d27f58243ae210e08a594112106c321ab8bfb2&scene=90&xtrack=1&req_id=1776475821342739&sessionid=1776482569&subscene=272&clicktime=1776483194&enterid=1776483194&flutter_pos=59&biz_enter_id=4&ranksessionid=1776482836&jumppath=30024_1776482890971,1104_1776482893374,30024_1776482896077,1104_1776482904324&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004724&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2/wtn3Gto08/5ML4vA5QRhLVAQIE97dBBAEAAAAAAAVKMtfye9cAAAAOpnltbLcz9gKNyK89dVj0Swbtz8Y8eCcBltjsp9TNe1cSD1SkcHqUgoQdVxQ5NFx1AOSPAviYQ2YW4VsrWs7mRseu7XW9RfY40Ub1tlFmp771hVZ5KzXJl3PrOe0DQcblG5OlxEC33ohAknbLd/E7/RsJw5sAA12JpEHoZp52mSML4zZM0duymIeNVuelKQGAbEZgAtj8ailiU1vJwzMPvoiwLuqVhStOnxGUF7GucBh9/Yt2ndYQ2offH8sHRg==&pass_ticket=H97gMCi4RBpB5wrK32r+0YLhhqGQwIfrMXlt1Pjulji+uNzFFbGxeL7L62ZY16J0&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/55c8a7ec-e259-4da7-9b4d-37a4e79f8c44/55c8a7ec-e259-4da7-9b4d-37a4e79f8c44/)
