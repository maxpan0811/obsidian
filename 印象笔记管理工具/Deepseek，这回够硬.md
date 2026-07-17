# Deepseek，这回够硬

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg2Nzc0MDM3Nw==&mid=224851...](https://mp.weixin.qq.com/s?__biz=Mzg2Nzc0MDM3Nw==&mid=2248517330&idx=1&sn=ec194cc97733f383120b05db68cc1b8f&chksm=ccde401e6c5bb588ba406c52d09f16c804d5d1cf997de42b536f7efc82d78899536cd9e594f0&scene=90&xtrack=1&req_id=1784043067807311&sessionid=1784043251&subscene=93&clicktime=1784043254&enterid=1784043254&flutter_pos=0&biz_enter_id=4&ranksessionid=1784043067&jumppath=1001_1784043221789,1102_1784043223027,1001_1784043233563,1104_1784043252165&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b3a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ43ReffD5GFP1RaMA3QX7ABLTAQIE97dBBAEAAAAAAHa9B4OvEz8AAAAOpnltbLcz9gKNyK89dVj0niUWemJ6MdXfkIaQg6Mx3uGvFs+sVyDwp5mlHTd4w/k6KUYPxDTLLrgEqtQlVUORvK9DWWhxVcakMWRorcsjbxhPUACbh1xX5xf8oZaVrvx5DBO9zzN7NfxI0r5xAPRxfck/KKSFBt7pSWSuAOqEXFiWRpsj3i8i+S9m4a+2Uv6oTK3KSnhtBhunew/Zl999eVnnM9WkAIx5xmCslfq1HaD6aRv4I1Rk4Gk7eVI=&pass_ticket=CSkaqYDwgAIkrwK47+L23aVRsCtwyivWs1fXbBe8LffhHqOMQbxB/2UbLMcmrr5g&wx_header=3)

Original荣智慧 南风窗

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/AD738D8F-7B3D-4B46-9808-1C5AB6EAEFBB.gif)![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/5D60A590-7362-4B97-9AF5-A7B69485D299.jpg)

作者 | 荣智慧

编辑 | 向现

Deepseek进军硬件了。

7月7日，据外媒报道，中国人工智能初创公司深度求索正在开发AI推理芯片。消息传出，当天英伟达股价盘前下跌约2%。

媒体援引知情人士消息，该项目“始于一年前”，目前仍处于早期阶段。深度求索近几个月加大了芯片设计工程师的招聘力度，但招聘均在私下进行，未在公开平台发布职位。

在三个星期前的6月16日，深度求索刚刚完成首轮外部融资，募资总额超500亿元，估值超3300亿元。6月17日，中国证监会宣布“科创板扩容”，允许未盈利的人工智能大模型企业上市。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/A6F2AEE0-FCF2-4FCF-8F26-B78343EFB56D.png)

深度求索完成首轮外部融资

全球范围内，AI大模型企业自研芯片蔚然成风。Meta第四代自研芯片Iris将于9月量产；OpenAI于6月发布首款自研推理芯片Jalapeño；Anthropic于4月公开表示“考虑自研芯片”。

可以说，大模型公司为什么“造芯”、造哪一种芯、怎么造芯，且会带来什么样的影响，是这一波“芯浪潮”之下最普遍的疑问。而中国顶级大模型公司深度求索，抛出了意料之外、情理之中的答案。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/F3F8E4DC-3E33-455C-B64A-74A7559332BF.png)

**为什么造芯？**

深度求索造芯，堪称“大势所趋”。这是深度求索在外部地缘政治影响、内部供应链压力，以及自身技术优势共同驱动下的必然选择。

2023年，梁文锋在杭州接受采访时说过：“我们真正的挑战从来不是资金，而是高端芯片的出口禁令。”

自2022年起，受美国严苛的半导体出口管制政策影响，英伟达最先进的AI芯片不能通过合法渠道引入中国。深度求索早期的模型靠的是囤积的英伟达A100，V3和R1模型依赖“中国特供版”英伟达H800芯片训练，但这些芯片先后遭全面禁售。

今年6月，美国商务部急发最新“指南”，规定即使中国企业实体身处中国境外——比如在海外设立的研发中心，也将被禁止购买、使用英伟达最先进的Blackwell及Rubin架构的芯片，完成空间上的“全球封堵”。

实际上，从后续的V4和V4-Flash大模型开始，深度求索已经全面适配华为芯片昇腾950PR，其单卡推理性能达到英伟达中国特供版H20的2.87倍。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/E05BE2A5-DDAC-4215-B292-65CBE3968088.jpg)

针对昇腾950PR的架构特征，深度求索定制开发了算法和架构，持续将Token推理价格打到“白菜价”。据OpenRouter数据显示，美国企业调用中国AI的Token占比，自今年2月起突破30%，峰值达46%，比起2025年上半年4%的水平，涨幅相当明显。

昇腾950好是好，但实在供不应求。毕竟它面向的是整个中国人工智能产业的算力需求，客户包括互联网巨头字节跳动、阿里巴巴、腾讯、百度、美团；包括政企巨头中国移动、中国电信、中国联通、国家电网、南方电网；也包括上海、深圳、成都等地方政府智算中心，还包括了各类做算力租赁的中小云厂商。

在代工厂中芯国际的先进制程“盘子”里，华为一家就占去了近一半的产能分配。就算如此，除去分给华为手机麒麟芯片的产能，留给昇腾芯片的晶圆也所剩无几。其他中国AI芯片企业如寒武纪等，还要争夺剩下的份额。

这样一算，与其去争抢紧张之又紧张的先进制程代工份额，中国大模型公司还不如自己打造推理专用的ASIC芯片。这类芯片不需要通用GPU那么极致的技术，14nm平台就能做——这部分产能，中芯国际是很充裕的。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/91594580-0BB8-41B2-8C8B-B1EAA119A0FE.jpg)

中芯国际

而且，深度求索做硬件，底气很足。它就是靠“打磨”芯片起家的，拥有顶尖的软硬件协同设计能力。

如果用上了自研的专用推理ASIC芯片，深度求索还可以再大幅降低Token调用成本，构建出更大的性价比优势。同时，近期的巨额融资，也为深度求索提供了充足的“子弹”。

全球顶尖AI大模型梯队，都在自研推理专用芯片。OpenAI与博通合作研发Jalapeño，Anthropic也被曝出正在接触三星，Meta的第四代自研芯片Iris将于9月量产，特斯拉的AI5芯片已面世。而互联网巨头谷歌、亚马逊均已深耕多年，有能力自研训练芯片。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/25A2F836-9EBE-4E7E-90C0-C7AD5B57AE3B.png)

无论天时地利人和，深度求索都走到“造芯”这一步了。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/2AD130E5-116A-4BB9-9A32-B202B4C8DBF1.png)

**只做“定制芯”**

大模型公司集体下场“造芯”，无一例外，做的都是ASIC，也叫专用集成电路。

为什么做ASIC，不用英伟达的GPU呢？中国大模型企业买不到英伟达，美国大模型公司总不至于买不到。而这些公司“一齐”选择ASIC，主要由需求决定。

英伟达GPU是通用处理器，为了兼容图形渲染、科学计算和多种复杂算法，保留了大量闲置的硬件逻辑。而大模型公司的诉求集中且纯粹——只需要芯片能跑特定参数规模的大语言模型。

而且，这些模型公司“自研”的芯片，只瞄准推理场景，而不是训练场景。训练芯片，需要非常高的算力密度，以及生态兼容度，比如英伟达的CUDA，门槛很高；而推理阶段的计算模式相对固定，用ASIC针对性优化，可以“榨干每一寸晶圆”的性能。

今年拜OpenClaw这只“龙虾”所赐，大量AI应用爆发，每天的线上调用都会产生海量的推理成本。对于大模型公司来说，在固定的推理任务上，一个架构完全定制化的ASIC，其Token的计算成本、功耗和延迟，都会显著优于通用的GPU芯片。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/8FB8415C-3260-4808-A5C0-CA408E618203.jpg)

AI智能体“龙虾”/ 新华社发（薛莹莹 摄）

另外，自研芯片的“自研”也“有说法”。一般而言，“自研”包括全栈自研和部分自研，大模型公司肯定不会“从头做起”，它们都是和其他芯片企业合作，自己负责擅长的“调校”部分。

像OpenAI发布的首款自研推理ASIC芯片，名叫Jalapeño，是一种产于墨西哥的著名辣椒。

这款芯片也如辣椒一样强劲火爆：Jalapeño采用了与苹果M3、M4系列以及英伟达Rubin架构同级别的台积电3nm制程；计算核心采用“曝光掩膜板极限尺寸”，和英伟达H100一样庞大；它还堆叠了8块的HBM，一口气能吞下几万亿参数的模型权重。

Jalapeño具备了顶级训练芯片的材料和体量，但专攻推理，从启动到流片仅耗时9个月，可见OpenAI砸下血本、快马加鞭，也是为了把GPT的运行成本死死压下去。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/194C5AE0-176B-4828-AC88-03517588660D.png)

OpenAI CEO奥特曼与博通 CEO陈福阳展示新芯片Jalapeño的晶圆

在分工上，OpenAI负责定义核心的计算图，指出芯片应该保留哪些数学计算逻辑，砍掉哪些无用的通用图形渲染逻辑；研发推理服务系统，确保芯片适配未来几年内自己的模型技术路线图。

博通本来就是全球ASIC定制化设计的“无冕之王”，谷歌的TPU就出自它手，它主要负责芯片的前端后端设计、高速互联技术，还出面搞定了台积电3nm的“宝贵产能”。

中国大模型公司的“造芯”思路也差不多。

近日也传出“造芯”消息的智谱，据悉已经向多家中国本土芯片设计公司如寒武纪、壁仞发出初步询问，评估为自家GLM模型定制专属ASIC的可行性。该项目处于早期方案接洽阶段，预计两年以上时间才能流片落地。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/FE78C535-B90B-4128-AFBA-86FA6198C426.png)

**把握“战略生路”**

中美的大模型巨头都从“算力买家”化身“造芯玩家”，会给全球AI产业带来一些深远影响。

首先，“硬件混搭”将成为趋势。

这几年，英伟达凭借硬件的算力，和独一无二的CUDA软件生态，除了中国市场，在AI领域垄断了超90%的市场份额。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/2C1A0F33-A12C-496F-8BE7-DF3FAE4A0079.png)

英伟达CUDA架构的生态循环

各家大模型公司自研芯片，会最先打破英伟达的“寡头”局面：训练芯片归英伟达，推理芯片自己做；同时，采用Triton、OpenXLA等开源或自研编译器生态，不再被CUDA“锁死”。

英伟达CEO黄仁勋多次对大模型巨头、云厂商自研ASIC表达强硬的观点，他认为ASIC缺乏灵活性，硬件过于固化、无法应对推陈出新的大模型架构；工程难度高，“90%的ASIC项目以失败告终”；即使对手芯片“零成本”，英伟达的总拥有成本（TCO）也依然更低。

不过，黄仁勋到底老谋深算，虽然口头上强硬反对，但商业动作极其务实。英伟达推出NVLink Fusion技术平台，开放其看家本领“高速互联”技术。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/B07B56A1-1D18-406B-8AB9-7F6B3AA34849.jpg)

英伟达推出NVLink Fusion技术平台

这意味着，如果科技巨头非要自己造芯片，英伟达也不强求你买它的GPU，但是你可以把自研的ASIC接入到英伟达的NVLink网络中——不买芯片，互联“过路费”总要交一交。

其次，AI推理成本再降，应用大爆发来临。

有研究显示，用定制ASIC替代GPU，单位Token的计算成本和功耗将降低50%或更多。推理成本的暴跌，会促进更多的AI“助理”低成本地嵌入各类日常生活软件和硬件中去。AI应用会进一步爆发，从高能耗的“奢侈品”变成普惠性的“基础设施”。

再次，行业生态迎来洗牌，有人欢喜有人忧。

博通、迈威尔以及中国本土的定制芯片设计公司，都会成为大模型企业的座上宾，历史性的“造富”机遇来临。大模型企业提供算法和需求，设计服务商提供硅片实现，“算法加硅片”的联合开发模式，取代传统的硬件厂商造什么、软件厂商就买什么的局面。

![](.evernote-content/FFB76553-CF40-4FF9-AEB0-AC026C534BCB/9B32EBCC-6AC5-4E33-8E66-FB10C7C7410E.jpg)

博通

而过去几年涌现的AI芯片初创公司，命运就难说了。它们本来瞄准的客户就是互联网巨头、大模型独角兽，现在客户都自己做芯片，它们的市场空间就被严重压缩了。

另外，技术路线持续分化，中美两国“各干各的”。

美国巨头霸占着最好的供应链，制造ASIC，依然追求极致性能和先进制程，以求利用绝对的技术代差维持“地表最强”统治地位。3nm工艺、HBM4显存一股脑用起来，仿佛这些东西“不要钱”一样，

中国企业没法单纯堆砌顶级硬件，因此继续采用“极致软硬协同”策略，用软件和算法的优势弥补硬件的缺陷。这也正是深度求索大展拳脚的机会，通过一系列创新性的架构和底层算法优化，压榨出极高的推理效率，走独特的自主可控路线。

总之，大模型公司“造芯”，本质是AI产业走向成熟的标志——最初各家都在开展不计成本的算力军备竞赛，现在都要拼效率、拼成本、拼商业落地、拼“工业化大生产”，证明行业从投资阶段逐渐转向“产出”阶段了。

当然，黄仁勋对ASIC的“反对”并不是毫无道理。但无论如何，ASIC之于中国大模型企业的意义，不仅仅是“省钱”，更是突破海外算力围剿、绕过英伟达生态壁垒、形成商业闭环的战略“生路”，需要自己把握住。

值班主编 | 吴擎

排版 | 阿车

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg2Nzc0MDM3Nw==&mid=2248517330&idx=1&sn=ec194cc97733f383120b05db68cc1b8f&chksm=ccde401e6c5bb588ba406c52d09f16c804d5d1cf997de42b536f7efc82d78899536cd9e594f0&scene=90&xtrack=1&req_id=1784043067807311&sessionid=1784043251&subscene=93&clicktime=1784043254&enterid=1784043254&flutter_pos=0&biz_enter_id=4&ranksessionid=1784043067&jumppath=1001_1784043221789,1102_1784043223027,1001_1784043233563,1104_1784043252165&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b3a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ43ReffD5GFP1RaMA3QX7ABLTAQIE97dBBAEAAAAAAHa9B4OvEz8AAAAOpnltbLcz9gKNyK89dVj0niUWemJ6MdXfkIaQg6Mx3uGvFs+sVyDwp5mlHTd4w/k6KUYPxDTLLrgEqtQlVUORvK9DWWhxVcakMWRorcsjbxhPUACbh1xX5xf8oZaVrvx5DBO9zzN7NfxI0r5xAPRxfck/KKSFBt7pSWSuAOqEXFiWRpsj3i8i+S9m4a+2Uv6oTK3KSnhtBhunew/Zl999eVnnM9WkAIx5xmCslfq1HaD6aRv4I1Rk4Gk7eVI=&pass_ticket=CSkaqYDwgAIkrwK47+L23aVRsCtwyivWs1fXbBe8LffhHqOMQbxB/2UbLMcmrr5g&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/de816063-a5ca-4b56-b4cc-5fd0679f6b6f/de816063-a5ca-4b56-b4cc-5fd0679f6b6f/)