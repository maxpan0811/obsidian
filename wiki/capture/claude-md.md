---
title: claude-md
type: capture
tags: [auto-capture, feedback]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


每完成一个项目，最后一步加 CLAUDE.md。

**内容要点：**
- 项目概述（一句话）
- 常用命令（dev/build/test/lint）
- 环境变量说明
- 架构决策（为什么这么设计，不做什么）
- 目录结构概览

**Why:** 让下次进项目的会话能快速进入状态，不用从零摸索。也是成本最低的"跨会话长期记忆"。

**How to apply:** 项目交付前，作为收尾步骤写入项目根目录的 CLAUDE.md。
