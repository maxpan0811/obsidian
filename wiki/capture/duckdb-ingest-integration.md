---
title: duckdb-ingest-integration
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-21
created: 2026-07-21
---


# DuckDB 入库整合进 LLM Wiki Ingest 流程

## 决策

DuckDB 数据入库现在是 LLM Wiki ingest 的**必选步骤**（SKILL.md 第8步），与 FAISS 向量索引并列。

## 完整 ingest 链条

```
文件 → wiki/sources/ → ingested_files.json → FAISS 向量索引 → DuckDB 数据入库（Excel）→ index.md 更新
```

## 脚本更新

`ingest_excel_to_duckdb.sh` 改为：
- 递归扫描 `RAW/Excel/` 所有子目录（删除 `-maxdepth 1`）
- 子目录文件表名加前缀（如 `途牛__xxx`、`同程__xxx`），避免同名冲突
- 路径从 `RAW/excel` 修正为 `RAW/Excel`

## 当前状态（2026-07-21）

| 目录 | 表数 | 行数 |
|------|------|------|
| Excel 根目录 | 920 | 75,230 |
| 途牛子目录 | 7 | 709 |
| 同程子目录 | 15 | 2,239 |
| artnova | 1,251 | 884,533 |

## 已知问题

路径大小写变更（`RAW/excel` → `RAW/Excel`）导致旧记录不匹配，产生了重复入库。后续需清理旧路径记录。

## Why

DuckDB 是结构化数据查询层（SQL聚合/分组/JOIN），FAISS 是语义搜索层（全文/关键词）。两者互补，Excel 文件 ingest 时缺一不可。

## How to apply

每次 ingest 新的 Excel 文件时，确保：
1. 跑 `bash /Users/panbo/Documents/artnova/scripts/ingest_excel_to_duckdb.sh`
2. 检查子目录文件是否入库（查 `_ingestion_metadata` 表）
3. 用 `DuckDB数据仓库查询` skill 做 SQL 分析

相关：[[duckdb-multisheet-ingestion]]、[[duckdb-excel-all-varchar]]
