---
title: LLM-Wiki管理工具 - ingest 索引维护笔记
created: 2026-06-29
tags: [程序开发, llm-wiki, ingest, index-maintenance, lint]
---

## 2026-06-29 Ingest 扫描逻辑修复 + 全量覆盖

### 背景
第一轮 ingest 只检查了 `-newer ingested_files.json` 的文件，遗漏了 1,332 个长期存在但从未入库的文件。

### 修复方案
**全量目录遍历 → 逐一查 ingested_files.json**，禁止使用 `-newer`、mtime 或其他时间戳过滤。

```python
# 错误做法 ❌
find RAW/PDF/ -newer wiki/ingested_files.json

# 正确做法 ✅
for f in RAW/PDF/*.pdf; do
  key="RAW/PDF/$(basename "$f")"
  python3 -c "import json; print('NEW' if '$key' not in json.load(open('wiki/ingested_files.json')) else 'OK')"
done
```

### ingested_files.json 重建
- 从 wiki 源页的 YAML frontmatter 中提取 `source_path`
- 必须使用 `yaml.safe_load()` 而非字符串操作（引号文件名问题）
- 仅保留源文件仍在磁盘上的条目
- 清理结果：20,440 → 4,892 entries（15,548 stale 条目移除）

### 3 个关键陷阱（已归档到 wiki/cards/）

| 陷阱 | 原因 | 修复 |
|------|------|------|
| `-newer` 遗漏旧文件 | 只检查时间戳，忽略从未入库的文件 | 全量比对 |
| macOS 大小写不敏感 | `RAW/md` = `RAW/MD` 同一目录，AI 双倍入库 | lowercase dedup |
| bare-directory 残留 | `RAW/Excel/` 目录路径被 `os.path.exists()` 放过 | `sp.endswith('/')` 检查 |

### 脚本更新
- `scripts/cleanup_ingested_index.py` — 用 `yaml.safe_load` 重建索引，自动去重
- `SKILL.md` — Ingest 扫描逻辑更新 + Lint 工作流步骤 0

### 最终数据
```
ingested_files.json:  4,892 entries（全量可验证）
wiki/sources/:       17,874 pages
ChromaDB:            24,330 chunks
```

### 本轮涉及文件
- `~/.claude/skills/LLM-Wiki管理工具/SKILL.md` — 扫描逻辑 + lint 工作流
- `scripts/cleanup_ingested_index.py` — 重建/清理脚本
- `wiki/sources/` → 1,332 个新增源页
- `wiki/cards/` → 3 张 Pitfall 卡片
- `wiki/ingested_files.json` → 清理重建
- `wiki/log.md` → 操作日志
- `~/.local/share/codex-memory/` → 经验保存
