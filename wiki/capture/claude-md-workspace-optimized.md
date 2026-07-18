---
title: claude-md-workspace-optimized
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**做了什么**
- `~/CLAUDE.md` 从 63 行 → 71 行
- 砍掉了与 `~/.claude/CLAUDE.md` 重复的层级索引表格、完成报告格式、元自检、private rules 清单、权限排除
- 新增：Working Style（从 4 条 feedback memory 聚合）、Do NOT 列表、Known Traps、Context Tiers

**Why**
- Workspace 层不应重复全局规则
- 聚合分散在 memory 里的行为规则，确保每次会话自动加载
- Do NOT 列表避免我已迁移的技术栈被重新引入

**How to apply**
- 今后 ~/CLAUDE.md 只放全局 CLAUDE.md 未覆盖的内容，不做冗余
- Working Style 有新经验时直接追加到此文件（不需要写在独立 memory 里再靠 MEMORY.md 索引）
- Known Traps 更新（Token 过期日、新发现的坑）直接修改此文件
