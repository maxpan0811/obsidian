---
title: "Workflow 教程（五）：如何利用 Workflow 与网页互动"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Workflow 教程（五）：如何利用 Workflow 与网页互动.md
tags: [印象笔记]
---

# Workflow 教程（五）：如何利用 Workflow 与网页互动

# Workflow 教程（五）：如何利用 Workflow 与网页互动 --- ![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/

---

# Workflow 教程（五）：如何利用 Workflow 与网页互动

---

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/9CC534B9-EFE7-4C09-879A-F5089719F735.jpg)

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/4606866F-0D8C-4807-A3C5-8588B6D9AA07.png)

编注：此为 [Workflow](http://sspai.com/tag/workflow) 系列教程补全计划，本文首发于 [越狱指南](http://jbguide.me/2015/03/03/how-to-use-the-new-articles-actions-in-workflow/)。

在效率软件中使用 URL 的好处
----------------

任何可以搜索的网页服务都遵循着各自 URL 的格式，比如在谷歌和百度搜索「少数派」，它们的 URL 将分别是：

* [http://www.google.com/search?q=`少数派`](http://www.google.com/search?q=%3Ccode%3E%E8%B6%8A%E7%8B%B1%E6%8C%87%E5%8D%97%3C/code%3E)
* [http://www.baidu.com/s?wd=`少数派`](http://www.baidu.com/s?wd=%3Ccode%3E%E8%B6%8A%E7%8B%B1%E6%8C%87%E5%8D%97%3C/code%3E)

这两个 URL 里，`少数派`是我们原本输入到搜索框里的东西，而其它的部分则是该网站搜索服务的 URL 格式。不信你可以把 `http://www.baidu.com/s?wd=` 粘贴到你的地址栏，然后在等号后面输入你想搜索的东西试试看。

只要我们了解了一个网页的 URL 的格式，就可以在 [Alfred](http://sspai.com/tag/Alfred)、[LaunchBar](http://sspai.com/tag/LaunchBar)、[Launch Center Pro](http://sspai.com/tag/Launch%20Center%20Pro)、[Drafts](http://sspai.com/tag/Drafts) 以及 [Workflow](http://sspai.com/tag/workflow/) 这样的效率软件中，把 URL 中固有的部分先设定好，在搜索的时候只需要输入想搜索的内容就可以了。

比如我想在 iPad 上知道一个 App 发布以来的价格变化，我只要运用 [Appshopper](http://sspai.com/tag/Appshopper) 的 URL 格式，在 LCP 中设定好一个动作，在搜索时只搜索 App 名即可：

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/2411D065-B768-4738-9F1C-DE460DF5A514.gif)

当你运用多个不同网页的搜索服务，比如说「谷歌」、「淘宝」、「优酷」的时候，这种搜索的精准和效率就可以更好地体现出来。

在 Workflow 中使用 URL
------------------

Workflow 当然是支持这个功能的，而且由于它独特的运行方式，URL 既可以是一个完整的动作，也可以是一个动作的一环。

我不建议在 Workflow 里把 URL 方面的使用当作一个完整的动作，这属于工具误用。比如有人在 Workflow 里单独将百度搜索作为一个动作，功能就是输入关键词，让百度来搜索。这让我非常不解：其一，你完全可以把 Spotlight 的搜索引擎设为百度，这样最效率；其二，退一步，即便你希望用效率软件做这样的事（虽然这么做已无效率可言了），你也完全可以用 Launch Center Pro，因为 Workflow 中如果对中文不进行 encode 是没办法直接用的。

所以，在 Workflow 中使用 URL，最好的办法是将其作为整个动作的一环。发挥 Workflow 的价值，不要用 Workflow 做那些其它 App 也可以做，甚至其它方法更省事的事情。

### 用 Workflow 获取需求的信息，自动填入 URL

在这里直接用 `Save App Icon`[1](http://jbguide.me/2015/05/02/how-to-use-url-in-workflow/#fn:1) 这个 Workflow 来详述整个过程。

*有能力的可以直接[下载 Workflow](http://cl.ly/aqb2)来看是怎么回事。*

`Save App Icon` 这个 Workflow 的作用是直接在 App Store 里保存软件的 icon，便于以后任何形式的分享。而且并不只是保存到相机胶卷，这个 Workflow 经过简单的修改，就可以把 Icon 直接在动作中分享到你需要分享的对方。

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/73D99B41-CD25-403B-B5EC-99119BC5C752.jpg)

#### 第一步：获取 App 的链接

*我强烈建议新手边操作边理解，文章里提到的整个方法绝对不难，但是如果没有基础，只看文章的话很快就头蒙了。*

在这里 Workflow 里，我们主要使用的是一个叫做 [icoicon](http://submit.icoicon.com/) 的服务。它的 URL 是：

```
http://submit.icoicon.com
```

而要想从这个网站获取某个 App 的图标，必须给 icoicon 提供这个 App 的链接，只有当它的 URL 满足下面这个状态：

```
http://submit.icoicon.com/?itunesurl=App链接
```

它才能够从中读取这个 App 的 Icon 并显示出来。

所以第一步，我们要获取 App 的链接，而这很简单，只要设定此 Workflow 只接受 `URLs`类型的数据就行了。

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/DC10CE57-8096-42B8-97CA-2174216A8FD1.jpg)

#### 第二步：将 App 的短链接拓展为原始链接

在 iOS 设备上的 App Store 里，我们获取的链接都不是一个正常的原始的链接，而是被缩短过的 App Store 专用链接。缩短了的链接将数据使用一个简单的代号表示，比如说，Tweetbot 的原始链接是：

```
https://itunes.apple.com/cn/app/tweetbot-4-for-twitter/id1018355599?mt=8
```

但通过 iOS 上的 App Store 获取的链接是缩短了的：

```
https://appsto.re/us/TEvdR.i
```

很多服务不能识别出这些链接的完整内容，所以会判断链接错误。在使用这种服务的时候，我们需要把短链接拓展为原始链接。

Workflow 提供了 `Expand URL` 这一超级实用的功能，在 Workflow 内部直接解决了这个问题。

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/CBBAC329-2F54-4B58-B355-2E7D973AB131.jpg)

#### 第三步：将原始链接填入 URL

第一步里，说到了我们需要用到 icoicon 的 URL 格式：

```
http://submit.icoicon.com/?itunesurl=App链接
```

我们在第二步已经获得了需要的`App链接`，下一步就是把它填进这个 URL。

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/28CC3217-F3A4-45AB-952D-0EBE49AB2B5B.jpg)

由于 `http://submit.icoicon.com/?itunesurl=` 是固定的，所以我们直接在 URL 这个框里填上固定的这部分。然后我们使用 `input` 把上一步面获得的原始链接承接过来：

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/0F51BB08-3A46-4F11-B091-2E664901632B.jpg)

当你想使用 `input` 把上一步得到的结果填入到下一步中，如果这个关系成立，就能在两步中间看到一条「线」，表示这两步的承接关系已经确立。

注意，URL 这一栏的内容并不完整，你需要先将 `http://submit.icoicon.com/?itunesurl=` 复制到 URL 中，然后在变量中找到 `Input`，把它放到等号后面。

#### 第四步：下载网页内容

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/B8856F63-3343-4825-AA62-3FEAF75ED35C.jpg)

`Get Content of URLs` 是 Workflow 这个 App 能够牛逼的重要原因之一，用它可以在不打开网页的情况下获取网页的内容，如果网址是可下载格式的文件还可以直接下载到手机并通过 Workflow 的其它动作将其分析出来或者播放。

当我们把一个 App 的链接，比如说 Tweetbot 的填入到 icoicon 的 URL 中，在 Safari 里我们将看到的是这样一个网页：

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/788312D3-C3CE-47B0-A237-544B73494E69.jpg)

我们可以在这个页面直接长按图片来保存。

但是在这一步，我们是要用 `Get Content of URLs` 来获取 icoicon 这个页面里的图标，我们不用打开浏览器，直接让 Workflow 帮我们拿我们需要的东西。

#### 第五步：从获取的结果里筛选出图标

利用 `Get Content of URLs` 我们会从链接中下载一切可以下载的内容，我们要从中提取出我们需要的部分，就需要使用 Workflow 的其它操作（想看 `Get Content of URLs` 都下载了什么东西？回忆一下 [Content Graph](http://jbguide.me/2015/02/19/what-can-workflow-do/) 的用法）。在这里，我们要的是图片，所以我们要使用`Get Images from Input` 来从下载了的内容里获得图片。

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/B8FB0F75-9F42-40BB-AF63-654A9B319E5F.jpg)

#### 第六步：处理获取了的 Icon

经过第五步，我们就获取到了想要获取的软件的 Icon。所以第六部其实是一个开放的选择，比如，你可以像我这样使用 `Save to Photos` 这个动作把它保存到相机胶卷：

![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/94C11492-C0AE-460E-B5A5-6C9E4CC8A1A6.jpg)

你也可以在下面直接用 `Share` 把这张图标发送到其它位置或者社交网站。

### 小结

我在这篇文章里用 `Save App Icon`[1](http://jbguide.me/2015/05/02/how-to-use-url-in-workflow/#fn:1)这个动作说明了 Workflow 在网页 URL 上应用的一些基本用法。读完这篇文章你应该掌握的用法有：

* 能够注意到、识别出并利用网页的 URL 格式。
* 用 Workflow 将短链接拓展为原始链接。
* 在 Workflow 中把具体内容填写到 URL 的特定部分。
* `Get Content of URLs` 的用法。

而且记住，不要单独地把 URL 相关的动作仅作为一个动作在 Workflow 里使用，要把它融入到一整个更大的、更适合 Workflow 这款软件的动作里。

1. 原构思来自[@P\_D何国平](http://www.weibo.com/u/2633691220)在[《【Workflow 测评】Workflow 是款什么软件？》](http://jbguide.me/2014/12/18/workflow-review-what-is-workflow/)的评论，我进行了修改。 [↩](http://sspai.com/31832#fnref:1 "return to article")

### Workflow 系列教程

* [Workflow 教程（七）：征服 Workflow 中的最高峰](http://sspai.com/30870)
* [Workflow 教程（六）：如何备份恢复你的 Workflow 动作](http://sspai.com/30591)
* [Workflow 教程（五）：如何利用 Workflow 与网页互动](http://sspai.com/31832)
* [Workflow 教程（四）：如何使用 Workflow 中关于文章的那些动作](http://sspai.com/31662)
* [Workflow 教程（三）：Workflow 本身能做什么？](http://sspai.com/30903)
* [Workflow 教程（二）：Workflow 基础用法](http://sspai.com/27846)
* [Workflow 教程（一）：Workflow 是款什么样的应用？](http://sspai.com/27733)
* [更多关于 Workflow 的文章 >](http://sspai.com/tag/workflow)

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[Workflow 教程（五）：如何利用 Workflow 与网页互动](http://sspai.com/31832)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/3544F77C-8E68-4B13-9F36-469678CD74E6/7A6CF4B6-E182-4350-8E81-F0107B1A8EE2.jpg)](http://sspai.com/collection/photography)

---

[🌐 原始链接](http://sspai.com/31832)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7e9f3562-3a38-480f-ad0f-431a3d816c05/7e9f3562-3a38-480f-ad0f-431a3d816c05/)