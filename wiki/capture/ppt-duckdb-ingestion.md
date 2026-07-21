---
title: ppt-duckdb-ingestion
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-21
created: 2026-07-21
---


## PPT 结构化入库 DuckDB

**Why:** 用户需要像 DuckDB 查询 Excel 一样查询 PPT 内容。PPT 比 Excel 复杂（XML+形状+媒体+备注混合体），没有单一工具能通吃，但 python-pptx + DuckDB 组合可以做到结构化查询。

**How to apply:**
- 入库脚本：`~/Documents/artnova/scripts/ingest_pptx.py`
- 虚拟环境：`~/Documents/artnova/.venv`（Python 3.10，含 duckdb + python-pptx + markitdown）
- 数据库：`~/Documents/artnova/duckdb/excel_data.duckdb` 的 `ppt_elements` 表
- 支持增量更新，跳过已入库文件
- python-pptx 不支持的图表类型（如 ofPieChart）记录 error 但不跳过整个文件
- MarkItDown 已安装但入库脚本用 python-pptx（保留位置/类型/备注元数据），MarkItDown 适合快速文本提取但不可 SQL 查询

**入库结果（2026-07-21）：**
- 302/309 成功（97.7%），3 失败（CRC损坏/格式错误/文件缺失），5 空文件
- 18,018 元素：TEXT 15,618 + TABLE 1,177 + CHART 654 + NOTES 569

**关键设计决策：**
- content_source 字段区分 body/table/chart/notes（DeepSeek 建议的 meta 标注）
- 表格存 JSON 格式（可 query 每行每列）
- 图表存 JSON 格式（series + values + categories）
- 位置信息从 EMU 转英寸（除以 914400）
- 单个 shape 出错不跳过整页（try/except 包裹）

**踩坑：**
- python-pptx 不支持 ofPieChart（饼中饼图）→ 需 try/except 包裹 chart.chart_type 访问
- Python 3.14 Homebrew 有 PEP 668 限制 → 用 uv venv 创建虚拟环境解决
- markitdown 输出 Markdown 格式（带 `### Notes:` 前缀），但不提供结构化元数据

**参考：** [[duckdb-multisheet-ingestion]]、[[duckdb-ingest-integration]]
