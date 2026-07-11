# 最懂Claude的人，是这样理解提示词的

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzI2MTI4NTYxMA==&mid=224750...](https://mp.weixin.qq.com/s?__biz=MzI2MTI4NTYxMA==&mid=2247506187&idx=1&sn=eaafeea1267a2ab572644d77c329b546&chksm=ea5e2a8edd29a3985c0d191c4f320bef5a66356115f716611af64b81140cc006272217706131&exptype=servicebox_7458314898044104704&subscene=0&scene=288&clicktime=1778200848&enterid=1778200848&flutter_pos=1&biz_enter_id=5&ascene=56&devicetype=iOS26.4.2&version=18004921&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0EWXQP2k5TzRXsTQNCTxVxLVAQIE97dBBAEAAAAAABiwAVQ93Q4AAAAOpnltbLcz9gKNyK89dVj0cNHUUc02wUUjJYUr1fFsNgkmqb5BgkTo5LmLDW3ZdJu0bCFFfmlP3WJLEnrqZBvTIg/mRV5KREsRSyuujGZQqp5vzDadNejbyj8NJPlw1jZYuncq0t4orMCAfCPozSUObZFh2f3Z+euAMgqb9xJKzNbz0VQxpI+3RtR4DhNXYfHOsyhKOKz410XK9vIsNy7jZ7DMmUrjKDCW01tIUYRSEgpsb0AkxHXizOBDUA2V6w==&pass_ticket=+EP17rKIrwfFn5IlZN0Itdsu0cGaie+Jzq6BMnMxrbAQkgIhoN0FMvn4lrbgL0P1&wx_header=3)

![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/97DEE18E-F127-4718-90A8-FCA5DD622D18.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/0D7B6A01-7944-4AE7-9FC9-60DE45E6DDD2.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/9F6F8943-EAD2-4E28-BA85-9D688BE2B0E6.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/C9FEA4CA-EB98-498A-B4CC-062EAB4231B4.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/AFE5600F-8DE7-4260-B983-E949E20373F6.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/D3E1F3CF-F896-4043-8745-6C89C4C0C2A9.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/C2F92AA6-1219-40D8-A963-CB6E72CF6C2D.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/63583576-C5CA-4D6F-A071-2A456E040C91.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/A6C960BC-EE33-45FB-8EF2-ADC56644FC74.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/BDBC3B4E-4A11-41F1-8E2C-3579FA406D02.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/9400759E-6F18-437B-A361-D7B705F51E93.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/90F93770-6102-4E29-A257-1949ED1EBCFB.jpg)![](.evernote-content/DA1EBFDE-CDC0-4A7C-AAE1-455533E1D095/1C575DD7-48DF-4574-A7E1-57068F1D7D05.jpg)

如果你想真正搞懂提示词工程是怎么回事，非常推荐你去听听Anthropic内部的这次圆桌讨论。

主持人Alex Albert，开发者关系负责人，前提示词工程师。

参与讨论的三个人，每个人都站在完全不同的视角：Amanda Askell负责微调团队，哲学背景，专门研究怎么让Claude变得诚实；David Hershey服务企业客户，天天帮人解决模型落地的实际问题；Zach Whitten是资深提示词工程师，关注普通用户怎么更好地用AI。

这场对话不是教你什么速成技巧，而是从根本上回答了一个问题：提示词工程到底是什么，为什么它值得被认真对待。

如果你觉得提示词工程就是往对话框里打几个字，那你可能错过了最重要的东西。

四个人坐在一起，第一个问题就很直接：什么是Prompt工程？为什么叫“工程”？

#AI#AI提示词#英文播客#提示词工程#提示词技巧

Close

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzI2MTI4NTYxMA==&mid=2247506187&idx=1&sn=eaafeea1267a2ab572644d77c329b546&chksm=ea5e2a8edd29a3985c0d191c4f320bef5a66356115f716611af64b81140cc006272217706131&exptype=servicebox_7458314898044104704&subscene=0&scene=288&clicktime=1778200848&enterid=1778200848&flutter_pos=1&biz_enter_id=5&ascene=56&devicetype=iOS26.4.2&version=18004921&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ0EWXQP2k5TzRXsTQNCTxVxLVAQIE97dBBAEAAAAAABiwAVQ93Q4AAAAOpnltbLcz9gKNyK89dVj0cNHUUc02wUUjJYUr1fFsNgkmqb5BgkTo5LmLDW3ZdJu0bCFFfmlP3WJLEnrqZBvTIg/mRV5KREsRSyuujGZQqp5vzDadNejbyj8NJPlw1jZYuncq0t4orMCAfCPozSUObZFh2f3Z+euAMgqb9xJKzNbz0VQxpI+3RtR4DhNXYfHOsyhKOKz410XK9vIsNy7jZ7DMmUrjKDCW01tIUYRSEgpsb0AkxHXizOBDUA2V6w==&pass_ticket=+EP17rKIrwfFn5IlZN0Itdsu0cGaie+Jzq6BMnMxrbAQkgIhoN0FMvn4lrbgL0P1&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/32d4eee9-e394-458b-b930-3047a3974d2f/32d4eee9-e394-458b-b930-3047a3974d2f/)