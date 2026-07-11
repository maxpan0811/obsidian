# 🔥用Claude Code写了一周代码的真实感受

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA4NjEwMTQ1NA==&mid=245386...](https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=2453864423&idx=1&sn=0a537ec101029a8b0530031f3ce4eff6&chksm=887b8346bf0c0a5099c9fd58309d187bd40c3a264ac34dc397953816c1bc850a8d32c9abc715&exptype=servicebox_7442919188105420800&subscene=0&scene=288&clicktime=1774531397&enterid=1774531397&flutter_pos=2&biz_enter_id=5&ascene=56&devicetype=iOS26.4&version=18004626&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQPXHBhWSkobw2lZJP11Hl4hLTAQIE97dBBAEAAAAAANtJOfymS+kAAAAOpnltbLcz9gKNyK89dVj0Tca828wwgA8Y8Mnbtw7iQsY049mqhnHyBRBiaEnFJKnUtMCc3lHky/U3szHp6iGTx4mVUh/Y7DdYWHyg77yD6usqK73g2AGNsfqIudrvvfZtHvTbC0IDH3rIuZmFzxbQDeeGsbWP3JfmitHDsxink9HK7atOPiohzUHses1ykhnHbzo2CwQrrea7v5iexAEsnjXf7dMRT5XCu5n3CK/TjMLGOloO2CN3z6ScN5o=&pass_ticket=JyWLedyeoQBhJEYkT0GkNhQIYVpFvzZyZH7H2m1GG3AlpLaSbftnQFtnWrYSLLIa&wx_header=3)

![](.evernote-content/F6727384-ED67-47CE-B721-FA4B736AE0F7/83CEBBF0-5509-4B47-BE44-7FF83093576A.jpg)![](.evernote-content/F6727384-ED67-47CE-B721-FA4B736AE0F7/00AB4947-E7D2-4535-91B2-93E342300881.jpg)![](.evernote-content/F6727384-ED67-47CE-B721-FA4B736AE0F7/B4DAC038-9C9C-422A-9FCF-26ED413AF8A3.jpg)![](.evernote-content/F6727384-ED67-47CE-B721-FA4B736AE0F7/25ECEE7C-2795-4A41-BF1E-AC47D0E312D3.jpg)![](.evernote-content/F6727384-ED67-47CE-B721-FA4B736AE0F7/67BF1FE4-0861-4ED5-9F48-836A7F9AD03B.jpg)

最近把日常开发主力工具换成了Claude Code，认真用了一周多，来聊聊真实体验。

先说说它是什么。Claude Code是Anthropic出的一个命令行AI编程工具，直接在终端里运行，不需要IDE插件，任何项目目录下敲个claude就能开聊。

最让我震撼的是它对项目的理解能力。之前接手一个老项目，几十个文件完全没文档，我说"帮我理清这个项目的认证流程"，它自己去翻了十几个文件，从路由到中间件到数据库模型，给我画出了完整的调用链路。这个过程我自己做可能要半天，它几分钟就搞定了。

改bug的体验也很不一样。有一次遇到一个偶现的并发问题，我把报错日志贴给它，它没有上来就猜答案，而是先去读了相关的锁机制代码，又看了测试用例，最后定位到是一个事务隔离级别的问题。这个排查思路比很多初中级工程师都靠谱。

重构是我用得最多的场景。比如要把一个大函数拆成几个小函数，或者把回调改成async/await，它能自动追踪所有调用方，一次性改完，不会漏改。之前我手动重构最怕的就是改了A忘了B，现在基本不担心这个问题。

还有一个很实用的能力——它能直接操作终端。跑测试、git提交、创建PR这些都可以让它代劳。我现在的工作流是写完需求描述，让它生成代码，我review一遍，然后让它跑测试、修复问题、最后提交。整个过程很流畅。

它还支持MCP协议接入外部工具。我接了Playwright插件之后，它能直接控制浏览器帮我做自动化操作，接了GitHub插件能直接查看PR评论和issue。这个扩展性是真的强。

说说不足。它偶尔会过度设计，一个简单的功能给你加一堆错误处理和抽象层，需要你在prompt里强调"保持简单"。另外对于特别大的项目，上下文窗口还是会成为瓶颈，复杂任务有时候需要拆成几步来做。

总的来说，它不是替代程序员的工具，而是一个很强的协作伙伴。用好了之后效率提升非常明显，尤其是那些重复性高、需要大量上下文理解的工作。推荐所有开发者都试试。

![](.evernote-content/F6727384-ED67-47CE-B721-FA4B736AE0F7/1326B4F3-4A0D-46BD-A9BC-2AB4521F7AD8.jpg)

HiddenState

Like the Author

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=2453864423&idx=1&sn=0a537ec101029a8b0530031f3ce4eff6&chksm=887b8346bf0c0a5099c9fd58309d187bd40c3a264ac34dc397953816c1bc850a8d32c9abc715&exptype=servicebox_7442919188105420800&subscene=0&scene=288&clicktime=1774531397&enterid=1774531397&flutter_pos=2&biz_enter_id=5&ascene=56&devicetype=iOS26.4&version=18004626&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQPXHBhWSkobw2lZJP11Hl4hLTAQIE97dBBAEAAAAAANtJOfymS+kAAAAOpnltbLcz9gKNyK89dVj0Tca828wwgA8Y8Mnbtw7iQsY049mqhnHyBRBiaEnFJKnUtMCc3lHky/U3szHp6iGTx4mVUh/Y7DdYWHyg77yD6usqK73g2AGNsfqIudrvvfZtHvTbC0IDH3rIuZmFzxbQDeeGsbWP3JfmitHDsxink9HK7atOPiohzUHses1ykhnHbzo2CwQrrea7v5iexAEsnjXf7dMRT5XCu5n3CK/TjMLGOloO2CN3z6ScN5o=&pass_ticket=JyWLedyeoQBhJEYkT0GkNhQIYVpFvzZyZH7H2m1GG3AlpLaSbftnQFtnWrYSLLIa&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ea5bbf71-cd21-4edf-a687-9709885d4e6f/ea5bbf71-cd21-4edf-a687-9709885d4e6f/)