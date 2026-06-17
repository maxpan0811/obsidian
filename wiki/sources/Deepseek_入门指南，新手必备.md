---
title: Deepseek 入门指南，新手必备
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/Deepseek 入门指南，新手必备.html
tags: [AI技术, 教育]
---

# Deepseek 入门指南，新手必备

原文链接: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NTk3OA==&mid=265126...

春节期间，Deepseek发布R1 模型，在推理和数学方面超越OpenAI O1 模型，关键还免费开源。
效率君体验了一下，比如说关于电影神话故事的分析，制作美食等等内容，它都回答的游刃有余。
网络上有很多教程，有专业的还有行业应用，效率君就教大家从0到1怎么使用它。
以及怎么本地部署。
最简单就是网页使用。打开网页，或者在应用商店搜索下载App。
https://chat.deepseek.com/

【深度思考】，就是R1的推理模型，可以自动思考。
【联网搜索】，就可以搜索到最近最新的内容，特别是查看最新的新闻。
选择文件（右下角），比如说图片、文档等等，让它提取图片或文档中的文字内容。
不过最近不了Deepseek 的服务器访问有点大，经常会显示服务器有问题，使用不了，这个时候我们就需要使用API，不过Deepseek 官方API 暂时也使用不了。
如果你打游戏或者有专门的显卡，可以自己在本地部署。
如果你没有显卡，可以使用第三方的API，速度也特别快，也很强大，虽然和官方的差一点，但也足够使用。
然后使用第三方的客户端连接就可以使用。
本地安装Deepseek R1Ollama 本地安装Deepseek R1 模型
https://ollama.com/
打开官网，然后点击下载，之后安装到本地。

然后打开Ollama 的模型列表，搜索到DeepSeek R1
https://ollama.com/library/deepseek-r1

像我们普通的电脑安装1.5B，7B就可以使用，然后在【右上角的的代码】复制在命令行中运行。

安装需要一段时间，我们等一下就可以等success，就代表安装成功。
输入【ollama list】，就可以查看安装的模型。

设置安装之后，我们只能在命令行中使用会特别的不方便。
我们需要找到一个第三方客户端。
客户端推荐Chatbox 和Cherry Studio，都很优秀，效率君以Cherry Studio 来演示。
Cherry Studiohttps://cherry-ai.com/
Cherry Studio 是一个特别强大的AI 客户端，支持国内外很多模型。
还内置很多提示词，文生图，文档等功能。
按照下面步骤添加即可。
我们在Cherry Studio 客户端配置Ollama 安装过的模型。
默认API：http://localhost:11434/v1
模型名：deepseek-r1:1.5b

第三方API如果大家的电脑没有GPU，不建议在本地安装，可以使用API。
我们使用【硅基流动】来给大家举例子。
https://cloud.siliconflow.cn
首先就是注册一个账号，注册送14 块，可以用好久。
然后打开【模型广场】，找到Deepseek R1，需要复制对应的模型。

然后再打开API Key 页面，https://cloud.siliconflow.cn/account/ak，创建一个api-key，再打开Cherry Studio。

模型配置好，打开聊天页面，在顶部选择R1 模型就可以使用了，爽歪歪。

免费API大家想使用免费或者便宜的APP，可以在这个网站上查找，它有各种价格的对比。还有免费，目前来说还有两种免费提供。
https://openrouter.ai/deepseek/deepseek-r1:free

...不过
