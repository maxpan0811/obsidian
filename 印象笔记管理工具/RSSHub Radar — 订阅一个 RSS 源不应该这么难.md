# RSSHub Radar — 订阅一个 RSS 源不应该这么难

---

RSSHub Radar — 订阅一个 RSS 源不应该这么难
===============================

RSSHub 是一个用来制作 RSS 订阅源的工具。与 Huginn、Feed43 等工具类似，RSSHub 在大部分网站上也是通过抓取网页的方式获得订阅源，不同的是在 RSSHub 中，已经完成了对抓取规则的编写，只需要用户简单的编辑下地址即可。

比如我希望订阅 YouTube 上 Linus Tech Tips 的视频，我在网页上找到 LTT 的用户名是「LinusTechTips」，根据 RSSHub 的 官方文档，我只需要在 `https://rsshub.app/youtube/user/` 之后加上这个用户名，即 `https://rsshub.app/youtube/user/LinusTechTips`，一个订阅源就制作完成了。

![](.evernote-content/A21223A4-2A2E-4081-B7C5-FAC36BDA3B55/9EA28E0D-6236-4691-81AB-5819F247A64B.png)

关联阅读：[通过 RSSHub 订阅不支持 RSS 的网站](https://beta.sspai.com/post/47100)

订阅一个 RSS 源太难了
-------------

RSSHub 上目前提供各类型的、总计超过 100 个网站的订阅源制作，而且随着参与者队伍的壮大，订阅源的数量还在快速上升中。从社交媒体到教务通知、从程序跟新到气象预警，只要你能想到的都会有不同的参与者开发完成。其中部分网站还提供多种订阅方式，比如 YouTube 可以订阅用户和频道、Telegram 可以订阅频道和贴纸包等等。

但是即使如此，一个普通用户想要订阅 RSS 还是非常不方便。首先你需要确保网站提供了 RSS（这一前提通常就无法满足）；然后我们要随缘在页面中找到 RSS 链接；接着复制链接，打开 Feedly、Inoreader 等 RSS 服务，点击添加订阅，粘贴链接，确认添加，如此重复下来，耐心已经消耗殆尽。

看，顺利订阅一个 RSS 源需要天时（随缘找到了 RSS）、地利（网站提供了 RSS）、人和（不因为订阅步骤过于麻烦而中途放弃），缺一不可。

都 9102 年了，世界不应该这样。

解决这个问题
------

为了解决这个问题，RSSHub Radar 诞生了。你可以通过下述链接安装使用：

[Chrome Web Store](https://chrome.google.com/webstore/detail/rsshub-radar/kefjpfngnndepjbopdmoebkipbgkggaa) | [GitHub](https://github.com/DIYgod/RSSHub-Radar)

RSSHub Radar 是 RSSHub 的衍生项目，它是一个可以帮助你快速发现和订阅当前网站 RSS 和 RSSHub 的浏览器扩展。

使用很简单，我们在进入一个新页面时，RSSHub Radar 会自动检测当前页面有没有 RSS 和 RSSHub 支持，检测到则会在右下角显示一个角标。如果我们想订阅当前页面的 RSS，点击扩展图标，会弹出一个列表，如图所示，列表有三项内容：当前页面上的 RSS、适用于当前页面的 RSSHub、适用于当前网站的 RSSHub，你可以选择复制链接或一键订阅到 Feedly、Inoreader 或者 TinyTinyRSS。

![](.evernote-content/A21223A4-2A2E-4081-B7C5-FAC36BDA3B55/D51418D5-02FB-46DA-AD05-61E5C5790D2B.jpg)

RSSHub Radar

设置页允许你使用自建的 RSSHub 域名、设置快捷键、立即更新规则、选择一键订阅到 TinyTinyRSS 还是 Feedly Inoreader、选择是否开启角标提醒等

![](.evernote-content/A21223A4-2A2E-4081-B7C5-FAC36BDA3B55/E3966052-C678-459E-99BF-E7DBA8D083D9.jpg)

设置

支持列表则列出了当前支持的 RSSHub 规则。

![](.evernote-content/A21223A4-2A2E-4081-B7C5-FAC36BDA3B55/1AF5A848-DEB0-4207-AEBB-D73B3A61E4EC.jpg)

支持列表

RSSHub Radar 是如何工作的
-------------------

RSSHub Radar 是开源的，你可以直接去 [GitHub](https://github.com/DIYgod/RSSHub-Radar) 看源码。

当我们进入一个新页面时，RSSHub Radar 开始检测当前页面的 RSS 和 RSSHub。

### 当前页面自带的 RSS

分析页面中的每个链接显然是不现实的，好在标准中指定了一种特殊 MIME 类型的 link 标签来指明 RSS 链接：`link[type="application/rss+xml"]` 和 `link[type="application/atom+xml"]`，RSSHub Radar 正是通过这个标签来检测页面是否有自带 RSS，具体实现在 [这里](https://github.com/DIYgod/RSSHub-Radar/blob/master/src/js/content/utils.js#L14)。

### 适用于当前页面的 RSSHub

使用 [给定规则](https://github.com/DIYgod/RSSHub/blob/master/assets/radar-rules.js)，根据当前页面的 URL 或 DOM 来获取 RSSHub 链接，规则各个字段的具体含义见 [文档](https://docs.rsshub.app/joinus/#%E6%8F%90%E4%BA%A4%E6%96%B0%E7%9A%84-rsshub-radar-%E8%A7%84%E5%88%99)，具体实现在 [这里](https://github.com/DIYgod/RSSHub-Radar/blob/master/src/js/background/utils.js#L111)。

为了让插件显示的 RSSHub 保持更新，RSSHub Radar 每隔 5 个小时就会从 GitHub 远程更新一次规则。

### 一键订阅

Feedly、Inoreader 和 TinyTinyRSS 都提供了用于订阅的接口，不同的是 Feedly 需要进入页面确认一下，而另外两个会直接订阅上。

比如访问这个 URL 可以快速使用 Feedly 订阅我的博客（需要点 FOLLOW 确认）：

`https://feedly.com/i/subscription/feed/https://diygod.me/atom.xml`

而这个 URL 可以快速使用 Inoreader 订阅我的博客：

`https://www.inoreader.com/feed/https://diygod.me/atom.xml`

参与我们
----

如果你对 RSSHub 感兴趣，欢迎 [参与](https://docs.rsshub.app/joinus/) 或 [支持](https://docs.rsshub.app/support/)我们。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/56079)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2238d8cf-429b-4c00-a714-2969fc3c89a6/2238d8cf-429b-4c00-a714-2969fc3c89a6/)