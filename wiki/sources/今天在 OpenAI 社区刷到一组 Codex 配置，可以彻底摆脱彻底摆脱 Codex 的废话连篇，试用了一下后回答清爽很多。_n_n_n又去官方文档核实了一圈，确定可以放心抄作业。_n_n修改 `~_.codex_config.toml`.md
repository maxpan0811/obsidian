---
title: "今天在 OpenAI 社区刷到一组 Codex 配置，可以彻底摆脱彻底摆脱 Codex 的废话连篇，试用了一下后回答清爽很多。_n_n_n又去官方文档核实了一圈，确定可以放心抄作业。_n_n修改 `~_.codex_config.toml`_n_n配置就这三行：_n_n```toml_nmodel_reasoning_summary = _concise_ # 简短摘要_nmodel_verbos"
type: source
created: 2026-07-18
updated: 2026-07-18
source: 印象笔记
source_path: 印象笔记管理工具/今天在 OpenAI 社区刷到一组 Codex 配置，可以彻底摆脱彻底摆脱 Codex 的废话连篇，试用了一下后回答清爽很多。_n_n_n又去官方文档核实了一圈，确定可以放心抄作业。_n_n修改 `~_.codex_config.toml`_n_n配置就这三行：_n_n```toml_nmodel_reasoning_summary = _concise_ # 简短摘要_nmodel_verbos.md
tags: [印象笔记]
---

## 摘要

今天在 OpenAI 社区刷到一组 Codex 配置，可以彻底摆脱彻底摆脱 Codex 的废话连篇，试用了一下后回答清爽很多。

又去官方文档核实了一圈，确定可以放心抄作业。

修改 `~/.codex/config.toml`

model\_reasoning\_summary = "concise" # 简短摘要

model\_verbosity = "low" # 输出极简

personality = "pragmatic" # 务实风格

具体每一项管什么，其实文档里面都有详细的介绍。

model\_verbosity输出详细程度

官方取值只有三档：`low | medium | high`。

设成 `low` 之后，Codex 会尽量只给代码和结论，砍掉铺垫、总结、鼓励式话术这些"废话"。

默认值其实是 `medium`，很多人嫌它啰嗦就是没改这项。

model\_reasoning\_summary推理摘要详略

这里要澄清一个常见误解：不管这项怎么设，Codex 展示给你的从来都只是"推理过程的摘要"，完整的思维链本来就不会输出。

取值有 `auto | concise | detailed | none` 四档，`concise` 就是把摘要压到最短，`none` 则直接不显示推理过程。

