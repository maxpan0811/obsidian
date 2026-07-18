---
title: feedback_file_date_update_rule
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


输出报表或修改脚本重新生成时，文件名和报表标题中的日期**永远用当天实际日期**，不能沿袭旧文件的日期。

- 数据截止日期写当天（YYYY-MM-DD），非数据源本身的日期
- 脚本中 `OUTPUT_FILE` 的日期也同步改为当天

**Why:** 用户反复纠正过这个问题。文件日期应与修改时间一致，方便版本管理。
**How to apply:** 每次创建/更新分析脚本时，脚本内每个日期字串都检查一遍。`OUTPUT_FILE` 路径和 Excel 标题中的日期字符串一并改为当前日期。
