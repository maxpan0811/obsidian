---
title: "其貌不扬，管理书签却是能手：Pinboard 入门指南"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/其貌不扬，管理书签却是能手：Pinboard 入门指南.md
tags: [印象笔记]
---

# 其貌不扬，管理书签却是能手：Pinboard 入门指南

# 其貌不扬，管理书签却是能手：Pinboard 入门指南 --- 在[《互联网匠人作品：「反社交」的书签服务 Pinboard.in》](https://sspai.com/post/38532)中

---

# 其貌不扬，管理书签却是能手：Pinboard 入门指南

---

在[《互联网匠人作品：「反社交」的书签服务 Pinboard.in》](https://sspai.com/post/38532)中，作者少楠介绍了 Pinboard 的前世今生以及分享了他本人使用 Pinboard 的工作流与实现效果。而这篇文章将另辟蹊径，旨在帮助一部分有针对性需求的读者，提供更多有关 Pinboard 使用的工具与技巧，帮助大家提高使用 Pinboard 的效率，但是本文不会涉及工作流的搭建和标签系统的使用等方面的内容。

在开始之前，我们不妨先来回顾一下 Pinboard 能提供什么功能，以及与其他同类服务相比有什么优势。读过前面那篇文章的读者们应该都知道，**Pinboard 是一个网络书签服务，提供了书签收藏、管理、存档和社交分享等功能。而与其他同类服务相比，Pinboard 的优势体现在服务稳定、搜索极速、管理灵活、接口开放等方面。**

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/9B6A78B5-386A-446E-9A83-1FD3A8B118A3.png)很「简陋」的 Pinboard 主页，但简单高效

如果你还希望在 Pinboard 上进行稍后读，那么与 Instapaper 和 Pocket 相比，Pinboard 的存档服务因为直接保存原网页的特性1，可以避免网页正文内容抓取失败等情况，同时在最大程度上保留了原网页的视觉效果。

在认清 Pinboard 的功能和优势后，如果你认为 Pinboard 能够满足你的需求，以及想了解如何高效地使用 Pinboard 这个服务，那么请你继续往下看。

书签手动添加
------

作为一个书签服务，最基础的功能一定就是添加书签了。Pinboard 官方给出了四种添加书签的方式：

* 第一种是直接在 Pinboard 的[网页版](https://pinboard.in/)右上角点击「add url」并输入网址来添加；
* 第二种是通过 Pinboard 官方的 [Bookmarklet](https://pinboard.in/howto/) 直接抓取当前网页添加为书签；
* 第三种是通过发送电子邮件到你的 Pinboard 邮箱地址2 来添加书签；
* 最后一种就是通过[浏览器插件](https://pinboard.in/resources/extensions/)来保存当前打开的所有网页为书签。

虽然这四种官方提供的办法是最稳定最简单的，但却不是最方便的。得益于 Pinboard 开放的 API，我们还可以通过各种第三方软件或者插件来更加方便地添加书签。

### LaunchBar

提起 Mac 上的效率软件，我们很难绕过 LaunchBar。所以意料之中的是，我们也可以通过 LaunchBar 来快速地添加书签到 Pinboard。在经过了对多个 Action 的试用后，我最终选择了这一个解决方案，大家可以通过 [GitHub](https://prenagha.github.io/launchbar/pinboard.html) 下载。

通过这个 Action，你可以直接将 Safari 的当前 Tab 显示的网页添加到 Pinboard。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/B51E8DDC-7970-4D1B-852B-F3823A7C3748.gif)

或者，你可以选中网址，然后通过 Instant Send 来将它发送到 Pinboard 添加为书签。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/9DFCE333-263B-4916-8494-F5378D006661.gif)

还有一个最粗暴的方式，就是直接在 LaunchBar 中输入网址，然后发送到 Pinboard 添加为书签。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/E10E738D-9846-4AE6-BB39-1A15B977BA81.gif)

这个 Action 几乎涵盖了你在 Mac 上添加书签到 Pinboard 的所有使用场景，你可以根据自己的需求来选择最方便的添加方式。不过值得注意的是，直接将 Safari 的当前 Tab 显示的网页添加到 Pinboard 的速度是最快的，耗时大概在1 秒左右。而另外两种方式需要耗费相当长的时间才能在完成 LaunchBar 的动作后把书签添加到 Pinboard，虽然不影响结果，但是需要更长的等待时间。

### Alfred

作为 LaunchBar 最直接的竞争对手，Alfred 也是可以完成添加书签到 Pinboard 这个任务的，两者的实现过程也非常接近。你可以从 [GitHub](https://github.com/spamwax/alfred-pinboard) 下载这个 Workflow，并安装使用。

安装后的第一步，你需要在 Alfred 中输入 `pa`，空一格后输入你的 Pinboard 账号对应的专属 API Token3，以此来关联你的 Pinboard 账号，然后你就可以使用这个 Workflow 通过 Alfred 对你的 Pinboard 完成一系列操作了。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/5BBCD052-A3F1-4E09-9A5A-DDAD24FDB2C2.png)

这个 Workflow 与前面提到的 LaunchBar 的 Action 相比，各有千秋。优势在于通过 Alfred 的这个 Workflow 你可以从 Chrome、Chromium、Firefox 和 Safari 添加网页到 Pinboard 作为书签，另外，你还可以通过 `p tag1 tag2 tag3 ; some optional note` 这个语句在添加书签的时候同时附上 Tag 和 Note；而劣势在于这个 Workflow 只能添加浏览器当前 Tab 显示的网页，不能通过其他方式。

### 第三方 Bookmarklet

之前提到的 Pinboard 官方 Bookmarklet 可以实现在抓取当前页面保存为书签的同时添加书签和设置稍后读等功能，但是你需要通过不同的 Bookmarklet 来实现不同的功能。如果你想使用同一个 Bookmarklet 来同时实现多个功能，那么你不妨给第三方 Bookmarklet 一个机会。

你可以从 [GitHub](https://gist.github.com/beh/3549933) 这个页面获取一段 javascript 代码：

```
javascript:q=location.href;if(document.getSelection){d=document.getSelection();}else{d='';};p=document.title;void(open('https://pinboard.in/add?later=yes&noui=yes&jump=close&tags=TAGS GO HERE&url='+encodeURIComponent(q)+'&description='+encodeURIComponent(d)+'&title='+encodeURIComponent(p),'Pinboard','toolbar=no,width=100,height=100'));
```

你可以把如上代码中的 `later=` 后面的部分改为你需要的值，如果你需要把添加的书签默认设为稍后读，那么就保持默认值不变，如果你不需要把添加的书签默认设为稍后读，那么把 `yes` 改为 `no`。此外，你还可以把 `TAGS GO HERE`这一部分改成你想要默认添加的标签。

改完这段代码后，我们把它添加到浏览器的书签中。以 Safari 为例，在 Safari 中是不能直接添加自定义输入的书签的，那么我们就只能曲线救国了。首先，我们把任意一个网页保存到书签，然后在 Safari 的「Bookmarks」工具栏中打开「Edit Bookmarks」，找到我们刚才保存的书签后，单击该书签对应的 Address，你就可以把原先的网址替换为我们修改好的 javascript 代码了，网页名同理，修改好后，退出编辑页面，重新回到我们需要保存的网页，在书签栏中单击刚才保存好的 Bookmark 就可以把当前 Tab 显示的网页保存到 Pinboard 了。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/ECAD2BF8-534B-463F-AE27-33DEF70E024E.png)

书签自动同步
------

### 自带同步服务

Pinboard 官方其实提供了多种自带的同步选项，囊括了 Instapaper、Readability 和 Pocket 等稍后读服务，以及 twitter 等社交网络。你可以在你的 Pinboard [设置](https://pinboard.in/settings/)页面分别添加相关服务的信息，让关联服务中出现的网页全部单向同步到 Pinboard 中添加为书签。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/9E3FBA38-1A02-47BE-A9C4-64AA14D1B425.png)

下面以 Instapaper 为例，我来展示一下如何将 Instapaper 上保存的文章全部同步到 Pinboard 上保存为书签。

第一步，在 Safari 上登录你的 Instapaper 账号，右键点击你需要同步的文件夹名，选中「Inspect Element」后，就会出现下方的浏览器后台界面。

第二步，在后台界面的搜索栏输入「rss」，就可以找到文件夹对应的一行代码，以我的 Instapaper 为例，显示的是：

```
<link rel="alternate" type="application/rss+xml" title="RSS" href="/rss/*******/********************" />
```

其中我们需要的只有 `rss/*******/********************` 这一部分4 。

最后一步，我们只需在 Pinboard 的设置页面 Instapaper 对应的输入框中填入 `http://www.instapaper.com/` 加上我们找到的 rss 地址 `rss/*******/********************` 即可。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/9E3FBA38-1A02-47BE-A9C4-64AA14D1B425.png)

不过这些外部服务与 Pinboard 的同步并不是完全实时的，而是采用了间隔性的同步方案。你可以在你的 Pinboard 网页的「account」界面查看你所有连接的外部服务的同步情况。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/C436CF52-7F91-4898-9003-8B9462372CB0.png)

### 第三方同步服务

得益于 Pinboard 开放的 API，我们也可以通过第三方服务来把网页同步到 Pinboard 并添加为书签。其实说到这里，应该有很多读者已经想到了要用什么第三方服务。没错，就是 IFTTT。以 Instapaper 和 Pocket 为例，可以看到通过 IFTTT 我们可以设置更加丰富的同步选项。除了稍后读服务，我们也可以把 Twitter 和微博也同步到 Pinboard 中来。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/F1A027C2-D857-4E7E-8808-F68A8E9B1567.png)

类似的功能，我们也可以通过 Zapier 来实现。你可以自己根据需求创建 Zaps，也可以直接使用官方推荐的现成的 Zaps。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/1B9DF5FD-BF9F-4147-BDD1-D76B16FA91E1.png)

但是 Zapier 与 IFTTT 相比，对于 Pinboard 接口的支持明显没有后者来的全面。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/6416472E-E169-47B0-ACCD-318EE722AA45.png)

除了 IFTTT 和 Zapier，还有很多 App 本身就提供与 Pinboard 的协同功能，比如说 Instapaper， 应用本身就提供了与 Pinboard 之间同步的功能，可以用来同步你喜欢的文章和笔记。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/8CDC3102-3FFC-4C85-968E-0F1931BA3D21.jpg)

那么在自带同步服务和第三方同步服务之间该如何选择呢？我在这里做一个简单的总结。首先，自带同步服务会同步你所关联服务中所有新增的内容，而使用第三方同步服务你可以自定义同步的选项；其次，自带同步服务如之前所说是间隔性同步，而第三方同步服务提供的是实时同步，当然具体的同步速度还是取决于服务器相应的速度。

其他功能
----

在「书签手动添加」的章节我分别介绍了一个通过 LaunchBar 和 Alfred 来添加书签的实例，其实这两个效率工具除了为 Pinboard 添加书签还可以完成其他的功能。还是以 LaunchBar 为例，你可以通过 [GitHub](https://github.com/gillibrand/launchbar-pinboard) 来下载这组 LaunchBar 的 Action。

在使用这组 Action 前，我们需要先在 LaunchBar 中键入关键词呼出其中一个用来关联 Pinboard 账户的 Action，然后在其中输入你的 Pinboard API Token。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/FB87069C-344C-43D1-8A6A-E9314E0CA8D2.jpg)

通过这套方案你可以浏览最近添加的 25 个书签和所有的未读书签。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/9EBE6AD8-0216-4C9B-96A8-E6A11E9C6F7C.png)

它还可以根据使用频率显示所有的标签，在选中任一标签后还能显示该标签下对应的书签。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/D0D19C5A-9E31-406A-BF28-5EEB0FA9A126.png)

这套 Action 还包含了强大的搜索功能，你可以在 LaunchBar 上通过标题、描述和标签来搜索你在 Pinboard 上保存的书签。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/E5E755C6-63F6-45D6-A5E5-2E0AE72D856A.png)

使用 Alfred 的朋友也不用难过，我在这里推荐一组 Pinboard 在 Alfred 上的 Workflow，可以实现更多的功能。有兴趣的朋友可以前往 [GitHub](https://github.com/jmjeong/alfred-extension/tree/master/alfred-pinboard) 下载并了解使用方法，在此不做更多的展开了。

第三方应用
-----

Pinboard 的开发者非常贴心地在[官网](https://pinboard.in/resources/)列出了一些 Pinboard 的第三方应用，你可以从中选择最适合你的。而我在这里只推荐一款 Pinboard 第三方客户端，那就是 Pinner。

Pinner 提供了 iOS、watchOS 和 android 三个平台上的客户端，你可以分别前往 [App Store](https://itunes.apple.com/app/pinner-social-bookmarking/id591613202) 和 [Google Play Store](https://play.google.com/store/apps/details?id=com.blork.pinner) 下载。作为目前个人认为最优秀的 Pinboard 移动客户端，Pinner 除了拥有优秀的 UI 设计外，还提供了 Spotlight 搜索、分享菜单快速添加、Slide Over & Split View、自定义搜索、通知中心小部件和 Hand Off 等功能。另外，Pinner 的夜间模式也非常令人满意。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/9C090523-9057-4D0A-9648-791A780862B3.png)

关于 Pinner，这里需要注意的一点是在使用 Share Extension 添加书签的时候，你会发现 Pinner 提供了两个选项：Add/Edit Bookmark 和 Quick Pin。区别在于使用 Add/Edit Bookmark 的话，你需要在添加前完善标题、描述和标签等相关信息，而使用 Quick Pin 的话该网页会被直接添加到 Pinboard 中。

![](.evernote-content/625589E3-DC84-414B-96FD-263BC95FC495/F58C932B-C2BE-4571-B072-1EAD0A6DD74B.png)

但是 Pinner 是不支持 Pinboard 的全文搜索的，即使你开通了 Bookmark archiving 也没有用。如果你必须用在移动客户端上使用全文搜索，那么你可以试一试 Pushpin 或者 Pinswift。

如果你想在 Mac 上使用 Pinboard，我只推荐使用 Pinboard 的官方 Web 版，这样一来你也不用担心跨平台使用的问题。如果你一定想用一个 Mac 客户端，那么 Spillo 可能是最佳选择。

后记
--

Pinboard 可以说是一个异常「简陋」的产品，它没有优雅的官网，甚至连官方客户端都没有，但是这些并不妨碍 Pinboard 成为一款优秀的产品。你可以使用 Pinboard 像[少楠](https://sspai.com/user/738326/posts)一样来做一个产品周刊，也可以只用它完成简单的书签收藏和管理。但是不管你有怎么样的目的，希望这篇文章都能够帮助你更好地玩转 Pinboard，提高你的工作和学习效率。如果你有其他更多关于 Pinboard 的使用技巧，也欢迎你与大家一起分享与交流。

---

[🌐 原始链接](https://sspai.com/post/41817)

[📎 在印象笔记中打开](evernote:///view/207087/s1/764f0fd0-ebc5-450c-af8e-5204f9d42328/764f0fd0-ebc5-450c-af8e-5204f9d42328/)