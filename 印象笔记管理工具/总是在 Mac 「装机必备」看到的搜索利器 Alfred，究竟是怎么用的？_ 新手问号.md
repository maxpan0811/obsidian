# 总是在 Mac 「装机必备」看到的搜索利器 Alfred，究竟是怎么用的？| 新手问号

---

总是在 Mac 「装机必备」看到的搜索利器 Alfred，究竟是怎么用的？| 新手问号
===========================================

04月11日

[![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/860976CB-64D2-4758-BF3A-E9AF5638A6D3)](https://sspai.com/user/713147)

#### [Umi](https://sspai.com/user/713147)

目录

**编注**：「新手问号」是少数派的一个全新栏目。它面向完全「零基础」的新手用户，通过最简单易懂的方式，帮助你快速掌握关于系统和软硬件的入门知识。

---

但凡初入 Mac 的新用户，在建立起自己的工作流前，大抵都会经历一段被疯狂安利 [Alfred](http://www.alfredapp.com/ "Alfred") 的时光。这种长期口碑积累所达到的效果，也使得 Alfred 经常出现在各自 Mac 「装机必备」清单中。

什么是启动器？顾名思义，就是通过键盘输入来执行相应动作，从而提高工作效率的软件。例如 macOS 自带的聚焦搜索（Spotlight），就能将文稿、邮件、应用等整合在一起，通过关键词匹配展示。

而本文要介绍的 Alfred，也可以看成是 Spotlight 的增强版，但它更多的高级功能，比如：

* 添加自定义网络搜索引擎；
* 指定规则精准定位本地文件；
* 在命令框内使用计算器、词典等实用工具;
* ……

总之， Alfred 的一切设计都以提高效率为本，帮助你建立一套更高效的工作体系。

相对于 [LaunchBar](https://sspai.com/app/LaunchBar "LaunchBar") 等竞品，Alfred 已经足够友好，但其全英文的界面，和高级版的售价还是可能会吓退一部分新用户。但其实，Alfred 的免费功能在大多数情况已经够用了，今天，少数派就为大家带来了 Alfred 的全面上手指南，希望能帮助你摆脱不知从何下手的困境。

**注意：由于本文主要面向新手，因而尽量只介绍 Alfred 免费版的功能，不会涉及高级版功能和自定义 Workflow 的用法。如果你有类似需求，请参阅 [少数派 Alfred 专题](https://sspai.com/search/article?q=Alfred "少数派 Alfred 专题")。**

基础设置
----

上手 Alfred 的第一步，当然是配置一套更顺手的快捷键。在 Alfred 偏好设置的 General 选项卡中，你便可以依自己喜好搭配 `⌘Command`、`⌥Option`、`⇧Shift` 等修饰键，召唤 Alfred 命令框。我的选择是双击 `⌘Command` 键，一根手指就能搞定，十分方便。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/803B8F47-9831-4ADC-A017-E02CB9A42922)

如果你比较习惯使用 Spotlight 快捷键的话，可以在「系统偏好设置-键盘-快捷键-聚焦」中修改其键位，再使用 `⌘Command+空格键` 召唤 Alfred。当然，不要忘了勾选让 Alfred 开机启动哦。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/F05C88E2-3C7F-4A22-964A-FAA0EB5BEA4F)

在 General 选项卡的最下面，你可以设置自己所在的国家或地区，不同的选择会导向特定的域名。例如，在加拿大，Google 搜索的默认域名就会被改为 google.ca。这一选项在大部分情况下都无关紧要，但如果你比较依赖科学上网，我建议将其改为你梯子的物理位置，以减少链接重定向次数，加快访问速度。

快捷网页搜索
------

在阅读本节内容前，我们不妨先呼出 Alfred 的命令框，然后输入 `wiki + 任意关键词` 并回车。你应该会发现，Alfred 帮助你打开了默认浏览器并在 Wikipedia 中搜索相关词条。这，就是 Alfred 的网页搜索功能。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/7ACAEBC4-2597-4E54-9747-DE30005307D4)

接下来，让我们把目光转向第二列的 Features 选项卡。在 `Web Search` 这一栏中，你可以管理所有搜索引擎，并自定义关键词映射等，免除打开浏览器输网址的繁琐操作。

Alfred 出厂时已经预装了 Google、Twitter、YouTube 等数家国外常用网站，均可以通过输入对应的 Keyword 来调用。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/437CF0B2-F1A2-4F0B-972D-C18FBC16B901)

不过，这些国外的搜索引擎还是有点儿不接地气，如果你想搜索国内网站的话，不妨点击右下角的「Add Custom Search」按钮，定制专属于你的个性化搜索方案。

在添加之前，我们首先需要掌握搜索引擎的关键字映射规则。以少数派为例，搜索 `umi` 后打开的链接是 `https://sspai.com/search/article?q=umi`，因此，我们可以合理推断，其中的 `umi` 就是改变搜索结果的变量。为了验证这一点，我们可以再继续几组实验，确保万无一失。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/352F8BB3-51EA-4DBD-9B77-0CEA4353EFE4)

核实后，只需要打开「Add Custom Search」，在 `Search URL` 内填入上面得到的链接，再将 `umi` 换成 `{query}`，然后选择心仪的触发关键词和标题，把相关图标拖进去就大功告成了。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/53EA6990-39D1-4172-9CC2-AE5AB8D689B4)

在这里，少数派也为大家总结了数十款常用搜索引擎的 URL 规则，可以直接填充进 Alfred 的动作框内，希望能节省你的时间。

| 网站名称 | 搜索 URL |
| --- | --- |
| 少数派 | <https://sspai.com/search/article?q={query}> |
| 百度 | <https://www.baidu.com/s?wd={query}> |
| 知乎 | <https://www.zhihu.com/search?q={query}> |
| 豆瓣全站 | <https://www.douban.com/search?q={query}> |
| 豆瓣电影 | <https://movie.douban.com/subject_search?search_text={query}> |
| 简书 | <https://www.jianshu.com/search?q={query}> |
| 微博 | [https://s.weibo.com/weibo/{query}](https://s.weibo.com/weibo/%7Bquery%7D) |
| 微信文章 | <http://weixin.sogou.com/weixin?type=2&query={query}> |
| 优酷 | [https://www.soku.com/search\_video/q\_{query}](https://www.soku.com/search_video/q_%7Bquery%7D) |
| 爱奇艺 | [https://so.iqiyi.com/so/q\_{query}](https://so.iqiyi.com/so/q_%7Bquery%7D) |
| 哔哩哔哩 | <https://search.bilibili.com/all?keyword={query}> |
| 中文维基百科 | <https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=Alfred> |
| 百度百科 | <https://baike.baidu.com/search/none?word={query}&pn=0&rn=10&enc=utf8> |
| 萌娘百科 | <https://zh.moegirl.org/index.php?search={query}> |
| 淘宝 | <https://s.taobao.com/search?q={query}> |
| 京东 | <https://search.jd.com/Search?keyword={query}> |
| 什么值得买 | <http://search.smzdm.com/?s={query}> |
| DuckDuckGo | <https://duckduckgo.com/?q={query}> |
| GitHub | <https://github.com/search?q={query}> |
| Stack Overflow | <https://www.stackoverflow.com/search?q={query}> |

即使你输入的关键词没有任何匹配结果，Alfred 也会询问你是否需要搜索整个互联网。你可以在 Default Results 选项卡右下角的 `Setup fallback results` 中设置要弹出的搜索引擎候选项。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/E0B693D6-7334-4B73-9449-019B8A5B6218)

### 搜索更进一步

你可能知道，不少搜索引擎都提供了高级筛选语法，例如 `site:sspai.com` 就代表仅搜索 `sspai.com` 站内结果。因此，如果你觉得少数派原生搜索功能比较渣的话，可以试试将上面的 URL 改成 `https://www.baidu.com/s?wd=site:sspai.com%20{query}`，调用百度来帮你。如果你想了解更多支持的语法，可以自行搜索，本文仅提供一种思路作为参考。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/D1001F8D-030C-4591-B522-D11A9DEA614E)

另一个 Alfred 的小技巧是，你可以为不同的搜索引擎设置相同的 Keyword，同类网站放在一起，方便聚合查看，也降低了记不清关键词的情况发生。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/C2C9BF75-208A-4F9D-9740-87D87AE41BEE)

除了搜索外，在 Alfred 中敲入网址还可以直接启动浏览器访问网页。在 `Web Bookmarks` 选项卡中，你还可以导入 Safari 和 Chrome 中添加的书签，用最舒服的方式打开我派。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/DC2FD565-2133-44F4-89AB-816C70B19BD5)

此外，单词后跟随 `://` 的命令会被当成 [URL Schemes](https://sspai.com/post/31500 "URL Schemes")，用于打开相应 App 执行动作。Alfred 默认会保留一个月的浏览记录，你可以在 `URLs/History` 选项卡中管理。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/1683D259-B0D9-4B91-A3B6-F4CA650F2A28)

本地文件操作
------

作为 Apple 力推的重要系统功能，Spotlight 聚焦搜索一直在不断进化，在模糊识别、文件预览、多应用整合等方面甚至比 Alfred 还要出色。

那么，Alfred 的优势是什么呢？在我看来，Alfred 的设计理念是为图形操作界面加上命令行，从而达到双手不用离开键盘的理想状态。

为此，Alfred 也做出了诸多细节改进。例如，你可以通过 `⌘Command+数字键` 直接跳转至底部搜索结果；而 Spotlight 则只能用方向键一点点滚下去，比较繁琐。

相较于 Spotlight 将所有类别文件一股脑扔给你的做法，Alfred 允许你通过前缀来指定搜索结果分类。例如，只要在最开始按下空格键，Alfred 就会排除本机文件外的结果。而若想在 Spotlight 中实现这一点，就只能在系统偏好设置里一损俱损的全部取消索引了。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/1093AB6B-8113-4461-9807-949A9EED83EF)

如果你比较怀念 Spotlight 的即时预览的话，只要选中项目后按 `⇧Shift` 键，熟悉的 QuickLook 就回来了。

除了空格键外，你还可以在前面加上 `open` 以打开文件，`f` 在 Finder 中查看，`in` 搜索文档内文字，`tags` 搜索指定标签文件。以上这些快捷键，也全部支持在 Search 选项卡中调教为你喜欢的组合。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/CF6857D4-DAD7-4829-BD54-B9B44A50AAA5)

定位到所需文件后，我们往往需要对其做进一步处理，在回车打开文件前，不妨先按下 `⌥Option + ⌘Command + \`，你会发现 Alfred 已经为你准备了解压、复制、分享、查重等数项常用操作，不用在 Finder 中翻来翻去了。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/926D155F-5E2B-4DC1-83F3-38A15C8F5EF2)

最后，让我们再次回到 Alfred 设置主界面，在 Default Results 中，你可以设置 Alfred 要索引的文件位置、类型等。如果你是设计师，可以用 Alfred 管理图片素材；如果你是程序员，可以让 Alfred 只索引工作目录。如果你还是喜欢 Spotlight 的方式，只要把屏幕中间 Unintelligent 选项打钩，Alfred 就会始终显示全部类别，但对性能会有一定影响。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/93DD9DDC-6A61-4CB1-AD3D-69B03B2A849B)

其它细节功能
------

除了以上特色功能外，Alfred 还为我们提供了数种实用工具，我们不妨在本节中逐一体验。

### 计算器

计算器大概是启动器应用们的标配功能了，Alfred 也不例外。只需键入算式，Alfred 就会直接给出正确答案，直观快捷。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/D273777C-C990-444C-83CA-505C4BA81ABE)

不过，加减乘除只是入门考验，真正让 Alfred 成为神器的，是完善的函数语法支持。只要在开头加上 = 号，你就能使用包括三角、对数、指数、开方等在内的高级运算符，同时支持圆周率等数学常数，瞬间从小学进化到高中知识范围。更详细的语法介绍，你可以参考 Calculator 选项卡中的说明。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/B83F9633-C717-490B-BF9F-DDC2B1EB344C)

### 词典

在 [把查词做到极致的 macOS 原生词典，其实很好用](https://sspai.com/post/43155 "把查词做到极致的 macOS 原生词典，其实很好用") 这篇文章中，我们已经学习了怎样导入第三方词库，改善查询体验。而 Alfred 同样支持调用原生词典释义，并指定默认语言。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/B614F5BA-BC7E-4520-B55E-12F990ECE9FB)

默认情况下，你可以输入 `dic` 搜索单词，`spell` 则能够查询单词发音。当然，你也可以在 Dictionary 选项卡中更改这两个关键词。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/F96AA001-1107-4888-BDE4-7C7831517FA0)

### 通讯录

如果你使用 iCloud 或其它手段同步通讯录的话，Alfred 也会将其编入索引。只需要直接输入联系人姓名，其个人信息就一览无余，并可以快速电邮、拨号、拷贝、访问社交网络等。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/B1CD53F3-F435-442C-AEE0-AC7EE520713E)

如果你想直接向联系人发送邮件，可以输入 `email + 姓名` 试试。除了使用默认电邮地址外，你还可以在设置中勾选显示全部地址或使用 Gmail 而非原生邮件 App 撰写邮件。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/6DE87CBF-EF9A-4036-8622-CFE2D5A30CB7)

在 Contacts 的高级选项中，你可以选择将姓显示在名前，符合国人习惯。此外，你也可以勾选显示职位、称呼等，以及查找位置所使用的地图链接。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/60792B08-5AEB-4B01-8FC0-F8A0456530DC)

### 系统命令

在日常使用 Mac 的过程中，你可能会遇到这样的烦心事：安装后的 `.dmg` 卷宗依然赖在桌面上不走、某国产大厂应用又陷入了假死卡顿的轮回、出去上个厕所不想锁定 Mac 又怕别人窥屏……

而有了 Alfred，你就可以通过简单几个字符执行系统命令。`ejectall` 帮助你弹出所有挂载卷宗、`forcequit` 可以强制退出指定 App，`sleepdisplays` 则能在不睡眠的情况下关闭屏幕。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/F2DA2F31-F9B8-44A7-ADA1-D0E6F493B5D3)

在 Alfred 的 System 选项卡中，你可以概览全部支持的命令，并可以自定义呼出关键词。如果你有点担心误触，只需要取消勾选命令前的方框或要求再次确认就可以了。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/98C33BEC-4A52-4F48-B473-2CFE8794E376)

### 其它贴心细节

即使是鲜有使用的小众需求，Alfred 也给出了众多原生解决方案。你可以按下 `⌘Command + L` 居中放大显示结果，方便视力障碍者，在机场接机找人时也有奇效。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/524F7A41-BD47-49B4-B5A3-93C42414B3E1)

由于 Alfred 的大部分命令都是英文，通过快捷键呼出后往往还要再切换一下输入模式。但如果你翻一下 Advanced 选项卡，就能找到 `Force Keyboard` 选项，默认使用英文键盘。此外，你还可以在这里设置是否联想首字母、修饰键配置以及同步方式等。

![](.evernote-content/4EF808AD-EEBF-46ED-B9A9-72795B7AE1FB/55B498F9-5798-4555-B1B7-852CE84DA672)

以上，就是本文要介绍的全部内容了，如果你也想体验一下，可以在 [Alfred 官网](https://www.alfredapp.com/ "Alfred 官网") 免费下载并使用其基础功能。

此外，购买 [Powerpack](https://www.alfredapp.com/powerpack/ "Powerpack") 还会为你解锁自定义 Workflow、剪贴板管理、短语片段替换、iTunes 播放控制和 1 Password 集成等更多高级功能。少数派也会在之后为大家推出这一部分的详细介绍，敬请期待。

> 继续阅读其他「新手问号」文章：

* [iOS 效率神器 Workflow 怎么用？跟着这篇入门指南从零开始](https://sspai.com/43849 "iOS 效率神器 Workflow 怎么用？跟着这篇入门指南从零开始")
* [macOS 上都有哪些既免费、又实用的工具？](https://sspai.com/post/41477 "macOS 上都有哪些既免费、又实用的工具？")

> 拿不定主意选什么 App，下载少数派 iOS [客户端](http://sspai.com/s/nqQk "客户端")、关注 [少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，我们帮你做选择

---

[🌐 原始链接](https://sspai.com/post/43973)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b1e93386-6e73-4854-878b-71f4ea7a3c95/b1e93386-6e73-4854-878b-71f4ea7a3c95/)