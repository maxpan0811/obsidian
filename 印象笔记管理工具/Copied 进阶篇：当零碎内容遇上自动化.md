# Copied 进阶篇：当零碎内容遇上自动化

---

Copied 进阶篇：当零碎内容遇上自动化
=====================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

本文主要介绍了剪贴板管理工具 Copied 的进阶用法与工作流。

前情回顾：[顶级剪贴板该有的样子：Copied | Best Of](https://sspai.com/article/41383?series_id=9)

---

> 剪贴板犹如智能设备的血液，在系统的各个角落四通八达。它的灵活与便捷程度远超你的想象。

意识到剪贴板工具无处不在的特殊地位，我试着挖掘它们的潜力，发现用剪贴板做内容记录是一种截然不同于做笔记的体验：**随记、随用、活用**。

我尽管往剪贴板里丢东西，等需要使用时，再把它们快速变为需要的格式。比如说，自动分拣出少数派的链接、在不同的编辑器里轻松运用不同的链接格式、一键创建出整齐的任务清单…… 不一而足。

这种感觉之于使用笔记应用，就像聘请私人助理之于自己亲力亲为。这就是剪贴板工具和自动化脚本擦出的奇妙火花。在更优体验的背后，有一款改变我使用习惯的效率工具，它就是 Copied。

自动归类：Rules
----------

记录是零碎内容管理的第一步，各种笔记、剪贴板和 [shelf app](https://sspai.com/post/41370) 都在丰富记录的方式。但是收集之后，这些内容仍然需要手动整理、分类。Copied 自动把这件事做了。

#### 思考：为什么剪贴板也需要列表

备忘录有文件夹、TaskPaper 有列表…… 剪贴板同样需要。列表是高级任务管理工具的三个基本特征之一 1，是整理、定位的利器。而剪贴板有了它，就摆脱了零散杂乱的固有形象，**一来便于查找，二来可以存储常用记录，防止误删它们**。Paste 宣传其列表功能时用到了「循环使用」这个词，切中我保存常用终端命令的需求 /

而 Copied 的更优之处，就是自动归类。它采用 Rules 规则，把符合一定条件的历史记录归入指定列表。比如说，来自购物网站的链接，自动存进「剁手清单」；而 App Store 的兑换码，一经复制就会出现在「重要」列表中。

Rules 有三个种类，或复杂或简单，应对多种来源、不同格式的剪贴板记录。Rules 设置位于 Settings-Rules，由于 macOS 更开放的机制，Application Rules 是 Mac 版特有的。

### Host Name Rules

Host Name（站点名）是最简单的规则，输入一个网站的名称，选择好目标列表、保存规则。如果列表不存在，点「New List」即现场新建一个。我在写剪贴板系列文章的时候，复制了大量参考文章的链接，其中我派的文章引用得最多，质量普遍较高，还可以直接访问；为了免去手动搜索「sspai」历史记录的麻烦，我做了一个「sspai」列表专门存储少数派的文章。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/7AAB390E-60DB-4245-9501-A007231AFDC8.png)

规则非常简单，只需要填入少数派的域名 `sspai.com`，再创建对应列表，最后选择存储格式。自定义的格式本是好事，可惜 Copied 对于中文网页的支持还不够好，时会弄巧成拙，一般我直接选第一个 Plain Text，以后还可以套用格式转换。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/83A53038-7C8D-4EAF-AF7C-984BDEE510E4.gif)

找一篇少数派文章，复制它的网址，就会发现出现在相应列表里了。使用 Share Sheet 发送到 Copied 也同样可以自动归类。Copied 的列表颜色很丰富，列表名会像彩色标签一样贴在历史记录上，美观且直观。

### Regular Expression Rules

对于要求更高一点的用户，显然 Host Name Rules 是不够用的。好在 Copied 加入了 Regular Expression Rules（正则表达式规则），相信稍有了解的读者已经感觉到了它的强大。通过一定的语法，能够实现更加精确的匹配。不过这篇文章不是专门讲正则表达式的，我只会简单演示一个例子，随后提供几个现成的实用规则。

这几日我订外卖比较频繁，就创建了一个手机号码列表存储外卖员号码。他们往往是短期兼职，不必特意存进通讯录，放在剪贴板临时使用更方便。我写了一个简陋的规则 `^(\d){11}$`，意思是不含特殊符号的 11 位数字。我在生活中，一般匹配到的就是手机号码。填好规则，在 Matches 中可以看见 Text（文本）和 URL（链接）两个选项，我只需要捕捉电话号码，选 Text。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/3DAE24B3-ACAC-4BE2-AEC2-41D91D0F86BA.png)

保存规则后，运行一下试试：

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/67D630B1-64BE-416E-BAD0-7A2219996277.gif)

例子里的正则表达式非常简陋，但是应付我的临时需求足够了。下面的几条规则更为细致，读者们可以直接复制下来使用：

* 手机号码：`1[345678]\d{9}`
* 邮箱地址：`^[a-Z0-9]+([._\\-]*[a-Z0-9])*@([a-Z0-9]+[-a-Z0-9]*[a-Z0-9]+.){1.63}[a-Z0-9]+$`
* AppStore 兑换码：`^[a-Z0-9]{12}$`

可以说，有了正则表达式，Copied 就鸟枪换炮，成了一个更专业的零碎内容捕手。当然，Copied 的自动分类有多强，取决于你编写的规则多么详尽，它到底能不能成为一个称职的分拣员，就看你的了。

### Application Rules

这一规则的触发条件是剪贴板记录的来源应用，比如检测来自到 Terminal 的内容，就把它放进「命令行」列表 。不过，我主要还是把 Application Rules **作为黑名单列表使用**。

不同于前两类规则，Application Rules 还具有「Do Not Save」的操作，对于比较私密的内容，你可以选择让 Copied 忽视他们。此时系统剪贴板还是继续工作的，不影响日常使用，不过也要当心后台其他的应用读取隐私内容。我就把 iCloud 钥匙串的内容设为不存储，毕竟密码往往「用后即焚」，不希望它们长期留在剪贴板中。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/BCD1C7E5-4A00-45C2-B207-22C475619EE5.png)

格式转换：Text Formatters
--------------------

记录好内容之后，就是把它们以适当的格式粘贴到合适的地方。比较代表性的一个格式转换就是用 Markdown 格式做摘录，写博客的人常常用到。我先后使用 Drafts Templates、workflow 来满足这个需求：

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/87D3C3BA-8CD0-42F3-B033-708C6C335928.png)

这看上去很棒。不过，一个缺憾是 Drafts 只能用一种摘录模板，无法实现更多的格式；而 workflow 输出的内容需要一个专门的地方来存储，我还得跑到笔记应用里去找它。

现在我可以用 Copied 直接实现格式转换，**复制 - 存储 - 转换 - 粘贴统一在剪贴板里完成，保证灵活格式转换的同时，还大大减轻了应用间跳转的操作量。**

官方提供了丰富的模板，用户也可以自己制作。我们先来看看官方的现货，在 Settings-Text Formatters-Get More 中，罗列了许多现成模板，其中的 Quote 应该是读者最熟悉的，即 Markdown 格式的引用。而设计师朋友应该会喜欢 Color Hex to RGB，转换这两个颜色格式不用求助专门的工具或网站了。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/589355AC-8A4D-4230-A694-7872F12933DE.png)

而更进一步的需求，就得自己做模板。Copied 人性化地准备两种制作方法，简单如搭积木的 Custom Template 一学就会，稍稍复杂的 Custom Script 可以满足更客制化的需求。

### Custom Templates

Custom Template（用户模板） 其实就是将三个元素 —— 链接、标题、文本 —— 以各种形式组合起来。当你从一个网页上复制些内容下来的时候，Copied 会自动捕捉标题、链接，以便日后组合使用。

三个元素的标准写法是 `{url}`、`{title}` 和 `{text}`，它们藏在花括号中，呈蓝色字体单词。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/FEB9DF5D-6062-454D-97E0-879191B01BC9.jpg)

在写文章的时候，插入图片链接是一件繁琐的事。我以前用 Drafts 做这个工作，但是换了 Byword 之后就得手动输入那些蹩脚的符号，或者请 workflow 帮忙。但这也只能应付一种特定格式，无法满足在不同平台写作的需求。

为此，我先用 Copied Custom Template 做了一个 Markdown 格式图片链接的模板，再换个组合方式，另做一个 html 格式的模板。如此一来，我在少数派写文章的时候直接用 Markdown 格式粘上去，而需要在博客里调整图片尺寸的话，就使用 html 模板。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/5A7FFAD3-BC5B-4215-9764-2FCBB7D65A29.png)

此外，用 Custom Template 也可以满足 Markdown 格式的摘抄，模板自取：

```
>{text}  
​  
[{title}]({url})
```

在多数浏览器和适配了 Safari View Controller 的 iOS 应用中，Custom Template 都可以正常工作。所谓的「多数」，就意味着没法对付那些相对封闭的应用 —— 比如，连 Share Sheet 都不支持的微信。

### Custom Scripts

Custom Template 的应用场景显然窄了一些，一般只能做简单的拼接工作，Custom Script 则允许用户自行编写 JavaScript 脚本，实现更复杂的转换、替换和排列组合。

不熟悉脚本不要紧，把 Custom Script 想象成一个有序的工厂。它主要有三部分，一大片绿色的是注释，你不用纠结它在说什么；两段颜色丰富的，则是真正起作用的脚本。这里以一个小写转大写的 Custom Script 为例。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/733573F6-09B3-4273-B4AC-71931CCEB360.png)

工厂的原料是 clipping，也就是你打算加工的整条历史记录。Clipping 可能包含了三个元素 —— 和 Custom Template，有 url、title 和 text。

第一段的作用是验证，即判断原料中是否具有第二步所需的元素。比如 `return clipping.text != null`，就意味着需要有 text 才能进行下一步加工。有时我既需要 url，又需要 text ，那么再加一行代码来验证 url 就好。

第二段代码的作用则是精加工。这些基础的代码看起来就像口语一样易懂：

1. 从 clipping 中榨取出我需要的部分 text：`var text = clipping.text`
2. 把文本中的英文字母变成大写 big：`var big = text.toUpperCase()`
3. 返回加工后的内容 big：`return big`

我们来试试这个 Custom Script 的效果：

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/44A8A9A2-1FF3-4201-A0E6-7BBF9F372012.gif)

耶，小写的「sspai」就变成大写了。这个 Custom Script 没什么用处，我们没事为什么要转大写呢？其实，看懂这个例子，你也能写别的脚本。

你大可把 text 换成其他的元素，也能把 `toUpperCase()` 换成别的加工方法，不过这里就没法展开了。如果你对 JavaScript 感兴趣，打算花上几个周末好好学习一下，我推荐《JavaScript 经典实例》一书，里面的例子简单易懂。下面是我日常用到的另几个 Custom Script，都不复杂，你可以直接使用，也能根据自己的需求再做改进。

#### 1. 首字母大写

方才那个我自己都吐槽的大写转换，如果搭配上正则表达式实现首字母大写，就实用了不少。给文档重命名的时候，我习惯大写每个单词的首字母，一般从文中复制出代表性短句，转个格式就可以作为标题一部分了。

```
function canFormat(clipping)  
    return clipping.text != null  
​  
function format(clipping) {  
    var text = clipping.text  
    var big = text.toLowerCase().replace(/^\S/g,function(s){return s.toUpperCase();});  
    return big  
}
```

#### 2. 提取文本中的数字

有时我复制完一段话，想从里面把数字串取出来，但不想手动移动光标，就可以借助这个 Custom Script。再结合之前介绍的正则表达式，你还可以把 `/\d+/` 换成别的表达式，提取出其他内容。

```
function canFormat(clipping)  
    return clipping.text != null  
      
function format(clipping){  
    var text = clipping.text  
    var re = /\d+/  
    var number = re.exec(text)  
    return number  
}
```

#### 3. RGB 转 Hex 格式颜色

官方只提供了 Hex 转 RGB 的，不过我有时也需要查查配色的 Hex 值，所以写了一个简单的反向转换脚本，相信设计师同行们会喜欢。

```
function canFormat(clipping)  
    return clipping.text != null  
​  
function format(clipping) {  
    var rgb = clipping.text  
    var reg=/(\d{1,3}),(\d{1,3}),(\d{1,3})/  
    var arr=reg.exec(rgb)  
    function hex(a) {  
        return ("0" + parseInt(a).toString(16)).slice(-2)  
    }  
    var hexnumber = hex(arr[1]) + hex(arr[2]) + hex(arr[3])  
    var hexcolor = "#" + hexnumber.toUpperCase()  
    return hexcolor  
}
```

注：有 JavaScript 基础的读者可能会欢天喜地开始自己写函数，但是小心，我发现 Copied 最后输出时只支持自带的 format 函数，**其他名称的函数不起作用**。Format 相当于仓库门，它能直接和剪贴板交互，省去手动写代码调用系统控件的麻烦。尽可能把你的函数写在 format 里面 —— 尽管这看上去不优雅。

组合历史记录：Merge Scripts
--------------------

也许你也遇到过这样的情况：需要把通讯录里的几个号码发给同事，但是 iOS 版微信不允许换行，只能一条一条地发。在职场里，这是非常不礼貌的行为，让对方觉得你很随便，回复有一搭没一搭。

我们都更喜欢一份清清楚楚的列表。Copied 在 **Settings-Merge Scripts** 里藏着一种特殊的脚本，专门把多条历史记录组合成一个列表，并且具有多种可选的格式。我用得最多的，是自带的 References 脚本，它能够将多条链接以 Markdown 格式组合起来。我常常用这个方法给朋友发干货文章列表，对方一看标题就知道文章大概讲什么，不用全部点开看。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/ADF26570-35C1-4841-BF80-66F4DC5F01D9.gif)

在 Copied 的应用界面里，配合 Drag and Drop 一次性选好需要组合的历史记录，往屏幕下方拖移，会出现一排按钮，把刚才那堆记录拖到第三个按钮上，就能进行组合。默认只是一行一行排列，点击最下方还可以选更多格式，除了我最爱的 Reference，还有按照有序列表分段排列的 Numbered Merge、加上分割线的 Line Separator。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/71147F08-DBD9-4E5B-8C6B-BDD0D137D2FA.png)

Merge Script 也可以自行编写，不过其上手难度比 Custom Script 高了一截。我自己的需求已经满足，暂时没有遇到需要自定义的情况，如果读者有特殊的组合需求请留言告诉我。

发送到 Copied：URL Schemes
----------------------

Copied 的格式转换功能非常强大，但它毕竟是一个剪贴板，故而不具备出众的文本编辑体验。如果我想记录一段长文本，还是会采用笔记应用输入 - 发送至 Copied 的流程。这里就以 Drafts 为例，展示如何通过 URL Schemes 快速发送内容到 Copied。这里默认读者们已经有了 URL Schemes 的基础知识。

我最常用的是 Copied New Clipping，它可以往指定的 Copied 列表中添加内容，成功后跳转回笔记应用。其 x-callback-url 是：

```
copied://x-callback-url/save?title={title}&text={text}&url={url}&list={list}&x-success={success_callback}&x-error={error_callback}
```

先复制下来，移步 Drafts。左滑呼出 Action 界面，点击右上角加号添加一个 Action，于 SPEPS 中加入 URL，把刚才复制的 x-callback-url 填入 Template。

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/18A1C82A-0708-46F8-AD1D-C53CC1925E7B.png)

再根据个人需要修改 x-callback-url。其中，`title={title}`、`text={text}`、`url={url}`、`list={list}` 都是可选的，前三个显然对应了 Copied 的模板三元素，而 Drafts 里刚好也有 `[[title]]`、`[[drafts]]` 与 `{title}`、`{text}` 对应。接下来的事就方便了，我把 `[[title]]` 和 `[[drafts]]` 换上，删掉不需要的 url 部分，`list` 指定为 Copied 中已有的 quote 列表。

最后把 `{success_callback}` 改为 `drafts://`，这表示草稿如果成功发送到 Copied，就跳回 Drafts，以便继续干别的事。`x-error={error_callback}` 部分是发送不成功时自动进行的操作，我还是把它指向了 Drafts，你也可以换成自己所需动作的 URL Schemes。

保存这个动作，发送一下试试：

![](.evernote-content/3AE43315-FBC0-4E6D-973D-3AA12EE0A451/087AB2D8-5159-4E91-B0F1-E310DEDBAB17.gif)

运行良好。鉴于 Drafts 没有 macOS 版本，我想快速把一条草稿同步至电脑的话，借用一下 Copied 还是很方便的。Copied 另有其他 URL Schemes，在其设置的 [Help/FAQ](https://copiedapp.com/help/) 中可获取，实用性和可玩性兼备。

小结
--

这篇文章应读者们深入了解 Copied 的期望而写，所以充满了进阶内容，部分读者可能觉得有些阻力，可以再读读[上一篇](https://sspai.com/article/41383?series_id=9)。

本文的知识，你不光光能用到 Copied 上，还可以推衍到许多高级工具：JavaScript 脚本 Drafts 也适用，正则规则更是在许多地方发力。

醉翁之意不在酒，在上一篇文章里我真正希望提供给大家的，是选择剪贴板的标准；而这一进阶篇，则是希望读者们能学一点放之四海皆准的好东西，灵活使用脚本、URL Schemes。

如果你下载了我的模板，用得很开心，这不错；而你根据自己的需求写了一个脚本、一个 Action—— 甚至运用到别的应用里 —— 就再好不过了。

1. [列表、标签和过滤。详见 @Hum 的系列教程《用更现代的方式做任务管理》↩](#)

[#文字编辑](https://sspai.com/tag/%E6%96%87%E5%AD%97%E7%BC%96%E8%BE%91)[#Best Of](https://sspai.com/tag/Best%20Of)[#剪贴板](https://sspai.com/tag/%E5%89%AA%E8%B4%B4%E6%9D%BF)[#我的自动化](https://sspai.com/tag/%E6%88%91%E7%9A%84%E8%87%AA%E5%8A%A8%E5%8C%96)[#macOS](https://sspai.com/tag/macOS)

---

[🌐 原始链接](https://sspai.com/post/41642)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f13f3fab-7d48-4090-b0f6-ea9c8158c9fb/f13f3fab-7d48-4090-b0f6-ea9c8158c9fb/)