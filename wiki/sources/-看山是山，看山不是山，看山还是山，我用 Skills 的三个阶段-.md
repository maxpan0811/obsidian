---
title: "看山是山，看山不是山，看山还是山，我用 Skills 的三个阶段"
type: source
created: 2026-06-28
updated: 2026-06-28
source_path: 印象笔记管理工具/看山是山，看山不是山，看山还是山，我用 Skills 的三个阶段.md
tags: [evernote, impression]
---
---
title: "看山是山，看山不是山，看山还是山，我用 Skills 的三个阶段"
source: evernote
type: note
export_date: 2026-06-28
guid: c4e8adc1-8928-4eb2-8ae2-62eeb7b1cde4
---

# 看山是山，看山不是山，看山还是山，我用 Skills 的三个阶段

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518394&idx=1&sn=a096ec4304557cdb2674aecc5261f5c8&chksm=e9e33fa2d391460fa41f3efff8f87cca1e862602740b6ec869e33dd10356ebd6c7103632a616&scene=90&xtrack=1&req_id=1782304563947128&sessionid=1782304295&subscene=93&clicktime=1782305042&enterid=1782305042&flutter_pos=4&biz_enter_id=4&ranksessionid=1782304563&jumppath=20020_1782304563171,1104_1782304736658,20020_1782304752025,1104_1782304851246&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQJuuoHt3m4I/6v4W4Qy+K7RLTAQIE97dBBAEAAAAAACEiOsmFILAAAAAOpnltbLcz9gKNyK89dVj0QRdAFi5wir9Yr0S+OKFbcnl9yrVKLXY917h08ZYWUkuJt3AAFq1+81GntZcvcVBHFQXqeykwkl0gmsxxQHUWidHsQU92dZaH7NqUDp36FJgW8AWrzs0PvZs9npZKharnshIRG7FmRY+bx8qIGctXk6myifKPnylsTOtBhFBbDFYaKGNo7ayPM4wrKvlXA/Igac8PM8VRoFfcsjkehuLN3aKQL64yhGvzLCupsDI=&pass_ticket=jGcwfPtDSJrkvPsXD/EIdGGt4Z8L8qA8rML9PgiB7Bgad0RmHcbd0Kbh/iGh7qM9&wx_header=3)

Original字节笔记本字节笔记本

我最开始管理Skills的方式是把近百个 Skill全部都塞进全局的配置目录，装完拉倒。

打开任何项目，Skills 都在，想用哪个就调用用哪个，看起来非常方便。

但随着 Skills 的迅速膨胀，光是摘要描述就会占用了大量的上下文，而且Coding 工具越来越多，还需要在不同的工具之间来回的复制这些 Skill，更可怕的是，一旦某个 Skill更新，维护起来就是一场灾难。

我后面才意识到这东西不是越多越堆越好，能力没增加，倒是噪声越来越大。

这是第一阶段，看山是山。

第二阶段，我写了SkillsLM这个桌面端工具。

将所有的 Skills 进行集中化的管理，把全局全部清掉，只在需要的工具、需要的场景和需要的项目下才同步对应的 Skill，不再做机械地复制粘贴。

![](attachments/8c98991c2f166fab.png)

这也是SkillsLM 这个工具的核心所在，不管电脑里面有多少的Skills，仓库里面只需要维护这一份Skills，一处修改，处处应用。

这阶段看山不是山，把 Skills 当成代码来管，有仓库、有版本、有测试。

最近我又重新升级了 SkillsLM，这次升级的核心理念就是不把 Skills 看成是 Skills。

如何理解呢？以我最近整理使用 FRP 的配置为例，装完之后没有刻意做成一个 Skill，没有写 SKILL.md，没有遵从任何格式规范。

只是建了一个目录，放了 FRP 的链接文档、几份配置文件、跑通过的稳定版本。

![](attachments/7243c45a8a0c5d58.png)

我专门在电脑下面放了一个这么样的目录，然后通过 SkillsLM 的目录浏览方式，复制文件的路径链接给 Agent ，让它直接读这个目录。

它没有完全按照 Skills 的规范来，甚至都没有一个专门的 Skills.md 的入口文件，但它做到了 Skill 所有应该做的所有事，固化了经验，下再次复用。

而且它是真正的按需加载，一旦它适应了某个项目，那我就可以直接把它写入到整个项目的 Claude.md 当中，下次读取的时候直接从这个入口文件就可以读取到对应的目录链接，连项目级的 Skills 配置也不需要了。

![](attachments/15309405c32cbab6.png)

这就是第三阶段，看山还是山。

这个阶段看什么都可以是 Skill。一段提示词是，一份配置文件是，一堆文档加链接也是，一个脚本也是，某次跑通之后留下的那个稳定版本也是。

只要 Agent 能读、能调用，是经验总结固化成的一个完整工作流，那么它就是 Skill，都是去实现将经验从大脑从本地里面拿出来交给 Agent 的认知接力。

而所谓的管理 Skills，本质上就是在管理着自己的上下文资产。

[榨干GPT！ChatGPT Web变身本地Codex，额度直接翻倍](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518164&idx=1&sn=fffd970106442d518e6659408909bdad&payreadticket=HF5aab_wuwe9B416dI40gcxNPLesPPK7YKdAa4mRqajAhJxEkqu7FrFyDlqEmJTsF_HQUyU&scene=21#wechat_redirect)

[今天最后一天！Codex 重置卡你还没拿吗？](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518381&idx=1&sn=e03b36de6831583686aff999bf69a3ca&scene=21#wechat_redirect)

[Claude Code 多窗口并行人都切麻了？ 一个看板, 掌控全局！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518334&idx=1&sn=f6ee965bcb2baec310819ce7dc8165d4&scene=21#wechat_redirect)
