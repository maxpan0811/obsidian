---
title: skills-delete-sync-symlinks
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


删除 `.claude/skills/` 下任何 skill 后，openclaw 的 symlink 副本会成为坏链，需要同步清理。

**受影响目录（全部 symlink 指向 `.claude/skills/`）：**
- `~/.openclaw/skills/`
- `~/.openclaw/workspace/peter/skills/`
- `~/.codex/skills/`（2026-06-14 新建，不含 `.system`）

**Why:** 避免 context tax 的量化框架中说"删除不需要的 skills 可释放 context budget"，但若不清理 symlink，坏链不会自动消失，下次启动时仍会被扫描。

**How to apply:** 在 `.claude/skills/` 执行 `rm -rf` 或 `mv` 到 Trash 之后，立即检查并清理三个目录的坏链：
```bash
find ~/.openclaw/skills/ ~/.openclaw/workspace/peter/skills/ ~/.codex/skills/ -maxdepth 1 -type l ! -exec test -e {} \; -delete
```
删除完后用 `ls -1 <dir> | wc -l` 核对数量，确保不会多删或少删。`~/.codex/skills/` 里的 `.system/` 目录不要动。
