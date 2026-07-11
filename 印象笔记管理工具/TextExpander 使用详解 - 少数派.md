# TextExpander 使用详解 - 少数派

---

TextExpander 使用详解
=================

注：本文截图截自 TextExpander 5，目前最新的版本为 TextExpander 6，不过不影响阅读和使用。

引言
--

你是不是经常在智能设备上输入这样一些内容：

* 你的邮箱地址
* 你的电话号码
* 你的住址
* 带有某种特定模板的邮件、文本
* 一些不太好记的东西，比如学校网络的 proxy
* 日期、时间
* ⌘Command 这样前面带有一个很难输的符号的组合
* ……

这其中的一些信息，你大概已经可以靠肌肉记忆去输入了，但你肯定至少有那么一刻，觉得自己逐字输入这些经常会用的内容，是不怎么效率的事；有那么一刻，你会在心里问：都已经这个时代了，难道就没有什么方法能输这些东西的时候不那么烦吗？！

方法，有，文本替换。

2005 年 8 月 22 日，德国的一名医学生 Peter Maurer 1[发布](http://petermaurer.name/blog/?id=8)了一款文本替换软件，名为 Textpander，目的就是解决这个问题。

2006 年 5 月 24 日，Smile 软件公司从 Peter Maurer 手中[买下了 Textpander，更名为 TextExpander](https://smilesoftware.com/news/entry/textpander-gt-textexpander)，正式接管这一软件，并在多年之后，使其成为苹果生态下文本替换软件的霸主。

文本替换是怎么提高我们输入效率的呢？

比方说我在写一篇 macOS 的技巧文章，在写到快捷键的部分时，想输入 ⌘Command。这时候，我会遇到两个问题：一是这个 ⌘ 字符很难打，另一个是这个组合此后也会用很多次。这时候，通过 Textpander，进行一番设置之后，只要输入 ccmd ——bang！—— 就会弹出 ⌘Command 这一组字符。

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/815A0F70-64DC-4C36-B5D0-48E51D22857C.gif)

直至今日，这个需求已经被市场所认可，主流的操作系统都会内置文本替换的功能。但从对这个需求的理解以及配套功能的完善程度来说，和 TextExpander 相比，操作系统内置的功能只能算刚刚起步。

作为 macOS 重点生产力工具系列文章的第一篇，我将为你全面讲解 TextExpander 的功能，并且说明，为什么它的地位至今无可替代。

功能详解
----

在这个部分，我会先简单介绍 TextExpander 的基本功能，以及它和 iOS 中文本替换有什么不同。接下来，我会基于我在使用 TextExpander 中遇到的门坎儿，来谈一谈如何从不习惯使用这种工具，到把这种工具用起来。最后，我会为你介绍 TextExpander 的进阶功能，这些功能是 TextExpander 在这个领域一骑绝尘的原因。

### 基本功能与软件介绍

TextExpander 之中，一个文本替换被称为一个 Snippet（片段）。

每个 Snippet，由以下 3 个部分组成：

1. Content（缩写内容）：被缩写的内容，比如词组、公文模板、生僻符号等等；
2. Abbreviation（缩写）：被缩写的内容的替换文本，比如 ccmd @@、 uurl
3. Label（标注）：类似于一个片段的标题，告诉使用者这个片段是什么。

用邮箱地址来举一个例子：

* Content（缩写内容）：whoisyourdaddy@gmail.com
* Abbreviation（缩写）：@@
* Label（标注）：主邮箱地址

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/6838EB37-CEE6-47BB-803D-93406C91D91A.png)

TextExpander 主界面

TextExpander 比苹果的文本替换功能要多一个 Label。因为苹果的文本替换，被替换的是最简单的纯文本，它不支持换行，更没有脚本之类的内容，所以显示起来很简单。而 TextExpander 因为功能强大，所以被替换的内容未必是一行简单的纯文本，它也可以是非常长的一个邮件模板。

在主界面中，点击「Content」这一栏，你可以看到以下四个选项：

* 富文本、图片
* Applescript
* JavaScript
* Shell Script

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/59C8CF33-1115-4CC8-BE34-AB207D51E28E.png)

有这么丰富的可被缩写的内容，我们自然需要有一个备注、标题一样的东西，在边栏提示你某一个缩写它实际的本体是什么。所以，TextExpander 比苹果的文本替换多了 Label 这么一个的标注。

### 使用思路

我在最初使用 TextExpander 的时候，卡了很久没用起来，归其原因，是因为围绕缩写的一整套思路没有搞清楚，这个思路我总结了一下，是：

1. 怎么想一个忘不掉的缩写；
2. 缩写还是忘了怎么速查；
3. 该什么时候添加一个缩写；
4. 怎样尽快地添加一个缩写。

所以在写 TextExpander 的进阶功能之前，有必要把使用思路先理清楚。

#### 1. 制作缩写的思路

什么是好的缩写，仔细盘算下来，我列出了 4 点要求：

1. 容易和它代表的内容联想，好记；
2. 不会在正常打字时触发，即我们想到的缩写，正常打字的时候不能敲出来；
3. 有独一性，即缩写不能一对多；
4. 容易打出来。

什么思路能满足这四个要求呢？我们来一点点探讨一下。

满足第一点 —— 容易联想 / 好记 —— 是很容易的，比如用 cu 代替 See you，发音类似，很容易记。

但是我们马上会意识到，很多单词里面都有 cu 这个组合，比如 cube、cult 等等，我们打中文 粗、醋、促 的时候也会用到这个 cu。我们肯定不想在打这些字词的时候，都蹦出一个 See you，所以这个 cu 对第二点要求 —— 不会在正常打字时触发 —— 完成得很差，不好用。那我们又舍不得 cu 这个发音很接近的好记的缩写，该怎么办？其实只要做一些小的修改，就能解决这个问题。

这个修改的方式延伸出了不同的理解，在以英文为主的使用者那里，有一种思路是在半角符号后面跟上单词缩写。比如可以用 .cu 或者 ;cu  来作为 See you 的缩写。这么做满足了第二点要求，不会在正常打字时触发。因为在英文规范里，符号后面一般要加一个空格才能跟字母，算是从根本上解决了这个问题。但是这么做，从输入效率的角度触发，有两个问题：

1. iOS 上必须切换键盘才能输入这些半角符号；
2. 中文输入法切换全角半角符号更是麻烦。

而我正在使用的方法，是将缩写的首字母多打一次，比如用 ccu 作为 See you 的缩写。这种缩写方法解决了使用符号时会出现的两个问题。而且在实际使用上并不会造成太多误触，可以说是对缩写的 4 个要求满足得最均衡的思路。

一些实例：

|  |  |
| --- | --- |
| 缩写 | 完整内容 |
| ggtd | Get Things Done |
| aasc | AppleScript |
| uurl | URL Schemes |
| xxcal | x-callback-URL |

如果在使用过程中真的发现有误触，可以以这个思路为主，再进行一些微调。比如 AppleScript，它的缩写按道理是 aas，但是 aas 是个字幕格式，所以我给缩写后面加了一个「Script」的第二个字母 「c」，变成了 aasc，就基本上不会误触了。

这只是一个思考缩写时用到的主要思路，在不同的场景还有更多的小技巧，在接下来我为大家介绍 TextExpander 功能的时候，我会一并介绍相关的缩写思路。

一个延伸的缩写思路

URL Schemes 和 x-callback-URL 是两个我经常用到的词组，而它俩的缩写我设为了 uurl 和 xxcal。这个思路是这样的：从左到右取这个词组的前几个字母，把首字母输两次。取几个字母可以按自己喜好，不用 uurl 和 xxcal，改用 uur 和 xxca 也没问题，只要不跟其它的缩写重复就行。

#### 2. 缩写忘了怎么速查

虽然我们很精心地设计缩写思路，力求不忘。但是随着缩写的增加，写作任务的转变，一些用得越来越少的缩写还是有被忘记的可能。针对这个问题，TextExpander 有两个解决办法：

1. 当你输入已经存在 TextExpander 中的内容时，给你提示；
2. 通过快捷键，搜索缩写。

提示缩写

提示缩写这个功能在 TextExpander 的设置选项中的「Suggestions（建议）」分页：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/F14D1F23-FA26-4723-956F-20D4754F1C83.png)

设置 - Suggestions

最底部这一项「Notify me of the abbreviation when I type a snippet that already exists」就是当我们输入已经存在 TextExpander 的内容时，提示我们可以用什么缩写来帮我们节省时间。

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/2A067D71-37B4-4C3A-A8F6-38A299C09009.png)

缩写提示

搜索缩写

TextExpander 的 iOS 与 macOS 版都可以在主界面搜索，更快的方式则是通过 TextExpander 的搜索快捷键来搜索。

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/F16A9B13-5411-4979-BBD6-1A1BC57EAB38.png)

设置 - Hotkeys

图中最后两项都是搜索缩写的功能，区别在于搜索框的位置一个在光标位，一个在屏幕右上角。被选中的这一项「Inline Search」的搜索框会出现在光标处，我个人比较常用。它的快捷键我设为了 ⌘Command-⌃Control-I，「I」 取的是「Inline」的首字母。

每次输入的时候，如果想不起快捷键的话，就按下这组快捷键，搜索内容、或缩写、或 Label，都可以快速匹配到想输入的内容：

搜索 TextExpander 缩写

#### 3. 什么时候添加一个缩写

用不起来 TextExpander 这样工具的第一道坎儿是不知道怎么想一个缩写，这我们已经解决了。现在我们面对的是第二到坎儿：不知道什么时候该把一个内容以缩写的形式保存在 TextExpander 之中。

我在初期也有这个问题，每天 TextExpander 使用频率不超过 20 次，一般都是输入邮箱，很少往 TextExpander 里添加缩写。不过现在我用 TextExpander 频率已经很高，写这篇文章我还做了几个缩写。

一个内容满足了「常用」和「难输」这两个因素，就应该做一个缩写。那么多常用是常用，多难输是难输要视人而定。在我这，写一篇文章超过 3 次的特定词汇，就算常用，就会被加入到 TextExpander 里做一个缩写；像是 OmniFocus、AppleScript 这种写的时候还要按一两下 ⇧Shift 键的，就算难输，也要做缩写。

这里有一些我自己在用的缩写类型，希望可以抛砖引玉：

1) 个人信息：

我们最常用的个人信息就可以做一组缩写。不过，安全起见，不太推荐记录银行卡、信用卡的卡号。

|  |  |
| --- | --- |
| 缩写 | 完整内容 |
| ttel | 你的电话号码 |
| aaddre | 你的地址 |
| nname | 你的名字 |
| ppost | 你的邮编 |
| em1 | 邮箱地址 1 |
| em2 | 邮箱地址 2 |

这个思路可以拓展很多，比如我上学的时候还记了学校的代理，缩写是 pproxy。

2) 修饰键：

苹果的修饰键，又常用又难打，所以强烈建议用缩写来输入它们。

|  |  |
| --- | --- |
| 缩写 | 完整内容 |
| ccmd | ⌘ |
| sshift | ⇧ |
| cctrl | ⌃ |
| aalt | ⌥ |
| ccap | ⇪ |

我写作时用快捷键时，一般会把图案和按键名一起显示出来，比如 ⌘Command-C，所以我的 ccmd 出来的直接是 ⌘Command，而不是 ⌘。

3) 常用软件名：

在这里可能会有人纠结一个点是「怎么叫常用软件」，我的答案依然是：只要你发现自己写作时提了这个软件 3 次以上，你就可以把它放到缩写里了。另一方面，如果你觉得一个软件名难打，也可以加到 TextExpander 里，比如 Keyboard Maestro ，我见到它第一次我就把它做了个缩写，导致后面这个单词我到现在也没背下来。举几个我常用软件的例子：

|  |  |
| --- | --- |
| 缩写 | 完整内容 |
| ttexte | TextExpander |
| kkeym | Keyboard Maestro |
| 11p | 1Password |
| llcp | Launch Center Pro |

4) 常用命令：

休眠屏幕是我在用 iMac 时很常用的命令行 pmset displaysleepnow，这样的好处是在熄屏之后我仍然可以用 iOS 设备访问 Mac 上的文件，比如串流一下 Mac 里保存的视频，所以我也给它设了一个缩写 ssleeps。

这个缩写的思路是：命令的目的是休眠屏幕 ——Sleep Screen，所以先输入两个首字母「s」，然后按着顺序从左往右打，打到「Screen」的首字母时命令就出来了。

5) 模板类内容：

邮件、周报等等工作中要用的文件，邮件的签名，格式化的日记等，都可以（应该）用 TextExpander 来生成一个模板，来提高输入效率。邮件模板的缩写，我是以 em 开头，然后后面跟几个字母来制作缩写，后面这几个字母和发邮件的目的或对方的身份有关，比如给教授发的，是 empr。

|  |  |
| --- | --- |
| 缩写 | 实际功能 |
| empr | 给教授发的邮件模板 |
| emqj | 请假邮件模板 |
| wweekly | 周报模板 |
| ddiary | 日记模板 |

这里表格的右侧依然是实际功能，因为模板这个东西更复杂，比如请假的邮件，TextExpander 可以弹出一些常用的借口来供你选择。这些牵涉到进阶功能的，都会在后面相关的地方来说明。

6) 常用 Markdown 语法：

TextExpander 的缩写文件格式很简单，可以轻松地导入导出，所以可以常见网上有人会分享他们的 Markdown 的 TextExpander 缩写组，提供给大家下载。

但我比较建议大家自己去思考自己的缩写，我也下载过用过他们的 Markdown 缩写组，一般都是覆盖了所有的 Markdown 语法，很没有必要，而且因为缩写思路我也摸不透，所以记不全。

我在这里只列举一下我常用的并做成缩写的 Markdown 语法：

|  |  |
| --- | --- |
| 缩写 | 实际功能 |
| mmdc | 插入代码块，让光标移动到上下两行 ``` 的中间 |
| mmdf | 插入脚注，让光标移动到 ^ 后面 |
| mmdt | 输入表格的行数和列数插入一个基本表格，光标在左上角的表头 |
| qquote | 用 Markdown 的引用格式粘贴剪切板内的内容，可以多行 |
| `` | 插入行内代码，让光标移动到两个 ` 之间 |

这些 Markdown 语法的缩写都比较特殊，使用了 TextExpander 的进阶功能，所以我在这里先只写它们的实际作用，等下面提到这些功能时再做详细解释。

7) 小结

你读这个部分的时候，大概会开始尝试回忆自己打字的时候经常出现哪些组合，然后在 TextExpander 开始加缩写，我建议不要这么干。制作缩写应该是先常用，再做缩写，从实践出发，而不是倒过来。

为了方便我们尽快制作缩写，TextExpander 还有特制的功能，我们会在下一个部分来详细介绍这些功能。

#### 4. 如何尽快地添加一个缩写

养成及时添加缩写的习惯有两个重点：

1. 在写作中，有意识地去发现那些常用难输的内容，把它们做成缩写；
2. 制作缩写的过程足够顺畅，阻力小。

通过 TextExpander 提示我们添加缩写

在第一点上，除了完全靠我们自己观察自己之外，TextExpander 也会主动检测你的输入。当它发现你常输入同样内容的时候，会自动在软件里把这个内容记到一个「Suggested Snippets」的缩写组中，并弹出一个提示，来告诉你这个内容你可以做一个缩写。

但是这个功能我觉得对于中文的使用者来说不是那么实用。我们有很多同音字，于是就会用很多拼写重复的词汇，比如我写这篇文章，因为写了不少「实用」和「使用」，TextExpander 就给我加了个缩写内容「shiyong」，这很明显是乱出主意。

如果你有兴趣使用这个功能观察一下，可以在偏好设置里的「Suggestions（建议）」选项里把它打开：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/F14D1F23-FA26-4723-956F-20D4754F1C83.png)

设置 - Suggestions

上面这俩没打勾的区域的功能就是 TextExpander 这个建议功能，它们分别是：

* 「根据我的输入习惯建议缩写」
* 「通知我缩写建议」

通过快捷键添加缩写

虽说建议缩写这个功能在我看来略微鸡肋了，但是针对第二点 —— 制作缩写过程必须顺畅，TextExpander 做得非常好。

在软件偏好设置里的「Hotkeys（快捷键）」里，有一组快捷键是关于添加缩写的：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/243F0A84-23E1-4FD2-8ABE-F299C0976A50.png)

关于添加缩写的快捷键

* Create New Snippet：创建新缩写
* Create Snippet from Selection：从选中内容创建新缩写（⭐️）
* Create Snippet from Clipboard：从剪切板创建新缩写
* Edit Last Expanded Snippet：编辑上一个展开了的缩写

这四项之中，我个人只用第二项「从选中内容创建新缩写」，因为我发现在需要添加新缩写时往往我已经把这个内容打出来了，下一步只要以最快的速度给这段内容加个缩写即可，所以选中再添加我认为是最快的。

如图所示，我给它设的快捷键是 ⌃Control-⌘Command-s，s 取 Selection（选中）的首字母。

只要在写作的时候有意识地去用这个功能，相信你可以很快地把 TextExpander 的每日平均使用量提到 100 上下。

### 将文本替换的需求满足到极致

在功能介绍的一开始，我们介绍了 TextExpander 的基本功能，以及它和苹果的文本替换的区别。相信你已经了解到文本替换这一功能完成的任务是十分基础的。那么，TextExpander 把这个需求完成到了什么地步呢？我们现在就来看看。

在添加缩写界面的「Label」左边，有三个小按钮：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/0DEFCEB8-98DD-438D-BAA9-C47336D9E4AC.png)

Label 左边的按钮

这 3 个按钮里，右边的两个是在制作富文本情况下才用得上的，属于样式功能。我们要关注的是最左边的这个光标样式的按钮，它蕴含了 TextExpander 的所有自动化能力。点击它，会出现一个两级菜单，这个菜单里展示的就是 TextExpander 的真正能耐。

#### 1. 日期与时间

菜单的第一项是「插入日期」，我用 TextExpander 用得最频繁的功能之一。日报、周报之类的文章，或者某次会议记录的时间戳，都由它来完成。我们用一个实例来看看它应该如何运用：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/43ED5340-95B0-4CD7-A9D9-BA8AA643B162.png)

快速输入日期的 Snippet

* Content（缩写内容）：%Y-%m-%d
* Abbreviation（缩写）：ddate
* Label（标注）：日期

当我们在打字的时候输入 ddate，就会以 2018-02-21 的格式弹出今天的日期。

对于普通用户来说，这里不太好明白是 Content 的部分：%Y 代表 4 位数的年（2018）、%m 代表两位数的月份（02）、%d 则代表两位数字的日期（21）。中间的短横 - 是我个人喜欢的日期格式，你也可以用 / 来替换，只要把缩写内容改为 %Y/%m/%d，再输入 ddate 时，就会发现输出的结果变成了：2018/02/21。

你可能会担心自己记不住这些 Y 啊 m 啊都是代表几位数的什么，没关系，TextExpander 中给了我们提示：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/AEE51F2A-02B2-4A6B-994C-E389659F85FC.png)

使用图形界面编写 Snippet

你只要在这个菜单里选择你想加入的样式，TextExpander 会自动转化为软件能识别的格式。

时间的添加也是一样，所以在这里就不多做介绍。

更复杂的日期格式

如果想让 TextExpander 帮你输入更加复杂的日期格式，比如 2018 第一季度的财报之类会常看到的 「Q12018」，TextExpander 同样可以实现，因为它支持 Unicode Date Format Patterns，详细解释可以看官方的这篇文档：*[More Elaborate Date Formatting with TextExpander](https://smilesoftware.com/textexpander/entry/more-elaborate-date-formatting-with-textexpander)*。

日期时间加减运算

在做周报的时候，我们一般在开头会这么写个日期： 2018-02-14 ~ 2018-02-21。

我们已经把输入当天日期的效率，也就是后面一个日期解决了，我们能不能把前面这个日期也能很迅速地摆平？

在 TextExpander 中这个问题很容易解决。

首先，在 「Date/Time Math」的菜单中，选择你想做的运算（加法或减法），然后选择单位（年月日时分秒）。

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/12CF2B13-5B6E-47F4-B813-C96109274A3B.png)

日期计算

现在我们想算的是 7 天前，那么应该要选减天数，而且因为单位是天，所以应该选「Substract Day (s)」这个选项。

选择它以后，你会发现 Content 里多了一个 %@-1D，这是一个日期时间的运算前缀，TextExpander 看到这个东西，就知道「哦，我接下来是要运算日期时间了。」这个前缀里 %@ 之后的部分都是可以修改的，比如现在我们想算 7 天前的日期，就需要把里面的数字 1 改成 7，这时候你的 Content 里应该看起来是这样：%@-7D

这还没完，我们接下来要把我们希望展示的日期格式告诉 TextExpander。比如之前我们用的是 2018-02-21 这样的日期格式，它在 TextExpander 里显示的方式是 %Y-%m-%d 。所以，7 天之后是几月几日，在 Content 中的写法就是 %@-7D %Y-%m-%d。根据 TextExpander 的[官方建议](https://smilesoftware.com/textexpander/entry/textexpander-date-and-time-math)，它的缩写可以是 d7。

#### 2. 代入其它片段（Snippet）

TextExpander 允许我们把片段放到另一个片段中，这样我们就不需要在利用同一段内容时，在不同的片段中重复地编辑。

它的格式为：%snippet:片段缩写%

还拿刚才那个周报日期部分的例子，它看起来大概是这样：2018-02-14 ~ 2018-02-21 周报。前一个日期是 7 天前，后一个日期是今天。

要在 TextExpander 里做这个片段，我们可以在 Content 里直接填上 %@-7D %Y-%m-%d ~ %Y-%m-%d ，也可以直接把「今天的日期」这个片段直接放在新片段中片段中：%@-7D %Y-%m-%d ~ %snippet:ddate%。

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/533E7399-2CA8-4293-BFE2-90BC4DA23D60.png)

周报日期

更多详细的用法可以看看官方文档：*[Use Nested Snippets for External Variables in TextExpander](https://smilesoftware.com/textexpander/entry/use-nested-snippets-for-external-variables-in-textexpander)*。

#### 3. 特殊按键（Key）

TextExpander 支持在缩写中添加 4 个按键，它们分别是：

* Enter：%key:enter%
* Esc：%key:esc%
* Return：%key:return%
* Tab：%key:tab%

我最常用的是 Tab 这个按键。

我发现在输入自己邮箱之后，大多数情况下会切换一下输入框。一个典型也是最常见的情境是输入账户密码：每一次输入邮箱我都要按一下 Tab 键，那我何不让 TextExpander 帮我按这个 Tab 键呢？

所以我自己的所有邮箱地址的 Content（缩写内容），里面都会加一个 %key:tab%，比如这么写：whoisyourdaddy@gmail.com %key:tab%

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/558271B8-20C6-4A41-8F77-B9FC1CDFCDFD.png)

添加过 Tab 键的邮箱缩写

#### 4. 填空（Fill-ins）

这个功能是 TextExpander 制作模板类内容的杀手锏。它有 4 种填空的模式：

1. Single line fields：填写单行内容；
2. Multi-line fields：填写多行内容；
3. Popup menu：选择预设内容填空；
4. Optional section：填写可选项。

最后还有一个特别功能：Show at top，是把这些需要填空的部分全部堆到弹出片段的顶部去填。

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/FBBC22AF-C8FA-4E16-BCC4-D959526F6186.png)

TextExpander 的 Fill-in 功能

接下来我们就来看看在制作模板时它们都有什么作用。

1) 填写单行内容（Single line fields）

给别人写邮件的时候经常会用到这个情境，因为对方的 ID 一般只有数个字符，一行足够，不需要空出太多的位置。一般来说效果是这样的：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/1B0EE572-13D9-43D7-9B75-F1FF062F6D84.png)

Single line fields 效果

在菜单中选择「Single line fields」之后，你会发现它弹出了一个对话框：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/EA71B43F-314A-443B-BF67-24635428642C.png)

Single line fields 对话框

这个对话框有 3 个选项：

1. Field Name：区域名称
2. Default Value：默认值
3. Width：文本框（在弹出菜单中预留的）宽度

其中 Field Name（区域名称）很重要：在同一个片段中，会有多个 Field Name 相同的部分，比如我们这里可以把 Field Name 填成「客户 1」，然后这封邮件里会出现多次客户 1 的名字，这时候改任一一个客户 1 的名字，其它的名字都会一起修改。

同样的 Filed 名意为同一变量

2) 填写多行内容（Multi-line field）

填写单行内容对应的一般是一条简单的行内的内容，而多行内容一般则是一个段落，它看起来效果是：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/29328E1E-6483-4315-A9AA-54A680248CAD.png)

Multi-line fields 效果

在 TextExpander 中，选择 Multi-line field 同样会出现对话框：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/B3AEFB27-7CC5-4076-9895-70ADBC1C5396.png)

Multi-line fields 对话框

1. Area Name：区域名称
2. Default Value：默认值
3. Width：文本框（在弹出菜单中预留的）宽度
4. Height：文本框（在弹出菜单中预留的）高度

这个 Area Name 和 Field Name 完全一回事，同时前面提到的 Field Name 特有的联通属性在 Area Name 这里也同样成立。另外，因为这次不是单行而是多行，所以需要考虑一下文本框的高度（Height）问题。

这部分开始的图片使用这个功能实现了 Markdown 中的 Code Block（代码块），这样每次需要填写 Code Block 的时候，就不需要先连按六个 ` 符号，再开始写内容了。

3) 选择预设内容填空（Popup menu）

Popup Menus 可以应用的场景很广泛，比如填写货物数量、产品类别、国家地区名称、请假理由等等等等。

Single line fields 和 Multi-line fields 里填写的内容可变性比较强，比如客户名称，没办法预存，而且量大，靠选择更费时间。而那些可以局限到一定数量的内容都可以用 Popup Menus 来表示。

在 Fill-in 的二级菜单里选择「Popup menu」后，弹出来的菜单就跟刚才那俩不太一样了：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/6643A171-AE0A-49AB-A0CF-62B0223B482C.png)

Popup Menu 对话框

但是这个菜单很容易理解：通过左下角的加减符号来增删候选项，需要修改候选项内容时，双击标题的区域就可以直接修改。

4) 填写可选项（Optional section）

一般一些商品会有一些补充说明，比如「过年期间发货延迟」，这种消息不是永远都应该让用户看到的，而是在某个特定时期把它显示出来就好。这一类的内容，就可以通过这个 Optional section 来解决：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/3FA4F2F2-D9D2-49D3-8699-AC7B30C684A5.png)

过年期间发货延迟

如图所示，在这部分信息之前有个对勾，我们需要它就打上这个对勾，不需要就不勾选它。

在 Fill-in 的二级菜单里选择 Optional section 之后，同样会弹出一个对话框：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/A76264D2-48A2-4372-B8B4-8C04A173E9D7.png)

Optional section 对话框

* Optional part name：可选预设内容部分的名称，这里其实可以不勾选，否则弹出的界面看起来会比较迷惑；
* Include by default：预设内容，这次这里的预设内容很重要，需要事先填好。

5) 将填写内容置顶显示（Show at top）

前 4 个功能，是我们在制作一个模板时经常会用到的，如果一个模板足够复杂的话，我们很有可能每种方式都会用到：

* Single line fields 来填写客户姓名；
* Multi-line field 来写一些较长的段落；
* Popup menu 来填写商品名称和数量；
* Optional section 来补充一些信息。

当这些内容分布在 TextExpander 的弹出界面时，就可能会非常乱，有可能会出现漏写漏编的情况：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/4D0B6FEB-5F01-4443-A965-68FE8FD05DB7.png)

整套模板（未将待定内容上移）

但是如果我们在片段的底部加上一条 %filltop%，就可以把这些需要填写的部分全部移动到上面，挨个处理，避免遗漏：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/D36DE51B-7E85-467D-9951-C48046829D94.png)

整套模板（已将待定内容上移）

填空（Fill-in）部分的官方文档：*[Creating and Using Fill-In Fields](https://textexpander.com/help/desktop/fillins.html)*

#### 5. 光标位置（Cursor）

因为 TextExpander 多用于写文章时使用，所以光标的位置也可以拿来做文章。比如说，我自己特别常用的一个做法是在输入行内代码的时候，让我的光标自动返回到两个代码中间：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/DF50CBE9-128B-43F3-A7FE-4799BF715095.gif)

光标自动移回符号之间

制作这个 TextExpander Snippet 很简单：

* Content：`%|`
* Abbreviation：``
* Label：inline code

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/9EA5223D-71DE-4E59-8D6D-95D4ED53404E.png)

Inline Code 的片段

在 TextExpander 中，除了指定光标位置之外，还可以告诉光标在缩写展开后光标去哪，比如向上一行或向下一行，这些都可以在「Fill-in——Cursor」这个菜单中看到。

#### 6. 剪切板和图片调用

我们可以在 TextExpander 的片段中调用剪切板，还可以使用 TextExpander 直接插入图片。这两个功能都很基本，就不多聊了，有一点需要注意，是插入图片时，要把 Content 的格式从 「Plain Text（纯文本）」改为「Formatted Text, Picture（富文本、图片）」，否则 TextExpander 会把 Content 中的纯文本给做成图片发出来。

#### 7. 调用脚本

前面说到了调用图片时，需要把 Content 的格式改为富文本与图片，那么相信大家在做这个改动的时候，会发现除了纯文本富文本以外，还有脚本语言。

TextExpander 可以用脚本语言有什么用呢？在我这里有一个妙用：以 Markdown 的格式粘贴引用。

在 Slack 中聊天，经常有需要引用对方多个发言的情况，Slack 是支持 Markdown 的，所以把每一个发言的前面加上一个 > 就可以打出漂亮的引用格式：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/A80C6634-79A1-4052-A2D6-F1D4319718DD.jpg)

这个工作一开始我当然也是手输的，但当发现 TextExpander 可以运行脚本语言之后，我就请 Minja 帮我搞了一个很简单的脚本，它可以做到：在我输入缩写 —— 比如 quote—— 时，结果出来的是每一行都加上引用格式的文本。

剪切板转 MD 引用

它的代码非常简单，而且由于这个脚本是用 JavaScript 写成，我们在 iOS 版的 TextExpander 里也能使用。

var result = TextExpander.pasteboardText;

var re = /\n/g;

result = result.replace(re,"\n>");

result = ">" + result

TextExpander.appendOutput(result);

在 TextExpander 中的设置是这样：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/1E8561A3-FF23-4E64-B9F1-E182149F854C.png)

MD 引用格式的片段设置

为什么是 TextExpander
-----------------

大约两年前 2，TextExpander 从一个 Mac 上的「买断型」工具转变为一个「订阅型」的服务。当时因为没有什么明显的更新，老用户的优遇做得也不大到位，再加上是第一个「买断转订阅」的大牌工具，一时引发众怒，各路 Power User 纷纷献计，试图用各种文本替换软件，甚至本职不是文本替换软件的工具来「取代」TextExpander。

所以总结起来，「取代 TextExpander」有两个原因：

1. 认为 TextExpander 黑，如此收费不合理；
2. 认为 TextExpander 可被替代。

那么我们就从这两个角度出发，来看看事情是不是这样。

### TextExpander 黑不黑

在 TextExpander 转订阅制的时候我也是很诧异的，而且比较抵制，至今我的 TextExpander 还是买断的版本。也就是说，它转换收费模式的契机、方式和噱头，都不能打动我。但是要说它黑，有一件事让我不能同意这个观点。

iOS 的 App Store 上至今有一个 TextExpander  (Legacy)，这是 TextExpander 在 iOS 上的买断版。11 周之前，也就是在 TextExpander 转为订阅制大概 1 年半之后，这个买断版发布了一次更新，使其第三方键盘支持了 iPhone X 的屏幕尺寸。而我当时正因为键盘尺寸不合考虑转为订阅制（第 14 期的 App 奏折可考）。一个工具一年半之后还对买断版进行设备适配，这很难叫「黑」了。

更何况，macOS 上的 TextExpander 买断版仍然可以正常工作（我还是 10.13.4 Beta ），也就是说在 iOS 和 macOS 这两个平台上，TextExpander 转为订阅制之后这么久老用户都完全可以正常使用。

因此，我实在没办法从一个经济的角度来说它黑。

### TextExpander 能不能被替代

在苹果的 Power User 圈，有一位非常低调的高玩 Dr. Drang。他的博客 [And now it’s all this](http://leancrew.com/all-this/) 是标准的玩家记录型博客，写得非常实在，也给我带来过很多灵感。在 TextExpander 转订阅制之时，身为从 Textpander 时代就开始用的老用户，Dr. Drang 当天发表[博文](http://leancrew.com/all-this/2016/04/the-new-textexpander/)表示失望，并表示没什么特别的原因的话，将不会再继续使用 TextExpander。

随后在他博文里记录了自己使用 Keyboard Maestro 代替 TextExpander 的过程：

但是在去年 8 月，Dr. Drang 发了一篇文章：*[Return to TextExpander](http://leancrew.com/all-this/2017/08/return-to-textexpander/)*。在文中他提出了两点回归 TextExpander 的原因：

1. iOS 上 TextExpander 的地位无可替代；
2. TextExpander 添加新缩写的体验要比 Keyboard Maestro 更好。

这两点也是我从始至终没有切换过工具的原因，特别是第一点。当我看到讨论各种 TextExpander 替代方案的文章时，我发现所有文章都在带有倾向性地去写在 macOS 上那种蹩脚的替代方案，但很少有文章敢碰 iOS 上如何替代 TextExpander 这个话题，因为这些人明白，TextExpander 在 iOS 上确实有无法撼动的地位。

因为长期稳定、优质的表现，TextExpander 的地位已经让它成为 Evernote、1Password 一样的「第三方接入首选工具」——iOS 上的相关工具如果考虑添加文本替换功能，直接使用 TextExpander 的 SDK（Software Development Kit，软件开发工具包） 是常见的选择。

大量的 Markdown 编辑器 / 笔记工具，如 Ulysses、Byword、iA Writer、1Writer、Editorial、Drafts 都接入了 TextExpander，连 Launch Center Pro 这样的效率工具也可以让用户关联 TextExpander。

可以说，在工具界，支持 TextExpander 就像支持 1Password、支持 Evernote 一样，是一种「我很优秀」的象征。这种地位很难撼动，更遑论替代。

内容梳理及总结
-------

文本替换这么一个小小的功能，已经事实上很大的改变了我们输入的效率，各主流平台都意识到了其实用性，但它们对这个需求的探索也远不如 TextExpander 走得这么远。

在这篇文章的开始，我介绍了 TextExpander 的 Snippet（片段）以及它的三个组成部分：Content、Abbreviation 和 Label。

接着我会分享从不爱用 TextExpander 到频繁使用 TextExpander 会遇到的两个坎儿和解决方法：

1. 想不出好的缩写 —— 可以先试试输两次首字母，后面接缩写的方法；
2. 想不起来用 TextExpander—— 善用 TextExpander 的提示功能和快速添加缩写的功能。

接下来我将介绍 TextExpander 是如何把文本替换这个需求满足到极致的，它主要的介绍轨迹根据的是 TextExpander 主界面中的光标按钮弹出的两级菜单：

![](.evernote-content/2F9693CB-1279-4621-995D-60CE2062ACB2/335A6BFD-2887-4874-B171-457FEE7594A6.png)

这些功能有：

* 插入日期、时间，包括日期时间的加减
* 代入片段
* 代按特殊按键
* 填空功能（制作模板的重点功能）
* 输入缩写后改变光标位置
* 使用脚本

最后我会结合一位 TextExpander 老用户 Dr.Drang 的经历，谈一下为什么我认为目前为止 TextExpander 的地位不是那么能轻易地被撼动的。

我一个人对 TextExpander 的使用多少是有限制的，欢迎各位 Power User 在评论中分享你们对 TextExpander 的用法，传统的、另辟蹊径的都好，众人拾柴火焰高。

---

[🌐 原始链接](https://sspai.com/post/43329)

[📎 在印象笔记中打开](evernote:///view/207087/s1/61521fc4-8398-419e-8307-729575238b11/61521fc4-8398-419e-8307-729575238b11/)