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
| Capture | `wiki/capture/` | 会话自动抓取记忆（Claude Code 双写 + hook 同步） |
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
3. **创建/更新 `wiki/sources/` 摘要页**（🚫 不要复制全文！只写摘要）:
   - 优先取原文的"速读摘要"/"智能摘要"段（印象笔记类文章常有）
   - 无现成摘要时，自己用 LLM 压缩为 200-600 字摘要
   - 始终附带 `原文链接` 和 `[摘要]` 标记
   - 全文搜索由 FAISS 在 vault 原文上执行，sources/ 只做关键词检索
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

## Capture 双写规则

memory/ 和 wiki/capture/ 同步写入——memory/ 写什么，capture/ 就写同样内容的一份。

**格式**：
- 位置：`wiki/capture/<name>.md`
- Frontmatter：`title=name`、`type=capture`、`tags=auto-capture + 内容相关 tag`、`source="Claude Code 会话 YYYY-MM-DD"`、`created=日期`
- Body：保持 memory 体内容，不加额外加工
- 不重复保存 — 同名文件已存在则跳过

**图片相关注意事项**：

当 capture 内容涉及图片时（如截图分析、UI 设计研究、图表解读等）：

1. **图片必须保存到本地** — 不要尝试通过 API 嵌入印象笔记或其他外部服务
   - 保存到 `wiki/products/<主题>-screenshots/` 或 `RAW/PIC/`
   - 文件名用 kebab-case，带序号前缀（如 `01-desktop.png`）

2. **笔记/页面中写图片位置** — 在文字内容里注明"图片已保存到 XX 路径"
   - 示例：`截图已保存到 wiki/products/nextstep-screenshots/`
   - 用户需要时可手动拖入印象笔记或插入 Obsidian

3. **不要尝试的方式**（已验证全部失败）：
   - ❌ Markdown 图片语法 `![alt](url)` — 外部 API 不会下载
   - ❌ Base64 data URI — 内容超 ~10KB 会被截断
   - ❌ 图床上传后嵌入 — 外部服务从这个网络超时

4. **Capture 内容本身可以引用图片路径** — 用相对路径或 vault 绝对路径
   - 示例：`![NeXTSTEP Desktop](wiki/products/nextstep-screenshots/01-desktop.png)`
   - Obsidian 可以正常渲染相对路径图片

**Why**：外部图片 API（印象笔记、图床等）要么不支持嵌入，要么网络不可达。本地保存 + 路径引用是唯一可靠方案。
