# 【Atom x AWS出海增长系列02】如何让产品被AI推荐——Topify创始人拆解GEO的底层逻辑

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg5NDc5NDkzMA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzg5NDc5NDkzMA==&mid=2247484394&idx=1&sn=a60994122d6aae355cc9570ec65ee769&chksm=c1b068130d002ae6b85062613cc2473e65bbc7607b8f3d155cf6812ba848d536c5c672299aee&mpshare=1&scene=1&srcid=0525KnRiwUAhC2vVpQI7vYCp&sharer_shareinfo=dcf1175f0582846508147f889a73aeaf&sharer_shareinfo_first=53fa6f9433edc43b9c70f3864edc9278&from=groupmessage&isappinstalled=0&clicktime=1779712567&enterid=1779712567&ascene=1&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2RjtmJryqQG/rmYUWo0jIhLnAQIE97dBBAEAAAAAABcBIjVdc/UAAAAOpnltbLcz9gKNyK89dVj0G1wUwNLg9wZYFwnqdH82E1mx8q+0srcylfdlfglPGWfRT0SZba96sYgK4Q766iCqYeHWKB6khU0Qcvw4YgqRbdYSC34ujs+2LuMKhfi+8KtXBde5xjLqWTFe3/zXSHC8zWdW0oq2hN7T1H0VAHf91zVzkuRxjiqaWJMFCi0edEYqmrMgtBURYx3+CSzAcA7TSgWUOP9Q+T0wcihn4HFv2zMJWdbTQbvGnE+lCoOnIBvyroAD2HnKcRHeDAoXVaMovA==&pass_ticket=HQdBFpLXt2lZ10OZSe8hlvuNpMM9/0ABJAt1YaYbw+obntkE4pYNzhfiLms0auqB&wx_header=3)

Original科技最前沿的Atom Capital

**写在前面**

做出海的AI创业者，多半都经历过这样的时刻——产品做得不错，但流量迟迟起不来；SEO好不容易冲到第一页，AI推荐的却是竞品；花了不少预算投广告，ROI却一塌糊涂。在AI出海这条路上，"增长"始终是最让人焦虑的命题。互联网大厂时代验证过的增长打法——砸预算、铺渠道、堆人头——放到今天的AI创业公司身上，正在批量失效。新的增长杠杆到底长什么样？带着这个问题，我们联合亚马逊云科技Startups策划了AI出海系列的第二期闭门工作坊，聚焦"全球增长"这一核心命题，邀请了三位一线出海增长操盘手，分别围绕低成本流量获取、GEO、以及出海GTM如何0到1，分享他们在实战中真正跑通的方法论和关键决策。本篇为这个分享系列的第二篇，来自Topify AI创始人陈家棋Jacky——当用户的搜索入口从Google变成大模型，品牌如何让AI找得到你、看得懂你、信得过你、愿意推荐你？![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/AB0A042C-6146-48D8-A421-DD773C27CD9B.jpg)![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**01****GEO的第一课：忘掉"铺量"这个词**

很多人听到GEO，第一反应是"在网上大量发内容，让AI抓到"——用AI批量生成文章，往各个平台一扔，坐等被引用。

实际上，Topify AI曾经拿新站做过详细测试，发现这类内容根本不会被AI引用。这背后的核心原因是LLM的推荐机制与传统搜索引擎有本质差异。谷歌的逻辑是"匹配关键词+权重排序"，内容铺得多确实能增加被索引的概率。但LLM在回答用户问题时，做的是一件更接近"判断"的事——它要在十几个信源之间做交叉验证，确认一个品牌在某个细分问题上是否真的可信，然后才决定是否推荐。

换句话说，AI更像一个极度理性的人。你要说服它，得摆事实、给证据、从多个渠道佐证你的品牌价值。靠重复轰炸去"攻击"它，在现阶段大模型的反注入机制下，不仅无效，反而可能伤害品牌。

**这是做GEO之前需要建立的第一个认知：你面对的不再是一个爬虫，而是一个有判断力的"裁判"。** 用做SEO的惯性去做GEO在AI搜索环境里会适得其反。正确的做法是先搞清楚AI的信任机制，然后围绕这个机制去组织你的品牌信息。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)**02****SEO没做好，GEO零可能**放弃做SEO的惯性是不是意味着SEO可以直接跳过？恰恰相反。Topify的判断很明确：SEO是地基，GEO是大楼——地基不打，楼盖不起来。

因为AI在很多场景下仍然依赖搜索抓取和公开信源获取信息。你的网站如果连谷歌爬虫都进不来，大模型根本看不到你的内容，后面所有的品牌认知、推荐、引用全部无从谈起。反过来也成立：只做SEO、不做GEO特定优化，在AI搜索引擎上同样拿不到量。两件事缺一不可，但有先后。

Topify给客户建议的标准节奏是：第一个月先做技术SEO的体检和修复——确保AI爬虫能正常抓取网站的全部关键内容（HTTPS配置、robots.txt、sitemap完整性、页面结构化标签等）。这些琐碎的技术细节，恰恰决定了AI能不能"看见"你。这些基础打好后，第二个月再进入GEO特定的优化阶段。

在体检这一步，Topify见到过大量的踩坑案例：比如网站用老旧CMS系统，关键内容全渲染在前端JavaScript里，爬虫根本抓不到；sitemap指向错误域名；英文页面混杂中文UI元素；产品页URL拖着一长串参数——每一项技术债，都在悄悄把你从AI的推荐列表上往下拽。

把这些技术债清完、进入GEO优化阶段之后，数据变化很快就能体现在GA后台：经过GEO优化的博客页面，排名靠前的几篇单篇会话数达到数百次，平均停留时长超过一分钟，部分页面会话关键事件率接近5%。

分享一个最简单的自检方法：**在LLM里直接搜你的品牌名和核心产品词——AI能不能找到你、信息对不对、推荐语境是正面还是负面。过不了这一关，说明地基还没打好，GEO的投入为时尚早。**

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**03****没有目标Prompt，所有优化都是盲打**

如果说SEO的起点是关键词研究，GEO的起点则是Prompt研究——你要搞清楚用户在LLM里到底是怎么提问的。

很多人没注意到，用户在谷歌搜索时，平均输入大约6个单词；在LLM里提问时，平均单词数是22到23个。问法完全不同，优化的锚点自然也不能照搬SEO的关键词库。

**那目标Prompt从哪里来？Topify团队摸索出的方法是去Reddit上挖。**围绕要推广的目标产品领域，系统性地抓取Reddit、Quora上的相关帖子，看哪些问题被高频提出、哪些帖子有大量讨论和互动。热度越高的问题，大概率也是用户在AI里频繁提问的方向。把这些真实的用户提问提炼成目标Prompt，按搜索量和竞争强度排优先级，整理成一份清单——这份清单就是GEO内容规划的起点，每篇内容都应该对应一个或一组明确的目标Prompt，而不是凭感觉选题。

在分享中，Topify展示了一个案例：某个产品基于Prompt研究做完优化后，几天之内就出现了每日数千次的AI引流访问，部分客户在一个月内AI来源流量出现了明显的阶跃式增长。关键就在于"精准"二字。与其写100篇没有方向感的博客，不如先锁定20个真正有流量的目标Prompt，围绕它们做深度内容。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/75292809-0F06-45B2-9A31-8F613F764514.png)![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**04****最被忽视的战场：优化你的产品页**

"所有人都在拼命写博客，但真正决定AI是否推荐你的关键页面，他们根本没碰。"这里Jacky说的正是产品首页和产品详情页。

在GEO的语境下，产品页的权重远大于单篇博客文章。因为当AI要向用户推荐一个产品时，它需要一个权威的第一手信源来确认"这个产品到底是做什么的、解决什么问题、适合谁用"。你的产品页，就是这个第一手信源。

如果产品页写得模糊、只堆卖点不讲场景、缺乏结构化的信息组织，AI在推荐时的"置信度"就会很低。

Topify的做法是基于Grounding Query来反向优化产品页。Grounding Query可以理解为AI的"检索关键词"——当用户提出一个复杂问题时，AI会先拆解成若干更短的查询词去检索。从网站已有的被AI抓取的查询词中，反推用户可能提出的问题，把这些问题整理成产品页FAQ，每组FAQ都围绕真实用户需求来组织。

这样优化后的产品页就同时具备了两个价值：对人的转化价值，和对AI的引用价值。一个简单的检验标准——如果AI把这个页面的内容原样复述给用户，用户能不能清楚地知道你的产品是什么、解决什么问题、跟竞品有什么区别？如果不能，说明信息密度不够。优先级上，产品页的GEO优化应该排在博客内容之前。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**05****AI味太重的内容，人和机器都不买账**

"GEO的内容生产能不能全交给AI？"想必这是非常多Founder都想过的思路，但这条路径实操下来的效果非常差。

原因很简单，Marketing本质上是零和博弈，同一个搜索词下面十几个玩家在抢流量，用最省力的方式去竞争，拿到的只能是最平庸的结果。另一方面是质量判定——谷歌的抓取系统会很快把大量AI生成的内容标记为低质量站点，用户停留时间短，搜索权重下降，形成恶性循环。

更深一层，AI搜索引擎本身也在判断内容是否"像人写的"。如果一篇文章通篇都是TL;DR、Key Takeaways、Direct Answer的模板化结构，满是"非常好的问题，我来直接回答你"这类机器腔，它在AI的内容质量评估中就会被扣分。

Topify在内容生产上的原则是：**核心观点和关键洞察必须来自人类专家，AI只做辅助。** 他们会根据客户所在的领域匹配对应的行业专家，从选题讨论到内容审核，确保每篇文章读起来是一个真正懂行的人在分享经验，而不是一台机器在堆砌信息。

Jacky展示了一个给工业通信设备客户写的GEO文章案例：从物流行业的通信痛点切入——仓库噪音、车队跨区域覆盖、调度延迟——再按部署路径匹配产品线，用实际参数和功能对比收尾。通篇没有自卖自夸，读起来更像一份选型指南。这种"场景+痛点→产品匹配"的结构，恰恰是AI在生成推荐答案时最容易引用的格式。

**好的GEO内容，首先要让真实用户读完觉得有收获，其次才有机会被AI理解、引用和推荐。这个顺序不能反。**这也意味着，如果你的产品本身还没有找到PMF，GEO虽然能解决"被看见"的问题，但解决不了"被选择"的问题——流量来了也接不住。对自己是否真正有PMF保持诚实，是所有创业团队做GEO之前的一道必答题。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**06****EEAT只是及格线，AI真正看的是"多源验证"**

许多GEO教程会告诉你：把EEAT做好就行了——加专家引用、加数据来源、加作者简介。Jacky在实操中的经验是：这些只是达标项，做了不加分，不做扣分。真正让AI决定推荐你的，是互联网上的交叉验证。

AI在回答问题时，会同时参考十几类信源——官网、Reddit讨论、YouTube测评、LinkedIn内容、行业媒体报道、第三方评测。如果只有你站内在说"我们是最好的"，AI会判定为自吹自擂，置信度打折。但如果多个独立信源都指向你——用户在讨论、博主在对比、媒体在引用——这种一致性信号，才是AI敢推荐你的底气。

需要注意的是，每个行业的信源权重分布完全不同。"Reddit是AI引用最多的UGC平台"这只是全行业平均数据，到了生物医疗领域，学术论文和行业白皮书才是关键信源，金融领域同理。一定要用监控工具去看你所在领域的实际信源分布，再决定资源投在哪里。

还有一个反直觉的点：虽然外部渠道很重要，但优化重心仍然应该放在站内。因为站内内容随时可以修改迭代，AI下次抓取就能看到更新；Reddit上的帖子发完之后，你几乎无法控制。最优策略是以站内为核心资产持续建设，外部渠道作为信任背书的辅助。

对于健康、金融、法律这类高信任门槛的行业，信任建设周期天然更长，可能需要4到5个月以上才能看到稳定效果。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**07****落地路径：5层架构，缺一层都不稳**

把上面的认知收拢起来，GEO的完整执行路径可以归纳为如下的五层递进结构：

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/BC34F538-8215-437C-BEB8-FC0D653D3804.jpg)

这五层是递进关系，跳过任何一层，上面的投入都会打折扣。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/B952F10D-FC0E-4F61-965B-3BBDAACF43D0.png)

Topify客户GEO后网站实际引流增长案例
----------------------

补充一个QA环节中被频繁问到的问题：多语种市场怎么做GEO？LLM的检索机制是——用户用非英语提问时，模型会先翻译成英语去检索，同时也用原始语种做一轮检索。因此英语内容是基本盘，做好了英语GEO，其他语种自动受益。但要针对特定市场做深度渗透（比如日本、台湾地区），就需要额外投入本地化内容。好消息是，非英语市场的GEO竞争烈度远低于英语——英语可能需要30多篇Reddit帖子才能在某个细分问题上建立存在感，繁体中文市场可能3到5篇就够了。这里面有明确的ROI差异，值得认真权衡。

![](.evernote-content/73C11B78-A6A1-4B0B-BCA3-1D0B16554315/D4B69002-A823-4CCE-A6ED-6D96FA1A672C.png)

**08****写在最后**

Jacky在分享中的一句话可以概括做好GEO的心法——"GEO跟你做PR、做公关稿、做社交媒体，本质上是同一件事。只是你面向的对象从人变成了AI，表达方式从感性驱动变成了结构化的、高置信度的论证。"

GEO这场仗，拼的不是谁铺的内容多，而是谁对自己的产品最诚实、对用户的问题最认真、对AI的判断机制最理解。GEO归根到底，是"让好产品被AI看见"的系统工程。

***About Atom Capital***

*Atom Capital 是双币早期AI基金，由连续创业者创立，横跨硅谷与中国，专注"从0到1"的颠覆式创新。投资组合超半数创始人来自清华，深耕AI Agent、智能硬件、基础设施等核心赛道。我们提供的不只是资金，更是跨越中美的资源网络与全周期陪跑。*

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg5NDc5NDkzMA==&mid=2247484394&idx=1&sn=a60994122d6aae355cc9570ec65ee769&chksm=c1b068130d002ae6b85062613cc2473e65bbc7607b8f3d155cf6812ba848d536c5c672299aee&mpshare=1&scene=1&srcid=0525KnRiwUAhC2vVpQI7vYCp&sharer_shareinfo=dcf1175f0582846508147f889a73aeaf&sharer_shareinfo_first=53fa6f9433edc43b9c70f3864edc9278&from=groupmessage&isappinstalled=0&clicktime=1779712567&enterid=1779712567&ascene=1&devicetype=iOS26.5&version=18004933&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ2RjtmJryqQG/rmYUWo0jIhLnAQIE97dBBAEAAAAAABcBIjVdc/UAAAAOpnltbLcz9gKNyK89dVj0G1wUwNLg9wZYFwnqdH82E1mx8q+0srcylfdlfglPGWfRT0SZba96sYgK4Q766iCqYeHWKB6khU0Qcvw4YgqRbdYSC34ujs+2LuMKhfi+8KtXBde5xjLqWTFe3/zXSHC8zWdW0oq2hN7T1H0VAHf91zVzkuRxjiqaWJMFCi0edEYqmrMgtBURYx3+CSzAcA7TSgWUOP9Q+T0wcihn4HFv2zMJWdbTQbvGnE+lCoOnIBvyroAD2HnKcRHeDAoXVaMovA==&pass_ticket=HQdBFpLXt2lZ10OZSe8hlvuNpMM9/0ABJAt1YaYbw+obntkE4pYNzhfiLms0auqB&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f9256837-fd22-4d4c-a42c-0ef4708af308/f9256837-fd22-4d4c-a42c-0ef4708af308/)