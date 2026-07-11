# 如何在本地将 DjVu 转换为 PDF：一次初步尝试

---

如何在本地将 DjVu 转换为 PDF：一次初步尝试
==========================

16小时前

[![](.evernote-content/1AF59D84-A7A5-43AF-84F7-7239CBC63371/D8A55C4C-BE90-42DA-9FA0-12CC988BD422)](https://sspai.com/user/830878)

#### [Chazeon](https://sspai.com/user/830878)

目录
:   1. [在移动设备上进行 DjVu 材料阅读的现状](https://sspai.com/post/45444#ss-H2-1530001520756)
    2. [将 DjVu 转换为 PDF](https://sspai.com/post/45444#ss-H2-1530001523202)
    3. [压缩 PDF 的体积](https://sspai.com/post/45444#ss-H2-1530001530220)

[DjVu](http://djvu.org/) 是一种常见于互联网的扫描版的电子书分发格式。由于把内容部分和背景部分分开保存，DjVu 格式的电子书能在较小体积的前提下仍然保证内容部分的锐利。许多老旧教材的电子版版本通常只能找到扫描版本，这类扫描版本通常是 DjVu 格式。

在移动设备上进行 DjVu 材料阅读的现状
---------------------

然而将 DjVu 转换为 PDF 的需求仍然存在，因为在不少系统上围绕 DjVu 搭建的基础设施极为有限。譬如在 iOS 上，对于 DjVu 格式的文档，目前我只找到了一款叫做 [BiLibre](http://kolyvan.com/bilibre/) 的应用，能够一定程度上支持使用 Apple Pencil 批注，这款程序还只是一个 [KyBook](http://kybook-reader.com/) 的程序的试验田而已。而反观 PDF，许多应用间能够直接传输、导入、阅读、批注 PDF，可以说一整套工具都是围绕着 PDF 搭建的。在移动设备上采用 PDF 而不是 DjVu 格式进行阅读相对来说自然是一种更优的选择。

线上一些网站将 DjVu 转换为 PDF 之后在锐度严重损失的前提下，体积通常会膨胀数十倍。这些线上工具也通常并未提供任何可以调整的参数。可能由于需求较少，目前也基本没有在本地找到一套完整可控的工具链能完成从 DjVu 到 PDF 的转换操作。因此我们开始尝试手动完成这一转换。

将 DjVu 转换为 PDF
--------------

目前探索来看，比较好的一对工具是 DjVuLibre 和 Ghostscript。

[DjVuLibre](http://djvu.sourceforge.net/) 是个开源的 DjVu 处理包。它提供了一个简易的图形化界面，能够进行简单的 DjVu 阅读。它的一系列命令行工具，能够比较好地进行 DjVu 的制作、解包工作，能把 PDF 以及许多图像格式转换为 DjVu。它同时也提供了编程库，被 [SumatraPDF](https://github.com/sumatrapdfreader/sumatrapdf/blob/master/AUTHORS) 等阅读器作为 DjVu 底层支持库使用。

[Ghostscript](https://www.ghostscript.com/) 则是老牌的 PostScript 处理程序，同样包括了用于阅读的图形化界面和一系列命令行脚本。这一系列程序被包含在 TeXLive 发行版中。

因此本文提出一种可行的操作，是使用 DjVuLibre 中的 `djvups` 命令将 DjVu 文件转换为 PostScript 格式，然后使用 Ghostscript 中的 `ps2pdf` 将 PostScript 格式的文件重新转换为 PDF。这样我们几乎得到了高质量的 PDF 原稿。

命令行操作的伪代码如下

```
djvups [djvu-file-name] [ps-file-name] [-verbose] [-page='1,3,7-10'] [-..]
ps2pdf [ps-file-name] [pdf-file-name]
```

要注意的是，如果没有提前将可执行文件的目录添加到 Path 中，两条命令均需要替换为实际的文件路径；Windows 下 `ps2pdf` 是个 `bat` 脚本因此要注意把拓展名包含在内，因为有个不含拓展名的文件实际上是个 Bash 脚本。另外在 `djvups` 中，`-verbose` 可以显示一个简易的进度条，`-page='1,3,7-10'` 选择转换的页码，还有后续更详细的设置能调整 PostScript 的分辨率、颜色和灰度等。

文章完成后，经过提醒，我注意到在 superuser 上对于这一过程有一定程度的[介绍](https://superuser.com/a/1194757)，可供参考。但最方便的 [djvu2pdf](http://0x2a.at/s/projects/djvu2pdf) 是 shell 脚本，并未提供 Windows 版本。

压缩 PDF 的体积
----------

可惜的是文件体积膨胀的问题仍没得到很好的解决，甚至可以说远远超出我的想象。原本 37 MB 的 DjVu 文件转换为 PostScript 文件后有 7.7 GB 之大，再次转换为 PDF 之后也有 1.44 GB，体积非常可观。下一步，我们只能看看能否在合理范围内缩减体积，无论是从最后压缩 PDF 还是基于损失 PostScript 文件的前提之下。Adobe Acrobat 将其转换为压缩体积的 PDF 能将体积减小到 242 MB，略小于线上转换出的 343 MB，两者的实际效果相差不大。

![](.evernote-content/1AF59D84-A7A5-43AF-84F7-7239CBC63371/4A693413-2B22-4A31-B9E6-EA8BEEC73A00)

在 Adobe Acrobat DC Pro 进行 ClearScan 操作

如果想要进一步地缩小文件大小，只能尝试一种被称为 ClearScan 的操作，这种优化与压缩的方案在 Adobe 的产品博客上有较为详尽的[比较和介绍](http://blogs.adobe.com/acrolaw/2009/05/better_pdf_ocr_clearscan_is_smal/)。这种优化方案简单说就是讲文本部分进行 OCR 处理，并构建一套共享的字体，通过这套共享的字体来优化体积。在 Adobe Acrobat DC Pro 中，这种操作的名字略有变化，选项位置藏在「工具 – 优化扫描的页面 – 文本识别选项 – 编辑 – 输出 – 可编辑的文本和图像」，这可以说是 DjVu 思路的 PDF 压缩方案，把前景的内容和背景分离，效果可以说见仁见智，但总体而言对于原本高分辨率的原稿，效果还是可以接受的。在我的实验之下，最终效果是把前文所述的 343 MB 的文件压缩到 172 MB。但这种操作由于涉及 OCR 的操作，因此耗时比较恐怖，可以考虑睡前进行。

本文提供的方案只是一种可行的本地操作方案而已，多了一种选择，但实际操作上，只能说还是要在体积和质量上做艰难的取舍。

---

[🌐 原始链接](https://sspai.com/post/45444)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1358308e-935d-46dc-a741-1148acf2511e/1358308e-935d-46dc-a741-1148acf2511e/)