---
title: duckdb-multisheet-ingestion
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-21
created: 2026-07-21
---


# DuckDB 多 Sheet Excel 入库方案

## 背景

DuckDB 的 `read_xlsx()` 函数有以下限制：
1. 默认只读取第一个 sheet
2. 对某些格式（标题行+空行+数据行的复杂结构）返回空数据
3. 无法自动检测和遍历所有 sheet

## 解决方案

使用 Python 脚本 `ingest_excel_multisheet.py`，实现双重读取机制：

### 核心逻辑

```python
for sheet_name in sheet_names:
    try:
        # 1. 优先使用 DuckDB 读取（性能快）
        conn.execute(f"""
            CREATE OR REPLACE TABLE "{table_name}" AS
            SELECT * FROM read_xlsx('{file_path}', sheet='{sheet_name}', all_varchar=true)
        """)
        
        # 2. 检查是否为空
        row_count = conn.execute(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
        
        # 3. 如果为空，fallback 到 openpyxl
        if row_count == 0:
            data_rows = read_sheet_with_openpyxl(file_path, sheet_name)
            if data_rows:
                ingest_sheet_with_openpyxl(conn, table_name, data_rows)
    
    except Exception as e:
        # 4. DuckDB 抛异常时，也 fallback 到 openpyxl
        data_rows = read_sheet_with_openpyxl(file_path, sheet_name)
        if data_rows:
            ingest_sheet_with_openpyxl(conn, table_name, data_rows)
```

### 关键特性

1. **自动检测所有 sheet**：使用 `openpyxl` 读取 sheet 列表
2. **每个 sheet 独立建表**：表名格式 `文件名__sheet名`
3. **双重读取机制**：DuckDB 优先，openpyxl 备用
4. **智能过滤**：跳过完全空的 sheet
5. **增量更新**：检查元数据表，跳过已入库文件

## 实际案例

### OTA_欧洲_Q2Q3同比_途牛同程去哪儿.xlsx

该文件有 4 个 sheet：
- `Sheet`（空）- 被跳过
- `Q2_行程开始`（38行）- DuckDB 返回空，openpyxl 成功读取
- `Q3_预订日期同期`（39行）- DuckDB 返回空，openpyxl 成功读取
- `口径说明`（4行）- DuckDB 直接读取成功

### 结果

```
✓ Q2_行程开始: 38 行, 16 列 (openpyxl fallback)
✓ Q3_预订日期同期: 39 行, 16 列 (openpyxl fallback)
✓ 口径说明: 4 行, 1 列 (DuckDB 直接读取)
⏭ Sheet: 空 sheet，跳过
```

## 环境配置

由于 PEP 668 限制系统 Python 安装包，需要在项目目录创建虚拟环境：

```bash
cd /Users/panbo/Documents/artnova/scripts
uv venv --python 3.12
source .venv/bin/activate
uv pip install duckdb openpyxl
```

## 使用方法

```bash
# 激活虚拟环境并运行多 sheet 入库脚本
cd /Users/panbo/Documents/artnova/scripts
source .venv/bin/activate
python3 ingest_excel_multisheet.py
```

## 经验总结

### DuckDB 的适用场景

**适合**：
- 标准 Excel 文件（单 sheet，简单结构）
- 需要快速查询和分析的场景
- 列式存储的 OLAP 查询

**不适合**：
- 多 sheet 文件（需要额外处理）
- 复杂格式（标题行+空行+数据行混合）
- 需要保留 Excel 格式信息的场景

### openpyxl 的优势

1. **兼容性好**：可以处理各种 Excel 格式
2. **灵活性高**：可以逐行读取，处理复杂结构
3. **完整信息**：可以获取 sheet 列表、合并单元格等信息

### 最佳实践

1. **优先 DuckDB**：性能快，适合标准 Excel
2. **备用 openpyxl**：兼容性好，处理复杂情况
3. **逐 sheet 处理**：每个 sheet 独立建表，避免数据混淆
4. **智能过滤**：跳过空 sheet，不记录失败

## 相关文件

- 多 sheet 入库脚本: `/Users/panbo/Documents/artnova/scripts/ingest_excel_multisheet.py`
- 单 sheet 入库脚本: `/Users/panbo/Documents/artnova/scripts/ingest_excel_to_duckdb.sh`
- 虚拟环境: `/Users/panbo/Documents/artnova/scripts/.venv`
- 数据库: `/Users/panbo/Documents/artnova/duckdb/excel_data.duckdb`

## 任务序列号

- 任务日期: 2026-07-21
- 无后台任务ID（直接执行 Python 脚本）
