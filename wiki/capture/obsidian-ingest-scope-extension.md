---
title: obsidian-ingest-scope-extension
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-22
created: 2026-07-22
---


Obsidian vault 内 4 个目录已纳入 LLM Wiki ingest 源目录（2026-07-22）：

| 目录 | 路径 | 文件数 | 类型 |
|------|------|--------|------|
| 程序开发 | `~/Obsidian/程序开发/` | 54 | 技术笔记/项目文档 |
| 随笔 | `~/Obsidian/20260520/随笔/` | 15 | 个人随笔/行业观察 |
| 幕布存档 | `~/Obsidian/20260520/幕布存档/` | 32 | 会议记录/培训笔记 |
| 股票分析 | `~/Obsidian/20260520/股票分析/` | 1 | 股票分析报告 |

**修改文件**：`/Users/panbo/Obsidian/20260520/wiki/CLAUDE.md`
- RAW 目录节新增「Obsidian 知识库笔记（只读）」子节
- Ingest 步骤1：5个来源→9个来源

**Why**：这些目录包含大量有价值的个人知识沉淀（技术复盘、会议记录、行业观察），之前被排除在 ingest 范围外，导致 wiki 无法覆盖这些内容。

**How to apply**：后续每次 ingest 时自动扫描这 4 个目录，与 RAW/ 和管线目录同等对待。FAISS 已覆盖全 vault，无需额外配置。DuckDB 只处理 Excel 文件，不受影响。

[[duckdb-ingest-integration]] — DuckDB 仅处理 Excel，不受此扩展影响
