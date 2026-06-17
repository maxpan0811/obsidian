---
title: Qwen3小模型实测：从4B到30B，到底哪个能用MCP和Obsidian顺畅对话？
type: source
created: 2026-06-11
updated: 2026-06-11
source_path: 印象笔记管理工具/Qwen3小模型实测：从4B到30B，到底哪个能用MCP和Obsidian顺畅对话？.html
tags: [qwen3, obsidian, mcp, local-llm, test]
---

**摘要**: 实测 Qwen3 系列本地模型（4B/8B/14B/30B-A3B）与 Obsidian-MCP 的知识库交互效果。4B 量化后丢失工具调用能力，8B 能调用但文件路径存在幻觉，14B+ 能正常对话但需 16G 显存。结论：本地小模型可用性逐步上升，但流畅交互仍需足够硬件。

## 核心观点

- 4B 量化版本完全丢失工具调用能力，含明确的工具名也无响应
- 8B 版本能识别工具调用但文件路径错误率高，存在幻觉改写风险
- 14B+ 版本 128K token 容量完美适配知识库场景，但需 16G 显存
- 云端大模型 + MCP 是当前折中方案

## 关键细节

- **Qwen3-4B**: 32K token，官方称匹敌 Qwen2.5-72B，但量产后指令理解丢失
- **Qwen3-8B**: 能调用 Obsidian-MCP 的 search 工具，但返回文件路径错误
- **Qwen3-14B**: 128K token，调用 Obsidian API 准确，openrouter 限制 40K 上下文
- **Qwen3-30B-A3B**: MoE 架构，激活参数仅 3B，表现优于 QwQ-32B
- **硬件需求**: 16G 显存才能本地部署 14B+
- **建议**: 云端大模型 + MCP 读取非敏感数据，做好隐私保护 + git 备份

## 相关页面

- [[concepts/Obsidian-MCP]]
- [[products/Qwen3]]
