---
title: 满血版671b DeepSeek【一键部署】！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/满血版671b DeepSeek【一键部署】！ 2.md
tags: [evernote, impression, yinxiang]
---

# 满血版671b DeepSeek【一键部署】！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkwMzE4NjU5NA==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247505723&idx=1&sn=d374241a42500e904461aba8abf50bd4&chksm=c1ef4809f181b2acc22a18321c7d751554d2f57c5696229d1072b47831ae1c2722d7f69158c5&scene=90&xtrack=1&sessionid=1738928730&subscene=93&clicktime=1738929952&enterid=1738929952&flutter_pos=1&biz_enter_id=4&ranksessionid=1738928436&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQoMF+rmYId//2RSYR2HkKWhLWAQIE97dBBAEAAAAAAN3pAnmGBPMAAAAOpnltbLcz9gKNyK89dVj0JCGbArxZzaixRvKR0SXi+IdsqYMSgmtd0RSP1DSNiUS7zic3EwBhU09RXdcsAn8sIWK5w9YfpnUwbus7ZRohaOPL1TnP2aXf1J8Iv4BAPrwUXZwoyKAsUyp8CqJaSDlw5Ald+mRJIt73MNRUHHqrDTOH+rFxTVv2x59K3RdsWBf8LQX+m4kb09rIr1Z3pjS6KqM/fwbgnItlW/ftruYDiCgyesH8KhYDkBjMUw48n3E=&pass_ticket=xSF9Zeum7ZE5uhin+xtvvDlhDrnUVBfTpyvZyE0yrUuNywaL9zRZtso0/sp1tswo&wx_header=3)

原创 袋鼠帝 袋鼠帝AI客栈

大家好，我是袋鼠帝，事情的起因是这样的，昨天晚上11.30，我正想出去吃个宵夜。微信上有个朋友突然找我，**问我能不能私有化部署deepseek满血版！**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/F54C3908-9486-4CAC-BA6F-93994E6C0B61.png)

我那一秒是懵的，还特意确认了一下是不是**deepseek 671b**那个版本。

说实话我还真不知道，，，也没有想过。

不过最近DeepSeek确实非常火爆，**官方app、网页动不动就服务繁忙，，，**

用的非常恼火

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/0CCAA428-A5FF-4297-ABA8-18B25443966D.png)

API平台虽然开放了，but**暂停充值了**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/E99BE763-B74E-4C4F-AC6F-17C696F95719.png)

*充值不了deepseek官方API也没关系，可以到这个高速AI\_API中转站看看（同样支持R1和V3）*

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

**KG高速AI\_API中转站：**https://kg-api.cloud/

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

但偏偏人家deepseek不差钱，一心搞技术（深度求索嘛），**面对着泼天的流量根本没有想扩容的意思。**

所以这就**给了大家"分肉吃"的机会~**

比如前几天**硅基流动**就**单独部署了一套满血版671b的deepseek**（包含R1和V3）

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/005753C8-2FBF-4CFB-8B59-8D0AC9832F54.png)

不过据说还是会卡，这流量硅基流动帮deepseek吃，也消化不掉呀。

**所以现在如果私有化部署一套满血版的deepseek是一定能吃到这波流量的。**

在好奇心和利益的驱使下，我去**研究了一下如何私有化部署一套满血版的deepseek。**

结果，我发现**阿里云直接给大家喂到嘴里了。**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/3F43DC76-6A3A-461B-AFC7-22CBD3238532.png)

接下来我就带着大家操作操作~

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/B0C72ECC-8E93-49B7-880F-FB12E74CB7D8.png)

一键部署满血版DeepSeek

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/B0C72ECC-8E93-49B7-880F-FB12E74CB7D8.png)

阿里云的**Model Gallery**支持一键部署671b参数的满血版DeepSeek

首先我们要**开通 阿里云的人工智能平台PAI**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

地址：https://pai.console.aliyun.com/?regionId=cn-shanghai&spm=a2c4g.11186623.0.0.2e35abf3ZgYVRQ#/workspace

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

进去之后实名认证，点击**一键授权**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/62ED9FA9-C89A-4629-ADA8-55A3932E15CE.png)

跳转之后同意授权

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/F8158A3B-0432-4FF1-9716-120D977257CB.png)

同意授权之后会跳转回刚刚页面，进入第二步（**开通服务**），点击**一键开通**即可。

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/D0A46E6C-555F-4A8B-97F8-91E53FE662BC.png)

**一键开通之前，要确保阿里云账号里面有余额**，否则会开通失败

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/486D1293-CE01-4367-9E93-CFA4C7E51FE3.png)

查询余额可以 把鼠标移动到右上角，点击**基本资料**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/07904F3B-2ED6-4501-9250-C9DE4F001F04.png)

点击**资金账户**就能看到自己的余额了，余额不足可以充值1块钱。

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/3835C6D8-168A-42FE-86D3-9CF06C7C275E.png)

有余额的话正常来说就能开通成功，成功之后会跳到PAI平台，我们点击左边导航栏中的**Model Gallery**，**就能看到DeepSeek的满血版模型了**（R1和V3）

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/18559C62-E5AA-4FCE-85BC-5DD797A8B8FC.png)

点击**DeepSeek-R1**右下角的**部署按钮**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/D9696FB5-A86C-4B3C-854E-6FE275FA0104.png)

好了，到最后一步了，点击左下角部署按钮就能一键部署啦。。。

**不过我是不敢尝试了，****这316/一小时我遭不住，，，**

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/6C2CB38D-590B-4FB1-863D-36C7889D49B9.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/0D842A0B-995B-4074-BB91-EC754E836DF0.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/099EAA5C-9F61-4545-B3F8-33920F9B9AF6.png)

配置是真的豪华

**CPU**：190 个虚拟 CPU 核心。

**内存**：970 GB。

**GPU**：8 个 GU120 GPU。

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/A1D62E6B-AF3F-4CFD-8A42-78D0DD24188A.png)

好了，方案给大家了，你们自己看着办。

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

阿里云官方文档：https://help.aliyun.com/zh/pai/user-guide/one-click-deployment-deepseek-v3-model

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/5AFA7599-3CAC-44E0-A50F-D72D1F9E6081.png)

有钱的老板可以试试水。

当然**如果你能保证部署之后覆盖成本的同时还赚钱**，那你也可以试试~

如果有部署过的朋友欢迎评论区分享~

如果是你，你会部署吗， 欢迎评论区讨论

********以上就是本期所有啦，能看到这里的都是凤毛麟角的存在！********

********如果觉得不错，随手点个赞、在看、转发三连吧~********

********如果想第一时间收到推送，也可以给我个星标⭐********

********谢谢你耐心看完我的文章~********

********星球有DeepSeek接入微信的详细教程（全新方案，更稳定）********

********![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/204D42BB-84FC-480A-A083-C11AAD4A5534.jpg)********

********![](.evernote-content/90623E2C-E82D-4567-96BB-5B7BBA477611/1FD484BF-E3E8-4848-ABF1-414A968F2E32.gif)********

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247505723&idx=1&sn=d374241a42500e904461aba8abf50bd4&chksm=c1ef4809f181b2acc22a18321c7d751554d2f57c5696229d1072b47831ae1c2722d7f69158c5&scene=90&xtrack=1&sessionid=1738928730&subscene=93&clicktime=1738929952&enterid=1738929952&flutter_pos=1&biz_enter_id=4&ranksessionid=1738928436&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQoMF+rmYId//2RSYR2HkKWhLWAQIE97dBBAEAAAAAAN3pAnmGBPMAAAAOpnltbLcz9gKNyK89dVj0JCGbArxZzaixRvKR0SXi+IdsqYMSgmtd0RSP1DSNiUS7zic3EwBhU09RXdcsAn8sIWK5w9YfpnUwbus7ZRohaOPL1TnP2aXf1J8Iv4BAPrwUXZwoyKAsUyp8CqJaSDlw5Ald+mRJIt73MNRUHHqrDTOH+rFxTVv2x59K3RdsWBf8LQX+m4kb09rIr1Z3pjS6KqM/fwbgnItlW/ftruYDiCgyesH8KhYDkBjMUw48n3E=&pass_ticket=xSF9Zeum7ZE5uhin+xtvvDlhDrnUVBfTpyvZyE0yrUuNywaL9zRZtso0/sp1tswo&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8676944f-a304-4b58-8f4f-be4f254ce566/8676944f-a304-4b58-8f4f-be4f254ce566/)
