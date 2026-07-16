---
title: "夯爆了！这个开源神器把任意书籍转成 Skill，轻松打造专业的随身顾问"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/夯爆了！这个开源神器把任意书籍转成 Skill，轻松打造专业的随身顾问.md
tags: [evernote, impression]
---

---
title: "夯爆了！这个开源神器把任意书籍转成 Skill，轻松打造专业的随身顾问"
source: evernote
type: note
export_date: 2026-06-23
guid: 4681540d-d916-4c10-927e-4fcb41cc082b
---

# 夯爆了！这个开源神器把任意书籍转成 Skill，轻松打造专业的随身顾问

原文链接: [https://mp.weixin.qq.com/s?chksm=fc794137cb0ec821c431c905c4103b0...](https://mp.weixin.qq.com/s?chksm=fc794137cb0ec821c431c905c4103b0cb05a96cfd6a806ecd4a65a426bb121f8075b1f5b7c85&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782029952_1&req_id=1782029952718987&scene=169&mid=2247543961&sn=e2238985b9346c2b8529f2f292259431&idx=1&__biz=MzU2MTI4MjI0MQ==&sessionid=1782029952&subscene=200&clicktime=1782031824&enterid=1782031824&flutter_pos=12&biz_enter_id=5&jumppath=WAWebViewController_1782031796096,WAWebViewController_1782031796625,20020_1782031812007,1104_1782031821120&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/DMbh11HSxirw3gxj3EcuRLTAQIE97dBBAEAAAAAAIdeC2F7ppEAAAAOpnltbLcz9gKNyK89dVj0taESgcs9A3HYgq6I4/l75vUDB60ef50E4VyTopnejS/Knh+E9G/+36c1ukUNJ9ENfAD/DG5W3KslSlBX9yuvu9EBngG1VjxlylcZ6bgBe+jOoQ/n0Chj1RcepeQF9C7i3lvZmxdG5QoeZQMoQosjjhLWiYUMEVsRIOKLfLZpYgs3BjJiC6v+HgJD/cUDeNoQmWQVb2QmB6zHrewHWkcLolNO3sT3egSjbGRDIeM=&pass_ticket=JHKT4hHUkCWFYe7EZExkEUc3xmW3umQ6+VuG6glKB/npRp+XWmEld61pAPLgGhBY&wx_header=3)

# 夯爆了！这个开源神器把任意书籍转成 Skill，轻松打造专业的随身顾问

Original丛林 极客之家

 

*字数 2591，阅读大约需 13 分钟*

我硬盘里躺着大概四五十本技术书PDF，买的时候雄心壮志，三个月后连第七章讲什么都说不上来，极大的浪费。

有个开源项目 **book-to-skill**，GitHub 5.3k star。它干了一件事：**把技术书PDF丢进去，吐出来一个结构化的 Claude Code Skill。** 写代码时打 `/your-book-slug replication`，Claude Code 从书里找出对应章节回答你。

# book-to-skill到底干了什么

它不是一个PDF阅读器，也不是一个笔记工具。它是一个编译管线：把一本书（或一堆文档）吃进去，吐出来一个完整的 Agent Skill。

![](attachments/df55ac80d2e38997.png)

book-to-skill 把技术书、文档文件夹，甚至一堆资料，转换成 Claude Code 的 Skill。生成后放在 `~/.claude/skills/<slug>/` 下面，里面不只是全文摘录，而是拆成 `SKILL.md`、章节摘要、术语表、patterns、cheatsheet 这些文件，用到哪章，加载哪章。

book-to-skill 跑完之后，我们的 skills 目录里会多出这些东西：

- • **SKILL.md**：核心心智模型 + 章节索引，约4000 token
- • **chapters/**：每章一个文件，每个约800-1200 token，按需加载
- • **glossary.md**：所有关键术语，按字母排好，标了章节出处
- • **patterns.md**：书里所有的技术模式、算法、设计模式
- • **cheatsheet.md**：决策表和速查规则

这套结构的精妙之处在哪？章节文件是按需加载的，你不问第五章，第五章的文件就躺在硬盘上不占token。只有你 `/book-slug ch05` 的时候，Claude Code 才去读那一个文件。

对比一下常规操作：把一本400页的PDF直接扔进Claude上下文窗口，200K token一次性烧完，每个问题、每一轮对话都重复烧。book-to-skill 只在第一次处理时烧token，之后每次查询只加载4K核心 + 1K目标章节。

# 功能详情

![](attachments/a18af6ff16acdb99.png)

book-to-skill功能总览

### 1. 支持绝大部分格式

PDF、EPUB、DOCX、TXT、Markdown、reStructuredText、AsciiDoc、HTML、RTF、MOBI/AZW/AZW3。

我在自己机器上试了，一本PDF格式的《Designing Data-Intensive Applications》，一本EPUB格式的《Clean Code》，都跑通了。纯文本格式（txt、md、rst）不需要额外依赖，PDF和EPUB需要装对应的提取工具。

### 2. 智能选提取器，不傻跑

这是我觉得做得最聪明的地方。book-to-skill 处理PDF之前会先问：这本书是技术书还是纯文本？

![](attachments/d6eee789800e7df7.png)

技术书（有代码、表格、公式）走 Docling 这条线，约1.5秒一页，但能保留markdown表格和代码块。

纯文本走 pdftotext，秒出。pdftotext 没装？自动fallback到 PyPDF2，再不行用 pdfminer.six。

我在一台Mac上跑了一本103页的技术书做基准测试，结果长这样：

| 方法 | 时间 | Token数 | 表格 | 代码块 |
| --- | --- | --- | --- | --- |
| pdftotext | 0.1s | 27K | 0 | 0 |
| Docling | 164s | 27K (+1.2%) | 48 | 36 |

Docling慢很多，但表格和代码块全保住了。pdftotext快但丢掉了所有结构化内容，选哪个取决于你的书长什么样。

这个"先问再跑"的设计比那些无脑一个方案走到底的工具聪明多了。

### 3. 输出不是摘要，是结构

book-to-skill 不在那给你总结"这本书讲了分布式系统的设计原则"这种废话。它提取的是作者花几年时间搭建的框架：命名的模式、精确的表述、反模式清单。

作者定了七条质量原则，我挑几条最说明问题的：

- • **密度优先于完整**：一份1000 token的摘要比一份10000 token的摘录强
- • **实践者口吻**：输出是"用X当Y"，不是"本书解释了X"
- • **永远不复制原文**：始终合成、总结、从源头提取信号

翻译成人话：book-to-skill 产出的东西像你认真读过这本书之后做的笔记，不是把书拆碎了重新排列。

![](attachments/e7805901495fe657.png)

架构图

### 4. 用途不止是书

名字叫 book-to-skill，但输入可以是任何结构化文字。把整个 `docs/` 文件夹揉成一个skill，写代码的时候直接问，你的架构决策记录、运维手册、新人指南就从一个"偶尔翻翻"的文件夹变成了你工作流里随时能调用的东西。

品牌书也能转，视觉规范、文案语调、组件原则变成一个团队共享的skill，比翻60页PDF快多了。论文集群加自己的笔记合并成一个skill，新论文来了还能往里加。RFC、API合约、合规文档这些你反复引用但永远记不住的东西，同样适合。

*只要你反复打开同一个文档、每次都想"要是记住就好了"，这东西就适合做成skill。*

### 5. 增量更新，不是一次性

![](attachments/8b475e3068c5b4fa.png)

生成的skill不是死的。你买了新版的PDF、读了一篇新论文、写了新笔记，可以直接fold进去：

/book-to-skill ~/articles/new-paper.pdf ~/.claude/skills/project-knowledge

指向已有的skill目录，它会识别出来，把新内容合并进去。这个设计让skill变成了一个活的、随时间增长的知识库，而不是一次性快照。

# 工作流程：一次编译，到处查询

book-to-skill 的管线分成10步，我把它简化成几个关键阶段说清楚：

**提取阶段**：你敲 `/book-to-skill your-book.pdf`，它先问你技术书还是纯文本，然后选提取器。PDF用Docling/pdftotext，EPUB用ebooklib，DOCX用python-docx，以此类推。提取出来的纯文本写到一个临时文件里，同时生成metadata。

**分析阶段**：Claude读这个文本，识别书名、作者、章节结构、核心主题。如果章节标题是标准格式（"Chapter N" / "第N章"），自动分段。如果不是，也能处理，只是章节索引需要手动指定。

**生成阶段**：这步是核心。它对每一章做深度分析，生成800-1200 token的章节摘要，包括代码示例和参考表格（技术书的话）。同时生成glossary（所有术语）、patterns（设计模式/算法）、cheatsheet（速查表）。最后生成一个约4000 token的SKILL.md主文件，里面是核心心智模型加上章节索引。

**交付阶段**：整个skill写到你Agent的skills目录。Claude Code是 `~/.claude/skills/<slug>/`，Copilot CLI是 `~/.copilot/skills/<slug>/`，Amp和跨Agent的在 `~/.agents/skills/<slug>/`，临时文件清理掉。

![](attachments/d16e40ed0d777b2a.png)

贴一组真实数据，作者跑了几本书的转换，用的是Claude Sonnet 4.5：

| 书 | 格式 | 页数 | Token | 章节 | 约花费 |
| --- | --- | --- | --- | --- | --- |
| Think Python 2 | PDF | 244 | 119K | 19 | $0.88 |
| Working Backwards | PDF | 371 | 175K | 10 | $0.96 |
| Pro Git | PDF | 501 | 229K | 自动检测失败 | $1.23 |
| Moby-Dick | EPUB | 未知 | 301K | 自动检测失败 | $1.42 |

一本技术书转换成本大概5-10块钱，一次性的，之后每次调用只花极少的token。

# 跟RAG和直接灌PDF比，这种东西到底好在哪

这个问题作者在FAQ里回答的很明白，我直接引他的逻辑：

**跟直接灌PDF比**：你把一本400页的PDF扔进Claude上下文，约200K token。每个问题、每一轮对话，这200K都要重复处理。book-to-skill处理一次花5元左右，之后每次查询只加载5K。一个500页的Pro Git，token占用差51倍。

而且LLM在接近满的上下文里检索具体事实会丢精度，这个现象叫"`lost in the middle`"。1K精炼过的章节 vs 200K原始文本，哪个回答更准，不需要测试也能猜出来。

**跟RAG比**：RAG在查询时工作：切块、嵌入、找相似向量、塞进prompt。它擅长"找到提到X的那一段"。

![](attachments/6ed3c002ac9efe3a.png)

book-to-skill在编译时工作：一次深度分析提取作者的框架、命名、使用条件、反模式。它回答的是"这个作者构建的12个框架是什么，什么时候用哪个"。

选哪个取决于场景：几十本书、浅层搜索，RAG合适。一两本书、深度应用，skill合适。它们是互补关系。

作者还做了一个 "`Discovery Loop Tax`" 的基准测试，测量回答一个具体问题token被烧了多少。直接灌PDF（`Context-dump`）和Agent自己翻PDF（`Discovery loop`） vs book-to-skill：

![](attachments/0b53029221182823.png)

Discovery Loop Tax对比

三本书的测试结果很一致：book-to-skill 比直接灌PDF省24到51倍token，比Agent自己翻书省2.4到15.6倍，章节越大，优势越明显。

# 安装和使用

安装不需要pip，不需要npm，直接git clone。我用Claude Code：

git clone https://github.com/virgiliojr94/book-to-skill.git ~/.claude/skills/book-to-skill

或者更简单，直接在Claude Code会话里敲：

Install book-to-skill: https://raw.githubusercontent.com/virgiliojr94/book-to-skill/master/SKILL.md

GitHub Copilot CLI用户：

git clone https://github.com/virgiliojr94/book-to-skill.git ~/.copilot/skills/book-to-skill
# 然后在copilot会话里：
/skills reload
/skills info book-to-skill

依赖方面，它不强制装任何东西。跑之前可以用 `python3 scripts/extract.py --check` 看哪些提取器已装好、哪些需要补。纯文本格式零依赖。PDF需要pdftotext或docling，EPUB需要ebooklib。缺什么它会告诉你具体装哪个命令。

使用更简单：

# 处理一本书，slug自动从文件名生成
/book-to-skill ~/Downloads/designing-data-intensive-applications.pdf
# 指定slug
/book-to-skill ~/books/clean-code.epub clean-code
# 把多个文件揉成一个skill
/book-to-skill ~/papers/paper1.pdf ~/notes/export.txt unified-research
# 整个文件夹一起处理
/book-to-skill ~/workspace/project-docs/ project-knowledge
# 增量更新已有skill
/book-to-skill ~/articles/new-paper.pdf ~/.claude/skills/project-knowledge

处理完之后直接用：

/designing-data-intensive-apps                    # 加载核心心智模型
/designing-data-intensive-apps replication        # 查具体主题
/designing-data-intensive-apps ch05               # 深入第五章
/designing-data-intensive-apps "what chapters do you have?"

Copilot CLI用户注意：创建完skill后要跑 `/skills reload` 刷新一下。Claude Code和Amp下次启动自动识别。

一些实际限制需要讲清楚：

*章节自动检测依赖标准格式（"Chapter N" / "Capítulo N"），如果你的书用罗马数字或者纯标题分段，自动检测会失败。书还是能处理，但你需要自己手动指定章节。Pro Git和Moby-Dick就是这种情况，都转换成功了，只是章节索引需要手动操作。*

# 写在最后

book-to-skill 解决的是一个真实问题：技术知识读了用不上。它不搞花活，不卖概念，就是把一本书编译成一个Agent Skill，然后你写代码的时候随时能问。

我装了一个礼拜，把一本技术书和两份使用手册都转成了skill。每次在Claude Code里敲 `/ddia ch05` 的时候，确实觉得这东西补齐了"读书"和"用书"之间那个缺口。

大家有这方面的需求的话，也可以研究一下这个开源项目。

GitHub地址：

*https://github.com/virgiliojr94/book-to-skill*


---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=fc794137cb0ec821c431c905c4103b0cb05a96cfd6a806ecd4a65a426bb121f8075b1f5b7c85&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1782029952_1&req_id=1782029952718987&scene=169&mid=2247543961&sn=e2238985b9346c2b8529f2f292259431&idx=1&__biz=MzU2MTI4MjI0MQ==&sessionid=1782029952&subscene=200&clicktime=1782031824&enterid=1782031824&flutter_pos=12&biz_enter_id=5&jumppath=WAWebViewController_1782031796096,WAWebViewController_1782031796625,20020_1782031812007,1104_1782031821120&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b28&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ/DMbh11HSxirw3gxj3EcuRLTAQIE97dBBAEAAAAAAIdeC2F7ppEAAAAOpnltbLcz9gKNyK89dVj0taESgcs9A3HYgq6I4/l75vUDB60ef50E4VyTopnejS/Knh+E9G/+36c1ukUNJ9ENfAD/DG5W3KslSlBX9yuvu9EBngG1VjxlylcZ6bgBe+jOoQ/n0Chj1RcepeQF9C7i3lvZmxdG5QoeZQMoQosjjhLWiYUMEVsRIOKLfLZpYgs3BjJiC6v+HgJD/cUDeNoQmWQVb2QmB6zHrewHWkcLolNO3sT3egSjbGRDIeM=&pass_ticket=JHKT4hHUkCWFYe7EZExkEUc3xmW3umQ6+VuG6glKB/npRp+XWmEld61pAPLgGhBY&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/4681540d-d916-4c10-927e-4fcb41cc082b/4681540d-d916-4c10-927e-4fcb41cc082b/)
