---

name: LLM Wiki 原文
type: source
tags: [LLM Wiki, Karpathy, 原文, 双语]
source_path: RAW/md/LLM Wiki Schema for Technical Writer.md

---

# Karpathy llm-wiki.md 原文（双语对照）

来源：[GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 作者：Andrej Karpathy

双语对照版（英文 + 中文翻译，含 Chat vs Reasoner 逐段对比）。

## 核心理念

LLM 不应像 RAG 那样每次从零检索知识，而应**增量式构建和维护一个持久的、结构化、相互链接的 Markdown wiki**。知识被一次性编译，然后保持最新。

> You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it.
> 你从不（或很少）亲自编写维基——LLM 负责编写和维护所有内容。

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.
> Obsidian 是 IDE，LLM 是程序员，维基就是代码库。

## 三层架构

| 层 | 角色 | 维护者 |
|---|------|--------|
| **Raw sources** | 原始资料（只读） | 用户 |
| **Wiki** | 结构化知识页面 | LLM |
| **Schema (CLAUDE.md)** | 规则/工作流定义 | 用户 + LLM 共同演进 |

## 三种操作

- **Ingest** — 读资料 → 讨论 → 写摘要 → 更新索引 → 更新相关页面 → 记录日志
- **Query** — 查索引 → 读页面 → 综合回答（答案可存回 wiki）
- **Lint** — 健康检查：矛盾、过期、孤立页、缺失交叉引用

## 适用场景

个人目标追踪、深度研究、读书笔记、团队内部 wiki、竞争分析、旅行规划等。

影响页面：[[concepts/LLM Wiki模式]]
