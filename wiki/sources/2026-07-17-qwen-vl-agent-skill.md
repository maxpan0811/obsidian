---
name: 2026-07-17-qwen-vl-agent-skill
type: source
tags: [qwen-vl-agent, multi-modal, ollama, skill]
source_path: /Users/panbo/Obsidian/程序开发/2026-07-17-Qwen-VL-Agent本地图片分析Skill搭建.md
---

[摘要] 本文档记录了 Qwen-VL Agent 本地图片分析 Skill 的搭建过程。背景：Claude Code 后端通过企业网关走 DeepSeek V4-Flash，不支持多模态输入（图片）。本机已有 Ollama 部署了 qwen3-vl:30b 模型（19GB），可补上此盲区。创建了 `/看图` skill，目录 `~/.claude/skills/qwen-vl-agent/`，包含 SKILL.md 和 scripts/qwen-vl.sh 分析脚本。支持 png/jpg/jpeg/webp/gif/bmp/tiff 格式，单图限制 20MB，默认 prompt 为"这张图片里有什么？请用中文详细描述。"支持自定义 prompt。输出结构为三段式 MARKER 格式。测试结果：首次调用（模型加载）27.8s，第二次调用（已驻留显存）19.7s，87.2 tok/s。同时进行了本地 qwen3.6:35b-mlx 与 Flash 的同题对比测试，本地模型在文本分析/数据解读方面约达 Flash 80-85% 水平，但编程和长链推理较弱。结论：无强隐私需求驱动的前提下，暂不构建 `/local` 纯文本本地代理。原文链接：/Users/panbo/Obsidian/程序开发/2026-07-17-Qwen-VL-Agent本地图片分析Skill搭建.md