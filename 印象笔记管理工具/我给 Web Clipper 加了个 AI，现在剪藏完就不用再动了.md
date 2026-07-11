# 我给 Web Clipper 加了个 AI，现在剪藏完就不用再动了

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI4OTkyODUzOA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzI4OTkyODUzOA==&mid=2247484053&idx=1&sn=e71da294510b243fc48377e292a5af17&chksm=ed883ac14d2804e4c59e4843264c1499b3c0d59e36c9c26e8fa7358ea3613ac0e00feefa7ef2&scene=90&xtrack=1&req_id=1779029786693150&sessionid=1779028622&subscene=93&clicktime=1779030185&enterid=1779030185&flutter_pos=91&biz_enter_id=4&ranksessionid=1779029786&jumppath=WAWebViewController_1779030161363,WAWebViewController_1779030161850,20020_1779030176224,1104_1779030177170&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0Sx1/NZs7gYQHUC/2MZ0yxLTAQIE97dBBAEAAAAAALJ7FWFo+nEAAAAOpnltbLcz9gKNyK89dVj0/E5Bp4WZQXjbqQZ45OOeZqyFJVPaWL9Rde0ueYOaCR6GVFU5Sm/6RJqeyVqtqDFKIVQ3vGdOqCdkxKuqKqvBdcPSob1B9KI0wZXglHHG996xozHfzVV5r4Ac7G7Mpu2UXlK2H7HxcC0PoEFvjqtbzgLggzS6k0/SGh0w8mOS2MaK3gPlE3DbupEcBRDBjoL+voR2rSSn5GVtPDCm27JR/RC70udJTV8tMuq5F2E=&pass_ticket=jiXvJJDTeWTEL/XVQGk2WLf/RX6ebYGQCSmuE1MQES1Qhb47b0a2+bV0kvYikAPX&wx_header=3)

Original阿蔺ALin 阿蔺 A-Lin

能。而且只要加一行配置，以后每次剪藏，AI 自动帮你生成摘要等信息。剪藏只是「搬运」，不是「加工」。一篇 3000 字的文章原封不动躺在 vault 里，跟没存一样。如果剪藏的那一刻，AI 就帮你把要点提好、摘要写好、标签打好呢？今天讲的就是这个：ObsidianWeb Clipper 的解释器功能。它能在你剪藏网页的同时，自动调用 AI 处理内容。剪完就是一篇整理好的笔记，不用再手动加工。全文 3 节，跟着做大概 5 分钟：

1️⃣ 开启解释器 + 配置模型（2 分钟）
======================

2️⃣ 改造你的剪藏模板（2 分钟）
==================

3️⃣ 进阶玩法
========

---

1️⃣ 开启解释器 + 配置模型
================

打开 Web Clipper 设置（点剪藏面板底部的齿轮图标）→ 滚到「解释器」部分。打开解释器把「启用解释器」开关打开。「自动运行」先别开。配置没跑通之前开了它，每次打开剪藏面板都会自动请求 AI，Key 填错或者模型没配对就会反复报错，白耗额度。等下面全部验证通过再回来开就行。

![](.evernote-content/BAF70ECD-4C07-4911-9862-776A8ED18F9C/A29339D6-2A55-44F2-9ACA-BAF4C1ACCE88.jpg)

拿到 API Key如果已经有 OpenRouter 的 Key 了或者自己的大模型，可以直接跳到下一步。

![](.evernote-content/BAF70ECD-4C07-4911-9862-776A8ED18F9C/6CA7E689-AE1C-4E94-8877-7F294E668325.jpg)

⚠️ Key 只显示一次，复制好存安全的地方。添加提供商回到 Web Clipper 解释器设置页面，往下滚到「提供商」，点「+ 添加提供商」：名称：OpenRouter（我用的是 OpenRouter，你用别的服务商按实际情况选）API Key：粘贴刚才复制的 Key

![](.evernote-content/BAF70ECD-4C07-4911-9862-776A8ED18F9C/A533DF36-82DF-4846-A501-BC71BDA886F3.jpg)

添加模型点「+ 添加模型」：

模型显示名称：Ring（随便起，方便识别）

模型 ID：去 OpenRouter 的 Models 页面搜你喜欢的模型，复制模型 ID（下面第一个图）

提供商：选刚才添加的 OpenRouter

![](.evernote-content/BAF70ECD-4C07-4911-9862-776A8ED18F9C/770D6952-3B77-4900-9F2D-62ED4876924A.jpg)

填完保存。搞定，解释器配好了。下一步才是重点，改模板。

![](.evernote-content/BAF70ECD-4C07-4911-9862-776A8ED18F9C/6A6E6E91-8195-4478-B856-66A6B971CE87.jpg)

---

2️⃣ 改造你的剪藏模板
============

你之前已经有一个剪藏模板了（跟着上一篇教程配的那个）。现在要做的就是往里面加 AI 指令。回到 Web Clipper 设置 → 找到你的模板 → 进入编辑页面。你会看到两个关键区域：属性和笔记内容。这两个地方都能写 AI 指令。语法很简单：双大括号 + 双引号包裹自然语言，就这样。下面先演示最简单的一招，跑通之后再告诉你进阶玩法。实操：属性区加一句话摘要在属性区域点「+ 添加属性」，加一行：

字段名：summary

值：{{"用一句中文总结这个页面的核心内容"}}

其他属性（type、status、url、created）都不用动。

![](.evernote-content/BAF70ECD-4C07-4911-9862-776A8ED18F9C/0D568A0D-7685-43D9-8B8A-C1A62E2F7BDC.jpg)

保存模板。然后随便打开一篇文章，点浏览器右上角的 Web Clipper 图标：

你会看到 summary 那行还是原始的指令。点一下面板上的「解释」按钮，Ring 开始处理。

几秒之后，摘要自动填好了：

确认没问题，点「添加到 Obsidian」保存。打开 vault 看一眼，笔记的 frontmatter 里已经多了一行 AI 生成的摘要。就这么简单。一行配置，每次剪藏自动生成摘要。💡 验证没问题了，现在可以回到解释器设置把「自动运行」打开。以后打开 Web Clipper 就自动跑 AI，不用每次手动点「解释」了。

---

3️⃣ 进阶玩法
========

跑通了摘要之后，解释器还能干更多。同一个模板里可以塞多个指令，剪藏时全部自动执行。几个方向供你探索：

自动打标签：让 AI 从你预设的标签列表里选最相关的几个

提取要点：AI 帮你把长文浓缩成 3-5 句话，放在原文上面

列行动项：文章里藏着的可执行动作，让 AI 帮你挑出来

组合技：以上全塞进一个模板，剪藏时一次全跑完

玩法就是改模板里的指令，语法都一样。自己试试，改坏了也不影响已有笔记。搞定，回顾一下今天做了两件事：① 开启了 Web Clipper 的解释器，接上了 Ring 模型 ② 在模板里加了一行 AI 指令，跑通了自动摘要以后每次剪藏网页，AI 自动帮你加工。 不用再手动提炼、不用再回头补标签。想要更多能力，往模板里加指令就行。

---

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI4OTkyODUzOA==&mid=2247484053&idx=1&sn=e71da294510b243fc48377e292a5af17&chksm=ed883ac14d2804e4c59e4843264c1499b3c0d59e36c9c26e8fa7358ea3613ac0e00feefa7ef2&scene=90&xtrack=1&req_id=1779029786693150&sessionid=1779028622&subscene=93&clicktime=1779030185&enterid=1779030185&flutter_pos=91&biz_enter_id=4&ranksessionid=1779029786&jumppath=WAWebViewController_1779030161363,WAWebViewController_1779030161850,20020_1779030176224,1104_1779030177170&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=1800492a&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0Sx1/NZs7gYQHUC/2MZ0yxLTAQIE97dBBAEAAAAAALJ7FWFo+nEAAAAOpnltbLcz9gKNyK89dVj0/E5Bp4WZQXjbqQZ45OOeZqyFJVPaWL9Rde0ueYOaCR6GVFU5Sm/6RJqeyVqtqDFKIVQ3vGdOqCdkxKuqKqvBdcPSob1B9KI0wZXglHHG996xozHfzVV5r4Ac7G7Mpu2UXlK2H7HxcC0PoEFvjqtbzgLggzS6k0/SGh0w8mOS2MaK3gPlE3DbupEcBRDBjoL+voR2rSSn5GVtPDCm27JR/RC70udJTV8tMuq5F2E=&pass_ticket=jiXvJJDTeWTEL/XVQGk2WLf/RX6ebYGQCSmuE1MQES1Qhb47b0a2+bV0kvYikAPX&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/fe505b28-53b6-44b8-8843-cddfcb75b455/fe505b28-53b6-44b8-8843-cddfcb75b455/)