---
name: Qwen3
type: product
category: ai-model
company: Alibaba (通义千问)
tags: [qwen3, alibaba, ai-model, local-llm, mcp]
created: 2026-06-11
updated: 2026-06-11
---

# Qwen3

阿里通义千问推出的新一代语言模型系列，涵盖 4B 到 235B 多种规格，优化了 Agent 和代码能力，加强对 MCP 的支持。

## 系列规格

| 模型 | 参数 | 架构 | 上下文 | 定位 |
|:----|:----:|:----:|:-----:|:-----|
| Qwen3-4B | 4B | Dense | 32K | 边缘/移动端 |
| Qwen3-8B | 8B | Dense | 128K | 消费级显卡 |
| Qwen3-14B | 14B | Dense | 128K | 工作站 |
| Qwen3-30B-A3B | 30B | MoE (3B 激活) | 128K | 高效推理 |
| Qwen3-32B | 32B | Dense | 128K | 高性能 |
| Qwen3-235B-A22B | 235B | MoE (22B 激活) | 128K | 旗舰 |

## 实测结果（与 Obsidian-MCP）

- **4B**: 量化后丢失工具调用能力，指令理解失效
- **8B**: 能调用工具但文件路径幻觉，需 git 备份防误删
- **14B+**: 工具调用准确，128K 上下文适配知识库场景，需 16G 显存

## 相关来源

- [[sources/Qwen3小模型实测-Obsidian-MCP]]
