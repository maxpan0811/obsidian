---
title: 不从Win7_Win8.1升级，直接全新安装并激活Win10方法
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/不从Win7_Win8.1升级，直接全新安装并激活Win10方法.md
tags: [evernote, impression, yinxiang]
---

# 不从Win7/Win8.1升级，直接全新安装并激活Win10方法

---

Top

![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/A25EA697-60F0-4EA5-AE48-03FF9F2BBE63.png)

[![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/62F86202-81A7-4143-9531-F33C5B6FBE57.png)](https://itunes.apple.com/cn/app/it-zhi-jia/id570610859?mt=8)

IT之家

资讯
--

* [IT资讯](http://wap.ithome.com/it/)
* [科学](http://wap.ithome.com/discovery/)

极客
--

* [安卓之家](http://wap.ithome.com/android/)
* [数码之家](http://wap.ithome.com/digi/)
* [智能时代](http://wap.ithome.com/next/)

微软
--

* [WP之家](http://wap.ithome.com/wp/)
* [Win10之家](http://wap.ithome.com/win10/)
* [Win8之家](http://wap.ithome.com/win8/)
* [Win7之家](http://wap.ithome.com/win7/)

苹果
--

* [iPhone之家](http://wap.ithome.com/iphone/)
* [iPad之家](http://wap.ithome.com/ipad/)
* [Mac之家](http://wap.ithome.com/mac/)
* [iOS之家](http://wap.ithome.com/ios/)

资源
--

* [软件之家](http://wap.ithome.com/soft/)
* [主题之家](http://wap.ithome.com/zhuti/)
* [壁纸之家](http://wap.ithome.com/bizhi/)

[IT圈](http://quan.ithome.com/wap/)

[注册](http://i.ruanmei.com/reg.aspx) 登录

[首页](http://wap.ithome.com/)>[Win10之家](http://wap.ithome.com/win10/)>[Win10学院](http://wap.ithome.com/win10xueyuan/)

不从Win7/Win8.1升级，直接全新安装并激活Win10方法
================================

2015-8-31 9:29:58   IT之家 　　  [![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/153612E5-7130-4917-A3A5-E9E52809B0FB.png) 401](http://wap.ithome.com/html/172955.htm#commentDiv)  ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/45371ECA-0EF2-4E96-93A0-CCDAFB09DBB2.png) **162907** 责编：凌空

本文针对那些还没有升级[Win10](http://win10.ithome.com/)的[Win7](http://www.win7china.com/)/[Win8.1](http://win8.ithome.com/)用户。关于[Windows10](http://win10.ithome.com/)系统激活，我想大多数用户还是想好好利用一下微软提供的免费升级途径的。根据微软公布的升级方案以及实际测试，[Windows7](http://www.win7china.com/)/[Windows 8.1](http://win8.ithome.com/)用户需要在当前系统基础上执行升级安装才能够保证Win10安装后自动激活。也就是说，（首次激活Win10）升级是必经之路。但肯定有朋友想**跳过升级，直接全新安装或安装双系统**，那有没有方法在这种情况下也能自动激活呢？

经[IT之家](http://www.ithome.com/)探索测试后，发现了以下可行的方法。有此需求的朋友们可以参考下面的方法来操作：

**1、**在你正在使用的Win7/Win8.1系统中（注意，要确保系统已经激活）打开下载的Win10 ISO镜像，在Sources文件夹中找到gatherosstate.exe程序，把它复制到桌面。

**提示：**Win7系统下可使用魔方虚拟光驱（[点此下载](http://down.ruanmei.com/tweakcube/partner/pcmastersetup_u151.exe)）打开ISO镜像。

**2、**双击gatherosstate.exe，稍后会在桌面生成名为GenuineTicket.xml的文件（名字翻译过来就是“正版通行证”），这份文件至关重要，把它保存好。

![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/1803AFE4-F4CA-4264-8818-BD0CE4AA37DC.jpg)

**3、**然后用你熟悉的安装方法安装Win10吧。[U盘法](http://www.ithome.com/html/win10/144880.htm)、[硬盘法](http://www.ithome.com/html/win10/144874.htm)、光盘法，随你选。但要注意一定要确保安装前后系统版本相对应，参考《[Win10正式版版本这么多，我到底该下载哪一个？](http://www.ithome.com/html/win10/166083.htm)》。安装过程中跳过一切密钥输入步骤。

**4、**安装完成后，打开C:\ProgramData\Microsoft\Windows\ClipSVC\GenuineTicket文件夹（注意ProgramData为隐藏文件夹），然后把保存的GenuineTicket.xml文件复制到这个目录中。

![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/7A9DCA99-24D6-4553-B7FA-F311C6BD855E.jpg)

**5、**重启电脑，确保系统已联网，稍后就会自动激活了。你也可以在系统属性中手动点击“立即激活”。

![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/ADA13018-88AF-4050-84CB-A2A8FB260066.jpg)

以上过程执行一次即可，激活后微软服务器会记录信息，再次重装后只需联网即可自动激活。

此方法对于升级总是失败的朋友会更有帮助，你可以直接选择全新安装，不用再去升级了。另外，本方法已在若干台电脑（未升级过Win10）中测试通过，但不排除会有其他因素导致激活失败。

玩转[Win10](http://win10.ithome.com/)，尽在[IT之家Win10特别专题>>](http://www.ithome.com/zhuanti/win10/)

微信搜索“IT之家”关注抢6s大礼！下载IT之家客户端（[戳这里](https://itunes.apple.com/cn/app/it-zhi-jia/id570610859?mt=8)）也可参与评论抽楼层大奖！

分享给小伙伴们：

[38](http://wap.ithome.com/html/172955.htm "累计分享38次")

本文标签：[Win10正式版](http://wap.ithome.com/tag/win10zhengshiban/)，[Win10系统](http://wap.ithome.com/tag/win10xitong/)

相关文章
----

* [Win10《应用商店》新功能：按设备类型查看评论](http://wap.ithome.com/html/172897.htm)08.30
* [回顾Windows开始菜单20年变化，你用过几个？](http://wap.ithome.com/html/172865.htm)08.30
* [Win10语音助手Cortana庆祝印度“兄妹节”](http://wap.ithome.com/html/172853.htm)08.30
* [Win10预览版10532语言包官方下载地址汇总](http://wap.ithome.com/html/172835.htm)08.30
* [一个Mac用户眼里的Win10](http://wap.ithome.com/html/172817.htm)08.29
* [IT之家学院：Win10如何为多显示器电脑设置不同壁纸](http://wap.ithome.com/html/172805.htm)08.29

### 发表评论[[ 账户禁言和解封规则 ]](http://quan.ithome.com/0/003/116.htm)愿您的每句评论，都能给大家的生活添色彩，带来共鸣，带来思索，带来快乐。

此文章年代太久远了，不再允许评论

软媒通行证

[注册](http://i.ruanmei.com/reg.aspx)   其他登录： 
![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/A0106354-7F25-4EEB-996C-E642E7512996.png)
 
![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/F3EE49BF-DA24-4066-A0D5-A9B3C9C29617.png)
 
![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/04AA38EB-3B4B-4F84-8A95-B59E0B6CC197.png)
密码

### 热门评论

* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/CE45B405-EDF8-4147-BDAB-32441CB0CD93.jpg)

  **[吃桃](http://quan.ithome.com/user/1050722 "软媒通行证数字ID：1050722")**[诺基亚 Lumia 1020](http://m.ithome.com/ithome/download/)湖北宜昌 2015-8-31 9:39:45

  这才是技术帖，刺客要多找点这样的小弟啊

  [展开(4)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(1114)反对(7)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/21B501FB-F966-4CC7-9801-F8A551EA52A8.jpg)

  **[凡瑶唯愛](http://quan.ithome.com/user/942387 "软媒通行证数字ID：942387")**[iPhone 6 Plus](http://m.ithome.com/ithome/download/)吉林白山 2015-8-31 9:38:27

  一男同学，冲出教室不小心摸到一位女同学的胸，刚想道歉。  
    
  只见女同学很生气的说：“真不要脸，乱摸人家胸。”  
    
  男同学立马整个人都不好了，回答道：“你有吗？我怎么没感觉啊！”  
    
  女生又问：“那你知道为什么地球是圆的，我们也没感觉到吗？那是因为它大！”

  [展开(9)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(599)反对(31)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/79190FFF-86AB-48E0-B0CD-0261AC8C387B.jpg)

  **[狼小天](http://quan.ithome.com/user/1065901 "软媒通行证数字ID：1065901")**[诺基亚 Lumia 930](http://m.ithome.com/ithome/download/)山东聊城 2015-8-31 9:53:33

  这不阅兵嘛，北京实行车辆单双号限行第一天，公交车上乘客爆满…… 一男子挤得实在受不了，喊到：“都别挤了，我tm都坐过好几站了”！另一哥们：“你那算啥，我tm只是路过，都被挤上车了”……一位四十多岁大哥从人缝中挤出脑袋，喊道：“都让让，都让让，我才是司机，现在谁开车呢？”!

  [展开(4)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(540)反对(24)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/7F9B7D60-FC25-4529-802F-D2631DB1ADD4.jpg)

  **[谢脑板](http://quan.ithome.com/user/884651 "软媒通行证数字ID：884651")**[诺基亚 Lumia 526](http://m.ithome.com/ithome/download/)江苏南京 2015-8-31 9:45:09

  于是两人吵嘴吵着吵着就走到到了一起，过上幸福生活  
  女生：为什么你X进来我没感觉啊？你太短了？  
  男生：不，你看汽油桶和水笔，汽油桶长宽比例不及水笔，看上去汽油桶比较扁而水笔看上去比较长，而实际上汽油桶的绝对长度远长于水笔，只是因为汽油桶宽而看上去短

  [展开(9)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(268)反对(16)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **[适宜幺捌](http://quan.ithome.com/user/793390 "软媒通行证数字ID：793390")**[索尼 Xperia Z2](http://m.ithome.com/ithome/download/)浙江舟山 2015-8-31 21:47:42

  建议微软卖掉一部手机，送一套正版系统。这样就又能解决手机销量，又能让更多人用win10,以后统一霸业就更容易实现了！支持的顶到前排！

  [展开(2)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(121)反对(8)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **[灌溉](http://quan.ithome.com/user/1008114 "软媒通行证数字ID：1008114")**[三星 Galaxy S4](http://m.ithome.com/ithome/download/)新南威尔士Randwick 2015-8-31 9:41:49

  你这段子太旧了，我在it之家起码看了三四次

  [展开(9)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(114)反对(9)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/F99B9F31-DF0B-4CC9-97DC-2D405FFC3610.jpg)

  **[ANYWHERE89](http://quan.ithome.com/user/53525 "软媒通行证数字ID：53525")**[魅族 MX4](http://m.ithome.com/ithome/download/)山西太原 2015-8-31 9:58:03

  居然有老婆 在IT之家你这也算是人生赢家了

  [展开(8)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(102)反对(0)
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/F93F462E-05D3-4815-B85A-F25EDD178803.jpg)

  **[Vamos丶浮生未歇](http://quan.ithome.com/user/818320 "软媒通行证数字ID：818320")**[小米 4](http://m.ithome.com/ithome/download/)四川成都 2015-8-31 11:45:11

  自己做U盘多好，淘宝全是盗版系统精简系统！经常搞系统的都知道！

  [展开(2)![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE32FBDF-28FB-477E-AA70-143E0AEAAAB8.png)](http://wap.ithome.com/html/172955.htm)

  支持(55)反对(0)

### 最新 最早全部评论

* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/37F41C1F-71AB-40D0-A4E5-F0D1EFABCB6C.jpg)

  **288楼****[畅玩微果卓](http://quan.ithome.com/user/884102 "软媒通行证数字ID：884102")**[被修改的iOS设备](http://m.ithome.com/ithome/download/)广西来宾 2015-9-25 23:23:37

  额

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **287楼****[Town Boy](http://quan.ithome.com/user/1210499 "软媒通行证数字ID：1210499")**香港 2015-9-23 11:23:33

  我用的是'ACER' netbook, 系統是自裝Win7旗艦版,跑得慢但算正常,巳激活,但沒有Win10可升級的標記;所以我用上述方法全新安裝, 安裝成功但激活失敗.

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/1D0B0507-B0D0-4820-85B6-D6797746B19B.jpg)

  **281楼****[存在在存在](http://quan.ithome.com/user/845239 "软媒通行证数字ID：845239")**[三星 Galaxy S6 edge](http://m.ithome.com/ithome/download/)安徽合肥 2015-9-20 17:11:20

  是啊

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/1D0B0507-B0D0-4820-85B6-D6797746B19B.jpg)

  **280楼****[存在在存在](http://quan.ithome.com/user/845239 "软媒通行证数字ID：845239")**[诺基亚 Lumia 822](http://m.ithome.com/ithome/download/)安徽合肥 2015-9-13 23:20:40

  居然还有人评论

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/E465CB13-732D-47DE-8C3A-8A8647D577B7.jpg)

  **279楼****[adminlock](http://quan.ithome.com/user/959751 "软媒通行证数字ID：959751")**[魅蓝 Note](http://m.ithome.com/ithome/download/)陕西西安 2015-9-12 9:17:19

  这种方法只能在全新磁盘安装时使用，在win7或win8.1直接升级方法不行的，豆豆小编也说了，亲测，如果有机友也遇到这种情况，顶一下。让更多人知道。

  举报支持(5)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/32F7E45D-8EDA-40DD-A040-FA14748495B8.jpg)

  **278楼****[Muvv](http://quan.ithome.com/user/658466 "软媒通行证数字ID：658466")**四川成都 2015-9-11 13:48:48

  今天看见一个老人摔倒，于是就过去扶， 没想到他一把抓住我的手，我急忙说:监控会还我清白！ 老人说:嘿嘿别傻了这里没监控！ 我直接一脚踹过去。T， M D没监控也敢这么吊。 他儿子及时出现说，我们在边上录下你踹人的视频。 我冷笑一声出示了南京方面提供的急性短暂性精神障碍症！

  举报支持(5)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **277楼****[zyx2900](http://quan.ithome.com/user/1188417 "软媒通行证数字ID：1188417")**[微软 Lumia 640 XL](http://m.ithome.com/ithome/download/)湖南长沙 2015-9-9 12:47:50

  真心好帖，真机测试已是Win7，Win10双正版系统

  举报支持(1)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **276楼****[aa425510131](http://quan.ithome.com/user/508040 "软媒通行证数字ID：508040")**[魅蓝 Note 2](http://m.ithome.com/ithome/download/)上海宝山 2015-9-7 14:39:30

  这算是正版吗？我是oem正版win7怎么全新安装10并激活？

  举报支持(2)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **275楼****[City-limit](http://quan.ithome.com/user/1013399 "软媒通行证数字ID：1013399")**[诺基亚 Lumia 925](http://m.ithome.com/ithome/download/)河北石家庄 2015-9-6 23:56:42

  win10的，lol界面特别几把卡，卡的无解了，，，

  举报支持(1)反对(5)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **274楼****[风吹稻花香123](http://quan.ithome.com/user/964555 "软媒通行证数字ID：964555")**[中兴 V5](http://m.ithome.com/ithome/download/)江西南昌 2015-9-5 14:40:54

  密钥无效😂

  举报支持(4)反对(1)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/59BD8565-A63F-4BB4-8A32-E5CEC6F8BE44.jpg)

    **1#****[邪恶的蛋蛋](http://quan.ithome.com/user/416525 "软媒通行证数字ID：416525")**[iPhone 5s 月光银](http://m.ithome.com/ithome/download/)浙江温州 2015-9-14 22:37:04

    我也是

    举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/1E902AEB-0F9B-4331-A4E3-86B60264BE70.jpg)

  **273楼****[Enyion](http://quan.ithome.com/user/830942 "软媒通行证数字ID：830942")**[三星 Galaxy Grand 2](http://m.ithome.com/ithome/download/)山东济南 2015-9-5 10:49:00

  win10GTA不能玩怎么办？兼容调了，管理员运行了，都不行！还是gta\_sa.exe已停止工作！

  举报支持(0)反对(0)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/843CC145-04ED-46CE-9AA1-517C36914413.jpg)

    **1#****[你说我笑](http://quan.ithome.com/user/1067611 "软媒通行证数字ID：1067611")**[诺基亚 Lumia 830](http://m.ithome.com/ithome/download/)福建三明 2015-9-5 11:23:46

    购买正版

    举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/385214CB-B43B-4D40-8530-F1AD03686B3E.jpg)

  **272楼****[星月尘缘](http://quan.ithome.com/user/67088 "软媒通行证数字ID：67088")**上海 2015-9-4 15:24:35

  好东西必须顶起！不过就怕微软封掉！

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/653A73FF-66B2-46F6-BDD2-F56779F2544F.jpg)

  **271楼****[XJAIYY](http://quan.ithome.com/user/755574 "软媒通行证数字ID：755574")**安徽阜阳 2015-9-4 9:19:13

  厉害

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **270楼****[scunsyt](http://quan.ithome.com/user/1120835 "软媒通行证数字ID：1120835")**[小米 2](http://m.ithome.com/ithome/download/)陕西西安 2015-9-4 1:43:47

  测试失败。。。

  举报支持(11)反对(0)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/59BD8565-A63F-4BB4-8A32-E5CEC6F8BE44.jpg)

    **1#****[邪恶的蛋蛋](http://quan.ithome.com/user/416525 "软媒通行证数字ID：416525")**[iPhone 5s 月光银](http://m.ithome.com/ithome/download/)浙江温州 2015-9-14 22:37:20

    同样

    举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/52573DE1-CDB6-44AF-9109-957CFE239738.jpg)

  **269楼****[＄┢┑○Ψ](http://quan.ithome.com/user/191952 "软媒通行证数字ID：191952")**[三星 Galaxy Grand Neo](http://m.ithome.com/ithome/download/)福建泉州 2015-9-3 22:10:21

  收藏起来待用

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **268楼****[诺殿](http://quan.ithome.com/user/911948 "软媒通行证数字ID：911948")**[Win10客户端](http://m.ithome.com/ithome/download/)山东泰安 2015-9-3 21:34:30

  这方法真心给力！现在双系统win10和win7

  举报支持(1)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **267楼****[紫宵银月](http://quan.ithome.com/user/1189671 "软媒通行证数字ID：1189671")**[荣耀3C](http://m.ithome.com/ithome/download/)江苏南京 2015-9-3 17:01:21

  按照这个方法安装之后，为什么系统会突然变成未激活，然后重启又激活，然后偶尔又是未激活  
  什么鬼

  举报支持(3)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **266楼****[弦默](http://quan.ithome.com/user/839740 "软媒通行证数字ID：839740")**山东济南 2015-9-3 15:07:23

  不错

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **265楼****[笑笑过日子](http://quan.ithome.com/user/859894 "软媒通行证数字ID：859894")**[Win10客户端](http://m.ithome.com/ithome/download/)北京 2015-9-2 12:09:55

  实测激活失败，win8.1已预定win10,更新补丁下不动，按这个教程弄的，U盘安装对应的家庭版，最后激活失败。

  举报支持(17)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **264楼****[笑笑过日子](http://quan.ithome.com/user/859894 "软媒通行证数字ID：859894")**[Win10客户端](http://m.ithome.com/ithome/download/)北京 2015-9-2 10:37:52

  技术贴

  举报支持(0)反对(1)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **263楼****[诺殿](http://quan.ithome.com/user/911948 "软媒通行证数字ID：911948")**[iPhone 5s 月光银](http://m.ithome.com/ithome/download/)山东泰安 2015-9-2 1:31:48

  许可证绑定电脑吗

  举报支持(2)反对(2)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

    **1#****[Town Boy](http://quan.ithome.com/user/1210499 "软媒通行证数字ID：1210499")**香港 2015-9-23 11:32:42

    對

    举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **262楼****[诺殿](http://quan.ithome.com/user/911948 "软媒通行证数字ID：911948")**[iPhone 5s 月光银](http://m.ithome.com/ithome/download/)山东泰安 2015-9-2 1:31:34

  求助！装系统遇到麻烦格式化找不到许可证了！用其他电脑生成一份可以不

  举报支持(0)反对(1)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/0C89C39A-701F-4C54-ACD5-725E29718535.jpg)

  **261楼****[snakegtd](http://quan.ithome.com/user/942822 "软媒通行证数字ID：942822")**[iPhone 6](http://m.ithome.com/ithome/download/)内蒙古呼和浩特 2015-9-2 0:37:46

  失败了

  举报支持(4)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/EE8FB8C5-051A-43B0-B9F9-7D2CC74DA90B.jpg)

  **260楼****[乔北峰](http://quan.ithome.com/user/1054008 "软媒通行证数字ID：1054008")**[小米 2S](http://m.ithome.com/ithome/download/)湖北武汉 2015-9-1 23:38:13

  技术贴，顶

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/09873657-4E83-4BF0-9101-EF35E17A90BB.jpg)

  **259楼****[【顺丰快递】王卫](http://quan.ithome.com/user/1165363 "软媒通行证数字ID：1165363")**[iPhone 5s 月光银](http://m.ithome.com/ithome/download/)安徽六安 2015-9-1 22:41:43

  已经升级win10的能不能把这个打包啊刻录到u盘供其他机子使用？

  举报支持(0)反对(1)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **258楼****[山青](http://quan.ithome.com/user/809502 "软媒通行证数字ID：809502")**北京 2015-9-1 22:19:11

  重装之前没看到这个，给微软打电话，说把win8.1的正版序列号给他们，他们给我换成win10的密钥。各种确认信息。

  举报支持(2)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **257楼****[国民青年](http://quan.ithome.com/user/1197108 "软媒通行证数字ID：1197108")**河北唐山 2015-9-1 22:01:52

  不错

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C4B86359-CB8C-437F-B0F5-B89C664194DD.jpg)

  **256楼****[金正电脑](http://quan.ithome.com/user/118622 "软媒通行证数字ID：118622")**[诺基亚 Lumia 638](http://m.ithome.com/ithome/download/)吉林四平 2015-9-1 21:50:49

  有才，又能封装win10了

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/0E1BA51F-CEA5-4020-B9A8-CD3253585467.jpg)

  **255楼****[泉帅](http://quan.ithome.com/user/64424 "软媒通行证数字ID：64424")**[iPhone 5s 土豪金](http://m.ithome.com/ithome/download/)福建福州 2015-9-1 19:36:08

  难得的一致好评啊。

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/BBC4DD74-47CF-4D91-A4FE-A512B0E3B777.jpg)

  **254楼****[Rio�2014](http://quan.ithome.com/user/849671 "软媒通行证数字ID：849671")**[诺基亚 Lumia 1020](http://m.ithome.com/ithome/download/)北京 2015-9-1 19:28:23

  马克

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/7575270B-C89E-4FE6-8EFA-29AB2AA6ECF2.jpg)

  **253楼****[飞天狐狸](http://quan.ithome.com/user/75616 "软媒通行证数字ID：75616")**[Win10客户端](http://m.ithome.com/ithome/download/)Phnum PenhPhnom Penh 2015-9-1 17:24:15

  技术贴要留名啊

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/11D854BD-C1EB-4968-B5E7-B9F48B71C2C7.jpg)

  **252楼****[shanemark](http://quan.ithome.com/user/294595 "软媒通行证数字ID：294595")**四川成都 2015-9-1 16:48:43

  pc网页端怎么收藏这文章哦

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/4CD667E2-6D2C-4638-8192-CF2920692988.jpg)

  **251楼****[こゆき](http://quan.ithome.com/user/171401 "软媒通行证数字ID：171401")**[LG G4](http://m.ithome.com/ithome/download/)安徽合肥 2015-9-1 16:17:49

  管用不？

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/12FCAE98-CC35-4E39-B3A7-510B2702E951.jpg)

  **250楼****[腾讯](http://quan.ithome.com/user/68143 "软媒通行证数字ID：68143")**[iPhone 5s 深空灰](http://m.ithome.com/ithome/download/)重庆 2015-9-1 16:16:29

  我可以其他win7电脑中这样做，然后再来激活自己的win10么？

  举报支持(3)反对(3)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

    **1#****[诺殿](http://quan.ithome.com/user/911948 "软媒通行证数字ID：911948")**[iPhone 5s 月光银](http://m.ithome.com/ithome/download/)山东泰安 2015-9-2 1:32:32

    我也想这样呢

    举报支持(1)反对(1)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **249楼****[kyle.du](http://quan.ithome.com/user/1174713 "软媒通行证数字ID：1174713")**北京 2015-9-1 14:49:31

  求助！！！正版32位win7用这个方法能否升级为正版64位win10？？？

  举报支持(4)反对(1)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

    **1#****[Town Boy](http://quan.ithome.com/user/1210499 "软媒通行证数字ID：1210499")**香港 2015-9-23 11:38:32

    本身電腦硬件可否支持跑64位?

    举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **248楼****[诟病](http://quan.ithome.com/user/1006401 "软媒通行证数字ID：1006401")**吉林吉林市 2015-9-1 14:07:10

  以后多发发这种技术贴。别老发没用的。

  举报支持(2)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/A2586832-B685-428D-AFB9-F327F84CF6C1.jpg)

  **247楼****[瀂家军技术指导互瀂娃](http://quan.ithome.com/user/1052245 "软媒通行证数字ID：1052245")**陕西西安 2015-9-1 12:44:18

  给豆豆加工资+1

  举报支持(2)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/777C90B3-2052-44E8-ADB1-B4CBDF81BBE6.jpg)

  **246楼****[吾举懒人](http://quan.ithome.com/user/1005866 "软媒通行证数字ID：1005866")**[诺基亚 Lumia 920](http://m.ithome.com/ithome/download/)河南三门峡 2015-9-1 12:38:57

  好帖。已收藏。

  举报支持(1)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

  **245楼****[Mahuaten](http://quan.ithome.com/user/1126501 "软媒通行证数字ID：1126501")**[iPad Air 2](http://m.ithome.com/ithome/download/)浙江台州 2015-9-1 12:21:05

  给豆豆加工资吧

  举报支持(3)反对(1)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/4B348CF7-E98E-430B-BD94-A661FE0AB4EA.jpg)

  **244楼****[丿风雅颂丶](http://quan.ithome.com/user/1081930 "软媒通行证数字ID：1081930")**[Win10客户端](http://m.ithome.com/ithome/download/)山西太原 2015-9-1 11:29:34

  马克一下

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/881A9906-EAD9-4B28-818D-A1C6493AA05B.jpg)

  **243楼****[布道者](http://quan.ithome.com/user/1110692 "软媒通行证数字ID：1110692")**[诺基亚 Lumia 930](http://m.ithome.com/ithome/download/)江苏南京 2015-9-1 11:13:16

  有人提出了32位能否升64位。  
  网吧的32位Windows7为什么能用8G内存呢？

  举报支持(0)反对(1)回复

  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/A0ABFE07-AF71-47C2-8722-C86E1719BE95.jpg)

    **1#****[法外狂徒](http://quan.ithome.com/user/805956 "软媒通行证数字ID：805956")**[华为 Ascend P7](http://m.ithome.com/ithome/download/)河南郑州 2015-9-1 11:32:49

    明明是64位系统

    举报支持(6)反对(1)回复
  + ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C8EAEDBA-6C43-4F52-874F-46A26E6DC324.png)

    **2#****[Town Boy](http://quan.ithome.com/user/1210499 "软媒通行证数字ID：1210499")**香港 2015-9-23 11:42:00

    可能是2G內存+6G虛擬硬碟.

    举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/C0FB52D2-F553-44D3-9FA7-7F6F99188AD5.jpg)

  **242楼****[小橘子s](http://quan.ithome.com/user/1105173 "软媒通行证数字ID：1105173")**[Win10客户端](http://m.ithome.com/ithome/download/)河南平顶山 2015-9-1 11:04:40

  然而问题就出在以前的系统就不是正版的

  举报支持(3)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/8AF5BC9D-8AAA-4201-B58B-129F139FC01F.jpg)

  **241楼****[叫我帅哥就给你辣条吃](http://quan.ithome.com/user/1167713 "软媒通行证数字ID：1167713")**[Android 客户端](http://m.ithome.com/ithome/download/)福建漳州 2015-9-1 10:14:22

  我觉得在正版登录一段时间的微软帐号，然后以后全新安装好也会登录就会激活了...

  举报支持(3)反对(3)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/0C89C39A-701F-4C54-ACD5-725E29718535.jpg)

  **240楼****[snakegtd](http://quan.ithome.com/user/942822 "软媒通行证数字ID：942822")**[iPhone 6](http://m.ithome.com/ithome/download/)内蒙古呼和浩特 2015-9-1 10:03:00

  升级时候提示升级家庭版是否可以用此方法安装专业版

  举报支持(1)反对(2)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/CE49D2C5-937B-4BB6-9A5B-FE280F66068D.jpg)

  **239楼****[逍遥\_64](http://quan.ithome.com/user/237994 "软媒通行证数字ID：237994")**云南曲靖 2015-9-1 9:46:37

  win7用的好好的，有必要升级吗？升级的系统有限制吗？俺的机器是装的是正版系统，一直都在自动升级和更新，我还需要升级win10吗？

  举报支持(3)反对(6)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/9F57968B-AA01-46BF-858D-C195FB48D355.jpg)

  **238楼****[Sea\_5](http://quan.ithome.com/user/74163 "软媒通行证数字ID：74163")**[坚果手机](http://m.ithome.com/ithome/download/)陕西西安 2015-9-1 9:10:21

  赞

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/D591434B-2CB3-404B-8BCA-9D342E2B1AA4.jpg)

  **237楼****[黑纸白字](http://quan.ithome.com/user/880122 "软媒通行证数字ID：880122")**[红米 2](http://m.ithome.com/ithome/download/)陕西西安 2015-9-1 9:04:27

  技术帖子，收藏了

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/84D74E23-2615-4C68-B6C9-FB0AE4B4BBC0.jpg)

  **236楼****[雨の清晨](http://quan.ithome.com/user/888365 "软媒通行证数字ID：888365")**[索尼 Xperia Z1 Compact](http://m.ithome.com/ithome/download/)福建厦门 2015-9-1 8:59:50

  好帖

  举报支持(0)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/57B91685-21B9-48A2-B1E2-96A9017B0B95.jpg)

  **235楼****[路过心上的感觉](http://quan.ithome.com/user/779850 "软媒通行证数字ID：779850")**[HTC One](http://m.ithome.com/ithome/download/)湖北武汉 2015-9-1 8:53:56

  我想问下企业版win8.1也可以这样激活吗？

  举报支持(1)反对(0)回复
* ![](.evernote-content/EF476B55-7A01-4375-B959-78002DA1A9B9/A0916F36-4F72-493C-9484-25A8E588AA42.jpg)

  **234楼****[呆毛dm](http://quan.ithome.com/user/1001564 "软媒通行证数字ID：1001564")**[iPhone 5c 绿](http://m.ithome.com/ithome/download/)安徽合肥 2015-9-1 7:40:45

  找了好久了，it之家技术贴就是好

  举报支持(0)反对(0)回复

查看更多评论 ...

[电脑版](http://wap.ithome.com/html/172955.htm#)    [**关于IT之家**](http://www.ithome.com/about.htm)  |  [**联系我们**](http://www.ruanmei.com/contact/)

软媒旗下网站，IT之家。

©2015 [软媒公司](http://www.ruanmei.com/) 版权所有

---

[🌐 原始链接](http://wap.ithome.com/html/172955.htm)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7f4bec54-c1cb-4e46-8220-b65672c8e960/7f4bec54-c1cb-4e46-8220-b65672c8e960/)
