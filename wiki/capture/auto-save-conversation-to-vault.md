---
title: auto-save-conversation-to-vault
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 会话自动保存到 Obsidian vault 三层架构

## 问题
Claude Code 会话中产生的有价值信息（数据口径、新事实、纠错、工作流偏好）只保存到 memory/（Claude Code 内部记忆），用户 Obsidian vault 里看不到，会话关闭后"蒸发"。compact 和 clear 命令也会导致 pending 记忆丢失。

## 方案：三层兜底

| 层 | 机制 | 作用时机 | 兜底范围 |
|----|------|---------|---------|
| L1 | CLAUDE.md 规则（我双写） | 每次我自动判断到有价值信息时 | 主流程，平时正常运转 |
| L2 | PostToolUse hook | 每次工具调用后自动触发 | compact/clear/崩溃前的最后一次 tool call |
| L3 | Stop hook | 会话正常结束时 | 会话正常关闭的二次确认 |

## 关键决策

| 决策 | Why |
|------|-----|
| 目标目录 `wiki/capture/` 而非 `wiki/cards/` | capture 是自动抓取临时区，经过滤后再迁入 cards。不与人工整理好的卡片混在一起 |
| PostToolUse 作为主力兜底而非 Stop | Stop 在 compact/clear 时不触发；PostToolUse 在每一步工具调用后都跑 |
| 同步脚本 idempotent（同名跳过） | 不重复写入，L2 和 L3 可共存互不冲突 |
| history memory 一次性同步 210 条 | hook 脚本测试时首次运行，后续只同步新条目 |

## 相关文件
- `~/.claude/CLAUDE.md` — 双写规则（第 186-192 行）
- `~/.claude/settings.json` — PostToolUse + Stop hook 注册
- `~/.claude/hooks/sync-memory-to-capture.sh` — hook 脚本
- `/Users/panbo/Obsidian/20260520/wiki/capture/` — 目标目录

**Why:** compact 和 clear 命令不清除 PostToolUse hook，所以即使我（Claude）还没来得及写 wiki/capture/，每次工具调用后的 hook 都会自动补写。三层独立，不依赖我的记忆。

**How to apply:** 新增类似自动保存/同步功能时，优先用 hook 兜底而非仅靠规则约束。hook 不依赖 AI 状态。
