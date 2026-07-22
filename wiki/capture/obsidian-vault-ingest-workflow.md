---
title: obsidian-vault-ingest-workflow
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-22
created: 2026-07-22
---


## 2026-07-22 Obsidian vault 4目录批量 Ingest

**背景**：将 Obsidian vault 内 4 个目录（程序开发 54 篇、幕布存档 27 篇、随笔 4 篇、股票分析 1 篇）纳入 LLM Wiki ingest 范围，共计 86 个新源文件。

**执行方式**：Claude Code Workflow，9 个并行 agent，68 万 tokens，16 分钟完成。

**结果**：
- sources 净增 86 页（54396 → 54482）
- overview/index/glossary/log 全部更新
- glossary 新增 5 词（PRODUCT_MAP/众信制造/四大联盟/NeXTSTEP/cdp-browser）

**系统序列号**：`wf_b745ebfe-aa1`（Workflow run ID）

**相关文件**：
- `wiki/CLAUDE.md` — RAW 目录新增「Obsidian 知识库笔记（只读）」子节
- `LLM-Wiki管理工具/SKILL.md` — 热区/RAW 目录更新

**Why**：之前 ingest 只覆盖 RAW/ + 3 个管线目录，Obsidian vault 内大量的个人知识沉淀被忽略。程序开发（技术复盘）、幕布存档（会议记录）、随笔（行业观察）都是高价值知识源。

**How to apply**：后续每次 ingest 时，自动扫描这 4 个目录作为一个来源分组（"Obsidian 知识库笔记"），与 RAW/ 和管线目录同等对待。

[[obsidian-ingest-scope-extension]] — 本操作的上一环节（CLAUDE.md 修改）
