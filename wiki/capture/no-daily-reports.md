---
title: no-daily-reports
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


用户明确要求：**不要再生成任何日报类内容**，包括但不限于：
- 印象笔记日报
- 其他形式的每日摘要/简报

**Why：** 用户不需要自动生成的每日报告，这些内容打扰且无用。

**How to apply：** 任何涉及"日报""每日报告""每日摘要""daily digest"类的生成，直接跳过。除非用户主动要求。特别是不在 nohup 或后台自动任务中生成此类内容。

参考：llm-daily-digest skill 也不应主动触发日报生成。
