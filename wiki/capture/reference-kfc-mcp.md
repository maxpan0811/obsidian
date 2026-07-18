---
title: reference-kfc-mcp
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# KFC MCP (@striderlabs/mcp-kfc)

## 安装位置
- npm 包：`@striderlabs/mcp-kfc` 全局安装
- Playwright：Chromium 浏览器（`npx playwright install chromium`）
- 配置：`~/.mcp.json` 的 `mcpServers.kfc` 字段

## 配置内容
```json
"kfc": {
  "command": "npx",
  "args": ["-y", "@striderlabs/mcp-kfc"]
}
```

## 功能
通过 MCP 协议在 Claude Code 中直接搜索肯德基菜单、加购、下单、查询附近门店等。

## 使用方式
重启 Claude Code 后自动加载。对话中用自然语言即可操作，如"搜索肯德基菜单"、"加一个香辣鸡腿堡"等。

## 注意事项
- 需 Playwright Chromium 浏览器运行（已在 2026-05-26 安装）
- 这是社区版连接器，使用 kfc.com 网页界面
- 与 Claude Desktop 的配置方式不同——Claude Code 用 `.mcp.json`，Claude Desktop 用 `claude_desktop_config.json`
