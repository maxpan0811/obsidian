---
title: config-stack-hooks-rules
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-06-13 受一篇 Claude Code 配置栈文章启发，做了三层对标改进。

## 改动清单

### 1. PostToolUse Auto-Format Hook
- 文件：`~/.claude/hooks/auto-format.sh`
- 触发：每次 Write/Edit/MultiEdit 后
- 行为：`.py` → 静默跑 `ruff format`；`.md` → trim trailing whitespace
- 预期效果：不再需要手动格式化，文件在下一轮对话前就是干净的

### 2. PreToolUse Git Push Gate
- 文件：`~/.claude/hooks/gate-git-push.sh`
- 触发：每次 Bash 执行前
- 行为：检测到 `git push origin main` 或 `git push ... main` → 返回 `defer` 暂停 session，等人工审批
- 预期效果：防止夜间 headless 或手滑误推 main

### 3. Path-Scoped Rules for artnova
- 目录：`~/Documents/artnova/.claude/rules/`
- 文件（从 memory 中迁移出来的业务规则）：
  - `business-excel-format.md` — 数值格式、字体、列宽行高
  - `business-data-caliber.md` — 品牌归属、供应商排名、门店省份映射、营收口径
  - `business-analysis-output.md` — 文件日期更新、数量核对、旧文件清理
- 加载时机：仅当操作 `Documents/artnova/**` 路径时
- 说明：原放在 `~/Documents/业务数据/` 下，后废弃该目录迁移至此

### 4. settings.json 更新
- `~/.claude/settings.json` hooks 段新增 PreToolUse + PostToolUse 两个 hook 组
- 现有的 Stop/Notification/UserPromptSubmit hooks 不受影响

**Why:** 之前业务数据口径规则散落在 memory 各条记录中，靠 recall 加载，既不自动也不及时。改为路径级 rules 后，只有在操作相关目录时才消耗 token。两个 hooks 是零成本 + 高 ROI 的确定性护栏。

**How to apply:**
- 继续分析 `Documents/artnova/` 下的 Excel 时会自动加载 rules
- hook 脚本在每次文件写操作后静默执行
- 在 `Documents/artnova/` 下生成任何 `.xlsx` 后，`~/Documents/artnova/.claude/CLAUDE.md` 强制要求自动调用 reviewer subagent 审查（写入工作流规则，非 hook 触发）

### 5. Custom Subagents for Report Review
- 文件：
  - `~/.claude/agents/business-report-reviewer.md` — 市占率/达成率报表审查
  - `~/.claude/agents/alliance-analysis-reviewer.md` — 联盟包团分析报表审查
- 模型：deepseek-v4-flash（便宜模型）
- 工具：Read, Grep, Glob, Bash(openpyxl only) — 窄权限只读
- 触发：每次生成报表后手动调用 Agent { subagent_type: "business-report-reviewer" }
- 覆盖：格式合规 → 数据口径 → 文件管理 → 供应商分析
- 入口：`~/Documents/artnova/.claude/CLAUDE.md` 中列出了工作流和调用方式

**Why:** 之前每次生成报表后全靠肉眼检查。subagent 用便宜模型在隔离上下文里跑 checklist，不占主循环 token 和昂贵模型。

**How to apply:** 生成 `artnova/` 下的 `.xlsx` 报表后，用 `Agent { subagent_type: "business-report-reviewer", prompt: "审查 artnova/下最新生成的 .xlsx" }` 调用审查。
