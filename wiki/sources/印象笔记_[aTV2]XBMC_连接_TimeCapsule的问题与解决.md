---
title: "[aTV2]XBMC 连接 TimeCapsule的问题与解决"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/[aTV2]XBMC 连接 TimeCapsule的问题与解决.md
tags: [印象笔记]
---

# [aTV2]XBMC 连接 TimeCapsule的问题与解决

# [aTV2]XBMC 连接 TimeCapsule的问题与解决 --- | | | --- | | [[aTV2]](http://bbs.weiphone.com/thread-htm-fid-

---

# [aTV2]XBMC 连接 TimeCapsule的问题与解决

---

|  |
| --- |
| [[aTV2]](http://bbs.weiphone.com/thread-htm-fid-351-type-498.html)XBMC 连接 TimeCapsule的问题与解决 |

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [kingjim](http://bbs.weiphone.com/u.php?uid=75418)  UID：75418  * 注册时间2008-01-19 * 最后登录2011-10-15 * 在线时间652小时  * 发帖25 * [搜Ta的帖子](http://bbs.weiphone.com/apps.php?q=article&amp;uid=75418) * 精华0 * we券70 * 贡献0 * 经验31 * 人气0  [访问TA的空间](http://bbs.weiphone.com/u.php?uid=75418)加好友用道具  级别: [小苹果](http://bbs.weiphone.com/profile.php?action=permission&amp;gid=18)  发帖  25  we券  70  贡献  0  经验  31  人气  0   * 关注Ta * 发消息 | 只看楼主更多操作 |  |  |  | | --- | --- | --- | |  |  |  | |  | * [倒序阅读](http://bbs.weiphone.com/read-htm-tid-2954037-ordertype-desc.html "倒序阅读") * 复制链接 * 使用道具 |  | |  |  |  | 楼主 发表于: 10-06  自己买ATV2的时候已经是Mac和TC的环境了，所以自然ATV2就连接到TC，装了XBMC后也就自然尝试连接TC直接播放硬盘上的影片。然而TC和一般的网络硬盘相比规格比较特殊，再加上小众产品可以查的资料也少，自己摸索着用SMB连接成功了。一开始的大半年看的都是1,2G大小的HDTV格式的片子，几乎完美，然而最近看5G朝上的720p时发现缓冲频繁的几乎不能看。同样的网上资料还是比较少，所以又不得不自己开始折腾。大致试了下面几种方法。   XBMC版本不好：更换后没有改善，由于原先没有看过720p的片子，所以不能保证一定会有那个过去的版本能彻底解决问题。放弃。  网络不给力：从2.4G换到5G换到有线，问题没有改善，理论上当前传输速度也不是瓶颈。放弃。  太多联网终端：好像在那里看到过这样的Hint，我试了关掉两台联网的电脑，包括iPhone，iPad，缓冲频度有所减少，运气好的时候片子具有可看性。然而看片子的时候挺难达到以上条件，最终放弃。  更换连接方式：SMB效率不好是早就知道的，但是TC不支持UPNP所以也没有过太多想法，查了一下忽然发现新版XBMC有新的AFP Client可以使用AFP，就考虑试用AFP连接，同样由于没有现成的资料说明自己就按界面尝试了，没有想到老不成功，就在要放弃之前，试了一下Reset所有设置（由于安装XBMC以后一直是更新，所以设置也有点乱了），新的Profile下竟然自动找到了AFP的TC了，连上去看看8G的片子竟然没有缓冲，至此问题完全解决。   由于看到少部分锋友有类似的问题所以抛砖一下（XBMC官方BBS帮助挺大的）。现在唯一还没有解决的是光纤输出AC3或DTS的时候声音有问题，由于用模拟的效果也还可以，自己的无线环绕耳机和BOSE的1+2系统都不是正规的功放，兼容性问题可能也无法解决所以就将就下去了，如果有同学在这方面有经验的话也希望能够Share一下。 |

---

[🌐 原始链接](http://bbs.weiphone.com/read-htm-tid-2954037.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6e289f48-10ee-4c88-9449-9c683834c8fe/6e289f48-10ee-4c88-9449-9c683834c8fe/)