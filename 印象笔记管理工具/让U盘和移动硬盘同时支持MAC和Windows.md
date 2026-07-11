# 让U盘和移动硬盘同时支持MAC和Windows

---

让U盘和移动硬盘同时支持MAC和Windows
=======================

时间：2010-11-25 14:52 来源：网络收集 [收藏](http://sc.115.com/) 复制分享 [共有评论(0)条](http://www.ylmf.net/plus/feedback.php?aid=11605)

如果您的 U 盘、移动硬盘既要用于 PC 又要用于苹果电脑，Mac OS X 系统的 HFS+ 和 Windows 的 NTFS 格式显然都不行……HFS+ 在 Windows 下不识别，NTFS 格式的 U 盘、移动硬盘插在苹果电脑上只能读不能写。格式化成 FAT32 显然可以支持两个系统，但单一文件大于 4GB 就歇菜。

![](.evernote-content/30389AF5-6B34-41B9-9D91-6E2CFE605683/1D188A2D-4723-4458-BE5D-A66DBBA2C413.jpg)

　　但苹果电脑 Mac OS X 10.6.5 系统做出了一项意义重大的升级：支持 exFAT 磁盘格式，格式化成 exFAT 格式的 U 盘、移动硬盘在 Windows PC 上和苹果电脑 Mac OS X 系统下均能读写，而且支持超过单个体积超过 4 GB 的大文件。

　　下面是将 U 盘、移动硬盘格式化成 exFAT 格式的方法，以及 exFAT、FAT32、HFS+ 三种格式下同一块 U 盘的读写速度测试

![](.evernote-content/30389AF5-6B34-41B9-9D91-6E2CFE605683/9325FF0A-080D-4B0C-B503-C7034893F860.jpg)

　　苹果电脑 Mac OS X 系统下把U盘、移动硬盘格式化成exFAT格式

　　点击苹果电脑屏幕右上角的放大镜按钮，Sportlight 搜索“磁盘工具”，在磁盘工具侧边栏选择要格式化的 U 盘或移动硬盘分区，右侧选择“抹掉”标签，在格式下拉菜单里选择 ExFAT 即可。如上图所示。

![](.evernote-content/30389AF5-6B34-41B9-9D91-6E2CFE605683/0943DCD7-BC9C-43E7-88D4-FEACC4E30D24.jpg)

　　Windows 系统下把U盘、移动硬盘格式化成exFAT格式

　　Windows 7 和 Vista 默认就支持 exFAT 格式，如果是 XP 系统，要下载 KB955704 补丁：http://www.[microsoft.com/downloads/details.aspx?displaylang=zh-cn&](http://microsoft.com/downloads/details.aspx?displaylang=zh-cn&) amp;FamilyID=1cbe3906-ddd1-4ca2-b727-c2dff5e30f61

　　至于 exFAT 格式的 U 盘的读写速度，下面是同一块 U 盘在同一台电脑(我的 Macbook Pro)上的读写速度测试，测试软件为 以前介绍的免费软件：AJA System Test。

![](.evernote-content/30389AF5-6B34-41B9-9D91-6E2CFE605683/7B361C1A-C060-4A0C-91D9-DB41186C2062.jpg)

　　FAT32、HFS+、exFAT 格式的 U 盘读写速度测试

　　顺时针依次是 FAT32、HFS+、exFAT 格式下 U 盘读写速度测试结果，不太妙。所以：只把 U 盘和移动硬盘的一个分区(专门用于 PC、Mac 之间交换文件)格式化成 exFAT 就行了。

(责任编辑：黑云)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a642e82a-d611-4d79-907d-27355c2466ee/a642e82a-d611-4d79-907d-27355c2466ee/)