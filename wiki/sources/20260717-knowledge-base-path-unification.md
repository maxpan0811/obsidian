---
name: 20260717-knowledge-base-path-unification
type: source
tags: [knowledge-base, obsidian, skill-md, path, program-dev]
source_path: /Users/panbo/Obsidian/程序开发/20260717-知识库管理工具程序开发路径统一.md
---

[摘要] 本文档记录了知识库管理工具 SKILL.md 中程序开发目录路径统一的过程。背景：用户要求所有程序开发相关笔记统一保存在 `obsidian/程序开发/`（根目录），而非 `obsidian/20260520/程序开发/`（子 vault）。知识库管理工具 SKILL.md 的 base path 设为 Obsidian/20260520/，导致目录结构图把程序开发/归在子目录下，文件引用解析到错误位置。改动 3 处：目录结构图明确程序开发/在 root 层级；基础路径拆分（20260520/ 为管线输出目录，程序开发/ 为 root 层级用绝对路径）；修复 ChromaDB 引用为绝对路径。2026-07-18 发现复发：3 个新文件被写入错误路径。根因分析：大量 skill 使用 20260520/xxx 作为输出路径，模型形成路径惯性。修复措施：加强 memory 规则增加禁止路径反例和对照表；强化 SKILL.md 路径警示框；清理存量文件。原文链接：/Users/panbo/Obsidian/程序开发/20260717-知识库管理工具程序开发路径统一.md