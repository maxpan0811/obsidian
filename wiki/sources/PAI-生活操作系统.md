---
title: PAI - Personal AI Infrastructure（生活操作系统）
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzkwMzY1Mjg5MQ==&mid=224748...]
source_path: 印象笔记管理工具/PAI：把 Claude Code 改造成你的生活操作系统.html
tags: [claude-code, pai, personal-ai, life-os, infrastructure]
---

## 一句话摘要

PAI（Personal AI Infrastructure）v5.0.0 / 13.4K Star，8 个月从 0 到万 Star——目前最激进的「AI 驱动个人操作系统」实验，把 Claude Code 从编程工具升级为生活操作系统。

## 三层架构

| 层 | 组件 | 职责 |
|---|------|------|
| **PAI 本体** | ~/.claude/ | 操作系统内核：技能系统、记忆系统、执行算法、身份文件 |
| **Pulse** | 守护进程 (port 31337) | 生命仪表盘：语音通知、Hook 执行、定时任务、可观测性 |
| **DA（Digital Assistant）** | 有名字的数字助手 | AI 围绕你运转的接口层 |

## 定位

作者 Daniel Miessler（安全领域老兵），此前做过 Fabric（AI 提示词模式集合）。Fabric 解决的是「问 AI 什么」，PAI 解决的是「AI 怎么围绕你运转」。

> AI 应该放大每一个人，而不只是前 1%。

## 相关页面

- [[products/Claude Code]]
- [[sources/Everything Claude Code完整上手攻略]]
- [[sources/Superpowers-14个技能拆解]]
