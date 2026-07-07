---
title: 新研究揭示DeepSeek_o3弱点：频繁切换思路放弃正确方向，最短答案往往就是对的！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/新研究揭示DeepSeek_o3弱点：频繁切换思路放弃正确方向，最短答案往往就是对的！ 2.md
tags: [evernote, impression, yinxiang]
---

# 新研究揭示DeepSeek/o3弱点：频繁切换思路放弃正确方向，最短答案往往就是对的！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzNjc1NzUzMw==&mid=224777...](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247775527&idx=1&sn=6b09354433568103fcfaed49b4086871&chksm=e90e3c99d47e024de38ed79c2e7ec7c2449954d1a317eb5dc11061537de04a05cbbb7158d322&scene=90&xtrack=1&sessionid=1738572539&subscene=93&clicktime=1738573193&enterid=1738573193&flutter_pos=19&biz_enter_id=4&ranksessionid=1738573120&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ9TN/vQNRq9RBP4jARJqjNhLWAQIE97dBBAEAAAAAAE5ZJK6dLkUAAAAOpnltbLcz9gKNyK89dVj0MX2T4EoxX7qU8rBXoKIDVmKYJxcwMUKN+bmw/AbuxT/B0eF/TIieH2i4RdZhc+h0S7I+5dDIh03Cy298zvHHhUSOz7DBdWkM8PAHgjo0VMZQF8jlYz9bs4Fdfn2brm94ZwSwgk1LJ6RdGP+XNbf7nKD88u/8+r55lFx9BGsw/u/DZMOuaporPjnwpFBjYTjK0mSuEgvd5GBO+3YEFWjdZ31+PYgdF8fTzs65iyy51Xk=&pass_ticket=iwzO/Jbl6NAKjh9remGllXvA72gvB+kqmfL0kDiLcBXHYThns8f34Cqxf2Q1+lhp&wx_header=3)

原创 关注前沿科技  量子位

##### 梦晨 西风 发自 凹非寺量子位 | 公众号 QbitAI

DeepSeek和o1/o3一类推理大模型持续带来震撼之际，**有人开始研究他们的弱点了**。

最新研究揭示：

在遇到高难度问题时，推理大模型可能像“三心二意的学生”一样频繁切换解题思路，却因缺乏深入探索而失败——这种现象被研究者称为**Underthinking**（欠思考）。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/B84D9C00-3931-4A2A-BA4D-61FBA017682D.png)

研究团队来自腾讯AI实验室、苏州大学和上海交通大学，主要研究对象是开源的**DeepSeek-R1和Qwen QwQ**系列模型。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/3F659F9B-F424-4937-A465-72D90F8903AA.png)

通过分析AI的错误答案，他们发现当前的推理大模型经常在思考早期就走上了正确的路线，但倾向于“浅尝辄止”，很快开始探索别的思路，导致后续生成的数千个tokens对解题毫无贡献。

这种“无效努力”不仅浪费计算资源，还显著降低了答案的正确率。

“三心二意”是罪魁祸首
-----------

这一现象在解决数学竞赛题等更为复杂任务时尤为明显。

为了系统分析，团队在三个具有挑战性的测试集MATH500、GPQA Diamond和AIME2024上，对类o1模型QwQ-32B-Preview、DeepSeek-R1-671B等进行了实验。

下图比较了正确和错误回答中的token使用量和思维切换次数。平均来看，类o1模型**在错误回答中比正确回答多消耗了225%的token**，原因是思维切换频率增加了418%。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/82851E43-E433-4139-B5A2-9F564310E980.png)

为了深入分析这一现象，研究团队开发了一套评估框架，用于判断被放弃的推理路径是否实际上足以推导出正确答案。

结果观察到，许多模型在回答开头阶段的思路是正确的，但并未继续深入完成推理。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/04CB4B45-290A-4C0B-835A-E883883154B5.png)

**超过70%的错误回答中至少包含一个正确的思路**。此外，在超过50%的错误回答中，有10%以上的思路是正确的。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/CF3A7D66-A82E-4417-B550-485FD1233214.png)

如下图所示的例子，例如，Thought 1通过识别给定方程类似于以(0,0)和(20,11)为中心的椭圆方程，启动了正确的解释。将两个表达式设为相等，是寻找满足这两个方程的公共点(x, y)的有效方法。

然而，模型并未专注于深入探索这一合理思路，使用进一步的代数操作和优化技术进行分析，而是频繁切换思路，额外消耗了约7270个token，却依然未能得出正确答案。

最终，它得出一个缺乏扩展COT过程支持的猜测答案。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/C410095A-4648-46CA-8926-FEBF568B5328.png)

基于这些观察，研究人员提出了一个用于量化Underthinking程度的指标（Underthinking Metric）。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/25D0DD19-2E50-49FD-958A-D44E8638DF2D.png)

这个指标通过测量错误答案中的token使用效率来评估推理效率，计算从回答开始到第一个正确思路出现所需的token数量与总token数量的比值。

实验结果表明，所有测试的类o1模型都存在显著的思维不足问题。模型的准确率与思维不足之间的关系在不同数据集上表现各异。

在MATH500-Hard和GPQA Diamond数据集上，性能更优的DeepSeek-R1-671B模型在取得更高准确率的同时，其UT得分也更高，表明错误回答中存在更多思维不足。

这意味着，尽管模型整体能力更强，但在不确定时可能生成更长但效率较低的推理过程，可能是因为模型探索了多个错误的推理路径，却未能有效收敛到正确解答。

相反，在AIME2024测试集中，DeepSeek-R1-671B模型不仅取得了更高的准确率，还表现出较低的UT得分，反映出较少的思维不足和更高的token效率。

这表明模型在该任务中，即使未得出正确答案，其推理过程依然保持专注和高效，团队表示这可能是因为模型与 AIME2024所要求的问题类型和推理过程更好地对齐。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/C9B9EE39-E8BC-484D-89E6-7111637A18A0.png)

理解思维不足现象对于开发能够提供正确答案并具备有效推理过程的模型至关重要。

如何让AI学会“一心一意”
-------------

如何让模型像优秀学生一样“沉下心来钻研”？

研究者借鉴了人类考试策略，提出了一种**“思路切换惩罚机制”**（Thought Switching Penalty，TIP）。

其原理类似于考试时给自己定规矩：“先专注当前方法，至少尝试10分钟再换思路”。

技术细节上，TIP会对触发思路切换的关键词施加惩罚，降低这些词在解码过程中的生成概率，迫使模型在当前路径上探索更久。

例如，当模型开始写“Alternatively, we can consider…”时，TIP会通过调整参数（惩罚强度α和持续时间β），抑制这种过早的切换倾向。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/3FFFCAEF-6F60-41DC-8E0D-C34B4BF031A6.png)

实验结果显示，加入TIP能让模型在数学测试上的准确率上升，同时UT Score下降，说明既减少了无效切换，又提高了答案质量。

例如在AIME2024数学竞赛测试上，加入TIP的QwQ-32B-Preview模型准确率从41.7%提升至45.8%，同时UT Score从72.4降至68.2。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/0B3B7DF1-2BD2-44AF-B256-76A73E752DF6.png)

并且这种“无痛升级”无需重新训练模型，仅需调整解码策略，展现了其实用价值。

One More Thing
--------------

**UC Berkeley教授Alex Dimakis**几乎同时分享了类似的观察，

对于DeepSeek-R1和所有推理模型，错误的答案更长，而正确的答案要短得多。

基于此，他们提出一个简单的解决办法，称为**“简洁解码”**（Laconic decoding）。

并行运行5次模型，从答案中选择tokens最少的。

初步实验结果表示，简洁解码在AIME2024测试上能提高6%-7%的准确率，比Consensus Decoding更好也更快。

![](.evernote-content/582E2FEC-514C-43BF-803D-6573491A60A8/BCDCB30C-3FF2-4C89-B921-2754D00F3F8E.png)

论文地址：https://arxiv.org/abs/2501.18585

参考链接：

[1]https://x.com/tuzhaopeng/status/1885179412163027406

[2]https://x.com/AlexGDimakis/status/1885447830120362099

— **完** —

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247775527&idx=1&sn=6b09354433568103fcfaed49b4086871&chksm=e90e3c99d47e024de38ed79c2e7ec7c2449954d1a317eb5dc11061537de04a05cbbb7158d322&scene=90&xtrack=1&sessionid=1738572539&subscene=93&clicktime=1738573193&enterid=1738573193&flutter_pos=19&biz_enter_id=4&ranksessionid=1738573120&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ9TN/vQNRq9RBP4jARJqjNhLWAQIE97dBBAEAAAAAAE5ZJK6dLkUAAAAOpnltbLcz9gKNyK89dVj0MX2T4EoxX7qU8rBXoKIDVmKYJxcwMUKN+bmw/AbuxT/B0eF/TIieH2i4RdZhc+h0S7I+5dDIh03Cy298zvHHhUSOz7DBdWkM8PAHgjo0VMZQF8jlYz9bs4Fdfn2brm94ZwSwgk1LJ6RdGP+XNbf7nKD88u/8+r55lFx9BGsw/u/DZMOuaporPjnwpFBjYTjK0mSuEgvd5GBO+3YEFWjdZ31+PYgdF8fTzs65iyy51Xk=&pass_ticket=iwzO/Jbl6NAKjh9remGllXvA72gvB+kqmfL0kDiLcBXHYThns8f34Cqxf2Q1+lhp&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/953a9722-bc27-48dd-a7cf-3429499183f5/953a9722-bc27-48dd-a7cf-3429499183f5/)
