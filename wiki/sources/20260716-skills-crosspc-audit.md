---
name: 20260716-skills-crosspc-audit
type: source
tags: [skill-audit, migration, self-contained, claude-code]
source_path: /Users/panbo/Obsidian/程序开发/20260716-Skills跨PC迁移全量审计与自包含改造.md
---

[摘要] 本文档记录了 Skills 跨 PC 迁移前的全量审计与自包含改造过程。背景：计划将 Mac 上 `~/.claude/skills/` 下约 100 个技能通过坚果云整体拷贝到 PC 版 Claude Code，但部分技能存在跨 skill 依赖（cd 到其他 skill 目录、symlink 指向外部等），直接拷贝到 PC 后无法使用。审计范围包括 `~/.claude/skills/` 和 `~/.codex/skills/`。发现并解决了多个问题：印象笔记文章保存脚本为空且依赖其他 skill 的 cd 路径（拷贝脚本到本地自包含）；印象笔记去重功能被覆盖已删除；evernote-yinxiang-backup 路径错误已删除；pdf-ocr 更新为 baidu-OCR 唯一策略；geo-market-research-tool symlink 转真实目录。清理了 anthropic-skills、huangshu 等来源的第三方非本人维护技能。最终状态：约 95 个技能为真实目录、自包含，可直接整体拷贝。PC 上需单独配置印象笔记 token、百度 OCR key、Playwright。经验：技能应自包含，scripts/ 和 .env 都在自己目录下，不依赖 cd 到其他 skill。原文链接：/Users/panbo/Obsidian/程序开发/20260716-Skills跨PC迁移全量审计与自包含改造.md