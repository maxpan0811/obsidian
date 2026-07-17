---
title: Anthropic 黑客松冠军项目 Everything Claude Code 完整上手攻略
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Anthropic 黑客松冠军项目 Everything Claude Code 完整上手攻略.md
tags: [印象笔记]
---


Anthropic 黑客松冠军项目 Everything Claude Code 完整上手攻略
===============================================

Original兔兔AGI 技术极简主义

 

**Everything Claude Code** 是由 Anthropic 黑客松冠军 Affaan Mustafa 创建的开源项目，提供了一套较为完整的 Claude Code 配置体系。其核心思路不是把 Claude Code 当作单一的编程工具，而是将其配置成一个由不同角色组成的「虚拟开发团队」。

这些配置来自作者超过 10 个月的高强度日常使用，并在真实产品开发中反复打磨和验证，核心包括 Agents、Hooks、Rules、Commands 和 Skills，用于支持任务拆解、代码审查、安全检查以及 TDD 等开发流程。

本文将重点对比该方案与基础 Claude Code 用法的差异，并梳理其整体架构及实际价值。

什么是 Everything Claude Code？
---------------------------



<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->