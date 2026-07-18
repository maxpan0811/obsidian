---
title: obsidian-output-markdown
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


所有写入 Obsidian 笔记目录的内容统一使用 **Markdown 格式**，而非 HTML。

**原因：** iOS 上的 .html 文件无法直接阅读，Markdown 在所有设备（特别是 iOS Obsidian 客户端）上均可正常打开。

**影响的管线：**

| 管线 | 脚本 | 变更 |
|------|------|------|
| 知乎管理工具 | `fetch_batch.py` | `--format md` 改为默认值 |
| 微信读书管理工具 | `gen_weread_html.py` | `--format md` 改为默认值 |

**How to apply:**
- 知乎新增文章 → 默认输出 `.md`，也可指定 `--format html`
- 微信读书划线摘录 → 默认输出 `.md`，也可指定 `--format html` 用精美排版
- 已有的 HTML 文件**不动**，新文件一律用 Markdown

**Why:**
用户明确说"以后统一用 Markdown"。iOS 无法阅读 HTML 是根本原因。旧的 HTML 文件不动（已保存），新导出的全用 Markdown。
