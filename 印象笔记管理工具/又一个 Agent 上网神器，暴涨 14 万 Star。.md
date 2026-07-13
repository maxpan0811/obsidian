# 又一个 Agent 上网神器，暴涨 14 万 Star。

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3NzU0NzIxMA==&mid=224751...](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247513982&idx=1&sn=f2e957ff64c0f217140860b9fc7eeb0c&chksm=cec3b6036193bc3d45f95ecbbb60647e42fbf4e746f3f1dc3f41422580bca89ab3dbe1b5f5e1&scene=90&xtrack=1&req_id=1783852038566418&sessionid=1783851610&subscene=93&clicktime=1783852078&enterid=1783852078&flutter_pos=8&biz_enter_id=4&ranksessionid=1783852038&jumppath=20020_1783852004864,1104_1783852006331,20020_1783852038112,1104_1783852065044&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b21&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQYYAZOFBULlRJ7S4sq5HRYhLTAQIE97dBBAEAAAAAANJ0Mzz/CYEAAAAOpnltbLcz9gKNyK89dVj0OGdagN5cTkF1NRt6uqZVB2E3QGyqdyzWZtJdFwE3pIJxxnkcX9Der1XwYUDuAVvPmG7QbtZIpYkJAAlLgRcrOLaqGtNzyZKIIRpWQ2RWVoX2Z8/x1uvTGGtr5PNrs24kLthq5MvNHkKlCBXHFUXTf8MOc2w18asqsLhU0bESzkPDHORSp3imIgpnFQsNNHk9NmczoH0UDbYz6U8Q5CkXxQxP1pjIJeJxXENp7t8=&pass_ticket=ilXOtwKDhPScubPWjKG7nzoIqNFLesV47v1DJtvC3GDqHKKYgijneJLGu9kSc1so&wx_header=3)

又一个 Agent 上网神器，暴涨 14 万 Star。
============================

Original开源日记开源日记

做 AI 应用的人，基本都会遇到相同的问题。

模型训练所用到的数据有一个截止时间，而现实世界每天都在发生变化。

为了让Agent获取到最新的网页数据，一般只能自己搭建爬虫或者购买网页数据API。

前者需要解决JavaScript渲染、反爬机制、代理池、数据清洗等一系列问题。

后者的成本很高，返回的数据不能直接用于大语言模型。

最近在 GitHub 上看到一个项目，已经把这件事做成了一个标准能力。

**它的名字叫做Firecrawl，在GitHub上有14.9万颗星。**

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/A09F1724-2F4A-4901-AB07-A68CD69A25AC.png)

用一句话概括：

**它把任意网页转换成干净的 Markdown 或结构化 JSON，并通过一个 API 直接交给 AI 使用。**

很多人第一次看到都会觉得：这不就是一个爬虫吗？

它所要解决的问题并不是网页抓取，而是使网页数据能够直接进入AI工作流。

先来看几个最典型的使用场景。
--------------

**给RAG系统加上网页数据**

很多 AI 应用都会遇到这样的问题。

比如用户问：西门子最新推出的产品是什么？

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/A5F64DBA-0A0E-4F01-A79C-70D376A3201A.png)

模型训练的时候不知道，但是官网已经更新了。

以前要重新写爬虫、解析网页、清洗数据，然后导入到向量数据库里。

现在只要抓取官网页面就可以得到干净的 Markdown。

直接添加到知识库里面。

**批量提取商品，新闻等结构化的数据**

对几个竞争者的网站进行分析。

传统的做法是为每一个网站分别编写CSS选择器、XPath或者正则表达式。

网站一旦有一点点变化，就必须要重新维护。

Firecrawl 可以直接定义出 JSON Schema。

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/3354CD6E-A1D3-4A26-83FC-D8BD12695F65.png)

比如商品名称、价格、评分、库存等等几个字段。

返回的结果就是标准的JSON格式。

不管网页用什么样的布局方式，也不用研究DOM结构，只要告诉它最后要获取的数据是什么就可以了。

**AI自己去网上找答案**

Firecrawl 新增的功能也最有趣。

以前必须事先准备好目标网址。

现在只要让AI说：整理出OpenAI最新的模型价格。

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/E47E185E-C701-41FD-903D-37CBD509FE93.png)

它会自动去搜索网页、进入网站、浏览页面然后提取出结果。

整个过程就是可以真正上网的 Agent。

到这里就差不多可以知道为什么 Firecrawl 会受到欢迎了。

它不仅是一个网页抓取工具，而且把网页获取、正文提取、结构化输出和Agent自动导航等所有功能都集成在一起，形成了一整套的功能。

有人要好奇怎么做到的
----------

**01 抓取层突破：12 种引擎并发竞速，自动处理 JS 渲染和反爬**

Firecrawl 内置了 Playwright、Puppeteer、Chrome CDP 等 12 种抓取引擎，在并发启动之后会自动选择出最快速、最稳定的结果。

同时实现了JavaScript渲染、代理轮换、反爬处理。

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/4F67D258-87BF-4FA0-929A-F748CBC0BF41.png)

开发者只需要写一个代码：

```
app.scrape("https://example.com")
```

浏览器启动、页面加载、正文提取等等都实现了自动化的功能。

**02 层级优化：输出格式LLM准备就绪，准确率96%**

支持Markdown、HTML、JSON、截图等格式输出，得到的就是已经清洗好的正文。

可以定义JSON Schema，Firecrawl会自动理解页面语义并输出结构化的数据。

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/0C740FED-11D3-40F7-B891-1C6C149BE571.png)

question 和 highlights 两种模式只返回核心内容，比整页抓取最多可以节省 100 倍的 Token 消耗。

**03 代理层进阶：从知道网址到知道目标**

开发者不需要提前准备好URL，只需要说明要达到的目的就可以。

比如说找到Notion最新的价格。

FIRE-1 Web Action Agent 内置有自动搜索、点击、填表单以及提取结果的功能。

![](.evernote-content/D1BB5C94-5752-4B99-BEB7-07D5A0D8F1F3/145387D0-D269-4210-B35F-B0C8CEC1C05D.png)

底层的PDF解析，链接提取等模块用到了Rust NAPI，速度提升3-5倍。

看完这些功能，相信很多人已经想试试了
------------------

Python用户：

```
pip install firecrawl-py
```

下面给出一些常见的API调用示例

**01 网页正文抓取**

```
from firecrawl import FirecrawlApp  
  
app=FirecrawlApp(api_key="your-api-key")  
  
result = app.scrape_url("https://example.com")  
  
print(result["markdown"])
```

输出就是干净的Markdown，可以被直接写入到向量数据库或者知识库中。

**02 用Agent来获取需要的信息**

```
result = app.extract(  
    [  
        "https://openai.com",  
        "https://openai.com/pricing"  
    ],  
    {  
        "prompt": "Extract pricing information for GPT-4 models"  
    }  
)
```

对自动化的数据采集和Agent的应用场景来说，这种方法比传统的网页爬虫更具有灵活性。

**03 也可以用 skill 的方式来使用**

打开CC之后执行以下命令：

```
npx -y firecrawl-cli@latest init --all --browser
```

这样就可以在命令行调用了。

写在最后
----

Firecrawl 并不是只有做网页爬虫的功能。

它把网页抓取、内容提取和结构化输出结合起来，让网页数据可以直接用到AI应用里。

但是它不能抓取需要登录的付费内容，并且会遵守robots.txt。

如果你在做RAG、AI Agent或者是企业知识库。

可以试一试这个项目。

项目基于 AGPL-3.0 协议开放，感兴趣的同学可以去 GitHub 仓库看看源码和文档。

开源地址：https://github.com/firecrawl/firecrawl

既然看到这了，欢迎随手点赞、在看、转发，也可以给我个星标⭐，接收最新的文章，我们下期见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247513982&idx=1&sn=f2e957ff64c0f217140860b9fc7eeb0c&chksm=cec3b6036193bc3d45f95ecbbb60647e42fbf4e746f3f1dc3f41422580bca89ab3dbe1b5f5e1&scene=90&xtrack=1&req_id=1783852038566418&sessionid=1783851610&subscene=93&clicktime=1783852078&enterid=1783852078&flutter_pos=8&biz_enter_id=4&ranksessionid=1783852038&jumppath=20020_1783852004864,1104_1783852006331,20020_1783852038112,1104_1783852065044&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b21&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQYYAZOFBULlRJ7S4sq5HRYhLTAQIE97dBBAEAAAAAANJ0Mzz/CYEAAAAOpnltbLcz9gKNyK89dVj0OGdagN5cTkF1NRt6uqZVB2E3QGyqdyzWZtJdFwE3pIJxxnkcX9Der1XwYUDuAVvPmG7QbtZIpYkJAAlLgRcrOLaqGtNzyZKIIRpWQ2RWVoX2Z8/x1uvTGGtr5PNrs24kLthq5MvNHkKlCBXHFUXTf8MOc2w18asqsLhU0bESzkPDHORSp3imIgpnFQsNNHk9NmczoH0UDbYz6U8Q5CkXxQxP1pjIJeJxXENp7t8=&pass_ticket=ilXOtwKDhPScubPWjKG7nzoIqNFLesV47v1DJtvC3GDqHKKYgijneJLGu9kSc1so&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/56d3da4f-b10a-45cb-94d0-6bb9731f5a2e/56d3da4f-b10a-45cb-94d0-6bb9731f5a2e/)