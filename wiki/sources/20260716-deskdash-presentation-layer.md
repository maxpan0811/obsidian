---
name: 20260716-deskdash-presentation-layer
type: source
tags: [dashboard, design-doc, schema, data-viz, html]
source_path: /Users/panbo/Obsidian/程序开发/20260716-桌面看板显示层-design.md
---

[摘要] 本文档是桌面看板显示层的完整设计文档。从 Übersicht 桌面 widget 方案转向自包含 HTML 页面 + 浏览器方案，原因是 Übersicht CoffeeScript 编译/设置反复踩坑且 widget 未显示。采用三层解耦架构：分析层（各 skill 按自己口径算指标、吐 schema JSON）、显示层（桌面看板 skill，V 层，不碰任何口径）、数据层（JSON 文件）。核心是 schema 契约——每个 view JSON 自描述 view_id/title/source/row_labels/col_labels/metrics/periods 等字段，显示层只认此格式。脱敏设计采用 --mask 模式，sensitive 指标整列从内联 DATA 里剔除（不是隐藏显示，源码里也没有）。大区口径采用混合口径：欧洲用目的地国家_归属业务区域 EU5，非欧洲用考核区域排目的地参团。六大区省份清单（华北15省、华东5省、华西4省等）固化在产品市占率分析工具，export 脚本 import 复用。设计涵盖产品市占率和渠道市占率两个 view，后者预留框架。HTML 交互包括内容切换 tab、时间切换（月/季/半年）、涨红跌绿、脱敏渲染。原文链接：/Users/panbo/Obsidian/程序开发/20260716-桌面看板显示层-design.md