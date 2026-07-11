# 为了平替Claude，阿里这次真拼了！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI3MzAzNDAyMQ==&mid=265789...](https://mp.weixin.qq.com/s?__biz=MzI3MzAzNDAyMQ==&mid=2657896234&idx=1&sn=2e37a21b4d5f9d9310a6adf915020fca&chksm=f11fbaef0e783eece7f98caf8174108c57fbc675e788e3006af95d2ec51bc3883f55fda23d88&scene=126&sessionid=1781497522&clicktime=1781498557&enterid=1781498557&forceh5=1&ascene=3&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ6ECY3jwE1HcjBbmlKLeSyRLTAQIE97dBBAEAAAAAAB/XBhPmfrYAAAAOpnltbLcz9gKNyK89dVj0HArDa9yydM1RvIMkKZboMAKUuXtMdsHScAVjtu79NmfD4KR2d9yM9Ath2G3qXP2mPIUDSxI6eHuA9hJkGT5l188OE4WQMHsNkEXwQ5XgKaWIC/hKrA+364U5aNcofgcr163BHIdAWm0LExnhBNkBLT4PLRruTUle2nmmZtNMfhN5+8UM7k6KjXoJNfPrWtoy4xAUM1QXhSYJfTVPCcjQvmNV27p5aNvtgtEIBGU=&pass_ticket=QMgTg3hrlBkT2OmkObgk7Hmhqw1kVUYafIshmgBH7GBji17Rm4gC7LSFt8NC1idS&wx_header=3)

小黑羊 特大号

不得不说，现在大模型的格局真是瞬息万变。比如，在AI编程界，大家都公认Claude是老大，尽管A社的做派很不讨人喜欢，但是挡不住他家东西好用。

![](.evernote-content/5EB3EA48-F898-4038-A0C3-F01913CDCD4B/20B2F776-C541-4348-9AB8-7D1738E822C8.png)

但是，就在前几天，阿里悄悄发了新旗舰模型Qwen3.7-Max，竟然跟不可一世的Claude杠上了。Qwen3.7-Max发布后，口碑一路攀升，在全球权威三方编程榜单Code Arena上，已经超越GPT-5.5、Gemini-3.5-Flash、GLM-5.1、Kimi-K2.6等一众模型，目前仅次于Claude系列。

![](.evernote-content/5EB3EA48-F898-4038-A0C3-F01913CDCD4B/16E389F1-4D13-4825-8468-5AA84ACBF5D8.gif)

甚至，还超过了Claude-opus-4.6，仅仅落后4.6-thinking 1分，GPT、Gemini们都被远远甩在后面。为什么大模型能力那么多，偏偏编程能力总被单拎出来说事呢？因为它几乎是当下模型智能水平最硬试金石，考验的是理解需求、拆解任务、逻辑推理、工程实现、错误修复和结果交付。更关键的是，代码能不能跑、功能是否完整，用户一眼就能验货，这不像生图或者写小作文，各花入各眼，不好评价优劣。所以，编程能力也成了大模型走向生产场景最瓷实的指标之一。而Code Arena，是目前全球最受关注的AI编程能力榜单之一，来自知名第三方盲测平台LMArena。这个榜单的评测玩法，是让开发者出题，要求模型从零生成完整、可交互的Web应用。用户在不知道模型身份的情况下，对两个模型的生成结果进行盲测PK，最终由真实投票形成排名。

![](.evernote-content/5EB3EA48-F898-4038-A0C3-F01913CDCD4B/1102433F-DA96-423A-8150-9E5224AFCCFD.png)

这次，千问的表现可谓「有点儿东西」，在全球开发者真实体验盲测中，一举冲进前四，打破了Claude长期霸榜的格局。而且，Qwen3.7-Max也成为榜单中唯一突破1540分大关的国产大模型。

![](.evernote-content/5EB3EA48-F898-4038-A0C3-F01913CDCD4B/57F33B7B-E2F7-4800-8783-FF60F9D93D8D.jpg)

再给大家补充点背景信息，Qwen3.7-Max主要面向Agent场景，最擅长干的就是编程、智能体、长程任务。尤其是长程任务，相当牛掰。在Qwen官方给出的实际例子中，千问3.7在一个全新的芯片平台上，通过自主编程和超1000次工具调用，连续不间断地跑了35个小时，实现了一个关键内核的自我进化，推理速度较原版本提升10倍。

![](.evernote-content/5EB3EA48-F898-4038-A0C3-F01913CDCD4B/0727500F-2A8C-4F1E-93E7-64A9987BC63F.png)

注：细看这张图很明显，其它模型跑一会儿就躺平了，只有Qwen一口气肝了30多个小时。很多开发者也评价它「长程自主执行能力惊艳」，适合作为Agent的基座模型。还有AI机构横向测评了Qwen3.7-Max、Claude 4.7 和GPT-5.5，给出的结论是千问3.7相比上代提升最大，推理成本最低，在速度和生成质量上都有明显优势。

![](.evernote-content/5EB3EA48-F898-4038-A0C3-F01913CDCD4B/D10532D0-A145-4047-BEDD-77192C37B61A.gif)

注：测评机构利用三个模型编写一个会玩俄罗斯方块并能自我训练的机器人，每个模型都可以读取自己的代码、运行基准测试，并在 10 轮迭代中重写和优化自己。结果，Qwen3.7-Max在每个维度都赢了。当然，所有这些，我觉得还不够。

我就盼着，国产模型们有一天能够把Claude彻底拉下马，让Y的求着我们用

。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI3MzAzNDAyMQ==&mid=2657896234&idx=1&sn=2e37a21b4d5f9d9310a6adf915020fca&chksm=f11fbaef0e783eece7f98caf8174108c57fbc675e788e3006af95d2ec51bc3883f55fda23d88&scene=126&sessionid=1781497522&clicktime=1781498557&enterid=1781498557&forceh5=1&ascene=3&devicetype=iOS26.5&version=18004a2f&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ6ECY3jwE1HcjBbmlKLeSyRLTAQIE97dBBAEAAAAAAB/XBhPmfrYAAAAOpnltbLcz9gKNyK89dVj0HArDa9yydM1RvIMkKZboMAKUuXtMdsHScAVjtu79NmfD4KR2d9yM9Ath2G3qXP2mPIUDSxI6eHuA9hJkGT5l188OE4WQMHsNkEXwQ5XgKaWIC/hKrA+364U5aNcofgcr163BHIdAWm0LExnhBNkBLT4PLRruTUle2nmmZtNMfhN5+8UM7k6KjXoJNfPrWtoy4xAUM1QXhSYJfTVPCcjQvmNV27p5aNvtgtEIBGU=&pass_ticket=QMgTg3hrlBkT2OmkObgk7Hmhqw1kVUYafIshmgBH7GBji17Rm4gC7LSFt8NC1idS&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0a8223ff-5864-409a-bca8-a4ecdae491e3/0a8223ff-5864-409a-bca8-a4ecdae491e3/)