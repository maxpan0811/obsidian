---
title: Claude Code三大利器命令用法
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Claude Code三大利器命令用法.html
tags: [AI技术]
---

# Claude Code三大利器命令用法

原文链接: https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=224748...

Claude Code 的 /goal、/loop、/workflows 常被误解为“让 Claude 多干一会儿”，其实三者解决的是完全不同的问题。/goal 管终点：给出可验证的完成条件，Claude 会多轮执行，达标即停，适合测试全绿、编译通过、issue 清空等任务。/loop 管节奏：按固定时间间隔重复执行同一件事，适合轮询 CI、部署状态、PR 列表或远程任务队列。/workflows 管规模：它不是启动任务，而是查看已启动 Workflow 的并行进度，适合大任务拆分、多智能体协作、批量迁移和交叉验证。判断方法很简单：终点明确且可验证，用 /goal；需要定时值守，用 /loop；任务太大、需要分头并行，先发起 Workflow，再用 /workflows 看进度。选错命令，浪费的不是功能，而是停止逻辑、时间节奏和协作结构。
Close
