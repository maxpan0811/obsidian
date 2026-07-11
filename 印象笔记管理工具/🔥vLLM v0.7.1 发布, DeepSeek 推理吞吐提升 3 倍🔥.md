# 🔥vLLM v0.7.1 发布,  DeepSeek 推理吞吐提升 3 倍🔥

---

原文链接: [https://mp.weixin.qq.com/s?ranksessionid=1738510260\_4&chksm=...](https://mp.weixin.qq.com/s?ranksessionid=1738510260_4&chksm=cebb51abf9ccd8bd82a4fa028a365855b61e61e3a698326465b77a3d1687e743a67477c598ca&exptype=masonry_feed_brief_content_elite_for_feeds_u2i&scene=169&mid=2247532378&subscene=200&sn=382741ff9d9381bab22d891fbe4927ae&idx=1&__biz=Mzg2NzU4MDgzMA==&sessionid=1738509696&clicktime=1738545870&enterid=1738545870&flutter_pos=43&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzN0uU2t3HD0ybNL/0VBQiRLWAQIE97dBBAEAAAAAAKwmDY41y1AAAAAOpnltbLcz9gKNyK89dVj0uDzPueSuj3QNdvCIJ3Ob4YV9E5I4gqEWBGF8zcNPTgQT4d/4JR3j1tT0L5NgBsbqhheQi1ZWjdNFBfCRQ/A+MYdZpMGMilTl+pK0EwF/3hFQfs/uRszP1h0y9Iu6PLtniXZ+g3Pdtg/RzDb+7yzVRlVgit96O1ycsCUNvKb/6xRH0rWBlVXgp+m1hYcthGu/mVkGCwddtQglqVB5M+XYhePQumwQLtk6IiLXG6DO/p8=&pass_ticket=fJo+CoXriYWu0WuBmZUV/a7LB5mhn+cm4rE0Dwe8fiK4hcOEdGeHi74p5WiVFuEi&wx_header=3)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/C915C104-D518-4386-A5C6-5C1991D10DEE.jpg)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/4B74BB4F-FEE3-4BB6-9145-99D1DD13EAFA.png)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/ABD9E856-2AB0-4655-9893-22FFC1BC31C1.png)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/04FA2EA9-5E76-44ED-8A4D-4851D338A903.png)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/F46FCF08-708F-46B7-B41B-542547368F52.png)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/115B88BB-FF8D-4518-9570-4D0097DCBAF5.png)

![](.evernote-content/ED928F5F-24D2-48D0-8AC5-79B96B8C3ABF/8F2767EC-A8E5-4833-9A53-2EAE4F2E6E16.png)

vLLM 团队发布针对 DeepSeek 优化的 1st batch 版本 v0.7.1，开始使用 MLA and cutlass fp8 kernels，相比 v0.7.0：  
  
🔥 3x the generation throughput  
🔥 ~10x the memory capacity for tokens  
🔥 horizontal context scalability with pipeline parallelism

关闭

名称已清空

喜欢作者其它金额

文章

暂无文章

返回

**其它金额**

赞赏金额

¥

最低赞赏 ¥0

1

2

3

4

5

6

7

8

9

0

.

AI 资讯,1

,

2025年02月02日 03:22,,湖南

---

[🌐 原始链接](https://mp.weixin.qq.com/s?ranksessionid=1738510260_4&chksm=cebb51abf9ccd8bd82a4fa028a365855b61e61e3a698326465b77a3d1687e743a67477c598ca&exptype=masonry_feed_brief_content_elite_for_feeds_u2i&scene=169&mid=2247532378&subscene=200&sn=382741ff9d9381bab22d891fbe4927ae&idx=1&__biz=Mzg2NzU4MDgzMA==&sessionid=1738509696&clicktime=1738545870&enterid=1738545870&flutter_pos=43&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQzN0uU2t3HD0ybNL/0VBQiRLWAQIE97dBBAEAAAAAAKwmDY41y1AAAAAOpnltbLcz9gKNyK89dVj0uDzPueSuj3QNdvCIJ3Ob4YV9E5I4gqEWBGF8zcNPTgQT4d/4JR3j1tT0L5NgBsbqhheQi1ZWjdNFBfCRQ/A+MYdZpMGMilTl+pK0EwF/3hFQfs/uRszP1h0y9Iu6PLtniXZ+g3Pdtg/RzDb+7yzVRlVgit96O1ycsCUNvKb/6xRH0rWBlVXgp+m1hYcthGu/mVkGCwddtQglqVB5M+XYhePQumwQLtk6IiLXG6DO/p8=&pass_ticket=fJo+CoXriYWu0WuBmZUV/a7LB5mhn+cm4rE0Dwe8fiK4hcOEdGeHi74p5WiVFuEi&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e7fee346-0353-4431-a07e-7138032f9209/e7fee346-0353-4431-a07e-7138032f9209/)