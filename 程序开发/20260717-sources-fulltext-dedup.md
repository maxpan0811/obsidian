---
task_id: "TASK-20260717-001"
title: "LLM Wiki sources/ 全文副本清理 + FAISS 二重索引修复"
date: 2026-07-17
status: 完成
tags: [LLM-Wiki, FAISS, sources, 向量库, dedup]
type: task
---

## 背景

Obsidian vault (`~/Obsidian/20260520/`) 的 LLM Wiki 知识库中，`wiki/sources/` 目录存了 52,123 篇印象笔记全文副本（784MB），而非按设计应有的摘要。同时 FAISS 向量扫描走整个 vault（包括 `wiki/sources/`），导致同一篇文章从 vault 原文和 sources/ 各索引一次，产生重复命中。

## 发现过程

用户发现 `wiki/sources/` 有 52,000+ 篇，而整个 vault 原文才 ~47,000 篇，提出疑问："为什么 Sources 比原文还大？"

经检查发现：
- `印象笔记管理工具/` 目录：47,484 篇原文（印象笔记导出 via 印象笔记管理工具管线）
- `wiki/sources/` 目录：52,123 篇（实际略多，因为有些 sources/ 文件是独立知识页）
- FAISS 的 `_scan_source_files()` 走整个 vault，sources/ 不在 `VAULT_SKIP_DIRS` 中
- 用户理解正确：FAISS 本来就能扫描 vault 原文，sources/ 的全文副本是多余的

## 修复方案（方案 A — 用户选择）

| 组件 | 改前 | 改后 |
|------|------|------|
| `wiki/sources/` | 全文副本 | 摘要（规则提取，200-500字） |
| FAISS 索引范围 | vault 全部（含 sources/） | vault 原文（排除 sources/） |
| 知识页（cards/concepts 等） | 保留在 FAISS | 保留在 FAISS |

## 执行步骤

### 步骤 1：sources/ 全文→摘要压缩

写 `compress_sources.py` 规则提取脚本：
- 有"速读摘要/智能摘要"段（~20% 文件）→ 保留该段
- 无现成摘要 → 取正文首 500 字（跳过 YAML/标题/原文链接）
- 始终附带 `原文链接` 和 `[摘要]` 标记

结果：
- 52,123 篇压缩耗时：**0.2 分钟**
- 磁盘：784MB → **56.5MB**（-93%）
- 平均大小：15KB → 1.1KB

### 步骤 2：FAISS 黑名单 + 缓存清理

- `wiki_faiss_build.py` 的 `VAULT_SKIP_DIRS` 加 `"wiki/sources"`
- 从 FAISS cache 删除全部 52,123 条 sources/ 条目
- 从 metadata 删除 352,674 个 sources/ chunks
- 清理旧备份（~4.5GB → 废纸篓）

### 步骤 3：FAISS 重建

`--rebuild` 从清理后的 cache 重建索引：
- Cache 条目：100,035 → **47,912**
- Index chunks：563,104 → **210,430**
- 一致性验证：✅ index = metadata

### 步骤 4：更新 ingest 流程

修改了 2 个 CLAUDE.md 文件，在 Ingest 步骤中明确：
1. **不要复制全文到 sources/**
2. 优先取已有"速读摘要/智能摘要"段
3. 无则用 LLM 压缩为 200-600 字摘要
4. 附带原文链接和 `[摘要]` 标记

## 改动的文件清单

| 文件 | 改动 |
|------|------|
| `wiki/scripts/compress_sources.py` | **新增** — 规则摘要提取脚本 |
| `wiki/sources/ 下 52,123 篇` | **重写** — 全文→摘要 |
| `.claude/skills/LLM-Wiki管理工具/scripts/wiki_faiss_build.py` | **修改** — VAULT_SKIP_DIRS + "wiki/sources" |
| `.claude/skills/llm-wiki-karpathy/CLAUDE.md` | **修改** — Ingest 流程加摘要提取规则 |
| `wiki/CLAUDE.md` | **修改** — 同上中文版 |
| `wiki/vector_store/` | **清理** — cache 去重 + 索引重建 + 旧备份移除 |

## 最终架构

| 组件 | 内容 | 用途 |
|------|------|------|
| `印象笔记管理工具/`（47k 篇） | 全文 | **FAISS 向量搜索**（全文检索引擎） |
| `wiki/sources/`（52k 篇） | 摘要 | **纯关键词搜索**（快速定位） |
| `wiki/cards/concepts/...`（82 篇） | 结构化知识 | **FAISS 向量搜索**（知识查询） |

## 经验总结

1. vault 原文已在 FAISS 扫描范围内，sources/ 不应存全文副本
2. 规则提取摘要比 LLM 压缩快 1000×（52K 篇 0.2 分钟 vs 可能几小时）
3. 约 20% 的印象笔记文章自带"速读摘要/智能摘要"段，优先利用
4. Ingest 流程是全文复制的根因——改了 CLAUDE.md 堵住源头
5. 删除前必须先确认 FAISS cache 里还有干净的来源数据，否则重建代价巨大

## 相关链接

- [FAISS v3 OOM 修复](faiss-v3-oom-fix.md)
- [FAISS Ollama 400 处理](faiss-400-handling.md)
- [LLM Wiki Schema](https://github.com/karpathy/LLM-Wiki)