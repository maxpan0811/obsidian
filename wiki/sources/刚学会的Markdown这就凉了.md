---
title: 刚学会的Markdown，这就凉了？MD已死，HTML当立
type: source
created: 2026-05-29
updated: 2026-05-29
sources: [刚学会的Markdown，这就凉了？MD已死，HTML当立！Claude Code的5大HTML实用场景.html]
source_path: 印象笔记管理工具/刚学会的Markdown，这就凉了？MD已死，HTML当立！Claude Code的5大HTML实用场景.md
tags: [claude-code, html, markdown, productivity]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "刚学会的Markdown，这就凉了？MD已死，HTML当立！Claude Code的5大HTML实用场景"
source: evernote
type: note
export_date: 2026-06-26
guid: 11bf5dbb-89d4-4b84-b341-0fea41bf6a44
---

# 刚学会的Markdown，这就凉了？MD已死，HTML当立！Claude Code的5大HTML实用场景

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzA4NjEwMTQ1NA==&mid=245386...](https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=2453865466&idx=1&sn=9a8689348c1943bf0296fe22cfcfe337&chksm=89b8fa979c289ace7004149445a235498367ba40a1af72f8ce7df8d4cce35da37ecaa810ccf2&scene=90&xtrack=1&req_id=1779066073178589&sessionid=1779066065&subscene=93&clicktime=1779066107&enterid=1779066107&flutter_pos=9&biz_enter_id=4&ranksessionid=1779066073&jumppath=20020_1779066072501,1104_1779066074630,20020_1779066082002,1104_1779066102483&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQZnnoar8IvRneUaa1cP/h3xLTAQIE97dBBAEAAAAAALHFJg3fIpIAAAAOpnltbLcz9gKNyK89dVj0+xkmu7ibJJCrBkccmoihpNiuzzbI3w+ItTns0kWl+OPtL4Qoj0RBTHJEWvEv7/VSyqc/PetPUopefVj/8o65juBrYqEkeElqW5RC+SSQTDNMwuKAscFkoEUapvhjJyGndEuhD3tdy3k9VPgZ6KRWLtNCVSy+UiKQvIJfGBvH6FLic92Se3nySc0pB48S5gJSBV+uzJxPpr5BZX8ZRqxbeXgzhWwTWyN9EMp+vsE=&pass_ticket=xso5EXjvJVnX1HFAk4Qy1JRsFLZxFr87cvoebLhTKfxwk8S1JzbSD3ZaaGCYWaes&wx_header=3)

OriginalHiddenStateHiddenState

我刚学会写Markdown，你跟我说它要凉了？

最近Anthropic的Claude Code工程负责人Thariq发的一篇长文在X上获得了超1500万的阅读，翻译过来就是：

「用Claude Code做事，HTML好用得离谱。」

他说自己现在做规划、写报告、代码审查，全都让 Claude Code 输出 HTML。Markdown？基本不碰了。

评论区里AI界著名的 Karpathy 卡神也说：这方法是真的好用。

但试了几天之后，我觉得Markdown和HTML各有优劣。

![](attachments/7ef37d77a8a15d27.png)

为什么HTML比Markdown强？

Markdown是给人手写设计的，HTML是给机器生成设计的。

当写文件的不再是你而是AI的时候，Markdown那套方便手写的优势就不存在了。

Thariq总结了HTML的三个碾压点：

![](attachments/22d8cd5102440040.png)

第一，信息量天差地别。

Markdown能干啥？标题、加粗、列表、代码块，没了。

Claude在Markdown里画流程图只能用ASCII码拼，像逼画家用筷子画油画。

HTML的表格、CSS样式、SVG图表、折叠面板、标签页切换——同样200行的技术方案，Markdown版瞟一眼就关了，HTML版就能认真读完。

![](attachments/b250c15c5b5b9669.png)

第二，分享成本为零。

Markdown文件发给同事，对方还得找个能渲染的工具打开。

HTML浏览器直接打开，甩个链接就行。

你的方案被老板真正读到的概率，直接翻倍。

第三，可以交互。

HTML里能加滑块、按钮、拖拽。

你可以让Claude做一个左右分栏的prompt编辑器——左边改prompt，右边实时预览，改完一键复制。

![](attachments/5531417a6d10bb82.png)

下面是重点：

我实测了5个使用HTML输出的好用的场景，直接告诉你怎么用。

1️⃣ 方案对比：

以前做技术选型，Claude给我一堆Markdown文字，看得眼花。

现在我说：「把三个方案做成HTML，网格并排对比，每个标注优劣」，出来的页面一眼就能看出哪个好。

2️⃣ 代码审查：

让Claude生成HTML格式的审查报告——行内批注、按严重程度标颜色、还能画流程图解释逻辑。

比纯文字的PR description清晰十倍。

3️⃣ 项目规划：

别写plan.md了。

一句prompt：帮我做项目规划的HTML页面，要有时间线、可折叠的任务详情、风险用红黄绿标注。

4️⃣ 一次性小工具：（我最爱的玩法）

30个任务要排优先级，让Claude做个拖拽看板。

调system prompt，做个左右分栏编辑器。用完就扔，但省下的时间远超你描述需求的30秒。

5️⃣ 研究报告：

让Claude翻你的代码库、git历史、网上资料，整合成一份HTML报告——带目录导航、带图表、带引用来源。

![](attachments/45bf5a36cad4baaf.png)

但有一点需要明确：HTML是更费token的！

HTML生成大概是Markdown的2-4倍token消耗。

有人算过账，一年多花5000美元。

但Thariq的反驳我觉得有道理：一份你真的会认真读的HTML，价值远大于一份你看两眼就关掉的Markdown。

👀

---

我的建议是：日常笔记、CLAUDE.md、README这些还是用Markdown。

但凡要给别人看的、需要对比分析的、一次性工具类的，直接上HTML。

![](attachments/d92ef0b131429b47.png)

不是Markdown不好，是写文件的人变了。

当创作者是AI的时候，那个为「方便人类手写」设计的格式，确实该让位了。

  
  
  

---


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzA4NjEwMTQ1NA==&mid=2453865466&idx=1&sn=9a8689348c1943bf0296fe22cfcfe337&chksm=89b8fa979c289ace7004149445a235498367ba40a1af72f8ce7df8d4cce35da37ecaa810ccf2&scene=90&xtrack=1&req_id=1779066073178589&sessionid=1779066065&subscene=93&clicktime=1779066107&enterid=1779066107&flutter_pos=9&biz_enter_id=4&ranksessionid=1779066073&jumppath=20020_1779066072501,1104_1779066074630,20020_1779066082002,1104_1779066102483&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQZnnoar8IvRneUaa1cP/h3xLTAQIE97dBBAEAAAAAALHFJg3fIpIAAAAOpnltbLcz9gKNyK89dVj0+xkmu7ibJJCrBkccmoihpNiuzzbI3w+ItTns0kWl+OPtL4Qoj0RBTHJEWvEv7/VSyqc/PetPUopefVj/8o65juBrYqEkeElqW5RC+SSQTDNMwuKAscFkoEUapvhjJyGndEuhD3tdy3k9VPgZ6KRWLtNCVSy+UiKQvIJfGBvH6FLic92Se3nySc0pB48S5gJSBV+uzJxPpr5BZX8ZRqxbeXgzhWwTWyN9EMp+vsE=&pass_ticket=xso5EXjvJVnX1HFAk4Qy1JRsFLZxFr87cvoebLhTKfxwk8S1JzbSD3ZaaGCYWaes&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/11bf5dbb-89d4-4b84-b341-0fea41bf6a44/11bf5dbb-89d4-4b84-b341-0fea41bf6a44/)
