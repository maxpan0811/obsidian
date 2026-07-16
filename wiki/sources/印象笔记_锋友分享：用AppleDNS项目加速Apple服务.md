---
title: "锋友分享：用AppleDNS项目加速Apple服务"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/锋友分享：用AppleDNS项目加速Apple服务.md
tags: [印象笔记]
---

# 锋友分享：用AppleDNS项目加速Apple服务

# 锋友分享：用AppleDNS项目加速Apple服务 --- 锋友“[多啦果粉](http://bbs.feng.com/forum.php?mod=viewthread&tid=10521792&

---

# 锋友分享：用AppleDNS项目加速Apple服务

---

锋友“[多啦果粉](http://bbs.feng.com/forum.php?mod=viewthread&tid=10521792&extra=page=3&filter=author&orderby=dateline&orderby=dateline)”表示，他最近在 Github 平台上找到了一个名为 AppleDNS 的项目，经过测试之后发现它的确可以加速 Apple 的服务。下面我们来看看具体情况。  
  
　该项目作者表示，AppleDNS 通过收集 Apple 在全中国几乎所有省级行政区的 CDN IP 列表，解决 App Store、Mac App Store、iTunes Store、Apple Music、iBooks 以及 TestFlight 在中国部分地区速度缓慢的问题。

![](.evernote-content/9B720F5D-0EFA-4A60-8169-268B7D52F0C9/853208E7-73E5-4D20-93CD-8DB6AA5C9CA2.png)

1.首先我们需要下载 AppleDNS，进入 AppleDNS 项目[首页](https://github.com/gongjianhui/AppleDNS)，点击页面右侧的 Clone or download，在弹出的窗口中点击 Download ZIP。

2.为了方便命令操作，请将下载后解压的项目移动至桌面。

3.打开终端，输入 cd ~/Desktop/AppleDNS-master

4.确认你的 ISP，电信用户输入 python [fetch-timeout.py](http://fetch-timeout.py) ChinaNet.json

联通用户输入 python [fetch-timeout.py](http://fetch-timeout.py) ChinaUnicom.json

移动用户输入 python [fetch-timeout.py](http://fetch-timeout.py) CMCC.json

输入上述命令后即开始进行测速，需等待数秒。

![](.evernote-content/9B720F5D-0EFA-4A60-8169-268B7D52F0C9/1717C64D-BA3A-41F7-8ED3-4370D8DA3311.png)  
  
![](.evernote-content/9B720F5D-0EFA-4A60-8169-268B7D52F0C9/052BA362-E537-4854-865C-7C35E8618C36.png)

5.导出 Hosts 配置

python [export-configure.py](http://export-configure.py) hosts

如果你是重度 Apple Music 用户，执行以下命令

python [fetch-timeout.py](http://fetch-timeout.py) Music.json

并将生成的结果替换掉之前 [aod.itunes.apple.com](http://aod.itunes.apple.com) 和 [streamingaudio.itunes.apple.com](http://streamingaudio.itunes.apple.com) 这两个域名中的 IP 地址。

![](.evernote-content/9B720F5D-0EFA-4A60-8169-268B7D52F0C9/78BD7149-EFBB-44B6-970F-285023D8B753.png)

6.鼠标选中终端输出的 Hosts 配置，并按 Command + C 拷贝。

7.在终端中输入以下命令并执行，根据提示输入密码：

sudo vi /etc/hosts

粘贴刚才生成好的 Hosts 配置

按下 ESC 键并输入 :wq 回车，即可保存 Hosts 的配置。

8. 清除 DNS 缓存，在终端窗口输入以下代码：

10.10.4 or later: sudo killall -HUP mDNSResponder

10.10 ~ 10.10.3: sudo discoveryutil mdnsflushcache

10.7 ~ 10.9.5: sudo killall -HUP mDNSResponder

10.6 ~ 10.6.8: sudo dscacheutil -flushcache

[阅读全文](http://www.feng.com/iPhone/news/2016-05-31/Feng-friends-sharing-use-AppleDNS-project-to-accelerate-Apple-services_648081.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2016-05-31/Feng-friends-sharing-use-AppleDNS-project-to-accelerate-Apple-services_648081.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/29aeff71-8fd4-4f2b-8b2e-7612caf2c81c/29aeff71-8fd4-4f2b-8b2e-7612caf2c81c/)