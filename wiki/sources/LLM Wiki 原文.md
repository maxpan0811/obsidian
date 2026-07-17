---

name: LLM Wiki 原文
type: source
tags: [LLM Wiki, Karpathy, 原文, 双语]
source_path: RAW/md/LLM Wiki Schema for Technical Writer.md

---


来源：[GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 作者：Andrej Karpathy

双语对照版（英文 + 中文翻译，含 Chat vs Reasoner 逐段对比）。

## 核心理念

LLM 不应像 RAG 那样每次从零检索知识，而应**增量式构建和维护一个持久的、结构化、相互链接的 Markdown wiki**。知识被一次性编译，然后保持最新。

> You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it.
> 你从不（或很少）亲自编写维基——LLM 负责编写和维护所有内容。

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.
> Obsidian 是 IDE，LLM 是程序员，维基就是代码库。

## 三层架构

| 层 | 角色 |

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->