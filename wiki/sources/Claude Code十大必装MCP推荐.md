---
title: 90%的人都在裸奔Claude Code，10大必装MCP推荐
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=245386...]
source_path: 印象笔记管理工具/90%的人都在裸奔Claude Code，10大必装MCP推荐.html
tags: [claude-code, mcp, tool-recommendation]
---

## 一句话摘要

MCP 是 Claude Code 的扩展系统，装上 MCP 后 AI 从「只能读写文件和对话」变成能操作浏览器、抓网页、连数据库、发飞书消息——**能力边界被完全打开**。

## 十大 MCP 推荐

| # | MCP | 功能 | 一句话场景 |
|:-:|:----|:-----|:----------|
| 1 | **Playwright** | 自动操作浏览器（点按钮、填表单、截图） | 小红书配图截图、自动发布全靠它 |
| 2 | **Desktop Commander** | AI 接管电脑（跑终端命令、管理进程、搜索文件） | 装了它才感觉是「完全体」 |
| 3 | **GitHub** | 操作代码仓库（提PR、查Issue、做Code Review） | 写代码的人迟早要用 |
| 4 | **Context7** | 自动注入技术框架最新文档，让 AI 不过时 | 装之前 AI 经常写过时的 API |
| 5 | **Firecrawl** | 抓取网页内容为干净文本 | 竞品调研、批量采集数据 |
| 6 | **Fetch** | 轻量版网页读取 | 快速看一篇文章、拉 API 返回结果 |
| 7 | **PostgreSQL / SQLite** | 直接操作数据库（查数据、建表、跑 SQL） | 说人话查数据库 |
| 8 | **Sequential Thinking** | 分步思考（Anthropic 官方出品） | 处理复杂任务更靠谱 |
| 9 | **飞书 MCP** | 读写飞书文档、操作多维表格 | 写周报、更新项目进度 |
| 10 | **Excel MCP** | 读写 Excel、写公式、操作工作表 | 丢个表说「按月汇总」它直接改好 |

## 安装方法

```bash
claude mcp add 名称 -- 启动命令
# 示例
claude mcp add playwright -- npx @playwright/mcp@latest
```

一行命令搞定，不用改配置文件。去 [mcp.so](https://mcp.so) 或 GitHub 搜 `awesome-mcp-servers` 可以找到上万个 MCP。

## 核心观点

> 不装 MCP 的 Claude Code 只发挥了三成功力。Claude 本身是大脑，MCP 是手和脚。

## 相关页面

- [[products/Claude Code]]
- [[features/MCP]]
- [[sources/claude-code-best-practice-工作流指南]]
