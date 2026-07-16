---
title: "向 Kindle 高级用户进阶，你可以试试这些搜索框命令"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/向 Kindle 高级用户进阶，你可以试试这些搜索框命令.md
tags: [印象笔记]
---

# 向 Kindle 高级用户进阶，你可以试试这些搜索框命令

# 向 Kindle 高级用户进阶，你可以试试这些搜索框命令 --- 为了方便调试，许多软件都会暗藏一些需要用特殊方式开启的命令代码，例如魂斗罗的 `↑ ↑ ↓ ↓ ← → ← → B A` 、Chr

---

# 向 Kindle 高级用户进阶，你可以试试这些搜索框命令

---

为了方便调试，许多软件都会暗藏一些需要用特殊方式开启的命令代码，例如魂斗罗的 `↑ ↑ ↓ ↓ ← → ← → B A` 、Chrome 的 `chrome://flags` 可以开启实验室功能，微信的 `:recover` 可以进入故障修复模式等。

而你可能不知道的是，我们常用的电子书阅读器 Kindle 中其实也隐藏着不少系统命令，可以通过在搜索框内输入来调用。少数派也在这里为大家整理了几条比较实用的命令，欢迎继续阅读。

重置阅读速度
------

我们阅读电子书时，Kindle 会自动统计翻页频率等数据，在左下角估算出本章剩余阅读时间，方便我们提前做好规划。但有时我们会把 Kindle 晾在一边做别的事情，导致该时间失去参考价值。

这时，你可以在阅读界面点击屏幕上方，在右上角的搜索框内输入 `;ReadingTimeReset` （半角分号，区分大小写）并回车，Kindle 就会重置统计数据，在左下角显示「了解阅读速度…」字样。再用正常速度读几页书后，你就能看到比较准确的剩余阅读时间信息了。

![](.evernote-content/64145616-1F6A-4652-B11F-DE7CD13A1CCF/714E0B68-E265-47FE-88DC-4BDEE9EFA920.png)

除了重置阅读速度外，你还可以通过输入 `;ReadingTimeOff` 关闭阅读速度功能，再输入 `;ReadingTimeOn` 就能重新打开该功能了。

保持屏幕常亮
------

默认状态下，Kindle 在闲置 10 分钟无动作后就会自动锁屏，关闭背光，以节省电量。但如果你正在精读某一段落，或者将内容誊抄至纸质笔记本上，这个功能就显得有些碍事了。

其实，只要在任意位置召唤出搜索框，输入 `~ds` （即 Disable Screensaver 的缩写）代码并回车，就可以临时禁用 Kindle 的锁屏休眠功能。即使你手动按下电源键，也不会有任何反应，彻底杜绝误触现象。

如果你之后想恢复锁屏功能，就需要长按 Kindle 电源键重启设备了，再次输入 `~ds` 是无效的。

![](.evernote-content/64145616-1F6A-4652-B11F-DE7CD13A1CCF/9C873BFB-C058-4114-A25A-1EE2E294DFAF.jpg)

在少数派出品的 [「Kindle 完全使用指南」](https://sspai.com/series/18 "「Kindle 完全使用指南」")付费栏目中，还讲述了如何自定义锁屏图片和关闭推广信息，欢迎订阅了解。

查看系统状态
------

在 Kindle 设置中的「设备选项」里，我们可以查看 MAC 地址、固件版本、序列号等信息。如果你想了解更多系统状态等信息，可以试试在搜索框内输入 `~dm` 命令。

`~dm` 意为 dump messgaes to /documents，它会执行 Kindle 系统中的 `/usr/bin/dm.sh` 脚本，将 Kindle 系统日志以本地文档的形式保存至本机，可以在「个人文档」分类内直接查看。

![](.evernote-content/64145616-1F6A-4652-B11F-DE7CD13A1CCF/57878484-9530-4066-8273-F9457AAA0310.png)  
此外，`;411` 命令可以查看 Kindle 服务器信息，`;611` 可以查看本地 WAN 口信息，`;711` 则可以查看 WiFi 相关信息。

重置 Kindle
---------

如果你想对自己的 Kindle 做次大扫除，或者转让给他人，可以在设置中的「设备选项」里选择重置设备，删除全部本地文档。而如果你想做的更彻底一点，不如直接在搜索框输入 `;urst` 试试。

`;urst` 会执行 Kindle 系统中的 `/usr/sbin/userstore_reset` 脚本，它会完全删除用户分区内所有内容，包括已下载书籍和文档、隐藏系统文件夹、日志文件等。由于**执行该命令前不会弹出确认对话框，请务必提前备份后再尝试。**

![](.evernote-content/64145616-1F6A-4652-B11F-DE7CD13A1CCF/917F01F7-010B-4680-AF9C-2B1496E8DABA.jpg)  
而如果你想更彻底地清理设备上全部内容，可以直接在搜索框内输入 `;shpm`，即 set device to shipping mode 的缩写，它会执行 `/usr/sbin/shipping_mode` 脚本，将设备完全还原为出厂状态，`;lzzl` 命令也有同样功效。**这两个命令同样不会要求再次确认，请谨慎操作。**

如果你想了解更多 Kindle 的实用技巧，欢迎订阅少数派出品的[「Kindle 完全使用指南」](https://sspai.com/series/18 "「Kindle 完全使用指南」")付费栏目。

* 如果你想了解更多 Kindle 搜索框命令，可以查看 MobiRead Wiki 的 [Kindle Touch Hacking Guide](https://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Useful_hidden_functionality "Kindle Touch Hacking Guide") 和 StackExchange 的 [What commands can be given in the Kindle's search box?](https://ebooks.stackexchange.com/questions/152/what-commands-can-be-given-in-the-kindles-search-box "What commands can be given in the Kindle's search box?") 。\*

关注 [少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，让智能设备 Power Up。

---

[🌐 原始链接](http://sspai.com/post/43609)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7406b7df-7aa2-449f-99c6-0f7d609a4bdc/7406b7df-7aa2-449f-99c6-0f7d609a4bdc/)