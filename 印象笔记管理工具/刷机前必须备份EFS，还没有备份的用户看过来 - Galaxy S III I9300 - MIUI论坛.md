# 刷机前必须备份EFS，还没有备份的用户看过来 - Galaxy S III I9300 - MIUI论坛

---

|  |  |  |  |
| --- | --- | --- | --- |
| [刷机前必须备份EFS，还没有备份的用户看过来](http://www.miui.com/thread-728527-1-1.html)     **[楼主](http://www.miui.com/forum.php?mod=viewthread&tid=728527)** 642232 2759 | *发表于 2012-9-3 15:37:57* | [复制](http://www.miui.com/thread-728527-1-1.html) |  | 跳转  |  |  |  | | --- | --- | --- | | 目前看到论坛上很多用户说按照官方教程刷机完以后手机没有信号，这就是efs信息丢失导致的，下面请大家刷机之前一定要阅读完此贴，不管是否刷机，都强烈建议先备份一遍手机的efs信息。  先来给大家科普下，EFS文件是用来存取手机IMEI串号、无线网卡MAC地址以及网络设置的重要信息组件，目前发现升级不明基带的ROM以及频繁刷机或者错误的双清方法会导致EFS信息丢失，IMEI串号被清空或置零，基带未知，无法使用移动网络等故障。  提供一个内核备份工具给大家，但是在使用的时候一定要注意，没有备份EFS的情况下，千万不要点击内核工具里面的“恢复EFS”，否则你还没有备份就已经丢失了全部信息。    备份步骤：  1.备份之前手机需要root（[点此查看ROOT教程](http://www.miui.com/thread-728484-1-1.html)），手机已经ROOT的请跳过此步骤  2.下载HC内核工具并安装到手机上     [HC内核工具.apk](http://www.miui.com/forum.php?mod=attachment&aid=NzU1ODAwfGU3NTBmNDA4fDE0MTcxNTQyNDF8MHw3Mjg1Mjc%3D) *(774.41 KB, 下载次数: 353261)*   3.打开软件，选择备份EFS分区到/sdcard/efs.img（SD卡根目录）     |  |  | | --- | --- | |  |  |    提醒：备份完毕后请及时把EFS信息复制到电脑上妥善保管    以上备份完成 后大家可以放心刷任何第三方ROM了，如果发现没有信号的情况只需要在安装一遍内核工具，然后恢复EFS即可，附上[MIUI for Galaxy SIII 官方刷机教程](http://www.miui.com/a-203.html) | |

---

[🌐 原始链接](http://www.miui.com/thread-728527-1-1.html)

[📎 在印象笔记中打开](evernote:///view/207087/s1/59cefad6-4b5d-429b-bfba-f6ba43be8ee6/59cefad6-4b5d-429b-bfba-f6ba43be8ee6/)