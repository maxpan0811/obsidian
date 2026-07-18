---
title: openspace
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## Decision rules

**Delegate to OpenSpace when:**
- Task requires tools/capabilities I don't have (e.g., desktop automation, complex shell orchestration)
- I tried and failed — OpenSpace may have a tested skill for it
- Complex multi-step task that benefits from its skill library and auto-evolution
- User explicitly asks to delegate

**Handle directly when:**
- Simple read/write/search — my built-in tools are faster
- Task is one-off and won't benefit from skill capture

**After every OpenSpace call, check for `evolved_skills`.** If `upload_ready: true`, decide:
- Skill originated from cloud → upload back as public
- Generally useful → upload as public
- Project-specific → upload as private, or skip

## Installation path (all under `~/.claude/`)

| Content | Path |
|---------|------|
| venv | `~/.claude/venvs/openspace/` |
| host skills | `~/.claude/skills/openspace/` (delegate-task + skill-discovery) |
| executable | `~/.claude/venvs/openspace/bin/openspace-mcp` |

## LLM config

- Model: `deepseek/deepseek-chat` via `api.deepseek.com` (standard OpenAI API, not the `/anthropic` proxy)
- API key: from `DEEPSEEK_API_KEY` env var (litellm picks it up natively)
- Timeout: 600s — complex tasks may take minutes

## Key env vars

- `OPENSPACE_HOST_SKILL_DIRS`: host skills directory
- `OPENSPACE_WORKSPACE`: workspace (logs, recordings)
- `OPENSPACE_MODEL`: litellm-format model name
- `OPENSPACE_LLM_API_BASE`: OpenAI-compatible API URL

## Uninstall

```bash
rm -rf ~/.claude/venvs/openspace ~/.claude/skills/openspace
# Remove openspace block from ~/.claude/mcp.json
```
