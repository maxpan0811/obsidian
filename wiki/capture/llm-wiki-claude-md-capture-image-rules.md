---
title: llm-wiki-claude-md-capture-image-rules
type: capture
tags:
  - auto-capture
  - llm-wiki
  - claude-md
  - capture-rules
  - image-handling
source: "Claude Code 会话 2026-07-20"
created: 2026-07-20
---

LLM Wiki CLAUDE.md (`/Users/panbo/Obsidian/20260520/wiki/CLAUDE.md`) 新增「Capture 双写规则」章节，位置在「约定」之后。

**内容要点**：
- memory/ 和 wiki/capture/ 同步写入规则
- **图片处理 4 条注意事项**：
  1. 图片必须保存到本地（`wiki/products/<主题>-screenshots/` 或 `RAW/PIC/`）
  2. 笔记中写图片位置说明
  3. 禁止尝试的 3 种失败方式（Markdown URL / Base64 / 图床）
  4. Capture 内容可用相对路径引用图片（Obsidian 可渲染）

**Why**：从 NeXTSTEP 图片嵌入任务中沉淀的经验——外部图片 API 全部失败，本地保存是唯一可靠方案。需要把这个规则固化到 wiki 操作手册里，以后所有会话自动遵守。

**How to apply**：以后任何涉及图片的 capture 双写场景，按这个规则执行。LLM Wiki 的 CLAUDE.md 是每次会话开始必读文件，规则会自动生效。

[[evernote-image-embedding-workaround]] — 印象笔记图片嵌入限制（上游经验来源）
