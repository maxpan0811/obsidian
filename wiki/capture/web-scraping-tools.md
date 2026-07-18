---
title: web-scraping-tools
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 网页抓取工具选型

### 核心区别

| 阶段 | 工具 | 职责 |
|------|------|------|
| **抓取**（拿 HTML） | curl / Playwright MCP / fetch-mcp | 拿到原始 HTML，包括 JS 渲染 |
| **提纯**（洗内容） | Defuddle | 把 HTML 中的广告/导航/侧栏/评论去掉，只留正文 |

Defuddle **不是抓网页工具**，是**正文提纯工具**。它不负责"怎么拿到 HTML"，只负责"拿到 HTML 后怎么洗干净"。

### 实操场景

| 场景 | 工具链 | 说明 |
|------|--------|------|
| 静态页（博客/新闻/统计局官网） | fetch + Defuddle（合起来可用 defuddle-fetch MCP） | 最轻量，一步到位 |
| SPA / JS 渲染 / 需登录 | Playwright MCP（先渲染）→ 可选丢 Defuddle 提纯 | 先拿到渲染后 HTML |
| 整站爬取 | Firecrawl | 自带浏览器层+反爬 |

### 已安装
- `defuddle` CLI — `npm i -g defuddle`，用法 `defuddle parse <url> --md`
- `@playwright/mcp` — Claude Code MCP，已注册，浏览器已装
- `fetch-mcp` — `pip install mcp-server-fetch`，已注册

### 避坑
- 不要用 curl + 正则去扒 HTML（之前踩过，结果是碎的）
- defuddle MCP 包装是 `defuddle-fetch-mcp-server`，可替代默认 fetch
- 国内站点兼容性 ~85%，付费墙/复杂论坛可能翻车
