# Winclone，也许这是最好的 Boot Camp 备份还原方案 | Matrix 精选

---

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/316C98B4-AF56-45F9-BD80-077F6132E530.jpg)

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/B91F2E97-DA45-46CC-B706-431C825969A9.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文仅代表作者本人观点，对排版语句有略作修改，[原文链接](http://matrix.sspai.com/p/ced70cc0)。

用什么
---

很多购买 Mac 电脑的用户，或多或少会主动或被动地使用 Boot Camp 安装 Windows 系统。具体大概有两类：一类是对软件有特定需求的，像 Windows 的 Office 比 Mac 的好用，Mac 电脑不兼容很多大型游戏；另一类是觉得 Mac 电脑好看，买 Mac 只是买一个外壳，些许带点装 X 性质的。

这些 Mac 装有 Windows 电脑的人都会遇到相同的问题——重装 Windows 系统。一般有三方面原因：

1. 当时 Boot Camp 给 Windows 的分区太少，不确定第三方软件是否可以完美重分配空间的；
2. 使用 Windows 时间长，系统不够快了，喜欢折腾，觉得需要重装系统的；
3. 该系统下莫名其妙中毒或有其他不可抗力导致无法正常使用的。

由上述原因造成的重装系统，会无可避免地造成时间的浪费。Boot Camp 驱动重装浪费时间，大量常用软件安装浪费时间，大量文件、程序、视频等备份浪费时间。总之，我在没有发现 Winclone 这款软件之前，平均两个月我就要重装一次系统，一次重装加上安装常用软件需要耗费半天的时间，这还算比较顺利的情况，不提安装过程中的奇葩问题（在老版本的 MacBook Pro 和 Air 中经常出现）。

终于，Winclone 解决了我的痛点，它可以完美地备份 Boot Camp 的 Windows 分区，无任何痕迹地还原备份前系统的模样。[Macworld](http://www.macworld.com/) 甚至称其为 Boot Camp 用户的必备工具软件。

关于 Winclone 软件的介绍和详细功能，可以参考 [官方网站](http://twocanoes.com/products/mac/winclone)，在这里不赘述，下面主要讲一下它备份和还原的方法，以及一些注意事项。

怎么用
---

### 1. 安装时需注意

Winclone 官网没有试用版，需购买后获得下载链接和授权文件，24小时后失效，过后需要重新输入 Paypal 购买账户邮箱重新获取链接和授权文件。

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/5A05E920-A391-479A-BA42-D92987C48F72.jpg)

### 2. 开始备份

1）点击备份按钮：

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/C5B2F33F-F541-4AD4-8B3A-D96A28B2D0B3.jpg)

注意：如果系统中有如 [Paragon NTFS For Mac](https://china.paragon-software.com/home/ntfs-mac/) 等支持 NTFS 格式的硬盘写入文件软件，需要先卸载，否则无法识别出 Boot Camp 分区。如果是 EI Capitan 的系统，需要重启 Mac 以关闭 SIP 安全设置。具体方法是：重启 Mac，按住 Command＋R，进入恢复模式，调用终端，输入 csrutil disable 后回车。

2）选择备份目标位置，这里推荐外接移动硬盘。

**![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/691C11FB-72F0-4DB1-B818-7D659D3441A9.jpg)**![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/492B4EA4-A4DA-4F3B-A416-D169326BA78A.jpg)

**![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/07305379-474C-47E2-8A38-D78825E26400.jpg)**注意：备份目标盘必须是 NTFS 或 Mac 系统下 OS X 扩展日志式等支持 4G 以上的大文件磁盘格式，备份文件 .winclone 比原本 Windows 分区所占的空间小很多，不过不要担心，不影响 Windows 系统完美还原。

### 3. 还原

1）将 Boot Camp 分区清除，在磁盘工具下将系统盘分区，重新划分预装 Windows 系统占比，格式选择 FAT。

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/44F87D04-2A05-4546-88B5-8CAE3698513B.jpg)![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/10989B2A-7ED7-4AFF-BB6A-A75BA6E73265.jpg)2）点击程序右边的还原按钮，还原 Windows 系统。

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/D7894FF8-7843-40F2-B3B0-6DE37AE37A5B.jpg)3）再次开机时，运行 Boot Camp 下的 Windows 分区，耐心等待磁盘重新分配，分配好后自动重启，稍后即可享受完美还原下的 Windows 系统。

关于购买
----

Winclone 分为基本版、标准版、专业版三种。具体各版本的对比如图，具体可参见 [官方网站](http://twocanoes.com/products/mac/winclone)。

![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/9C58787D-1584-4128-8E9A-5AA632A3E02B.jpg)

写在最后
----

说了这么多，无非是希望喜欢折腾、需要重装系统的读者可以节约时间，避免不必要的时间浪费，如今有很完美的解决方案。

最后建议各位第一次使用 Boot Camp 重装 Windows 后，把常用的软件和驱动再备份一次，以后每次还原的就是清爽无比、毫不费力的新系统了。

你可以前往 [Winclone 官方网站](http://twocanoes.com/products/mac/winclone) 购买或了解详情。

文章来源 [少数派](http://sspai.com/) ，原作者 [zhouyu3092070](http://sspai.com/author/716010) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime

少数派（ [http://sspai.com](http://sspai.com/) ）

[![](.evernote-content/4ACF1224-2F47-4C0C-8A31-7282A3A80807/FBFBD022-F2E6-446B-8B1F-64AE0C14BE59.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:k12/destination:http%3A%2F%2Fwww.apple.com%2Fcn-k12%2Fshop)

---

[🌐 原始链接](http://sspai.com/34731)

[📎 在印象笔记中打开](evernote:///view/207087/s1/76065883-e293-4f0d-84e0-391a017d122c/76065883-e293-4f0d-84e0-391a017d122c/)