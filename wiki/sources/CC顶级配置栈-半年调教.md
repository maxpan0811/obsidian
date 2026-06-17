---
title: 半年调教出的 Claude Code 顶级配置栈
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzI0NDQ0ODU3MA==&mid=224754...]
source_path: 印象笔记管理工具/别再瞎用Claude了！我花了半年调教出的顶级配置，效率直接降维打击.html
tags: [claude-code, configuration, best-practice, power-user]
---

## 一句话摘要

真正拉开差距的不是 prompt 写得多漂亮，而是 `.claude/` 配置栈有没有搭起来——一个/的 power user 配置目录通常有 CLAUDE.md + rules/ + agents/ + skills/ + settings.json + .mcp.json，每个文件都很短很准很有边界。

## Power User 的 .claude/ 结构

```
.claude/
├── CLAUDE.md
├── rules/              # 路径级行为规则
├── agents/             # 子智能体配置
├── skills/             # 可复用技能
├── settings.json       # 全局设置
└── .mcp.json           # MCP 配置
```

**关键不是文件多，而是每个文件都很短、很准、很有边界。**

## 核心配置理念

### Memory Hierarchy（五层）

1. 个人偏好（`~/.claude/`）
2. 项目根目录 CLAUDE.md
3. 路径级 rules/ 文件
4. 本地未提交覆盖
5. 每个 session 自动写入的 memory

**重点**：CLAUDE.md 每次 session 开始都加载，永久消耗 token。不要把它当 wiki 用——500 tokens 以下最好。

### 配置原则

- 主 memory 文件控制在 500 tokens 以下
- 每个 rules 文件只负责某个路径下的行为
- 每个 subagent 大约三十行
- hooks 只做 pre-tool gate + post-tool formatter
- MCP server 保留 5 个真正有用的，不装 15 个

## 效果对比

| 场景 | 无配置 | 完整配置栈 |
|------|:-----:|:----------:|
| 给 retrieval 加引用生成+评估+PR | 一下午 | **30 分钟** |

## 相关页面

- [[products/Claude Code]]
- [[features/CLAUDE.md与上下文管理]]
- [[features/Hooks]]
- [[features/Subagent]]
- [[sources/CC-Skills审计-8个比30个好]]
- [[sources/Claude Code七层约束-Hook-Skill-CLAUDE]]
