---
title: feedback-command-skill-agent-boundary
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


From claude-code-best-practice analysis — the three extension mechanisms form a hierarchy:

**Skill (preferred default):** Lightweight, runs inline, can be auto-invoked by Claude via description matching. Use for reusable procedures and domain knowledge. Set `context: fork` if isolation is needed. Set `disable-model-invocation: true` to prevent auto-fire.

**Agent (context isolation):** Runs in separate context window. Use when the task will generate lots of intermediate output you don't need in main context. Can preload skills for domain knowledge. Heavier than skill — only use when skill is insufficient.

**Command (user-initiated only):** Never auto-invoked, only via `/xxx`. Use for workflow entry points and orchestration. Good for wrapping multi-step flows that involve agents + skills.

Resolution order when Claude decides which to use: Skill → Agent → (Command never, requires `/`).

**How to apply:** Default to skill. Escalate to agent only when intermediate noise would pollute main context. Write a command only when there's a user-initiated workflow that needs orchestrating.
