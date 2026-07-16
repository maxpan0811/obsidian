---
title: "如何用手机指纹远程解锁 Windows 电脑 _ 工具推荐"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何用手机指纹远程解锁 Windows 电脑 _ 工具推荐.md
tags: [印象笔记]
---

# 如何用手机指纹远程解锁 Windows 电脑 _ 工具推荐

# 如何用手机指纹远程解锁 Windows 电脑 | 工具推荐 --- 如何用手机指纹远程解锁 Windows 电脑 | 工具推荐 ============================= | 本文

---

# 如何用手机指纹远程解锁 Windows 电脑 | 工具推荐

---

如何用手机指纹远程解锁 Windows 电脑 | 工具推荐
=============================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

如果你用过或者看过别人使用指纹来登录电脑，想必会觉得这项功能十分方便。因为指纹登录可以减少每次登录都要输入密码的麻烦，是能让生活更轻松的功能。更重要的是，由于输入方便，因此我们可以设置更加复杂的密码，来提升电脑的安全性。

但是，不是所有的笔记本电脑都自带指纹硬件，更不用说台式机了。虽然淘宝上面有通过 USB 插入的指纹识别硬件购买，但是价格都比较贵，还占用了一个笔记本电脑上面稀缺的 USB 口。

今天我就给大家带来一个免费的解决方案 —— 使用 [Remote Fingerprint Unlock](https://play.google.com/store/apps/details?id=ro.andreimircius.remotefingerauth) 应用来解锁你的 Windows 电脑。

效果
--

和拓展显示器与远程控制等软件类似，Remote Fingerprint Unlock 也需要同时安装手机端与电脑端，按照下文的安装步骤完成配置后可以将安卓手机虚拟化成为一个指纹识别硬件，从而开启指纹登录功能。实际使用起来非常迅速便捷：

![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/D29AE280-CA69-4970-BF46-E65606892C44.gif)

电脑开机时解锁

除了开机之后解锁电脑，Remote Fingerprint Unlock 还能通过发送 WoL（Wake on Lan，网络远程开机功能，大多数有线网卡都支持，无线网卡则因设备而异）**唤醒关机的电脑并解锁进入桌面，进入办公室 / 房间就能直接开始工作**：

![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/F2E686A2-5B65-4480-9485-5F5823258A6A.gif)

关机唤醒电脑并解锁

不仅如此，应用还支持多设备唤醒，甚至每个设备都可以用专门的桌面小部件来管理：

![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/C017517E-3D3F-40E0-8E5C-A69F35409AB3.gif)

桌面小部件解锁笔记本电脑

此外，每个添加的设备还可以单独登录多个不同的账户。最重要的是，只需要手机和电脑在同一个局域网 / 蓝牙配对 / Wi-Fi 热点的情况下就能实现远程解锁，比起电脑自带的硬件或者淘宝上购买的硬件，Remote Fingerprint Unlock 的连接方式与功能都更加丰富。

实现过程
----

使用 Remote Fingerprint Unlock 实现远程解锁电脑的步骤十分简单：

1. 同时安装[手机端](https://play.google.com/store/apps/details?id=ro.andreimircius.remotefingerauth)和[电脑端](https://drive.google.com/drive/folders/1bktvp0JcJKfE92efgxQlo06ARrMfLDFd)，访问不了谷歌硬盘的朋友可以在这个[国内备份链接](https://cdn.sspai.com/ee/remote%20fingerprint%20unlock%201.3.2.zip)下载手机端和电脑端。

   **提示：下面的步骤必须在电脑显示登录屏幕时设置。**
2. 在手机端的侧边栏菜单中选择「Scan」，或者点击右下角加号选择「By Scanning」来寻找所有已经安装电脑端的设备。

   ![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/1EB7D520-B1C9-4971-B6B1-0E0A2FA96FDA.jpg)

   扫描界面
3. 如果没有错误应该会立刻看到所有支持的设备，点击扫描出来的设备起一个自己喜欢的名字，连接方式选择「Wi-Fi Scan」（无线连接），想要关机唤醒的话还可以勾选「Send WoL-Packet」（高级版功能，售价 2.49 美元）。

   ![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/D7C0B31B-26C5-490C-A57D-9CA68A2A65B1.jpg)

   设置设备
4. 在手机端侧边菜单中选择「My Accounts」，点击连接设备列表的右下角的「Add account」添加要指纹登录的账户，账户名就是锁屏时候显示的名称，密码则是 PIN 或者 Microsoft 账户密码（取决于你的管理员账户类型），填完之后验证一下指纹。

   ![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/6A024D17-7C5D-48A2-8988-7405591EBFAA.jpg)

   添加登录账户
5. 确认手机上显示的 session ID 与电脑登录屏幕上 Fingerprint Unlock 显示的 ID，点击「Process」即可添加完毕。

   ![](.evernote-content/1C8CEA9D-9CC1-4F3C-BFE8-40B86A13C24C/14CA8830-7766-4A6F-BF7C-A2BDE66284EF.jpg)

   session ID 确认

这样整个流程就已经配置完毕，（开启 WoL）以后无论电脑处于什么状态，只要你在手机端主界面或者小部件上验证一下指纹，电脑就会登录并进入桌面。

原理
--

Remote Fingerprint Unlock 的电脑端是一个没有在后台运行的程序，只有在登录界面激活时才会被唤醒。在使用管理员权限安装时，电脑端会把自己提权为管理员权限，所以可以控制账户登录。这也是为什么电脑处于登录屏幕时才能配置手机端信息。

手机端配置时所有信息都会被加密然后生成一个 session ID，与电脑端的 session ID 对应后就能确认手机已经添加了账户信息，并将账户信息（包括账户名称与密码）用指纹生成的密钥加密保存到电脑上。

每次解锁计算机时，手机验证指纹成功后会利用这个指纹信息重新生成密钥，并将密钥与账户名称（注意，没有账户密码）发送到电脑，电脑再用这个密钥解密账户信息然后发送到 Windows 登录屏幕上正常登录。

安全性
---

除了便捷以外，Remote Fingerprint Unlock 的安全性是人们最关心的点，作者也专门针对这个做了[详细的解释](https://docs.google.com/document/d/1ZheUUDFRdiS81ufpSFyw7y7uzMwiPOOyrfenzFDsRGg/edit#heading=h.ztbsrkyk97)。

首先，每次解锁电脑时手机不会发送密码，仅发送账户名称，检查的只是每次登录屏幕上的 season ID。

其次，每次扫描指纹的时候都会生成一个唯一的密钥，这个密钥储存在手机本地上，只能通过成功扫描指纹获得。密钥被用来加密计算机上保存的账户信息，也就是说数据是放在电脑端的。所以只有在手机上扫描成功指纹后，才能够发送密钥到电脑端，电脑端才能解密账户信息，解密后才能利用这些信息登录。

最后，如果卸载手机端或者在手机执行了添加新指纹等安全性更改，密钥就会永久失效，电脑端上储存的账户将永远丢失，只能重新添加。电脑端只是负责储存数据与转发数据到 Windows 本身的登录模块，不会自行解锁账户，数据也只在本地进行通信，不会上传到任何互联网上的位置。

更多解释可以参考作者自己做的一份详实的 Q & A：[文档地址](https://docs.google.com/document/d/1ZheUUDFRdiS81ufpSFyw7y7uzMwiPOOyrfenzFDsRGg/edit#heading=h.ztbsrkyk97)

不足之处与未来计划
---------

虽然应用本身十分快捷好用，安全性也非常可靠，但我在使用中还是发现了几个不足的地方。

首先是应用不能在主页面切换多设备解锁，想要切换设备必须在侧栏菜单中选择「My Accounts」，然后点击想要切换的设备和账户，需要登录多台设备是比较麻烦，临时的解决方法是设置多个桌面小部件。

然后是添加账户时，用户可能会发现登录不成功。因为有时候密码是 Pin，有时候密码是微软账户的密码，需要试两次。

作者本身也知道这些缺点并在不断地完善，未来还会添加 Linux 的远程解锁支持、远程锁定电脑、唤醒通知、定时解锁等功能。

总结
--

有了 Remote Fingerprint Unlock，我可以轻松地在早上起床时唤醒解锁电脑查看当日的日程。接着在到达公司楼下的时候唤醒解锁办公室的电脑，走到办公室就可以直接进入工作状态，解锁效率比 Windows Hello 更高。更好的是可以不用购买昂贵的硬件和适应别扭的识别位置，拿起手机就能统一管理身边所有的 Windows 电脑设备。

---

[🌐 原始链接](https://sspai.com/post/54746)

[📎 在印象笔记中打开](evernote:///view/207087/s1/57103485-db28-41db-8096-9f851ee2ae34/57103485-db28-41db-8096-9f851ee2ae34/)