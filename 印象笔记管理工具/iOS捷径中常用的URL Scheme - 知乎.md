# iOS捷径中常用的URL Scheme - 知乎

---

iOS捷径中常用的URL Scheme
===================

[一点搜罗](https://www.zhihu.com/people/he-bai-73-76)

公众号：一点搜罗，叫我皮哥就好，大四挣扎毕业狗，软件发烧友

文章中整理了一些在捷径中比较常用的URL Scheme，之后会不断更新！

使用方法非常简单，只需要将文中提供的链接复制至URL处即可，并且需要在URL后插入一个【打开URL】的指令才可正常运行使用。

![](.evernote-content/A73CF35A-5BE1-47A8-8B5A-C9499B169E08/6A4F484D-7CD3-4655-BAC2-B1A73D1F28D5.jpg)

---

***举个简单的例子：***

![](.evernote-content/A73CF35A-5BE1-47A8-8B5A-C9499B169E08/75AE20DF-6E06-409A-8B2E-01BC33E3533A.jpg)

以全能支付的捷径规则为例

将本文中的微信扫一扫的URL Scheme复制并粘贴到上图中的URL处，然后添加一条【打开URL】的指令，即可实现一键打开微信扫一扫的操作。

---

**网易云音乐、QQ音乐、酷我音乐、微信、支付宝、高德地图、哔哩哔哩、手机QQ、TIM、淘宝、京东、百度网盘、百度贴吧、百度地图、百度阅读、手机百度**

**网易云音乐：**

1.打开网易云音乐

orpheuswidget://

2.打开网易云音乐听歌识曲

orpheuswidget://recognize

3.打开本地音乐列表（已下载的歌曲）

orpheuswidget://download

4.打开指定歌单

orpheus://playlist/歌单ID

需要将【歌单ID】替换成需要打开的歌单ID

5.打开指定歌曲

orpheus://song/SONG\_ID

需要将【SONG\_ID】替换成需要打开的歌曲ID

6.打开指定歌手

orpheus://artist/ARTIST\_ID

需要将【ARTIST\_ID】替换成歌手的ID

7.打开私人 FM 并开始播放

orpheus://radio

**QQ音乐：**

打开 QQ 音乐

qqmusic://

在QQ音乐中打开我喜欢单曲

qqmusic://://[http://qq.com/ui/myTab?p=%7B%22tab%22%3A%22fav%22%7D](https://link.zhihu.com/?target=http%3A//qq.com/ui/myTab%3Fp%3D%257B%2522tab%2522%253A%2522fav%2522%257D)

在QQ音乐中播放本地歌曲

qqmusic://today?mid=31&k1=3&k4=0

在QQ音乐中播放热歌

qqmusic://://[http://qq.com/media/playRadio?p=%7B%22radioId%22%3A%22199%22%2C%22action%22%3A%22play%22%2C%22cache%22%3A%221%22%7D](https://link.zhihu.com/?target=http%3A//qq.com/media/playRadio%3Fp%3D%257B%2522radioId%2522%253A%2522199%2522%252C%2522action%2522%253A%2522play%2522%252C%2522cache%2522%253A%25221%2522%257D)

**酷我音乐：**

打开酷我音乐

com.kuwo.kwmusic.kwmusicForKwsing://

**微信：**

打开微信

weixin://

打开微信扫码

weixin://scanqrcode

**支付宝：**

打开支付宝

alipays://

打开收款

alipays://platformapi/startapp?appId=20000123

打开付款

alipay://platformapi/startapp?appId=20000056

打开转账

alipayqr://platformapi/startapp?saId=20000116

打开二维码扫一扫

alipayqr://platformapi/startapp?saId=10000007

打开乘车码

alipayqr://platformapi/startapp?saId=200011235

打开记账本

alipay://platformapi/startapp?appId=20000168

打开滴滴

alipay://platformapi/startapp?appId=20000778

打开蚂蚁森林

alipay://platformapi/startapp?appId=60000002

打开手机充值

alipayqr://platformapi/startapp?saId=10000003

打开生活缴费

alipays://platformapi/startapp?appId=20000193

打开彩票

alipays://platformapi/startapp?appId=10000011

打开股票

alipays://platformapi/startapp?appId=20000134

打开快递查询

alipays://platformapi/startapp?appId=20000754

打开还信用卡

alipays://platformapi/startapp?appId=09999999

**高德地图：**

打开高德地图

iosamap://

高德地图驾驶导航

iosamap://navi?sourceApplication=applicationName&backScheme=applicationScheme&poiname=fangheng&poiid=BGVIS&lat=36.547901&lon=104.258354&dev=1&style=2

**哔哩哔哩：**

打开哔哩哔喱

bilibili://

用哔哩哔喱搜索

bilibili://search?keyword=[输入]

需要将【输入】二字替换为你需要搜索的内容

**手机QQ：**

打开手机 QQ

mqqapi://

打开手机 QQ 扫一扫

mqqapi://qrcode/scan\_qrcode?version=1&src\_type=app

手机QQ快速搜索好友

mqqapi://card/show\_pslcard?src\_type=internal&version=1&uin=UIN

将【UIN】替换为需要快速打开的QQ号码

手机QQ快速打开群

mqqapi://card/show\_pslcard?src\_type=internal&version=1&card\_type=group&uin=UIN

将【UIN】更换为需要快速打开的QQ群号码

**TIM：**

打开 TIM

tim://

打开 TIM 中的扫一扫

tim://qrcode/scan\_qrcode?version=1&src\_type=app

**淘宝：**

打开淘宝

taobao://

用淘宝搜索指定物品

taobao://s.taobao.com?q=[输入]

需要将【输入】二字替换为你需要搜索的内容

**京东：**

打开京东

openApp.jdMobile://

**百度：**

百度网盘

baiduyun://

百度贴吧

com.baidu.tieba://

百度地图

baidumap://

百度阅读

bdbook://

手机百度

bdboxiosqrcode://

微信公众号：一点搜罗

帮你搜罗一切最好用的iOS、Android、Windows应用以及各种小技巧！

---

[🌐 原始链接](https://zhuanlan.zhihu.com/p/57567971)

[📎 在印象笔记中打开](evernote:///view/207087/s1/646b394d-e453-497f-9dcf-f14cc17c8e4d/646b394d-e453-497f-9dcf-f14cc17c8e4d/)