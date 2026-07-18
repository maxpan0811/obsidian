---
title: active-task-work
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


借鉴 PAI 的 WORK 层设计，在 `~/.claude/active-task.md` 记录活跃任务状态。

**Why:** 之前的 memory 只保存"做完后值得记住的经验"，但进行中的任务状态（分析到哪一步了、数据源是什么、卡在哪儿）会话结束就丢了。下次启动得从头沟通。

**How to apply:** 
- 启动新任务时在 active-task.md 填写任务标题、数据源、当前状态、下一步
- 任务完成时更新状态并清空"活跃任务"区段
- 会话启动时自动读取此文件恢复上下文
- 经验类的收获仍写入 memory/
