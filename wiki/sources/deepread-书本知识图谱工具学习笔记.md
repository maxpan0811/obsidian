---
name: deepread-书本知识图谱工具学习笔记
type: source
tags: [DeepRead, 知识图谱, AI结构化, booktools, Claude-Code]
source_path: /Users/panbo/Obsidian/程序开发/DeepRead-书本知识图谱工具学习笔记.md
---

[摘要]

本文档记录了DeepRead开源项目的学习笔记。DeepRead（GitHub: liujuntao123/DeepRead）是一个用AI将书籍拆解成知识节点的工具，通过双向链接串成可交互的知识网络，可部署为静态网站或导入Obsidian使用。已覆盖26本书（四大名著、百年孤独、资本论三卷等），共1800+知识节点。

技术架构为四步管线：(1)格式转换——BookTools/MinerU将EPUB/PDF转为Markdown；(2)宏观分析——AI Agent（Claude Code）识别全书结构，划分维度，生成任务清单；(3)批量填充——按任务清单逐个生成节点，自动建立双向链接；(4)发布——Obsidian或Quartz部署GitHub Pages。

配套工具库DeepReadTools已发布为npm包`booktools`，核心功能包括封装epub2md做EPUB→Markdown转换、清理引用格式、创建books目录结构、复制.claude/模板。Claude Code Agent工作流使用Architect Agent（通读全书→输出宏观蓝图和todo.md）和Generator Agent（每批10个节点→从原文提取信息→生成结构化Markdown）。每个知识节点为独立Markdown文件，含YAML frontmatter、核心定义、原文引述（1-3条）、展开阐述、关联节点（双向链接）五部分。

关键可迁移设计思路：(1)先规划再填充——宏观分析→任务清单→批量生成；(2)Markdown存储——人类可读可编辑可版本控制；(3)双向链接自动建立；(4)人机分工清晰——AI做提取和结构化，人做校验；(5)每本书自定义维度。对LLM Wiki知识库的启发：自动双向链接可在wiki ingest管线中复用，"先规划再填充"比当前ingest的一锅炖更可控。

原文链接：/Users/panbo/Obsidian/程序开发/DeepRead-书本知识图谱工具学习笔记.md