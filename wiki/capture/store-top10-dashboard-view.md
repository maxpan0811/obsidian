---
title: store-top10-dashboard-view
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 门店市占率 Top10 视图实现（2026-07-18）

## 做了什么

在桌面看板中新增第三个视图 **store_top10（门店市占率）**：

### 新增
- `export_store_top10.py` — 读 `/tmp/store_view_final2.json`（19时段×6大区×30省×Top10门店）→ 标准化 `store_top10.json`
- template 新增 `renderStoreTop10Table()` — 9列表格（排名/门店名称/26产量/26双品牌/26市占/25产量/25双品牌/25市占/市占同比）
- 省表头：「XX家门店 Top10占比XX% | 省双品牌市占XX% 同比±X.X%」
- 低市占 < 40% 标红（`.low-share` CSS）+ `fmtRev` 营收格式化（≥10000万→亿，≥1→万）

### 修复
- **国四/省五筛选按钮** — 标签一致性视图新增客户类型栏（[省五][国四]），切换数据源（`provinces`/`guosi_provinces`），国四格式为单列客户列表
- **按钮凹陷问题** — `.pbtn.active` 加 `!important` 确保 Platinum 凹陷样式（上左暗边、下右亮边、深灰底）
- **表格对齐** — 标签一致性表格加 `table-layout: fixed` + 固定列宽比例（rank 3%/name 25%/num 10%/chk 8%/mgr 9%），省头横幅与表格对齐

### 关键决策
- 数据源用现已存在的 `/tmp/store_view_final2.json`，不复写口径（用户确认不动）
- 国四格式不同于省五（单列客户列表 vs 核心/容量双列对比），`renderLCTable()` 按 `lcType` 分两支渲染
- 用 `!important` 修复按钮状态而非改 CSS 结构——最小改动原则

**Why：** 用户需要看各省内头部门店的双品牌市占率，识别低渗透门店（<40%标红）以便针对性提升。
**How to apply：** 未来更新数据时替换源数据文件 → 跑 `export_store_top10.py` → 跑 `build_dashboard.py`

[[deskdash-market-share.md]]（上层设计）·[[dashboard-html-build-pitfalls.md]]（HTML陷阱）·[[dashboard-store-top10-view.md]]（原设计）
