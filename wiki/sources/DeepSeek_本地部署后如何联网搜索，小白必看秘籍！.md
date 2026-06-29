---
title: DeepSeek 本地部署后如何联网搜索，小白必看秘籍！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/DeepSeek 本地部署后如何联网搜索，小白必看秘籍！.html
tags: [AI技术]
updated: 2026-06-27
---

---
title: "DeepSeek 本地部署后如何联网搜索，小白必看秘籍！"
source: evernote
type: note
export_date: 2026-06-27
guid: 014ea5d9-8d84-4f5a-a434-945a56b0c61a
---

# DeepSeek 本地部署后如何联网搜索，小白必看秘籍！

原文链接: [https://mp.weixin.qq.com/s?chksm=9f081971a87f90677b8e9832cd951d9...](https://mp.weixin.qq.com/s?chksm=9f081971a87f90677b8e9832cd951d9c903661f28d778678f5ee71abe2ce123731e1eded36e1&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_2&scene=169&mid=2247484622&sn=349ab4a818e8ae936530e929cbf42d2a&idx=1&__biz=MzA3MzgxMzIwMA==&sessionid=1738654840&subscene=200&clicktime=1738658007&enterid=1738658007&flutter_pos=48&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVX78C4O59oCW1BQrIto4MBLWAQIE97dBBAEAAAAAAOTrLnDmHp4AAAAOpnltbLcz9gKNyK89dVj0jQWIXBHSY2XZRY8UhJTydYJqI6w27bmOaRP+5DfvR4DVkVmqqs0e4wtB7ttSgXeKJA9Ho4csnDIrclE0qCDL+tip7qdMoqsiVhh38fvSWw28Euq+yOVKXNSEdEGeUKmRX7UO/Zp/R/RSYoPk1V8ZO4P5VAItoYKup7ZmVLdZCAjD4H4X61V524e2xl28KivSp+PsxXDFkCbZeijP3l6PBiP9NLUqqasjKtK4Tk34nSM=&pass_ticket=hdv9u80/6f7pvh17GIdzMK9ykEhOr787LKqgjWORmcM8dVw6dyjIsb3sSOdMJP1Y&wx_header=3)

原创阮小贰阮小贰

还不知道如何进行DeepSeek本地部署的童鞋赶紧去看看这篇文章：

[一篇文章带你搞定DeepSeek本地部署](https://mp.weixin.qq.com/s?__biz=MzA3MzgxMzIwMA==&mid=2247484521&idx=1&sn=863c6d016358b4165666dbc0037f77d1&scene=21#wechat_redirect)

下午刚发布完 DeepSeek 本地部署的文章之后，

看到评论区有兄弟问到了如何使用联网功能，

于是，晚饭都没吃就立马卷了起来，

经过一番折腾，终于搞定！

废话不多说，先来带大家看一看 DeepSeek 本地部署后联网的效果。

## 一、DeepSeek本地部署联网效果

这是没联网时的答案：

![](attachments/82ae83ee1e67be10.png)

这是联网后的答案：

![](attachments/8e3af18dc4af5801.png)

## 二、DeepSeek本地部署如何实现联网？

OK，怎么实现的？

接下来，跟着我的思路一步一步来。

这里要给大家介绍一个浏览器插件：**Page Assist**

![](attachments/d4b9b6b0a90f8a80.png)

这个插件有啥用?

看它的名字就知道了。

### 2.1、Page Assist插件官网介绍：

**Page Assist** 是一款开源浏览器扩展程序，可为您的本地 AI 模型提供侧边栏和 Web UI。它允许您从任何网页与您的模型进行交互。

- 1、本地 AI 模型的 Web UI，支持可视化交互操作（不用安装 Docker 环境，也不用安装 Python 环境）
- 2、支持联网搜索功能

![](attachments/45f906b30803d558.png)

Github 官网：https://github.com/n4ze3m/page-assist

### 2.2、Page Assist插件浏览器支持

![](attachments/4c36782bdadeeaca.png)

安装方法，这里分为两种情况：

- 1、可以科学上网，推荐使用 Chrome 谷歌浏览器
- 2、无法进行科学上网，推荐使用 Firefox 火狐浏览器或者 Brave 浏览器

## 三、具体操作步骤

这里只给介绍两种浏览器（**Chrome** 和 **Firefox**）的安装方式，其他的浏览器的插件安装方式都类似，

需要注意的是，**Edge** 浏览器目前我还没有找到这个在线插件。

## 3.1、Chrome 浏览器

1. 前提：自行解决科学上网（这里不做介绍，懂的都懂）
2. 打开谷歌应用商店：https://chromewebstore.google.com/
3. 输入【Page Assist】 搜索插件
4. 选择【Page Assist - 本地 AI 模型的 Web UI】
5. 点击【添加到 Chrome】即可，然后固定到 Chrome 浏览器的导航栏上（固不固定都可以）
6. 点击【Page Assist】插件即可打开 DeepSeek 的可视化界面
7. 右上角齿轮【设置】——》【RAG 设置】——》选择文本嵌入模型——》点击【保存】按钮即可

![](attachments/d3ae7af6aeac8bd6.png)

![](attachments/ba2075a1f3ddd9c9.png)

![](attachments/182bf76956a22187.png)

![](attachments/6178047bd12f1b74.png)

![](attachments/0ed0c5343e7f2642.png)

## 3.2、Firefox 浏览器

1. 不需要科学上网，同样是通过扩展打开，地址栏输入：about:addons
2. 输入【Page Assist】 搜索插件
3. 选择【Page Assist - A Web UI for Local AI Models】
4. 点击【添加】即可，然后固定到 Firefox 浏览器的导航栏上（固不固定都可以）
5. 点击【Page Assist】插件即可打开 DeepSeek 的可视化界面
6. 右上角齿轮【设置】——》【RAG 设置】——》选择文本嵌入模型——》点击【保存】按钮即可

![](attachments/0cb45880687b8243.png)

![](attachments/9853866ef4b8e6cb.png)

![](attachments/ec4c963ca5454599.png)

![](attachments/9afdc6588a011bb3.png)

![](attachments/f58ef859c7903e43.png)

![](attachments/e9abe1e45ecbb015.png)

![](attachments/5229d02afe74abf5.png)

![](attachments/a53369c729db4e33.png)

![](attachments/d0c75b7a0c275fc0.png)

![](attachments/0ed0c5343e7f2642.png)

## 四、注意事项

- 1、Ollama 服务必须启动起来。否则会报错
- 2、如果是用的 Chrome 浏览器，需要科学上网，否则打不开谷歌商店，也就没办法在线安装插件

### 4.1、如何查看 Ollama 服务是否开启？

看到这个 Ollama 的任务栏图标即表示服务已开启。

![](attachments/b1a511d11ad87802.png)

### 4.2、如何开启 Ollama 服务？

非常简单，任务栏的搜索框里面输入【Ollama】——》找到 Ollama 应用，直接单机即可

![](attachments/2ae1999579d56176.png)

以上就是本期所有啦，

基本上能看到这里的都是人中龙凤！

如果觉得不错，随手点个赞、在看、转发三连吧！

谢谢你耐心看完我的文章~![](attachments/ba49e27fb394ea68.png)![](attachments/ba49e27fb394ea68.png)![](attachments/ba49e27fb394ea68.png)
