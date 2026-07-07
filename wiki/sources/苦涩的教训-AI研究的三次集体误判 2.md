---
title: 苦涩的教训：AI研究的三次集体误判 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/苦涩的教训：AI研究的三次集体误判 2.md
tags: [evernote, impression, yinxiang]
---

# 苦涩的教训：AI研究的三次集体误判

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIyMzk1MDE3Nw==&mid=224767...](https://mp.weixin.qq.com/s?__biz=MzIyMzk1MDE3Nw==&mid=2247674691&idx=2&sn=c3ee09428950ca9d8eb84deb4e31d6dc&chksm=e939540ee1cd15cc0885a414828cb6a2173427a6f37d4beac5ee9d12d3b67b1598ef777e5b96&mpshare=1&scene=1&srcid=0207uNekFVzNid1P1iBkBvuh&sharer_shareinfo=8c929350f824a9863d08125da3acc4dc&sharer_shareinfo_first=8c929350f824a9863d08125da3acc4dc&from=groupmessage&isappinstalled=0&clicktime=1770420904&enterid=1770420904&ascene=1&devicetype=iOS26.2.1&version=18004431&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ4MchDjNwuZ+2OW842rs57RLoAQIE97dBBAEAAAAAAPjLFUBhpRQAAAAOpnltbLcz9gKNyK89dVj0vjSgTCe1PXHweKoDv8ICT7859SawXtDgsuccEYT8WVfbtoHC33nwn6XiUx2qSRyih9+2Ri+Iu5zkczvyC3hvc+E2O43kzjaNWLnP1LlMcKKy7MgJMCOQJSSfFLd16XilLRQn3OOHPJ13EKiVrx7RAfZrlw5S7hShNeN5zQ/utkUjETNVDyk23IlWbzVUtEZtQa/hiZvPSrwuPCYBbHSDpbJQbHBOhyHgUgBy3K11Hk68z53r6YC2fQ7nErmvd++COW0=&pass_ticket=wJ9cvRzdY7D9kgNpzHTidNNGf4xMnUNwCz5DrPT5ir0PeE2frwkhHRvjpN/3S9n4&wx_header=3)

图灵人工智能

The following article is from 烂芒Author Mango

转自烂芒，仅用于学术分享，如有侵权留言删除

理查德·萨顿 Richard S. Sutton是人工智能研究者、教授。

主要贡献：被认为是**强化学习（Reinforcement Learning）领域的奠基人之一**，他的教科书和论文是该领域的核心参考资料。

![](.evernote-content/37A60D2B-265D-4EF2-9C8E-18316713046B/6B2D40A0-C76F-4ED2-9C7E-354BAEBA8937.png)

在http://www.incompleteideas.net/IncIdeas/BitterLesson.html撰写： **《The Bitter Lesson（苦涩的教训）》****。**

tl;dr📌 **文章核心观点:**

文章总结了**70年人工智能历史的一个深刻教训**：

1. **通用方法 + 大规模算力 优于人类知识工程**

   文章认为那些能够**利用大量计算资源的通用方法**最终在AI任务中表现最好，而不是依赖人类设计的复杂、特定领域规则。人类领域知识通常在短期有用，但长远看效果不如通用算法（搜索、学习等）。
2. **摩尔定律的影响**

   之所以如此，是因为随着时间推移，**计算成本持续下降**，使得大量计算变得可能，从而推动AI方法的规模化和普适性。
3. **历史例子**

   Sutton 在文中提到像**计算机国际象棋、围棋、语音识别、计算机视觉等领域的进步**，都体现了这种情况——简单通用的计算驱动方法最终超过了手工设计的规则和知识。
4. **为什么是“苦涩的教训”**

   对研究者来说，这个观点“苦涩”在于它**否定了依赖人类直觉和领域知识的直觉路径**，而强调让算法通过数据和计算自己**发现结构。**

---

**Boris最后补上的第四条,不是经验,是****警告**
------------------------------

Boris Cherny 是 Anthropic 的工程师 / 开发者体验负责人之一，也是《Programming TypeScript》一书的作者，他擅长把“复杂系统 → 人能长期使用的工具”。
--------------------------------------------------------------------------------------------------

他在 Anthropic 负责 Claude Code / Developer Experience（开发者体验），关注点包括：如何让开发者真正用好 Claude、AI 编程助手、代码理解、Agent 工作流、“人如何和模型协作写代码”，而不是模型炫技。
-------------------------------------------------------------------------------------------------------------------------------

里奇·萨顿 Rich Sutton《The Bitter Lesson》，和 Boris 的取向其实是互补的：Sutton：规模、算力、通用方法终将胜出Boris：那人类应该站在什么位置？工具怎么设计，才能让人不被规模碾压？非常在意：人是否能理解系统在干什么工具是否**可控、可组合、可调试**AI 是否在**放大工程师能力**，而不是替代思考**不是造模型的人，而是决定模型“怎么被人用”的人。**Claude Code 能不能成为：程序员的真实工作伙伴，而不是“写 demo 很强、落地很弱”的 AI，👉 这正是他在解决的问题。
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

三个领域,同一个陷阱
----------

### 1. 国际象棋(1997)

**表象**:深蓝击败卡斯帕罗夫,AI胜利。

**当时的共识**:

* 国际象棋太复杂,需要深度搜索
* 这套方法能推广到其他领域
* **研究方向:更强的搜索算法**

**20年后的现实**:

* 初期投入大量精力研究免采用搜索策略
* 后来发现游戏的特殊性才是关键
* 方法无法有效泛化到其他应用

**问题不在于**深蓝不够强,**而在于**研究者把特例当成了通则。

真正值得追问的是:**如果一个方法只在国际象棋有效,为什么要投入20年去研究它的泛化能力?**

---

### 2. 计算机国际跳棋(同期)

**当时的方法**:

* 基于搜索和手工设计的评估函数
* 深度搜索+专家知识调参

**结果**:

* 在跳棋领域取得成功
* 但这套方法**只对跳棋有效**
* 难以迁移到其他问题

又是一个**高度专用的解决方案**被误认为通用方法论。

---

### 3. 咨询问答领域(20世纪70年代)

**DARPA资助的早期项目**:

* 利用人类知识的特殊方法(问答、语音识别等)
* 基于隐马尔可夫模型(HMMs)的统计方法
* **手工构建的专家系统**

**结果**:

* 在咨询问答领域有效
* 但无法泛化到其他领域
* 深度学习出现后,这些方法被彻底替代

**因果链**:

1. 研究者选择基于专家知识的方法
2. 在特定领域调参成功
3. 误以为找到了通用解决方案
4. 投入大量资源深化这个方向
5. 多年后发现**根本没有泛化能力**

---

共同的认知陷阱
-------

**三个案例的共性**:

1. 在特定领域取得突破
2. 研究者过度乐观,认为方法可泛化
3. 投入大量资源深化这个方向
4. **多年后发现是死胡同**

真正值得追问的是:**为什么同样的错误要犯三次?**

---

计算机视觉领域(2026)
-------------

Boris提到:**这个教训现在正在重演**。

**当前状态**:

* 深度学习在视觉任务表现优异
* 研究者投入大量资源深化这个方向
* 或许已经达到设计SIFT特征的方法无法继续推进的程度

**如果**历史重演,**那么**:

* 现在投入的资源可能大部分浪费
* 真正的突破可能来自完全不同的方向
* **我们正在重复70年代的错误**

问题不在于深度学习不够好,而在于**是否又把特定领域的成功当成了通用方法论**。

---

利益结构在哪
------

**谁在承担风险?**

* 学术界:投入研究资源在可能的死胡同
* 工业界:基于当前方法构建的系统可能很快过时
* 研究生:**职业生涯押注在可能被淘汰的技术栈上**

**谁在享受收益?**

* 当下:发论文、拿funding、出成果的研究者
* GPU厂商:深度学习需要大量算力
* **未来:那些没有跟风,在探索其他方向的人**

**制度约束在哪?**

* 学术界的发表压力:**跟风研究更容易出成果**
* 工业界的短期KPI:**用现成方法更快见效**
* 资助机构的评审机制:**热门方向更容易拿到钱**

如果整个系统都在激励短期行为,**谁来承担长期探索的成本?**

---

Boris真正想说什么
-----------

**这是一个沉重的教训**。

作为一个领域,我们**过去未能吸取这些经验**。

因为我们**往往不断重复同样的错误**。

要认识到这一点**并有效抵制它**,我们必须:

1. 警惕"这次不一样"的想法
2. 不要把特定成功当成通用方法
3. **保持对当前共识的怀疑**

---

表象背后的因果
-------

**表象**:AI在多个领域取得突破,前景光明。

**因果链**:

1. 某个方法在特定领域成功
2. 研究者和资本涌入这个方向
3. 短期内产出大量成果和应用
4. 形成"这就是未来"的集体共识
5. **几年/十几年后发现泛化失败**
6. 资源浪费,研究者转向
7. **新方法出现,循环重复**

真正值得追问的是:**我们现在对深度学习、Transformer、大模型的信心,是基于它真的通用,还是因为它暂时有效?**

---

风险的真实来源
-------

**不在于**技术路线选错。

**在于**:

1. 把阶段性成功当成终极答案
2. 在单一方向上过度投入
3. **缺少对现有共识的系统性怀疑**

如果1997年的研究者知道搜索方法会是死胡同,他们还会投入20年吗?

如果2025年的研究者知道当前方法会遇到瓶颈,他们还会all in吗?

**问题是:他们不知道,我们也不知道**。

---

Boris没说透的那句话
------------

"我们必须警惕"的真实含义:

不是说深度学习不好。

不是说Transformer会失败。

不是说大模型是泡沫。

而是:**如果所有人都在同一条路上狂奔,那么这条路大概率会走到尽头**。

真正值得追问的是:

**当Claude Code为六个月后的模型设计时,是在押注模型会继续进化,还是在准备模型进化停滞后的Plan B?**

如果是前者,Boris在重复70年代的错误。

如果是后者,他比我们看得更远。

---

**这是一个沉重的教训**。

问题不在于我们是否会犯错,而在于**我们是否会在同一个地方跌倒四次**。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIyMzk1MDE3Nw==&mid=2247674691&idx=2&sn=c3ee09428950ca9d8eb84deb4e31d6dc&chksm=e939540ee1cd15cc0885a414828cb6a2173427a6f37d4beac5ee9d12d3b67b1598ef777e5b96&mpshare=1&scene=1&srcid=0207uNekFVzNid1P1iBkBvuh&sharer_shareinfo=8c929350f824a9863d08125da3acc4dc&sharer_shareinfo_first=8c929350f824a9863d08125da3acc4dc&from=groupmessage&isappinstalled=0&clicktime=1770420904&enterid=1770420904&ascene=1&devicetype=iOS26.2.1&version=18004431&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ4MchDjNwuZ+2OW842rs57RLoAQIE97dBBAEAAAAAAPjLFUBhpRQAAAAOpnltbLcz9gKNyK89dVj0vjSgTCe1PXHweKoDv8ICT7859SawXtDgsuccEYT8WVfbtoHC33nwn6XiUx2qSRyih9+2Ri+Iu5zkczvyC3hvc+E2O43kzjaNWLnP1LlMcKKy7MgJMCOQJSSfFLd16XilLRQn3OOHPJ13EKiVrx7RAfZrlw5S7hShNeN5zQ/utkUjETNVDyk23IlWbzVUtEZtQa/hiZvPSrwuPCYBbHSDpbJQbHBOhyHgUgBy3K11Hk68z53r6YC2fQ7nErmvd++COW0=&pass_ticket=wJ9cvRzdY7D9kgNpzHTidNNGf4xMnUNwCz5DrPT5ir0PeE2frwkhHRvjpN/3S9n4&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0ba4c698-5875-4596-bbe2-1f6e77faf043/0ba4c698-5875-4596-bbe2-1f6e77faf043/)
