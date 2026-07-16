---
title: "XLD：macOS 无损音频转换的不二之选 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/XLD：macOS 无损音频转换的不二之选 - 少数派.md
tags: [印象笔记]
---

# XLD：macOS 无损音频转换的不二之选 - 少数派

# XLD：macOS 无损音频转换的不二之选 - 少数派 --- XLD：macOS 无损音频转换的不二之选 ===================== ![](.evernote-content/

---

# XLD：macOS 无损音频转换的不二之选 - 少数派

---

XLD：macOS 无损音频转换的不二之选
=====================

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/6287CBEA-A06A-40A2-A1AF-800D8F754BEE)

XLD：macOS 无损音频转换的不二之选

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

随着流媒体音乐的兴起和版权意识的普及，收费相对合理的 QQ 音乐、网易云音乐、虾米、Apple Music 以及 Spotify 逐渐成为人们日常使用的音乐服务，在线听「无损」已经成为现实，曾经风靡数年的「国砖」播放器也变得越来越小众。

但流媒体音乐始终无法解决一些现实中的需求：

* 自己珍藏的经典音乐 CD 由于播放机的没落可能在不久的将来无法很方便的读取；
* 车载流媒体音乐播放暂时还未普及；
* 需要将资料附带的音频 CD 抓取转换并放入孩子的早教机；
* 出于某种情怀，喜欢在离线的环境下，一个人静静地欣赏 \*.wav 等。

平时经常会有人问我如何不花钱在 macOS 下转换音频格式，我通常都会抛给他们一个经典「神器」：XLD（[X Lossless Decoder](https://tmkk.undo.jp/xld/index_e.html)），一款开源免费的支持各种无损音频转换的工具。自 2006 年发布以来，更新了一百多个版本，最新版是今年 10 月 4 日发布的 20191004 版（64bit）。

安装配置
----

### 下载 XLD

访问官网：<https://tmkk.undo.jp/xld/index_e.html>

最新版下载：<http://sourceforge.net/projects/xld/files/xld-20191004.dmg>

8.4 MB 的 DMG 包含了主程序、多语言说明文件、授权信息以及命令行版本。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/C8188139-DD4A-4D99-8A08-00D615B45C87.png)

DMG 文件

直接拖拽 XLD.app 到应用程序目录即可，有一点需要特殊说明的是，打开 app 后，不会看到类似传统软件的主界面，你可以通过菜单栏找到它。个人猜测作者这么设计的意图是为了引导用户改进自己的使用习惯，需要转换哪个文件直接双击就好了。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/C9D1A220-1EF8-40B5-8377-E701426635EF.png)

菜单栏

### 配置 XLD

在菜单栏里点击 「XLD - 预置」，可在各个选项卡中设置需要的选项，主要有「导出格式」、「导出路径」和「File Naming」三个选项。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/2EB28ADC-C466-422C-B0B4-F45D0B501FF8.png)

预置选项

通过下图可以看到，XLD 支持导出各种常见的音频格式。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/5A6548FD-F85C-415A-A6CA-AAACB4F2CE88.png)

导出格式设置

对于「国砖」类播放器，建议选择 FLAC，可以得到无损音频以及较小的空间占用。

对于旧式车载播放器，建议选择 MP3 ([LAME](http://lame.sourceforge.net/))，这样可以保持良好的兼容性。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/90A763E3-4305-4CFA-AB54-47B5D9BF9F25.png)

MP3 码率设置

对于转换至苹果设备使用，不在乎空间大可选择 Apple Lossless，一般建议选择 MPEG-4 AAC (QuickTime/CoreAudio)，可以获得不错的音质并能控制空间占用。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/3F4AAA12-916A-4779-8096-6735E33118DD.png)

AAC 码率设置

如果不需要切换格式，只需设置这么一次，以后都是傻瓜化操作，简单快速。

主要功能及使用说明
---------

### 格式转换

例如，要将某个或多个 WAV 文件转换成 MP3 给车载播放器使用，只需双击 WAV 文件即可（前提是未将 “\*.wav” 格式文件关联其他应用）。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/305B9E92-4A7A-4AB6-9E52-253000CA4787.png)

MP3 转换

转换速度非常快，稍后即可在预设的路径下看到转换好的音频文件。

转成其他格式的操作方法也是如此简单，只需提前调整通用选项卡中的「导出格式」即可。

### 抓取 / 烧录 CD

抓取和烧录 CD 需要提前备好外置刻录机（现在几乎没有仍在服役的带光驱的 MacBook 了吧？虽然我是个例外，办公室仍偶尔打开 2008 款 MacBook 做备机）

只有一个建议：打开 ReplayGain 选项，使每个音轨音量均衡。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/A6B1295C-348A-46FC-BDE8-02C718675BE9.png)

抓取 CD 设置

### 使用 CUE 分割音轨

抓取的 CD 默认会被存储成一个 WAV + 一个 Cue Sheet，这对于仅需要播放其中某首单曲的情况不太方便，因此，我习惯于把抓取的整轨音频分割成单曲的状态。其实操作起来也异常简便：双击 Cue Sheet 文件，点击「Transcode」按钮。

![](.evernote-content/307225A1-56CB-49FF-B1DD-E899A46F7693/3F0EA40D-CF29-4178-93E2-AFFD2C7A14D7.png)

分割音轨

### 命令行模式

作为老牌应用，自然保留着适用批量操作的命令行工具，现实中估计很少能遇到。操作命令直接参考官网的参数说明。

```
% xld [-c cuesheet] [-e] [-f format] [-o outpath] [-t track] file
```

### 扩展插件

如果觉得支持格式还不够全面，官网还提供了第三方插件下载：

只需把下载好的插件放入下述路径，重新打开 XLD 即可。

```
~/Library/Application Support/XLD/PlugIns
```

### 总结

在没有发现 XLD 之前，面对无损音乐转换需求，第一时间想到的是去找 Windows 平台下的 Foobar2000，现如今，终于可以体面的吹一波 macOS 平台下的**开源免费**音频转换工具了！

题图来自 Pixabay 。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e) ，发现更多实用应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://beta.sspai.com/post/56940)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0bf65e08-100e-4aac-85d6-34997c1e1463/0bf65e08-100e-4aac-85d6-34997c1e1463/)