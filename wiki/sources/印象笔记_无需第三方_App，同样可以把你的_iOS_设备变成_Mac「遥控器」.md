---
title: "无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」.md
tags: [印象笔记]
---

# 无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」

# 无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」 --- ![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F

---

# 无需第三方 App，同样可以把你的 iOS 设备变成 Mac「遥控器」

---

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/5DA50858-EB10-4846-8875-C899A74C01F4.jpg)

一个月前 [JailbreakHum](http://matrix.sspai.com/user/681230) 同学写了一篇[《把你的 iOS 设备变成控制 Mac 的「遥控器」》](http://sspai.com/35242)。碰巧我当时也想要写一篇类似的文章，当这标题映入眼帘，我心里便是咯噔一下，脑海里闪过 N 个加粗大字：「该死，我想写的东西居然被抢先了！」。

不过，仔细一读，发现虽然晚了一步，但自己的方法还是有可取之处的，简单来讲，我的方法和 JailbreakHum 那篇文章实现的效果相同，都利用了 AppleScript，但是我不需要用 Hazel，事实上无需任何第三方应用，就可以实现通过 iPhone 来控制 Mac。

原理
--

想要遥控 Mac，关键就在于 Mac 上要有一个能根据手机上的指令自动触发 AppleScript 的后台程序。但是，我们有没有必要为了遥控 Mac 特意买一些应用（比如 Hazel），然后单纯为了遥控 Mac 就让这些应用常驻后台，这是对金钱和内存的双重浪费。

所以在我看来，这个用来触发 AppleScript 的扳机应该满足两个条件：

1. 这是一个我们本来就一直放在后台的应用；
2. 这个应用最好免费。

好消息是，确实有两个应用完全符合要求，它们就是 Message 和 Mail 两个原生应用。大多数人都不知道 Message 和 Mail 都自带了自动运行 AppleScript 功能，下面请让我一一介绍。

通过 Message 操控 Mac
-----------------

Message 启用自动触发 AppleScript 的方法是在应用偏好设置中打开 「通用 - AppleScript 处理程序」菜单，从中选择我们想要运行的 AppleScript。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/10411FB3-268A-4E3F-95F4-A2B19DC0B82F.jpg)

令人意外的是，苹果已经为我们准备好了几个十分有用的 AppleScript，例如用来遥控 iTunes 的 iTunes Remote Control。而这些用来运行的 AppleScript 就储存在 `/Users/用户名/Library/Application Scripts/com.apple.iChat/` 中。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/164341D5-BB9E-4108-B133-4A2C7641DE21.jpg)

点开这些 AppleScript 文件，在文件最开头的是苹果的免责声明，后面就是脚本代码了，代码的注解非常详细，即使不熟悉 AppleScript 的人也能大概看懂（学习 AppleScript 的好教材）。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/1B88779B-AFCB-41C1-B930-5FBF8B4CCC71.jpg)

这里以选择 iTunes Remote Control 为例。先让我们来看一下这个 AppleScript 的效果。

首先，确保我们 Mac 上所使用的 iMessage 帐号与我们手机上的帐号不同（你可以先试一试如果账号一样会发生什么）。

然后，我们只要从 iPhone 上向电脑上的 iMessage 帐号发送 `play`，iTunes 就会被自动打开并播放音乐，不仅如此，你还会收到 iMessage 回复告诉现在正在播放的是什么。除了 play 以外，其它指令还包括：

* `pause`: 暂停status: 播放状态
* `next`: 下一首
* `previous`: 上一首
* `mute`: 静音
* `unmute`: 解除静音
* `help`: 显示帮助

但是，这个 AppleScript 有两个小的问题。

1. 我们 Mac 上的 iMessage 帐号与 iPhone 上的一般是一样的，我们不可能为了遥控器的需求，去让 Mac 使用一个不同的账号 ，但请看代码的这里：

```
        on getCurrentiTunesTrack()
                
                set theCurrentTrackMessage to "Not playing."
```

由于反馈信息 （theResponse） 被默认为 「Unknown Command.」，即一旦收的任何没有预先设定过的命令，Apple Script 都会自动回复 「Unknown Command」, 而 「Unknown Command.」 本身也并非定义过的指令！所以当自己给自己发送信息后会发生什么，相信聪明如你应该明白了吧。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/8B50F8FC-3512-420C-B1F3-26CF181E1514.jpg)

2. 万一你的基（姬）友也看到了这篇文章，趁你在开会时给你发了 「unmute」「play」那又该怎么办……？

**所以，我们希望能通过「自己给自己发短信」的形式来激活这个 AppleScript，而且确保只有自己的 iMessage 账号才能遥控 Mac。**

为了解决这些问题，我想先简单介绍一下这个 AppleScript 的代码。代码主要由两部分组成，第一部分类似一个「控制器」（message received），会在收到手机发来的信息时将命令提取出来，之后通知第二部分（runiTunesRemoteControl）用提取出的命令对 Mac 上的 iTunes 进行操作。

操作结束后，第二部分会生成一个反馈信息，并将它发回「控制器」，再由「控制器」将反馈信息发给手机。

可以想象，如果「控制器」能在收到信息时检查一下信息是否来自我们本人，再决定是否通知第二部分进行操作，并且能在发送反馈信息给手机前，确保不会再将 「Unknown Command.」 发回，一切不就解决了吗？

因此我们的改动将集中在「控制器」，也就是这段代码上：

```
        on message received theMessage from theBuddy for theChat
                
                -- 将命令（theMessage）传到第一部分，并将反馈信息存在 theResponse 中
                set theResponse to runiTunesRemoteControl(theMessage)
                
                -- 向手机发送 theResponse    
                send theResponse to theChat
                
        end message received
```

改动后：

```
        on message received theMessage from theBuddy for theChat
                set serviceBuddy to name of service of theBuddy
                -- 检查发送者是否是我自己
                if serviceBuddy = myiMessageAccount then
                        
                        set theResponse to runiTunesRemoteControl(theMessage)
                        -- 确保反馈不是 「Unknown Command.」
                        if theResponse ≠ "Unknown command." then
                                send theResponse to theChat
                        end if
                        
                end if
                
        end message received
```

这样一来，问题就算是解决了，当然你也可以在此基础上加上其他你想要的功能，例如关闭屏幕等。这些改动需要在代码的第二部分中完成，只需要在多加几个 「if」 条件语句即可。

如果你有一定编程基础的话，这个脚本还可以变得更加强大，它可以把手机上发来的信息直接输入 Mac 的 Termial，这样一来我们手机上的 Message 应用可以变成一个类似 shell 的存在，可以动态执行手机上传来的命令。

也就是说，我们的手机可以遥控 Mac 干任何事情，如果有读者有兴趣，我会在更新时贴上实现方法。

通过 Mail 操控 Mac
--------------

相较于使用 Message， Mail 的好处在于可以设定不同规则触发不同的 AppleScript，这样我们就没有必要把所有 AppleScript 写在一个文件里或是写一个需要调度其他 AppleScript 的 AppleScript。

除此以外，还有一个好处就是如果你是 Android 手机，可能无法使用 iMessage 给自己发信息，但是 Mail 却是完全通用的。

Mail 的设置相较 Message 容易，因为我们可以通过 Mail 直接设定 AppleScript 的触发条件，而不是在 AppleScript 里用代码来判断。这样对于没有编程基础的人来说更为简单。

这里以添加一个能关闭屏幕的 AppleScript 为例。

1. 先创建一条关闭屏幕的 AppleScript，在应用程序中打开「脚本编辑器」，新建一个 AppleScript，命令很简单，只要输入一行 `do shell script "pmset displaysleepnow"` 即可，之后保存。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/A080E132-A463-4224-8E05-7B9870378842.jpg)

2. 打开邮件应用，在偏好设置里点击「规则 － 添加规则」；

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/CA6FD8B5-4FFD-4272-9B15-80AFEF167F92.jpg)

3. 在这里我们就可以设定条件，我们把条件设置为 「主题包含 Turn off the screen」 且 「发件人等于 [XX@XXX.com](mailto:XX@XXX.com)（你的邮箱）」，并在「就执行下列操作」中选择「运行 AppleScript」，然后选择运行我们事先写好的可以关闭屏幕的脚本，在运行完后视情况删除邮件。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/05515605-B1A7-4532-8349-B7BE525158CD.jpg)

与 Launch Center Pro & Workflow 整合
---------------------------------

所谓没有最懒只有更懒，通过 [LCP](http://sspai.com/tag/Launch%20Center%20Pro) 与 [Workflow](http://sspai.com/tag/Workflow)，我们在遥控时就不用重复输入命令了。

首先介绍 Message 版的设置方法：

1. 在 Workflow 里建立动作，在 Text 块中输入命令，这里以 「Pause」 为例，然后添加一个 Send Message 块。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/490BB0CA-1DF7-48AD-AA6B-0243C037E9D5.jpg)

2. 点击右上角的齿轮，选择 「Share Workflow」，在第二行中选择 「Add to Launch Center」 。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/18E00E8E-8E42-4E87-A189-7F3D30BD0772.jpg)

3. 然后在 LCP 中，建立一个 Remote Control 组，把 Workflow 放入即可。

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/0503C115-5802-470B-AAA6-7EE6A15A9980.jpg)

这样一来，我们就能两键暂停 Mac 上的音乐了（因为发送信息还要点一次）。

对于 Mail 版，操作则可以彻底一键化，因为 Workflow 可以在应用内发送邮件。我们可以这样设置 Workflow：

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/C86FE6F5-CEDF-4EE3-8D4E-BA4A67AEE199.jpg)

同样，与 LCP 整合后：

![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/4E79AAD8-71D1-4484-8350-1575D58BEEFF.jpg)

写在最后
----

我原来还想介绍一下如何用 「Command - C」 来遥控，但是因为 macOs Sierra 的新特性——通用剪贴板， 「Command - C」 可以说已经退出了历史的舞台。

同时我也要感谢 JailbreakHum 的文章，结合他的文章，读者们也许可以学到更多。

希望大家能在这篇文章里学到一些有用好玩的技巧。

**参考文章：**

1. [《把你的 iOS 设备变成控制 Mac 的「遥控器」》](http://sspai.com/35242)
2. [AutoForwardIMessageText.applescript](https://github.com/yongjunj/AutoForwardIMessage/blob/master/AutoForwardIMessageText.applescript)
3. [ASLR\_intro](https://developer.apple.com/library/content/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)

文章来源 [少数派](http://sspai.com) ，原作者 [Elyon314](http://sspai.com/author/724398) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/A7C6E9BC-2635-4A6D-8549-205AB4A1ED3F/D188270C-6348-43CD-89E6-26017B428BF8.jpg)](http://click.dji.com/ACLR_BH5xMntFK-4gR0?pm=link&as=0002)

---

[🌐 原始链接](http://sspai.com/35799)

[📎 在印象笔记中打开](evernote:///view/207087/s1/962dfe28-b7e9-433c-8f84-1d38eaa52c1a/962dfe28-b7e9-433c-8f84-1d38eaa52c1a/)