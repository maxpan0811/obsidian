---
title: feedback-excel-format
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Excel 数值格式偏好

所有 Excel 输出的数值和百分数格式统一规则：

- **数值**：千分号分隔，无小数位 → `#,##0`
- **百分数**：无小数位 → `0%`
- **字体**：微软雅黑
- **标题**：12pt，加粗
- **正文**：11pt
- **对齐**：文本左对齐，数字居中
- **列宽**：自适应最佳宽度（中文≈2.2字符宽，ASCII≈1.1）
- **行高**：标题行30，数据行22

## ⚠️ 常见陷阱

**`cell.font.name` 判断陷阱**：openpyxl 新建单元格默认 font.name='宋体'，不是 None。
```python
# ❌ 错误：这个条件永远为 True，导致格式化全部跳过
if cell.font and cell.font.name:
    continue

# ✅ 正确：直接覆盖，不需要先判断
cell.font = BODY_FONT
```

**How to apply:** Excel 导出脚本中不要用 `cell.font.name` 判断"是否已格式化"，默认字体不是 None。直接用全局覆盖即可。

**Why:** 2026-07-12 的 `add_target_analysis.py` 因为多了一个 `continue`，导致 3 个新增 Sheet 全部用了宋体 + General 格式，浪费一轮重跑。所有 Excel 格式化函数应该直接赋值，不要前置判断。

## How to apply:
新建 Excel 导出脚本时，数值格式用 `#,##0`，百分数用 `0%`，不要用含小数的格式。已有的渠道市占率分析工具、华北众信门店预估数据的脚本都已统一更新。
