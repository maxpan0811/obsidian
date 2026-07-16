---
title: "macOS 效率启动器双雄：Alfred vs. LaunchBar"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/macOS 效率启动器双雄：Alfred vs. LaunchBar.md
tags: [印象笔记]
---

# macOS 效率启动器双雄：Alfred vs. LaunchBar

# macOS 效率启动器双雄：Alfred vs. LaunchBar --- macOS 效率启动器双雄：Alfred vs. LaunchBar ========================

---

# macOS 效率启动器双雄：Alfred vs. LaunchBar

---

macOS 效率启动器双雄：Alfred vs. LaunchBar
==================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

**编注**（@文刀漢三）：网上关于 LaunchBar 和 Alfred 的讨论，大多比较片面，并没有完整地对比过两款工具的功能。

Minja 本身是一位很擅长自动化工具的玩家，长期使用 LaunchBar。为了写这篇文章，专门将 Alfred 作为主力启动器使用了 4 个月，也为两款工具写过大量的自定义动作：

* [LaunchBar 动作](https://github.com/BlackwinMin/launchbar-gallery)
* [Alfred 动作](https://github.com/BlackwinMin/alfred-gallery)

因此，我们安排了 Minja 来写这篇 LaunchBar 和 Alfred 的对比文章。

启动器（Launcher）可以视为一批快捷操作的集合，集打开应用、取用文件和搜索资讯为一体，macOS 自 10.10 开始重塑的 Spotlight 就是其中典型；高级一些的还可以直达应用内部功能，甚至允许用户自编写自动化动作，这就到了以 Alfred 和 LaunchBar 为代表的第三方启动器的领域。想成为使用 macOS 的高手，免不了要和这些工具打交道。

Alfred 相对名声更大，经常出现在所谓的「装机必备」清单上，很多在 iPhone 4 流行后 1 才进入苹果生态的人，多半是通过 Alfred 才接触到「启动器」这一概念；而 LaunchBar 则是一家从上世纪开发至今的老字号，常常被视为唯一可以和 Alfred 对标的工具。

关于两者的对比不在少数，可惜很多都只是站在自己所用工具立场上的讨论。这篇文章不会给出一个一边倒的结论，而是从入门功能、进阶功能一路比到自定义的自动化，并且把最后的选择权交给各位读者。

由于对比的项目较多，我们准备了对比结果的汇总表格，大家可以点击查看大图，也可以在 [这里](https://www.notion.so/8ba15f9c3dc74e23bcd392d4691f7421?v=a2805c9ec0f74bc8afdb8e697123580a) 看到 Notion 的在线版本。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/DA8E8FB6-72AB-43D7-85F9-86FCD33E41DD.jpg)

LaunchBar vs. Alfred 详细对比（点击查看大图）

注：参与对比的是付费版 LaunchBar 和已解锁 Powerpack 的 Alfred，两者潜能皆已放到最大。未特别说明的情况下，对比截图的顺序统一为左 LaunchBar、右 Alfred。

基础功能
----

基础部分主要考虑启动器的自带功能，包括它对于**资讯的查询、文件的搜索、文本的处理以及和应用内部功能的交互**，这些功能一般不需要用户花太多力气，顶多在设置中稍加配置即可正常使用。对于绝大多数用户来说，熟悉启动器的过程都是从这些自带基础功能开始的，所以在跨过自定义动作的门槛之前，我们将重点对比 Alfred 和 LaunchBar 在基础功能方面的异同。

### 网络搜索

对于任何一款启动器来说，最基础、核心的功能就是搜索。Alfred 和 LaunchBar 都是同类工具里的标杆，可以不脱离启动器界面而直接输入关键词，并直达所需站点。

同样贴心的是，Alfred 和 LaunchBar 都拥有**模糊识别**的功能，LaunchBar 拥有完全的**模糊识别**功能，不求输入站点的全名，比如你想在 Google 搜点资料，可以只打 `goo`，甚至漏打几个字母变成 `goge`，它也能识别出来；而 Alfred 则稍差一些，打 `goo` 还能找到部分 `goo` 开头的项目，但跳过部分字母就无法识别搜索引擎或搜索 Workflow（感谢读者 @garyzhalo 和 @waynewu 的指正）。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/15C7E125-3F8C-4E74-B89D-BA9BDDB1DB59.png)

LaunchBar 拥有模糊识别功能

另外一个小差别是，如果你在 Alfred 里写了个搜索动作并且附上了缩写，那么输入这个缩写时候就只能出现有缩写的站点，会影响原有的模糊识别功能。设置搜缩写时需要稍微注意一下。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/2BD8150A-EDE3-4D95-ABEE-83F0DD8CA20F.png)

缩写会影响模糊识别

显然，两者的区别并不在于步骤的多寡，但是进一步的搜索细节差异泾渭分明了。

#### 搜索建议

对于**搜索结果的呈现**，不装插件的 LaunchBar 更胜一筹，它自带了**搜索建议**。LaunchBar 内置的 Google、DuckduckGo 等搜索引擎都可以列出前几个搜索结果：

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/06D6BFD2-3896-4F09-A352-7AC18E58D12B.png)

LaunchBar 自带的 Google 搜索就具有搜索建议

经 @契丹神童 提醒，这种搜索建议特性要归功于 LaunchBar 自带的脚本 Suggestions Script，同时这一脚本在用户自行编写搜索动作时也可以派上用场。

虽然 Alfred 没有自带搜索建议，但是因为它人气较高，常见网站都有人给写了搜索 Workflow，搜索建议的呈现效果同样优秀：

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/D69B89FA-1057-45E5-A24C-67A1A9CFEBDD.png)

Alfred 的搜索 Workflow 也可以呈现搜索建议

就实际使用而言，两个工具的搜索建议呈现效果都不错。

#### 多站点搜索

至于**多站点搜索**，Alfred 则凭借设置简单技高一等。在比价、购物、找文献时我们经常需要搜多个网站，对于这类场景，可以在 Alfred 里设置一个 Workflow 模板，把你要搜索的网站链接唰唰丢进去，从而实现输入一次、搜索多处。

下面就是一个多站点搜索动作，可以同时搜索 500px、freepik 和 Unsplash 等 3 个图片站点，需要的读者可以点击 [这里](https://github.com/BlackwinMin/Alfred-gallery/tree/master/Search%20Picture%20Sites) 下载 Alfred 版 。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/3E4E809D-EE40-40DE-8DF8-F72AA567DAE5.gif)

用 Alfred 同时搜多个站点

虽然这个动作需要自己动手制作，不过依然非常简单，几乎就是把三个 Alfred 自带的搜索操作拼在一起。想换用其他搜索引擎的话，也只替换动作里的几处 URL。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/6361DBE5-51A6-4360-968A-48722059BE15.png)

Alfred 的 Workflow 流程可以很简单

同样的多站点搜索在 LaunchBar 中实现起来要复杂得多，一般需要配合 Automator 或者编写脚本。

### 文件搜索

如果把 Alfred 的文件搜索功能列在 LaunchBar 之上，相信多数人对于这个结论都没有太大意见；但是具体到背后的原因，可能不少人会说「LaunchBar 不支持中文」—— 这实属被工具的外观给骗了。我们将在后半篇的操作方式部分详细说明，这里先基于**两者都支持中文**这一前提进行比较。不过结论仍然不变， **Alfred 更加易用使用，而 LaunchBar 则在操作上有一些独到之处。**

如果给搜索功能分分层，以原生 Finder 的高级搜索功能为满分线，文件搜索的要求从基础到高级有这几层：

1. 最简单，**关键词搜索**，给你一串结果列表。不过这种搜索方式往往掺上大量无关文件。
2. 进阶一些，**支持搜索语法**，典型如输入 `tag:red` 把结果限定为标有红色标签的文件。对此，Alfred 和 LaunchBar 都有简单涉及。
3. 高级功能，**对搜索结果进行操作**，比如预览、按日期排序或显示源文件，厉害一点的还能搜到图片后进行批量压缩、找出 Word 文档后转为 PDF，等等。

两位选手在 3 个方面都有涉及，交火主要发生在对于搜索结果的后续处理上。总的来说，Alfred 在文件搜索功能上更加偏向原生 Spotlight，允许用户在搜索结果中直接查看文件的预览效果，看图片时尤其方便；最近升级到 4.X 大版本后还在 File Navigation（文件导航）界面里加入了排序功能，已经部分超过了 Spotlight 而向 Finder 看齐。你在 Spotlight、Finder 里最常做的文件搜索及操作，相当一部分可以放心交给 Alfred。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/CFAC1AED-8927-41F3-A28F-B8465CF808FA.png)

Alfred 可以预览和排序文件

LaunchBar 似乎走向了另一个方向，不管你搜什么，给出的都是小图标、 文件名和文件路径的组合。这样的呈现方式并不讨好眼球，搜索结果项太多时还要一个一个按空格预览，不如 Alfred 那样明了 —— 何况 Alfred 也可以只显示名称等精要信息。国外高玩 Dr.Drang 倒是认为 [LaunchBar 的显示方式更简练紧凑](https://leancrew.com/all-this/2019/04/back-to-launchbar/)，更加适合处理大宗任务。但就日常使用而言，**在搜索结果的显示方式上，LaunchBar 还是无奈败下了阵来。**

不过 LaunchBar 的**结果显示方式**给它在文件搜索上扳回了半局。如果文件命名妥当，在 LaunchBar 里只要按一下目标文件的头几个字母就能把它们快速过滤出来。例如在曲库里有一堆歌手 `HAG` 的音乐，都用 `HAG` 打头，那么按一下 `h`，这些文件就会涌到搜索结果最上面。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/2BED8E55-CA1C-4F94-9865-522A53E72737.gif)

LaunchBar 可以通过文件名首字母或前几位字母快速定位

而 Alfred 的首字母排序功能较弱，它会把名字带 `h` 的都列出来，在文件较多时并不利于查看。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/213DBF51-6EE0-47CC-9392-CFD8AFCFCF47.png)

Alfred 列出了所有带字母 H 的歌曲

### 文本操作

文本操作这个概念比较宽泛，把一段英文句子首字母大写算文本操作，快速插入邮箱地址也算文本操作。总体上看，启动器内置的文本操作有这几类：

* **剪贴板管理（Clipboard Manage）**：保管剪贴板的历史记录，方便调用以前拷贝过的内容。LaunchBar 和 Alfred 都可以保存一段时间内的文本、图片或文件路径历史，并且可以显示拷贝来源。  

  ![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/46F6BCA5-CB0A-4583-87F6-74D097474025.png)

  LaunchBar 和 Alfred 的剪贴板管理界面
* **文本片段（Snippet）**：只打几个字母就快速插入一整段常用文本，例如输入 `ddate` 就插入当前的日期。  

  ![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/FD877C65-C4AB-4916-8BC7-5BBAE8792DB4.png)

  LaunchBar 和 Alfred 的文本片段
* **其他动作**：通过系统 / 工具内置服务或用户自定义动作来处理文本，包括但不限于繁体 / 简体转换、去重复多余空格、等等。一般来说只要启动器支持脚本，这些犄角旮旯的功能都不难实现。  

  ![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/522E2F01-59BA-4726-B8F1-37787E21C60D.gif)

  我为 LaunchBar 编写的文本替换动作

这里要先表扬一下两个工具，**在剪贴板管理和缩写方面做得都不错**，均支持为这些子功能设置快捷键，在涉及大量文本操作 —— 比如填写表单 —— 时很方便，不用再去启动器界面里搜索。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/C209845D-FE01-4B87-9BA0-C90946FF2A8E.png)

为剪贴板历史界面设置快捷键

不过一转到 **Snippet 的编辑界面**，Alfred 就开始显得更加友好。LaunchBar 的遗憾在于全靠文本文件来储存 Snippet，而 Alfred 可以在设置界面直接进行编辑，同时把可使用的占位符（Place Holder）都列了出来，能看懂英文就能猜出来它们的用途。Alfred 新版本中还支持了富文本，同时 LaunchBar 一直以来也支持富文本片段，在 Snippets 文件夹中存入 `.rtfd` 即可。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/F37CF581-6CD0-4251-A636-F6FC338E02D1.png)

Alfred 的 Snippet 编辑界面更简单

至于文本动作，LaunchBar 做得更好，它的杀手锏是**支持系统和应用的内置动作（也叫服务）。**比如系统自带的大小写转换、简繁体转换服务，或者选中一段文本直接添加到 Evernote 里作为新笔记。而 Alfred 用户的选择比较少，一般需要去网上寻找别人编写的动作。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/24AAF0C5-1B68-40D9-A971-FB1988B9A313.png)

LaunchBar 一大优势是可以使用其他工具里的现成动作

拓展到自定义动作方面，尽管理论上两者功能近似，LaunchBar 却凭**操作干脆**再胜一步。借助 Instant Send 功能，我们除了在启动器里直接输入文本，更可以在任何能选中文字的地方把要处理的文本**发送**给 LaunchBar，就像按下火箭发射按钮一样。比如在网页上看到一个生词，就可以「发送」到 LaunchBar 里进行搜索。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/8FB89BCF-A7A5-4BF4-B0F7-0E29969100C6.gif)

通过双击 ⌘Command 键从任何地方把文本发送给 LaunchBar 处理

Alfred 倒是也能 [借助 Workflow 模仿这一操作](https://sspai.com/post/46088)，可惜仍然不敌 LaunchBar：后者的 Instant Send 功能通吃文本、单文件和批量文件，不需要背一堆快捷键。

熟悉其他文本处理工具的读者可能已经发现，启动器的文本功能和其他文本处理工具有很大重合。同样功能丰富的前提下，**Alfred 的功能细节更加全面**，如果你没有用过 TextExpander 或者 Keyboard Maestro 来快速输入文本，或者还没专门的剪贴板管理工具，那么 Alfred 很可能是第一个颠覆你对于文本处理认识的工具；不过当你任务变多变重之后，大概率会需要几款专门的文本处理工具 2 来分担启动器的压力，此时 LaunchBar **操作轻快**的优势就显示了出来。

总而言之，论及文本处理，单枪匹马的 Alfred 可以让轻度用户**一步到位**，LaunchBar 则适合在重度工作中和其他文本处理工具**打好配合**。

### 应用交互界面

除了文件、文本这些常见对象， 启动器也负责直接和应用内部功能交互。在 iOS 折腾过自动化的读者多少都知道 URL Scheme（最起码，3D Touch 可以直达扫码付款是人尽皆知），和它类似，macOS 启动器的一大重要职责就是**跳过应用的重重界面，直达所需的功能**，例如：

* 不开启 iTunes 主界面，直接点播曲库中的专辑
* 不打开行事录，直接添加带日期和地点的日程
* 不打开通讯录，直接调出联系人的邮箱
* ……

这些事情不少高级自动化工具都能做，LaunchBar 天生就可以，乐意折腾的话 Keyboard Maestro 也可以，可惜都难以和 Alfred 比肩。从和通讯录的交互就看出 Alfred 的所呈现信息之丰富：

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/0E422474-1431-4AC5-AC63-A51E63FAF1F1.png)

Alfred 能比 LaunchBar 呈现更多的应用内信息

相比之下 LaunchBar 就显得很克制甚至有点保守，从文件图标到联系人头像都是裁成同一个尺寸的缩略图。Alfred 能够给新手「洗脑」的魔力很大程度上就来自其出众的视觉冲击力，如果甩一堆 Alfred&iTunes、Alfred&Contacts 和 Alfred&Files 的截图过去，相信很多人是会买账的（如果要使用 Alfred 控制 iTunes 迷你播放器，[需要先去 iTunes 里打开 xml 数据共享](https://www.alfredapp.com/help/troubleshooting/itunes/)）。在 Alfred 和应用的「交互」是相互的，很多时候有即时反馈，用户知道发生了什么。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/D8555E08-DB82-4049-930A-51C684D602BD.png)

Alfred 的迷你播放器

严格来说 Alfred 所做的事情已经超出了一个启动器的本职，从通讯录详情呈现、iTunes 界面控制到一些玩家自己写的迷你监控器，Alfred 早就不只是一堆按钮的集合，它还配上了呈现信息的大屏幕，摇身一变成了**集输入和输出为一体**的自动化处理中心。下图是一个 [高玩](https://wil.dog/ariafred/) 写的 Aria2 下载进度查看器，足以一窥 Alfred 的全能。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/2F5BDF90-C4A0-49C2-B684-A44CE42911E6.png)

用 Alfred 查看下载进度 图 /wil.døg

LaunchBar 自然也有简单的输出界面，可更多时候只是提供一些子选项，其所呈现信息的丰富程度是无法和 Alfred 相比的。

高级功能
----

区别于工具的基础功能，高级功能或多或少需要用户自己动手制作或配置。从 Alfred 和 LaunchBar 的社区状况多少可以反映出它们高级功能的易用程度高低：Alfred（的用户）实在活跃太多，和它的**可视化编辑界面**脱不了关系。但如果只看到表面的数字，也就不必写这篇文章了 —— 我们将对两个工具在不同方面的高级功能进行对比，看看他们之间到底是「差距」还是「差异」。

### 应用服务

在自行编写动作之前，其实有一类不能忽视的自动化动作：**系统和应用自带的自动化动作，即 Services 服务**。比起 Alfred 和 LaunchBar 自己的动作，这些用系统原生工具编写的「小插件」结构更简单，在网上能找到的资源也更多。

LaunchBar 在对于这些小插件的支持上，可以说是完胜 Alfred，因为后者至今为止也没能支持系统和应用自带的服务动作 —— 假设你从网上下了个生成 Markdown 链接的服务、或者统计字数的服务，很可惜，在 Alfred 里跑不了。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/F7ABFEB2-6115-469A-BE98-45DB714BE378.png)

LaunchBar 可以和任何类型的服务协作

在不编写或下载任何动作的情况下，LaunchBar 天生就能做到：

* 将选中的单词用标准发音读出来
* 让选中的文件上传到 CloudApp 并随后获得链接
* 把当前网页的视频转到 IINA 里通过串流播放，避免出现广告
* ……

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/5E20B2DB-3676-4AB2-B2E0-5ABB571FED3B.gif)

把网页视频通过 LaunchBar  发送到 IINA 里播放

这些都让未配备 Workflow 的 Alfred 望洋兴叹。

### 自定义动作：Workflow or Action？

虽然 Alfred 在内置服务动作的表现上失利，但动作方面的比试还未结束，我们来看看最难的一关：用户自定义动作。

能否自定义动作，是 Alfred 和 LaunchBar 与一批「应用启动器」的分水岭。这句话有两层意思：

1. **可以跑各种脚本。**脚本算是动作的一种，获得了运行脚本的能力后，理论上只要用户能自己编写动作或搜到别人做的动作，几乎 macOS 上的任何操作都可以实现。去年 Mojave 系统发布后很火的几个「暗色模式切换」动作，里面就是一段切换系统主题的脚本（[动作作者 @涔 C](https://sspai.com/post/45857)）。  

   ![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/CF2E4D6A-7090-467E-A54E-5230637CF904.gif)
2. **可以方便地把数据传递给动作。**光是孤零零地启动一个动作还不够，进一步要能够把一段文本或一个文件交给动作去处理。这种原地变戏法一般的操作是高级启动器工具的精髓，LaunchBar 的 Instant Send 发送功能 Alfred 和文件批处理快捷键 `⌥Option-⌘Command=\` 都是个中佼佼者。  

   ![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/FA0B4D3E-0778-446D-94AA-0C4CCF83460D.gif)

在自动化能力上，Alfred 和 LaunchBar 是基本等价的。两年前我从 Alfred 切换到 LaunchBar 后大部分动作都是从头开始编写，这几百个看似 LaunchBar Only 的动作其实改下头尾代码，基本就能直接搬到 Alfred 里去。

![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/490FD070-2DD9-4EE1-8AD8-DBEFC4FFFD6E.png)

因为能力等价，基本上可以为两个工具同步制作新动作

不过在功能比不出高下的情况下，Alfred 的动作制作方式更加简单。保持了脚本功能的前提下，Alfred 的最大特色就是拥有**图形化编辑界面，可以不用任何代码知识**。不熟悉自动化的读者别怕被这些名词唬住，它用起来和捷径基本差不多，前面搜索小节我们介绍过一个多站点搜索的动作，它就是用一个个「积木」搭起来的：

1. 输入动作触发词和搜索关键词
2. 打开多个不同的网站  

   ![](.evernote-content/D16B8B15-8E23-405A-A788-4D4B2DF5F2FF/6361DBE5-51A6-4360-968A-48722059BE15.png)

   Alfred 简单易懂的动作编辑界面

Alfred 的动作称为 Workflow，不过比一根肠子通到底的捷径动作更厉害，可以通过连线组成复杂的逻辑网络，上面的多站点搜索是一个「一拖三」的例子，已经足以看出 Alfred 动作编辑器朴素界面背后的强大。尽管通过图形化界面制作的动作无法移植到其他工具里，但没人可以否定 Alfred 的简单易上手 3 。

小结
--

Alfred 的**界面和功能**更直观，符合我们已有的习惯。比如从 Spotlight 那里学来搜索结果预览、从 Automator 那儿继承图形化动作编辑界面…… 这些 Mac 原生工具的闪光点都集成在了 Alfred 中。没有用过启动器、或者对于整个 macOS 自动化都不熟悉的用户，挑 Alfred 是一个不会出错的选择；有过一定折腾基础的读者也可以直接买下 Alfred 的 Powerpack，用自己熟悉的方式改造它。

而 LaunchBar 拥有**更贴心的操作**，并且集成了系统和第三方应用的**大批动作**。操作方面，我们已经提到过快速处理文件和文本的 Instant Send、文件搜索中的首字母定位等特性，它们带来了符合直觉的全键盘操作。一旦我们接受了这些操作，就很容易享受 LaunchBar 的大部分功能：刚上手时有自带动作，稍稍熟悉后可以调用系统和第三方工具的服务，熟练了之后也能下载脚本或自己编写，整个学习过程是一段相对平稳的曲线。也正是因为 LaunchBar 和众多第三方工具配合得很好，我个人选择了留在 LaunchBar。

同作为 macOS 上的顶级启动器，Alfred 和 LaunchBar 之间只有细节的差异，而不具有本质的差距。挑选一个启动器是累人的，若非兴趣使然，并不建议像我这样在每个工具上都投入数年时间。希望这一篇文章可以帮你节省亲自比对的工夫，尽快找到自己的搭档。

最后，感谢同事 @Hum 的推荐、以及作者 @契丹神童 的教程（撰写阶段就让我先睹为快），给我一个从 Alfred 切换到 LaunchBar 的尝试机会；也感谢作者 @涔 C 的系列 Alfred 文章，让我在使用 LaunchBar 同时能够同步关注着 Alfred 的发展。

群讨论预告：Windows、Android、iOS 等平台的启动器对比
-----------------------------------

本文是侧重 macOS 平台的启动器对比，因此不适合加入其它平台的内容。但考虑到读者里也有很多其它平台的用户，所以我们决定将 Windows、Android、iOS 等平台的启动器内容放到 Power+ 会员群讨论中进行。

欢迎大家和我们分享其它平台的启动器应用，以及说一说你选择它的原因。

* **时间：**周四（7.11）晚上 8:00–8:30
* **地点：**Power+ Slack 会员群的 #闲聊 频道
* **参与方式：**[点此了解如何加入 Power+ 会员群](https://sspai.com/post/51265)

1. [Alfred 是 2011 年发布的↩](#)
2. [比如在 iOS 设备上快速输入文本就选 TextExpander，需要跨设备同步剪贴板历史就用 Copied。这些都是几款启动器目前做不到的。↩](#)
3. [同时一点也不耽误你写脚本。↩](#)

[#macOS](https://sspai.com/tag/macOS)[#自动化](https://sspai.com/tag/%E8%87%AA%E5%8A%A8%E5%8C%96)[#Alfred](https://sspai.com/tag/Alfred)

---

[🌐 原始链接](https://sspai.com/post/55614)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f6419a93-915d-4657-8810-0dca8176fa79/f6419a93-915d-4657-8810-0dca8176fa79/)