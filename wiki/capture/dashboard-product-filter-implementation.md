---
title: dashboard-product-filter-implementation
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 看板产品维度筛选实现（2026-07-18）

## 实现内容

### 1. 产品板块筛选按钮
- 在省五和国四视图都添加 5 个产品按钮（欧洲/美洲/澳新/中东非/中亚高加索）
- 切换产品时，表格按该产品的容量过滤和排序
- 只显示所选产品容量 > 0 的客户

### 2. 产品维度容量数据
- 从看板数据（华程客户公司相关数据看板）提取按目的地区域细分的容量
- 建立目的地区域 → 产品板块映射（PRODUCT_MAP）
- 每个客户存储 5 个产品的容量数据（product_cap 字段）

### 3. 省五/国四格式统一
- 省五：容量前5的非国四客户，与国四相同列结构
- 国四：所有国四客户（携程/去哪儿/同程/途牛/众信）
- 列结构：# / 客户名称 / 客户等级 / XX容量（万） / 客户指标（万） / 26年完成（万） / 达成率 / 25年完成（万） / 同比 / 负责销售
- 非核心客户等级标红
- 按产品容量降序排序

### 4. 数据格式标准
- 金额单位统一用"万"，表头加"（万）"备注
- 数据列只显示纯数值（千分位逗号），不带"万"/"亿"后缀
- 比率用百分号%（不是千分号‰）
- 数据截止日期从文件名提取（20260716 → 2026-07-16）

## 关键修改

### export_desktop.py（非携程渠道达成率分析工具）
- 添加 PRODUCT_MAP 映射目的地区域到产品板块
- 提取产品维度容量（get_product_cap 函数）
- 省五数据结构改为与国四一致（product_cap, ind, prod26, prod25, rate, yoy）
- 从看板文件名提取数据截止日期

### template.html（桌面看板）
- 添加产品板块按钮（省五和国四都显示）
- 省五/国四表格统一使用国四列结构
- 按产品容量过滤和排序
- 非核心客户标红
- fmtCap 函数改为返回千分位逗号数值（无后缀）
- 比率显示为百分号%（带千分位逗号）

## 数据流
```
看板数据（华程客户公司相关数据看板20260716.xlsx）
  ↓ load_board()
board_raw（包含目的地区域列）
  ↓ get_product_cap()
product_cap（5个产品的容量字典）
  ↓ export_json()
label_consistency.json（包含 product_cap 字段）
  ↓ build_dashboard.py
dashboard.html（前端筛选和排序）
```

## 经验总结

**Why**: 用户需要按产品板块查看客户容量，而不是总容量。省五原来的"核心vs容量"双列对比意义不大，改为与国四统一格式更实用。

**How to apply**: 
- 未来新增产品板块时，更新 PRODUCT_MAP 映射
- 数据格式标准适用于所有看板视图
- 日期必须从文件名提取，不硬编码

## 2026-07-18 后续修正：同期同比计算

### 问题
用户指出"同比"应该是"同期同比"，不是简单的全年对比。

### 正确定义
**同期同比** = 以相同的预定日期为截止点，对比不同年份的全年出发产量

例如：
- 2026年同期同比 = 2026年7月16日之前预定的 → 2026年全年出发的产量
- 2025年同期同比 = 2025年7月16日之前预定的 → 2025年全年出发的产量

### 修正实现
修改 `export_desktop.py` 的 `reconcile_coarse` 函数：
- **2026 prod26**：使用看板数据的"累计完成产量"（已是下单日期<=2026-07-16的2026年出发产量）
- **2025 prod25**：从订单数据筛选（下单日期<=2025-07-16 且 出发日期在2025年）
- **yoy** = (prod26 - prod25) / prod25

### 关键代码
```python
# 2025年同期数据：筛选下单日期 <= 2025-07-16 且出发日期在2025年的订单
from datetime import datetime
cutoff_date_2025 = datetime(2025, 7, 16)
order_sum_2025 = defaultdict(float)
for o in orders_2025:
    cc = o.get('客户公司')
    amt = o.get('成交销售额')
    if cc and amt is not None and str(cc) not in SKIP_CUSTOMERS:
        order_date_str = o.get('下单日期')
        dep_date_str = o.get('出发日期')
        if order_date_str and dep_date_str:
            try:
                order_date = datetime.strptime(str(order_date_str)[:10], '%Y-%m-%d')
                dep_date = datetime.strptime(str(dep_date_str)[:10], '%Y-%m-%d')
                if order_date <= cutoff_date_2025 and dep_date.year == 2025:
                    order_sum_2025[str(cc)] += float(amt) / 10000
            except (ValueError, TypeError):
                pass
```

### 经验
**同期同比** ≠ 简单全年对比，必须按相同的预定日期截止点筛选，才能反映真实的预订进度对比。
