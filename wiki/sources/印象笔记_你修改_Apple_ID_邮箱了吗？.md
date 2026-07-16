---
title: "你修改 Apple ID 邮箱了吗？"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/你修改 Apple ID 邮箱了吗？.md
tags: [印象笔记]
---

# 你修改 Apple ID 邮箱了吗？

# 你修改 Apple ID 邮箱了吗？ --- 国内很多用户是使用网易、163、QQ 一类的邮箱做为 Apple ID 的登录帐号，遭遇过一次网易邮箱被拖库的安全事故后不知道还有多少人依旧在使用。没

---

# 你修改 Apple ID 邮箱了吗？

---

国内很多用户是使用网易、163、QQ 一类的邮箱做为 Apple ID 的登录帐号，遭遇过一次网易邮箱被拖库的安全事故后不知道还有多少人依旧在使用。没有启用「双重验证」的账户，邮箱依旧是密码重置的主要途径之一，以往 Apple 只允许用户更换成其他的第三方邮箱地址，如今会推荐更新为 iCloud 或 me 的邮箱。

![](.evernote-content/25B1C183-2DE4-42EF-9A6F-0A92E52335C7/BFEB89A9-775F-422C-91F4-56BA4F4636F6.png)

更换有什么好处呢？
---------

其实如果已经启用了「双重验证」，即便对方攻破了你的邮箱地址，对 Apple ID 的安全没啥影响，你的邮箱地址只是一个登录用的名称，不会发送密码重置邮件到这个邮箱。没有启用「双重验证」就不一样了，通过邮件地址接收邮件可以重置密码。所以换成 iCloud 的邮箱总是没有坏处的。

Apple ID 邮箱地址通常会收到一些安全方面的通知邮件：

* 「查找我的 iPhone」已在 iPhone 上禁用
* 已为您的 Apple ID 生成 App 专用密码
* 您的 Apple ID 信息已更新

用 iCloud 的邮箱比使用国内的邮箱地址更安全，iOS 和 macOS 上启用 iCloud 就等于启用了 iCloud 的邮箱，不用额外配置，支持邮件的推送。

如何更换为 iCloud 的邮箱
----------------

登录 [Apple ID 管理网站](https://appleid.apple.com/) ，编辑你的 Apple ID。如果你以前已经注册过 iCloud 甚至更早的 me 的邮箱，直接填写邮件地址即可。

![](.evernote-content/25B1C183-2DE4-42EF-9A6F-0A92E52335C7/A0C7A866-E112-41AA-A204-046D4F8556EC.png)

更换 Apple ID 邮箱地址后，所有使用这个 Apple ID 登录的设备都需要重新登录一次完成安全验证。Fantastical 一类读取 iCloud 日历的应用需要重新生成「App 专用密码」。

> 提示：一旦换成 Apple 系的邮箱就不能再更换成第三方的邮箱地址作为 Apple ID。

从列表中移除设备
--------

「双重验证」有个不好的地方，就是没法单独选择不需要发送验证码的设备。每次登录验证的时候一圈同一个 Apple ID 登录的设备都会弹验证信息窗口。

和 iPhone、Macbook 不同，家里的 iPad 设置的是 4 位数的弱密码，每次看到它也弹窗口的时候都想把它从双重验证里踢出去。然而，Apple 并没有针对这个需求的方案，要么直接「从列表中移除设备」，要么一起弹窗。

![](.evernote-content/25B1C183-2DE4-42EF-9A6F-0A92E52335C7/065751F8-B91D-4EA5-8686-5141E2A4F6A5.png)

基于同样的理由， 不常用的旧设备还是移除了比较好。移除设备可确保它不再显示验证码，当然它也无法再访问 iCloud 和其他 Apple 服务（包括「查找我的 iPhone」），直到您再次通过双重认证登录。

Apple ID 更换可能带来的其他问题
--------------------

更换 Apple ID 邮箱地址后，AirDrop 好像出问题了，想想也对，MacBook 和 iPhone 彼此的发现是基于 Apple ID 的邮箱地址的，AirDrop 设置成「所有人」双方都能看到说明蓝牙连接和 AirDrop 访问是正常的，改成「仅限联系人」之后 iPhone 能看到 MacBook，反过来 MacBook 看不到 iPhone，所以问题应该还是 Apple ID 更新后信息没有更新导致的。

遇到类似问题建议先试试：把 iPhone 和 Mac 上的蓝牙跟 WiFi 都「关闭 / 开启」一次。不行才考虑用注销登录的终极方式。

和 iCloud 账户有关的问题大多数都是 Apple ID 验证上的问题，iPhone 和 Mac 分别注销 iCloud 重新登录后问题解决。PS：Mac 上注销 iCloud 账户前请务必检查备份 iCloud Drive 及文稿中的数据，注销时也可以勾选在本地保留一个副本。

![](.evernote-content/25B1C183-2DE4-42EF-9A6F-0A92E52335C7/270F10CA-4CEA-4F13-97F5-E2CF82BDC466.png)

---

**参考文章：**

* [如果您忘记了自己的 Apple ID 密码](https://support.apple.com/zh-cn/ht201487)
* [Apple ID 的双重认证](https://support.apple.com/zh-cn/HT204915)

---

[🌐 原始链接](https://sspai.com/post/41621)

[📎 在印象笔记中打开](evernote:///view/207087/s1/d99c8783-d35c-4ba2-87eb-5a862ec71b7f/d99c8783-d35c-4ba2-87eb-5a862ec71b7f/)