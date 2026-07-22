---
name: 20260716-non-ctrip-channel-rate-plan
type: source
tags: [huacheng, data-analysis, implementation-plan, reconciliation, checkpoint]
source_path: /Users/panbo/Obsidian/程序开发/20260716-非携程渠道达成率分析-plan.md
---

[摘要] 本文档是非携程渠道达成率分析工具的实施计划，包含 7 个任务的完整代码和设计。目标：新建 skill，对华程全客户公司（941 个，含携程）的达成率做对账+诊断+客户分层，输出 4 sheet Excel。架构为单文件主脚本 `analyze.py`（配置区+加载+对账+诊断+分层+输出），配套 SKILL.md。Tech Stack 为 Python3 + openpyxl，不引入 pandas/polars。关键口径：看板全 941 客户公司（含 264 携程+677 非携程），订单状态 4 种均计入实际成交（已成交/部分退订/担保占位/订金占位），按出发日期而非下单日期。每步写 checkpoint CSV 支持重跑跳过。执行中途发现平台分类器故障（claude-glm-5.2 模型不可用导致 auto 权限分类器阻塞写操作），只读可用。执行实测 Task1+2 已跑通：看板行数 5704、有效订单 48410、对账客户 947、匹配 822/订单表无匹配 111/看板无完成产量 10/订单偏低 4、平均绝对差异率 0.1%（口径一致，以看板为准）。另有国四（携程/同程/途牛/众信）/省五（每省总容量前 5）客户指标覆盖分析增强版。原文链接：/Users/panbo/Obsidian/程序开发/20260716-非携程渠道达成率分析-plan.md