# 从零开始学习 Alfred（上）：基础功能及设置

---

[少数派 从零开始学习 Alfred（上）：基础功能及设置](http://sspai.com/32979)

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/887FBB79-253A-49F8-AEA6-D46E9670D17F.jpg)

### *编注*

Alfred 是 Mac 上一款著名的效率应用，强大的功能和众多的扩展能让你在实际操作中大幅提升工作效率，少数派此前曾有多篇[关于的 Alfred 的评测和技巧](http://www.sspai.com/tag/alfred)的文章。

不少读者虽然青睐 Alfred 的高效操作，但是也因为它看起来过于复杂而不敢尝试，为了让更多对 Alfred 感兴趣的人能够真正体验到它带来的高效，这次我们将对 Alfred 内的各个功能进行详细的讲解，让你可以从零开始了解和学习这款应用。

本文于 2014 年首发在作者个人博客，经[修电脑的哲学家](http://matrix.sspai.com/user/717277)二次排版及部分内容完善，少数派已获得原作者授权转载，[点此阅读原文](http://wellsnake.com/jekyll/update/2014/06/15/001/)。

前言
--

记得以前在 Windows 平台有一个叫 Everything 的软件，主要特色就是输入关键字后能够快速得定位出你想要的文件。今天我们要介绍的 Alfred 也有和它有一样的功能。当然，如果只是简单的搜搜文件那也就称不上「神软」了。

Alfred 是一个用键盘通过热键、关键字、自定义插件来加快操作效率的工具，它不但是搜索工具，还是快速启动工具，甚至能够操作许多系统功能，扩充性极强，如果有兴趣应该还可以写一个煮咖啡的插件出来。简单点说就是使用了 Alfred 后你就可以丢掉鼠标了！

关于 Alfred 的介绍将分为上、下两篇：

* 上篇介绍 Alfred 免费版和 PowerPack 版（**需要付费购买**）的部分功能；
* 下篇着重介绍 Alfred PowerPack 的 Workflows 扩展功能，其实这才是 Alfred 可以称为神软的功能。

当然其实免费版本已经大大为我们提高了效率，不是重度用户使用免费版本也已经够用了。

下图就是 Alfred 的主界面。我们所有的操作都在这一个界面上进行。通过热键打开主界面，输入「 a 」之后 Alfred 就会为我在候选界面上显示操作系统中所有与 a 相关的文件及操作。

如果我们继续输入后续的内容，下拉选框内会动态显示候选操作。如果第一行正好是你想要的操作那么直接回车即可，同样我们也可以通过提示的热键来选择后面的操作。

我个人设置的 Alfred 的呼出快捷键为双击`Command`键。这样设置不仅呼出速度非常快，而且可以避开和其它应用的呼出快捷键冲突，例如 [Manico](http://sspai.com/32457)。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/72B65D78-08FE-44EF-8175-2A65ACED1B0B.jpg)

接下来通过 Alfred 的 Preferences（偏好设置）面板来深入了解这款应用到底有哪些神奇的功能。

General（通用）
-----------

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/4EE75775-08A0-4CE0-87A4-D99FFE114767.jpg)General 的选项很简单，只有下面三项：

* **Startup：**设置系统启动时是否自启动。
* **Alfred Hotkey：**设置呼出 Alfred 的热键。
* **Where are you：**这个设置比较特别，因为 Alfred 内置了常用网站搜索功能，在这里设置了你所在的国家后，Alfred 在搜索时会打开搜索网站对应国家的网站。

Features（特性）
------------

这里是免费版的重点，Alfred 里所有的搜索功能都在这里设置。接下来我们一一介绍：

### Default Results（默认结果）

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/09058948-9BB0-4B25-B6D1-8F8E6949778A.jpg)

* **Essentials：**可以设置搜索「应用程序」、「联系人」、「设置」、「Safari 书签」、其它的还能查询「文件夹」、「文本文件」、「压缩文件」、「图片」、「AppleScript」等其它文件。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/3504BCE4-316E-4F6F-94D5-AC9B9BD83240.jpg)

* **Search all file types：**搜索所有文件类型，不过 Alfred 建议我们可以通过 `Open + 关键字` 或者 `Space（空格键）` 来查询文件或者文件夹，因为如果全部选中的话不但影响查询速度，还容易混淆查询结果。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/5388ACCC-E03D-4F16-BC8A-0AD007F1BC55.jpg)

* **Search Scope：**设置 Alfred 查询时会搜索的文件夹，我们在这里可以自己添加和删除文件夹。
* **Fallbacks：** 是设置如果没有查到结果使用 Google 还是其它网站来搜索结果。默认反馈结果为 Google、Amazon、Wikipedia 网页搜索。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/98024B4A-3C91-43C8-BDE6-119ABA0D415F.jpg)

注：

* **检索外置移动硬盘数据**：如果需要 Alfred 也所能搜索外置移动硬盘中的文件、应用程序和元数据的话，请添加外置移动硬盘的目录或拖动文件夹到 **Search Scope**中；
* **排除 Library 文件夹**：为了保证搜索结果的准确性和相关性，建议排除应用程序文件存放位置 `~Library`；
* **检索 Chrome 书签**：Alfred 检索的书签是 Safari 中的数据，因此，如果你的主力浏览器是 Chrome 的话，则需要打开 Safari 后，通过文件→ 导入自→ 谷歌 Chrome 导入书签数据。

### File Search（文件搜索）

#### 1. Search（搜索） 选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/FF141D98-5D47-4F52-A0F0-A23BFAFFF4B0.jpg)

* **Quick Search：**快速搜索，勾选该选项后，我们可以使用`‘（单引号）`或者`Space（空格键）`快速启用打开文件或者文件夹，功能类似于使用`Open + 关键字`。
* **Opening Files：**输入`open`打开文件或者文件夹。
* **Revealing Files：**输入`find`查询文件或者文件夹的位置。
* **Inside Files：**输入`in`查找文本文件内含有查询文字的文件（这个功能很强大啊）。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/8FE950F6-4386-4846-B8BD-9B328FD0D27E.jpg)

* **File Tags：**输入`tags`查询含有查询 tags（标签） 的文件或者文件夹。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/B651F23B-EE3F-4F5F-AA98-026D0606F31D.jpg)

* **Don‘t Show：**选择查询结果中不出现「邮件」、「书签」、「音乐」、「联系人」、「历史记录」等其它文件内容（注：如果需要更为复杂的结果过滤，则需要使用自定义结果过滤的 WorkFlow ）。
* **Result Limit：**自定义显示结果个数——更多的结果意味着更大的灵活性（flexibility），而更少的结果以为这更高的性能（performance）。

#### 2. Navigation（导航）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/F06CA30C-F966-4942-95CE-8CD7E682DF67.jpg)

在这里，我们可以设置文件导航工具。我们可以使用`/`来直接定位到根目录，或者使用`~`来直接定位到当前用户的 home 目录。在文件定位工具中我们可以设置是否使用左右键来作为前进或者后退的功能键。在新版本的 Alfred 中，还增加了 Fuzzy Matching（模糊匹配）的设置项。

默认情况下，在 Alfred 中，`→` 为「显示动作面板」，`Command + ↓`为前往下一层文件夹，`Command + ↑`为前往上一层文件夹。

* **Shortcuts：** 我们可以设置使用 `←`和 `→` 为文件夹导航的快捷键，设置`return（回车键）`为在 Finder 中打开选中文件夹的快捷键。
* **Previous Path：**先前路径，在此可以设置热键（默认为`Option + Command + /`）或关键词，来快捷地访问最近一次在 Alfred 中使用文件导航访问的路径。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/9E72303C-B9BA-4C44-894D-8952B3E86D84.jpg)

#### 3. Buffer（缓存）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/00DB8E11-DF83-48F8-A38B-3B036D50F528.jpg)

这也是 Alfred 的神奇功能之一，我们可以将查找到的文件或者文件夹加入到缓存中，然后就可以对搜索到的结果作批量处理了。这里的设置也很简单，主要就是是否启用缓存功能和缓存功能的几个快捷键，并且可以设置使用完后是否清空缓存等。

* 通过`Option + ↑` 来将选中的文件夹或者文件加入到缓存，我们可以看到如果存在缓存的话 Alfred 搜索界面上会出现选中文件的小图标。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/5FD65284-3F1C-4435-8792-574FBA102951.jpg)

* 通过`Option + →`来批量处理缓存中的文件夹和文件。我们可以打开、发邮件、拷贝、移动、删除（嗯对了你是不是感觉到这个功能就是代替鼠标选中文件然后右键的功能）。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/E809DD01-F2A4-424E-975C-C45214361C92.jpg)

* 使用`Option + ↓`可以添加一个文件到缓存并移动到下一选择项。
* 使用`Option + ←`可以移除已添加的缓存项中的最后一项。

#### 4. Action（动作）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/595941EF-3000-4390-AFEE-21B2B3CC9765.jpg)

这个选项设置的功能基本和上面差不多，主要功能是在查询到文件夹或者文件后选择快捷键来显示操作界面。

另外，我们还可以在 Finder 中选中文件夹或者文件后使用快捷键来快速打开相同的操作界面。如果只是文件夹被选中的话我们可以有更多的操作可以做，比如：在 Finder 中打开文件夹、查询相似的文件、在控制台内打开文件夹、将目录拷贝粘贴板等。

* **Show Actions：**可以设置调出动作的快捷键，默认设置为 `n` 和`Control`；如果勾选 **Action Ordering** ，Alfred 则会根据你对动作的使用频次排列动作列表；
* **Default Action：**可以根据个人偏好，勾选动作；
* **File Selection：**可以设置热键（默认为 `Option + Command + /`），显示针对「当前已选文件」的「动作」面板。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/5F159A6B-F6BE-442D-9D5D-61FF288FED2D.jpg)5. Advanced（高级）选项
![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/0B233C07-F631-428E-B8DA-D46AF44D17A4.jpg)

* **Copy Path：**复制路径，选中该选项后,如果使用了将目录拷贝至粘贴板的功能后会在目录前后加上单引号。
* **Quick Look：**快速查看，选中该选项后，选中查询结果然后使用`Shift`或者是 `Command + Y`，可以使用系统的快速预览功能。
* **AppleScript：**AppleScript 脚本，选中该选项后可以使用`Command+O`来打开 AppleScript 编辑器，而 Alfred 默认的操作是直接执行脚本。
* **Performance：**在搜索外部存储文件时使用文件类型图标？（这个没有试过不知道是不是这个功能）。
* **Sorting：**这个设置应该是每次打开查询结果的文件后，更新文件的 「`kMDItemFSContentChangeDate`」 的值（具体作用不明，待 Google 之）。
* **Home Folder：**设置表示 home 文件夹字符，默认为 `~`。

### Web Search（网页搜索）

这里当然是网站搜索的一些设置，我们可以使用 Alfred 默认的一些搜索功能，或者自己设置一些自定义搜索。图中可以看到已经设置了「亚马逊中国」、「亚马逊日本」、「Google」、「百度」、「BiliBili」、「Youku」等其它自定义查询。点击 **Add Custom Search** 后我们就可以自定义查询了。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/AD50089B-16D8-45CB-8513-FFB9A68803B0.jpg)

在设置自定义查询界面中，主要设置有：

* **Search URL：**网站查询的 URL，每个网站的查询 URL 可以先通过网站查询功能，然后查看浏览器的地址栏就能知道了。当然查询内容使用 `{query}` 变量来代替。
* **Title：**标题，这个是设置在查询时 Alfred 查询主界面显示的提示文字。
* **Keyword：**查询关键字，尽量使用简短容易辨识的文字。
* **Validation：**有效性，这个是用来测试设置是否有效的。

另外每个查询设置都能设置相应网站的图标，只要将网站图标拖到设置的位置即可。在新版本的 Alfred 中，还增加了 **Use HTTPS for default searches if possible** 选项，以强化安全性。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/E74F00DB-C8FE-4C05-A55C-912E9AC25EFF.jpg)

### Calculator（计算器）

计算器这个就不多说了，主要有两个功能，一个就是直接输入简单的加减运算，一个就是输入 `=` 来输入复杂的计算，支持许多高级的数学函数。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/BBA08A30-2E69-4921-A095-D3FDE6806EEF.jpg)

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/541078A5-F860-4447-9A39-CCC1055186B7.jpg)

### Dictionary（字典）

字典功能其实使用的是 Mac 系统自带的字典，可以设置使用的字典和查询关键字，输入 di+关键字来查询中英字典

### Contacts（联系人）

#### 1. Contacts 选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/C637CEB3-38B3-4616-A458-8B3E42FE8F16.jpg)

这里我们可以设置查询到联系人后使用哪些操作，图中已经增加了点击名字拷贝到粘贴板和点击邮件地址直接发送邮件（系统默认操作），另外 Alfred 还支持 [URL Scheme](http://sspai.com/31500) 来打开任意 App 。

* 查询联系人

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/2CBC4911-D0EF-481D-B7B2-C262E5437E53.jpg)

* 联系人详细界面可以选择邮箱地址直接发送邮件

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/8463862B-14D8-476F-A4E1-B080EE7FD8B2.jpg)

#### 2. Email 选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/A0BCC00F-0102-46D6-A4C6-A8A234FEB2D6.jpg)

这里是发送邮件的选项。可以设置发送邮件的关键字，也可以设置打开 Gmail 网页来代替系统的邮件 app 来发送邮件。另外还可以设置如果有单个附件和多个附件的情况下邮件主题栏显示的文字（此功能主要是和前面文件搜索后发送邮件的功能有关）。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/5F46DCE8-1328-4AC0-95BF-F8F645B3CA5D.jpg)

#### 3. Advanced（高级） 选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/812D0F39-191F-4340-9643-7F65FFDA9DC1.jpg)

这里可以设置联系人搜索结果的展示，比如：姓和名显示顺序对调、显示职位、显示工作、如果有地图信息还能打开地图。

中文用户建议大家勾选 **Show last name before first name** 选项，这样 Alfred 就能够以中文先姓后名规则显示。

### Clipboard（剪贴板）

#### 1. History（历史）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/DBF44A92-D829-4198-AFA5-2BF55F733B24.jpg)

基于隐私的考虑，Alfred 是默认关闭「剪切板历史」功能的，我个人设置的查看「剪切板历史」的热键是`双击 Control`，方便调出；对于普通用户来说，Alfred 的剪贴板功能已经完全够用了，无需重复购买 Paste 等剪贴板管理工具。

这里是查看粘贴板历史记录的选项：

* **Clipboard Histroy：**剪切板历史，用于设置粘贴板历史保存的时间（默认为 24 小时）。
* **Viewer Hotkey：**查看热键，用于设置打开粘贴板查看器的热键。
* **Viewer Keyword：**查看关键词，用于设置打开粘贴板查看器的关键字。
* **Snippet Keyword：**片段关键词，用于设置片段查询的关键字。
* **Clear Keyword：**清空关键词，用于设置清空粘贴板历史的关键字。
* **Ignore Apps：**忽略应用程序，用于设置忽略记录至粘贴板历史的应用程序。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/5AF821FD-5295-4867-9F21-E4C0B709508E.jpg)

#### 2. Snippets（片段）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/CA78617F-F6BD-45AC-8FCC-425D58AA6C96.jpg)

此功能主要是用于设置文本片段，便于快速输入。例如，实现快速输入地址、常用问候语、常用代码片段等：

* **Name：**文本片段名称
* **Keyword：**文本片段关键字
* **Snippet：**文本片段内容

使用时可以通过打开粘贴板浏览器根据名称和关键字查询，或者直接使用前面设置的片段查询关键字来查询。

* 使用 snip 关键字查询文本片段

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/AD354654-4CC1-4F38-B14C-154819593135.jpg)

* 查询到结果后直接回车便能将片段内容输入到当前激活的应用程序内

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/2AAB7396-BF81-422D-AB8B-ECE73982BCC5.jpg)

#### 3. Merging 选项

这是一个神奇的功能：当我们复制了一段文本后，再选中另外一段文本后，通过使用 `Command ＋ 双击 C 键` 可以将当前选中的文本追加到第一次复制的文本后面。并且可以设置是使用空格、回车来分割不同的片段。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/4C7989B4-047D-41CB-9704-311B149108EB.jpg)

#### 4. Advanced（高级）选项

这里主要设置自动粘贴当前选中的记录和设置复制文本内容的最大字节。

### 2.8 iTunes

#### 1. General（通用）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/3FEF39F2-E6A4-473A-A5BC-7D224F64B2AD.jpg)

这个功能就类似一个 iTunes 的迷你播放器：

* **Mini Player：**用来设置打开迷你播放器的热键和关键字，默认为`Control + Command + Return`和 `itunes`。
* **Playback：**如果使用随机选择专辑命令，Alfred 只会选择歌曲数目大于5的专辑。
* **Behaviour：**查询并选中歌曲后自动关闭迷你播放器界面。
* **Searching：**查询歌曲后 Alfred 会自动在 iTunes 内添加播放列表。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/E82DFD06-D001-4DB7-9903-545F120869AF.jpg)

#### 2. Keywords（关键字）选项

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/DC049672-BE33-4CC4-80EF-9F8E1710E632.jpg)

这里主要用于设置 iTunes 播放命令的关键字。主要有：

* **Play/Pause（播放/暂停）：**`play/pause`
* **Next Track（下一曲）：**`next`

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/3F44FC27-930D-4FA9-B696-050F4C8992FD.jpg)

* **Previous Track（上一曲）：**`previous`
* **Random Album（随机选择专辑）：**`random`

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/94CBAC61-2D00-4E0D-8A9E-67C3415CC168.jpg)

* **Max Volume（最大音量）：**`volmax`
* **Half Volume（一半音量）：**`volmid`
* **Mute iTunes（静音）：**`mute`

另外，选中了 **Show these keywords in Alfred Default Results**后不但可以在迷你播放器内使用这些命令还能在搜索界面内使用以上命令。

#### 3. Advanced（高级）选项

这里主要设置 iTunes 的资料库目录，如果 Alfred 没有找到我们可以手动设置。另外 Alfred 还能查询不在 iTunes 资料库内的歌曲。我们还可以设置 Alfred 在 iTunes 内的播放列表的名称。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/8DD34343-4964-4A99-8DD9-8FD06ACBCDAE.jpg)

### 1Password

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/0FD2A16A-8AB9-448C-BF54-0D659C4DB90E.jpg)

如果你购买了 [1Password](http://www.sspai.com/tag/1Password) 这个 Mac 上的密码管理应用的话，我们就可以直接在 Alfred 内直接搜索密码库了。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/5C5CB892-2E98-448E-83DA-6852022E052C.jpg)

不过需要注意的是如果 Alfred 显示 **Unable to find 1Password Data**的话我们需要打开 1Password 的**启用与第三方应用整合**这个选项。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/17BBF48A-4D79-408A-97CA-6FC8FDCD8774.jpg)

### System（系统）

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/1EA76BC4-C6E6-4A8D-BBD3-147F7492E683.jpg)

这里主要是设置一些系统命令的关键字。建议将一些常用的系统命令、程序管理命令、盘符管理命令设置为剪短好记的语词。例如，我将「清空回收站」的关键字设置为`em`，将「推出所有盘符」的关键字设置为`tui`。

* **常规系统命令：**屏幕保护程序（`screen saver`）、显示回收站（`trash`）、清空回收站（`empty trash`）、登出（`logout`）、睡眠（`sleep`）、锁定（`lock`）、重启（`restart`）、关机（`shutdown`）。
* **程序管理命令：**隐藏（`hide`）、关闭（`quit`）、强制关闭（`forcequit`）、关闭所有应用程序（`quitall`）。
* **盘符管理命令：**推出某个盘符（`eject`）、推出所有盘符（`ejectall`）、设置盘符黑名单。

### Terminal/Shell（终端和 Shell ）

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/C36F522A-0D37-4459-A59F-EBF42DEE8FD7.jpg)

Alfred 还能输入控制台命令。这里设置比较简单了，设置输入命令的关键字和使用的默认控制台程序。

![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/3EC0DC64-6131-4310-A0F7-D5F437BA833E.jpg)

好了，终于把上篇 Alfred 的基本功能全都说个了遍，基本上没有啥遗漏的功能了。如果能掌握上面所有的功能的话已经能够减少大部分的鼠标操作和重复性操作，将大大提高操作系统使用效率。

**关联阅读：**

* [《5 款提高文件处理效率的 Alfred 扩展》](http://sspai.com/32680)
* [《4 款「本地化」的 Alfred 扩展分享》](http://sspai.com/32281)
* [《OS X 效率启动器 Alfred 详解与使用技巧》](http://sspai.com/27900)
* [《OS X 效率启动器 Alfred 的 5 个实用扩展推荐（一）》](http://sspai.com/27854)
* [《OS X 效率启动器 Alfred 的 5 个实用扩展推荐（二）》](http://sspai.com/27929)
* [《OS X 效率启动器 Alfred 的最佳伴侣：Alfred Remote for iOS 上手详解》](http://sspai.com/28137)

文章来源 [少数派](http://sspai.com) ，原作者 [wellsnake](http://sspai.com/author/718367) ，转载请注明原文链接

原文可获取应用下载链接：[从零开始学习 Alfred（上）：基础功能及设置](http://sspai.com/32979)   
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime   
少数派（ <http://sspai.com> ）

[![](.evernote-content/86711D51-302D-41E7-A655-48E0F839A669/1EF07038-A53F-4444-A177-14EE0F2CEA7D.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:buyAW/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fwatch%2Fbuy%2F)

  
  
  
<http://sspai.com/32979>

Sent with [Reeder](http://reederapp.com)

发自我的 iPhone

[📎 在印象笔记中打开](evernote:///view/207087/s1/d7f43b6d-da72-4fb6-98b1-7957096f4a39/d7f43b6d-da72-4fb6-98b1-7957096f4a39/)