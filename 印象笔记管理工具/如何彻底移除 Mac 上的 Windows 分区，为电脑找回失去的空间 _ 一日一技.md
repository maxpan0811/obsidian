# 如何彻底移除 Mac 上的 Windows 分区，为电脑找回失去的空间 | 一日一技

---

过去，通过 Mac 系统自带的工具「启动转换助理」安装或者移除 Windows 10 十分方便；然而在 macOS 版本更新至 High Sierra 后，你可能发现「安装或移除 Windows 7或更高版本」的按钮变成了灰色，没法移除 Windows 分区；或者，移除分区后那一部分空间就「不见了」。

![](.evernote-content/7A4DC047-0533-414A-B44D-B927F71236A1/E270C02D-FCF9-4EAF-B3F8-1CDB62B1B61E.png)无法移除分区

本文教你用命令行来解决这一卸载难题。

此操作需要一定动手能力，一共三步，步骤完成后现有 Mac 系统不会有任何变化，Windows 10 系统会被彻底移除，Mac 系统将会重新拥有全部硬盘空间。

1. 打开「磁盘工具」- 从左侧选中「BOOTCAMP」- 从上方工具图标中选择「抹掉」工具 - 弹出的对话框「格式」那一栏选择「APFS」- 点击「抹掉」按钮

![](.evernote-content/7A4DC047-0533-414A-B44D-B927F71236A1/4002F912-1F40-480B-ACF6-F079ADDBDF9D.png)磁盘工具

2. 打开「终端」输入代码 `diskutil list`，并按「Return」来显示所有磁盘信息，记下 `BOOTCAMP` 盘所对应的「IDENTIFIER」，我这里所对应的盘符是 `disk0s3`；

终端

3. 继续在「终端」输入代码 `sudo diskutil eraseVolume free none disk0s3` 并按「Return」来彻底移除刚刚记录下的这个磁盘；

4. 继续在「终端」输入代码 `sudo diskutil apfs resizeContainer disk0s2 0` 并按「Return」来将所有可用空间恢复到 Mac 盘。

究其原因，是因为在 macOS High Sierra 中，系统的底层文件系统被彻底替换为 APFS， 但是系统自带的「磁盘工具」并未针对APFS 进行更新，很多常用操作（比如磁盘扩容）无法用它实现，导致现阶段移除 Windows 10 系统分区后重新分配这部分磁盘空间异常繁琐。

如果你安装了 Mac、Windows 10 双系统启动，但出于各种原因，需要将 Windows 10 移除、 使 Mac 恢复到刚买回来初始单个系统盘状态的，却发现「启动转换助理」不奏效，可是试试本文提供的命令行方法。

本文只专注于从 Mac 上移除 Windows 10 且料理后续磁盘问题，不会讲解如何安装双系统，如有需求欢迎在评论中提及，将会单独开文讲解流程。

---

> 开启 macOS 隐藏功能，就在专题 [轻松玩转 Mac 命令](https://sspai.com/topic/183) 💻

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用 ⚡️

---

[🌐 原始链接](http://sspai.com/post/43699)

[📎 在印象笔记中打开](evernote:///view/207087/s1/da891b26-765e-4ea1-b75a-54050aa7cb90/da891b26-765e-4ea1-b75a-54050aa7cb90/)