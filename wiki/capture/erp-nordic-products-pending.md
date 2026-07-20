---
title: erp-nordic-products-pending
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-20
created: 2026-07-20
---


**华程北欧产品分析进展（2026-07-20）**

使用"华程欧洲产品比较工具"分析华程集团北欧产品时发现：

**已确认的北欧产品：**
1. 北京出发 · 私家团精品冰岛一地极光+瑞典10天8晚（ID: 1674710）— 3钻，翔龙万里行
2. 上海出发 · 【ZWY包团】精品挪威罗弗敦群岛+冰岛18天16晚（ID: 1690751）— 4钻，翔龙万里行

**瓶颈：**
- `ms.hcgtravels.com` 老ERP极不稳定，Playwright 90%请求超时，curl间歇性成功（~25%）
- `uat.api.etibooking.com/swagger` 返回403/404（可能需内网或本机IP）

**下一步：** 明天获取 ERP MCP 后重新完整扫描各分公司北欧产品，补价格字段

**Why:** 用户要求拉取各分公司全部北欧产品汇总，当前只获取到27个已知产品ID中的2条北欧
**How to apply:** 获取ERP MCP后，直接用MCP工具查询"北欧"/"冰岛"/"挪威"等关键词，提取详情后补充Excel

**相关链接：**
- Excel已输出到桌面：`华程北欧产品总表.xlsx`
- SKILL: `hc-europe-product-compare`
