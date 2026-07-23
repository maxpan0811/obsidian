---
tags: [★★★★★]
---

# 读过的书全忘了？有人做了 AI 驱动的智能书籍知识图谱，重塑阅读体验

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzAxNDIzNzc4MQ==&mid=264939...](https://mp.weixin.qq.com/s?__biz=MzAxNDIzNzc4MQ==&mid=2649399226&idx=1&sn=c7333bd1224760e795bd3d5ed52424d9&chksm=82f1908bc2c6dbd95afe242b9be5696cab81276f9c2bd404efdeebd20fe7c6d705a7a761642b&scene=90&xtrack=1&req_id=1782912544367384&sessionid=1782910875&subscene=93&clicktime=1782915983&enterid=1782915983&flutter_pos=5&biz_enter_id=4&ranksessionid=1782912544&jumppath=WAWebViewController_1782915841363,20020_1782915974550,1122_1782915975414,1104_1782915976998&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQLJUe1vsDUuwgyrmnIiUyDRLTAQIE97dBBAEAAAAAAB++IwqoKBgAAAAOpnltbLcz9gKNyK89dVj0AIQ7KCGLKPY/0dtE8cgebskf8768ksuqeVo2cCoW94r4T25qN40o3+T2W7VLBRwn50ndDArSb3Awmz9FR/QvP95/ICTJH0jteC91R0BAMyS8W0IE0dd71G8YmPUQMEqnvWhL6oRQqrJWYUnYVRy3NzsoHhvcDi1xADxGs/SOzYEui0OY8txYbnd5kKx3kuRYjNd7twcSMz3hTacrw6FkZeNoBwV0VsTL5kkQD/8=&pass_ticket=YyZAuaAs8+GidSZp4zuMgzOG6KJyJl9eHvWv3/3XRerNHN687BW8MMO31gCOVpIg&wx_header=3)

Original洞见AI IT开发者生活

![](.evernote-content/D2EE471E-9DEB-4F71-BD44-7D010DD859DD/B0426A16-C299-4A92-943D-7019543CA42B.png)

事情是这样的。这两天逛 GitHub 偶然发现了一个叫 **DeepRead** 的开源项目，介绍写着一句话：**用 AI 把任何一本书变成可交互的知识图谱。**

很多人看完都愣了一下。点进去逛了详细了解就知道，这东西值得更多人知道。

痛点：读完就忘
-------

你读完一本书之后，脑子里是不是经常一团浆糊？

**人物关系记不清，核心概念散落在各处，明明刚读完却说不出来这本书到底讲了什么。**

很多人都是这样。

啃完《三国演义》，朋友凑过来问一句：「诸葛亮为什么要北伐？」支支吾吾说了半天，最后憋出一句——你自己去看吧，真的很好看。

挺尴尬的。

![](.evernote-content/D2EE471E-9DEB-4F71-BD44-7D010DD859DD/8854D473-1D2E-41BE-890C-2454E20BB803.png)

把一本书变成"知识博物馆"
-------------

DeepRead 解决的就是这个事。

它的做法很直接：**用 AI 把一整本书拆解成一个个知识节点**——人物、事件、概念、地点、组织——全部结构化，然后用双向链接串起来，变成一个可以点击、跳转、探索的知识网络。

打开《三国演义》的知识图谱，长这样：

* **左边**是人物列表，诸葛亮、曹操、刘备、关羽，94 个核心人物排得清清楚楚
* **右边**是势力阵营，魏、蜀、吴、群雄，每个都有独立页面
* **往下翻**，赤壁之战、官渡之战、夷陵之战，重大事件全部梳理好了

**不是维基百科那种干巴巴的词条。** 每个节点都是 AI 读了全书之后提炼出来的，有人物背景、关键事件、与其他节点的关联。

点进「诸葛亮」，能看到他的完整背景——隆中对的谋略、六出祁山的经历、跟刘备的君臣关系、对蜀汉的鞠躬尽瘁。每个关键信息都链接着其他节点，**像逛博物馆一样逛一本书。**

![](.evernote-content/D2EE471E-9DEB-4F71-BD44-7D010DD859DD/894C3F11-6202-4724-AFA1-EA5F388F1995.png)

这种体验，怎么说呢，很过瘾。

---

26 本书，1800+ 个知识节点
-----------------

说实话，最让人震惊的不是技术本身，而是 **覆盖范围**。

这个项目已经做了 26 本书的知识图谱：

**四大名著全齐**——西游记 192 个节点、三国演义 94 个、水浒传 95 个、红楼梦 73 个

**经典社科**——《百年孤独》48 个、《资本论》三卷加起来 168 个、《孙子兵法》64 个

**还有哲学**——《做哲学》164 个节点，把整本书的哲学概念体系梳理出来了

**你敢信？？？**

而且它不是那种「丢给 AI 一键生成」的粗糙玩意。每一本书都有清晰的分类体系。

拿《西游记》举例，分了 **七个维度**：主要人物、神佛仙圣、妖魔鬼怪、法宝兵器、地名仙府、重要事件、八十一难。192 个节点覆盖了原著几乎所有的关键信息。

点进「事件-三打白骨精」——

白骨精三次变化分别是什么、孙悟空每次怎么识破的、唐僧什么反应、猪八戒怎么挑拨的，**全部结构化地拆解出来了。** 不是简单的剧情复述，是真正的事件拆解。

四步做出一个知识图谱
----------

可能有朋友会问，这东西怎么做的？

坦率的讲，流程比想象中简单。

![](.evernote-content/D2EE471E-9DEB-4F71-BD44-7D010DD859DD/54CF2A66-D41B-4D1C-9EB6-CF88328CF46D.png)

**第一步：格式转换。** 把书转成 Markdown 格式。EPUB 用 **BookTools** 一键转换，PDF 用 **MinerU** 智能解析，TXT 直接拿来用。

**第二步：AI 宏观分析。** 把转好的文本丢给 **Gemini**，它会自动识别全书的结构，分出人物、事件、概念这些维度，生成一个任务清单，规划好需要填充哪些节点。

**第三步：批量填充节点。** AI 按照任务清单，一个一个生成知识节点，同时自动建立双向链接。比如生成「孙悟空」的时候，会自动链接到「如意金箍棒」「花果山」「大闹天宫」「唐僧」「猪八戒」。

**第四步：发布上线。** 可以在 **Obsidian** 里本地使用，看图谱视图、做笔记。也可以用 **Quartz** 部署到 GitHub Pages，变成一个公开网站。

整个流程的核心就两个东西：**Gemini CLI** + **BookTools 命令行工具**。配合起来，一本书从 EPUB 变成可交互的知识图谱网站，**一个人就能搞定。**

它改变了读书的方式
---------

说到底，这东西改变了读书的方式。

传统阅读是线性的——从第一页读到最后一页，知识是一条线。**但大脑不是这样工作的，大脑是网络状的，神经元之间互相连接。**

DeepRead 做的事，就是 **把书的线性结构还原成网状结构**，让知识呈现的方式跟大脑处理知识的方式一致。

读《三国演义》的时候，读到一半忘了马谡是谁，翻回去找？很麻烦。但在知识图谱里，点一下链接就过去了。想知道「赤壁之战」跟哪些人物相关、跟哪些事件相关，**一眼就能看到全部关联。**

**这种阅读体验，以前只有把一本书反复读三四遍才能达到。**

而且它还能帮你发现一些读第一遍时完全注意不到的关联。比如看了《西游记》的知识图谱之后才发现——原来那么多妖怪都跟天上的神仙有关系，不是他们的坐骑就是他们的童子。这个规律在原著里是分散在一百回里的，**不连起来看根本发现不了。**

想想就觉得有意思。

说点实在的，也有局限
----------

当然，这东西也有局限。一是技术门槛。 目前的制作流程需要你会装命令行工具、能配置调用大模型、懂基本的 Markdown 语法。虽然作者写了很详细的教程，但对完全不懂技术的人来说，还是有点劝退。

**二是 AI 准确率。** AI 的理解不是百分百准确的。有些复杂的人物关系、隐喻和潜台词，AI 可能会漏掉或者理解偏差。不过好在所有节点都是 Markdown 文件，可以手动修改和补充。

**三是覆盖面。** 现在只有 26 本书，虽然覆盖了四大名著和一些经典，但离「任何一本书」这个愿景还有距离。

不过说真的，这些问题都不影响对这个项目的看好。因为它的核心思路是对的——**用 AI 做知识的提取和结构化，用人来做最终的校验和补充。** 不是替代人读书，而是帮人更好地读书。

![](.evernote-content/D2EE471E-9DEB-4F71-BD44-7D010DD859DD/20A0A201-A815-4F14-8051-61DB046ADDAF.png)

快速使用
----

GitHub地址：https://github.com/liujuntao123/DeepRead；

网站：https://deepread.aizhi.site，所有已做好的知识图谱可以直接体验，也有完整的制作教程。如果你有一本特别想深入理解的书，不妨试试自己做一个知识图谱。

AI 时代最让人兴奋的事，不是 AI 能替代人做什么，而是 **AI 能帮人做到以前做不到的事。**

把一本书变成一个可交互的知识网络，一个人花几个小时就能搞定——这在以前是不可想象的。而这种能力，现在就在你的浏览器里。

---

以上，既然看到这里了，如果觉得不错，随手点个**赞**、**在看**、**转发**三连吧，如果想第一时间收到推送，也可以给我个**星标**⭐～ 谢谢你看我的文章，我们，下次再见。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzAxNDIzNzc4MQ==&mid=2649399226&idx=1&sn=c7333bd1224760e795bd3d5ed52424d9&chksm=82f1908bc2c6dbd95afe242b9be5696cab81276f9c2bd404efdeebd20fe7c6d705a7a761642b&scene=90&xtrack=1&req_id=1782912544367384&sessionid=1782910875&subscene=93&clicktime=1782915983&enterid=1782915983&flutter_pos=5&biz_enter_id=4&ranksessionid=1782912544&jumppath=WAWebViewController_1782915841363,20020_1782915974550,1122_1782915975414,1104_1782915976998&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b30&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQLJUe1vsDUuwgyrmnIiUyDRLTAQIE97dBBAEAAAAAAB++IwqoKBgAAAAOpnltbLcz9gKNyK89dVj0AIQ7KCGLKPY/0dtE8cgebskf8768ksuqeVo2cCoW94r4T25qN40o3+T2W7VLBRwn50ndDArSb3Awmz9FR/QvP95/ICTJH0jteC91R0BAMyS8W0IE0dd71G8YmPUQMEqnvWhL6oRQqrJWYUnYVRy3NzsoHhvcDi1xADxGs/SOzYEui0OY8txYbnd5kKx3kuRYjNd7twcSMz3hTacrw6FkZeNoBwV0VsTL5kkQD/8=&pass_ticket=YyZAuaAs8+GidSZp4zuMgzOG6KJyJl9eHvWv3/3XRerNHN687BW8MMO31gCOVpIg&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/476a35c4-4f9f-4f4e-a1f0-203980c0fb5c/476a35c4-4f9f-4f4e-a1f0-203980c0fb5c/)