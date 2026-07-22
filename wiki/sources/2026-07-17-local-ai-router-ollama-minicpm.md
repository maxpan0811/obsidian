---
name: 2026-07-17-local-ai-router-ollama-minicpm
type: source
tags: [ollama, ai-router, minicpm-v, deepseek, multi-modal]
source_path: /Users/panbo/Obsidian/程序开发/2026-07-17-本地AI路由Ollama-minicpm-v搭建笔记.md
---

[摘要] 本文档记录了本地 AI Router 的搭建过程。目标：搭建一个本地多模态模型弥补 DeepSeek 不能看图的缺陷，同时开发路由脚本自动判断输入类型（含图片→本地模型，纯文本→DeepSeek API）。硬件为 MacBook Pro M4 Max 64GB 统一内存。最终技术方案：本地引擎使用 Ollama 0.31.1（Flash Attention + Q8_0 KV Cache），本地模型 minicpm-v:8b（5.5GB，面壁智能出品，中文友好），云端使用 DeepSeek API，路由脚本为 Python `~/Project/ai-router/router.py`，支持交互模式和单次模式。网络加速方面，Ollama CDN 国内直连 15-19 MB/s，VPN 下反而慢（3-5 MB/s）；HuggingFace 必须 VPN 才能下载。mlx-vlm 0.6.4 的兼容性有限，只原生支持 Gemma 系列，Qwen2.5-VL 等新品 VL 模型的图片预处理不完整导致识别失效。经验要点：先问再动手、Ollama 是国内最佳入口、VPN 策略区分使用、M4 Max 64GB 绰绰有余。原文链接：/Users/panbo/Obsidian/程序开发/2026-07-17-本地AI路由Ollama-minicpm-v搭建笔记.md