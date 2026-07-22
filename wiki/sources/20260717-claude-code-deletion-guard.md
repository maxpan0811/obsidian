---
name: 20260717-claude-code-deletion-guard
type: source
tags: [claude-code, security, hooks, deletion-protection]
source_path: /Users/panbo/Obsidian/程序开发/20260717-ClaudeCode三层删除防护搭建.md
---

[摘要] 本文档记录了 Claude Code 三层删除防护的搭建过程。参考 Codex（Starlark prefix_rule）的删除防护方案搭建对等的三层保护。三层结构：模型层（~/.claude/CLAUDE.md 删除铁律，让 Claude 生成代码时自觉用 trash 而非 rm）、工具层（~/.claude/settings.json permissions.deny 硬拦，模型绕不过）、代码层（~/.claude/hooks/block-dangerous.sh PreToolUse hook，补充 deny 匹配不到的绕法）。PreToolUse hook 拦截清单包括：rm -rf/rm/rmdir 等、find -delete/exec rm、git clean -fd/fdx、git checkout --、git restore（--staged 放行）。关键踩坑：两次 jq 调用的 stdin 竞争问题（一次性读完 stdin 解决）、grep \b 不对 -- 匹配（改用空格/行尾替代）。测试 7 种场景全部通过，包括 rm、find、git clean、git checkout、git restore 拦截和 ls 放行。与 Codex 对比：Claude Code 的 deny glob 匹配比 Codex 的逐 flag prefix_rule 简洁得多。原文链接：/Users/panbo/Obsidian/程序开发/20260717-ClaudeCode三层删除防护搭建.md