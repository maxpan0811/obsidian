---
title: "简中求效：Markdown 遇上 LaTeX _ Matrix 精选 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/简中求效：Markdown 遇上 LaTeX _ Matrix 精选 - 少数派.md
tags: [印象笔记]
---

# 简中求效：Markdown 遇上 LaTeX _ Matrix 精选 - 少数派

# 简中求效：Markdown 遇上 LaTeX | Matrix 精选 - 少数派 --- 简中求效：Markdown 遇上 LaTeX ====================== ![](.ev

---

# 简中求效：Markdown 遇上 LaTeX | Matrix 精选 - 少数派

---

简中求效：Markdown 遇上 LaTeX
======================

![](.evernote-content/FC14FA04-60CF-4D1F-9BC1-B15D9986AF98/C2B004F7-E341-4E75-8E6B-9A835271C323)

简中求效：Markdown 遇上 LaTeX | Matrix 精选

2016 年 12 月 06 日

![](.evernote-content/FC14FA04-60CF-4D1F-9BC1-B15D9986AF98/4B90C9EA-0A69-4E92-8C45-3988A108A9F9.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章对标题和排版略作修改，[原文链接](http://matrix.sspai.com/p/d87d72a0)。

---

前言
--

我是一个物理工作者，MS Word／WPS 什么的很早就扔掉了。LaTeX 才是我们的家常便饭。本科时候在课堂上我就喜欢拿着 LaTeX 编辑器做笔记，当时就盼望着哪天 Evernote 能够支持 LaTeX 语法。在 macOS 下配置 LaTeX 编译环境十分简单，只要下载一个 [MacTeX](http://www.tug.org/mactex/)，它自带 TeXShop，然后一切就都搞定了。

后来知道了 Markdown 语法，这样一个花 2 分钟就能学会的「标记语言」直接戳中我这样一个极简主义者的 G 点。与 LaTeX 最大的不同在于，它不会像大多数 LaTeX 编辑器一样在仅修改了一个标点之后，都要求重新编译。

然而要同时实现 Markdown 的极「简」，和 LaTeX 的「效」能是非常艰难的。虽然在静态博客里可以使用 MathJax 显示公式，但在 macOS 端编辑博文时没有 LaTeX 预览也是很难过的一件事。

* ### [MWeb](https://sspai.com/tag/MWeb)

你可能会说 MWeb 就支持 LaTeX 的编辑和预览呀！的确，我尝试过它，但这里提出两点我后来放弃它的原因：

1. 预览的公式字体太难看，不知道为什么作者不设置为科学期刊上最为常用的 Latin Modern Math 字体。我在作者的 GitHub 下发过一个 issue，他也没能给我一个有效的答复。
2. MWeb 没有 iOS 版，不能多设备同步。

* ### [Typora](https://sspai.com/tag/Typora)

还有声名鹊起的 Typora，我觉得它单作为 Markdown+LaTeX  编辑器可谓最优选：插入公式的方式不能再漂亮、默认的主题也简单优雅。

但它不能对文档进行管理，没有所谓的「外部文件夹」。而且，它也没有 iOS 版。

综上，我的要求其实很苛刻 —— 优秀的编辑环境、Markdown、LaTeX 预览、多设备同步集合为一体。于是我开始在 [Ulysses](https://sspai.com/tag/ulysses) 和 [iA Writer](https://sspai.com/tag/IA%20Writer) 上寻求出路，因为这两个软件首先就符合我对「优秀的编辑环境」的要求。最终我找到了我的解决方案。

方案一：Ulysses + HTML
------------------

Ulysses 是支持 HTML 预览的，所以我们在 Markdown 文档里插入一些 HTML 语言也没有关系。前天我就在 [@ulysses](https://twitter.com/ulyssesapp) 官推上看到了这个在 Ulysses 下实现公式预览的方案。

只需要在文档开头加入这四行 Raw Source Block 即可

```
~~ <script type="text/x-mathjax-config">
~~ MathJax.Hub.Config({tex2jax: {inlineMath:[['$','$']]}});
~~ </script>
~~ <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

其实这就是 HTML 下的 MathJax 相关设置。不用担心那些小波浪号，它们是 Ulysses 用来标记 Raw Source 的符号，无论是导出还是发布到你的的静态博客上都不会影响。

之后只要将正常 LaTeX 语法包裹进 Raw Source 格式中即可，比如

```
神奇公式：
~~ $$\left(iD\!\!\!/+m\right)\psi = 0$$
~$\dfrac{1}{2}$~，这就是二分之一，想不到吧！
```

然后调整 Ulysses 的导出格式为 HTML，使用 ⌘+⇧+P 就可以预览文档里的公式了！

![](https://ulyssesapp.com/blog/wp-content/uploads/2016/11/MathJax-Example.png)

原文链接：[Writing Mathematical Equations in Ulysses](https://ulyssesapp.com/blog/2016/11/eline-explains-5/)

方案二：iA Writer + Export Markdown to PDF
--------------------------------------

我们也可以利用 iA Writer 实现 Markdown + LaTeX。

同样是解决 LaTeX 公式预览问题，我发现了这样一个系统服务 ——[Export Markdown to PDF](https://github.com/lukaskubanek/iA-Writer-Export)。它是基于 pandoc 命令，在 iA Writer 下将文档转换为 PDF，并在默认 PDF 应用程序下预览。虽然不像 iA Writer 自带的预览那样高效，但如果只是插入几行公式，对我来说这已经最佳方案了。况且近日发布的 iA Writer 4 支持多文件、模块化编辑，对于每个子文件而言 pandoc 的编译效率也十分高了。

![](.evernote-content/FC14FA04-60CF-4D1F-9BC1-B15D9986AF98/F366A642-AC61-4594-BAB7-413310814F7D.jpg)

遗憾的是，这个 Export Markdown to PDF 已多年没有维护了，它环境变量设置已经因为新版本路径更改无法使用，而且最致命的是它不支持中文文档。于是我将它 Fork 了一下，修改成为了支持中文的 LaTeX 编译服务，下面我用四步教大家如何配置它：

### 第一步

首先，毋庸置疑你的电脑里必须安装有 [MacTeX](http://www.tug.org/mactex/)，并且我建议安装最新的 2016 版，否则环境设置可能会略有不同，导致不必要的麻烦。

以及，转换 PDF 所需的 pandoc（在终端下用 [brew](http://brew.sh/index_zh-cn.html) install pandoc 命令安装）。

### 第二步

配置 xelatex 中文编译模板

```
mkdir ~/Templates
cd ~/Templates
pandoc -D latex > template.tex  %导出pandoc默认模板文件
```

然后我们在导出的默认模板文件 template.tex 上进行修改。定位到 `% if luatex or xelatex`，在 `\fi` 的下一行（下图白色箭头处）插入如下语句：

```
% SUPPORT for Chinese
\usepackage[boldfont,slantfont,CJKchecksingle]{xeCJK}
\usepackage{fontspec,xltxtra,xunicode}
\defaultfontfeatures{Mapping=tex-text,Scale=MatchLowercase}
\punctstyle{quanjiao}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKsansfont{KaiTi}
\setCJKmonofont{SimSun}
\defaultfontfeatures{Ligatures=TeX,Scale=MatchLowercase}
```

![](.evernote-content/FC14FA04-60CF-4D1F-9BC1-B15D9986AF98/3079375C-F18A-45EC-A25C-6A810810E612.jpg)

其中 `\setCJKmainfont{WenQuanYi Micro Hei}` 可以自定义主字体（LaTeX 老司机也可以尝试修改其他内容），我测试时用的是「文泉驿微米黑」字体，大家可自行修改。但最好像我一样使用字体的英文名称。什么？你不知道怎么查看字体的英文名称？到终端使用下面这条命令查阅系统内的字体英文名吧。

```
fc-list :outline -f "%{family}\n"
```

### 第三步

下载我 Fork 的 [Export Markdown to PDF](https://github.com/patricorgi/iA-Writer-Export)，把 Workflow 文件放到「~/Library/Services」路径下

### 第四步

在 iA Writer 下使用：iA Writer - Services - Export Markdown to PDF 即可。编译的时候可以看到右上菜单栏会有个旋转的小齿轮，特别可爱。如果 LaTeX 语法有错误，错误信息会以弹窗的形式出现，方便你 debug。

![](.evernote-content/FC14FA04-60CF-4D1F-9BC1-B15D9986AF98/7F98E45A-4EDC-4CBB-8A2F-2D492F8EA1C3.png)

### 一些说明

* `$ \dfrac{1}{2}$` 会报错，要改为 `$\dfrac{1}{2}$` 才行，好像是第一个 $ 后面不能出现空格
* 需要自行研究一些特殊宏包的插入，例如页边距的设置等，毕竟在 Markdown 文档里无法使用 `\usepackage` 命令了，有些茫然不知所措
* 用 Automator 打开 Export Markdown to PDF.workflow 你可以看到下面这些内容：
  + pandoc 环境设置
  + xelatex 环境设置
  + pandoc 转换 pdf 的命令，其中 --template 字段设置的是 pandoc 编译模板，这就是第二步中为何要生成～/Templates/template.tex 文件的原因，你可以自行配置多个模板，然后记得在 workflow 文件里修改模板位置。

结语
--

祝大家 LaTeX 愉快！

---

[🌐 原始链接](https://sspai.com/post/36420)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7d2b6d7f-56a1-4dda-95ca-7533e41f01d9/7d2b6d7f-56a1-4dda-95ca-7533e41f01d9/)