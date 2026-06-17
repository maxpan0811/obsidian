---
title: LLM Wiki Schema for Technical Writer
type: source
created: 2026-06-11
updated: 2026-06-11
sources: [LLM Wiki Schema for Technical Writer.md]
source_path: RAW/md/LLM Wiki Schema for Technical Writer.md
tags: [source, LLM Wiki, wiki运维, schema, 技术写作, 方法论]
---

# LLM Wiki Schema for Technical Writer

> LLM Wiki的技术写作者操作手册，定义了wiki结构、实体类型、工作流和约定规范。

## 目录结构
```
wiki/
├── index.md        ← 主目录（每次ingest更新）
├── log.md          ← 只追加的活动日志
├── overview.md     ← 全局概览
├── glossary.md     ← 术语表和风格规则
├── sources/        ← 原始来源摘要页
├── features/       ← 产品功能页
├── products/       ← 产品或工具页
├── personas/       ← 用户画像页
├── concepts/       ← 核心概念或领域思想页
├── style/          ← 风格指南
└── analyses/       ← 分析产出页
```

## 实体类型
| 类型 | 位置 | 用途 |
|------|------|------|
| Source | `wiki/sources/` | 原始文档的摘要 |
| Feature | `wiki/features/` | 产品功能描述 |
| Product | `wiki/products/` | 产品或工具概览 |
| Persona | `wiki/personas/` | 用户类型画像 |
| Concept | `wiki/concepts/` | 领域概念 |
| Style Rule | `wiki/style/` | 写作约定 |
| Analysis | `wiki/analyses/` | 综合产出 |

## 页面格式
每个页面必须有YAML frontmatter：
```yaml
---
title: <标题>
type: source|feature|product|persona|concept|style|analysis
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [来源文件名列表]
tags: [标签]
---
```
正文结构：一句话摘要 → 主体（标题/列表/表格） → 相关页面（`[[wiki-page-name]]` 链接）

## 工作流
- **Ingest**：读源文件 → 讨论关键点 → 创建source页 → 更新现有页 → 创建新实体页 → 更新glossary/index/overview/log
- **Query**：读index → 读相关页 → 综合回答 → 选择是否存档为analysis页
- **Lint**：读全部页 → 报告矛盾/孤立/缺失 → 修复

## 关键原则
- 内部链接统一用 `[[filename-without-extension]]`
- 术语出现时→添加到glossary；冲突时→显式标记
- 优先更新现有页而非创建新页
- 文件名为kebab-case

## 相关页面
- [[concepts/LLM Wiki模式]]
- [[sources/LLM Wiki 原文]]
