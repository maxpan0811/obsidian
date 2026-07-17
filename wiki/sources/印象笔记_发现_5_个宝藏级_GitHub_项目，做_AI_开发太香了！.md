---
title: "发现 5 个宝藏级 GitHub 项目，做 AI 开发太香了！"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/发现 5 个宝藏级 GitHub 项目，做 AI 开发太香了！.md
tags: [印象笔记]
---


来源：[打开原文](https://mp.weixin.qq.com/s/HkzRvaAcr_zY4bJepCld3w)

\* 戳上方蓝字“程序掘金”关注我

01 Outlines
-----------

这是 Python 生态里做 LLM 结构化生成（Structured Generation）的利器。

大语言模型的输出经常不可控，普通做法是生成完再用正则或解析器去修，脆弱又麻烦。Outlines 直接在 token 生成阶段就用有限状态机约束输出，保证结果一定符合你指定的 JSON Schema、Pydantic 模型或正则表达式——不需要重试、不需要后处理。

![](.evernote-content/2180F10C-D65C-4A54-9BE2-5C4E7AAF2414/F10FDEF0-842B-41E4-8A12-2F3717DE21FD.jpg)

它支持 OpenAI、Anthropic、vLLM、transformers、llama.cpp、Ollama 等主流后端，写法也很 Pythonic，比如 outlines.generate.json(mode

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->