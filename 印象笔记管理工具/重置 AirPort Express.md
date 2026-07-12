# 重置 AirPort Express

---

﻿重置 AirPort Express
===================

#### 

您可以在此处了解如何重置 AirPort Express 基站。  
  
**注意：**本文仅适用于 AirPort Express。要重置其他基站，请参阅[AirPort 支持页](http://www.apple.com.cn/support/airport)。

在 AirPort Express 之前，只有两种类型的重置：**软**重置和**硬**重置。AirPort Express 引入了第三种类型的重置：**出厂默认值**重置。

* 如果您忘记了您的基站密码，则可执行**软**重置。
* 如果 AirPort Express 停止响应或有网络可访问性问题，则可执行**硬**重置。此重置不会抹掉保存的描述文件。
* 如果需要将 AirPort Express 返回到出厂配置，则可执行**出厂默认值**重置。此重置将抹掉保存的描述文件。

重置按钮位于音频端口下面：

![](.evernote-content/86B4E231-8A13-4A5B-95D9-7D9098AC0E18/7048C5C5-ECC5-4E4C-9FD1-38166D0D28C8.jpg)

下面是重置按钮图标的特写视图：

![](.evernote-content/86B4E231-8A13-4A5B-95D9-7D9098AC0E18/8779D9BD-92A9-4AA8-8969-0EA57E470158.jpg)

要执行下面的步骤，您需要使用已拉直的回形针来按下重置按钮。按下重置按钮时，应能够感觉到该按钮点按到压下的位置。您可能需要在该单元已拔掉的情况下练习此操作，直到您已掌握了该按钮操作。   
  
**如何执行软重置**

1. 请确保 AirPort Express 已连接到电源。
2. 在 **Apple** 菜单中，选择**系统偏好设置**。
3. 在**查看**菜单中，选择**网络**。
4. 在“显示”弹出式菜单中，选择“AirPort”。
5. 点按 TCP/IP 标签。
6. 在“配置”弹出式菜单中，选择“使用 DHCP”。
7. 按住重置按钮整一秒。在此期间，指示灯将以琥珀色闪烁，表示 AirPort Express 处于软重置模式。

   **提示：**如果未在按下重置按钮的五分钟之内进行更改，则 AirPort Express 将返回到以前的配置。指示灯将更改回纯绿色（或重置之前所处的任何状态）。
8. 在 AirPort 菜单栏项中，选择 AirPort Express 创建的网络（网络名称不更改）。
9. 打开“AirPort 管理实用程序”。它位于“应用程序”文件夹下的“实用工具”文件夹中。
10. 选择 AirPort Express，然后点按“配置”。您可以在下面看到显示的对话框。您可以使用该对话框可以进行以下更改：  
    * IP 地址：除非 Internet 服务提供商或系统管理员已为您提供了 IP 地址，否则不要更改 IP 地址。
    * 重置基站密码。
    * 打开加密功能以激活 AirPort 网络的密码保护功能。如果打开加密功能，请为 AirPort 网络输入新密码。

      ![](.evernote-content/86B4E231-8A13-4A5B-95D9-7D9098AC0E18/0280CB2C-6A00-439A-87D0-305186B2AAD7.jpg)
11. 点按“更新”。AirPort Express 将重新启动以加载新设置。

AirPort Express 处于软重置模式时，“访问控制”和 RADIUS 设置会临时中断。在 AirPort Express 重新启动之后，所有 AirPort Express 基站设置都将可用。  
  
  
**如何执行硬重置**  
  
如果 AirPort Express 停止响应，您可能需要对其执行硬重置。然后，可以从保存的描述文件恢复设置，或使用 AirPort Express 助理 (Windows)、AirPort 设置助理 4.1 版或更高版本 (Macintosh) 或 AirPort 管理实用程序（Windows 或 Macintosh 平台）重新设置。  
  
**重要信息：**

1. 对 AirPort Express 执行硬重置将抹掉所保存的描述文件之外的所有设置。抹掉的设置包括“访问控制”和 RADIUS 设置。AirPort Express 必须在此过程中连接到电源。
2. 根据 AirPort Express 上安装的固件版本是 6.1.1 版或更高版本（可从[此处](http://www.apple.com.cn/support/airport)下载）还是早于 6.1.1 版的版本，重置步骤会略有不同。

**对于 6.1.1 或更高版本**

1. 按住重置按钮。
2. 继续按住该按钮，直到状态指示灯 (LED) 开始快速闪烁（应在大约 5 秒之后发生）。
3. 松开该按钮，AirPort Extreme 将硬重置。

**对于早于 6.1.1 版的固件**

建议先升级到 [6.1.1 版或更高版本](http://www.apple.com.cn/support/airport)（如果可能）。如果不可能，请执行以下步骤：

1. 要执行硬重置，请按住重置按钮整 10 秒。
2. 松开该按钮，AirPort Extreme 将硬重置。

**硬重置期间发生的情况**

指示灯将快速闪烁几秒，然后 AirPort 将重新启动。短时间内，AirPort Express 将在 AirPort 菜单或 AirPort 管理实用程序中不可见。完成整个该过程大约需要 45 秒。然后，可以使用处于其默认状态的 AirPort Express，重新加载保存的描述文件，或使用 AirPort Express 助理或 AirPort 管理实用程序重新配置 AirPort Express。在重置期间，AirPort Express 将加载以下默认设置：

* 设置为按 DHCP 请求 IP 地址
* 基站密码为“public”
* 基站名称将转换为“Base Station XXXXXX”，其中 XXXXXX 是无线 MAC 地址的最后 6 位
* 网络名称为“Apple Network XXXXXX”，其中 XXXXXX 是无线 MAC 地址的最后 6 位

MAC（媒体访问控制）地址是网络端口的唯一硬件标识号。AirPort Express 有两个 MAC 地址：一个用于有线 Ethernet 端口，一个用于无线 Ethernet 端口。无线 MAC 地址也称为 AirPort ID。  
  
  
**如何执行出厂默认值重置**  
  
**重要信息：**此重置将抹掉所有设置和保存的描述文件。抹掉的设置包括“访问控制”和 RADIUS 设置。  
  
请执行下列步骤：

1. 将 AirPort Express 从电源插座拔出。
2. 按住重置按钮。
3. 将 AirPort Express 插回到电源插座（仍按住该按钮）。
4. 继续按住该按钮，直到看到指示灯快速闪烁（应在几秒之后发生）。
5. 松开该按钮。

与执行硬重置时一样，短时间内，AirPort Express 将在 AirPort 菜单项或 AirPort 管理实用程序中不可见。请记住，完成整个该过程大约需要 45 秒。然后，可以使用处于其默认状态的 AirPort Express，或使用 AirPort Express 助理或 AirPort 管理实用程序重新配置 AirPort Express。有关默认设置的信息，请参阅上面的硬重置部分。

[📎 在印象笔记中打开](evernote:///view/207087/s1/c2bb6ff7-0d20-4226-87da-444ae400821e/c2bb6ff7-0d20-4226-87da-444ae400821e/)