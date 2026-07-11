# 为了换上 Apple Silicon 的「芯」，苹果都做了什么 - 少数派

---

为了换上 Apple Silicon 的「芯」，苹果都做了什么
===============================

苹果要换「芯」早就不是新闻，但当 Tim Cook 正式宣布 Apple Silicon 的那一刻，仿佛以 Apple Park 的环形大楼为震央，全世界科技圈发生了一次地震。

「Apple Silicon 地震」不仅震动了所有关注苹果的人，更是一场对苹果团队自身的挑战。Mac 换「芯」之后，原来的应用还能不能正常运行？从 iOS 到 macOS，应用能带给用户一致的良好体验吗？

为了这次换「芯」手术，苹果做好准备了吗？

从 Intel 到 Apple Silicon，应用适配的挑战
-------------------------------

换「芯」之后的第一项挑战，就是 Mac 应用对 Apple Silicon 的适配。

对于 Windows 与 macOS 之间的应用不能通用，可能比较容易理解，毕竟两类应用从编程语言、源代码到系统都完全不同。但同样是 Big Sur 系统，应用也都是基于 Swift 语言（或 Object-C），为什么搭载 Apple Silicon 的 Mac，就不能直接运行现有的 macOS 应用呢？

问题就出在「应用编译」这一步。

开发者使用高级语言（例如 Swift、Java 或者 C++）编写应用，形成源代码（Source code)，但 CPU 不能直接识别源代码，只能识别二进制的机器代码（Machine code）组成的指令。所以开发者需要借助编译器，将源代码转换成机器代码。这个过程就像是建筑师（开发者）完成了设计（源代码），但工人们（CPU）没法看着漂亮的渲染图就开始施工，于是还需要技术人员，将建筑师的设计转换为工人能理解施工图纸（机器代码），在上面很多固定格式的标注（x86\_64 指令），这就是编译的作用。

不过 Apple Silicon 替换 Intel 芯片后，相当于换了一批建筑工人。很不巧，这群建筑工人读不懂图纸上的 x86\_64 指令，他们只认识一种叫 arm64 指令。所以即使建筑师、设计图纸都相同，但是建筑工人是没法照着为上一个团队准备的施工图纸开工。

既然有两个施工团队，那就让技术人员在做施工图纸的时候，一次性标注两套图纸，再打包到一起。到时候无论是哪个施工团队，找到自己能读懂的那一套不就可以开工了？

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/6AAB8778-1F6F-4E9F-BF06-8DA0C8D4B7E4.png)

Universal 2 应用包

Universal 2 正是照着这个思路实现的。在 Xcode 12 中，开发者可以选择同时为 Intel 芯片和 Apple Silicon 编译应用，并且会将编译后得到的两套可执行代码文件，打包成一个 Universal 应用。由于包含了两套文件，Universal 应用的体积自然也会变大。不过之后无论是在装有 Intel 芯片还是 Apple Silicon 的 Mac，Universal 应用都能顺利运行。

然而这项技术也不能完美地解决 Apple Silicon 带来的应用适配问题。

虽然在 Xcode 中只需要将应用选为 Universal 就可以开始编译，但如果你有基于某些 CPU 特性的代码，可能需要开发者做相应的修改 1 。其次如果开发者使用了第三方（非苹果官方提供）的代码库，那就必须等到第三方代码库的开发者提供 Universal 版本，才能将自己的应用也编译为 Universal 版本。如果应用是支持插件的，插件也必须为 Apple Silicon 重新编译 2 。

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/4E23F644-1682-42CC-9A0D-BAB6630D41FD.png)

所以对于开发者来说，Universal 2 并不是一棵忘忧草，想要保证应用能达到之前一样的体验和性能，还是需要付出额外的工作。

不仅如此，Universal 2 最大的问题，是它不支持第三方框架开发的应用。

「框架」是提供给开发者的一套可重复利用的组件，便于开发者快速完成应用开发功能。就像有人给建筑师提供了一套模版图纸，让他不用从头开始设计建筑。苹果官方给 macOS 提供了 AppKit，但同时也允许开发者使用其他团队提供的框架，例如 VS Code 所用的 Electron 和 WPS 使用的 Qt 框架。

为了解决第三方框架应用的适配问题，苹果准备了 Rosetta 2。

Rosetta 2 的思路和 Universal 2 不同，虽然我不能重新做一套带有 arm64 指令的标注，但是我给施工团队发一套字典，让他们自己查字典，将 x86\_64 指令转换成 arm64 指令，这不就可以开工了吗？

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/498A2EB5-B76B-4E19-B339-6107DBF6D4EA.png)

Rosetta 2 在系统中的位置

在用户从 Mac App Store 下载、通过安装包安装或者第一次启动时，Rosetta 2 就会启动，开始将应用所使用到的指令进行翻译，最终形成一本字典（官方称之为 「Stored translation」）。在应用运行时，发出的 x86\_64 指令就会先经过 Rosetta 2 的翻译，变成 Apple Silicon 能理解的指令。整个过程都是会在后台进行，对于用户来说，就像一切如常。

Rosetta 2 可以让用户在 Apple Silicon 的 Mac 上运行原来的应用，但性能和运行速度就无法保证和在 Intel 芯片的 Mac 上一样了。根据开发者的测试，Geekbench 5 通过 Rosetta 2 运行在装有 A12Z 芯片的 Apple Mac Mini Developer Transition Kit 中，单核跑分比 A12Z 在 iPad Pro 12.9 中低了大约 [25%](https://www.notebookcheck.net/First-A12Z-Bionic-DTK-Geekbench-5-benchmarks-show-Apple-s-transition-holds-immense-promise-only-a-28-in-drop-seen-in-single-core-score-compared-to-the-MacBook-Air-2020.477595.0.html)。尽管两者的硬件环境以及芯片频率等因素都不相同，这个跑分对比并不严谨，但 Rosetta 2 对于应用运行效率有不小影响这一点，是可以得出肯定结论的。

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/17E36CE1-C2E6-4CBE-B6A3-F86DC94D7DC1.png)

在「简介」中调整

值得注意的是，即使是针对 Apple Silicon 编译过的应用，用户还是可以自己以 Rosetta 2 来运行。某些应用本体更新了 arm64 版本，但插件没有更新的时候，用户就可以选择以 Rosetta 2 来启动，保证之前的工作流不受影响。

最后，即使是 Rosetta 2 也不保证能完美运行所有应用，官方文档中明确指出，「Kernel extensions」和针对 x86\_64 的虚拟机应用将无法通过 Rosetta 2 运行，只能期待开发者会推出 arm64 版本的应用。

不过作为消费者的我们不必太过担心，Universal 2 和 Rosetta 2 虽然不能完全解决应用适配问题，但它俩更重要的使命是给开发者和用户争取时间。从上一次 PowerPC 到 Intel 芯片的迁移历史来看，苹果从宣布迁移到最终终止对 PowerPC 芯片的系统更新，足足有[四年时间](https://zh.wikipedia.org/wiki/MacOS)，这四年时间一方面让使用 PowerPC 的 Mac 用户得以发挥设备的价值，另一方面给开发者足够时间去适配自己的应用，由此最大程度降低了过渡期对开发者和用户的影响。

有了之前的经历，再加上苹果目前在科技圈如日中天的影响力，给了开发者很大的信心。奇点微博、One Switch 的开发者[图拉鼎](https://sspai.com/post/30876)就说道：

> （芯片架构的转变）对普通用户来说，可能不熟悉。但对有点年份的开发者来说，这件事已经发生过一次了。所以开发者们普遍都比较积极和充满信心。

从 iOS 到 macOS，应用如何迁移
--------------------

Apple Silicon 带来的重大机遇，就是 iOS 和 iPadOS 的应用可以原生地运行在 macOS 中了。

对苹果持续有关注的读者，可能会指出来，去年 WWDC 2019 的时候，就宣布 macOS Mojave 能运行 iPadOS 上的应用了，这次只不过加上了 iOS，并没有实质性的改变。

其实虽然结果都是 macOS 上运行移动设备上的应用，其实这两次有着本质的不同。

去年苹果推出的是 [Mac Catalyst](https://developer.apple.com/mac-catalyst/) 计划，引导开发者将 iPadOS 上的应用移植到 macOS 中。在这个过程中，开发者需要重新编译应用，编译后的应用是可以运行在 Intel 芯片的 Mac 中的（当然有 arm64 的编译版本，也可以运行在 Apple Silicon）。而今年苹果宣布的计划中，iOS 应用不需要由开发重新编译，就可以直接从 Mac App Store 中下载运行，但只有装载 Apple Silicon 的 Mac 能享受到这项福利。

了解了两者的不同，可能会产生一个疑惑：既然经过编译可以让 iPadOS 应用运行在 Intel 芯片上，为什么苹果不提供工具，让开发者可以把 iOS 应用也编译一下，也运行在 Intel 芯片的 MacBook 上呢？苹果这么做，是不是为了特意给装 Apple Silicon 的 Mac 增加卖点呢？

想了解背后的缘由，我们还得回到去年 WWDC 上，看看 [Mac Catalyst](https://developer.apple.com/mac-catalyst/) 计划做了什么。

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/3F62B865-AECE-4459-8A43-8A74C44630B2.png)

想让一直跑在 A 系列芯片的 iOS 应用运行在 Intel 芯片的 Mac 上，要将应用从 arm64 编译到 x86\_64 版本，这恰好和从 Intel 迁移到 Apple Silicon 的过程相反。但这么多年阻止 iOS 登陆 macOS 还有更深的原因：两类应用的开发框架不同。虽然都是苹果的原生开发框架，但 iOS 应用使用的是 UIKit，和 AppKit 完全不同。

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/D05756A2-FE4C-4DC4-9966-62C47124D95A.png)

而 Mac Catalyst 所做的，是确保 AppKit 和 UIKit 所使用一样的底层技术，并移植一部分 UIKit 组件在到 macOS 中，这样也就实现了在 macOS 中运行 iPadOS 应用的目的。而今年 iOS 应用能登陆 macOS，同样是依靠 UIKit 在 macOS 中的移植，而且比 Mac Catalyst 更方便的是，因为 iOS 应用本身就是为 A 系列芯片编译的，在 Apple Silicon 上都不需要开发者重新编译，只需要开发者在后台开启跨平台选项，用户就能在 Mac App Store 中搜索到 iOS 应用。

![](.evernote-content/147F0B4B-47C9-4159-8276-729F4E41C387/28A20590-28E3-4BA5-82FA-26B144D5462F.png)

将这两届 WWDC 串联起来看，为了实现系统大一统， macOS 与 iOS 在底层技术和交互层面上不断融合，其中开发框架自然也会开放融合，Mac Catalyst 项目只是 UIKit 与 AppKit 在融合过程中诞生出的副产物。去年就提供给开发者，而不是等到今年，其实是给开发者多一年时间，去尝试同时适用全平台的交互与开发范式。

如果明白了这一点，站在苹果的角度，不难看出投入人力物力实现 iOS 应用在 Intel 芯片的运行，其实没有太大意义，毕竟两年后所有的 Mac 产品线都会是 Apple Silicon。

更重要的是从开发者的角度出发，Mac Catalyst 其实并没有明显地吸引 iPadOS 应用开发者投入精力，因为直接移植的应用品质不佳，并不能吸引消费者付费。正如国外知名设计团队 Iconfactory 在 [《What to Expect From Marzipan》](https://sspai.com/post/54715)一文中说道：

> 如果做一个 Mac 应用只是拨开开关的功夫，客户为什么要为它付费呢？

所以开发者也不买账 Mac Catalyst，由此一来，苹果团队自然会全力投入到 macOS 与 iOS 在 Apple Silicon 上的融合，而不是开倒车，去解决 iOS 应用在 Intel 芯片上运行的的事情。

当然，macOS 与 iOS 的系统融合是一个漫长的过程，iOS 应用目前也只是能运行在 macOS 上而已。从采用 Mac Catalyst 的应用表现来看，iOS 应用运行在 macOS 上，会因为硬件差别、UI 差别与系统差别出现不少体验上的问题。

One more thing
--------------

自从 2015 发布 Apple Music 之后，苹果似乎已经忘记了让观众肾上腺素飙升的「One more thing」环节，这次 Apple Silicon 的宣布，虽然 Tim Cook 没有念出这句「咒语」，但是达到了相同的效果。

对于我来说，让我振奋的不仅是 Apple Silicon 出现后，Mac 系列可能会出现的巨大变化，更是折服于苹果团队为实现目标所做出的精心准备。为了实现横跨多种类的大一统系统，微软选择直接将 Windows 通用于不同设备，谷歌选择从 Chrome OS 和 Android 两条路线尝试。而苹果选择的是先硬件、再软件，先底层、再 UI 的路线，一步一个脚印，让目标逐渐变为了现实。

其实技术路线本身并没有对错优劣，但相比各种天马行空的技术设想，工程师呕心沥血做出的成果，更让我为之动容。

编注：感谢 @图拉鼎 对本文提供的建议。

关联阅读：

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，第一时间了解 WWDC 2020 资讯

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

1https://developer.apple.com/documentation/xcode/building\_a\_universal\_macos\_binary

2https://developer.apple.com/documentation/xcode/porting\_your\_macos\_apps\_to\_apple\_silicon

---

[🌐 原始链接](https://sspai.com/post/61276)

[📎 在印象笔记中打开](evernote:///view/207087/s1/999163e1-5a12-4001-8e98-663cdefde8e9/999163e1-5a12-4001-8e98-663cdefde8e9/)