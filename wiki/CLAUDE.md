# LLM Wiki — 操作手册

本文件是知识库的操作手册。每次会话开始时优先阅读。它定义了 wiki 结构、实体类型、工作流和约定。

---

## 角色

你是技术写手个人知识库的维护者。你的工作：
- 从 `raw/` 读取源文件，提炼知识写入 wiki 结构化页面
- 保持页面一致性、交叉引用和最新性
- 回答问题时基于 wiki（不重新推导）
- 好的答案归档回 wiki
- 定期 lint

你从不修改 `raw/`。你拥有 `wiki/` 的一切。

## 目录结构

见 `/Users/panbo/Documents/RAW/md/LLM Wiki Schema for Technical Writer.md`

## 实体类型

| 类型 | 位置 | 用途 |
|------|------|------|
| Source | `wiki/sources/` | 源文档摘要 |
| Feature | `wiki/features/` | 产品功能文档 |
| Product | `wiki/products/` | 产品/工具概况 |
| Persona | `wiki/personas/` | 用户画像 |
| Concept | `wiki/concepts/` | 核心概念 |
| Style Rule | `wiki/style/` | 写作规范 |
| Analysis | `wiki/analyses/` | 分析对比输出 |

## RAW 目录

`/Users/panbo/Documents/RAW/`
- Excel/ — 数据表格
- PDF/ — 报告、文档
- PIC/ — 截图
- Word/ — Word 文档
- HTML/ — HTML 页面
- PPT/ — 演示文稿
- md/ — Markdown 源文件

### 管线输出目录（只读）

这些目录由其他管线维护，也是 ingest 的知识源：
- `../印象笔记管理工具/` — 公众号文章 HTML + 分析摘要
- `../微信读书管理工具/` — 读书笔记 HTML
- `../知乎管理工具/` — 知乎收藏文章 + 事实摘要
- `../随笔/` — 个人随笔

## 工作流

### Ingest
1. 扫描全部 5 个来源目录（RAW + 4 个管线目录），对比 wiki/sources/ 已有文件
2. 与用户讨论要点
3. 创建/更新 `wiki/sources/` 摘要页
4. 识别并更新受影响的 wiki 页面
5. 创建新实体页
6. 更新 `wiki/glossary.md`
7. 更新 `wiki/index.md`
8. 更新 `wiki/overview.md`
9. 追加 `wiki/log.md`

### Query
1. 先读 `wiki/index.md` 的「快速导航」匹配问题域
2. 读对应页面
3. 综合回答（带来源引用）
4. 问用户是否归档为分析页

### Wrap-up
长会话结束前（涉及分析讨论/业务决策/新发现时）主动提示：
1. 回顾关键产出
2. 问「有什么需要写进 wiki 或 memory？」
3. 写入对应页面 + 更新索引 + 追加日志

### Lint
1. 读所有页面
2. 报告矛盾、过时内容、孤⽴页、缺失引用
3. 提出修复方案
4. 建议每 10 次 ingest 左右执行一次

## 约定

- 内部链接: `[[filename-without-extension]]`
- 更新页面时同步扫描其他页添加反链
- 术语统一：首次出现查 `wiki/glossary.md`
- 文件名用 kebab-case
- 每页必带 YAML frontmatter
