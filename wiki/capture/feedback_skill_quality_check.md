---
title: feedback_skill_quality_check
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


安装新 skill 之前，先做 3 项检查：

1. **description 不为空** — YAML frontmatter 的 description 有实质内容，不是 `|` `>-` 等空壳标记
2. **有实际功能逻辑** — 目录下有脚本（scripts/、main.py 等），不只是纯文档壳
3. **不与已有 skills 重复** — 功能已被现有 skill 覆盖则跳过

**Why:** 之前的 skills audit 发现多个安装的 skill 是空壳（description 为空或只有符号标记），占用了 context budget 但毫无用处。

**How to apply:** 每次用户说"安装这个 skill"或我主动建议安装 skill 时，先 Read SKILL.md 检查上述三项，再决定是否安装。
