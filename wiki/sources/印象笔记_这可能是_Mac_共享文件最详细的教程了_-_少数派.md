---
title: "这可能是 Mac 共享文件最详细的教程了 - 少数派"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/这可能是 Mac 共享文件最详细的教程了 - 少数派.md
tags: [印象笔记]
---

# 这可能是 Mac 共享文件最详细的教程了 - 少数派

# 这可能是 Mac 共享文件最详细的教程了 - 少数派 --- 这可能是 Mac 共享文件最详细的教程了 ==================== ### **Matrix 精选** [Matrix

---

# 这可能是 Mac 共享文件最详细的教程了 - 少数派

---

这可能是 Mac 共享文件最详细的教程了
====================

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

如果希望让一台 Mac 访问另一台 Mac 上的文件，就可以使用 Mac 的**文件共享**功能。

而且不仅是 Mac 之间，甚至用 iPhone、iPad、Windows PC 都可以访问 Mac 的共享文件。

首页要保证共享文件的 Mac 和另一台设备（iPhone/iPad/Windows）**都处于同一局域网**下，也可以理解为都连的同一个路由器 Wi-Fi。

开启文件共享的 Mac 要怎么设置？
------------------

在需要共享文件的 Mac 上打开「系统偏好设置-共享」，在左侧选项栏勾选「文件共享」。这时候右侧的文件共享就会显示打开的状态。然后会有一串类似 [smb://xxxxxx.lan](https://sspai.com/post/61388smb://huangyangdembp.lan) 这样的地址，这就是这台 Mac 的共享网络地址。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/26125400-5CA0-4A08-B860-0C6235A19F5F)

再下面会显示共享的文件夹，一般默认有一个「xx的公共文件夹」，可以添加这台 Mac 的其他文件夹作为共享文件夹。比如我添加了「下载」文件夹。在右侧「用户」可以设置其他 Mac 访问这个文件夹的权限设置。比如管理员用户（黄杨）可以读和写，其他用户只读。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/E44722C4-A569-4F78-8088-A1F705808B63)

如果希望其他设备以客人用户登录共享，而不是以管理员或普通账户登录，可以在「用户与群组」中，把「客人用户」勾选「允许客人用户连接到共享文件夹」。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/D3420C79-FE9F-433E-840D-6C7F6265E49B)

另一台 Mac 怎么访问开了文件共享的 Mac 呢？
--------------------------

在另一台 Mac 上打开访达，点左侧的「位置-网络」图标，就能看到同一局域网打开了「文件共享」的 Mac。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/54BAF88D-86EE-4B80-9072-3D5E14B26E74)

双击打开这台 Mac 的图标，第一次需要「连接身份」。不同账户类型获取的文件夹访问权限不一样。

选择**「客人用户」，不需要验证就能访问开启共享 Mac 的共享文件夹**（例子中的公共文件夹和下载文件夹）。这种适合别人的电脑只访问这台 Mac 共享文件，比如在办公室环境。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/CBD9B8AF-C38D-4B07-8DDE-D971F42B0885)

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/82F8009B-CA09-4EA6-B609-C569F49402B9)

如果选择「注册用户」，需要输入共享 Mac 的任一账户的登录账户名和密码（可以是管理员账户或者普通账户）。用共享 Mac 的管理员账户登录，除了可以看到共享文件夹，还能看到 Mac 里的所有文件。管理员账户登录适合自己的另一台 Mac、iPad 或 iPad 访问这台 Mac 的全部文件。不建议把 Mac 管理员账户密码分享给其他人。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/A22E25AE-2F36-4AA3-91F4-563C3E470C72)

点击共享的文件夹，就能查看、复制和往文件夹里拷贝文件（取决于权限的大小）。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/152BB24B-82E6-4473-A1C3-C60DA33FBC5B.gif)

还有一种方法连接被共享的 Mac 。就是在访达菜单栏选择「前往-连接服务器」（或用快捷键 `shift-command-K`），然后输入被共享 Mac 的网络地址，就是之前那串类似 [smb://xxxxxx.lan](https://sspai.com/post/61388smb://huangyangdembp.lan) 这样的。同样输入账户密码后，就能连接。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/2A35FB43-6030-4DA9-BE99-3B668AA84246)

iPhone 和 iPad 怎么连开了文件共享的 Mac？
-----------------------------

在 iPhone 或 iPad 打开「文件」App，点击右上角选项图标，选择「连接服务器」，然后输入服务器地址，紧接着选择「客人用户」或「注册用户」登录进去就连接上了。操作跟 Mac 很像。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/B1E83347-F107-4884-A914-632BDF2A56DC)

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/3AFBE68C-DAF2-4BBC-8B01-FA23E23D8832)

连过一次的共享，下次可以直接在「文件」App 的「已共享」里看到。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/0BC9FC6F-75E5-4AEE-8DEB-3F19B708F879)

Windows PC 怎么连开了文件共享的 Mac？
--------------------------

要让 Windows 访问 Mac 的共享文件，需要先做一些设置。放心，不会太复杂。

首先共享 Mac 这边要先开启 Windows 文件共享。在「系统偏好设置-共享」点击右侧「选项…」，在弹出窗口勾选「使用SBM来共享文件个文件夹」，并勾选「Windows 文件共享」下面的一个账户（建议选一个普通账户）。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/84640BE7-5134-4312-9F65-9F54A0F92C24)

接着打开「系统偏好设置-网络」，在已连接的网络右下角点「高级」按钮。

选择 WINS，输入 Windows 的工作组名称。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/E374551A-334B-47EA-A27B-F984538448F2)

可以在 window 上打开「系统」窗口，就能看到工作组的名称（一般是 WORKGROUP）。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/39D2B694-FE89-4F70-BC1A-D64F75200642)

准备工作做好了，下面试试用 Windows 访问 Mac 共享文件。

打开 Windows 的「文件资源管理器」，看到左侧的「网络」，点开。然后就能发现同一个局域网的开启了文件共享的 Mac。是不是跟 Mac 访问 Mac 很像。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/AAB4A0D3-78FA-44A3-B28A-152BF2ACE427)

点击共享 Mac 名字的图标，并用之前设置的 Mac 用户账户登录，就能看到 Mac 的共享文件啦。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/D908603D-5374-45CF-AD68-4F7A632DC52F)

我的尝试中，Windows 并不能通过客人账户模式（不需要用户和密码）访问 Mac 共享文件。所以除非是信任的 Windows，否则建议添加一个 Mac 普通账户用来给 Windows 共享，并严格设置文件夹读写权限。

Mac 文件共享有什么用？
-------------

有了 Mac 文件共享，就可以很方便的给局域网其他设备分享文件。Mac 和 Windows 之间共享文件也变得更方便。

可以把一台 Mac 作为「共享盘」，把其中一个共享文件夹开放完全读写权限，别人可以访问和下载这个共享文件夹的文件，也可以把别的设备的文件放到这台 Mac 的共享文件夹中。在小型办公室场景还蛮好用的。

比如我就把 2T 移动硬盘通过 MacBook Pro 整盘共享出去。自己的 iOS 设备和家人的 Mac、iOS 设备都可以直接读写硬盘文件。有点 NAS 的意思。（我家里还没有 NAS）

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/940D83F6-5D7C-40DF-BC0E-461D36BFBBCC)

文件共享本质上就是利用了 SMB 协议，所以只要是支持 SMB 连接协议的设备理论上都可以 访问 Mac 共享。比如路由器、NAS。我还尝试在 Apple TV 的 infuse 软件连接 Mac 的共享文件夹，就可以直接用 Apple TV 播放 Mac 里的电影。

![](.evernote-content/E17A8FC0-B85F-4F47-8F80-B59EAE309A79/BB34A9DA-8349-4713-A94E-85DDB9E4916F)

> 下载少数派  [客户端](https://sspai.com/page/client) 、关注  [少数派公众号](https://sspai.com/s/J71e) ，了解更妙的数字生活

20528

iPhone 和 iPad 怎么连开了文件共享的 Mac？

---

[🌐 原始链接](https://sspai.com/post/61388)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b2b45886-c783-4728-86f1-6412fe5277fc/b2b45886-c783-4728-86f1-6412fe5277fc/)