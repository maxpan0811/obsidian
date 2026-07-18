---
title: huaxi_analysis_script
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


产品市占率分析工具 skill 下新增了 `update_huaxi_analysis.py`，基于华北脚本改造，核心差异：
- 省份：华西4省（四川、重庆、云南、贵州），线下门店所在省份和线上用户出发站省份均用此范围
- 输出：`华西欧洲携程平台双品牌产品市占率分析YYYYMMDD.xlsx`
- Sheet1/3/4 标题和标签改为"华西(4省市)"

**Why:** 用户要求出华西、华南、华东多个区域同口径数据，已逐步创建各区域脚本模板。
**How to apply:** 华南(粤桂琼)和华东(沪浙苏皖赣)可参照此模板，只需修改省份列表和输出文件名。
