---
title: reference-getnote-mcp
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Get笔记 MCP (@getnote/mcp)

## 安装
- `npm install -g @getnote/mcp` — v1.5.0，106 packages
- 配置文件：`~/.mcp.json` 的 `mcpServers.getnote` 字段

## 配置内容
```json
"getnote": {
  "command": "getnote-mcp",
  "env": {
    "GETNOTE_API_KEY": "gk_live_...",
    "GETNOTE_CLIENT_ID": "cli_..."
  }
}
```

## 功能
通过 MCP 协议在 Claude Code 中直接操作 Get笔记：
- 保存笔记（文本/链接/图片）
- 搜索笔记（语义搜索）
- 管理知识库和标签

## 凭证来源
- Get笔记开放平台：https://www.biji.com/openapi
- 需创建应用获取 API Key（`gk_live_` 开头）和 Client ID（`cli_` 开头）

## 相关 skill
- `~/.claude/skills/getnote/` 下有同名的 OpenClaw skill（SKILL.md），也可用于 API 调用
