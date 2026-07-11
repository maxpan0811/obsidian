# 从头教你用制作 Workflow 万能扫码 | Matrix 精选 - 少数派

---

从头教你用制作 Workflow 万能扫码 | Matrix 精选
=================================

[森二](http://matrix.sspai.com/user/735919)

1小时前

**
[iOS](http://sspai.com/tag/iOS)

[**
5](http://sspai.com/37132#list-comment)

**
3

![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/52384FEF-B1BD-42F3-BF48-0AACDA047402.jpg)

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/0D6E35AD-2785-4100-8CCC-BBE0870D9F01.png)](http://sspai.com/attachment/origin/2016/08/15/342459.png?origin)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章对标题和排版略作修改，[原文链接](http://matrix.sspai.com/p/dd283600)。

---

引子
--

「二维码真是越来越多了」一如既往我拿起手机准备 3D touch 微博的 ICON 扫码登录，突然觉得这个动作似曾相识，好像我如此重复的时候还有很多，比如：

* 电脑逛淘宝想用手机接着看的时候我要用手机淘宝扫一下
* 偶尔登一下万年不用的 QQ 邮箱时我要用手机 QQ 扫一下
* 我要做书籍记录的时候我要点开豆瓣扫一下
* 支付宝、微信支付的时候我要扫一下
* 电脑上用微信登录的时候我要扫一下
* ……

天哪，这实在太麻烦了，我要做一个 [Workflow](http://sspai.com/tag/workflow) 完成所有的扫码动作。

多合一
---

我想把所有要扫码的地方全部用一个扫码界面代替。目前实现了如下功能：

1. 扫描二维码登录淘宝、微博、微信、支付宝、京东
2. 扫描电脑版淘宝页面二维码跳转到手机淘宝相关页面
3. 扫描电脑版京东页面二维码跳转到手机淘宝相关页面
4. 扫描书籍 ISBN 码跳转到手机豆瓣相关页面
5. 微信扫码支付、加好友等
6. 支付宝扫码支付、加好友等
7. 如果既不是网页也不是 ISBN 码那就复制到剪贴板（万一你对象给你写了悄悄话藏在二维码里呢٩( ᐖ )و

淘宝、支付宝、豆瓣可以直达二维码链接界面。但是微博、微信需要跳转到本身的扫码界面二次扫码。虽说是二次扫码，但是也是极快的。具体原理可以参考微信的一篇文章。[微信扫码为啥那么快？](http://www.tuicool.com/articles/bQbQrqR)

也可以通过两张动图对比一下。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/8B6ED2F5-20DE-4FF7-87FD-66F6D0FF67BF.gif)](https://ww1.sinaimg.cn/large/006tNc79gw1fbu0cy2wchg30800e8qv7.gif)

 微信登陆（二次扫码）

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/FB994B57-873D-4A18-B918-0230D51D1BE4.gif)](https://ww1.sinaimg.cn/large/006tNc79gw1fbu0jg8epxg30800e8u0z.gif)

淘宝登陆（扫码直达）

实现原理
----

实现这个 Workflow 的原理主要基于 URL SCHEME 的应用和豆瓣 API 的调用。

#### 1. 首先获取各个 App 的 URL SCHEME

这些信息部分网上都可以搜到。

* 淘宝：`taobao://`
* 微博：`weibo://qrcode`
* 微信：`weixin://scanqrcode`
* 支付宝：`alipayqr://platformapi/startapp?saId=10000007`
* 豆瓣：`douban://`
* 京东：`openApp.jdMobile://virtual?params={参数}`

#### 2. 研究调用机制

示例中分为一次扫码是如何实现的呢？一次扫码像是淘宝、支付宝和豆瓣，App 本身就支持从链接跳转到 App 中制定页面，但是如何获取这个「链接」就是关键了。以情况不复杂的支付宝扫码举例。复杂的情况类似于京东需要抓包分析，本文不涉及。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/4C73042C-AF0A-4B32-BD08-80A0B5B3DD22.jpg)](https://ww1.sinaimg.cn/large/006tKfTcgy1fbw82eklhaj31kw141nne.jpg)

这个二维码包含了一个网页：`https://qr.alipay.com/a6x00588utz0thcokf77vv7d`然后我试着直接打开看看。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/B0E77D2A-411D-4F7A-AB9C-C9A58FEFBC8C.jpg)](https://ww2.sinaimg.cn/large/006tKfTcgy1fbw8c0dzfkj31kw141dxz.jpg)

这是一个新的网址，有没有觉得有点眼熟？

```
https://ds.alipay.com/?from=mobilecodec&scheme=alipays%3A%2F%2Fplatformapi%2Fstartapp%3FsaId%3D10000007%26clientVersion%3D3.7.0.0718%26qrcode%3Dhttps%253A%252F%252Fqr.alipay.com%252Fa6x00588utz0thcofk77v7d%253F_s%253Dweb-other
```

这个 URL 经过了编码，首先来解码。

```
https://ds.alipay.com/?from=mobilecodec&scheme=alipays://platformapi/startapp?saId=10000007&clientVersion=3.7.0.0718&qrcode=https://qr.alipay.com/a6x00588utz0thcofk77v7d?_s=web-other
```

将其分段便于理解。

```
https://ds.alipay.com/?from=mobilecodec
&scheme=alipays://platformapi/startapp?saId=10000007
&clientVersion=3.7.0.0718
&qrcode=https://qr.alipay.com/a6x00588utz0thcofk77v7d?_s=web-other
```

从上至下一眼便知，第二行是支付宝客户端的 URL SCHEME，第四行是刚刚二维码内含的网页。把第二行和第四行结合起来去跑一下看看：

```
alipays://platformapi/startapp?saId=10000007&qrcode=https://qr.alipay.com/a6x00588utz0thcofk77v7d?_s=web-other
```

果然成功了！直接进入了我的个人主页。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/29BED333-C486-4957-9131-BB303ABB81A7.gif)](https://ww4.sinaimg.cn/large/006tKfTcgy1fbw8vfsxewg30800e84qp.gif)

然后就可以在 Workflow 里开工了。首先扫描二维码，把扫描到的内容保存到一个变量中，我的 Workflow 里起名叫做 code。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/99F6FF0A-DA25-471A-9FF5-5D6E82C22E3F.jpg)](https://ww1.sinaimg.cn/large/006tKfTcgy1fbw8y3zhtaj30yi1pcmzj.jpg)

随后我清空了剪贴板，这是一个个人习惯。如果不需要可以删除。接着就是 Get Variable 用 If 语句判断刚刚读到的内容里面是否含有：

```
qr.alipay.com
```

这个元素，如果有的话，那刚刚读到的应该是一个调用支付宝打开的链接。那么我们给他在他前面加上一端：

```
alipays://platformapi/startapp?saId=10000007&qrcode=
```

使得链接变成这样：

```
alipays://platformapi/startapp?saId=10000007&qrcode=https://qr.alipay.com/xxxxxxxxxxxxxxxxxxxxxx
```

最后使用 Open URLS 就可以了。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/1F93E3E9-4642-4FCA-94BD-CC5D521660C7.jpg)](https://ww2.sinaimg.cn/large/006tKfTcgy1fbw9ay467gj30yi1pc40s.jpg)

为了展示效果简化了判断是否为链接的判断，也是同样用 IF 判断即可。

#### 3. 罗列一下其它 App 的解决方案

淘宝，替换链接中 https 为 taobao：

```
taobao://taobao.com/xxxxxx     //淘宝页面
taobao://tb.cn/xxxxx           //淘宝扫描二维码登陆
```

微信，如包含以下关键字，调用`weixin://scanqrcode`二次扫码：

```
tenpay.com                     //微信支付
weixin.qq.com                  //微信公众号、小程序、个人名片链接
```

微博，如包含以下关键字，调用`weibo://qrcode`二次扫码：

```
weibo.cn                       //微博扫码登陆
```

豆瓣，替换链接中 https 为 douban：

```
douban://douban.com/book/xxxx  //豆瓣读书
```

京东，替换商品 id 或者登录 Key。

阅读前文后可以自己尝试看看。

#### 4.调用豆瓣API

有兴趣的可以研究一下。在这个 Workflow 里是扫描书背后的条形码跳转到豆瓣的页面里。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/2F0ECD48-05C9-4A02-B6D8-61B538989D31.gif)](https://ww4.sinaimg.cn/large/006tKfTcgy1fbwauqh9odg30800e8kjl.gif)

豆瓣的 API 页面：[豆瓣图书Api V2](https://developers.douban.com/wiki/?title=book_v2)

当我们扫到了书的条形码，就是那个 978xxxxxxxxxx 的 13 位数字之后，如何将它变成一个豆瓣可以打开的链接呢？这里以《岛上书店》举例。这本书的 ISBN 号是 9787539971810。

打开这个链接：

```
https://api.douban.com/v2/book/isbn/9787539971810
```

我们可以获得如下的信息：

```
{"rating":{"max":10,"numRaters":49715,"average":"7.7","min":0},"subtitle":"","author":["[美] 加布瑞埃拉·泽文"],"pubdate":"2015-5","tags":[{"count":8523,"name":"小说","title":"小说"},{"count":6457,"name":"外国文学","title":"外国文学"},{"count":4281,"name":"好书，值得一读","title":"好书，值得一读"},{"count":4024,"name":"美国文学","title":"美国文学"},{"count":3438,"name":"文学","title":"文学"},{"count":3267,"name":"生活","title":"生活"},{"count":3070,"name":"美国","title":"美国"},{"count":2878,"name":"深夜读书","title":"深夜读书"}],"origin_title":"The Storied Life of A. J. Fikry","image":"https://img3.doubanio.com\/mpic\/s28049685.jpg","binding":"平装","translator":["孙仲旭","李玉瑶"],"catalog":"第一部\n《待宰的羔羊》 \/ 3\n《像里兹饭店那样大的钻石》 \/ 27\n《咆哮营的幸运儿》 \/ 41\n《世界的感觉》 \/ 81\n《好人难寻》 \/ 89\n《卡拉维拉县驰名的跳蛙》 \/ 135\n《穿夏裙的女孩》 \/ 167\n第二部\n《与父亲的对话》 \/ 183\n《逮香蕉鱼的最佳日子》 \/ 197\n《泄密的心》 \/ 209\n《铁头》 \/ 223\n《当我们谈论爱情时我们在谈论什么》 \/ 249\n《书店老板》 \/ 257\n--\n注：整本书的章节标题都是文学作品的标题。\n《岛上书店》是一部小说。","ebook_URL":"https:\/\/read.douban.com\/ebook\/9580262\/","pages":"271","images":{"small":"https://img3.doubanio.com\/spic\/s28049685.jpg","large":"https://img3.doubanio.com\/lpic\/s28049685.jpg","medium":"https://img3.doubanio.com\/mpic\/s28049685.jpg"},"alt":"https:\/\/book.douban.com\/subject\/26340138\/","id":"26340138","publisher":"江苏凤凰文艺出版社","isbn10":"7539971819","isbn13":"9787539971810","title":"岛上书店","URL":"https:\/\/api.douban.com\/v2\/book\/26340138","alt_title":"The Storied Life of A. J. Fikry","author_intro":"加布瑞埃拉·泽文 Gabrielle Zevin\n译作目录：http:\/\/book.douban.com\/doulist\/14076\/\n译文小集：http:\/\/www.douban.com\/note\/34107135\/\n李玉瑶，编辑，译者。七十年代生人，现任职于上海译文出版社。译有《阿克拉手稿》《与狼共舞》《房间》《激情》等作品。","summary":"岛上书店是间维多利亚风格的小屋，门廊上挂着褪色的招牌，上面写着： 没有谁是一座孤岛。","ebook_price":"16.80","series":{"id":"34361","title":"全球顶级畅销小说文库：加·泽文作品"},"price":"CNY 35.00"}
```

很长的一段信息，包含了这本书的封面图片、简介等信息。这一次要提取的信息是《岛上书店》这本书的豆瓣 id：

```
"title":"岛上书店","URL":"https:\/\/api.douban.com\/v2\/book\/26340138",
```

URL 下有这本书的 id，这本书的豆瓣网页链接也包含了这个信息：

```
26340138
https://book.douban.com/subject/26340138/
```

接下来进行文字替换，打开链接即可。

```
https://api.douban.com/v2/book/26340138

douban://douban.com/book/26340138
```

下面用 Workflow 来完成这个动作。

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/B08040DD-D2EB-4811-8159-2F49CC124AFD.jpg)](https://ww3.sinaimg.cn/large/006tKfTcgy1fbwaeenyauj31kw1ekaft.jpg)

#### 5.如何把以上东西全部放到一个 Workflow里

以上的教程单单领出来一个可能制作起来很方便，但是要怎么自动识别读到的文字呢？这里要用到正则表达式进行判断，首先判断一下是不是 ISBN 码，它的特征是 13 位数字，978 开头。

```
^978[0-9]{10}$
```

再可以判断是不是 http 开头的链接，这里就不展开了，这需要一些耐心琢磨。

推荐大家两个网站可以自学：

* [正则表达式在线测试](http://tool.chinaz.com/regex/)
* [正则表达式30分钟入门](http://deerchao.net/tutorials/regex/regex.htm)

抛砖引玉
----

这个 Workflow 还远远没有完美，希望大家一起完善。这种东西少数派的大神肯定早就做过了吧，我心里是这样想的，希望能够抛砖引玉。我暂时还没有办法找出手机 QQ 扫码界面的 URL。微博微信的扫码还需要跳转到 App 本身的扫码界面二次扫码，并不像淘宝和豆瓣那样可以直达。

欢迎留言。

👉🏻 [Workflow 下载](https://workflow.is/workflows/50c68c91dfc5481689599b2c96ab98ba)

### Update

* 2017-01-23  增加大众点评扫码登陆 & 扫码跳转到手机大众点评
* 2017-01-22  增加京东扫码登陆 & 扫码跳转到对手机京东
* 2017-01-19  增加了支付宝扫码付款 & 扫码加好友等功能
* 2017-01-18  First Release，支持淘宝、微博、微信、豆瓣

* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/75D80D68-7ACF-4289-A9AF-51B6320D26A8.jpg)](http://sspai.com/topic/2016/)

原作者：
[森二](http://matrix.sspai.com/p/dd283600)

文章来源：
[少数派 Matrix](http://matrix.sspai.com/p/dd283600)

**本文为转载，版权归原作者所有。

* [** iOS](http://sspai.com/tag/iOS "查看所有关于 iOS 的文章")
* [** 技巧](http://sspai.com/tag/%E6%8A%80%E5%B7%A7 "查看所有关于 技巧 的文章")

[**

3](http://sspai.com/37132#)

* [](http://sspai.com/37132#)
* **

* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/0FFD315C-8248-480D-A3CE-F0D00A96E900.jpg)](http://matrix.sspai.com/user/642408)
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/E68EA5F3-3271-41A2-9F69-B2D20C7E01B8.jpg)](http://matrix.sspai.com/user/706656)
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/E6792EBE-3CE8-4686-AE43-F6C76EA130E5.jpg)](http://matrix.sspai.com/user/659019)

[![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/3F748117-453A-41C2-B496-7E712C5E746B.jpg)](http://matrix.sspai.com/user/735919)

[森二](http://matrix.sspai.com/user/735919)
**
[** 查看Ta的文章](http://matrix.sspai.com/user/735919)

* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/3F3F6771-107D-4436-95A0-5768D38D721B.jpg)

  iOS 版印象笔记大更新，重心终于回到了效率上](http://sspai.com/37091 "iOS 版印象笔记大更新，重心终于回到了效率上")
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/56C75E58-8183-43AE-9590-E70466CC661E.jpg)

  它让我开始尝试在 iPad 上写作：MWeb for iOS 使用体验](http://sspai.com/36980 "它让我开始尝试在 iPad 上写作：MWeb for iOS 使用体验")
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/BF498070-34C4-47F8-B3A6-5BDE22FAE403.jpg)

  在线阅读处理流程：从需求、到方法、再到工具](http://sspai.com/36795 "在线阅读处理流程：从需求、到方法、再到工具")
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/A6EF472F-9307-4007-B4E2-4178945999DE.jpg)

  为让更多人享受优质壁纸，我们做了 Cuto 小程序](http://sspai.com/37083 "为让更多人享受优质壁纸，我们做了 Cuto 小程序")
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/BDCD5BFF-B8A0-4F99-8A76-07ACB7477E5E.jpg)

  一段「银河历险记」风格的奇幻探险：横版冒险游戏 Yuri](http://sspai.com/37038 "一段「银河历险记」风格的奇幻探险：横版冒险游戏 Yuri")
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/E8318A1E-F910-49C4-A079-02ADEFAB360C.jpg)

  只用学生证，开通 Apple Music 大学生优惠方案丨一日一技](http://sspai.com/37121 "只用学生证，开通 Apple Music 大学生优惠方案丨一日一技")

评论 (5)

* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/E68EA5F3-3271-41A2-9F69-B2D20C7E01B8.jpg)](http://matrix.sspai.com/user/706656)

  [沨沄极客](http://matrix.sspai.com/user/706656)

  这个很实用诶，感谢作者~  
  刚刚测试了一下自己用纯文本生成的二维码，扫描之后直接结束了Workflow，是不是能考虑添加一个“无法识别就放在剪贴板”的分支呢

  10分钟前

  回复

  [](http://sspai.com/37132#)
  0
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/86D30A54-EA4B-43D6-8AA3-E24DCCB93067.jpg)](http://matrix.sspai.com/user/735919)

  [森二](http://matrix.sspai.com/user/735919)

  我昨晚更新了，居然没有发布最新版本...残念

  52分钟前

  回复

  [](http://sspai.com/37132#)
  0

  + [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/034677B6-DEFB-440C-9253-DBBFEA41D9C9.jpg)](http://matrix.sspai.com/user/718855)
    ![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/8C43D92C-9484-42C9-B8C3-0C89C4776EE3.png)

    [Tree Li](http://matrix.sspai.com/user/718855)

    吓？我现在修改

    41分钟前

    回复

    **
    0
  + [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/86D30A54-EA4B-43D6-8AA3-E24DCCB93067.jpg)](http://matrix.sspai.com/user/735919)

    [森二](http://matrix.sspai.com/user/735919)
    回复 [Tree Li](http://matrix.sspai.com/user/718855)

    Thx~

    39分钟前

    回复

    **
    0
* [![](.evernote-content/43A30DA8-D6E7-4FD2-9FC6-00728821DEAC/7501F42F-5CFE-494E-A2FC-F817A0A86E1B.jpg)](http://matrix.sspai.com/user/726257)

  [x1n](http://matrix.sspai.com/user/726257)

  这么有耐心研究，辛苦了

  55分钟前

  回复

  [](http://sspai.com/37132#)
  0

[微博登录并评论...](http://sspai.com/37132#)

---

[🌐 原始链接](http://sspai.com/37132)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ef3d1e58-179f-43c5-a965-5a3fccd98fc2/ef3d1e58-179f-43c5-a965-5a3fccd98fc2/)