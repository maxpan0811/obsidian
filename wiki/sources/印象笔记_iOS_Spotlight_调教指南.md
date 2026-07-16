---
title: "iOS Spotlight 调教指南"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/iOS Spotlight 调教指南.md
tags: [印象笔记]
---

# iOS Spotlight 调教指南

# iOS Spotlight 调教指南 --- ![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/72A45461-C3C9-4F

---

# iOS Spotlight 调教指南

---

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/72A45461-C3C9-4FC4-BC0B-20F92802D51D.jpg)

[![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/3EE32BD4-A330-4FD4-8805-669F8D58FE2C.png)](http://matrix.sspai.com/user/681230/posts)

Spotlight 在 iOS 上有很长的历史，但是一直因为其位置的不适、功能的限制和卡顿等原因让它一直没有发挥出应有的作用。经由 iOS 7、8、9，苹果可以说对 Spotlight 已经度过了摸索阶段。现在的 Spotlight 在任何情况下都可以无障碍地从屏幕顶部拉出，在主屏幕时更可以通过下拉手势直接召唤。功能上，从最初的搜索应用以及邮箱、信息等原生应用中的内容，到 iOS 8 加上的搜索推荐，再到 iOS 9 之后加入的第三方应用内搜索，让 Spotlight 已经不仅是可用，还成为了很多功能的**最快入口**。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/B9842812-ECB0-4538-83C4-17ED3A7A7518.jpg)

*你甚至可以在 Spotlight 中直接使用 3D Touch！*

虽然 iOS 10 在 Spotlight 方面没有什么大动作，但对于中文使用者来说，修复了一个让我们刺挠已久的小问题——中英文应用名输入与识别的问题：在 iOS 9 Spotlight 只能根据系统语言识别应用，比如你是中文系统，你在 Spotlight 找音乐这个应用的话搜 *"Music"* 是找不到的，这是不是很蠢。在 iOS 10，Spotlight 对语言的要求放宽，在中文系统下同样可以使用应用的英文名称来在 Spotlight，也就是说在中文系统下搜 *"se"* 同样能得到设置这个应用。

这还没有算上键盘。在使用了外接键盘的 iOS 设备上，已经可以做到「完全不触摸屏幕」地使用 Spotlight。首先用 `⌘Command` + `空格` 呼出 Spotlight，Spotlight 就会自动进入输入模式，你可以直接通过键盘输入关键字，并通过回车直接打开第一个结果。第一个结果不理想也没关系，可以通过上下方向键来选择其它结果，手依然不用离开键盘。

在 iOS 继续保持它目前这个沙盒机制的情况下，Spotlight 作为启动器和入口的优势毫无疑问会继续扩大。

**所以，是时候认真对待它了。**

在此前尝试过 Spotlight 的人大概都知道，除了应用以外，大多数我们搜索的东西都不会给我们返回理想的结果。所以这里我所谓的「认真对待」，就是指充分利用它作为入口的便捷性的同时减少它提供的无用信息或干扰信息。兼顾这两点并不难，我们只要观察明白 Spotlight 提供的搜索结果，再对其进行针对性地设置。

首先，请打开：**设置 - 通用 - Spotlight 搜索**

**我们接下来的所有操作都只是打开或关闭里面的开关而已。**

Siri 建议
-------

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/1AB3A99A-5E95-4A6B-94F3-8246B07A477F.jpg)

Siri 建议有两个功能：

**功能一：显示最近使用过的或使用频率高的应用**

最近使用过的或使用频率高的应用很容易理解，比如说大多数人这里肯定都堵着一个微信。不过这里还有一个容易被忽视的功能：当你新下载一个应用，它会出现在 Siri 建议中。这能够帮桌面乱铺的人快速找到刚下载的应用。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/55300F25-BF05-47F4-8237-9DF91BCFA637.jpg)

**功能二：搜索历史**

Siri 建议会根据关键词的搜索频率和最近搜索（应该主要是根据最近搜索），保留一些搜索结果。

我建议开启 Siri 建议。因为很多人安排主屏的时候有一种一厢情愿，譬如把任务管理软件放入 Dock，可实际上我们真的不会那么频繁地打开任务管理软件。Siri 建议是对你使用习惯的真实反应，是根据你使用频率形成的「Dock」。很多时候，你拉出 Spotlight，想搜一个应用时，发现它就在 Siri 建议里，会方便不少。

Spotlight 建议
------------

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/231CC740-2C13-41E3-8E9F-DAFCDC988C71.jpg)

Spotlight 分为搜索建议和查询建议两部分。前者是在 Spotlight 中搜索的内容，后者是选中文字在弹出菜单选择「查询（Look Up）」后出现的查询建议。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/1A0ADE81-1CB4-429C-911F-5D18D144D433.jpg)

**搜索建议是干扰搜索结果的最大因素**，所以我强烈建议把它关掉。首先，在我的使用情境下，即使我把系统语言调为英文，App Store 账户换到美区，搜索建议出现的没用的结果要远多于我想要的。毕竟，通过一个关键词而知道你想要的东西还是太难了。其次还有它太占地儿，从上图就能看出，一个关键词，推荐网页要占 3 个格子，Bing 搜索要占 3 个格子，Youtube、Twitter、iTunes Store 等等服务里有相关内容了都要占格……这种撒网式的做法说明，它不知道我真的想要什么，以至于给了我太多我不想要的。

而**查询建议**是可以开启的。当你选中一个词，查询建议可能是在 iOS 设备上搜索这个词的最快方式。除此之外，因为这个词一般是从文章中的句子里选中的，不像我们想出来的关键词那么模糊，精准性也会强一些；最后也是最主要的，查询建议的项目不占地方。**查询**这个动作我们最多用的肯定是查单词，而查询建议的项目都在字典项目的下面，所以建议的结果理想了当然是最好，不理想也不会像搜索建议里的条目一样占用大量关键位置，我们还是可以最快地使用本来习惯的字典功能。

搜索结果
----

搜索结果里就是我们系统中的应用列表，这个列表按照「中文」→「数字」→「A-Z」的顺序排列所有应用。其中大多数应用没有真正支持 Spotlight 搜索，而支持的也有可能有功能重合的部分。我在下文会介绍我关闭 Spotlight 开关的标准，和一定会打开 Spotlight 开关的一批应用及原因，以供参考。

### 关闭没有支持 Spotlight 的应用的开关

大整理之前，我们肯定是先把不能用的碍眼的东西扔掉，再从作用相似的东西里选择最优秀的和最无可替代的。同理，在调整设置之前，我会首先将那些没有支持 Spotlight 的应用的开关全部关闭。虽然开不开它们实际上对搜索结果没有影响，但是如果不关，会影响我们以后进一步的筛查。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/BC83E216-E7A4-4F78-860F-F3196DF3F1A5.jpg)

*在哪个图里找到 Dropbox 更容易？*

因为我们每个人的应用都不同，我也无法给出一个「没有支持 Spotlight 的应用列表」，所以最开始你不妨先直觉性地过一遍，你觉得一个应用不可能支持 Spotlight 搜索，或从来没有印象，也不指望它在 Spotlight 里给你提供什么便捷服务的，你都可以关掉。如果你害怕其中某些应用日后会添加 Spotlight 搜索，也可以把它们留下来。

**附：不支持 Spotlight 的苹果自家应用：**

*查找 iPhone、地图、电话、家庭、健身记录、相机、音乐备忘录、照片、App Store、Apple Store、Facetime、iBooks、iTunes Store、Safari、Wallet、Watch、GarageBand。*[1](http://sspai.com/35818#fn1)

### 关闭社交应用的开关

社交类软件包括微信这样的也包括微博这样的。当然了，近年每每被钦点的微信并没有支持 Spotlight，从未被钦点的 Slack、Telegram 和 Whatsapp 却早已支持。这三个应用在 Spotlight 里表现的还挺好，只是提供联系人搜索，不会搜索聊天内容。怕就怕 IM 应用学苹果自带的**信息**这种搜聊天记录的模式。聊天记录涵盖的信息太宽泛了，误触率高，真想搜某段对话最好到信息里面去搜。不过微信深谙我国家庭伦理，想必日后支持了 Spotlight 也不会走搜聊天记录的路子。

微博、Twitter 这样的社交软件跟**信息**一样，Spotlight 搜索的开关都要关掉。IM 应用搜出来的至少还是你收发的消息，微博和 Twitter 会搜出什么你想都想不到，这样的方式能搜出有效信息要靠奇迹。如果真的需要搜 Twitter 的话，可以用 [Ai Search](http://sspai.com/tag/Ai%20Search) 或者我做的 [Twitter Advanced Search 的 Workflow](https://workflow.is/workflows/daac2610aa484cdd93566c33428cd209)。

### 同类功能应用的开关只开其中最合适的一个

iOS 的原生日历和 [Timepage](http://sspai.com/tag/Timepage) 都支持 Spotlight 搜索，搜一个事儿会出来两个一样结果。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/04CF8DCC-C720-44DE-9B41-582749A54732.jpg)

这样的情况恐怕还不少，很多对 iOS 了解和熟悉的人或许设备上都会有很多同类应用，当这些同类应用都支持 Spotlight 的时候，你要有选择性的去开启开关。有一些应用虽然一样但可能对 Spotlight 支持的方式不同，比如有的文本编辑类软件支持全文搜索有的只支持标题搜索，你可以根据它们不同的特性选择留下谁或者都留下。

### 关闭你已经养成习惯在应用内搜索信息的应用的开关

这类应用包括邮件、播客等等。

首先这类应用和社交软件一样，涵盖了太多信息，几乎搜什么都有它。而且，这类有明显搜索需求的应用，我们早就养成了在应用内部进行搜索的习惯，在通过 Spotlight 搜索此类应用出现明显的长处之前，维持曾经的搜索习惯就好。

另一个典型是 [Pocket](http://sspai.com/tag/Pocket)，它竟然可以在 Spotlight 里全文搜索未被 Archive 的文章。但是首先我估计我们都不会这么打开 Pocket，其次要真找文章也是找 Archive 里读过的，反而不会找没读的，没读的谁记得住……

### 关闭那些使用通知中心部件更合适的应用的开关

典型是 [Launcher](http://sspai.com/tag/Launcher)，如果你的搜索关键字是包含在 Launcher 的 URL 库里的应用的话，它会在 Spotlight 问你是不是要添加那个应用的快速启动器。Spotlight 本来就可以直接打开应用，我为什么还要在搜索结果里添加一个 Launcher 的启动器。

另外，虽然 Launcher 的其它动作也是可以用 Spotlight 搜索的。但是它本身就是个通知中心部件（Today Widget），我们要用哪个动作直接在通知中心打开就好，没有搜索的必要。

另一个类似的是 [TeeVee](http://sspai.com/tag/TeeVee)，一款用于追美剧的应用。它在 Spotlight 里可以搜索你存在里面的电视剧和电影，但很明显我们设备里有这样的软件是为了看追的剧还剩多久，而完成这个功能用通知中心部件更加合适。

值得打开 Spotlight 开关的应用
--------------------

值得打开 Spotlight 开关的应用标准相较之下比较简单：

1. 看这个应用对 Spotlight 的支持是否正常合理
2. 你是否可以至少通过标题之类的内容，精确定位你想获得的结果

能满足这两点的我认为都可以打开，它应该达到的最理想的效果是：经过调教（让 Spotlight 记忆你的选择）之后，你想要的结果永远出现在第一个。

下面列出的是我在我的设备上打开 Spotlight 搜索开关应用以及原因。

### 办公应用

对拿移动设备使用办公软件的人来说，Spotlight 能不能搜到自己工作用的软件肯定算是头等需求。好消息是，苹果、Google、微软三大公司的 iOS 应用都可以做到这点。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/52DCC992-64AC-48D9-8DDA-CF16BDB97B0E.jpg)

苹果的三大办公套件永远是跟着系统的提升而更新的，Spotlight 自然也不例外。而且苹果在这里实现的方法很妙，考虑到你有可能把文件存到本地或 iCloud 里。Spotlight 既可以通过 iWork 应用搜索仅存在于本地的文件，也可以搜索 iCloud Drive 里的内容。不过，当你选择 Spotlight 中显示的储存在 iCloud Drive 中的 iWork 文件时，它会自动打开相应的 iWork 应用。所以如果你所有文件都在 iCloud Drive 里，你可以把 iWork 应用的 Spotlight 开关给关掉，这样可以避免重复的搜索结果。

Google 家的办公应用没有这种先天优势，却也用了 URL 的跳转方法，比如我搜索一个存在 [Google Sheets](https://itunes.apple.com/us/app/google-sheets/id842849113?mt=8&uo=4&at=10lJSw) 中的表格，它会给我返回 [Google Drive](https://itunes.apple.com/us/app/google-drive-free-online-storage/id507874739?mt=8&uo=4&at=10lJSw) 的结果，但当我选择了结果，它也会经由 Google Drive 跳转到 Google Sheets，并打开我选择的表格。

微软作出的选择比较传统，Spotlight 的搜索结果会是相应应用的结果而不是 One Drive 中的，所以想搜 Word 就要把设置里 Word 的 Spotlight 搜索开关给打开。

虽然三家公司用的方式各有不同，但都可以通过 Spotlight 来搜索文件并直达。

### 原生应用

**计算器**

计算器在 Spotlight 里是杀手锏级的功能，是你一有这样的需求就能想到 Spotlight 的存在。它可以基本代替计算器类、单位换算类、货币换算类三种第三方应用的通知中心插件。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/B0660779-9666-49B8-ABAF-D6056EEA28ED.jpg)

**闹钟**

闹钟在 Spotlight 里有一种独特的显示方式：

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/1642B31C-60B4-4A07-987A-1BDDD2E6D71B.jpg)

这种显示方式非常实用，不知道苹果是不是试水。除了闹钟外健康和日历也是这样，但都不如闹钟实用。

**音乐**

Spotlight 可以直接搜索歌曲名、专辑名、歌手名来定位某一首歌，也可以选择播放列表来播放音乐。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/CDA8A850-DAA5-41D4-8480-6872F7C49C88.jpg)

但是在这个位置的操作是在是太有限了，比如你选择了一个播放列表，你却不能调整它的**重复**和**随机**状态。这样的话，如果你在搜这个列表之前用了单曲循环，你用 Spotlight 播放的列表也会只循环列表的第一首歌，这就很尴尬。为了换状态还要再打开音乐，去调整重复和随机。iOS 10 里重复和随机本身就不怎么好找了，如果你开了歌词还得先隐藏歌词才能找到那俩按钮，苹果还是得好好改这个地方。

另外我因为等不及了所以也做了个 Workflow（[下载](https://workflow.is/workflows/a5eb60638a464462827962dee8997b14)），可以做到在通知中心选择列表（注意是选择，选择要比输入快）并且可以临时选择或预设循环和随机的模式。你如果有 Workflow 的话这是最快选择并播放某个播放列表的方式。

**通讯录**

通讯录大概是必须要留的，如果关了它就不能在 Spotlight 里搜索联系人。

### 第三方应用

**1Password**

一直以来，[1Password](http://sspai.com/tag/1Password) 在 iOS 上比自带的**密码**强就强在可以快速搜索。早先是通过 [URL Schemes](http://sspai.com/31500)，用 Launch Center Pro 或者 Workflow，可以做出搜索 1Password 条目的动作。现在这个优势直接被嵌到了 Spotlight 里，拉开 Spotlight 就可以搜索 1Password 条目，宛如 iOS 上的 1Password mini。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/45E679C1-E8F5-4E0E-B93E-3CD7D4563F94.jpg)

但这样做的弊端是像上图右侧一样，通过 Spotlight 搜索 1Password 条目后，左上角的返回按钮会变成**搜索**。在这一点，一个**预存了关键字**的 Workflow 动作可以完成得更理想。我们可以直接从通知中心跳到 1Password，因为这一步不是通过搜索进入的 1Password（也不是通过 Workflow 进入的，这种做法并不会没打开 Workflow），所以它可以直接通过左上角返回到上一个需要输入密码的应用。

所以在 Workflow 里预设好关键词的，可以照旧用 Workflow 跳；搜索不常用的密码的，用 Spotlight 找。

**Workflow**

[Workflow](http://sspai.com/tag/workflow) 有自己的通知中心部件，但我个人只在这里放那种仅通过通知中心就可以完成的动作。在通知中心跑一部分，再打开 Workflow 跑一部分的 Workflow 放这里只是浪费宝贵的位置。

我有 20 个左右的 Workflow 是需要从 App 内部打开的，其中我用的比较频繁的一个 Workflow 是从最近添加的音乐里选几首歌形成一个临时的播放列表（[下载 Workflow](https://workflow.is/workflows/dbf9455ce42a475b97b9b346693d46c5)）[2](http://sspai.com/35818#fn2)。这个 Workflow 不能在通知中心独立运行，因为选歌的步骤必须在 Workflow 里操作，所以这种动作用 Spotlight 搜就特别合适。

**云储存类应用**

iCloud Drive、Dropbox、Google Drive 和 One Drive 全部支持 Spotlight 搜索。前提是你需要起码打开过这些应用，并且进入过你想搜索的条目的相应目录。Dropbox 只在 Spotlight 返回已经读取过的文件。

这些应用特别适合用 Spotlight 搜索，因为当你在这些应用内进行搜索时，都多少需要读取一段时间才能返回搜索结果。但在 Spotlight，它不需要这个读取时间，因为 Spotlight 只是给你缓存过的结果，也就是说它没有应用内搜索给的完整。不过实用的点恰恰就在这里，因为缓存的位置是我们用过的位置也是我们接下来更有可能会用的位置，Spotlight 反而帮我们过滤了不常用的选择，实用性并不会打多少折扣。

举个例子，我头像的图在 Dropbox 里的名字叫 `03.jpg`。任何一个用 Dropbox 的人在 Dropbox 里搜 03 估计都能搜出来一堆文件，但因为我之前在 Dropbox 里找过这张图，所以再在 Spotlight 搜 03，就会首先出现这张图。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/9C376E6E-C60C-4B03-B2E6-119B96978FA0.jpg)

**写作、笔记类**

我所用的写作类 App 里[3](http://sspai.com/35818#fn3)，支持在 Spotlight 搜索的是 [1Writer](http://sspai.com/tag/1Writer) 和 [Byword](http://sspai.com/tag/Byword)，两个都是标题搜索加全文搜索，所以只用其中一个就好。

除了正式的写作类，笔记类的应用里，[Drafts](http://sspai.com/tag/Drafts) 和苹果自家的备忘录对 Spotlight 支持都很好。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/0B810BF2-88E8-475A-9046-776FE8FAFBAC.jpg)

**任务管理类应用**

目前人气比较高的 [Omnifocus](http://sspai.com/tag/Omnifocus) 和 [2Do](http://sspai.com/tag/2Do) 都支持在 Spotlight 里搜索任务，相信其它知名的任务管理类应用也能做到。

Omnifocus 的 Project（项目）、Context（上下文）和 Perspective（透视）都可以直接通过 Spotify 搜索，选择相应结果就可以跳转到相应位置。而在 Spotlight 中搜索 2Do 的某个列表，它会把你该列表内的任务给显示出来。两种不同的处理方式，看你的喜好。

![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/6D27A01C-B618-4434-8B66-8FC84CC6A0CC.jpg)

**Google Photos**

这一点 Google 甚至在 iOS 上走在了苹果的前面。

苹果连自己的照片应用都还没支持 Spotlight 搜索，[Google Photos](https://itunes.apple.com/us/app/google-photos-free-photo-video/id962194608?mt=8&uo=4&at=10lJSw) 里的**地点**和命名过的**人脸**等默认的相册分类就都可以在 Spotlight 里搜索得到了。

**Google Maps**

不得不说，Google 的应用对这些自己需要支持的地方都支持得非常到位。

你可以在 Spotlight 中搜索你在 [Google Maps](https://itunes.apple.com/cn/app/google-de-tu/id585027354?mt=8&uo=4&at=10lJSw) 保存过的地点，比如 Home 和 Work。

除了 Spotlight 搜索支持得好以外，Google Maps 的通知中心插件也很好，有在用的人可以留意一下。

**其它**

* [PDF Expert](http://sspai.com/tag/PDF%20Expert)：可通过 Spotlight 搜索其中的文件标题
* [Airtable](https://itunes.apple.com/us/app/airtable-flexible-database/id914172636?mt=8&uo=4&at=10lJSw)：可通过 Spotlight 搜索其中的列表
* [Evernote](http://sspai.com/tag/%E5%8D%B0%E8%B1%A1%E7%AC%94%E8%AE%B0)：只能搜索近期的文档的标题

我 iPad Pro 上装了 263 个应用（且几乎无国产），但总共也就扒拉出来这么几个值得打开 Spotlight 开关的应用，都是同类里的翘楚。所以也可以看出真正在思考这个位置的开发者和公司还不多，对 Spotlight 的支持还不是一个共识，这时候就看哪些开发者能走在别人前面了。

结语
--

Spotlight 搜索仍有进步空间，比如现在有一种情况是对 Spotlight 的滥用，几乎搜什么 Spotlight 都有它，苹果是不是应该在源头规避一下这种行为。我还希望用户能够对应用在 Spotlight 中所呈现的结果进行自定义。举个例子，对于我来说，写作软件的全文搜索是没必要的，只有标题就够了，所以如果 1Writer 能让我选择是全文还是标题搜索，就更好。

不过，在经过了设置、试错和调教之后，Spotlight 的表现已经让我基本满意：我要搜 1Password 项目的时候能够将相应的 1Password 项目放在第一位，找备忘录某个条目的时候那个条目就在第一个结果，搜 「03」 它就知道我要找的是那个藏在重重文件夹内的图片……这都是我从未指望在 iOS 上能够有的体验。

现在，一个应该对 Spotlight 有良好支持的应用是否做到了这一点，已经是我判断它是否足够优秀的标准之一。

欢迎在评论补充你打开了 Spotlight 开关的应用，供大家参考。

*注：虽然作者测试了文中提到的每一个应用，但因使用地区和语言选择似乎都与 Spotlight 的搜索结果有关，测试结果无法做到完全正确。具体情况还需读者进一步加以确认。*

1. iWork 的文件可以通过 Spotlight 在 iCloud Drive 中找到，选择结果可以直接跳转到相应应用，但其本身不支持 Spotlight 搜索。音乐备忘录里的内容也可以通过 iCloud Drive 找到，但不会跳转到音乐备忘录去。 [↩︎](http://sspai.com/35818#ffn1)
2. 这个 Workflow 并不会真的在音乐里添加个列表，但是选择的这几首歌可以临时地重复或随机播放，直到你手动换了音乐或者音乐应用从后台退出。 [↩︎](http://sspai.com/35818#ffn2)
3. 我在 iOS 上使用的写作类应用有：[Editorial](http://sspai.com/tag/Editorial)、[1Writer](http://sspai.com/tag/1Writer)、[iA Writer](http://sspai.com/tag/iA%20Writer) 和 [Byword](http://sspai.com/tag/Byword)。是的，没有 [Ulysses](http://sspai.com/tag/Ulysses) 🙃，但 Ulysses 也支持 Spotlight 搜索。 [↩︎](http://sspai.com/35818#ffn3)

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/69B89BCF-24B3-4EEE-ADFB-090125A2E460/F0FE736C-C7F2-41E3-B24E-77579FA11B10.jpg)](http://click.dji.com/ACLR_BH5xMntFK-4gR0?pm=link&as=0002)

---

[🌐 原始链接](http://sspai.com/35818)

[📎 在印象笔记中打开](evernote:///view/207087/s1/61963920-ef62-4325-b4ab-696adb91babc/61963920-ef62-4325-b4ab-696adb91babc/)