---
title: Claude记忆力归零？用NotebookLM装上_永久大脑_ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/Claude记忆力归零？用NotebookLM装上_永久大脑_ 2.md
tags: [evernote, impression, yinxiang]
---

# Claude记忆力归零？用NotebookLM装上"永久大脑"

---

原文链接: [https://mp.weixin.qq.com/s?chksm=f0bfb224c7c83b327119890d56a8e7e...](https://mp.weixin.qq.com/s?chksm=f0bfb224c7c83b327119890d56a8e7e33982ec6341f70db78b2667aafc6c9fc0d5e63380b320&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1775145141_1&req_id=1775145141093471&scene=169&mid=2247487555&sn=fc803ce12560b86d89b84919b9634074&idx=1&__biz=MzYzMjMzODE4NA==&sessionid=1775145474&subscene=200&clicktime=1775145812&enterid=1775145812&flutter_pos=11&biz_enter_id=5&jumppath=20020_1775145677508,1104_1775145772101,30024_1775145786992,1104_1775145799545&jumppathdepth=4&forceh5=1&ascene=56&devicetype=iOS26.4&version=1800462d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0kMRZ7zrnffQpTdpZyMSXBLTAQIE97dBBAEAAAAAABuADEqw008AAAAOpnltbLcz9gKNyK89dVj0wJnzo4ZuRS4fqwEY2e5ZylbKwovn+0qVREMYO/HqyOUC0si8KOLTVfDmuc2lPN3LGV0muAqn/lMll4CLI5+SNDhZiMEx+3QyediJ8yPerErIau6ZtbuyflW6EYKNmFRLQH3EJNv8gYd06RPgnf1Sh7ei3y1tp2nKRvpbCo94wxntCMv01zx9SkSE5FL2CJLaO05P3qaGtfhe9FjFqstpcvUYYnMAkjfVJQQxASs=&pass_ticket=9xpwSuTK6C0Qec0ErIPnmt4jI9D++aqNnymlwMmmBUoWH/ctQj2s6gM5nYA/OM7G&wx_header=3)

Original老刘的笔记本老刘的笔记本

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

Claude的记忆机制分两种：**会话内记忆**和**跨会话记忆**。会话内记忆是它的工作区，当前对话里说过的一切，它都知道。但一旦关闭对话，清零。

跨会话记忆是大问题。目前主流的解法是"塞文件"——你把项目背景、历史对话、用户画像写成文档，每次开新对话就让Claude读一遍。这确实管用，但代价是：

**每次"补课"都要消耗token**。一份详细的项目文档可能几万字，读一遍就是一大笔成本。更糟的是，如果你有十个项目、每个项目都有大量背景材料，你要么选择性地喂资料（遗漏重要信息），要么全部喂进去（token用完就没钱干活了）。

Jack把这个问题叫做"Claude的失忆症"。他说："Claude HQ确实在努力解决这件事，他们现在发版非常积极，我感觉Claude总部放了很多咖啡。但在他们解决之前，我们得有自己的方案。"

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/D1F0CB91-9947-4D69-AE39-25A28B2AFF8F.png)

二、NotebookLM是什么？为什么它能解这道题
-------------------------

NotebookLM是Google推出的**研究智能平台**，本质上是一个基于RAG（检索增强生成）的知识库系统。

什么叫RAG？Jack打了个很形象的比方：假设你要同时处理《哈利·波特》全系列和《魔戒》全集，如果把所有书都塞进上下文窗口，你会被淹没。但如果有一个语义搜索系统，你问"甘道夫最后一次使用魔法是哪里"，它直接给你翻到那一段——这就是RAG的工作方式。**精准检索，而不是暴力灌入。**

NotebookLM的核心能力：

* • **永久项目记忆**：你做的决策、建立的上下文，跨会话永久保存
* • **功能类个人CRM**：可以记录联系人信息、项目进展、决策日志
* • **会议智能**：把会议记录上传，永久可检索
* • **内容倍增器**：从一份资料出发，可以生成播客、视频脚本、社交媒体内容、演示文稿、信息图——而且**全部免费，不消耗你的API token**

最后一点值得重复一遍：**NotebookLM生成内容是免费的。** 你让Claude生成一张信息图要花token，但通过NotebookLM生成，Google替你买单。

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/B47CB7E2-CA3B-457B-A8EC-A8D38F857380.png)

三、十分钟配置：两个技能文件搞定一切
------------------

Jack设计了两个技能文件，分别对应Claude Code和Claude Co-work两个环境。

**针对Claude Code的配置：**

1. 1. 下载NotebookLM技能文件（视频描述区有链接）
2. 2. 把文件拖入Claude Code对话框，输入"execute this skill"，回车
3. 3. Claude Code会自动下载Python脚本（从GitHub repo），并提示你登录NotebookLM
4. 4. 点击弹出的浏览器链接，用Google账号登录NotebookLM
5. 5. 登录成功后，Claude Code自动获取cookie/token，配置完成

完成后，你可以测试："告诉我我最近三个notebook的标题，并下载最新生成的视频。"如果能正确返回，说明打通了。

Jack在演示中直接问Claude："告诉我最近三个notebook的标题，并从最新的notebook下载最后生成的视频。" Claude找到了一个叫"Agentic Drift的数学"的notebook，并把视频保存到了下载文件夹。这个视频是NotebookLM生成的——"人工智能行业正在从单一模型提示工程转向智能体编排设计"……Jack评价道："不完美，但真的令人印象深刻。"

**针对Claude Co-work的配置：**

Co-work和Code是不同的运行环境，不能直接共享token。Jack的解决方式很巧妙：

1. 1. 在Claude Code里，输入"请把NotebookLM添加为Co-work技能"
2. 2. Claude Code会自动生成一个 `notebooklm_skill.workmd` 文件，保存到桌面
3. 3. 打开Co-work → 点击左下角"+"→ Skills → Manage Skills → Upload a skill
4. 4. 上传刚才生成的文件即可

为什么要这样绕一圈？因为Claude Code能获取token，但Co-work本身不能。Claude Code帮你做了这一步，然后把配置打包成文件给你。

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/94D1A8DA-9E33-4CBF-B523-3207F17A615C.png)

四、用例一：深度增强——让70个资料来源为你工作
------------------------

第一个真实场景：**你在Claude Co-work里有一个运营了很久的YouTube频道项目，想要获得更深入的增长洞见。**

普通做法：问Claude，Claude凭它知道的内容给你答案，参考价值有限。

接入NotebookLM后的做法：

Jack对Claude说："请基于你对我的全部了解，以及这次对话中的内容，创建一个全新的notebook。完成后，给我10条精华洞见，以及我需要立刻执行的3个核心行动。"

Claude调用NotebookLM技能，运行在后台——"拿好你的咖啡，等它跑完"，Jack说。

返回结果：10条基于**超过70个资料来源**的精华洞见，包括：他的完整频道策略、过去30个视频的数据表现、4个最高播放量视频的字幕、他的社区页面、关于YouTube增长的2篇深度研究文章……

一条洞见是这样的："你的频道本质上是一台转化机器。" Jack的反应是："很大方的评价，但我很欣赏。"

这里的技术价值在于：如果你让Claude直接处理这70份资料，上下文窗口会爆，或者花费惊人。**但通过NotebookLM的RAG系统，Claude只需要发出一个查询，Google那边处理完所有语义匹配，然后把"钻石"——最相关的结果——返回给Claude。** 整个过程对你的Claude token消耗极小。

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/D1F0CB91-9947-4D69-AE39-25A28B2AFF8F.png)

五、用例二：免费内容工厂——从对话到精美信息图
-----------------------

第二个场景：**你要周二给客户做汇报，需要一套关于邮件营销5步序列的信息图。**

步骤：

1. 1. 先在Claude Code里讨论邮件策略，建立框架（钩子→故事→价值投放→销售推荐→成交收尾）
2. 2. 然后直接说："请在NotebookLM里帮我生成一张信息图，用漂亮的配色和专业字体。"
3. 3. Claude调用NotebookLM，NotebookLM生成信息图，Claude下载并打开

Jack打开了生成结果：**一张包含5个环节的邮件序列信息图**——Hook、Story、Value Drop、Pitch、The Closer。完全免费，没有消耗任何Claude token。

这背后的逻辑是：**你用Claude做思考和规划，用NotebookLM做内容生产。** 两者各司其职，彼此互补。

NotebookLM能免费生成的内容类型远不止信息图：

* • **深度调研**：把20篇行业文章喂进去，获得一份综合摘要
* • **竞品分析**：摄入竞争对手的公开资料，提炼竞情情报
* • **尽职调查**：文献综述、趋势发现
* • **项目复盘**：上传项目记录，分析什么出了问题、为什么出问题
* • **提案起草**：喂入RFP（招标需求书），生成有充分依据的方案
* • **SOP与手册**：把操作流程标准化，适合团队入职

同时解决了另一个常被抱怨的问题：**Obsidian方案的上下文爆炸**。很多人用Obsidian管理知识库，然后把整个库都塞给Claude，结果token迅速耗尽，体验极差。Jack的方案是"jab and get results back"（一击获回报）：发一个查询，Google处理，只拿回你真正需要的那部分。

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/B47CB7E2-CA3B-457B-A8EC-A8D38F857380.png)

六、用例三：记忆持久化——Wrap-up技能让对话"留存"
-----------------------------

这是三个用例里Jack认为**最重要的一个**。

问题：你和Claude谈了一个很长的会话，里面有很多有价值的决策、方向确认、创意——但会话结束，全部消散。

解法：**Wrap-up技能**。

配置方式和前面一样，上传 `wrap-up.workmd` 技能文件到Co-work（或Code）。

使用方式：在一次重要的长会话结束前，输入 `/wrap-up`。

技能会自动：

1. 1. 检查你是否有"大脑notebook"（如"Jack's Brain"）——如果没有，引导你创建
2. 2. 遍历整个会话，提取关键决策、行动项、上下文
3. 3. 把这些全部存入NotebookLM对应的notebook

Jack展示了他自己的"Jack's AI Brain"notebook，打开后显示："战略规划会话摘要，2026年3月29日"——完整的会话摘要、执行了什么、讨论了什么，全部在里面。

更进一步，Jack在Co-work的项目说明里加了一行："在回答关于策略的任何问题时，始终查阅NotebookLM里的jackbrain.md。"

效果：**任何时候他问策略问题，Claude自动先去"Jack的大脑"里语义搜索，拿回最相关的历史决策和背景，然后在此基础上给建议。** 对话越多，大脑越强。

这套系统的妙处在于它**不是线性积累而是语义积累**。传统的上下文方案是线性的——你加多少进去，Claude就带着多少重量。NotebookLM的RAG方案是语义的——不管你积累了多少内容，每次查询只取最相关的片段，计算成本基本保持不变。

**核心原则：让Claude知道去哪里找答案，而不是把所有答案都塞给Claude。**

![](.evernote-content/1D4FDDE1-D526-4AED-B34B-BFE1C8681AB0/94D1A8DA-9E33-4CBF-B523-3207F17A615C.png)

七、它在哪里能用？
---------

好消息是这个系统完全通用：

* • **Claude Code** ✓
* • **Claude Co-work（包括Co-work Projects）** ✓
* • **普通Claude Chat** ✓

在Co-work Projects里使用效果尤其好，因为项目本身已经有背景文件，加上NotebookLM的长期记忆，等于双重上下文加持。

### 总结与核心行动

Claude的记忆问题是真实的，但解法不是等Claude官方更新，也不是花更多钱买更多token——而是**外包记忆层**。

NotebookLM提供了一个免费的、基于RAG的语义检索系统。接入Claude之后，你的AI工作流会从"每次归零"变成"越用越聪明"。

**现在就能做的三件事：**

1. 1. **装好技能**：按照视频说明，把NotebookLM技能文件配置好，花10分钟，一次搞定
2. 2. **测试Enrichment**：在你当前最重要的项目里，让Claude创建一个NotebookLM notebook，感受70个来源的威力
3. 3. **建立你的AI大脑**：在接下来每次重要对话结束前执行 `/wrap-up`，坚持一个月，看看会发生什么

记忆不是Claude的限制，是你使用方式的限制。

"与其把所有书都装进脑子，不如知道书架在哪。" —— 用NotebookLM构建Claude的外脑

#Claude #NotebookLM #AI工具 #AI记忆 #提示词工程 #AI效率 #大模型应用

作者提示: 内容由AI生成

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=f0bfb224c7c83b327119890d56a8e7e33982ec6341f70db78b2667aafc6c9fc0d5e63380b320&exptype=unsubscribed_card_recommend_item_heat_tlfeeds&ranksessionid=1775145141_1&req_id=1775145141093471&scene=169&mid=2247487555&sn=fc803ce12560b86d89b84919b9634074&idx=1&__biz=MzYzMjMzODE4NA==&sessionid=1775145474&subscene=200&clicktime=1775145812&enterid=1775145812&flutter_pos=11&biz_enter_id=5&jumppath=20020_1775145677508,1104_1775145772101,30024_1775145786992,1104_1775145799545&jumppathdepth=4&forceh5=1&ascene=56&devicetype=iOS26.4&version=1800462d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0kMRZ7zrnffQpTdpZyMSXBLTAQIE97dBBAEAAAAAABuADEqw008AAAAOpnltbLcz9gKNyK89dVj0wJnzo4ZuRS4fqwEY2e5ZylbKwovn+0qVREMYO/HqyOUC0si8KOLTVfDmuc2lPN3LGV0muAqn/lMll4CLI5+SNDhZiMEx+3QyediJ8yPerErIau6ZtbuyflW6EYKNmFRLQH3EJNv8gYd06RPgnf1Sh7ei3y1tp2nKRvpbCo94wxntCMv01zx9SkSE5FL2CJLaO05P3qaGtfhe9FjFqstpcvUYYnMAkjfVJQQxASs=&pass_ticket=9xpwSuTK6C0Qec0ErIPnmt4jI9D++aqNnymlwMmmBUoWH/ctQj2s6gM5nYA/OM7G&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c6a9ebee-1059-482c-9523-37b697e700af/c6a9ebee-1059-482c-9523-37b697e700af/)
