---
title: deepread-booktools-discovery
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# DeepReadTools (npm: booktools) — 实际可用工具

## 发现

DeepRead 的配套工具库 [DeepReadTools](https://github.com/liujuntao123/DeepReadTools) 已发布为 npm 包 `booktools`。

## 安装与使用

```bash
npm install -g booktools
booktools
```

交互式 CLI：扫描 epub → 转换 → 创建 `books/` 目录 → 复制 `.claude/` 模板。

## 核心机制

`booktools` 最关键的产出不是 EPUB 转换，而是**在输出目录写入 `.claude/` 模板**，利用 Claude Code 的 Agent/Command 系统完成 AI 分析：

- `agents/Architect.md` — 通读全书 → 宏观蓝图 + todo.md
- `agents/Generator.md` — 每批 10 个 → 从原文提取信息 → 结构化 Markdown
- `commands/Initial_construction.md` — 启动 Architect
- `commands/node_generation.md` — 循环处理 todo.md

## 与之前文章说的区别

文章说用 Gemini CLI，但实际 repo 的 AI 工作流走的是 **Claude Code Agent 系统**（`.claude/agents/` + `.claude/commands/`）。

## 可学习的设计

机器部分（booktools）和 AI 部分（Agent 模板）是分离的。booktools 只做格式转换和模板复制，AI 分析逻辑全在 Agent 定义里。这种解耦让用户可以选择不同的 AI 后端。
