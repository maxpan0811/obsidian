---
title: 20260715-codex-config-verbosity
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Codex 配置优化：三参数减少废话

## 场景
用户从 OpenAI 社区发现一组 Codex 配置，可以大幅减少回答中的废话和冗余，跑到官方手册核实后确认有效。

## 配置

```toml
model_reasoning_summary = "concise"  # 推理摘要压到最短
model_verbosity = "low"              # 输出极简，砍铺垫和重复总结
personality = "pragmatic"            # 工程师式沟通，不寒暄
```

## 要点

1. **model_verbosity** 只对 Responses API provider 生效。用户用的是 custom provider（DeepSeek）但 wire_api = "responses"，所以能用
2. **personality** 有双层结构：`[features] personality = true` 是功能开关，顶层 `personality = "pragmatic"` 设值，两个都要开
3. 三档取值已从官方手册确认：personality 可选 `friendly | pragmatic | none`，model_reasoning_summary 可选 `auto | concise | detailed | none`，model_verbosity 可选 `low | medium | high`

## 效果
Codex 回答变得更加直给——代码和命令为主，不再有大段解释和重复总结。风格偏向工程师之间的沟通方式而非助手式客套。
