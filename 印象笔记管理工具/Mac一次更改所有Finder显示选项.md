# Mac一次更改所有Finder显示选项

---

Mac 一次更改所有 Finder 显示选项
======================

**
发表于
 2018-12-01

|

**
 分类于 
[Mac](https://dazzwoo.xyz/categories/Mac/)

|

**

在 Finder 中，更改显示选项仅对当前文件夹起作用，而有时我们想将全部文件夹都设置成自己喜欢的显示模式，手动一个个文件夹设置十分繁琐，这里有一个简便更改所有文件夹显示模式的办法。

1. 打开 Finder，点击 “⌘+↑” 数次，直到没反应可查看到磁盘的图标为止；

![](.evernote-content/D413EC0B-6B26-4A37-94FF-B07C87FCBB55/F252850C-3F76-460D-B6DA-CAC54D5FDD8D.jpg)

2. 选择需要的显示类型 (图标：⌘+1；列表：⌘+2；分栏：⌘+3)，再按⌘+J， 或者点击工具栏的小齿轮，打开 “查看显示选项”；

![](.evernote-content/D413EC0B-6B26-4A37-94FF-B07C87FCBB55/3C4B1E37-B21C-46E4-A854-32DCDA89CF8E.jpg)

在显示选项内调整好自己想要的效果，笔者这里设置为 “始终以列表显示方式 打开”、“字体大小 12” 等若干后点击下方 “用作默认”

![](.evernote-content/D413EC0B-6B26-4A37-94FF-B07C87FCBB55/61083DA5-C024-4455-ABAA-36BA0FA94F53.jpg)

3. 打开终端，打开终端界面输入以下命令，回车后根据提示输入你的密码再回车等待即可

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo find / -name .DS_Store -exec rm {} + ``` |

4. 等待第 3 步完成后，在终端输入

|  |  |
| --- | --- |
| ``` 1 ``` | ``` killall Finder ``` |

来重启 Finder，完成。

[# macOS](https://dazzwoo.xyz/tags/macOS/)
[# Finder](https://dazzwoo.xyz/tags/Finder/)

[** OpenVZ 平台魔改 BBR 一键脚本之 Rinetd 方式](https://dazzwoo.xyz/2018/11/29/openvzbbr/ "OpenVZ平台魔改BBR一键脚本之Rinetd方式")

[PyOne 一键安装脚本 for Debian 8+/CentOS 7 **](https://dazzwoo.xyz/2018/12/05/PyOne/ "PyOne一键安装脚本 for Debian 8+/CentOS 7")

---

[🌐 原始链接](https://dazzwoo.xyz/2018/12/01/findersort/)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c81bf95e-7e6a-4637-b6b1-ad01321b67af/c81bf95e-7e6a-4637-b6b1-ad01321b67af/)