---
title: YAML Frontmatter 模板
type: style
created: 2026-05-29
updated: 2026-05-29
sources: [LLM Wiki Schema for Technical Writer]
tags: [style, template, frontmatter]
---

# YAML Frontmatter

每页必须包含以下 YAML 头。

## 模板

```yaml
---
title: <页面标题>
type: source | feature | product | persona | concept | style | analysis
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [源文件名列表，来自 raw/]
tags: [标签列表]
---
```

## 类型说明

| type | 对应 wiki 目录 |
|------|---------------|
| source | `wiki/sources/` |
| feature | `wiki/features/` |
| product | `wiki/products/` |
| persona | `wiki/personas/` |
| concept | `wiki/concepts/` |
| style | `wiki/style/` |
| analysis | `wiki/analyses/` |

## 示例

```yaml
---
title: ERP 功能优化 v4 (5/7)
type: source
created: 2026-05-07
updated: 2026-05-07
sources: [ERP系统功能优化说明（20260507）.pdf]
tags: [erp, release-notes, v4]
---
```

## 相关页面

- [[CLAUDE]]
- [[glossary]]
