---
title: "探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端） - 知乎"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端） - 知乎.md
tags: [印象笔记]
---

# 探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端） - 知乎

# 探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端） - 知乎 --- 探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端）

---

# 探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端） - 知乎

---

探究抓包获取ClassIn课程回放直链的方法①（HttpCanary Android端）
============================================

一、探究背景
------

> ClassIn是翼鸥教育发布的一款功能强大的在线教室直播系统，凭借先进的多路视频通信技术，以及完善的全球布点建设云通信系统，ClassIn一直致力于在线教育技术的快发展。

在实际使用过程中，发现ClassIn历史课程回放仅支持「在线播放」，而没有「下载」功能，仅可在授课老师分享课程后方可获取下载链接。

这给学生「分享课程」等操作造成了极大困难。

因此，尝试通过其它手段获取回放直链，就显得尤为重要，而「抓包」思想是我首先想到的方法。

二、准备工具
------

* 一部Android手机（必须使用**Android 11以下**的设备，否则会有证书安装问题）
* 一个ClassIn账号以及一个有效的课程
* 如可以，建议给手机开启ROOT权限

三、方法讲解
------

### 1.安装软件

[1]ClassIn App

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/837B32CB-8FF0-4F97-9B04-C9BD2765939E.jpg)

ClassIn官网下载渠道

ClassIn官方提供下载渠道，可以直接在[下载窗口](https://link.zhihu.com/?target=https%3A//www.eeo.cn/cn/download.html)下载安装。

[2]HttpCanary App

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/56A8BDB3-46CB-42AF-BA29-C20632EAB371.jpg)

酷安原动态

由于在各大应用市场均未搜到本应用，同时原作者也已经停止了日常维护，这里提供酷安大佬“NEKOOKEN”分享的[下载链接](https://link.zhihu.com/?target=https%3A//url.ctfile.com/f/17101289-503900686-2ca6e2)（访问密码：3513）。

### 2.软件初步调试

[1]ClassIn App

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/0BA50690-9CB5-469B-B5DF-A68E3174B4A4.jpg)

ClassIn App 登录界面

将已有的ClassIn账号输入登录，进入「首页」界面，点击上方的「课程表」按钮，查看需要获取回放直链的课程。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/F02EA276-8869-4F32-8DC6-A441533081E6.jpg)

ClassIn App 课程表示例

[2]HttpCanary App

进入APP，依次安照初始化步骤，同意条款→配置VPN→安装根证书→移动证书到系统CA列表（如无ROOT权限，可以选择右上角的跳过）

注：在「安装根证书」步骤中，可能会弹出Android系统自带的「为证书命名」窗口，在凭据用途中请选择「VPN和应用」（即默认选项），如图（示例为Android 10 原生ROM）。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/90C81C10-A16D-4FF2-89D5-87ECE92D7AAB.jpg)

“为证书命名”示例

**请注意：如您使用Android 11设备，在安装证书时会提示必须在“设置”中安装CA证书，建议使用Android 11以下的设备或参考文末附录解决方法。**

若一切正常，即可进入首页界面，准备后续的抓包操作。

### 3.开始抓包

*\* 在开始之前，建议将不必要的应用移出后台，避免收集到不必要的抓包数据。*

①打开HttpCanary App进入首页，点击右下角按钮，开始抓包（可以通过是否有悬浮窗来判断是否已经成功开始抓包）。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/F1705270-64F2-496B-BF10-03BEB0F1176D.jpg)

HttpCanary App “开始抓包”示例

②打开ClassIn App，选择需要的课程，点击「回放观看」按钮。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/8CD9F749-4615-4927-A526-46F514025C01.jpg)

ClassIn App “回放观看”示例

③观看5-10秒时间，然后退出ClassIn App，重新进入HttpCanary App，再次点击右下角按钮，停止抓包。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/43641E42-9F51-48E8-B3BA-66FD4827C5F3.jpg)

HttpCanary App “停止抓包”示例

④分析抓包数据，观察记录里GET记录，可以发现有[https://playback.eeo.cn/](https://link.zhihu.com/?target=https%3A//playback.eeo.cn/)开头的链接，此即为课程回放直链，点击它查看详细内容。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/4EAEF234-A37F-4FCF-9AC4-3481BEDA5B59.jpg)

HttpCanary App “分析抓包数据”示例

⑤点击该URL，即可复制到剪贴板了。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/79691721-2D0A-47C5-9DD5-68D7C8AC63DA.jpg)

HttpCanary App “复制URL”示例

⑥在浏览器中打开测试，成功。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/B036B7DE-4D06-4574-B706-E8DF15EF2064.jpg)

“测试URL”示例

四、原理总结
------

本方法是通过HttpCanary利用VPN代理抓取ClassIn客户端的数据包后进一步分析得到。

相比之下，本方法步骤简单，技术含量较少，利于“小白化”操作。

同时也在研究其它方法实现其目的。

五、文末附录
------

### 1.ClassIn API

ClassIn官方提供使用「GitBook」发布的API，可供技术人员参考。

详细请[点击本链接](https://link.zhihu.com/?target=http%3A//www.eeo.cn/partner/api_manage/classin_api_book/zh-hans/)。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/014C0171-9FB4-489F-96D8-A5CA2B4C8F90.jpg)

ClassIn API简介

### 2.HttpCanary Android 11 安装证书问题

由于Android 11收紧了APP安装「CA证书」的权限，只能用户手动安装，因此导致了用户无法正常使用HttpCanary。

![](.evernote-content/E778FAA4-035A-40B3-9F9D-6A62AF4BB171/2BEDD9D5-50B3-4170-AE82-45C3B309229E.jpg)

Android 11 安装证书示例

具体解决方法，请参见酷安大佬“蓝瓦”所写的教程[点击链接](https://link.zhihu.com/?target=https%3A//www.coolapk.com/feed/22762279%3FshareKey%3DMjM5MDA2NThiMmRiNjExMGVkYjk~%26shareUid%3D670404%26shareFrom%3Dcom.coolapk.market_11.2.2)。

但是操作较为复杂，建议更换Android 11以下的设备进行抓包操作。

---

[🌐 原始链接](https://zhuanlan.zhihu.com/p/398055786?ivk_sa=1024320u)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8bdd759e-335d-4497-a7f2-06e9df0fdeb0/8bdd759e-335d-4497-a7f2-06e9df0fdeb0/)