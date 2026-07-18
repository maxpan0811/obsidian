---
title: reference-deepseek-cost-skill
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## deepseek-cost-analysis skill

路径：`~/.claude/skills/deepseek-cost-analysis/`

分析 DeepSeek API 月度用量 CSV，生成六格可视化报告图（每日花费、模型堆叠、请求量、缓存命中率、模型饼图、API Key 对比）。

### 用法
```bash
cd ~/.claude/skills/deepseek-cost-analysis
python3 scripts/analyze.py <csv_dir> <year_month>
```

CSV 文件命名格式：`cost-{year}-{month}.csv`、`amount-{year}-{month}.csv`

输出：`reports/{year_month}/report.png` + `summary.json`

### 关键指标
- 缓存命中率通常 95%+（OpenClaw / Claude Code 用量）
- 综合有效成本远低于标价（命中率拉低 input 成本）
- v4-flash 约 0.07 CNY/百万token，最便宜的主力模型

### 模型价格 (CNY/百万token)
| 模型 | Output | Input Hit | Input Miss |
|------|--------|-----------|------------|
| chat & reasoner | 3.00 | 0.20 | 2.00 |
| v4-flash | 2.00 | 0.02 | 1.00 |
| v4-pro | 6.00 | 0.025 | 3.00 |
