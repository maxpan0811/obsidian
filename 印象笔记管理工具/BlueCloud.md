# BlueCloud

---

|  |
| --- |
| BlueCloud |

  

如何在 iOS 设备中使用我们的服务
------------------

AnyConnect VPN (推荐)
-------------------

优点：

* 可智能代理。不影响访问国内网站的速度，可以一直打开VPN
* 可在某些系统VPN无法连接的特殊网络环境中使用
* 锁屏、切换网络永不掉线

设置步骤

1. 点击链接 [AnyConnect](https://itunes.apple.com/us/app/cisco-anyconnect/id392790924?mt=8) 并下载安装
2. 打开AnyConnect，点击 **Connection** 添加VPN链接

   ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/DA3D3B88-8A82-4AC6-883F-D8B938542C37.png)
3. 点击 Add VPN Connection

   ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/29F62F7E-DD7D-44F0-A3FB-7A6BC469CFA2.png)
4. 在 Server Address 位置输入 **hk.link.ac.cn** 并点击 **Save** 保存

   ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/C20E2943-58E4-4946-B9A2-9A1D1E7D7C40.png)
5. 点击返回 返回 Anyconnect 主界面， 点击开关连接 VPN并输入您注册的Email 作为用户名 。

   ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/A8301E87-4CAB-40A2-9B16-0833B7CE94D1.png)

### 关于分组的说明(必读)

**目前的三个分组分别为 global （全局），smart（非中国IP走代理），smart-bllacklist（部分无法直接访问IP走代理）
请您按照您的需求选择合适的分组。
由于AnyConnect限制，某些情况下IP判断可能有误，请您注意**。

\*\*关于切换节点，请您断开连接后点击 *连接* 即可看到所有可用节点。 请不要直接输入其他服务器地址进行连接。

6. 点击连接并输入您的密码完成连接

   ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/C87E4126-E9C9-4A9E-BDA3-B3F04E3EBBD5.png)
7. 您断开连接之后即可在*Connection*中看到所有可用的服务器

   ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/195C6BC5-10B4-4579-A20F-7D4714C5A6DB.png)

默认服务器可能速度并不能使您满意，您可以参照本站后台页面的说明切换其他服务器。

线路说明： Auto 为自动选择服务器。 其他线路请参照本站后台页面的说明。

iOS VPN配置
---------

支持 iOS 6.X/7.X/8.X 版本iOS系统
支持iPhone/iPad/iPod touch 等各种使用上述系统版本的苹果设备

由于安全原因，我们暂时下线了配置文件安装页面。您可以手动设置IPSec 服务器。共享密钥是 otin

设置步骤

1. 使用系统内置的Safari 浏览器登录您的账户

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/A5BD2311-6A53-49DC-9FF1-C3A50F7FF389.jpg)
2. 点击安装iOS配置文件 并点击安装按钮

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/F8AB41B8-FE84-425B-9646-5AD8AE1AABC5.jpg)
3. 进入设置界面，再点击VPN 上的开关即可打开VPN

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/65988772-E4A8-4AF1-9227-F3B8126EE36D.jpg)

  

|  |
| --- |
| BlueCloud**Source URL:** <https://bluecloud.xyz/page/view/8> |

|  |
| --- |
|  |

在 Chrome 浏览器中使用我们的服务
--------------------

本教程适用于 BlueCloud 标准套餐
---------------------

Chrome 插件
---------

支持所有可以安装 Chrome / Chromium浏览器的操作系统 也可通过软件转换成为 普通代理供其它浏览器/软件使用

**请注意：您的Chrome版本需要高于 Chrome 46，否则在使用我们服务时可能会遇到兼容性问题。**

配置步骤

1. 打开Chrome 浏览器，并安装代理插件。 插件地址 [点这里](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)

如果遇到Chrome 应用商店打不开，请戳 [这里](https://bluecloud.xyz/page/view/13)

如果您使用的是之前一个版本的插件，请先删除上一版插件。

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/2C341DC9-2F12-46CD-A5AF-2B32B689029D.png) 2. 插件安装好后点击浏览器右上角的插件图标，然后点击 **选项**![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/E72124CC-C5D0-4F1F-9101-2E00666F3CCA.png) 3. 点击 **导入\导出** ，然后在 **在线恢复备份** 栏中输入https://bluecloud.xyz/upload/switchy.bak这个地址。 然后点击**在线恢复备份**按钮， 再在弹出的对话框中点击 **确定** 。即可导入代理设置。 如果在线恢复失败，请尝试将 https://bluecloud.xyz/upload/switchy.bak 复制到地址栏，下载后手动导入。或者清除Chrome 浏览器缓存后再试。

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/219082F6-5DC9-4866-BDDD-FE6D40D18265.png) 4. 点击地址栏右边的插件图标，点击需要使用的配置项以启用代理。 ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/8BC6D6EC-A88D-4A34-8E26-0D398CC877FC.png) 5. 如果提示框出现，输入您在网站使用的 **Email** 和密码即可开始浏览网页。(用户名和密码与您在本网站注册使用的Email / 密码组合相同 ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/2CEC4359-D3C9-4E8E-9C23-7613D4DBA5BF.png)

如果您需要保存密码，请按照以下步骤进行，如果不需要保存用户名密码，则到这一步已经完成配置。如果您认为当前节点速度不理想，请切换列表中的其他节点尝试。

**请注意， 默认模式下仅收录了无法直接访问的网站，如果您要访问某些可以直接访问但是速度较慢的网站请切换至全局模式**

### 保存用户名密码

1. 点击浏览器右上角的插件图标，然后点击 **选项**![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/E72124CC-C5D0-4F1F-9101-2E00666F3CCA.png)
2. 在您要使用的节点上点击 *代理登陆*![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/7F6ED060-34D7-46FB-B264-06CF84427759.png)
3. 输入您的 Email 作为用户名，您在BlueCloud 账户的密码作为登陆密码。 并点击保存更改。 如果您需要在多个节点上保存密码请重复以上步骤。 ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/024F9741-7941-420B-BB26-9D00A2EB7D48.png)

  

|  |
| --- |
|  |

  

服务器列表
-----

| 服务器地址 | 支持类型 | 状态 | 位置 | 流量比例 |
| --- | --- | --- | --- | --- |
| sfo.link.ac.cn | Chrome 插件,IPSec,IKEv2 | ** Online | San Francisco,California,US | 100% |
| lax.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Los Angeles,California,US | 150% |
| las.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Las Vegas ,Nevada,US | 100% |
| tokyo.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Tokyo,JP | 100% |
| tokyo2.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Tokyo,JP | 100% |
| tokyo3.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Tokyo,JP | 100% |
| sin.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Singapore | 100% |
| hk.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Hong Kong | 100% |
| hk2.link.ac.cn | Chrome 插件,IPSec,AnyConnect | ** Online | Hong Kong | 150% |
| london.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | London,UK | 100% |
| ovb.link.ac.cn | Chrome 插件,IPSec,IKEv2,AnyConnect | ** Online | Novosibirsk,Russia | 100% |

服务器选择说明

电信用户推荐选择 HK ,Tokyo2 , Tokyo 3,San Francisco, Los Angeles 的服务器

不同地区网速差异显著，如果您觉得当前服务器速度不好，请尝试其他服务器

联通用户推荐 Tokyo2 ，HK1 或 Los Angeles 服务器

教育网IPv6 用户可以选择 Tokyo , Tokyo2 或者全局模式 这几个节点均支持IPv6 可以免教育网流量。目前 IPv6 仅支持在Chrome 插件中使用

由于中国网络出口速度的不稳定性，如果您认为当前速度不理想，可以尝试其他服务器

  

|  |
| --- |
|  |

  

在 PC 或 Mac 中使用 AnyConnect 客户端
-----------------------------

AnyConnect VPN

优点：

可智能代理。不影响访问国内网站的速度，可以一直打开VPN 可在某些系统VPN无法连接的特殊网络环境中使用

配置步骤 1. 根据您的设备类型下载安装对应版本的 AnyConnect 客户端。

Windows [AnyConnect-win-4.2.02075](https://static.link.ac.cn/anyconnect/anyconnect-win-4.2.02075-pre-deploy-k9.msi)

MacOS [AnyConnect-macosx-i3864.2.02075](https://static.link.ac.cn/anyconnect/anyconnect-macosx-i386-4.2.02075-k9.dmg)

Linux 64bit [Anyconnect-linux-64-4.2.02075](https://static.link.ac.cn/anyconnect/anyconnect-linux-64-4.2.02075-k9.pkg)

Linux 用户还可以在对应发行版源中安装openconnect， 设置信息请参照 Android 上openconnect 教程

2. 安装 AnyConnect VPN 。Mac 用户请注意 **仅安装VPN即可，其他附加软件不用安装**

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/1844B102-C3C2-4AAA-9E8C-BEC6A62E3DB1.png)

3. 打开 AnyConnect VPN 在地址栏中输入hk.link.ac.cn 点击连接。 ![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/AF4978DC-1FB6-4305-BE49-6002A7849850.png)
4. 输入用户名后即可连接并自动更新所有服务器列表。用户名是您注册所使用的 Email 地址。断开 VPN 之后您就可以在下拉列表中看到所有可用的服务器。

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/C54AF003-4965-4F95-BE5E-477A090A4260.png)

### 关于节点的说明(必读)

\*\*不同地区网速和网络情况差异巨大，默认节点可能速度不理想，请您根据您的情况选择合适的节点。

### 关于分组的说明(必读)

**目前的三个分组分别为 global （全局），smart（非中国IP走代理），smart-bllacklist（部分无法直接访问IP走代理） 请您按照您的需求选择合适的分组。 由于AnyConnect限制，某些情况下IP判断可能有误，请您注意**

**使用 global （全局）和 smart（非中国IP走代理）模式时请注意 : 如果使用用迅雷，电驴等等p2p工具下载盗版电影。请断开VPN 连接。如被机房发现下载盗版电影或软件并投诉，我们将会永久删除您的账户**

|  |
| --- |
|  |

  

本教程适用于 BlueCloud 标准套餐
---------------------

Chrome 插件（强烈推荐）
---------------

优点：

* 配置简单，只需在Chrome安装插件后即可使用
* 可以自动区分国内外流量
* 适合不想折腾主要用来浏览网页的用户

配置方法请参见 [在 Chrome 下使用我们的服务](https://bluecloud.xyz/page/view/8)

Cisco AnyConnect (推荐)
---------------------

优点：

* 配置简单
* 可以自动区分国内外流量

配置方法请参见 [使用 AnyConnect](https://bluecloud.xyz/page/view/16)

IPSec VPN 方式
------------

优点：

* 连接速度快

缺点：

* Mac 系统会在连接一定时间后强制断开连接

支持 OS X 10.7.X 以及更高版本

配置步骤：

1. 进入系统偏好设置

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/E9960310-4FD2-4A51-958A-E24FBDE0807D.png) 2. 点击网络 然后再单击左下角的 **加号** 并选择对应接口和 VPN 类型。如下图

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/53752037-BDA4-4EBF-98AA-2EEC31188944.png) 3. 在刚才新添加的VPN连接设置中，点击 **鉴定设置** 。然后输入密钥，并保存。共享密钥为 **otin**

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/BDF58084-C1CF-48E9-8BCC-C25208884F19.png) 4. 最后，输入服务器地址 （请从服务器列表中支持 IPSec 的服务器中选择 [服务器地址](https://bluecloud.xyz/server) ），您注册使用的 **Email** 做为账户名称。密码与网站登录密码相同。 再点击应用以保存设置。 之后再点击 连接 按钮即可连接到VPN。

![](.evernote-content/A636FDF0-76AF-480B-8EA1-EEF3958E8898/61DB1735-68CF-4BDA-9BEA-8C0C8AC98A87.png)

**请注意 : 如果使用用迅雷，电驴, BT 等等p2p工具下载盗版电影。请断开VPN 连接。如被机房发现下载盗版电影或软件并投诉，我们将会永久删除您的账户**

---

[🌐 原始链接](https://bluecloud.xyz/page/view/10)

[📎 在印象笔记中打开](evernote:///view/207087/s1/7f744e30-3d20-46e8-b530-14dfe4155b8b/7f744e30-3d20-46e8-b530-14dfe4155b8b/)