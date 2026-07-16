---
title: "LaTeX（排版系统）_百度百科"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/LaTeX（排版系统）_百度百科.md
tags: [印象笔记]
---

# LaTeX（排版系统）_百度百科

# LaTeX（排版系统）_百度百科 --- LaTeX（排版系统）\_百度百科 ================= : LaTeX ===== （排版系统） ------ [编辑](#) [锁定](

---

# LaTeX（排版系统）_百度百科

---

LaTeX（排版系统）\_百度百科
=================

:   LaTeX
    =====

    （排版系统）
    ------

    [编辑](#)
    [锁定](https://baike.baidu.com/view/10812319.htm "锁定")

LaTeX（LATEX，音译 “拉泰赫”）是一种基于 ΤΕΧ 的排版系统，由美国计算机学家莱斯利・兰伯特（Leslie Lamport）在 20 世纪 80 年代初期开发，利用这种格式，即使使用者没有排版和程序设计的知识也可以充分发挥由 [TeX](https://baike.baidu.com/item/TeX/3794463) 所提供的强大功能，能在几天、甚至几小时内生成很多具有书籍质量的印刷品。对于生成复杂表格和[数学公式](https://baike.baidu.com/item/%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F/10349953)，这一点表现得尤为突出。因此它非常适用于生成高印刷质量的科技和数学类文档。这个系统同样适用于生成从简单的信件到完整书籍的所有其他种类的文档。[1]

中文名
:   拉泰赫

外文名
:   LaTeX

属    性
:   排版系统

开发者
:   美国计算机学家莱斯利・兰伯特

开发时间
:   20 世纪 80 年代

适用范畴
:   大型论文排版和数学公式输入

释义
--

[编辑](#)

【**正式名称**】：LATEX

【**纯文本名称**】：LaTeX

【**概述**】

LaTeX 使用 [TeX](https://baike.baidu.com/item/TeX) 作为它的格式化引擎，当前的版本是 LaTeX2ε。

Leslie Lamport 开发的 LaTeX 是当今世界上最流行和使用最为广泛的 TeX 宏集。它构筑在 Plain TeX 的基础之上，并加进了很多的功能以使得使用者可以更为方便的利用 TeX 的强大功能。使用 LaTeX 基本上不需要使用者自己设计命令和宏等，因为 LaTeX 已经替你做好了。因此，即使使用者并不是很了解 TeX，也可以在短短的时间内生成高质量的文档。对于生成复杂的数学公式，LaTeX 表现的更为出色。LaTeX 自从八十年代初问世以来，也在不断的发展。最初的正式版本为 2.09，在经过几年的发展之后，许多新的功能，机制被引入到 LaTeX 中。在享受这些新功能带来的便利的同时，它所伴随的副作用也开始显现，这就是不兼容性。标准的 LaTeX 2.09 引入了 “新字体选择框架”(NFSS) 的 LaTeX、SLiTEX，AMS-LaTeX 等等，相互之间并不兼容。这给使用者和维护者都带来很大的麻烦。为结束这种糟糕的状况，FrankMittelbach 等人成立了 ATeX3 项目小组，目标是建立一个最优的、有效的、统一的、标准的命令集合。即得到 LaTeX 的一个新版本 3. 这是一个长期目标，向这个目标迈出第一步就是在 1994 年发布的 LaTeX2e。LaTeX2e 采用了 NFSS 作为标准，加入了很多新的功能，同时还兼容旧 LaTeX 2.09。LaTeX2e 每 6 个月更新一次，修正发现的错误并加入前，LaTeX2e 将是标准的[2]
。

历史
--

[编辑](#)

### TeX 格式

最基本的 [TeX](https://baike.baidu.com/item/TeX) 程序只是由一些很原始的命令组成，它们可以完成简单的排版操作和程序设计功能。然而，TeX 也允许用这些原始命令定义一些更复杂的高级命令。这样就可以利用低级的块结构，形成一个用户界面相当友好的环境。

在处理器运行期间，该程序首先读取所谓的格式文件，其中包含各种以原始语言写成的高级命令，也包含分割单词的连字号安排模式。接着处理程序就处理源文件，其中包含要处理的真正文本，以及在格式文件中已定义了的格式命令。

创建新格式是一件需要由具有丰富知识的程序员来做的事情。把定义写到一个源文件中，这个文件接着被一个名叫 iniTeX 的特殊版本的 TeX 程序处理。它采用一种紧凑的方式存贮这些新格式，这样就可以被通常 TeX 程序很快地读取。

### Plain TeX

Knuth 设计了一个名叫 PlainTeX 的基本格式，以与低层次的原始 TeX 呼应。这种格式是用 TeX 处理文本时相当基本的部分，以致于我们有时都分不清到底哪条指令是真正的处理程序 TeX 的原始命令，哪条是 PlainTeX 格式的。大多数声称只使用 TeX 的人，实际上指的是只用 PlainTeX。

PlainTeX 也是其它格式的基础，这进一步加深了很多人认为 TeX 和 PlainTeX 是同一事物的印象。

PlainTeX 的重点还只是在于如何排版的层次上，而不是从一位作者的观点出发。对它的深层功能的进一步发掘，需要相当丰富的编程技巧。因此它的应用就局限于高级排版和程序设计人员。

### 1 LaTeX

Leslie Lamport 开发的 LaTeX 是当今世界上最流行和使用最为广泛的 TeX 宏集。它构筑在 Plain TeX 的基础之上，并加进了很多的功能以使得使用者可以更为方便的利用 TeX 的强大功能。使用 LaTeX 基本上不需要使用者自己设计命令和宏等，因为 LaTeX 已经替你做好了。因此，即使使用者并不是很了解 TeX，也可以在短短的时间内生成高质量的文档。对于生成复杂的数学公式，LaTeX 表现的更为出色。

LaTeX 自从八十年代初问世以来，也在不断的发展。最初的正式版本为 2.09，在经过几年的发展之后，许多新的功能，机制被引入到 LaTeX 中。在享受这些新功能带来的便利的同时，它所伴随的副作用也开始显现，这就是不兼容性。标准的 LaTeX 2.09，引入了 “新字体选择框架”(NFSS) 的 LaTeX，SLiTEX，AMS-LaTeX 等等，相互之间并不兼容。这给使用者和维护者都带来很大的麻烦。为结束这中糟糕的状况，Frank Mittelbach 等人成立了 LaTeX3 项目小组，目标是建立一个最优的、有效的、统一的、标准的命令集合。即得到 LATEX 的一个新版本 3。这是一个长期目标，向这个目标迈出第一步就是在 1994 年发布的 LaTeX2e。LaTeX2e 采用了 NFSS 作为标准，加入了很多新的功能，同时还兼容旧的 LaTeX 2.09。LaTeX2e 每 6 个月更新一次，修正发现的错误并加入一些新的功能。在 LaTeX3 最终完成之前，LATEX2e 将是标准的 LATEX 版本。

### 2 AMS-TeX/AMS-LaTeX

AMS-TeX 是美国数学会提供的，在 Plain TeX 基础上开发的 TeX 宏集。它主要用于排版含有很多数学符号和公式的科技类文章或书籍。AMS-TeX 给出了许多高级命令，可以让使用者很方便地排版大型的、复杂的数学公式。AMS-TeX 排版数学公式等的功能通过 AMS-LaTeX 中的宏包 amsmath 在 LaTeX 中得到实现。AMS-TeX 最新版本为 2.1。

AMS-LaTeX 包括两部分，一是上面提到的 amsmath 宏包，主要的目的是用来排版数学符号和公式。另一部分是 amscls，提供了美国数学会要求的论文和书籍的格式。AMS-LaTeX 目前的版本为 2.0。在提供 AMS-TeX 和 AMS-LaTeX 的同时，美国数学会还提供一套数学符号的字库，AMSFonts。这套字库中增加了很多 TeX 的标准字库 Computer Modern 所没有的一些数学符号，粗体数学符号等。AMSFonts 现在的版本为 2.2，有 Metafont 和 Type1 两种字库提供下载。

### 3 TeX 和 LaTeX 的关系

LaTeX 是 TEX 中的一种格式 (format) ，是建立在 TeX 基础上的宏语言，也就是说，每一个 LaTeX 命令实际上最后都会被转换解释成几个甚至上百个 TeX 命令。但是，普通用户可以无需知道这中间的复杂联系。就像编程的时候如果使用一些已经编译好的函数库和模板可以使我们仅仅用几个命令就实现很多功能一样，LaTeX 根据人们排版文章的习惯，定义了许多命令和模板，通过这些命令和模板，我们可以很快的得到漂亮的排版结果。

### 4 LaTeX 2.09 和 LaTeX2e 的区别

LaTeX 2.09 是 LaTeX 在 LaTeX2e 之前的一个版本（参见问题 6）。LaTeX2e 对 LaTeX 2.09 做了很大的改进，增加了很多新功能。从文件内容上看，两者最显著的不同在于 LaTeX 2.09 使用 \documentstyle 命令定义文档类型以及所包含宏包，如 \documentstyle [twoside,epsfig]{article}

而 LaTeX2 使用 \documentclass 命令定义文档类型，用 \usepackage 命令包含宏包，如

|  |  |
| --- | --- |
| 1  2 | `\documentclass[twoside]{article}`  `\usepackage{epsfig}` |

如果你使用的不是几十年前的老机器，你的系统的 LaTeX 都是 LaTeX2

![](.evernote-content/64869C41-5FAF-4620-827D-27C02F3678CE/F5AF8117-2985-4D5A-97B6-8AED40F637E0.png)

版本。LaTeX 2.09 文件一般都可以在 LaTeX2

![](.evernote-content/64869C41-5FAF-4620-827D-27C02F3678CE/F5AF8117-2985-4D5A-97B6-8AED40F637E0.png)

系统中以兼容方式编译。但是兼容方式编译速度慢，而且很多 LaTeX2

![](.evernote-content/64869C41-5FAF-4620-827D-27C02F3678CE/F5AF8117-2985-4D5A-97B6-8AED40F637E0.png)

的新功能无法使用。如果你不是需要编译以前的 LaTeX 2.09 文件，你根本无需使用 LaTeX 2.09 ，也不用知道 LaTeX 2.09 与 LaTeX2

![](.evernote-content/64869C41-5FAF-4620-827D-27C02F3678CE/F5AF8117-2985-4D5A-97B6-8AED40F637E0.png)

的差别。大部分 LaTeX 2.09 文件都可以通过用 \documentclass 命令和 \usepackage 命令代替 \documentstyle 命令修改为 LaTeX2

![](.evernote-content/64869C41-5FAF-4620-827D-27C02F3678CE/F5AF8117-2985-4D5A-97B6-8AED40F637E0.png)

格式。有时可能需要一些特殊宏包，例如 latexsym ，对旧的 LaTeX 2.09 命令提供支持。

### 5 MiKTeX、fpTeX、teTeX、CTeX 的关系

TeX 在不同的硬件和操作系统上有不同的实现版本。这就像 C 语言，在不同的操作系统中有不同的编译系统，例如 Linux 下的 gcc，Windows 下的 Visual C++ 等。有时，一种操作系统里也会有好几种的 TeX 系统。目前常见的 Unix/Linux 下的 TeX 系统是 Texlive，Windows 下则有 MiKTeX 和 fpTeX。CTeX 指的是 CTeX 中文套装的简称，是把 MiKTeX 和一些常用的相关工具，如 GSview，WinEdt 等包装在一起制作的一个简易安装程序，并对其中的中文支持部分进行了配置，使得安装后马上就可以使用中文。

### 6 LaTeX 文件的框架

|  |  |
| --- | --- |
| 1  2  3  4 | `\documentclass{article}`  `\begin{document}`  `This is the body of the article`  `\end{document}` |

第一句：\documentclass [选项]{类}，确定整篇文章的处理格式，期刊或者会议论文一般可选类为 article，再附上控制全局格式的选项，比如字体、字号、页面格式、纸张大小等等。也有期刊直接提供[类模板](https://baike.baidu.com/item/%E7%B1%BB%E6%A8%A1%E6%9D%BF)，比如 Lecture Notes in Computer Science，只要把相应的类名放到 {类} 里就 OK 了，不需要自己去费神。老版本此处使用 \documentstyle。

接下来是包含一些使用的宏包来增强功能，\usepackage {宏包}，宏包包含在.sty 文件中，用过的宏包有：CJK 支持中文环境；times TIMES 字体；graphicx 插图；pyperref 引用超链接。也有期刊提供宏包来定制格式，比如 IEEE Computer Society Press。感觉就像 C 语言里的 #include 一样为第三方提供接口。有些提供的样例文件中在 documentclass 的选项中添加宏包，这是与老版本兼容。

以上为导言区，接着余下的都是正文部分，包含在 \begin {document} 和 \end {document} 内。LaTeX 命令的作用对象和范围和 HTML 的标签有点类似，有开始和结束标志，开始位置内会定义一些表现格式。导言区还可能有 \pagestyle {选项}，页面样式，比如 empty 选项表示没有页眉和页脚。导言区还有其它全局性的设置等。

正文部分首先是文章标题 \title {标题}，然后是作者信息 \author {作者信息}。其中作者信息多行表示，用 \\ 断行，自动居中。多个作者用 \and 连接，自动按格式分列横排或者居中竖排。接着是日期 \date {日期}，如果不写这条命令缺省为当前日期。可以使用 \maketitle 表示本页为标题页，以便自动格式化。

接着是文章正文内容各部分了。摘要 \begin {abstract}...\end {abstract}，或者直接 \abstract。章节为 \section {第一层标题}，\subsection {第二层标题}，\subsubsection {第三层标题}(注意：没有 \subsubsubsection {第四层标题} 这样的命令)。

再后面是参考文献部分，用过两个方法。第一个方法是手工逐条在正文尾部的 \begin {thebibliography}{最大条数}... \end {thebibliography} 内加入 “\bibitem {关键词} 文献信息”，文章中引用的地方用 \cite {关键词}，自动按加入的顺序编号，形如 [1]。第二个方法是使用 bibTex。建立一个文献数据库文件：数据库名.bib，里面有按字段填写的文献信息，以及相应的 “引用关键词”。 bibTex 会生成.bib 文件，其中包含引用文献具体内容，在正文末尾用 \bibliography {文献数据库名} 包含该文件内容，注意文献数据库名不能包含空格。文章中引用格式同前面的方法，文献数据库中被引用的文献按格式出现在文末，未被引用的文献可以使用 \nocite {关键词} 来使其出现在文末。后一种方法的好处有：一、文献数据库可以共享；二、文献的内容与表现格式分离，内容填写更清晰，也可以更好的控制格式比如文献的排列顺序。格式控制是在导言区加入 \bibliographystyle {格式名}，其中格式包含在.bst 文件里，可以是 LaTeX 提供的，也可以是期刊单位提供的。

从结构上看，文章算排版结束了。下面就文章正文内容的一些细节留些注意点。

插图：使用 graphicx 宏包很方便引用.eps 格式图片，个人一般图片都是 Matlab 绘制图片，可以直接输出 eps 格式。特别地，PS 的 eps 不行。图片一般集中放当前目录下子目录中，使用子目录在导言中用 \graphicspath {{子目录名 /}}，这个里面的 {} 不能少，图片文件名被引用时即可省略子目录名，指明.eps 时效率高。

表格：表格单元都是由内容撑起的，可以使用 \rule [起始位置]{宽度}{高度} 来撑起达到预期格式。rule 定义的是一个矩形，起始位置指底线与当前行基准线的距离，负值表示底线在基准线下面。

插图、表格、公式都可以贴上各自自动编号的标签 \label {关键词}，引用时 \ref {关键词} 可以自动出现相应编号。

文章排版好了，输出文档需要注意几点。按照导言区格式设置，编译生成 dvi 作为中间预览基本不会有问题，但一般都需要最终 pdf 输出。

### 7 简单的规则

（1）空格：LaTeX 中空格用来隔开单词 (英语一类字母文字)，多个空格等效于一个空格；对中文没有作用。

（2）换行：用控制命令 “\\”, 或 “ \newline”.

（3）分段：用控制命令 “\par” 或空出一行。

（4）换页：用控制命令 “\newpage” 或 “\clearpage”

（5）特殊[控制字符](https://baike.baidu.com/item/%E6%8E%A7%E5%88%B6%E5%AD%97%E7%AC%A6)：#，$, %, &, - ,{, }, ^, ~

要想输出这些控制符用下列命令：

\# \$ \% \& \- \{\} \^{} \~{} $\backslash$ 表示 “ \”.。

### 8 西文字符转换表

\rm 罗马字体 \it 意大利字体

\bf 黑体 \sl 倾斜体

\sf 等线体 \sc 小体大写字母

\tt 打字机字体 \mit 数学斜体

### 9 字号转换命令表

点数 (pt) 相应中文字号 控制命令

25 一号 \Huge

20 二号 \huge

17 三号 \LARGE

14 四号 \Large

12 小四号 \large

10 五号 \normalsize

9 小五号 \small

8 六号 \footnotesize

7 小六号 \scriptsize

5 七号 \tiny

### 10 纵向固定间距控制命令

\smallskip \medskip \bigskip

### 11 页面控制命令

\[tex](https://baike.baidu.com/item/tex)twidth=14.5cm

\textheight=21.5cm

系统默认：字号 10pt= 五号字；西文字体为罗马字体；

[textwidth](https://baike.baidu.com/item/textwidth)=12.2cm,textheight=18.6cm。相当于美国标准信纸大小。

### 12 常见数学公式排版命令

（1）行中数学公式状态命令

\begin {math} 数学公式 \end {math}

简式 1： \(数学公式 \)

简式 2： $ 数学公式 $

（2）独立数学公式（不带编号）状态命令

\begin {displaymath} 数学公式 \end {displaymath}

简式 1： \[数学公式 \]

简式 2： $$ 数学公式 $$

（3）独立数学公式（带编号）状态命令

\begin {equation} 数学公式 \end {equation}

\begin {equation\*} 数学公式 \end {equation\*} 可以取消编号

### 13 使用 LaTeX 编辑表格

\begin{tabular}{|r|l|}\hline

Header & Row \\ \hline \hline

A & Silly \\ \hline

tabular & structure \\ \hline

\end{tabular}

其中 & 号代表分割线，也就是将一行表格分割为一块一块

\\ 代表换行

读音书写
----

[编辑](#)

由于 [TeX](https://baike.baidu.com/item/TeX) 一词应该读作 /tɛx/（[国际音标](https://baike.baidu.com/item/%E5%9B%BD%E9%99%85%E9%9F%B3%E6%A0%87)中的 /x/ 读如 “喝” 音），音译 “泰赫”，所以 LaTeX 一词可以音译为 “拉泰赫”。

在英语中，LaTeX 实际通常读作 /ˈleɪtɛk/（音译 “累泰克”）或者 /ˈlɑtɛk/（音译 “拉泰克”）。

在法语中，实际通常读作 /latɛk/（音译 “拉泰克”）。LaTeX 的开发者 Lamport 表示对 LaTeX 的读音没有偏好。

参考资料
:   * 1.
      [LaTeX – A document preparation system](https://baike.baidu.com/reference/1212106/9182Kb-y5yecS730qjFiXHMzcD5bd-dwOmjqlhZ2e3rLo4BAvCFqEGLtZQNaMBPAobDRrsDsZw)
      ．LaTeX - Official Site[引用日期 2016-05-09]
    * 2.
      [完全自学入门 LaTeX 排版的简版电子书](https://baike.baidu.com/reference/1212106/8a18bAUSG40lMBVmkFvCSNAeUvECW7YfPbben8WjdKSpKa1pSS3OrGhlRYH8HuTcDQdYYm6YdoGiNUwX8u37z5dmQCu34wXtzcFX25A)
      ．科学网．2013-5-31 [引用日期 2013-06-08]

---

[🌐 原始链接](https://baike.baidu.com/item/LaTeX/1212106?fr=aladdin)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d341c349-7a4b-4aed-a958-6fc3dc8a2cf0/d341c349-7a4b-4aed-a958-6fc3dc8a2cf0/)