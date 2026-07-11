# 用了一段时间 Claude Code 以后，我发现一个挺现实的问题：会话一长，信息一多，后面的表现就容易不稳定

---

原文链接: [https://mp.weixin.qq.com/s?ranksessionid=1781246251\_1&chksm=...](https://mp.weixin.qq.com/s?ranksessionid=1781246251_1&chksm=9b1df9ffac6a70e995ae06980af6eeee6d8e9f255757913c92081aeb4ccc447c0688b16c0d1e&exptype=masonry_feed_brief_content_elite_for_feeds_u2i&req_id=1781246251009995&scene=169&mid=2247488080&subscene=200&sn=3017ec648bbb9edc2bd0bd043d6bc6ad&idx=1&__biz=MzAwNTQzOTE2OA==&sessionid=1781246250&clicktime=1781246852&enterid=1781246852&flutter_pos=0&biz_enter_id=5&jumppath=20020_1781246849119,1156_1781246850436,20020_1781246851556,1104_1781246852027&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAdqXHoVpJk4Tut1bScRsvxLTAQIE97dBBAEAAAAAAO6BNtbipxYAAAAOpnltbLcz9gKNyK89dVj0s2xFklzvzJhNMd4U9wD+/LC1B5YvsDu+rs30KJOPMmnE+1Vu62t1VTxG9VLNRqHyrZglcveJfXs5ZDe9XOIrdkP14Ki12CuY1O9xYIpfsMJ6ToqJ9wjfly11G0Pi2RKFSbqn9q0cOuGkHj6lo1ndtXBQTHwIA9dFXC+E4ZM11Wc9D0PVjewGy3kuUF/AXlIEgEI5NgLvH0kS7/Unj449dDkVvb0K8kZB5eyVJkM=&pass_ticket=mabydk6N+IRbjNIcxCGNF3LEoq3cFUHh4eQY2PhZWBfhA6SsT4NDn6wtzEwCOzqM&wx_header=3)

![](.evernote-content/F4381351-82C4-46EC-807E-C3DAF1C75648/34AFAF4E-D31B-48C5-BB52-3F8E4FB302BD.jpg)

用了一段时间 Claude Code 以后，我发现一个挺现实的问题：会话一长，信息一多，后面的表现就容易不稳定。

有时候不是它能力不行，而是上下文里堆了太多东西。

前面聊过的需求、改过的文件、临时补充的想法，全混在一起，后面它再继续改，就容易理解偏。

`claude-hud` 这类插件挺有价值。GitHub 地址：https://github.com/jarrodwatts/claude-hud

它有点像给 Claude Code 加了一个仪表盘。

我们在使用 Claude Code 的过程中，再也不用凭感觉判断当前状态，能实时看到上下文使用率、模型、分支、工作目录、任务进度这些信息。

安装方式也很简单，GitHub 地址发给 Claude Code，就可以自动安装。

我自己的经验是：上下文使用率到 30% 左右的时候，就要开始特别关注了。

这个阶段通常还能比较充分发挥 AI 的能力，但如果继续堆太多信息，后面的理解、执行和稳定性就可能慢慢下降。

个人建议尽量少用 `/compact`。压缩上下文确实能让会话继续跑下去，但压缩一定会带来信息损耗，有些前面讨论过的细节、临时决策、边界条件，压缩之后可能就没那么完整了。

一个相对独立的任务结束后，最好直接新开一个窗口。如果是复杂任务，一开始就拆小，不要让一个会话无限拉长。

与其一直研究更多提示词技巧，不如先把精力放在控制上下文使用率上。

上下文越清楚，AI 的能力越容易发挥出来。

高效使用 Claude Code 之前，先给自己装一个看得见的仪表盘。

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?ranksessionid=1781246251_1&chksm=9b1df9ffac6a70e995ae06980af6eeee6d8e9f255757913c92081aeb4ccc447c0688b16c0d1e&exptype=masonry_feed_brief_content_elite_for_feeds_u2i&req_id=1781246251009995&scene=169&mid=2247488080&subscene=200&sn=3017ec648bbb9edc2bd0bd043d6bc6ad&idx=1&__biz=MzAwNTQzOTE2OA==&sessionid=1781246250&clicktime=1781246852&enterid=1781246852&flutter_pos=0&biz_enter_id=5&jumppath=20020_1781246849119,1156_1781246850436,20020_1781246851556,1104_1781246852027&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAdqXHoVpJk4Tut1bScRsvxLTAQIE97dBBAEAAAAAAO6BNtbipxYAAAAOpnltbLcz9gKNyK89dVj0s2xFklzvzJhNMd4U9wD+/LC1B5YvsDu+rs30KJOPMmnE+1Vu62t1VTxG9VLNRqHyrZglcveJfXs5ZDe9XOIrdkP14Ki12CuY1O9xYIpfsMJ6ToqJ9wjfly11G0Pi2RKFSbqn9q0cOuGkHj6lo1ndtXBQTHwIA9dFXC+E4ZM11Wc9D0PVjewGy3kuUF/AXlIEgEI5NgLvH0kS7/Unj449dDkVvb0K8kZB5eyVJkM=&pass_ticket=mabydk6N+IRbjNIcxCGNF3LEoq3cFUHh4eQY2PhZWBfhA6SsT4NDn6wtzEwCOzqM&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7ccb83db-0289-43b1-8e16-1781d6ee8cd1/7ccb83db-0289-43b1-8e16-1781d6ee8cd1/)