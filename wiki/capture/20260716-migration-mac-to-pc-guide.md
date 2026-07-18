---
title: 20260716-migration-mac-to-pc-guide
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## Claude Code Mac → PC 迁移经验（2026-07-16）

### 迁移包内容
打包文件：`~/Desktop/claude-code-migration-mac-to-pc.tar.gz`（427MB）

| 分组 | 包含 |
|------|------|
| 配置文件 | `~/.claude.json`, `~/CLAUDE.md`, `~/AGENTS.md` |
| 全局规则 | `~/.claude/CLAUDE.md`, `~/.claude/settings.json`, `~/.claude/settings.local.json` |
| 私有规则 | `~/.claude/rules/` (3个：auto-memory, cite-sources, context7) |
| 记忆系统 | `~/.claude/projects/-Users-panbo/memory/` (181条) |
| Skills | `~/.claude/skills/` (104个技能目录) |
| MCP 配置 | `~/.claude/mcp.json`（含 API Key） |
| 活跃任务/模板 | active-task.md, analysis-request.md |
| 定时任务 | scheduled_tasks.json, jobs/pins.json |
| Hooks | 2个 .sh 脚本 |
| 自定义脚本 | 6个 .py/.sh |

### 已排除（不需迁移）
- sessions/, session-env/, file-history/（平台无关）
- venvs/（Windows 需用 `uv sync` 重建）
- telemetry/, cache/, paste-cache/, backups/（缓存/临时数据）
- daemon/, data/, src/（平台相关）

### PC 端必须调整的文件
| 文件 | 调整内容 |
|------|---------|
| mcp.json | npx 命令路径 → Windows 格式；API Key 重配 |
| hooks/*.sh | 改为 .bat/.ps1 或重写逻辑 |
| settings.json deny 路径 | macOS → `C:\Users\...` |
| settings.local.json | 权限配置路径改 Windows 格式 |

### 验证步骤
1. 启动 Claude Code，问"我的记忆有哪些" → 应看到 181 条
2. 测试一条私有规则（如 cite-sources）是否自动触发
3. 测试 MCP 连接

### 相关记忆
- [[20260716-skills-crosspc-audit]] — 跨 PC 迁移前 skills 全量审计
- [[20260716-skills-quote-dir-cleanup]] — skills 目录脏数据清理

**Why:** 这套配置涉及 100+ skills、私有规则、记忆系统、MCP 集成和定时任务，需要完整打包而非手动逐项搬运，避免遗漏。排除 sessions/venvs 等平台无关数据以减小包体积。
