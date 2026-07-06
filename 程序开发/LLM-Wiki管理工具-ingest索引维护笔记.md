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

## 2026-07-01 第6批次全量ingest（RAW+知乎+微信读书 131篇）

### 背景
五源全量扫描发现 12,947 个"新文件"，但实际新文章仅 131 篇——其余是附件图片（jpg/webp/png/gif）和之前脚本误计。

### 关键发现

**1. 附件图片惯性误计**
列出目录时必须排除 `attachments/` 子目录，否则 find+walk 会把 2,494 张知乎附件图、11,000+ 张印象笔记附件图全部算作"新文件"。
```python
# 正确：只计顶层 .md 文件
files = [f for f in os.listdir(dir) if f.endswith('.md')]
# 而非
files = os.listdir(dir)  # ❌ 会把图片/子目录都算进去
```

**2. `ls "$base"/*.md` 在 14K+ 文件时返回空**
目录文件超过 ~4K 时 shell glob 失效。必须用 Python `os.listdir` 或管道：
```bash
# wrong ❌
ls "/印象笔记管理工具/"*.md | wc -l

# correct ✅
python3 -c "import os; print(len([f for f in os.listdir('dir') if f.endswith('.md')]))"
```

**3. `HF_HUB_OFFLINE=1` 保障离线向量索引**
bge-m3 embedding 模型已本地缓存，但 `sentence_transformers` 默认会联网检查更新。在 huggingface.co 不可达时（如中国网络环境）必须：
```bash
HF_HUB_OFFLINE=1 python3 wiki_vector_ingest.py "wiki/sources/xxx.md"
```

**4. PDF 二进制提取策略**
使用 PyMuPDF（fitz）提取文本；扫描件返回空 → 创建元数据页（标题+分类+来源路径）。62% 的 PDF 成功提取正文。

### 批量处理数据
```
总计 131 个新源页：
  知乎管理工具:   40 篇（军事/历史/中国发展/macOS软件）
  RAW:            83 个（学习资料45 + 商业分析11 + 行业报告8 + 书籍6 + 其他9 + PPT/脚本4）
  微信读书管理工具: 8 篇（GEO实战、何以为父、教育新语、智人之上等）
```

### 向量索引
- 分 5 批（每批 ~30 文件）执行 `wiki_vector_ingest.py`
- 共新增 131 条 chunk（每文件 1 条，短文本未触发 chunk 拆分）
- ChromaDB: ~24,418 chunks

### 本轮涉及文件
- `wiki/sources/` → 131 个新增源页
- `wiki/ingested_files.json` → +131 entries（总计 ~18K）
- `wiki/index.md` → 新增 6 个 sections
- `wiki/log.md` → 追加批次日志
- `wiki/overview.md` → 更新 last_update
- `~/.local/share/codex-memory/` → 经验保存
