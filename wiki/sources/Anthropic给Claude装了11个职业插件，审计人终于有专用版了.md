---
title: Anthropic给Claude装了11个职业插件，审计人终于有专用版了
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Anthropic给Claude装了11个职业插件，审计人终于有专用版了.html
tags: [AI技术]
updated: 2026-06-27
---

---
title: "Anthropic给Claude装了11个职业插件，审计人终于有专用版了"
source: evernote
type: note
export_date: 2026-06-26
guid: 8f491f91-eb7e-43b0-aa3b-be0a9327f043
---

# Anthropic给Claude装了11个职业插件，审计人终于有专用版了

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI0MjgxMzg1Mw==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzI0MjgxMzg1Mw==&mid=2247505600&idx=1&sn=0dad922c107212761d53a15c5349e218&chksm=e81ed7d0f12359806e480be5da299ccceaa531ccee0fb2660272eed85783776660fca3161230&scene=90&xtrack=1&req_id=1779750943057682&sessionid=1779750938&subscene=93&clicktime=1779752601&enterid=1779752601&flutter_pos=3&biz_enter_id=4&ranksessionid=1779750943&jumppath=20020_1779752318852,1104_1779752319560,20020_1779752329884,1104_1779752594993&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQd+anYIezbIQ3JNIE74i2NRLTAQIE97dBBAEAAAAAAHFQJZSDGuMAAAAOpnltbLcz9gKNyK89dVj0fvRDv9jVhOo07T2zWBICYAulv0+QDZtmb5wQUcT3wO4O/nX6dxqC2Ur7rDTvhmXgAFiVewCChsmkM544w81IKSgflYbPgutTlxnLMdzD2Tq/HVrJvSQqLM1DKHYhyxXMTS51SHV54BIVgI/1HN5cRAYmdornjBf1JE1gLOF7ujBnoPiap7og+R9OTwSh/ZuM89GIVvGaBiX6mcDNt0RrSg+uT3P0xTmlRSirdCI=&pass_ticket=Gp5lqitVnjRLCOu3UHQo4+BMveB1vIwvbWRJeWqJGL5zbIyv1rOpYGybtRy/Cd6S&wx_header=3)

# Anthropic给Claude装了11个职业插件，审计人终于有专用版了

Originalnigo 逆行的狗

![](attachments/6213071efa2781aa.png)

上周用Claude Code写了个关联方识别的Skill，跑了一遍12个维度的自动核查，效果还不错。

但这几天GitHub上出现了一个更有意思的东西——Anthropic自己下场了。

他们开源了一套叫 **knowledge-work-plugins** 的项目，给Claude装上了11个职业角色插件。销售、法务、财务、产品经理……每个插件把一个岗位的专业知识、工作流程、工具连接全部打包好，装上就能用。

其中有一个 **finance** 插件，直接覆盖了审计和财务的工作场景。

14k⭐，一周不到。

https://github.com/anthropics/knowledge-work-plugins

---

## 这个插件到底是什么

先说清楚它不是什么。

它不是一个App，不是一个网站，也不是一个SaaS产品。

它是一堆 **markdown文件**。

对，就是跟你平时写笔记一样的markdown。只不过这些markdown里装的是专业知识——怎么做凭证、怎么做银行对账、怎么做SOX测试、怎么做差异分析。

Claude读了这些文件，就变成了一个懂财务和审计的助手。

这跟我们现在用的Skill本质上是一回事。只不过Anthropic把它标准化了，给了一套固定的目录结构。

---

## 架构：三层设计

每个插件由三部分组成：

**第一层：Skills（技能）**

核心知识层。每个技能是一个SKILL.md文件，包含某个工作领域的完整方法论。

finance插件目前有8个技能：

| 技能 | 干什么 |
| --- | --- |
| audit-support | SOX 404控制测试、抽样方法、缺陷分类 |
| reconciliation | 银行对账、GL与子账核对、关联方对账 |
| journal-entry | 凭证准备——应计、折旧、预摊、薪酬、收入 |
| journal-entry-prep | 凭证编制最佳实践和审核流程 |
| financial-statements | 财务报表生成（利润表、资产负债表、现金流量表） |
| variance-analysis | 差异分析——价格/量、利率/组合分解 |
| close-management | 月末结账检查清单和任务排期 |
| sox-testing | SOX合规测试——样本选取、测试底稿模板 |

Claude会根据你问的问题，自动匹配相关的技能文件来辅助回答。

**第二层：Commands（命令）**

你可以用斜杠命令直接触发特定操作：

- /journal-entry ap-accrual 2026-03 — 自动生成AP应计凭证
- /reconciliation cash 2026-03 — 执行银行对账
- /sox-testing revenue-recognition 2026-Q1 — 生成收入确认控制测试底稿
- /variance-analysis revenue 2026-Q1 vs 2025-Q4 — 收入差异分解
- /income-statement monthly 2026-03 — 生成月度利润表

每个命令后面跟的是参数，告诉Claude具体要处理什么。

**第三层：Connectors（连接器）**

通过MCP协议连接外部数据源。配置写在 `.mcp.json` 里：

1234Snowflake → 数据仓库，直接拉科目余额
BigQuery → 查询财务数据
Slack → 发送报告、催审批
Microsoft 365 → Excel、Outlook

![](attachments/cf755dfcbed51c56.png)

连上之后，Claude可以直接从你的ERP里拉试算平衡表，自动生成凭证，再把结果发到Slack上。

不连也行，手动粘贴数据一样能用。

---

## 实际跑一个：银行存款审计程序

光说架构没意思，来个具体场景。

假设我正在做一个年审项目，需要做银行存款的审计程序。

### 第一步：对账

输入：

/reconciliation cash 2026-03

Claude会按照reconciliation技能里的方法论，走完整个银行对账流程：

123456789101112银行对账单余额：      ¥12,345,678.90
加：在途存款          ¥234,567.80
减：未兑现支票        (¥156,789.00)
加/减：银行差错        ¥0.00
调整后银行余额：      ¥12,423,457.70
 
账面余额：            ¥12,400,000.00
加：银行利息未入账    ¥23,457.70
减：银行手续费未入账  (¥0.00)
调整后账面余额：      ¥12,423,457.70
 
差异：                ¥0.00 ✅

它还会告诉你哪些是常见差异原因——手动凭证没过子账、批次过账时间差、系统接口错误。

### 第二步：控制测试

输入：

/sox-testing treasury 2026-Q1

Claude按照sox-testing技能生成完整的控制测试底稿：

1. 识别关键控制——列出资金管理相关的控制点
2. 确定样本量——按控制频率（日/周/月）给出抽样表
3. 选取样本——随机、系统、定向三种方法
4. 生成测试模板——每个样本的测试步骤和预期证据
5. 缺陷分类——不足、重要不足、重大缺陷三个等级

它甚至会告诉你什么是充分证据、什么是不充分证据：

✅ 截图、签字审批、邮件确认、系统审计日志

❌ 单纯口头确认、无日期文档、无操作人记录

### 第三步：差异分析

输入：

/variance-analysis cash 2026-Q1 vs 2025-Q4

Claude把差异拆解成驱动因素——价格/量、利率/组合，生成瀑布图数据，附上文字解释。

### 第四步：生成凭证

输入：

/journal-entry prepaid 2026-03

如果连上了ERP，它会自动拉试算平衡表和预付摊销明细，生成：

12345678910凭证：预付费用摊销 — 2026年3月
编制人：Claude    日期：2026-03-31
 
| 行 | 科目编码 | 科目名称   | 借方    | 贷方    |
|----|---------|-----------|---------|---------|
| 1  | 6601    | 保险费     | 12,000  |         |
| 2  | 6602    | 软件费     | 8,500   |         |
| 3  | 1801    | 预付保险费 |         | 12,000  |
| 4  | 1802    | 预付软件费 |         | 8,500   |
|    |         | \*\*合计\*\*   | 20,500  | 20,500  |

---

![](attachments/c5e121369fbd432c.png)

## 这套架构的精髓

看完上面这个流程，你可能觉得：这不就是让AI按步骤执行吗？

对。但关键不在于步骤本身，而在于**知识是怎么被组织起来的**。

每个SKILL.md文件其实就干了三件事：

1. 定义触发条件——什么情况下该用这个技能（通过frontmatter里的description）
2. 编码专业知识——把审计方法论、会计准则、最佳实践写进markdown
3. 给出执行模板——输出格式、工作底稿模板、判断标准

这意味着你可以**完全自定义**。

Anthropic写的是SOX框架、GAAP准则、美国审计方法论。但目录结构是开放的——你fork一份，把中国的审计准则、企业会计准则、你的所内方法论塞进去，就变成了一个中国审计专用插件。

---

## 从单个场景到审计全流程：还有多远

finance插件展示了「知识编码」的可行性。但如果想在真实的国内审计项目里跑起来，光fork一份改改内容是不够的。

差距在哪？

**第一，准则体系完全不同。**

插件里写的是SOX 404、GAAP、COSO框架。中国审计用的是企业会计准则、中国注册会计师审计准则。两套体系的概念框架、术语体系、判断标准都不一样。

这不是翻译问题，是重写。

比如审计抽样——插件里用的是AICPA的抽样表，中国审计准则第1314号有自己的抽样逻辑和样本量要求。每个SKILL.md都得按中国准则重新组织。

**第二，数据接不上。**

插件的连接器指向Snowflake、BigQuery、Slack——这些都是美国企业的标准技术栈。

国内审计项目的现实是什么？

客户给你的是一堆Excel。科目余额表、明细账、银行对账单，全在Excel里。有的还是PDF扫描件。甚至还有纸质盖章的。

MCP连接器得换成能读Excel、读PDF、接企业微信/钉钉的。这个技术上有解决方案，但每个客户的系统都不一样，适配成本不低。

**第三，审计流程远比财务流程复杂。**

finance插件覆盖的是财务闭环——凭证、对账、报表、差异分析。这些是结构化的、流程化的，适合用技能文件来编码。

但审计的核心不是执行流程，是**判断**。

风险评估阶段，你得判断这个客户的收入有没有重大错报风险。这个判断取决于你对行业的理解、对管理层的评估、对经营环境的感知。这些东西很难写成SKILL.md里的规则。

实质性程序阶段更复杂。函证回函率不够怎么办？替代程序怎么选？发现的差异是调整项还是可接受误差？每个判断都依赖项目经验。

**第四，底稿标准和质量控制。**

每个事务所有自己的底稿模板、复核流程、质控标准。SKILL.md里输出的格式，不可能恰好匹配你所用所的要求。

更关键的是**责任问题**。AI生成的审计工作底稿，谁来签字？出了问题谁负责？目前这个插件在每个SKILL.md开头都写了一句话：

*This skill assists with workflows but does not provide audit advice. All outputs should be reviewed by qualified professionals.*

这行免责声明说明Anthropic自己也很清楚——现阶段它只能当助手，不能当审计师。

**第五，数据安全和保密。**

审计数据包含客户的核心财务信息。把科目余额表发给Claude，等于把客户的家底上传到Anthropic的服务器。

国内监管对数据出境有严格要求。大型审计项目的数据，大概率不能直接用云端AI处理。

（ 注：但可以借鉴用私有算力，开源 agent 工具实现 ）

---

![](attachments/f4c2bd92a9774fd5.png)

### 落地路径

说了这么多差距，不代表这事做不了。只是说需要一个务实的路径：

1. 先把知识层建起来。不考虑自动化，就按审计准则把每个环节的方法论、判断标准、底稿模板写进SKILL.md。这本身就是对所内知识体系的标准化——很多事务所连这个都没做完
2. 从数据输入端解决。不指望直接连ERP，先把「给AI一堆Excel它能读、能算、能生成底稿」这件事跑通
3. 选择性地自动化。别上来就想全流程自动化。银行对账、凭证生成、差异分析这些规则性强的环节先做，风险评估、职业判断这些先留给人
4. 本地化部署。用本地模型或者私有化部署解决数据安全问题。Claude Code支持第三方模型，这块是可以绕过去的

---

## 怎么装

在Claude Code里两行命令：

12345*# 先添加插件市场*
claude plugin marketplace add anthropics/knowledge-work-plugins
 
*# 安装finance插件*
claude plugin install finance@knowledge-work-plugins

装完自动生效。不用配置，不用写代码。

如果想自定义，fork到自己的GitHub仓库，改SKILL.md里的内容，重新安装就行。

---

## 写在最后

这个插件加起来大概 **60多KB** 的markdown文件，没有一行代码。

但它的意义不在于能立刻帮你跑完一个审计项目。说实话，离那个目标还有不小的距离。

它的意义在于展示了一种可能性：**审计知识是可以被结构化、被复用、被持续迭代的**。

在这之前，让AI懂审计的门槛是「训练一个审计领域的专业模型」。微调、数据标注、算力成本，光是想想就劝退了99%的事务所。

现在Anthropic把这个门槛降到了「写好你的审计方法论」。

把你的所内手册、审计准则理解、判断标准写进markdown文件，AI就能按你的方式干活。

这60KB不是终点。但它可能是一个起点。

![](attachments/a87c8bbb734457b3.jpg)
