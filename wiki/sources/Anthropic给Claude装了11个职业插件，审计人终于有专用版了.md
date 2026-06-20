---
title: Anthropic给Claude装了11个职业插件，审计人终于有专用版了
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Anthropic给Claude装了11个职业插件，审计人终于有专用版了.html
tags: [AI技术]
---

# Anthropic给Claude装了11个职业插件，审计人终于有专用版了

原文链接: https://mp.weixin.qq.com/s?__biz=MzI0MjgxMzg1Mw==&mid=224750...

...Anthropic给Claude装了11个职业插件，审计人终于有专用版了Originalnigo 逆行的狗 
上周用Claude Code写了个关联方识别的Skill，跑了一遍12个维度的自动核查，效果还不错。
但这几天GitHub上出现了一个更有意思的东西——Anthropic自己下场了。
他们开源了一套叫 knowledge-work-plugins 的项目，给Claude装上了11个职业角色插件。销售、法务、财务、产品经理……每个插件把一个岗位的专业知识、工作流程、工具连接全部打包好，装上就能用。
其中有一个 finance 插件，直接覆盖了审计和财务的工作场景。
14k⭐，一周不到。
https://github.com/anthropics/knowledge-work-plugins
这个插件到底是什么先说清楚它不是什么。
它不是一个App，不是一个网站，也不是一个SaaS产品。
它是一堆 markdown文件。
对，就是跟你平时写笔记一样的markdown。只不过这些markdown里装的是专业知识——怎么做凭证、怎么做银行对账、怎么做SOX测试、怎么做差异分析。
Claude读了这些文件，就变成了一个懂财务和审计的助手。
这跟我们现在用的Skill本质上是一回事。只不过Anthropic把它标准化了，给了一套固定的目录结构。
架构：三层设计每个插件由三部分组成：
第一层：Skills（技能）
核心知识层。每个技能是一个SKILL.md文件，包含某个工作领域的完整方法论。
finance插件目前有8个技能：
技能
干什么
audit-support
SOX 404控制测试、抽样方法、缺陷分类
reconciliation
银行对账、GL与子账核对、关联方对账
journal-entry
凭证准备——应计、折旧、预摊、薪酬、收入
journal-entry-prep
凭证编制最佳实践和审核流程
financial-statements
财务报表生成（利润表、资产负债表、现金流量表）
variance-analysis
差异分析——价格/量、利率/组合分解
close-management
月末结账检查清单和任务排期
sox-testing
SOX合规测试——样本选取、测试底稿模板
Claude会根据你问的问题，自动匹配相关的技能文件来辅助回答。
第二层：Commands（命令）
你可以用斜杠命令直接触发特定操作：
/journal-entry ap-accrual 2026-03 — 自动生成AP应计凭证
/reconciliation cash 2026-03 — 执行银行对账
/sox-testing revenue-recognition 2026-Q1 — 生成收入确认控制测试底稿
/variance-analysis revenue 2026-Q1 vs 2025-Q4 — 收入差异分解
/income-statement monthly 2026-03 — 生成月度利润表
每个命令后面跟的是参数，告诉Claude具体要处理什么。
第三层：Connectors（连接器）
通过MCP协议连接外部数据源。配置写在 .mcp.json 里：
 
 
 
1234Snowflake → 数据仓库，直接拉科目余额
BigQuery → 查询财务数据
Slack → 发送报告、催审批
Mic
