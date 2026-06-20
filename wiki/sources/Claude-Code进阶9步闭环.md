---
title: Claude Code进阶9步闭环
type: source
created: 2026-06-20
updated: 2026-06-20
source_path: 印象笔记管理工具/Claude Code进阶9步闭环.html
tags: [编程, AI]
---

Claude Code进阶9步闭环
原文链接: https://mp.weixin.qq.com/s?__biz=MzkyNzY5MTM5OA==&mid=224748...多数人把 Claude Code 当成需要盯着看的初级助手：提需求、看改动、人工检查、再继续。真正高效的用法，是把它纳入一套类似资深工程师的工作闭环。这套方法核心不是换更强模型，而是搭建流程：先用 Explore subagent 只读理解代码库；再进入 Plan Mode，列出改动文件、顺序和风险；把团队规范写进 CLAUDE.md；按小步构建，避免巨大 diff；用 hooks 强制执行 lint、test 等关键检查；让代码用测试证明有效；再启动独立 review subagent 审查安全、边界条件和规范违背；发现问题后修复、重测、复审，直到 clean；最后把整套流程封装成 /ship slash comma…
