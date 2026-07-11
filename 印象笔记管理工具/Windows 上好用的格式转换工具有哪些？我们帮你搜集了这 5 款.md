# Windows 上好用的格式转换工具有哪些？我们帮你搜集了这 5 款

---

相信大家在日常工作生活中，或多或少都会遇到需要转换文件的问题。这时候在通过各大搜索引擎去找工具，很容易遇到各式各样的广告，或者功能单一并不好用的软件，甚至是恶意软件和病毒。这篇文章希望通过分享几个我还算常用的文件转换工具，为大家日后需要时做准备。

全能型格式转换工具：格式工厂
--------------

相信很多人都希望有一个「一劳永逸」、什么都能转换的文件格式转换工具，那么**格式工厂**将是非常好的选择。格式工厂能够转换视频、音频、图片、文档、光盘等文件，无需任何命令行和依赖程序，开箱即用。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/6DC12A43-242A-44E0-BFDE-46486D147371.png)

内置的预设和界面对新手非常友好，主界面左侧就是文件类型转换和目标格式，右侧就是转换的队列。在转换设定中，界面也非常清晰明了。当然，在转换页面对熟手也提供了相应的参数修改选项，方便直接使用高级功能。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/3084B1B7-04C3-4324-9FEB-9A49781A6CD1.png)

此外视频转换工具还提供了爱奇艺缓存文件的解码，以及图片转换工具对 HEIC 文件的支持，真的堪称强大且好用。

你可以在 [格式工厂官网](http://www.pcgeshi.com) 免费下载，安装时需要注意有推广软件。

视频转换工具：小丸工具箱
------------

当然也不是每个人都需要一个「全能型」的转换工具的。在视频转换方面有一定的需求的人，这时候我就建议使用**小丸工具箱**。小丸工具箱界面相较于格式工厂更为复杂些，视频转换常用的标签页是视频和封装。

小丸工具箱的视频标签页中提供了在质量、压缩时间、最后文件的体积之间尽可能平衡的参数，帮助新手直接开箱使用。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/E70F7235-A322-47D5-BF0B-067C16B7EF09.png)

选择编码器后，再选择 CRF（ Constant Rate Factor ，可以理解成目标视频质量，0为无损，18以下肉眼几乎无分别，30以上则会很糊），或者 2Pass （指定视频码率，数字越大视频越清晰，并通过2次压制的过程获得最后的码率），最后点击压制就开始了。

同样针对老手也提供了非常多的参数，能够快速获得想要的结果。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/916774F3-51CC-4630-B396-3F1999DC7E57.png)

封装主要是起到一个文件夹（或者压缩包）的作用，并不会对视频轨和音频轨造成影响。而抽取是对封装的反向操作。

用户无需了解命令行，转换的过程会出现命令行窗口，转换完成以后就会自动关闭。

你可以在 [小丸工具箱官网](https://maruko.appinn.me) 免费下载。

文档转换工具：Pandoc
-------------

### Pandoc

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/08069708-55CB-474F-B209-6CA71A178D5C.png)

相信很多小伙伴都并不觉得 Word 写论文是个很好的选择，奈何很多学校最后要提交 Word 格式，而 Pandoc 是一款基于命令行的文档格式转换器，支持1

> 输入格式:Markdown、格式轻量级标记语言、HTML、ReStructuredText、LaTeX、OPML、Org-mode、DocBook、Office Open XML (Microsoft Word .docx)，输出格式：Office Open XML(Microsoft Word .docx)、OpenDocument、HTML、Wiki markup、Adobe InDesign ICML文稿 （ Adobe InCopy文稿交换格式）、web-based slideshows、电子书（Epub格式等）、OPML多、种 TeX (以及 PDF).

在转换的时候需要用到命令行语句，以下是常用命令的解释：

```
-s 代表的是 Standalone 转换过程，通过适当的页眉和页脚生成输出
  
  
  
-f 选项代表 from ，其后是源格式
  
  
  
-t选项（代表“to”）后跟输出格式
  
  
  
-o选项代表“output”，后面跟着输出文件名或是带输出名称的输出路径
  
  
  
以及跟随在最后的原始文件名
```

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/8D544690-529C-4DB4-88BA-FA59E2F2CEA1.png)

使用的时候需要将命令行的路径，切换到你想要转换的文件目录下。在使用命令进行转换。

`pandoc -s -f markdown -t icml -o my.icml my.md`

这里我用 Pandoc 将名叫 my 的 markdown 格式转换成名叫 my 的 icml格式。

通过 Pandoc 就可以使用自己喜欢的工具完成论文了。

想要了解更多关于 Pandoc 命令行的用法，可以在 [Pandoc 官方说明文档](https://pandoc.org/MANUAL.html) 中查看。

你可以在 [Github](https://github.com/jgm/pandoc/releases/tag/2.1.3) 下载 Pandoc。如果你喜欢通过 Chocolatey 安装软件，可以使用 `choco install pandoc`这条命令进行安装。

### Typora + Pandoc

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/CBDC6B77-4104-4A64-A69A-E90E6155833F.png)

Typora 本质是 Markdown 编辑器，如果额外安装 Pandoc 插件则可以直接通过 Typora 转换文档格式，不过不如通过命令行转换的格式多。不过可视化的特性，针对搞不定命令行的使用者显得就非常友好了。

想要了解更多关于 Typora 的特性，可以看看这篇《[让 Markdown 写作更简单，免费极简编辑器：Typora](https://sspai.com/post/30292)》

你可以在 [Typora 官网](https://typora.io/) 下载。

图片转换工具：iMazing HEIC
-------------------

### HEIC - PNG：iMazing HEIC Converter

相信 iOS 11 的 HEIC 的图片格式既让人爱也让人痛。小巧的体积能帮助用户节省大量的空间，但是除去 macOS High Serria 和还为发布的 Windows 10 RS4 (Build 17133.1) 以外，其他设备都不支持，让查看和分享照片变成了一件困难的事情。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/9E1BE3BD-D765-4FD2-8267-E30F39177599.png)

不过 iMazing HEIC 工具能够轻松转换将图片从 HEIC→PNG/JPEG。我非常推荐使用这款软件是因为 iPhone 7 以及以上机型都支持拍摄 P3 广色域照片，所以转换后的图片是否携带色彩配置文件就格外的重要，不携带配置文件进行传播，很大可能性会导致色彩出现偏差，让你美美的照片想的不是那么漂亮。

你可以在 [iMazing HEIC 官网](https://imazing.com/heic/download) 下载。

### 在 PNG - JPEG - GIF 之间转换格式：Windows 画图

虽然 PNG、JPEG、GIF 这些格式在现代互联网中几乎是通用的，基本可以无视格式。不过总有例外，有些网站会限制图片格式。不过 Windows 内置的画图软件能够很轻松的进行转换，获得想要的格式。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/71DAE878-B288-43B6-B636-D7B5793AA512.png)

音频转换工具：Foobar 2000
------------------

大家对音频转换的要求可能没有那么高，毕竟现在大家不是使用流媒体服务就是直接在国内的平台上下载歌曲。当然有的时候突然要使用到就很焦急，不过好在 Foobar 2000 和 XLD 的存在还是能够帮助转化大部分非特有格式的音乐。比如将无损的 FLAC 转换成 mp3 ，又比如曾经 iTunes 还不支持 FLAC 的时候要把他们转换成 ALAC 格式。

Foobar 2000 虽然有转换功能，但是实际上还是款播放器，不过不支持中文，国内网络上有不少汉化版本，不过自然安全性就很难进行保证了。

![](.evernote-content/08BC1B9A-2027-4A59-BF17-493380376ADD/F42CC820-A608-48EC-A741-F4D8EC3AF06B.png)

转化步骤非常的简单，选中想要转换的音轨以后，「右键 - Converter - … - 设定 Output format/Destination/Processing/Other - 点击 Convert」，等待进度条走完就转换完毕啦。

你可以在 [Foobar2000 官网](https://www.foobar2000.org) 和 [Microsoft Store](https://www.microsoft.com/zh-cn/store/p/foobar2000/9pdj8x9spf2k?rtc=1) 下载。

> App 那么多，怎么选？下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让我们帮你做决定。

---

[🌐 原始链接](http://sspai.com/post/44131)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ad6e2a3c-5e54-4c47-9e67-eed2e808de21/ad6e2a3c-5e54-4c47-9e67-eed2e808de21/)