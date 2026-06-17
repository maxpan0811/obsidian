---
name: MCP
type: feature
tags: [claude-code, mcp]
---

# MCP（模型上下文协议）

所属产品：[[products/Claude Code|Claude Code]]

## 概述

MCP = Model Context Protocol，一套标准接口让 Claude Code 调用外部工具和数据源。MCP 服务器运行在用户本地电脑上，Claude Code 自动判断何时调用。

## 安装方式

- **推荐**：CC-Switch 桌面工具（图形化管理）
- **CLI**：`claude mcp add <名称> -- <启动命令>`
- 查看已安装：`claude mcp list`
- 删除：`claude mcp remove <名称>`

## 推荐 MCP

### 通用精选（来自社区实测）

| MCP | 用途 | 一句话场景 |
|-----|------|----------|
| **Playwright** | 自动操作浏览器（点按钮、填表单、截图） | 小红书配图截图、自动发布 |
| **Desktop Commander** | 跑终端命令、管理进程、搜索文件 | 觉得「这才是完全体」 |
| **GitHub** | 提PR、查Issue、做Code Review | 代码仓库操作 |
| **Context7** | 自动注入技术框架最新文档 | 装之前AI经常写过时的API |
| **Firecrawl** | 抓取网页内容为干净文本 | 竞品调研、批量采集 |
| **Fetch** | 轻量版网页读取 | 快速看一篇文章、拉API返回 |
| **PostgreSQL / SQLite** | 直接操作数据库 | 说人话查数据库 |
| **Sequential Thinking** | 分步思考（Anthropic官方） | 处理复杂任务更靠谱 |
| **飞书 MCP** | 读写飞书文档、操作多维表格 | 写周报、更新项目进度 |
| **Excel MCP** | 读写Excel、写公式 | 丢个表说「按月汇总」它直接改好 |

### 专业领域

| MCP | 用途 |
|-----|------|
| 企查查类 | 企业信息查询、工商/诉讼/知识产权 |
| 法宝MCP | 案例和法规检索 |
| 高德/百度地图 | 地理信息、侵权门店调查 |
| Arxiv 论文助手 | 论文检索与解读 |
| AntV 可视化图表 | 数据可视化 |

查找更多：ModelScope MCP 广场、阿里云百炼 MCP 广场、[mcp.so](https://mcp.so)、GitHub `awesome-mcp-servers`

### 安装方式

```bash
claude mcp add 名称 -- 启动命令
# 示例
claude mcp add playwright -- npx @playwright/mcp@latest
```

一行命令搞定，不用改配置文件。

## 安全原则

MCP 获取的数据 = 手动粘贴给 Claude Code 的数据。公开信息放心用，客户敏感信息别碰。

## 数据流

用户提问 → Claude Code API → Claude 决定调用 MCP → MCP 服务（本地）获取数据 → 数据返回作为上下文 → Claude 处理回复

来源：[[sources/Claude Code教程-五-MCP]] · [[sources/Claude Code十大必装MCP推荐]]
