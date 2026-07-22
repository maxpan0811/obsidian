---
name: piliang-tupian-chongmingming-gongju-youhua-jilu
type: source
tags: [图片重命名, qwen3-vl, Ollama, 命名工具, 性能优化]
source_path: /Users/panbo/Obsidian/程序开发/批量图片重命名工具优化记录.md
---

[摘要]
文件命名工具下新增rename_images.py的优化记录，用本地qwen3-vl:30b批量分析图片内容并自动命名。从最初77张40分钟优化到67张10分钟。

关键发现：qwen3-vl:30b是MoE架构（31.1B总参，实际激活约3B），非稠密30B。M4 Max 64G推理速度88.5 tok/s，小图全流程仅15s。不需要补轻量副驾模型。

加速三板斧：ThreadPoolExecutor并发4（约2.4倍加速，Ollama共享权重）、大图sips缩放（1MB+缩到2248px短边，约30%提速）、Checkpoint+mapping（断点秒续跑）。

实战踩坑6个：两个batch同时跑撞车（8进程抢同一模型，单张15s拖至40-180s）、后台输出被缓冲（需PYTHONBUFFERED=1）、已命名文件被重复改名（需ALREADY_NAMED_PATTERN正则跳过）、Checkpoint mapping存反（old→new）、文件列表锁定后源文件消失（try/except FileNotFoundError）、qwen3-vl:14b标签不存在（Ollama registry只有30b版本）。

三批实测数据：第1批71张JPG 16m55s（平均14.3s，cold启动）、第2批67张PNG 10m36s（平均9.5s，warm）、第3批42张mixed 7m7s（平均10.2s，含旧名跳过），成功率100%。

原文链接: /Users/panbo/Obsidian/程序开发/批量图片重命名工具优化记录.md