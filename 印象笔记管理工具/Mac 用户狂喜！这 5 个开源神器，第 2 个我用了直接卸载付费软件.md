# Mac 用户狂喜！这 5 个开源神器，第 2 个我用了直接卸载付费软件

---

来源：[打开原文](https://mp.weixin.qq.com/s/3bDMjVJmaPbNaeiltBCdpQ)

这里每天分享一个 iOS 的新知识，快来关注我吧

前言
--

又到周更时间了。这周翻 GitHub 翻得有点上头，挖到的东西比预想的多——有几个是老熟人，也有刚冒头的新货，整体看下来都挺能打。

每次整理这种推荐，自己其实是最大的受益者。不少之前没留意的库、工具，就是这么一个个补回来的。

这次一共 10 个。

废话少说，直接进正题。

开发工具推荐
------

alt-tab-macos - Mac 上的 Windows 任务切换器
------------------------------------

GitHub：lwouis/alt-tab-macos[6]

从 Windows 转过来的同学，多半受不了 macOS 默认的 Command+Tab——它只能切应用，不切窗口。这工具就是给 Mac 装了个 Windows 风格的 Alt+Tab，能直接预览所有窗口然后切过去。

我自己用了一阵子，真香。尤其同时开一堆 Chrome 窗口或者好几个 Xcode 项目的时候，效率直接起飞。窗口实时缩略图、各种快捷键自定义、连切换动画都能调。

完全免费开源，Swift 原生写的，性能贼好，几乎感觉不到它在跑。Star 12k+，作者更新很勤。多窗口工作流的 Mac 用户强烈推荐，装上就摘不掉。

Easydict - 颜值能打、实力也在线的翻译神器
--------------------------

GitHub：tisfeng/Easydict[7]

我用过最顺手的 macOS 翻译工具，没有之一。原生 Swift，UI 干净利落，划词翻译、截图翻译、OCR 都支持，还能同时拉好几个翻译引擎对比结果（有道、Google、DeepL、ChatGPT 都行）。

![](.evernote-content/BE9548D1-0989-484D-91C0-73C0EE4B2053/BB02D88D-5A26-4E20-99C8-06FFBD8E796F.png)

Easydict

最戳我的是它集成了苹果系统自带的词典和翻译 API，离线也能凑合用。对天天看英文文档的人来说，真就是刚需。我现在基本全天挂着，划词即翻，效率提升肉眼可见。

完全免费、开源，作者还在持续更新。Star 13.3k+，国产开源里挺亮眼的一个。要是你还在用那些花里胡哨的翻译软件，真心建议换这个试试，高下立判。

cmux - 给 AI 时代准备的终端
-------------------

GitHub：manaflow-ai/cmux[8]

比较新的一个项目，基于 Ghostty 终端内核做的 macOS 原生终端。最大亮点是垂直标签页，再加上针对 AI 编码代理（比如 Claude Code、Codex）的通知优化。

![](.evernote-content/BE9548D1-0989-484D-91C0-73C0EE4B2053/E455F5B8-4FBD-4933-B378-61944F4A52D1.png)

cmux

如果你每天用 Claude Code 或者 Codex 干活，cmux 能在后台任务跑完的时候直接通知你，再也不用干瞪着终端等结果了。垂直标签页对同时开多个会话也友好——屏幕利用率比横向那套高不少。

性能上，Ghostty 内核本身就是出了名的快，cmux 又在上面叠了一层 macOS 原生体验。重度终端 + AI 编码工作流的人会喜欢。项目还比较新，但维护挺活跃，可以蹲一下。

CodexBar - AI 编码用量监控菜单栏
-----------------------

GitHub：steipete/CodexBar[9]

iOS 圈大佬 steipete 做的，也是龙虾（OpenClaw）的创始人，一个 macOS 菜单栏小工具，专门拿来显示 Codex 和 Claude Code 的用量统计。订阅了这些 AI 编码服务的话，肯定多少在意每天烧了多少 token、还剩多少额度。

他上次截图说自己一个月烧了 130 万美元的 token 额度。

![](.evernote-content/BE9548D1-0989-484D-91C0-73C0EE4B2053/B8929F09-E750-402F-BF39-1B07FCEA60BE.png)

steipete 的使用额度

最赞的一点：不用登录任何账号，它直接读本地的使用记录。装好之后菜单栏就能看到当天用量，再也不用翻网页去查。Swift 原生写的，轻量，几乎不占资源。

适合所有重度玩 AI 编码工具的人。Star 暂时不算多，但作者本身就是 Apple 平台的老熟脸，代码质量不用担心。订了 Claude Pro 或 ChatGPT Pro 的同学强烈建议装一个。

总结
--

这周这 10 个项目质量都还挺能打的。

这些库和工具你用过哪些？自己有没有什么压箱底的好东西想安利？ 评论区聊聊呗，下周接着挖。

参考资料

[1]

getsentry/sentry-cocoa: https://github.com/getsentry/sentry-cocoa

[2]

pointfreeco/swift-composable-architecture: https://github.com/pointfreeco/swift-composable-architecture

[3]

sparkle-project/Sparkle: https://github.com/sparkle-project/Sparkle

[4]

vdugnist/DVAssetLoaderDelegate: https://github.com/vdugnist/DVAssetLoaderDelegate

[5]

spotify/SPTPersistentCache: https://github.com/spotify/SPTPersistentCache

[6]

lwouis/alt-tab-macos: https://github.com/lwouis/alt-tab-macos

[7]

tisfeng/Easydict: https://github.com/tisfeng/Easydict

[8]

manaflow-ai/cmux: https://github.com/manaflow-ai/cmux

[9]

steipete/CodexBar: https://github.com/steipete/CodexBar

[10]

newmarcel/KeepingYouAwake: https://github.com/newmarcel/KeepingYouAwake

这里每天分享一个 iOS 的新知识，快来关注我吧

[📎 在印象笔记中打开](evernote:///view/207087/s1/acf47dc6-8d84-4248-b32a-56a7450c54f2/acf47dc6-8d84-4248-b32a-56a7450c54f2/)