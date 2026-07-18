---
title: 20260716-skills-quote-dir-cleanup
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 技能目录脏数据清理

**日期**: 2026-07-16
**操作**: 删除 `/Users/panbo/.claude/skills/"` 脏目录

## 背景

在 skills 目录下发现一个名为 `"`（单引号字符）的异常目录，内部嵌套了 `Users/panbo/Library/Mobile Documents/iCloud~md~obsidian/Documents/20260520/程序开发/` 的路径镜像，最深层有一篇笔记文件 `印象笔记同步管线.md`（8.3KB）。

推测成因：某次 shell 命令路径参数中遗留了多余的引号字符，导致创建了意外目录。

## 处理

- 移入废纸篓 `~/.Trash/skills_quote-dir_20260716`
- 验证已清理干净（grep 检查无残留）

**Why**: 脏目录不影响 skills 加载（不匹配 skill 命名规则），但占据了 skills 目录的条目计数，让 `ls` 输出有 1 个无效条目，可能干扰后续技能审计。

**How to apply**: 如果再次遇到类似残留引号的目录，直接移入废纸篓，不需要检查内部文件——没有正常流程会往 `"` 目录写东西。
