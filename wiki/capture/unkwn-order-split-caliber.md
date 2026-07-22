---
title: unkwn-order-split-caliber
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-23
created: 2026-07-23
---


# unkwn 线上订单拆分口径（2026-07-23 确认）

## 用户决策（Q1-Q3）
- **Q1**：branch_channel 只拆 `订单销售公司='unkwn'` 的订单，用 `新架构团公司` 字段判断分公司归属。事业部订单（订单销售公司=事业部名）不拆。
- **Q2**：national_overview/全国合计不动——全国合计本就是全部产量(32.95亿)，门店省份只影响内部不显示的"未分配"桶，不改。
- **Q3**：事业部订单（中东非澳洲事业部/美洲中亚事业部等）**不拆、不单列事业部行，只折进全国合计**。

## 拆分实现（export_desktop.py branch_channel，26同期+25年两循环）
```python
company = str(o.get('订单销售公司', '')).strip()
if company == 'unkwn':
    company = str(o.get('新架构团公司', '')).strip()  # unkwn 用新架构团公司 fallback
branch = COMPANY_TO_BRANCH.get(company)
if not branch:
    continue  # 事业部值(中东非澳洲事业部等)不映射→跳过，不进分公司明细
```
COMPANY_TO_BRANCH keys：北京公司/上海公司/广州公司/成都公司/武汉公司/厦门公司/内蒙古招商公司 → 6分公司。

## 数值（cutoff 7/20，文件20260720）
- unkwn 订单共 4.57亿：其中新架构团公司=上海/北京/广州/成都公司 ≈2.0亿→进分公司明细；新架构团公司=事业部值(中东非澳洲事业部16,822/目的地参团4,499/美洲中亚4,334/海外拼小团28)≈2.57亿→不进。
- 事业部订单(订单销售公司=事业部名：美洲中亚事业部24,589/中东非澳洲事业部18,988/集团欧洲事业部3,062/新渠道2,234等)≈4.9亿→不进分公司明细，折进全国合计。
- 修复后：branch_channel 6分公司合计 23.46亿→25.47亿(+2.0亿 unkwn拆分)；全国合计仍32.95亿。

## 关键区分
- 全国合计（national_overview 求和，含"未分配"桶）= 全部产量 = 32.95亿，永远对，不动。
- 分公司明细（branch_channel，6分公司）= 只含6传统分公司 + unkwn→新架构团公司可映射部分；事业部折进全国合计不单列。
- national_overview 内部"未分配"桶(5.69亿)不单独显示成行，只折进全国合计。

## 踩坑
- 07-23 初版拆分是**直接改HTML内嵌JSON**做的，没进export_desktop.py脚本。本会话用脚本重建(cutoff动态化+national_targets)时，脚本无拆分逻辑→**覆盖了07-23手改JSON的拆分**（branch_channel 24.16亿→23.46亿）。修复：把拆分写进脚本，重建自动存活。
- 教训：重建产物前核对脚本是否已含之前的直接JSON补丁，否则会丢失手改。

## 相关
[[branch-to-region-mapping]]（分公司归属用订单销售公司非门店省份）、[[ctrip-vs-nonctrip-field-caliber]]（unkwn是客户公司值10亿）、[[national-target-product-board-caliber]]、[[backup-before-modify]]
