---
title: evernote-image-embedding-workaround
type: capture
tags:
  - auto-capture
  - evernote
  - api-limitation
  - image-embedding
source: "Claude Code 会话 2026-07-20"
created: 2026-07-20
---

印象笔记 createNoteFromMCP / updateNoteFromMCP **不支持嵌入图片**，3 种方式全部失败：

1. ❌ Markdown 图片语法 `![alt](url)` — API 接收成功但不下载，resources=0
2. ❌ Base64 data URI — 内容超 ~10KB 后被静默截断，只剩标题
3.  图床上传（tmpfiles.org / catbox.moe）— 全部超时

**正确流程：**
1. 图片下载到本地（Obsidian vault 或任意文件夹）
2. 笔记内容里写"图片已保存到 XX 路径"
3. 用户手动把图片拖进印象笔记

**Why：** 印象笔记的图片需要走单独的 Resource Upload API，MCP 技能只暴露了笔记 CRUD，没有资源上传接口。

**How to apply：** 以后所有往印象笔记存图片的场景，走这个流程，不要浪费时间尝试 API 嵌入。相关截图已存到 `wiki/products/nextstep-screenshots/`。

[[evernote-dedup-before-save]] — 保存印象笔记前先搜索去重
[[evernote-yinxiang-skill-upgrade]] — 印象笔记 Skill 升级历史
