---
title: macOS 内录从工具到实战 _ Matrix 精选 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/macOS 内录从工具到实战 _ Matrix 精选 2.md
tags: [evernote, impression, yinxiang]
---

# macOS 内录从工具到实战 | Matrix 精选

---

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/6553C231-4022-465B-BE57-5E5CAA0E0057.jpg)

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/11C5D3DC-0B86-4690-A948-ECB03E1EBC35.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文内容仅代表作者本人观点，文章对标题和排版略作修改，[原文链接](http://matrix.sspai.com/p/d78026e0)。

内录是指录制电脑自身发出的声音，用于混音、保存或串流的功能。如果你想要做游戏直播，播客直播，或者仅仅是想要录制 FaceTime Audio 的电话录音，都需要使用内录功能。

对于 PC 用户而言，打开音频设置中的「立体声混音」输入设备就可以内录，而且只要音频硬件不是特别旧，一般都不会有什么问题。而对于 Mac 用户来说，macOS 并没有在系统上提供原生的内录方案，使得在 Mac 上做内录变得很复杂。与此同时，第三方开发者也为此做出了很多努力，也让 Mac 用户有机会在内录上玩出更多的花样。因为笔者曾经在 Bilibili 做过一段时间的直播，在这方面积累了一定的经验，将在本文中一并介绍给大家，希望能够对各位有所帮助。

Audio Hijack
------------

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/44CDCAF0-BE0C-41EC-8BA6-27E85B378FA1.jpg)

Audio Hijack 因其在录制播客上的优秀表现为人所知，其本身也是一款强大的内录工具。使用这款工具，你不仅可以将各种声音的来源和去向进行有效的组织，还可以对声音进行初步的处理，甚至可以进行计划任务，自动的完成广播工作。我们来看一个例子：

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/1137483A-8093-4186-910E-90F33FD4CC1C.jpg)首先点击左下角的「New Session」按钮，新建一个录制场景，你可以从零开始，也可以选择一个模版来使用。这里我们选择「Application Audio」作为初始场景。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/F177E82A-F7C1-4ACE-8393-BA7FDC636C08.jpg)

假设我们这里的需求是，录制 Skype 聊天和 iTunes 播放的音乐，把这些内容混音后录制到文件中，并且在我们的耳机里播放出来供监听。（典型的做播客的需求）那就可以在蓝图的左边拖拽增加一个「Application」块，把目标应用设为 Skype，再拖入一个输入设备，将源设置为话筒，最后把最右边的输出设备调整为耳机。（由于 Skype 本身的声音中只包含对方的声音，所以还要加上自己的话筒）结果如下。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/E8E178DB-2B7B-4240-AE48-79D5C338E314.jpg)

我们还可以再要求的丧心病狂一点，我们要让 iTunes 播放的音乐过一遍均衡器，再给我们的聊天加一个回声，最后我们还要看到实时的电平。结果看起来像是这样的。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/6044C2A6-C4FB-4133-B136-78A21943CE44.jpg)

一切的操作都由拖拽来完成，每一个处理块都可以通过点选来进行细节的设置，也可以临时开关一些处理块。

在录制完成后，你就可以在程序的录制结果选项卡中找到录制的音频了。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/F8C747C0-E435-49CA-80EE-CC0857358DAA.jpg)

通过以上的例子，大家应该对 Audio Hijack 的功能有所了解，那么这款软件有没有什么缺点呢？我们可以发现，这款软件的功能主要都体现在录制上，并没有支持把混音后的声音输出给其他应用进行再混音或者是串流的功能。所以，Audio Hijack 仅适用于对内录的内容进行简单混音和录制的需求。

你可以在 [Audio Hijack](https://rogueamoeba.com/audiohijack/)官网下载 Audio Hijack，售价 49 美元，同时有免费版可供下载。

LoopBack
--------

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/FDD13D09-3E05-4B69-84B1-040AF5BFB523.jpg)

LoopBack 这款软件的功能正是 Audio Hijack 缺失的功能（可惜不能和 Audio Hijack 协同工作），它可以将选定软件发出的声音进行简单混合后，以虚拟输入设备的方式提供给其他程序利用。我们来看一个例子：

比如我们要通过 Skype 远程给一群人讲课，课程的材料是一段朗读语音。我们可以在 LoopBack 中新建一个虚拟声卡，在右边的列表中添加我们用来播放朗读音频的 QuickTime 和我们的麦克风。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/B43085C7-B949-4D0D-9104-209B919969F4.jpg)

选中「Monitor audio through」选项，让自己能够用耳机监听自己的声音，以及听到 QuickTime 播放的声音。

接下来在 Skype 的首选项中选中刚才建立的虚拟声卡，经过一番测试和对音量的调整之后，就可以开始上课了。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/E5872178-B628-42DB-9565-D952F7684613.jpg)

和 Audio Hijack 一样，此软件也可以定义多个录音场景。LoopBack 还可以调整输入声音和输出声音在声道上的对应，你可以将某个声音源单独输出在某个声道上，来实现一些特殊需求。总的来说，这款软件比较专注于软件之间的音频互通，可以支持一些很复杂的混音场景。

使用过程中遇到的问题也有很多，比如上面这个例子，在打开「Monitor audio through」选项之后，你可以在耳机中听到自己话筒的回声，这是一个很要命的问题。试想一下你在给别人讲课的时候，耳边一直有自己声音的回声是一种怎样的体验。（这个问题在 Audio Hijack 中就可以通过仅给 QuickTime 加监听块来解决）还有就是其对于 Java 的支持问题，因为 LoopBack 选择音源靠的是选择一个 .app 结尾的程序文件，对 Java 应用程序（比如 Minecraft）无能为力，当我尝试用这款软件直播玩 Minecraft 的时候，意识到了这个问题的严重性。而且，这款软件还有一个重要的缺点：贵！要比 Audio Hijack 贵出 50 刀！

那如果我不需要像「Channel Mapping」这样的高级功能，也不需要同时进行多组内录，有没有办法用 Audio Hijack 实现同样的功能呢？我们来看下面这个工具。

你可以在 [LoopBack](https://rogueamoeba.com/loopback/) 官网下载 LoopBack，售价 99 美元，同时有免费版可供下载。

Soundflower
-----------

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/B235E3EE-4C78-4581-8DE7-29AE5294153D.jpg)

Soundflower 是一款开源软件，已经在 2014 年停止了功能维护，仅由原开发者进行一些新系统的适配工作，但作为一个免费[开源](https://rogueamoeba.com/freebies/soundflower/)的简易内录软件，至今仍不可替代。Soundflower 的功能非常简单，它提供了两个虚拟声卡（2ch 和 64ch），你只需要将你想要提供给其他程序的声音输出到其中一个声卡上，再将另一个程序的声音输入设置为这个声卡，就可以完成简单的音频路由了。我们来看一个例子：

这里我们要用 QuickTime 录制系统发出的全部声音。首先在系统偏好设置中将 Soundflower(2ch) 设置为系统输出设备，这意味着将系统发出的全部声音发送到 Soundflower。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/A0040D03-B278-4B0B-B1AD-FE1D85731D7B.jpg)打开 QuickTime，新建一个音频录制，将输入设备也设为 Soundflower(2ch)。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/2C46DF88-733C-4B7A-A5D5-68579109736F.jpg)之后直接开始录音就可以了。

Soundflower 的默认音量是 50%，如果你需要提高音量适应录制需求的话，可以在系统的 Midi 音频设置中对其进行调整。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/36EA05DF-2BF2-4FFF-ACBB-FA91EE8EDFC7.jpg)

如果你尝试过了的话，应该已经发现其中的问题了，在录音的过程中，你听不见任何声音。这是因为为了新系统的适配，软件取消了自带的控制工具，使其无法设置监听功能，使用起来十分尴尬。在接下来的实战篇，我将会讲解如何将这款软件与 Audio Hijack 结合，创建一个优雅的内录工作流。

四、案例实战

介绍完了常用的内录工具，我们来用一个实际的案例来操作一下。这里的案例就是在 macOS 上做游戏直播。

这里我们使用 OBS 作为我们的直播串流工具。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/225B32D2-8E77-4FA9-8AC4-1FBBB7FE2DEC.jpg)想法是这样的，我们要在直播中包含我们的游戏声音，防止观众觉得无聊加上的 BGM，还有和伙伴的聊天语音。能够把自己的麦克风声音单独做控制，方便处理一些突发状况。还要能够听见上述声音，不能妨碍正常游戏。

于是我们在 Audio Hijack 中设计了一个这样的场景：

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/0F24CA51-F392-4CF6-A5AD-71AC03BD6A75.jpg)

将所有的音源输出到 Soundflower 中供捕获，再全部输出到耳机进行监听。我们将 Soundflower 作为中继，给 Audio Hijack 增加了原来没有的把声音输出到其他程序的功能。

在 OBS 中，我们作这样的设置：

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/B1AD88EE-11BC-442A-8B44-7C3267D671C4.jpg)

将两个音频设备分别设置为 Soundflower 和默认麦克风，从而实现在直播时对话筒的分离控制。

接下来只要一切就绪，就可以开始直播了。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/F08FFE11-9505-427B-AB8B-66DD61AF60A5.jpg)

Soundflower 为 GitHub 开源软件，你可以在 GitHub 中[免费下载](https://github.com/mattingalls/Soundflower)。

一些提示和想法
-------

今天介绍这些工具会在系统中安装虚拟声卡，因为 macOS 并不能有效的判断这些音频设备的使用场景，所以在你取下插在笔记本上的耳机的时候，系统有时会切换到错误的音频设备上。所以如果你在安装这些软件后突然出现了系统不出声，打 Facetime 对面听不见声音的情况，请先检查系统或者软件的音频设置，是否选择了正确的音频输入设备。

本教程中介绍的三款软件，都是 RogueAmoeba 的作品，在这里感谢这些优秀的开发者给我们创造了这些优秀的工具。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/1A6319FC-2187-4CEC-96B4-DC6E9EA4F11B.jpg)

Soundflower 的开发停止几乎是种必然，因为 LoopBack 这一图形化工具的出现，维护这样一款上古时期的软件已经显得没有必要了。但是如果没有这个工具，在 macOS 上直播 Minecraft 几乎是不可能的。为了表达对 Soundflower 开发者的感谢，我曾经为其绘制过一个新的图标，也写邮件给了目前的维护者，可惜至今没有收到回复。

![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/01D4FCDE-23DA-40DC-9B98-41329403A006.jpg)

希望这篇文章能够解决一些大家实际遇到的问题，也欢迎大家一起分享你们在音频制作和混音上的经验与技巧。

文章来源 [少数派](http://sspai.com) ，原作者 [Megabits](http://sspai.com/author/707024) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/21B8BD37-9215-4A71-B691-8159B2870EA1/526D5FF3-4548-4EB7-B661-8B2B338902F9.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:iPhone7/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fshop%2Fbuy-iphone%2Fiphone-7)

---

[🌐 原始链接](http://sspai.com/36247)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9f2f52a0-e9b1-4a56-a4c6-94cb3d916aad/9f2f52a0-e9b1-4a56-a4c6-94cb3d916aad/)
