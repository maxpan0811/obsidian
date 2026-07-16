---
title: "如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨 - 少数派.md
tags: [印象笔记]
---

# 如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨 - 少数派

# 如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨 - 少数派 --- 如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨 

---

# 如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨 - 少数派

---

如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨
===========================================

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/0083F13D-BF60-465C-AF0A-3E0B1A0CC1BF)

如何让群辉 NAS 的 Video Station 正确获取元数据、支持 DTS 音轨

除了备份存储数据，很多人购买 NAS 的目的是搭建家庭媒体中心。群辉 NAS 提供了一些第一方的软件来实现这个功能，比如管理数字音乐可以使用 Music station，而管理本地下载的视频、电影或者是剧集，则可以使用 Video Station。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/B97342B1-CEC3-4E7D-BEE1-F84EAA58B4D4.png)

不过，Video Station 也有一些自己的问题：一方面近期 Video Station 用来刮削媒体元数据的工具突然失效，下载的视频无法正常显示媒体数据；另一方面则是群晖的 Video Station 对音轨格式有所限制，无法直接播放 DTS、EAC3 等音轨格式的视频。

以往要解决这个问题，唯一可行的办法是将 Video Station 版本降级，再安装第三方的解码器。但这种方式有一个缺点 —— 不能更新套件。我们需要更加直接的解决方案，一方面解决刮削器无法正常获取媒体元数据的问题，另一方面则是让新版本 Video Station 可以直接播放 DTS、EAC3 等音轨的视频。

第一步：将你的群晖 NAS「root」
-------------------

要想充分发挥 Video Station 的潜能，就要从系统层面「动刀」。这就需要提权，通过超级用户进行操作，好在群晖并非像 Android 手机那样麻烦，而只需要通过开启终端，正常获取权限即可。

首先用浏览器登录你的局域网里面的群晖 NAS，在 DSM 的「控制面板」中「终端机 和 SNMP」，勾选「启动 SSH」功能，然后将端口号修改为非 22 端口（为安全考虑） ，然后点击应用。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/77ACE76D-5428-44F0-B305-5E22C9CCDE5E.png)

然后在你的电脑上使用 SSH 工具（Windows 上可以用 Windows Terminal，macOS 上可以用终端）来登录你的群晖 NAS。IP 选择当前局域网下群晖 NAS 的 IP（就是你登录 DSM 后台的地址），然后端口号选择刚才修改的端口（我使用的是 1022），账号是你登陆群晖 DSM 的账号，密码也是登录 DSM 的密码。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/3CE038B0-4990-408D-9DA2-E60B8D6C5AF6.png)

使用 SSH 工具，用用户名和密码登录你的群晖 NAS 之后，默认并不是 root 权限，在终端窗口中输入 `sudo -i`，然后再输入一次密码，就可以正常切换到 root 账户了。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/3E8E4AE9-D7EF-4F37-965F-1364C5C44E93.png)

不过目前这种临时 root 在每一次操作时都要进行提权，考虑到后面需要在 root 权限下进行比较频繁的操作，因此最好的办法是直接开启永久的 root 权限（以下操作在 DSM 6.2.2 下测试成功）：

首先还是在当前的 SSH 终端中，使用 `cd /etc/ssh` 切换到 SSH 目录下。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/5BA693E3-7212-4B7E-800B-2F92B12249ED.png)

紧接着给配置文件赋权：`chmod 755 sshd_config`

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/76EBE952-93FB-46CE-97F9-790B0C095CDD.png)

然后输入 `vim /etc/ssh/sshd_config` ，在终端中使用 vim 打开配置文件，然后在英文输入法下按键盘上的 `i` 键进入编辑模式，然后方向键移到 `#PermitRootLogin prohibit password`，然后将其改成 `PermitRootLogin yes`，改完之后按键盘上的 `ESC` 键退出编辑模式，然后输入`:wq` 保存编辑。

完成之后，手动在 DSM 界面中重启 NAS。

之后再次用 SSH 工具登录，并且再次切换到临时 root 权限，然后输入 `synouser --setpw root [你的密码]` 来设置你的 root 账户密码，如下图

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/B8096A3B-3140-4A22-8D49-B2EE20C9FEF2.png)

回车之后关掉 SSH 终端，然后将当前的 SSH 账户信息修改一下，将用户名改为 `root`，然后密码改成刚才设置的 root 密码，然后保存并登录，看到终端出现 `#` 符表示已经获得永久的 root 权限。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/BC4E7637-C488-4505-BCD3-95EF00DB4EA0.png)

第二步：让你的 Video Station 正确获取元数据
-----------------------------

从今年开始，几乎所有下载的影视剧在 Video Station 的显示信息都变成空白一片，原本的视频元数据也无法显示。导致这个问题的原因是其中元数据刮削器目前无法在中国大陆正常使用。

解决方式是以 root 权限修改群晖的 hosts 文件，重新指向刮削器可以正常访问的 IP 地址即可。首先先用 SSH 工具以 root 权限登录群晖。然后输入 `vim /etc/hosts` 打开 hosts 文件

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/C5CDA084-2C07-4F59-9FEA-8002D105810B.png)

英文输入法下在键盘上按下 `i` 键进入编辑模式，然后添加以下内容

```
13.226.238.76 api.themoviedb.org  
13.224.161.90 api.themoviedb.org  
13.35.7.102 api.themoviedb.org  
13.225.103.26 api.themoviedb.org  
13.226.191.85 api.themoviedb.org  
13.225.103.110 api.themoviedb.org  
52.85.79.89 api.themoviedb.org  
13.225.41.40 api.themoviedb.org  
13.226.251.88 api.themoviedb.org  
13.225.89.239 api.thetvdb.com  
13.249.175.212 api.thetvdb.com  
13.35.161.120 api.thetvdb.com
```

然后按键盘上的 `ESC` 键退出编辑，再输入`:wq` 保存并退出编辑器。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/5A5C1BBB-4D9A-45BD-8852-1CB52FD9D095.png)

这时候在浏览器上登录群晖 DSM，打开 Video Station 的设置，在「视频库」中找到对应的视频目录，然后点击「再次搜索所有视频信息」让刮削器重新启动，等一会儿 Video Station 中的视频元数据就会被成功下载并正确显示了。

第三步：让 Video Station 正常播放带专利音轨的视频
--------------------------------

根据群晖的说法，在 Video Station 上播放的视频中，音轨必须不含有专利编码，只能正常播放带有 AC3 、DD5.1 或者 AAC 的音轨。而如果视频音轨采用 DD+ 或者 DTS 这样的音轨将无法正常播放，如果在电视上使用将会跳转到第三方软件，至于 Web 端或者 iOS 端则直接显示为无法播放。

以前我们的做法是降级 Video Station 并安装第三方解码器来解决（缺点是套件不能升级）。今天要介绍的方法则一劳永逸 —— 使用第三方解码器通过 root 权限来替换 Video Station 的内置解码器。这样无需降级，即使升级到最新的 Video Station 套件也可以正常播放。

首先，我们需要在 DSM 中的「套件中心」中打开「设置」，在「套件来源」选项卡中新增一个社区套件源 synocommunity：

`http://packages.synocommunity.com`

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/2308C327-A78C-46F3-BD29-C43B0D488E09.png)

之后在「常规」选项卡中找到信任层级，选择「任何发行者」后点击确定，完成社群源 synocommunity 的添加。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/D95EA990-DCC1-4B3F-B64A-301D0ADDEBF7.png)

之后在「套件中心」-「社群」中找到套件「ffmpeg」，然后点击安装。由于 ffmpeg 本身比较大，所以安装时间会比较长。

如果你无法正常通过套件中心下载并安装 ffmpeg ，也可以手动安装 spk 来解决（需要信任「任何开发者」），不过由于群晖的处理器架构比较多，因此首先你需要在 [这个地址](https://github.com/SynoCommunity/spksrc/wiki/Architecture-per-Synology-model) 查询你的群晖设备的架构以及对应的包版本，然后再到 [这里下载](https://github.com/th0ma7/synology/tree/master/packages) 对应架构的 ffmpeg 安装包，而安装方式则是在「套件中心」右上角选择「手动安装」即可。

接下来打开 SSH 工具，使用 root 权限来登录群晖，我们需要做的就是将原先 Video Station 的视频解码库中的配置代码注释掉，换成我们自己安装的社区源 ffmpeg 中的视频解码库。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/6A8E9CCF-8CF7-4982-8929-45D589204B4B.png)

（接下来都是代码了，注意输入或者复制的时候不要出错）

首先修改 ffmpeg 包里的相关文件权限（SSH 终端里逐行输入回车）

`chmod +s /var/packages/ffmpeg/target/bin/ffmpeg`

`chmod +s /var/packages/ffmpeg/target/bin/ffprobe`

`chmod +s /var/packages/ffmpeg/target/bin/vainfo`

然后备份原来中 Video Station 内置的 ffmpeg（SSH 终端里逐行输入回车）

`sed -i'-old' -e 's/eac3/ZAAP/' -e 's/dts/ZAP/' -e 's/truehd/ZAPZAP/' /var/packages/VideoStation/target/lib/libsynovte.so`

`mv /var/packages/VideoStation/target/bin/ffmpeg /var/packages/VideoStation/target/bin/ffmpeg-old`

`mv /var/packages/VideoStation/target/bin/ffprobe /var/packages/VideoStation/target/bin/ffprobe-old`

`mv /var/packages/VideoStation/target/bin/vainfo /var/packages/VideoStation/target/bin/vainfo-old`

下面就是更改调用 ffmpeg 脚本（SSH 终端里逐行输入回车）

`echo "H4sICEoigl4AA2ZmbXBlZwCtU8tOwzAQvO9XLEmkPlAwrRCHVokqBOILOEUVctN1YtE8FFumEvDvOA9KSQInfEhsZ2ZnPN64F2wnc7bjKgWws8ChI8XIDK9YyeMXnpBiQmQlJUzzKiHd4NsdB8DF+4e7p0egOC3Q8TYOhiEynZUd5OpQJACWqILpDF5TeSCMIvRc9BON17jdwr6AmCuy7IWDMge0wzdlVQgLnjVLO1Qqhf5a1PUug6njH5e3Nx3SaQqc8Ot1V0iMl3CNCLxpZ9sKv6OiPfqEE3veosq4DnKzWF7NVcwP9Gw4LyU7nyeTDu2x1RmBTU56jUyXT7cciGoi9Hk/sf9zAz/ttNJGrDDyjNiO3lY/YyPqaO1zkK0cjzYrjKSgPuCgluzdUi+e1l7Lj7zm/afHzsh81hfqdQIpHkPrcV/kBKBIo+9bL281I9psP/q97Nk2/7WhG8TI/jdpGYaDv8A9fYZPjqtrMXcDAAA=" | base64 -d | gunzip > /var/packages/VideoStation/target/bin/ffmpeg`

`ln -s /var/packages/ffmpeg/target/bin/ffprobe /var/packages/VideoStation/target/bin/ffprobe`

`ln -s /var/packages/ffmpeg/target/bin/ffprobe /var/packages/VideoStation/target/bin/ffprobe`

最后解决原来有专利音轨的屏蔽，然后再调整权限（SSH 终端里逐行输入回车）

`sed -i'-old' -e 's/eac3/ZAAP/' -e 's/dts/ZAP/' -e 's/truehd/ZAPZAP/' /var/packages/VideoStation/target/lib/libsynovte.so`

`chmod +x /var/packages/VideoStation/target/bin/ffmpeg`

`chmod +s /var/packages/VideoStation/target/bin/ffmpeg`

`chown root:VideoStation /var/packages/VideoStation/target/bin/ffmpeg`

操作完成之后我们可以找一个带有专利音轨的视频播放一下。如果未来套件更新导致可能的无法正常播放，重新从「调用 ffmpeg 脚本」的部分再操作一次即可。

![](.evernote-content/41ABD746-8F09-4631-BDFD-DE8E7A3BEC91/535D75BA-7AF6-44B5-8A81-297434D3F435.png)

*参考来源：*

更多 NAS 内容：

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，让你的数字生活更精彩

---

[🌐 原始链接](https://sspai.com/post/60610)

[📎 在印象笔记中打开](evernote:///view/207087/s1/87e5a08f-3977-4007-b402-a58a61b01244/87e5a08f-3977-4007-b402-a58a61b01244/)