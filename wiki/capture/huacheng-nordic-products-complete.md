---
title: huacheng-nordic-products-complete
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-20
created: 2026-07-20
---


**华程北欧产品分析完成（2026-07-20）**

通过 etibooking API 翻页抓取950个欧洲产品，精确过滤后确认 **104条** 北欧产品。

**数据来源：** etibooking API
- Swagger: https://api.etibooking.com/products/index.html
- Token 用户：彭彭（ID:9178）
- 搜索: POST /Product/SearchProduct → 按areaIds:[2](欧洲)翻页19页取950条
- 详情: GET /Tour/GetTourResourceInfo?tourId={id}

**各分公司北欧产品数量：**
| 城市 | 数量 | 价格区间 |
|:----:|:----:|:--------:|
| 上海 | 39 | ¥8,549 ~ ¥95,150 |
| 北京 | 37 | ¥6,999 ~ ¥123,299 |
| 广州 | 19 | ¥12,099 ~ ¥48,599 |
| 厦门 | 4 | ¥20,699 ~ ¥36,200 |
| 深圳 | 4 | ¥24,699 ~ ¥44,999 |
| 成都 | 1 | ¥44,199 |

**覆盖产品类型：** 惠品/质品/精品散拼、定制包团、北极邮轮、冰岛一地环岛、罗弗敦群岛深度、北欧多国连游+波海国家

**核心字段：** 产品名称、出发城市、目的地国家、钻级(几乎全4钻)、天数、同行价、直客价、产品类型、品牌(翔龙万里行)

**Why:** 用户用"华程欧洲产品比较工具"分析北欧产品，最初只找到2条(ERP不稳定)。后通过API翻页950条完整扫描找到104条
**How to apply:** 翻页欧洲全量产品(areaIds:[2])可获取完整产品列表，关键词搜索结果受限。单条详情用TourId查。

**Outstanding:**
- 老ERP中冰岛一地+瑞典产品(id=1674710)在新API不存在
- 待ERP MCP对比验证完整性
- 如需月份拆分价格需查Tour/GetOtherTourByProductId接口

**相关链接：**
- Excel: `/Users/panbo/Desktop/华程北欧产品总表.xlsx`
- SKILL: `hc-europe-product-compare`
