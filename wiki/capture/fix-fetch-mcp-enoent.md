---
title: fix-fetch-mcp-enoent
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 问题

`~/.claude/mcp.json` 中配置的 fetch MCP 使用 `@anthropic/fetch-mcp`，该包在 npm 上不存在（404），导致 Claude Code 启动时报 `Failed to reconnect to fetch: ENOENT`。

## 修复

把包名换为 **`@mokei/mcp-fetch`**（v0.7.0，2026-06 活跃维护，轻量，依赖少）。

提供 `get_markdown` 工具 — 输入 URL 返回 Markdown 格式内容。

## 其他可选包

- `fetch-mcp` — egoist 维护，v0.0.5，一年未更新
- `mcp-fetch-server` — v1.1.1，支持 HTML/Markdown/JSON/字幕

## 排查过程

1. 定位 MCP 配置：`~/.claude/mcp.json`（用户级），`~/Project/.mcp.json`（项目级）
2. `npm view @anthropic/fetch-mcp` → 404
3. 多个备选包名（`@modelcontextprotocol/server-fetch`、`@anthropic/mcp-server-fetch`）都 404
4. 从 `npm search` 结果中对比选型，`@mokei/mcp-fetch` 最合适
5. 验证：pipe a JSON-RPC 请求确认工具列表正常返回

**Why:** 包名是拼写错误的旧配置，官方 fetch MCP 可能从未以 `@anthropic/fetch-mcp` 发布过。
**How to apply:** 遇到类似 `Failed to reconnect to <name>: ENOENT` 且 name 在系统工具列表中，先 `npm view <包名>` 确认是否存在。
