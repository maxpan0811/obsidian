---
title: reference-mcp-api
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## API Routing

**Default model route** (`settings.json`):
- `ANTHROPIC_BASE_URL`: `https://api.deepseek.com/anthropic`
- `ANTHROPIC_MODEL`: `DeepSeek-V4-flash`
- `ANTHROPIC_REASONING_MODEL`: `Deepseek-v4-pro`

**Why separate DeepSeek routing paths:**
- Claude Code SDK → `api.deepseek.com/anthropic` (Anthropic-compatible proxy)
- OpenSpace (litellm) → `api.deepseek.com` directly (OpenAI-compatible)
- Never confuse the two. If a tool uses `anthropic` SDK, point it at `/anthropic`. If it uses `openai` SDK, point it at the root.

## MCP Server Config (`~/.claude/mcp.json`)

| Server | When to use | Config note |
|--------|-------------|-------------|
| wechat | Daily communication | Node.js channel |
| context7 | Library docs lookup | npx, needs API key |
| firecrawl | Web scraping/search | npx, needs API key |
| playwright | Browser automation | npx, no API key needed |
| openspace | Skill evolution / complex multi-step tasks | venv under `~/.claude/` |

**When to add a new MCP server:** Only when the task can't be done with existing tools AND recurs at least 3 times.
**When to remove:** If unused for 30 days, remove. Dead config is noise.

## Skills installed (for reference)

18 lark-*, 3 obsidian-*, context7-mcp, defuddle, json-canvas, openspace. These are loaded automatically — no need to manually invoke.
