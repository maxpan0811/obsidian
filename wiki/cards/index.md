---
title: 知识卡片索引
type: index
created: 2026-06-03
updated: 2026-06-03
tags: [meta, cards]
---

# 知识卡片索引

从 wiki 分析页和来源中提炼的独立可复用知识单元。三类：**Decision**（决策+否决理由）、**Pattern**（可迁移做法）、**Pitfall**（踩坑记录）。

质量标记：`verified` = 人工确认，`unreviewed` = AI 提取待确认。

## 旅行社业务

| 卡片 | 类型 | 状态 |
|------|------|------|
| [[cards/渠道市占率-上航四川华程11pct]] | Pattern | verified |
| [[cards/渠道市占率-贵州海外延安中路攻坚]] | Pattern | verified |
| [[cards/人效-武汉减员增效模式]] | Pattern | verified |
| [[cards/人效-三城打法对比]] | Decision | verified |
| [[cards/经营-汇率利好掩盖真实效率]] | Pitfall | verified |
| [[cards/经营-非携程渠道收客持续下滑]] | Pattern | verified |
| [[cards/携程未询单-四川29pct率偏高]] | Pattern | verified |

## LLM Wiki / 知识管理

| 卡片 | 类型 | 状态 |
|------|------|------|
| [[cards/llm-wiki-否决记录价值]] | Pattern | verified |
| [[cards/llm-wiki-热区冷区分层]] | Decision | verified |
| [[cards/llm-wiki-简单方案阈值]] | Pattern | verified |
- [[cards/ingest-scan-逻辑陷阱]] — Ingest 扫描用全量比对不是 -newer 时间戳
- [[cards/filesystem-case-insensitive-陷阱]] — macOS APFS 大小写不敏感导致 duplicate entries
- [[cards/stale-cleanup-bare-directory-陷阱]] — 目录路径本身 os.path.exists 返回 True 导致漏检
