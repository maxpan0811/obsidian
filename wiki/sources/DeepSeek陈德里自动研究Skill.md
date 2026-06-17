---
title: DeepSeek陈德里开发自动研究Skill
type: source
created: 2026-05-29
updated: 2026-05-29
sources: [DeepSeek陈德里开发自动研究Skill，写一篇论文人类只动脑2小时.html]
source_path: 印象笔记管理工具/DeepSeek陈德里开发自动研究Skill，写一篇论文人类只动脑2小时.html
tags: [ai, agent, research, deepseek, autonomy]
---

# DeepSeek陈德里开发自动研究Skill

> 来源：量子位
> 原文链接：微信公众号

## 一句话
DeepSeek研究员陈德里用自研AutoResearch Agent写了篇46页论文，他本人只花了不到2小时的"脑力CPU时间"。

## 关键信息

### L1-L5 自主度分级体系
类比自动驾驶SAE分级，定义AI Agent的5级自主度：

| 级别 | 名称 | 代表 | 说明 |
|:----:|------|------|------|
| L1 | 自动补全 | GitHub Copilot | 预测下一行代码 |
| L2 | 任务执行 | ChatGPT/Claude+工具 | 分解任务但每步需人类批准 |
| L3 | 多步骤执行 | Claude Code, Cursor Agent | 10-100步自主，关键点请求审核 |
| L4 | 受限全自主 | 当前最前沿 | 给定目标完成实验/代码/论文，不自主选题 |
| L5 | 完全自定研究议程 | 未实现 | 自主选题、分配资源、长期积累知识 |

### 4种智能体架构模式
1. **单智能体循环**（ReAct/Reflexion/LATS）— 简单高效，复杂任务有限
2. **多智能体协作**（CAMEL/AutoGen/MetaGPT）— 分工多视角，成本高
3. **分层调度**（Claude Code/Devin）— 长时程复杂研究
4. **工具增强执行**（SWE-Agent）— 能力由工具边界决定

### 论文产出
- L1-L5框架 + 17个主流系统六维特征矩阵分析
- 6大开放问题：认知循环陷阱、上下文限制、创新性评估、可复现性、安全伦理、成本
- 实际应用采用混合架构

## 相关页面

- [[concepts/LLM Wiki模式]]
- [[sources/Claude Code教程-九-完结篇]]
