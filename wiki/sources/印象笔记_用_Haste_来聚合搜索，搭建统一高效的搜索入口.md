---
title: "用 Haste 来聚合搜索，搭建统一高效的搜索入口"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/用 Haste 来聚合搜索，搭建统一高效的搜索入口.md
tags: [印象笔记]
---

# 用 Haste 来聚合搜索，搭建统一高效的搜索入口

# 用 Haste 来聚合搜索，搭建统一高效的搜索入口 --- 用 Haste 来聚合搜索，搭建统一高效的搜索入口 ========================= 1小时前 [![](.evern

---

# 用 Haste 来聚合搜索，搭建统一高效的搜索入口

---

用 Haste 来聚合搜索，搭建统一高效的搜索入口
=========================

1小时前

[![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/1654D8D3-B56B-4448-A32D-AC64488854EB)](https://sspai.com/user/734392) [Adventure](https://sspai.com/user/734392) 责编: [Minja](https://sspai.com/user/731139)

目录
:   1. [快速调出搜索窗](https://sspai.com/post/47117#ss-H2-1536811610009)
    2. [本地搜索同样在行](https://sspai.com/post/47117#ss-H2-1536811618943)
    3. [自定义搜索引擎](https://sspai.com/post/47117#ss-H2-1536811622769)
    4. [进阶操作：使用搜索语法](https://sspai.com/post/47117#ss-H2-1536811628334)
    5. [小结](https://sspai.com/post/47117#ss-H2-1536768940639)

搜索，是现代人的基本技能。

然而，我们的搜索习惯一般是怎样的？打开浏览器、点击输入框、输入关键词、按下回车。这套常见的搜索流程算不上高效。此外，我们可能需要在不同的网页进行搜索，如何快速找到需要的搜索引擎也是个问题；如果要在购物网站搜索，没准还要忍受几个首页广告。

聚合搜索是一个有效的办法。iOS 设备可以借助少数派此前介绍的 [捷径动作](https://www.icloud.com/shortcuts/1741ab3496cc419bbc7a71783cab218d)；在 macOS 上，进阶用户可能已经在通过 [LaunchBar](https://www.obdev.at/products/launchbar/index.html)、[Alfred](https://www.alfredapp.com/) 等工具实现聚合搜索。我个人用 [Keyboard Maestro](http://www.keyboardmaestro.com/main/) 创建了动作，在我输入搜索内容后，调出常用的搜索引擎供我选择。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/FB0810BF-C179-4F53-99FE-50C48AF33EE6.gif)

Keyboard Maestro 聚合搜索

可惜的是，这些应用都有一定的使用门槛，再加上不算低的价格，导致不少人对它们敬而远之，依然采用最传统的方式进行搜索。

上架 Mac App Store 不久的 [Haste](https://itunes.apple.com/cn/app/haste-quick-web-search/id1175250324?mt=12) 为我们提供了一个全新的选择。它简单易用，又有足够强大的功能，免费版也已足够好用。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/E86B327A-A139-4FFF-BD59-359E5B9A5459.png)

#### Haste - Quick web search

Mac

[相关文章](https://sspai.com/app/Haste%20-%20Quick%20web%20search)

下载

在我们的期望中，一个优秀的聚合搜索应该满足这些条件：

* 能够方便地调出应用和选择搜索引擎；
* 能够快速获取搜索内容；
* 自定义设置方便，可以自行添加所需搜索引擎。

而 Haste 在满足了以上条件的同时，还有一些额外的惊喜。

快速调出搜索窗
-------

Haste 的默认激活方式是双击 ⌘Command 键，你也可以在偏好设置中根据习惯调整。在输入搜索内容的时候，Haste 会像搜索引擎一样猜测你要输入的全文，你可以直接通过⌘Command + 数字的方式选择。如果你用过 LaunchBar 和 Alfred，不难发现双击呼出和数字选择正是这两个启动器的亮点功能，而 Haste 将两者集合在了一起。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/9B6FC45D-1765-41A8-B5DF-1A2D27C56A95.png)

注意右侧显示的快捷键

确认搜索内容后，你就可以选择本次搜索使用的搜索引擎。Haste 默认提供了不少网站供你选择，并已经为它们设置了相应的快捷键。例如，G 对应了 Google 搜索，W 对应了维基百科。这样设置快捷键固然方便记忆，但也难免会产生重复。例如，Google 图片和 GitHub 的符合直觉的快捷键也应该是 G。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/C8CE3225-A457-4129-B264-EDF74CFEB31C.png)

一个快捷键对应了多个网站

Haste 用一个巧妙的方法避免了这一麻烦。如果你使用过 Keyboard Maestro，一定不会对这个功能陌生。1

Haste 可以最多为一个网站依次设置三个快捷键，如 Google 图片（Google Image）的默认快捷键是 GI。当你按下 G 之后，Haste 会筛选出所有首位快捷键是 G 的网页，并默认选中快捷键只有 G 的 Google 搜索。你可以按下回车使用该搜索引擎，也可以再按下 I 来选中 Google 图片，按下回车键跳转搜索。这一功能让记忆和使用快捷键来选择网页变得极为便捷。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/17A7980C-82B2-484D-B492-8048B0B9592E.png)

除此之外，Haste 也没有忘记向 LaunchBar 看齐。LaunchBar 有一个功能叫做「Instant Send」。利用这一功能，可以通过快捷键快速将选中的文本发送给 LaunchBar。相比复制粘贴，这样操作方便了不少。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/C4670E3A-7081-412F-A5EB-5D2787B58B5A.gif)

Instant Send 功能

Haste 的「Copy and Haste」功能也可以实现类似的效果。选中文本并复制后，在一定的时间间隔之内调出 Haste，选中的文本就会自动粘贴到 Haste 的搜索栏。Haste 默认的时间间隔是 5s，你也可以在偏好设置中进行调整。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/D6695866-3669-42C1-A984-5E35213F5901.gif)

除此之外，Haste 还有一个浏览器插件，可以让该功能在浏览器中有更好的表现。你可以在它的偏好设置页面激活。针对可能的隐私问题，开发者也在该页面做出了相应承诺。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/F71406FF-382B-4929-A741-C3CC1B14DBED.png)

开启插件后，你只需在浏览器中选择文本，不再需要复制，调出 Haste 后文本就会自动显示在搜索栏。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/BBBA9502-2BC4-4167-B279-E063FAD65A95.gif)

本地搜索同样在行
--------

除了借助搜索引擎进行搜索，Haste 还聚合了部分本地应用，进一步拓展了搜索范围。目前，Haste 支持 macOS 原生的词典（快捷键 D）、地图（快捷键 M）和 App Store（快捷键 MAS）。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/A6DCE557-106A-4332-9CA4-26CA13084DFF.png)

对我来说，支持本地词典给 Haste 加分不少。结合 Haste 的自动填充功能，在我遇到陌生的词汇时，可以直接复制后调出 Haste，再一键转到词典，整个过程方便又高效。

自定义搜索引擎
-------

虽然 Haste 已经原生提供了不少搜索页面，但是它毕竟出自国外开发者之手，自带的网页不一定符合我们的需要。我们可以根据自己的需要，进一步地定制 Haste 中可用的搜索网页。

调出 Haste 主页面后，点击设置图标并选择「Edit Custom Searches」就打开了自定义界面。你也可以点击 Haste 在菜单栏的图标来实现。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/CDA16A79-5039-4438-AF5B-92601234878E.png)

对于你并不需要的网页，可以将其停用，或是干脆直接删除。你也可以对已经提供的网址进行修改。例如，Haste 提供的亚马逊网站为美亚，你可以将地区更改为国内。点击页面左下角的「+」可以自行添加新的搜索选项。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/E49ADACD-FDD6-4251-A07E-821A8FA5460D.png)

自定义页面

对于新添加的搜索页，标题栏和快捷键不必多说，但获取目标网站的 URL 则可能有一定的难度。

一般来说，搜索所使用的 URL 格式是这样的：

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/49293947-52A0-43BC-B7D1-0A0B0800E11A.png)

来源：《如何提高搜索的精度与速度》/ Minja

要想得到目标网站的 URL，你可以在该网站任意搜索一个关键词，提取搜索页面的网址，再对照通用的 URL 格式，就可以得到我们要提取的部分。需要注意的是，把 URL 填入 Haste 后，需要将 @haste 添加到网址中原来关键词所在的位置。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/4327F50D-A147-4EB4-8E93-B814E25AC3E6.png)

获取 Haste 可用的 URL 流程

@ [Umi](https://sspai.com/user/713147/updates) 在介绍 Alfred 的 [文章](https://sspai.com/post/43973)中，曾总结了常用搜索网站的 URL 地址。在此基础上，我为这些 URL 添加了 Haste 所需的 @haste，并把它们列在了下面。你可以根据自己的需要直接复制。

|  |  |
| --- | --- |
| 网站名称 | 搜索 URL |
| 少数派 | [https://sspai.com/search/article?q=@haste](https://sspai.com/search/article?q={query}) |
| 百度 | [https://www.baidu.com/s?wd=@haste](https://www.baidu.com/s?wd={query}) |
| 知乎 | [https://www.zhihu.com/search?q=@haste](https://www.zhihu.com/search?q={query}) |
| 豆瓣全站 | [https://www.douban.com/search?q=](https://www.douban.com/search?q={query})[@haste](https://sspai.com/search/article?q={query}) |
| 豆瓣电影 | [https://movie.douban.com/subject\_search?search\_text=](https://movie.douban.com/subject_search?search_text={query})[@haste](https://sspai.com/search/article?q={query}) |
| 简书 | [https://www.jianshu.com/search?q=](https://www.jianshu.com/search?q={query})[@haste](https://sspai.com/search/article?q={query}) |
| 微博 | [https://s.weibo.com/weibo/](https://s.weibo.com/weibo/%7Bquery%7D)[@haste](https://sspai.com/search/article?q={query}) |
| 微信文章 | [http://weixin.sogou.com/weixin?type=2&query=](http://weixin.sogou.com/weixin?type=2&query={query})[@haste](https://sspai.com/search/article?q={query}) |
| 优酷 | [https://www.soku.com/search\_video/q\_](https://www.soku.com/search_video/q_%7Bquery%7D)[@haste](https://sspai.com/search/article?q={query}) |
| 爱奇艺 | [https://so.iqiyi.com/so/q\_](https://so.iqiyi.com/so/q_%7Bquery%7D)[@haste](https://sspai.com/search/article?q={query}) |
| 哔哩哔哩 | [https://search.bilibili.com/all?keyword=](https://search.bilibili.com/all?keyword={query})[@haste](https://sspai.com/search/article?q={query}) |
| 中文维基百科 | [https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=](https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=Alfred)[@haste](https://sspai.com/search/article?q={query}) |
| 百度百科 | [https://baike.baidu.com/search/none?word=](https://baike.baidu.com/search/none?word={query}&pn=0&rn=10&enc=utf8)[@haste](https://sspai.com/search/article?q={query})[&pn=0&rn=10&enc=utf8](https://baike.baidu.com/search/none?word={query}&pn=0&rn=10&enc=utf8) |
| 淘宝 | [https://s.taobao.com/search?q=@haste](https://s.taobao.com/search?q={query}) |
| 京东 | [https://search.jd.com/Search?keyword=@haste](https://search.jd.com/Search?keyword={query}) |
| 什么值得买 | [http://search.smzdm.com/?s=@haste](http://search.smzdm.com/?s={query}) |
| 亚马逊中国 | <https://www.amazon.cn/s/&field-keywords=@haste> |
| Pexels | [https://www.pexels.com/?s=@haste](https://duckduckgo.com/?q={query}) |
| DuckDuckGo | [https://duckduckgo.com/?q=@haste](https://duckduckgo.com/?q={query}) |
| Stack Overflow | [https://www.stackoverflow.com/search?q=@haste](https://www.stackoverflow.com/search?q={query}) |

当当：<http://search.dangdang.com/?key=@haste&act=input>

除了这篇文章以外，@ [Tp](https://sspai.com/user/749322/updates) 还曾经分享过一些实用的专用搜索引擎。你也可以根据上文，自行添加需要的搜索引擎。

参考文章：《 [这 8 个专用搜索引擎，帮你从海量信息中找到真正需要的那一个](https://sspai.com/post/45325)》。

进阶操作：使用搜索语法
-----------

要实现良好的搜索效果，除了选择合适的搜索引擎，使用搜索语法也能起到很好的作用。

举例来说，如果你觉得少数派网站上的搜索功能不够理想，可以使用下面的 URL，借助 Google 进行搜索。

https://www.google.com/search?q=site:sspai.com+关键词

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/2F32CECD-9A64-4A17-A58F-88C4841076B9.png)

搜索效果

在这个例子中，我把关键词site:sspai.com放在了关键词之前，实现了在少数派的站点内搜索的目的。根据上文就可以知道，我们只需将 URL 添加到 Haste，并将其中的关键词更改为@haste，就可以打造一个进阶版的「少数派搜索」。

![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/4D7B4402-D56F-4DF7-84B8-A746FE789B24.png)

类似地，通过百度搜索少数派站内搜索的 URL 为：

https://www.baidu.com/s?wd=site:sspai.com @haste

你也可以将 URL 中少数派的网址更换，实现其他网站的站内搜索。除了site:，还有不少搜索语法同样实用。我将 Google 的常用搜索语法列在了下面：

* -关键词：不搜索减号后面的关键词，你可以借此排除那些可能造成干扰的的搜索结果。
* "关键词"：精准搜索引号内的关键词，和「精确匹配」作用一致。
* 关键词 filetype:文件格式：只搜指定格式的文件，适合用来找资料。
* &lr=zh-Hans：添加在 URL 后，查看中文搜索结果。
* lr=zh-Hant：添加在 URL 后，限制搜索结果语言为中文。
* hl=zh-CN：添加在 URL 后，限制搜索页面语言为中文。

对于其他网站，你也可以参考其官方文档，自行查找所需的搜索语法。少数派作者 @ [Eric\_hong](https://sspai.com/user/724096/updates) 就曾对 [GitHub](https://github.com/) 的搜索语法进行过深入的介绍。

参考文章：《 [掌握 3 个搜索技巧，在 GitHub 上快速找到实用软件资源](https://sspai.com/post/46061)》。

小结
--

总的来看，Haste 操作足够简单，非常容易上手，同时又有着强大的功能，足以成为你的主力聚合搜索工具。Haste 采用免费 + 内购的模式，免费版应用可以添加至多 5 个自定义搜索选项，付费 ¥ 40 解锁内购可以解除该限制。

你可以在 [Mac App Store](https://itunes.apple.com/cn/app/haste-quick-web-search/id1175250324?mt=12) 中下载 Haste。

---

> 下载 [少数派客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用

1. [当同一个快捷键对应了多个动作时，Keyboard Maestro 允许通过键入这些动作名称的第一个不同字母的方式进一步选择。](#)[↩](#)

[#](https://sspai.com/tag/%e6%95%88%e7%8e%87%e5%b7%a5%e5%85%b7)效率工具 [#](https://sspai.com/tag/%e6%95%88%e7%8e%87)效率 [#](https://sspai.com/tag/macOS)macOS

© 本文著作权归作者所有，并授权少数派独家使用，未经少数派许可，不得转载使用。

---

[15](#)

---

[![](.evernote-content/0536C81C-95C1-42B0-8A28-4ED89506565A/F513D599-11B1-499B-AD49-E3861F60CD48)](https://sspai.com/user/734392)

#### 

#### [Adventure](https://sspai.com/user/734392)

---

[🌐 原始链接](https://sspai.com/post/47117)

[📎 在印象笔记中打开](evernote:///view/207087/s1/54d8b3f1-2e3d-44d0-beb6-7e22428a486a/54d8b3f1-2e3d-44d0-beb6-7e22428a486a/)