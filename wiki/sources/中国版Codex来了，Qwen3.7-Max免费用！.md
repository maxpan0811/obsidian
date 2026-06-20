---
title: 中国版Codex来了，Qwen3.7-Max免费用！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/中国版Codex来了，Qwen3.7-Max免费用！.html
tags: [AI技术, 科技产业]
---

# 中国版Codex来了，Qwen3.7-Max免费用！

原文链接: https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=265372...

Original冷逸 沃垠AI 
大家好，我是冷逸。
最近AI圈最火的Agent产品，非Codex莫属。
那玩意好用是好用，但它只能用GPT模型，而且需要魔法。GPT-5.5这模型怎么说呢？在Agent编程上，它的上下文管理、自主规划能力和复杂任务能力确实很强。但审美是真的一言难尽，就总给人一种“浓眉大眼”的感觉。
毕竟Sam Altman自己都说过，“GPT-5.5 IQ很强，但不如Claude有品味”。让GPT-5.5写个网页，一眼看过去全是SaaS模板味，太理工思维了。
作为见惯了Claude、Kimi、Qwen、GLM、MiniMax前端审美的人，看到GPT-5.5出的页面，是真的会被丑哭。
怎么办？直到我遇到了Qoder Desktop。
跟Codex一样，它的核心也是Quest控制台驱动。你把需求往里一扔，比如“帮我实现一个用户登录功能”，剩下的拆解、分工、编码、测试，背后的单Agent或Experts专家团自己搞定，你回来验收成果就行。
而且，Qwen3.7-max、M3、K2.6、DeepSeek-V4这些最新的主力模型，它都支持。更重要的是，还支持接第三方Coding Plan，不消耗Credits。
如果你用Qwen3.7-Max的话，每天有200次的免费额度。
最关键是，这是中国团队做出来的Codex级产品，不用魔法，所有人都能用。
下面，我带大家沉浸式体验一下。
一手体验
0）前置准备
首先，前往 qoder.com/desktop，下载安装「Qoder Desktop」。
注意别选错了，不是Qoder Work，也不是Qoder Wake。macOS、Windows、Linux均支持，也有手机APP，可以从手机端遥控桌面Qoder。
安装完先看界面。
典型三栏布局：Quest任务管理区、Chat会话区、产物功能面板。功能面板里有任务概要、pwsh执行终端和产物预览窗口，设计很清晰。
这里顺便科普一下「Quest」这个概念，这是Qoder整个产品逻辑的核心设计，也是它区别于普通AI工具的地方。
普通AI Chat是单次任务委派（Task Delegation），一问一答，完成就散，没有任何状态延续。Quest不一样，它是一个Agent-First的开发工作台，涵盖任务委派、状态追踪、产物审查等全流程环节，端到端把任务跑完。
工作模式分两种：单Agent处理日常任务，Experts专家团处理复杂全栈开发。你只需描述目标，AI从需求澄清到产物交付，全程在统一的任务界面里推进，中间的执行细节你不需要操心。

...核心理念是「Define the goal. Review the result」，设立目标，交付结果。
来重点看一下Chat会话区的几个配置项，有几个地方很值得聊：
工作文件夹：建议每次任务单独选一个文件夹，这样Qoder只在这个范围内动，不会污染你其他的项目，也方便事后归档和版本管理。
工作模式：单Agent适合日常任务，Experts适合全栈开发和复杂任务（需要自己配置Sub-Agent，下面专门讲）。
模型选择：Qwen、MiniMax、GLM、Kimi、DeepSeek等都能自由选，不锁死在某一家，这点很关键。
还有一个Spec驱动模式，勾选之后，每次执行任务前会先跟你对齐需求、生成结构化Spec，由你审核确认后再执行。这不是「即兴编程」，而是正经的「需求澄清→执行→验
