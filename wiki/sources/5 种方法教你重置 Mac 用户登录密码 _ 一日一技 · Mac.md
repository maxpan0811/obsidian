---
title: 5 种方法教你重置 Mac 用户登录密码 _ 一日一技 · Mac
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/5 种方法教你重置 Mac 用户登录密码 _ 一日一技 · Mac.md
tags: [印象笔记]
---

# 5 种方法教你重置 Mac 用户登录密码 | 一日一技 · Mac

---

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/10B44A81-C382-421B-AC8D-442886CBD06E.jpg)

作为鉴定用户身份的主要方式，用户密码（也称为登录密码）大概是我们在 OS X 中接触得最多且最重要密码之一了 —— 当我们登录用户账户、使用安装器安装应用程序以及进行某些重要的修改时都会用到它。

在日常使用中，为了避免用户密码被遗忘，我们不妨在设置密码的同时，设置密码提示，让我们在遗忘密码后能够更快地回忆起来；或将用户密码、FileValut 2 恢复秘钥等存储到 1Password 或 LastPass 等专业的密码管理应用中进行统一管理。

但即便如此，我们也还是可能会遇到自己或好友丢失或遗忘用户密码的情形。这时，了解几种重置用户密码的方法就显得十分必要了。

未开启 FileVault 的用户
-----------------

### 方法一：使用 Apple ID 重置

在 OS X Mavericks（10.9）及其后的系统版本中，Apple 对 Apple ID 和管理员密码做了整合，从而使得我们能够使用 Apple ID 对用户密码进行快速重置。

在使用此方法重置用户密码前，需要确保你的 Mac 已经登入 Apple ID，并已在「系统偏好设置 - 用户与群组 -登录选项」中勾选「允许用户使用 Apple ID 重设密码」。

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/8348CC3A-1880-4F89-B973-9908994177BB.jpg)

如果你并未勾选此项，请使用如下方法：

1. 在登录窗口中，连续输入一个密码三次，直到系统弹出提示窗口「如果忘记密码，您可以…使用您的 Apple ID 来重设 / 使用您的主密码来重设」。
2. 点击「使用您的 Apple ID 来重设」右侧的小箭头。随后输入 Apple ID 及密码，点击「重设密码」。
3. 在重设密码窗口中，设定并确认新的用户密码、密码提示信息（可选），完成后点击「重设密码」。
4. 重设完成后，重新启动 Mac，使用新密码登录即可。

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/4BA5B33F-1B2D-46A6-9248-3605F8623D24.jpg)

### 方法二：使用主密码重置

如果你此前设置过，并且依然记得主密码（Master Password）的话，那么也可以通过主密码去重置管理员、普通成员账户的用户密码。具体重置方法类似于「方法一」，不再赘述。

### 方法三：使用其他管理员账户重置

如果你知道 Mac 上另外一个管理员账户的名称和密码的话，那么不妨通过该管理员账户来重置密码。

1. 使用另一管理员帐户的名称和密码登录。
2. 进入「系统偏好设置 - 用户与群组」，点按小钥匙，输入密码以解锁。
3. 从用户列表中选择需要重置密码的用户，点按「重设密码」按钮，然后按照说明重设新密码。
4. 重设密码完成后，注销账户，使用新密码重新登录到你的账户即可。

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/D8D358B6-23B9-4276-B4AA-082EF9857947.jpg)

### 方法四：进入 OS X 恢复模式重置

1. 关闭你的 Mac。
2. 按住 `Command + R`（⌘R） 组合键，并点按开机按钮，直到出现  标志，进入恢复模式（Recovery Mode）（当然，你也可以先按开机键，在听到启动声后，立即按住 ⌘R 键）。
3. 选择「以简体中文作为主要语言」（或其他语言），点击向右的箭头。在「实用工具」菜单栏中选择「终端」。

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/4472543D-7D33-4E67-ADF6-8C06C5F3C3E2.jpg)

1. 在终端中输入命令（注：连写，且均为小写字母）：`resetpassword`，回车确认。
2. 在出现的「重设密码」窗口中，依次选择包含密码的启动磁盘卷宗、希望重设的用户账户；输入并确认新的用户密码，并为其设置密码提示信息（可选）；点击「重设」。
3. 点击菜单栏中的 ，并选择「重启」或「关机」。下次启动时，使用新密码登录即可。

开启了 FileVault 的用户
-----------------

对于已经启用了 FileVault 2 的 Mac 用户来说，在「用户与群组」面板中是不会显示「允许用户使用 Apple ID 重设密码」的。只有当你在此前设置 FileVault 2 过程中，勾选「允许我的 iCloud 账户解锁磁盘」，才可以使用 iCloud 账户解锁磁盘并重设密码。具体重置方法类似于「方法一」，故不再赘述。

如果你在设置 FileVault 2 过程，选择的是「创建恢复秘钥且不使用我的 iCloud 账户」，并保存了恢复秘钥的话，则可以使用恢复密钥重置用户密码。

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/D2A40024-4D56-4BE0-B09A-E87E5DBE031C.jpg)

1. 在登录窗口中，点按「 ？」，弹出提示窗口「如果忘记密码，您可以…使用您的“恢复秘钥”来重设密码」。
2. 点按右侧小箭头，密码栏将变为「恢复密钥」栏。
3. 输入您的恢复密钥，然后按照屏幕上的说明创建新密码。完成后，点按「重设密码」。
4. 重设完成后，重新启动 Mac，使用新密码登录即可。

重设用户钥匙串
-------

由于 OS X 的用户账户都有一个通过密码访问的本地加密钥匙串，并且其密码通常为该账户的用户密码。因此，当用户密码被重置后，新设定的密码将不再与他的钥匙串密码匹配，从而无法访问。为此，我们需要在首次登录时，根据系统提示更新或重设钥匙串密码。

* 如果你还记得钥匙串的旧密码，请选择「更新钥匙串密码」，从而恢复此前保存在钥匙串中的密码信息；
* 如果你忘记了旧密码，请选择「创建新钥匙串」；
* 如果你希望忽略系统提示的话，则可以选择「继续登录」（注：笔者强烈建议你不要这么做，因为后续诸多应用程序会「不厌其烦」地请求访问旧的钥匙串中的密码）。

![](.evernote-content/9C15CC53-0EC2-4141-81E2-C07FCA2FE5E1/EA98A03F-F3EB-4228-8037-D3B3F1C2C6BC.jpg)

▲ 图片来自：Kevin M. White: OS X Support Essentials 10.11

其他
--

**如何防止他人恶意重置我的用户密码？：**考虑到默认情况下，任何能够使用你的 Mac 的人（理论上）都可以进入恢复模式，并使用终端命令重置用户密码。因此，出于防止被恶意重置的考虑，不妨参照 [为你的 Mac 添加「固件密码」保护](http://sspai.com/33355) 一文设置固件密码，阻止他人进入恢复模式进行操作。

**参考链接：**

1. [Apple Support：Apple ID 可用于重设用户帐户密码](https://support.apple.com/zh-cn/HT202274)
2. [Apple Support：更改或重设 OS X 用户帐户的密码](https://support.apple.com/zh-cn/HT202860)
3. [Coolest Guides on the Planet: Reset Forgotten Admin Password OS X 10.11 El Capitan](https://coolestguidesontheplanet.com/reset-forgotten-admin-password-mac-osx/)
4. [Kevin M. White: OS X Support Essentials 10.11 - Supporting and Troubleshooting OS X El Capitan](https://www.amazon.cn/OS-X-Support-Essentials-10-11-Apple-Pro-Training-Series-Supporting-and-Troubleshooting-OS-X-El-Capitan-White-Kevin-M/dp/013442820X/ref=sr_1_4?ie=UTF8&qid=1461996551&sr=8-4&keywords=apple+support+essentials)

文章来源 [少数派](http://sspai.com) ，原作者 [修电脑的哲学家](http://sspai.com/author/717277) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/34023)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8b4a4aaf-c770-49fc-b90e-903ac9d7ad86/8b4a4aaf-c770-49fc-b90e-903ac9d7ad86/)
