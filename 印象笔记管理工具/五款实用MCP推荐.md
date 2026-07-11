# 五款实用MCP推荐

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkyNzU0MzQwOQ==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkyNzU0MzQwOQ==&mid=2247484320&idx=1&sn=f573baef0ecfbed1eb0db21a0ee108aa&chksm=c3182654e6623e5caa5343c8fc303ef2ec6eaa0067d1c82db01bef6d8a9f8ee92c3b229e642c&scene=90&xtrack=1&sessionid=1746951169&subscene=93&clicktime=1746951616&enterid=1746951616&flutter_pos=8&biz_enter_id=4&ranksessionid=1746951472&jumppath=20020_1746951425706,1104_1746951453168,20020_1746951472270,1104_1746951608041&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b26&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQE1Cv1EoAbPLvqPcSFZ/LPhLVAQIE97dBBAEAAAAAAFo2NYqLRxgAAAAOpnltbLcz9gKNyK89dVj01x3bJDaG85OIcT/LY8+1iQ7+kCMJRYirnk3Jg/2QefXvwyGd/ljUY0grEDpwWi/K1JHiqo2pfu5nAcjxiQw2oWwv9I/agV0cxkH8GhJe/TOjN7nXVXR7HeW0zVznMnBm6oItZxoHu2XYttz+5L25A/wRt6v9F4RxcS8grOHnZ9tOzTFtxOCfVWbTmeOdp/CcJwZ3B8g8xiWE3rZhqYiXzTseoNlUwZgPeHgLtC2LKA==&pass_ticket=FXPM5oVjRVtL3wyT6oVPlIFuCyPINQj7Y/HLs6f/r5u9K1CqvF8ucTBCrdewiyl/&wx_header=3)

Original黄益贺 newtype AI

视频号：黄益贺

YouTube / Medium: huangyihe

以下为视频内容的文字版

MCP火这么久了，有哪些是日常当中经常会用到的，真的能提升生产力的？

本期视频我会介绍五个我基本上每天都会用的MCP。看起来特别朴实无华、没什么节目效果，但它们就是好用。

这些MCP，以及更多AI工具，我平时都会在社群内分享。想提升AI生产力的小伙伴记得加入。

那咱们先从前两个MCP开始，它们是一对组合。

Tavily是我用了很久的、专门为大模型优化过的搜索引擎。它的MCP里包含了搜索和提取两个工具，特别实用。但是，如果你只用这一个MCP，虽然可以联网搜索，但答案不会太好。

比如，我提了一个问题：皇马在本赛季为什么表现不好？详细分析。

Claude使用Tavily找了一堆网页，似乎回答了我的提问。但咱们来仔细看，它所谓的详细分析，说什么“比赛成绩不稳定”、“欧冠表现不佳”，这都是现象，不是原因，根本不叫“详细分析”。

你看，作为模型，Claude 3.7 Sonnet够强了吧？结果，给出的答案却这么水。

这个时候，就需要Sequential Thinking这个MCP。它的作用就是让模型进行多步骤推理。加上之后，效果非常明显。

还是同样的问题，详细分析皇马本赛季的原因。我特意要求使用Sequential Thinking和Tavily这一对组合。

开始都一样，就是搜集资料。但在此之后，Claude调用了七次Sequential Thinking。

展开之后可以看到，有了这个MCP，模型的逻辑明显变强了。Claude把皇马的问题提炼了出来，包括伤病、疲劳、训练方式和体能管理等等。再看正式的答案，明显比刚才的靠谱多了，对吧？

这一对组合，Tavily解决信息的问题，Sequential Thinking解决逻辑的问题。这两个都是很基础、很重要的能力，一定要给模型加上。

OK，咱们再来看接下来的两个MCP，也是一对组合。

Filesystem能让模型接入指定的文件夹，比如桌面，去读取桌面上的文件，以及创建新的文件。

像Cursor之类的客户端，因为它是拿来编程用的，所以天然就具备很强的文件读取和编辑能力。但是，像ChatWise这种客户端就难搞了。所以需要Filesystem。至于安全问题，大家可以放心：文件夹都由咱们来指定，不用担心模型会乱来。

跟Filesystem搭配的MCP是Markitdown。这是微软之前出的工具，能够将PDF转成Markdown格式。现在出了MCP之后，模型终于可以处理PDF这种文档了。

我个人对PDF是深恶痛绝的。从技术角度看，这种格式都快接近图片了，搞起来太费劲。PDF在AI时代就应该被完全淘汰。

那么，Filesystem加上Markitdown，能怎么用呢？

比如，我在桌面上有一个PDF文档，是特别有名的《Bitter Lesson》。如果我想把它转成Markdown格式的话，现在可以直接跟模型说。它会先用Filesystem确认能不能访问桌面。然后用Markitdown做转换。最后再用Filesystem在桌面创建新文件，把提取出来的内容写进去。

或者，我也可以直接让模型帮我总结。

你看，我跟模型说，帮我读取并总结桌面上的PDF文档。它马上就知道，要用Filesystem和Markitdown进行读取和提取，然后就可以总结了。

Claude上下文窗口不大，处理这种只有两页的PDF是OK。如果碰上那种十几页的，最好还是换成Gemini系列。

刚才介绍的两组MCP，前一组用来处理网页信息，后一组用来处理文档信息。那么，自己的笔记信息怎么通过MCP给到模型呢？

如果你像我一样用本地向量数据库的话，可以选择Milvus。这个数据库支持存储和检索。部署好之后，OrbStack一直挂着运行。然后不管你用哪个客户端，都可以随时通过MCP获取数据。

关于Milvus的部署，我前两天出了一期社群专属视频，把要点都一一介绍了。已经加入社群的小伙伴记得看。

如果你想用云端向量数据库的话，可以选择Pinecone。它同样也有MCP。如果你动手能力再强一些的话，可以使用AWS，这个就更强力了。之后我也会出社群专属视频详细介绍。

所以，这五个就是我每天都在使用的MCP。你发现没有，它们都围绕信息展开——让模型获取更多信息，让模型处理信息的能力提升。有了这些工具，模型就不再是缸中之脑。

OK，以上就是本期内容。想了解AI，想成为超级个体，想找到志同道合的人，就来我们newtype社群。那咱们下期见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkyNzU0MzQwOQ==&mid=2247484320&idx=1&sn=f573baef0ecfbed1eb0db21a0ee108aa&chksm=c3182654e6623e5caa5343c8fc303ef2ec6eaa0067d1c82db01bef6d8a9f8ee92c3b229e642c&scene=90&xtrack=1&sessionid=1746951169&subscene=93&clicktime=1746951616&enterid=1746951616&flutter_pos=8&biz_enter_id=4&ranksessionid=1746951472&jumppath=20020_1746951425706,1104_1746951453168,20020_1746951472270,1104_1746951608041&jumppathdepth=4&ascene=56&devicetype=iOS18.4.1&version=18003b26&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQE1Cv1EoAbPLvqPcSFZ/LPhLVAQIE97dBBAEAAAAAAFo2NYqLRxgAAAAOpnltbLcz9gKNyK89dVj01x3bJDaG85OIcT/LY8+1iQ7+kCMJRYirnk3Jg/2QefXvwyGd/ljUY0grEDpwWi/K1JHiqo2pfu5nAcjxiQw2oWwv9I/agV0cxkH8GhJe/TOjN7nXVXR7HeW0zVznMnBm6oItZxoHu2XYttz+5L25A/wRt6v9F4RxcS8grOHnZ9tOzTFtxOCfVWbTmeOdp/CcJwZ3B8g8xiWE3rZhqYiXzTseoNlUwZgPeHgLtC2LKA==&pass_ticket=FXPM5oVjRVtL3wyT6oVPlIFuCyPINQj7Y/HLs6f/r5u9K1CqvF8ucTBCrdewiyl/&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ba6c9a0a-d59d-4062-a8ae-08e124fb6acb/ba6c9a0a-d59d-4062-a8ae-08e124fb6acb/)