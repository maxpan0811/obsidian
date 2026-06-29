---
title: Nature：Google 把 7 个AI 智能体组成科研团队Co-Scientist。从 2300 个药物里筛选，2 天独立复现实验组用十年才发现的耐药机制
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/Nature：Google 把 7 个AI 智能体组成科研团队Co-Scientist。从 2300 个药物里筛选，2 天独立复现实验组用十年才发现的耐药机制.md
tags: [evernote, impression]
---

---
title: "Nature：Google 把 7 个AI 智能体组成科研团队Co-Scientist。从 2300 个药物里筛选，2 天独立复现实验组用十年才发现的耐药机制"
source: evernote
type: note
export_date: 2026-06-22
guid: 7f1eadd4-c272-457f-9a58-fb0c6fd1d09c
---

# Nature：Google 把 7 个AI 智能体组成科研团队Co-Scientist。从 2300 个药物里筛选，2 天独立复现实验组用十年才发现的耐药机制

原文链接: [https://mp.weixin.qq.com/s?chksm=97974fc3a0e0c6d58306ef4c04ead84...](https://mp.weixin.qq.com/s?chksm=97974fc3a0e0c6d58306ef4c04ead84411e300c50aad3a79a60c1d570ba233c3b31f91a85821&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782032740_1&req_id=1782031330553375&scene=169&mid=2247483824&sn=2267d43bfb1a7afc7ce6ba6047123706&idx=1&__biz=MzIxNTU4NzYxMg==&sessionid=1782032739&subscene=200&clicktime=1782033140&enterid=1782033140&flutter_pos=6&biz_enter_id=5&jumppath=20020_1782033106717,1122_1782033111560,20020_1782033112997,1104_1782033137294&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQQAUWL/2YLAPnwetISr0S0hLCAQIE97dBBAEAAAAAAKdQDd/GluQAAAAOpnltbLcz9gKNyK89dVj0ab1aUnZllXJdFErWga8mqDXaoydP2dDywVyGAM/QSw3/2YVkixmp0o2f8Kv8Ax8TqWfAgPqtJPsU9o+z8mJ7ZgPMCJpK1pVNjrGwpS0B0o0UCg+uNicGQC/Wq2P48aVVT3VKpWr5ZmvwQeVdVrMw+kQ6GSNrVIIV9oM0S6KoVOw6IJL01RQMZJd3iuaNZHgXkkCU3ypDx/3cyAob&pass_ticket=6DZMzIbVCsc44aRAhnbrsRtgRMKAy2AEcRQfYg1GLHl19kKbz/mNZDtO9WbB0pEN&wx_header=3)

OriginalRyan 科研Agent实验室

顶刊雷达: Google DeepMind + Cloud AI + Research 三方联合，再加 Stanford 医学院、Imperial College London、Houston Methodist 等机构，9 位共同一作（Juraj Gottweis 和 Vivek Natarajan 领头），发表在Nature 2026-05（DOI 10.1038/s41586-026-10644-y）。这一篇拆 7 件事：科研最大的瓶颈为什么不是没想法、Co-Scientist 怎么把"做一步"换成"当一支团队"、7 个智能体 3 个阶段怎么分工、Elo 锦标赛借鉴的是 AlphaGo 什么思路、白血病湿实验从 2,300 药物到 IC50 低至 2 nM 候选的完整漏斗、Co-Scientist 怎么在 2 天里复现实验组用近十年才发现的耐药机制、跟之前的文章 MOSAIC 形成的"知识切片 vs 流程切片"对照。

|  |
| --- |
| Google DeepMind 五月登 Nature 的重磅工作：**Co-Scientist**，一个"多智能体 AI 科研伙伴"。  先讲一个数字：在 Stanford 医学院的白血病研究中，临床医生用 Co-Scientist 跑药物再利用的**整个过程**，从给系统写研究目标，到拿到最终筛选好的 in vitro 候选，花了**不到 4 小时**（其中 prompt 设计 1 小时，最终评审 3 小时）。Co-Scientist 后台在这段时间里筛遍了 **2,300 种 FDA 已批准药物 × 34 种癌症**的候选空间，挑出 30 个 top 候选，临床专家从中选 5 个进湿实验，3 个真的有效。**同样的工作量，论文里科学家原本估计要花几天到几周**。  Co-Scientist 的底层思路：**不让 AI 帮你做某一个步骤，让它当一整支研究团队**。7 个基于 Gemini 2.0 的专门智能体，分成生成、辩论、进化三个阶段，自己开会、互相评审、做 Elo 锦标赛对弈来排出最优假设。借鉴的是 AlphaGo 那套对弈训练，但下的不是棋，是**科学辩论**。100+ 合作机构验证过一年，在白血病、肝纤维化、抗菌素耐药三个生物医学难题上都拿到了真实结果。 |

|  |
| --- |
| 速览 · Co-Scientist 关键事实  专家全程时间  < 4 小时  原本几天到几周  候选漏斗  2,300 → 30 → 5 → 3  药物 / top / 测试 / 有效  最强候选 IC50  2 nM  对 TK6 对照高 ~20,000 倍  耐药机制独立推  2 天 vs 近十年  cf-PICIs 假设 |

## 一、科研最大的瓶颈，从来不是没想法

论文 Introduction 直接点出科研工作者的真实困境：*"Researchers are faced with a breadth and depth conundrum."* 翻译过来就是**科研工作者一直被广度和深度两难夹击**。

什么意思？现在科学专业化程度越来越深，PI 要在自己的窄领域里站稳，得每天读最前沿的论文；但科学史告诉我们，**真正的洞察经常来自跨学科的连接**，需要广度。这两件事在精力上互斥。

叠加上 PubMed 每年新增 150 万篇论文的节奏，一个 PI 每天能精读 2-3 篇就到顶了。**不是没有人想从草堆里捞针，是没有人有时间把整个草堆翻一遍**。前面 Day 1-7 写过的 AI 工具，DrugCLIP、CBNN、MOSAIC、SCIGEN，每个解决的都是科研流程里的一个具体环节。Co-Scientist 想啃的是更上游、也更难的事情：**整段研究流程**。

## 二、Co-Scientist  · 让 AI 当一支完整的研究团队

Co-Scientist 跟当前主流的 AI 助手在四个维度上完全不同：

| 环节 | 传统 LLM 助手 | Co-Scientist |
| --- | --- | --- |
| 角色 | 一个全能但样样松的助理 | 7 个专门化 agent + 1 个总督导 |
| 思考方式 | 线性 chain-of-thought | 异步并发 + 多路径同时探索 |
| 质量控制 | 模型自评 / 用户事后筛 | Elo 锦标赛对弈 + agent 互评 |
| 算力分配 | 主要花在生成 | 主要花在 verify（验证），不在 generate |
| 推理预算 | 一次推理 | test-time compute scaling：算力越多假设越好 |

第四行的"算力主要花在 verify"是论文里一句很关键的话，原文是：*"the majority of the system's computation is dedicated to verifying these hypotheses"*。意思是 Co-Scientist 不是一个"暴力产生想法"的系统，而是一个**非常谨慎地核对每个假设的系统**。它会调用 web search + ChEMBL（化合物库）+ UniProt（蛋白序列库）+ AlphaFold 等专业工具反复 cross-check，从结构上压住 LLM 最头疼的幻觉问题。

## 三、7 个智能体分工详解

按科研流程分成三个阶段，外加 1 个总督导：

| 阶段 | 智能体 | 职责 |
| --- | --- | --- |
| 总督导 | Supervisor | 把高层研究目标拆成可执行步骤，分配资源，协调其他 agent 并行运行 |
| 生成 | Generation | 用 4 种策略来产生假设：文献检索、模拟科学辩论、迭代识别可测试假设、研究扩展 |
| 生成 | Proximity | 对生成的假设做聚类，去重 + 保证多样性 |
| 辩论 | Reflection | 虚拟同行评审，6 种 review 模式（初评 / 全面评审 / 深度验证 / 观察验证 / 模拟 / 迭代） |
| 辩论 | Ranking | 组织 Elo 锦标赛，让假设两两 PK |
| 进化 | Evolution | 用 6 种策略 refine top 假设（搜索增强 / 提升可行性 / 启发 / 组合 / 简化 / 跳出框架） |
| 进化 | Meta-review | 综合所有辩论的洞察，反馈给其他 agent，输出最终 research overview |

几个工程细节值得专门讲：

- **不是 7 个相同 LLM 跑 7 遍取共识**：每个 agent 有自己的角色定义、提示词模板、行为模式。Generation Agent 是"想点子的人"，Reflection Agent 是"挑刺的人"，Ranking Agent 是"主持辩论的人"
- **Evolution Agent 只生成新假设，不修改 / 替换现有的**：每个新假设必须重新进锦标赛 PK，从结构上防止"坏改动污染好想法"
- **Meta-review 是"无需反向传播的学习机制"**：识别出的 pattern 直接 append 到其他 agent 的 prompt 里，下一轮起作用。这绕开了 fine-tune 和 RL
- **Reflection Agent 的 search 功能效应巨大**：论文 ablation 显示，在已知非新颖的想法集上，**没有搜索时 Co-Scientist 给的 novelty 评分 6.14（10 分制），有搜索后掉到 2.38**。能不能调用外部工具，决定了这套系统是不是在自欺欺人

## 四、Elo 假设锦标赛 · 用 AlphaGo 的对弈思路下科学辩论

Ranking Agent 的设计最有意思。它借鉴的是 AlphaGo / AlphaStar 训练时的**对弈框架**：

|  |
| --- |
| **步骤 1**：Generation Agent 产几百到几千条候选假设，每条初始 Elo = 1200  **步骤 2**：Ranking Agent 让候选两两对抗，**高排名假设用多轮辩论 PK，低排名假设用单轮对比**（节省算力）  **步骤 3**：每场辩论的胜负更新 Elo 分数，跟围棋选手对弈累积 Elo 一个道理  **步骤 4**：高 Elo 假设被 Evolution Agent 进一步精化，再回到锦标赛继续打  **步骤 5**：整个过程不断注入新知识（web search + ChEMBL + UniProt + AlphaFold），让假设空间扩展，避免局部最优 |

这套设计的好处是**结果有量化痕迹**。Co-Scientist 不是给你"我觉得 X 是对的"，而是"X 在 N 场辩论里赢了 M 场，比 Y 高 300 分"。论文测了 203 个研究目标，发现：**给越多 test-time compute，Co-Scientist 的 Elo 分数持续上升，没看到饱和迹象**。在 15 个由 7 位生物医学专家精选的高难度目标上，Co-Scientist 最终超过 Gemini 2.0 Pro Experimental、OpenAI o1、OpenAI o3-mini-high、DeepSeek R1，也超过了人类专家的 best guess。

## 五、白血病湿实验 · 从 2,300 药物到 IC50 = 2 nM 的完整漏斗

这是论文最有说服力的部分，**Co-Scientist 不只在 benchmark 上跑分，是在真实实验室里被验证过**。研究目标是**急性髓系白血病（AML）的药物再利用**：在 2,300 种 FDA 已批准药物里，找出可以用来治疗 AML 的候选。论文 Methods 完整披露了漏斗每一层：

|  |
| --- |
| **第 1 层**：Co-Scientist 在 **2,300 种已批准药物 × 34 种癌症**的候选空间里跑预测  **第 2 层**：输出 30 个 top-ranked AML 候选交给临床专家评审  **第 3 层**：专家选 5 个进入 in vitro 湿实验：Binimetinib、Pacritinib、Cerivastatin、Pravastatin、Dimethyl fumarate  **第 4 层**：3 个药物显示出抗白血病活性（Binimetinib、Pacritinib、Cerivastatin），2 个无显著效应  **验证细胞系**：4 个 AML 细胞系（MOLM-13、KG-1a、HL-60、NOMO-1）+ 1 个非 AML 对照（TK6 淋巴母细胞系） |

**最有戏剧性的是 Binimetinib 的数字**。这个 MEK 抑制剂原本是黑色素瘤的药，Co-Scientist 提出可以再利用到 AML：

| 细胞系 | 类型 | Binimetinib IC50 |
| --- | --- | --- |
| HL-60 | AML | 2 nM |
| MOLM-13 | AML | 10 nM |
| KG-1a | AML | 20 nM |
| TK6 | 非 AML 对照 | 38.71 μM |

最敏感的 HL-60 跟 TK6 对照之间，IC50 差距**大约 20,000 倍**。意思是 Binimetinib 可以在远低于伤害正常对照细胞的浓度下，把白血病细胞活性压下去。这种"治疗窗"是临床转化的关键指标。

更精细的是 Co-Scientist 的**临床转化分析**。它不只指出 Binimetinib 在 AML 上有活性，还结合 ELN2022 风险分层 + 患者人口学特征 + 安全性数据，主动推理出一个非常具体的临床场景：**Binimetinib 走 UGT1A1 代谢通路，绕开 CYP3A4 介导的与抗真菌药 azole 的相互作用，这是其他 AML 靶向药的主要使用限制。所以它特别适合反复治疗失败的体弱（frail）AML 患者**。论文里这段分析非常有意思，因为它说明 Co-Scientist 不只是"找匹配"，是在做**真正的临床决策推理**。

## 六、KIRA6 · Co-Scientist 自己挑出来的全新候选

Binimetinib 这条线还有前期文献支持。论文里更厉害的是另一个实验：研究者要求 Co-Scientist **不要依赖任何先验文献，纯靠推理产出 AML 新候选**。系统给了 3 个：**Nanvuranlat、KIRA6、Leflunomide**。其中 KIRA6 一个 IRE1α 抑制剂，展现出非常漂亮的选择性：

| 细胞系 | 类型 | KIRA6 IC50 |
| --- | --- | --- |
| KG-1a | AML（primitive stem-like） | 10 nM |
| NOMO-1 | AML | 144 nM |
| TK6 | 非 AML 对照 | 180 nM |
| HL-60 | AML（分化） | 870 nM（弱） |
| MOLM-13 | AML（分化） | 1,750 nM（弱） |

注意 KG-1a 和 TK6 的比值是 **18 倍**。更重要的是，**KIRA6 对原始 stem-like AML 群体（KG-1a）显著更敏感，对分化谱系（HL-60、MOLM-13）效果弱**。这是一个有强生物学意义的发现：白血病干细胞最难杀，KIRA6 显示出"挑性"。Co-Scientist 在论文 Supplementary Note 5.2 里详细给出了 IRE1α-XBP1 轴的机制解释。"我猜出了候选，还猜对了为什么"，这种能力是 Co-Scientist 跟普通 AI 工具最不一样的地方。

|  |
| --- |
| Co-Scientist · 一句话总结  不是 AI 帮做一步  是 AI 当一支团队  生成 · 辩论 · 进化 · Elo 锦标赛  大部分算力花在验证  不在产想法  数据来源：Nature（2026-05-19）· DOI 10.1038/s41586-026-10644-y  Google DeepMind + 100+ 合作机构 · 科研 AGENT 实验室 |

↑ 长按保存或截图发到 AI4Science / 科研 AI 工具群

## 七、肝纤维化 + 抗菌素耐药 · 另外两个真实验证

论文测试的三个生物医学场景，沿着**难度递增**的顺序排：

| 应用 | 挑战类型 | 复杂度 | 未知维度 |
| --- | --- | --- | --- |
| AML 药物再利用 | 复杂搜索 | 中 | 有界 |
| 肝纤维化新靶点 | 识别新靶点 | 高 | 大 |
| 耐药基因转移机制 | 理解复杂系统 | 极高 | 无界、动态 |

**肝纤维化（与 Stanford Gary Peltz 团队合作）**：Co-Scientist 提出 3 个表观遗传修饰物（epigenetic modifier）作为新靶点，团队找出对应的 3 种药物逐一测试，**其中 2 种显示出显著的抗纤维化活性**，且对细胞无毒。关键药物是 **Vorinostat**，已 FDA 批准用于另一种癌症适应症，这意味着 Co-Scientist 不只是找出了新机制，还**跨疾病做了药物再利用**（cancer → liver fibrosis）。

**抗菌素耐药（与 Imperial College London 的 José R. Penadés 团队合作）**：这是论文里最戏剧性的一个验证。研究目标是解释 cf-PICIs（capsid-forming phage-inducible chromosomal islands，产生衣壳的噬菌体诱导染色体岛）如何在多种细菌物种间传播，这些染色体岛携带毒力和抗生素抗性基因，跨越 E. coli、K. pneumoniae 等。**Penadés 团队从 2015 年开始研究这件事，做实验积累了近十年，2024 年才有了关键发现，对应论文跟 Co-Scientist 工作同期投到 Cell**。研究者把同一个研究目标喂给 Co-Scientist，**只给最少背景信息，2 天内 Co-Scientist 独立提出了 top-ranked 假设：cf-PICIs 通过与不同噬菌体尾部互动来扩展宿主范围，跟 Penadés 团队近十年研究的核心发现完全一致**。这个对比是论文里最有说服力的一段证据。

## 八、跟 MOSAIC 对照 · 知识切片 vs 流程切片

本周 Day 5 写过 Yale + Boehringer 的 **MOSAIC**（2,498 个化学小专家集体协作）。Co-Scientist 跟 MOSAIC 表面上都是"多智能体"，但切分逻辑相反：

| 维度 | Day 5 MOSAIC | 本期 Co-Scientist |
| --- | --- | --- |
| 切分逻辑 | 按**知识**切（化学子领域） | 按**流程**切（科研环节角色） |
| 智能体数量 | 2,498 个（多而细） | 7 + 1 个（少而精） |
| 协同方式 | 问题路由到对应专家 | 异步并发 + Elo 锦标赛 |
| 出品方 | 学界（Yale）+ 工业（BI） | 产业巨头（Google）+ 学界 |
| 底座 | Llama-3.1-8B 微调（开源） | Gemini 2.0（闭源） |
| 主要应用 | 化学合成协议生成 | 生命科学假设生成 |

**本质区别：MOSAIC 是"按领域分工的专家网络"，Co-Scientist 是"按角色分工的研究团队"**。如果问题主要是**知识检索**（合成路径），按知识切；如果问题主要是**判断和推理**（科学假设），按流程切。两条路其实可以串起来用，Co-Scientist 的 Reflection Agent 调用 MOSAIC 来验证化学步骤，但这种串联还没人做。

## 九、几个值得追问的边界

|  |
| --- |
| 边界 1 · **不是自主科学发现**。论文 Discussion 明写：所有验证都**有 expert-in-the-loop**。Co-Scientist 提假设、给排名，但实验做不做、临床推不推，决定权和责任仍在科学家手里  边界 2 · **知识来源偏差**。Co-Scientist 依赖**开放获取文献**，付费墙后的关键先验 + 负面实验结果都进不来。论文自承"may lead to omission of critical prior art behind paywalls"  边界 3 · 模型**Gemini 2.0 闭源**。学界很难独立复现 / 审计。Supplementary Note 8 给了 pseudocode，Note 9 给了 prompts，但完整源代码不公开。Google 提供 "Hypothesis Generation" 实验访问工具  边界 4 · **仍是初步验证**。AML 是 in vitro 细胞实验，没到 in vivo 或临床。论文专门强调"these wet-lab experiments function as a viability check, yet they are not a replacement for the rigorous pre-clinical and clinical assessment"  边界 5 · **CBRN 风险被官方主动谈**。团队自做了化学 / 生物 / 放射 / 核武器的误用评估，加了 custom safety classifier。这件事被写进 Discussion 本身，说明 Google 内部觉得风险足够大  边界 6 · **潜在加剧科学可重复性危机**。论文 Discussion 罕见地坦白：*"Improper use of such AI systems without rigorous peer-review and guardrails could also lead to worsening of the scientific reproducibility crisis through production of low quality scientific artifacts."* |

|  |
| --- |
| 数据来源 · 访问层级说明  *Accelerating scientific discovery with Co-Scientist*，Nature（2026-05-19），DOI 10.1038/s41586-026-10644-y ｜ 已读：完整全文（含 Abstract、Introduction、Results、Discussion、Methods、References、Extended Data Figures/Tables）｜ Google DeepMind 官方 blog（2026-05-19）｜ 9 共一以 Juraj Gottweis 领头，project leads Vivek Natarajan + Alan Karthikesalingam + Annalisa Pawlosky + Yunhan Xu + Pushmeet Kohli ｜ 100+ 合作机构 ｜ 资助 NIH 1R01DC021133 + 1R24OD035408（to Gary Peltz）+ Alphabet ｜ 配套独立论文：Guan Y. (Adv Sci 2025, 肝纤维化) + Penadés JR (Cell 2025, AMR) + He L. (Cell 2025, AMR 独立验证) |

科研 AGENT 实验室 · 顶刊雷达 · Nature Co-Scientist 多智能体科研伙伴

2026-06-10
