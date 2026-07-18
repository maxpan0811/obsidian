---
title: user_answer_priority_wiki_first
type: capture
tags: [auto-capture, user]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 回答优先级规则

用户明确要求，以后回答问题按此优先级：

## 优先级

1. **先查 wiki**：
   - 子目录：sources/（源文档）、features/（产品功能）、products/（产品概况）、personas/（用户画像）、concepts/（核心概念）、analyses/（分析）、cards/（知识卡片）
2. **wiki 没有再上网搜索**：使用 Tavily（通过 `search_client.py tavily --query "..."`），需要 `AISA_API_KEY` 环境变量
3. **保存最佳资料到 wiki**：挑数据最完整/权威的源，写入 `wiki/sources/` 目录

## 执行约束

- Tavily 搜索需要 `require_escalated` 权限（网络访问）
- 搜索前先确认 `AISA_API_KEY` 已配置，否则走备选方案（curl + GitHub API / CDP browser）
- 保存到 wiki 前检查是否已有相同/similar 条目

## Tavily API 配置

Key 状态：已配置（tvly-dev-...）
API 端点：`POST https://api.tavily.com/search`

使用方式（curl）：
```bash
curl -s "https://api.tavily.com/search" -H "Content-Type: application/json" -d   '{"api_key":"tvly-dev-xxx","query":"...","search_depth":"basic","max_results":5}'
```

返回字段：results[] 含 url/title/content/score，content 是结构化文本。
搜索深度 basic 够用，advanced 更深入但慢。
