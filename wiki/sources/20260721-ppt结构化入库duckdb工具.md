---
name: 20260721-ppt结构化入库duckdb工具
type: source
tags: [DuckDB, PPT, python-pptx, 入库工具]
source_path: /Users/panbo/Obsidian/程序开发/20260721-PPT结构化入库DuckDB工具.md
---

[摘要]

本文档记录了2026年7月21日实现PPT结构化入库DuckDB的工具开发过程。需求类似DuckDB查询Excel的方式查询PPT内容，但PPT比Excel复杂（XML+矢量形状+媒体+备注/母版的混合体）。

方案选型对比了MarkItDown、python-pptx、MinerU和Unstructured.io。最终选择python-pptx，因为用户需要"DuckDB式查询"——需要结构化数据而非纯文本。表结构设计包含file_path、file_name、slide_number、layout_name、shape_type（TEXT/TABLE/CHART/NOTES）、content_source（body/table/chart/notes）、text_content、table_data（JSON格式）、chart_data（JSON格式）等字段。

入库脚本 `ingest_pptx.py` 关键设计包括：支持增量更新、不支持图表类型记录error不跳过整个文件、单个shape出错不跳过整页（try/except包裹）、表格存JSON格式、图表存JSON格式（series+values+categories）、content_source字段区分来源。入库结果：扫描309个文件，成功302个（97.7%），总元素18,018个（文本15,618+表格1,177+图表654+备注569）。全文搜索、表格提取、备注搜索、跨PPT搜索均在毫秒级。

通过DuckDB查询发现4组共15个重复文件（UUID系列×5个、任霞系列×3个等），已移到PPT_Temp目录待确认。踩坑记录包括python-pptx不支持ofPieChart（饼中饼图）、Python 3.14的PEP 668限制需用uv venv创建虚拟环境（Python 3.10）。

数据库位置：`/Users/panbo/Documents/artnova/duckdb/excel_data.duckdb`，入库脚本：`~/Documents/artnova/scripts/ingest_pptx.py`。

原文链接：/Users/panbo/Obsidian/程序开发/20260721-PPT结构化入库DuckDB工具.md