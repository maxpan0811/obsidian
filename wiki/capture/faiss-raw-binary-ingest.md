---
title: faiss-raw-binary-ingest
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 变更（2026-07-18）

wiki_faiss_build.py 扩展支持 RAW 目录下二进制文档的全文索引：

| 格式 | 提取库 | fallback |
|------|--------|----------|
| PDF | PyMuPDF (fitz) | — |
| Excel .xlsx | openpyxl | xlrd(旧格式) → msoffcrypto(加密空密码) |
| Excel .xls | xlrd | — |
| Word .docx | python-docx | — |
| Word .doc | textutil (macOS) | — |
| PPT .pptx | python-pptx | ZIP XML 直接解析(绕过图片CRC) |
| PPT .ppt/.pps | textutil (macOS) | — |

**关键决策**：
- wiki/sources **退出 FAISS**，只用于 grep 关键词搜索（用户要求）
- FAISS 仅索引 RAW 原始文件全文
- `_ollama_embed` 改为：先清理空白(`\s+` → ` `)，再逐步截断重试（4000→2000→1000 字符）
- checkpoint 每 50 文件保存，防止崩溃丢进度

**最终结果**：2,821/2,984 成功（99.3%），15 个损坏文件不可提取

**踩坑**：
- ❌ 错误示范：`_save_cache` 只在循环结束后调用 → 崩溃丢失全部进度。正确：每 50 个文件存一次 checkpoint
- ❌ 错误示范：15000 字符截断以为够用 → bge-m3 中文 token/字比高达 3-4，8192 token 上限实际只容纳 ~4000 中文字
- ❌ 错误示范：python-pptx 遇图片 CRC 损坏直接崩 → 正确：fallback 到 zipfile 直接解析 slide XML 中的 `<a:t>` 标签
- ✅ Python nohup 后台跑必须用 `PYTHONUNBUFFERED=1` + `python3 -u`，否则日志为空

**How to apply**：新增 RAW 文件后跑 `wiki_faiss_build.py --incremental`，损坏文件会跳过。加密 Excel 用 msoffcrypto 空密码尝试，失败则跳过。

关联: [[20260714-ollama-faiss-v3]], [[faiss-v3-oom-fix]], [[20260716-faiss-400-handling]]
