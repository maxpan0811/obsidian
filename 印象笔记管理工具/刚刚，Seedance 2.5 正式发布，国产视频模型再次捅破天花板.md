# 刚刚，Seedance 2.5 正式发布，国产视频模型再次捅破天花板

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5MjAyNDUyMA==&mid=265109...](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=2651095111&idx=1&sn=faf986f09c90d79709ff0ec0e7aedc18&chksm=bcd1517c7d135608a25e52b5081c850db01489c26c005aad735b3f5eaea1553caa4f3c1d250c&scene=90&xtrack=1&req_id=1782205385197482&sessionid=1782205475&subscene=93&clicktime=1782205488&enterid=1782205488&flutter_pos=1&biz_enter_id=4&ranksessionid=1782205385&jumppath=MMFlutterViewController_1782205477494,1104_1782205479144,MMFlutterViewController_1782205480778,1104_1782205482161&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b29&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQLI2hKtzBsGTjwlbtAf/HuRLTAQIE97dBBAEAAAAAAFLiMrQj9FwAAAAOpnltbLcz9gKNyK89dVj01tAARC8QsKdWgCHPpOyea1OjObDc40RtJDEaDoAwPRP5CWXPb0k1TBWrYLaP9CulVzPmFfGbVd5TC2UnJy0afYedEXObXb2AyyNWba18yt05c++JLObbHE/V1GDPZwm6n4hcZNGg3isCF3qJiEIbS1TwKKv1YNh3yPIcQFsm280K24+hcuBIk17Pga8ecYPCI5LzPCXl5wUDQqAxhpUrN5rdiXDdxZ7LpsDPZB4=&pass_ticket=N/GOdkUqqbyI0HVwWTaQm6nmGbA4gL8TcDauwZePL1olS976u3ZIiOPkcu/NmI+6&wx_header=3)

Original发现明日产品的 APPSO

180 万亿。这是截至今年 6 月，豆包大模型的日均 token 调用量。相比最初发布足足增长了几个数量级，且完全没有放缓的迹象。火山引擎总裁谭待在 2026 火山引擎 FORCE 原动力大会上公布这个数字时，台下更是掌声雷动。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/727FA77E-887B-4379-ABFC-82E509E22A42.png)

更值得注意的是市场份额。在公有云大模型市场，火山引擎把份额提升至 49.5%。每消耗两个 token，就有一个是火山引擎提供的。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/8721F21F-3C94-4DD8-A91E-10A4E2A38C2D.png)

去年 12 月，「万亿 token 俱乐部」还只有 100 家企业，现在已经暴涨至 200 多家。足够夸张的数字背后，反映了 token 已逐渐成为像水电一样的基础消耗。

越来越多企业不再把大模型当作一个「试试看」的新工具，而是开始把它接进核心流程——写代码、做视频、跑分析、做客服、做决策。豆包 2.1 Pro：既 SOTA，也划算这场大会真正的主角，是刚发布的豆包大模型 2.1 Pro。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/1C12CB2A-4E5F-428A-B968-41656288A88D.png)

按谭待的说法，这是一个突破了「生产质变点」的旗舰模型，意思是它写的代码能真正交付、进入企业研发流程，而不是停在「玩具」阶段。coding 能力上，几个硬榜单它都拿得出手。Terminal Bench 这种最贴近真实研发的终端编程评测，模型要在命令行里端到端跑完一整个工程任务，2.1 Pro 和 Claude Opus 4.7 基本持平，进了全球第一梯队；

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/4BFEE875-369B-4E10-82C3-862B07C47994.png)

覆盖五大学科科研问题的 SciCode 拿到 59.8 分，超过 Opus 4.7；从需求文档出发从零生成整个可运行仓库的仓库级评测，拿到 47 分。现场还演示了个硬核 case：让 2.1 Pro 围绕一个 16×16 PE 的微型模型，连续跑 18 个小时、迭代九轮，最终写出六个核心模块、1300 多行 RTL 代码——芯片设计里最严谨的环节，通常要 3 到 5 名资深工程师干上数周——

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/6433390E-B467-43A2-9D21-84BF1DDB6FEA.png)

而且不只是生成代码，还跑通了仿真测试、综合检测，最后通过了手写数字识别验证。Agent 能力上，在 OpenAI 那套覆盖九大行业 44 种职业的 GDPval 真实经济价值评测里，2.1 Pro 拿了国内第一；评测 AI 用真实 MCP server 和工具能力的 MCP Atlas 上，全面超过 Opus 4.7。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/2CCEF9EA-5492-46BB-942B-8951ACF8B7A4.png)

价格是另一记重拳。百万 token 输入 6 元、输出 30 元，缓存命中只要 1.2 元，对比 Claude 同系列成本降了接近 80%，另有个价格只要 Pro 一半的 turbo 版本。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/EFB1F505-D18C-4FAE-B3F6-0776DB3151C8.png)

Seedance 2.5 登场，AI 视频终于不止 15 秒了模型矩阵的下一块是视频，也是发布会的重头戏。今年 2 月发布的 Seedance 2.0，是中国第一个全球 SOTA、也是第一个跨过「生产质变点」的视频生成模型。谭待表示，在它出来之前视频模型更像玩具，5 到 10 秒的 UGC 内容为主；2.0 之后，15 到 30 秒的广告、影视、科普短片被全面解锁。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/173ADE7F-19A1-4A00-B70E-BCD5CA353DE4.png)

这次先给 2.0 上了个大升级：原生 4K。以旗袍广告作为一个典型案例，720P 下，刺绣线迹和面料肌理不够清楚；用超分把 720P 拉到 4K，画面虽然锐化了，但细密绣线反而被平滑掉，质感更差；而原生 4K 从生成阶段就保留更高密度的有效信息，发丝、丝线走向、面料纹理都清晰完整。Seedance 2.0 原生 4K 还率先支持 4K 10bit 高位深，色彩层次更丰富，给后期调色留足空间。但 4K 只解决了画质。更长、更多参考、更强编辑这三个挑战，得靠新主角。万众期待之下，Seedance 2.5 登场，目前已在内测尾声，预计 7 月初正式见面，三个升级全是「全球第一/最多」：

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/AD6D5E6C-701E-4ADC-BD78-DC9EE4B47379.png)

单条视频生成长度最高 30 秒，全球第一。市面上同类模型最多只支持 15 到 20 秒，这次直接突破瓶颈，镜头表达更连贯。多参考能力支持 50 个全模态素材联合输入，全球最多。现场一次性输入十多位演员的图像资产，让模型自己编排。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/74759661-78BD-4F68-95B5-FDC4CE4717E3.png)

更灵活的视频编辑：可以在整体画面不变的前提下，对局部单独修改——微调背景、更换商品、更换模特。现场一个口红广告演示，直接把「挑口红」这个困惑给解决了。它还能稳定承接专业创作。现场输入一个接近 10 万面的宇宙飞船白膜加一份渲染材质参考，让模型生成渲染视频模拟镜头，飞船主体轮廓、比例、复杂结构在镜头缓慢推进中都稳定保持。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/DCCE6D27-83D4-469B-A6A8-D07B16C33128.png)

在实体产业，Seedance 2.5 能自动生成多语言产品视频说明书，能给具身智能合成多场景多视角的高质量训练数据，能给自动驾驶合成极端天气、罕见路况这类案例补上训练盲区。当视频模型跨过生产质变点，它积累的对物理世界的理解，正在成为世界模型的重要基础。模型只是入口，生产系统才是终点视频之外，图像和音频这两块也各自上了新东西。图像这边接棒的是 Seedream 5.0 Pro。年初发布的 Seedream 5.0 Lite 已经在帮用户把普通产品图转成高级广告海报、把线稿上色成完整插画，5.0 Pro 则是智能水平上的全新尝试。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/85E948BA-DDAF-4564-9B12-392F57D35DB4.png)

最直观的是交互式精准编辑。创作者既能用语言描述空间关系，也能直接在画面上标记圈选。比如一张图里，把树枝上的松鼠移到左下角树桩、在右下角加两只小猫的结婚照、把小黄狗移到左侧——模型能识别箭头和高亮块，理解意图、定位元素、生成符合要求的画面。设计师随手画的草图线稿，它也能编辑成符合意图的视觉效果。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/924F4BC3-D3B0-49EB-A80A-0E39B0711380.png)

另一个能力是多图层分离。圈选点选任意区域、任意颗粒度，小到一行字、大到整个版面，都能拆分输出成独立图层。把人物从画面拿走后，模型会自动智能填充背景；还能递归拆分，对拆出去的人物再拆出帽子、滑板，方便二次拖拽缩放编辑。还有个一直让大模型头疼的能力，高密度信息呈现。复杂图表、多层结构、甚至一整页 PPT 的信息量，都可能被完整塞进一张图，模型还会自动优化版面、保持审美。它还支持英语、西班牙语、阿拉伯语、日语、韩语等 10 余种主要语言，并自动适应每种语言的排版习惯。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/8DF9AD40-B8D8-4714-9F46-376FAAE77599.png)

Seedream 配 Seedance 还能一加一大于二。以「天问一号发射」科普视频为例，先用 5.0 Pro 把探测器外观、发射、着陆几个关键阶段准确生成，再喂给 Seedance 2.5，就得到一个高品质的 30 秒科普视频。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/35F842D3-F4FF-4975-AC34-8D4C5EF3B1A0.png)

音频方面，Seed-Audio 1.0 支持情绪、口音、背景音、氛围音、拟音特效一次直出，做到影视级成品音效。落到产业侧，奔驰、东风都在基于豆包大模型探索智能座舱的语音交互。

![](.evernote-content/A93DDAB6-A1E2-4653-89AB-FA9E3F5CE25B/ECA2C62C-7891-41C3-9CDA-741AA7B3A9E1.png)

奔驰中国研发负责人在现场视频里提到，已经把豆包大模型集成进新款纯电车型，让车里的对话更自然、更能读懂用户意图和情绪。而开头所说的 180 万亿 token 指向的不只是一个规模数字，更是一条正在不断延伸的能力曲线。企业每天把客服、营销、研发、内容生产、办公协同、数据分析等任务交给模型处理，模型也在这些高频调用中持续暴露问题、修正偏差、积累经验，逐步逼近真实生产环境的要求。这背后，是一场长期的能力攀登。字节跳动 CEO 梁汝波在大会上提到，攀登 AI 高峰是字节当下最重要的事情——收缩业务宽度，把精力重点聚焦到 AI，并在 AI 内部进一步聚焦于提升模型能力。火山引擎正是这个方向的对外出口。它把字节内部沉淀的模型能力、工程体系和应用经验，转化为云服务、模型 API、行业解决方案和工具链，交付给企业使用。高峰还在前方，但路径已经清晰。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&mid=2651095111&idx=1&sn=faf986f09c90d79709ff0ec0e7aedc18&chksm=bcd1517c7d135608a25e52b5081c850db01489c26c005aad735b3f5eaea1553caa4f3c1d250c&scene=90&xtrack=1&req_id=1782205385197482&sessionid=1782205475&subscene=93&clicktime=1782205488&enterid=1782205488&flutter_pos=1&biz_enter_id=4&ranksessionid=1782205385&jumppath=MMFlutterViewController_1782205477494,1104_1782205479144,MMFlutterViewController_1782205480778,1104_1782205482161&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b29&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQLI2hKtzBsGTjwlbtAf/HuRLTAQIE97dBBAEAAAAAAFLiMrQj9FwAAAAOpnltbLcz9gKNyK89dVj01tAARC8QsKdWgCHPpOyea1OjObDc40RtJDEaDoAwPRP5CWXPb0k1TBWrYLaP9CulVzPmFfGbVd5TC2UnJy0afYedEXObXb2AyyNWba18yt05c++JLObbHE/V1GDPZwm6n4hcZNGg3isCF3qJiEIbS1TwKKv1YNh3yPIcQFsm280K24+hcuBIk17Pga8ecYPCI5LzPCXl5wUDQqAxhpUrN5rdiXDdxZ7LpsDPZB4=&pass_ticket=N/GOdkUqqbyI0HVwWTaQm6nmGbA4gL8TcDauwZePL1olS976u3ZIiOPkcu/NmI+6&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/417c40b0-0421-42a7-b02b-4d8d5f803233/417c40b0-0421-42a7-b02b-4d8d5f803233/)