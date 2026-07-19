---
title: evernote-api-no-image-embed
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-20
created: 2026-07-20
---


印象笔记 createNoteFromMCP / updateNoteFromMCP 接口**不支持嵌入图片**。

**尝试过的方式：**
1. ❌ Markdown 图片语法 `![alt](url)` — API 接收成功但不会下载图片，resources 仍为 0
2. ❌ Base64 data URI — 内容超过 ~10KB 后 API 静默截断，只保留标题
3. ❌ 图床上传（tmpfiles.org / catbox.moe）— 从这个网络全部超时

**正确的做法：**
- 图片保存为本地文件（Obsidian vault 或任意文件夹）
- 笔记里写文字说明 + 图片来源
- 用户手动把图片拖进印象笔记

**为什么：** 印象笔记的图片是通过单独的 Resource Upload API 上传的，MCP 技能只暴露了笔记 CRUD 接口，没有暴露资源上传接口。

**How to apply：** 以后遇到需要往印象笔记存图片的场景，直接保存图片到本地 + 在笔记里写"图片已存到 XX 路径"，不要浪费时间尝试 API 嵌入。
