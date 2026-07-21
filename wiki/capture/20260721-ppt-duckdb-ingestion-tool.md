---
title: 20260721-ppt-duckdb-ingestion-tool
type: capture
tags: [auto-capture, project, duckdb, ppt, python-pptx, markitdown]
source: Claude Code 会话 2026-07-21
created: 2026-07-21
---

# PPT 结构化入库 DuckDB 工具

## 背景

用户需要一个类似 DuckDB 查询 Excel 的方式来查询 PPT 内容。PPT 比 Excel 复杂（XML + 矢量形状 + 媒体 + 备注/母版的混合体），没有单一工具能通吃。

## 方案选型

| 工具 | 特点 | 适用场景 |
|------|------|---------|
| **MarkItDown** | 微软开源，PPTX→Markdown，三行代码 | 快速文本提取，不可 SQL 查询 |
| **python-pptx** | 结构化提取，保留元数据 | **已采用**，可 SQL 查询 |
| MinerU | VLM+OCR | 图表截图多的学术 PPT |
| Unstructured.io | 20+ 元素类型检测 | 企业级流水线 |

**选择 python-pptx 的原因**：用户需要"DuckDB 式查询"，需要结构化数据而非纯文本。

## 实现

### 表结构

```sql
CREATE TABLE ppt_elements (
    file_path VARCHAR,      -- 源文件路径
    file_name VARCHAR,      -- 文件名
    slide_number INTEGER,   -- 页码
    layout_name VARCHAR,    -- 版式名
    shape_type VARCHAR,     -- TEXT / TABLE / CHART / NOTES
    content_source VARCHAR, -- body / table / chart / notes
    text_content VARCHAR,   -- 文本内容
    table_data VARCHAR,     -- JSON 格式的表格数据
    chart_data VARCHAR,     -- JSON 格式的图表数据
    shape_name VARCHAR,     -- 形状名称
    position_x REAL,        -- X 坐标（英寸）
    position_y REAL,        -- Y 坐标（英寸）
    element_index INTEGER   -- 页内元素序号
);
```

### 入库脚本

`~/Documents/artnova/scripts/ingest_pptx.py`

关键设计：
- 支持增量更新（跳过已入库文件）
- python-pptx 不支持的图表类型记录 error 但不跳过整个文件
- 单个 shape 出错不跳过整页（try/except 包裹）
- 表格存 JSON 格式（可查询每行每列）
- 图表存 JSON 格式（series + values + categories）
- content_source 字段区分 body/table/chart/notes

### 入库结果（2026-07-21）

| 指标 | 数值 |
|------|------|
| 扫描文件 | 309 |
| 成功入库 | 302 (97.7%) |
| 失败 | 3 (CRC损坏/格式错误/文件缺失) |
| 空文件 | 5 |
| **总元素** | **18,018** |
| 文本 | 15,618 |
| 表格 | 1,177 |
| 图表 | 654 |
| 备注 | 569 |

### MarkItDown vs python-pptx 对比

| 对比 | MarkItDown | python-pptx（已用） |
|------|-----------|-------------------|
| 输出 | Markdown 文本 | 结构化 JSON + 元数据 |
| 可 SQL 查询 | ❌ | ✅ |
| 备注标注 | 有 `### Notes:` 前缀 | content_source='notes' |
| 表格 | Markdown 表格 | JSON 数组（可查行列） |
| 图表 | 不提取 | series + values |
| 位置/版式 | 无 | ✅ |

## 用法

```bash
# 查询 PPT 内容
~/Documents/artnova/.venv/bin/python3 -c "
import duckdb
conn = duckdb.connect('/Users/panbo/Documents/artnova/duckdb/excel_data.duckdb', read_only=True)
# 搜关键词
print(conn.execute(\"\"\"
    SELECT file_name, slide_number, LEFT(text_content, 100)
    FROM ppt_elements WHERE text_content LIKE '%你想搜的%'
\"\"\").fetchall())
"

# 增量入库新 PPT
cd ~/Documents/artnova && .venv/bin/python3 scripts/ingest_pptx.py
```

## 踩坑

1. **python-pptx 不支持 ofPieChart（饼中饼图）**
   - 访问 `chart.chart_type` 时抛 ValueError
   - 解决：整个 chart 提取包 try/except，记录 error 到 chart_data

2. **Python 3.14 Homebrew 有 PEP 668 限制**
   - 无法直接 pip install
   - 解决：用 `uv venv` 创建虚拟环境（Python 3.10）

3. **MarkItDown 输出不可 SQL 查询**
   - 输出 Markdown 格式，适合阅读但无法结构化查询
   - 已安装但入库脚本使用 python-pptx

## 相关文件

- 入库脚本：`~/Documents/artnova/scripts/ingest_pptx.py`
- 虚拟环境：`~/Documents/artnova/.venv`（Python 3.10）
- 数据库：`~/Documents/artnova/duckdb/excel_data.duckdb`
- Skill 更新：`~/.claude/skills/DuckDB数据仓库查询/SKILL.md`

## 关联

- [[duckdb-multisheet-ingestion]] — Excel 多 Sheet 入库方案
- [[duckdb-ingest-integration]] — DuckDB 入库整合进 LLM Wiki
- [[tianjin-xinye-store-analysis]] — 同会话完成的门店产量分析
