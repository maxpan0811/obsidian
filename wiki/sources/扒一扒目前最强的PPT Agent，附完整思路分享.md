---
title: 扒一扒目前最强的PPT Agent，附完整思路分享
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/扒一扒目前最强的PPT Agent，附完整思路分享.md
tags: [evernote, impression, yinxiang]
---

# 扒一扒目前最强的PPT Agent，附完整思路分享

---

原文链接: [https://mp.weixin.qq.com/s?chksm=fad356f0cda4dfe6bf731ad9ffb95ad...](https://mp.weixin.qq.com/s?chksm=fad356f0cda4dfe6bf731ad9ffb95ad66fe30f76e89f9144102fa592a73d52cc86b6981fede9&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1774701403_3&req_id=1774701678605167&scene=169&mid=2247551655&sn=01dc1de92f599099df135d8d8b38a827&idx=1&__biz=MzUzODg3MzE0NA==&sessionid=1774700038&subscene=200&clicktime=1774703692&enterid=1774703692&flutter_pos=74&biz_enter_id=5&jumppath=20020_1774703613642,20020_1774703625225,20020_1774703660118,1104_1774703662205&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004627&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQXaRgaSFku5/b2Xcazd9EihLTAQIE97dBBAEAAAAAABRiNJz5HMcAAAAOpnltbLcz9gKNyK89dVj07YDhFySqvmi1880fIlos1WZfp6nANs8C54XMi+cyXngvPT1FRVn9sybJnC7T7uo1axgqrydJ5gNgEMnM5hCr7JjkqKhcNBewlZW9pbhkX8uWrNr1oUDN1e4oGNtT2Z2lNS5BNvJsNeUe9P5iu43rADlbNasHj43gm94Nz3B/f7wiuYhSr+/gwucJO4n3ckLrrsZpMYGLG505MF6/osJeJRMwJeJN+tDxl0jfzKA=&pass_ticket=S7a23HrJbvtJomxg1rcExK7V1zPhJ/Mo+/V7b3Ezuxc1bJIf5B3OtQy9UumMnvmL&wx_header=3)

扒一扒目前最强的PPT Agent，附完整思路分享
=========================

Original三顿三顿

三顿的PPT Agent上线后，很多小伙伴好奇它背后的运行机制。我就想写篇文章和大家聊聊。  
有些小伙伴可能还没用过三顿的Agent，简单分享一些目前我们能生成的效果。  
![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/4F96CE7C-A164-4528-89AA-D386782C61C7.jpg)![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/FBD1FD42-86B7-4FA5-B293-87282739B31C.png)![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/2D9F0057-A4D5-477B-A919-C37F511EE93D.png)  
可以搞定各种风格的设计：  
![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/9868ABF2-34B2-4D16-B183-D29050320DF5.png)![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/AA14E420-6FC7-44AB-B33B-74F769EB9F34.png)

你可能会想，这不就是又一个AI PPT玩具吗？

不。你只需要给它一个主题，比如“Dify企业介绍”，然后就可以去泡杯咖啡了。它会像一个真正的专家团队那样，自己跑完从**需求调研 → 资料搜集 → 大纲策划 → 生成策划稿 → 生成设计稿**的全流程。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/1819B3DF-7F11-4439-82C7-F4F2BA33A07F.gif)  
最后做出这样一套完整的设计：  
![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/51ACED9D-9540-4DB5-9847-AFE59AB436C7.gif)

目前已经正式上线，大家可以直接访问下面的网址使用体验。

https://sandun.cc

我可以非常自信地说，这绝对是一个你从未见过的PPT Agent思路。接下来的内容，希望能对你有所启发。

> 1.从“提问”开始

市面上几乎所有的AI PPT工具，都犯了一个致命的错误。

你一输入主题，它就猴急地给你丢出一个粗糙大纲，然后用一堆现成的模板糊弄你，恨不得马上把花里胡哨的设计怼到你脸上。

但说真的，PPT的灵魂是内容，不是皮囊。

想想我们自己做PPT的流程：是不是得先搞清楚“为谁做？做什么？达到什么目的？”

所以，我们让AI做的第一件事，就是**像一个专业顾问一样去“需求调研”** 。它会先去网上扒一圈相关资料，然后像模像样地问你几个关键问题，让你把真正的需求说清楚。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/500198D9-6BC2-423C-877A-513E2D2EA329.png)

只有当我们把需求聊透了，它才会结合搜集到的资料，去生成一份真正“有的放矢”的大纲。

聊到大纲，我又把我用了多年的一个“笨方法”教给了AI——**便利贴法**。

过去我做复杂PPT时，会把每一页的核心内容写在一张张便利贴上，贴满一墙。这样逻辑结构一目了然，哪里不好就撕掉，顺序不对就调换，高效又直观。

现在，我们把它做进了产品里。**每一个页面，就是一张“数字便利贴”**，让你看得清清楚楚，调得明明白白。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/416EBF2E-A476-42D7-9C80-BFEEFD9DB267.gif)

这个思路，你完全可以自己复现。在你动工前，先别急着打开PPT软件，试试把你的需求完整地告诉AI，让它扮演你的“PPT规划师”。

下面这个我们项目在用的正式版Prompt，也**直接开源**给你，让你也能拥有一个顶级的“PPT结构架构师”：

  

```
# Role: 顶级的PPT结构架构师

## Profile

- 版本：2.0 (Context-Aware)

- 专业：PPT逻辑结构设计

- 特长：运用金字塔原理，结合**背景调研信息**构建清晰的演示逻辑

## Goals

基于用户提供的 **PPT主题** 和 **背景调研信息 (Context)**，设计一份逻辑严密、层次清晰的PPT大纲。

## Core Methodology: 金字塔原理

1. 结论先行：每个部分以核心观点开篇

2. 以上统下：上层观点是下层内容的总结

3. 归类分组：同一层级的内容属于同一逻辑范畴

4. 逻辑递进：内容按照某种逻辑顺序展开

## 重要：利用调研信息

你将获得一些关于主题的搜索摘要。请务必参考这些信息来规划大纲，使其切合当前的市场现状或技术事实，而不是凭空捏造。

例如：如果调研显示"某技术已过时"，则不要将其作为核心推荐。

## 输出规范

请严格按照以下JSON格式输出，结果用[PPT_OUTLINE]和[/PPT_OUTLINE]包裹：

[PPT_OUTLINE]

{

"ppt_outline": {

"cover": {

"title": "引人注目的主标题",

"sub_title": "副标题",

"content": []

},

"table_of_contents": {

"title": "目录",

"content": ["第一部分标题", "第二部分标题", "..."]

},

"parts": [

{

"part_title": "第一部分：章节标题",

"pages": [

{ "title": "页面标题1", "content": [] },

{ "title": "页面标题2", "content": [] }

]

}

],

"end_page": {

"title": "总结与展望",

"content": []

}

}

}

[/PPT_OUTLINE]

## Constraints

1. 必须严格遵循JSON格式。

2. **页数要求*：{{PAGE_REQUIREMENTS}}
```

  
> **2.去大量检索资料。**

大纲只是骨架，血肉需要真实、准确的信息来填充。这个因为很多工程上的问题，我们自己项目用的是国内的搜索接口。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/02CA5A72-EB6D-4137-AC4D-566DD6AA2A7D.png)

但如果你想自己DIY这个流程，我墙裂推荐一个神器：**Grok** 。

别的不说，它是我目前用过搜索和信息总结能力最强的AI，没有之一。用法简单到发指：把上一步生成的大纲标题，一个一个丢给Grok，它就能帮你把所需资料搜集、整理得妥妥帖帖。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/4AFD8A0C-11F9-4E4C-8812-8D95AC28CAE7.png)  
> **3.PPT居然还有策划稿？**

拿到内容后，多数人就直接让AI上设计了。但我们多加了一个操作——**策划** 。

啥，PPT还要做策划呢？我想这个词很多PPT设计师都没听过，五年前，我也一样。

那时候我去到了国内顶尖的PPT设计公司锐普，他们的PPT报价是1万+一页。

他们有一个专门的岗位，叫策划师。没错，你前面看到的，需求调研、资料检索，大纲规划，这事儿都归他们干。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/E2808A90-7D33-4151-8A08-BDB3C3DC07FC.png)

他们最终会提供一个PPT草稿给到设计师，每页什么位置要放什么元素，用什么样的版式，全都固定好。

就像这样：

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/DDBA4353-390D-4CDC-B740-9C3CABC2415D.png)  
真正让AI去做PPT的时候，你也可以试试一样的处理。先让AI生成一个，不要各种复杂效果，简简单单，清清爽爽的页面初稿。  
![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/FDB47395-92B0-4545-B93E-97A1FF5010EE.png)  
到后面再去加设计的效果：  
  
![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/CE51D8DD-5C12-48AF-9CB0-485F0E8F48DF.png)

我们做了大量测试，发现这套人类专家的工作流，AI完全能理解！策划部分负责版面规划，设计部分来做风格样式，跑下来的效果非常好。

你啥都不用干，等AI跑完这套流程就能用，甚至都不太需要改。

那当然，如果是一些特别重要的PPT，你也可以在策划稿阶段精调内容，再去让AI跑最终的设计，把效率和颜值都最大化。

> **4.用这个PPT技巧让AI跑设计。**

三顿之前做PPT课程的时候，有一个可以给到“夯爆了”的PPT技巧，叫卡片式布局。

啥是卡片式布局呢，喏，你在苹果的发布会上经常能看到。把内容放进了一个个卡片里。

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/31ED402F-AFA0-418E-8FAB-9A370EFE4C43.jpg)

这样做有三大好处：

1. **能装：** 一页里能清晰地承载大量信息。
2. **灵活：** 卡片数量、大小、位置可以随意组合，版式变化无穷。
3. **AI能懂：** 这是最关键的！我们发现，“卡片”是AI最容易理解和掌握的一种设计语言。

我们把这套方法论，写成了一段精确的指令，告诉AI如何像顶级设计师一样思考布局。这可以说是我们项目的核心壁垒之一，今天也一并分享了：

  

```
内容页的便当网格 (Bento Grid) 布局

这是一种灵活的网格系统，其布局应由内容本身的需求驱动，而非僵硬的模板。通过组合不同尺寸的卡片，创造出动态且视觉有趣的布局。

- 核心原则:

- 灵活性: 卡片数量不固定。可以是 1, 2, 3, 4, 5 或更多个，取决于如何更好地呈现信息。

- 层级感: 使用卡片尺寸建立视觉层级。最重要的信息放在最大的卡片上。

- 留白: 在所有卡片之间保持至少 20px 的间距。

- 布局组合示例:

- 单一焦点: 一张大卡片覆盖大部分区域 (w=1200, h=580)。适用于单一、有力的信息或详细的图表。

- 两栏布局:

- 50/50 对称: 两张等宽的卡片。

- 非对称: 一张较宽的卡片（如 2/3 宽度）用于主内容，一张较窄的（1/3 宽度）用于辅助信息、数据或图片。

- 三栏布局: 三张等宽的卡片，适合并列比较三项内容。

- 主次结合: 一张大的居中卡片，两侧各一张小的垂直卡片。

- 顶部英雄式: 顶部一张宽幅“英雄”卡片，下方是 2-4 个较小的等宽卡片网格。

- 混合网格 (自由度最高): 自由混合各种尺寸的卡片，例如一个中等方块、两个小的水平矩形和一个垂直矩形。这种方式可以极大地适应不同内容的需求。
```

如果大家自己去跑也很简单，拿你刚刚用Grok检索到的内容结果，加上我下面这段提示词：  

```
作为精通信息架构与 SVG 编码的专家，你的任务是将完整的文字内容转化为一张高质量、结构化、具备高级感、简洁感和专业感的 SVG 演示文稿页面。要求如下：

1.画布: SVG viewBox 必须是 0 0 1280 720。

2.内容页的便当网格 (Bento Grid) 布局

这是一种灵活的网格系统，其布局应由内容本身的需求驱动，而非僵硬的模板。通过组合不同尺寸的卡片，创造出动态且视觉有趣的布局。

- 核心原则:

- 灵活性: 卡片数量不固定。可以是 1, 2, 3, 4, 5 或更多个，取决于如何更好地呈现信息。

- 层级感: 使用卡片尺寸建立视觉层级。最重要的信息放在最大的卡片上。

- 留白: 在所有卡片之间保持至少 20px 的间距。

- 布局组合示例:

- 单一焦点: 一张大卡片覆盖大部分区域 (w=1200, h=580)。适用于单一、有力的信息或详细的图表。

- 两栏布局:

- 50/50 对称: 两张等宽的卡片。

- 非对称: 一张较宽的卡片（如 2/3 宽度）用于主内容，一张较窄的（1/3 宽度）用于辅助信息、数据或图片。

- 三栏布局: 三张等宽的卡片，适合并列比较三项内容。

- 主次结合: 一张大的居中卡片，两侧各一张小的垂直卡片。

- 顶部英雄式: 顶部一张宽幅“英雄”卡片，下方是 2-4 个较小的等宽卡片网格。

- 混合网格 (自由度最高): 自由混合各种尺寸的卡片，例如一个中等方块、两个小的水平矩形和一个垂直矩形。这种方式可以极大地适应不同内容的需求。

请你根据我的内容输出SVG代码，我的内容是：
```

直接发送Gemini处理，我们用的是3 Flash，有条件可以直接上3.1 Pro:

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/7017B12E-4B5A-4248-B537-D71A6A870766.png)  
它直接就能生成这样一整个页面的SVG代码了：  
![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/EB065F93-13FA-494E-9EB9-D4CDE220DAEF.jpg)

市面面上的 AIPPT 大多是调用 Banana 或者生成 html，我们采用了生成整页 SVG 的方案。

SVG是PPT里兼容性最好的格式，生成的代码你可以直接拖到Office 2016以上的版本里去做使用。

为什么选了这种SVG格式呢？说起来也是泪。

好处是可以导入 PPT，完全可编辑，甚至各种设计软件都支持，而且可以无限放大，保证清晰度。代价是，三个多月里我们花了大量时间处理 SVG，因为没人做过，一切都得从零开始，不断摸索。

那如果你喜欢我们的思路，可以自己去动手试试，或者直接访问三顿的PPT Agent，这个是我们进行深度调优后的终极版本。

https://sandun.cc

![](.evernote-content/96BD4D2F-02A0-46D1-ADF4-33BFD796B909/EF5065DD-13F8-421C-8EB3-950653003F06.png)

---

最后也想聊聊，为什么想把这个思路分享出来呢，特别是发的提示词已经是我们项目里用的。同事觉得我傻，不怕别人马上抄走吗。

那第一，我觉得，我现在做的这个东西，也只是挖掘了AI做PPT，大概5%的能力，我们还有非常多棒的思路，会去一一实现，这些对于PPT的理解和积累，是没办法复制的。

第二，我是真的不太服气。市面上这些AI PPT工具，他们的开发根本都不懂PPT。给个大纲，硬套模板，让很多人用完都说：AI PPT，也就这样了，不行。

不该是这样的。

我教了7年PPT，做了3年AI产品，我坚信，AI有能力也已经在改变我们制作和演示信息的方式。这些效果是现在我平衡成本和效果下，能跑出来的极限，但远远不是AI的极限。

  
> PS.最后的最后，我知道也有很多小伙伴在蹲订阅计划，实在是很抱歉，三顿这两天还是持续头秃持续修BUG中，我还是想让它能跑到一个稳定的状态再去跟大家聊收费的事儿，所以咕咕到明晚上，请大家耐心等等。
>
> 然后急用的小伙伴也可以充值积分，正式上线订阅后，对这部分小伙伴我们会赠送额外积分，有任何问题也都可以戳网站内右上角的联系方式联系我解决，感恩大家！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=fad356f0cda4dfe6bf731ad9ffb95ad66fe30f76e89f9144102fa592a73d52cc86b6981fede9&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1774701403_3&req_id=1774701678605167&scene=169&mid=2247551655&sn=01dc1de92f599099df135d8d8b38a827&idx=1&__biz=MzUzODg3MzE0NA==&sessionid=1774700038&subscene=200&clicktime=1774703692&enterid=1774703692&flutter_pos=74&biz_enter_id=5&jumppath=20020_1774703613642,20020_1774703625225,20020_1774703660118,1104_1774703662205&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004627&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQXaRgaSFku5/b2Xcazd9EihLTAQIE97dBBAEAAAAAABRiNJz5HMcAAAAOpnltbLcz9gKNyK89dVj07YDhFySqvmi1880fIlos1WZfp6nANs8C54XMi+cyXngvPT1FRVn9sybJnC7T7uo1axgqrydJ5gNgEMnM5hCr7JjkqKhcNBewlZW9pbhkX8uWrNr1oUDN1e4oGNtT2Z2lNS5BNvJsNeUe9P5iu43rADlbNasHj43gm94Nz3B/f7wiuYhSr+/gwucJO4n3ckLrrsZpMYGLG505MF6/osJeJRMwJeJN+tDxl0jfzKA=&pass_ticket=S7a23HrJbvtJomxg1rcExK7V1zPhJ/Mo+/V7b3Ezuxc1bJIf5B3OtQy9UumMnvmL&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f12eafb3-e0f7-4c79-879a-a0703864d504/f12eafb3-e0f7-4c79-879a-a0703864d504/)
