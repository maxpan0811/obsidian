---
title: qwen-vl-agent
type: capture
tags: [auto-capture, project]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


创建了 `qwen-vl-agent` skill，调用本地 Ollama 部署的 qwen3-vl:30b 模型分析图片。

**文件**: `~/.claude/skills/qwen-vl-agent/`
- `SKILL.md` — skill 描述和用法
- `scripts/qwen-vl.sh` — 分析脚本（接受图片路径 + 可选 prompt）

**Why**: DeepSeek 和当前企业网关(ada-cli)都不支持多模态输入（图片），本地 VL 模型补上这个盲区，且数据不出本机。

**How to apply**: 用户拖图片到终端时，或说"/看图""看看这张图""分析截图"时触发。脚本返回三段式输出（RESULT_START / RESULT_END / META）。

**性能**: M4 Max 上 ~19-28s/张（首次加载慢，后续驻留显存更快），~25-87 tok/s

**同题对比**：本地 35B 与 Flash 在业务分析上差距不大（约 80-85%）。当前暂不需要 `/local` 纯文本本地代理——分析质量够但无强隐私需求驱动。

**后续可做**: 批处理功能（遍历目录批量识图）
