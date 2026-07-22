---
title: national-target-product-board-caliber
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-23
created: 2026-07-23
---


# 全国合计指标口径：用集团产品板块sheet，非分公司求和

**Why：** 预算表 `华程2026年预算指标汇总_分公司事业部月度.xlsx` 含两 sheet：
- 第一sheet `全国指标`（分公司×产品线分解）：**非欧产品基本为0**——分公司分解只列了欧洲为主，中东非/澳新/美洲只有个别分公司零星几条，中亚完全没有。中东非分公司求和仅2277万 vs 集团真实43162万，差近20倍。
- 第二sheet `集团产品板块指标`（2026-07-23 新增）：集团汇总口径各产品板块全年指标（含各事业部自有产品），欧洲388359/中东非43162/澳新23177/美洲38176/中亚5672/合计498546万。这才是全国真实指标。

**坑：** 看板全国"合计"行达成率 = total26 / natTarget。若 natTarget 用分公司求和（第一sheet），非欧产品达成率会荒谬偏高（中东非曾达1209%）。必须用第二sheet集团产品口径。

**How to apply：**
- 全国指标（各产品板块+全部）→ `load_national_targets(path)` 读第二sheet `集团产品板块指标`，返回 `{欧洲/美洲/澳新/中东非/中亚高加索/全部: gmv万}`
- JSON 字段 `national_targets`；template.html 合计行 `natTarget` 取 `v.national_targets[lcProduct]`（全部取`全部`）
- 分公司级指标（分公司视图、ind_coverage满足率）仍用 `branch_targets`/`load_budget`（第一sheet），分公司分解对分公司级是对的
- 板块名映射：`美洲(北美洲+南美洲)→美洲`、`中亚→中亚高加索`、`合计→全部`

**相关：** [[non-eu-data-from-sales-perspective]]（非欧数据来源）、[[同期同比定义规则]]（cutoff口径）
