---
title: feedback-save-to-evernote
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


保存微信公众号文章到印象笔记时：
- 一次发多篇链接 → 逐篇保存，最后汇总状态
- 用户会阅读保存结果并指出质量问题（段落合并、代码框丢失）
- 需要即时诊断并修复提取器，然后重存
- 每篇保存后给出简洁的指标对比（修复前 vs 修复后）
- 遇到 CAPTCHA 或不可达的链接，说明原因让用户重发

**Why:** 用户肉眼检查保存质量，发现问题直接反馈，需要快速响应修复。
**How to apply:** 批量保存后不要直接结束，等待用户反馈。如有质量问题，诊断 DOM 结构 → 修复提取器 → 重存。
