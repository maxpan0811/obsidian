---
title: reference_claude_memory_dreams_conway
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


# Claude Memory Files / Dreams / Conway 功能对标

来源：TestingCatalog 爆料（2026年6月），Anthropic 正在测试的新功能，
本质上与 OpenClaw/NanoClaw 龙虾体系同源同宗。

## Memory Files（文件记忆）

- 替代原来一条滚动摘要的「经典记忆」模式
- 按话题/项目自动编写结构化文档，未来对话按需检索而非全量灌入
- 容量无上限，精度大幅提升（聊代码只读技术文档，聊旅行只读出行偏好）
- 用户可像编辑 Wiki 一样浏览/修改/删除
- **对标龙虾：[[reference_openspace|byterover]]** — 结构化项目知识库，跨会话持久上下文

## Dreams（梦境）

- 异步后台记忆整合机制，灵感来自人类 REM 睡眠
- 自动合并重复项、替换过时条目、解决逻辑矛盾、挖掘隐藏模式
- 触发条件：累积 5 次对话或距离上次整合超过 24 小时
- Claude Code 中已有 `/dream` 命令
- 实战效果：Netflix 等首批企业首次处理错误率暴降 97%，文档验证提速 30%
- **对标龙虾：[[skills-audit-backup|capability-evolver]]** — 自进化引擎，自动优化行为

## Conway（永不下线 Agent 平台）

- 独立运行时环境（搜索/对话/系统三功能区）
- 常驻后台，监听 Webhook、操控浏览器、运行 Claude Code
- 支持 CNW ZIP 自定义扩展包格式
- 跑在 Anthropic 托管云上，安全 vs 自由的取舍
- **对标龙虾：OpenClaw/NanoClaw** — 7x24 常驻后台，clawhub install 装技能 = 装 APP
- 安全对比：OpenClaw 被发现 9 个 CVE + 4.2 万暴露实例，Conway 云托管安全性更好但锁在生态里

## 值得关注的差异

1. Anthropic 做消费级原生功能，龙虾体系需自行维护基础设施
2. Conway 的安全模型（托管云 + 显式安装 + 逐服务 Webhook 开关）是龙虾的软肋
3. 但「龙虾先行，大厂跟上」——说明龙虾架构思路正确

## 原文提及对 OpenClaw 的认可

> 「OpenClaw、Hermes 这些长时运行的 AI 智能体，早就在用类似的架构。」
