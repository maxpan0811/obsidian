---
title: four-source-answer-rule
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


用户要求所有回答必须从四个来源分别查证并明确标注来源，禁止不标来源直接输出训练数据。

**四个来源：**
1. **🧠 训练数据** — Claude 模型训练阶段积累的知识
2. **📓 Wiki 知识库** — 用户的 Obsidian 个人知识库
3. **🌐 Tavily 搜索** — Tavily Search API（key 在 `$TAVILY_API_KEY`）
4. **📊 向量数据库** — FAISS 向量索引

**规则：**
- 回答前必须检查所有四个来源
- 搜不到的要明确写"该来源无相关记录"
- 按来源分类呈现，不混为一谈
- 多个来源一致时标注"交叉验证一致"

**例外：** 闲聊/问候/简单确认不触发；用户说"不用查了"不触发。

**Why:** 用户发现我之前回答 NeXTSTEP 问题时 100% 只用了训练数据，没有分来源查证和标注。要求以后所有信息问题都四源并行查证后再回答。

**How to apply:** 接到问题后，先并行执行：①内部回忆（🧠）②grep/搜索 Obsidian vault（📓）③curl Tavily API（🌐）④搜索 FAISS 索引（📊）。然后按来源分类输出。
