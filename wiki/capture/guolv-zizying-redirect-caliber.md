---
title: guolv-zizying-redirect-caliber
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-23
created: 2026-07-23
---


# 国旅自营平台桶重定向口径（2026-07-23 确认）

## 背景
融合订单表里 `客户公司='携程'`（精确）≈10亿（cutoff7/20），是国旅自营平台直采桶。但看板**无"携程"客户条目**（只有携程旅行网-XX/携程国旅/携程-直采/携程旅游网-自营），所以 guosi（按看板客户名识别）抓不到这10亿，携程系 prod26 仅8.57亿、漏54%。

## 用户决策（B方案）
按 `新架构团公司` 字段把国旅自营量重定向到对应分公司下的**主携程旅行网账号**：

| 新架构团公司 | → 携程旅行网账号(看板字节一致) |
|------------|---------------------------|
| 上海公司 | 携程旅行网上海（12397）(注意:无"-") |
| 北京公司 | 携程旅行网-北京（12150） |
| 广州公司 | 携程旅行网-广东（11478）(广州→广东) |
| 成都公司 | 携程旅行网-成都（49242） |
| 湖北代理组 | 携程旅行网-湖北（46531）(仅64万2单,用户确认仍归此) |
| 事业部值(中东非澳洲/美洲中亚/目的地参团/海外拼小团) | **不映射**→留原"携程"(无看板条目,不进guosi,留全国合计,同Q3) |

公司可映射部分≈4.83亿分配；事业部≈5.16亿留全国合计。

## 实现（export_desktop.py）
- 模块级 `GUOLV_ZIZYING_REDIRECT` + `remap_cc_for_guolv(cc,o)` + `_remap_guolv_zizying(orders)`
- **main里加载订单后、reconcile_coarse/export_json前** in-place 重定向 `o['客户公司']`——一次性覆盖 reconcile_coarse(order_sum) + period(agg_by_departure_month) 所有按客户公司聚合的点
- 目标账号名须与看板**字节一致**（全角括号；上海无"-"其余有"-"），否则不聚合/不匹配看板客户

## 关键区分
- national_overview 用**门店省份**归分公司(不受客户公司remap影响)→全国合计32.95亿不变,无双重计算
- guosi/recs 用**客户公司**→remap后携程旅行网-XX含国旅自营份额
- branch_channel 用订单销售公司(不受影响)

## 数值(20260720)
携程系 prod26: 8.57亿→13.40亿(+4.83亿); 上海26.8k→59.6k/北京10.7k→21.3k/广东6.4k→10.9k/成都5.4k→5.8k/湖北2.2k→2.3k

## 相关
[[unkwn-order-split-caliber]](同用新架构团公司)、[[national-target-product-board-caliber]]、[[ctrip-vs-nonctrip-field-caliber]](unkwn是客户公司值)
