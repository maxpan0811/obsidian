# 让外接屏实现一键调亮度调音量，一个 MonitorControl 就够了

---

让外接屏实现一键调亮度调音量，一个 MonitorControl 就够了
====================================

### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

相信很多 Mac 用户的日常 Setup，都是一台 MacBook + 一台外接屏。这样不仅可以提高效率，也能换来更好的大屏体验。但这样以来就会牺牲掉 Mac 上两个方便的功能：不能用键盘直接调节外接屏的亮度和外接屏输出的音量。

![](.evernote-content/D781525F-9906-4244-AA9E-C5B2771124EB/DC5FCE6F-2F57-4CB3-A3B3-5174C3F79223.png)

具体的原因是由于 HDMI、DisplayPort 和雷电等接口传输的都是数字音频信号，并不能调节音量大小，只有模拟信号才能进行调节。

但是，如果靠按显示器那种停留在上世纪 90 年代的按钮解决方案，显然会让 macOS 体验变得十分割裂。因此我们就得想个办法，把这两个功能给找回来。在这里，我推荐的 app 是 MonitorControl。

![](.evernote-content/D781525F-9906-4244-AA9E-C5B2771124EB/22476A5D-C5F6-4EEA-8BCE-071A93C37989.png)

MonitorControl 是一款 GitHub 上的开源软件，支持 macOS Sierra 及以上系统，不仅可以对外接屏的音量、亮度调节，还可以对外接屏的对比度进行调节，并可以自定义选择快捷键控制的类型，或是指定在某个屏幕启用这些功能，甚至连 `⇧Shift+⌥Option` 这种微调音量控制都能支持。

从 [这里](https://github.com/the0neyouseek/MonitorControl/releases) 即可下载到最新的 Releases 版。安装完成后，直接将音量输出选择到对应的外接屏，并在 MonitorControl 的「Keys」选项中选择监听形式，然后按下对应的按钮即可调节。此外，你也可以在菜单栏上点击 MonitorControl 的图标来进行调节。

![](.evernote-content/D781525F-9906-4244-AA9E-C5B2771124EB/8A910444-0B2A-46CC-9F38-0A8C70708355.png)

如果结合 Keyboard Maestro 或者 Karabiner 这类键盘映射工具，还可以方便地实现用外接键盘调节外接屏幕的音量和亮度，做到几乎和 LG UltraFine 一致的体验。

![](.evernote-content/D781525F-9906-4244-AA9E-C5B2771124EB/C615C7AF-08EC-49EA-9EA8-A49FC42B1EB4.png)

唯一的一个小问题，就是 LG 的屏幕在调节音量时，会出现屏幕自带的音量控制条，按一次出现一次，略微影响体验。

![](.evernote-content/D781525F-9906-4244-AA9E-C5B2771124EB/C1B5AF6A-8226-45BD-822E-DF9F567A1E7B.gif)

对了，这里要插一句的是，虽然 macOS 不能调节外接屏输出的音量和亮度，但在 Mac 上用 BootCamp 安装的 Windows 却可以，搞不懂苹果怎么想的……

如果你好奇原理，还可以点击 [这里](https://en.wikipedia.org/wiki/Display_Data_Channel) 查看 MonitorControl 所采用的 DDC 协议。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让你使用 Mac 更有效率 ⏱

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/56176)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c70ae668-7c1b-4222-aa61-406dfaeaf8ce/c70ae668-7c1b-4222-aa61-406dfaeaf8ce/)