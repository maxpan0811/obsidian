---
title: feedback-show-progress-every-minute
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 每分钟显示进度

**规则来源**: Hy 2026-06-27 明确要求

**规则**: 后台运行长时间任务（导出、批量处理、下载等）时，每 1 分钟显示一次进度，让用户了解当前状态。

**Why**: 用户需要实时感知工作进展，不是跑完了才通知。5 分钟间隔太长了，用户中途想了解进度时还得主动问。

**How to apply**: 
- 后台任务启动后，用 ScheduleWakeup 设置 `delaySeconds: 60` 的循环
- 每次显示：当前进度/总数 + 百分比 + 关键指标
- 如果进度没变化（进程卡死/rate limit），也要报告"等待中"而不是静默

**例外**:
- 如果用户说"说开始就跑"、"执行"等明确指令后没有附加条件，不等二次确认，立即执行
- 如果已知剩余时间 < 3 分钟，不停了，直接等完成
- 如果用户说"有进展再通知"才改为完成通知

**Related**: [[runtime-log-format]], [[feedback_context_management]]
