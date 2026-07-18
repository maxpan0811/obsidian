---
title: agents-md-claude-hierarchy-2026
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 改动

2026-06-13 将 Workspace 层（`~/`）改为**共享真理 + 工具桥接**架构：

| 文件 | 角色 |
|------|------|
| `~/AGENTS.md` | 共享真理层：项目索引、跨项目路径、工具链、Memory 索引、通用工作约定 |
| `~/CLAUDE.md` | Claude 桥接层：首行 `@import AGENTS.md` + Claude 专属规则（模型选择、分层索引、权限排除） |

同时更新了：
- `~/.claude/CLAUDE.md` 中 Workspace 层描述 → 指向桥接层
- `~/.codex/AGENTS.md` 中 Workspace 层描述 → 指向共享真理层

## 为什么

原本 `~/CLAUDE.md` 与 `~/AGENTS.md` 内容几乎重复，改了一边忘改另一边（`~/AGENTS.md` 还指向废弃的 `业务数据` 目录）。Codex 不读 `CLAUDE.md`，Claude Code 也不读 `AGENTS.md`，双维护必然腐化。

## 如何应用

- 修改通用规则（项目路径、工具链、约定）→ 只改 `~/AGENTS.md`，两者自动感知
- 修改 Claude 专属规则（`@import`、`allowed-tools`、模型选择）→ 只改 `~/CLAUDE.md`
- Codex 专属规则 → 只改 `~/.codex/AGENTS.md`
- 项目级 AGENTS.md 可以 `@import` 上级 AGENTS.md 继承共享规则
