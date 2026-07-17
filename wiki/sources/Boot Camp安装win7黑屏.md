---
title: Boot Camp安装win7黑屏
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/Boot Camp安装win7黑屏.md
tags: [印象笔记]
---


|  |  |
| --- | --- |
| 你必须在mac下删除一个驱动。。。  1.用bootcamp对硬盘进行分区，插入windows7的安装盘开始安装  2.进入安装后选择bootcamp分区，要格式化成NTFS才能继续  以上相信大家都知道，接下来的就是问题所在了  3.windows7开始安装，前面按照正常步骤安装，当进度条快要结束，也就是安装的最后一步时，会突然黑屏，过一会便重启。这时候如果你不进行任何操作那在windows7的logo出现后就只是黑屏了。  4.正确方法是当这次重启时按住option键选择光驱启动，按任意键运行CD。在“安装”（install now）的左下方有两行小字。选择“repair your computer”忽略所有弹出的提示，当出现一个列表时选最后一个“Command Prompt"  5.输入DEL C:\WINDOWS\SYSTEM32\DRIVERS\ATIKMDAG.SYS 删除驱动后再选择重启  6.正常进入windows，用Mac安装盘安装驱动   回答完毕。。。坛子里有个兄弟早就发帖说过了    |  | | --- | | 

<!-- [摘要] 规则提取，如需全文请查看 vault 原始笔记 -->