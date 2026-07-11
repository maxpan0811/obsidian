# ¥229 的苹果新品「蓝牙追踪器」AirTag 值不值得买？我想说说……

---

速读摘要

也是业界通用的方法就是低功耗蓝牙信标。这样我们就能在中距离内，也就是蓝牙信号可以传播的范围内，确定物件到底在不在了。一旦它发生了移动就会发出提示声来提醒附近的人，你一样可以使用支持NFC的手机去查看这个AirTag有没有启用「丢失模式」。会根据这个标识符确定相应的AirTag是不是随您移动的那个AirTag，这时需要你大范围走动来查看「发现正在跟随您移动的AirTag」提醒还会不会触发。

原文约 3008  字  | 图片 18 张 | 建议阅读 7 分钟 | [评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2021-05-07&nu=c5e4ec62-e9de-448a-96f5-63c4884a93d9&fr=myyxbj&ud=328ef&v=2&sig=67696803C797ECF036D4C19C96FD3B53)

¥229 的苹果新品「蓝牙追踪器」AirTag 值不值得买？我想说说……
------------------------------------

原创 广陵止息 少数派

2021 苹果春季发布会上，「跳票」多次的 AirTag 正式登场，加上其他设备都将于 5 月中下旬正式的发售，这使得这个专门「用来找东西」的 AirTag 在这个长假期间显得话题颇多。因此我们拿到后趁着假期体验了一下，整理出几个大家最关心的问题，给还在考虑要不要买 AirTag 的读者提供一个参考。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/41EC4343-2CE4-4CF7-BFC5-C51D57B602CC.png)

**▍****AirTag 究竟是怎么工作的**
------------------------

AirTag 本身不带有 GPS 和移动数据，且只依赖于纽扣电池供电。那么它是如何把自身的位置信息传递给手机的？

最简单，也是业界通用的方法就是低功耗蓝牙信标。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/5DA1D500-4DDE-4487-BF82-53EECC26061A.jpg)

蓝牙信标可以简单感知位置

当我们把蓝牙信标放在一个位置以后，这个蓝牙信标会向周围进行连续性广播，周围的设备接收到这个信号以后就可以确认大致的距离和方向。这样我们就能在中距离内，也就是蓝牙信号可以传播的范围内，确定物件到底在不在了。我这里猜测下苹果在 AirTags 上使用的是自家的 iBeacon 蓝牙信标技术。

依靠蓝牙信号只能得到一个大概的位置，但想要精准定位则需要新型的无线通信技术，也就是 AirTag 上使用到的超宽带（Ultra Wide-Band，UWB）技术。UWB 技术本身实现也非常简单，无线电信号可以先从 iPhone 上发出，这些信号会被 AirTag 所接受，接下来 AirTag 将在一小段事件后再次发送相同的无限电信号，这些信号再会被 iPhone 接收到。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/A6A69302-3CA4-4F8E-A9A9-BF2276BF1EA0.jpg)

计算信号到达时间

这时，iPhone 可以通过发生和接收到信号之间所需要的时间，计算信号到达时间，从而估算 iPhone 到 AirTag 所需要的距离；再通过计算信号到达的角度估算 AirTag 的所在的大概范围。这样我们就能相比蓝牙信标获得更精确的位置和方向了。

既然近距离查找和中距离定位的问题都解决了，那么远距离定位怎么办？苹果给出的方案是 Find My 众包网络。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/BEEB3F25-C943-435C-8429-0171F2E28224.jpg)

Find My 众包网络

Find My 众包网络是由数亿台苹果设备组成的网络，它通过蓝牙进行数据交换，来检测附近有没有丢失的设备或物品；如果别人的苹果设备发现了附近有被主人标记为丢失的物件，则会把当前的大概位置上报给物件主人，物件附近经过的人越多，基于蓝牙的大致位置也就会更准确。整个过程经过加密，无需担心隐私问题。

我相信这里可能有人会担心耗电的问题，事实上发送和接受蓝牙信标所耗费的电量都很低，不用担心使用 AirTag 或者帮助别人找设备导致设备异常耗电。

**▍****AirTag 实际使用起来怎么样**
-------------------------

### **配对 AirTag**

AirTag 配对依然贯彻着类似 AirPods 的体验，拨开外 AirTag 包装以后，最近的 iPhone 上会弹出配对提示，经过确认、命名和注册这三个简单的步骤，你将能听到 AirTag 发出的提示音，同时你也能在 Find My 里看到这个 AirTag 了。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/AE2911A7-4B85-48B9-B02B-9211FDAE88B0.png)

配对 AirTag 的过程

### **精确查找 AirTag**

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/AB1DE047-82F7-485A-969C-2E2552301F43.png)

精准查找 AirTag

精确查找 AirTag 的功能需要配备超宽带技术的 iPhone，通过它我们可以在 AirTag 的蓝牙信标范围内，找到一条前往相应物品所在位置的路线。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/4478CA61-02FD-4FD1-BEDD-6E00A22EC199.png)

简单直观的查找

看起来 UWB 使用的体验极佳，但是受限于 AirTag 的体积和允许发射的功率，UWB 信号实际上很容易到阻隔的，一个简单的包或者家中的墙就能很容易阻隔掉 UWB 信号。这时你想要找到这个 AirTag ，只能先前往它的蓝牙范围内，再只能在它可能的地方进行走动，最后让 iPhone 对走动过程中接收到 UWB 的信号进行处理，来触发路线查找。在大部分的测试过程中 UWB 只有 10m 的有效范围，而蓝牙信标范围则至少有 72m，所以 AirTag 宣传的是找东西而不是防偷盗。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/A267E908-F6D4-4B3B-A704-61E43A1ED74D.png)

哪怕在家里也很容易触发弱信号

### **丢失 AirTag 以后**

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/7DC18D23-09C1-4A7D-AD8E-928068DA7CA2.png)

启用丢失模式

我试着把我的包丢在朋友店里一晚上以后，在手机上打开了 AirTag「丢失模式」，这个过程需要输入电话号码和信息。当朋友抵达它的店里等待一段时间以后，我会能收到一条消息提示并会在地图上显示一个蓝色的范围，提示我可以前往这个圈里找这个 AirTag。我依然是那么认为的，知道 AirTag 的大概位置以后，你还需要回想你去过这个范围里的哪些位置，再在附近使用 UWB 查找，也就是防丢但不一定防盗。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/1B8DE017-1C28-43CF-B283-3B30E590E010.jpg)

扫描 AirTag

打开「丢失模式」以后，其他人可以通过支持 NFC 的 Android 和 iPhone 来扫描这个 AirTag，通过获取上面输入的联系信息，帮助这个 AirTag 的主人找到这个丢失的物件。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/64F8E9C0-C399-419D-961D-C8F662536D68.png)

扫描打开「丢失模式」得到的结果

**▍****AirTag 与隐私**
-------------------

AirTag 能被用来跟踪物件，很多人会担心隐私问题：「查找网络会暴露个人信息和位置吗」以及 「AirTag 会被拿来跟踪人吗」

「查找」网络不会暴露个人信息和位置。「查找」网络查找任何设备和 AirTags 的时候，所有人的信息都会被端到端加密，没有人（包括 Apple）会知道协助定位丢失的设备或 AirTags 的用户或具体设备的具体位置和身份。

那么「AirTag 会被拿来跟踪人吗？」，会但是会有提示。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/433AD988-FC51-4089-8E3C-CB47DB7ABF67.png)

有 AirTag 始终跟随你触发的安全提示

首先是「发现正在跟随您移动的 AirTag」提醒，只要是其他人的 AirTag 和配对者分开，且这个 AirTag 正在随你四处移动你就会收到这个提醒。你可以让这个 AirTag 发出声音，帮助你找到这个跟踪你的 AirTag。这个 AirTag 可能是：

* 附在你借用的物品上
* 其他人不小心丢失的物品
* 用来跟踪你的

如果这个 AirTag 是来自于你借用的物品上的话，你可以选择「暂停安全警告」一天；如果这个物品上的 AirTag 绑定的是家庭组成员的 Apple ID，那么你不仅可以既可以关闭一天还可以选择永久关闭。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/4AB19E11-3A7C-4530-8767-2838C9520873.png)

这个 AirTag 跟随你的轨迹和可以做的操作

如果是别人不小心丢失的物品，那么可以通过支持 NFC 的 Android 和 iPhone 来扫描这个 AirTag，来确认失主有没有启用「丢失模式」。另外别人的物品如果和注册者离开了一段时间（官方表示最长 3 天），一旦它发生了移动就会发出提示声来提醒附近的人，你一样可以使用支持 NFC 的手机去查看这个 AirTag 有没有启用「丢失模式」。

如果你确定一个 AirTag 既不是借来物品上附带的，也不是别人遗失的，那么你可以随时停用这个 AirTag。点击「停用 AirTag 的说明」，然后按照屏幕上的步骤进行操作即可。需要注意的是，如果 AirTag 整夜都在你身边，它的标识符可能会发生更改，而 iPhone 会根据这个标识符确定相应的 AirTag 是不是随您移动的那个 AirTag，这时需要你大范围走动来查看「发现正在跟随您移动的 AirTag」提醒还会不会触发。

实测过程中，我需要带着朋友的 AirTag 走上两个小时就会触发这个提示。但是，如果不是 iPhone 用户的话甚至要最长等待 3 天，让 AirTag 自己发出声音才会意识到自己被跟踪了。也就是说跟踪非 iPhone 用户还是可能会发生的。

**▍****AirTag 能不能不购买挂绳**
------------------------

能，但是只能放在各种包里。

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/C0B44FCC-846B-456C-B16B-C79D9E2511C4.jpg)

AirTag 和一元硬币的体积

AirTag 本身体积并不大，和一元硬币比也就是大了两圈而已；而且本身也没有任何的粘胶，所以从其他物件上脱落的概率还是很大的。如果你不想购买挂绳的话，为了稳妥起见，我的建议 AirTag 还是只能放在包里使用。

不使用挂绳还会大大减少 AirTag 的使用场景，毕竟钥匙、雨伞、耳机或是自行车等等更常用的场景，想把 AirTag 挂上去还是用挂绳最方便也最靠谱。

另外如果你的行李箱是金属的，AirTag 放在行李箱里的时候，iPhone 将不能收到 AirTag 的 UWB 信号；虽然 UWB 信号可以穿透塑料行李箱，当我尝试把塑料行李箱塞满以后，这时 iPhone 接收到的 UWB 信号也已经微乎其微了。因此 AirTag 想跟踪行李箱也需要搭配专门的行李牌。

最后需要注意的是 AirTag 的材质也很容易被钥匙之类的尖锐物品划花，不过买了这个东西总还是要用的，也就很难避免磕碰导致的划痕。

**▍****AirTag 的续航**
-------------------

AirTag 的官方说法是可以在「每天播放四次声音并进行一次精确查找」的情况下可以使用一年多，在你的 AirTag 电池低电量时，iPhone 上也会收到相应的提示。

AitTag 使用的是 CR2032 纽扣电池，你可以在大部分地区买到。更换电池的方式也很简单：

1. 向下按压并逆时针转动 AirTag 的抛光不锈钢电池护盖，直到护盖停止转动，取出旧电池
2. 装回新电池，确保正极朝上
3. 装回护盖，确保护盖上的三个卡扣与 AirTag 上的三个插槽对齐
4. 顺时针转动护盖，直到它停止转动

**▍****AirTag 的其他一些细节**
-----------------------

这些 AirTag 的细节你也需要注意：

* AirTag 防水防尘等级是 IP67，只要不是浸没在水中不用担心出现问题
* 每个 Apple ID 目前最多只能绑定 16 个 AirTag
* 旅行的时候需要注意 AirTag 是不是真的能发挥全部作用，比如在韩国你就无法使用「查找」网络
* AirTag 不能用于跟踪活物，主要是 UWB 信号范围较小且易受环境影响，蓝牙信标定位也够不及时

以上就是本文的全部内容了，希望可以帮助到你了解 AirTag 的工作原理、理清自己的需求并下定决心购买 AirTag。

题图来自 Unsplash：@jonaselia

**更多热门文章**

[![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/00044B1E-3A4F-48B7-B6E4-B58EAA3B18C8.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247514832&idx=1&sn=23a5690a2e5866f339ba977289283dbe&chksm=fdb34fbacac4c6ac4fd7ef87d972d572ee38097c741fa6cb8a9d000cb616ab4081a0fec39369&scene=21#wechat_redirect)

[![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/E2B8B198-C94E-4830-8D95-0EC314E98A02.png)](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247514763&idx=1&sn=21c77057453bbc54dcf9c816c2e0f23c&chksm=fdb34fe1cac4c6f7d694b835a2f3857f54735a25a973f18934977914ceb17c546d8cdfd19079&scene=21#wechat_redirect)

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/658A4ED3-725A-49BC-A7E0-86ED40C813A2.png)

![](.evernote-content/FE5BD87C-C26C-4F80-A813-59068B7EFC37/78CE0A7F-0E31-4086-9B05-D821BEC00CF4.gif)

[阅读原文](https://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247515008&idx=1&sn=04ebfaa0d9feb31c71ab5892b8cf5b89&chksm=fdb34eeacac4c7fcf29f6d00399a2ef783b0ff16d94e1c930084d5bd58507b8f7eed7e5915bf&mpshare=1&scene=24&srcid=0507jeJQcSGvUrYwc3lDcGOA&sharer_sharetime=1620376996245&sharer_shareid=196a7290cec677abfe41ca4bbe251b79##)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzU4Mjg3MDAyMQ==&mid=2247515008&idx=1&sn=04ebfaa0d9feb31c71ab5892b8cf5b89&chksm=fdb34eeacac4c7fcf29f6d00399a2ef783b0ff16d94e1c930084d5bd58507b8f7eed7e5915bf&mpshare=1&scene=24&srcid=0507jeJQcSGvUrYwc3lDcGOA&sharer_sharetime=1620376996245&sharer_shareid=196a7290cec677abfe41ca4bbe251b79#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/09b57c76-8e60-424b-a255-8cf50a61fc02/09b57c76-8e60-424b-a255-8cf50a61fc02/)