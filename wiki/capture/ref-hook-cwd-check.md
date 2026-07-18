---
title: ref-hook-cwd-check
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# hook-cwd-check.py

**创建时间**: 2026-06-15
**位置**: `~/.claude/scripts/hook-cwd-check.py`
**注册**: `settings.json` → `hooks.UserPromptSubmit[2]`

**功能**: 每次用户发消息前检测当前工作目录。当 cwd 是 `.claude/` 目录时，强制注入警告提醒切换到正确项目。正常 cwd 下完全静默退出，不浪费上下文空间。

**Why**: 之前 "确认 cwd 正确再操作" 只是 hook-discipline 中的文本提醒（第4条），没有实际检测逻辑。这个 hook 把提醒升级为工程约束——自动检测、条件触发、静默退出。

**How to apply**: 如果将来有新的异常 cwd 模式需要检测（如特定子目录），直接编辑本脚本的条件列表。不改 settings.json。

**Related**: [[reference-constraints-system-article]], [[config-stack-hooks-rules]]
