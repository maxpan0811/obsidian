---
title: feedback-excel-auto-col-width
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


所有市占率分析Excel文件输出前，**必须对每个Sheet调用自动列宽函数**（中文字符×2倍宽，英文×1.1倍，最小8最大40）。

**Why:** 列宽写死或漏调会导致数据被截断（如 `3,000,000` 只显示 `3,000,0`）或列距过宽难读。2026-06-27 Hy 明确要求所有输出Excel都加"最适合列宽"。

**How to apply:**
```python
def auto_col_width(ws, min_w=8, max_w=40):
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            if cell.value:
                v = str(cell.value)
                w = sum(2 if ord(c) > 127 else 1 for c in v)
                max_len = max(max_len, w)
        ws.column_dimensions[col_letter].width = max(min_w, min(max_w, max_len * 1.1))
```
每个Sheet写完之后调用 `auto_col_width(ws)`。

**关联:** SKILL.md 格式化标准表"列宽"行
