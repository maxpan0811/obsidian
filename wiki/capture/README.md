---
title: Capture 目录说明
type: meta
tags: [meta, auto-capture]
---

# Capture 目录

自动抓取区。Claude Code 会话中判定为有价值的信息，
自动存入此处，供 FAISS 索引和 Obsidian 搜索。

## 来源

- Claude Code 会话中的自动记忆双写（主力）
- Stop Hook 安全网补写（兜底）

## 与 wiki 其他目录的关系

| 目录 | 用途 |
|------|------|
| `capture/` | 自动抓取，临时存放，定期整理后可迁入 cards/analyses/concepts |
| `cards/` | 经过整理的原子知识卡片 |
| `analyses/` | 完整的分析报告 |
| `concepts/` | 核心概念解释 |

## 格式规范

```yaml
---
title: 条目名称
type: capture
tags: [auto-capture, 内容分类标签]
source: Claude Code 会话 YYYY-MM-DD
created: YYYY-MM-DD
---
```

## 维护

- capture/ 自动纳入 FAISS 索引（在 wiki/ 下，不在排除列表）
- 定期（每 1-2 周）把有价值条目迁入 cards/analyses/concepts
- 过期/无用条目直接删除（废纸篓）