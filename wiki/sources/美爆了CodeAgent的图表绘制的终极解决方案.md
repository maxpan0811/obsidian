---
title: 美爆了！Code Agent的图表绘制的终极解决方案
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/美爆了！Code Agent的图表绘制的终极解决方案.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---


title: "美爆了！Code Agent的图表绘制的终极解决方案"
source: evernote
type: note
export_date: 2026-06-26
guid: 9e35dfba-ecba-4f96-9710-7a232a691006
---

# 美爆了！Code Agent的图表绘制的终极解决方案

来源：[打开原文](https://mp.weixin.qq.com/s/gb_Bprf0kz29TsBb1J7VAw)

一图胜千言，使用图表可以非常清晰地展示代码逻辑架构以及各种流转的状态。但在有AI之前，画架构图这类东西，真的是一件非常麻烦的事情。

打开 Visio 或者 draw.io，拖半小时方块和箭头，改一个字段名又要重新拖。这种工具和 AI agent 的工作流完全不兼容，一个靠鼠标，一个靠文本。

Mermaid 是这个矛盾的解法。

它是一套纯文本语法，用来描述图表结构，然后由工具渲染成图。不用再拿着鼠标去描图了，直接用AI来写文本的描述就可以。

以一张前后端分离时序图为例，文本内容如下：

sequenceDiagram

前端->>后

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->