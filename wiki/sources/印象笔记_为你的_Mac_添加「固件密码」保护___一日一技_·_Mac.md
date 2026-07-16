---
title: "为你的 Mac 添加「固件密码」保护 _ 一日一技 · Mac"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/为你的 Mac 添加「固件密码」保护 _ 一日一技 · Mac.md
tags: [印象笔记]
---

# 为你的 Mac 添加「固件密码」保护 _ 一日一技 · Mac

# 为你的 Mac 添加「固件密码」保护 | 一日一技 · Mac --- ![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/139

---

# 为你的 Mac 添加「固件密码」保护 | 一日一技 · Mac

---

![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/1391CCAA-4FF5-43DF-B5E3-4531966C23E4.jpg)

### *关于栏目*

「一日一技」是少数派的全新栏目，我们将会介绍各种简单又实用的小技巧。这些技巧可能是你知道的，也可能是你还未注意到的；它可能是一个系统的操作技巧，也可能是某个 App 里的细节功能或用法……我们希望通过这个栏目，让你更好了解手中的设备和 App，能更充分去利用它们的特性，以此一点点改善与提升你的数字生活。

数据安全是一个如何强调都不为过的问题。在 OS X 中，你可以通过多种方式去增强电脑的安全性，例如：

* 设置登陆密码，以防止未授权的登入行为；
* 使用 FileVault 2 进行全磁盘加密，以防止他人在未经授权的情况下（尤其是被盗取时）访问您的个人数据；
* 使用 Time Machine 备份，防止意外情形下的数据丢失。

但除此之外，我们还可以通过一个硬件层面的安全措施——固件密码（ Firmware Password ）来防止他人恶意从其它磁盘启动你的 Mac，重新安装系统 ，或通过恢复分区重置登陆密码或抹掉你的数据。

硬件要求
----

根据 Apple [支持页面](https://support.apple.com/en-us/HT204455) 的说明，正常开启「固件密码」的硬件要求为：

* MacBook Air（2010年末及其后机型）
* MacBook Pro（2010年初及其后机型）
* MacBook Pro with Retina display（所有机型）
* MacBook （12寸 Retina 屏幕，2015年初机型）
* iMac（2011年中及其后机型）
* Mac mini（2011年中及其后机型）
* Mac Pro（2013年末机型）

方法
--

步骤一：关闭你的 Mac。

步骤二：按住 `Command + R`（ ⌘R ） 组合键，并点按开机按钮，直到出现  标志，进入恢复模式（注：当然，你也可以先按开机键，在听到启动声后，立即按住 ⌘R 键）。

步骤三：选择「以简体中文作为主要语言」（或其他语言），点击向右的箭头。在「实用工具」菜单栏中选择「固件密码实用工具」。

![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/AE418DA2-F221-48CA-9FD5-3570B46D78C1.jpg)

步骤四：在出现的「固件密码实用工具」窗口中，点击「开启固件密码」。

步骤五：输入并确认所需要设置的密码，回车以完成。

步骤六：点击菜单栏中的 ，并选择「重启」或「关机」，下次启动时，固件密码将自动激活。

如果你希望关闭或更改固件密码，则只需在步骤四中选择「关闭固件密码」或「更改密码」，输入此前设置的密码，回车确认，并重启 Mac 即可。

最终效果
----

当你的 Mac 从默认磁盘启动系统时，将不会出现输入「固件密码」验证的窗口，而是会像平时一样，直接进入用户登录界面。

![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/AD9A0E00-524E-4CD1-AC97-6367AE7E1819.jpg)

但如果你从其他磁盘启动（如 U 盘恢复系统、Time Machine 备份磁盘、CD 或 DVD 介质等），或以恢复系统（ Recovery Mode ）、单用户或详细模式启动时，将出现认证窗口，提示你输入固件密码。只有正确输入密码后，方能进一步操作。

![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/8A1D8048-4DEF-4357-BFFB-D72FA7FBDAB6.jpg)

如果你在 Mac 上设置了「Find My Mac」，并通过 iCloud 远程锁定你的 Mac 时。那么他人在试图进入恢复模式或从其他磁盘启动时，将会出现「输入 PIN 码以解锁这台 Mac」的窗口，而不是固件密码的验证窗口。

![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/DCFD13F5-86E4-4C66-BE1B-0638AE8BE189.jpg)

注意
--

1. 1. 请一定要记住自己所设置的固件密码（再啰嗦一遍：推荐使用 [1Password](http://www.sspai.com/tag/1password) 或 [LastPass](http://www.sspai.com/tag/LastPass) 等专业的密码管理软件来记录自己所设置的密码）。否则，你就只能带上购买凭据，送去 Apple 零售店或授权服务提供商解锁了 :-(
   2. 固件密码的移除：大多数 2010 年以前生产的机型，可以通过首先移除某些系统内存，然后重启你的 Mac，使用 `Command + Option + P + R`（⌘⌥PR）组合键开机，一直到 Mac 重启为止。此时再松开，固件密码就将被清除。但对于大多数 2010 年以后生产的机型来说，则并不支持这种办法。
   3. 需要注意的是，固件密码对磁盘数据的保护是**间接**的，毕竟当磁盘被物理移除时，固件密码就不再起作用了。与之相反，即便是磁盘被物理移除，FileVault 2 也仍能够保护你的数据。因此，对安全性要求更高的用户，推荐使用 FileVault 2 或同时使用两者。

参考链接：

* [Apple Support: Use a firmware password on your Mac](https://support.apple.com/en-us/HT204455)
* [Apple Support: 如何以单用户模式或详细模式启动 Mac](https://support.apple.com/zh-cn/HT201573)
* [Apple Support: 使用 FileVault 加密 Mac 上的启动磁盘](https://support.apple.com/zh-cn/HT204837)
* [iDownloadBlog: Securing your Mac with a firmware password](http://www.idownloadblog.com/2016/03/04/how-to-set-mac-firmware-password/)

想要获得更多简单实用的小技巧？*[查看往期「一日一技」>](http://sspai.com/tag/%E4%B8%80%E6%97%A5%E4%B8%80%E6%8A%80)*

[![](.evernote-content/403FBE70-E164-44D0-975F-AD692D3B6FAC/B0A5DBF3-A598-4087-A3CB-63CA45DE41F4.jpg)](http://sspai.com/su/ay5)如果你希望通过赞助方式支持更多优质内容，请[联系我们](mailto:will@zookr.net)。

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/33355)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a5633a63-fa15-42b8-aaa7-c5697eaaf36e/a5633a63-fa15-42b8-aaa7-c5697eaaf36e/)