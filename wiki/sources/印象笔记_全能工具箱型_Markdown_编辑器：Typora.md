---
title: "全能工具箱型 Markdown 编辑器：Typora"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/全能工具箱型 Markdown 编辑器：Typora.md
tags: [印象笔记]
---

# 全能工具箱型 Markdown 编辑器：Typora

# 全能工具箱型 Markdown 编辑器：Typora --- 全能工具箱型 Markdown 编辑器：Typora ========================== | 本文为付费栏目文章，您

---

# 全能工具箱型 Markdown 编辑器：Typora

---

全能工具箱型 Markdown 编辑器：Typora
==========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

编注（@Minja）： 对于使用 Markdown 写作的人来说，主力编辑器有一款就够了，折腾太多反而舍本逐末，成了「工具控」。不过，在把 Ulysses 当作写作主力的同时，我也安装了 Typora 作为备用，偶尔需要编辑图表、扒取网页内容、上传图片时就把它拿出来。这样一款工具箱一样的编辑器，不专门写文章介绍实在可惜，于是我邀请作者 @SpencerWoo 撰写此文，带大家深入了解 Typora 这款「全能型选手」。

好工具有两种，要么某个功能刚好打动你，要么提供了丰富的备选功能乃至自定义空间，把可能性留给你；不管是哪一种，要是能满足一个额外条件那就更棒：门槛低一些。

对于 Markdown 编辑器来说也是这样的。「编辑器之争」常常在各种讨论串中上演，谈及的对象中不乏优秀之作，不过大部分 Markdown 编辑器或是价格高昂、或是界面复杂，让许多新手玩家望而却步。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/B1D92DAA-12F4-4308-8EEC-68805898A39E.png)

在这些编辑器中，国内开发者的作品 [Typora](https://www.typora.io/) 就属于第二种**「全功能」型工具**。它凭借界面简洁、功能全面且免费使用而一枝独秀，特别是「所见即所得」的渲染方式，为不少刚从 Word 等富文本编辑器过渡过来的朋友搭建了良好的桥梁。

作为一款使用场景广泛的工具，Typora 非常适合作为 Markdown 新手的入门工具，甚至在已经有其他编辑器作为主力的情况下也可以留作备用。接下来我们就从基础功能讲起，站在「全功能 Markdown 编辑器」的角度了解 Typora。

全功能 Markdown 编辑器该是什么样子
----------------------

在介绍 Typora 具体的功能之前，我们先来谈一谈什么样子的 Markdown 编辑器称得上是「全功能」的。

要是说什么能称得上 Markdown 编辑器界的集大成者，那还要从最基础的功能开始说起。对我来说，一个优秀的 Markdown 编辑器至少需要把 Markdown 该有的功能做到，同时把 Markdown 设计得不人性化的地方补足：

* **正确的渲染最基础的 [CommonMark](https://commonmark.org/) 格式的 Markdown 文本**，能支持全部的 [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) 就更好。
* **有良好的图片管理模式**。最好能拖拽放图，或者复制粘贴。如果需要手动输入图片路径，至少需要自动补全的功能。
* **有优秀的表格编辑功能**。表格是原生 Markdown 的弱项，我并不希望每次编辑表格都要在 [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) 里面写好再复制进来，这种割裂感非常影响写作体验。
* **导出格式上**，支持**导出 Markdown 渲染好的内容**为 PDF、HTML 或长图，并且支持**主题的设置**。
* **操作方式上**，支持某些格式的**快捷键**（比如多级标题、加粗、斜体等），给用户一个更个性化的操作体验。
* 支持**中文字数**的统计。
* ……

在这些功能的基础之上，诸如「打字机模式」「专注模式」「图床支持」「博客发布」等功能都算是锦上添花；与此同时，如果编辑器本身有「文件库」，或是有基于第三方云平台的同步功能，那么就是再好不过的了；更上一层楼的，如果编辑器支持「历史版本回溯」，或是类似 Git 的版本管理功能，作为用户我们就只剩欢呼了。

下面我们就一层一层地看看，Typora 到底怎样满足 Markdown 编辑中大大小小的需求。

Typora 的基础功能
------------

所谓的基础功能自然还是围绕 Markdown 展开，Typora 虽有创新，但仍然严格遵守 Markdown 语法，懂 Markdown 语法的人就能马上上手；同时它对图片、表格等 Markdown 的弱项也进行了改进，让编辑更加直观。

### What You See Is What You Mean

首先，Typora 让绝大多数用户赞不绝口的功能就是它「What You See Is What You Mean」方式的写作、渲染模式。简而言之，Typora 将「编辑」和「预览」这两个传统 Markdown 编辑器分开显示的功能合二为一了。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/BA94264B-76E6-4467-9880-19716B4B4E5F.gif)

「指哪儿打哪儿」的渲染模式，让 Typora 在很多用户心中都成了最舒服的 Markdown 编辑器。身为一名开发者，我也知道 Typora 这种模式的写作方法的代码实现要比双栏预览的形式麻烦不少。Typora 更加贴近直觉的交互方式也让它积累了很高的用户口碑。

### 标准的 Markdown 渲染

Typora 支持的是 GitHub Flavored Markdown，集成了基础的加粗、斜体、删除线、多级标题、有序与无序列表、任务列表、块引用、代码块、LaTeX 数学公式、表格、尾注、分割线、图片和目录。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/F095C2D3-A4EE-4975-A2A8-32EC482D0234.png)

和 GitHub 渲染效果几乎一致的 Typora

由于 Typora 有着对通用 Markdown 语法标准的良好支持，这意味着对于新手用户来说，简单的 GitHub Flavored Markdown 语法上手非常简单，可以暂时不学习 Typora 的专属功能或高级功能；而专业用户在标准语法的基础上也有发挥空间。

更加全面的 Markdown 语法请看：[Typora 的官方 Markdown 语法参考](http://support.typora.io/Markdown-Reference/)。

### 方便的图片插入

在 Typora 里面，插入图片非常简单。只需要一拖、一拽，图片就通过「相对路径」的方式自动引入了。我们也可以直接将图片复制粘贴进入 Typora，效果一致。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/6BD274E3-792D-4096-98AA-FF77CF15252A.gif)

拖拽插入图片

当然，很多时候我们在 Markdown 中使用图片时，都会通过「本地图片引用」或者「图片外链引用」（也就是图床）这两种方式插入图片。在「拖拽」的基础之上，Typora 还相应的优化了上面我提到的这两种方式的图片引入。

#### Typora 对本地图片的管理

对于本地图片，我个人习惯将 Markdown 文档本身和图片整理成为如下结构的文件夹：

```
.
├── <Markdown 原文稿>.md
└── image // 一个专用于放图片的文件夹
    ├── image_1.png
    └── image_2.png
```

这样的形式会让一个 Markdown 文稿对应一个专用的 `image` 文件夹，清晰直观，方便管理。同时，将 Markdown 文档以压缩包的形式发给别人的时候，图文分开的形式也方便检索。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/6B33D13D-86C7-4F3B-9606-8C01A6FA98CE.png)

很幸运，Typora 直接的支持了这种方式的图片管理。在「偏好设置 → 编辑器 → 图片插入」处，我们可以设置将拖拽或复制插入的图片，自动的「复制进入当前文件夹」或「复制到指定的文件路径」。可以看到，我个人偏好选择「复制到指定的路径」并将路径设置为 `./image`，也就是当前文件路径下 `image` 文件夹内。这样管理图片非常清晰整洁。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/21BECF1F-38AE-462C-A3A4-DE378F9CAF8A.png)

管理图片的设置

同时，如果当前文件路径下没有 `image` 文件夹，Typora 在你首次拖拽插入图片的时候也会事先询问你是否需要新建这个文件夹，非常人性化。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/4886DD14-BAE4-427C-9261-41DB3D239BA0.png)

首次拖拽时询问是否添加文件夹

#### Typora 对图床的支持

配图问题估计难倒过一片写作者，即便做好了插图、找好了图床，也往往卡在**上传**这一步。Typora 把上传图床的过程简化到了**只需一次点击**。

Typora 可以通过「编辑 → 图片工具 → 使用 iPic 上传本地图片」来将当前文档的全部本地图片上传至图床。我们也可以配置 Typora 在我们每次拖拽或复制插入图片的时候，自动通过 iPic 上传图片，并将图片路径引用自动替换为图床 URL。这样比如我们准备发布博文，需要将 Markdown 文档中引入的全部本地图片上传至图床再发表的时候，利用 Typora 进行操作就非常方便了。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/039AC1BF-77E5-4B73-97E2-DF99633B2302.png)

通过 iPic 上传图片

另外，复制粘贴网络图片的时候（比如从网页上面复制一张图片，在 Typora 中粘贴）Typora 会优先使用图片本身原有的链接。实际使用场景欢迎参考我在 Power+ 写的另一篇文章：[如何把网页制作成个性化电子书 | 实用技巧](https://sspai.com/post/54578)

有关 Typora 对图片的更多支持，请参考：[Images in Typora](http://support.typora.io/Images/)

注：目前 Typora 第三方图床支持需要 [iPic](https://itunes.apple.com/cn/app/ipic-markdown-%E5%9B%BE%E5%BA%8A-%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%B7%A5%E5%85%B7/id1101244278)，故只支持 macOS。

### 简洁的表格编辑

Typora 中对于 Markdown 表格的编辑功能**算是 Typora 一大绝对优势。**很多情况下，我在 Markdown 中创建表格都需要借助外界工具，或是查阅官方文档才能让表格的格式准确。Typora 中创建 Markdown 格式的表格则非常方便，一站式解决问题。我们通过快捷键 `Command + Alt + T` 可以快速唤起表格编辑功能，也可以通过菜单中「段落 → 表格」唤起。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/E59304D2-CC9D-4D53-9DBE-5FB97D002FDF.png)

在 Typora 中插入表格

指定行列之后，Typora 就会自动为我们创建相应的表格，我们接下来就可以通过**类似于 Word 的方式**直观的编辑表格了。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/F933A4F2-6899-4CAC-9B9F-57115DFE1BF6.png)

同时，Typora 对于 Markdown 语法支持的表格样式（比如对齐方式）都有着完善、直观的编辑方式。在表格创建之后，我们也可以通过和 Word 几乎一致的交互方式来调整表格行数和列数。这样的表格编辑方式让我们彻底告别原有简陋的、通过纯文本进行编辑的 Markdown 表格，非常友好。

### 全面的代码渲染

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/C4911C02-7BF5-4090-AB89-32615DE15F77.png)

代码渲染效果

Typora 对于代码块的渲染很全面。由于其底层是通过 CodeMirror 进行代码高亮的，因此 Typora 支持多达 106 种语言，而且无论是代码块还是行内代码，Typora 都能正确的渲染。在导出 PDF 和 ePub 的时候，渲染的代码块也能正常高亮。

需要注意的是，Typora 对代码语言的识别是区分大小写字母的。有关全部 Typora 支持的语言，请参考：[Language Support in Code Fences](http://support.typora.io/Code-Fences-Language-Support/)

### 基本 LaTeX 数学公式的支持

和输入表格一样，我们也希望在 Typora 中能直接解决数学公式的输入，少换工具。Typora 对于相当一部分的 LaTeX 内容都有着相应的支持。对于数学公式来说，我们只需要通过下面的方法唤起数学环境即可。

```
$$
... // LaTeX 数学公式
$$
```

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/13FE92C8-FB54-4F69-95BA-BA37AFA92B24.gif)

用 Typora 编辑数学公式

可以看到，Typora 对 LaTeX 数学公式的渲染也是实时的，非常直观。同时，一些相对复杂的 LaTeX 语法，比如下面图里面**用来将上下公式的「等号」对齐**的 `{align*}` 环境，Typora 同样支持。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/FE3D43B6-F377-495A-ADC1-5677D701C398.png)

试试渲染数学公式

Typora 也支持在行内插入 LaTeX 数学公式，这部分语法支持需要在「偏好设置 → Markdown → Markdown 扩展语法」里面手动开启。（同时，我们也可以开启 Typora 对上下标、高亮以及 Mermaid 语法的支持。）

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/510F40E2-677C-49E9-8C17-75C91743E008.png)

开启部分拓展语法

之后，我们就可以通过 `$ LaTeX 内容 $` 的语法插入行内数学表达式了，也可以插入一些 LaTeX 支持的特殊字符，比如 `\LaTeX` 这一经典的 LaTeX 字符等等。对于用 LaTeX 书写的化学方程式，Typora 也可以正常的渲染。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/CFA32D83-44FE-4A9B-A068-6E61FA15087C.png)

在行内渲染数学公式

有关更多 Typora 对于数学表达式等 LaTeX 内容的支持，请参考：[Math and Academic Functions](http://support.typora.io/Math/)

### 功能全面的侧边栏

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/BDAA913A-7F5C-478F-A510-24AEFA363EB9.png)

Typora 的侧边栏

Typora 的侧边栏集成了文件树、大纲两种视图，有着文件树、文档列表与目录大纲的三大功能。这三种功能里面：

* **文件树：**有列表和树两种视图
* 文档列表：仅显示打开文件夹下的全部 Markdown 文件
* 文档树：显示了包括 Markdown 文件和次级文件夹的全部内容
* **目录大纲：**就会将你正在编辑的文稿的目录进行显示，方便定位

多种展现形式的侧边栏，让我们在撰写大文章乃至一整份教程的时候，即使将文章的不同部分在多个文件中编排，利用 Typora 也能方便地管理。有些读者表示在编辑长文时编辑器会卡顿，不妨试试分成几个文档来管理。

### 字数统计

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/371CD691-3E26-491F-A8DC-CEE636ED633E.png)

中文字数统计

大多数 Markdown 编辑器都支持字数统计，但是没有做很好中文本土化的编辑器对中文字符的统计并不完美，基本没有什么参考意义。

实际上，中文统计的标杆就是 Word，原理可能不是每个人都那么关心，关键是最后统计结果要和 Word 一致或接近。Typora 的中文字数统计就比较靠近 Word，而且不仅能够统计全部的词数，还能统计字符数量、行数以及预计的阅读时间。右上角的显示也可以进行调整，来选择我们希望看到的文档字数详情。

### 其他

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/865A95AB-0EF6-4B98-9238-ADB283151653.png)

其他功能

除此之外，Typora 还支持尾注、自动添加与更新目录以及自动补全 Emoji 的功能。这些小功能让我们可以少装好多插件，在 Typora 中一站式解决问题。

Typora 的高级功能
------------

对于原生 Markdown 写作来说，Typora 在操作、中文本地化等方面做的优化已经是有目共睹。但是之所以我能称 Typora 为「全功能」的 Markdown 编辑器，更是因为下面这些 Typora 相比于其他付费或非付费的 Markdown 编辑器的所拥有的高级功能。

### 高度定制化的主题

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/F24785A3-825A-4587-80C0-D71CD8436B02.png)

自定义主题

首先一点就是 **Typora 的主题的高度可自定义化**。Typora 的全部界面都是可以**通过引入 CSS 样式表进行自定义的。**在文本编辑器界，大多数类似的 App 都会有主题的自定义功能，主题通常有两种主要的类型，我们往往会通过「Syntax Scheme」和「Color Theme」进行区分。

* **前者「Syntax Scheme」被称为「文本（语法）主题」**：这种主题往往仅仅能定义文本的高亮颜色，也就是 Markdown 编辑区域的色彩，并不能对文本编辑器的整体 UI 设计主题进行定义。
* **后者「Color Theme」被称为「色彩主题」**：我们往往称这种主题为「全局样式主题」，能够定义包括文本语法高亮和**编辑器 UI 色彩搭配**在内的全部样式。

Typora 支持的是后者。可能你已经发现了，我前面很多 Typora 的截图好像都有 Bear 的 UI 设计的身影，甚至空白页面、侧边栏等等和 Bear 几乎一致。确实，Typora 的主题就是可以定义的如此全面，我使用的 Bear 主题叫做「Ursine」，是一个开源的主题，GitHub 地址位于：[aCluelessDanny/typora-theme-ursine](https://github.com/aCluelessDanny/typora-theme-ursine)。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/28A6C0F0-952C-4E25-B828-0FBE4165D6AE.png)

仿 Bear 主题

作者本人也介绍了这个主题「受 Bear 启发」，为 Typora 自定义了字体、背景（经典的 Bear 空白页面）、强调色（Bear 红）、辅助色（侧边栏黑）等等在内的一系列色彩主题。我们在 [typora-theme-ursine/releases](https://github.com/aCluelessDanny/typora-theme-ursine/releases) 下载相应的 Release 版本压缩包，并复制到在 Typora 的主题文件夹下，在 Typora 中就可以使用了。

除此之外，Typora 还有丰富的优秀主题，我们在 [Typora Themes](http://theme.typora.io/) 这里可以找到社区提供的主题。也推荐参考 Minja 整理的《[简单又好看，你的 Markdown 文稿也能加上个性化主题](https://sspai.com/post/43873)》。

另外，自定义主题不仅可以定义「主题」，还可以实现待办事项等特殊功能。比如在 CSS 样式表中添加下面这样的代码 1，我们就可以将清单中已完成的内容划掉；如果你在写作时列了很多要点，又觉得在任务管理工具里事无巨细地添加事项有点牛鼎烹鸡，可以直接把零碎事项清单放在 Typora 里面。

```
.task-list-done {
    /* styles for completed tasks */
    text-decoration: line-through;
}
.task-list-not-done {
    /* styles for incomplete tasks */
}
```

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/BBB426DF-CC88-420C-A2D5-538FDBA4233B.png)

创建轻量级待办清单

有时候我写文章时会「灵光一现」想到一些好例子，但一时间不知道放在哪里合适，这种情况下就可以暂时把例子顺手搁在 Typora 的清单中，写完一个划掉一个，不怕漏掉灵感。

这些都是由于 Typora 优秀的架构所支撑的，虽然会牺牲部分性能，但是带来了更美丽的界面、更优秀的跨平台特性与更强的功能。

### 丰富的导出格式

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/1DFBEDBC-C60B-40BA-BDB9-EF858F557D6B.png)

Typora 丰富的导出样式

Typora 支持导出多种格式的文件，包括丰富样式的 PDF、兼容性高的 HTML，以及 Word、RTF、ePub、LaTeX、reStructuredText、Media Wiki、Textile、OPML 这些格式的内容。不仅如此，**Typora 还支持导出图片。**也就是说，我们完全可以在 Typora 中编写好我们自己设定好样式长文本，通过图片的形式进行分享，非常方便快捷。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/C598EAE9-0311-4C88-927E-1B69D5002F56.png)

导出长图

同时，Typora 渲染好的整个文稿是可以直接通过「富文本」的形式复制的，我们甚至可以直接使用 Typora 撰写好微信公众平台的文章，直接复制粘贴进入微信公众平台，我们就得到可以直接使用、发表的富文本格式的文章了。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/E1A24C67-7EF5-4233-9CEA-BEAC2DA5F673.png)

导出公众号文章

**推荐阅读：**[使用 Typora 一次性搞定公众号写作与排版](https://sspai.com/post/40524)

### 自动保存与版本控制

Typora 是支持某种形式的版本控制的，或者说是「后悔药」。对于某个文档，我们可以回溯并将文档复原到历史的某个版本，这样我们就不必连按一系列的「撤销」了。**在 macOS 平台上，Typora 集成了 macOS 内置的版本控制功能，**我们可以在「文件 → 复原到… → 浏览所有版本」来查看当前文档的全部历史版本，并回溯到我们希望恢复到的历史版本进行复原。非常方便。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/ABB65134-DD65-43BC-BB57-0B5CBFED1CB7.gif)

版本控制

在 Windows 和 Linux 平台，根据官方文档的提示，仅有 Windows 10 支持[原生的版本控制功能](https://www.pcworld.com/article/2974385/how-to-use-windows-10s-file-history-backup-feature.html)。其他的系统只有一个「当 Typora 闪退或者出现异常时的补救」的功能，在设置界面有「恢复未保存的草稿」这一功能。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/F581B60F-6DD5-47F0-881A-1768AC22FF0F.png)

闪推时恢复草稿的设置

有关版本控制的详细信息，请参考官方文档：[Version Control and Recovery](http://support.typora.io/Version-Control/)

### Mermaid 渲染引擎的支持

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/9A285830-329D-4E8E-A924-741112BAD74D.png)

Mermaid 渲染引擎

Typora 内部集成的 Mermaid 渲染引擎或许是 Typora 最强大的功能。强大的 Mermaid 渲染引擎能够让 Typora 直接渲染流程图、时序图和甘特图，同时 Typora 也支持 [js-sequence](https://bramp.github.io/js-sequence-diagrams/#syntax) 以及 [flowchart.js](http://flowchart.js.org/) 来绘制流程图和时序图的语法。

**推荐阅读：**[如何在 Markdown 里绘制各种图表 | 实用技巧](https://sspai.com/post/52993)

### 内嵌视频、音频与 `<iframe>` 格式的网页内容

Typora 支持在 Markdown 文件内部直接嵌入音频和视频等多媒体内容。

我们可以通过下面的语法嵌入视频：

```
<video src="xxx.mp4" />
```

相应的，音频内容也可以通过下面的语法嵌入：

```
<audio src="xxx.mp3" />
```

上面两个部分，`src` 对应的链接是和图片路径偏好设置一致的，往往都是本地的相对路径。

除此之外，Typora 还支持直接嵌入支持外链的 `<iframe>` 网页内容。比如 Twitter 推文、[CodePen](https://codepen.io/) 以及 [CodeSandbox](https://codesandbox.io/) 代码等等。

![](.evernote-content/7919F07F-BEC5-46C9-A94A-530EF3BA7570/3BBA8D41-DA8E-45C4-8084-C9E9E83EADBD.png)

嵌入丰富的外链内容

有关多媒体文件嵌入的详细内容，请参考官方文档：[Embed Video, Media or Web Contents](http://support.typora.io/Media/)

### 利用第三方云服务的可拓展性

由于 Typora 本身没有云服务与账户同步功能，因此我们只借助 Typora 本身一定是无法实现云同步功能的。但是借助第三方的云盘，比如 DropBox、OneDrive、坚果云等等跨平台的同步盘，我们还是可以实现「Markdown 文件」的多设备同步。

### 免费

对！目前来讲，能有 Typora 这般强大的 Markdown 编辑器，价格都不菲。由于 Typora 现在处于 Beta 阶段，因此尚未有未来的收费计划，当然，想必就算接下来 Typora 进行了某种形式的收费，其功能也会只增不减。

Typora 仍有待提高的地方
---------------

虽然前面介绍了很多 Typora 做的非常好的功能，但是不得不说 Typora 还是有一些地方目前并不完善。

### 缺少内置的标签功能

**Typora 没有标签这一概念。**当然，Typora 本身也没有文档库，所有类似「文档库」的功能都是通过「打开文件夹」的方式进行的。我们当然也没有办法通过标签对我们本地的文档进行分类，方便后期检索。这也是「开放的文件系统」与「私有的文档库」管理方式的不同。使用 Typora 的我们，可能管理文件只能靠勤劳的双手了。

### 并不优秀的内存占用

要知道，为了跨平台，Typora 的 Windows 和 Linux 版是采用 Electron 技术进行构建的 3。Electron 在业界有着并不好听的「RAM eater」称号，主要因为其内部实际上是一个 Chrome。Typora 也不例外，其内存占用确实很高，往往我打开一个或者两个窗口，Typora 的内存占用就快要赶上 Chrome 了。

当然，虽然 Typora 可能会消耗很多计算机资源，但是它为我们带来了很多内置的强大功能，包括一些我们可以自由定义的功能（比如前文提到的自定义划掉任务清单功能）。

小结
--

文章到这里就基本结束了。我们分析了 Typora 的功能、缺点以及**独占性质的绝对优势**，总体来说，Typora 作为一款免费的 Markdown 编辑器，确实是一个元老级别的「集大成者」。如果你还记得 Mou，要知道 Typora 可是和它同一个时代的产物，不同的是，Typora 仍在坚持开发着。

从 2015 年一直到今天，Typora 不仅为我们带来了全新的 Markdown 编辑体验，还为我们提供了一系列强大的功能。「所见即所得」的编辑方式让 Typora 从一众 Markdown 编辑器中脱颖而出，让小白用户不再为面对如代码般的 Markdown 而头疼。不仅如此，进入源代码模式仅需快捷键 `CMD + /`，极高的自由度让 Typora 对 Markdown 老手依旧非常友好。

Why Typora?2 因为它是目前来说，唯一一个「所见即所得」、「全功能的」Markdown 编辑器。对于 Markdown 新手玩家来说，Typora 是零成本的入门之选；而对于那些早在另一个 Markdown 编辑器里安营扎寨的高手同学来说，Typora 也完全可以作为一个备选编辑器，以解不时之需。感谢阅读。

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/56604)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0056508e-5369-43a3-9e67-5a90556481e1/0056508e-5369-43a3-9e67-5a90556481e1/)