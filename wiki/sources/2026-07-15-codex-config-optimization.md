---
name: 2026-07-15-codex-config-optimization
type: source
tags: [claude-codex, code-config, personality, verbosity]
source_path: /Users/panbo/Obsidian/程序开发/2026-07-15-Codex配置优化-model_verbosity-model_reasoning_summary-personality.md
---

[摘要] 本文档记录了 Codex 配置优化经验。2026年7月15日，用户从 OpenAI 社区发现一组 Codex 配置，可大幅减少回复中的废话（铺垫、总结、鼓励式话术）。三条核心配置写入 `~/.codex/config.toml`：`model_verbosity = "low"`（输出极简）、`model_reasoning_summary = "concise"`（推理摘要简短）、`personality = "pragmatic"`（务实风格）。各参数的生效范围不同：model_verbosity 仅对 Responses API provider 生效，Chat Completions 忽略此设置；personality 需在 `[features]` 下加 `personality = true` 开启功能开关，同时顶层设值。配置效果：Codex 以代码和命令为主，不再有大段解释和重复总结，风格偏向工程师之间的直接沟通。原文链接：/Users/panbo/Obsidian/程序开发/2026-07-15-Codex配置优化-model_verbosity-model_reasoning_summary-personality.md