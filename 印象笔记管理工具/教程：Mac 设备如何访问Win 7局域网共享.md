# 教程：Mac 设备如何访问Win 7局域网共享

---

教程：Mac 设备如何访问Win 7局域网共享
=======================

[![](.evernote-content/D9F692FD-E8B9-48F7-ABDA-5BA0828060A0/6B692123-ED80-4794-9C1A-263A725E8D87.gif)](http://fullrss.net/r/http/bbs.feng.com/u.php?uid=798198)

投稿by：[叫我知心哥哥丶](http://fullrss.net/r/http/bbs.feng.com/u.php?uid=798198) 来源：威锋网

PostTime：2015-07-12 21:33:16

[收藏](http://fullrss.net/r/javascript/www.feng.com/apple/MAC/2015-07-12/void(0)) [已收藏](http://fullrss.net/r/http/bbs.feng.com/home.php?mod=space&do=favorite&type=news)

微博

[![](.evernote-content/D9F692FD-E8B9-48F7-ABDA-5BA0828060A0/9FD25F7E-8C83-453B-B143-132D2B804BF2.jpg)](http://fullrss.net/r/http/weibo.com/weiphone?zwm=tech)

微信![](.evernote-content/D9F692FD-E8B9-48F7-ABDA-5BA0828060A0/558C1F85-D9FA-4C98-A0F8-5DE01457FBAB.png)*扫一扫加威锋官方微信号***微信号：weiphone\_2007** [加载中...](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml#comment)

[Twitter](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml#twitter) [Share](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml#Share) [Email](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml#Email) [Save](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml#Save) [Print](http://fullrss.net/r/http/www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml#Print)

> 如果这个教程都解决不了，直接上 U 盘吧。

[![](.evernote-content/D9F692FD-E8B9-48F7-ABDA-5BA0828060A0/1820F6E9-DDA6-4691-8356-8F5553141DFC.jpg)](http://fullrss.net/r/http/bbs.feng.com/aodoo3/click.php?n=a6444c89&zoneid=128)

以下为文章全文：

![](.evernote-content/D9F692FD-E8B9-48F7-ABDA-5BA0828060A0/CB151900-2775-4517-B574-6584B2C14E3A.jpg)

  
　　由于 Mac 设备的 OS X 系统跟普通 PC 设备所运行的 Windows 之间存在差异，因此涉及到这两种设备的互通使用问题的时候，通常不像两台运行同样系统的设备那么容易实现，比如 Mac 设备访问 Windows 7 系统的局域网共享，当然，并非不能成功访问。  
  
　　就在昨天，锋友 macliang 在威锋论坛内分享了 Mac 设备访问 Windows 7 系统的局域网共享的方法，只需简单的几个步骤就能让 Mac 设备成功访问共享，一起来看看具体如何操作吧。  
  
　　1. 首先，Mac 设备访问 Windows 7 系统局域网共享的先决条件是，Mac 设备和运行 Windows 7 的 PC 处于同一个局域网中，并在 Windows 7 系统里设置成 guest 用户可以远程访问。需要注意的是，绝大部分使用快速装机工具安装的 Windows 7 系统都会将这一选项关闭，我们要做的就是将它开启。  
  
　　2. 记住 PC 的电脑名称和组用户名(在“我的电脑”上点击右键，就能在属性中查看组用户名，默认是 WORKGROUP)。完成这一步之后，我们可以使用同一局域网内的其他 PC 尝试一下能否访问目标 PC 的局域网共享。  
  
　　3. 设置好需要共享的文件夹及其访问权限，注意，这里一定要给 guest 用户权限。到这一步，PC端的设置已经完成，接下来是 Mac 设备。  
  
　　4. 在 Mac 设备上进入设置 > 网络 > 高级 > WINS, 设置好 Mac 的电脑名称和工作组名称，工作组的名称一定要和 PC 端的一样，否则将无法最终访问 PC 端的局域网共享。  
  
　　5. 返回设置之后，网络 > 共享 > 选项，勾选“使用 SMB 来共享文件和文件夹”。  
  
　　6. 进入 Mac 设备的 finder(finder 的功能类似 Windows 资源管理器)，在菜单中选择前往 > 连接服务器，输入服务器地址如下：  
  
　　<smb://PC> 电脑名，或者是 <smb://PC> 的 IP 地址  
  
　　如果出现输入用户名的要求，可以选择来宾用户，如果 Windows 7 系统上并未设置 guest 用户可以远程访问，则无法成功访问。  
  
　　对于上述操作步骤，锋友 macliang 还根据自己遇到的状况给出了几点建议：  
  
　　- PC 端的共享设置非常麻烦，锋友们可以下载一个 Windows 7 系统的局域网设置工具，互联网上一搜就有。  
  
　　- 如果无法成功完成第一步和第二步，可以考虑在 Windows 7 系统中建立一个新账户，记住用户名和密码即可。当然，在进行文件夹共享的时候要注意给这个新建账户打开权限。

---

[🌐 原始链接](http://www.feng.com/apple/MAC/2015-07-12/Tutorial-how-to-access-the-Mac-equipment-Win-7-LAN-Shared_618528.shtml)

[📎 在印象笔记中打开](evernote:///view/207087/s1/082e171a-4288-47ba-818b-0a579bd2da69/082e171a-4288-47ba-818b-0a579bd2da69/)