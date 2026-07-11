# 终于，Claude Code 封号的原因被曝光了！竟然针对中国用户，植入隐形代码？！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI1NDczNTAwMA==&mid=224758...](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588292&idx=1&sn=00a748cb79f2cb762927cb3597c32ce2&chksm=e80e0be5eabd468f5a96ff5881fbccab93506603953e42bd629796907866acafb15fd3e63abe&scene=90&xtrack=1&req_id=1782892801708098&sessionid=1782892858&subscene=93&clicktime=1782893632&enterid=1782893632&flutter_pos=1&biz_enter_id=4&ranksessionid=1782892801&jumppath=1001_1782892830299,1104_1782892859106,20020_1782892864160,1104_1782893629810&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0bvDwjRjqPT2d2lT8PqW7xLTAQIE97dBBAEAAAAAAIrgMLCw7TAAAAAOpnltbLcz9gKNyK89dVj0bA6NYKUFNuFJ9lytHZ+TdyxlyWabW27dZycK1FbP7Ebo/ys1/QyLStyf5MgocCTqYMAimGRuLosHAo5GhmcBWY7ySbPhXH6RliXUciePwISJnb4Wy9qPFxnj1rFrwwVOXRnTcyb64RCDf2mogoJe6YZjz1vst6xUovGPRG2jYW9YXlC8HAwbDqqVwXFrPj3ivDjjrSZOLJURdVAYuYJsLfVJXJh8Sb07UL+pXz8=&pass_ticket=YS5XSDBi/4ArXMwoIQTmB0tfxNXYl4MJI3DUkhYJVtyn+aRyKRzZCAGZV1poff3g&wx_header=3)

Original程序员鱼皮 程序员鱼皮

大家好，我是程序员鱼皮。

这两天 Claude Code 又炸了，国内开发者被大面积封号，很多人稳定用了一年的号也翻车了，甚至有百人规模的公司被团灭，一众天才程序员就此陨落！

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/2DC16067-FDCC-4A95-926B-906B32BC13F4.png)

众所周知，A ÷ 一直在封禁中国用户，但之前没有人搞清楚，自己明明都跑到美国了，它到底是怎么把自己揪出来的？

直到昨天，国外开发者对 Claude Code 做了逆向工程，直接把 A ÷ 的底裤扒了下来，原来它在客户端里偷偷藏了一套隐蔽的用户标记系统。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/77DBF3B9-6297-4A00-94ED-287BE1645C8C.png)

好家伙，这下全世界的开发者都见识到了 A ÷ 的丑恶嘴脸。

我看完整个技术分析之后，也是被恶心到了。

下面我用傻子都能懂的语言给大家解释一下 Claude Code 封号的手段，建议各位在吃饭的时候别看，我怕你气到吃不下去。

Claude Code 封号原因
----------------

先简单概括一下 Claude Code 的封号思路：Claude Code 会偷偷读取你电脑上的本地信息，然后用一种肉眼完全看不到的方式，悄悄给你发送给 AI 服务器的每一个请求，打上「这个人是中国用户」的隐形标记，传回 Anthropic 的服务器。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/E2C39EB8-98F0-4294-ACEA-B18D04E63477.png)

根据多位独立研究者的验证，这套检测机制有一个触发条件，就是你必须设置了一个叫 `ANTHROPIC_BASE_URL` 的环境变量，把 Claude Code 的请求指向了非官方的 API 地址。换句话说，如果你直接连的是官方的 `api.anthropic.com`，这套标记机制不会激活。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/3875FCDC-C77E-4C83-8184-DD5512C676D3.png)

但问题是，国内大多数用户都需要通过中转站来用 Claude Code，所以很多中国开发者都设置了这个变量，也都会被这套机制检查到。

### 两条识别路径

在这个前提下，Claude Code 通过 2 条路径来判断你是不是中国用户。

**第一条路径，读取你电脑的系统时区。**

只要你的系统时区是 `Asia/Shanghai` 或者 `Asia/Urumqi`，Claude Code 就会把你标记为中国用户。

而绝大多数中国开发者虽然切换了网络，但一般不会去改电脑时区，毕竟还要正常看时间和日历，所以这条路径几乎能命中所有人。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/C123773C-7526-4809-A751-DCDFBC40EEAC.png)

**第二条路径，把你的中转地址跟一份域名黑名单做比对。**

因为国内访问不了 Claude 的官方 API，很多开发者和公司都是通过中转站来调用的。Claude Code 会把你在 `ANTHROPIC_BASE_URL` 里填的地址提取出来，跟一份内置的域名名单做匹配。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/CC134CE7-90D3-49F0-A3A7-DEF0E0AE1CC2.png)

这份名单本身也是被混淆加密存储的，被逆向大佬解码后发现一共有 **147 个域名**。

我看了一下这份名单，真蚌埠住了。

上来就是中国顶级域名 `cn`，直接腰斩。

紧接着就是百度、阿里、字节等国内大厂的域名。（诶，怎么没有腾讯的？）

而且连阿里和百度的内网域名都没放过！很难想象 Anthropic 的 CEO Dario 之前在百度经历了什么。

此外 DeepSeek、智谱等几乎所有国内 AI 公司的域名和关键词也在名单里，剩下的大头就是各种 API 中转服务的域名了。看看你正在用的中转站在里面么？

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/8F415B92-98D5-475D-95FA-0FDF3FACD9B2.png)

### 更离谱的操作

前面讲了 Claude Code 怎么识别中国用户，你可能已经觉得够离谱了，但接下来才是真正让我大开眼界的部分。

Claude Code 识别出你是中国用户之后，是怎么把这个信息传回服务器的呢？

每次你在 Claude Code 里输入提示词，它在把请求发给 Anthropic 服务器之前，都会在最前面拼一段系统提示词。

这段提示词里有一行平平无奇的日期信息，长这样：

Today's date is 2026-06-30.

就是这行看起来人畜无害的文字，Claude Code 会在发送请求之前，对它动两处手脚。

**第一处，改日期分隔符。**

如果检测到你的时区是中国时区，日期格式会从 `2026-06-30` 变成 `2026/06/30`，连字符变斜杠。

**第二处，改单引号的 Unicode 编码。**

根据你中转地址的匹配结果不同，`Today's` 里面那个单引号会被替换成不同的 Unicode 字符，分别代表不同的含义。

* `'`（U+0027，正常 ASCII 单引号）= 没命中任何名单
* `'`（U+2019，右单引号）= 命中了域名列表
* `ʼ`（U+02BC，修饰字母撇号）= 命中了 AI 实验室关键词
* `ʹ`（U+02B9，修饰字母角分符）= 两个都命中了

这四个字符长得一模一样，你在编辑器和终端里根本看不出区别。但在机器层面，它们是完全不同的编码值。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/5395A7C1-9487-497F-B49B-60B210247C2A.png)

这种手法叫做 **隐写术**，就是把秘密信息藏在看起来完全正常的内容里。

就像你写了一封普通的信，但其中某些字母用了不同品牌的墨水，收件人用特殊仪器一扫就能读出暗号，而你拿着信怎么看都觉得一切正常。

Anthropic 的服务器收到请求后，只需要检查一下那个单引号是哪个 Unicode 字符、日期用的是连字符还是斜杠，立刻就能判定这条请求来自中国用户、是否通过中转站、是否和国内 AI 公司有关。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/FD86D0F2-2EA1-46F1-91C3-3EA3E26E4A6C.jpg)

而且整个过程不需要额外的网络请求，不会留下任何可疑的流量痕迹，因为这些修改后的字符在显示层面和正常字符一模一样。

这也是为什么这事一直没人发现，直到有人对 Claude Code 的程序文件做了逆向工程。

可能有人会问：A ÷ 直接封掉所有用中转站的用户不就完了，为什么要搞这么复杂？

因为很多海外的企业和开发者也会因为安全合规等原因使用自定义 API 网关，如果一刀切全封就会误伤大量正常用户。所以 A ÷ 选择了一种更「聪明」的方式：先静默标记、持续收集情报，等积累了足够多的数据之后，再在服务端做针对性的封禁决策。

**说白了，就是先暗中观察你，等掌握了足够证据再动手。**

另外提醒一下，如果你真的收到了封号邮件，想申诉解封，打开邮件的时候也要小心！

因为有人发现 Anthropic 的邮件里埋了追踪像素，你一打开邮件它就能获取到你的真实 IP 地址，相当于二次确认你在中国。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/6062A2F0-40DF-4587-976E-4F505CEAC325.jpg)

看到这里，你会发现，Claude Code 为了封你的号，背后做了多大的努力。我倒是真佩服 A ÷ 这股劲儿，怪不得人家能做到这么大呢？

大家怎么看？
------

逆向了 Claude Code 的那位国外开发者老哥，直接怒斥 Anthropic 在 Claude Code 里嵌入了「间谍软件」。

虽然有人认为这不算间谍软件，只是一种反滥用的合规措施；但更多人认为，在用户完全不知情的情况下搞隐蔽标记，就是不对。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/E7FB8043-50C3-414D-8FD9-DE8E698152A7.png)

我觉得吧，Claude Code 不是一个普通的聊天软件，它运行在你的终端里，拥有文件系统权限，能读写你的代码和配置，甚至能执行各种 Shell 命令。开发者把这么大的信任给了它，结果它背着你在每一条请求里偷偷夹带私货，这种事情一旦被发现，大家以后用它的时候心里都会有根刺，总想着它是不是还在背后搞别的什么小动作。

**今天它能上报你的时区，明天就能偷偷上报你所有的数据。**

而且 Anthropic 自己在安全政策文档里一直标榜「透明」和「可信」，结果自家产品里用隐写术藏标记，被外界觉得「双标」也是很正常的。

另外还有一个很现实的问题，这套机制对真正搞大规模转售和模型蒸馏的人来说，想绕过并不难，改个时区、换个域名就完事了。最终被精准打击的，反而是那些正常付费使用的普通开发者。

总之就是，想正常用上 Claude，现在是越来越难了，很多人的时间和金钱，全浪费在对抗 A ÷ 上了。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/EACD2D8A-81B1-4354-86C2-182131F87549.jpg)

我们面临的 AI 困境
-----------

最近这段时间，我作为一名 AI 编程博主，明显感受到了 AI 困境和 Tokens 焦虑。

除了 Claude Code 封号之外，OpenAI 的 Codex 在 6 月也连搞了两波封禁，200 刀的账号没有任何预警直接封停。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/8AA101C3-F7D1-4153-A1A7-E5FE50402291.png)

Cursor 也是一直存在地区限制，有不少人反映更新到 3.9 版本后无法使用模型了。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/8602281D-ED19-460D-BC85-660C95F5E82D.png)

再看国内这边，DeepSeek V4 正式版即将引入峰谷定价，高峰时段 API 价格直接翻倍。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/8343E7C4-647F-4DBE-8EEC-E5EDD6C579F6.png)

智谱的 GLM Coding Plan 因为算力紧张搞了限量发售，天天盯着都抢不到。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/A87E7601-AE56-4A17-9467-644B2ADB74A6.png)

豆包也推出了付费专业版，用最直接、最不绕弯子的方式告诉我，高级版每月 500 元。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/CA515029-1F79-4305-8D8D-EBA81C01BF03.png)

如今 AI 的能力的确是越来越强了，但能稳定用上的门槛也越来越高了。

**以前每次有新模型发布我都很兴奋，现在更多的则是焦虑。**

如果别人能正常用上最强的 AI 模型和工具，你用不上，生产力就会有明显的差距。而且老板可不管你是被封号了还是被限流了，活儿该干还得干。

![](.evernote-content/40282A14-1120-4C67-A3CA-474584514470/80E08FE1-A6CD-4D30-BD4E-F33A175CF7C2.png)

我现在已经不奢求 AI 再有什么突破性进展了，只希望一件事，就是让我正常用，别今天封号、明天涨价、后天限流的。

评论区聊聊，你们怎么看这件事？有人中招了么？

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI1NDczNTAwMA==&mid=2247588292&idx=1&sn=00a748cb79f2cb762927cb3597c32ce2&chksm=e80e0be5eabd468f5a96ff5881fbccab93506603953e42bd629796907866acafb15fd3e63abe&scene=90&xtrack=1&req_id=1782892801708098&sessionid=1782892858&subscene=93&clicktime=1782893632&enterid=1782893632&flutter_pos=1&biz_enter_id=4&ranksessionid=1782892801&jumppath=1001_1782892830299,1104_1782892859106,20020_1782892864160,1104_1782893629810&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0bvDwjRjqPT2d2lT8PqW7xLTAQIE97dBBAEAAAAAAIrgMLCw7TAAAAAOpnltbLcz9gKNyK89dVj0bA6NYKUFNuFJ9lytHZ+TdyxlyWabW27dZycK1FbP7Ebo/ys1/QyLStyf5MgocCTqYMAimGRuLosHAo5GhmcBWY7ySbPhXH6RliXUciePwISJnb4Wy9qPFxnj1rFrwwVOXRnTcyb64RCDf2mogoJe6YZjz1vst6xUovGPRG2jYW9YXlC8HAwbDqqVwXFrPj3ivDjjrSZOLJURdVAYuYJsLfVJXJh8Sb07UL+pXz8=&pass_ticket=YS5XSDBi/4ArXMwoIQTmB0tfxNXYl4MJI3DUkhYJVtyn+aRyKRzZCAGZV1poff3g&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a3d25d9b-d9c9-4782-81f5-72817ba010c2/a3d25d9b-d9c9-4782-81f5-72817ba010c2/)