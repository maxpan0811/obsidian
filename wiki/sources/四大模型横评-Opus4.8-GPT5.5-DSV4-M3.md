---
title: 四大模型横评：Opus 4.8/GPT-5.5/DeepSeek V4/MiniMax M3
type: source
created: 2026-06-08
updated: 2026-06-08
sources: [https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=265372...]
source_path: 印象笔记管理工具/横评Opus 4.8、GPT-5.5、DeepSeek V4、MiniMax M3，356元测出来的真实排名.md
tags: [model-review, benchmark, claude, gpt, deepseek, minimax]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "横评Opus 4.8、GPT-5.5、DeepSeek V4、MiniMax M3，356元测出来的真实排名"
source: evernote
type: note
export_date: 2026-06-26
guid: 46570039-eb0c-497e-a71e-5f660b877de7
---

# 横评Opus 4.8、GPT-5.5、DeepSeek V4、MiniMax M3，356元测出来的真实排名

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwMTU5OTQ1Nw==&mid=265372...](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653727559&idx=1&sn=3df4046ac89ae91395e8ce4c6c59a804&chksm=8ca919f402216b0cb1847f8aca8d54a9d6c40a555b780a55c95b32d5868b66a2c7cd012df968&mpshare=1&scene=24&srcid=06055g2w726kncTmWW0Fdq5d&sharer_shareinfo=72a3b6d5798fee2575ca65311bf180d6&sharer_shareinfo_first=72a3b6d5798fee2575ca65311bf180d6&clicktime=1780738375&enterid=1780738375&ascene=14&devicetype=iOS26.5&version=18004a28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQNj8KeLFFs3VKG/BhLF+/NBLTAQIE97dBBAEAAAAAAGipFInsSWQAAAAOpnltbLcz9gKNyK89dVj0rjD572VZNcMlJ09SZWE+FHFbpQJJLOFoEB+yEbbNPbBSOKh6R+diLyVs19yWmPBs73mF2VKsdcc/KalHr+xkyKwP3e0GgdX6/vaypWLKyz5uU/N7OWU2qBX/cUv1l9kBZWtIgPlymwW6I4qYT3tPxT+uEqppPnOtUMOoUQ6aAKyFtR+fxFHPB6IVk6fxR34nyGAOcBVtUiDKwYE/Q0cbp+EfRhKeI2xbwOy0iP0=&pass_ticket=xzzcrpvcGD+GOjwhBkPg/c4lrRWoG2UUal7q1uxNvXBFHFKPHpqTW34zqPNKiZ40&wx_header=3)

Original冷逸 沃垠AI

大家好，我是冷逸。

最近，模型圈的节奏又加快了。Opus 4.8、GPT-5.5、Qwen3.7-Plus、MiniMax M3，四款重量级模型几乎同时登场，想认真跟一遍都很难。

昨天，我注意到一个榜单叫「Browse Code」，专门测LLM在真实浏览器环境里完成编程和网页自动化任务的成功率。

![](attachments/1ea54070f7ff63ce.png)

没想到，MiniMax M3在这个榜上从M2.7时期的倒数第二直接冲到了全球第五，和Claude 4.6 Sonnet、Gemini 3.5 Flash并排。

当然，一个榜单说明不了全部问题。所以我花了356元，把Claude Opus 4.8、GPT-5.5、DeepSeek-V4-Pro和MiniMax M3这四个模型拉到一起，用同一套任务、同一条提示词、同一个评分标准，全部接API走Claude Code/Codex测了一遍。

覆盖了3D编程、视觉编程、游戏开发、Agent长程任务四大场景，横评结果如下。

![](attachments/5db6f1cc7d61e280.jpg)

一手横评

本次测评的原则是：变量归一，对比才有意义。

四个模型用同一份视觉素材、同一条提示词，分别接各家API在Claude Code / Codex里跑，最终从任务完成度和输出质量两个维度来评价，场景覆盖3D编程、视觉编程（网站开发）、游戏开发和Agent长程任务（Office三件套 + Coding）。

1）3D任务

先给模型看一张金门大桥的实景照片，然后让它根据桥体外观，用Three.js写一个3D交互网页。

![](attachments/ff3604289ef0e3cd.png)

这个任务的考验是三维的：第一，模型要有视觉理解能力，能从图片里提取出关键的结构特征；第二，要能把这些特征准确映射到三维空间的几何关系上；第三，Three.js代码质量要过关，别写出跑起来就崩的东西。

三项能力任缺一项，结果都会差很多。

提示词：
参考“金门大桥.jpeg”的外观构造，帮我开发一个旧金山的金门大桥的3D交互网页，要求如下：
- 使用 Three.js，全部用程序化几何体生成，不加载外部3D模型。
- 桥体主色为国际橙色(#C47832)，塔柱为Art Deco风格，桥体结构高度还原“金门大桥.png”的倒弧形外观结构。
- 准确还原金门大桥标志性的国际橙色桥塔、双塔悬索结构，包含主缆、吊索、桥面和车道分隔线。
- 环境包括：深蓝色波浪海水、天空渐变雾效，远处绿色山丘和城市群。
- 动态：海水浮动、云影移动、支持鼠标拖拽旋转/缩放。
- 性能：全屏自适应，使用Three.jsr128，输出一个可直接运行的HTML文件。
- 支持鼠标拖拽旋转、缩放、平移，初始视角从西南方向俯瞰大桥。

Claude Opus 4.8：

![](attachments/da82b8be681b6aa4.gif)

GPT-5.5：

![](attachments/150dfd5f3b8f04ed.gif)

DeepSeek-V4-Pro：

![](attachments/0338d75413a09edd.gif)

MiniMax M3：

![](attachments/8e0b30d5302dcc65.gif)

这个Case里，毋庸置疑表现最好的是Claude Opus 4.8，MiniMax M3紧随其后。

这两个模型都准确还原了金门大桥最标志性的一个物理细节：主缆从两侧塔顶向跨中垂下来的倒弧形外观。这说明它们不只是在描述一座桥，而是真正理解了悬索桥的结构原理，并能把这个理解翻译成三维几何。

GPT-5.5和DeepSeek-V4-Pro则没有还原出这个特征，输出的桥体五花八门。

尤其是GPT-5.5，它的编程审美怎么描述呢，有种浓眉大眼的感觉，就很粗糙。后面几个Case，它的这个特征会一直持续。Claude和M3的视觉语言则完全相反，一看就很精致、高级，有明确的设计意识。

另外值得一提的是，DeepSeek的海洋流体动效设计得挺有意思，但天空出现了穿模问题，说明三维空间的碰撞逻辑还是处理得不够扎实。

![](attachments/4685abdd32f8c76a.gif)

这轮实测：Claude Opus 4.8 > MiniMax M3 > GPT-5.5 > DeepSeek-V4-Pro。

2）视觉编程（网站开发）

前几天给大家分享了“冷同学的院子”这个民宿概念，这次顺手让模型给它开发一个官网。

我的提示词故意没有给出具体的设计指令，只丢了民宿信息和素材包，让模型自己做判断——哪些素材该用、怎么排版、用什么设计语言。

这其实是在测两件事：一是视觉理解能力，模型能不能“看懂”图片、视频素材的内容和质量；二是设计决策能力，能不能根据品牌调性做出合理的创作取舍。

提示词：
给这家民宿设计一个官方网站。
民宿的基本信息：
- 民宿名称：冷同学的院子
- Slogan：云朵上的院子，冷同学的家
- 地理位置：四川汶川（羌族文化核心区、高山峡谷地带）
- 品牌调性关键词：温暖治愈 · 在地羌韵 · 自然松弛 · 外冷内热 · 有故事感
- 目标客群：追求慢生活的年轻人、亲子家庭、文化旅行者、成都周末度假客、川西旅游爱好者
文件夹【民宿资料包】放着很多民宿的素材，有logo、门店、房间、周边和宣传视频，你自己决定用哪些素材（不是所有素材都用上）。我只需要最终交付的网站顶级审美，让人看了就想马上去玩。

Claude Opus 4.8：

![](attachments/7e7f65aacad33e8e.png)

**（可上下滑动，查看全图）**

GPT-5.5：

![](attachments/22fe7814be0d2723.png)

**（可上下滑动，查看全图）**

DeepSeek-V4-Pro：

![](attachments/ccd896a82f51481d.png)

**（可上下滑动，查看全图）**

MiniMax M3：

这轮表现最好的是MiniMax M3。它确实“看懂”了我的素材和需求，一上来先给我梳理了开发计划。

![](attachments/7fa80da0e4c0a183.png)

然后定义出设计语言：大面积米白留白加克制几何为"冷"，羌红/赭金/暖木色为"热"，再把这两套视觉语言融在一起，做成"外冷内热"的调性表达。审美参考了了Aman侘寂、松赞在地文化和虹夕诺雅的克制感。

![](attachments/e7068f063ec39bba.png)

这就是视觉理解能力和设计品位带来的差距。只靠读文字提示词，是做不到这个程度的。

房型展示那一屏，M3用了左右交错的错位布局来呈现房型和价格，节奏感很好，看完真的有预订的冲动。

![](attachments/d2f63d413a477c07.png)

Opus 4.8也不赖，几处书法字体的运用尤其喜欢，素材选用也很克制，没有全部堆进去。

![](attachments/b88c74fbbe89a509.png)

GPT-5.5继续它“浓眉大眼”的直男审美：大标题、方方正正的排版，完全没有灵活性，是真的很丑。

DeepSeek-V4-Pro的审美比GPT-5.5耐看一点，但它缺乏视觉理解能力，所以根本不知道哪些图该用、用在哪里，索性把所有素材全堆进去，结果图文错乱，部分页面文不对题。这是能力上的硬限制，不是调整提示词能解决的问题。

这轮测试：MiniMax M3 > Claude Opus 4.8 > GPT-5.5 > DeepSeek-V4-Pro。

3）游戏开发

不知道大家在手机上玩过“抓大鹅”没？你可能没玩过，但你的另一半一定玩过。

这次我先跟AI沟通设计了一份PRD，再让模型根据PRD开发一款web端的抓大鹅游戏。

![](attachments/42513ebe60794864.png)

**（可上下滑动，查看全图）**

这个任务的考验点在于：模型能不能完整、准确地读懂设计文档里的功能描述，并把每一条需求准确地转化成可运行的代码，同时把游戏体验和视觉完成度都顾到。

提示词：
请按PRD“大鹅.png”的要求，帮我创建一个网页版《抓大鹅》3D堆叠消除游戏。要求：
1、6种不同颜色/形状的物品，共36个，随机堆叠在3D空间中。
2、鼠标点击物品后消失，图标进入底部7格暂存栏。
3、暂存栏出现3个相同物品时自动消除。
4、暂存栏满7个不同物品时失败，场上物品清空时胜利。
5、提供洗牌、移除、回退三个道具按钮，各3次使用次数。
6、支持鼠标拖拽旋转视角和滚轮缩放。
7、支持localStorage保存进度和复活功能。
8、输出一个完整的html文件，可直接在浏览器运行。

Claude Opus 4.8：

![](attachments/1d227517e43f82a4.gif)

GPT-5.5：

![](attachments/218981af553a56a7.gif)

DeepSeek-V4-Pro：

![](attachments/ae4694493c20ee6f.gif)

MiniMax M3：

![](attachments/75c45be8532f8de0.gif)

四个模型都把游戏开发出来了，核心功能都对，说明面对有明确PRD的开发任务，主流模型基本都能过关了。

有意义的差异集中在两点：一是前端审美，Claude依旧最耐看，DeepSeek和M3也还行，GPT-5.5最丑；二是细节完成度，PRD里有一项要求是“通关后奖励一只大鹅”，只有M3做到了，其他三个模型都漏掉了这个细节。

这轮测试：Claude Opus 4.8 ≈ MiniMax M3 > DeepSeek-V4-Pro > GPT-5.5。

4）Agent长程任务

最后一个Case也是最复杂的：我们让各个模型用Claude Code / Codex做一个联网搜索 + word/PDF生成 + skill调用 + 网站开发的复杂长程任务。

提示词：
联网搜索电影《火遮眼》的关键信息内容，尽量从权威信源获取内容。先给我创建一份2000字的word调研报告（含pdf版）。然后调用guizang-ppt skill生成一份12页的PPT，宣传一下这部电影。

Claude Opus 4.8：

![](attachments/0d46aaf9c2bd77ad.png)

**（可上下滑动，查看全图）**

![](attachments/85ba369e5fd2cc02.gif)

GPT-5.5：

![](attachments/585d5475e8dea5e6.gif)![](attachments/6cccefe9d4bb1291.gif)

DeepSeek-V4-Pro：

![](attachments/6897b3d365324144.gif)![](attachments/4be82d0ce564bb47.gif)

MiniMax M3：

![](attachments/1197a326ca11b392.gif)![](attachments/4318cc94b0555379.gif)

这个任务的难点在于“长”——不只是单步执行，而是要求模型在跨越多个工具调用节点的情况下，始终保持上下文连贯、指令不漂移。这对模型的长程稳定性和工具协调能力要求很高。

先说PPT的完成度：GPT-5.5、Opus 4.8和M3都交付了质量不错的PPT，Claude每页带微动画，GPT-5.5有真实配图（应该是Codex的原因），M3的色彩搭配比较好看。DeepSeek-V4-Pro在这一项差了明显一截，排版、配色和交互都不在同一个水平线上。

调研报告的内容质量：Opus 4.8、M3和GPT-5.5不相上下，DeepSeek-V4-Pro垫底。

关于DeepSeek-V4-Pro有一个独立的问题值得单说：它在Claude Code里跑得极慢，而且频繁中途停摆不再继续输出。这个PPT任务它跑了整整36分钟，期间多次卡顿。

![](attachments/e605321c7156d8cf.png)

大概率是DeepSeek并未针对Claude Code做更多适配导致的，属于工程层面的问题，而不只是模型能力本身的问题。但从用户体验角度来说，这个差异是实实在在存在的。

这轮测试：GPT-5.5 ≈ Claude Opus 4.8 ≈ MiniMax M3 > DeepSeek-V4-Pro。

![](attachments/f6bd94d8eb15c38d.jpg)

实测总结

四轮任务跑下来，先看综合能力，再看成本。

![](attachments/335d5345d6e8eb89.png)

能力上，Claude Opus 4.8是这次横评里综合实力最强的，稳如预期。

M3是最大的惊喜，整体水平大约在Opus 4.7和4.8之间，与Opus 4.8的差距比我预想的要小。

GPT-5.5表现不稳定，有时候在线，有时候掉链子，前端审美上的短板在编程场景里是一个贯穿始终的减分项。

DeepSeek-V4-Pro整体能力不如其他三家，Agent长程任务的稳定性和代码生成质量都有差距。

成本这块，本期测评费用明细：

![](attachments/3223d298d26c15b5.jpg)

- Claude Opus 4.8，接API测的，50美刀；
- GPT-5.5，在Codex里用的，大约2美刀；
- MiniMax M3，我订的Token Plan极速版，每月有12亿额度的M3 Token，这期用了约2000万token，折下来大约2 块钱；
- DeepSeek-V4-Pro，大量输入命中缓存，不到2元。

换算下来总计356元，而两款国产模型加起来不到总费用的零头。性价比这件事，真的越来越不好意思讨论了。

![](attachments/6c5158106a5fe3da.jpg)

写在最后

模型到底行不行，很多时候只有真实用过才知道，benchmark数字只是参考，不是结论。

至少从这几轮Coding任务来看，Claude Opus 4.8的前沿地位还是稳的。MiniMax M3也不差，大概是Opus 4.7的水准，很接近Opus 4.8了。

GPT-5.5可能在办公类任务上更有优势，但Coding层面的审美问题不是小问题，对于编程场景来说是一个明显的硬伤，而且这个问题不是靠调提示词就能解决的。

DeepSeek-V4-Pro性价比依然很高，但这次测评也暴露了它在Agent适配、长程稳定性和代码生成质量上与另外三家的真实差距。差距不是追不上，但需要时间。

说实话，这轮测下来最让我兴奋的是前几天发布的M3。我没想到它能这么接近Opus 4.8。1M上下文+原生多模态+Coding SOTA，配合Token Plan的定价，真的能做很多事情。

我是冷逸，你们的测评手替。如果你有想测的场景，欢迎在评论区甩出来，咱们互相抄作业。

如果觉得本期内容有用的话，欢迎三连支持，感谢。

我们下期见。
