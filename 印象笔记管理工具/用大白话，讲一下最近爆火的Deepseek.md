# 用大白话，讲一下最近爆火的Deepseek

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI5MDQxNzE1NQ==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzI5MDQxNzE1NQ==&mid=2247509334&idx=1&sn=b89eab8fb0bf367c4adc568dea5c9ca4&chksm=ed860433078abaf377011667f417db8307da34e1ea0795dd9fdf75754a4a35e5edfe717562de&scene=90&xtrack=1&sessionid=1737978098&subscene=272&clicktime=1737978565&enterid=1737978565&flutter_pos=36&biz_enter_id=4&ranksessionid=1737976240&ascene=56&devicetype=iOS18.2.1&version=1800382b&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ4Mk7muNPerrlEO22tuVdKBLYAQIE97dBBAEAAAAAANM4OJHeYnYAAAAOpnltbLcz9gKNyK89dVj0XIKViw7lTonJ+sBqzGyzavUAmnFLKNOc7kmiGW33EPcHGJNcN4xp0l0mu6lkSfFO3e7D7DNrS4c3W7ruY1yq1XQ4UUdk0wUJ+VnbVKuxjYhubx5dg+93jgnwYaWKDEaGyYGxCGyXgWjoTRs239U5SGj0bJT/nACJ0BkUT27GgdvDhz3Y6tYlK80yxRHOzmX6+T4Cm4vpGsp3SilbvcCdAQ/0nlxA9Q/bQ4NegFDgpNX0fQ==&pass_ticket=h4vr040Yvfc70siiOUH1Eqit083oJsz3Qz99BwucJLsqbaiPXasRrnE1uiOpyuvq&wx_header=3)

原创星海老局星海情报局

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/38FD2173-AEC7-45E8-891C-3CD70B0AD0C7.gif)

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/5BB9695A-F2B9-4DBC-B56B-78C3FD242160.jpg)

1957年10月4日，苏联成功发射了"斯普特尼克1号"人造卫星。消息传出后，从华盛顿到伦敦，整个西方都陷入了震惊和恐慌——因为这意味着：西方国家开始在技术上落后于非西方的国家。

**从此之后，"斯普特尼克时刻"也就成了一个专有词汇，特指那些使得西方国家陷入技术落后局面的事件。**

现在，"斯普特尼克时刻"又来了：顶着各种制裁，用着远低于美国科技企业的预算，一家中国企业开发的AI大模型，竟然实现了近似于GPT-4o大模型的效果。

更重磅的是：就在今天中午时分，DeepSeek已经登顶了中国和美国的应用商店，超过了ChatGPT，成为了最受欢迎的AI应用。这个历史性的时刻，至少在目前十年内绝无仅有。

这家中国企业，叫幻方量化。他们开发的AI大模型，就是这几天爆火的Deepseek（深度求索）。《黑神话：悟空》背后的那个男人，Yocar冯骥将其称为“国运级别的科技成果”。

**今天，我们就来聊聊Deepseek，看它为何能成为AI界的"斯普特尼克"。**

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/90FBAF4B-1D0D-4D96-98DC-694E5858CB10.jpg)

**不传统的技术路线**

从技术原理上来说，Deepseek的成功，尤其是最新一代deepseek R1的成功，来自于它所采用的RL强化学习策略，这是它以极低的成本却可以实现和GPT-4o差不多效果的根本原因。

**要理解这种颠覆性，得先看清传统AI的局限。**

在之前的文章里，我们就认为当下AI的故事很可能已经讲不下去了——因为以GPT为代表的传统AI，其策略的本质是"在人类监督下的猜字谜游戏"——GPT们其实并不会思考，它们虽然会生成看上去还挺靠谱的回答，但它们做出这些回答并不是它们了解事物运行的原理，而是这样回答有更大概率被人类所接受。

这种猜字谜的游戏，最多也就是生成一些"看似靠谱实则无法深究"的东西，根本没有办法投入现实、转化为生产力工具。早期绘画AI经常把人画出六个指头也是类似的原因——AI根本不知道人的手掌上应该有几个指头，它只是生成一个"乍一看还可以"的东西。

**但deepseek不一样，deepseek是真的会“思考”，或者说“推理”的。**

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/9AD4A74C-D6E1-4674-B001-2C83984BE5C9.png)

以现在爆火的deepseek R1来说，它完全抛弃了那种"猜字谜"的训练方式，转而采用了之前在围棋和智能驾驶领域常用的RL策略（强化学习）。

如果说以前的策略是人类告诉AI什么是对的什么是错的，AI只是在人类的指导下对人类进行模仿。那么RL就是人类仅仅起一个"引进门"的作用，剩下的"修行"就全部靠AI自己慢慢学习了。

这种"修行"在最初阶段或许很笨拙，但越训练AI的能力就越强——关键在于AI不需要遵循人类的生理极限。人类要吃饭睡觉，但AI不用，在高性能芯片的加持下，AI训练一年所见识过的棋局、游戏，往往比一个职业棋手、职业电竞玩家十辈子见过的都多——老司机哪怕开一辈子车，最多也就开个几百万公里。但自动驾驶AI只要开始训练，公里数就是以亿为单位计算了。

简而言之就是：RL策略，是真正地让AI学会认识世界、了解事物规律，而不是亦步亦趋地迎合人类的口味——**这也就是为什么很多人在看到deepseek的成功后都认为2025年将会是RL强化学习的元年。**

没办法，RL策略现在看来确实是太诱人了。

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/D59B89C5-786F-4272-8E56-61CB66F10884.jpg)

**技术突破带来的降本增效**

当技术路线换道超车，成本结构就会发生核爆式变革。

因为底层的技术路线上颠覆了以GPT为代表的传统AI，所以deepseek R1把性价比拉高到了一个不可思议的程度——相比起硅谷那群人动辄数亿数十亿美金的投资和数万张显卡的超级集群，我们仅仅靠着2000多张显卡和600万美元左右的成本就实现了近似乃至更好的效果。

用美国META公司一位匿名员工的话来说：**"META内部一个负责AI项目的高管年薪拿出来，就足够训练deepseek了，而这样高薪的高管，META有几十个。"**

......我只能说：跟着这群虫豸在一起，怎么能搞好AI呢？

同时，这波操作直接改写了游戏规则。deepseek的颠覆式创新也向外界传播了一个信息：不需要那么高的投入，也不需要那么多英伟达的GPU，你也可以做出很棒的大模型——OpenAI训练GPT-4耗费约6300万美元和25000张A100显卡，而Deepseek R1仅用600万美元达到可比效果，甚至可能用的还是国产显卡。

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/2836C991-592D-4DBE-9D1A-4DEFC3009261.png)

数据最能说明问题：RL策略使模型在对话轮次、任务复杂度等维度实现80%的收敛速度提升，数据利用率提高5倍以上。

**黄仁勋一觉醒来，感觉自己家的地基被人刨了，因为AI的泡沫眼看着就要被戳破了**——在传统技术路径下，90%的算力消耗在试错过程中，而Deepseek的自主学习机制能将无效训练降低60%。RL策略对并行计算的需求较传统架构下降40%，这使得国产显卡在特定计算任务中能达到英伟达GPU 75%的能效比。

这就带来了更大的打击：算力市场上的格局将会被重构——随着华为昇腾910B等国产芯片在RL框架中表现持续优化，美国试图通过A100/H100禁运遏制中国AI发展的策略正加速失效——国产显卡又不是不能用，那我为啥还要高价进口呢？既然如此，那么美国的"小院高墙"的制裁路线还有意义吗？靠芯片靠GPU还能卡住东方大国的脖子吗？

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/77F724FD-060C-4615-83EE-6BF7F1D43268.jpg)

**deepseek的爆火背后的几点观察**

毫无疑问，deepseek确实是取得了巨大的成功，而且使用体验的确远超GPT系列的大模型，尤其是R1版本特有的思考过程，真的不再是单纯模仿人类，而是真的有自己的想法，甚至比人类更全面、更周密。

**综上所述，老局有这么几点观察：**

第一，RL路线的含金量已经不再需要怀疑，必然会是下一个阶段AI大模型的核心策略。这也意味着我们向着真正的“人工智能”开始了前进。

第二，靠着堆显卡、堆资本来发展AI的“Scaling law”的价值需要被重新审视，这不意味着Scaling law的崩盘，反而可能是Scaling law的二阶段形态。因为虽然定价已经虚高了，并不需要这么多钱也可以实现很棒的效果，但不意味着英伟达就是割韭菜——不得不承认，如果有更好的条件，AI必然会有更大的进步。

第三，AI行业可能真的没有什么核心的护城河，模型技术的超越将会是常态。今天deepseek超越了OpenAI，明天指不定有人也能超越deepseek——整个行业的格局没有固化，中美AI竞争的大局还早着呢。

第四，deepseek的成功确实意味着之前一个阶段里美国的“小院高墙”制裁策略失效了。但对我们来说，硬件上的突破和国产替代之路远未结束。国产GPU还要继续发力，这是基础性的力量，不能因为deepseek的成功，就觉得咱们已经不需要再警惕英伟达的技术优势了。

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/F8FBDD53-8017-4B73-95E2-259B8B43B81D.png)

**····· End ·····**

**星海情报局 系统研究**

**中国制造与国****产替代**

**专注中国产业崛起故事**

**▲关注产业资讯，破解科技密码**

**追赶先进技术风口，看中国制造的星辰大海**

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/235F99AB-855F-4A30-ACF7-4492DC481770.jpg)

入驻媒体平台

36Kr/ 观察者网风闻社区/ 网易

虎嗅/ 雪球/ 腾讯新闻

![](.evernote-content/2FC032B1-5C95-4044-BC79-17ABABAB8C17/C1DB772B-7C71-4152-98ED-4074136AD166.gif)

个人观点，仅供参考

修改于

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI5MDQxNzE1NQ==&mid=2247509334&idx=1&sn=b89eab8fb0bf367c4adc568dea5c9ca4&chksm=ed860433078abaf377011667f417db8307da34e1ea0795dd9fdf75754a4a35e5edfe717562de&scene=90&xtrack=1&sessionid=1737978098&subscene=272&clicktime=1737978565&enterid=1737978565&flutter_pos=36&biz_enter_id=4&ranksessionid=1737976240&ascene=56&devicetype=iOS18.2.1&version=1800382b&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ4Mk7muNPerrlEO22tuVdKBLYAQIE97dBBAEAAAAAANM4OJHeYnYAAAAOpnltbLcz9gKNyK89dVj0XIKViw7lTonJ+sBqzGyzavUAmnFLKNOc7kmiGW33EPcHGJNcN4xp0l0mu6lkSfFO3e7D7DNrS4c3W7ruY1yq1XQ4UUdk0wUJ+VnbVKuxjYhubx5dg+93jgnwYaWKDEaGyYGxCGyXgWjoTRs239U5SGj0bJT/nACJ0BkUT27GgdvDhz3Y6tYlK80yxRHOzmX6+T4Cm4vpGsp3SilbvcCdAQ/0nlxA9Q/bQ4NegFDgpNX0fQ==&pass_ticket=h4vr040Yvfc70siiOUH1Eqit083oJsz3Qz99BwucJLsqbaiPXasRrnE1uiOpyuvq&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9840bb18-96d5-48e7-952b-67169284ebea/9840bb18-96d5-48e7-952b-67169284ebea/)