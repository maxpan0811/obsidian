---
title: exclude-single-resource-schengen-visa
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 排除单资源和申根签证规则（2026-07-18 确认）

## 规则

在处理订单数据时，需要排除"目的地归属区域"列中的以下两个值：
- **单资源**
- **申根签证**

## 适用范围

- 26年订单数据
- 25年订单数据
- 所有基于订单数据的产量计算

## 原因

这两个产品类型不属于核心的跟团游业务，需要在数据分析时排除，以确保数据口径一致。

## 实现方式

在遍历订单数据时，检查"目的地归属区域"字段：
```python
region = o.get('目的地归属区域')
if region and str(region).strip() in ['单资源', '申根签证']:
    continue  # 跳过这条订单
```

**Why**: 用户要求排除这两个产品类型，确保数据分析口径一致。
**How to apply**: 在所有订单数据处理逻辑中添加此过滤条件。
