---
name: 20260715-deskdash-market-share
type: source
tags: [deskdash, market-share, ubersicht, widget, data-pipeline]
source_path: /Users/panbo/Obsidian/程序开发/20260715-deskdash-market-share.md
---

[摘要] 本文档是携程市占率桌面看板的完整实施计划和实施记录。目标：在 macOS 桌面上通过 Übersicht 桌面 widget 实时显示华程双品牌市占率，5 个产品板块（欧洲/美洲/澳新/中东非/中亚高加索）× 6 个大区（华北/华东/华西/华南/华中/福建）× 4 项指标（华程市占/市占率同比/华程营收同比/大盘营收同比）的矩阵数据，支持月/季/半年时间切换。架构为两层：Python Polars ETL 管线读取 3 个 artnova 年度订单明细 Excel 文件，计算聚合切片，输出 JSON；Übersicht CoffeeScript widget 读取 JSON 文件在桌面上渲染。实施过程中遇到 Übersicht JSX 编译不稳定（改用 CoffeeScript）、Widget 目录名过长导致编译失败（改名 ms.widget 解决）、口径校准（从下单日期改为出发日期、考核区域口径偏大）、Widget 编译交互功能被移除等问题。最终状态：数据管线可跑，JSON 已生成，但 widget 处于 hidden 状态未显示，口径待校准。原文链接：/Users/panbo/Obsidian/程序开发/20260715-deskdash-market-share.md