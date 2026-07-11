# Token 无限免费，终于来了。

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3NzU0NzIxMA==&mid=224751...](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247513384&idx=1&sn=29c025ebe4a8580c7726a1d06478dbd8&chksm=ce05b96c3bf9d8b37749cfa89afd6e82903f33075b989972324087f4ef8a218e0d56c2f6af3f&scene=90&xtrack=1&req_id=1782573090796231&sessionid=1782571959&subscene=93&clicktime=1782573326&enterid=1782573326&flutter_pos=33&biz_enter_id=4&ranksessionid=1782573090&jumppath=20020_1782573090261,1104_1782573200310,20020_1782573207262,1104_1782573322674&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQfVYUpVUc4Y7f7oGIT+cX3hLTAQIE97dBBAEAAAAAAH+WBaRk1GIAAAAOpnltbLcz9gKNyK89dVj0Te6P6sysUDvHoG/Rr/tVIfPKKaM/YatfIUE5q9coh36hMiv2YUcLPTxMfQfWPJB1gaGcHdeEP4C6uGDdXayDFV9YdvgcGH5lB9R7J/ZpfgLZb3VBWmLspFF7cOyfQV3kc3AglTXqsRV2H8NZzg0wGEO54/BuB6GUC4TLQORhIWaU98VVy2Wwi2AlOU9ZNRTSt4n5jJv3wq0tj+OYUQaK0aejnZ1KqjWHn8SJPBE=&pass_ticket=Dl5lljhxaMno3aMu+MBuhxEjQg8vVXVEzPSe+F00opHtq2g2IwATwLCmNJH4Mecj&wx_header=3)

Original开源日记开源日记

上线两周，调用量 3.12 万亿 Token。

第三周的时候，用量已经达到了4.11万亿Token。

图片生成累计上千万张，视频生成累计数百万秒。

这些数据来自一个叫 Agnes AI 的产品。它是全球榜单前十的 AI Lab 。

6 月 1 日，他们搞了个大事情。

把文本、图片和视频这三个模型的 API 全部都免费对外开放了。

**无限期免费开放三个模型的 API：**

* 文本模型 Agnes-2.0-Flash
* 图片模型 Agnes-Image-2.1-Flash
* 视频模型 Agnes-Video-V2.0

不是试用期，也没有上限，直接把调用费用降到0。

我先用 3个 案例给你们看看
--------------

**文本模型：以前处理长文档要算 Token**

一个搞运维的要对一份有 50 多页的硬件采购合同进行分析，并从中发现其中存在的风险条款。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/098C41A6-4168-4D49-AAF3-80746FC05183.png)

你要用GPT，光输入就消耗掉几万多个 token，再加上合同数据一条条地分析、生成报告，来回几次账单就会很高。

用上 Agnes-2.0-Flash：把整份合同丢进去，让它逐条分析并标注出风险点，还可以任意提问，费用全免。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/4AB66347-509E-4804-93A9-CE84CE276663.png)

**图片模型：以前做设计要算张数**

一个老板要给新开的烧烤店做几个不同尺寸的海报，要发布到微信、微博、抖音这三个平台上。

很多人说用 Midjourney 来生成图片，效果好，单一张图大概要几十块钱，如果尺寸不对还要再生成一次。真心用不起。

用 Agnes-Image-2.1-Flash：给它一句话，然后让其产生多种大小的海报，要横版有横版，要竖版有竖版，全免费。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/CFC71DB1-C13E-4FB7-9399-D92AEEFED98D.png)

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/6836EC63-50A2-4E25-B3F7-A6380E89519C.png)

看一下成片，很有感觉吧。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/DF93FECC-E5C3-4FFF-9E68-B342849EEC3E.png)

**视频模型：以前做素材要算秒数**

我用Agnes-Video-2.0做了一个15秒的视频。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/4F5AE98B-6ED7-433E-8679-3A4F5AB328E1.png)

整个过程大概就 5 分钟左右。成片的质量还可以，大家自己看。

这要用 Runway 来做，每秒视频几毛钱，光是生成费用就要一两百块。要是效果不理想的话，还要再做一遍。

它把三种全模态模型的能力都给你
---------------

**01 文本模型：一句话就可以替代一本书**

Agnes-2.0-Flash 最多可以支持 1M 的上下文，但是在调用高峰的时候会被限制在 512K。

1M 这到底意味着什么？

可以把一本书、一份合同或者整个项目的全部代码扔进去，不需要切片、不需要分段，它会自己去理解。

以前做长文档分析要不断地分段、合并，现在可以直接把整个文档交给模型来处理。

**02 图片模型：4K超清、可修改**

Agnes-Image-2.1-Flash 可以生成 4096×4096 的 4K 图片，比一般的高清还要清晰一点。

不仅可以生成图片，还可以对图片进行修改、换背景、局部修改、变风格。

**03 视频模型：画面声音一起出**

视频生成本来就是个烧钱的事情，现在也可以免费用了。

Agnes-Video-V2.0 可以做到画面和声音同时出现，并且不需要人工配音。可以用一张图来生成视频，用两张图做过渡，做出多个镜头的内容。

免费不代表实力减弱，在评测数据中可以看得出是有底气的
--------------------------

很多人一听到“免费”，第一反应就是：

免费的东西，能力一定不好吧？

但是从公开的数据来看，Agnes 还是很能打的。

Agnes-2.0-Flash 在全球 Agent 能力榜上排名前十，在部分任务中甚至超过了Gemini Flash 和 MiniMax M2.7。

Agnes-Image-2.0-Flash 也进入了 Artificial Analysis 图片编辑榜的世界前列。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/41B40859-A351-4AA8-BD69-1202718BB424.png)

注意 Artificial Analysis 采用的是真实用户的盲测方式，评判者不知道作品来自哪个模型，只根据结果打分。

同时成品数量也创新高。

图片模型每周能产生超过 567 万张的图片，视频模型每天能够产生超过 237 万秒的视频。

图片、视频占的比例很大，也说明免费政策确实击中了用户需求。

所以 Agnes 想证明的并不是“免费但缩水”，而是：

**同样的品质，更低的门槛，甚至直接免费。**

而且它兼容主流工具，上手成本几乎为零
------------------

Agnes 接口与 OpenAI 完全兼容，只须改动一个地址即可使用。

怎样接入呢？非常简单：

首先到 platform.agnes-ai.com 上注册一个账号，并获得API key

然后打开 cc-switch，填上 https://apihub.agnes-ai.com/v1 和 上面的 API key

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/7BE06E02-6F81-4386-91E4-113B42F1EF29.png)

模型 Key 别填错了。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/1462CD4C-B55B-437B-B9C2-B929E216005D.png)

最后打开  ClaudeCode 就可以用了。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/C7F14CDD-6F4F-4E4E-B60D-F9F57752F659.png)

文本、图片、视频三种模式都可以使用，并且调用也是一样的。

写在最后
----

注意目前视频生成是异步的，不能实时拿到结果，需要等一会儿再查询。

高峰期排队可能要等 3-5 分钟，不像文本和图片那样秒出。

生成出来的视频链接是暂时性的，要尽快下载并保存好，否则过了期限就没有了。

感兴趣的朋友们可以去 https://agnes-ai.com 试一试。

另外官方还开了一个 GitHub 仓库来追踪用户的反馈问题。

https://github.com/AgnesAI-Labs/Agnes-AI/issues

遇到响应慢、图片偶发报错、客户端接入失败这类问题，都可以去这里找答案。

![](.evernote-content/C2FFA5F7-4D05-4F2E-A967-539F295F0FBA/E38A4719-DB2A-4CD2-993E-CE7B3659B4F6.png)

既然看到这了，欢迎随手点赞、在看、转发，也可以给我个星标⭐，接收最新的文章，我们下期见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247513384&idx=1&sn=29c025ebe4a8580c7726a1d06478dbd8&chksm=ce05b96c3bf9d8b37749cfa89afd6e82903f33075b989972324087f4ef8a218e0d56c2f6af3f&scene=90&xtrack=1&req_id=1782573090796231&sessionid=1782571959&subscene=93&clicktime=1782573326&enterid=1782573326&flutter_pos=33&biz_enter_id=4&ranksessionid=1782573090&jumppath=20020_1782573090261,1104_1782573200310,20020_1782573207262,1104_1782573322674&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2d&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQfVYUpVUc4Y7f7oGIT+cX3hLTAQIE97dBBAEAAAAAAH+WBaRk1GIAAAAOpnltbLcz9gKNyK89dVj0Te6P6sysUDvHoG/Rr/tVIfPKKaM/YatfIUE5q9coh36hMiv2YUcLPTxMfQfWPJB1gaGcHdeEP4C6uGDdXayDFV9YdvgcGH5lB9R7J/ZpfgLZb3VBWmLspFF7cOyfQV3kc3AglTXqsRV2H8NZzg0wGEO54/BuB6GUC4TLQORhIWaU98VVy2Wwi2AlOU9ZNRTSt4n5jJv3wq0tj+OYUQaK0aejnZ1KqjWHn8SJPBE=&pass_ticket=Dl5lljhxaMno3aMu+MBuhxEjQg8vVXVEzPSe+F00opHtq2g2IwATwLCmNJH4Mecj&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8450be9a-eb6c-4a27-9895-b49371fb9118/8450be9a-eb6c-4a27-9895-b49371fb9118/)