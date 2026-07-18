---
title: channel-share-analysis-skill
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 渠道市占率分析工具

Skill 路径：`/Users/panbo/.claude/skills/渠道市占率分析工具/`
分析脚本：`scripts/analyze_ctrip_europe.py`

## 数据源

`/Users/panbo/Documents/业务数据/artnova/携程渠道数据/25年和26年1-4月携程渠道门店海长数据.xlsx`
80 列订单明细，Sheet 名 `noSave_53516_1778921320908`

## 品牌定义

- **华程**：订单归属（col 3）含"华程"（广州/上海/北京/成都/武汉/厦门/其他华程订单）
- **自营**：下单时是否双好自营（col 68）= 1
- 旅行顾问 uid（col 42）大量为 `unkwn`，旅顾从门店名称以"旅行顾问"前缀提取

## 当前分析

2026-05-21：福建省厦门市欧洲渠道，前20门店 + 前10旅顾
- 输出：`欧洲携程渠道双品牌渠道市占率分析20260521.xlsx`
- 2026年同比2025年总营收下降约29%（1-4月口径）
- 厦门欧洲渠道华程占绝对主导（Top门店85-94%），自营几乎无数据
