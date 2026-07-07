---
title: Vibe Coding 的完整工作流程 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Vibe Coding 的完整工作流程 2.md
tags: [evernote, impression, yinxiang]
---

# Vibe Coding 的完整工作流程

---

原文链接: [https://mp.weixin.qq.com/s?chksm=8838311ebf4fb808ea722387eb9a8f5...](https://mp.weixin.qq.com/s?chksm=8838311ebf4fb808ea722387eb9a8f54df2a26b2ed58760e7df9f9597f3a7ce8d337740841ec&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1773504967_1&req_id=1773504967155910&scene=169&mid=2649162075&sn=4c3c69fcaec1150aaf8344c9f438fb06&idx=1&__biz=MzA4ODM0NDg3NA==&sessionid=1773504752&subscene=200&clicktime=1773505186&enterid=1773505186&flutter_pos=11&biz_enter_id=5&jumppath=20020_1773504983311,WCWebImageBrowserViewController_1773505038359,20020_1773505044938,1104_1773505166518&jumppathdepth=4&ascene=56&devicetype=iOS26.3.1&version=18004531&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQMGYJQkz2+EY+guaNI65m3hLVAQIE97dBBAEAAAAAAM9SD7fBPNAAAAAOpnltbLcz9gKNyK89dVj0jLkYQnRNgExAnkl22obaDgEecS+qNMZyiXibO3QxCko9rxzXLdwUGPwOL7+bBdfIR3VM5dBCmqAvHGcNdM34SLlV4muvTH7hm6tunekhH/Fn1ZcOw1ZPPEN8T+HA4ijO39KZREhq80r5tyKZEfXAtV94jsQfsrts5IhWXPd5cuPD4GAkk3weEGyfaqKWLRZvgAN8mPBxIGjvJBvn+b13cw10KorYvX2A/ELk7s8cHA==&pass_ticket=ZhS9CRIZOf0I3dGI6rtgUnuQY+oaCzNq4XUD4Ju5nUExJ5WjWyIZn//3Oqap+ufA&wx_header=3)

Vibe Coding 的完整工作流程
===================

Original麥柯Michael麥柯Michael

如果说很多人对 Vibe Coding 的第一印象，是“用一句话把页面做出来”，那真正进入实战之后你就会发现，**Vibe Coding 从来不是一句 Prompt 的问题，而是一整套产品构建流程的重组。**

它不是单点工具，也不是某个模型突然变聪明了。

它真正改变的，是从“想法出现”到“产品落地”之间的整条链路。

过去，一个产品通常会经历：

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/368BF0BC-11F7-4974-8E86-8D7ED007D1DE.png)

想法 → 需求整理 → 信息架构 → 设计稿 → 前端开发 → 

联调测试 → 上线 → 迭代

而在 Vibe Coding 的工作流里，这条链路并没有消失，但它被重新压缩、重构、并联了。

也就是说，**流程还在，只是顺序、节奏和角色分工都变了。**

**本篇文章就来聊一聊：一套真正可执行的****Vibe Coding 完整工作流程**，到底应该怎么跑。

**一、第一步不是写代码，**
---------------

**而是先定义“要解决什么问题”**
------------------

很多人一打开 AI 工具，就迫不及待开始输入：

“帮我做一个 SaaS 官网”

“生成一个类似 Apple 风格的 landing page”

“做一个简洁高级的 dashboard”

表面上看，效率很高。但实际上，很多项目从第一句就已经开始跑偏了。因为你描述的是结果，不是问题。而任何一个能长期跑下去的产品，都必须先回答三个问题：

**第一，这个东西是给谁用的。**

**第二，他要解决什么核心问题。**

**第三，用户为什么要在你这里停留、行动，甚至付费。**

如果这三个问题没想清楚，后面生成得越快，偏得越远。

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/BC79C6EE-D1F0-4FD4-B91B-33129C2286DE.png)

所以 Vibe Coding 的第一步，不是“让 AI 开始写”，而是你先把问题框定出来。

例如你要做一个设计师学习平台，那么你至少要先明确：

* 目标用户是设计师、产品经理，还是创业者？

* 用户是零基础入门，还是已经会工具但缺乏体系？
* 你的平台核心价值是教程、案例、工作流，还是模板资源？
* 用户第一次进入首页，最应该感受到的是什么？
* 你是想让他订阅、留资、购买课程，还是先建立品牌认知？

这些东西看似不像代码，但它们决定了后面所有页面结构和功能优先级。

Vibe Coding 最容易让人误解的一点，就是它看起来像是在省略前期思考。

其实不是。它不是不要思考，而是要求你把思考变得更直接、更结构化、更能马上作用于结果。

二、第二步是把模糊想法，

整理成可以驱动 AI 的结构化输入

很多人说 AI 生成得不稳定，其实很大一部分原因，是因为输入本身不稳定。你脑子里可能有一个感觉，但 AI 需要的不是“感觉很好”，而是尽可能明确的结构化上下文。

这一步你要做的，是把你脑海里的模糊构想拆成几个关键模块：

1. 产品目标

这个页面或产品是干什么的。

是展示、转化、教学、销售，还是内容沉淀。

2. 目标用户

用户是谁，他的基础水平如何，他最关心什么，他为什么会来。

3. 核心任务

用户来到这里，最想完成什么动作。

比如浏览课程、查看案例、预约咨询、提交需求、注册试用。

4. 风格参考

你希望整体偏什么气质。

例如 Apple 式克制、Notion 式清晰、Linear 式理性、或者更偏媒体化、未来感、杂志感。

5. 内容模块

页面应该由哪些部分组成。

例如 Hero、价值点、案例展示、课程目录、FAQ、CTA、Footer。

6. 技术边界

你准备用什么栈。

比如 Next.js、React、Tailwind、Sanity、Framer Motion、Shadcn/ui 等。

7. 可维护性要求

哪些地方要模块化，哪些内容后续要交给 CMS 管理，哪些组件会复用。这一层非常关键。因为从这里开始，Vibe Coding 才从“随便生成”进入“可控生成”。说白了，AI 不怕你要求高，怕的是你自己也没想清楚。

**三、第三步是先做“信息架构”和“页面骨架”，**
--------------------------

**不要一开始就陷入视觉细节**
----------------

很多人一上来就盯着视觉效果：

要不要玻璃态、要不要渐变、要不要 3D、要不要视差、要不要大字排版。

这些都很重要，但都不是第一优先级。

因为一个页面真正决定体验上限的，首先不是视觉，而是：

```
信息顺序对不对

层级清不清楚

用户能不能快速扫读

页面有没有节奏

每个模块是否承担明确任务

转化动作放得合不合理
```

所以第三步最合理的做法，是先让 AI 帮你搭出页面骨架。例如可以先让它输出：

```
首页的完整区块结构

导航层级

每个 section 的目的

用户滚动时的信息递进关系

CTA 应该出现在哪些节点
```

这个阶段，你追求的不是“像成品”，而是“像结构”。

因为结构一旦对了，后面视觉和交互才有稳定落点。

如果结构是错的，视觉做得越满，后面返工越大。

这一步本质上对应的是传统流程中的：

**信息架构 + 低保真框架 + 页面逻辑设计**

只是现在，这部分可以更快完成，而且能直接进入下一步验证。

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/04BD8DF5-9226-4504-A20F-EEACCB21CA4A.png)

四、第四步是快速生成第一版可运行原型，

让抽象讨论尽快变成真实体验

这一步才是很多人以为 Vibe Coding 一开始就在做的事。但其实，它应该发生在前面几步之后。当目标、用户、结构都比较清楚了，你就可以让 AI 开始生成第一版可运行原型。这里的重点不是“做漂亮”，而是“尽快能看、能点、能改”。

你需要第一时间验证的，通常包括：

```
页面节奏是否顺

区块之间是否自然

文案密度是否合适

视觉方向是否匹配品牌

交互逻辑是否流畅

导航结构是否直观

首屏信息是否足够有吸引力

用户是否知道下一步该做什么
```

很多过去在 Figma 里讨论半天的问题，到了浏览器里五分钟就能看明白。这也是 Vibe Coding 最有价值的地方之一：

**它把很多纸面讨论，提前变成了真实体验。**

你不再只是“想象这个界面可能如何”，而是能直接看到、滚动、点击、感受它。一旦进入这个状态，产品判断会比单纯讨论快很多。

**五、第五步是进入“连续导演式迭代”，**
----------------------

**一轮一轮把结果拉准**
-------------

很多外行以为 AI 生成一次就差不多结束了。

实际上，真正的工作往往从第一版出来之后才正式开始。因为第一版通常只能解决“有”，解决不了“准”。接下来你需要做的，是连续几轮非常高密度的定向调整。这一步很像导演拍片，也像资深设计师带着团队一轮一轮 refine：

第一轮：改结构

看看模块顺序是否合理，是否有冗余 section，是否有重要信息被埋没。

第二轮：改视觉层级

调整标题大小、留白节奏、卡片密度、按钮权重、图片位置。

第三轮：改交互状态

补 hover、loading、empty state、error state、切换反馈、动效节奏。

第四轮：改内容表达

把空话、套话、AI 味过重的文案改成更有判断、更贴合目标用户的表达。

第五轮：改组件系统

开始抽离可复用组件，统一 spacing、radius、字号、颜色、shadow、栅格逻辑。到这个阶段，Vibe Coding 已经不再是“帮我生成一个页面”，而是在做真正的产品打磨。也是从这里开始，使用者的专业能力差异会被无限放大。因为 AI 可以提供速度，但什么该保留、什么该删、什么该增强、什么该统一，这些都必须靠人判断。

六、第六步是把页面

从“演示逻辑”推进到“真实产品逻辑”

这一关是很多 AI 生成项目最容易翻车的地方。

因为 demo 很容易看起来像样，

但一旦开始接真实数据、接表单、接 CMS、接登录权限、接动态内容，问题就会出现。

所以第六步的重点，是从“静态演示”升级为“真实可用”。通常包括几类事情：

1. 接内容系统

例如把课程、文章、案例、作者信息、FAQ 等交给 Sanity、Notion 或其他 CMS 管理。

2. 接表单与转化链路

比如咨询表单、订阅表单、邮件收集、提交需求。

3. 接动态数据

例如文章列表、推荐内容、分类筛选、搜索结果、用户状态。

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/54DBE068-49CC-44BF-9D32-22E748E62677.png)

4. 补边界状态

包括没有内容时怎么办，加载慢时怎么办，提交失败怎么办，字段报错怎么办。

5. 检查响应式和设备适配

桌面端好看，不代表移动端可用。

很多布局和动效一到手机上就出问题。

6. 检查性能

尤其是用了较多动画、3D、视频背景、大图资源时，性能会直接影响真实体验。

这一阶段开始，Vibe Coding 真正接近“交付”。

因为产品不是只给自己看，而是给用户用。

用户不关心你是不是 AI 生成的，他只关心：

**好不好用，快不快，清不清楚，值不值得继续留下来。**

**七、第七步是建立设计系统和代码系统，**
----------------------

**不让项目越做越乱**
------------

很多人前面冲得很快，后面就开始乱。页面越多，组件越多，改动越频繁，结果整个项目越来越难维护。所以一个成熟的 Vibe Coding 流程，不能只看前期生成速度，还必须尽早进入系统化整理。

你至少要开始统一这些东西：

```
颜色体系

字号和字重体系

间距规则

栅格逻辑

按钮规范

表单规范

卡片结构

状态反馈

动效节奏

组件命名

文件夹结构

内容字段命名
```

这件事听起来没那么性感，但它决定了你的项目能不能继续长大。

没有系统的项目，AI 会越帮越乱。

有系统的项目，AI 才能越帮越快。

所以严格来说，Vibe Coding 的中后期核心，不再是“继续生成”，而是：

让生成结果逐渐进入系统管理。

这也是从个人 demo 到真实产品之间最关键的一道坎。

八、第八步是测试、复盘、优化，

而不是“生成完就算结束”

产品上线不是结束，而是另一轮学习开始。Vibe Coding 的一个巨大优势，是因为构建速度快，所以你可以更频繁地测试和优化。这意味着上线之后，你应该持续看：

* 用户停留在哪一屏
* 哪个按钮点击率高
* 哪个 section 被快速跳过
* 用户最常在哪一步离开
* 哪种文案转化更好
* 哪种布局更适合阅读
* 哪种内容更容易引发咨询

以前做这些优化，可能改起来成本高，团队协作链路长。

现在如果工作流成熟，很多调整都可以快速完成。

于是产品不再是“先做一版再说”，

而是可以真正进入一种更轻、更快、更连续的迭代节奏。

这也是为什么我越来越觉得，Vibe Coding 最终改变的不是某个岗位，

而是整个数字产品的演化速度。

九、把完整流程收束成一句话：

Vibe Coding 不是写代码，

而是在导演产品成型

如果把前面所有内容收束一下，一套完整的 Vibe Coding 工作流程，大概可以概括为：

定义问题 → 整理上下文 → 搭建结构 → 生成原型 → 连续迭代 → 接入真实逻辑 → 系统化整理 → 上线测试优化

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/651EECF5-3C05-45BA-8686-25273039FD9F.jpg)

你会发现，它本质上仍然符合产品设计和开发的底层规律。

只是 AI 把很多环节压缩了，把很多角色之间的距离拉近了，也让很多原本串行的流程变得可以并行推进。

所以 Vibe Coding 从来不是跳过方法论，而是让方法论更快抵达结果。

在这个过程中，真正重要的不是你会不会写某一句 prompt，而是你有没有能力判断：

* 目标是否成立
* 结构是否清晰
* 体验是否顺畅
* 系统是否稳定
* 内容是否有价值
* 产品是否可持续迭代

到最后你会发现，AI 并没有替你做产品。

它只是让你第一次有机会，把脑海里的判断，更直接地作用到产品本身。

**结尾**
------

很多人把 Vibe Coding 理解成一种“更快做页面”的方法。

但我更愿意把它理解为一种新的产品工作流。

它不是某个单点工具的技巧，而是一种把产品、设计、内容、前端实现重新连接起来的方式。

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/0BBD7121-20B9-473F-A39A-58F3E38A990E.jpg)

真正成熟的 Vibe Coding，不是一键生成，不是拼命堆特效，也不是把项目做得像个漂亮 demo。而是你能不能用一套更快的工作流，把一个模糊想法稳稳推进成一个可用、可改、可持续演化的产品。

这，才是它最核心的价值。

*欢迎加入讨论学习小组，加好友进群*

![](.evernote-content/D3ED7E18-A727-4AF7-BD86-4C0458D67A41/BD16A8FA-983E-42B1-A3ED-C4941C7D6F77.png)

  

大家好，我是麦柯 Michael，

设计师 / 开发者 / 摄影师。

和我一起用Vibe Code构建属于自己的产品！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=8838311ebf4fb808ea722387eb9a8f54df2a26b2ed58760e7df9f9597f3a7ce8d337740841ec&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1773504967_1&req_id=1773504967155910&scene=169&mid=2649162075&sn=4c3c69fcaec1150aaf8344c9f438fb06&idx=1&__biz=MzA4ODM0NDg3NA==&sessionid=1773504752&subscene=200&clicktime=1773505186&enterid=1773505186&flutter_pos=11&biz_enter_id=5&jumppath=20020_1773504983311,WCWebImageBrowserViewController_1773505038359,20020_1773505044938,1104_1773505166518&jumppathdepth=4&ascene=56&devicetype=iOS26.3.1&version=18004531&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQMGYJQkz2+EY+guaNI65m3hLVAQIE97dBBAEAAAAAAM9SD7fBPNAAAAAOpnltbLcz9gKNyK89dVj0jLkYQnRNgExAnkl22obaDgEecS+qNMZyiXibO3QxCko9rxzXLdwUGPwOL7+bBdfIR3VM5dBCmqAvHGcNdM34SLlV4muvTH7hm6tunekhH/Fn1ZcOw1ZPPEN8T+HA4ijO39KZREhq80r5tyKZEfXAtV94jsQfsrts5IhWXPd5cuPD4GAkk3weEGyfaqKWLRZvgAN8mPBxIGjvJBvn+b13cw10KorYvX2A/ELk7s8cHA==&pass_ticket=ZhS9CRIZOf0I3dGI6rtgUnuQY+oaCzNq4XUD4Ju5nUExJ5WjWyIZn//3Oqap+ufA&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/252166b3-526c-4fbb-8fb2-6028b253ceb4/252166b3-526c-4fbb-8fb2-6028b253ceb4/)
