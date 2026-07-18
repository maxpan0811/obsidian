---
title: 20260717-icloud-path-cleanup
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Obsidian vault iCloud 旧路径清理

**问题：** Obsidian vault 已从 iCloud 路径 (`/Users/panbo/Library/Mobile Documents/iCloud~md~obsidian/Documents/20260520/`) 移到本地路径 (`/Users/panbo/Obsidian/20260520/`)，但 11 个 skill 脚本仍硬编码旧 iCloud 路径，每次运行都会在 iCloud 目录下重建 vault 结构。

**修复范围：**

| Skill | 文件数 | 说明 |
|-------|--------|------|
| 印象笔记管理工具 | 7 个脚本 + SKILL.md | `OUTPUT_DIR` 改到 `/Users/panbo/Obsidian/20260520/印象笔记管理工具` |
| 知乎管理工具 | 3 个脚本 | `OBSIDIAN_DIR` 改到 `/Users/panbo/Obsidian/20260520/知乎管理工具` |
| LLM-Wiki管理工具 | 1 个脚本 | `obsidian_root` 改到 `/Users/panbo/Obsidian/20260520` |
| 知识库管理工具 | SKILL.md | 文档基础路径改到 `/Users/panbo/Obsidian/20260520` |
| 每日选股分析 | SKILL.md | 报告复制路径改到 `/Users/panbo/Obsidian/20260520/股票分析` |

**残留清理：** iCloud vault 目录（含 87 个文件）已移入废纸篓。

**Why：** vault 迁移时只改了 Obsidian 配置，没排查所有 skill 脚本中的硬编码路径。AI 对写路径的引用缺乏全局意识，需要主动 grep 发现。

**How to apply：** vault 路径迁移后，必须全局 grep `iCloud.*md~obsidian` 检查所有 .claude/skills/ 下的 .py/.sh/.md 文件。

**相关：** [[20260716-skills-quote-dir-cleanup]]（skills 目录脏数据清理——iCloud 路径镜像）
