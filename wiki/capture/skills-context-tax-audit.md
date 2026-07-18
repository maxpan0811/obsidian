---
title: skills-context-tax-audit
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


## Skills Context Tax 的核心量化框架

每个已安装 skill 的 description 都会在每一轮对话中占据 context window。Anthropic 官方为 skill descriptions 分配的预算上限是 **1% 的 context budget**（约 1536 chars 每条），一旦超过 8-12 个，成本开始显著显现。

**两个可量化的代价：**
- **延迟**：模型在触发前需要"读完一小本工具说明书"，30 个 skills = 30% context 被无关描述占用
- **准确率**：模型被无关选项分散注意力——让它格式化 markdown，它可能同时考虑要不要调数据库迁移 skill

**两层权衡（Skills-first, MCP-second）：**
- **Skills** 处理 thinking layer（理解系统、架构模式），context tax 较低（仅 description）
- **MCP servers** 处理 doing layer（实时数据、外部 API），但每次加载完整 JSON schema，可能一次吞掉 50K tokens
- 原则：本地 skill 能解决的就用 skill，不够时再用 MCP

## 每月 Audit Checklist（每 30 天跑一次）

对 `.claude/skills/` 下每个 skill 问四个问题：

1. **过去 30 天触发过吗？** → 否就删。以后还能重装。不为不用的工具付 context tax。
2. **description 跟另一个 skill 抢同样的触发短语？** → 合并或砍掉弱的。否则模型会浪费 tokens 在它们之间做选择，甚至幻觉出混合体。
3. **这件事能不能只是一条 CLAUDE.md 规则（one-shot prompt）？** → Skills 执行逻辑和串联工具；Prompts 设定规则。不是所有重复需求都需要做成 skill。
4. **安装体积配得上它占用的 token 吗？** → 需要 Python 脚本 + 密集 YAML 配置的大型 skill 应能省下小时级的工作量；只包一条 bash 的不如手动输入。

## 高级 vs 初级使用模式

| 维度 | 初级 | 高级 |
|------|------|------|
| 安装策略 | 看到推荐就装，积累到 30+ | 8-12 个经过审计的 skills |
| skill-creator | 不用 | 用来合并重叠 skills、优化 description 触发精度 |
| 设计方向 | 接受 AI 默认审美（中性色/Inter/浅灰） | 用 theme-factory + frontend-design 锁定设计 token |
| 安全 | 发版后等客户发现漏洞 | 合并前跑 /security-review（Semgrep 抓 80% 模式化漏洞） |
| MCP 策略 | 开源 registry 全装，先吞 50K tokens | skills-first，用 mcp-builder 按需构建小专用 server |

## 关键认知转变

- Context tax 是**每轮对话都在支付的持续成本**，不是一次性安装开销
- "装着备用" 不是免费策略——未触发的 skills 仍然在每轮消耗 context budget
- Audit 的输出不是"这份名单"，而是**这个检查框架本身**——每 30 天跑一次

**How to apply:**
- 列出 `/Users/panbo/.claude/skills/` 当前所有 skills，逐条按 audit checklist 检查
- 合并 description 重叠的 skills
- 把简单的规则型需求写进 CLAUDE.md 而非做成 skill
- 每月初跑一次审计，清理死重
