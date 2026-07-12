# 用 Bear 来做阅读、批注与归档

---

用 Bear 来做阅读、批注与归档
=================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

你可能不相信，在 iOS 上，一直以来都没有一个工具把阅读、批注与归档这三个需求真正舒服地结合起来。

所谓舒服，在我看来至少要满足下面这四个需求：

1. 抓文效果好；
2. 能做批注，划线、高亮、评论等；
3. 这个工具本身有层级属性，可以胜任对文章的管理；
4. 最好可以把批注结果导出 PDF，方便我们直接保存。

现有的选择：Instapaper
----------------

相信各位很容易想到 [Instapaper](https://itunes.apple.com/cn/app/instapaper/id288545208?mt=8&at=10lJSw)。它抓文好、可以批注 / 评论，还有文件夹。

但首先，它的批注和评论只能留在 Instapaper 里，不能随着整篇文章一起做成 PDF 或是发到 [Evernote](https://itunes.apple.com/cn/app/evernote-stay-organized/id281796108?mt=8&at=10lJSw)。Instapaper 的层级系统也不足以让它做稍微复杂一点的内容管理。再加上它只能抓文章，我们无法输入内容，所以我们也不会真的把它当作一个内容的聚集地去处理。

尚未成器的替代品：DEVONthink To Go
-------------------------

[DEVONthink](http://www.devontechnologies.com/products/devonthink/overview.html) 是 macOS 上一款非常知名的文件管理工具，功能齐全，在 Mac 上可以把网页用单页 PDF 的形式抓下来，比多页 PDF 能够更好地保留原文格式，非常适合保存文档。

但在 iOS 上，DEVONthink 的移动版 ——[DEVONthink To Go](https://itunes.apple.com/cn/app/devonthink-to-go/id395722470?mt=8&at=10lJSw) 却没有抓文的能力，所以不得不将其放弃。

剩下的似乎没什么选择了，绝望之际我意外地发现了 [Bear](https://itunes.apple.com/cn/app/bear/id1016366447?mt=8&at=10lJSw)。

Bear 的抓文
--------

发现 Bear 是因为要准备一篇 Power+ 的文章，来对比这些笔记类的工具。在我考察 Share Sheet 的功能的时候，发现 Bear 有三种保存网页内容的方式：

* `链接`：顾名思义就是只保存网页链接
* `标题链接`：是以 Markdown 的形式，保存 标题 + 链接
* `网页内容`：就是我们需要的扒网页的功能了

在扒网页这个需求上，必须要考虑的一点是在 iPhone 端的表现如何。单纯地把网页生成 PDF 存下来，在 iPhone 上阅读就会非常辛苦。特别是在 iPhone 上我们更适合滚动的浏览方式，而不会习惯翻页的 PDF 以及因为翻页而出现的排版问题：

![](.evernote-content/200E7317-C348-4EC3-9AC9-3D819AA5E778/53B74CC9-3B4B-40BB-A9C5-61FB9AB6F47A.png)

Margin Note 抓网页后生成的 PDF 排版

Bear 因为其本身是一款笔记工具，iPhone 上的阅读体验自然不在话下 —— 你可以在设置里对 Bear 调整行高、行款、行间距、字体等，也可以修改主题：

![](.evernote-content/200E7317-C348-4EC3-9AC9-3D819AA5E778/FFB3F77C-F023-4C7C-B489-7D47EAA7DF50.png)

Bear 的阅读

从右图还可以看出，它可以对文本高亮，这就是 Bear 的批注功能。

Bear 的批注
--------

Bear 的抓文不仅是把文本图片抓下来，而且还把 HTML 的内容转化成了 Markdown 的形式。换句话说一篇文章下来之后，我们相当于拿到了它的 `.md` 文件，所以可以在其基础上自由发挥。

Bear 可以基本满足我们对批注的要求：

* 高亮：用 `::` 来前后包住文本；
* 评论：用 ```` 用 Code Block 包住评论内容就可以与原文明显区分开；
* 下划线：用 `~` 包住文本就可以作出下划线。

![](.evernote-content/200E7317-C348-4EC3-9AC9-3D819AA5E778/DCE83125-5982-4327-ABE6-C90333ED082F.png)

高亮、评论、下划线

这些大概就是我们阅读在线文章这种「不轻不重」的文章时基本的批注需求了。如果有更进一步的需求的话，首先 iPhone 可能就不适合了，这时候也自然会有更适合的工具和流程。

Bear 的整理
--------

Bear 支持多层级的标签，这与 [Pocket](https://itunes.apple.com/cn/app/pocket-save-stories-for-later/id309601447?mt=8&at=10lJSw) 在整理文章的思路上有异曲同工之妙。

在 Bear 里，标签的实现方式和微博一样，用两个井号 `#` 包住文本就是一个标签，比如 `#精读#`。这个标签会出现在 Bear 主 App 的侧栏里。

如果你想制作有层级的标签，可以通过在两个标签里插入斜线 `/` 来制作子标签。比如 `#精读/效率#` 就是在 `#精读#` 这个标签下的子标签，在 Bear 的侧栏里它会有一个折叠的效果。

Bear 的导出
--------

前些天 Bear 在 App Store 中和 [LongScreen](https://itunes.apple.com/cn/app/longscreen/id913571256?mt=8&at=10lJSw) 的工具被展示为了「长图」应用。因为 Bear 的导出功能很有特点，它可以把文本导出为一张加长的 JPG 图片，在写作 / 笔记类工具里，只有 Bear 可以做到这件事。

除了 jpg 这样的怪咖，Bear 也支持下面 5 种导出格式：`.md`、`.pdf`、`.html`、`.DOCX`、`.RTF`。足以让我们把批注好的文章，放到我们真正的文件管理工具中去。

干掉最后的 Boss：Evernote
-------------------

每当有笔记工具发布，都会有一波 Evernote 要被替代的理论。Bear 一直是其中呼声特别高的一个，在 ProductHunt [关于 Mac 上的笔记工具对比的投票](https://www.producthunt.com/ask/1529-what-s-the-best-notes-app-for-mac)里，Bear 第一名 205 票，Evernote 第二只有 99 票。

Bear 的剪藏实在是它对 Evernote 的杀手锏，特别是在 iOS 上，Evernote 的自带插件偶尔会把网页上的漂浮元素也截进来：

![](.evernote-content/200E7317-C348-4EC3-9AC9-3D819AA5E778/27FD46DF-AB38-4CD6-9524-75A3065C15FA.png)

网页上的漂浮元素

相比之下 Bear 支持 Markdown，把文章以 Markdown 形式扒下来，以 Bear 内在的主题来阅读，体验好太多。同时价格的对比也在那放着。

Evernote 在功能的深度广度上依然是或许仍然无竞品能及，但起码在 iOS 的抓文与批注的体验方面，着实输给了 Bear。

---

[#笔记应用](https://sspai.com/tag/%E7%AC%94%E8%AE%B0%E5%BA%94%E7%94%A8)[#阅读](https://sspai.com/tag/%E9%98%85%E8%AF%BB)

---

[🌐 原始链接](https://sspai.com/post/41228)

[📎 在印象笔记中打开](evernote:///view/207087/s1/3b047b04-33c9-465e-acbd-925a7cdd9c24/3b047b04-33c9-465e-acbd-925a7cdd9c24/)