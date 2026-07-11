# 比你想的更简单！Claude Code 官方的Loop循环设计指导

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518687&idx=1&sn=b7bba6e5ecc4f965ef4a2fc99ee3302f&chksm=e908fb1b10b31629cad69ff9aef059419a1313e95a59ece6de7fb78eccdb7be73152552e0dcc&scene=90&xtrack=1&req_id=1783431192707702&sessionid=1783431181&subscene=93&clicktime=1783431582&enterid=1783431582&flutter_pos=4&biz_enter_id=4&ranksessionid=1783431192&jumppath=20020_1783431192177,1104_1783431538420,20020_1783431546713,1104_1783431575381&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b35&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQE/D6WU4ksFxBOI/4yr4ckBLTAQIE97dBBAEAAAAAAPIVFqVieWMAAAAOpnltbLcz9gKNyK89dVj0gViHPbtC8N2KOHlbjVbRIdLyskXnoGoCx9N3VL6bbbALKYqMaS+pDqNRuMjDLbupNBRWvBsahTSE1Y06HnP125mUoebDx6ykbM9Oiq58Y0dsGRffbO+MRNL2x0H76WZd8zjupb52uEVj/RrnWYouFklRX2l6+S2oC3G6gzjxyltms3Rm4NBSs1FcN2sua2v31bhgKkBa6QqSroglTbh6QFi8I89+xYtqjtUr8Qk=&pass_ticket=pHL+xjIGm7yQ19Hl+8xQ6IC7na2x2oKBiQWvZIACRQMR8MFh76tiwTT35f5LgNAy&wx_header=3)

Original字节笔记本字节笔记本

AI 圈子最喜欢造名词。

仿佛不整点生僻词汇就显得不够高大上，不讲得云山雾罩就衬托不出自己有多懂行。

我本人对这种东西真的是深恶痛绝，不信这你去搜索一下那些讲"Loop Engine"的文章，一个个说得头头是道，看完之后你脑子里绝对是一片空白，压根不知道他到底在讲什么，最后听君一席话，如听一席话。

说白了，所谓的 Loop，翻译过来也就是让 Agent 按某种规律重复干活而已，哪有那么多花头？  
  
今天 Claude 官方出了一份关于设计循环Loop的指南Getting started with loops，看完你会发现，这个概念就是旧瓶装新酒。

![](.evernote-content/FA74D96B-AE81-4570-B889-25EECF1BD688/BF1DAEAD-6328-438D-A1C6-54A04E397F06.jpg)

各路媒体热衷造词，某种程度上就是在贩卖焦虑，让你觉得不跟上这些黑话就落后了。但拆开来看，说白了就是把工具用明白，仅此而已。  
  
那循环到底是什么？

Claude Code 团队给了个相对靠谱的定义：

Agent 不断重复执行工作周期，直到满足某个预设的停止条件。

拆开看其实是四种套路，分别对应触发方式、停止条件、依赖的基础指令、适用场景。  
  
  
第一种，回合制循环。

触发靠你手动输入，停止靠Claude自己判断活儿干完了。

这种循环适合于那些临时起意、不进常规流程的短任务。

做法就是把你脑子里验收标准写进SKILL.md，比如规定UI改完必须启动开发服务器、真实点一遍按钮、截图对比、查控制台报错。

验证标准越量化，Claude自我判断的准头就越高，你来回改的次数自然就少了。

**第二种，目标导向循环，靠`/goal`触发。**

也讲过。[Codex&Claude Code的 /goal 指令的高级进阶使用技巧](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247516287&idx=1&sn=b09eacc8e7f33cc93a927bc063a28fe7&payreadticket=HCmqwkiBT1hKfNXqGsIwJQhqWsaaDUVmbuulyuAcOgBfTFVWGCySkp4zc_FtviTP2esCAtI&scene=21#wechat_redirect)

说白了就是给一个目标，给一个标准，让 Agent 做。

例如："Lighthouse跑分提到90分以上，尝试5次为止"。

它就会不断迭代，直到达标或者撞上次数上限才收手，这种就适合有明确客观数据能判断对错的活儿。

**第三种，基于时间的循环**

同样讲过：[Loop Engineering 解析&应用案例](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518081&idx=1&sn=8882884596a51004fe5b9a3d68e4aeb9&payreadticket=HMzXeSD2VROUmWp3CAI72Ggnq8dc1LsNSq3XLQqVcloPM8q1o26Zjq9jLqdYae86HYqVh14&scene=21#wechat_redirect)

所使用的工具就是**`/loop`和`/schedule`。**

有些活是周期性的，比如每天早上汇总一遍 Slack， 有些是需要盯着外部系统变化的，比如盯一个可能随时收到review意见或者CI跑挂的PR。

`/loop`在你本地跑，关机就停，想搬到云上7x24小时值班，用`/schedule`。

第四种，主动式循环。

把前面三种加上动态工作流、自动模式拼在一起，就是主动式循环。

它就能处理长期跑的复杂工作流，比如漏洞分诊、依赖升级这类源源不断的活。

怎么组合？

用`/schedule`定时检查有没有新反馈，用`/goal`定义"本轮所有报告都处理完才算完"，再用动态工作流让几个Agent分头去分类、修复、审查，最后开自动模式让整条流水线不用你手动点确认。

关于代码质量这块，官方建议是代码库本身干净，Claude写出来的东西才会跟着干净。

用一个没被历史对话带偏的全新Agent做code review，偏见更少。

这条我自己深有体会，用同一个上下文一路跑到底的Agent，很容易陷入自己骗自己的循环，找个干净上下文的裁判角色，效果立竿见影。具体做法可以看[Fable5 仅用 2%的额度 1:1 复刻 Notion](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518648&idx=1&sn=f5007382ddf222cf10c5711dde4e3df8&scene=21#wechat_redirect)

Loop这种东西它也并不是万能药，首先是token消耗极大，所以小任务别动用多Agent复杂循环，杀鸡用不着牛刀。

大规模跑动态工作流之前先切小块试跑，心里有底再上量。

确定性的工作直接上脚本，别指望大模型每次现场推理一遍，以现在的模型能力来长时间跑不跑偏，很难很难，即使是 Fable 5。

循环也不是越复杂越好。

先从最简单的回合制开始，找一个你手头总卡壳的任务，问自己三个问题：

能不能写出自动验证的检查项？目标够不够清晰？任务是不是按周期发生的？

想清楚这三条，该用哪种循环基本就有答案了。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518687&idx=1&sn=b7bba6e5ecc4f965ef4a2fc99ee3302f&chksm=e908fb1b10b31629cad69ff9aef059419a1313e95a59ece6de7fb78eccdb7be73152552e0dcc&scene=90&xtrack=1&req_id=1783431192707702&sessionid=1783431181&subscene=93&clicktime=1783431582&enterid=1783431582&flutter_pos=4&biz_enter_id=4&ranksessionid=1783431192&jumppath=20020_1783431192177,1104_1783431538420,20020_1783431546713,1104_1783431575381&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b35&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQE/D6WU4ksFxBOI/4yr4ckBLTAQIE97dBBAEAAAAAAPIVFqVieWMAAAAOpnltbLcz9gKNyK89dVj0gViHPbtC8N2KOHlbjVbRIdLyskXnoGoCx9N3VL6bbbALKYqMaS+pDqNRuMjDLbupNBRWvBsahTSE1Y06HnP125mUoebDx6ykbM9Oiq58Y0dsGRffbO+MRNL2x0H76WZd8zjupb52uEVj/RrnWYouFklRX2l6+S2oC3G6gzjxyltms3Rm4NBSs1FcN2sua2v31bhgKkBa6QqSroglTbh6QFi8I89+xYtqjtUr8Qk=&pass_ticket=pHL+xjIGm7yQ19Hl+8xQ6IC7na2x2oKBiQWvZIACRQMR8MFh76tiwTT35f5LgNAy&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6dad4045-1f95-401b-b4f7-45a8e9fa5af6/6dad4045-1f95-401b-b4f7-45a8e9fa5af6/)