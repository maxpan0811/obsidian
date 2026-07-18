---
title: weread-html-generator
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 微信读书 HTML 生成器

脚本路径：`/Users/panbo/.claude/skills/微信读书管理工具/scripts/gen_weread_html.py`

## 功能

- 解析微信读书导出的 Markdown 文件（`## 划线` / `## 想法` 格式）
- 按章节分色显示每条高亮
- 显示位置引用（`位置 XXXX`，从 `range` 字段提取起始值）
- 内嵌封面图（base64，不依赖外部 CDN）
- `--cover` 参数支持本地文件或 HTTP URL

## 解析注意事项

- WeRead 导出格式为：`<!-- time: X -->\n...\n<!-- range: X -->\n\n> content`（comments 在 `>` 之前）
- `_parse_highlights` 使用 `r'<!-- time: (.+?) -->\n.*?<!-- range: (.+?) -->\n\n> (.+?)(?:\n|$)'` 匹配
- `## 想法` 中 review 可能有 paired（摘录+想法）或 standalone（仅想法）两种格式

## 关键 bug 修复（2026-05-21）

旧版 regex `r'> (.+?)\n<!-- time: (.+?) -->\n.*?<!-- range: (.+?) -->'`（comments 在 `>` 之后）会静默漏掉每章最后一条高亮，且时间/位置配对错位。

## 样式

- 暗色 book-header + 封面左置
- 每章节轮换 6 种柔和色系（蓝/紫/橙/绿/粉/金）
- 章节标题文字随色，带数字徽章
- 卡片左 4px 彩色边框，hover 右移动效
- 「位置 XXXX」彩色药丸徽章在 card header 右侧
