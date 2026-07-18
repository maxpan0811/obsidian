---
title: feedback-excel-no-stripe
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


Excel 市占率分析报表中取消所有 E8F0FE 浅蓝偶数行条纹底纹，全部白色底，**仅保留黄色高亮行**（FFF2CC）。

**Why:** 条纹与黄色高亮叠加太花，不易阅读。2026-06-27 Hy 直接要求去掉。

**How to apply:**
1. 所有 update_*.py 脚本中，Sheet1 数据行 fill 只判断高亮：`fill = HL_FILL if is_hl else None`
2. Sheet3 同比增长和 Sheet4 季度的偶数行条纹 `fill = EVEN_FILL if dr3 % 2 == 0` / `fill = EVEN_FILL if qi % 2 == 1` 全部替换为 `fill = None`
3. openpyxl 中 E8F0FE 实际存为 `FFE8F0FE`（8位 RGB，不是 6位）
4. SKILL.md 中的格式化标准表里，"条纹行" 改为 "无条纹，全部白色底"

**关联文件:** `update_huabei_analysis.py`, `update_huaxi_analysis.py`, `update_sichuan_analysis.py`, SKILL.md
