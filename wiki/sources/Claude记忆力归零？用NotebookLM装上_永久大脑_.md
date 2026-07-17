---
title: Claude记忆力归零？用NotebookLM装上_永久大脑_
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Claude记忆力归零？用NotebookLM装上_永久大脑_.md
tags: [evernote, impression, yinxiang]
---


每次你打开Claude新对话，你们的"关系"就清零了。

你花了三天跟它讨论的商业策略、你的用户画像、你的品牌调性——全部不见了。你得重新"介绍自己"，重新塞入上下文，然后看着token余额哗哗往下掉。

这不是偶发bug，这是Claude的底层设计决定的——**会话记忆天然短暂**。

Jack Roberts，一个曾把自己的科技创业公司卖出去、积累超过6万付费用户的连续创业者，最近分享了他的解法：**把Google NotebookLM接入Claude，构建一套几乎零token成本的长期记忆系统。**

这个方案的核心很反直觉：不是把更多信息塞进Claude的上下文窗口，而是让Claude"知道去哪里找答案"。

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/94D1A8DA-9E33-4CBF-B523-3207F17A615C.png)

一、Claude的失忆症：每次对话都是从零开始
-----------------------

先把问题说清楚，才能理解解法的价值。

Claude的记忆机制分两种：*

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->