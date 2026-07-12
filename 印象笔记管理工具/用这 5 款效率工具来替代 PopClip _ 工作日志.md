# 用这 5 款效率工具来替代 PopClip | 工作日志

---

用这 5 款效率工具来替代 PopClip | 工作日志
============================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

[PopClip](https://sspai.com/post/25483) 是一款在 macOS 上曾经很火的小工具。它的灵感来自于 iOS 上的复制粘贴菜单，当你选中一段文字后，PopClip 会在文字上方弹出分享菜单，方便你进行快捷操作。比如我们可以选中文字进行网页搜索，可以将文字发送到任务管理软件，可以修改文字的格式，统计字数等等。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/CDCFDA84-AE6D-4657-858E-447EFDF69EC5.jpg)

iOS 复制粘贴菜单和 PopClip 的分享菜单

正是因为简单快捷，PopClip 被很多人列进了「macOS 必备软件清单」，我也一度是 PopClip 的忠实用户。但是，随着对 macOS 系统的深入使用，我逐渐发现了 PopClip 的一个严重缺点 —— **影响复制操作的速度**。

具体表现为：当选中文字后快速按下复制快捷键 `⌘Command-C`，有一定的几率会复制失败。直到去到另一个 app 发现粘贴的内容是空白的，又再次回到原 app 进行重新复制。

这严重影响了操作的连贯性，也降低了操作的速度。导致那段时间我为了保险起见，每次复制都要按两次快捷键，生怕复制失败。后来经 [Umi](https://sspai.com/user/713147/posts) 提醒，这其实是 PopClip 的运行原理导致的冲突。因为 PopClip 不能直接读取选中的文本，所以需要借助系统剪贴板，先复制选中的文本，然后再读取剪贴板内容，才能获得选中的文本。

我曾经还期待这个问题什么时候能被解决，但发现这是一个从根本上 PopClip 没办法解决的事情，于是便开始寻找 PopClip 的替代品。

用这些工具来替代 PopClip
----------------

PopClip 平时处理的需求主要可以分为这两类：

1. **选中文本 / 链接发送到其它 app。**比如发送到浏览器、任务管理工具、邮件、稍后读、日记、备忘录、写作工具等。
2. **对选中的文本本身进行处理。**比如在文本两端加上引号、Markdown 加粗符号、Markdown 代码符号，或者将多行文本转换为 Markdown 列表格式，转换英文大小写，统计字数等。

**对于第一类需求，**著名启动器应用 [LaunchBar](https://www.obdev.at/products/launchbar/index.html) 的 Instant Send 功能是最好的解决方案。它同样也是先选中文本，然后通过一组快捷键（比如双击 `⇧Shift`），将文本发送到其它应用里。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/6E26F05B-E49B-4F69-8D22-6F754E5A35A3.gif)

用 Instant Send 发送文本到 Safari 进行搜索

像我之前在 PopClip 里常用的几种操作，用 Google、百度、维基百科、淘宝、亚马逊等网站来搜索选中的文本，将选中的文本发送到 Todoist、Drafts、Ulysses，都能通过 Instant Send 来实现。

首先我们需要到 LaunchBar 的「设置 - Shortcuts」里为 Instant Send 设置一组快捷键，比如设置为双击 `⇧Shift`：

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/B081A23A-2D90-444E-AFD9-E7BC9DE936AB.jpg)

为 Instant Send 设置快捷键

LaunchBar 本身已经内置了一些常用的搜索引擎（比如 Google、维基百科、亚马逊等）和第三方工具（比如 Todoist、OmniFocus、Things、Drafts、Ulysses 等，需要先安装对应的 app）。我们只需选中文字后，按下快捷键触发 Instant Send，然后选择对应的动作进行处理即可。

除了内置的搜索引擎，我们也可以自己添加百度、淘宝、豆瓣等其它网站。只需要打开 LaunchBar 的 Index 设置（快捷键为 `⌥Option-⌘Command-I`），在「Search Templates (UTF–8)」里创建新动作，将网站的搜索 URL 填进去，并将搜索关键词替换为 `*` 就可以了。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/7E5B404C-5CDA-438E-A377-4B7174BE76CC.jpg)

添加自定义搜索引擎

LaunchBar 详细的使用方法，可以参考这两篇文章：

* 契丹神童写的《[LaunchBar，加速并简化 Mac 操作的必备利器](https://sspai.com/post/36732)》
* Oscar Gong 写的《[⌘ Space：LaunchBar 的力量](https://sspai.com/post/38526)》

如果你用的是 Alfred（最近刚更新了 4.0 版本），那么可以参考《[在 Alfred 上实现 Launchbar 的 Instant Send](https://sspai.com/post/46088)》这篇文章来实现相似的效果。

**对于第二类需求，**我主要使用剪贴板管理工具 [Pastebot](https://itunes.apple.com/cn/app/pastebot/id1179623856?mt=12) 来实现。

Pastebot 中有一个叫 Filter 的功能，实际上就是对文本进行格式化处理。使用方法为：选中文本后，先进行复制，然后在 Pastebot 中选择 Filter 进行格式化，并覆盖到原文本中。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/5B646192-D568-4A8A-B644-772040918E04.gif)

用 Filter 来格式化文本.gif

Pastebot 内置了 12 种 Filter，包括查找替换、改变大小写、编码、运行 Shell Script 等，基本能够应对常见的文本处理需求。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/6EF49F54-0D33-42D1-9E17-26002CCAB4ED.jpg)

Pastebot 内置的 12 种 Filter

我自己最常用的 Filter 有：

* 在行首插入 Markdown 引用符号 `>`（支持多行文本）：

  ![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/9A5DDB65-0F95-42E6-B717-9144B97BF1AC.jpg)

  在行首插入 Markdown 引用符号
* 转换 Markdown 为 HTML：

  ![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/D51889FD-1C1B-4FE4-9304-24463098B289.jpg)

  转换 Markdown 为 HTML
* 在首尾加上 Markdown 代码块符号：

  ![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/9699B33B-2DD2-4118-8A7A-31B68F15821D.jpg)

  在首尾加上 Markdown 代码块符号
* 转换为纯文本：

  ![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/1DEC3396-89C0-4C60-B542-1721D4015D92.jpg)

  转换为纯文本
* 转换英文大小写：

  ![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/7FE74389-6361-4639-9A55-FB999773DA9F.jpg)

  转换英文大小写

如果你不是 Pastebot 的用户，也没关系，同类的剪贴板管理工具 [Copied](https://itunes.apple.com/cn/app/copied/id1026349850?mt=12)，文本替换工具 [TextExpander](https://textexpander.com/)，和自动化工具 [Keyboard Maestro](https://www.keyboardmaestro.com/)，都能实现类似的效果。

Copied 本身内置了一些文本替换模板，但如果想要自定义的话，得稍微懂点 JavaScript。Minja 也曾写过《[Copied 进阶篇：当零碎内容遇上自动化](https://sspai.com/post/41642)》（Power+ 1.0）来介绍 Copied 在格式转换方面的进阶用法。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/431D9F69-CA94-48C1-BA92-CB80C4F24E36.jpg)

Copied 里的文本替换模板

TextExpander 也是类似的思路，同样是复制文本后，使用 TextExpander 的模板进行替换，达到转换格式的效果。比如下面的这个模板，就可以为文本两边套上代码符号：

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/58D96965-4D88-41EE-81A4-A497D75C98B8.jpg)

为文本两边套上代码符号的模板

关联阅读：《[TextExpander 使用详解](https://sspai.com/post/43329)》（Power+ 1.0）

Keyboard Maestro 实现的方式也差不多，同样是复制文本后，在「Insert Text by Pasting」文本框内调整格式，最后通过快捷键或短语输出。

![](.evernote-content/22454274-165E-403D-A27C-B679E2797E0C/725C9B25-94EB-4493-99DA-4B9F3D106274.jpg)

Keyboard Maestro 的「Insert Text by Pasting」

这几款工具都可以互相替换，一般来说选择自己用得趁手的那款就行。

权衡利弊后的选择
--------

至此，PopClip 的主要功能都被我用前面提到的几款工具实现了，我自己用的组合是 LaunchBar 和 Pastebot。

但是，这个问题并没有完全被解决。准确地说，我只是复现了 PopClip 的功能，并没有复现 PopClip 的操作方式。因为 PopClip 的本质是独立通过触控板（或鼠标）来完成快捷操作，而我前面提到的方案，多多少少都得借助键盘的帮助。

在《[拓宽键盘和触控板功能的效率工具 | 我的自动化](https://sspai.com/post/42391)》（Power+ 1.0）这篇文章里，我曾提到过自己对待工具的思路是**尽量拓宽每一个设备的功能，让键盘和触控板都能独立做更多的事**。

> 因为我们总有单独使用键盘或者触控板的时候，比如我常常一只手托着下巴一只手操作触控板浏览网页，或者双手在键盘上打字。这些情况我都不愿意频繁在两个设备之间切换，尽量用当前的设备解决所有事情，保持操作的连贯性。

PopClip 总体上是一款对新手更友好的工具，拥有可视化的操作，界面也比较讨喜（容易让人联想到 iOS），能让触控板（或鼠标）更加独立。但这款工具也存在着客观的不足，严重影响了复制粘贴的效率。我只能根据现状来权衡利弊，最终选择了**重要性更高、日常使用频率也更高**的复制粘贴，舍弃 PopClip。

没有工具是完美的，所以很多人才会不断探索新的工具。但同样因为没有工具是完美的，我也应该懂得[如何对工具做出取舍，避免陷入反复纠结的状态。](https://sspai.com/post/54965)

---

[🌐 原始链接](https://sspai.com/post/55010)

[📎 在印象笔记中打开](evernote:///view/207087/s1/46e48cf7-d4f3-4668-a5f1-18c99b4537e7/46e48cf7-d4f3-4668-a5f1-18c99b4537e7/)