# DeepSeek 本地部署后如何联网搜索，小白必看秘籍！

---

原文链接: [https://mp.weixin.qq.com/s?chksm=9f081971a87f90677b8e9832cd951d9...](https://mp.weixin.qq.com/s?chksm=9f081971a87f90677b8e9832cd951d9c903661f28d778678f5ee71abe2ce123731e1eded36e1&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_2&scene=169&mid=2247484622&sn=349ab4a818e8ae936530e929cbf42d2a&idx=1&__biz=MzA3MzgxMzIwMA==&sessionid=1738654840&subscene=200&clicktime=1738658007&enterid=1738658007&flutter_pos=48&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVX78C4O59oCW1BQrIto4MBLWAQIE97dBBAEAAAAAAOTrLnDmHp4AAAAOpnltbLcz9gKNyK89dVj0jQWIXBHSY2XZRY8UhJTydYJqI6w27bmOaRP+5DfvR4DVkVmqqs0e4wtB7ttSgXeKJA9Ho4csnDIrclE0qCDL+tip7qdMoqsiVhh38fvSWw28Euq+yOVKXNSEdEGeUKmRX7UO/Zp/R/RSYoPk1V8ZO4P5VAItoYKup7ZmVLdZCAjD4H4X61V524e2xl28KivSp+PsxXDFkCbZeijP3l6PBiP9NLUqqasjKtK4Tk34nSM=&pass_ticket=hdv9u80/6f7pvh17GIdzMK9ykEhOr787LKqgjWORmcM8dVw6dyjIsb3sSOdMJP1Y&wx_header=3)

原创阮小贰阮小贰

还不知道如何进行DeepSeek本地部署的童鞋赶紧去看看这篇文章：

[一篇文章带你搞定DeepSeek本地部署](https://mp.weixin.qq.com/s?__biz=MzA3MzgxMzIwMA==&mid=2247484521&idx=1&sn=863c6d016358b4165666dbc0037f77d1&scene=21#wechat_redirect)

下午刚发布完 DeepSeek 本地部署的文章之后，

看到评论区有兄弟问到了如何使用联网功能，

于是，晚饭都没吃就立马卷了起来，

经过一番折腾，终于搞定！

废话不多说，先来带大家看一看 DeepSeek 本地部署后联网的效果。

一、DeepSeek本地部署联网效果
------------------

这是没联网时的答案：

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/DAC89DC2-62D7-4CE2-8B32-B0E6CA466027.png)

这是联网后的答案：

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/6BC7C014-E19D-41C6-AE39-C470730647E8.png)

二、DeepSeek本地部署如何实现联网？
---------------------

OK，怎么实现的？

接下来，跟着我的思路一步一步来。

这里要给大家介绍一个浏览器插件：**Page Assist**

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/6D343CF6-56E9-483F-8DD7-88AAB9186C17.png)

这个插件有啥用?

看它的名字就知道了。

### 2.1、Page Assist插件官网介绍：

**Page Assist** 是一款开源浏览器扩展程序，可为您的本地 AI 模型提供侧边栏和 Web UI。它允许您从任何网页与您的模型进行交互。

* 1、本地 AI 模型的 Web UI，支持可视化交互操作（不用安装 Docker 环境，也不用安装 Python 环境）
* 2、支持联网搜索功能

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/6DF34DE6-D66C-4957-9DDC-BF468043D946.png)

Github 官网：https://github.com/n4ze3m/page-assist

### 2.2、Page Assist插件浏览器支持

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/56C21E41-2DE3-469F-9ECD-52C8231672E3.png)

安装方法，这里分为两种情况：

* 1、可以科学上网，推荐使用 Chrome 谷歌浏览器
* 2、无法进行科学上网，推荐使用 Firefox 火狐浏览器或者 Brave 浏览器

三、具体操作步骤
--------

这里只给介绍两种浏览器（**Chrome** 和 **Firefox**）的安装方式，其他的浏览器的插件安装方式都类似，

需要注意的是，**Edge** 浏览器目前我还没有找到这个在线插件。

3.1、Chrome 浏览器
--------------

1. 前提：自行解决科学上网（这里不做介绍，懂的都懂）
2. 打开谷歌应用商店：https://chromewebstore.google.com/
3. 输入【Page Assist】 搜索插件
4. 选择【Page Assist - 本地 AI 模型的 Web UI】
5. 点击【添加到 Chrome】即可，然后固定到 Chrome 浏览器的导航栏上（固不固定都可以）
6. 点击【Page Assist】插件即可打开 DeepSeek 的可视化界面
7. 右上角齿轮【设置】——》【RAG 设置】——》选择文本嵌入模型——》点击【保存】按钮即可

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/7910E420-0074-4BD1-A0DA-86510B94B691.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/1C1E1190-1754-4D26-AE9E-439FC26A31BA.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/13E06278-62E1-4104-8999-F14EE8FF7125.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/D077D3FE-6E86-42B0-9651-95F141DC1266.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/CC08F9DD-25F1-4A14-8AB6-C93A45E61B2D.png)

3.2、Firefox 浏览器
---------------

1. 不需要科学上网，同样是通过扩展打开，地址栏输入：about:addons
2. 输入【Page Assist】 搜索插件
3. 选择【Page Assist - A Web UI for Local AI Models】
4. 点击【添加】即可，然后固定到 Firefox 浏览器的导航栏上（固不固定都可以）
5. 点击【Page Assist】插件即可打开 DeepSeek 的可视化界面
6. 右上角齿轮【设置】——》【RAG 设置】——》选择文本嵌入模型——》点击【保存】按钮即可

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/C6FBF9F2-8A2A-4F39-9BC0-7389ABA3C5C3.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/CCE5204D-7C50-43B5-997D-FBFE932AD1C2.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/21593DAE-581B-49C2-B6BF-7ED74CE9BB13.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/2C872259-6ABC-4C14-8807-A4182DF92520.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/0C911B4F-5109-4AC4-97FC-9A732CC39A08.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/E015E206-39BE-4232-9C33-8CD088268441.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/F5235CDE-88F9-4AC1-BB82-BEE264E9000E.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/749ECA3A-186D-4182-86A2-BE4521BD9E2E.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/968A4260-1477-4CD7-9AC5-C961BCF11302.png)

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/CC08F9DD-25F1-4A14-8AB6-C93A45E61B2D.png)

四、注意事项
------

* 1、Ollama 服务必须启动起来。否则会报错
* 2、如果是用的 Chrome 浏览器，需要科学上网，否则打不开谷歌商店，也就没办法在线安装插件

### 4.1、如何查看 Ollama 服务是否开启？

看到这个 Ollama 的任务栏图标即表示服务已开启。

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/F34D6B87-59D5-41B4-84AF-E709F07D3D1C.png)

### 4.2、如何开启 Ollama 服务？

非常简单，任务栏的搜索框里面输入【Ollama】——》找到 Ollama 应用，直接单机即可

![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/29D22D86-1414-4C29-9747-5F0B7839F946.png)

以上就是本期所有啦，

基本上能看到这里的都是人中龙凤！

如果觉得不错，随手点个赞、在看、转发三连吧！

谢谢你耐心看完我的文章~![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/B5E5827C-20DF-4EDD-B40C-04F757DBD80D.png)![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/B5E5827C-20DF-4EDD-B40C-04F757DBD80D.png)![](.evernote-content/6030791F-C295-4568-AD4E-6EC6C0C61056/B5E5827C-20DF-4EDD-B40C-04F757DBD80D.png)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?chksm=9f081971a87f90677b8e9832cd951d9c903661f28d778678f5ee71abe2ce123731e1eded36e1&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738657625_2&scene=169&mid=2247484622&sn=349ab4a818e8ae936530e929cbf42d2a&idx=1&__biz=MzA3MzgxMzIwMA==&sessionid=1738654840&subscene=200&clicktime=1738658007&enterid=1738658007&flutter_pos=48&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVX78C4O59oCW1BQrIto4MBLWAQIE97dBBAEAAAAAAOTrLnDmHp4AAAAOpnltbLcz9gKNyK89dVj0jQWIXBHSY2XZRY8UhJTydYJqI6w27bmOaRP+5DfvR4DVkVmqqs0e4wtB7ttSgXeKJA9Ho4csnDIrclE0qCDL+tip7qdMoqsiVhh38fvSWw28Euq+yOVKXNSEdEGeUKmRX7UO/Zp/R/RSYoPk1V8ZO4P5VAItoYKup7ZmVLdZCAjD4H4X61V524e2xl28KivSp+PsxXDFkCbZeijP3l6PBiP9NLUqqasjKtK4Tk34nSM=&pass_ticket=hdv9u80/6f7pvh17GIdzMK9ykEhOr787LKqgjWORmcM8dVw6dyjIsb3sSOdMJP1Y&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/014ea5d9-8d84-4f5a-a434-945a56b0c61a/014ea5d9-8d84-4f5a-a434-945a56b0c61a/)