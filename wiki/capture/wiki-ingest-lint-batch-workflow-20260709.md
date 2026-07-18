---
title: wiki-ingest-lint-batch-workflow-20260709
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 2026-07-09 全量 Ingest 会话记录

## 做了的事
1. **vault 迁移**: iCloud → `/Users/panbo/Obsidian/20260520/`，更新 SKILL.md + cleanup 脚本路径
2. **Lint + 索引瘦身**: cleanup_ingested_index.py 移除 16,913 条 stale 条目（35,106 → 18,193）
3. **清理孤儿源页**: 删除 2,252 篇 source_path 指向已删文件的源页 + 367 篇无 source_path 源页（24,249 → 21,630）
4. **知乎 40 篇 Ingest**: 首次批量 wiki source 页创建 + 向量索引
5. **印象笔记 1,000 篇 Ingest**: 批量方式，其中 791 篇成功向量索引（shell展开问题），185 篇含特殊字符后用 subprocess 补索引
6. **ChromaDB 现状**: 全量重建未完成（原 HNSW compaction 失败后一直被清空未重建），目前只重建了约 1,800/22K chunks

## 重要教训
- 文件名含 `#` / `@` / 空格时，shell 展开会破坏参数 → 用 Python subprocess list 传参
- `ingested_files.json` 基于 YAML 的 `source_path` 重建，不适合手动编辑
- `_pending` 目录不一定是笔记文件，注意过滤非 .md 文件
- ChromaDB HNSW compaction 失败后全库重建是已知缺口，需要另找时间全量跑

## 下一步建议
- ChromaDB 全量重建：对整个 wiki/sources 跑 wiki_vector_ingest.py（~22K 篇，约 12h）
- 可以在空闲时后台执行
