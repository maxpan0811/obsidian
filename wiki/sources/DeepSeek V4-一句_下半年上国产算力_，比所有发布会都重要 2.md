---
title: DeepSeek V4：一句_下半年上国产算力_，比所有发布会都重要 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/DeepSeek V4：一句_下半年上国产算力_，比所有发布会都重要 2.md
tags: [evernote, impression, yinxiang]
---

# DeepSeek V4：一句"下半年上国产算力"，比所有发布会都重要

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI5MDQxNzE1NQ==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzI5MDQxNzE1NQ==&mid=2247515563&idx=1&sn=68a2fddbaa449221799b773096a41578&chksm=ed56ff01fdaa37627aacbbd6a49990b3400d5dc61ac5acc90bfc554b5fd0fbec93c76e14b1a8&scene=90&xtrack=1&req_id=1777017612236286&sessionid=1777017859&subscene=272&clicktime=1777018545&enterid=1777018545&flutter_pos=14&biz_enter_id=4&ranksessionid=1777017864&jumppath=20020_1777017863867,WCWebImageBrowserViewController_1777017943346,20020_1777017952555,1104_1777018120444&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004728&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQSaS/9mneF+VG0N/JeOhK7BLVAQIE97dBBAEAAAAAAJWvDpmLZbAAAAAOpnltbLcz9gKNyK89dVj0c0bE41Ge/thVF3X6+rb4j4Y+MQeXDlQXYqBINkBZxWlt8vTdWVNSZzDy8UHczjng0MrqEur928evFynCVhrdy1Ce6WYZGFjPV4HrFX8EV/nnPD9sE8A1fv081w4jh6oQ00VXRoVh+qxFHBuEgDsBQkYleQg2DWmWk29oRuRwptOnipu94az6uPGcQN8w9li06Xfr3V9crn9CN9ccernzoac3MRgiji8T+BJOTy4cDQ==&pass_ticket=ljPNqTXyMrNK5yeuPrHuc8qi7nNg/CvZ+pn79iGa3anu6S7RNeQgVRh8q3Jtr8wR&wx_header=3)

Original星海老局 星海情报局

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/09B8ECC2-B3A3-4AB3-B900-BDEF4E230B18.gif)

他来了，他来了，他带着V4走来了。

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/971882B2-764F-4288-A12A-205EC15E5A0C.png)

前两天我们才聊过DeepSeek融资的事儿，今天V4就上新了，普天同庆了属于是。

上一次DeepSeek引发全球震动，是2025年初V3正式发布的时候。那一次，一个中国团队用据称不到600万美元的算力成本，训练出了一个可以和GPT-4正面竞争的模型，然后把它开源，整个硅谷集体失语了几天，英伟达股票直接一波暴跌。

之后的一年，AI圈的发布节奏快得令人眩晕。Anthropic发了Claude 4系列，Google推了Gemini-Pro-3.1，OpenAI在o系列上持续迭代，最近更是恐怖，一周时间里，我们相继见证了image 2.0和GPT-5.5的发布，全球AI领域堪称是“勃勃生机，万物竞发”的境界。

而DeepSeek那边，只发了几个不算引人注目的中间版本：V3.1、V3.2-Exp，每次跑分和前代差不多，看起来像是在原地踏步。

关于V4什么时候发的传言从2025年底就没停过。有人说是和之前一样在春节前，结果却是一直等到了四月底。

然后零帧起手，毫无预警，DeepSeek把V4放出来了。同步开源，同步上线官网和App，同步更新API。发布稿结尾引了一句荀子：「不诱于誉，不恐于诽，率道而行，端然正己。」

现在回头看那些"没什么亮点"的中间版本，才明白那是在铺路。

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/A0E23219-D33F-46A4-840D-534436AA18B1.jpg)

**V4是什么**
---------

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/77A96043-46CC-42C5-8399-BD3FA764D051.png)

这次V4一口气发了两个版本。

**DeepSeek-V4-Pro**，总参数1.6万亿，每次推理激活49亿。定位是对标顶级闭源模型的旗舰版本。**DeepSeek-V4-Flash**，总参数2840亿，激活130亿，是更小更快的经济版本。

理解这两个数字需要先理解V4的架构。

V4采用的是MoE（混合专家）架构，模型内部有大量"专家"子网络，每次处理一个token时，由路由机制决定激活哪几个专家参与计算。这意味着，V4-Pro虽然有1.6万亿参数，但实际每次推理的计算量更接近一个490亿参数的稠密模型。总参数决定知识容量，激活参数决定推理成本，这是MoE架构最核心的商业逻辑。

为什么这个原理很重要呢？

因为推理成本主要由**激活参数量**决定，不是总参数量。

所以V4-Pro的实际推理开销更接近一个49B的稠密模型，而不是1.6T。但它的"知识容量"理论上接近1.6T，因为不同token会激活不同的专家组合。

打个简单的比方就是：一家公司有1600个员工，个个都身怀绝技，每个项目只调49人上阵，但可以按需组合不同专家。

在能力评估上，DeepSeek的官方定位有几个值得注意的地方。

首先，他们没有回避上限，这本身就是一种坦然和自信。发布稿明确写道，V4-Pro的Agent能力优于Sonnet 4.5，交付质量接近Opus 4.6非思考模式，但仍与Opus 4.6思考模式存在一定差距。这种有上限有下限的写法，在国内AI发布稿里相对罕见，反而增加了可信度。

其次，能力的分布是不均匀的。在数学、STEM、竞赛型代码等推理密集的任务上，V4-Pro声称超越所有开源模型，比肩顶级闭源。这和DeepSeek历来的强项一致。但在世界知识方面——也就是对事实性信息的覆盖广度——V4-Pro仅稍逊于Gemini-Pro-3.1，大幅领先其他开源模型。世界知识这块的差距来自数据，Google有Search索引和更大规模网页抓取的结构性优势，这不是算法可以短期弥补的。

V4-Flash的定位是明确的性价比选择。推理能力接近Pro，世界知识稍逊，但因为激活参数只有13B，API价格更便宜，响应更快。在Agent测评中，Flash在简单任务上和Pro旗鼓相当，复杂任务上有明显差距。对于大多数实际部署场景，Flash可能是更合理的默认选择。

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/6507DCD1-B2CA-429D-B51C-7937D2ED7973.jpg)

**1M上下文：从王牌变成“基本操作”**
---------------------

这是V4最值得认真对待的变化，但理解它需要一点背景。

一年前，百万token的上下文窗口是Gemini的独家特性，是Google用来区隔竞争对手的产品王牌。彼时其他所有主流模型，闭源的要么128K要么200K，开源的几乎没人能在这个量级上做到可用。1M上下文意味着可以把一整部长篇小说、一个大型代码库、几十份研究报告同时塞进模型的"工作记忆"里。这是一种质变，不只是量变。

今天，DeepSeek把1M上下文定成了所有官方服务的标配，并且开源。

问题是：为什么现在可以做到了？

传统Transformer架构有一个根本性的扩展难题：注意力机制的计算量随上下文长度平方级增长。上下文翻倍，计算量变四倍。这意味着把上下文从128K扩展到1M，理论上计算量会增长约60倍。在这个约束下，1M上下文要么需要极大的算力投入，要么速度慢到不可用，要么两者兼而有之。

V4的回答是DSA，DeepSeek Sparse Attention，稀疏注意力机制。

用大白话解释一下就是：想象你在读一本1000页的书，你要回答的问题是"第500页的观点和哪些内容有关"。笨办法是把第500页和其他999页逐一比较，一共做999次比较。页数翻倍，工作量变四倍——这就是平方增长的问题。

聪明办法分两步：

**第一步（****DSA****）**：先粗略扫一眼，判断哪些页面可能相关，只精读那几十页，其他的直接跳过。大多数页面和第500页根本没关系，不算也不会影响答案。

**第二步（****token****压缩）**：就算是那几十页"相关页面"，也不需要一字不差地读，可以先把每页压缩成一段摘要，用摘要来做比较。信息量再缩一轮。

两步叠加之后，书从1000页变成2000页，工作量不再是原来的四倍，而是大概两倍多——增长曲线被压平了。

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/20B8440E-7FCD-4667-86C9-B2D7E3616156.png)

这就是V4能把1M上下文做得既长又不贵的核心原因。。

这个架构的种子早在V3.2-Exp就已经种下。当时外界几乎没有人注意到DSA的引入，因为跑分变化不大，看起来像是一次无聊的中间版本。现在回头看，那是在用一个低调的版本验证新架构在生产环境下的稳定性。V3.2是V4的地基，不是一次失败的尝试。

1M上下文变成开源标配的意义，不在于数字本身，而在于**成本曲线的改变**。这个技术壁垒一旦被打穿并且开源，任何团队都可以在这个架构基础上继续迭代。长上下文从一个"有足够算力才能玩"的高端功能，变成了任何人都能用的基础能力。

这对Agent应用的影响尤其直接。

Agent任务的一个核心约束一直是上下文管理：任务链越长，需要维护的状态越多，有限的上下文窗口很快就成为瓶颈。1M窗口意味着Agent可以在一个更长的操作链里保持状态连贯，处理更大规模的代码库，跨越更多文档进行推理。

这也部分解释了为什么V4在Agent评测上的提升幅度如此显著——不只是模型变聪明了，底层条件也发生变化了。

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/C7D843CF-8A50-419D-ADBD-E7979CDA33E3.jpg)

**国产算力：一条不依赖英伟达的路**
-------------------

发布稿里有一句话被很多人忽略了：下半年批量上国产算力。

![](.evernote-content/476F28F9-D4A7-425C-837F-73CAF605E32C/39C30BE9-F623-4BA1-83C4-6561989699B2.png)

这句话的分量，需要放在过去两年的地缘政治背景里才能看清楚。

2023年以来，美国对华芯片出口管制持续升级，英伟达H100、H800、A100相继被限制出口中国。这对中国AI公司的算力供给构成了实质性压力。训练和部署大型语言模型需要大量高端GPU，而可以合法获得的选项越来越少。

DeepSeek此前的训练主要依赖英伟达算力，V3的训练用的是H800集群。但随着出口管制收紧，这条路的可持续性越来越存疑。

昇腾系列是目前国内最成熟的替代方案。这次发布稿里，昇腾方面提供了相当详细的技术数据。昇腾950超节点上，V4-Pro的推理延迟可以达到TPOT 20毫秒，V4-Flash达到10毫秒。

当然，这些数字都是在离线推理模式下采集的，不包含实际服务调度的负载，现实部署中的数字会有折扣。但方向是明确的：昇腾已经能够支撑V4系列模型的量产部署，不再只是实验室里的备选方案。

"下半年批量上国产算力"意味着什么？至少有两个层面的含义。

第一层是供给安全。如果DeepSeek能在昇腾上实现和英伟达相近的推理性能，那么算力供给就不再是一个单点风险。出口管制的影响会被部分对冲。

第二层是生态信号。DeepSeek是中国最具影响力的开源模型之一，如果它正式在昇腾上规模部署，会带动整个开源社区和下游应用去适配昇腾生态。这对国产算力来说是一个远比单纯硬件销售更有价值的背书。

不过，无论如何吧，DeepSeek和国产算力的深度绑定，是这次发布里最具长期战略意义的一笔——算是从底子上开辟新格局，有自己的生态了。

虽然说现在还是有一定的遗憾，但能看出来，时期

V4发布稿结尾引的那句荀子的话，放在整个故事的语境里有点意味深长：

不诱于誉，不恐于诽，

率道而行，端然正己。

走自己的路，让他们说去吧！

这个节奏本身，也许就是他们最想传递的信息。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI5MDQxNzE1NQ==&mid=2247515563&idx=1&sn=68a2fddbaa449221799b773096a41578&chksm=ed56ff01fdaa37627aacbbd6a49990b3400d5dc61ac5acc90bfc554b5fd0fbec93c76e14b1a8&scene=90&xtrack=1&req_id=1777017612236286&sessionid=1777017859&subscene=272&clicktime=1777018545&enterid=1777018545&flutter_pos=14&biz_enter_id=4&ranksessionid=1777017864&jumppath=20020_1777017863867,WCWebImageBrowserViewController_1777017943346,20020_1777017952555,1104_1777018120444&jumppathdepth=4&ascene=56&devicetype=iOS26.4.1&version=18004728&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQSaS/9mneF+VG0N/JeOhK7BLVAQIE97dBBAEAAAAAAJWvDpmLZbAAAAAOpnltbLcz9gKNyK89dVj0c0bE41Ge/thVF3X6+rb4j4Y+MQeXDlQXYqBINkBZxWlt8vTdWVNSZzDy8UHczjng0MrqEur928evFynCVhrdy1Ce6WYZGFjPV4HrFX8EV/nnPD9sE8A1fv081w4jh6oQ00VXRoVh+qxFHBuEgDsBQkYleQg2DWmWk29oRuRwptOnipu94az6uPGcQN8w9li06Xfr3V9crn9CN9ccernzoac3MRgiji8T+BJOTy4cDQ==&pass_ticket=ljPNqTXyMrNK5yeuPrHuc8qi7nNg/CvZ+pn79iGa3anu6S7RNeQgVRh8q3Jtr8wR&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4e50b922-71e1-49b0-9add-1256f6235df6/4e50b922-71e1-49b0-9add-1256f6235df6/)
