---
title: auto-monitor-long-running-tasks
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# 终端长时间任务自动监测

**Why:** 2026-07-14 FAISS 构建跑了 34 小时，多次崩溃、内存泄漏、Swap 满，均是被动等用户发现。Claude 应主动监测和处理。

**How to apply:** 任何 `nohup`/`run_in_background` 超过 3 分钟的任务，每轮对话必查。

## 监测清单

| 指标 | 命令 | 正常 | 警告 | 危险 |
|------|------|------|------|------|
| 进程 RSS | `ps aux \| grep` | < 2GB | 2-5GB | > 5GB |
| 系统 Swap | `sysctl vm.swapusage` | < 1GB | 1-3GB | > 3GB |
| CPU 使用率 | `ps aux \| grep` | > 3% | 1-3% | < 1% (卡死) |
| 日志新鲜度 | `ls -lt` | < 2min | 2-5min | > 5min ⚠️ |
| 速率偏差 | 对比预期 | > 50% | 20-50% | < 20% |
| 风扇/温度 | 用户反馈 | 正常 | 稍响 | 异常响 |
| 进程存活 | `ps aux \| grep` | 存在 | — | 不存在 (已崩) |

## 检查频率

- 每 5 分钟主动检查一次全量指标
- 用户问"现在怎么样"时，先自查再回复
- 发现异常立即告警，不等用户问

## 异常处理

| 异常 | 处理 |
|------|------|
| RSS > 5GB | 检查是否有内存泄漏，考虑 kill 重启 |
| Swap > 3GB | 减少并行进程数，kill 旧残留进程 |
| 日志 > 5min 未更新 | 进程可能卡死，检查 CPU 和 Ollama 状态 |
| 速率 < 预期 20% | 检查 Swap 是否拖慢，Ollama 是否正常 |
| 进程已死 | 检查日志错误原因，修复后重启 |
