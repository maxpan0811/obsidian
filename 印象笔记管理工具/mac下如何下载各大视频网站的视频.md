# mac下如何下载各大视频网站的视频

---

mac 下如何下载各大视频网站的视频
==================

2018 年 12 月 23 日

[![](.evernote-content/20B2A385-5810-4F65-A02F-5459BB6D898D/7FC784EB-C1B4-4C40-A966-F5E8B287579A)](https://sspai.com/user/843694/updates) 

#### [yiranzhimo](https://sspai.com/user/843694/updates)

最开始只是想下载我想要的视频收藏，后来，就想，要不试试各大视频怎么下载（此处的下载不是指解析 VIP 视频，而是指如何下载各大视频网站的免费的视频）  
##bilibili  
哔哩哔哩的视频用 Mac 版的 bilibili 客户端下载就 OK 了  
下载速度很 OK，还是多线程的 aria2 下载  
只是有一个问题，就是下载完以后的视频为 flv 格式，且为分段的  
这并不影响观看，用 IINA 或者 bilibli 就可以看了  
但是如果是收藏视频就得自己转换合并了。  
推荐工具 ffmpeg, 或者别的软件都可以做到的。  
下载速度很不错

![](.evernote-content/20B2A385-5810-4F65-A02F-5459BB6D898D/4415297B-19BC-47A6-B3EE-FB5A8C9AC149.jpg)

bilibili

## 优酷

Mac 的 downie 就搞定了

还是举个例子，复制网页链接 -- 文件 -- 打开链接，就搞定了

我这排字刚打完，就下载好了，速度很快

![](.evernote-content/20B2A385-5810-4F65-A02F-5459BB6D898D/F426175B-051D-4BE6-A226-C675622D88A1.jpg)

优酷

## 腾讯

腾讯的视频下载把我难的啊

先来说一下我的挖坑历程

首先第一步，我尝试客户端下载，然后找到文件，转化合并格式就好了

但是，等我找到文件之后，我惊讶的发现文件竟然都是 ts 格式的了，而且每段都是 10s 左右的，于是，我想着用软件转化并且合并，结果转化的东西都是音频没有视频，而且 ts 格式的源文件也是只有音频没有视频。无奈，放弃了这个方法。

第二步，我尝试了 github 上的项目，you-get ,youtube-dl,annie，结果，这三个没有一个能下载，无奈，这条路又放弃了

第三步，我尝试用 downie 和 apowersoft, 但是两个软件的下载速度不太行，而且，基本上都是失败的。

第四步，事到如今，只能退而求其次了，我想到了两个办法，第一个办法，我用网页嗅探视频，然后下载合并，尝试下载电视剧还好，视频基本会被截成 20Mb 左右的一段，而且，最让我愕然的是，如果我打开斗罗大陆的视频，会被截成不到 2Mb 的文件，这是有多少段啊，好的，这条路也没了。

![](.evernote-content/20B2A385-5810-4F65-A02F-5459BB6D898D/41BEF291-5176-4AF8-AD24-9CD160D98B3D.jpg)

于是，悲催的我只能借助第三方网站，解析视频，可是，我在我自己的存的网站里面，没找到一个，最后，千搜万搜，才找到了一个网站：

<http://old.flvurl.cn/default.aspx>

只有这个网站可以

![](.evernote-content/20B2A385-5810-4F65-A02F-5459BB6D898D/E634C2E1-C61C-4589-AF4B-E09CD5BB3863.jpg)

腾讯

之后，下载视频，保存，合并就好了，基本上五分钟一段。

这是目前想到的法子。

## 爱奇艺

爱奇艺的视频网页嗅探没用，网页解析没用，you-get,youtube-dl，downie ,apowersoft，统统没用，还好有 annie

举个例子，我下载大江大河第一集

这速度不错，而且默认下载最高格式。

![](.evernote-content/20B2A385-5810-4F65-A02F-5459BB6D898D/D9054252-6656-4D83-8E7E-143E484C98F6.jpg)

iqiyi

爬坑至此，做个总结

bilibili for mac 客户端地址：

<https://typcn.com/legacy/bilimac/>

[github 地址：](https://typcn.com/legacy/bilimac/)<https://github.com/typcn/bilibili-mac-client>

[下载优酷视频所用软件：downie](https://typcn.com/legacy/bilimac/)

[下载腾讯视频所用网站:](https://typcn.com/legacy/bilimac/)<http://old.flvurl.cn/default.aspx>；视频合并软件：videoproc

[下载 iqiyi 的工具：annie；github 上的地址：](https://typcn.com/legacy/bilimac/)<https://github.com/iawia002/annie>

[注：](https://typcn.com/legacy/bilimac/)

[在这个过程中尝试的插件是：猫抓和 flash video downloader](https://typcn.com/legacy/bilimac/)

[其他尝试的工具有：youtube-dl：](https://typcn.com/legacy/bilimac/)<https://github.com/rg3/youtube-dl/blob/master/README.md#output-template-examples>

[you-get：](https://typcn.com/legacy/bilimac/)<https://github.com/soimort/you-get>

[而且，在这个过程中尝试的工具，youtube-dl 和 you-get 应该对外网的视频下载更友好，annie 对国内比较友好，而且 downie 能下载很多网站的视频，猫爪和 flash video downloader 我一般用来下载公众号附带的视频。而且，我所选用的视频下载方法，只是针对于某一类比较好的方法，其实是上述的几个视频网站的下载方法之间是有交叉的。](https://typcn.com/legacy/bilimac/)

[关于腾讯的下载问题，还没有完全解决，只是退而求其次，强迫症的我一定要搞定这个问题，大不了，我好好学习，写个工具。](https://typcn.com/legacy/bilimac/)

[欢迎交流！！！](https://typcn.com/legacy/bilimac/)

---

[🌐 原始链接](https://sspai.com/post/52127)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ccecaafb-5589-43c4-b84c-26ef21ea67f0/ccecaafb-5589-43c4-b84c-26ef21ea67f0/)