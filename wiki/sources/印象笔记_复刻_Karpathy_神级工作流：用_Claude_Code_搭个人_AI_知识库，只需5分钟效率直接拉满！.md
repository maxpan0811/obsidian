---
title: "复刻 Karpathy 神级工作流：用 Claude Code 搭个人 AI 知识库，只需5分钟效率直接拉满！"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/复刻 Karpathy 神级工作流：用 Claude Code 搭个人 AI 知识库，只需5分钟效率直接拉满！.md
tags: [印象笔记]
---


Andre Karpathy 最近发布了一种使用 LLM 构建知识库的方法，这种方法相比传统方法有了巨大突破，因为 AI 可以持续记忆并帮你整理信息。小林我已经在自己的电脑上搭建了，使用claude code +obsidian,感觉很牛，分享给大家。

![](.evernote-content/E3A8B7AE-B407-451E-B4BB-45A1D6153A0E/03658749-7A48-4CB7-95EF-7FDEF55A2FCF.png)

这个核心流程是：输入原始数据 → 自动整理 → 建立关系 → 支持查询。同时还能发现知识缺口，并进行补充研究。传统 AI 对话是短暂的，记忆不会保留，而这种方式可以让知识持续积累。

整个搭建过程约 5 分钟，不需要复杂架构，只需要和claude code对话。

Karpathy 方案的灵魂，就是把「原始资料、处理过程、成品 Wiki」彻底分开，避免混乱。

这种方式在成本和 token 使用上更高效。有用户将 383 个文件和 100 多份会议记录整理为 Wiki，token 使用降低了 95%。此外，不需要复杂配置，只需让 Cl

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->