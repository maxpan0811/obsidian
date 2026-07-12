# 教程：用 Mac mini 搭建本地下载服务器 | Matrix 精选

---

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/91C25CEF-1EC0-4E36-ADE0-55C1C27347A3.jpg)

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/347F4CF4-502D-48D5-B5B6-A85CE839D714.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章排版有略作修改，[原文链接](http://matrix.sspai.com/p/d09314a0)。

*注：本教程仅适用于 Mac，其他操作系统流程类似但不相同。*

因为我买了新的 MBP，原来的 Mac mini 就闲下来了，而且笔记本合上盖子继续下载会影响散热，影响使用寿命，OS X原生也没有提供这样的设置。所以，我就用 Mac mini 搭建了一个本地的下载服务器，用于在我睡觉的时候继续下载。

**1. 目标设备的系统配置**

首先，请在路由器或系统中给目标设备配置一个固定的 IP 地址方便远程访问。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/6D788B94-2A29-4CA2-B1FC-21FF0CE7C620.jpg)  
在系统中打开需要的共享选项，自己添加一些需要共享的文件夹。 在远程管理中选择好自己需要的管理权限，我就直接全选了。由于远程共享中包含远程控制，所以不需要同时打开屏幕共享。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/E6B29396-930D-46C2-AD4C-8323C3FA9FA3.jpg)  
在节能器中调节选项以禁用自动睡眠功能。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/6E121406-7096-42A6-A08D-985199AB3E1F.jpg)  
测试 SSH、文件和屏幕共享的可用性。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/FCA065C6-000E-4C49-93BB-046B2EE09A75.jpg)![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/33246FC9-D7B5-4D0F-88D6-44408411B347.jpg)

**2. 在目标设备上安装 Aria2c 迅雷，将 WebUI 添加到其他设备的 Safari 书签中备用。**

* 迅雷就不说了，Aria2c 按照 [少数派这个教程](http://sspai.com/32167) 就好。
* 目前比较常用的 WebUI 有 [zahamza](http://ziahamza.github.io/webui-aria2/) 和 [YAAW](http://binux.github.io/yaaw/demo/)，自己选一个用，加在其他设备的书签栏就好。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/DFB759F9-82AA-4E10-9356-5DB7C120E284.jpg)  
选好后在设置中修改服务器地址，改成下载服务器的 IP，其他的选项自己看着改。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/AA85D69D-5594-4256-A144-D2B26532DD9C.jpg)  
确认可以正确连接到服务器，可以自己添加两个任务试试看（目标设备服务已经开启的情况下）。

也可以选择在目标设备中安装 WebUI，这样可以不用每次都去打开 Github 下载 [YAAW](http://binux.github.io/yaaw/)。方法是：

* 将其文件存入目标设备的 `/资源库/WebServer/Documents/` ，删除其中原有的文件。
* 终端运行`sudo apachectl start`，确认可以在其他设备中运行。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/D5CD1B22-2A56-4643-97A5-D1FA293069DB.jpg)

**3. 安装配套工具**

在所有需要访问下载的设备的 Chrome 中安装 [百度云下载助手](https://chrome.google.com/webstore/detail/baiduexporter/mjaenbjdjmgolhoafkohbhhbaiedbkno?hl=zh-CN) 和 [迅雷离线助手](https://chrome.google.com/webstore/detail/thunderlixianassistant/eehlmkfpnagoieibahhcghphdbjcdmen?hl=zh-CN)，这两个插件均有 Safari 版本，但由于系统限制，会出一些问题，所以需要使用 Chrome 在插件的设置中填写下载服务器的地址。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/01F00DAD-4608-4BF7-A969-CE7C7088CF85.jpg)  
iOS 上有一个收费 6 块的 Aria2c 控制器叫 [AVee](https://itunes.apple.com/us/app/avee-aria2-download-manager/id934291183?uo=4&at=10lJSw)，虽然不好看，但是挺好用的。其中自带了百度云和迅雷离线的脚本，可以直接添加此类任务。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/1B2A21C6-81D1-4E1B-AA51-610F5C3B63D2.jpg)在设置中填写下载服务器的地址。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/1CD69B4F-61C1-4620-944D-019CEFF9D48C.jpg)在用户脚本中安装百度云和迅雷离线助手。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/B37AC73C-CB47-4797-BE3F-83FA296D3B67.jpg)

**4. 设置开机启动**

使用系统自带的 Automator 新建一个应用程序，添加一个运行 Shell 脚本的操作。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/9D4D6FD0-E76B-4966-96E9-BCC2BEC5D2BB.jpg)输入以下代码：

```
/usr/local/Cellar/aria2/1.24.0/bin/aria2c --conf-path="/Users/megabits/.aria2/aria2.conf" -D
```

（注意：脚本中的路径可能因为你 aria2c 版本的不同而不同，请注意）

把这玩意随便保存在哪，然后添加到系统的登录项中。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/48B6F006-F68D-49FC-A38D-DEF3CA8909EA.jpg)

**5. 日常使用**

需要使用服务器时只需打开电源，等待开机。

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/1FDBDDE0-2AEE-42B0-AF6D-A0D47D21C3A3.jpg)  
打开书签中存好的 WebUI 进入管理页面。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/2FC583B9-030B-4150-8EF7-88758A78B4E8.jpg)  
进入百度云或网页版迅雷离线建立任务，或者只在 WebUI 中建立一个普通的下载任务。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/B8FEDF45-2A92-4053-A158-FFC4CA7204D9.jpg)去睡觉（逃

呼～～呼～～呼～～呼～～

最后，从共享文件夹中将服务器的文件下载到本地。  
![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/3803DD6A-E3CC-4F90-8A66-431B3234BA1D.jpg)SSH 连接到远程服务器关机，搞定。

```
ssh [ip]
sudo shutdown -h now
```

![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/A6270301-6EFD-4274-AC15-D63C55F7C9E7.jpg)

本教程结束，如果还需要什么其他的信息，Google 大法好。

（题图来自 [iMore](http://www.imore.com/mac-mini)）

文章来源 [少数派](http://sspai.com) ，原作者 [Megabits](http://sspai.com/author/707024) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/8A5003D7-017F-487F-96E8-76977071703C/95EAF35B-887B-4258-8559-E15785F0C557.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:BASE/destination:http://www.apple.com/cn/shop/product/HK2R2ZM/A/%E9%85%8D%E5%A4%87-smart-connector-%E7%9A%84-logi-base-%E5%85%85%E7%94%B5%E6%94%AF%E6%9E%B6-%E9%80%82%E7%94%A8%E4%BA%8E-ipad-pro?fnode=85)

---

[🌐 原始链接](http://sspai.com/35002)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d9ab69f8-0bcb-45cc-88b9-f7a23ad258a7/d9ab69f8-0bcb-45cc-88b9-f7a23ad258a7/)