---
name: 20260717-sources-fulltext-dedup
type: source
tags: [llm-wiki, faiss, dedup, vector-store, sources]
source_path: /Users/panbo/Obsidian/程序开发/20260717-sources-fulltext-dedup.md
---

[摘要] 本文档记录了 LLM Wiki sources/ 全文副本清理和 FAISS 二重索引修复。问题：Obsidian vault 的 wiki/sources/ 目录存了 52,123 篇印象笔记全文副本（784MB），而非按设计应有的摘要。同时 FAISS 向量扫描走整个 vault（含 wiki/sources/），导致同一篇文章从 vault 原文和 sources/ 各索引一次，产生重复命中。修复方案（用户选择）：sources/ 改为摘要（规则提取），FAISS 索引范围排除 sources/。执行步骤：写 compress_sources.py 规则提取脚本（有速读摘要段则保留，无则取首 500 字），52,123 篇压缩耗时仅 0.2 分钟，磁盘从 784MB 降至 56.5MB（-93%）。FAISS 黑名单加 wiki/sources/，从 cache 删除全部 sources/ 条目，重建索引（cache 条目从 100,035 降至 47,912，chunks 从 563,104 降至 210,430）。更新 ingest 流程 CLAUDE.md 明确不要复制全文到 sources/。更新前约 20% 的印象笔记文章自带速读摘要/智能摘要段，优先利用。原文链接：/Users/panbo/Obsidian/程序开发/20260717-sources-fulltext-dedup.md