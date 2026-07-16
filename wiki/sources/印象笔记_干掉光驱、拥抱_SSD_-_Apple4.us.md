---
title: "干掉光驱、拥抱 SSD - Apple4.us"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/干掉光驱、拥抱 SSD - Apple4.us.md
tags: [印象笔记]
---

# 干掉光驱、拥抱 SSD - Apple4.us

# 干掉光驱、拥抱 SSD - Apple4.us --- [干掉光驱、拥抱 SSD](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html "Pe

---

# 干掉光驱、拥抱 SSD - Apple4.us

---

[干掉光驱、拥抱 SSD](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html "Permalink to 干掉光驱、拥抱 SSD")
==============================================================================================

[riobard](http://apple4.us/author/riobard/ "Posts by riobard") on 2011-3-8, 11:36 [Comments (40)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html#comments "Comment on 干掉光驱、拥抱 SSD")

我几乎不用光驱，但它却占据了笔记本内相当大一部分空间（见图）。光驱用的是 SATA 接口，我决定把它拆出来，换上一块固态硬盘（后文称 SSD）。我垂涎 SSD 已久，但又有很多资料需要存储，在笔记本内保留一块大容量传统机械式硬盘（后文称 HDD）同时加装一块 SSD 做系统盘似乎是最完美的选择。

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/B4C4B698-8F9B-4298-BF2B-476D4BE7A6C0.jpg)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/inside-macbook)

13寸 Unibody MacBook 内部

目前市面上不同品牌、不同种类的 SSD 很多，品质良莠不齐。综合考虑性能、价格、可靠性之后，我选择了 Intel X25-M 第二代 SSD，容量 120GB 作为系统盘。这款 SSD 售价 230 加币（约合人民币 1500 元）。我买的时候碰上 Intel 搞活动，返现 35 加币。淘宝上看到这款的售价目前在 1400 左右。如果你不是很放心其他品牌的 SSD，买正品 X25-M 比较省心。记得看到过一个数据说过去几年中 Intel SSD 的退货率是最低的。

安装的时候面临一个选择：是把 SSD 装在硬盘槽还是光驱槽？OS X 的系统深度休眠（电池供电时，若电量不足时，系统会将内存内容写入磁盘然后整体掉电）后只能从硬盘槽正常唤醒，SSD 装光驱槽的话就不能使用深度休眠了。另一方面，苹果本的硬盘槽支持『突然运动传感器』(SMS, Sudden Movement Sensor)，如果笔记本意外滑落时系统可以将硬盘磁头收回（parking）以防落地震动中磁头划伤盘体。这意味着 HDD 需要留在硬盘槽，那 SSD 就只能去光驱槽了。

思前想后决定还是把 HDD 留在硬盘槽，毕竟资料更重要。SSD 不需要防震，而电池没电、深度休眠的情况也很少遇到。如果你选择此种方式，请在 Terminal.app 里执行命令 “`sudo pmset -a hibernatemode 0`”（不含引号）将 OS X 的休眠模式改为普通模式（内存内容不写入硬盘）。禁用深度休眠后，还有一个必要的操作是删除系统的内存镜像文件，方法是在 Terminal.app 中执行 “`sudo rm /var/vm/sleepimage`”。这个文件大小和你的内存容量一样，我的是 4GB。在寸土寸金的 SSD 上留这么大一个用不着的文件太浪费了。

其实有个两全其美的方法：部分笔记硬盘自带加速度传感器，可以在坠落时将磁头收回，无需依赖笔记本支持。比如希捷的 7200.4 有种型号 ST9750420ASG （注意最后结尾那个 G 字母，没有 G 字母结尾的型号不具有此功能）。希捷将这种特性称为『自由落体保护』（Free Fall Protection）。可以将这种型号的硬盘装在光驱槽里面。据说最好不要将这种型号的硬盘直接装在硬盘槽，因为硬盘上的坠落保护可能和苹果本的 SMS 冲突。如果你需要将这种型号的硬盘装在硬盘槽，建议关闭 OS X 的 SMS 特性，方法是在 Terminal.app 里面执行命令：“`sudo pmset -a sms 0`”。

HDD/SSD 不能直接装在光驱槽里，需要一个支架固定，还需要一个转接口以便能将 HDD/SSD 上的标准 SATA 接口连到笔记本主板上的微型接口上。[MCE OptiBay](http://www.mcetech.com/optibay/) 是一款专为苹果本设计的光驱槽硬盘支架，可以完美的将第二块 HDD/SSD 固定在光驱槽内。

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/10F41B9E-C986-4A7B-93E3-970342A6A9B2.jpg)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/mce-optibay)

MCE OptiBay 光驱槽硬盘支架

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/7194814F-8D2B-4CAF-8B5A-C4D4DE881941.jpg)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/x25m-in-optibay)

Intel X25-M SSD 安装在 MCE OptiBay 里面

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/F101127E-E9DA-472F-BC1B-101B1716BDEC.jpg)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/optibay-in-macbook)

MCE OptiBay 安装在 Unibody MacBook 的光驱槽中

MCE OptiBay 还附送一个 USB 外置光驱盒子，可以将拆下来的笔记本光驱变成一个移动光驱。这样偶尔需要用到光驱的时候也有办法解决，还可以给其他没有光驱但有 USB 接口的设备（如 MacBook Air、上网本之类）提供支持。

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/00095A92-178E-4B7A-85D8-14EC3CC9E5C7.jpg)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/mce-portal-cdrom-enclosure)

随 MCE OptiBay 赠送的 USB 光驱盒子

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/A2159FF1-D885-4590-A4B7-D5E422CEB090.jpg)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/usb-cddrive)

MCE OptiBay 附带的 USB 光驱盒子（安装好后）

OS X 自带的 DVD 播放器需要内置光驱才能正常启动和播放正版 DVD 电影，否则会报错并崩溃退出（见图）。MCE OptiBay 的解决方案也想到了这一点，提供了专门的软件包给 OS X 的 DVD 播放器打补丁避免这个问题。

[![](.evernote-content/0C361BA3-9AA3-4780-A888-6B6F49F46130/4BD6D950-6485-4A7E-B562-4001462E5042.png)](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html/win)

OS X 自带的 DVD 播放器不认外置光驱

MCE OptiBay 价格比较贵，需要 99 美元，国内貌似没有卖。需要购买的朋友可以[去它的官网订购](http://store.mcetech.com/Merchant2/merchant.mvc?Screen=CTGY&Category_Code=STORHDOPTIBAY)（需要注意选择适合你机型的型号）。另外一个选择是在淘宝上买替代产品。[@jjgod](http://blog.jjgod.org/2010/04/17/macosx-ssd-tweaks/) 和 [@cocoabob](http://www.cocoabob.net/?p=502) 都确认说有种叫 Fenvi 的光驱槽硬盘支架可以装进苹果本里，售价大概 100 多人民币。我之前在淘宝上问过这种支架的卖家，他明确说没有型号支持苹果本，所以不清楚情况到底是怎样。另外如果还需要移动光驱的话，要单独购买适合的 USB 移动光驱盒子。但这样 DVD 播放软件的问题就无法解决了。如果你经常需要播放正版 DVD 的话，需要使用其他的播放器软件，或者购买 MCE OptiBay 以获取相应的补丁。

装好 SSD 后，可以用 [SuperDuper!](http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html) 将原先的系统盘原封不动的复制过去。我因为之前装了太多杂七杂八的软件，所以选择了重新安装系统。可以用刚才做好的外置光驱插入恢复光盘安装。但光盘并不方便，噪音大，而且速度慢。我有一份零售版 Snow Leopard 系统安装 DVD，事先用 Disk Utility 将它 restore 到了一个 U 盘里面，从这个 U 盘启动安装。如果你用的 U 盘读取速度较快（有些山寨 U 盘很慢。我用过最好的是 [SuperTalent](http://www.supertalent.com/) 的，读取速度能达到 20MB/s 以上），安装系统时速度会比光盘快很多。由于新买的 SSD 没有初始化，在进入 OS X 安装界面后需要选择顶上 Utilities 菜单里的 Disk Utility 将 SSD 格式化成 Mac OS Extended (Journaled) 分区（不要选 case-sensitive 那个）后，安装程序才会认出 SSD 并将系统安装上去。

另外一个常见的优化措施是关闭文件系统的访问时间记录（atime）。正常情况下文件系统会记录每个文件的最后访问时间，也就是说每次读取一个文件的时候都伴随有相应的写操作。但 atime 是个鲜有用到属性，几乎没有任何程序会用到它。可以安全的关闭文件系统的 atime（起码我这样做了一年多以来并没有遇到任何问题）。在 Snow Leopard 之前的 OS X 系统，常见的方法是修改系统文件 `/etc/fstab` 加入一行 “`/dev/disk0s2 / hfs rw,noatime`”（不含引号）。但从 Snow Leopard 开始 OS X 已经不再使用 `/etc/fstab` 文件管理磁盘选项了，而是使用更为先进的 Launchd 进程。相应的关闭文件系统 atime 的方法是：在 `/Library/LaunchDaemons` 目录下创建一个文件，例如名为 `com.apple.hfs.noatime.plist`，然后编辑这个文件内容为：

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
        "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.apple.hfs.noatime</string>
        <key>ProgramArguments</key>
        <array>
            <string>mount</string>
            <string>-vuwo</string>
            <string>noatime</string>
            <string>/</string>
        </array>
        <key>RunAtLoad</key>
        <true />
    </dict>
</plist>
```

然后需要将这个文件的所有权设为系统 root，方法是在 Terminal.app 里运行 “`sudo chown root:wheel /Library/LaunchDaemons/com.apple.hfs.noatime.plist`”（不含引号）。之后重新启动系统后可以在 Terminal.app 里运行命令 “`mount`”（不含引号）检查是否生效。如果看到有一行（通常是第一行）是形如 “`/dev/disk0s2 on / (hfs, local, journaled, noatime)`”。如果你不明白这个优化到底在干什么，可以跳过不做这个优化，其实区别并不是很大。

装好系统后用 Xbench 大概测了下磁盘性能，果然是有质的飞跃。对平时使用影响最大的随机读取性能上比 HDD 有数量级的提升。由于此项进步，我这台第一代 Unibody MacBook 的 Xbench 得分甚至高过最新的 Sandy Bridge i5 的 MBP。实际使用的时候感觉也非常明显：开关机速度有大幅度提高；启动程序几乎是瞬间的事，甚至同时启动多个大型程序也可以在数秒内完成。这样的主观感受上的明显进步似乎最近几年非常罕见。

```
Sequential
    Uncached Write      112.69 MB/sec [4K blocks]
    Uncached Write      99.01 MB/sec [256K blocks]
    Uncached Read       40.08 MB/sec [4K blocks]
    Uncached Read       204.58 MB/sec [256K blocks]
Random
    Uncached Write      85.91 MB/sec [4K blocks]
    Uncached Write      102.74 MB/sec [256K blocks]
    Uncached Read       9.99 MB/sec [4K blocks]
    Uncached Read       173.11 MB/sec [256K blocks]
```

不常用到的文件都存在 HDD 里。如果一段时间没有访问 HDD，OS X 会自动关闭它。我之前将苹果本自带的较为安静的 5400 转日立硬盘换成了容量更大、速度稍快的 7200 转500GB 希捷 7200.4。问题是 7200 转的硬盘噪音非常大，为此饱受折磨。当 OS X 关闭掉它只用 SSD 时，『这个世界终于清静了』。

后话
--

硬盘和光驱在苹果本中占据了几乎三分之一的空间，成为了苹果本进一步缩小的瓶颈。

目前发达国家的家用网络带宽已经达到足够下载大型软件的程度了。在 OS X 上，App Store 的兴起将使通过光盘分发软件很快成为历史。不具有光驱的 MacBook Air 随机附送的系统恢复 U 盘（图）很可能会成为 Lion 的标准分发方式。即便苹果继续使用 DVD 盘片分发系统，使用 OS X 自带的 Disk Utility 工具可以很方便的自行制作系统安装 U 盘。重装系统也并不需要光驱了。

以 iTunes 音乐商店为代表的数字音乐消费方式已经在很大程度上替代了实体店购买 CD。目前通过 iTunes 音乐商店购买的音乐是经过压缩的、有少许音质损失，不少发烧友认为传统 CD 的音质更佳。但绝大多数人在绝大多数消费级耳机、音响上根本听不出 iTunes 的高比特率 AAC 音乐和 CD 有任何区别。有传闻说苹果正在和唱片公司讨论开发比 CD 音质更好的数字音乐（据说有 96kHz/48位采样，远高于 CD 的 44.1kHz/16 位采样），音乐 CD 的末日也不远了。

托网络带宽增长的福，以 Netflix、Hulu、iTunes 电影商店、Apple TV 电影租赁为代表的互联网视频服务正在逐步普及，用户可以足不出户就享受到点播电影服务。这些视频服务采用 H.264 技术压缩，在带宽允许的情况下通常提供比传统 DVD 电影稍好的画质。在互联网和蓝光的双重冲击下，DVD 也不会存在得特别久。高清蓝光视频也许是传统光驱的最后阵地，但不少人认为蓝光来得太迟了。苹果明确表示不会在任何设备上采用蓝光技术，那唯一可能的结局是光驱、光盘将和多年前的软驱、软盘一样，成为苹果平台上即将淘汰的技术。

传统硬盘的磁盘、电机、磁头等机械结构限制了其尺寸不能缩得更小。高速旋转的磁盘和磁头系统需要适当的安全保护，封装占了不少空间。独立的硬盘部件放入笔记本又需要考虑减震、易于更换等因素，稳固部件又占去了不少空间。SSD 没有这些限制。 转用 SSD 能够给笔记本设计留出更大空间： SSD 的存储芯片颗粒尺寸很小，而且由于没有机械部件，保护封装尺寸要小很多，而且电路板形状的灵活性很大。MacBook Air 中出现的 mSATA SSD 款型和笔记本内存条大小相当，占用空间小、布置灵活。这应该会是以后苹果本预装 SSD 的标准方式。将存储融合为主板的一部分后用户就不能自行更换了，这也意味着不需要相应的机构，简化了设计、节省空间，也降低了售后服务成本。现在 SSD 的价格和容量都还不能和传统硬盘相比，但 SSD 的价格似乎也遵循了摩尔定律，再过一两年就会有适宜的型号满足多数人的笔记本需求。

苹果说没有光驱、完全采用 SSD 的 MacBook Air 是『下一代的苹果本』。苹果本的进化方向已经很明确了。

---

[🌐 原始链接](http://apple4.us/2011/03/kill-cdrom-embrace-ssd.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bf6a0424-31e7-4f50-abc2-f8b09b6bb417/bf6a0424-31e7-4f50-abc2-f8b09b6bb417/)