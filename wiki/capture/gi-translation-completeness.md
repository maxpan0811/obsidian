---
title: gi-translation-completeness
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Game Informer 翻译全覆盖要求

翻译 Game Informer 标题时，不能依赖模式匹配（如只翻 Review/Preview 前缀）——这样会留下英文尾巴。

**正确做法**：每一条标题的每一个单词都必须翻译成中文。生成后逐条验证 `C` 行是否 100% 中文。

**验证方法**：提取所有 `.item-zh` 的文本，检查是否包含中文字符（`[\u4e00-\u9fff]`）。凡是没有中国字的都要补翻。

**生成脚本注意事项**：
- 生成 HTML 后必须对所有 `.item-zh` 做一轮正则扫描，确认无纯英文残留
- 不能在 HTML 页面里留下任何英文标题残余

Files affected: ~/.claude/skills/news-gameinfomer/SKILL.md
