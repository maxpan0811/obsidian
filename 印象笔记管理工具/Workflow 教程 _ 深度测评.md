# Workflow 教程 | 深度测评

---

Workflow 教程（一）：Workflow 是款什么样的应用？ | 深度测评
========================================

2014 年 12 月 19 日

本文首发于 [越狱指南](http://jbguide.me/2014/12/18/workflow-review-what-is-workflow/) ，原作者 [Jailbreakhum](http://weibo.com/u/2208752785 "由jailbreakhum发布") ，少数派经由原作者授权转载此文，仅对文章标题及正文版式、用词略有改动，[点此](http://jbguide.me/2014/12/18/workflow-review-what-is-workflow/) 查看原文。

---

为什么我们要「折腾」效率应用
--------------

[Larry Wall](http://zh.wikipedia.org/wiki/%E6%8B%89%E9%87%8C%C2%B7%E6%B2%83%E5%B0%94) 说程序员（黑客）有三大美德：

> 懒惰、傲慢、缺乏耐性。

这里的懒惰说的是「为了让事情变得轻松一点而不辞辛苦」，原文是：

> 驱使你极力努力以减少精力的总的消耗的美德。

这话这么说可能看起来怪，但中文也有含义差不多的谚语 ——「磨刀不误砍柴工」。

使用电脑和手机这样的「智能」设备，想实现某个结果都有一定的流程，很多时候这些流程里的某些步骤是重复的。重复就会有两个弊端：第一是浪费时间，试想如果你能把某个常用的流程缩短了几步，那么每一次用这个流程你都省了一点儿时间，长久累积起来你能节省的时间就很可观了；第二个弊端是增加干扰，从锁屏就能看到的通知开始，智能设备里一切元素都是为了吸引你的注意力，步骤越多你受到的干扰就越多被打断的可能就越高，很多时候你想到一件事需要用手机完成，但是你拿出手机划了一会就忘了你当初为什么要拿出手机了。

所以在智能设备上我们需要那些能够缩短我们流程的应用，能够帮我们直击任务，从而让我们保持注意力并且节省时间。

试想你看到一个网页上有部分设计不错要分享给同事，在 iOS 上，它的流程就是这样：

> 截图 → 打开一个编辑图片的应用 → 选择刚才的截图 → 圈出你认为设计好的部分 → 保存到相机胶卷 → 分享给朋友 → 删除截图

这里面有许多多余的干扰，比如你会想「我用哪个图片编辑应用好？」打开图片编辑应用后有的可能还会让你登录；不同的编辑应用取图的逻辑不一样，有的是按从新到旧排有的是从旧到新排序，所以你需要找一下你刚截的那张图；然后修改完保存完分享的时候又要找一下刚保存的截图，而且注意你现在有两张截图了，一张是改过的，一张是原始截图；最后你要把两张图都删除掉。

通过 Workflow，这整个过程就会化简很多：它会自动地获取你刚截的那张图片，通过 Workflow 内置的 [Aviary SDK](https://developers.aviary.com/)，你获取了刚刚的截图就可以直接开始编辑图片，编辑完毕以后自动弹出 iOS 内置的分享选项（你也可以设定某个具体应用、某个具体联系人，这样每次就会直接通过你惯用的应用发给固定的同事），最后删除刚才的截图。由于图片修改并未保存到相机胶卷所以被修改的截图本来就不存在。

这样的操作，首先目前只有 Workflow 才能做到不说，关键在于 Workflow 使用的图形操作模式，让整个流程变得可见所以容易。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A8AC15BA-58B4-40B5-AADB-DACF13AEBEC9.png)

有的人不看好这样的应用，因为在目前的 iOS 平台上它们看起来「实用性」不大，跳来跳去的，折腾半天可能也成功不了。说它们是效率应用还不如说它们是爱折腾那帮人的「玩具」。这让我想到凯文・凯利的话：

> 在 1800 年，200 年前的时候，当时的高科技就是帆船，就是能够远航的船，非常的复杂，非常的高科技。它也是在全世界运输产品的好方式，这些运营公司都是全球性的公司，他们都是当时世界上最大的工作。当出现第一艘蒸汽船的时候，大家都嘲笑这些蒸汽船，说很可笑，很滑稽，很没有效率。他们经常出故障，然后成本也很高。大家把它们称作玩具，他们的确是玩具，因为他们没有用。但是他们做了一件事情是那些帆船做不了的，那就是他们能够往上游走。人类数千年来总是从上游到下游，但是你无法从下游到上游，这些蒸汽船就可以往上游走。然后，他们把这个小小的发明，这种小玩具的发明一直不断地持续，年复一年，日复一日，直到有一天在 1875 年的时候，基本上没有一家帆船运输公司留下来，他们都破产了。

Workflow 是一款让所有人开心的效率应用
-----------------------

能够缩短我们日常操作流程的效率应用 iOS 上已经出来了不少，Launch Center Pro、Drafts、Editorial、Pythonista 等应用各有所长，可以说各自坐稳了自己的江山，看起来这块领域已然无肉可分。但越狱开发者出身 [1](https://sspai.com/post/27733#fn:1) 的 [Ari Weinstein](https://twitter.com/AriX) 却在这种市场环境下做出了 Workflow ，不仅一炮而红，而且获得了几乎整个 iOS 生态圈的认可：从小白到 Power User，再到应用开发者一片赞誉；苹果在 Workflow 发布当天就将其置为 Editor's Choice；而越狱相关的开发者们也都向以前的同行道喜祝贺。

小白能喜欢说明它简单 —— 在 Launch Center Pro 里很多行「天书」的动作，在 Workflow 里只要拖几个动作块过来排排队就行了；Power User 喜欢说明它坑深 —— 对于 Power User 来说，一个工具如果一折腾就到底就没意思了，这个工具的能力必须大于 Power User 的脑洞，才能被 Power User 认可；上面提到的那些效率应用的开发者之所以无一不称赞 Workflow，不仅因为 Workflow 本身优秀，还因为 Workflow 与这些应用之间的配合相得益彰。Workflow 开售后甚至带动了 Launch Center Pro 的销量 [2](https://sspai.com/post/27733#fn:2)；Workflow 这次在分享菜单里弄这么大的动静苹果都给了 Editor's Choice ，回想起 Launcher 的境遇，觉得有点看明白苹果的意思了：通知中心就是来看的，想办事就用分享插件，随你折腾；插件开发者的祝贺是理所应当的 —— 不仅因为作者曾是越狱开发团队 Chronic Dev Team 的一员，还因为插件开发本身就是为了拓展 iOS 设备的能力，所以 Workflow 这样的「Pushing the boundaries of automation on iOS.」的应用自然会被他们承认。

Workflow 的操作逻辑
--------------

当你第一次进入 Workflow，这款应用会引导你做一个「Make GIF」的动作来让你了解整个应用的操作逻辑。基本来说，它就是拖拽和排列，只要你能想清楚整个流程发展的顺序，你就能成功地制作一个 Workflow。

就拿 GIF 这个来说，你当然必须先拍照，再合成 GIF。Workflow 的工作流程是从上到下的，所以你必须把拍照放在合成 GIF 之上，然后你要想分享这张 GIF，就得把分享放在 GIF 之下。整个逻辑很自然。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/CC9664E9-3ADE-4646-8707-A61583B305F1.png)

第一版 Workflow 给了你 [超过 150 个内置的动作](https://s3.amazonaws.com/f.cl.ly/items/031m050u0B39231z0Z2k/Workflow_Actions_List%20copy.pdf)，在此之上作者还可以直接向应用加入动作而无需通过苹果审核，通过这些内置的任务理论上你可以做的事情非常多。所以它给了你足够的发展空间，就看你能不能根据自己的需求和能力制作出好用的 Workflow 了。

Workflow 的优势
------------

前面提到 iOS 上的效率应用的格局似乎已经写定，但 Workflow 却能够在这样的格局下一鸣惊人，没有自身的优势是做不到的。

### 直观所以简单

#### 易于摸索

对于效率应用新手来说，Workflow 的优势就是直观 ——「看得见」很重要。你知道你在干什么，你知道下一步将会发生什么，如果运行失败你也比较容易查出来问题出现在哪。让一个 Workflow 新手弄出来「将一张图片同时分享到微博和 Twitter 并配上想说的话」这样的动作很容易的，而在 Launch Center Pro 里通过 URL Schemes 来完成同样的话，恐怕就不是一个新手能够做到的。Workflow 门槛很低，会不会你都可以根据自己的需求把几个方块来回摆弄摆弄运行运行试试，先从两三个方块儿那种做起，慢慢把积木搭起来。

#### 易于分享

做成一个 Workflow ，想分享给别人是非常容易的，只要点击 Workflow 界面右上角的齿轮就可以看到分享的选项。Workflow 的分享机制只要是生成一个链接，然后将链接通过你选择的分享渠道分享出去。任何人只要点这个链接就可以看到你的 Workflow 的大概内容，然后点按下载就可以直接下载到自己的 Workflow 里。下载了的 Workflow 可以直接查看具体的内容和编辑，所以这非常利于学习和交流。

#### 易于学习

同时由于它直观，你不仅容易摸索，而且容易学习。学习有很多种，学校教授的内容由于系统性是很强的，所以我们一般要从头学起，从基础学起，那样的弊端就是漫长且枯燥。Workflow 不一样，Workflow 不一样，打开应用，你就可以看到顶部状态栏有个 Gallery：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/37739EF8-3EB2-48E7-9293-01A7DE2C053A.png)

Gallery 里内置了不少作者已经编写好的 Workflow 供你使用参考学习。你可以直接下载别人的 Workflow，看看他是怎么弄的。这样的应用实用目的很强，你有什么目标，你就参考什么方面的 Workflow，然后自己再结合自己的情况修改，就能做成一个为你所用的 Workflow。

### 哪哪都能用

大多数效率应用执行动作的时候最大的问题是「离不开自己」，每一次想启动某个特别的动作都需要进入特定的应用才能进行。Launcher 想到了从通知中心激活这些动作，然后就 [被苹果封印了](http://jbguide.me/2014/09/28/apple-takes-off-launcher/)。Workflow 则是运用了 iOS 8 的 Extension，分享插件是 iOS 上覆盖度仅次于通知中心的操作界面，这就让 Workflow 在不越线的情况下超越了「一个应用」而遍布于 iOS 的各个角落。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/95EC88FA-BD40-4F25-A0E9-16CF2D69D9DF.jpg)

结合 Workflow 支持 URL Schemes，它就能充当很多应用临时的分享插件，比如 Command-C、Instagram、Editorial 等等。

而且 Workflow 也可以在 Safari 里大显身手。比如下载某个视频网页中正在播放的这个视频；又比如在网页里选择了某一句话，把它按照「出处，引用文本，日期」的格式保存到 Evernote 等等。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A05E500E-D707-4104-A627-AD44CBF627BF.png)

### 独特的内置动作

Workflow 与大多数效率类应用最不同的一点是，它的主要内置动作不在于串联第三方应用的配合（当然和第三方配合得也很好），而是挖掘 iOS 内置功能。通过应用内部的引导你已经知道了 Workflow 可以调用相机，并且可以设定拍一定数量的照片后启动下一个动作。其它的内置功能还有获取联系人信息、查询日历中某一天的事件等等。在 Workflow 里，如果你使用 Apple 的地图应用的话，当你要计算到某地的事件的时候，它甚至可以让你先选步行还是坐车。

除此之外 Workflow 里有许多功能型 [3](https://sspai.com/post/27733#fn:3) 的内置动作是效率应用里独有的，比如把文件压缩、把结果制作成一张 PDF、把内容保存到 iCloud 等等。

而对于第三方应用它也有很多独特之处，比如你一定没有用过任何一款应用在分享照片到 instagram 的时候，是可以自动帮你把你想要加上的那句话给填好的。Workflow 就可以，而且仅是一个内置的动作。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/B536E387-F78C-43D7-93FD-4A679D091CCD.png)

### 复杂动作

Workflow 可以通过「Variable（变量）」、「If（条件匹配）」、「Repeat（重复）」、「List（列表）」、「Menu（菜单）」之间的配合来制作相对来说较为复杂的动作，这些是你不需要具备编程知识，只要思路清晰就能摸索出来的。

#### 变量

举例来说，你要在 Day One 里记一篇模式化的日记 [4](https://sspai.com/post/27733#fn:4)，里面要写上你今天读了什么书，做了什么有意义的事，吃到了什么特别的东西等等，最后可能还要附上今天拍到的一张好照片。这些内容在 Dayone 你打算用表格来呈现，所以会用 Markdown 来制作表格：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/3327F0DF-A35E-4804-B6A6-B871C404CC3E.png)

我们来看这个表格，「书名」「菜名」「事件」都是变量，它们是变化的，但表格左边那一栏的内容是每次都一样的，所以你不应该每次都制作这个表格，而应该让某个应用帮你把表格制好，你就直接填空就行了。这个活交给 Workflow 干非常合适，因为你可以通过「Ask for input」在 Workflow 里自制对话框：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/D134B850-6725-43DA-93B0-7B6799F45F8E.png)

按照图里的填好的话，每次你的 Workflow 运行到这个「Ask for input」，就会出现一个对话框，来提示你填写什么内容：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/E00F611C-8071-455C-BF8C-B4B9F8291B43.png)

然后它你可以把你临时输入的内容设为变量，这些变量最后会全部进入表格结构里，一起发送到 Dayone。

变量是 Workflow 的神髓之一，变量让你整个 Workflow 变得更加灵活。比如你做一个兑换汇率的 Workflow ，你把两种货币如果定死（比如说是 USD 跟 CHY），那这个 Workflow 的功能就很局限，只能转换你设定的这两种汇率。但如果你把两种货币设为你临时填写（或通过列表选择）的变量，这个 Workflow 就能应付多种货币间的汇率转换了。掌握好变量你就可以通过 Workflow 做到很多其它效率应用做不到的事情。

#### 条件

我们所说的条件就是「当 ' 什么什么 ' 满足的时候，就会发生 ' 什么什么 '。」这个「当」是假设，英文就是 If。

Workflow 提供了 If 语法，你把它拖到你的 Workflow 里就会看到：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/8E358D36-2F70-4F4E-B9D4-99D06D38786F.png)

If 框里有一个「String Contains」，它的意思是「字符串包含」，后面空余的部分是要你来填写包含的内容。这个动作的原理是从上一步的结果中匹配需要的字符，来精简选项（理想的话可以精简到一项），让整个 Workflow 更智能。

比如说搜索歌词，我在播客 [5](https://sspai.com/post/27733#fn:5) 里说这可能是上手 Workflow 以后的人玩的最多的一个东西了。但是大家一般做的都是「获取名称」——google.com/search?=||input||。这样做出来的 Workflow 还不如你直接从 Spotlight 搜呢对吧。我们用 Workflow 起码要让它直接打开正在播放的歌曲的歌词网页才过得去吧。这就需要用 If 来匹配内容，比如在 Google 搜索英文歌词，一般「Azlyrics」这个歌词站的内容都会出现在最前排，那么你就可以使用 If 来进行条件匹配，在「String Contains」后面输入「azlyrics」。这样的话你就能直接打开你搜索的歌词在 Azlyrics 这个网站的页面。

#### 重复

玩手机的人都知道自己的手机里会经常留下很多屏幕截屏，这些截屏你要么是发给朋友看一下，要么是在社交网站上晒一下，要么是写测评要用到。无论什么用途，一部分截图在一次使用以后就没有保留的意义了。但是大多数人应该不会用完就删，所以低头看你手机相册你大概会发现很多截图。怎么一次性地选择所有截图，然后有选择的消灭掉这些截图？

用了 Workflow 的话你就会知道，它可以帮你读取截图，也可以一次性帮你都删了。但如果你想自己决定删哪张不删哪张，就需要用到重复。在 Workflow 里要用的是「Repeat With Each」这个动作。

Repeat 和 If 经常会搭配起来用，用于匹配内容会很有帮助。

### Web 相关的动作

Workflow 这个应用目前能力的上限，应该就是它与 Web 编程相关的能力。如果你具备 JSON、正则表达式的匹配语法等知识，你就可以直接从开放了 API 的网站获取其实时的消息。

内置的 Gallery 里就有个 Workflow 是匹配正则表达式来获取二维码中的 html 链接：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/EBB6D7E2-0B02-4206-9DA8-9893E95152A8.png)

比如你可以通过 Google Exchange Rate API 获得实时的汇率，你可以通过 Yahoo Weather API 获得实时的天气数据等等。然后你可以把它们作为你 Workflow 的一部分，设定变量，最后在 Workflow 里写出一个个汇率程序或者天气程序。

结语
--

一般这样的应用都要回答「适合我吗」这样的问题，但这样的问题其实只有了解自己使用情境的你才能回答。如果你担心你不会用，这问题不大，因为我接下来还会出教程，而且这个应用小白是很容易上手的。很多人包括折腾老手上手这个应用的困难在于不知道怎么用，不知道思维怎么从 Launch Center Pro 这样的应用逻辑里跳出来，结果就做了类似于「百度搜索」这样的谁都能干而且不能体现这款应用价值的 Workflow。在这点上，效率应用新手可能要比老手有优势，因为没有思维桎梏。

文章里影影绰绰地提到了一些 Workflow 的逻辑和用法，但是没有给出链接。这是因为这篇不是教大家怎么具体制作 Workflow 的文章，而只是简述 Workflow 是个什么应用。在之后的教程里，我会给把文章提到的 Workflow 还有我制作和搜集到的 Workflow （的链接）分享给大家，并且分析讲解值得学习的 Workflow。如果你很有欲望获得一些现成的 Workflow 并自己开始学习或者折腾，那么你可以看看 Reddit 的 [Workflow 区](http://reddit.com/r/workflow)（Workflow 的作者偶尔会出现在这里），或者人们分享到 Twitter 里的 [Workflow 动作](https://twitter.com/search?q=workflow.is/workflows)。

Workflow 目前并不是个成熟的应用。硬伤方面就有中文支持不佳 [6](https://sspai.com/post/27733#fn:6)、某一步运行失败就有可能闪退（或者有时竟然可以继续运行下去，但当然已经毫无意义）、偶尔会挂起（应用一直处于登录界面）、其他应用中打开 Workflow 时有时无、在其他应用运行 Workflow 后不消失…… 除此之外，使用体验方面的考量也非常一般，比如你做一个比较长的 Workflow 的话，每一次拖动作到你的 Workflow 里都得从最上面拖到最下面，应用本身要是特别稳定还好，拖到一半儿就闪退可真受不了。

就目前的使用体验来说，我想说它是爱折腾的人的玩具更为合适，但是 Workflow 的团队并不是一个只顾利益的态度高冷的商业团队，Workflow 的团队是一堆热血的年轻人，他们还在 Twitter 上[招募](https://twitter.com/WorkflowHQ/status/543868075431305217)那些乐于助人又想挣点外快的人作为 Workflow 的客服人员，所以我想他们是能够听进用户意见并能积极地进行修改的。

最后，如在播客里所说，我觉得这款应用的未来将会是一片光明。

---

1. [From Jailbreaks To App Store Awards, Developers Grow Up iPhone](http://techcrunch.com/2013/09/04/from-jailbreaks-to-app-store-awards-developers-grow-up-iphone/)
2. 见 Contrast 创始人 David Barnard 在 [Twitter 上公布的数据](https://twitter.com/drbarnard/status/544219666722201600)
3. 功能型动作就是它本身是一个完整的功能，而不是参数匹配之类的中继型动作。
4. 模式化日记可以参看格志这款应用的思路，对于想写日记但不知道写什么的人来说，模式化日记是个很好的开端。
5. [TalkJB 第 46 期：关于 Workflow 的头脑风暴](http://jbguide.me/2014/12/14/talkjb-46/)

一些 URL 里包含中文就会必然闪退，向上文提到的发送中文日记到 Day One 就会导致闪退。

---

### Workflow 系列文章

Measure

Measure

|  |
| --- |
| Workflow 教程（二）：Workflow 基础用法 Source URL:<https://sspai.com/post/27846> |

Workflow 教程（二）：Workflow 基础用法
============================

2014 年 12 月 31 日

本文首发于 [越狱指南](http://jbguide.me/) ，原作者 [Jailbreakhum](http://weibo.com/u/2208752785 "由jailbreakhum发布") ，少数派经由原作者授权转载此文，仅对文章标题及正文版式、用词略有改动，[点此](http://jbguide.me/2014/12/30/getting-started-with-workflow/) 查看原文。

---

[上篇文章](https://sspai.com/27733) 算是大略地介绍 Workflow 是什么的引文，这篇开始将要正式地使用 Workflow 了。第一篇文章将直接以大家最常用的社交网站为例来介绍 Workflow 的基础用法。

具体内容是：

1. 把同样的文字内容一次性发送到 Weibo 或 / 和 Twitter。
2. 把同样的文字 + 图片一次性发送到 Weibo 或 / 和 Twitter。
3. 通过 Share Sheet 分享任意链接并且加上自己想说的话，然后发送到 Weibo 或 / 和 Twitter。
4. 将以上三步合并为一个 Workflow，执行时选择其中一个然后让 Workflow 自动进行后面的工作。

将文字内容送到  Weibo 或 / 和 Twitter
----------------------------

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/57F91CD4-4A36-4851-B4CA-AAED4866766E.png)

▲ 在这里用到的动作只有三个

### Text

Text 是最简单也比较常用的动作，最关键的是我们对它非常熟悉 ——「就是个输入框嘛，往里打字就可以了呗。如果你这么想就对了，这软件上手就是这么的傻瓜式 —— 你要做的就是把想发的微博内容输入到 Text 的文本框里。

### Ask for Input

上面介绍的是 Text 文本框，我们看到它非常熟悉，但是它的一大缺点是会保留上一个操作留下的内容。也就是说，你每一次通过 Workflow 发微博，都需要把上一次发的内容先删了才行。所以我实际上建议在这个 Workflow 里实用 Ask for Input 这个动作。

Ask for Input 这个动作也是 Workflow 里最常用的动作，我在 [上一篇文章](https://sspai.com/27733) 也提到过它。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/5C81E04C-1865-4690-87B0-51ABD4F0F2F4.png)

你把 Prompt 里填上「微博内容」，这样每次打开这个 Workflow，直接点击运行。它就会弹出个对话框让你输入微博内容。

### Tweet

Tweet 的动作框里，前半部分写着「Show Compose Sheet」意思是「显示内容编辑框」，后面是一个开关：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/20381850-DDCB-4920-A033-89FF0B71B2B8.png)

▲ 内容编辑框

如果你把开关打开，那么就是选择显示内容编辑框，这么做的优势在于：

1. 可以看到文本（图片）内容、字数。
2. 如果你是多账户的话，临时可以选择账户。
3. 可以临时修改内容。
4. 可取消该步骤

但想必你会马上意识到「我刚写好的东西有什么可修改的？」所以其实显示内容编辑框的优势并不明显。而关闭那个开关，也就是不显示内容编辑框的话，界面就会变成这样：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/4A2832D6-2F76-4DAE-82DD-0539BA8579D5.png)

▲ 关闭开关

它的好处是：直接后台发送内容，省掉你点击编辑框的时间，以及等待发送成功再进行下一步的时间。

但是如果你确实有选择账户的需求，又不想看到内容编辑框浪费时间呢？Workflow 同样可以做到：按下 Tweet 动作框里选择账户的部分，你就能看到一个弹出菜单，里面会有 Ask When Run、Clipboard、Input 三个选项，你选择 Ask When Run，就能在动作进行到这一步的时候自动出现一个对话框来问你选择哪个账户发送。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A5F32C6D-FD5D-4C7E-B30D-0091D825941A.png)

注意，在内容编辑框里，我们需要先按一下选择账户那个位置 —— 也就是说我们要先看一下那个位置在哪 —— 然后再选择账户。而在 Ask When Run 这种方式下，我们是直接选择账户。

另外，记住，在 Workflow 这款软件里，凡白皆可点，每个动作框里只要有白色的区域就是可以点的，只要有菜单出现就至少能看到 Ask When Run、Clipboard、Input 这三个选项，活用 Ask When Run 能让你做到一些你认为你做不到的事。

### Share

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/EB669819-7FDA-4FD8-86BC-B03D5733744D.png)

Share 这个动作就是大家最熟悉的分享按钮了，之所以要用到它是因为 Workflow 在当前版本（1.0.1）还没有支持微博的分享功能，等到支持了应该就能和 Tweet 这个动作一样，可以在后台发送。也就是说，你只要编辑好内容，点一下发送，剩下的 Workflow 帮你做好。

将文字 + 图片发送到 Weibo 或 / 和 Twitter
-------------------------------

在这一步我们将谈到变量，你会发现它果然也很容易。

会发文字微博了，图文微博怎么办。在文字微博那个 Workflow 上再加几步就能做到。

### 选择照片

在动作列表里找到 Select Photots 这个动作，用它来选择照片。拖到你的 Workflow 里以后你会发现有个 Select Multiple 的开关，打开就能多选图片，但是 iOS 本身不能上传多图到社交网站 —— 你可以自己试试在相册里选择多图的话，Twitter 和微博这两个选项都会不见的 —— 所以 Workflow 以及任何通过 iOS 内置的功能去分享照片的办法只能分享一张照片。所以这个开关在这个 Workflow 关上就行了。

另外，如果你经常分享最后一张照片（或者是手机截图）的话，你可以在 Workflow 的动作列表里找到 Get Latest Photos 和 Get Latest Screenshots 这些选项，拖到 Workflow 里试试看会有什么效果～

### 设定变量

终于看见「变量」这俩字了，是时候克服你从初中数学开始就对这两个字产生的恐惧了。

为了节省时间，我们要使用 Workflow 把两种不同的内容（文字和图片）作为一个整体发送出去。这一点的困难就是你得告诉 Workflow 他们俩（文字和图片）是一起的。在 Workflow 里的做法，就是：把文字放到一个变量里，把图片放到一个变量里，然后把这俩变量合成一个变量，交给 Workflow。

具体的操作是，在动作列表里找到 Set Variable 也就是「设定变量」这个动作，然后拖到 Select Photos 这一步的下面，你会发现这两个动作中间连起了一条线，这就说明 Workflow 明白了你要把你选的那张照片设为一个变量。然后你可以在 Set Variable 后面的空白处输入你想输入的东西，我在这里输入了「图片」，你可以输入「img」，它就像给这张图片起了个临时的名字，什么名字都可以，中文英文符号只要你明白就都可以。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/E6874D95-5BA2-447F-8CFB-51B1DAAA1FCB.png)

所以你可以这样看 Workflow 里的变量 —— 给前面那一步的结果起个名字。

### 添加变量

前面说到，我们在这里用变量的原因是要用 Workflow 把两种不同的内容（文字和图片）作为一个整体发送出去。所以要给图片起个名字（设个变量）、给文字也起个名字（也设个变量），然后把它俩放在一起成为一个组合，再给组合起个名字（设个新变量）。

在 Workflow 里，这个步骤要分开来做。也就是说，图片起了名字以后，直接就可以成立组合，等一会儿给文字起名字以后把他加到这个组合里就行了。这在 Workflow 里的具体做法是：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/3BD293B4-15F2-4F49-9255-6321A57C2278.png)

在动作列表里找到 Add to Variable 也就是「添加到变量」这个动作，拖到你的 Workflow 里，Set Variable 这一步下面，那条连接的线就又会出现，你应该已经懂得它代表什么了。同样，这个组合的名字你可以随便给，我给的是「图文」。

### 对文字的处理

我们现在已经把文字和组合的变量设妥了，现在要处理文字了。我们要给文字设个变量，再把文字这个变量加入到组合的变量里。具体做法是：

把 Set Variable 拖到 Ask for Input 下面，给它起个名字；再把 Add to Variable 拖到 Set Variable 下面，注意，这里现在要填的是组合的名字，你不能再胡给名字了。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/199A0B78-DF89-4286-87FB-1EE98BE16D13.png)

### 删除照片

Workflow 可以在处理完照片以后删除这张我们再也不会用的照片，在这个 Workflow 里，只要你把 Delete Photos 这一步放到 Share 这一步的下面就可以了：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/FD43B8AA-17D3-421A-8E2C-9ECB7EE86529.png)

Workflow 里有修改图片的功能叫做 Edit Photo，这个在分享照片的时候很实用，一般你给人看图片就会有希望让他看的那个「点」，通过 Edit Photo 你就可以把你想让对方看的地方标记出来。那么你能不能在这个环节介绍的 Workflow 里加上 Edit Photo 这个动作，让你的 Workflow 更实用？

有时候人们分享图片是只想分享图片，不加字儿，但是新浪微博要求必须加字才能发微博。所以它官方客户端在只分享图片的时候的做法是自动添四个字「分享图片」。通过 Workflow 能不能做到？

通过 Share Sheet 分享任意链接发送到 Weibo 或 / 和 Twitter
--------------------------------------------

有时候你看到了一篇网站或者在你的 RSS/Read Later 客户端里读到了一篇你想分享的文章，你在 App Store 看到了一个好的 App 或者游戏，你想把它同时分享到 Twitter 和微博，通过 Workflow 也可以轻松做到。

### Workflow Type

在这个环节我们要接触 Workflow Type，它只有两种，所以没什么难的。

查看 Workflow Type 的方法是在每个具体的 Workflow 的右上角寻找齿轮图标，里面是一个菜单，其中有一项是让我们选择 Workflow Type：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/E6282C6F-AE14-4880-96E6-290E935D4591.png)

* Normal 类型的 Workflow 不会出现在 iOS 的分享菜单里面，只能通过 Workflow 这个程序本身运行。前面的内容都是在 Narmal 这个类型里完成的。
* Action Extension 类型的则可在 Workflow 程序内运行也可在分享菜单中运行（Workflow 的相应位置有图解）。我们在这里要用到它，比较强力的 Workflow 一般都要用到它。

我们选择 Action Extension 能看到 Accepts 这个选项，打开后里面有一个列表，这个列表里显示的是 Workflow 分享菜单里接受的数据类型。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/C09C0C4A-A649-43B1-A08D-16E44382B09B.png)

我们在这里是要分享链接到微博和 Twitter，所以可以把其它的都删掉只要留下 URLs 就可以。

这其实已经是「分享链接到微博和 Twitter」这个 Workflow 的第一步 —— 获取链接，下一步我们要做的，就是要给链接设一个变量 —— 我在这里设置的是「链接」—— 好把这个链接和我们一会想发的微博放在一起。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/57E18DA4-7405-4E47-AC5A-D50E4C23E6E4.png)

然后下一步，我们要开始输入微博正文了，我们还是和以前一样要用到 Ask for Input ，然后给它的结果也设置一个变量，我在这里设置的是「正文」。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/F2C00045-4311-4143-B871-44DDD2AA786C.png)

最后通过 Text 框把两个变量放到一起。这一步有点小技巧：当你点进 Text 框，你会发现弹出的键盘上有 Ask When Run、Variable...、Clipboard 这三个按钮，选择 Variable...，你就可以看出一个弹出的菜单，里面有你在前面设置好的所有变量。比如说我前面设定了选择其中的变量，就会在 Text 框里出现一个套着蓝色框的变量 —— 这就是 Workflow 的自定义变量的表现方式：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/9E93DF11-4CDA-404F-A22E-0FDAF9FE5368.png)

到了这一步的逻辑是，你给链接设了个变量（link），然后输入微博，给这个微博内容也设个变量（正文），最后在 Text 框里面给这两个变量排一下顺序，决定让微博内容在先还是链接在先，最后将 Text 框里的整体作为微博发送出来。所以最后不要忘记加上 Tweet 跟 Share 这两个动作。

既然是分享链接（一般是文章）到社交网站，比较方便的办法其实是直接引用文中一段话作为对这个链接的介绍。所以你可以想想，能不能这个环节介绍的 Workflow 稍作改动，做一个「Clipboard+link 的 Workflow」？

如果你不只想分享链接，还想分享 Safari 里看到的文章的标题，要怎么做？试试看 Get Name 这个动作。

将以上三步合并为一个 Workflow
-------------------

我们用效率软件是因为我们「懒」，所以既然懒了，就要有懒到底的精神。

现在你已经分别掌握了发送文字内容 / 图文内容 / 链接内容到微博和 Twitter 的方法。如果你三种使用情境都有的话，这就意味着你要做 3 个 Workflow 了。做三个 Workflow 没什么不好，唯一的缺点是「不够懒」。既然都是把东西发送到微博和 Twitter，我们能不能把它们做到同一个 Workflow？让我们做到在分享内容的时候只用这一个 Workflow，然后弹出一个菜单里面有「文字微博」、「图文微博」、「分享链接」，然后我们需要哪种分享方式就选哪种分享凡事，剩下的交给 Workflow 来处理。

答案自然是可以。在这里我们要介绍 Workflow 这款软件里复杂动作的核心内容 ——List、If 和 Choose from Menu。

### List—— 列表

我们要做的是要弹出一个菜单，里面有「文字微博」、「图文微博」、「分享链接」给我们选，所以这第一步，可以是一个列表。从 Workflow 里找到 List 拖到你的 Workflow 里，在里面分别写上「文字微博」、「图文微博」、「分享链接」，行不够了可以按添加按钮来添加行。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/BC2EAEF4-C2AF-449A-A1C5-CFD0F0B252A7.png)

然后我们要从这个列表里选一样，所以要用到 Choose from List 这个动作。同样，找到它然后拖到你的 Workflow 里。因为我们选的是其中「一项」，所以可以把「Select Multiple」这个开关关闭。

然后下一步，就是选完其中一项以后，让 Workflow 知道你选的是什么，然后执行之后的操作。那么其实这里面的逻辑是：

* 「如果」我选择的是文字微博，「那么」就让 Workflow 执行关于文字微博的操作；
* 「或者」我选择的是图文微博，「那么」就让 Workflow 执行关于图文微博的操作；
* 「又或者」我选择的是分享链接，「那么」就让 Workflow 执行关于分享链接的操作。

### If—— 条件

这个「如果…… 那么……」在 Workflow 里就是 「If 语句」，上述的逻辑在 Workflow 里的操作是：

把 If 拖进 Workflow，你会发现它和其它动作不太一样。If 会带下来 otherwise 和 End If 两个配套的动作。

我们在 If 框里的「String Contains」后面，输入「文字微博」。然后在这一步的下面，把发文字微博的 Workflow 的动作 ——Ask for Input、Tweet、Share 依次排好：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/3060D52C-694C-4B1A-98FC-FF3A7F6A5106.png)

图片中 If 下面的内容，都会有一个缩进，它的意思就是这些缩进了的内容都是在 If 框里设定的条件达到后才会运行的。这整个一步完整的意思是：如果我们在 List—— 列表里选择的内容里有「文字微博」，我们就执行文字微博的 Workflow。

做好文字微博这部分了，我们反回头看 Otherwise 跟 End If。

如果你的 Workflow 只匹配一个条件，匹配到了就执行该条件下的内容，匹配不到就拉倒的话。你就不需要管这个 Otherwise 跟 End If。比如说，你想吃苹果，不想吃任何其他水果，然后你去菜市场买苹果。这个情境用 If 来表示就是：

If 有苹果，买 ——Otherwise 没苹果，不买东西 ——End If。

在发微博这个情境里，我们有三种情况。第一个 If 我们匹配了「文字微博」，第二个 If 要加到哪？加到 Otherwise 下面：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/4B911E87-FD47-4443-94C3-404825CD1AC1.png)

这就成立了一个新的关系：If—— 如果匹配到「文字微博」，就执行文字微博的 Workflow；Otherwise If—— 或者匹配到「图片微博」，就执行图片微博的 Workflow…… 所以相信剩下内容已经不用再说了，包括最后一个「分享链接」的 Workflow 你也应该知道该怎么办了。

### Choose from Menu—— 从菜单中选择

通过 List 和 If，你已经做到了把 3 个同类 Workflow 合并到一起，它们两个的合作还会有更多强大的功能。但是，在我们这个「分享微博」的 Workflow 里，它们不是最合适的。因为 If 只是匹配我们在 List 列表里选出的结果的内容的字符，不是我们想要的「选了菜单的某一项就自动进行这一项下的内容」，两者有本质上的不同。

最合适这个 Workflow 的功能是 Choose from Menu：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/2BFEBD8D-5F33-4E68-8603-368892CC5C1E.png)

把动作拖到你的 Workflow 里，在菜单填上「文字微博」、「图文微博」、「分享链接」，然后相关部分的名字自然也会发生改变，然后你可以在「文字微博」这一项目下做你的文字微博的 Workflow ，在「图文微博」的条目下做图文微博的 Workflow……

Choose form Menu 在这个分享微博这个需求下明显直观许多，也比 If 要精确。但也正因如此，它没有 If 的应用面广。在 Workflow 里，做出来一个能运行的 Workflow 是第一步，找到最适合它的动作把它优化到最简单最直观是终极目的。

为什么用这种办法发微博？
------------

1. 方便
2. 减少干扰
3. 减少对别人的干扰

### 方便

如果通过 Workflow 做某件事不如用以前的方法简便，就不要用 Workflow。

在「同时发送微博和 Twitter 」这个情境下，使用 Workflow，你就不需要分别打开两款软件的微博客户端，不需要等待客户端的读取，不需要看某些客户端的启动广告，然后不需要去点击编写按钮，甚至不需要去点击发送按钮；在分享链接的情况下，你不需要去点 Safari 的地址栏去全选链接，然后再复制链接，然后再分别打开两个客户端，重复前面提到的动作…… 高下立判。

### 减少干扰

微博客户端不只是个分享内容的地方，还是个浏览内容的地方。所以它的问题在于，你虽然最初是只想「发一条微博」，但开了微博客户端以后，你就不只是发微博了，你的 Timeline 吸引着你，瞥了一眼搞笑图片结果「哈哈哈哈哈」个不停，一不小心一个小时就没了，说不定最初你想发的那条微博都没发出来。

### 减少对别人的干扰

其实如果只是图方便，用 IFTTT 也可以做到，而且好像比 Workflow 还简单些。但是 IFTTT 是无条件地将一个服务的所有内容全部转到另一个服务，这点很蠢，更重要的是这样很骚扰人。如果你的微博昵称跟 Twitter 的用户名一样，当那些用 IFTTT 的人用微博和 Twitter 中的一个服务 at 你，另一个服务就也会 at 你。此外，你在微博转发一条内容 IFTTT 会把你说的话同步到 Twitter 但不会把你转发的原微博同步到 Twitter，所以如果你 Fo 了一些用 IFTTT 的人，你会看到他们总是在说一些摸不着头脑没有上下文的话。

如果你希望同时把内容微博发到微博和 Twitter，你就要首先学会取舍。这里有一个很简单的逻辑，如果你两个地方说的话都永远一样，那别人（除了表示关系好以外）有什么必要两个地方都 Follow 你？你可能会说你的粉丝里有那种只用其中一种服务而不用另一种服务的人，这点其实没那么有必要担心，只要用 Twitter 的人，几乎都会用微博。相信我，那些故意不用微博只用 Twitter 的中文 microblog 使用者，不太会在意一个用 IFTTT 无筛选地同步所有内容的人所发的东西。

与 Launch Center Pro 比较的优势
-------------------------

使用 Launch Center Pro 时间久的朋友应该都知道通过 Launch Center Pro 也是可以做到分享文字 + 图片或纯文字内容到 Weibo 和 Twitter 的。[@饺子如何是好](http://weibo.com/u/3183472515) 就曾做过一个 Launch Center Pro 的 [动作](https://launchcenterpro.com/dhh0sw) 来完成这两个功能。

你可以点开网站看一下那个 URL Schemes 。它和 Workflow 到底谁简单我们另论，且说功能本身，与 Launch Center Pro 相比，Workflow 在这个动作上就有至少两个优势：

第一：我们总会遇到那种想发到微博或 Twitter 其中某个地方而，由于 Launch Center Pro 不支持 x-cancel，所以如果你是按照先发推后发微博的顺序写好 Url Scheme 的话，你就不能临时取消发推这个动作，因为一旦你取消发推的话，动作就被中止了，后面发到微博的那一步就不会执行了。而 Workflow 则能够中断其中一步而执行下一步。换句话说，比如你习惯了通过 Workflow 来发送原创微博，有些内容你不想发到 Twitter 只想发到微博，那你可以在 Workflow 里取消发送到 Twitter 而进行下一步发送到微博的操作。

第二：Workflow 支持分享插件，这一点是非常聪明的，它让 Workflow 直接渗透到了 iOS 的各个角落。

复习
--

读完这篇文章，你应该熟悉的关于 Workflow 的内容有：

+ Text 文本框
+ Ask for Input 功能（以及它和文本框的区别）
+ Tweet 功能（Show Compose Sheet 开或关有何不同？）
+ 凡白皆可点
+ Ask When Run 的作用以及何时使用
+ Set Variable 设定变量
+ Add to Variable 添加到变量
+ 部分关于图片的动作
+ Workflow Type & Action Extension
+ List 列表
+ If 条件
+ Choose From Menu 从菜单中选择

---

### Workflow 系列文章

Measure

Measure

|  |
| --- |
| Workflow 教程（三）：Workflow 本身能做什么？ Source URL:<https://sspai.com/post/30903> |

Workflow 教程（三）：Workflow 本身能做什么？
===============================

2015 年 09 月 01 日

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/7E5D4988-DAD8-44E0-9DD8-300C654C3BAB.png)

编注：此为 [Workflow](https://sspai.com/post/tag/workflow) 系列教程补全计划，本文首发于 [越狱指南](http://jbguide.me/2015/02/19/what-can-workflow-do/)。

---

在[《如何上手 Workflow》](https://sspai.com/27846)中用「同时把内容发送到微博和 Twitter」这个例子带大家体验了一下 Workflow 的简单易上手。但是 Workflow 不是一款这么简单的软件，它值得按部就班地学习。在这一部分，我们先看看 Workflow 跟 iOS 内置的那些原生软件结合可以做出什么样的事情。

确定 Wi-Fi 后再打开相应服务
-----------------

我时不时的会看 Twitch 上一些游戏直播，我只看原画质所以对网速有一定的要求。我平时出门用的是移动 Wi-Fi，回家以后用家里的。移动 Wi-Fi 供不起原画质，但是因为它一直关联着设备，所以导致有时候我从外面回到家想看 Twitch 的时候，打开 Twitch 觉得卡，然后才发现原来手机连的还是移动 Wi-Fi。

所以我利用 Workflow 内置的 Get Network Name 这个动作，做了个 Workflow：

检测现在连接着的网络的名称 → 如果名称包含的是家里 Wi-Fi 的名称 → 通过 URL Schemes 打开 Twitch → 如果匹配的不是家里的 Wi-Fi → 弹出换 Wi-Fi 的提示。

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/0DCA11B8-2033-429C-A891-5E2695BAAF66.jpg)](http://cdn.jbguide.me/wp-files/2015/02/15.jpg)

我把这个 Workflow 放到 Launch Center Pro 里，来代替我打开 Twitch 的动作。而且 Launch Center Pro 还可以基于地理位置提供提示，这一点也值得好好利用。

条件匹配 ——Filter
-------------

Workflow 在 2 月 13 日发布了它的 1.1 版本，Filter 就是其中最亮眼的更新之一：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/288C585A-368B-425D-B1E7-5497D9087B34.jpg)](http://cdn.jbguide.me/wp-files/2015/02/25.jpg)

Filter 可以精确地分类和定位你的各种资料和信息，Mac 上，从某种程度上来说，有没有 Filter 是判断这个软件在同类软件里的地位的一个标准。在这里，我打算用图片的 Filter 来具体说明它是什么。

比如说我手机容量不够了，一看相册里有 1000 张照片，而且好多都是屏幕截图，那我第一步肯定是把屏幕截图都删了，但是除了一张一张看以外，有什么办法能够精确地一下把所有的截图都给提出来呢？最简单的办法是分辨率。屏幕截图的图片的宽和高肯定和屏幕一致，所以你只要知道其中一项，你就能匹配出截图。而且 Workflow 甚至提供了专门的 Is a Screenshot（是屏幕截图）的选项，避免你相册中有那种和屏幕截图分辨率一样的图片。

比如我要筛选出所有 iPhone 5 的屏幕截图，它的 Filter 就是这样的：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/02B3FCBE-AC1B-4930-A682-AAF8913F3077.jpg)](http://cdn.jbguide.me/wp-files/2015/02/33.jpg)

首先来看框里的第一条：All of the following are true（符合所有条件），点它你能看到另一项：Any of the following are true（符合任一条件）。

这两项是 Filter 的第一前提，你必须先告诉软件你下面列出的条件它需要都匹配还是匹配到任何一项就可以。一般来说默认的是匹配所有条件，但符合任一条件也是很有用的，但这里不展开说了。

然后来看上图里颜色不同的部分。每个颜色不同的部分都是一个菜单，可修改：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/CA4C2261-ECDF-4FEF-A4C2-6F468B462A3F.jpg)](http://cdn.jbguide.me/wp-files/2015/02/41.jpg)

Filter 使用的思路就是：一般来说你要先确定一个对象或者类型，再确定一个范围，再确定具体的起始数字。学会使用 Filter 可以让你更清楚你要操作的对象是什么，让你更清楚你要干什么。这种思维方式不光在使用软件和智能设备上有用，在日常生活中也很有用处。

找餐馆然后打电话然并确定路线
--------------

有时候决定吃什么是个问题，而且还有个问题是你决定好吃什么了以后那里有可能没空位了。所以不知道吃什么的时候，在自己常吃的类别里选一样（甚至可以或者随机选一样），然后马上给店家打预约电话，同时获取最短路线应该是个很实用的功能。

应该的意思是，根据 Workflow 支持的地图在我国的表现，本功能实际上可能并不那么实用……

这个 Workflow 的起始是选择一项我们常吃的东西，所以我们需要做个列表。[上篇文章](http://jbguide.me/2014/12/30/getting-started-with-workflow/)里我写过了 List 的用法，但这里有更简单的创建 List 的方式，其中用到了 Split Text（分割文本） 这个功能：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/069E6BE2-45F1-4B63-A2CF-CDBF1EDCF15D.jpg)](http://cdn.jbguide.me/wp-files/2015/02/5.jpg)

当你把列表做出来，就得在里面选一个，前面说可以随机，是你实在没主意的时候，可以用 Get Item from List（从列表中获取）这个动作 ，它内部有个动作是 Random Item（随机一项）。而如果你有主意的话，可以在列表下面接 Choose from List（从列表中选择） 这个动作。

选出一个类别以后，就可以利用 Workflow 里 Search Local Businesses（搜索本地商户） 这个动作，来搜索具体饭店了。同一类别的店铺未必只有一个，所以你还要再接一个 Choose from List（从列表中选择）来选一家你想去的店铺。

在地图信息里，一般都会有店铺的电话，所以你可以用 Get Phone Numbers from Input（从 Input 中获取电话号码） 这个动作从店铺信息中获取电话。下面再接上 Call 这个动作，就能在获取电话号码后直接打电话预约了。

至于怎么同时搜索并确定路线，你可以自己想想。

快速得到具体某天的空闲时间
-------------

动作略复杂，可以先在自己设备里下载了这个动作后结合文章理解。

这是 Workflow 的 Gallery 里自带的一个动作，叫做 Share Availability。它是和 iOS 的日历软件相结合的一个非常有用的动作，当别人问你具体某天什么时候有空的时候，有时候你也不清楚，你需要查看一下日程，最后自己总结一下什么时候有闲，给别人答复。这个工作，Workflow 完全可以帮你做到，不过前提是，你会把你每天的事务安排记录在 iOS 设备上的日历里。

除了实用，这个 Workflow 里还够复杂，里面涉及了不少具体的动作的用法，研究透它以后这些动作你就都能搞懂了。

首先是 Get Upcoming Events（获取接下来的日历事件）：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/2E9316D2-CE71-4137-9E7E-1909AE04BCA2.jpg)](http://cdn.jbguide.me/wp-files/2015/02/6.jpg)

这是这个 Workflow 的第一个动作，默认选择了所有的日历（很多人不会只用一个日历，因为需要给工作、家庭、个人事务等建立不同的日历，便于区分）；下一行的 Get 20 Events 是选取 20 个事件，你可以根据自己的繁忙情况选择事件数；下一行的 Day 后面默认的是 Specified Day，你可以设为今天或者明天，当你选择 Specified Day 以后，会出现新的选项，内容是 Ask When Run，这是让你临时选择具体的一天。

下面的动作大部分都被括在 Repeat with Each 和 End Repeat（结束重复） 里，这个 Repeat with Each 的隐含要求是上一个动作的结果应该是个列表，Repeat with Each 做的就是对上个动作产生的列表中的每一项都进行 Repeat with Each 和 End Repeat 之间的所有操作。

然后来看在这个 Workflow 中， Repeat with Each 和 End Repeat 之间有什么：

第一，设定变量 Event：这是把上个动作产生的列表中的每一项都设为一个变量，在这个例子里是每一个具体的日历事件。

第二，用 Get Detail of Calendar Events 获取起始时间 Start Date—— 用 Set Variable 给起始时间设定变量 —— 并用 Format Date 将其设定为最简短的时间格式。

第三，用 Get Variable 获取之前设定的日历事件变量 Event。因为我们除了事件的起始时间，还要获得事件的终结时间。但刚才在获得起始时间的时候，我们用了一次 Event 这个事件了，如果现在直接在下面再用 Get Detail of Calendar Events 来获取终结事件，肯定会报错。这是软件不如人聪明的地方，当我们要对一个信息使用两次，我们就得调用它两次，所以要使用到 Get Variable。它是个做复杂 Workflow 非常常用的动作。

第四，和第二步基本一致，只是事件的起始时间要改为事件的终结事件。

第五，因为你这是在回答你具体某天什么时候有空，所以你回复对方的时候，也要先跟对方说那一天的日期，然后再说什么时候有空。所以你得先获取当天的日期，这第五部分就是再用一次 Get Variable 获取事件（也就是获取日期），然后 设为变量。

最后，生成一个文本框：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A48576D1-5D4D-4EFB-B03B-EE727A7963F9.jpg)](http://cdn.jbguide.me/wp-files/2015/02/7.jpg)

这个文本框里是每一个事件的起始时间和终结时间，中间有一个连接符 -。

上面就是 Repeat 的整个过程，它对每一个事件都生成了起始时间和终结时间，然后填入最后的文本框里。但是这里的文本框还不能直接用，因为它们是分开的，每个事件都有自己的文本框。如果你在下面用 Quick Look 这个动作来直接看结果，你会看到很多个分散的结果，我们必须把它们汇聚成一个结果。所以需要使用到 Combine Text，把它们聚合在一起。

最后再用一个文本框，生成最终的文本。

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/FC8748E6-CC0F-4560-B509-930091B085F9.jpg)](http://cdn.jbguide.me/wp-files/2015/02/8.jpg)

在这个文本框里， Date 是之前在 Repeat 的过程里获得过的日期，input 是继承的上个动作的结果，也就是你用 Combine Text 整合的当天所有事件的起始和终结时间。而且你要看这个文本框里，有变量，有 Input ，说明文本框里不光可以输入东西，还可以往里放变量，或者直接用 Input 来使用上个动作的结果。

最后这个文本内容你可以通过分享的方式给任何一个人。

具体 Workflow 你可以在 Gallary 的 Calander 分类中下载，你可以修改最后的文本框，让它变得更加本地化。而且你还可以获取事件名，从而你可以告诉对方，你在某天的几点到几点是因为什么没空。这些也当作业来练手吧。

图片找路
----

这部分是使用 Workflow 获取照片的拍摄地，然后可以在地图上显示从本地到照片上的地址的具体路径、或者复制地址等。这个功能的重点在于它背后的 Content Graph。

获取图片的地理位置信息有很多用处，比如，我和朋友约了一个我没去过的地方见面，他到了我没到，我问他具体怎么走，他给我拍了张标志性建筑物的照片，我从这张照片获取地址信息，然后还能在地图上打开路径，最后到了地方还能对照这张照片看看我找的对不对（比 Google 街景还要即时哟）。而且这个功能还有个家庭伦理的用法，就是你问另一半在哪，让他 / 她拍个照片给你，你可以获取这个照片的拍摄时间，来知道他 / 他是不是拿以前的照片糊弄你，然后你可以获得地址，然后你懂得。

具体的做法很简单，就是在 Workflow 里用 Select Photos 这个动作获取一张照片，然后如果你想获取路径，可以用 Show Directions 直接获取路径。如果你想复制地址，你可以先用 Get Addresses from Input 获得地址，然后再用 Copy to Clipboard 把地址复制下来。而如果你想又复制地址，又在地图里显示路径，那么你可以复习下这篇文章前面写到的内容，想想当你要对同一个信息多次的时候，该怎么办？（提示，Get Variables）

再说回这个动作，其实你应该感到纳闷，「为什么可以在照片里获取地址信息呢？」这就是 Workflow 的核心功能 ——’Content Graph’。Workflow 里对这个 View Content Graph 这动作的描述是 ——the technology that powers Workflow。

在 Workflow 里，每一个动作都会产生一个或多个结果，而它能够产生什么结果，你可以用 View Content Graph 这动作来看看它能产生什么结果。

我们把 View Content Graph 放在 Select Photos 下面，选一张你手机拍的照片，正常情况下就会出现图中的结果：

[![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/28670AF4-99CE-40C5-B04F-C81A6690AABC.jpg)](http://cdn.jbguide.me/wp-files/2015/02/9.jpg)

最中央的就是照片文件本身，它发散出来 Text、Date、Location、Image 四个节点，我们获取的地址信息就是在这个 Location 里，而我们之所以能够直接在自带的地图软件里显示这个地址是因为 Location 后面有 Maps link。

所以当你不知道你对一个动作的结果能做什么处理的时候，可以考虑先用 View Content Graph 看看。

小结
--

这篇的主题是探讨仅用 Workflow 在 iOS 设备上能干什么，所以用的全部是 Workflow 自身的动作和 iOS 内置的软件。关于 URL Schemes 还有如何利用网页服务跟 API 来制作更「神奇」的 Workflow 的办法会在以后的教程中写到。

复习
--

看完本文你应该懂得的关于 Workflow 比较重要的用法有：

- Filter
- Split Text
- Repeat
- Get Variable
- 在 Text 里将变量和字符结合
- Combine Text
- View Content Graph

---

### Workflow 系列文章

Measure

Measure

|  |
| --- |
| Workflow 教程（四）：如何使用 Workflow 中关于文章的那些动作 Source URL:<https://sspai.com/post/31662> |

Workflow 教程（四）：如何使用 Workflow 中关于文章的那些动作
=======================================

2015 年 10 月 28 日

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/7E5D4988-DAD8-44E0-9DD8-300C654C3BAB.png)

编注：此为 [Workflow](https://sspai.com/post/tag/workflow) 系列教程补全计划，本文首发于 [越狱指南](http://jbguide.me/2015/03/03/how-to-use-the-new-articles-actions-in-workflow/)。

---

用新动作在 Safari 里做文摘
-----------------

每天你都会在电子设备上阅读很多东西，保留其中你认为有价值的部分的一个办法是摘抄。而如果你要把摘抄的内容统一起来放在一起，你就要考虑它的整洁度，也就是格式。

在电子设备上，最简单的让摘抄内容的格式统一起来的办法应该是用 Markdown：

文章名称:

> 引用文本

日期

这样出来的结果就会是：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/3F443445-7F14-4D31-94C4-DEEC9A66D1CE.jpg)

有出处，点出处可以看到原文。引用文本有层级显示。最后还有摘抄的日期。

但是，在 Workflow 出现之前，这个过程是很繁琐的：你需要获取文章的名称、链接，还要复制好喜欢的内容，最后还要加上日期。但因为你每一次只能从网页粘贴到 Evernote 一项内容，所以你要来回选中复制再粘贴，还要考虑格式（字体字号）问题，实在太痛苦。

Workflow 1.1.1 版中添加了一套关于网页文章的动作 ——Articles，让这整个步骤变得极其容易。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/B52E7C5C-2EE0-4C9C-9CA7-22CBF14BA7E6.jpg)

仅能在 Safari 中做摘抄的办法
------------------

用 Articles 的功能做摘抄虽然简单，但是它的能力范围有限。它只能作用在 Safari 的网页里，对稍后读软件（ Pocket / Instapaper）和 RSS 软件都不起作用。

### 动作目的

对每个动作，你都要首先想清楚，你想做什么。想得越具体，你的目标就越明确，就越容易成功。

在这个动作里，我们首先要用 Workflow Type [1](https://sspai.com/post/31662#fn1) 去获取文章。然后我们要获得 4 个变量 [2](https://sspai.com/post/31662#fn2)：文章的标题、链接，你想摘抄的文本，还有日期。

最后我们要把它们以下面的 Markdown 的格式放到一个 Text 文本框里：

文章名称:

> 引用文本

日期

然后我们要把 Markdown 的内容转化为 HTML，最后把转化好的内容发送到 Evernote。

接下来一步一步来做。

### 用 Workflow 获取文章

首先要把这个 Workflow 的类型设置为 Action Extension，并且仅接受 Articles 这个类型的内容：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/9AA2B038-09BD-4A8C-A3C4-23BE01B2BAFB.jpg)

### 获取文章的名称、链接及引用文本

Workflow 1.1.1 版中添加了 Get Details of Articles 这个动作。对这一个动作重复利用，就能够获取我们想获得的标题、链接跟引用文本。

但首先，我们要把获取了的 Article 先设为一个变量：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/3B8AAEEE-7FBE-4D99-9AF2-B292F0893BCA.jpg)

原因是由于，我们总共需要三个变量（标题、链接跟引用文本）每次我们只能向这个 Article 获取一个内容，所以我们需要用到 Article 这个变量三次。

第一次，设完变量后可以直接从变量获取元素，所以我们可以直接从 Article 获得 Title（标题），并设为变量：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/314762C5-6868-441E-B3F0-91F6E39C247A.jpg)

第二次，获得 URL（链接），并设为变量：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A65728B3-C80A-4D96-8E7D-248286B178C4.jpg)

获取引用文本：

Workflow 目前似乎还不支持直接从 Safari 获取选中文本，所以在这里需要绕一下，利用剪切板曲线救国。

具体做法是，在运行摘抄这个 Workflow 之前，先把你想要摘录的文字首先复制了。由于在 Text 文本框里，我们使用 Clipboard 这个常量，所以 Workflow 回把复制的内容自动填入正确的位置。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/72E265DB-2516-4FEA-9D54-E29C3DBE709C.png)

以上，我们就获得了我们摘抄所需要的一切元素。下面我们要获得日期。

### 获得日期

获得日期在 Workflow 里是一套动作，首先要获得日期，其次要决定这日期显示格式。

获取日期的动作是 Date，我们要在这个动作里选择 Current Date。然后在下面我们要接上 Format Date，来设定日期显示的格式。因为是摘抄，所以也没必要特别精确，所以我用的是不显示时间，日期用的是最短的格式：年-月-日。

最后，将其设为变量。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/CF87CF95-4477-48B6-BC7D-BA6735DC98F4.jpg)

### 把变量填入文本框

获得了我们需要的四个变量，下一步就是按照 Markdown 格式把它们放到文本框中：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/72E265DB-2516-4FEA-9D54-E29C3DBE709C.png)

### 把 Markdown 转化为 HTML，并发送到 Evernote

把 Markdown 转化为 HTML 是 Workflow 第一版就有的动作，叫做 Make Rich Text from Markdown。

在它的下面，我们接上 Append to Evernote[3](https://sspai.com/post/31662#fn3)，在笔记本中填入摘抄用的笔记本（我的是「Excerpt」）。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/90773042-CC71-4E46-96E5-07F47D3DDEE3.png)

这样整个动作就结束了。要注意先把想要摘录的文本复制好，然后再运行该 Workflow。

[下载该 Workflow](https://workflow.is/workflows/ed52c9885bce43299c35415050579af1)

### 不足之处

这个动作很容易，但是它作用范围只有 Safari 和一些可以在本 App 中以网页形式打开网址并运行 Share Sheet 的 App。后者其实并不多，因为大多数软件打开网址都不是也网页的形式，而是包括在了自己的软件内。像 RSS 阅读器、稍后读这些软件统统不能用这个办法。

当然神通广大的 Workflow 不会就此举白旗，但是方法会变得复杂很多，我们在以后的教程会说明这种方法。下面我们来看另外几个新动作的应用。

用新动作筛选某网站的文章后一并发送到稍后读
---------------------

这个动作因为 Workflow 本身的一个缺陷在当前版本使用并不理想，后文会详述原因。

一般来说，我们对信息来源有一种信赖感。而且针对同一个专题的内容，同一个信息来源获取的消息更为联贯，逻辑承接更容易。但是，同一个信息来源有时候未必只会对你感兴趣的那一个点发布内容，比如我在指南并不是只写 Workflow 教程的，但是有些人可能因为他不越狱，所以对我写的插件方面的内容并不感冒，只想看关于 Workflow 的这些教程。如果你是这样，这次 Workflow 更新的关于 Articles 的动作对你来说就有用了。

它可以让你把某个信息源的关于某个专题的文章先筛选出来，然后一气儿全部发送到稍后读服务，然后你可以慢慢地看。

### 用 RSS 链接获取某网站的文章归档

Get Items from RSS Feed 是 Workflow 早就有的功能，用来获得具体 Blog 的博文归档。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/92D91C49-AD5E-4AF0-91E1-B8EDC0B9BE0D.jpg)

我们在 URL 里填上博客的订阅链接，然后在下一行选择获取的文章数。

### 筛选文章

Filter 是[上一篇教程](https://sspai.com/30903)详细介绍过的内容，这里不再赘述，只用具体例子来说明如何筛选文章：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/38D7BE0F-8996-4124-90C7-772D5AF7C55B.jpg)

上一步我们已经从越狱指南的 RSS 链接里获取了 10 篇最近的文章，现在通过筛选，我们要得到这 10 篇文章名称里包含「Workflow」的文章。然后按发布日期，从早到晚来排序。

### 全部发送到 Pocket

获取了符合标准的文章们，我们接下来要做的就是把它们一并发到稍后读。

处理一个列表中每一项内容的方法是使用 Repeat with Each 这个动作，这个动作我也已经在《[Workflow 教程：Workflow 本身能做什么？](https://sspai.com/30903)》里详解过了，这里也只说例子：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A2376732-8BAA-4DA5-868B-624063E99451.jpg)

如图，只要在产生列表的下一步放上 Repeat with Each，Workflow 就知道下面是处理列表中的每一项内容，我们把 Add to Pocket 放到 Repeat with Each 里，Workflow 就明白这是要它把列表中每篇文章都发到 Pocket。

[下载该 Workflow](https://workflow.is/workflows/24668776f2f647bb99724e78c9dc2c41)

### 不足之处

Workflow 1.1.1 版更新出的这些 Articles 功能都足够好用，但是从 1.0 就有的 Get Items from RSS Feed 这个功能却一直有个毛病 —— 它只能获取 10 项内容，你不管设定多少项，它只获取 10 项。所以这也成了这部分讲的整个 Workflow 的短板，比如说指南现在的文章，按时间来排序，最新的两篇是 Workflow，接下来的就是只接到第 14 和第 15 篇了。所以用本文的方法，只能获取前两篇。

---

### Workflow 系列文章

Measure

Measure

|  |
| --- |
| Workflow 教程（五）：如何利用 Workflow 与网页互动 Source URL:<https://sspai.com/post/31832> |

Workflow 教程（五）：如何利用 Workflow 与网页互动
==================================

2015 年 11 月 11 日

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/7E5D4988-DAD8-44E0-9DD8-300C654C3BAB.png)

编注：此为 [Workflow](https://sspai.com/post/tag/workflow) 系列教程补全计划，本文首发于 [越狱指南](http://jbguide.me/2015/03/03/how-to-use-the-new-articles-actions-in-workflow/)。

---

在效率软件中使用 URL 的好处
----------------

任何可以搜索的网页服务都遵循着各自 URL 的格式，比如在谷歌和百度搜索「少数派」，它们的 URL 将分别是：

这两个 URL 里，少数派是我们原本输入到搜索框里的东西，而其它的部分则是该网站搜索服务的 URL 格式。不信你可以把 http://www.baidu.com/s?wd= 粘贴到你的地址栏，然后在等号后面输入你想搜索的东西试试看。

只要我们了解了一个网页的 URL 的格式，就可以在 [Alfred](https://sspai.com/post/tag/Alfred)、[LaunchBar](https://sspai.com/post/tag/LaunchBar)、[Launch Center Pro](https://sspai.com/tag/Launch%20Center%20Pro)、[Drafts](https://sspai.com/post/tag/Drafts) 以及 [Workflow](https://sspai.com/tag/workflow/) 这样的效率软件中，把 URL 中固有的部分先设定好，在搜索的时候只需要输入想搜索的内容就可以了。

比如我想在 iPad 上知道一个 App 发布以来的价格变化，我只要运用 [Appshopper](https://sspai.com/post/tag/Appshopper) 的 URL 格式，在 LCP 中设定好一个动作，在搜索时只搜索 App 名即可：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/F8B5E3E5-8732-4CA9-B6C1-0036821A73E6.gif)

当你运用多个不同网页的搜索服务，比如说「谷歌」、「淘宝」、「优酷」的时候，这种搜索的精准和效率就可以更好地体现出来。

在 Workflow 中使用 URL
------------------

Workflow 当然是支持这个功能的，而且由于它独特的运行方式，URL 既可以是一个完整的动作，也可以是一个动作的一环。

我不建议在 Workflow 里把 URL 方面的使用当作一个完整的动作，这属于工具误用。比如有人在 Workflow 里单独将百度搜索作为一个动作，功能就是输入关键词，让百度来搜索。这让我非常不解：其一，你完全可以把 Spotlight 的搜索引擎设为百度，这样最效率；其二，退一步，即便你希望用效率软件做这样的事（虽然这么做已无效率可言了），你也完全可以用 Launch Center Pro，因为 Workflow 中如果对中文不进行 encode 是没办法直接用的。

所以，在 Workflow 中使用 URL，最好的办法是将其作为整个动作的一环。发挥 Workflow 的价值，不要用 Workflow 做那些其它 App 也可以做，甚至其它方法更省事的事情。

### 用 Workflow 获取需求的信息，自动填入 URL

在这里直接用 Save App Icon[1](http://jbguide.me/2015/05/02/how-to-use-url-in-workflow/#fn:1) 这个 Workflow 来详述整个过程。

有能力的可以直接[下载 Workflow](http://cl.ly/aqb2) 来看是怎么回事。

Save App Icon 这个 Workflow 的作用是直接在 App Store 里保存软件的 icon，便于以后任何形式的分享。而且并不只是保存到相机胶卷，这个 Workflow 经过简单的修改，就可以把 Icon 直接在动作中分享到你需要分享的对方。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/7433C708-4C2D-442C-A775-626995902BE3.jpg)

#### 第一步：获取 App 的链接

我强烈建议新手边操作边理解，文章里提到的整个方法绝对不难，但是如果没有基础，只看文章的话很快就头蒙了。

在这里 Workflow 里，我们主要使用的是一个叫做 [icoicon](http://submit.icoicon.com/) 的服务。它的 URL 是：

http://submit.icoicon.com

而要想从这个网站获取某个 App 的图标，必须给 icoicon 提供这个 App 的链接，只有当它的 URL 满足下面这个状态：

http://submit.icoicon.com/?itunesurl=App链接

它才能够从中读取这个 App 的 Icon 并显示出来。

所以第一步，我们要获取 App 的链接，而这很简单，只要设定此 Workflow 只接受 URLs 类型的数据就行了。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/E71E078C-C4A8-4D3E-89FE-34F6A20FAB4F.jpg)

#### 第二步：将 App 的短链接拓展为原始链接

在 iOS 设备上的 App Store 里，我们获取的链接都不是一个正常的原始的链接，而是被缩短过的 App Store 专用链接。缩短了的链接将数据使用一个简单的代号表示，比如说，Tweetbot 的原始链接是：

https://itunes.apple.com/cn/app/tweetbot-4-for-twitter/id1018355599?mt=8

但通过 iOS 上的 App Store 获取的链接是缩短了的：

https://appsto.re/us/TEvdR.i

很多服务不能识别出这些链接的完整内容，所以会判断链接错误。在使用这种服务的时候，我们需要把短链接拓展为原始链接。

Workflow 提供了 Expand URL 这一超级实用的功能，在 Workflow 内部直接解决了这个问题。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/FB4A6FCB-1464-4C00-B79F-220AEBEA5043.jpg)

#### 第三步：将原始链接填入 URL

第一步里，说到了我们需要用到 icoicon 的 URL 格式：

http://submit.icoicon.com/?itunesurl=App链接

我们在第二步已经获得了需要的 App链接，下一步就是把它填进这个 URL。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/D0BE9E6F-A5C6-4227-901B-988F94BDE82B.jpg)

由于 http://submit.icoicon.com/?itunesurl= 是固定的，所以我们直接在 URL 这个框里填上固定的这部分。然后我们使用 input 把上一步面获得的原始链接承接过来：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/23BD85F2-01F6-4D77-8ED5-1C6885883A62.jpg)

当你想使用 input 把上一步得到的结果填入到下一步中，如果这个关系成立，就能在两步中间看到一条「线」，表示这两步的承接关系已经确立。

注意，URL 这一栏的内容并不完整，你需要先将 http://submit.icoicon.com/?itunesurl= 复制到 URL 中，然后在变量中找到 Input，把它放到等号后面。

#### 第四步：下载网页内容

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/0FCA2C4D-E44F-451B-B691-2DCD1D217424.jpg)

Get Content of URLs 是 Workflow 这个 App 能够牛逼的重要原因之一，用它可以在不打开网页的情况下获取网页的内容，如果网址是可下载格式的文件还可以直接下载到手机并通过 Workflow 的其它动作将其分析出来或者播放。

当我们把一个 App 的链接，比如说 Tweetbot 的填入到 icoicon 的 URL 中，在 Safari 里我们将看到的是这样一个网页：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/3B4448CF-FD25-4AB8-8379-81BE0F1B6F5C.jpg)

我们可以在这个页面直接长按图片来保存。

但是在这一步，我们是要用 Get Content of URLs 来获取 icoicon 这个页面里的图标，我们不用打开浏览器，直接让 Workflow 帮我们拿我们需要的东西。

#### 第五步：从获取的结果里筛选出图标

利用 Get Content of URLs 我们会从链接中下载一切可以下载的内容，我们要从中提取出我们需要的部分，就需要使用 Workflow 的其它操作（想看 Get Content of URLs 都下载了什么东西？回忆一下 [Content Graph](http://jbguide.me/2015/02/19/what-can-workflow-do/) 的用法）。在这里，我们要的是图片，所以我们要使用 Get Images from Input 来从下载了的内容里获得图片。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/DB9E06FA-8915-4BA3-879D-4943C917668E.jpg)

#### 第六步：处理获取了的 Icon

经过第五步，我们就获取到了想要获取的软件的 Icon。所以第六部其实是一个开放的选择，比如，你可以像我这样使用 Save to Photos 这个动作把它保存到相机胶卷：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/4B43A169-48AD-443D-A1BB-8BF3C3D82737.jpg)

你也可以在下面直接用 Share 把这张图标发送到其它位置或者社交网站。

### 小结

我在这篇文章里用 Save App Icon[1](http://jbguide.me/2015/05/02/how-to-use-url-in-workflow/#fn:1) 这个动作说明了 Workflow 在网页 URL 上应用的一些基本用法。读完这篇文章你应该掌握的用法有：

* 能够注意到、识别出并利用网页的 URL 格式。
* 用 Workflow 将短链接拓展为原始链接。
* 在 Workflow 中把具体内容填写到 URL 的特定部分。
* Get Content of URLs 的用法。

而且记住，不要单独地把 URL 相关的动作仅作为一个动作在 Workflow 里使用，要把它融入到一整个更大的、更适合 Workflow 这款软件的动作里。

---

### Workflow 系列教程

Measure

Measure

|  |
| --- |
| Workflow 教程（六）：如何备份恢复你的 Workflow 动作 Source URL:<https://sspai.com/post/30591> |

Workflow 教程（六）：如何备份恢复你的 Workflow 动作
===================================

2015 年 08 月 11 日

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/7E5D4988-DAD8-44E0-9DD8-300C654C3BAB.png)

Workflow 用了一段时间以后会积攒一些自己常用的动作，这些动作用顺手了就会想在不同的设备上做到。虽然很难想象，但 [Workflow](https://workflow.is/) 至今也没有推出一个备份 / 恢复 / 同步动作的方案，不过以这个应用的能力，做到这点也并非难事。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/B2FBABEB-CADD-48DE-9F14-EFA8397BA950.gif)

如果对 Workflow 比较熟悉，可以直接看「步骤说明」，如果想了解整个制作的思路可以看「思路说明」。

步骤说明
----

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/0448B799-7BDA-4917-A20F-4F7A53365C87.jpg)

思路说明
----

### 第一步：找到动作的下载链接

在将 Workflow 分享到他人和其它设备的方法里，我最常用的是通过链接下载这种老式的方法，在下载的时候我发现，其实 Workflow 的下载页面里的那个 GET WOKRFLOW 的按钮是另一个链接，这个链接才是存放你要下载的动作的地方，我叫它下载链接，而通过 Workflow 的设置分享出来的，我叫它网页链接。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/255FD188-43C5-44F8-A96E-E616653B0E48.jpg)

通过下载链接，你就不需要每次都打开一个网页才能下载相应的动作，你可以在 Workflow 里试试：新建一个动作，在 Text 栏里填上下载链接，再在下面放上 Open URLs 这个动作，然后运行这个动作，就能在不打开 Safari 的情况下直接将一个动作下载到你的设备上。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/33162893-6575-4928-A861-28120E4B5D0C.jpg)

但是 Workflow 导入动作有个默认设定，就是导入后会自动打开（但不运行）这个动作。如果这个默认设定不改变，就没办法保持同一个 Workflow 的运行，也就是说每次只能导入一个动作，导入一个动作后就被迫中断原本正在运行的导入动作，打开新的动作。这样那样也不能提高多少效率。

解决这个办法异常地容易，只要在导入的 URL 后面加上一句： &silent=true 就可以做到导入动作以后不打开。

经过以上步骤，我们已经可以做到直接导入一个动作而不打开它了，下一步我们只要能重复这个步骤，即导入多个动作而不打开它们，就成功了。

### 第二步：认识下载链接的格式

我们在上面图片中看到的直接下载动作的链接，是这样的：

workflow://import-workflow/?url=https://workflow-gallery.s3.amazonaws.com/workflow/6894c6e8fa164088b4ecf6c5f027efc2.wflow&name=Example

在这一长串链接里，只需要注意最后一个 / 后面的部分：

* 在 .wflow&name 之前，是每个 Workflow 动作的链接的路径的最后一部分，这一串字符是独一无二的，每个 Workflow 都不同。
* 在 .wflow&name 之后，是每个 Workflow 动作的名称。

所以我们现在要做的事情是两件：

1. 获取 Workflow 动作的链接的最后一部分字符。
2. 获取这个动作的名称。

而这两件事对于 Workflow 来说都很容易。

### 第三步：获取动作名称

通过 Workflow 动作的链接打开的网页的名称，就是那个 Workflow 的名称，所以只要获取网页名称即可。

获取网页名称的办法很简单：先下载网页内容，然后获取其名称。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/9A038AB6-AB1D-4586-9826-9D0870A877A0.jpg)

这些名称有的含有空格等字符，需要编码，否则不能作为链接的一部分，所以要在后面加上 URL Encode 这一步对名称进行编码。

### 第四步：获取动作链接的关键部分

网址的不同位置都是用 / 来分割的，我在[《Workflow 本身能做什么？》](http://jbguide.me/2015/02/19/what-can-workflow-do/)这篇文章里写过 Split Text 的用法，这里正好可以用到。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/FABBBF2C-DC7F-4FC6-93E0-AA75FADC787F.jpg)

通过 Split Text 可以把一个 Workflow 的网址分为几段，比如一个 Workflow 的网址是：

https://workflow.is/workflows/6894c6e8fa164088b4ecf6c5f027efc2

那么可以将其分割成：

* https:
* 空白
* workflow.is
* workflows
* 6894c6e8fa164088b4ecf6c5f027efc2

而我们要的是最后一部分，所以可以直接用 Get Item from List 这个功能，获取最后一项也就是 Last Item。

### 第五步：获取网页链接

我们现在可以从 Workflow 动作的网页链接里获取每个动作的名称和关键字符来组成下载链接了。那么问题是，网页链接怎么获取？

在这里还是没什么聪明办法，每个动作的网页链接还是要大家手动获取，但是获取以后可以存放到一些可以在各个设备上同步的应用里，可以一劳永逸。

我的做法是存放到 Drafts 里，因为 Workflow 可以通过 Drafts 里笔记的 UUID[1](https://sspai.com/post/30591#fn1) 获取笔记内容，不需要通过网络。

获取 Drafts 任一笔记的 UUID 可以用[这个 Drafts 的动作](http://drafts4-actions.agiletortoise.com/a/1Pk)。

然后在笔记中，你可以按照

> 动作名称：动作网页链接

这样的格式在 Drafts 里规矩地排放好每一个动作，同时，你也可以把你的动作分组放到不同的笔记里。比如常用的和测试用的，iPad 用的和 iPhone 用的等。设备的使用情境不同，Workflow 的使用应该也是不一样的。

然后在 Get Contents of Draft 这一步的下面，接上 Get URLs from Input 就能直接获取所有的链接而不获取名称了。

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/FD57185E-9EFA-4175-BEFC-98D7A183C0D1.jpg)

### 第六步：循环下载动作

目前为止，我们知道了：

1. 无需打开网页就能在 Workflow 里下载单个动作的链接。
2. 我们可以获得下载链接所需要的关键字符和名称。
3. 我们可以获得网页链接从而得到下载链接。

最后一步要做的是重复这些步骤，下载所有备份的 Workflow。在 Workflow 里，通过 Repeat 就能做到这一点。

因为我们要重复的是从获取动作链接到打开下载链接的这部分，所以从 Drafts 获取网页链接的部分以外全部需要框在 Repeat 跟 End Repeat 之间。

结语
--

Workflow 是肯定会加入备份 / 恢复 / 同步动作这些功能的，只是时间问题。但是不是说这些尝试就是鸡肋呢？这要看你对自己的要求。看你是愿意动动脑子完成一件目前你需要但是官方没有给出的功能呢，还是愿意听天由命求开发者看对方心情赏给你。

除此之外，通过对 Workflow 的探索是对各功能认识加深的过程，光指望下载别人做好的动作不会有太大长进。这也是我几乎不会在 Workflow 文章里直接分享下载链接的原因。

除了情怀，实用性上通过这种方法备份也是有好处的。这种方法可以把 Workflow 的动作分开保存，可以针对不同的设备和目的保存到不同的 Drafts 笔记中，恢复的时候可以有选择性地恢复。同时，这种方法经过简单修改，也可以做到直接从文章和网页中下载别人分享的 Workflow，具体怎么做还请你动脑想想。

---

1. UUID 是通用唯一识别码的英文 Universally Unique Identifier 的缩写，在这里你可以理解为，UUID 是每一条笔记的唯一标识。 [↩︎](https://sspai.com/post/30591#ffn1)

---

Measure

Measure

|  |
| --- |
| Workflow 教程（七）：征服 Workflow 中的最高峰 Source URL: <https://sspai.com/post/30870> |

Workflow 教程（七）：征服 Workflow 中的最高峰
================================

2015 年 08 月 25 日

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/7E5D4988-DAD8-44E0-9DD8-300C654C3BAB.png)

和 API 的结合是 [Workflow](https://sspai.com/post/tag/workflow) 最复杂的功能，大概也是 iOS 里的效率软件目前能够做到的最效率的事，掌握了如何在 Workflow 里使用 API 就可以说这个 App 已经被你征服了。

API 是 Application Programming Interface 的缩写，中文译为应用程序接口，术语解释到此结束，你对这单词有个感觉就行。

普通用户使用 API 的理由不外乎方便，很多时候我们对搜索结果的期待只是一些具体的内容或数值，比如汇率的数值、气温的度数等等，能够直接抓取这些内容对于开发者很重要，但对于我们普通用户来说，如果能够直接获取数值或字符，也省去了每次都打开以及加载网页的时间和流量。

这篇文章以以下三个例子带大家入门 API 以及如何在 Workflow 里使用 API（文章长，如果没耐性，可以只读第二个例子，因为它最详尽）：

* 在 iOS 上做到一键让 PC 上下载自己 iOS 设备的最新固件
* 在 iOS 上做到 Search Link
* 在 iOS 上做到批量保存 Google Image 第一个搜索结果

利用 Transloader 一键下载最新固件
-----------------------

这部分内容并没有在 Workflow 里调用 API，主要目的通过做个小玩意儿使你接触这个东西，知道它是什么，减低对它的恐惧。

作为一个 Jailbreaker，跟固件打交道是常有的事，尤其是当越狱突然放出的时候，我会马上更新到最新固件然后越狱。但是，固件发布当时我未必在家，加上固件都不小回家以后要下载很久。所以必须想个办法能够让我在手机上点一下，家里的电脑就会自动下载我的设备的最新版固件。

Workflow 结合 [ipsw.me](https://ipsw.me/) 的 API 再加上 [Transloader](https://itunes.apple.com/cn/app/transloader/id572280994?mt=8) 可以解决这个问题，只要我知道自己设备的型号，就能够通过 Transloader 在家里的 Mac 上下载最新版的固件，这样回到家以后，新鲜的固件就躺在那里等着我了。

想要用好 API，要养成翻开发者文档的习惯，你或许对「文档」这两个字的理解是枯燥乏味以及晦涩难懂。这是正常的，因为它们不是睡前读物，它们更多的是工具，要做到的是规范和高效，所以它们的用词才会机械，从而也便于搜索和定位。

ipsw.me 的 URL 格式在其 [官方文档](https://api.ipsw.me/docs/2.1/Firmware) 里有很明确的表述。

我们想要下载的是自己设备的最新固件，用到的 URL 就是：

http://api.ipsw.me/v2.1/设备的Identifier/latest/url

比如说我的 iPhone 6 Plus 的最新固件下载链接的 API 页面，就是：

http://api.ipsw.me/v2.1/iPhone7,1/latest/url

打开这个界面，你会看到一串网址：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/C101AD5F-A7DC-4873-B010-B31A4E83F57C.png)

相信你应该能看出来这串网址就是固件的下载链接。

你可能还不太明白为什么会是这样的结果，我们来看一个关于固件的稍复杂一点的 API 的页面，应该能让你理解地更轻松一些。

这个 [页面](http://api.ipsw.me/v2.1/firmwares.json) 列出了所有的固件信息，我们只取其中一个的一部分来看：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/A4871B13-644C-4C58-8160-7F5AE183A883.png)

这是该页面最顶部的一部分内容，它包含了 Apple TV 2G 这款设备的 7.1.2 版本固件的所有信息。

在图中，首先我们可以看到一个明显的层级关系，分别由不同的大括号所区分。最顶级的只有一个内容：devices。在下一层也就是第二层，我们看到了 Apple TV 2G 的 Identifier：AppleTV2,1，这一层下面有一些内容，最下面的是第三层：firmwares，里面包括了更多的信息。图片里截下来的部分只是 7.1.2 版固件的信息，再往下翻，还有同层级的其它版本固件的信息。

你可以注意到，在这个页面里，信息都是引号冒号引号的格式，冒号前的引号中是类别，冒号后的引号中是具体信息。我们通过 API 要做的，就是在知道左边的类别后获取右边的信息。

图片里我标记了三个箭头，分别在 name（名称）、version（版本）、url（链接） 之前，你可以通过这三项你比较熟悉的对象来增强理解。如果你也越狱，你应该还能看见 signed 这一项，这一项后面如果是 true，就说明可以恢复到这个版本。

想了解 API 的话你以后会经常看到这样的界面，但现在我们是想要下载自己设备的最新版本的固件，那么只需要知道自己设备的 Identifier 就足够了。查看设备 Identifier 首先得知道设备型号，设备型号就在设备的背面印着，看一眼就行了：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/C6C502B0-4DC2-4C47-A206-AB12E5F958E8.jpg)

图片来自 OSXDaily.com

搞清楚机型以后就可以在这个 [页面](https://www.theiphonewiki.com/wiki/Models) 对应查询到该设备的 Identifier。

下一步要做的是和 Transloader 这个应用的联动：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/2CE321C8-F57C-46AA-B988-2E365112E5F0.png)

整个动作很简单，首先做一个菜单，将自己的设备名和带有 Identifier 的 API 页面的 URL 关联起来，然后下一步是从 API 页面获取下载地址，并复制到剪切板。最后通过 Transloader 的 URL Schemes，可以直接跳转到 Transloader 并开始下载剪切板链接里的内容。

[Transloader](https://itunes.apple.com/cn/app/transloader/id572280994?mt=8) 的机制是，将下载链接保存到 iCloud，如果 Mac 同样运行着 Transloader 并链接到了网络上，就会直接获取链接开始下载。

Search Link
-----------

在 iOS 上也做到 Search Link 的效果，自定义的余地比较大。

[Brett Terpstra](http://brettterpstra.com/) 做过一个名叫 [Search Link](http://brettterpstra.com/projects/searchlink/) 的小工具，如果你下载了这个工具，当你选中一串字符 —— 比如 [@JailbreakHum](https://weibo.com/jailbreakhum)—— 再按下设定好的 Search Link 的快捷键，就能做到把 @JailbreakHum 外面套上中括号，并且在后面加上一个小括号，小括号内是 Google 搜索的第一个结果的链接 ——[@JailbreakHum](weibo.com/jailbreakhum)。这对用 Markdown 写作的人来说是个很方便的工具，而这个工具核心就是 Google Search 的 API。一旦知道了这个 API，那么在 iOS 就可以通过 Workflow 做到同样的事情。

[Google Web Search API 的官方文档](https://developers.google.com/web-search/docs/) 新手没有必要看，我们通过 Workflow 来使用 API，最关键的是找到我们需要的 JSON（新手不需要彻底知道是什么）页面，在 Search Link 这个动作中，我们需要的页面的 URL 是：

https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=JailbreakHum&rsz=1

这就是使用 Google 搜索 JailbreakHum 以后第一个搜索结果的 JSON 页面：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/71DEB577-D936-48C1-810D-9B9DC4CEFF56.png)

在这个 URL 里，要注意的只有最后那一小段（因为前面的是固定格式）：q= 后面的字符是你要搜索的关键字，而 &rsz=1 则是只获取（第）一个数据的意思，数字可以改，但我们只想获取第一个结果所以在这里要让它是 1。

在上面的图片里，也就是这个地址打开后的界面里，你会看到 unescapedUrl:

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/368DE18F-0288-4087-B775-BE73CCA622AB.png)

而在它后面的那个链接，就是在 Google 搜索 JailbreakHum 以后会出现的第一个结果的链接，也就是微博链接：

http://weibo.com/jailbreakhum

如果能够自动获取这个 URL，就能够获取在 Google 上搜索 JailbreakHum 的第一个结果的链接了，同理，你也可以获得你想搜索的任何关键词的第一个结果的链接，这就是 Search Link 的核心。而如果你想给关键字套上中括号，给链接套上小括号，这都是 Workflow 里的基础操作了。

下面我们具体来结合 Workflow 的动作流程看看如何实现这个功能：

### 第一步：获取 / 输入关键词，编码，填入 URL

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/937DA8BB-5F2A-4EF4-A21F-43F91D11AACA.jpg)

首先，因为 iOS 上目前还没办法直接在选中字符后打开 Sharesheet，所以我用的是通过获取剪切板内容来获取关键词，使用这种办法的好处是可以直接用 Launch Center Pro 或者 Launcher 这样的应用直接激活动作。另外你也可以在这里建一个菜单，设一个 Ask for Input 这样的动作，这样你可以临时输入关键词。

然后说解码，简单来说，URL 里只能填入最基本的字符，其它的都需要编码。要养成一个填入 URL 之前编码的好习惯。

把关键词填入 URL 就是那个 text 文本框做的事，也可以使用 URL 这个动作，但 URL 我一直都不喜欢用，因为不好修改里面的内容。

### 第二步：获取链接

这一步是 Workflow 跟 API 打交道的重要步骤：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/4A00F6ED-A011-4716-9C46-2DB73A37C1ED.jpg)

首先下载链接内容，也就是获取 JSON 页面。然后从页面中获取词典（不用纠结，只要知道有这一步即可）。

下一步开始一步一步获取 key：先是获取第一层的 key——responsedData 的内容，再获取第二层的 key——results 的内容，最后获取我们想要的 key——unescapedUrl 的内容，也就是 http://weibo.com/jailbreakhum。

每个 key 的引号后面的全部字符都是这个 key 的内容，所以必须一步步精确到我们要的那一层，计算机不会跳步，你直接要 unescapedUrl 它就不知道该怎么办了。

### 第三步：处理链接

获得链接以后，最后一步就是处理这个链接，这一步就简单了：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/9EA079EB-8B5D-4436-91C8-370A9CF1C61F.jpg)

你可以做个菜单，选择复制到剪切板或是跳转到你常用的文本编辑软件。相信对于读过我之前教程的人都不是难事。有能力的，甚至可以和 Editorial 里的动作进行搭配，在 Editorial 里完全做到 Search Link 也并非不可能。

批量保存 Google Images 的第一个搜索结果
---------------------------

同样使用 Google 的 API，但比 Search Link 简单些，可以作为练手。

批量保存图片的情况属于那种不常遇到，但如果遇到的话会很麻烦的事情。在 Google 一张一张地搜索再一张一张的打开原图保存，那酸爽…… 比如有时候软件测评媒体经常会做这样一种专题图，它要有许许多多的大牌应用图标作为背景，一张一张图搜了下载是个办法、直接从 ipa 文件里获取也是办法，但若论效率的话直接以 应用名icon 输入所有应用的名称然后从 Google Image 获取第一个下载结果应该是更好的办法 [1](https://sspai.com/post/30870#fn1)。而通过活用 Google Image Search 的 API，可以轻松的在 Workflow 做到这件事。

有了前面 Google Search 的例子，这里的描述会容易很多。首先，我们要找的是那个含有 JSON 页面的 URL：

https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=关键词&rsz=1

然后我们直接结合 Workflow 的动作流程来看看如何在 Search Link 的基础上稍作修改做到直接下载 Google Image 搜索结果的第一张：

### 第一步：输入关键词

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/38918700-D88B-4829-88D8-E250EA224E20.jpg)

在图中我们看到多了一步 Split Text，这是我们用过多次的将文本转换成列表的功能，使用它是为了在需要批量下载图片的时候方便一些。在 Split Text 里我们看到是用 Space 也就是空格来划开字符，那么当你需要下载多张图片的时候，只需要在不同的关键词之间输入空格即可。（不要忘记编码～）

### 第二步：填入 URL，获取图片

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/14EE4AC8-41B8-48E4-8112-003B9574CEE0.jpg)

首先用 Repeat 把动作框起来，这样的话单张多张图片搜索的时候都可以用。

下一步和 Search Link 一样，就是把关键词填入 URL，获取词典，再不断地获取 Key，直到获取了图片的网址。

下一步用下载网址的内容或从网址获取图片都可以，但最后不要忘记把它们存到相机胶卷。当然你也可以改存到其它位置，看个人需求。

小结及补充
-----

1. 用 JSON FORMATTER & VALIDATOR 将 JSON 页面变得整洁 [2](https://sspai.com/post/30870#fn2)。

本文涉及的 API 内容都是 JSON，一般 JSON 的代码看起来是一坨：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/029A987E-40DD-4765-8337-67C5ADA3BBB3.png)

想要把这一坨东西按照层级排列起来可以用 [JSON FORMATTER & VALIDATOR](https://jsonformatter.curiousconcept.com/) 这个服务，把代码粘贴进去，整洁的结果就出来了：

![](.evernote-content/804FFA51-FFE3-4D85-A350-57499410FD40/222826DF-A505-4828-8549-088BF9A63EF7.png)

2. 其它公共 API 获取的地方

API 分公共 API 和私有 API，公共的可以不用注册专门的账户直接用，私有的则不可以。而 Workflow 能用的也只是部分公共 API 能做到的事情，比较有名的公共 API 库有 [ProgrammableWeb](http://www.programmableweb.com/), [Mashape API](https://www.mashape.com/), 和 [Data.gov](http://www.data.gov/)[3](https://sspai.com/post/30870#fn3)。除此之外，你也可以使用 Apple 的 [iTunes Search API](https://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html#searchexamples) 跟 Yahoo 等公司的公共 API 来做有意思的事，比如 Search Link 有直接获取 App 的 iTunes 链接的功能，你可以参考上面的文章来挑战一下这个。另外 [@do-fine](http://weibo.com/dofine) 就给用 Yahoo Weather 的 API 做了个给女朋友发天气的 Workflow，虽然实用性好像不如 IFTTT，但也是很好的练手方法。

---

1. 在这里你当然也可以使用 Apple 的 API，我以 Google Image 为例是因为 Google Image 的整体实用范围更广，当然如果你的使用情境更侧重于 iOS 应用，那么可以参看 [Apple 的文档](https://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html#searchexamples)，相信你看了这篇文章应该也会使用 Workflow 结合 Apple 的 API 做一些事情了。 [↩︎](https://sspai.com/post/30870#ffn1)
2. 该网站由 [@geekdada](https://github.com/geekdada) 分享。[↩︎](https://sspai.com/post/30870#ffn2)
3. 来自 [Geekwithjuniors](http://www.geekswithjuniors.com/note/8-reasons-to-love-the-new-workflow-app-for-ios.html)。[↩︎](https://sspai.com/post/30870#ffn3)

---

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/27733)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a4d940e5-78de-40a5-abe9-6a3cab436d00/a4d940e5-78de-40a5-abe9-6a3cab436d00/)