# Workflow 教程：如何使用 Workflow 中关于文章的那些动作

---

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/888E5A6A-4F45-46F8-BFE7-15C82F45C0B7.jpg)

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/4DA44923-B822-43DC-BEA4-F02CAA5DC34D.png)

编注：此为 [Workflow](http://sspai.com/tag/workflow) 系列教程补全计划，本文首发于 [越狱指南](http://jbguide.me/2015/03/03/how-to-use-the-new-articles-actions-in-workflow/)。

Workflow 在 1.1.1 版的更新中添加了两项功能。一项是内置了 GIF 服务 Giphy，这个熟悉 Launch Center Pro 的都应该很了解了。相对于 Workflow ，我认为 Launch Center Pro 更适合 Giphy 这个服务，所以我并不打算多提它。这篇文章要说的是另一项更新——关于 Articles（文章） 的一套动作。

用新动作在 Safari 里做文摘

每天你都会在电子设备上阅读很多东西，保留其中你认为有价值的部分的一个办法是摘抄。而如果你要把摘抄的内容统一起来放在一起，你就要考虑它的整洁度，也就是格式。

在电子设备上，最简单的让摘抄内容的格式统一起来的办法应该是用 Markdown：

文章名称:

> 引用文本

日期

这样出来的结果就会是：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/F99644E1-A891-49C3-9284-DF3488D9AB42.jpg)

有出处，点出处可以看到原文。引用文本有层级显示。最后还有摘抄的日期。

但是，在 Workflow 出现之前，这个过程是很繁琐的：你需要获取文章的名称、链接，还要复制好喜欢的内容，最后还要加上日期。但因为你每一次只能从网页粘贴到 Evernote 一项内容，所以你要来回选中复制再粘贴，还要考虑格式（字体字号）问题，实在太痛苦。

Workflow 1.1.1 版中添加了一套关于网页文章的动作——Articles，让这整个步骤变得极其容易。

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/B42E1BA6-FCAB-4660-B0E2-8A26F3727189.jpg)

仅能在 Safari 中做摘抄的办法

用 Articles 的功能做摘抄虽然简单，但是它的能力范围有限。它只能作用在 Safari 的网页里，对稍后读软件（ Pocket / Instapaper）和 RSS 软件都不起作用。

动作目的

对每个动作，你都要首先想清楚，你想做什么。想得越具体，你的目标就越明确，就越容易成功。

在这个动作里，我们首先要用 Workflow Type [1](http://sspai.com/31662#fn1) 去获取文章。然后我们要获得4个变量[2](http://sspai.com/31662#fn2)：文章的标题、链接，你想摘抄的文本，还有日期。

最后我们要把它们以下面的 Markdown 的格式放到一个 Text 文本框里：

文章名称:

> 引用文本

日期

然后我们要把 Markdown 的内容转化为 HTML，最后把转化好的内容发送到 Evernote。

接下来一步一步来做。

用 Workflow 获取文章

首先要把这个 Workflow 的类型设置为 Action Extension，并且仅接受 Articles 这个类型的内容：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/06F7365D-40AF-42C7-A222-24A71EDFC0FB.jpg)

获取文章的名称、链接及引用文本

Workflow 1.1.1 版中添加了 Get Details of Articles 这个动作。对这一个动作重复利用，就能够获取我们想获得的标题、链接跟引用文本。

但首先，我们要把获取了的 Article 先设为一个变量：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/E702E019-97CC-4D71-857E-F0C7E9AA429B.jpg)

原因是由于，我们总共需要三个变量（标题、链接跟引用文本）每次我们只能向这个 Article 获取一个内容，所以我们需要用到 Article 这个变量三次。

第一次，设完变量后可以直接从变量获取元素，所以我们可以直接从 Article 获得 Title（标题），并设为变量：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/77ACD122-D85B-4176-8A42-1D19436BBCDE.jpg)

第二次，获得 URL（链接），并设为变量：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/000E9687-B80D-475A-AAF1-5026581884B8.jpg)

获取引用文本：

Workflow 目前似乎还不支持直接从 Safari 获取选中文本，所以在这里需要绕一下，利用剪切板曲线救国。

具体做法是，在运行摘抄这个 Workflow 之前，先把你想要摘录的文字首先复制了。由于在 Text 文本框里，我们使用 Clipboard 这个常量，所以 Workflow 回把复制的内容自动填入正确的位置。

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/D0E9C963-B08A-4CC8-B8EA-6B56DF3AF360.jpg)

以上，我们就获得了我们摘抄所需要的一切元素。下面我们要获得日期。

获得日期

获得日期在 Workflow 里是一套动作，首先要获得日期，其次要决定这日期显示格式。

获取日期的动作是 Date，我们要在这个动作里选择 Current Date。然后在下面我们要接上Format Date，来设定日期显示的格式。因为是摘抄，所以也没必要特别精确，所以我用的是不显示时间，日期用的是最短的格式：年-月-日。

最后，将其设为变量。

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/A5D0AE32-B75E-41A9-B4F2-AFAD3CB7B4B2.jpg)

把变量填入文本框

获得了我们需要的四个变量，下一步就是按照 Markdown 格式把它们放到文本框中：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/D0E9C963-B08A-4CC8-B8EA-6B56DF3AF360.jpg)

把 Markdown 转化为 HTML，并发送到 Evernote

把 Markdown 转化为 HTML 是 Workflow 第一版就有的动作，叫做 Make Rich Text from Markdown。

在它的下面，我们接上 Append to Evernote[3](http://sspai.com/31662#fn3)，在笔记本中填入摘抄用的笔记本（我的是「Excerpt」）。

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/D54DB569-9DD5-4EA3-8C66-C44776A80E50.jpg)

这样整个动作就结束了。要注意先把想要摘录的文本复制好，然后再运行该 Workflow。

[下载该 Workflow](https://workflow.is/workflows/ed52c9885bce43299c35415050579af1)

不足之处

这个动作很容易，但是它作用范围只有 Safari 和一些可以在本 App 中以网页形式打开网址并运行 Share Sheet 的 App。后者其实并不多，因为大多数软件打开网址都不是也网页的形式，而是包括在了自己的软件内。像 RSS 阅读器、稍后读这些软件统统不能用这个办法。

当然神通广大的 Workflow 不会就此举白旗，但是方法会变得复杂很多，我们在以后的教程会说明这种方法。下面我们来看另外几个新动作的应用。

用新动作筛选某网站的文章后一并发送到稍后读

这个动作因为 Workflow 本身的一个缺陷在当前版本使用并不理想，后文会详述原因。

一般来说，我们对信息来源有一种信赖感。而且针对同一个专题的内容，同一个信息来源获取的消息更为联贯，逻辑承接更容易。但是，同一个信息来源有时候未必只会对你感兴趣的那一个点发布内容，比如我在指南并不是只写 Workflow 教程的，但是有些人可能因为他不越狱，所以对我写的插件方面的内容并不感冒，只想看关于 Workflow 的这些教程。如果你是这样，这次 Workflow 更新的关于 Articles 的动作对你来说就有用了。

它可以让你把某个信息源的关于某个专题的文章先筛选出来，然后一气儿全部发送到稍后读服务，然后你可以慢慢地看。

用 RSS 链接获取某网站的文章归档

Get Items from RSS Feed 是 Workflow 早就有的功能，用来获得具体 Blog 的博文归档。

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/B7FCDD5A-6FDE-4870-9FBA-AAB94090982B.jpg)

我们在 URL 里填上博客的订阅链接，然后在下一行选择获取的文章数。

筛选文章

Filter 是[上一篇教程](http://sspai.com/30903)详细介绍过的内容，这里不再赘述，只用具体例子来说明如何筛选文章：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/97F1D908-4184-4116-988A-0F691185B4E5.jpg)

上一步我们已经从越狱指南的 RSS 链接里获取了10篇最近的文章，现在通过筛选，我们要得到这10篇文章名称里包含「Workflow」的文章。然后按发布日期，从早到晚来排序。

全部发送到 Pocket

获取了符合标准的文章们，我们接下来要做的就是把它们一并发到稍后读。

处理一个列表中每一项内容的方法是使用 Repeat with Each 这个动作，这个动作我也已经在《[Workflow 教程：Workflow 本身能做什么？](http://sspai.com/30903)》里详解过了，这里也只说例子：

![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/00B6985D-4245-4C77-B651-0AEF01DE0A40.jpg)

如图，只要在产生列表的下一步放上 Repeat with Each，Workflow 就知道下面是处理列表中的每一项内容，我们把 Add to Pocket 放到 Repeat with Each 里，Workflow 就明白这是要它把列表中每篇文章都发到 Pocket。

[下载该 Workflow](https://workflow.is/workflows/24668776f2f647bb99724e78c9dc2c41)

不足之处

Workflow 1.1.1 版更新出的这些 Articles 功能都足够好用，但是从 1.0 就有的 Get Items from RSS Feed 这个功能却一直有个毛病——它只能获取10项内容，你不管设定多少项，它只获取10项。所以这也成了这部分讲的整个 Workflow 的短板，比如说指南现在的文章，按时间来排序，最新的两篇是 Workflow，接下来的就是只接到第14和第15篇了。所以用本文的方法，只能获取前两篇。

具体设置办法可以看第一篇教程——[《Workflow 教程：如何上手 Workflow》](http://sspai.com/30903) 的 Workflow Type 部分。 [↩](http://sspai.com/31662#ffn1) 变量的讲解也在 [《Workflow 教程：如何上手 Workflow》](http://sspai.com/30903) 这篇文章里。 [↩](http://sspai.com/31662#ffn2) 关于 Append 的意思，可以看之前的这篇文章：[《以Evernote为例来谈Drafts的内置动作》](http://jbguide.me/2013/05/30/drafts-actions-evernote/)[↩](http://sspai.com/31662#ffn3) Workflow 系列文章 [Workflow 教程：Workflow 本身能做什么？](http://sspai.com/30903) [Workflow 教程：征服 Workflow 中的最高峰](http://sspai.com/30870) [Workflow 教程：如何备份恢复你的 Workflow 动作](http://sspai.com/30591) [Workflow 教程：如何上手 Workflow](http://sspai.com/27846) [深度测评：Workflow 是款什么样的应用？](http://sspai.com/27733) [更多关于 Workflow 的文章 >](http://sspai.com/tag/workflow)

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[Workflow 教程：如何使用 Workflow 中关于文章的那些动作](http://sspai.com/31662)

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime

少数派（ <http://sspai.com> ）

[![](.evernote-content/8E28C94E-F2E4-4C98-BB3A-4AF8D54C5BF9/E78ADBE9-DBB8-457C-A67C-617A5AB5AC56.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:iMac/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fmac%2F)

---

[🌐 原始链接](http://sspai.com/31662)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0fc8a966-8d84-4f52-9edb-399f083c7bf8/0fc8a966-8d84-4f52-9edb-399f083c7bf8/)