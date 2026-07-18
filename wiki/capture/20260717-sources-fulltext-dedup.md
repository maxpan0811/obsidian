---
title: 20260717-sources-fulltext-dedup
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# wiki/sources 全文副本修复

2026-07-17 发现 LLM Wiki 的 `wiki/sources/` 目录有 52,123 篇印象笔记全文副本（784MB），而非按设计本应是的摘要。

**根因**：ingest 管线直接把印象笔记导出全文复制进 sources/，未做摘要提取。FAISS 扫描整个 vault（包括 sources/），导致同一篇文章从原文和 sources/ 各索引一次，产生重复命中。

**修复**：
1. `compress_sources.py` 规则提取摘要（先找已有"速读摘要/智能摘要"，无则取首500字），52K篇跑0.2分钟，磁盘 784MB→56.5MB（-93%）
2. `wiki_faiss_build.py` 的 `VAULT_SKIP_DIRS` 加 `"wiki/sources"`，FAISS 不再索引 sources/
3. FAISS cache 清理：100,035→47,912 条目；chunks：563K→210K
4. 旧备份 ~3.5GB 移入废纸篓

**架构变化**：
- `印象笔记管理工具/` → FAISS 向量搜索（全文检索）
- `wiki/sources/` → 仅关键词搜索（摘要，快速定位）
- `wiki/cards/ 等知识页` → FAISS 向量搜索（结构化知识查询）

**Why:** 原文已在 vault 中，sources/ 的全文副本毫无意义。后续新 ingest 应直接生成摘要，不再全文复制。

**How to apply:** (1) 新 ingest 时只写摘要进 sources/；(2) 修改日志记得同步此配置。
