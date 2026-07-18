---
title: mubu-obsidian-export
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


2026-07-18 将幕布全部文档（4文件夹+28根文档=137个）批量导出为Markdown，保存到 Obsidian `程序开发/随笔/幕布存档/`，后用户手动移到 `20260520/幕布存档/`。

**Why:** 用户要将幕布笔记迁移到 Obsidian，一次性完成。

**How to apply:**
- 使用了 skillhub 的 `mubu-integration` skill（v1.3.6），通过 API 批量拉取文档
- 使用 `export_markdown()` 将幕布大纲结构转成 Markdown
- 每个文件带 `title` + `source: 幕布` frontmatter
- 文件夹作为子目录保存（`📁 文件夹名/` 前缀）
- 凭据存入 `~/.workbuddy/.env.mubu`

**导出结构：** `~/Obsidian/程序开发/随笔/幕布存档/`
**凭据位置：** `~/.workbuddy/.env.mubu`
