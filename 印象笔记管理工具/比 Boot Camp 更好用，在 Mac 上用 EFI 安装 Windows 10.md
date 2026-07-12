# 比 Boot Camp 更好用，在 Mac 上用 EFI 安装 Windows 10

---

**特别提醒：数据无价！请务必在动手前做好数据备份工作！**

为什么要使用 EFI 安装？
--------------

1、Boot Camp 会模拟旧电脑的 BIOS 环境（即 Legacy 模式）来引导 Windows ，这或多或少会造成性能损失。而大多数 Mac 以及 Windows 10 都是支持 EFI 启动的。（难道 Apple 是为了防止用户装 Windows ？）

2、使用 macOS 自带的 Boot Camp 助理安装 Windows 10 时，系统会把磁盘的分区表类型转换为 GPT+MBR 混合型（仅限 2015 年之前推出的 Mac ）。然而很多分区工具都无法识别这种 GPT+MBR 混合型分区表，在分区之后会导致分区表损坏，从而导致分区数据丢失。这是最致命的问题。使用 EFI 安装 Windows 10 之后，分区表类型不会被修改，因此可以在 Windows 10 下自由分区。

3、使用 EFI 安装 Windows 10 之后可以使用快速启动功能。

4、玩外接显卡的朋友应该知道，使用 Boot Camp 引导由于有 32 位寻址的限制从而使显卡出现 `Error 12` 错误而无法启动，通过 EFI 安装也可以完美解决。

我的安装环境
------

* 机型：MacBook Pro 15" Mid 2015
* 系统：macOS 10.12.6
* 硬盘：500G SSD （只有 macOS 分区）

安装步骤
----

### 下载 Boot Camp 驱动程序

打开 **Boot Camp 助理**，然后打开菜单栏中的 **操作 - 下载 Windows 支持软件**，把驱动程序下载到安装盘中。

![](.evernote-content/3D6D806B-DD5E-46D3-859D-85954DF76316/5F374DFC-3923-443C-921A-897179AC118D.png)下载驱动程序

### 确定磁盘的大小和剩余空间

点击左上角的 **** ，然后选择**关于本机**，再点击**储存空间**查看。

![](.evernote-content/3D6D806B-DD5E-46D3-859D-85954DF76316/B3570B31-BEAE-468D-A804-E3DEF2E89AFA.png)磁盘用量

### 通过命令行压缩 macOS 分区

> 自从 OS X 10.11 开始，系统中的磁盘工具功能遭到了大阉割，很多功能都没了，其中就包括压缩分区。所以这里不得不使用命令行来压缩分区。

以下通过调整 macOS 分区大小的方式来压缩 macOS 分区。

例如，这里 macOS 分区大小是 **500G** ，您想分 **100G** 给 Windows ，那么 macOS 分区在压缩后的大小就是 500-100=**400G** 。

请根据可用空间大小合理划分。

#### 打开**终端**，然后根据实际情况**选择其中一条命令执行**。

#### 1. 如果开启了 FileVault 全盘加密

输入`diskutil resizevolume / 400G`，回车执行。

#### 2. 如果没有开启 FileVault 全盘加密

输入`diskutil cs resizevolume / 400G`，回车执行。

上面的 400G 是 macOS 分区的最终大小，请根据实际情况调整。

以下是我的执行结果（第一种）

```
[zenandidi: ~]$ zenandidi$ diskutil resizevolume / 400G
```

```
Resizing to 400000000000 bytes
Started partitioning on disk0s2 Macintosh HD
Verifying the disk
Verifying file system
Using live mode
Performing live verification
Checking Journaled HFS Plus volume
Detected a case-sensitive volume
Checking extents overflow file
Checking catalog file
Checking multi-linked files
Checking catalog hierarchy
Checking extended attributes file
Checking volume bitmap
Checking volume information
The volume Macintosh HD appears to be OK
File system check exit code is 0
Resizing
Shrinking file system
Copying booter
Modifying partition map
Finished partitioning on disk0s2 Macintosh HD
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.3 GB     disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                  Apple_HFS Macintosh HD            400.0 GB  disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
```

#### 注意

执行完成后如果提示如下信息

```
Error: -69787: The partition cannot be resized; try reducing the amount of change in the size of the partition
```

说明磁盘剩余空间不足，请增大分区后的大小。

### 在 Windows 安装向导中创建分区并安装

把安装盘插到 Mac 上，重启 Mac 并按住 **option** 键，选择 **EFI Boot** （黄色硬盘图标，如图所示）回车启动。

![](.evernote-content/3D6D806B-DD5E-46D3-859D-85954DF76316/7E70D430-343D-4601-B6AF-C9090BCB987C.jpg)启动项选择

然后一直下一步，到选择安装位置这里（如图所示），选择“未分配的空间”，然后点击新建，再点应用，弹出的窗口点确定最后点下一步即可开始安装。

![](.evernote-content/3D6D806B-DD5E-46D3-859D-85954DF76316/3131A5AB-DBDC-44B6-8826-D0BCA6708969.jpg)选择安装位置

### 安装驱动程序

进入 Windows 系统后，安装已经下载好的驱动程序，完工！

注意事项
----

1. Windows 启动盘建议在 Windows 系统下使用 UltraISO 制作（可先安装 Windows 虚拟机）。
2. 使用 Fusion Drive 混合硬盘未经过测试，请自行摸索。
3. 我的 MacBook Pro 使用 EFI 安装之后，每次启动之后键盘灯都会调到最高亮度，目前找不到解决方法，不知道是不是个例。
4. 在老机器上使用 EFI安装可能会存在设备驱动的问题（如声卡），有些机器可以通过 EFI Shell 映射设备的方法解决（最简单的解决方法就是替换引导文件，每次开机会自动调节）。老机器使用 EFI 还可能会遇到一些神奇的问题，比如安装好显卡驱动的独显机器登录画面黑屏十秒钟左右才亮起来，但并不影响启动速度。

---

[🌐 原始链接](https://sspai.com/post/40834)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1c891974-647b-4645-adfe-c303d0257219/1c891974-647b-4645-adfe-c303d0257219/)