---
title: "Mac 技巧：截取 Mac OS X 的登录屏幕"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Mac 技巧：截取 Mac OS X 的登录屏幕.md
tags: [印象笔记]
---

# Mac 技巧：截取 Mac OS X 的登录屏幕

# Mac 技巧：截取 Mac OS X 的登录屏幕 --- ![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/3B575F16-A

---

# Mac 技巧：截取 Mac OS X 的登录屏幕

---

![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/3B575F16-A282-4E71-B646-EC101F99B0A4.jpg)

OS X 在启动过程中、锁定的时候将会进入登录屏幕，在此登录屏幕用户可以进行验证身份，切换用户等操作。那么如何截取 Mac 的登录屏幕呢？其实这一操作在新版本的 OS X 上比较简单，在老旧的 OS X 版本上操作将会稍微复杂一些。

本文接下来我们就演示一下如何在最新的 OS X El Capitan 系统下和老旧的 OS X 系统下分别截取这一登录界面的屏幕内容。

截取 OS X El Capitan 的登录屏幕
------------------------

其实不光光是 OS X El Capitan，从 OS X Yosemite (10.10) 以后的 OS X 版本都支持「直接」截取，最方便的操作莫过于使用快捷键了。

1. 进入 OS X 的登录屏幕（开机过程中，锁定设备，或是快速用户时）。
2. 按下 Command＋shift＋3 快捷键组合。

该登录窗口的截图将出现在桌面上（「LW」前缀的 .PNG 格式文件）。

好简单，对不对？

![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/A431C700-F00E-4B76-80FD-68FA7FB80705.jpg)

截取较早的 OS X 版本的登录屏幕
------------------

如果你想截取较早的 OS X 版本的登录屏幕，那么就要稍微折腾那么一下。具体的过程需要涉及到使用 SSH 来远程登录到目标 Mac 电脑，然后借助 SSH 通道使用命令行截取登录屏幕的内容。下面我们就来看一看。

在开始之前，你需要允许目标 Mac 电脑可以使用远程登录来连接，还需要知道 Mac 电脑正在使用的 IP 地址。

![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/84D21335-43A6-4943-804E-E278A36B1F8B.jpg)

![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/182D25FB-4663-44F3-906C-4DFA237F6143.jpg)

1. 打开「设置」应用程序，选择「共享」项。
2. 选择左侧共享服务中的「远程连接」，OS X 会让你选择远程访问的权限，选择完毕后确定即可（此时该 Mac 已经启用远程连接服务，你可以使用 SSH 服务来连接到它）。
3. 记下窗口中的 IP 地址（如192.168.0.150）。
4. 在刚刚启用了 SSH 服务的 Mac 电脑上进入登录屏幕（锁屏或者是切换用户）。
5. 借助 SSH 通道使用上面记录的 IP 地址，从另一台计算机（Mac 或任何 SSH 客户端均可）登录到目标 Mac：

```
ssh mac@192.168.0.150
```

  6. 现在继续输入命令：

```
 screencapture ~/Desktop/login-screen-shot.png
```

大功告成！

![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/BC302549-FD6D-4EA0-A62A-A0F76253CC7A.jpg).PNG 格式截图文件仍然保存在你的 Mac 桌面上。

正如你所看到的，截取 OS X 较早版本的登录屏幕内容要相对「折腾」一下，新的版本 OS X，你只需要使用快捷键。OS X 在不停演化前行，也在不停地降低用户学习成本、不停地提升用户的工作效率。

*（本文编译自 [OS X Daily](http://osxdaily.com/2015/11/11/howto-take-screenshot-login-screen-mac-osx/)）*

#### 关联阅读

* [Mac 基础教程：如何玩转 Mac 截图](http://sspai.com/25978)
* [三种实用方案教你在 Mac OS X 上轻松截图](http://sspai.com/26841)
* [Mac 基础教程：如何更改 OS X 默认的截图文件格式](http://sspai.com/26321)
* [Mac 基础教程：去除系统截图名的日期后缀](http://sspai.com/28800)

文章来源 [少数派](http://sspai.com) ，原作者 [iTumbledSea](http://sspai.com/author/642336) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/26DF7B32-8FA1-4B0C-9A95-38C28E8FB295/F1DF79E2-9D84-43F3-B95A-71338BB4B6F3.jpg)](http://sspai.com/collection/photography)

---

[🌐 原始链接](http://sspai.com/31846)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b70f5452-438f-4d5a-96a1-2465bb614d96/b70f5452-438f-4d5a-96a1-2465bb614d96/)