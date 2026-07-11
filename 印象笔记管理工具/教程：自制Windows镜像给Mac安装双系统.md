# 教程：自制Windows镜像给Mac安装双系统

---

教程：自制Windows镜像给Mac安装双系统
=======================

[![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/60C5E6D7-6B40-4508-BFCE-1F03EBF326B6.gif)](http://fullrss.net/r/http/bbs.feng.com/u.php?uid=798198)

投稿by：[叫我知心哥哥丶](http://fullrss.net/r/http/bbs.feng.com/u.php?uid=798198) 来源：威锋网

PostTime：2015-04-02 22:01:14

[收藏](http://fullrss.net/r/javascript/www.feng.com/apple/MAC/2015-04-02/void(0)) [已收藏](http://fullrss.net/r/http/bbs.feng.com/home.php?mod=space&do=favorite&type=news)

微博

[![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/B0DD3EDD-A118-46BE-8EE7-CBB5F27E247A.jpg)](http://fullrss.net/r/http/weibo.com/weiphone?zwm=tech)

微信![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/2E510A38-A31E-454F-9C07-B7BD5D9FF3EA.png)*扫一扫加威锋官方微信号***微信号：weiphone\_2007** [加载中...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml#comment)

[Twitter](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml#twitter) [Share](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml#Share) [Email](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml#Email) [Save](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml#Save) [Print](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml#Print)

> 对于用不惯 OS X 的用户来说，如何翻来覆去的作死，给自己心爱的 Mac 装上 Windows 系统，是一件急需解决的事情。

[![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/E901FD9A-269E-4C7F-83E9-9861A8CA0369.jpg)](http://fullrss.net/r/http/bbs.feng.com/aodoo3/click.php?n=a6444c89&zoneid=128)

以下为文章全文：

![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/C7A490EE-BDFA-477D-9DF3-07FFC36CFA72.jpg)

  
　　对于用不惯 OS X 的用户来说，如何翻来覆去的作死，给自己心爱的 Mac 装上 Windows 系统，是一件急需解决的事情。今天，小编就给大家带来了锋友 liuxl17 提供的自制 Windows 镜像、给 Mac 安装双系统的简易教程，一起来看看吧。  
  
　　通常，Mac 用户想要安装 Windows 系统的话，第一时间想到的就是 Boot Camp 这款能让你安装并运行 Windows 的应用软件，但是使用这个软件最大的问题是，你需要用它把镜像文件(所谓镜像，是把一系列文件按照某种特定格式制作成单一文件，最基本的特点是可以被特定软件识别并且可以直接刻录到光盘上。它可以说是光盘的“提取物”)转化到 Windows 系统的引导 U 盘上，过程繁琐不说，还容易出现无法引导的状况。  
  
　　在这样的情况下，我们可以考虑换个办法，比如使用 Winclone。Winclone 是一个运行于苹果电脑 Mac OS X 系统下的类似 PC 电脑 Ghost 的软件，它可以直接调用 Boot Camp 来修复引导，避免启动不了的问题。  
  

![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/1FFA44D9-F408-4B54-AA21-D097EB763974.jpg)

  
　　**在开始具体操作之前，我们需要做好以下准备工作：**  
  
　　· 一块 SSD 固态硬盘(速度比较快)  
  
　　· 一个 USB 转换器，硬盘盒子也行  
  
　　· 一个 U 盘和一台电脑(电脑主要用于将 Windows 系统安装到 SSD 固态硬盘)  
  
　　· Windows 系统安装文件(最好是纯净版的，必须是 NTFS 格式)  
  
　　**接下来，开始进入动手操作部分：**  
  
　　1. 首先，我们要进行 Winclone 镜像文件的制作。安装纯净版 Win 系统之后，将 SSD 固态硬盘从电脑上拆下来，接到 USB 转换器或硬盘盒子上，并与 Mac 连接。  
  
　　2. 打开 Winclone 软件，将 SSD 里的系统做成镜像文件 Win.winclone。  
  
　　3. 尽管我们使用的是 Winclone，但还是要按照 Boot Camp 的规则创建一个 NTFS 格式的 Win 盘，后期需要用上的，别忘了这一点。  
  

![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/08B948F7-39BA-42C7-8F0E-3A6B979BDBBB.jpg)

  
　　4. 将 Win.winclone 镜像文件恢复到第三步所说的 Win 盘，这时候我们会看到一个选择更改 BCD 文件(通过不同的 BCD 文件来实现直接启动不同的系统)的选项，然后 Winclone 会自动调用 Boot Camp 软件来修改 Mac 的启动盘。  
  
　　5. 重启 Mac 之后，系统会自动导入 Win 盘，识别系统硬件。再次重启（记得按住 ALT 键），安装 Boot Camp 驱动等软件就可以了。  
  

![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/0A1958E6-DFEF-4FF3-A764-C41CA6A12B63.jpg)

  
　　这样一个看似复杂的教程其实很容易完成，liuxl17 本人还分享了自己安装 Windows XP 系统的最新进展，想要了解更多详情的锋友可以点击[这里](http://fullrss.net/r/http/bbs.feng.com/forum.php?mod=viewthread&tid=8971114&extra=page=1&filter=author&orderby=dateline&orderby=dateline)进入帖子原文，一起来谈谈自己的安装心得吧。

[[文章纠错]](http://fullrss.net/r/http/kf.feng.com/problem/welcome/submit/7.html?url=http%3A%2F%2Fwww.feng.com%2Fapple%2FMAC%2F2015-04-02%2FTutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml&title=%E6%95%99%E7%A8%8B%EF%BC%9A%E8%87%AA%E5%88%B6Windows%E9%95%9C%E5%83%8F%E7%BB%99Mac%E5%AE%89%E8%A3%85%E5%8F%8C%E7%B3%BB%E7%BB%9F)

分享到：

### 投票调查

* 投票 1
* 投票 2
* 投票 3
* 投票 4
* 投票 5
* 投票 6

[提交](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml)

9.5

### 推荐阅读

* [![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/43F123B5-FDE1-46C7-A62A-8A79B96B9057.jpg)](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Powerful-image-editing-Mac-version-Pixelmator-half-price-promotions_611350.shtml)

  [强大的图片编辑Mac版Pixelmator半价促销](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Powerful-image-editing-Mac-version-Pixelmator-half-price-promotions_611350.shtml)
* [![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/76C15ACF-D386-406F-882E-68CB0AF75B1A.jpg)](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-01/Apple-vs-Intel-do-you-think-it-is-imperative-to-ARM-the-Mac_611275.shtml)

  [苹果vs Intel：你认为ARM Mac势在必行吗？](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-01/Apple-vs-Intel-do-you-think-it-is-imperative-to-ARM-the-Mac_611275.shtml)
* [![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/4A4E0165-04AD-43F2-AC8A-7773882440D0.jpg)](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-25/Apple-will-open-Force-Touch-API-ecological-will-be-more-rich_610694.shtml)

  [苹果将开放Force Touch API:生态会更丰富](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-25/Apple-will-open-Force-Touch-API-ecological-will-be-more-rich_610694.shtml)
* [![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/09F1DFD5-A508-445E-B431-25C9F5681E89.png)](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-24/For-nearly-30-years-ago-Mac-Plus-can-also-browse-the-web-page-now_610598.shtml)

  [将近30年前的Mac Plus也能浏览现在的网页](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-24/For-nearly-30-years-ago-Mac-Plus-can-also-browse-the-web-page-now_610598.shtml)

#### 相关阅读：

* [9个市场齐了! Watch登加拿大时尚杂...](http://fullrss.net/r/http/www.feng.com/apple/news/2015-04-02/Nine-market-together-_611397.shtml)04-02
* [愚人节的礼物: iFixit带来苹果手表...](http://fullrss.net/r/http/www.feng.com/apple/news/2015-04-02/April-fool-s-day-gift-iFixit-brings-apple-watches-the-latest-apart_611389.shtml)04-02
* [库克彻底走出乔布斯阴影 树立独有...](http://fullrss.net/r/http/www.feng.com/apple/news/2015-04-02/Cook-completely-out-of-jobs-Set-up-the-unique-leadership-style_611381.shtml)04-02
* [苹果IBM再推八款企业应用 主攻医疗...](http://fullrss.net/r/http/www.feng.com/apple/news/2015-04-02/Apple-IBM-another-eight-major-medical-and-industrial-enterprise-applications_611377.shtml)04-02
* [英媒：亲自接触苹果手表后就会忍不...](http://fullrss.net/r/http/www.feng.com/apple/news/2015-04-02/UK-media-personal-contact-apple-after-watch-can-t-help-pay_611371.shtml)04-02
* [Force click交互给Mac带来了全新的...](http://fullrss.net/r/http/www.feng.com/apple/macbook/2015-04-02/Force-click-interaction-for-Mac-has-brought-new-possibilities_611370.shtml)04-02
* [真果粉 由苹果设备打造起来的车载...](http://fullrss.net/r/http/www.feng.com/apple/news/2015-04-02/True-fan-Build-up-in-car-entertainment-systems-by-apple-devices_611369.shtml)04-02

#### 本栏目的其它文章：

* [强大的图片编辑Mac版Pixelmator半...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-02/Powerful-image-editing-Mac-version-Pixelmator-half-price-promotions_611350.shtml)04-02
* [苹果vs Intel：你认为ARM Mac势在...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-04-01/Apple-vs-Intel-do-you-think-it-is-imperative-to-ARM-the-Mac_611275.shtml)04-01
* [苹果将开放Force Touch API:生态会...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-25/Apple-will-open-Force-Touch-API-ecological-will-be-more-rich_610694.shtml)03-25
* [将近30年前的Mac Plus也能浏览现在...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-24/For-nearly-30-years-ago-Mac-Plus-can-also-browse-the-web-page-now_610598.shtml)03-24
* [了解手中的设备 让科技服务生活之...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-16/To-understand-the-hands-of-the-equipment-Let-the-service-life-of-the-152th-issue-of-science-and-technology_609902.shtml)03-16
* [25年后 Photoshop 1.0 和 Mac 再遇...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-16/Five-years-later-Photoshop-1.0-and-Mac-again-how_609860.shtml)03-16
* [这机械键盘适配Mac: 青轴茶轴可选...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-03-16/This-mechanical-keyboard-adapter-Mac-green-tea-axis-optional-costs-one-thousand-yuan_609857.shtml)03-16

![](.evernote-content/C0DD9714-1E9C-47FE-8F64-502E5A9A66B4/1A8D1F12-A2EC-4FC8-BBE5-EC42B9849E41.gif)

[fullrss.net](http://fullrss.net/)

---

[🌐 原始链接](http://www.feng.com/apple/MAC/2015-04-02/Tutorial-homemade-mirror-for-Mac-installed-double-Windows-system_611399.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/394276f6-01d8-44e2-9073-18a86cf35406/394276f6-01d8-44e2-9073-18a86cf35406/)