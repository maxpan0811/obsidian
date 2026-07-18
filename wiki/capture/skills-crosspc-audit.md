---
title: skills-crosspc-audit
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


**范围**：~/.claude/skills/ 下约 100 个技能 + Codex + OpenClaw

**发现并修复的问题**：
1. **印象笔记文章保存** — scripts/ 空目录，原 cd 到印象笔记管理工具。修复：自包含 3 个脚本 + .env，SKILL.md 路径改本地
2. **印象笔记去重** — 同样依赖印象笔记管理工具。修复：**已删除**（文章保存&管理工具已覆盖）
3. **evernote-yinxiang-backup** — 路径写 ~/.qclaw（不存在）。修复：**已删除**（备份不可用）
4. **pdf-ocr** — 默认 tesseract 本地 OCR。修复：改为 baidu-OCR 唯一方式（用户确认弃用 tesseract）
5. **geo-market-research-tool** — symlink→.openclaw。修复：转 ~/.claude/skills/ 真实目录
6. **skills-orange-line / 参考图集管理** — OpenClaw 真实技能。修复：copy 到 claude，OpenClaw 换 symlink
7. **Codex** — 全部 symlink→claude（无需处理）
8. **OpenClaw 第三方技能** — anthropic-skills/huangshu/baoyu/weread/processon → 全部删除

**完整记录**：Obsidian 程序开发/20260716-Skills跨PC迁移全量审计与自包含改造.md

**Why**: 技能依赖外部目录跨机器 copy 会断链，必须自包含才能保证 PC 上立即可用。
**How to apply**: 新建技能时 scripts/ + .env 放自己目录下，不以 `cd` 引用其他 skill。
