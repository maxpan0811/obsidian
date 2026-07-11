---
title: DeepRead书本知识图谱工具学习笔记
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 程序开发/DeepRead-书本知识图谱工具学习笔记.md
tags: [DeepRead, 知识图谱, AI结构化, booktools, Claude-Code]
---

DeepRead 是一个开源项目（MIT），用 AI 将书籍拆解成知识节点（人物、事件、概念、地点、组织），通过双向链接串成可交互的知识网络，最终可部署为静态网站或导入 Obsidian 使用。已覆盖 26 本书，共 1800+ 知识节点。

## 四步管线

| 步骤 | 工具 | 说明 |
|------|------|------|
| 格式转换 | BookTools / MinerU | EPUB→Markdown（booktools），PDF→MD（MinerU） |
| 宏观分析 | AI Agent（Claude Code） | 识别全书结构，划分维度，生成任务清单 |
| 批量填充 | AI Agent（Claude Code） | 按清单逐个生成节点，自动建立双向链接 |
| 发布 | Obsidian / Quartz | 本地使用或部署 GitHub Pages |

## 实际可用工具

配套工具库 [DeepReadTools](https://github.com/liujuntao123/DeepReadTools) 已发布为 npm 包 `booktools`：

```bash
npm install -g booktools
booktools    # 交互式 CLI：扫描 epub → 转换 → 整理
```

核心功能：封装 `epub2md` 做转换、清理引用格式、创建 `books/` 目录、复制 `.claude/` 模板。

## Claude Code Agent 工作流

`booktools` 会在输出目录写入 `.claude/` 模板，利用 Claude Code 的 Agent 系统：

| 文件 | 职责 |
|------|------|
| agents/Architect.md | 通读全书 → 宏观蓝图（按人物/事件/概念分类）+ todo.md |
| agents/Generator.md | 每批 10 个节点 → 从原文提取信息 → 结构化 Markdown |
| commands/Initial_construction.md | 启动 Architect |
| commands/node_generation.md | 循环读 todo.md，每批 10 个委派给 Generator |

## 可迁移的设计思路

1. **先规划再填充** — 宏观分析 → 任务清单 → 批量生成，比一锅炖可控
2. **Markdown 存储节点** — 人类可读、可手动编辑、可版本控制
3. **双向链接自动建立** — 生成节点时同步关联，而非事后手动链接
4. **人机分工清晰** — AI 做提取和结构化，人做校验和补充

## 对本知识库的启发

- 自动双向链接可在 wiki ingest 管线中复用
- "先规划再填充"比当前 ingest 的一锅炖更可控
- Query 管线可增加知识图谱视图，不限于文本搜索
