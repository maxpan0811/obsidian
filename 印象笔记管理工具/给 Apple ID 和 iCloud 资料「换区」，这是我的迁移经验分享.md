# 给 Apple ID 和 iCloud 资料「换区」，这是我的迁移经验分享

---

智能摘要

备份中的内容，在退出iCloud账号后，依然储存于设备上，只须等待上传至新的Apple ID中。如果你的设备没有使用Apple ID登录，那么你将无法在这些设备上访问"隐藏邮件地址"。待更换Apple ID后，取消「设置」中的本地账户，即可上传至新的iCloud中。第三方App中，直接在iCloud云盘中储存数据的App(如Taio)，在拷贝iCloud云盘文件的过程中，已完成了备份。

原文约 5103  字  | 图片 24 张 | 建议阅读 11 分钟 | [评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2024-01-27&nu=5ac0b0c9-cd45-4b63-96ed-e1d987aec415&fr=myyxbj&ud=328ef&v=2&sig=79F6A8C259AEC208F8DD72A2B577A735)

近日，我更换了设备的 Apple ID，自中国大陆地区的账户更改为美国地区的账户，同时迁移了原账户的 iCloud 内容与数据。迁移过程中，我参考了少数派作者 ElijahLee 的[《更换 Apple ID 后的资料备份与迁移，我是这样做的》](https://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247568448&idx=1&sn=5d0ff7a1c9671061675dfed38832efb9&chksm=fdb2392acac5b03c589b90923ccf505261590944ac3924cea8cbd506a881485f04d95571f5f0&mpshare=1&scene=1&srcid=0127L6k0XwZeuVybUoJRQJ9b&sharer_shareinfo=9b0bfe08af9011579886469394c686c1&sharer_shareinfo_first=9b0bfe08af9011579886469394c686c1#rd)一文，也碰到了一些随时间推移、系统更新产生的新的问题，在此记录。

本文基于 iOS 17.2.1，iPadOS 17.2，macOS 14.2.1 系统下的设备。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/D1838779-6173-4069-89DB-06C5108B9659.png)

注：如果仅是想要更改账户地区，在用完 Apple ID 上的所有余额后，参见 Apple 支持的《更改 Apple ID 国家或地区》[1] 进行更改，可以免去 iCloud 迁移之累、资料损失之虞。

**▍****设备上的 Apple ID**

Apple 支持将不同的 Apple ID 分别用于 iCloud 与媒体订阅和购买项目 ，即在 iPhone 或 iPad 的「设置」> [你的姓名] 中登录第一个 Apple ID 用于 iCloud，在 App Store 中登录第二个 Apple ID 用于媒体订阅和购买项目。本文中出现的「更换 Apple ID」「更换 iCloud 账户」等描述一般为前者。

**☁️**
------

**iCloud 保存内容的方式**
------------------

为了尽可能确保迁移数据的完整性，先了解一下 iCloud 保存了哪些内容。

* iCloud 保存内容的方式有两类：同步和备份 。
* 如果订阅了 iCloud+，则可能还使用了其提供的功能，如「隐藏邮件地址」。
* 「通过 Apple 登录」功能同样建立在使用相应 Apple ID 登录 iCloud 的基础上。
* AirPods、AirTag 或「查找」网络中的其他配件或设备 ，须提前解除与 Apple ID 的配对。

分别描述如下：

**▍****同步**

同步指的是信息自动同步云端，每次更改后在所有设备上保持最新状态，如：

* iCloud 照片（在照片设置中开启 iCloud 照片）
* iCloud 云盘
* 备忘录
* 密码和钥匙串（包含通行密钥 、无线局域网密码 ）
* iCloud 云端「信息」
* 查找
* 家庭
* Apple Books
* 使用 iCloud 的第三方 App，如 GoodLinks

使用同步功能的 App，可以在「使用 iCloud 的 App」中查看，前往：

* iPhone 或 iPad：「设置 > [你的姓名] > iCloud > 使用 iCloud 的 App」
* Mac：「 > 系统设置 > [你的姓名] > iCloud > 使用 iCloud 的 App」

须注意的是，iPhone、iPad、Mac 所列出的 App 不尽相同，应分别检视。

iCloud 同步的内容，在退出 iCloud 账户后，仅有部分可以保留副本，因此这是迁移过程中应关注的重点。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/4223DAE2-BF31-4654-BA13-8C1DA31F377E.png)

使用 iCloud 的 App

**▍****备份**

备份指的是 iPhone 和 iPad 上储存的尚未同步到 iCloud 的所有信息和设置，包括：

* 设备设置、主屏幕布局和 App 排列方式
* Apple Watch 备份
* 不使用 iCloud 同步功能的 App 数据，如微信的聊天记录

此外，如果未启用「iCloud 照片」、iCloud 云端「信息」等服务，即这些内容仅本地储存于当前设备，那么 iCloud 会对其进行备份。

iCloud 备份中的内容，在退出 iCloud 账号后，依然储存于设备上，只须等待上传至新的 Apple ID 中。为保护数据安全，建议在此之前先进行一次完整的本地备份。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/9E850B20-B0A7-4187-8BAD-64D79153001D.jpg)

自上而下依次为使用 iCloud 的 App，iCloud 备份

**▍****iCloud+ 功能：隐藏邮件地址**

「隐藏邮件地址」指的是创建随机且唯一的电子邮件地址并将其中的邮件转发到个人收件箱（与 Apple ID 关联的电子邮件地址）。

创建的电子邮件地址可以前往 iPhone 或 iPad 的「设置」、Mac 的「系统设置」里**[你的姓名] >「iCloud」>「隐藏邮件地址」**中检视。

根据 Apple 的说明：

> 请确保你在每台设备上都使用相同的 Apple ID 登录。如果你的设备没有使用 Apple ID 登录，那么你将无法在这些设备上访问“隐藏邮件地址”。

「隐藏邮件地址」与 Apple ID 绑定，我没有找到迁移方法，只能逐项检查确认。

在退出所有设备的 Apple ID 后，iCloud+ 订阅生效期间，可以访问 iCloud.com（中国大陆地区为 iCloud.com.cn）管理「隐藏邮件地址」。注意：iCloud+ 订阅失效后，将无法在网站上访问「隐藏邮件地址」。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/BCC18D77-F01D-4E69-8348-C74EFB79D200.jpg)

左图为 iCloud+ 订阅状态，右图为 iCloud+ 未订阅状态

**▍****通过 Apple 登录**

「通过 Apple 登录」功能基于当前 Apple ID，常与「隐藏邮件地址」共用。目前我没有找到迁移方法，只能手动登录第三方 App 和网站进行换绑。

尽管网页以及安卓或 Windows 等平台也能接入「通过 Apple 登录」功能，同个服务商的 iOS 平台 App 支持而其安卓平台 App 不支持该功能的情形亦时有发生（如 Duolingo、Pokemon Sleep），提请注意。

查看配合「通过 Apple 登录」功能使用的 App，前往 iPhone 或 iPad 的「设置」、Mac 的「系统设置」里的 **[你的姓名] >「登录与安全性」>「通过 Apple 登录」**；或登录 appleid.apple.com 查看。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/D1203EE4-E280-4658-875A-D2A9759BAB1D.png)

**▍****AirPods、AirTag 等设备或物品**

根据 Apple 的说明：

> 如果你在尝试设置 AirPods 等 Apple 设备、AirTag 等物品或“查找”网络中的另一个配件时看到一条信息，提示相应设备或物品已与另一个 Apple ID 配对，则这个设备或物品需要先从那个 Apple ID 中移除，然后才能与新的 Apple ID 配对。原拥有者可能必须按照相应步骤取消配对。

> 这些步骤是将设备或物品从 Apple ID 中移除及取消配对并移除“查找锁定”的唯一方法。这些操作可以在使用同一 Apple ID 登录的任一 iPhone、iPad、iPod touch 或 Mac 上完成。Apple 无法为你移除“查找锁定”。

> 重置设备或物品时，设备或物品不会将自身的位置信息提供给原拥有者。尽管如此，你仍无法将相应设备或物品与另一个 Apple ID 配对。

如果不预先移除 AirPods、AirTag 等物的配对，新的 Apple ID 将无法与之配对。移除步骤在「查找」App 中进行，详见 https://support.apple.com/zh-cn/102620。

**📱**
-----

**备份设备**
--------

在迁移资料之前，先完整地本地备份一次所有设备。

**▍****备份 iPhone、iPad 和 iPod touch**

**在电脑上进行的备份不包含已通过 iCloud 同步的数据**，如 iCloud 照片、iCloud 云端「信息」。

* 为备份 iCloud 照片，须先下载完整大小副本 ，并关闭 iCloud 同步。注意：操作前请确认 iCloud 照片已在所有设备上同步，以免遗漏（下同）。前往**「设置 > [你的姓名] > iCloud > 照片」**，选择「下载并保留原片」，待完成下载后，关闭「同步此 iPhone」。
* 备份 iCloud 云端「信息」的方式相似。前往「设置 > [你的姓名] > iCloud > iCloud 云端“信息”」，关闭「在此 iPhone 上使用」，信息将下载至设备。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/048F3AF4-8273-4027-99DF-FCC75E904A1D.jpg)

关闭 iCloud 照片，iCloud 云端「信息」

iPhone 备份包含了 Apple Watch 的备份，详见 https://support.apple.com/zh-cn/HT204518。

通过 Mac 或 PC 进行备份的具体步骤，详见 https://support.apple.com/zh-cn/HT203977。

备份时，选择「将 iPhone 上所有的数据备份到此 Mac」，并勾选「加密本地备份」来备份「健身记录」「健康」和「钥匙串」数据 。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/94E8D0B9-830F-4A61-8CB1-B526619F99B7.png)

通过「访达」进行备份

**▍****备份 Mac**

经过上述操作后，iPhone 等设备的备份已储存于 Mac 上。

备份 Mac 的具体步骤，可以参考 https://support.apple.com/zh-cn/104984。

**💾**
-----

**可保留副本的数据**
------------

在退出 iCloud 账户前，部分使用 iCloud 的 App 数据可作为副本下载，保留至设备中。

**▍****iCloud 照片、iCloud 云端「信息」**

通过「下载并保留原片」，可以保留 iCloud 照片至设备。通过关闭 iCloud 云端「信息」，可以保留 iMessage、短信等至设备。具体步骤见前文「备份设备：备份 iPhone、iPad 和 iPod touch」部分，或者访问 icloud.com 下载图库照片。

**▍****手记**

iPhone：「设置 > [你的姓名] > iCloud」，轻点「显示全部」，关闭「手记」，选择「保留于 iPhone」。

### ****▍**快捷指令**

更换 iCloud 账号后，会保留已添加的的快捷指令与自动化。

### ****▍**天气**

更换 iCloud 账号后，会保留天气 app 中添加的地区。

**▍****日历、股票、健康、通讯录、钥匙串、Safari**

在退出 iCloud 账号时，系统会提示是否保留以上资料的副本。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/0824EFCA-EB27-47F0-940E-AA07C544D8E1.jpg)

退出 iCloud 时的提示

* 按照 ElijahLee 的建议，为避免数据重复，保留除「日历」以外的项目。
* 更换 Apple ID 后，可能需要重新订阅特定地区的节日日历 。
* 如果保留了「通讯录」的副本，更换 Apple ID 后，设备上的通讯录可能未及时自动上传至 iCloud。前往**「设置 > [你的姓名] > iCloud」**，关闭再开启一次「通讯录」。

**💾**
-----

**手动下载的数据**
-----------

**▍****iCloud 云盘**

iCloud 云盘上的所有数据，会在退出 iCloud 时从设备上移除，因此先将其拷贝至本地位置。

在 Mac 上，打开「访达」，点按窗口边栏的「iCloud 云盘」，选择全部文件（Command + A），拷贝并粘贴至本地位置，离线文件会在拷贝到新位置前先下载到设备。

在 iPhone、iPad 或 iCloud.com 拷贝文件的步骤可以参考 Apple 支持的说明：https://support.apple.com/zh-cn/HT204055。

**▍****备忘录**

在 Mac 上，前往「备忘录」的「设置」，启用本地账户，将 iCloud 下的备忘录文件夹依次拖入本地账户。

* 默认的名为「备忘录」的文件夹无法直接拖动，点按该文件夹后，全选其中的备忘录（Command + A），拖入本地账户的新建文件夹中暂存。
* 待更换 Apple ID 后，取消「设置」中的本地账户，即可上传至新的 iCloud 中。
* 如「备忘录」设置了密码，须先关闭密码。
* 迁移后，「标签」会临时失效。重新添加一次标签后，所有带有该标签的备忘录会重新建立索引。建议迁移前，对原来的所有标签，截图记忆。

在 iPhone 或 iPad 上的操作类似。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/F6CDB5AF-4877-4D41-A0BD-21CE89C94C4E.png)

我的 Mac，即本地账户

**▍****语音备忘录**

在 Mac 上，可直接拖放所有录音至本地位置。

在 iPhone 或 iPad 上，也可以复制或共享录音，详见 https://support.apple.com/zh-cn/HT204055。

**▍****音乐备忘录**

「音乐备忘录」App 中的内容储存于 iCloud 云盘的同名文件夹，在拷贝 iCloud 云盘文件的过程中已完成备份。「音乐备忘录」不再更新，也可以先将其中的录音导出到「语音备忘录」。

**▍****图书**

在 Mac 上，打开「图书」，点按窗口侧栏「书库 > 全部」，全选（Command + A）拖放至本地文件夹。

**▍****重点和备注**

导出的书籍不包含「重点和备注」和「书签」。「重点和备注」可以手动导出。

* 在 Mac 上，点按书籍左上角的「显示高亮标记和笔记」，右键选择一项，全选（Command + A）后拖放至文本编辑器中。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/A9630A44-E2BE-423B-8D52-264ECFA95A6D.gif)

在 Mac 上拖放

* 在 iPhone 或 iPad 上，轻点书籍右下角的标识，轻点「书签与重点」，长按「重点」中的项目，轻点「选取」，选择所有项目（或参考下图方式），拖放至文本编辑器中。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/AF7C994D-34D9-4B32-9706-E5A15CAB1F1F.gif)

在 iPhone 上拖放

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/C49E9EB7-AAD8-4F80-ABE6-56285E2548AE.png)

邮件共享

**▍****自定义短语**

在 Mac 上，可以拖放导出、导入自定义短语，详见 ElijahLee 文中「自定义短语」部分 。

**💾**
-----

**其他数据**
--------

**▍****iCloud 邮件**

添加原先的 iCloud 账号以使用邮件功能：

* iPhone 或 iPad：「设置 > 邮件 > 账号」，添加 iCloud 账号。
* Mac：「 > 系统设置 > 互联网账户」，添加 iCloud 账号。

也可以从 iCloud.com 访问 iCloud 邮件。或者参考 https://support.apple.com/zh-cn/100627 将电子邮件从 iCloud 移动或拷贝到 Mac 。

**▍****提醒事项**

如上述，添加原先的 iCloud 账号后，也可以在相同位置启用「提醒事项」。

注意：如果原账号开启了「高级数据保护」功能，则无法通过该方式启用「提醒事项」，也无法在 iCloud.com 上直接查看（须 Apple 受信任设备授权）。

一个折衷的办法是，将提醒事项列表与新的 Apple ID 共享。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/20D6957A-432F-42C1-A0CB-5BF36F87BE7F.png)

左图为开启 iCloud 高级数据保护，右图未开启

**▍****钱包**

「钱包」中的银行卡、交通卡、钥匙等都将被移除，自行添加的会员卡、票券等可以保留。

交通卡上的余额，可以通过发卡机构的 App 进行退款操作。在「钱包」中选择交通卡，轻点右上角符号，选择「卡片详细信息」，可以看到发卡机构的 App。

不同发卡机构的退款操作略有不同，如上海交通卡在同名 App 内申请退卡，余额退回至 App 中（可提现或充值使用）；宁波交通卡在「宁波市民卡」App 内申请退卡，余额退回至原支付账户或支付宝中。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/AD3B17C2-53FB-4032-9F68-CF3719B46B09.png)

发卡机构的 App

**▍****音乐**

在 Mac 上的「音乐」App 中，可以导出 XML 格式的播放列表，导入新的资料库中，详见 https://support.apple.com/zh-cn/guide/music/mus27cd5060f/mac。

ElijahLee 介绍了通过关注 Apple Music 账户的方法迁移播放列表，详见其文 Apple Music 部分 。中国大陆地区账户可能无法使用此功能。

**▍****地图**

如果想要迁移「地图」App 中的「指南」，参见 ElijahLee 文中地图「指南」部分 。

**▍****健身**

更换 Apple ID 后，「健身」App 保留了我的奖章、好友。

此处存疑，好友关系应该与添加时的 Apple ID 相关，我的好友也仅有不常联系的一位，不能确信。

**▍****Game Center**

更换 Apple ID 后，未保留 Game Center 的朋友关系、成就。

在 iPhone 或 iPad 的「设置」、Mac 的「系统设置」的「Game Center」处，可以退出登录账号。

**▍****iMessage、FaceTime**

更换 Apple ID 后，iMessage、FaceTime 使用的 Apple ID 可能仍为上一个。可以前往 iPhone 或 iPad 的「设置」，在「信息」「FaceTime」处登录新账号。

### ****▍**家庭**

我没有找到「家庭」中的配件的转移方式，只能重新添加。

### ****▍**其他**

以下内容见前文「iCloud 保存内容的方式」相应副标题处：

* 隐藏邮件地址
* 通过 Apple 登录
* AirPods、AirTag 等设备或物品

**💾**
-----

**使用 iCloud 的第三方 App 数据**
-------------------------

第三方 App 中，直接在 iCloud 云盘中储存数据的 App（如 Taio），在拷贝 iCloud 云盘文件的过程中，已完成了备份。待更换 iCloud 账号后，重新导入 iCloud 云盘即可。

另有一些 App 的数据，储存于 iCloud 内部，在退出 iCloud 账号时可能会清除，须在各个 App 内寻找导出的方式。在「使用 iCloud 的 App」中确认须转移资料的 App。前往：

* iPhone 或 iPad：「设置 > [你的姓名] > iCloud > 使用 iCloud 的 App」
* Mac：「 > 系统设置 > [你的姓名] > iCloud > 使用 iCloud 的 App」

须注意的是，iPhone、iPad、Mac 所列出的 App 不尽相同，应分别检视（该部分较为重要，故引用前文再注释一遍）。

迁移方式因 App 而异，以下列出两例。

**▍****GoodLinks**

在 iPhone 或 iPad 上，打开 GoodLinks，轻点左上角「设置」>「高级」>「导出资料」，选择一个本地文件夹，导出 JSON 格式的文件。登录新的 iCloud 账号后，重新导入。

**▍****1Password 7**

在 iPhone 或 iPad 上，打开 1Password 7，轻点「设置 > 高级 > 创建备份」。使用数据线连接 iPhone 至 Mac，打开「访达」，点按窗口边栏的 [你的 iPhone 名称] >「文件」，展开「1Password 7」，将「Backups」文件拖放至「访达」的本地文件夹中。登录新的 iCloud 账号后，拖放回原位置。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/1DC56ADA-04A8-4644-9ACF-CD1A1B6A2330.png)

**❓**
-----

**迁移过程中出现的问题及解决方案**
-------------------

**▍****无法退出 Apple ID**

如果「设置 > [你的姓名] > 登出」为灰色，提示「因为某些限制，无法登出」，可能是因为启用了「屏幕使用时间」。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/893DCE24-DB26-4CBB-A5C9-766DC613D878.png)

**解决方案：**

* 前往「设置 > 屏幕使用时间」，轻点底部的「关闭 App 与网站活动」；
* 轻点「更改屏幕使用时间密码」，选择「关闭屏幕使用时间密码」；
* 关闭「在设备之间共享」；
* 轻点「内容与隐私限制」，确认「允许变更」部分「账户更改」设置为「允许」。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/A2DB55FF-BEAF-4B78-93AC-B88D38D40D38.png)

**▍****迁移后「照片」缺失**

我在第一台设备上登录新的 Apple ID 后，发现本地以及随后上传至 iCloud 的照片、视频数量有失，其中八千余照片中缺失约两百张，两百余视频中缺失约二十张。

在退出 iCloud 账号时，系统应该会提示尚有「照片」数据在云端，但当时未提醒我。推测是我将 iPhone 放置一晚用于下载原图，有少量数据未下载成功。后来经过排查，发现大部分是体积较大的视频、照片。

我尝试用另一台设备下载原图，上传至新的 iCloud 账户，但仍有缺失。后来通过 Mac 多用户功能（见下文），登录原先的 Apple ID，在「照片」App 中排查补全（所幸数量不多）。

如果担心出现这类情况，可以从 iCloud.com 下载所有照片和视频，再导入「照片」App，上传至新的 iCloud 账户。

☁️

**管理原先的 Apple ID**

**▍****访问 iCloud.com 查看数据**

在 iCloud.com（中国大陆地区为 iCloud.com.cn ）查看原先的 iCloud 数据。

注意：如果此前开启了「高级数据保护」，且当前无使用此 Apple ID 登录的受信任设备 ，将无法查看照片、备忘录、提醒事项、文件和文稿等数据。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/50B9E327-17B3-4769-AC46-E997F1050142.png)

**▍****使用闲置的 iPhone 或 iPad**

在闲置的 iPhone 或 iPad 上查看原先的 iCloud 数据。

注意：如果此前开启了「高级数据保护」，不支持低于 iOS 16.2、iPadOS 16.2 和 macOS 13.1 的设备。

**▍****使用 Mac 的多用户功能**

在 Mac 上添加用户，使用原先的 Apple ID 登录以查看数据。

此方法可以查看到原先 Mac 上能访问的绝大部分 iCloud 数据，并能将符合要求的 Mac 用于「高级数据保护」的授信，切换用户也比较方便。操作详见下方链接。

🔗 https://support.apple.com/zh-cn/guide/mac-help/mchl3e281fc9/mac

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/EAE7F702-4CDC-4349-A975-65977F9F0FAB.png)

「快速用户切换」窗口

**▍****访问 appleid.apple.com 管理账户信息**

登录 appleid.apple.com ，更新密码、更新 Apple ID 电子邮件地址等 ，查看配合「通过 Apple 登录」功能使用的 App。

根据 评论中网友「liberatechina」所述 ，删除的 Apple ID 使用的电子邮件地址将被占用，无法用于注册新的 Apple ID。如果后续准备删除原先的 Apple ID，可以先更改 Apple ID 电子邮件地址为不常用地址。

**▍****访问 privacy.apple.com 管理储存于 Apple 的个人信息**

登录 privacy.apple.com ，访问「数据和隐私」页面上的隐私管理工具 ，获取数据拷贝，暂时停用或永久删除 Apple ID 等。也可以在此获取 iCloud 照片、iCloud 云盘文件等的拷贝，Apple 的准备时间最多可能需要 7 天。

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/474A7469-7F6C-41D6-8F5D-4728C278A8A8.png)

以上为我于 2024 年 1 月迁移 iCloud 账户数据的经验，部分操作具有时效性，具体操作可参考 Apple 支持的文章，获取最新信息。

原文链接：

https://sspai.com/post/85912?utm\_source=wechat&utm\_medium=social

作者：宴息

责编：waychane

******/****更多热门文章****/******

[![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/48458386-C810-4100-8DB2-4DA83FF6AEC1.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247568319&idx=1&sn=86250b04ef83c67c155f7324e14e2553&chksm=fdb23ed5cac5b7c37365e486b5a21dc8fdd9b343fd438760c3a7329df12ce71bbd43dd988101&scene=21#wechat_redirect)

[![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/0CEEFA87-04B3-4D2D-825C-45CB3929A90F.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247568263&idx=1&sn=c1f93ca11f1fcdf2913b70696118a788&chksm=fdb23eedcac5b7fbae7dc41b89ee6c987fe2522f3cac4db74f7f660c9f42900b3da20b1a6176&scene=21#wechat_redirect)

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/A2A1B240-8519-44BD-AF54-1BA9556898FD.png)

![](.evernote-content/EA5187C3-C73D-4B14-9E85-F18398437583/E0D1CC26-8CF7-4F58-BFFA-93BA6244AA1F.gif)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247568448&idx=1&sn=5d0ff7a1c9671061675dfed38832efb9&chksm=fdb2392acac5b03c589b90923ccf505261590944ac3924cea8cbd506a881485f04d95571f5f0&mpshare=1&scene=1&srcid=0127L6k0XwZeuVybUoJRQJ9b&sharer_shareinfo=9b0bfe08af9011579886469394c686c1&sharer_shareinfo_first=9b0bfe08af9011579886469394c686c1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/784a8623-e90f-49c2-af91-f68c911d2bc9/784a8623-e90f-49c2-af91-f68c911d2bc9/)