---
name: excel结构化数据库方案-duckdb
type: source
tags: [DuckDB, FAISS, 数据库, Excel, 架构设计]
source_path: /Users/panbo/Obsidian/程序开发/Excel结构化数据库方案-DuckDB.md
---

[摘要]

本文档记录了Excel结构化数据库方案——DuckDB双轨架构的完整设计。背景是694个Excel文件（410MB）散落在多个目录，向量检索（FAISS）无法处理数值聚合/筛选类查询。选型对比DuckDB、SQLite和PostgreSQL后，确定DuckDB是唯一正确答案——原生读Excel（read_xlsx()零导入）、向量化分析性能（百万行秒级）、单文件零运维。

核心设计为**双轨架构**：轨1 FAISS继续管非结构化文本（公众号文章、会议纪要、竞对新闻、wiki页），轨2 DuckDB管理所有结构化Excel数据。Agent（DeepSeek V4）收到问题后判断要精确数还是解读，路由到对应轨道，最终综合解读。FAISS新增schema_catalog.md的嵌入索引，让Agent知道有哪些表和字段。

数据分层为T1活跃数据（artnova/ 72文件222MB + Desktop/指标制定/ 13文件91MB，schema_catalog收录+DuckDB直查）、T2归档数据（RAW/Excel/ 549文件111MB，按需收录）、T3低频数据（暂不收录）。schema_catalog.md放Obsidian vault raw/下，被FAISS索引。Phase 1-4全部完成：基础设施安装、数据摸底（83文件/461sheets/65.6万行）、3个demo查询跑通、FAISS索引schema_catalog.md（2,828向量，语义搜排名第一）。

记录了6个Excel读取陷阱（混合类型列必须加all_varchar=true、合并单元格、多级表头、空行、日期格式、中文列名）和性能边界。建立了retailer-analysis-dual-view原则（先看全平台总量了解客户全貌，再看华程份额）。2026-07-21完成583个文件批量入库，生成409张表，数据库约100MB。

原文链接：/Users/panbo/Obsidian/程序开发/Excel结构化数据库方案-DuckDB.md