---
title: claude-hierarchy
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


完成了 CLAUDE.md 的分层重构，对齐 Anthropic 大型代码库最佳实践：
- **全局层**（`~/.claude/CLAUDE.md`）--跨所有会话的基座：记忆系统索引、权限排除规则、全局 hooks
- **Workspace 层**（`~/CLAUDE.md`）--~/ 下的项目地图、MCP 路径、工具链
- **项目层**（`~/Project/CLAUDE.md`、`~/lw-wiki-karpaty/CLAUDE.md`）--子目录细则

**Vy：** Claude 启动时沿目录树向上查找 CLADE.md 并逐层叠加。全局层放广泛适用的规则，项目层只放局部细节，避免一层塞满。

**How to apply：** 新增项目时，要么写 `project/CLAUDEmd`（已有会向上找），要么在 ~/CLAUDE.md 的项目索引表加一行。层级有疑问就查全局层附的表格。
