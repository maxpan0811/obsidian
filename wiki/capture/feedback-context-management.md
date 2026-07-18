---
title: feedback-context-management
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**Context rot starts at ~300-400k tokens** on 1M context model, not at the hard limit. Quality degrades before you hit the wall.

**Rewind (double-Esc) over correcting.** Failed attempts + correction messages left in context pollute future quality. Rewind to before the failure and re-prompt with what you learned instead.

**Compact with a hint** (`/compact focus on X`), don't wait for autocompact. Autocompact fires when the model is already at its dumbest (context rot), so it makes worse summarization decisions.

**/clear + write your own brief** for high-stakes next steps. Compact is fine for mid-task momentum, but you lose control over what's preserved.

**Every turn is a branching point.** After Claude finishes, consciously choose among: Continue, Rewind, Compact, Clear, or Subagent. Don't default to Continue.

**Why:** These rules come from Thariq (Anthropic) who built Claude Code's session management. The cost of bad context management compounds with longer sessions.
