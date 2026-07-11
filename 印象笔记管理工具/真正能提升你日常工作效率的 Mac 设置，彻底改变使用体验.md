# 真正能提升你日常工作效率的 Mac 设置，彻底改变使用体验

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0MzU5NzQ4Mw==&mid=224749...](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247495359&idx=1&sn=fbd4f7c1376bd2b3cff663bf27012f39&chksm=c25edecf70033db848830f9df7cb8274d288535511457d9a1c51bf28fc5a0ad386844c331ae4&scene=90&xtrack=1&req_id=1764161760000387&sessionid=1764161763&subscene=93&clicktime=1764161773&enterid=1764161773&flutter_pos=3&biz_enter_id=4&ranksessionid=1764161759&jumppath=20020_1764161608268,1104_1764161758525,1001_1764161759713,1104_1764161763779&jumppathdepth=4&ascene=56&devicetype=iOS26.1&version=1800412f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQklQ9y9GEmqr4lCpjDIMmyxLAAQIE97dBBAEAAAAAAGD+FbhG9YYAAAAOpnltbLcz9gKNyK89dVj0G+NqOGaIXWmSEdCLunQ7beBmlRO8gQRqWZKQJ32DbzMn/tx8tEiKdR+rVMh8RB/7SiN4YXQnB7Kqao+y5tfsNrkc+j41wUM8kDexvjkENPM93kF46njEFQHGiRQSP8ht6lBcL1ud6c+fImXI3sABeTEr5CBFV3f8rIWSlW6QZZox9+VouY1VzWDdv4Q6WMDCU+OSwtvamQrTaQ==&pass_ticket=Fe1pnBUyJPNaS2HaiZK29+osYlImpdlsG9lcQlJIk/tUxll5nUgKXNsIym50nbCb&wx_header=3)

Original 点蓝色字关注👉 程序员echo

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/72930C5E-602F-42BE-9C45-1AB3125E6BDA.gif)

说到 Mac 的设置，我第一年用 MacBook 的时候，总觉得别人都知道我不知道的秘密，好像他们都参加过一个叫“如何让你的 Mac 不烂”的培训班，而我当时还在喝咖啡。后来才发现，我其实有点对，真的有一些设置能彻底改变你的使用体验，只是大部分人根本懒得去碰它们，因为这些设置不是藏在三层菜单深处，就是需要打开终端敲几行看起来像在黑 Pentagon 的命令。

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/80A1A338-AEE0-462C-A7B6-4445C70B7A5D.jpg)

所以我整理了一些真正让我的 Mac 使用感提升的设置，不是什么换壁纸这种花里胡哨的操作，而是那种每天用起来会觉得快、顺手、不像在和电脑斗气的调整。

一、超级增强 Quick Actions（你不知道的右键菜单隐藏技能）
-----------------------------------

Quick Actions 本质上就是 Automator 的工作流，藏在右键菜单里，大多数人忽略它是因为默认选项太无聊，但只要你自己加几个操作，就像给自己加了超能力

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/1FD8842B-FBE4-48BA-B8AD-9C371F1EC1D4.png)

怎么创建呢：打开 Automator（应用程序里有），选择 Quick Action，然后按照自己的需求建工作流

举个例子，我经常写东西，截图多得跟海一样，每张截图都大得可怕，这个 Quick Action 就能让我右键任意图片（或一堆图片）就能统一缩放到我想要的尺寸

在 Automator 里操作步骤如下：

* 先选择文档类型 “Quick Action”，然后点 “Choose”
* 设置“Workflow receives current”为 Image Files
* 添加动作：选中 Copy Finder Items，拖到工作区（注意，如果想保留原文件，不要勾“Replace existing files”）
* 再添加动作：Scale Images，设置你想要的宽度，比如 480px 或 800px
* 按 Cmd + S 保存工作流，比如命名为 “Image Resize”
* 现在，去文件夹里选中图片，右键 -> Quick Actions -> Image Resize 就搞定
* 图片会按 Copy Finder Items 里的目标路径输出，比如我选的图片在 Downloads 文件夹，缩放后的会到 Desktop

Quick Actions 功能太多了，我打算专门写一篇帖子聊 Automator 和 Quick Action 的高级玩法，比如批量重命名、自动加水印、文本处理等等，用起来你会怀疑自己以前为什么要手动做这些操作

二、Finder 高手操作
-------------

Finder 本身用起来还行，但稍微调一调，就能从“凑合用”变成“真好用”

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/B5DDD01D-FFD9-4619-A3CD-CDD928A2AE5B.png)

* 加入 “Recents” 到侧边栏：Finder → 设置（Cmd + ,）→ 侧边栏，把 “Recents” 勾上，这样就能一键看到最近打开的文件，不用再翻文件夹找昨天存的东西
* 文件剪切粘贴（终于）：你可能一直用 Cmd + C 复制文件，再 Cmd + V 粘贴，但其实也能剪切文件，就像 Windows 一样，Cmd + C 复制，然后 Cmd + Option + V 就能移动到新位置，原位置文件就消失
* 显示完整路径：Finder → 视图 → 显示路径栏，现在每个 Finder 窗口底下都有完整路径，可以直接点路径里的文件夹跳转，超级方便

三、 Safari 阅读模式（因为现在的网站都太烦了）
---------------------------

不知从什么时候起，网站全都爱弹窗、自动播放视频、新闻订阅铺满半屏，让你连第二段都没看到就烦死了

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/9F656154-7225-47C6-96A5-59A4CC99858F.png)

Safari 的 Reader Mode 能把这些全部去掉，只留文章内容，清爽到像给眼睛戴了降噪耳机

问题是，每次都要手动点击地址栏 Reader 图标，第三篇文章就烦了 解决办法：让支持的网页自动打开阅读模式，同时可以设置不想自动开启的网页 Safari → 设置（Cmd + ,）→ 网站 → 阅读模式 → 打开“访问其他网站时启用” 这样，每篇文章都会自动干净显示，需要看完整页面随时点图标切换

四是触控板缩放（眼睛看不清时的救星）
------------------

有时候字体、图片太小，眯着眼看累得要命，其实可以用触控板手势随时放大

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/0BD05A76-D782-4537-8AB0-21BEED410DCF.png)

系统设置 → 辅助功能 → 缩放 → 开启“使用触控板手势缩放”，然后三指双击就能放大，再三指双击拖动就能动态缩放，几乎任何地方都能用，网页、PDF、图片，眼睛舒服多了

五是 **热角（不再误触）**热角非常好用，想触发 Mission Control 或锁屏，只要把鼠标甩到角落就行，但如果你跟我一样，一天中被误触十几次，就会抓狂 技巧：加修饰键，比如 Command、Option、Control 或 Shift，设置角落动作时按住键再触发，就不会误操作

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/8892D223-D21E-42D3-81FF-5E365DE19A59.png)

系统设置 → 桌面与 Dock → 热角快捷方式，这样只有你刻意触发时才会生效

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/A23F132D-83C7-4273-9B10-AC374814DD68.png)

六是夜间模式（为什么晚上眼睛像被沙子刮过）
---------------------

MacBook 晚上发出的蓝光让你大脑以为是中午，夜深人静时看屏幕像被审讯 夜间模式能自动把屏幕调成暖色，从日落到日出渐渐变暖

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/389FCA4F-4105-4772-B9EA-2C1AA93AD96E.png)

系统设置 → 显示器 → 夜间模式 → 日落到日出 当然你也可以用 f.lux，这个免费 App 可调节全天不同时间的色温，还能精细设置渐变速度和作息表

七是关闭后台应用刷新（电池更耐用）
-----------------

Mac 会悄悄刷新后台应用，很多你已经好久没打开的 App 都在偷偷消耗电量 系统设置 → 通用 → 后台应用刷新，把不常用的关闭，你的电池寿命会明显提升 iPhone、iPad 也可以同样操作

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/288504D6-4D16-4D54-B33B-4AA4FA4AF267.png)

八是审查开机启动项（开机快 30 秒）
-------------------

很多应用安装时会问是否开机自启，我当时全部同意，现在开机 60 秒都是 Spotify、1Password、Notes 等没用的软件在启动 系统设置 → 通用 → 登录项与扩展，滚动列表，把不常用的去掉，开机速度和内存占用都会好很多，我从 12 个登录项砍到 4 个，MacBook 开机大概 15 秒就好了

九是关闭 Dock 动画
------------

点击 Dock 时那种弹跳动画，看起来慢得像在干等，看着就烦 终端输入命令就能关掉：

```
关闭: defaults write com.apple.dock launchanim -bool false; killall Dock    
开启: defaults write com.apple.dock launchanim -bool true; killall Dock
```

如果你用 Raycast 或 Alfred，可以做成快捷命令，每月改一次也方便

十是减少系统动画（让 Mac 更灵敏）
-------------------

动画很漂亮，但慢 系统设置 → 辅助功能 → 显示 → 减少动画，能让窗口打开、Mission Control 响应更快，操作起来立刻觉得顺手

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/D4D99722-C72F-4F49-B00D-A57B21F224F4.jpg)

说实话，这些调整都不是什么黑科技，也不会让你的 Mac 一夜变超级计算机，但每天用起来，你会明显感觉顺手、舒服 Dock 不再卡顿、电池多坚持几分钟、Finder 变得更聪明、网页更干净 就是这种“从和电脑斗，到和电脑配合”的感觉

好了，我去把 Dock 动画开回去，因为我突然想念它的弹跳了 你有什么 Mac 设置是别人一定要知道的，也分享一下吧，我一直在找新的小技巧来折腾（也就是找灵感）😭又到了告别的时刻，本期的分享到这了，下期我们再见！！！🚀

![](.evernote-content/BBA31292-5868-4B05-A902-A3E73A8EE1C3/D8D0F6F1-F131-422D-8675-7C0EF4010CA9.gif)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247495359&idx=1&sn=fbd4f7c1376bd2b3cff663bf27012f39&chksm=c25edecf70033db848830f9df7cb8274d288535511457d9a1c51bf28fc5a0ad386844c331ae4&scene=90&xtrack=1&req_id=1764161760000387&sessionid=1764161763&subscene=93&clicktime=1764161773&enterid=1764161773&flutter_pos=3&biz_enter_id=4&ranksessionid=1764161759&jumppath=20020_1764161608268,1104_1764161758525,1001_1764161759713,1104_1764161763779&jumppathdepth=4&ascene=56&devicetype=iOS26.1&version=1800412f&nettype=WIFI&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQklQ9y9GEmqr4lCpjDIMmyxLAAQIE97dBBAEAAAAAAGD+FbhG9YYAAAAOpnltbLcz9gKNyK89dVj0G+NqOGaIXWmSEdCLunQ7beBmlRO8gQRqWZKQJ32DbzMn/tx8tEiKdR+rVMh8RB/7SiN4YXQnB7Kqao+y5tfsNrkc+j41wUM8kDexvjkENPM93kF46njEFQHGiRQSP8ht6lBcL1ud6c+fImXI3sABeTEr5CBFV3f8rIWSlW6QZZox9+VouY1VzWDdv4Q6WMDCU+OSwtvamQrTaQ==&pass_ticket=Fe1pnBUyJPNaS2HaiZK29+osYlImpdlsG9lcQlJIk/tUxll5nUgKXNsIym50nbCb&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e07ffd55-21ea-4081-bdc7-87d4083d17f2/e07ffd55-21ea-4081-bdc7-87d4083d17f2/)