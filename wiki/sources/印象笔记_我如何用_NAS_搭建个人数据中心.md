---
title: "我如何用 NAS 搭建个人数据中心"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/我如何用 NAS 搭建个人数据中心.md
tags: [印象笔记]
---

# 我如何用 NAS 搭建个人数据中心

# 我如何用 NAS 搭建个人数据中心 --- 今年（2017年）2月份入手了 Synology DS216j，不知不觉已经过去了半年。 当初考虑使用 NAS，是因为使用了小米盒子后，开始追求离线下载

---

# 我如何用 NAS 搭建个人数据中心

---

今年（2017年）2月份入手了 Synology DS216j，不知不觉已经过去了半年。

当初考虑使用 NAS，是因为使用了小米盒子后，开始追求离线下载以及观看影音的体验。

半年以来，这台 NAS 成了我的数据中心，影视、照片、音乐、TimeMachine 都存放在两块 2TB 西数红盘上。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/425DBA5F-B1A6-4F38-A6DD-474EE213BCCE.jpg)两块 2TB 红盘

DS216j 有两个盘位。起初我在犹豫到底做 RAID0 还是 RAID1, 后来想想，我的硬盘里大部分是影音，做 RAID1 未免太浪费，倒不如做 RAID0, 然后定期把最重要的数据同步到另一块移动硬盘里。

在首次安装、启动、配置后，我把它放在家中的一个角落，之后就再也没有管它了，它就角落里安静地服役。即使它摆在你的房间，你也完全不会感受到他的存在。当然，如果你嫌 LED 灯太刺眼，可以在设置里关闭它。  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/3B283A0D-D73F-4332-9FDC-A15F09A87294.jpg)  
NAS 的本质只是一台低功率、持续运行的计算机。理论上自己也可以 DIY 一台 NAS，有很多人也这么做。但是为什么很多人还会选择购买群晖的解决方案，一个很重要的原因是群晖的软件生态——DSM.

### DSM

DSM 是群晖 NAS 中运行的「操作系统」。这个打引号的「操作系统」指的不是我们常说的操作系统，而是一个用于组织管理 NAS 上的文件的程序。DSM 提供了一个 Web 界面，一切操作都可以在这个界面中进行。  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/008BFB3E-5F97-45FC-B7B4-973A76D14E5B.png)DSM  
除了 Web 界面，群晖在移动平台提供一系列的 APP，读取和操作不同类型的资源。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/2735F537-3D43-49F2-AC45-75378C9A1C39.jpg)DS APP  
在 Web 界面中，我一般会通过 File Station 管理我的文件，类似于 Finder.

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/E6ED989F-6A7D-4311-BE94-1E9986719D68.png)File Station  
DSM 的生态在于套件中心，但实际上在我半年里的使用来看，我真正用到的套件只有那么几个。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/E0F229BB-49C1-4F5C-8544-E005CF8C4DD7.png)套件中心

### 多媒体中心

作为多媒体中心，有两个最重要的要素，分别是下载资源的体验，和观看资源的体验。

先说下载资源的体验。DSM 本身提供 Download Station 这个套件，可以在上面添加管理下载任务，也提供电驴和迅雷离线下载的入口。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/B02DF597-FAED-4E11-9969-C490AD9632AB.jpg)Download Station  
但是使用多次后，我毅然放弃了 Download Station, 原因有几个：

1. **响应速度非常慢**。这是绕不过去的坎。由于我家使用的移动宽带给我分配的是内网 IP, 我无法通过 DDNS 在外网访问我的 NAS, 所以只能使用 DSM 提供的 Quick Connect，在群晖的服务器做一个中转。访问速度可想而知。从进入 DSM，到获取下载列表任务，再到添加任务，花费的时间非常长。
2. **迅雷离线下载入口，只是看上去很美**。拉取离线下载任务列表相当耗时，添加任务还不一定成功。总的来说，我没有一次在 Download Station 里成功地通过迅雷下载。

Download Station 唯一比较有用的功能是提供从 RSS Feed 中下载资源的功能，比如我只要提供一个持续更新下载地址的 RSS，通过过滤器，可以自动的根据正则表达式进行对应的行为。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/0068087D-BEA2-4A2E-ACED-DF2116370BCB.jpg)RSS Feed 过滤器  
但是影响下载速度和稳定性的因素是资源的质量，如果单纯使用 http 下载，有些资源恐怕从我上班到下班回家都不一定下载完。所以需要放弃 Download Station, 另辟蹊径。

#### Aria2

通过 ssh，我在 NAS 里跑了 Aria2, 配合像 BaiduExporter (百度盘导出任务到 Aria2) 这种插件，可以畅快地建立下载任务，临睡前把下载任务开始，一晚上能下载很多资源。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/FDA0C42F-7C33-41A1-B8F2-7A24CF0F40A9.png)Aria2 下载队列  
但是因为没有外网 IP 的原因，在外面我就无法直接访问 Aria2 的 Web UI 添加任务，所以我需要另一种下载方式进行互补。

#### 迅雷远程下载

我在 NAS 又跑了一个 Xware, 通过 Xware 可以关联迅雷远程下载和 NAS. 这样既能够在外面管理下载任务，又能享受迅雷的高速通道和离线下载资源。  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/A1EE6325-3804-4DD9-92E5-E032E46320E5.jpg)迅雷远程下载  
至于观看，DSM 的 Video Station 会对文件夹中的视频进行分析，自动从多个影视 API 获取相关信息，然后整理。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/1E9D1C6B-5662-44A7-BC3D-837E14D9DE5C.jpg)Video Station  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/1BD8BEC8-82FD-45EB-9D99-4A19E36FA217.jpg)  
然而我只会在使用移动设备进行观看的时候才会使用 Video Station. 因为 Web 版的 Video Station 用的是普通的 `<video>` 标签，支持的视频格式不多（DS216j 也没有转码功能），所以我一般是通过 Finder 连接 NAS，之后用本地的播放器进行播放。  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/DB28040A-5A67-48AD-BD6B-4BD7F80A0F20.png)通过 Finder 连接 NAS  
因为我有一台小米电视，所以主要的影视播放都在电视上。我一般会通过两种方式在电视上播放 NAS 的视频。

第一种，通过小米电视自带的「高清播放器」应用，可以连接远程的服务器，只要填写 NAS 的地址和用户名密码，就能访问里面的文件夹。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/0058A5F5-6FA9-4DB1-9512-1AC66A641245.jpg)  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/443CB35E-AE70-4021-87DB-0C05A3CBEFF5.jpg)  
![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/74B4F3F0-70F2-49AB-B198-3D1B2CAC6150.png)流畅播放 1080P  
我一般是从文件夹里找到我要看的视频。小米电视也会自动识别出文件的影视信息，但是识别不是特别准确。

第二种是通过 Airplay/DLNA，移动设备上用 DS Video 选好要看的视频，然后直接 Airplay 到电视上。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/D2B4070F-CBE4-4490-9CBF-B01B9C2227D7.jpg)串流  
至于管理音乐的 Audio Station，对我这个音乐发烧友来说也显得尴尬。因为听音乐我更倾向于串流服务，比如 Spotify 和 网易云音乐，很少存放音乐文件，一般存放音乐文件到本地只是为了满足我对音乐的收藏欲。

Photo Station 做得很好，在买了 Dji Spark 以后，对图片视频存放的需求也就有所增多，因为 TF 卡的容量也有限。手机上我会常用 DS Photo 同步我比较喜欢比较重要的照片到 NAS 上。但是我没有使用增量同步的功能，因为我订阅了 iCloud 50GB 的空间，目前手机 7000 多张照片，只占用了 iCloud 26GB 多一些。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/BC15B3B3-2D17-4039-B8CC-11030E6E04CE.png)Photo Station

#### TimeMachine

macOS 的 TimeMachine 原生支持网络设备，所以只要在 TimeMachine 里把备份位置设定到 NAS 的文件夹后，每当我回家插上电源，就会自动备份到 NAS 上。

![](.evernote-content/656A9533-E36C-439E-B785-E4F01F0E4061/2CC2F95B-7CC9-4C1E-BCBD-0E0A47A55134.png)TimeMachine

### 总结

NAS 极大的改善了我观看影视的体验，实现了下班回家就能看最新剧的需求。同时还成为了我的数据中心。以往 TimeMachine 要定期插一个移动硬盘进行备份，现在只要接上电源，无需操心。

DS216j 的价格很适合作为 NAS 的入门之选。然而入门 NAS 的花费不仅在于机器本身，还有硬盘的花费。同时你可能还需要把你的百兆路由扔掉，重新买一个千兆路由。�

然而 DS216j 的配置十分尴尬，32 位的 CPU 导致你无法使用 docker 这个利器。 我安装 Aria2 和 xware 的时候，只能费尽力气找对应的编译好的包来安装的。�所以如果有充足的预算，建议直接买 DS216 II+ 一步到位。

---

[🌐 原始链接](https://sspai.com/post/39949)

[📎 在印象笔记中打开](evernote:///view/207087/s1/16329c2d-d048-41e6-b0d5-97fad07847f7/16329c2d-d048-41e6-b0d5-97fad07847f7/)