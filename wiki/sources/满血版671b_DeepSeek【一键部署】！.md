---
title: 满血版671b DeepSeek【一键部署】！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/满血版671b DeepSeek【一键部署】！.html
tags: [AI技术]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "满血版671b DeepSeek【一键部署】！"
source: evernote
type: note
export_date: 2026-06-27
guid: 8676944f-a304-4b58-8f4f-be4f254ce566
---

# 满血版671b DeepSeek【一键部署】！

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkwMzE4NjU5NA==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247505723&idx=1&sn=d374241a42500e904461aba8abf50bd4&chksm=c1ef4809f181b2acc22a18321c7d751554d2f57c5696229d1072b47831ae1c2722d7f69158c5&scene=90&xtrack=1&sessionid=1738928730&subscene=93&clicktime=1738929952&enterid=1738929952&flutter_pos=1&biz_enter_id=4&ranksessionid=1738928436&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQoMF+rmYId//2RSYR2HkKWhLWAQIE97dBBAEAAAAAAN3pAnmGBPMAAAAOpnltbLcz9gKNyK89dVj0JCGbArxZzaixRvKR0SXi+IdsqYMSgmtd0RSP1DSNiUS7zic3EwBhU09RXdcsAn8sIWK5w9YfpnUwbus7ZRohaOPL1TnP2aXf1J8Iv4BAPrwUXZwoyKAsUyp8CqJaSDlw5Ald+mRJIt73MNRUHHqrDTOH+rFxTVv2x59K3RdsWBf8LQX+m4kb09rIr1Z3pjS6KqM/fwbgnItlW/ftruYDiCgyesH8KhYDkBjMUw48n3E=&pass_ticket=xSF9Zeum7ZE5uhin+xtvvDlhDrnUVBfTpyvZyE0yrUuNywaL9zRZtso0/sp1tswo&wx_header=3)

原创 袋鼠帝 袋鼠帝AI客栈

大家好，我是袋鼠帝，事情的起因是这样的，昨天晚上11.30，我正想出去吃个宵夜。微信上有个朋友突然找我，**问我能不能私有化部署deepseek满血版！**

![](attachments/c70ae0962cacdf3b.png)

我那一秒是懵的，还特意确认了一下是不是**deepseek 671b**那个版本。

说实话我还真不知道，，，也没有想过。

不过最近DeepSeek确实非常火爆，**官方app、网页动不动就服务繁忙，，，**

用的非常恼火

![](attachments/181208c7a0eabeff.png)

API平台虽然开放了，but**暂停充值了**

![](attachments/e43805cd3df50640.png)

*充值不了deepseek官方API也没关系，可以到这个高速AI\_API中转站看看（同样支持R1和V3）*

![](attachments/6831f956d2d426aa.png)

![](attachments/6831f956d2d426aa.png)

**KG高速AI\_API中转站：**https://kg-api.cloud/

![](attachments/6831f956d2d426aa.png)

![](attachments/6831f956d2d426aa.png)

但偏偏人家deepseek不差钱，一心搞技术（深度求索嘛），**面对着泼天的流量根本没有想扩容的意思。**

所以这就**给了大家"分肉吃"的机会~**

比如前几天**硅基流动**就**单独部署了一套满血版671b的deepseek**（包含R1和V3）

![](attachments/828568da9426deb7.png)

不过据说还是会卡，这流量硅基流动帮deepseek吃，也消化不掉呀。

**所以现在如果私有化部署一套满血版的deepseek是一定能吃到这波流量的。**

在好奇心和利益的驱使下，我去**研究了一下如何私有化部署一套满血版的deepseek。**

结果，我发现**阿里云直接给大家喂到嘴里了。**

![](attachments/251bc2b2276430fb.png)

接下来我就带着大家操作操作~

![](attachments/0ec84596510133a5.png)

一键部署满血版DeepSeek

![](attachments/0ec84596510133a5.png)

阿里云的**Model Gallery**支持一键部署671b参数的满血版DeepSeek

首先我们要**开通 阿里云的人工智能平台PAI**

![](attachments/6831f956d2d426aa.png)

![](attachments/6831f956d2d426aa.png)

地址：https://pai.console.aliyun.com/?regionId=cn-shanghai&spm=a2c4g.11186623.0.0.2e35abf3ZgYVRQ#/workspace

![](attachments/6831f956d2d426aa.png)

![](attachments/6831f956d2d426aa.png)

进去之后实名认证，点击**一键授权**

![](attachments/b98483bc0e1aa7ec.png)

跳转之后同意授权

![](attachments/5cbbc6cc37a83271.png)

同意授权之后会跳转回刚刚页面，进入第二步（**开通服务**），点击**一键开通**即可。

![](attachments/24df9153907f6329.png)

**一键开通之前，要确保阿里云账号里面有余额**，否则会开通失败

![](attachments/cc9ba3aea44ca03e.png)

查询余额可以 把鼠标移动到右上角，点击**基本资料**

![](attachments/78d3f15bdb7dd35f.png)

点击**资金账户**就能看到自己的余额了，余额不足可以充值1块钱。

![](attachments/8cf08d0119d68ee2.png)

有余额的话正常来说就能开通成功，成功之后会跳到PAI平台，我们点击左边导航栏中的**Model Gallery**，**就能看到DeepSeek的满血版模型了**（R1和V3）

![](attachments/e89bf9173846b709.png)

点击**DeepSeek-R1**右下角的**部署按钮**

![](attachments/1b9b83bf007c041d.png)

好了，到最后一步了，点击左下角部署按钮就能一键部署啦。。。

**不过我是不敢尝试了，****这316/一小时我遭不住，，，**

![](attachments/44e31085aeb14ed5.png)

![](attachments/bfae6707d7f0ccb4.png)

![](attachments/b799293236152650.png)

配置是真的豪华

**CPU**：190 个虚拟 CPU 核心。

**内存**：970 GB。

**GPU**：8 个 GU120 GPU。

![](attachments/932b35af2c9bc485.png)

好了，方案给大家了，你们自己看着办。

![](attachments/6831f956d2d426aa.png)

![](attachments/6831f956d2d426aa.png)

阿里云官方文档：https://help.aliyun.com/zh/pai/user-guide/one-click-deployment-deepseek-v3-model

![](attachments/6831f956d2d426aa.png)

![](attachments/6831f956d2d426aa.png)

有钱的老板可以试试水。

当然**如果你能保证部署之后覆盖成本的同时还赚钱**，那你也可以试试~

如果有部署过的朋友欢迎评论区分享~

如果是你，你会部署吗， 欢迎评论区讨论

********以上就是本期所有啦，能看到这里的都是凤毛麟角的存在！********

********如果觉得不错，随手点个赞、在看、转发三连吧~********

********如果想第一时间收到推送，也可以给我个星标⭐********

********谢谢你耐心看完我的文章~********

********星球有DeepSeek接入微信的详细教程（全新方案，更稳定）********

********![](attachments/63263d003402e010.jpg)********

********![](attachments/38b8da9d590b528b.gif)********
