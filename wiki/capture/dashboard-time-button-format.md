---
title: dashboard-time-button-format
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


看板时间按钮标准格式（2026-07-17 用户确认"特别好"）：

```
[月] [季] [半年] [全年]  [下拉框选具体月/季]
```

- 4个类型按钮：月、季、半年、全年
- 选中类型后，右侧出现下拉框选择具体时段（如选了"月"，下拉框显示1-12月）
- 放在筛选栏最右侧（`margin-left:auto`）
- CSS 类名：`seg`（标签）、`pbtn`（按钮）、`active`（当前选中）

**Why**：用户2026-07-17明确说"这个时间按钮设置的特别好，以后都可以用这种格式"。产品市占率表的renderPeriodBar是最初设计，门店市占率表复制了同样的格式。

**How to apply**：未来新增看板视图的时间筛选，统一用这个格式。不要用把所有月份平铺展开的方式（太丑太长）。
