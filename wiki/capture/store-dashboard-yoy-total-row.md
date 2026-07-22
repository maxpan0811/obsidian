---
title: store-dashboard-yoy-total-row
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-22
created: 2026-07-22
---


# 门店管理看板：总计行 + 同期同比列

## 2026-07-22 新增功能

在「携程渠道」「全部大区」「全部产品」视图的表尾新增：

### 总计行
- 双线分隔（`border-top:3px double #333`），灰底（`#e0e0e0`），加粗
- 门店数/旅顾数求和，产量求和后重算市占和同比

### 同期同比列
- 公式：`(26年总产量 - 25年总产量) / 25年总产量`
- 颜色：↑绿(up) / ↓红(down) / →灰(zero)
- 定义见 [[同期同比定义规则]]

### 修改位置
- 文件：`~/Desktop/2026年华程门店管理数据看板.html`
- 函数：`renderStoreTop10Table()` → `lcRegion === '全部'` 分支

### 待办
- [ ] 构建脚本 `/tmp/build_store_dashboard.py` 丢失，需恢复或重写
- [ ] 途牛/同程构建脚本 `/tmp/build_tuniu_tongcheng.py` 也丢失
- [ ] 数据更新至最新 Excel（当前截止 2026-07-16）

**Why**：用户要一眼看到全国总量和同比增长情况，不用自己心算。
