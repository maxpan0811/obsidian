# Qwen3.6-Plus实测：能力像Claude，价格像拼多多

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIwMTU5OTQ1Nw==&mid=265372...](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726261&idx=1&sn=d8e841805b2b9d9697ef143bcaa56481&chksm=8caff92a50300fca50d01d48af27036c4bb13a4bad41a818d8fa36aafc790e05fede766af099&scene=90&xtrack=1&req_id=1775310094334408&sessionid=1775305459&subscene=93&clicktime=1775310159&enterid=1775310159&flutter_pos=30&biz_enter_id=4&ranksessionid=1775310094&jumppath=20020_1775310083831,1104_1775310085314,20020_1775310093873,1104_1775310127980&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004630&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQhrEMrobHlQPJ0ckUOvRELBLTAQIE97dBBAEAAAAAAP5OEI1VznwAAAAOpnltbLcz9gKNyK89dVj0KjBonxfqKkRHnp89dNaz3enEaXQXGOTQVd+2vzekSfWYB9uvAFlG9T66xWnzn0aPVP+Kc/r0wzyYQTcJJfHf6chgYvlCjfNDUTaby5lkTMnWL9Qx/DXGx2EuB04mJVn/J3eSAPmMfq8euC7TPzNMTWvhthezQCjquOREELF6pJTcED7fS1jWFoaD80KOMT6XdmdwdCBAnmIu6M/umJQuqT9Lwfk49xkSgwKog8Q=&pass_ticket=PHg29m7acN1SVoFG2M6c7tad2UQsSQMCc3Rwi4z2zhGnIdBJx9RznxPLDh6DHAI+&wx_header=3)

Original冷逸沃垠AI

大家好，我是冷逸。

最近阿里千问的节奏，已经不能用“高强度更新”来形容了，更像是“腹泻式发布”。

想问下阿里的小伙伴，你们是不是把整个Qwen团队都蒸馏成了同事.skill啊，不然怎么做到一天发一个模型的？![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/8F294FD6-5ADE-4140-9BCC-90847D8EA8F7.png)

你看这节奏：

* 3月30日，发布全模态模型Qwen3.5-Omni，直接拿下215项SOTA；
* 4月1日，发布图像模型Wan2.7-Image，据我身边不少朋友实测，超长文字渲染能力离谱地强；
* 4月2日，发布基座大模型Qwen3.6-Plus，比3.5又拉开了一截；
* 4月3日，又掏出Wan2.7-Video，一句话就能P视频。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/0D309F4C-38E0-45B3-828E-A6CF05B420CA.jpg)

真的，如果我有5个冷逸.skill，我一定把这些模型全都测一遍。

可惜，目前我还没完成自我炼化，只有一个真人冷逸。所以今天，我们重点测一下Qwen3.6-Plus。

先快速认识一下这个模型：

* 100万上下文窗口
* 重点强化Agentic Coding
* 原生多模态（支持文本/图片/视频输入）
* 原生联网+Function Calling，可调用外部工具，适配龙虾
* API价格：输入¥2/百万tokens，输出¥12/百万tokens，不到Claude的1/18
* 兼容OpenAI和Anthropic协议，Claude Code、Codex和OpenClaw都能用

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/42DE008E-4C63-45F4-9B5C-594847E1C483.jpg)

顺带一提，这张信息图，也是Qwen3.6-Plus直接生成的。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/1F2B9D33-248C-456D-AE6E-D9D2F2A65F49.jpg)

一手实测

这次，我主要测了3大场景6个Case，交叉使用Claude Code、OpenClaw、cherry studio、chat.qwen.ai来综合评估这个模型。

1）视觉编程

先来个简单的。

我给了Qwen3.6-Plus一张学生书包图片，让它生成商品网页。

Prompt：请为这款学生书包设计一个精致的图文发布网页，目标人群是6-15岁的中小学生。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/594265E2-7EE8-4F03-8110-98C18DAC7FD4.png)

出来的页面还挺像那么回事。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/4CC7B7C0-C929-46F4-A1D2-7B83DFED3E15.jpg)

整体主色调是奶油白 + 暖灰，和书包本身的米白色呼应。视觉风格是典型的日系极简风（Minimalist & Clean）。

既保留了学生用品的亲和力，又不会显得廉价。

能看出，这个模型对视觉内容的理解还是比较在线的。

于是我决定给它加点难度。我喂了一整个文件夹模特照片，让它生成一个摄影师作品网站。

Prompt：我是拍模特广告的摄影师，我的工作室叫「小逸摄影」，文件夹 D:\Vibe Coding\Qwen3.6-plus\模特图片 放了一些模特图片，给我生成一个高级审美、大师水准的摄影师作品网站，用上文件夹里的图片并配上精美的讲解。

成品出来的时候，我第一反应是：有点惊艳。

整体是深色主题+金色点缀+优雅字体，整个气质看起来像那种电影节摄影展网站。

而且细节也没偷懒：

* 点击图片灯箱放大
* 页面滚动渐显动画
* 响应式设计（手机/平板自适应）

但真正让我意外的，是它的文案能力，我挑几张给大家看下。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/1265D40E-9D48-4BE6-9D6B-B06A66B1AC72.png)![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/4CC7D6DF-AFAB-4702-979D-585FF4BFE1F2.png)![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/BA5006EA-30DD-4232-B356-AFA1F66BB0EB.png)

真的，这种一看就很高级，很舒服。

很多模型做网页有个通病：「UI很好看，但文案像实习生写的。」

但Qwen3.6-Plus这次，从Logo到Slogan，以及小字解释，它写的文案，我几乎挑不出什么毛病。

Vibe Coding真正进入生产场景，多模态能力是刚需。目前全球既擅长Coding又具备视觉理解能力的模型，其实没几家。

从我的实测来看，Qwen3.6-Plus在视觉编程这一块，是合格的。

2）视觉理解&推理

接着，我测了一个稍微变态一点的题。

一张成都地铁线路图。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/E2B1578F-487E-4A8B-AE73-8B0340E177B1.png)

问题是：我在二仙桥，如果7号线瘫痪，我去火车南站一共有多少条路线？最少的换乘路线是哪条？

这题其实挺难的，模型思考了128秒才回答我。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/9BEB0158-6704-4F6F-89E6-5DDA669CD647.png)

我原本以为它会翻车，结果却答对了。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/13387477-43F3-4CA9-832D-B1E772CBA804.png)

接着我又测了一道题，把Qwen3.6-Plus的视觉benchmark表现发过去，问它Qwen3.6究竟强在哪里。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/0C02A4A7-D313-4ADE-AE81-21F0285FE99D.png)

答案：

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/ADAA471C-0F4B-4965-B6A7-9D32F662CA3D.png)

现在，再回过头来看这张benchmark，一下子就懂了。

这说明什么？

说明这个模型已经不只是看图识物、OCR文字识别，而是能结合视觉理解、路径推理、信息定位，来完成复杂任务。

当模型不再停留在“看懂图片”，而是开始图表解析、UI理解、文档理解、细粒度定位……那它就已经不是一个“视觉模型”，而是开始向多模态智能体进化。

而Qwen3.6-Plus，正是阿里发布的第二款原生多模态基座模型。

3）Agentic任务

最后，我重点测了一件事情：Agentic能力+长程任务。

第一个case，是我前几天给大家介绍过的自动写公众号神器。

我的需求是：

```
给我做一个“沃垠AI写作神器”的全功能网站，直接打开html主页就能运行。  
  
功能要求：  
1、有三个核心功能：正文生成、标题摘要生成（先生成正文后，再根据正文来生成标题和摘要）、封面生成。正文、标题摘要接同一个模型，图片接另外一个模型。  
2、主界面有一个输入会话框，给到示例模板“帮我写一篇公众号文章，主题是xx，字数xx，内容要点有：1.xx，2.xx……”，用户输入内容主题和写作要求后，开始调用大模型进行写作。  
3、输入会话框设计有“联网”功能，支持用户手动打开和关闭联网功能。  
4、输入会话框还设计有风格1、风格2等可选的写作风格模板。目前只有一个“风格1：科技媒体评论”，风格控制Prompt见本地文件“风格1：科技媒体评论.txt”。  
5、写作和生图均支持用户自行调用大模型。调用接口设计成可视化窗口，用户只需要输入模型url、模型key和模型名字，就可以使用。  
5、先写正文，写完正文后，再批量出一批标题和摘要，供用户选择。  
6、最后，再根据本文的核心内容提炼2-3个关键内容点，并生成封面图片的文生图prompt，统一尺寸比例2.35:1，用户选定某个prompt后，调用生图模型一键生成封面图片。  
7、正文和标题摘要，都设计有复制按钮，支持用户一键复制文本。封面图片，设计有下载按钮，支持用户下载到本地。
```

新版「沃垠AI写作神器」，不需要做本地配置，直接打开HTML，然后接入API就能用。

它可以自由加载你训练的写作风格（结构化的提示词），只需要点“写作风格”旁的+号，它会自动解析文件内容（文件名统一为“风格xxx.txt”），并添加到下拉列表。后面，我们只需要点一下就能使用。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/AEC34E91-342E-4C50-B250-1959400E737D.png)

需要新版本的朋友，直接后台回复【写作】，就能领走这个HTML。

这次开发，我只迭代了5个版本，整个过程半小时搞定，直接交付2000+行可运行代码。

比我上次的开发效率，至少提升了两倍。

接着，我又用搜索+office+skills任务测了一轮Qwen3.6-Plus。

需求是，联网调研张雪机车的发展轨迹，生成5000字Word报告，然后调用skills把报告做成知识网站。

Prompt：联网搜索、调研张雪机车的发展轨迹，尽量从权威信源获取信息。首先，给我创建一份5000字的word调研报告。然后，调用Knowledge Site Creator Skills给这份报告创建一个知识学习网站，页面高级审美。

期间，模型调用了web search、python-docx、Claude skills等工具。我数了一下，工具调用超过50次。

先看word报告。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/16F7CB2E-A8DC-43FF-B896-BFC440BB0D05.gif)

信息完整度还是不错的。老实说，我一直想系统了解张雪机车，这份报告对我来说挺有价值。

然后再看它生成的知识网站。

我第一眼看到的时候，直接一句「卧槽」。

这UI和内容质量，都比我预期高很多。

整体跑下来，我的结论很简单：Qwen3.6-Plus的Agentic能力，明显被低估了。

当一个模型同时拥有：

* 100万上下文
* 原生多模态
* 强工具调用能力

那它在Agentic Coding和Agentic Work领域，都是非常有想象空间的。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/A82BC17D-FEAC-49EB-A618-420AF2C82894.jpg)

写在最后

整体体验下来，我觉得Qwen3.6-Plus在文本推理、视觉理解、代码能力、长程任务和Agentic能力上都还挺强的。

难怪它能够在多个benchmark上拉开Qwen3.5一大截。

![](.evernote-content/D7C6333B-6AB6-44FE-A243-8965C25595E9/B5297D32-2875-4A90-BEFC-5BB327B2CAAB.png)

而这个价格却不到Claude的1/18。

这就有点像什么？

就好像一个演员，明明是小李子的演技，却拿着李洪绸的片酬，然后天天坐在片场看隔壁李现的表演。

更离谱的是，这个李洪绸，还时不时把自己的作品免费上传B站。

这对吗？

说实话，我不知道。

但我在他们官方文章里看到一句话：在未来不久，我们还将开源更小规模的模型版本，以此重申我们对技术普惠与社区驱动创新的坚定承诺。

看完后，我就觉得：源神牛逼。

修改于

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726261&idx=1&sn=d8e841805b2b9d9697ef143bcaa56481&chksm=8caff92a50300fca50d01d48af27036c4bb13a4bad41a818d8fa36aafc790e05fede766af099&scene=90&xtrack=1&req_id=1775310094334408&sessionid=1775305459&subscene=93&clicktime=1775310159&enterid=1775310159&flutter_pos=30&biz_enter_id=4&ranksessionid=1775310094&jumppath=20020_1775310083831,1104_1775310085314,20020_1775310093873,1104_1775310127980&jumppathdepth=4&ascene=56&devicetype=iOS26.4&version=18004630&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQhrEMrobHlQPJ0ckUOvRELBLTAQIE97dBBAEAAAAAAP5OEI1VznwAAAAOpnltbLcz9gKNyK89dVj0KjBonxfqKkRHnp89dNaz3enEaXQXGOTQVd+2vzekSfWYB9uvAFlG9T66xWnzn0aPVP+Kc/r0wzyYQTcJJfHf6chgYvlCjfNDUTaby5lkTMnWL9Qx/DXGx2EuB04mJVn/J3eSAPmMfq8euC7TPzNMTWvhthezQCjquOREELF6pJTcED7fS1jWFoaD80KOMT6XdmdwdCBAnmIu6M/umJQuqT9Lwfk49xkSgwKog8Q=&pass_ticket=PHg29m7acN1SVoFG2M6c7tad2UQsSQMCc3Rwi4z2zhGnIdBJx9RznxPLDh6DHAI+&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/02eddcc3-8f3b-4ae6-af7c-cfdb2d61838f/02eddcc3-8f3b-4ae6-af7c-cfdb2d61838f/)