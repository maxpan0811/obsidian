---
title: DeepSeek 本地部署后如何联网搜索，小白必看秘籍！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/DeepSeek 本地部署后如何联网搜索，小白必看秘籍！.html
tags: [AI技术]
---

# DeepSeek 本地部署后如何联网搜索，小白必看秘籍！

原文链接: https://mp.weixin.qq.com/s?chksm=9f081971a87f90677b8e9832cd951d9...

原创阮小贰 阮小贰 
还不知道如何进行DeepSeek本地部署的童鞋赶紧去看看这篇文章：
一篇文章带你搞定DeepSeek本地部署
下午刚发布完 DeepSeek 本地部署的文章之后，
看到评论区有兄弟问到了如何使用联网功能，
于是，晚饭都没吃就立马卷了起来，
经过一番折腾，终于搞定！

废话不多说，先来带大家看一看 DeepSeek 本地部署后联网的效果。
一、DeepSeek本地部署联网效果这是没联网时的答案：

二、DeepSeek本地部署如何实现联网？OK，怎么实现的？
接下来，跟着我的思路一步一步来。
这里要给大家介绍一个浏览器插件：Page Assist

这个插件有啥用?
看它的名字就知道了。
2.1、Page Assist插件官网介绍：Page Assist 是一款开源浏览器扩展程序，可为您的本地 AI 模型提供侧边栏和 Web UI。它允许您从任何网页与您的模型进行交互。

1、本地 AI 模型的 Web UI，支持可视化交互操作（不用安装 Docker 环境，也不用安装 Python 环境）
2、支持联网搜索功能

Github 官网：https://github.com/n4ze3m/page-assist
2.2、Page Assist插件浏览器支持
安装方法，这里分为两种情况：
1、可以科学上网，推荐使用 Chrome 谷歌浏览器
2、无法进行科学上网，推荐使用 Firefox 火狐浏览器或者 Brave 浏览器
三、具体操作步骤这里只给介绍两种浏览器（Chrome 和 Firefox）的安装方式，其他的浏览器的插件安装方式都类似，
需要注意的是，Edge 浏览器目前我还没有找到这个在线插件。
3.1、Chrome 浏览器前提：自行解决科学上网（这里不做介绍，懂的都懂）
打开谷歌应用商店：https://chromewebstore.google.com/
输入【Page Assist】 搜索插件
选择【Page Assist - 本地 AI 模型的 Web UI】
点击【添加到 Chrome】即可，然后固定到 Chrome 浏览器的导航栏上（固不固定都可以）
点击【Page Assist】插件即可打开 DeepSeek 的可视化界面
右上角齿轮【设置】——》【RAG 设置】——》选择文本嵌入模型——》点击【保存】按钮即可

3.2、Firefox 浏览器不需要科学上网，同样是通过扩展打开，地址栏输入：about:addons
输入【Page Assist】 搜索插件
选择【Page Assist - A Web UI for Local AI Models】
点击【添加】即可，然后固定到 Firefox 浏览器的导航栏上（固不固定都可以）
点击【Page Assist】插件即可打开 DeepSeek 的可视化界面
右上角齿轮【设置】——》【RAG 设置】——》选择文本嵌入模型——》点击【保存】按钮即可

四、注意事项1、Ollama 服务必须启动起来。否则会报错
2、如果是用的 Chrome 浏览器，需要科学上网，否则打不开谷歌商店，也就没办法在线安装插件
4.1、如何查看 Ollama 服务是否开启？看到这个 Ollama 的任务栏图标即表示服务已开启。

...4.2、如何开启 Ollama 服务？非常简单，任务栏的搜索框里面输入【Ollama】——》找到 Ollam
