# 原来顶级AI团队，是这么写CLAUDE.md

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzcwNjE3NDkyNg==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzcwNjE3NDkyNg==&mid=2247483808&idx=1&sn=3a0ae5eb4ebbcd5d50658f2cb31d7e62&chksm=f4d90b01c3ae8217559b216ab07d922be87512c9343473c5ab824df67d4a520ec943e2c26377&from_masonry=1&sessionid=1781019577&subscene=288&scene=132&ascene=0&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQtOxAXAGTDDmnIpfAVjYs+hLTAQIE97dBBAEAAAAAAF1VBv2eBPMAAAAOpnltbLcz9gKNyK89dVj09inEVcDL2BSf/raeGDnibgG2ehZafECS3vrOpFHsDcOgKokuZOo8Na1hQH8ZxEIys5awnUWPxiXDNqAY/R/b/RZ1C6/DnqWapJYpbXulwtOcfEvKt4zvGbbwBWMhevLw1v1DHywcM+71UIv9J1t134xhjBEybABrwWndubNvhOO7UAqQJd5c1fiIWXxJvf2Ei38b+NHFCP5b5fZ42sBP+XddYN1h1eQCODSzlbA=&pass_ticket=vf/rPk3/oOxMEllHkti+tYNdsvwawBbhkeUjuEcp5oF+wav8h9iEin14S6iTgsNH&wx_header=3)

![](.evernote-content/67E5FED6-7117-4A49-9E33-487A6DD25C6B/41513F28-264E-4E97-A511-20B28F0D6EA1.png)![](.evernote-content/67E5FED6-7117-4A49-9E33-487A6DD25C6B/1D5CB43E-EF3F-4A9B-B98E-A137758BFE42.png)![](.evernote-content/67E5FED6-7117-4A49-9E33-487A6DD25C6B/8D73D2CF-F602-4C86-86E1-49264F03A99D.png)![](.evernote-content/67E5FED6-7117-4A49-9E33-487A6DD25C6B/E7C1252F-A5C1-4A83-A8D4-8F4F7356F315.png)![](.evernote-content/67E5FED6-7117-4A49-9E33-487A6DD25C6B/B0DAD7B1-6821-4FD4-8475-515938A682A7.png)

翻了几十个GitHub高星项目的CLAUDE.md和AGENTS.md，本来只是想学点配置技巧，结果发现一件挺反直觉的事：

真正会用AI Agent的工程团队，不只是换更强的模型，也不是写一堆玄学prompt。

他们会先给模型写一份很明确的规则清单，比如：

开始前先列计划；

改文件前必须先读文件；

不确定就停下来问；

不要顺手修无关问题；

没跑过测试不算完成。

这些听起来都很基础，但恰恰是Agent最容易失控的地方。

因为模型很聪明，但它并不知道你的工程边界在哪里。

你不写清楚，它就会自己猜、自己扩展、自己决定下一步。

所以CLAUDE.md的本质，不是限制AI，而是把人类默认知道的协作规矩，翻译成模型能执行的SOP。

我把GitHub高星项目里最值得抄的8条规则整理成了这组图。

每条都可以直接复制进你的CLAUDE.md，再按自己的项目微调。

完整版，包括每条规则的项目出处、原文上下文和我为什么这么改，已经整理在公众号文章里。

[顶级AI工程团队偷偷写在CLAUDE.md里的8条规则，我替你挖出来了](https://mp.weixin.qq.com/s?__biz=MzcwNjE3NDkyNg==&mid=2247483798&idx=1&sn=bc98783dbcab2f4852f4e5882a3c2880&scene=142#wechat_redirect)

#CLAUDEmd#Claude#Harness#AI编程#AIAgent#ClaudeCode#AI#规则文件

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzcwNjE3NDkyNg==&mid=2247483808&idx=1&sn=3a0ae5eb4ebbcd5d50658f2cb31d7e62&chksm=f4d90b01c3ae8217559b216ab07d922be87512c9343473c5ab824df67d4a520ec943e2c26377&from_masonry=1&sessionid=1781019577&subscene=288&scene=132&ascene=0&devicetype=iOS26.5&version=18004a2a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQtOxAXAGTDDmnIpfAVjYs+hLTAQIE97dBBAEAAAAAAF1VBv2eBPMAAAAOpnltbLcz9gKNyK89dVj09inEVcDL2BSf/raeGDnibgG2ehZafECS3vrOpFHsDcOgKokuZOo8Na1hQH8ZxEIys5awnUWPxiXDNqAY/R/b/RZ1C6/DnqWapJYpbXulwtOcfEvKt4zvGbbwBWMhevLw1v1DHywcM+71UIv9J1t134xhjBEybABrwWndubNvhOO7UAqQJd5c1fiIWXxJvf2Ei38b+NHFCP5b5fZ42sBP+XddYN1h1eQCODSzlbA=&pass_ticket=vf/rPk3/oOxMEllHkti+tYNdsvwawBbhkeUjuEcp5oF+wav8h9iEin14S6iTgsNH&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/edb188a2-6f6d-4f60-9d30-980d176b463f/edb188a2-6f6d-4f60-9d30-980d176b463f/)