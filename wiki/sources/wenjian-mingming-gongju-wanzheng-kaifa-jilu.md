---
name: wenjian-mingming-gongju-wanzheng-kaifa-jilu
type: source
tags: [文件命名, 批量重命名, OCR, DeepSeek, 工具开发]
source_path: /Users/panbo/Obsidian/程序开发/文件命名工具_完整开发记录.md
---

[摘要]
文件命名工具从概念到实现的完整开发记录，覆盖15+文档格式，融合文档标题检测、LLM（DeepSeek）和百度OCR三条路径。

方案评估排除了smart-rename（3个macOS致命bug）、ai-renamer（图片为主对表格弱）、gemini_file_renamer（偏文献不覆盖全部格式），最终采用自写Python+LLM方案。

命名规则：时间_人物_事件.ext，标题来源优先级为元数据标题→第一页大标题→LLM概括(DeepSeek)→百度OCR回退。日期格式YYYY年MM月DD日，符号统一为下划线，连续下划线合并，总长度限制25 CJK字符。

核心技术演进：textutil→pandoc（扩展格式支持）、pandoc→pdftotext（PDF读取）、subprocess curl→urllib（沙箱兼容）、Ollama qwen2.5:7b→DeepSeek V4（实测质量更优）、Tesseract→百度OCR（识别质量差且730MB）、pdftoppm→fitz（沙箱稳定性）。

LLM选择：DeepSeek V4在日期提取、内容概括和格式遵从方面均优于本地qwen2.5:7b。前期笔记曾记录qwen质量更好，那是小样本测试结论，大规模实测后反转为DeepSeek更优。

实测覆盖6批文件（.doc/.docx/.pdf），含百度OCR回退的5份扫描件。OCR管线自动触发（pdftotext无法提取有效文本时），渲染PDF第一页为PNG后调用百度OCR accurate_basic接口。

原文链接: /Users/panbo/Obsidian/程序开发/文件命名工具_完整开发记录.md