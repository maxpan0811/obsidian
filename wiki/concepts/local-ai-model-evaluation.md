---
title: 本地 AI 模型选型评估（M4 Max 64GB）
type: concept
date: 2026-07-17
tags: [ollama, mlx, multimodal, hardware, apple-silicon, evaluation]
---

# 本地 AI 模型选型评估

## 背景

2026年7月，为 AI Router 项目评估 M4 Max 64GB Mac 上的最佳本地多模态（视觉+文本）模型方案。评估覆盖三种信息源：训练知识、本地资料库、Tavily 网络搜索。

## 溯源图标系统

用户要求在回答中标注每条信息的来源。[决策] 这套图标来自同日的用户偏好确认。

| 图标 | 含义 |
|------|------|
| 💭 | 训练知识（Agent 内置知识） |
| 🗂️ | 本地资料库 / 向量数据库 |
| 📖 | Wiki 资料库 |
| 📊 | Tableau 数据可视化 |
| 🌐 | Tavily 网络搜索 |

## 硬件预算

- 芯片：Apple M4 Max
- 统一内存：64 GB
- 模型权重可用上限：~35-40 GB（预留 20 GB+ 给系统和 KV Cache）
- 推理引擎：Ollama v0.31.1（支持 MLX + GGUF 双后端）、mlx-lm v0.31.3

## Tavily 配置

[决策] 用户提供 Tavily API Key，实现第三信息源查询。

- API Key 存入 `~/.zshrc`
- 客户端：`tavily-python` v0.7.26
- 用途：Agent 自动搜索最新技术资料，补训练知识过时和本地资料不足

🌐 来源说明：Tavily 是专为 AI Agent 设计的结构化搜索引擎，返回结果比人用浏览器更适合 LLM 解析。

## 三源头回答原则

[决策] 用户要求后续所有问题的回答必须同时参考三部分信息：

1. 💭 训练知识（Agent 受训练时的知识库）
2. 🗂️ 本地资料库 + 📖 Wiki 资料库
3. 🌐 Tavily 网络搜索（获取最新信息）

例外场景：纯本地操作（文件整理、数据分析）和纯代码实现问题可不搜索。

## 候选模型评估

### 关键发现

**Qwen3.6-35B-A3B 是纯文本模型，不带多模态能力。** ❌

💭 关于 Qwen 系列的命名规则：带 `-VL` 后缀的才是视觉语言模型（如 Qwen3-VL-30B），纯数字编号如 Qwen3.6-35B 是文本模型。

### 候选模型清单

#### Qwen3-VL 系列

🌐 来源：Ollama Models Cheat Sheet 2026 评为"the strongest open vision-language family on Ollama now"。available sizes: 2B, 4B, 8B, 30B, 32B, 235B, 256K-1M context.

| 版本 | 内存 | 备注 |
|------|------|------|
| GGUF Q4_K_M | ~35.4 GB | 在 64GB 上可运行，余量够 |
| MLX 4-bit | ~20-22 GB | 需通过 mlx-lm 直接调用 |

🌐 关键限制：
- **Ollama MLX vision 输入 bug** (#17065)：Ollama MLX 引擎的 vision 模型在 Apple Silicon 上收不到图片输入。Open 状态。
- **GGUF 看图崩溃** (#16264)：Qwen3-VL-8B GGUF + mmproj 在 Apple Silicon 上处理图片时 exit code 2 退出。Open 状态。
- ✅ mlx-lm 直接调 MLX 4-bit 版本：专门 macOS 指南确认可用，持续维护。

#### Gemma 4 系列（Google DeepMind，2026年4月发布）

🌐 所有版本均支持视觉+音频多模态，"encoder-free multimodal"（无独立视觉/音频编码器）。

| 版本 | 参数量 | Q4 内存 | 特点 |
|------|--------|---------|------|
| Gemma 4 12B | 12B dense | ~6.6 GB | "26B-MoE-class quality"，DocVQA 94.9 |
| Gemma 4 26B-A4B | 26B MoE | ~15-18 GB | 开源，MLX MTP 加速 +90% |
| Gemma 4 31B | 31B dense | ~18-22 GB | 最高质量密集版 |

🌐 关键限制：
- **Gemma 4 12B 不可用** (#16562)：Ollama 上 8 分钟生成、死机、空响应。Open 状态。
- **MLX vision bug** (#17065) 同样波及 Gemma 4 12B。
- 💭 MLX MTP（Multi-Token Prediction）在 v0.31 中默认启用，Apple Silicon 上加速接近 90%。

#### 已排除方案

| 模型 | 排除原因 |
|------|----------|
| Llama 4 Maverick (400B MoE) | Q2 也要 64GB，无余量 |
| DeepSeek-V3 | Q4 需 72GB，超 64GB |
| Pixtral / InternVL3 | 未查到 Ollama MLX 明确支持记录 |

## Ollama 后端兼容性问题

💭 Ollama v0.31.1 支持两个后端引擎：MLX（v0.19 引入，预览版 2026年3月）和 GGUF/llama.cpp（v0.30 增强，2026年6月）。

🌐 2026年7月时 Apple Silicon 上的多模态模型有三个已知 open issue：

| Issue | 模型 | 问题 |
|-------|------|------|
| #17065 | Gemma 4 12B / Qwen3.5 4B | MLX 引擎收不到图片输入 |
| #16562 | Gemma 4 12B | 生成极慢、死机、空响应 |
| #16264 | Qwen3-VL-8B (GGUF) | 看图直接崩溃退出 |

**结论：Ollama 的 vision pipeline 在 Apple Silicon 上当前（2026年7月）不可靠。**

## 最终推荐方案

[决策] 双模型 → 路由分工，Ollama 管文本 + mlx-lm 管看图。

| 职责 | 模型 | 引擎 | 内存 | 理由 |
|------|------|------|------|------|
| 💬 纯文本 | `qwen3.6:35b-mlx` | Ollama MLX | ~19-20 GB | 稳定高速，MLX 引擎无问题 |
| 🌐 看图 | `Qwen3-VL-30B-A3B-Thinking` | mlx-lm 直接 | ~20-22 GB | MLX 4-bit 维护中，避开 Ollama 所有 bug |

### 推荐理由

1. **qwen3.6:35b-mlx** 是纯文本类的首选。💭 35B A3B 架构在 4-bit MLX 上仅 ~19 GB，M4 Max 64GB 绰绰有余。🌐 Ollama MLX 引擎文本推理无 bug。
2. **Qwen3-VL-30B-A3B-Thinking** 是多模态首选。🌐 macOS 专有指南推荐 mlx-lm 直连，4-bit MLX 构建持续维护，"strongest open vision-language family"。💭 30B total / 3B active 的 A3B 架构 + thinking 推理模式。
3. **Gemma 4 12B 暂不可用**。尽管 6.6GB 的微小体积很诱人，但 Ollama 上的两个 open bug 使其无法在 Apple Silicon 上正常使用。
4. 两个模型不同时加载，不抢内存。

## 相关参考

- [Ollama MLX Performance Blog (2026-06-11)](https://ollama.com/blog/mlx-performance)
- [Ollama Faster Gemma 4 on MLX with MTP (2026-06-29)](https://ollama.com/blog/faster-gemma-4-mlx-mtp)
- [Ollama GGUF 改进 (2026-06-05)](https://ollama.com/blog/improved-performance-and-model-support-with-gguf)
- [Run Qwen3-VL-30B-A3B-Thinking on macOS Guide](https://codersera.com/blog/run-qwen3-vl-30b-a3b-thinking-on-macos-installation-guide)
- [Ollama Models Cheat Sheet 2026](https://computingforgeeks.com/ollama-models-cheat-sheet)
- Ollama Issues: [#17065](https://github.com/ollama/ollama/issues/17065) [#16562](https://github.com/ollama/ollama/issues/16562) [#16264](https://github.com/ollama/ollama/issues/16264)
