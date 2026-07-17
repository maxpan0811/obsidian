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
 
 ## 三级路由策略
 
 [决策（2026-07-17）] 三层路由替代原本的"有图→本地，无图→云端"二分法。
 
 ### 架构
 
 输入 → 三层判断：
 
 1. 🌐 **含图片** → `Qwen3-VL-30B-A3B-Thinking`（本地 mlx-lm 直接调用）
 2. 💬 **纯文本，简单/隐私** → `qwen3.6:35b-mlx`（本地 Ollama MLX）
 3. 💬 **纯文本，复杂/专业** → DeepSeek API（云端）
 
 ### 什么时候走云端
 
 | 场景 | 原因 |
 |------|------|
 | 复杂推理（多步逻辑链、数学证明、代码生成） | 云端 671B MoE 无损推理，质量远超量化 35B |
 | 超长上下文 | 本地 KV Cache 受内存限制 |
 | 质量敏感输出（重要邮件、报告） | 值得花 token 费 |
 | 本地模型切换间隙 | 两模型不能同时驻内存 |
 | 公开信息查询、日常问答 | 无需隐私保护 |
 
 ### 什么时候走本地
 
 | 场景 | 原因 |
 |------|------|
 | 含图片输入 | 唯一必选本地场景，roter 搭建初衷 |
 | 隐私内容（公司数据、个人资料） | 数据不出本机 |
 | 离线环境（飞机、无网） | 本地可脱离网络运行 |
 | 高频低价值查询 | 省 API 费 |
 | 快速响应需求 | 本地 MLX 延迟更低 |
 
 ### 手动覆盖
 
 - `--local`：强制本地文本模型
 - `--cloud`：强制云端 DeepSeek API
 - `--image <path>`：指定图片
 


---

## 关键纠正：Ollama MLX ≠ mlx-lm

[来源：Tavily 搜索 + 两篇技术分析文章]

Ollama 的 MLX 后端和原生 mlx-lm 是两套东西：

| 路径 | 权重格式 | 推理引擎 | Ollama 是否支持 |
|------|---------|---------|--------------|
| 原生 mlx-lm | safetensors + MLX 元数据 | mlx-lm (Python 包) | ❌ 不认 |
| Ollama MLX 路径 | safetensors（特调）+ nvfp4/mxfp8 量化 | Ollama 内嵌 MLX 库 | ✅ 只认仓库里带 mlx tag 的官方镜像 |

💡 Ollama 的 "MLX 支持" ≠ "支持 mlx-lm 格式的模型"。Ollama 0.19 引入 MLX 引擎后，只认自家仓库里打了 `mxfp8`/`mlx-bf16`/`nvfp4` 等 tag 的模型。目前这些 tag 只覆盖了 Qwen3.5/Qwen3.6 几个纯文本编码型号，Qwen3-VL 系列还没出 MLX 变体。

## Qwen3-VL-30B 在 Ollama 的现状

- 架构: `qwen3vlmoe`，30B-A3B MoE（实际激活 3B）
- Ollama library 里有 `qwen3-vl:30b`，但走的是 **llama.cpp/GGUF 路径**，不是 MLX
- 量化 Q4_K_M，~20 GB
- 要求 Ollama ≥ 0.12.7，`ollama pull qwen3-vl:30b` 直接跑

## 三条路线对比（M4 Max 64GB）

| 路线 | 方式 | 内存 | 速度 | 说明 |
|------|------|------|------|------|
| A | Ollama GGUF (`qwen3-vl:30b`) | ~20 GB | ~42 tok/s | 省事，一行搞定 |
| B | mlx-vlm 原生 (4bit) | ~18 GB | 更快（无 llama.cpp 中间层） | 推荐，M4 Max 宽裕 |
| C | mlx-vlm 原生 (bf16) | ~62 GB | 最快 | 贴满 64GB 内存，不实用 |

路线 B 是这台机器的 sweet spot：`mlx-community/Qwen3-VL-30B-A3B-Instruct-4bit`。

## 实验性导入

Ollama 的 `--experimental` 导入支持部分 safetensors 架构，但不支持 `Qwen3VLMoeForConditionalGeneration`（MoE + 视觉的复合架构）。

## 最终选型（2026-07-17）

当前方案不动，够用：

| 模型 | 用途 | 引擎 |
|------|------|------|
| `qwen3.6:35b-mlx` | 纯文本 | Ollama MLX |
| `qwen3-vl:2b` | 看图 | Ollama GGUF |
| DeepSeek API | 复杂任务 | 云端 |

如果未来需要提升看图质量，走路线 B：`mlx-vlm` 原生跑 4bit 版。

## 下载纪律（经用户确认，记入 ~/AGENTS.md 约束红线）

禁止私自下载模型文件。下载前必须：
1. 说清楚这是什么模型（厂商、架构、用途）
2. 说清楚为什么要下它（替代什么、解决什么问题）
3. 说清楚大小和影响（多少 GB、占多少内存）
4. 等用户说"好"才动手

---

## 本地 vs 云端对比测试（2026-07-17）

### 测试环境

- 本地：`qwen3.6:35b-mlx` via Ollama MLX（M4 Max 64GB）
- 云端：DeepSeek API（deepseek-chat）
- 测试项：简单问答 / 中等推理 / 复杂推理

### 测试结果

| 测试项 | 本地 tok/s | 云端 tok/s | 本地耗时 | 云端耗时 | 本地回复 | 云端回复 |
|--------|-----------|-----------|---------|---------|---------|---------|
| 简单问答 | 102 tok/s | 28 tok/s | 17.5s | 1.0s | 678 tok | 28 tok |
| 中等推理 | 100 tok/s | 55 tok/s | 27.6s | 10.3s | 2734 tok | 571 tok |
| 复杂推理 | 100 tok/s | 71 tok/s | 27.1s | 14.5s | 2672 tok | 1024 tok |

### 结论

1. **本地模型生成速度更快**（~100 vs ~55 tok/s），但首包延迟高（第一次 10-17 秒加载模型）
2. **本地回复更详细**（回复 token 数约为云端的 2-5 倍）
3. **云端首包延迟低**（1-2s），适合快速对话
4. **质量差异不明显**——简单任务本地足够，复杂任务都可以，云端更简洁
5. **Router 的复杂度检测逻辑成立**——简单/隐私走本地，复杂走云端

### 实践规则

- 本地模型加载后常驻内存，后续请求无额外首包延迟
- 首次请求尽量避免在实时对话中出现，可通过预加载或 keep-alive 缓解
