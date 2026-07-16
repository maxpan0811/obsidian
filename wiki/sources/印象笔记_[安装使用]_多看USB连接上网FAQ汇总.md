---
title: "[安装使用] 多看USB连接上网FAQ汇总"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/[安装使用] 多看USB连接上网FAQ汇总.md
tags: [印象笔记]
---

# [安装使用] 多看USB连接上网FAQ汇总

# [安装使用] 多看USB连接上网FAQ汇总 --- [[安装使用]](http://www.duokan.com/forum/forumdisplay.php?fid=47&amp;filter=

---

# [安装使用] 多看USB连接上网FAQ汇总

---

[[安装使用]](http://www.duokan.com/forum/forumdisplay.php?fid=47&amp;filter=type&amp;typeid=17) 多看USB连接上网FAQ汇总
==========================================================================================================

|  |
| --- |
| [返回列表](http://www.duokan.com/forum/forum-47-1.html) **1**[2](http://www.duokan.com/forum/viewthread.php?tid=1777&amp;extra=&amp;highlight=%E5%A4%9A%E7%9C%8B%2B%E4%B8%8A%E7%BD%91&amp;page=2)[下一页](http://www.duokan.com/forum/viewthread.php?tid=1777&amp;extra=&amp;highlight=%E5%A4%9A%E7%9C%8B%2B%E4%B8%8A%E7%BD%91&amp;page=2) [发帖](http://www.duokan.com/forum/post.php?action=newthread&amp;fid=47)[回复](http://www.duokan.com/forum/post.php?action=reply&amp;fid=47&amp;tid=1777) |

|  |  |  |
| --- | --- | --- |
| [多看软件开发组](http://www.duokan.com/forum/faq.php?action=grouppermission&amp;searchgroupid=20)  主题  13  精华  1  积分  680  注册时间  2010-4-30 | ***1*楼*跳转到 »*[倒序看帖](http://www.duokan.com/forum/viewthread.php?tid=1777&amp;extra=&amp;ordertype=1)** [打印](http://www.duokan.com/forum/viewthread.php?action=printable&amp;tid=1777) 字体大小:tT  [grm](http://www.duokan.com/forum/space-uid-52.html)*发表于 2010-8-23 10:29* | [只看该作者](http://www.duokan.com/forum/viewthread.php?tid=1777&amp;page=1&amp;authorid=52)  |  | | --- | | *本帖最后由 **多看**总管 于 2010-8-31 09:43 编辑*   本帖集中汇总**多看** KINDLE 通过USB**上网**的一些问题及相关解决办法  Q:USB连接**上网**是干什么用的？  A:USB连接**上网**，是为Kindle上的**多看**系统连接互联网，并下载书籍以及看RSS新闻等功能所采取的一种**上网**方式。  Q:USB连接**上网**的原理是什么？  A:Kindle将usb连接作为一个USB网卡设备,在PC上会以USB网卡方式出现,然后,连接的PC机,通过Internet 连接共享（Internet Connection Sharing）方式，将 Kindle发送来的包，通过NAT( Network Address Translation )，将数据包路由到公网上，从而实现Kindle**上网**。  Q:为什么我Kindle现在看不到U盘了？  A:进入联网模式后，USB连接线，是作为USB网卡设备出现的，而不是USB大容量存储设备出现的，因此，不会看到U盘的标志。  Q:实现USB**上网**的最简单步骤是什么？  A:断开Kindle的USB连接，双击下载来的“USB连接共享.exe”文件，然后在后继窗口中选择接受，假如安装了防火墙或杀毒软件，可能会弹出安装程序中有木马的提示，请选择信任，假如没有选择信任或放过等操作，请先断开网络后，关闭杀毒软件或防火墙后再次双击下载来的“USB连接共享.exe”文件进行安装。安装完毕后，插上USB连接线，假如弹出发现新的USB设备的安装向导，请选择自动安装软件后点下一步进行安装。驱动安装完毕后，大概等3分钟后，在**多看**系统主目录中点击menu，选择“进入书城”，正常下，应该可以进入书城。  Q:按上述步骤操作后，还是不能**上网**，我该怎么做？  A:查看 计算机名，请确保名称长度总共不超过4个汉字或8个英文字符。在服务中，查看是否存在名称为Duo Kan Share Lan Service的服务，并且服务状态为已启动，未启动，请手工启动。在设备管理器->网络适配器 中，是否存在名为“Linux USB Ethernet/RNDIS Gadget“的网卡，不存在或存在类似的名称的网卡，请先卸载并重新安装USB连接共享.exe。  Q:假如重新安装多次USB连接共享.exe，还是不能**上网**怎么办？  A:暂时关闭第三方防火墙及杀毒软件，重新安装USB连接共享.exe，然后再开启杀毒软件及防火墙。  Q:假如上述办法都试过了，还是不成，或者不想关闭杀毒软件或防火墙，有没有纯手工的方式设置方法：  A:Win7或Vista下操作步骤：在**多看**系统主目录中点击menu，选择“进入书城”，稍后，假如没有安装KINDLE的网卡启动，会提示一个发现新的USB设备的安装向导，请使用相关的INF文件安装驱动，找不到的话，将USB连接共享.exe用WinRar解压缩，使用里边附带的Kindle.INF。成功安装驱动后，在设备管理器->网络适配器 中，会存在名为“Linux USB Ethernet/RNDIS Gadget“的网卡。假如设备上带叹号，请重新安装驱动。控制面板->网络和 Internet->网络和共享中心 页面内，在访问类型： Internet 连接：XXX(例如为 本地连接), 点击XXX，属性->共享，在“允许其他网络用户通过此计算机……”前的框内打上勾。然后点确定。然后在访问类型： 无法连接到网络 连接：XXX(例如为 本地连接 #2), 点击XXX，属性->网络，连接时使用：应为类似Linux USB Ethernet/RNDIS Gadget。修改IPV4地址为192.168.177.1。大概等3分钟左右，即可连接网络。  Win2000,Winxp下操作步骤：断开USB连接。桌面上在网上邻居点击右键->属性应该能看到一个本地连接，这个是能连接公网的网卡（下面称为公网连接）。连接KINDLE，等大概5秒，此时应该除了公网连接外，多出另一个本地连接来，（下面成为KINDLE连接），假如出现USB设备的安装向导，请安装KINDLE网卡驱动。在公网链上右键点击属性，选择高级，在 “允许其他网络用户通过此计算机……” 前打勾，并确定。 然后在KINDLE连接上将IP地址改为192.68.177.1。大概等3分钟左右，即可连接网络。   Q:Win7下安装USB连接共享.exe，但并不存在名称为Duo Kan Share Lan Service的服务。  A:在控制面板->用户帐户和家庭安全->更改 Windows 密码->更改用户帐户控制设置 窗口下。将滑动条从默认，拖动到最底下的从不通知，然后点确定，重启后再次安装安装USB连接共享.exe 即可。   Q:既有无线网卡，又有有线网卡怎么办？  A:有些人连接到笔记本电脑上时，会既有有线网卡，又有无线网卡，Duo Kan Share Lan Service服务，会找个能**上网**的连接启用连接共享，因为一台电脑假如两个网卡都能**上网**，那一般会随便找一个连接网络，假如共享的不是需要共享的网卡，那就可以断开那个网卡或临时禁用掉。 | |

---

[🌐 原始链接](http://www.duokan.com/forum/viewthread.php?tid=1777&highlight=%E5%A4%9A%E7%9C%8B%2B%E4%B8%8A%E7%BD%91)

[📎 在印象笔记中打开](evernote:///view/207087/s1/0313f638-f430-45f0-88e6-20ad415aa970/0313f638-f430-45f0-88e6-20ad415aa970/)