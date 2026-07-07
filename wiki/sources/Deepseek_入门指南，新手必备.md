---
title: Deepseek 入门指南，新手必备
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Deepseek 入门指南，新手必备.md
tags: [AI技术, 教育]
updated: 2026-06-27
---

---
title: "Deepseek 入门指南，新手必备"
source: evernote
type: note
export_date: 2026-06-26
guid: 6bdb486a-cad2-47c7-99f2-aa5783de3142
---

# Deepseek 入门指南，新手必备

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzE4NTk3OA==&mid=265126...](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NTk3OA==&mid=2651267199&idx=1&sn=117bde69c93b5b2e4c6e5022940e0a84&chksm=f2d971604b6f510a28319eaffcac79605b6ebb2b3cef05b5d02e9145cdeb6dcd7bea540d8a11&scene=90&xtrack=1&sessionid=1738654840&subscene=93&clicktime=1738656152&enterid=1738656152&flutter_pos=6&biz_enter_id=4&ranksessionid=1738655331&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQYVc9aTJnjbexPpnCaJoNKRLWAQIE97dBBAEAAAAAACSNA0+oSc8AAAAOpnltbLcz9gKNyK89dVj0GPTPSIdlEHrir3+5wDrcgMfFwsrJicQhOqPqy5QmvkfNYb5dhQ7oXAswKGHOPje+gqgyZ5DuKWRZ3ow9g18IhBTXMxycm8Aw+gHOZuzC6KJzOY7MeqguMeHmvQH36kYZ/3IxY+U9a+aKOiuNdZWx5sEkrzt8uO1HkD4xSf2knyAAVrVeiBwMai5t19p8hSAHtKUPO2uTc57X255gqLNJ9+pcazuljCUV/0QSdWPWMKE=&pass_ticket=tOp2jrPpH0J1E382kq6g0Xv2d/nSgqUFocoT6YcR3HLBtho5ai95WeUPcVUxjI9c&wx_header=3)

原创 效率君 高效率工具搜罗

春节期间，Deepseek发布R1 模型，在推理和数学方面超越OpenAI O1 模型，关键还免费开源。

效率君体验了一下，比如说关于电影神话故事的分析，制作美食等等内容，它都回答的游刃有余。

网络上有很多教程，有专业的还有行业应用，效率君就教大家从0到1怎么使用它。

以及怎么本地部署。

最简单就是网页使用。打开网页，或者在应用商店搜索下载App。

https://chat.deepseek.com/

![](attachments/ede76e379a08683c.png)

【**深度思考**】，就是R1的推理模型，可以自动思考。

【**联网搜索**】，就可以搜索到最近最新的内容，特别是查看最新的新闻。

选择文件（右下角），比如说图片、文档等等，让它提取图片或文档中的文字内容。

不过最近不了Deepseek 的服务器访问有点大，经常会显示服务器有问题，使用不了，这个时候我们就需要使用API，不过Deepseek 官方API 暂时也使用不了。

如果你打游戏或者有专门的显卡，可以自己在本地部署。

如果你没有显卡，可以使用第三方的API，速度也特别快，也很强大，虽然和官方的差一点，但也足够使用。

然后使用第三方的客户端连接就可以使用。

### 本地安装Deepseek R1

Ollama 本地安装Deepseek R1 模型

https://ollama.com/

打开官网，然后点击下载，之后安装到本地。

![](attachments/9f442665538137a9.png)

然后打开Ollama 的模型列表，搜索到DeepSeek R1

https://ollama.com/library/deepseek-r1

![](attachments/d5792e49871bccb0.png)

像我们普通的电脑安装1.5B，7B就可以使用，然后在【**右上角的的代码**】复制在命令行中运行。

![](attachments/1b850d8284553dd6.png)

安装需要一段时间，我们等一下就可以等success，就代表安装成功。

输入【**ollama list**】，就可以查看安装的模型**。**

![](attachments/9b096a668651f6bd.png)

设置安装之后，我们只能在命令行中使用会特别的不方便。

我们需要找到一个第三方客户端。

客户端推荐Chatbox 和Cherry Studio，都很优秀，效率君以Cherry Studio 来演示。

### Cherry Studio

https://cherry-ai.com/

Cherry Studio 是一个特别强大的AI 客户端，支持国内外很多模型。

还内置很多提示词，文生图，文档等功能。

按照下面步骤添加即可。

我们在Cherry Studio 客户端配置Ollama 安装过的模型。

默认API：**http://localhost:11434/v1**

模型名：**deepseek-r1:1.5b**

![](attachments/5d9bb14554d75d76.png)

![](attachments/b52d198c9f714dca.png)

### 第三方API

如果大家的电脑没有GPU，不建议在本地安装，可以使用API。

我们使用【硅基流动】来给大家举例子。

https://cloud.siliconflow.cn

首先就是注册一个账号，注册送14 块，可以用好久。

然后打开【**模型广场**】，找到Deepseek R1，需要复制对应的模型。

![](attachments/874d9fbbea6fe7b9.png)

然后再打开API Key 页面，https://cloud.siliconflow.cn/account/ak，创建一个api-key，再打开Cherry Studio。

![](attachments/af2ff40b7afd8317.png)

模型配置好，打开聊天页面，在顶部选择R1 模型就可以使用了，爽歪歪。

![](attachments/28a33e9521eade9f.png)

### 免费API

大家想使用免费或者便宜的APP，可以在这个网站上查找，它有各种价格的对比。还有免费，目前来说还有两种免费提供。

https://openrouter.ai/deepseek/deepseek-r1:free

![](attachments/d0a8aac27cf44071.png)

不过其他提供API 的价格还是很感人的，大家可以暂时使用。

![](attachments/a3c038c7812b9670.png)

不过和官方比，很多还是很贵的；等官方API 恢复，价格快还便宜。

![](attachments/314278d8bc0d949a.png)

### Prompt

https://api-docs.deepseek.com/prompt-library

![](attachments/f4728111467042da.png)

这个是deepseek 官方的一个提示词网站，它上面包含了很多提示词网站，大家可以参考使用。

可以让它生成提示词，还可以扮演各种角色，格式化输出，代码改写，仿写功能。

使用Deepseek R1，明确【关键词】，提供【上下文】，避免【歧义】，如果有时效性，把联网功能打开。

比如：

- 你作为一个大厨，帮我出美食做法教程，包含步骤注意点食材调料，具体到秒。
- 你现在是一个产品专家和设计专家，帮我梳理分析衡量产品需求，还有细分需求和 app 原型图设计
- 肉饼说中国不会再出一个OpenAI，反驳一下他
- 模仿余华的风格写一段xx的经历
- 导演的主旋律电影，分别都是什么时候上映？
- 我现在月入xx，怎么做一个月入xx的f 业，我懂一些编程和运营方面的技能

大家想要Deepseek 更多玩法，等效率君更新。

大家有什么疑问，欢迎在评论区留言，效率君会一一解答。

**更多推荐：**

- [7 个超级无敌的软件，强大到没对手](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NTk3OA==&mid=2651267151&idx=1&sn=e44d0b521ab57ca9b5552664445f4c5e&scene=21#wechat_redirect)
- [这8 款冷门软件真香，让你的电脑变强](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NTk3OA==&mid=2651267139&idx=1&sn=b106dcae99e72e5845c2c34d403c5001&scene=21#wechat_redirect)
- [推荐6 款免费无敌的软件，真的没有对手](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NTk3OA==&mid=2651267122&idx=1&sn=b6ff5a377e64f46ce63f52e173110073&scene=21#wechat_redirect)

更多优质软件关注效率君公众号：**高效率工具搜罗**（ID：gongju006）。
