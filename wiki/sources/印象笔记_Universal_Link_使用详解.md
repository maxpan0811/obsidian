---
title: "Universal Link 使用详解"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Universal Link 使用详解.md
tags: [印象笔记]
---

# Universal Link 使用详解

# Universal Link 使用详解 --- Universal Link 使用详解 =================== | 本文为付费栏目文章，您已订阅，可阅读全文 | URL Schem

---

# Universal Link 使用详解

---

Universal Link 使用详解
===================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

URL Schemes 是 iOS Power User 必须了解的一种基础自动化技巧。

它最大的用处是可以让我们直达应用的某项功能，比如网易云音乐的[听歌识曲](https://sspai.com/post/46871orpheuswidget://recognize)，或者打开支付宝的[扫码界面](https://sspai.com/post/46871alipayqr://platformapi/startapp?saId=10000007)…… 而不必受到主屏角标、应用内广告、界面设计变化等等因素的干扰。

支持 URL Schemes 也是一个工具达到一定完成度的标志。对 URL Schemes 支持得比较完整的工具往往是同类翘楚，比如：OmniFocus、Things、Ulysses、Drafts……

URL Schemes 使用上的常见问题
--------------------

在使用 URL Schemes 时，最常见的问题是 —— 不知道某个应用的具体 URL Schemes 是什么。这主要是因为 URL Schemes 没有编写的规范。对于用户来说，找一个应用的 URL Schemes 会遇到两大难题：

1. 无迹可寻：复杂 URL 是由每个开发者指定的，没有规律，甚至大多数应用没有复杂 URL。
2. 功能不全：因为每个功能都要开发者指定，所以一个 App 功能越多，复杂 URL 就越难覆盖它的全功能。

尽管 Power User 们可以根据文档查询、搜集数百条 URL，也还是解决不了这两个难题。

特别是对于我们经常使用的网页服务，国内如知乎、微博、淘宝等，国外有 YouTube、Twitter、Instagram、Wikipedia…… 使用复杂 URL 很难覆盖到它们客户端的所有功能，所以我们会发现它们甚至没有什么复杂 URL。很多我们需要的功能，比如说搜索、收藏、购物车之类的，也因为没有 URL，**似乎**也都没办法直接跳转。

但是，如果你经常使用国外这些服务，你可能会发现，有时候你点一个链接，比如在 Twitter 客户端点了一个 YouTube 的视频链接，它会跳转到 YouTube 客户端，并且直接打开这个视频。

实现这个效果的，就是苹果在 2015 年 WWDC 公布的 Universal Link。

Universal Link 是什么
------------------

简单来说，当一个服务，同时拥有网页和客户端时，只要开发者对 Universal Link 进行了支持，就可以让用户在 iOS 上通过传统 URL，直接打开应用的具体功能。

换句话说，开发者不用为网页里的每一个具体功能制定特殊的 URL Schemes，用户只要用正常的「https」打头的 URL 就可以跳转客户端，甚至跳转到具体功能。

比如用 iMessages 发给对方一个 YouTube 的链接：<https://youtu.be/rzc3_b_KnHc> 对方点了之后，不是在 Safari 中打开这个视频，而是直接在 YouTube 客户端中打开这个视频。

点击 YouTube 链接后直接在客户端打开

所以 Universal Link 直接解决了传统的 URL Schemes 不可避免的**无迹可寻**和**功能不全**这两个问题：

1. 针对**无迹可寻**：同一个 URL，网页出啥界面，应用就出啥界面。
2. 针对**功能不全**：网页只要有页面，应用就能跳转。

这个功能在 iOS 上使用得十分广泛，特别是国外的不少知名服务都开始使用了这个功能。接下来我会为大家展示一些我整理到的用法以及特例，以便让大家更容易理解它的用法，把它融入自己的操作习惯。

Universal Link 实例与应用
--------------------

在 Universal Link 的使用里，主要可以分为 2 种情况。

1. 使用 https 的 URL 跳转，比如 <https://twitter.com/JailbreakHum>，这是一般意义上的 Universal Link。
2. 使用应用的 Host 加上网页 URL 跳转，比如 [sspai://sspai.com/post/31500](https://sspai.com/post/46871sspai://sspai.com/post/31500)，这是一种特殊的 Universal Link 和 URL Schemes 的结合。

这两种使用情景又各自有一些小情况，我们会在相关的部分分别探讨。

### 通过 https URL 跳转

使用 https + URL 是最标准的 Universal Link 使用方式，国外不少知名服务都已经对它有很好的支持。大众的前面已经提过了，小众一点的，有 Trello、Airtable、Notion、Medium、Quora 等等。如果你用这些服务的话，可以点击下面的链接来尝试一下：

* Trello：[我建立的 Trello 测试 Board](https://trello.com/b/ROz1heAY/%E6%B5%8B%E8%AF%95-board)
* Airtable：[我之前整理的 Mojave 软件支持表格](https://airtable.com/tblQO5tc27ymRSJ0S/viwgI4sNHz05X8Mg8)
* Notion：[Notion 的引导文档](https://www.notion.so/Travel-Planning-72f6be22d26848dd884d1e9aae894a4e)
* Medium：[Medium 的收藏页](https://medium.com/me/list/bookmarks)
* Quora：[Quora 的收藏页](https://www.quora.com/bookmarked_answers)

这些直接跳转到具体功能的 URL 全部是通过 https 打头的 URL 直接跳转的，它们要么是本来没有可以直接跳转客户端的 URL Schemes，如 Quora、Medium；要么是有 URL Schemes 但是逻辑记下来很麻烦，比如 Trello 和 Airtable。

现在用 https 打头的 URL，完全不用去记或者猜 URL 的规律，只要这个链接能打开网页，然后你装了这个服务的客户端，那你点这个链接就会直接跳转到客户端的相应界面。

我最常用的大概是 Medium 和 Quora 的收藏页，特别是 Medium，保存到 Pocket 效果变得很差，它本地阅读体验又很好。所以干脆就直接把打开 Medium 收藏的 URL 放到 Launch Center Pro 里，要看的时候就可以直接跳转。

#### 结合工具使其更实用

我们已经说过 Universal Link 支持服务的所有网页，所以它就不只能用于跳转，还能用于传输一些数据。这里最常用的大概就是搜索了：

1. YouTube：[YouTube 搜索关键字「Rap」](https://m.youtube.com/results?search_query=rap)
2. Twitter：[Twitter 搜索关键字「Metoo」](https://mobile.twitter.com/search?q=metoo)
3. Medium：[Medium 搜索关键字「Productivity」](https://medium.com/topic/productivity)

我们可以把这些链接最后的关键字部分，给换成 `[prompt]`，就可以在 Launch Center Pro 中直接做聚合搜索，搜索后跳转到具体的客户端来查看结果的动作了。比如「YouTube 搜索」的 Launch Center Pro 动作，它的 URL Schemes 就是：

```
https://m.youtube.com/results?search_query=[prompt]
```

此外，还有一种情况，是有些应用，不让我们点击链接后跳出该应用，比如微信。这种情况我们需要复制链接后跳转。

但是你会发现，当我们复制链接，在 Safari 粘贴并前往之后，它不会跳转客户端，而是在网页中打开。

如果你想直接跳转客户端，而不是这样在 Safari 打开粘贴的链接的话，可以使用 Launch Center Pro、Workflow 或者 Launcher 这样的工具，做一个直接打开剪切板链接的动作。它们的编写方式很简单，如截图所示：

![](.evernote-content/86F14810-9BD1-49B4-8A5A-81F64694F400/1A377393-C2E0-4617-B409-CDF25ECF2B41.png)

左 Launch Center Pro、中 Workflow、右 Launcher

复制链接后通过这些动作，可以直接跳转到客户端的相应界面，而不是打开 Safari。

### 应用 Host + URL 跳转

国外的工具大多都遵守 Universal Link 的使用规范，直接通过 https + URL 的方式就可以跳转客户端的具体界面或者具体功能。

但是国内却很少有工具在用 Universal Link，比如微博，它的部分功能，比如微博文章、单条微博、用户界面等等，都是用了 Universal Link。但是其他功能，比如搜索之类的，似乎就没有用。

我们比较常用的服务里，用 Universal Link 的大概是淘宝和知乎这两个。但是它们用了一种很稀奇的方式，是 Host + URL 的方式。

举个例子，比如我想打开知乎的搜索界面，按照 Universal Link 的逻辑，用知乎搜索「Rap」的 URL 应该是：[https://www.zhihu.com/search?type=content&q=Rap](https://www.zhihu.com/search?type=content&q=sspai)

而按照 Host + URL 的格式，用知乎搜索「Rap」的 URL 就变成了：[zhihu://www.zhihu.com/search?type=content&q=Rap](https://sspai.com/post/46871zhihu://www.zhihu.com/search?type=content&q=Rap)。注意前面的前缀是 zhihu 而不是 https。

淘宝也有一样的情况，我们可以用 URL 直接跳转淘宝购物车：[taobao://h5.m.taobao.com/mlapp/cart.html](https://sspai.com/post/46871taobao://h5.m.taobao.com/mlapp/cart.html)。它也是 Host + URL 的方式。

我咨询了 Price Tag 的开发者 61（微博：[@im61](https://weibo.com/u/1734549517)），他表示这两种 URL 本质上是一样的，都是接收了一段链接进行处理，但是至于为什么国内的人偏爱这种 Host 的用法，就不得而知了。

在我的使用中，发现 Host + URL 的形式有时候只能支持某个服务的单一功能，比如淘宝的功能就不能完全通过 Host + URL 的形式猜到。支持功能比较全面的国内服务，测来测去似乎只有知乎。

结语
--

其实苹果使用 Universal Link 并不是为了这篇文章中提到的这些 Power User 的用法，它主要的考虑是解决 URL Schemes 遗留的一些问题。首先是 URL Schemes 不唯一，所以才会造成当初的[拦截支付宝 URL Schemes 的安全事件](https://www.jbguide.me/2015/03/26/url-scheme-is-vulnerable/)。现在 Universal Link 和功能是唯一对应了，安全性提高很多。

同时，因为 Universal Link 本质上就是一个 https 开头的网页链接，所以用户安装不安装应用，这个链接都是可用的，用户体验更好，也更容易引导用户去下载客户端。

但是 Universal Link 的出现，使我们拥有了一条有迹可循、功能覆盖全面的，跳转客户端具体功能的方法。作为传统 URL Schemes 的补足，它让我们在面对网页服务的时候有了很有力的对策。

[#URL Schemes](https://sspai.com/tag/URL%20Schemes)[#使用详解](https://sspai.com/tag/%E4%BD%BF%E7%94%A8%E8%AF%A6%E8%A7%A3)

---

[🌐 原始链接](https://sspai.com/post/46871)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d6466bdd-707d-4463-9719-3ff0d1bdbd86/d6466bdd-707d-4463-9719-3ff0d1bdbd86/)