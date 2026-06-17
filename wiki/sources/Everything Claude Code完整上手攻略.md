---
title: Everything Claude Code 完整上手攻略
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?chksm=a6de8a9891a9038eaf3280c46d69fef...]
source_path: 印象笔记管理工具/Anthropic 黑客松冠军项目 Everything Claude Code 完整上手攻略.html
tags: [claude-code, agents, hooks, skills, workflow, hackerthon]
---

## 一句话摘要

Anthropic 黑客松冠军项目，提供一套完整的 Claude Code 配置体系——**不是把 Claude Code 当编程工具，而是配置成一个由不同角色组成的「虚拟开发团队」**。

## 项目信息

- **作者**: Affaan Mustafa
- **GitHub**: `everything-claude-code`
- **战绩**: 2025年 Anthropic x Forum Ventures 黑客松冠军（8小时搭建 zenith.chat）
- **来源**: 超过 10 个月高强度日常使用打磨

## 核心组件

| 组件 | 说明 |
|------|------|
| **Agents** | 按角色划分的子智能体（规划/架构/TDD/代码审查/安全/构建错误解决等） |
| **Skills** | 封装工作流和领域经验（编码规范/后端模式/前端模式/TDD/安全审查） |
| **Hooks** | 根据触发条件自动执行流程 |
| **Commands** | 快速执行的斜杠指令 |
| **Rules** | 始终生效的开发规范和约束 |
| **MCP Configs** | 连接到外部服务的配置 |

## 智能体分工体系

```
主会话（协调器）
  ├── 规划智能体（架构决策）
  ├── 代码审查智能体（质量检查）
  ├── TDD 指导智能体（测试实现）
  ├── 安全审查智能体（漏洞扫描）
  └── 构建错误解决智能体（调试）
```

每个智能体只做一件事，主会话只负责协调——输出更稳定，更接近真实团队的协作方式。

## 黑客松实测数据

| 指标 | 使用前 | 使用后 | 提升 |
|------|:-----:|:-----:|:----:|
| 功能完成速度 | 基线 | +65% | 🟢 |
| PR 平均问题数 | 12.3 | 3.1 | -75% |
| 测试覆盖率 | 48% | 82% | +34% |
| 会话切换次数 | 23次 | 7次 | -70% |

## 解决的问题

1. **上下文腐化**：长会话导致上下文信息逐渐失真
2. **代码质量不一致**：缺乏统一规范
3. **重复说明成本高**：项目背景和约定需要反复说明

## 相关页面

- [[products/Claude Code]]
- [[features/Skills]]
- [[features/Hooks]]
- [[features/Subagent]]
- [[sources/claude-code-best-practice-工作流指南]]
- [[sources/Claude Code十大必装MCP推荐]]
