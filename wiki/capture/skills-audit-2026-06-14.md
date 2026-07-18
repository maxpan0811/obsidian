---
title: skills-audit-2026-06-14
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 🟡 需合并的冗余分组（合并后显著减少 skill 数量）

### 分组 1：PDF 处理 → pdf + mineru-pdf 就够了
- **保留**: `pdf`（通用 PDF）+ `mineru-pdf`（重 OCR，保留因为 1.2GB 没必要重复）
- **删**: `pdf-text-extractor`, `pdf-poppler-utils`, `iyeque-pdf-reader`, `document-pro`
- **待定**: `geminipdfocr` — 如果 mineru-pdf 已覆盖 Gemini OCR 可删
- **待定**: `mineru-pdf` — 1.2GB 极大，如果很少触发应删
- **Count**: 7 → **2**

### 分组 2：文档办公 → document-skills bundle（pdf + docx + xlsx + pptx）
- 你理论上已经装了 document-skills 的 pdf/docx/xlsx/pptx
- **删**: `word-docx`, `excel-pro`, `excel-xlsx`, `docx-editing`, `docx-toolkit`, `docx-typo-checker`, `Office`, `Office-Editor`, `Office-mcp`, `document-pro`, `md-to-office`
- **Count**: 16 → **4**

### 分组 3：Lark/飞书 22 个 → 保留常用 8-10 个
- **必须保留**: `lark-im`（IM 消息）, `lark-doc`（云文档）, `lark-sheets`（电子表格）, `lark-base`（多维表格）, `lark-calendar`（日历）, `lark-contact`（通讯录）, `lark-drive`（云空间）, `lark-wiki`（知识库）, `lark-task`（任务）
- **可删**: `lark-event`, `lark-mail`, `lark-minutes`, `lark-openapi-explorer`, `lark-shared`, `lark-skill-maker`, `lark-vc`, `lark-whiteboard`, `lark-workflow-meeting-summary`, `lark-workflow-standup-report`, `feishu-bitable-creator`, `feishu-card-v2`, `feishu-lark-sheets-edit`
- **Count**: 22 → **8-9**

### 分组 4：Get笔记 6 个 → 合并为 2 个
- **保**: `getnote-kb` + `getnote-note`（核心功能）
- **删**: `getnote`, `getnote-auth`, `getnote-search`, `getnote-tag`（功能被 kb/note 覆盖）
- **Count**: 6 → **2**

### 分组 5：Evernote 5 个 → 合并为 2 个
- **保**: `evernote-yinxiang`（综合 API）+ `印象笔记文章保存`（公众号专用管线）
- **删**: `evernote-note`, `印象笔记去重`, `印象笔记管理工具`
- **Count**: 5 → **2**

### 分组 6：微信读书 3 个 → 1 个
- **保**: `weread-official-skills`（官方功能最全）
- **删**: `weread-analyzer`, `weread-book-finder`（功能被官方覆盖）
- **Count**: 3 → **1**

### 分组 7：Obsidian/知识库 4 个 → 2 个
- **保**: `obsidian-cli` + `知识库管理工具`
- **删**: `obsidian-bases`, `obsidian-markdown`
- **Count**: 4 → **2**

### 分组 8：File Manager 系列 → 2 个
- **保**: `file-manager` + `file-organizer-zh`
- **删**: `filesystem`, `filesystem-access`, `file-browser`, `local-file-manager`
- **Count**: 6 → **2**

### 分组 9：Skill Discovery 系列 → 2 个
- **保**: `skill-creator` + `openspace`
- **删**: `skill-discovery`, `skill-vetter`, `find-skills`, `find-skills-in-tencent-skillhub`, `skillhub-preference`, `find`
- **Count**: 7 → **2**

### 分组 10：baoyu 内容管线 — 持续用保留，其余可清理
- **核心管线保留**: `baoyu-diagram`, `baoyu-translate`, `baoyu-post-to-wechat`, `baoyu-url-to-markdown`, `baoyu-imagine`, `baoyu-image-cards`, `baoyu-infographic`, `baoyu-comic`, `baoyu-youtube-transcript`
- **低频可能删**: `baoyu-article-illustrator`, `baoyu-cover-image`, `baoyu-format-markdown`, `baoyu-markdown-to-html`, `baoyu-post-to-weibo`, `baoyu-post-to-x`, `baoyu-slide-deck`, `baoyu-compress-image`, `baoyu-danger-gemini-web`, `baoyu-danger-x-to-markdown`
- **保留待定**: `baoyu-format-markdown` vs `markdown-formatter` 重叠

### 分组 11：OCR — baidu-ocr + screenshot-ocr + azure-doc-ocr
- baidu-ocr（百度 API）和 azure-doc-ocr（Azure）有各自用途
- screenshot-ocr 是截图场景，不同
- doc-ocr-skills（16MB）与多个 OCR 重叠 → **可删**

### 分组 12：设计/视觉 — 多重重叠
- `canvas-design`, `mar-canvas-design`（描述几乎一样）→ 保留一个
- `theme-factory` + `frontend-design` → 保留，有用
- `brand-guidelines` → 低频，可删
- `algorithmic-art` → 低频，可删
- `data-visualization-2` → 低频，可删


## 🟢 确定保留的核心（25-30 个）

### 业务分析（高频使用 — 不动）
- `产品市占率分析工具`
- `华程达成率分析工具`
- `四川省联盟包团分析工具`
- `四川省联盟市占率分析工具`
- `渠道市占率分析工具`
- `huaxi-inquiry-analysis`
- `hc-europe-product-compare`
- `差旅报销工具`
- `旅游行业市场调研工具`
- `模型成本分析`
- `微信读书管理工具`
- `知乎管理工具`
- `邮箱管理工具`
- `错题本`
- `expense-assistant` / `expense-claims-ops` → 重复，删一个

### 系统基础设施
- `claude-api` — API 参考
- `context7-mcp` — 库文档
- `cdp-browser` — 浏览器控制
- `deepseek-pro-agent` — 模型委托
- `llm-wiki-karpathy` — Wiki 维护
- `LLM-Wiki管理工具` — Wiki 维护 skill 版本
- `planning-with-files` — 复杂任务规划
- `webapp-testing` — 前端测试
- `taskmaster` — 任务管理
- `self-improving-agent` — 自我改进
- `proactive-agent` — 主动代理
- `skill-creator` — 创建/优化 skills
- `mcp-builder` — 创建 MCP servers

### 个人工具（低频但特定用途）
- `a-share-portfolio-calibrator` — A股组合
- `stock-analyzer` — 选股
- `advisory-board` — 私董会


## 📊 汇总：删除 vs 保留估算

| 操作 | 数量 |
|------|------|
| 当前安装 | **152** |
| 🔴 立即删除（废弃/空壳/明确重复） | ~25 |
| 🟡 需合并的冗余（15 组 → 5-6 组） | ~60→~25 |
| 🟢 确定保留的核心 | ~25-30 |
| **清理后预估** | **~30-35** |


## ⚠️ 特别标注：大体积 skill

| Skill | 体积 | 建议 |
|-------|------|------|
| `mineru-pdf` | **1.17 GB** | 含 ML 依赖，如果很少用 PDF OCR 建议删，用 `geminipdfocr` 替代 |
| `gstack` | **734 MB** | 不知用途，建议删 |
| `pdf-text-extractor` | **32 MB** | 应删，pdf skill 已够 |
| `doc-ocr-skills` | **16 MB** | 与 baidu-ocr/mineru-pdf 重叠，可删 |
| `canvas-design` | **5.4 MB** | 低频，可考虑删 |


## 操作建议

1. **确认权限** — 先确认上面分析中你不同意的部分
2. **我逐组执行删除** — 已确认的组我立即执行
3. **核实** — 删除后清理 MEMORY.md 中相关的引用（如有）
