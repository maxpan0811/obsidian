# 别被生态绑架，这两个 app 让你的 Windows 和 iPhone 也能同步剪贴板

---

智能摘要

Apple生态中的跨设备剪贴板同步很实用，比如你可以在iPhone上复制文本、然后在Mac上直接粘贴。虽然体验不如Apple生态那样流畅且只支持文本内容，但用起来也还算方便。设置界面，在「辅助功能」模块中设置自动运行该动作，防止忘记启动导致剪贴板数据丢失。发送剪贴板到iOS，除了前文提到的Quicker，还需要借助Bark这款应用。iPhone」这个动作，在其编辑界面右侧的「变量定义」中找到token变量，在变量的默认值中填入刚刚获得的Device Token，保存并退出。

原文约 1417  字  | 图片 9 张 | 建议阅读 3 分钟 | [评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2023-03-04&nu=508441ca-b197-4139-8c25-72174a0bde3e&fr=myyxbj&ud=328ef&v=2&sig=C0638AF80F3A6910BE3B9513A76F20F6)

别被生态绑架，这两个 app 让你的 Windows 和 iPhone 也能同步剪贴板
===========================================

原创 Burgess 少数派

Apple 生态中的跨设备剪贴板同步很实用，比如你可以在 iPhone 上复制文本、然后在 Mac 上直接粘贴。

所以从 Mac 切换到 Windows 后我就一直在寻找一种可以实现 Windows 与 iOS 剪贴板同步的方法，前前后后尝试了快贴、clipboard-online 等工具但效果都不理想，直到使用了 Quicker 这款应用才逐渐摸索出一套可行的方案。

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/860F5AA7-C54B-485C-89DF-A2B69B997DCD.jpg)

虽然体验不如 Apple 生态那样流畅且只支持文本内容，但用起来也还算方便。关于 Quicker 的基本使用，请参看官方的软件使用教程。

接下来，我将分别从 iOS 和 Windows 两个平台介绍该方案。

**▍****iOS to Windows**

在进行操作前，请确保你已通过邮箱注册并登录了 Quicker，然后进入 Quicker 的动作页，按照下图所示步骤打开推送服务，接着点击推送工具进入会员中心，即可看到与你的账号绑定的推送验证码，请妥善保管。

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/5B2E6025-8620-4613-B446-52B8FAA00D52.png)

打开推送服务

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/4D296B26-2808-4F42-820B-81EB02012042.png)

推送验证码

接下来，在 iOS 设备中安装「发送到电脑」这个快捷指令，进入编辑界面后，根据提示填写 Quicker 账号的邮箱和前文获取的推送验证码，这样你就可以就可以在 iPhone 上直接复制文本运行该快捷指令，或者选中文本通过共享表单运行、将内容发送到 Windows 设备。

如果你的 Windows 处于输入状态，接收后系统会直接将内容粘贴到光标处。需要注意的是，在连续运行多次后 Quicker 推送服务器的原因可能会出现运行错误，若出现此类错误请等待几秒钟后再尝试。

为了获得更流畅的使用体验，我们可以将上文的快捷指令添加到「辅助触控」中，具体方法是进入 iPhone 设置，然后依次点击「辅助功能 > 触控 > 辅助触控 > 自定义顶层菜单」添加该快捷指令。添加完成后，就可以在需要同步剪贴板时点击屏幕上的辅助触控球，快速运行快捷指令发送内容了。

另外建议在 Windows 端安装一个剪贴板管理工具，推荐使用「剪贴板」这个 Quicker 动作，它非常好用而且不需要额外安装应用，你可以查看、搜索、收藏历史剪贴板，同时当剪贴板内容有变化时它会显示通知。在动作安装完成后，记得进入 Quicker 设置界面，在「辅助功能」模块中设置自动运行该动作，防止忘记启动导致剪贴板数据丢失。

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/7C3934A8-55A1-4427-BB84-9C542FE81872.png)

设置自动运行动作

**▍****Windows to iOS**

要想从 Windows 发送剪贴板到 iOS，除了前文提到的 Quicker，还需要借助 Bark 这款应用。

首先，从 App Store 下载 Bark 并授予它通知权限，接着进入设置页面，可以看到 Device Token（这是你当前设备的真实 Token，请妥善保管），复制 Token 后可以现学现用，按上文的操作直接发送到 Windows 的剪贴板中。

最后，在 Quicker 中安装「发送到 iPhone」这个动作，在其编辑界面右侧的「变量定义」中找到 token 变量，在变量的默认值中填入刚刚获得的 Device Token，保存并退出。

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/68F4376C-AB65-42FC-B83C-907E8484172E.png)

填入 Device Token

同步剪贴板时，选中要发送的内容（如果没有选中则使用剪贴板中的内容）然后点击运行该动作，即可将内容发送到你的 iPhone 上。当收到 Bark 的通知时，长按它就可以直接复制内容。如果内容是 URL 还会自动打开。同时你可以在 Bark 中查看历史消息，不必担心不小心清除了通知。

**▍****总结**

通过以上两部分的内容，我们就实现了 Windows 与 iOS 的剪贴板同步，虽然无法与 Apple 全家桶的跨设备体验媲美，有些人也可能难以理解这么麻烦为什么不直接用 Apple 全家桶——也许你是对的，但还是希望大家都能够不被某个品牌的生态所绑架，成为自己设备的主人。

**相关链接**

快捷指令「发送到电脑」：

https://www.icloud.com/shortcuts/76733f5517dc4b1180b4235d51e04db6

Quicker 动作「剪贴板」：

https://getquicker.net/Sharedaction?code=9ec53d43-5539-4571-6886-08d8c752bfcb

Quicker 动作「发送到 iPhone」：

https://getquicker.net/Sharedaction?code=d1111e17-77b8-41d1-178f-08db13055cfd

原文链接：

https://sspai.com/post/78530?utm\_source=wechat&utm\_medium=social

作者：Burgess

责编：克莱德

******/****更多热门文章****/******

[![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/1A471B4E-A87F-4CB3-835C-21EA7F0C3C57.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247550868&idx=1&sn=4faf016cbc2dd024cde922ef1b3bcc74&chksm=fdb3f2fecac47be86d93b77ab6410e5e0607419ce9d58e5f7b610ac24bf4e0c04d77a31d0f3c&scene=21#wechat_redirect)

[![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/16F91DAB-5B40-4094-ADB5-792C533244E5.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247550826&idx=1&sn=a74081d7b3eb01333b6d0ac7ff6f2eb8&chksm=fdb3f200cac47b16d8b41ff739ffa274e481b0ea6084b9f7e5567604dd9e96d086a42d63a0da&scene=21#wechat_redirect)

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/E3A387B1-7AAF-4A9B-A540-4768D69A67F9.png)

![](.evernote-content/381B1F06-056C-4093-B896-B513CF323C51/D9D43FFF-F1B0-4B51-8BCF-DBD5A99B750E.gif)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247550886&idx=1&sn=5593185f606fb9a1ece31af587f8bac7&chksm=fdb3f2cccac47bda73995f88e4b151b01fc29e9bcd082c1b5e11a5743ce207a47db0a9409025&mpshare=1&scene=1&srcid=0304bfWzEezdJndBlTyG9FsQ&sharer_sharetime=1677915812636&sharer_shareid=ee47b9411760e9070f0b59d8d8655fa1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6b175b01-657f-47e8-b011-82331c10ea92/6b175b01-657f-47e8-b011-82331c10ea92/)