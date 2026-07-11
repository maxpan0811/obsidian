# 锋友分享：Mac安装双系统以及共享分区

---

目前关于 Mac 安装双系统和共享分区的方法有很多，但有些不够通用，或者太复杂，日前，锋友“[弱碱性工程师](http://bbs.feng.com/forum.php?mod=viewthread&tid=11405548&extra=page1filterauthororderbydatelineorderbydateline)”分享了一种通用、简单的方法，不需要重装 macOS 系统也可以实现，一起来看看吧。

![](.evernote-content/4D48C576-F9E2-4187-B77E-33E369A85E93/049264E6-8C45-404C-AA1A-87DECADF1EF1.png)

该锋友表示，这个操作办法适用于非 Fusion Drive 硬盘，如果是 Fusion Drive 硬盘，关闭 CoreStorage 后当做两个硬盘安装双系统即可。CoreStorage 是苹果为 Fusion Drive 设计的一种磁盘管理方式。

工具：

Mac 自带的“终端”、“Boot Camp 助理”以及“磁盘工具”软件

步骤：

1. 首先关闭 CoreStorage。

![](.evernote-content/4D48C576-F9E2-4187-B77E-33E369A85E93/E44261C5-8A37-42D0-85CD-7205F1566A20.png)

我们需要打开“终端”，输入指令 sudo diskutil CoreStorage revert / 并按下回车键，输入密码，执行完成后重启 Mac。

2. 使用 Boot Camp 安装Windows。

![](.evernote-content/4D48C576-F9E2-4187-B77E-33E369A85E93/6C166223-5A33-48FD-B18D-931667FBCDB5.png)

打开 Boot Camp，选择“打开 Boot Camp 帮助”，根据苹果官方教程安装 Windows，教程包括以下步骤：

- 检查软件更新

- 获取 Windows ISO 映像

- 准备 Mac 以安装Windows

- 安装 Windows

- 安装 Windows 支持软件

3. 使用“磁盘工具”创建多分区。

![](.evernote-content/4D48C576-F9E2-4187-B77E-33E369A85E93/BED56506-C07C-4C50-B319-BAC6524E2205.png)

- 安装完 Windows 后，重启 Mac 按 Option 键选择 Mac 系统进入。

- 打开“磁盘工具”，选中整个硬盘，选择“分区”。

- 选中“MacintoshHD”分区，按“+”增加所需分区，大小根据自己需要分配，格式选择 exfat，两个系统都可以访问这个格式。

- 分配完后选择“应用”。

4. 重启 Mac 即可。

![](.evernote-content/4D48C576-F9E2-4187-B77E-33E369A85E93/B0EF6FEA-DB11-41A9-AD95-CBC4DAAAAABB.png)  
  
![](.evernote-content/4D48C576-F9E2-4187-B77E-33E369A85E93/CE126DC3-1900-4FFA-85DB-03B17A59CA21.jpg)

[阅读全文](http://www.feng.com/iPhone/news/2017-08-24/Feng-friends-sharing-Mac-installed-double-system-and-Shared-partitions_689327.shtml)

---

[🌐 原始链接](http://www.feng.com/iPhone/news/2017-08-24/Feng-friends-sharing-Mac-installed-double-system-and-Shared-partitions_689327.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5e5acfed-de3d-4c6c-bf73-a223bd40dcb3/5e5acfed-de3d-4c6c-bf73-a223bd40dcb3/)