---
title: 我用 Claude Code 给孩子做了一个他是主角的AI绘本 skill（工作流） 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/我用 Claude Code 给孩子做了一个他是主角的AI绘本 skill（工作流） 2.md
tags: [evernote, impression, yinxiang]
---

# 我用 Claude Code 给孩子做了一个他是主角的AI绘本 skill（工作流）

---

原文链接: [https://mp.weixin.qq.com/s?chksm=c24ce6bef53b6fa81f7cb6ccf972ab0...](https://mp.weixin.qq.com/s?chksm=c24ce6bef53b6fa81f7cb6ccf972ab003cfd6985d4f7f678dc741c2eb5685d709f5cf0d89fa3&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1774078938_1&req_id=1774078938873208&scene=169&mid=2247485968&sn=867703a7b893e7c9f08525ca1f4b8f29&idx=1&__biz=MzkzMzM2MzEzNw==&sessionid=1774078777&subscene=200&clicktime=1774082088&enterid=1774082088&flutter_pos=15&biz_enter_id=5&jumppath=20020_1774082036543,1104_1774082041576,20020_1774082048094,1104_1774082082433&jumppathdepth=4&forceh5=1&ascene=56&devicetype=iOS26.3.1&version=18004533&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ1HvoBKvrgB4WONBjk3OhwhLVAQIE97dBBAEAAAAAAH68Mv8PubEAAAAOpnltbLcz9gKNyK89dVj0Po9+EaBTwLWIuV4LqoExLmjYiNZbIiLKug0uBJsslSjCbJYcy5YG7WGynE9GRcRru5GIXPpfM9BiSDqCuNRCbG4PT85+zeUvKzYG3lfHop9d4OZK7YH7Kbyygy3RoMRdQf99xVW4XP6SQG+mRW2dnALz3SgJBIFZ6taEKgedvrbHDrbn5Hg2Me/0WFecX9ojHt8nE6LP5wYWv6nbIneVzzEmQXshzSd0o1UpaOtzdw==&pass_ticket=HZL+8yR8TBogk1sk5vazMWHXl6MiZdghvH7Bcpiu40XVj0zRR3WVhYS6sNNJ0s17&wx_header=3)

OriginalMQ老师 MQ的AI原住民计划

欢迎关注&星标，一起做**AI原住民**

我给和和做了一本他是主角的绘本
===============

（用 Claude Code 做的）

第三版出来的那一刻，我自己先愣住了。

上一页，小男孩睡在草地上，写着「脚痒痒的」

![](.evernote-content/398A6B68-8D12-46B4-8DA8-3BE7A1B1911D/83E43DD2-5F78-4B21-856C-5E72E95BF9CA.png)

下一页，画面里，小男孩飞向太空。

![](.evernote-content/398A6B68-8D12-46B4-8DA8-3BE7A1B1911D/70936833-7E73-43D8-89EC-16B2C55238DF.jpg)

我盯着屏幕，心想：这……有点好啊。

和和还不知道这本书的存在。我自己先喜欢上了。

01 以前这件事有多麻烦

AI 绘本这两年大家没少见。

但说实话，大部分都一言难尽。

要么角色每页都在变脸——第一页是圆眼睛，第三页变成了长眼睛，第五页干脆换了个人。要么图画了一个孩子在飞，文字也写「他飞起来了」，1+1=1，叠在一起反而变得更平。

这是两道很难的坎：角色一致性和图文真正的配合。

前者让定制绘本一直停留在「尝鲜」阶段——好玩，但做出来自己都觉得凑合。后者让 AI 绘本和真正好的绘本之间，始终有差距。

02 我是怎么迭代工作流的

我用 Claude Code 创建了这个画定制绘本的工作流。只要上传一张孩子的照片，Claude Code 和孩子互动以后，就能创建出以自家孩子为主角的故事绘本。

（Claude Code 是一个自主性更高的 AI 智能体，可以直接执行任务——生成图片、写代码、组装 HTML，一气呵成。）

V1：第一版出来，故事有了，画面也出来了。但和和的形象每页都在飘——这一页胖，下一页瘦，头发长短不一，感觉是六个不同的小男孩客串了同一个故事。

![](.evernote-content/398A6B68-8D12-46B4-8DA8-3BE7A1B1911D/644A66E3-DB63-48B4-A896-FB6D8D6065A5.jpg)![](.evernote-content/398A6B68-8D12-46B4-8DA8-3BE7A1B1911D/2555D568-FB72-48BB-9DC0-B9058212CB0E.jpg)

V2：我把形象固定下来了。专门生成了一张「角色参考图」，每次画新的一页都把这张图一起喂给 AI，让它「照着画」。角色一致性问题基本解决。

![](.evernote-content/398A6B68-8D12-46B4-8DA8-3BE7A1B1911D/8BC61F7D-7977-4E54-A068-ED275D1E0790.jpg)

但 V2 有新的问题——图和文有一种奇怪的累赘感。图已经画得很清楚了，文字又把同一件事说了一遍。读起来像是给画面配了个字幕，多余。

V3：我告诉 AI，图文应该怎么分工。文字只说画面画不出来的东西——触觉、声音、内心感受。画面负责视觉。两者各管一半，让读者自己在缝隙里拼出完整体验。

还有留白。情感最浓的地方，文字反而要退场。

我说完，它迅速就有了进步。

整个 V1 到 V3 的迭代，半小时以内。

后台回复「小和和」，能看到「小和和飞向宇宙」的V2 到 V3 的迭代过程。

03 我以为我在教 AI 做绘本

但做完这件事，我发现自己也学到了东西。

我之前懂一点绘本——知道图文要配合，但不知道怎么配。做这件事的过程中，AI 把真正的方法论带给了我。

松居直说绘本是「文字 × 图画」，不是相加，是相乘。Nikolajeva 和 Scott 把图文关系分四个层次，反衬力量最强，对称是在浪费。Molly Bang 说构图形状本身就在传递情感——水平线是平静，对角线是冒险。

这些东西，AI 都知道。我是跟着它建 Skill 的过程中，才真正弄明白的。

我突然想，如果换一个人类画师，给他讲这套图文分工的逻辑，他理解、消化、真正内化到作品里，大概需要一段时间。

AI 不需要。给到方法论，它立马就能用。

这不是说 AI 比人厉害——画师的感受力、直觉、那种「只可意会」的东西，AI 可能还不能完全做到。

但在「理解并执行一套清晰的老师傅方法论」这件事上，它的进化速度确实让我有点惊异。

04 这件事真正让我兴奋的

不是技术。

是这件事现在属于每一个父母了。

你可以给孩子做一本真正属于他的绘本——他的故事，他来编；他的形象，他是主角；画风，你们一起挑。

它离顶级绘本肯定有差距。但它能到达一个还不错的分数，而且这个分数还在快速往上走。

更重要的是：这本书里，是你孩子的名字，是他的脸，是他想象的宇宙。

你说，这对一个六岁的孩子意味着什么？

05 如果你也想试

这套工作流的逻辑是（可以参考思路，在自己的 cc 里玩起来）

孩子给出主题 → CC 和孩子一起编故事 → 定角色、定画风 → 逐页生成插画 → 组装成可以打开的 HTML 绘本，还有可以打印的 PDF。

孩子可以全程参与。这本书从第一个字开始，就是他的。

这本专属于和和的绘本叫《小和和飞向宇宙》。

他还不知道。

等他看到的那天，我再来告诉你他说了什么。

后台回复「小和和」，能看到「小和和飞向宇宙」的V2 到 V3 的迭代过程。

END

欢迎转发给你朋友圈的妈妈和教育工作者，一起培养在 AI 时代的原住民。

📖 新书推荐：《AI 家庭教育指南》

我和 Evan 妈咪（Crystal 老师）合著的 20 万字实战手册。感谢同路人的支持，目前已经第四次重印。覆盖 AI 时代家庭教育的方方面面——从 AI 伙伴筛选与协作到认知升级，从亲子互动到学习方法。

包含 30+ 应用场景，100+ 上手可用的提示词，随书赠送我们不断认知迭代的智能体。一定要扫码书签，智能体都在里面！

如果你也在思考如何在 AI 时代培养孩子，这本书或许能给你一些启发。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=c24ce6bef53b6fa81f7cb6ccf972ab003cfd6985d4f7f678dc741c2eb5685d709f5cf0d89fa3&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1774078938_1&req_id=1774078938873208&scene=169&mid=2247485968&sn=867703a7b893e7c9f08525ca1f4b8f29&idx=1&__biz=MzkzMzM2MzEzNw==&sessionid=1774078777&subscene=200&clicktime=1774082088&enterid=1774082088&flutter_pos=15&biz_enter_id=5&jumppath=20020_1774082036543,1104_1774082041576,20020_1774082048094,1104_1774082082433&jumppathdepth=4&forceh5=1&ascene=56&devicetype=iOS26.3.1&version=18004533&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ1HvoBKvrgB4WONBjk3OhwhLVAQIE97dBBAEAAAAAAH68Mv8PubEAAAAOpnltbLcz9gKNyK89dVj0Po9+EaBTwLWIuV4LqoExLmjYiNZbIiLKug0uBJsslSjCbJYcy5YG7WGynE9GRcRru5GIXPpfM9BiSDqCuNRCbG4PT85+zeUvKzYG3lfHop9d4OZK7YH7Kbyygy3RoMRdQf99xVW4XP6SQG+mRW2dnALz3SgJBIFZ6taEKgedvrbHDrbn5Hg2Me/0WFecX9ojHt8nE6LP5wYWv6nbIneVzzEmQXshzSd0o1UpaOtzdw==&pass_ticket=HZL+8yR8TBogk1sk5vazMWHXl6MiZdghvH7Bcpiu40XVj0zRR3WVhYS6sNNJ0s17&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9cee63e7-b2c6-4e08-a451-e7c001b09be2/9cee63e7-b2c6-4e08-a451-e7c001b09be2/)
