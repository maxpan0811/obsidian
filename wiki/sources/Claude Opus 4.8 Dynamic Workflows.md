---
title: Claude Opus 4.8上线：Dynamic Workflows+650亿美元融资
type: source
created: 2026-05-29
updated: 2026-05-29
sources: [刚刚，Claude Opus 4.8 上线，张口就说自己是 DeepSeek、Qwen.html]
source_path: 印象笔记管理工具/刚刚，Claude Opus 4.8 上线，张口就说自己是 DeepSeek、Qwen.html
tags: [anthropic, claude, opus, funding, dynamic-workflows]
---

# Claude Opus 4.8 上线

> 来源：APPSO

## 一句话
Anthropic发布Claude Opus 4.8（编码/推理/Agent全面提升）+ Dynamic Workflows多Agent协作+650亿美元H轮融资（估值9650亿）。

## 关键更新

### Claude Opus 4.8
- 编码、Agent任务、推理、知识工作全面改进
- 诚实性提升：代码缺陷未经说明通过率降至前代的**1/4**
- 被发现自称DeepSeek/Qwen（疑似蒸馏痕迹，客户端难以复现）
- 价格不变：$5/M input token, $25/M output token

### Effort Control（思考强度调节）
- high/extra/max 三级，决定Claude投入多少推理算力
- Claude Code中对应xhigh，超长时间异步任务用max

### Dynamic Workflows（动态工作流）
- Claude根据任务动态编写编排脚本，并行运行数十到数百个subagents
- 典型场景：代码迁移/安全审计/性能优化/框架替换/多角度验证
- 演示案例：Bun从Zig迁移到Rust → 75万行Rust代码 + 99.8%测试通过率 + 11天
- 支持CLI/Desktop/VS Code Extension，Max/Team/Enterprise

### H轮融资（650亿美元，估值9650亿）
- 领投：Altimeter Capital / Dragoneer / Greenoaks / Sequoia Capital
- 算力协议：AWS 5GW + Google/Broadcom 5GW TPU + SpaceX Colossus GPU
- Claude首个同时进入AWS/GCP/Azure三大云的前沿模型

### 后续
- Messages API支持system entries运行时更新
- Claude Mythos（比Opus更高水平）数周内面向所有客户

## 相关页面

- [[sources/Claude永久大脑双模记忆Conway]]
- [[sources/拆解Anthropic]]
- [[products/Claude Code]]
