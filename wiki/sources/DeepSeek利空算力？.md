---
title: DeepSeek利空算力？
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/DeepSeek利空算力？.md
tags: [AI技术, 教育]
updated: 2026-06-27
---

---
title: "DeepSeek利空算力？"
source: evernote
type: note
export_date: 2026-06-26
guid: c6fdccab-873b-4ccb-9f70-e2531186bce8
---

# DeepSeek利空算力？

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkyMTU4OTE2OA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=MzkyMTU4OTE2OA==&mid=2247490134&idx=1&sn=89ab76990095744564b9fbde6bab0978&chksm=c04381870871560d6be9a9261f6c1b84db368aeeaa46b87c1b4a25dd4bacd392af21f143196c&mpshare=1&scene=1&srcid=0127eUF4OxeWO7uLVXJpkDsq&sharer_shareinfo=1b1efd95c2ab68b52de310ffd2b1d4e3&sharer_shareinfo_first=1b1efd95c2ab68b52de310ffd2b1d4e3&from=groupmessage&isappinstalled=0&clicktime=1737970834&enterid=1737970834&ascene=1&devicetype=iOS18.2.1&version=1800382a&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQWexX/G2oDT9sqt6MBHP6PRLsAQIE97dBBAEAAAAAAOjhMM5Dyl8AAAAOpnltbLcz9gKNyK89dVj00JVU3Aj6aUjN4YmJo1jTikWWRL1197ld1EUN9YdJyMhTmBJ/ega2zg5coQVyyIu50o8Z8aZtARTdM+JSz6HkICxGAAMudgSYPUVNIsj2qCg46KsFvA/3+iXguecgad3IqCJx6VJ//Uu2mOzEVo6v6fBSjPyp8vUR7MwJncauDC8Vo41JOsrPUEER7QuN+OyXaIprhADzbB7buokDfz3MMoGzMaM1NTb0Pev9teNydmQByiCiQGymWTS+cs7DxtPlSeAjqjtI&pass_ticket=WkLtYcWrh9ayXPRIDrQQVVIfTjuZA0fahFJQMzPQoZaD5+quMXnYYFhJQSagRq71&wx_header=3)

信息平权 信息平权

其实具体逻辑，从12月deepseek v3到这周的r1，我们前前后后分析过很多次了，不妨总结梳理下

1. 海外广泛引用的550万美金是v3，而不是r1的训练成本，且550万只是v3实际训练成本的零头。v3论文原话：**上述成本仅包括DeepSeek-V3 的正式训练，不包括与架构、算法、数据相关的前期研究、消融实验的成本**。社群内一位算法工程师就曾说“v3**用了幻方自己的r1模型生成数据**，这个部分的反复尝试要不要算在成本里呢？”一个意思。

2. 前沿探索和后发追赶，所需要的算力本就不是一个量级。表现为**训练同一代模型所需算力每隔N个月就是指数级降低。原因包括算法本身的进步（FP8、混合MoE）、算力的持续通缩、复现方法如蒸馏等对数据的浓缩。**最关键的是，探索就意味着会有浪费，而后发追赶“站在巨人肩膀上”本就可以规避浪费。就比如o1的训练成本肯定远超GPT-4，幻方r1的训练成本肯定也超过v3。而从o3到o4/o5，从r1到r2/r3，训练算力只会更多。

3. 单次训练降本了，不代表整体训练成本会下降。训练效率提高，实验室就减少投入吗？不会，**真实逻辑是：基于更高效率，榨干算力，去攫取更大收益**。就拿幻方来说，infra优化降本能力这么强、提前囤卡也挺多、没怎么扩张API服务专注于研究与训练的情况下**，依然还在缺卡。**横向对比之下，北美某些花了更多钱的实验室，的确显得很尴尬...但他们之后就降本增效吗？不会。消化吸收幻方开源的方法+比幻方多得多的算力=攫取智能的更大提升。训练算力最应该担心的是撞墙，算力使用效率提高，反而可能是提高了模型本身的天花板。

4. **幻方代表的是整个开源相对闭源的一次胜利。**对社区的贡献会快速转化为整个开源社区的繁荣。如果真的说利空的Loser，那可能是闭源模型。中国这一点已经提前经历了，被Llama支配的恐惧，跑不过Llama3的中国闭源模型公司被迫倒闭、转应用、转开源。而今天中国开源打到了北美闭源...如果现在还不如r1（以及即将到来的r2 r3），那这家公司的API价值基本归0。**但说实话这个过程的确会让模型训练参与方快速缩减。**

5. 最关键的，以上讨论都是训练，而未来显然更大需求来自**推理**。有一点被大家忽略了，**幻方对推理成本的消减，比训练来的更为震撼。**今天大家都看到了**AMD宣布支持幻方v3**，用我们嘉宾Y博的话就是：DeepSeek架构的优雅之处就在于，和标准的transformer架构比较起来, 并没有引入特殊的算子。理论上可以相对轻松支持各种类型卡...（这也是被GPU禁运逼出来的）大家体会下这句话的分量，以及对于CUDA的启示...幻方这帮人都是手撸算子的天才...

推理成本降低，对算力是利好还是利空？比训练更好理解。请对比：刚推出来贵到没人用的**o1**，以及掀起API价格战之后的**豆包。**推理成本的降低大概率会带来应用的繁荣，反而会拉动更大的算力需求。

这里再引用下星球Y博的评论，现在回头看非常前瞻：DeepSeek-V3将支持私有部署和自主微调，为下游应用提供远大于闭源模型时代的发展空间。未来一两年，**大概率将见证更丰富的推理芯片产品、更繁荣的LLM应用生态。**

6. 如何平衡**北美仍在疯狂的基建，和过去浪费的投资？**美国的确**CSP仍在疯狂抢电，都抢到2030年去了**。其实各大CSP过去2年千亿美金砸下去，没有一家单纯是为了训练，基本都是自身业务需求+推理业务增长驱动。只有微软为OpenAI准备的算力credit、AWS算力租赁给了下游客户用于训练、Meta/xAI部分算力用于自身训练，但算力大头都是因为自身的推荐系统业务/自动驾驶业务本身需求。以及微软已经相当于拒绝了Sam Altman继续All in的诉求，转而聚焦回报更确定的推理（Satya亲口这么说）。

因此幻方这件事对北美CSP来说，客观来讲，过去某些训练投入的确是打水漂了。为冒险、探索新市场付出的必要成本。但看未来，开源的整体繁荣一定最终是利好这些“中间商”。之前我们阐述过，他们其实不是亲自冒险的矿工，他们只是铲子的搬运工，以及基于这些模型（无论开源or闭源）建立更具商业价值的应用生态。卡并不只是用于训练，**越来越大比例会挪到推理**。假如训练的高效让模型更快进步，应用生态更加繁荣，他们怎么可能不继续投呢？

最后，继续引用下《the bitter lesson》：长远来看，**算力才是真正的决胜因素**。历史的经验一次又一次地告诫我们，AI研究者常常试图将人类的知识灌输到AI算法中，这种做法在短期内通常有效，并且带来个人成就感和虚荣心。但长远来看，它会造成瓶颈，甚至阻碍进一步发展。最终的突破性进展往往源于一种截然不同的思路，即通过**搜索**和**学习**来扩展**算力规模**。而那些最终的成功往往伴随着苦涩，难以被下咽，因为算力的成功，意味着对我们以人类为中心的固有思维和虚荣心，是一记响亮的耳光。

（欢迎加入社群继续讨论这个话题，各种角度都有，此外今天还有很多重要更新）

![](attachments/d93a6eb57948a379.jpg)
