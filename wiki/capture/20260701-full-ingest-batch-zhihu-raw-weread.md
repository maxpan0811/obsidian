---
title: 20260701-full-ingest-batch-zhihu-raw-weread
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 全量 Ingest 第6批次（RAW+知乎+微信读书 131篇）

## 关键发现

### 1. 附件图片统计陷阱
列出目录时必须排除 `attachments/` 子目录。`find -type f` 会把附件图片都算成"待处理文件"。知乎有 2,494 张附件图，印象笔记 attachments/ 有 32GB。

**正确做法**：只统计顶层 .md 文件 → `[f for f in os.listdir(dir) if f.endswith('.md')]`

### 2. Shell Glob 在 14K+ 文件时失效
`ls "$base"/*.md` 在目录超过 ~4K 文件时返回空。必须用 Python `os.listdir` 或 `ls "$base" | grep '\.md$'`。

### 3. HF_HUB_OFFLINE=1 保障离线向量索引
bge-m3 模型已本地缓存，但 `sentence_transformers` 默认会联网检查更新。在中国网络环境 huggingface.co 不可达时必须：
```bash
HF_HUB_OFFLINE=1 python3 wiki_vector_ingest.py "wiki/sources/xxx.md"
```

### 4. PDF 批量提取
- 可用库：PyMuPDF (fitz) ✅、openpyxl ✅、python-docx ✅、python-pptx ✅
- 不可用：pypdf、pdfminer、PyPDF2、pdfplumber（未安装）
- 62% 的 PDF 成功提取正文文本；扫描件返回空 → 创建元数据页

### 5. 向量索引批量策略
- 分 5 批（每批 ~30 文件）执行
- 脚本本身支持多文件：`wiki_vector_ingest.py <file1> [file2] ...`
- 含空格的文件名需要用 Python subprocess 传参

## 批次数据
```
总计 131 个新源页：知乎 40 + RAW 83 + 微信读书 8
ChromaDB: ~24,418 chunks
wiki/sources/: ~18,006 pages
```
