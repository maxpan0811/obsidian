# Fantastical for Mac 支持修改被邀请事件的时间 | App 奏折 046

---

Fantastical for Mac 支持修改被邀请事件的时间 | App 奏折 046
=============================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

本周值得关注的应用有： Fantastical for Mac 支持修改被邀请事件的时间、VLC 支持 Chromecast 串流和 360 度视频、Keyboard Maestro 简化了变量相关语法。

Fantastical for Mac 2.5
-----------------------

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/D2B59602-6C90-4711-A07A-DBC70234C5C1.png)

**Fantastical for Mac 2.5（2018-07-18）**

[下载链接](https://itunes.apple.com/cn/app/fantastical-2/id975937182?mt=12&at=10lJSw)

#### **应用简介**

Fantastical 是一款苹果生态下的全功能日历工具，它最大的特点是自然语义识别，可以通过文字输入一次性为日程添加时间、地点等信息。在界面上则相对规矩一些，在提供日 / 周 / 月视图等功能的同时，Fantastical 也保持了近乎原生简洁的界面。

#### **值得注意的变化**

Fantastical for Mac 这次更新出了 3 个值得一提的功能：

1. 使我们可以提议修改被邀请的日历事件的时间。
2. 对贯穿多天的事件进行更合理的显示。
3. 增加了 Calendar Set 的 URL Schemes

### 修改被邀请事件的时间

邀请功能是 iCloud 或 Google 这样的日历服务都支持的一个功能。当一个事件需要多人参与，就可以通过他们关联日历的邮件去邀请他们，当他们接受邀请后，该事件就会显示在他们的日历上。不过，因为被邀请人不是该事件在软件上的发起人，他也就没有权限修改事件时间。

Fantastical 这次的改进就是针对这个问题，让任何一个被邀请人都可以申请修改日历事件的时间：

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/202CC9AB-4FF9-48AD-A55A-B59268C1561C.png)

在 Fantastical 中修改日历事件的时间

当我们提出了建议的时间后，Fantastical 会调用系统的邮件客户端，把该建议通过邮件的形式发送出去，重新邀请参与者。

这个功能现在还没有在 iOS 版上实现，但是上周奏折中推荐的限免日历软件 Week Calendar 支持这个功能。

### 贯穿多日的非全天事件视图改进

在 Fantastical 里，如果是全天事件的话，它以一个小横幅的形式，显示在视图的日期下面；如果是非全天事件的话，它会按时间占用量，在日历上以不同大小的事件块来表示。

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/3C5437F9-C1E8-41F1-BB86-97C532C17B86.png)

Fantastical 的全天事件与非全天事件

因此，一直以来，如果一个事件，虽然贯穿多天，但如果它的开始和结尾都是一个特定的，由时 / 分组成的时间点，那它的时间块就会占据街面上一整条甚至好几条时间线：

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/8C69E75B-FA06-4A3C-B6BD-80C04D3AEFA6.png)

过去的 Fantastical 多日时间视图

但是现在，当我们在 Fantastical 中的「Appearance」中，找到「Show multi-day events in all-day section」, 就可以让这种非全天事件按全天事件来显示了：

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/DDD111C4-0237-40F2-A024-58F8720AC259.png)

Fantastical 设置选项

### Calendar Set 的 URL Schemes

Calendar Set 是 Fantastical 一个很便利的功能，它让拥有多日历的用户可以把不同的日历分为不同的集合。

现在我们可以用 URL Schemes 调用不同的集合，它的语法是：

`x-fantastical://show/set?name=日历集名`

### 其它

以上就是比较值得注意的 Fantastical for Mac 2.5 的更新内容。当然这次不只是这些，Fantastical 还关联了 [meetup.com](https://www.meetup.com/)、把修改日历持续时间的操作改得更加顺手、把 Fantastical 的迷你窗口作为一个全屏界面的 Split View 等等。

更多更新细节，可以去查看 Fantastical 的官方博文。

VLC 3.1.0
---------

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/A1B31E73-E8FB-4A9C-A14D-5D4FA6DC1F5F.png)

**VLC 3.1.0（2018-07-18）**

[下载链接](https://itunes.apple.com/cn/app/vlc-for-mobile/id650377962?mt=8&at=10lJSw)

#### **应用简介**

VLC 是 iOS 上音频 / 视频播放器，格式支持，支持手势操作，

#### **支持 Chromecast，变速不变声**

VLC 等视频播放器有一个玩法叫「串流」，简单说就是在一个设备上播放另一个设备的视频，由于版权和习惯，老外经常这么用。但是国内大家往往还是下载到本地慢慢看，所以 Chromecast 的支持也不多说。

比较让我感兴趣的是声音的稳定性的改进，在变速播放视频时音频失真（变成尖锐的机器人音色）情况变少了。我读书时，身边就有不少人在拿 iPad+VLC 的组合看考研视频，大家都喜欢加速赶时间刷完，但偶尔出现音频失真可就不好受，看着屏幕里德高望重的老教授发出小女孩的声音，非常破坏心情。这次升级，对学生族来说是比较开心的。

此外，360 度视频和 H.265 格式文件的解码能力也有了提升，摄像爱好者可以在 iPad 甚至 iPhone 上直接预览刚拍好的片子。

Keyboard Maestro 8.2.2
----------------------

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/CDB32E9A-4601-490E-BA52-8EA702ABFA35.png)

**Keyboard Maestro 8.2.2（2018-07-13）**

[下载链接](https://www.keyboardmaestro.com/main/)

#### **应用简介**

Keyboard Maestro 是一款 macOS 平台的通用型自动化工具，可以通过快捷键、文本输入、文件变化等触发条件，进行一系列的自动化操作。少数派对 Keyboard Maestro 有过几篇介绍文章：

* [Keyboard Maestro 入门指南](https://sspai.com/post/36442)
* [懒的前提是要足够高效： Mac 效率工具 Keyboard Maestro 详解](https://sspai.com/post/28721)

#### **简化变量语法**

先说一句，根据同步记录显示，我已经 2 个月没怎么折腾 Keyboard Maestro 了，**很大一个原因就是它的界面和语法过于复杂**。既然我懂一点点编程，为何不打开 LaunchBar 的编辑器敲上几行代码呢？

过去，Keyboard Maestro 语法中最让人头疼的，估计就是变量的表示方式。比如下面这个 Workflow 的介绍模板，我把输入的第一段文字设为变量「功能介绍」，接下来想用到「功能介绍」时，居然要用 `%Variable%功能介绍%` 来调用，前面那半截实在是累赘。所幸，以后直接用两个百分号包住变量名就能调用了，比如这样：`%功能介绍%`。

![](.evernote-content/6AADB387-02A4-41E3-92D4-CA08D6F9848E/A62D6EC3-7DDA-4080-8626-0220015B3785.png)

变量语法前后对比

8.2.2 版本以后的 Keyboard Maestro 兼容旧语法，你不改老 Macro 里的变量名也能正常使用。这次更新还提供了代码语法高亮，总体来说都让编辑 Macro 变得更舒服了。

对了，如果你 Keyboard Maestro 和我一样总是发出「嘟嘟」的错误提示音，升级到最新版也许可以解决问题。

---

[🌐 原始链接](https://sspai.com/post/45767)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9fd2425e-ec61-44a8-99c7-35668bc9eca8/9fd2425e-ec61-44a8-99c7-35668bc9eca8/)