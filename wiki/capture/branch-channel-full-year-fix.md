---
title: branch-channel-full-year-fix
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-19
created: 2026-07-19
---


分公司渠道明细(branch_channel)数据结构必须同时包含同期和全年字段。

**Why:** 2026-07-19 发现看板"25年全年"列显示与"25年同期"完全相同的数值，因为 branch_channel 只有 ctrip25/nonctrip25（同期），缺少 ctrip25_full/nonctrip25_full（全年）。模板直接用同期值填全年列。

**正确数据结构:**
```
branch_channel[分公司][产品] = {
    ctrip26, nonctrip26,       # 26年同期
    ctrip25, nonctrip25,       # 25年同期（下单日期<=7/16）
    ctrip25_full, nonctrip25_full  # 25年全年
}
```

**How to apply:**
- export 脚本：26年循环加日期过滤（同期口径），25年循环分两路聚合（全年+同期）
- template：25年全年列读 `ctrip25_full`/`nonctrip25_full`，占比用 full 基数算
- 同理：任何有"同期"+"全年"两列的场景，数据源必须分别提供两个值
