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

配套工具库 [DeepReadTools](https://github.com/liujuntao123/DeepReadTools) 已发布为 npm 包 `bookto

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->