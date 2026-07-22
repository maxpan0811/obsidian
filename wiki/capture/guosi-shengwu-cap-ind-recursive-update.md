---
title: guosi-shengwu-cap-ind-recursive-update
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-23
created: 2026-07-23
---


# 国四省五客户数据批量更新（cap/ind/prod26）

## 口径：容量只统计有指标的产品板块

从 `华程客户公司相关数据看板20260722.xlsx` 更新国四/省五客户的 cap/ind/prod26 时：

| 字段 | Excel 源列 | 口径 |
|------|-----------|------|
| ind | 指标金额(万元) | 按 目的地区域→产品板块聚合，SUM |
| cap | 总容量(万元) | **只统计该客户有 ind>0 的产品板块** |
| prod26 | 累计完成产量(万元) | SUM |

❌ 错误：把所有目的地区域的容量都加起来（含无指标的板块）→ 天津携程 cap=8200（错）
✅ 正确：只加有指标金额的板块 → 天津携程 cap=5500（对，欧洲=5500）

**Why**：容量是配合指标使用的——客户只在有指标的板块有考核容量，美洲/澳新等无指标板块的容量不算入。

## JSON 递归全节点更新

看板的 `periods` 结构中，每个月份/季度/半年/全年都复制了完整客户数据副本。
只更新顶层 `guosi_data`/`provinces` 不够——必须递归 walk 整个 JSON 树。

❌ 错误：只更新 `v['guosi_data']` + `v['guosi_provinces']` + `v['guosi_groups']`
→ 57 处旧值残留（`periods` 中的副本未更新）
✅ 正确：递归遍历所有节点，匹配到 `name` 字段就更新

```
def walk_and_update(obj):
    if isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict) and 'name' in item:
                update_item(item)
            walk_and_update(item)
    elif isinstance(obj, dict):
        for key, value in obj.items():
            walk_and_update(value)
```

**How to apply**：以后更新此看板的任何客户数据，必须递归遍历全部 JSON 节点，不能只改顶层引用。
