---
title: user-role
type: capture
tags: [auto-capture, user]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


User is an experienced Claude Code user who prioritizes simplicity and pragmatism over tool proliferation.

## Decision rules

**Model routing:** Always route through `api.deepseek.com/anthropic` with `DeepSeek-V4-flash` as the default. The `/anthropic` proxy path preserves Claude API compatibility. For OpenSpace's litellm (which needs standard OpenAI-compatible endpoints), use `api.deepseek.com` directly — two different routing paths for two different SDKs.

**Tool selection:** Minimal MCP count. Only add a tool when it solves a real, recurring pain — not "this looks useful." Current stack: wechat (daily communication), context7 (docs lookup), OpenSpace (skill evolution), firecrawl (web scraping), playwright (browser automation). That's enough.

**Installation boundary:** Third-party tools and dependencies go under `~/.claude/`. Work projects (`/Users/panbo/Project/`) stay separate. Never mix config/tooling with project code.

**Work style:** Ad-hoc conversation first, skill auto-invoke second. No custom commands or agents. When choosing between a new skill and a one-off script, prefer the script.

**Theme:** `light-daltonized` — colorblind-accessible. Don't suggest theme changes.

## Setup snapshot (for debugging, not driving decisions)

- DeepSeek-V4-flash default model, Deepseek-v4-pro for reasoning
- Custom status line: `~/.claude/statusline-command.sh`
- Skills: lark-* (18), obsidian-* (3), context7-mcp, defuddle, json-canvas, openspace
- Rules: `~/.claude/rules/context7.md`
