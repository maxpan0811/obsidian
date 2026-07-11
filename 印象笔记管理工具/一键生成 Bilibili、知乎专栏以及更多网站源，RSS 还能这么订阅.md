# 一键生成 Bilibili、知乎专栏以及更多网站源，RSS 还能这么订阅

---

[少数派](https://sspai.com/)

登录

* [专题广场](https://sspai.com/topics)
* [Matrix](https://sspai.com/matrix)
* [付费栏目](https://sspai.com/series)
* [效率工具](https://sspai.com/tag/%E6%95%88%E7%8E%87%E5%B7%A5%E5%85%B7#home)
* [手机摄影](https://sspai.com/tag/%E6%89%8B%E6%9C%BA%E6%91%84%E5%BD%B1#home)
* [生活方式](https://sspai.com/tag/%E7%94%9F%E6%B4%BB%E6%96%B9%E5%BC%8F#home)
* [游戏](https://sspai.com/tag/%E6%B8%B8%E6%88%8F#home)
* [硬件](https://sspai.com/tag/%E7%A1%AC%E4%BB%B6#home)

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/250055DF-27F7-417C-8511-6C682950372B.jpg)

一键生成 Bilibili、知乎专栏以及更多网站源，RSS 还能这么订阅
====================================

[![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/944993EB-C64A-4191-91B2-3BBB550006D1.png)](https://sspai.com/user/731139)

#### [Minja](https://sspai.com/user/731139)

12月21日

81 17

我一直认为，订阅 RSS 是一种近乎手工艺的劳动，尤其当我遇到了不提供现成 RSS 源的网站，还得想方设法为它生成订阅源。非常幸运的是，已经有不少开发者为热门网站制作了生成 RSS 地址的工具，我所做的不过是在他们劳动成果上为 RSS 阅读事业添砖加瓦，做了一个让「生成 RSS 地址」这一步更加轻松的小工具，希望 RSS 用户们会喜欢。

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/46262EEB-D843-4289-A3B5-81454E9D564F.gif)

本文以订阅 Bilibili 和知乎为例。

生成 RSS 地址
---------

首先感谢 [DIYGod](https://diygod.me/3264/ "DIYGod") 和 [lilydjwg](https://rss.lilydjwg.me/ "lilydjwg")，是他们造好了轮子，让我们可以轻松生成 Bilibili 和知乎的 RSS 地址。

不过，每次都打开生成工具的网页，总是麻烦了一些；实际上，各个生成工具的作者也常常指出，只需要把目标站点的部分网址（往往是末尾那一串数字和字母组合）取出作为「后缀」，和生成工具的提供的地址「前缀」组合，就获得一个可用的订阅源了。

所以我做了这个简单的 AppleScript 脚本（下例用于订阅 Bilibili up 主），**不打开生成工具网页，直接在当前页面制作订阅源：**

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/E0FA1D2B-F20A-4711-ACEA-CC0A8B5222F0.png)

中间四行主要部分的作用分别是：

1. 获取当前 up 主空间地址；
2. 取出其特殊的字段，这里是空间地址最后几位数字；
3. 和生成工具地址拼接；
4. 把生成的 RSS 地址拷贝到剪贴板。

于是一个 RSS 地址就做好了。其中取出特殊字段的脚本用到了[正则表达式](https://zh.wikipedia.org/zh-hant/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F "正则表达式")，表示「取出最后几位数字」。即便丝毫不懂编程。你也可以花上不多的时间学学它，这将是一次性价比非常高的学习。

为了在 Bilibili 番剧、知乎专栏等网页都可以用同一个脚本来订阅，我再加了一点判断（蓝色部分），不同的网页进行对应的取出、拼接操作。

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/31421C2E-5BE4-4156-BA69-982D1728BA2A.png)

你用得着的网页，也大可如法炮制，一个一个往脚本里添加。

至于运行，没有装第三方自动化工具的读者可以使用系统自带脚本编辑器，在勾选其设置中的「Show Script in menu bar」，并把脚本丢到 `/Users/apple/Library/Scripts` 下，就能随时从菜单栏召唤来用，获取当前页面的 RSS 订阅地址。

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/970236CC-0986-4A95-9734-88DA31B2C47B.png)

🤔️**为什么要用 RSS 来订阅 Bilibili**

订阅知乎我想多数人还可以理解，毕竟只是看个文章，那么 Bilibili 呢？我当然不是要在 RSS 阅读器里看视频，而是为了**接收 up 主和番剧更新的通知**。这就跟使用 BB 机一样，「有更新哦」，就去看一下。

添加进阅读器
------

我有一点强迫症，尽管不差打开手动阅读器那几秒，但我还是希望机器能帮我完成，下面只是适合我个人的一种思路，如果你有其他的应用场景与方法，也不妨在评论里留言。

每个阅读器的添加方式不同，有的直接开放了 API、URL Schemes 或者 AppleScript 接口，不过我使用的 Reeder 3 却没有提供上述任何一者，无奈我只能使用 Keyboard Maestro 做了一个动作：

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/26D3F187-4AD9-4F37-8FE4-C271CD766B5B.png)

其实这就是模拟了一遍打开 Reeder 3、添加地址的流程，简单粗暴，效果就是文章开头那样：

![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/46262EEB-D843-4289-A3B5-81454E9D564F.gif)

如果你不经常订阅 RSS，就不用特意为它设置快捷键，只需让这个动作显示在 Keyboard Maestro 的菜单栏里，毕竟没有多少人每天都要添加一大堆 RSS 地址嘛（我例外 :p ）。

小结
--

使用 RSS 的好处用过自知，我可以在一处阅读几乎所有感兴趣的内容，并且尽可能减少广告带来的影响，也避免了部分网页别有用心的追踪。我根据自己需求，让当前的脚本支持了 Bilibili、知乎和微博，其他热门网站的生成方式在文末有项目地址。

如果这篇文章能让你更舒服地使用 RSS，我就非常满意了。

---

感谢开发者：

订阅 Bilibili up 主和番剧：[DIYGod](https://diygod.me/3264/ "DIYGod")

订阅微博：[DIYGod](https://github.com/DIYgod/Weibo2RSS "DIYGod")

订阅知乎专栏：[lilydjwg](https://rss.lilydjwg.me/ "lilydjwg")

订阅 V2EX：[lilydjwg](https://rss.lilydjwg.me/ "lilydjwg")

---

脚本下载： [某云](https://pan.baidu.com/s/1bGMBAe "某云")

注：工具只能直接用于 Mac，熟悉原理亦可在其他操作系统上自制。

[bilibili](https://sspai.com/tag/bilibili) [稍后读](https://sspai.com/tag/%E7%A8%8D%E5%90%8E%E8%AF%BB) [阅读](https://sspai.com/tag/%E9%98%85%E8%AF%BB) [RSS](https://sspai.com/tag/RSS)

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

---

81

---

[![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/E68FE869-83F4-4451-A887-395877F11D8C.png)](https://sspai.com/user/731139)

#### 

#### [Minja](https://sspai.com/user/731139)

平面设计，汉字输入，macOS 自动化

关注

:   [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/a/npRP "应用宝征文")

---

发送

### 评论（17）

* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/747979)

  ##### [Jamella](https://sspai.com/user/747979)

  自己造了一个可为任意页面生成全文rss的轮子，算是缅怀yahoo pipe
    
  https://github.com/Boneflame/gpipe43

  2天前

  举报 回复
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/798144)

  ##### [董汉臣](https://sspai.com/user/798144)

  授人鱼不如授人渔，不是说各个生成工具的作者也常常指出，只需要把目标站点的部分网址（往往是末尾那一串数字和字母组合）取出作为「后缀」，和生成工具的提供的地址「前缀」组合，就获得一个可用的订阅源了。关键的是生成工具提供的前缀怎么弄啊，你这个不是只能订阅bb和知乎吗？

  2天前

  举报 回复
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/755674)

  ##### [Fedrov](https://sspai.com/user/755674)

  小白表示没懂起啊 。。。。我是不是很笨。

  2天前

  举报 回复
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/798035)

  ##### [吴三水](https://sspai.com/user/798035)

  知乎专栏好像直接用专栏的地址就可以订阅了。。。
    
   一直用http://jianshu.milkythinking.com这个工具订阅简书文章，但是好像最近不好使了，作者你这个方法可以订阅简书的么。。。

  12月21日

  举报 回复
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/717119)

  ##### [SCheng](https://sspai.com/user/717119)

  Make RSS great again!

  12月21日

  举报 回复 4
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/759132)

  ##### [joysisyphu](https://sspai.com/user/759132)

  bilibili那个运行良好，但是订阅知乎专栏的功能在我这里不工作。
    
  请问为什么蓝字部分可以解决知乎专栏的订阅，set theURL to URL of front document并没有对知乎专栏的网址进行处理啊

  12月21日

  举报 回复

  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/731139)

    ##### [Minja](https://sspai.com/user/731139)

    joysisyphu君：
      
      
    我重新涂了一遍颜色，看看这次的蓝色 if 部分。

    12月21日

    举报 回复
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/759132)

    ##### [joysisyphu](https://sspai.com/user/759132) 回复 [Minja](https://sspai.com/post/42401)

    如果我没理解错的话，这样不是对知乎专栏的链接没有处理吗？
      
    我刚自己写了知乎专栏的
      
    if theURL contains "zhihu.com" then
      
     do shell script "str=" & theURL & "
      
     echo ${str##\*com}"
      
     set rssURL to "https://rss.lilydjwg.me/zhihuzhuanlan" & result as string
      
     set the clipboard to rssURL
      
     end if

    12月21日

    举报 回复
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/731139)

    ##### [Minja](https://sspai.com/user/731139) 回复 [joysisyphu](https://sspai.com/post/42401)

    你没有理解错，我就是让你「你用得着的网页，也大可如法炮制，一个一个往脚本里添加」

    12月21日

    举报 回复
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/680229)

    ##### [Ponderous](https://sspai.com/user/680229)

    https://rss.lilydjwg.me/zhihuzhuanlan/XXXX
      
    XXXX处换成专栏名，例如
      
    https://zhuanlan.zhihu.com/junyue
      
    亲测有效的。

    1天前

    举报 回复
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/759132)

    ##### [joysisyphu](https://sspai.com/user/759132) 回复 [Ponderous](https://sspai.com/post/42401)

    嗯，我贴的那段代码就是自动解决这个问题的，只是一开始我误以为Minja的代码已经解决了知乎的问题

    16小时前

    举报 回复
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/703655)

  ##### [Milisa](https://sspai.com/user/703655)

  最后提供的这个github订阅微博的工具，并不能抓取一条微博的所有图片，全部只显示第一张。之前一直用的微博档案貌似停止服务了，虽然之前订阅的还在推送，但无法增加新的订阅。所以微博这项还暂时无解。

  12月21日

  举报 回复

  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/798016)

    ##### [白菜丶](https://sspai.com/user/798016)

    https://api.izgq.net/weibo/这个服务可以获取一条微博的所有图片，昨晚亲测过了

    12月21日

    举报 回复 1
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/703655)

    ##### [Milisa](https://sspai.com/user/703655) 回复 [白菜丶](https://sspai.com/post/42401)

    感谢!! 我试试看

    12月21日

    举报 回复
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/703655)

    ##### [Milisa](https://sspai.com/user/703655) 回复 [白菜丶](https://sspai.com/post/42401)

    好像不能使用了

    12月21日

    举报 回复
  + [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/798016)

    ##### [白菜丶](https://sspai.com/user/798016) 回复 [Milisa](https://sspai.com/post/42401)

    可以用的，只是那个网页有点问题。。。https://api.izgq.net/weibo/rss/{微博博主的uid}通过这个使用就好了

    2天前

    举报 回复
* [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/703655)

  ##### [Milisa](https://sspai.com/user/703655)

  感觉RSS工具又完整了一块，开心
    
  感谢！

  12月21日

  举报 回复

### 关联阅读

[![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/724096) #### [Eric\_hong](https://sspai.com/user/724096) 12月16日
:   [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/post/42184)

    ### [除了 Pocket 和 Instapaper，还有更多简单实用的稍后读工具](https://sspai.com/post/42184)

    前段时间，苹果 App Store 商店由于神秘原因下架了 Instapaper 和 Pocket 两款大热的稍后读应用（Android 玩家表示淡定），虽然少数派已经分享了「已经从 App Stor...

    30 49

[![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/647567) #### [挨石](https://sspai.com/user/647567) 11月23日
:   [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/post/41961)

    ### [使用书摘 App 集中管理所有读书笔记](https://sspai.com/post/41961)

    要在纸书与电子书之间做出抉择的话，除了书籍数量、便捷性等因素，能否高效记录读书笔记也是一大考量，而在此方面电子书通常是完胜的。但即便都是电子书，由于版权的限制我们也不得不同时在 Kindle、豆瓣阅读...

    45 21

[![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/684386) #### [huhuhang](https://sspai.com/user/684386) 06月14日
:   [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/post/39242)

    ### [为什么 NewsBlur 是我最喜欢的 RSS 服务](https://sspai.com/post/39242)

    RSS 作为一种轻便的内容聚合服务，一直以来都是许多读者阅读资讯的主要手段。虽然，Google 在 2013 年就关闭了旗下的 Google Reader 服务，但这并未浇灭大家对于 RSS 的热情。...

    62 29

[![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/user/681230) #### [JailbreakHum](https://sspai.com/user/681230) 04月14日
:   [![](.evernote-content/DEE01BFF-F9B4-4A1A-857B-D412B8EBBA86/234E06B1-55CC-4336-BC2E-0B4826F0008A.gif)](https://sspai.com/post/38794)

    ### [唯一完全支持 iOS 外接键盘操作的 RSS 阅读器：Fiery Feeds 深度测评](https://sspai.com/post/38794)

    请输入图片标题操作惯性这个点很有意思。一般来说，我们会觉得用 Apple Pencil 去执行 iPad 上的界面操作是很矫情的事，但当你用 Apple Pencil 记过笔记之后，就会自然而然地用它...

    31 9

* [支持我们](https://sspai.com/page/support)
* [作者招募](https://sspai.com/apply/writing)
* [用户协议](https://sspai.com/post/37739)
* [FAQ](https://sspai.com/post/37793)
* [Contact Us](https://sspai.com/post/42401)

© 2013-2017 [少数派](https://sspai.com/post/42401) | [粤ICP备09128966号-4](http://www.miitbeian.gov.cn/) | CC BY-NC 4.0

App 打开

---

[🌐 原始链接](https://sspai.com/post/42401)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f88ba28c-7509-49e2-824b-77c76e54db59/f88ba28c-7509-49e2-824b-77c76e54db59/)