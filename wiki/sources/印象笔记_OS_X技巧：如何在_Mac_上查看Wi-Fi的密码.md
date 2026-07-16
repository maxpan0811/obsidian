---
title: "OS X技巧：如何在 Mac 上查看Wi-Fi的密码"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/OS X技巧：如何在 Mac 上查看Wi-Fi的密码.md
tags: [印象笔记]
---

# OS X技巧：如何在 Mac 上查看Wi-Fi的密码

# OS X技巧：如何在 Mac 上查看Wi-Fi的密码 --- [![](.evernote-content/4E2FE149-C0F5-4FCC-8FD1-E0A6981E58FF/D7A3024

---

# OS X技巧：如何在 Mac 上查看Wi-Fi的密码

---

[![](.evernote-content/4E2FE149-C0F5-4FCC-8FD1-E0A6981E58FF/D7A3024C-6F1E-45F6-97B1-234A289740DE.jpg)](http://www.feng.com/iPhone/news/2015-08-10/OS-X-skills-how-to-view-the-wi-fi-password-on-Mac_621218.shtml)

![](.evernote-content/4E2FE149-C0F5-4FCC-8FD1-E0A6981E58FF/D7A3024C-6F1E-45F6-97B1-234A289740DE.jpg)

威锋网讯，在互联网的世界里，开始有越来越多的密码需要我们去记住，电脑的开锁密码、银行账户、还有 Wi-Fi 密码，苹果为此设计了 iCloud 钥匙串来帮我们记住这些密码。不过使用 Mac 上的终端来查看 Wi-Fi 的密码也很方便，尤其是别人问你家里 Wi-Fi 密码是什么，而你又忘记了的时候。

**如何在 Mac 上找到 Wi-Fi 的密码**

打开终端的办法有很多种，我们就不一一介绍。

1.要访问 Wi-Fi 密码你需要知道自己的管理员用户名，Mac 的密码，和 Wi-Fi 网络的名称。

在终端中，复制并粘贴以下指令：

security find-generic-password -ga “WiFiNAME” | grep “password:”

“WiFiNAME”更换为你要寻找密码的对应无线网络名称，例如你的无线网络名称为 xxx，则指令应该“长”这样：

security find-generic-password -ga “xxx” | grep “password:”

2.点击回车，然后系统会要求你输入用户名和密码。

这些信息是用于访问你的钥匙串，并提供你要找寻的密码，当输入正确的信息后，终端就会显示出对应的 Wi-Fi 密码。

![](.evernote-content/4E2FE149-C0F5-4FCC-8FD1-E0A6981E58FF/D82CB3D1-C030-4D77-BA95-2D99D222FF0F.jpg)

需要指出的是，这种方法只能够找到在这部 Mac 上曾经使用过的 Wi-Fi 的密码，对于之前从未连接过的 Wi-Fi，它是无法获取密码的。

[阅读全文](http://www.feng.com/iPhone/news/2015-08-10/OS-X-skills-how-to-view-the-wi-fi-password-on-Mac_621218.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2015-08-10/OS-X-skills-how-to-view-the-wi-fi-password-on-Mac_621218.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ab9f268b-981b-4afc-a403-83befc607d43/ab9f268b-981b-4afc-a403-83befc607d43/)