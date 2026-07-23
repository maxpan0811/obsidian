---
title: dashboard-html-naming-modification-date
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-23
created: 2026-07-23
---


# 渠道管理看板 HTML 文件名口径

**文件名**：`2026年华程渠道管理数据看板-{修改日期MMDD}.html`
- 修改日期 = `datetime.now()` 的今天（MMDD），**不是**数据下载/cutoff日期。
- 数据下载日期（看板内 `updated` 字段，如 2026-07-20）与文件名后缀（如 0723）**不一定相同**——数据可能7/20下载、7/23才改看板。

**Why（用户纠正 2026-07-23）**：我曾用数据updated日期做后缀→-0720，用户纠正"文件名日期应是当前修改日期，和数据下载时间不一定相同"。

**How to apply**：
- `build_dashboard.py`（桌面看板 skill）已改为 `data_date = datetime.datetime.now().strftime("%m%d")`，直接写 `~/Desktop/2026年华程渠道管理数据看板-{MMDD}.html`。
- 同日多次重建同名自覆盖（不产生副本）；跨日重建才换后缀（产生新 -MMDD，旧的按需清理）。
- ❌ 不要再手动 `cp 看板.html -MMDD.html`——build_dashboard 直接产出带日期文件，无需中间无后缀副本（会分叉）。
- ❌ 不要用 view.updated（数据日期）做文件名后缀。

**相关**：[[backup-before-modify]]、[[unkwn-order-split-caliber]]、[[同期同比定义规则]]
