# Fable 5已近妖！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzIzMzQyMzUzNw==&mid=224751...](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518638&idx=1&sn=139d633b073f0ef4acc5b56f198a341b&chksm=e9c419a3e32d86d8441195bf620307cd3e88ec97d93330f589f3d88dfbcd85df4fcbb2d7c329&scene=90&xtrack=1&req_id=1783265481187771&sessionid=1783265507&subscene=93&clicktime=1783265511&enterid=1783265511&flutter_pos=0&biz_enter_id=4&ranksessionid=1783265481&jumppath=1001_1783265502848,1102_1783265504412,1001_1783265506005,1104_1783265508345&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b34&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQq2EwvWnEy3jvUKrSswb3oBLTAQIE97dBBAEAAAAAAAQON41d0qMAAAAOpnltbLcz9gKNyK89dVj0ZkKUKlbYpPfGT6g/rvtS7ZXt4ggCxIS50WiOVj128yZa0LonwM2c2k0UZ1YSn52DbSZkG5EItA+TzMFF4zV8CVWAG0LCQt1jPfmTb77vNkakZFYtVnzyXY/ZlQOUvk1PZ2kx8vcLHH3bKyUT85qSrtf/qgNwv3HnH6DokiALYWdVObKsthADDWZpeSAd/1kGiB/pnHHbPSSJ1u65DpyGeSLayLtVbT3gO5nujYE=&pass_ticket=x0x6nukZRwdHvfA8LTtVZgRc2umPGnoN2Q8AbMLYcRzvwApYG38/COQZSpC9rR2o&wx_header=3)

Original字节笔记本字节笔记本

如果说以前的 AI 编程，还是人类在 Human in loop ，一点点指挥、纠偏、验收，那么现在的 Fable5，已经是暴力编程了。

今天我让 ChatGPT 用图片的形式生成了一份页面设计稿，接着又把里面的页面元素提取出来，做成一套图片素材包。

![](.evernote-content/4A208D05-5144-4A73-9BBB-3FAF43FDAFB3/20617ED3-C6B5-4341-8CBD-4FF42DD3F5DE.png)

想着最好是能直接把每个素材单独切出来，透明底 PNG，打包下载，发现完全不行。

后来直接转到 Fable5，我原本以为，它大概率会写一个简单脚本，跑一遍图片裁切就结束了，没想到整个过程越看越离谱。

Fable5 先用 Python 跑了一遍图片识别算法，测试切割结果，把结果输出到本地。接着，它又把这套 Python 算法转成了 TS，直接做成了一个完整可用的网页工具。

这个网页还不是一个临时 demo。它有参数阈值调整，有图形范围选择，有单个素材预览，也有批量打包下载，甚至连国际化和移动端适配都一起做好了。

![](.evernote-content/4A208D05-5144-4A73-9BBB-3FAF43FDAFB3/224FDE70-4380-4B60-A9E2-587021466736.png)

我后来点进页面细看，才发现每个元素组件还自动分析出了颜色层级变化，点击就能复制色值。而这些功能，我从头到尾一个字都没有提过。

![](.evernote-content/4A208D05-5144-4A73-9BBB-3FAF43FDAFB3/CCFE8380-E5EF-4B39-A207-E3233DA58CC0.png)

这就很恐怖了。

以前我们说 AI 编程，更多还是你说一步，它做一步，但 Fable5 现在给人的感觉是，它会自己理解这个任务真正要变成什么产品，然后顺手把周边能力也补齐。

本来你只是想要一把刀，它直接给你搭了一个工作台。

用了这几天，我发现，Fable5 已近妖！

[用 Fable 5 把小盆友的英语课本变成点读机](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518592&idx=1&sn=0cfdbe281175d09819344f03809aa334&scene=21#wechat_redirect)

（这次做出来的工具地址，后续如果你有相同的需求，可以直接使用。）

https://pixup.bytenote.net

[Token腰斩，性能狂飙！神级插件Superpowers 6由Fable 5重构](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518630&idx=1&sn=19cbff8dbba7535b4e38340607940113&scene=21#wechat_redirect)

[我目前使用的两套远程Vibe Coding的方案](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518611&idx=1&sn=08857091b5996c8e27bc516e7920d85e&scene=21#wechat_redirect)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247518638&idx=1&sn=139d633b073f0ef4acc5b56f198a341b&chksm=e9c419a3e32d86d8441195bf620307cd3e88ec97d93330f589f3d88dfbcd85df4fcbb2d7c329&scene=90&xtrack=1&req_id=1783265481187771&sessionid=1783265507&subscene=93&clicktime=1783265511&enterid=1783265511&flutter_pos=0&biz_enter_id=4&ranksessionid=1783265481&jumppath=1001_1783265502848,1102_1783265504412,1001_1783265506005,1104_1783265508345&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b34&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQq2EwvWnEy3jvUKrSswb3oBLTAQIE97dBBAEAAAAAAAQON41d0qMAAAAOpnltbLcz9gKNyK89dVj0ZkKUKlbYpPfGT6g/rvtS7ZXt4ggCxIS50WiOVj128yZa0LonwM2c2k0UZ1YSn52DbSZkG5EItA+TzMFF4zV8CVWAG0LCQt1jPfmTb77vNkakZFYtVnzyXY/ZlQOUvk1PZ2kx8vcLHH3bKyUT85qSrtf/qgNwv3HnH6DokiALYWdVObKsthADDWZpeSAd/1kGiB/pnHHbPSSJ1u65DpyGeSLayLtVbT3gO5nujYE=&pass_ticket=x0x6nukZRwdHvfA8LTtVZgRc2umPGnoN2Q8AbMLYcRzvwApYG38/COQZSpC9rR2o&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2f8b1772-0635-4fb4-97c7-faf2a0df107f/2f8b1772-0635-4fb4-97c7-faf2a0df107f/)