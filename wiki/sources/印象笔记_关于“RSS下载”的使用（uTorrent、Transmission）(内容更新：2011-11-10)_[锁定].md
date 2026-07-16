---
title: "关于“RSS下载”的使用（uTorrent、Transmission）(内容更新：2011-11-10) [锁定]"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/关于“RSS下载”的使用（uTorrent、Transmission）(内容更新：2011-11-10) [锁定].md
tags: [印象笔记]
---

# 关于“RSS下载”的使用（uTorrent、Transmission）(内容更新：2011-11-10) [锁定]

# 关于“RSS下载”的使用（uTorrent、Transmission）(内容更新：2011-11-10) [锁定] --- 一、什么是“RSS下载”？ “RSS下载”是类似于购物车的概念，把想要下

---

# 关于“RSS下载”的使用（uTorrent、Transmission）(内容更新：2011-11-10)  [锁定]

---

一、什么是“RSS下载”？  
  
   “RSS下载”是类似于购物车的概念，把想要下载的种子加入“RSS下载”，软件在一定时间间隔后即可自动开始下载，无须再通过“下载 → 添加 → 确认等繁琐操作”，只需一次点击即可完成。“RSS下载”其实是一种的RSS订阅，下载内容由您自己管理。  
  
二、为什么要使用“RSS下载”？  
    
   1、通常的下载步骤：下载种子 → 打开软件（WebUI）→ 添加种子，步骤繁琐；  
   2、如果需要远程添加，由于下载机在内网，很多人无法使用 WebUI；  
   3、使用手机浏览，浏览器也无法正常使用 WebUI；  
   4、以前的RSS订阅无法充分过滤出自己想要下载的内容。  
  
三、如何使用“RSS下载”？  
  
   首先，你的软件需要支持RSS订阅，并且可以自动下载订阅内容，比如 μTorrent 。  
  
    1、点击页面顶部的用户信息栏的[[RSS下载]](http://chdbits/myrss.php)，如图所示  
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/53E367D6-EAC8-46F5-A7E9-87B11BC039A8.png)   
  
       当出现如下图页面时，复制自己的订阅地址。  
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/18EE34EF-8BB1-4FBB-BA84-C26A3E4323E5.png)  
  
       将这个RSS订阅地址粘贴到 μTorrent ，如下图所示：  
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/37339469-9570-4756-B2BF-7C2CBD4155FA.png)  
  
       修改你的RSS自动下载路径，如下图所示：  
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/1E257F5C-D060-42DF-8A73-C2540C54217B.png)  
  
   如果不修改的话，系统会默认为C盘相应路径下，那到时候你可能就有麻烦了。。。  ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/AC3C67C4-595C-4A4F-AEAD-80FC7DB65321.gif)   
  
          2、当完成 μTorrent 的RSS订阅地址添加后，就可以回到PT的种子浏览页面来选取我们想要加入“RSS下载”的种子了！ ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/AC78B9F9-E6DC-46B7-9BAA-B2812C9901F0.gif)   
  
                 1）如果是待添加则显示这个图标：   
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/EA0C02A0-D112-48E5-A8B0-2F6017B47181.png)  
  
                 2）如果已添加，但你的 μTorrent  还没自动开始加入下载，则会显示这个图标：  
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/99A8C978-8229-4FE1-B1FD-CD357733593C.png)  
  
                 3）当你的 μTorrent  已开始自动下载或已下载完毕，则会显示这个图标：  
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/2E130F9C-91C2-4D4B-BCE7-928BFC60B3B2.png)  
  
                 4）当 μTorrent 开始自动下载时，会如图显示：                
           ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/7576FD14-7337-4523-BACB-169A43013239.png)  
  
                 5）当你在远程控制时，比如使用手机、平板电脑、笔记本电脑操作时，可以通过查看[[RSS下载]](http://chdbits/myrss.php)，以随时了解家中或单位电脑的种子状态和下载进度，并且能通过点击“RSS下载”的状态小图标来进行RSS种子的移除操作：  
                       ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/D866197D-7500-4CE1-96BB-B48E38849BBF.png)  
  
  
四、对于RRS下载在 Transmission 客户端的使用方法（感谢热心网友 ElviN 提供！）  
  
transmission设置文件settings.json增加／修改以下三项：  
"watch-dir": "/whatever/watch",   
"watch-dir-enabled": true,  
"trash-original-torrent-files": true,  
保存，启动transmission  
注意，要先停止transmission再修改保存。  
  
需要python2.4以上；  
下载feedparser: <http://code.google.com/p/feedparser/>  
下载RSSDler: <http://code.google.com/p/rssdler/>  
分别解压缩；  
分别进入解压生成的目录，以root权限执行：  
python setup.py install  
  
建立工作目录：  
~/.rssdler  
创建config.txt文件，以下是我的，很简单：  
  
[global]  
urllib = true  
  
scanMins = 15   
minSize = 0  
maxSize = 0  
  
log = 1  
logFile = downloads.log  
verbose = 0  
  
runOnce = False  
saveFile = savedstate.dat  
  
[CHDbits]  
link = [http://chdbits.org/torrentrss.php?myrss=1&linktype=dl&uid=yyyyyy&passkey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx](http://chdbits.org/torrentrss.php?myrss=1&amp;linktype=dl&amp;uid=yyyyyy&amp;passkey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)  
active = true  
directory = /whatever/watch  
  
保存，后台运行rssdler：  
rssdler -d  
  
其中link = 那一串换成你自己的。  
  
  
**五、常见问题  
  
问：为什么我无法删除已经添加的？也无法添加？  
答：“RSS下载”的显示有缓存，实际上已经操作成功。  
  
问：为什么我添加了，过了好一会也没有开始下载？  
答：软件需要在一定时间内更新了RSS之后，才会开始下载。软件默认设置情况下，μTorrent 的更新时间是15分钟。如果有必要，请在高级设置中设置更新时间(rss.update\_interval)，但是考虑到服务器的压力，不建议设置时间过短。  
  
问：为什么我的手机、电脑的浏览器看不到这个新增的“RSS下载”图标呢？  
答：请先清除您的浏览器的内容缓存，然后再刷新页面就有了。  
  
问：如果我用的是 https 方式登录的网站，点击“RSS下载”后，种子下载链接也是 https 协议地址的吗？  
答：是的，但需要手动添加s。**  
      **请注意：能用http的尽量使用http吧，因为https对网站服务器的性能开销会比较大。**  
  
其他问题后续补充。。。  
  
  
**备注：文章中部分操作说明参考了 HDChina 站的相关文章，在此表示感谢！** ![](.evernote-content/BCA07EAC-0C44-44C0-8F6B-92291BF3EF11/BF3E4CB1-586E-41D3-9CDD-1846716E74AF.gif)  

最后被[**Rock**](http://chdbits.org/userdetails.php?id=2)编辑于2年4月前

---

[🌐 原始链接](http://chdbits.org/forums.php?action=viewtopic&forumid=12&topicid=49598)

[📎 在印象笔记中打开](evernote:///view/207087/s1/94761dc5-7f9d-4f1a-9036-041a14be8897/94761dc5-7f9d-4f1a-9036-041a14be8897/)