---
name: 20260721-excel批量入库duckdb实施记录
type: source
tags: [DuckDB, Excel入库, 数据仓库, 数据库]
source_path: /Users/panbo/Obsidian/程序开发/20260721-Excel批量入库DuckDB实施记录.md
---

[摘要]

本文档详细记录了2026年7月21日将RAW/excel和artnova两个目录下所有Excel文件批量入库DuckDB的完整实施过程。由于PEP 668限制系统Python环境安装第三方包，最终使用duckdb CLI工具直接执行SQL，创建了 `ingest_excel_to_duckdb.sh` 脚本。首轮执行结果：583个文件全部成功，生成409个表。

入库脚本功能包括：扫描指定目录下所有.xlsx/.xls文件、使用duckdb CLI的read_xlsx()函数直接读取Excel、文件名自动转换为合法标识符、创建元数据表记录入库状态、支持增量更新。通过DuckDB验证了携程订单数据（102,646行）、欧洲目的地分布、上海门店产量排名等查询。

此后进行了三次升级：(1) 多Sheet入库方案——创建Python版 `ingest_excel_multisheet.py`，使用openpyxl自动检测所有sheet，每个sheet独立建表，DuckDB读取失败时自动fallback到openpyxl。解决OTA文件第一个sheet为空的读取问题。(2) 子目录递归扫描——将-maxdepth 1改为递归扫描，子目录文件加前缀避免同名冲突。途牛子目录7表709行，同程子目录15表2,239行。总计1,658个表和884,533行数据。(3) 整合进LLM Wiki ingest工作流作为第8步（必选），与FAISS形成互补——FAISS做语义搜索，DuckDB做结构化SQL查询。已知问题包括路径大小写重复导致部分文件被入库两次。

最终数据库位置为 `/Users/panbo/Documents/artnova/duckdb/excel_data.duckdb`，核心表包括2024-2026年携程订单明细（每年77列）、华程直采融合订单（61列）、市占率分析数据和联盟门店分析数据。

原文链接：/Users/panbo/Obsidian/程序开发/20260721-Excel批量入库DuckDB实施记录.md