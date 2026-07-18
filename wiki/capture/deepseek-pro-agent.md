---
title: deepseek-pro-agent
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## 使用方法

用户说"用 Pro 做 X"时，调用 skill 脚本处理：
```bash
bash ~/.claude/skills/deepseek-pro-agent/scripts/deepseek_pro.sh "<完整prompt>"
```

## 输出格式

模型响应在 `>>>RESULT_START` 和 `>>>RESULT_END` 之间。Token 用量打在 stderr。

## 注意事项

- 复杂分析、金融建模、多因素推理任务适合 Pro
- 简单查询、文件操作、工具调用不需要 Pro
- 用户主动标记模式 — 不说"用Pro"就不走这条路径
