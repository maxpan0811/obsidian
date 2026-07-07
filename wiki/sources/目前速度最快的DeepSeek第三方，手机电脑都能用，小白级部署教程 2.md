---
title: 目前速度最快的DeepSeek第三方，手机电脑都能用，小白级部署教程 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/目前速度最快的DeepSeek第三方，手机电脑都能用，小白级部署教程 2.md
tags: [evernote, impression, yinxiang]
---

# 目前速度最快的DeepSeek第三方，手机电脑都能用，小白级部署教程

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MjM5MTU0MzIwOA==&mid=245224...](https://mp.weixin.qq.com/s?__biz=MjM5MTU0MzIwOA==&mid=2452242889&idx=1&sn=b356d173de7f0b8f32741db9cb94ae6e&chksm=b01a14ebea487e147ee4d2ddef4a4bf281345664bbec859b5a7a47a99b190ede1dcffdd552fd&scene=90&xtrack=1&sessionid=1738568109&subscene=93&clicktime=1738568619&enterid=1738568619&flutter_pos=3&biz_enter_id=4&ranksessionid=1738568125&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ9qdLbvQK0e9oUfFVdbL4rBLWAQIE97dBBAEAAAAAAGXjJSnctmoAAAAOpnltbLcz9gKNyK89dVj0uuMIHFUXxYgr6M2VC/yvXJfhXYejCgMJTVNTP0JcP7u0tnDSZvYWbzKEWOQNm7VLJocewl5OreRgojlOfG9pX8IRM4MgjJUBAxjaz3LQZLSv781Un8Sx3iGyz0BeuF/NMxWJGdIt/XnevaLuQF3QFPLTTxTsmfqeZ1pjeipFBorSynmqwoL7Jm+5/xxeIMicO/oqNax9rARtMBerQ1NZAjPpie4hq3um3CF5k3QbUbw=&pass_ticket=oHyay+mX5vCx6L1IQig8Hmc3B5crqBSzwOw0fEHywr3Y2wQKyz12Le7jT/7NSUXn&wx_header=3)

原创 王抖抖  王抖抖

之前介绍了几个免费使用DeepSeek-R1的平台（文章见此：[满血版DeepSeek-R1五大平台白嫖攻略](https://mp.weixin.qq.com/s?__biz=MjM5MTU0MzIwOA==&mid=2452242857&idx=1&sn=a08c99aeb3ac1776c3a5bb99cc1567d9&scene=21#wechat_redirect)）。

有网友提醒说，“硅基流动”联合“华为云”刚刚上线的DeepSeek体验也很不错，虽然要收费但一定程度可以“白嫖”。下面就是具体教程：

---

**一、注册账号**

首先打开硅基流动主页：https://cloud.siliconflow.cn/models，点击右上方“Login”：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/D2F33C87-E8C8-46CE-837C-EB9D9E4CCD90.png)

在这个页面注册账号，手机收验证码（不用尝试其它登录方式，因为最后还是会问你要手机号）：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/3C678D7B-5AF6-4282-B64F-5C85CF74D785.png)

注册成功后进入对话界面，直接可以开始互动：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/6F65B1BE-F801-4E0B-9BC6-613F74BF2EB7.png)

如果没有进入对话界面，可点击左侧“模型广场”，然后点击DeepSeek-R1：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/5A70E72F-FCE6-46C9-B1C5-99DF9914B024.png)

选择“在线体验”即可进入对话界面：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/2F4571BB-FF9C-467C-BB5B-ACBBCF6DEF59.png)

你可以随时通过左边的下拉菜单切换其它模型（费用各不相同）：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/0027A431-C945-4304-A9D5-B014813F7ED7.png)

但是，通过“在线体验”对话，每次重新进入，内容就全部清除了。想保留历史对话，需要使用API。

---

**二、生成API KEY**

点击左边菜单的“API密钥”，再点击右边的“新建API密钥”：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/32639C27-9581-4B43-87A4-9EB98FFDA6FA.png)

这里可以填写描述，也可以不填，然后点击“新建密钥”：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/E90098F1-DB97-4F8F-836D-0DC7997FBDA3.png)

此时API密钥就建好了，可以将鼠标移到密钥上复制：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/4E2B7B10-F346-4ACB-BB7E-D7BACC181B08.png)

---

**三、安装Chatbox AI**

密钥怎么使用呢？最简单的方法是使用Chatbox AI这个工具，网址：https://chatboxai.app

该工具支持Windows、IOS、安卓（谷歌商店）、APK安装包：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/7CA81AD7-8BCE-4EBB-8C4B-F9C5D51D511D.png)

首先尝试Windows版，下载安装后初次启动会弹出这个界面，选择“使用自己的API Key或本地模型”：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/5B9FF93E-29DF-48E9-9C17-9215E7A7A1EA.png)

然后选择“SiliconFlow API”：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/B7DF301E-8EC1-4D26-A0A9-B3264D781090.png)

接下来，把刚才复制的密钥黏贴到“密钥”栏，并在下拉菜单中选择DeepSeek-R1：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/2ABE4A7C-3738-4B20-976C-5D3040231F34.png)

通过上方菜单可以设置其它参数，比如是否显示消息的Token数量：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/957D5A24-1F77-4896-9BF8-4159D158FA91.png)

是否自动生成聊天标题：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/C67D45FB-F747-43DB-8A2B-0962AEEA003B.png)

设置完成后“保存”就来到了聊天界面，可以通过左边“新对话”开启新互动，之前聊天记录会保留：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/83B0DB1D-1BBA-4776-8E2F-4CE08EF5C153.png)

遗憾的是，虽然Chatbox有联网和上传文件的选项，但使用的话，会提示API不支持。要实现联网功能，只能自己用浏览器插件，这里不多介绍。

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/E9D92A9C-3C83-4FC5-9359-AC348E092EF6.png)

手机端的安装如出一辙：首先在安卓商店或苹果商店找到Chatbox AI（认准图标别搞错了）：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/D1404358-1535-40A0-896E-17A74C988790.png)![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/A4AA902A-682B-4FDE-9DFC-8635FAC9994C.png)

以安卓为例，安装Chatbox AI之后，同样会弹出这个界面：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/2CC6A10A-30BB-4626-B12F-6696FAB32BB1.png)

接下来操作和Windows一样：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/F526C7C9-84B9-44C1-82D2-AACA8D08D8C4.png)

很快就可以使用了，反应速度比较快：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/6707B6E7-E6EB-44F6-98D0-3B1E5B989BF6.png)

无论你是在电脑还是手机上部署，今后都只需打开Chatbox AI，就可以使用DeepSeek。

---

**四、费用和“白嫖”**

到这里，有人可能会问，不是说可以“白嫖”吗？

在硅基流动官网，点击“余额充值”可以看到，官方给予注册就送14元余额的优惠：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/E19B3D0D-786D-4A9D-B5E7-8B4F61836A43.png)

这里我问了三个问题，消耗2798Token，花费0.0442元（AI深度思考的内容，也要耗费Token）：

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/7E900044-473E-4542-B438-91728B6B7444.png)

按此计算，**注册赠送的额度，基本可以互动1000次左右**，普通人足够用好几天。

注意，在线体验和通过API调用，都会同等消耗Token。

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/E5B0D330-448B-4A31-B8BD-27DCECF2B983.png)

**关键来了：目前硅基流动的规则是，邀请一名新用户，就可以获得14元余额，相当于又可以免费对话上千次。（点击菜单“我的邀请”可以看到选项）**

![](.evernote-content/93747437-6AE6-47E3-BB9C-8D1CBD783408/1BD61B07-26A3-4BA1-A1FB-16CA3226BC71.jpg)

**此外，因为是手机号注册，如果你有多个手机号，也可以邀请自己注册，你的两个号码都将获得14元余额（新账号需要重新生成API Key）！**

不过，如果你是重度用户，或者要通过API为其他人提供服务，还是实名认证并交钱吧！

---

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MjM5MTU0MzIwOA==&mid=2452242889&idx=1&sn=b356d173de7f0b8f32741db9cb94ae6e&chksm=b01a14ebea487e147ee4d2ddef4a4bf281345664bbec859b5a7a47a99b190ede1dcffdd552fd&scene=90&xtrack=1&sessionid=1738568109&subscene=93&clicktime=1738568619&enterid=1738568619&flutter_pos=3&biz_enter_id=4&ranksessionid=1738568125&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ9qdLbvQK0e9oUfFVdbL4rBLWAQIE97dBBAEAAAAAAGXjJSnctmoAAAAOpnltbLcz9gKNyK89dVj0uuMIHFUXxYgr6M2VC/yvXJfhXYejCgMJTVNTP0JcP7u0tnDSZvYWbzKEWOQNm7VLJocewl5OreRgojlOfG9pX8IRM4MgjJUBAxjaz3LQZLSv781Un8Sx3iGyz0BeuF/NMxWJGdIt/XnevaLuQF3QFPLTTxTsmfqeZ1pjeipFBorSynmqwoL7Jm+5/xxeIMicO/oqNax9rARtMBerQ1NZAjPpie4hq3um3CF5k3QbUbw=&pass_ticket=oHyay+mX5vCx6L1IQig8Hmc3B5crqBSzwOw0fEHywr3Y2wQKyz12Le7jT/7NSUXn&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/22a890c4-f25e-490c-b7f5-bca123fd7932/22a890c4-f25e-490c-b7f5-bca123fd7932/)
