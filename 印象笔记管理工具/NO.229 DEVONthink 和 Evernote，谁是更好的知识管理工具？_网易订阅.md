# NO.229 DEVONthink 和 Evernote，谁是更好的知识管理工具？_网易订阅

---

NO.229 DEVONthink 和 Evernote，谁是更好的知识管理工具？
-----------------------------------------

作者：vanilla2w

　　作为一个文件管理工具，DEVONthink 因为强大的收集整理系统，以及独有的面向文件的人工智能分析功能，成为了很多海外 Power Users 构造个人知识库的第一选择。但是，DEVONthink 高昂的售价、不完备的中文支持、瘠薄的社区氛围和强大的竞争对手使得它在中国市场有点寸步难行。除了这些客观的因素，人们主观上对 DEVONthink 进阶功能的畏难情绪也是导致 DEVONthink 在中文圈水土不服的重要原因。

　　而 Evernote 作为最负盛名的知识管理工具，得益于良好的中文支持，在中文世界几乎横扫了这片市场。很多中国用户都会使用 Evernote 来剪藏网页上的内容，收集到自己的笔记本里，打上标签，分门别类地整理好，需要灵感或参考的时候再从中找到有价值的信息。

　　那么，如果拿 Evernote 和 DEVONthink 相比较，在知识管理这个领域到底谁能更胜出一筹呢？

　　核心区别

　　首先我们需要搞清楚的是 DEVONthink 和 Evernote 这两个工具的定位在本质上是有区别的。

　　虽然 **Evernote** 拥有全平台覆盖的客户端以及完备的笔记离线功能，但是它 **其实是一个基于网络的服务**。所有导入进 Evernote 的笔记或者附件都会无差别地通过 Evernote 的服务器（托管于 Google Cloud 上）在各个客户端之间同步，你无法选择同步哪些笔记或者笔记本。Evernote 像是一座只进不出的孤岛，一方面因为它的笔记导出后唯一的格式就是 Evernote XML Format，这种格式的文件几乎没有第三方应用能够打开（DEVONthink 是少有支持这种格式的应用之一），另一方面 Evernote 又通过它的 API 来与其他一些第三方应用关联，比如通过 IFTTT 将 Instapaper 中的高亮文本自动发送到 Evernote 中，或者将 Reeder 中的文章直接在应用中添加到 Evernote。

　　DEVONthink 则是一个彻头彻尾的本地文件管理器，没有自己的云同步服务器，更不提供 API 供第三方应用或者服务使用。DEVONthink 可以视作是 Finder 的一个延伸，它支持几乎所有格式的文件的导入与导出，这就方便了它与其他应用之间的互通与协作。除此之外，DEVONthink 支持在应用内对 PDF、DOCX、PPT、XLSX、HTML 等多种主流格式直接预览，还可以直接编辑修改 RTF、Markdown、Text 和 Formatted Note 等格式的文本文件。

　　在这些类 Finder 的属性之上，DEVONthink 独特的文件管理功能、人工智能分析功能和强大的自动化功能让它成为了在 macOS 上远比 Finder 还强大得多的本地文件管理器。

　　对比标准

　　在开始比较 DEVONthink 和 Evernote 在知识管理领域的长短之前，我们需要明确的是：什么是知识管理工具的必备素质？在我的使用环境中，它需要满足以下 4 个基本要求：

**资料收集**：它必须要有自己的工具来**捕捉网上的内容或者导入离线的文件**，也就是资料的收集；

**资料整理**：在网页内容或者文件进入应用后，它得**有完善的系统**来管理这些资料；

**资料编辑**：应用**对文件内容的编辑功能**也很重要，因为这些资料是需要保持更新的；

**资料搜索**：要确保自己构建的知识库是能被轻松调取使用的，也就是说你需要的信息**可以通过应用内的搜索引擎查**找到。

　　接下来，就让我们从资料收集、管理、编辑和搜索这四个方面来一探究竟，看看 Evernote 与 DEVONthink 在这些方面究竟孰优孰劣。

　　资料收集

　　资料收集主要包含了**捕获网页信息**和**导入离线文件**两部分，我们分开来看。

　　捕获网页信息

　　Evernote 是通过它的浏览器插件 Clip to Evernote 来实现网页剪藏的，同样地 DEVONthink 也是通过浏览器插件 Clip to DEVONthink 来实现这方面的功能，那么相比之下谁的收集功能更强大呢？下面我们来做一个详细的对比。

　　从 Evernote 的剪藏菜单可以看到，Evernote 对网页文章的处理可以分为三种：

　　文章（Article）：在全网页的基础上只保留文章的部分，去除了评论和广告等，但是依旧保留了原网页中文章的排版；

　　简化版文章（Simplified Article）：在文章（Article）的基础上简化排版，也就是我们俗称的「阅读模式」；

　　全网页（Full Page）：简单粗暴地直接把整个网页捕获了下来，保留了这个网页中的所有元素，包括评论和广告等。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/F57B6F5A-F823-4FCE-AF8D-227181629F2A.png)

　　Evernote 的裁剪功能

　　不管选择哪一种剪藏形式，在 Evernote 中最终生成的事实上都是 Evernote XML Format 格式的笔记，而这种单一格式的笔记文件在日常使用中是有很大的限制的：

　　Evernote XML Format 作为 Evernote 自己开发的标记语言，在独树一帜的同时也意味着它的兼容性很差，也就是说 Evernote 的笔记导出后是无法被其他应用打开和编辑的；

　　其他格式的文件在 Evernote XML Format 格式的笔记中只能以附件的形式存在，于是像 PDF 这样的文件就无法自由地进行批注；

　　对于 Markdown 这种在效率爱好者中流行的标记语言，Evernote 对它的支持几乎是零，受限于 Evernote XML Format 格式，Evernote 无法对 Markdown 文件进行导入、预览或者编辑。

　　而 DEVONthink 作为一个全格式支持的文件管理器，**完全可以弥补 Evernote 的这些弊端**。DEVONthink 通过它的浏览器插件「Clip to DEVONthink」来收集网页资料，在下图中我们可以看到 DEVONthink 提供了非常多的格式供你选择，这样一来我们就可以自由地选择最适合收藏、编辑、协作或者分享的格式。图中的这九种选项至上而下分别为：

　　Plain Text 纯文本格式，文件后缀名为 text；

　　Rich Text 富文本格式，文件后缀名为 rtf；

　　Bookmark 书签格式，文件后缀名为 webloc；

　　Formatted Note 格式化笔记，文件后缀名为 html；

　　HTML Page 超文本标记语言，文件后缀名为 html；

　　Markdown 标记语言，文件后缀名为 md；

　　Web Archive 网页存档格式，文件后缀名为 webarchive；

　　PDF（One Page），文件后缀名为 pdf，单页模式；

　　PDF（Paginated），文件后缀名为 pdf，分页模式。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/F7D5B9DB-FB58-46CA-BD24-DE83D43F8958.jpg)

　　DEVONthink 的剪藏功能

　　在上图中可以看到界面下方有一个 「Use clutter-free layout」的选项，在 DEVONthink 中勾选它对应的就是 Evernote 中的「简化版文章」模式，不勾选它对应的就是 Evernote 中的「全网页」模式。

　　虽然 DEVONthink 对于网页文章的捕获只提供了勾选「Use clutter-free layout」与否两种排版方式，但是它提供了多达 9 种格式上的选择，就算刨去两种非离线的保存格式 Bookmark 和 HTML Page 也还剩下 7 种，这样一来你就有了 13 种选择，少了 1 种是因为 Plain Text 不能勾选「Use clutter-free layout」。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/D28C8776-9DE8-4CC8-BA3D-72B904995D95.png)

　　DEVONthink 两种剪藏模式的区别

　　我从少数派任意选择了一篇文章《2018 年主流 RSS 服务选哪家？Feedly、Inoreader 和 NewsBlur 全面横评》，来测试一下剪藏的效果。以下分别为使用 Evernote 剪藏插件的「文章」、「简化版文章」和「全网页」模式的呈现效果：

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/B4DBBC98-E6FB-4D61-8077-4867AD6E9DEE.jpg)

　　Evernote 三种剪藏插件的效果对比

　　我们在上图中可以看到，在「简化版文章」模式下，这篇文章的目录被省略了，而在「全网页」模式下，网页中少数派的 LOGO 、右上角的工具栏和文章下方的评论（受篇幅影响图中未能显示）都得以保存。

　　再来看 DEVONthink 对网页的捕获效果，从之前提到的 13 种选项中筛选掉不适合用来离线保存网页文章的 Plain Text、Rich Text 和 Markdown 格式，最终有 6 种文章呈现的效果。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/8B8C3C70-E5C2-444A-991A-809F45297F7D.jpg)

　　DEVONthink 的 6 种剪藏效果

　　对比 Evernote 和 DEVONthink 对同一篇文章的捕获效果，我们可以看出两者不分伯仲。但是，**DEVONthink 比 Evernote 提供了更多文件格式上的选择。如果你想要编辑捕获下来的文件内容，你可以选择 Formatted Note 格式；如果你想要在编辑捕获下来的文件中批注，那么你可以选择 PDF 格式；如果你只想离线保存原网页的所有元素，那么你可以选择 Web Archive 格式。**

　　这种多格式的选择，为你在使用 DEVONthink 来收集网络资料时提供了更大的自由度，因为你可以根据自己的需求来选择对应的格式，所以 DEVONthink 在这一环节略胜一筹。

　　导入离线文件

　　接着，再来看两个应用导入离线文件这一部分的对比。

　　在 Evernote 中你无法直接往应用里导入文件，你只能往已经创建好的笔记里导入文件，而且除了图片，其他格式的文件都是以附件的形式存在于笔记中，无法预览，也无法编辑。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/BEACB978-2DDB-4422-83D4-8888EA31C21C.png)

　　Evernote 中图片以外的文件是附件格式的

　　而 DEVONthink 不但可以导入（Import）文件，还可以选择索引（Index）文件，与本地的源文件直接关联。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/CCF698C2-17F0-4ABE-84CD-331985D34DDF.jpg)

　　DEVONthink 可以导入和索引文件

　　如果你选择导入文件，那么这些文件将会独立存在于 DEVONthink 的数据库中，与原路径下的源文件没有任何的关联，你对导入的文件做出的任何修改都不会影响 Finder 中的源文件，包括在同步状态下文件的自动更新。 而索引这个功能只是读取了文件中的内容，并没有将 Finder 或者外接硬盘中的文件真正地导入应用中，但是你依旧可以对这些索引的文件进行与导入的文件几乎相同的操作，包括预览、编辑和更改附加状态（包括标签、旗标、注释等）。与导入文件不同的是，索引的文件更像是源文件在 DEVONthink 中的一个快捷方式，不管你对索引文件还是源文件作出任何的修改，另一个文件也会随之更新到相同的状态。借助这个特性，DEVONthink 可以通过索引其他第三方应用的外部文件夹来与其他应用形成一个互通与协作的过程。

　　综上所述，**DEVONthink 在捕获网页信息上比 Evernote 提供了更多的格式选择，又采取了导入与索引两种形式来导入离线文件，而 Evernote 独有的 Evernote XML Format 格式则成了它自己最大的束缚，所以在资料收集这方面 DEVONthink 无疑更胜一筹。**

　　资料管理

　　如今，我们已经可以通过搜索功能来找到我们想要的文件。但是优秀的文件管理习惯，依然能提高你找到文件的速度；一个优秀的文件管理系统，也可以提高搜索的成功率。

　　在这一部分，我将从结构、过滤和链接这三方面来解释 DEVONthink 在资料管理上是如何全方位碾压 Evernote 的。

　　结构

　　DEVONthink 的资料管理系统中的结构比 Evernote 要多两个维度，这就意味着 DEVONthink 的资料管理能力更加强大和灵活。

　　Evernote 的文件管理结构很简单，只有笔记本和标签这两个维度。虽然 Evernote 可以通过笔记本来整理笔记，但是让很多使用者不满的一点是，Evernote 的笔记本只能实现一次嵌套。也就是说，你可以将你的笔记本放到一个笔记本组中，但是不能把这个笔记本组或者其他笔记本放到另一个笔记本组中。这就是 Evernote **在笔记本这个维度上的二级层级。**

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/77963939-A0D7-4737-89B5-9E60AEB067A1.png)

　　Evernote 的笔记层级

　　Evernote 可以给笔记加上标签，这个**标签系统是无限层级的**，也就是说你可以无限嵌套 Evernote 中的标签。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/BD4495CC-F6DC-4B44-BA33-C40C5D655D86.png)

　　Evernote 中的标签

　　另外，在 Evernote 中，你**必须把笔记放入某一个笔记本中，但不是必须要给这个笔记打上标签。**

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/84DC567F-B78B-4E26-99D2-86DB36225058.png)

　　在 Evernote 中文件夹是必需的

　　DEVONthink 的文件管理系统的情况会略微复杂一点，因为它有更多的维度：

　　第一个维度（Sync Store）：你在设置同步方式的时候，不管选择哪一种同步方式都需要创建一个 Sync Store，而在同一个同步云盘下你可以添加多个 Sync Store，目的在于满足用户对不同同步选项的需求。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/4E72E4D4-05B0-4EAC-BFF2-F9EE7F82E318.png)

　　DEVONthink 的同步选项

　　第二个维度（Database）：你可以在每一个 Sync Store 中都创建 Database，根据 DEVONthink 的版本你可以创建一个或者多个 Database。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/8E7AB6C4-1E9F-4326-B366-45B604F12BDA.png)

　　DEVONthink 中的 Database

　　第三、四个维度（文件夹与标签）：在 Database 中，你可以选择把文件**单独放入**文件夹中或者放入标签中，或者选择把文件**同时放入**文件夹和标签中。

　　为什么有「放入标签中」这种说法呢？因为在 DEVONthink 中标签的作用几乎与文件夹相同，除了你可以为同一个文件打上不同的标签却只能把它放入一个文件夹这一个区别。

　　从下图中可以看出，其中三个文件打上了「test」的 标签，所以它们在「test」这个标签下，但是它们不隶属于任何一个文件夹。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/C49816A2-24FD-4501-A0A1-E8D25453DDBE.png)

　　打上「test」标签的文件

　　过滤

　　过滤的作用在于快速筛选出有价值的信息，减少重复查找文件的时间。**Evernote 提供的过滤功能是通过保存搜索的形式来实现的，具体来说就是先搜索关键词配合过滤参数，然后保存这次搜索方便日后调用。**在 Evernote 中，过滤参数主要包含了笔记本、标签、笔记内包含、笔记源、创建日期和修改日期这六种。这六种参数在使用中只存在并列的关系，即搜索结果只显示同时满足所有过滤条件的笔记。 而 DEVONthink 采用了和 Finder 类似的文件过滤方式，就是智能文件夹。与 Evernote 只提供了 6 种过滤参数形成鲜明对比的是 DEVONthink 的智能文件夹功能包含了多达 37 种属性以供筛选，其中包括了文件名、标签、文件体积、文件格式、添加日期等基础参数和元数据、版权、尺寸等进阶参数。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/E3B0687B-A136-4455-869D-6C0A36D00B82.png)

　　DEVONthink 中可选的的过滤参数

　　除了大量的过滤参数外，DEVONthink 还提供了很多 Evernote 不具备的过滤功能：

　　可以将筛选范围限制在指定 Database 或者所有 Database 中；

　　每一条过滤规则可以选择「全部满足」或者「满足其一」；

　　过滤规则可以实现无限嵌套；

　　可以设置是否忽略变音符和是否启用模糊查询。

　　例如通过下图这个设定，我可以在这个智能文件夹中快速地提取出所有满足任一过滤规则的文件，目的在于收集归纳我在这一年中对财务开支、资产捐款和书籍阅读等方面的记录，方便我平时查阅以及在年终总结中调取使用。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/74F9F744-BB9C-496E-943D-5EC79B8A4C46.png)

　　DEVONthink 过滤示例

　　链接

　　虽然 DEVONthink 和 Evernote 都可以获取每个文件或者笔记的专属链接，但是 DEVONthink 提供了更多的链接功能，其中就包括了页码链接（Page Link）和维基（WikiLinks）。

　　Evernote 提供的笔记链接功能，是为每一个笔记都设置了一个独有的链接，通过这个链接，你可以直接在其他笔记中跳转到链接指向的笔记，另外通过这个链接你也可以直接与朋友共享这个笔记。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/BA7B6543-8A5C-46FF-AE91-1A8FC6AA9BE6.gif)

　　Evernote 通过链接共享笔记

　　DEVONthink 提供了一个类似的功能叫项目链接（Item Link），通过这个链接你也同样可以实现文件之间的跳转。默认情况下，点击项目链接后指向的笔记会在同一个窗口中打开。如果你想在新的窗口中打开，你可以右键点击项目链接，然后选择「Open Link in New Tab」。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/AB157DC1-4858-436C-A86F-098DAFDB761B.gif)

　　DEVONthink 的项目链接

　　除了与 Evernote 对标的项目链接功能，DEVONthink 在文件链接跳转的功能上更进一步，精确到了每一部分内容对应的页码位置。通过在文件中复制任意一部分内容所对应的页码链接，你就可以从其他文件中直接跳转到原文件中被复制部分的相应页码了。

　　DEVONthink 的文件链接跳转功能

　　不管是 Evernote 的笔记链接还是 DEVONthink 的项目链接和页码链接，都需要通过你的手动复制和粘贴来创建文件之间的联系，而 DEVONthink 的维基链接功能彻底跳脱出了这个限制。 如果在 DEVONthink 中某一个文件的文件名或者 Alias 在其他文件中出现了，那么在其他文件中相对应的字符将会自动变成一个链接，点击就可以跳转到相对应文件名或者 Alias 的文件，这与维基百科中的实现效果非常接近。通过这个功能，你可以在 DEVONthink 中构建出一个互相连接的知识网络，而不只是一个个独立的点。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/CC063CFB-EBC8-4EEA-BE36-928B801AF7AB.gif)

　　DEVONthink 的知识网络

　　凭借维基链接自动创建关联这个杀手锏，DEVONthink 继续建立了自己在链接这一方面对 Evernote 的领先优势。

　　资料编辑

　　在资料编辑方面，DEVONthink 的优势也是非常明显。

　　在上文中反复提到的 Evernote XML Format 一方面帮助 Evernote 构建了一个出色的富文本编辑器，但是另一方面也限制了 Evernote 的文件编辑能力。Evernote 只能编辑笔记正文的内容，包括文字、图片和表格，而对于其他格式的附件，Evernote 既无法直接在笔记正文中显示，也无法编辑。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/10F45628-CD84-4C7F-A2BF-5C3FD7816EA5.gif)

　　Evernote 无法编辑图片以外格式的附件

　　而 DEVONthink 因为它对于全格式支持的属性，所以它可以直接在应用中对 Text、RTF、Formatted Note、HTML、Markdown 和 Sheet 等各种格式的文件进行创建、编辑和预览。

　　DEVONthink 编辑支持丰富的格式

　　除了可以创建空白的新文件，DEVONthink 还可以通过模版功能创建预制好内容或者排版格式的新文件，大大提高了资料编辑的效率。模版创建和使用的具体使用方法可以参见《围绕 DEVONthink 打造我的写作工作流》一文。

　　在默认情况下，DEVONthink 会调用应用内置的编辑器来打开文件。如果你想要用第三方编辑器来打开文件，你可以右键点击文件后在「Open With」选项中选择你偏好的应用，或者在选中文件后使用快捷键 command + shift + O 直接使用系统默认的编辑器打开。而你在其他编辑器中作出的所有修改，在应用中点击保存后都会同步到 DEVONthink 中。

　　Markdown 作为一门轻量和高效的标记语言，已经成为了很多人写作的首选。说起对 Evernote 笔记编辑功能的需求，Markdown 也老是会被人们提起，但是 Evernote 至今还是没有原生支持 Markdown 语法，只能通过第三方应用，如马克飞象，来实现 Markdown 的功能。所以在这一方面，Evernote 无疑落了下风。

　　与之形成鲜明对比的是 DEVONthink 对于 Markdown 完备的支持，除了可以直接创建和编辑 Markdown 格式的文件，DEVONthink 还可以实现对于 Markdown 语法的实时预览。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/D715394F-7EFE-4590-B6B4-AD478C366D8F.jpg)

　　DEVONthink 可以实施预览 Markdown 语法

　　资料搜索

　　在资料搜索这方面，Evernote 和 DEVONthink 的表现可谓是各有千秋：Evernote 在中文搜索领域有卓越的建树，对中文用户更加友好；而 DEVONthink 凭借它的人工智能技术，在英文搜索领域有更加强大的实力和更出众的表现。

　　Evernote 的搜索功能在订阅了高级帐户的情况下才是完整的。只有订阅了高级帐户的 Evernote，你才可以搜索笔记中的图片、附件中的 Office 套件（包括 Word、PPT 和 Excel 等）和 PDF 文件中的内容。值得一提的是，作为一家以图像文字识别起家的公司，Evernote 在中国市场的本地化做得非常好，所以它对于中文搜索的支持也很完善，几乎不会出现遗漏或者错误的情况。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/38D64472-8615-4A37-BE93-2A08346DD207.png)

　　Evernote 的定价

　　DEVONthink 不需要额外的内购或者订阅，所有购买的版本都可以搜索文本类文件中的内容，但是不能直接搜索图片中的文字，只能通过 OCR 功能来间接实现这个功能。 DEVONthink 升级到 DEVONthink Pro Office 版本后内置了 OCR 功能，采用的是 ABBY Finereader 的技术，可以将图片转换为可搜索文字的 PDF 文件。你可以使用各类第三方应用扫描文档后导入 DEVONthink 然后手动启用 OCR 或者使用 Folder Action 自动触发 OCR，在 Mac 版本中你也可以调用系统自带的 Image Capture 功能直接扫描文档并启用 OCR 功能。 经过测试，DEVONthink 对于 ABBY Finereader 支持的语言经过 OCR 后的文本识别率还是很高的，当然这其中不包括中文。

　　如果你的数据库中的内容以英文资料为主，那么 DEVONthink 的搜索功能绝对可以让你放弃 Evernote，让 DEVONthink 成为你打造第二大脑独一无二的选择。 不同于 Evernote 在搜索结果中简单地罗列所有满足搜索条件的文件，在 DEVONthink 中搜索结果会根据文件内容与搜索关键词的相关性排序。首先 DEVONthink 通过扫描文件中的内容来找到所有包含搜索条件的文件，然后再凭借它的人工智能技术对这些文件的内容再做一次分析，根据内容的相关性对搜索结果匹配一个相应的分数，最后依据这个相关性分数对所有符合条件的文件做出一个排序。当你的搜索条件不够精确或者数据库非常庞大时，你很容易得到多条搜索结果，这时 DEVONthink 这个搜索结果排序功能的好处就会体现地淋漓尽致，因为你可以立即找到最有可能符合你条件的文件，而无需一个一个文件点开查看了。

![](.evernote-content/39399C87-99BB-4FBF-A253-5AE4249CCE7F/A1721656-D52A-4AAD-9DE6-698A3A7A7BF5.jpg)

　　DEVONthink 的搜索结果

　　但是，如果你的数据库以中文资料为主，那么 DEVONthink 的搜索功能对你来说就有点鸡肋了。 食之无味是因为 DEVONthink 对于文件内容的完美搜索只局限于部分语言，其中并不包括中文。虽然在 DEVONthink 中搜中文偶尔也能搜到文件中的内容的，但是问题在于**搜索成功的概率非常低，而且你完全无法预测哪些字词能搜索到哪些字词搜索不到。**

　　而弃之可惜是因为虽然 DEVONthink 搜索正文中中文内容的成功概率很低，但是当你在**搜索文件名、标签和注解中的中文时，DEVONthink 也是可以完美地找到相应的文件的。**

　　后记

　　从各个方面的比较中可以看出，DEVONthink 在**资料搜集、资料管理和文件编辑三个方面可以说是完胜 Evernote**，但是开发商对于中文市场的不够重视导致 DEVONthink  **在中文搜索方面的表现捉襟见肘**，远远低于 Evernote 所能达到的水平。

　　不过除了文中提到的四个方面，DEVONthink 擅长的**自动分组、相似推荐、词频分析、RSS 订阅、下载管理、邮件归档以及自动化功能**等进阶功能是 Evernote 所不具备的。DEVONthink 这些杀手锏进阶功能配合它优于 Evernote 的资料搜集、管理和编辑等基础功能，让我果断地放弃了限制颇多、功能迭代滞后的 Evernote，转投了 DEVONthink 的怀抱。 通过一年多的尝试和磨合，DEVONthink 已经成了我最依赖的应用之一，它管理着我所有的信息，包括收藏的文章、技术文档、个人资料、工作资料、书签、财务总结、读书笔记、Gmail 邮件等各种类型的文件，通过 iCloud 同步可以在各个客户端方便地查看和调用。

　　如果你也对尝试使用 DEVONthink 来作为你的第二大脑有兴趣，那么可以期待一下我正在筹备中的 DEVONthink 教程，希望可以帮助你更好地找到 DEVONthink 在自己工作、学习或者生活中的应用场景。

特别声明：本文为网易自媒体平台 “网易号” 作者上传并发布，仅代表该作者观点。网易仅提供信息发布平台。

---

[🌐 原始链接](http://dy.163.com/v2/article/detail/DK388DB505118DFD.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/80978efc-6f58-40bf-8980-affb8a3f2893/80978efc-6f58-40bf-8980-affb8a3f2893/)