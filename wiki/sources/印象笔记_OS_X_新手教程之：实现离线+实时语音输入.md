---
title: "OS X 新手教程之：实现离线+实时语音输入"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/OS X 新手教程之：实现离线+实时语音输入.md
tags: [印象笔记]
---

# OS X 新手教程之：实现离线+实时语音输入

# OS X 新手教程之：实现离线+实时语音输入 --- OS X 新手教程之：实现离线+实时语音输入 ====================== [![](.evernote-content/A3

---

# OS X 新手教程之：实现离线+实时语音输入

---

OS X 新手教程之：实现离线+实时语音输入
======================

[![](.evernote-content/A36F7BCF-6227-45B9-B310-7221A16AE362/C6DDE64A-0914-49BF-BF9B-BFB1AC40259C.jpg)](http://fullrss.net/r/http/bbs.feng.com/u.php?uid=2250262)

投稿by：[vanfam](http://fullrss.net/r/http/bbs.feng.com/u.php?uid=2250262) 来源：威锋网

PostTime：2015-01-14 23:43:53

[收藏](http://fullrss.net/r/javascript/www.feng.com/apple/osx/2015-01-14/void(0)) [已收藏](http://fullrss.net/r/http/bbs.feng.com/home.php?mod=space&do=favorite&type=news)

微博

[![](.evernote-content/A36F7BCF-6227-45B9-B310-7221A16AE362/998052F8-5559-47B0-8ED8-D59A6C5B3A73.jpg)](http://fullrss.net/r/http/weibo.com/weiphone?zwm=tech)

微信![](.evernote-content/A36F7BCF-6227-45B9-B310-7221A16AE362/81A589E1-D77E-4EC5-BDC6-CCF9A1B3CE49.png)*扫一扫加威锋官方微信号***微信号：weiphone\_2007** [加载中...](http://fullrss.net/r/http/www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml#comment)

[Twitter](http://fullrss.net/r/http/www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml#twitter) [Share](http://fullrss.net/r/http/www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml#Share) [Email](http://fullrss.net/r/http/www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml#Email) [Save](http://fullrss.net/r/http/www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml#Save) [Print](http://fullrss.net/r/http/www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml#Print)

> 虽然说语音输入的准确性没有键盘（或虚拟键盘）输入的准确性高，但是在一些场景下语音输入还是有一定的作用的。

以下为文章全文：

![](.evernote-content/A36F7BCF-6227-45B9-B310-7221A16AE362/CD9FEF9E-61E0-4A7B-933D-2516694DE97A.png)

  
　　威锋网讯，我们对于在 iPhone 和 iPad 上进行语音输入已经不陌生了，虽然说语音输入的准确性没有键盘（或虚拟键盘）输入的准确性高，但是在一些场景下语音输入还是有一定的作用的。今天为大家介绍的是如何在 OS X 系统中实现离线和实时语音输入，本教程由锋友 gguo 提供，资深用户可无视。  
  
　　苹果电脑从 Mac OS X 10.8 Mountain Lion 系统开始原生支持语音输入（默认是双击 fn 键启动，支持中文），比打字方便很多，而且也挺准的。但必须联网时才能用，你说完了，Mac 把声音传到苹果的服务器，服务器分析后再把文字传回 Mac。  
  
　　在 OS X Yosemite 中，你依然可以把苹果的听写数据库下载到电脑本地硬盘。这样不联网也能进行语音输入，而且也没有了此前和服务器通信造成的延迟，说话的同时就自动打字了。  
  

![](.evernote-content/A36F7BCF-6227-45B9-B310-7221A16AE362/15A3469C-6455-4506-A8BD-ABE4590E182C.jpg)

**（由于小编的 Mac 没有配置麦克风，所以会出现上方的提示）**

  
　　点击 Mac 屏幕左上角的苹果标志，下拉菜单里选择”系统偏好设置",面板里选择“听写与语音”，如上图所示。选择好语言，勾选"使用优化听写"。下面会出现数据库下载进度条和时间估算，设置好快捷键，方便以后调用。

---

[🌐 原始链接](http://www.feng.com/apple/osx/2015-01-14/The-OS-X-tutorials-offline-real-time-speech-input_605338.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/24acbf94-d24f-4fef-bd52-a65fc663c1f2/24acbf94-d24f-4fef-bd52-a65fc663c1f2/)