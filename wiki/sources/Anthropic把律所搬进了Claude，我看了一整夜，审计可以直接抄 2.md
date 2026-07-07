---
title: Anthropic把律所搬进了Claude，我看了一整夜，审计可以直接抄 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Anthropic把律所搬进了Claude，我看了一整夜，审计可以直接抄 2.md
tags: [evernote, impression, yinxiang]
---

# Anthropic把律所搬进了Claude，我看了一整夜，审计可以直接抄

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0MjgxMzg1Mw==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzI0MjgxMzg1Mw==&mid=2247505550&idx=1&sn=79cad986e8783ebb62a9f6346ec2f098&chksm=e8bb1c0556dc9ca38bf4102ccdc8c3b1328bd2d2c167976adc90251b53aa0a7c3232a9b95b76&scene=90&xtrack=1&req_id=1778812569132530&sessionid=1778812560&subscene=93&clicktime=1778812667&enterid=1778812667&flutter_pos=3&biz_enter_id=4&ranksessionid=1778812569&jumppath=20020_1778812564634,1104_1778812565881,20020_1778812568566,1104_1778812660114&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004927&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ5A6ZkGmcOvowyLyzYCSCNBLVAQIE97dBBAEAAAAAAAQAGaMtMBsAAAAOpnltbLcz9gKNyK89dVj07uah5grBwgoN6d4cKW3OKiKj9Dktj+ObBuC2k++WYf4sg1H3CNwoTxIoHuw6ClaRDtZ1oVXqbHv4rQGrrVpHUeNgZ2NF6tRFoCgYNUrA9QKnh3foy5IFY0l5JFN9+TctpmDUXqhK+UfCQDf6oBOEmtlfmcDelNiAYNkIO5XHji+svYrgkr/eOa4QhJ40rOuoScGCsYdU3M4tu6X1JiUT5YLHck7phvUsBk/7h69f4A==&pass_ticket=aM8C3O6puj90MdEjBz0RgSt8Acl2cNaW4FMNgShOr4WuhbXXGpufm7XjhM01soll&wx_header=3)

Anthropic把律所搬进了Claude，我看了一整夜，审计可以直接抄
====================================

Originalnigo 逆行的狗

Anthropic 新开源了一个项目，叫 **claude-for-legal**，火了一把。

简单说就是——**把律师事务所搬进了 Claude Code。** 11个法律业务领域，60多个专用Agent，合同审查、尽职调查、诉讼管理、知识产权……律师日常干的活，全拆成了一个个能直接调用的Agent。

律师事务所是专业服务机构，会计师事务所也是。同行抄作业，天经地义。

![](.evernote-content/9F1C3AD6-71DD-4EC2-9741-E3EA795F49CF/A6D8BEE4-A20B-497F-A891-32F0B793E2F0.jpg)

---

律所搬进Claude长什么样
--------------

![](.evernote-content/9F1C3AD6-71DD-4EC2-9741-E3EA795F49CF/C06443D4-FA14-4C61-A7AE-23C8F8C806CC.jpg)

先说这个项目做了什么。

Anthropic 做了一件事：**把律师事务所的日常业务拆成了11个插件**，每个插件覆盖一个法律实务领域。

11个领域，60多个 Agent，涵盖了：

| 插件 | 做什么 |
| --- | --- |
| commercial-legal | 供应商合同审查、NDA分类、续约监控 |
| corporate-legal | M&A尽职调查、交割清单、董事会决议 |
| privacy-legal | DPA审查、DSAR响应、隐私影响评估 |
| litigation-legal | 案件管理、诉求图表、证言准备 |
| ip-legal | 商标查重、FTO初筛、侵权分析 |
| employment-legal | 招聘/解雇审查、用工分类、内部调查 |
| …… | …… |

这不是一个“通用法律AI助手”。

**是60多个专用的、有名字的 Agent。** 每个 Agent 只干一件事，但干得很精。

比如合同审查这件事，它不是笼统的“帮我看看这份合同”，而是拆成了：

* Vendor Agreement Reviewer — 按你的 playbook 审查供应商合同，输出 redline 备忘录
* NDA Triager — 把收到的 NDA 分成绿/黄/红三档，只有红色才需要律师亲自看
* Amendment Tracer — 追踪一份合同从原始版本到历次修订的所有变化
* Renewal Watcher — 后台自动扫描合同到期日，提前预警

看到这里你可能会想：这不就是我们审计想干的事吗？

**把一个大流程拆成一堆小任务，每个任务交给专门的 Agent，后台自动跑。**

是。但真正让我看了一整夜的，不是这些 Agent 本身，而是它们背后的**架构设计**。

---

三个让这个项目成立的设计
------------

![](.evernote-content/9F1C3AD6-71DD-4EC2-9741-E3EA795F49CF/952ED5E4-8352-4D85-8F07-128B0A97C42A.jpg)

### 设计一：冷启动面试

这是整个项目最精妙的部分。

每个插件安装之后，**不会直接开始干活**。它会先跟你做一次结构化访谈，大概10-20分钟：

1. 你们怎么审查合同的？
2. 给我一份你们做过的审查备忘录当模板
3. 你们的升级规则是什么？什么情况需要合伙人审批？
4. 你们用什么合同管理系统？

访谈结束后，它把你的方法论、模板、偏好写成一份 **CLAUDE.md 实务档案**。

**后续所有 Agent 都读这份档案。**

这意味着：同一个插件，A律所和B律所安装后，行为完全不同——因为它们的方法论不同。

### 设计二：共享上下文，不是串联流程

我之前一直觉得“串流程”需要做一个大的编排引擎，像工作流软件一样。

但 claude-for-legal 的做法完全不同。

**它不串流程。它串上下文。**

每个 Agent 是独立的，但它们都从同一份 CLAUDE.md 读取信息。CLAUDE.md 就是那个“串联点”——你不需要显式地连接它们，共享的方法论档案自然就让他们对齐了。

123456789101112131415
┌──────────────────────────────┐
│  CLAUDE.md（实务档案）         │
│  - 方法论                     │
│  - 模板                       │
│  - 风险偏好                   │
│  - 升级规则                   │
├──────────────────────────────┤
│                                │
│  Agent A  Agent B  Agent C     │
│  （各自独立，都读 CLAUDE.md）   │
│                                │
├──────────────────────────────┤
│  Connector（连接外部系统）     │
│  合同管理系统 / 法院系统 / ... │
└──────────────────────────────┘

这个设计很妙。**你加一个新的 Agent，不用改任何已有的东西，只要让它也读 CLAUDE.md 就行。**

### 设计三：输出永远是草稿

每个 Agent 的输出都标注：**DRAFT — 需律师审核。**

不是法律意见，不是法律结论，不能替代律师。

引用必须标注来源。如果没连上法律数据库，引用会标记 `[verify]`，提醒你这条没有经过验证。

**关键决策点设“门”（gate）：** 自动处理到某一步，必须由人确认才能继续。

---

映射到审计：一套可以抄的架构
--------------

![](.evernote-content/9F1C3AD6-71DD-4EC2-9741-E3EA795F49CF/F855CBA6-78F4-4987-BE90-CA9AC470D735.jpg)

法律和审计的相似度比很多人想的高：

|  | 法律 | 审计 |
| --- | --- | --- |
| 交付物 | 法律意见书、备忘录 | 审计报告、审计底稿 |
| 流程 | 尽调→审查→出意见 | 计划→执行→完成 |
| 风险 | 法律责任 | 审计风险 |
| 数据来源 | 法院系统、合同库 | 财务系统、凭证库 |
| 专业判断 | 律师 | 注册会计师 |

所以 Anthropic 这套架构，**几乎可以直接映射到审计**。

### 冷启动 = 审计计划

律师的冷启动面试，本质上就是我们审计的**计划阶段**。

审计项目开始时你要做什么？

* 了解被审计单位及其环境
* 评估重大错报风险
* 确定重要性水平
* 制定总体审计策略

这些信息，完全可以写成一个 `audit-setup` 的冷启动 skill：

/audit:cold-start

→ 访谈问题：

1. 客户行业？上市/非上市？报告类型？
2. 上年审计的关键事项？
3. 重要性水平怎么算？
4. 审计软件用什么？数据在哪？
5. 请提供：上年审计报告、本期未审报表

→ 输出：项目级 CLAUDE.md

**这份 CLAUDE.md 就是整个审计项目的共享上下文。** 后续所有 Agent 都知道这个项目的基本情况，不用每次重复输入。

### 按阶段拆 Agent

法律项目按业务领域拆插件。审计可以按**阶段**拆：

**计划阶段**

| Agent | 做什么 |
| --- | --- |
| client-acceptance | 客户承接评价（独立性、诚信评估） |
| risk-assessment | 风险识别与评估 |
| materiality-calc | 重要性水平计算与分配 |
| audit-plan | 生成审计计划 |

**执行阶段**

| Agent | 做什么 |
| --- | --- |
| analytical-procedures | 分析性复核（波动分析、比率分析） |
| voucher-check | 凭证抽查（记账凭证→原始凭证核对） |
| bank-confirmation | 银行函证生成、追踪、差异处理 |
| related-party | 关联方识别与交易审查 |
| revenue-testing | 收入循环测试 |

**完成阶段**

| Agent | 做什么 |
| --- | --- |
| going-concern | 持续经营评估 |
| audit-summary | 审计总结 |
| management-letter | 管理建议书起草 |
| audit-report | 审计报告起草 |

每个 Agent 从 CLAUDE.md 读项目上下文，输出审计底稿草稿，标注需项目经理复核。

### 后台 Agent 自动跑

法律项目有一堆 scheduled agent：合同到期监控、法院案件更新、法规变化摘要。

审计的对应物更刚需：

| 后台Agent | 频率 | 做什么 |
| --- | --- | --- |
| confirmation-tracker | 每天 | 追踪函证回函状态，超期预警 |
| deadline-watcher | 每天 | 报告日期倒计时，关键节点提醒 |
| client-news-monitor | 每周 | 监控客户舆情/公告/处罚信息 |

这些东西不需要人盯着，后台跑就行。

### 信任层：审计比法律更需要

法律项目每个输出都标“草稿，需律师审核”。

审计？**必须比这更严格。**

AI 输出的每个判断都需要标注：

* 数据来源（哪个底稿、哪个系统）
* 置信度
* 关键节点的“门”——重要性水平要高级经理确认，审计意见类型要合伙人确认

这不是限制 AI 的能力，是**保护注册会计师**。

---

怎么开始：三步走
--------

![](.evernote-content/9F1C3AD6-71DD-4EC2-9741-E3EA795F49CF/2B5F8D60-9A3C-4729-B85D-4D07366315A4.jpg)

看完这个项目，我理出了一条可以落地的路径。

### 第一步：搭架子

不用一口气做 60 个 Agent。先搭好结构：

12345678910
audit-plugin/
  CLAUDE.md                ← 审计方法档案（模板）
  skills/
    cold-start-interview/  ← 项目初始化
    materiality-calc/      ← 重要性水平计算
    voucher-check/         ← 凭证抽查
    analytical-procedures/ ← 分析性复核
  agents/
    confirmation-tracker/  ← 函证追踪
  .mcp.json               ← 连接审计工具

### 第二步：一个 Agent 做透

选一个**最痛的场景**，做到极致。

凭证抽查、分析性复核、函证追踪，哪个最让你头疼，就从那个开始。

关键是：

* 定义好判断逻辑（什么情况自动处理，什么情况停下来问人）
* 接上数据源（科目余额表、明细账、凭证库）
* 在一个项目上跑通

### 第三步：靠 CLAUDE.md 串起来

一个 Agent 验证可行之后，再加新的。

**每个新 Agent 都从 CLAUDE.md 读项目上下文**，自然就协作了。你不需要设计一个大流程引擎，共享的上下文就是串联。

这就是 claude-for-legal 最核心的洞察：

**不要试图串流程，要串上下文。**

---

一句话
---

Anthropic 没有做一个“万能法律AI”，它做的是一套**让律师的方法论变成AI的行为规范**的基础设施。

审计也一样。我们缺的不是 AI 能力，是**把审计方法论翻译成AI能理解的语言**的中间层。

claude-for-legal 给了一个参考答案。开源的，Apache 2.0 协议，可以直接看代码。

项目地址：https://github.com/anthropics/claude-for-legal

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI0MjgxMzg1Mw==&mid=2247505550&idx=1&sn=79cad986e8783ebb62a9f6346ec2f098&chksm=e8bb1c0556dc9ca38bf4102ccdc8c3b1328bd2d2c167976adc90251b53aa0a7c3232a9b95b76&scene=90&xtrack=1&req_id=1778812569132530&sessionid=1778812560&subscene=93&clicktime=1778812667&enterid=1778812667&flutter_pos=3&biz_enter_id=4&ranksessionid=1778812569&jumppath=20020_1778812564634,1104_1778812565881,20020_1778812568566,1104_1778812660114&jumppathdepth=4&ascene=56&devicetype=iOS26.4.2&version=18004927&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ5A6ZkGmcOvowyLyzYCSCNBLVAQIE97dBBAEAAAAAAAQAGaMtMBsAAAAOpnltbLcz9gKNyK89dVj07uah5grBwgoN6d4cKW3OKiKj9Dktj+ObBuC2k++WYf4sg1H3CNwoTxIoHuw6ClaRDtZ1oVXqbHv4rQGrrVpHUeNgZ2NF6tRFoCgYNUrA9QKnh3foy5IFY0l5JFN9+TctpmDUXqhK+UfCQDf6oBOEmtlfmcDelNiAYNkIO5XHji+svYrgkr/eOa4QhJ40rOuoScGCsYdU3M4tu6X1JiUT5YLHck7phvUsBk/7h69f4A==&pass_ticket=aM8C3O6puj90MdEjBz0RgSt8Acl2cNaW4FMNgShOr4WuhbXXGpufm7XjhM01soll&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a4fb2ee4-9de2-4b5a-9c9c-1da09abf8ce5/a4fb2ee4-9de2-4b5a-9c9c-1da09abf8ce5/)
