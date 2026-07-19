---
title: raw-files-readonly
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-20
created: 2026-07-20
---


RAW/Excel 目录下的原始文件**只能读，不能动**（不改内容、不重命名、不删除）。

发现有重复文件时：移到 `~/Downloads/Temp/` 让用户自己判断，不要替用户做去重或清理的决定。

**Why:** 原始文件是数据源头，任何修改都可能破坏可追溯性。用户需要自己对原始数据做判断。

**How to apply:**
- ✅ `Raw/Excel/` 文件只读，用 DuckDB / openpyxl 读内容做分析
- ✅ 合并结果写入 `artnova/` 或其他输出目录
- ⚠️ 发现重复文件 → 移到 Temp/ 让用户自己判，不移也行但绝对不能删
- ❌ 禁止修改、重命名、删除 Raw/Excel/ 下的任何文件
- ❌ 禁止替用户做去重或清理决定
