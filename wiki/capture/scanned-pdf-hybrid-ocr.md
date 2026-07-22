---
title: scanned-pdf-hybrid-ocr
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-22
created: 2026-07-22
---


## 扫描版 PDF 混合 OCR 处理

**Why:** 97 个扫描版 PDF（1920 页）需要 OCR 识别后入库。没有现成工具，需用已有资源（百度 OCR + qwen3-vl）搭建混合方案。

**How to apply:**
- 策略：百度 OCR（免费 1000 次/月）优先，配额用完自动切换到 qwen3-vl
- 脚本：`~/Documents/scanned-pdf-ocr/hybrid_ocr_processor.py`
- 核心类：`HybridOCRProcessor`
  - `hybrid_ocr()` — 先尝试百度 OCR，失败（错误码 17/18）自动降级到 qwen3-vl
  - `classify_pages()` — PyMuPDF 检测文本层
- 保存到印象笔记：`~/Documents/scanned-pdf-ocr/save_to_evernote.py`
  - 笔记在"工作篮"，标签 `OCR扫描, PDF识别`
  - 必须用 Markdown 格式，直接 Python 调用 curl API（shell 传参丢失换行符）

**测试结果（10 个文件）：**
- 173 页，耗时 3.5 分钟（50 页/分钟）
- 百度 OCR 覆盖率 100%，qwen3-vl 兜底 0 次
- 印象笔记保存 10 篇全部成功

**DeepSeek 评审补丁：**
- ✅ 提示词工程（结构化 + 负面约束）
- ✅ 断点续传（文件级完成标记）
- ⏳ DuckDB 块级表升级（含 bbox/type/confidence）— 待实施

**参考：** [[pdf-ingest-duckdb]]、[[evernote-yinxiang-skill-upgrade]]
