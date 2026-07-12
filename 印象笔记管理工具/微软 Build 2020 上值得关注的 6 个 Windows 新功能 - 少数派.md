# 微软 Build 2020 上值得关注的 6 个 Windows 新功能 - 少数派

---

微软 Build 2020 上值得关注的 6 个 Windows 新功能
====================================

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/21520255-A7DF-406F-A1D3-4478A8E58518)

微软 Build 2020 上值得关注的 6 个 Windows 新功能

本周，微软一年一度的开发者大会 ——Build 2020—— 在线上拉开帷幕。

尽管开发者大会的主要目的是为开发人员介绍微软在程序开发、云计算、AI、物联网等各方面的新进展，但依然有不少针对消费者市场，特别是 Windows 系统相关的内容。

PowerToys v0.18.0：Windows 版的聚焦搜索
--------------------------------

[PowerToys](https://github.com/microsoft/PowerToys/releases) 是微软推出的系统增强小工具合集，里面包含了一些带有实验性的系统功能，例如窗口管理、快捷键提醒、Markdown 预览、批量调整图片尺寸…… 你可以把它看成是微软为 Windows 推出的「外挂」，能让你实现许多实用有趣的小功能。

这次的 Build 2020 上，微软宣布又为它加入了两个新工具：启动搜索与键盘重映射。

启动搜索类似于 macOS 上的聚焦搜索，你可以利用快捷键（默认 `ALT + 空格`）呼出一个搜索框，然后输入软件或文件的名字，快速打开和进行操作。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/737D3CF5-CFE6-4C61-9474-2D460A82F5F9.jpg)

听起来这个功能好像和 Win+R 运行以及 Windows 10 上的 [系统搜索](https://sspai.com/post/55906) 没区别。微软表示它并不是为了代替系统已有的功能，而是为喜欢使用键盘的用户提供一种更快的启动方式。此外微软还计划为它加入更多实用的小功能，包括计算器、必应搜索等等。

实际上，Windows 上已经有不少类似的第三方应用，比如 [Wox](https://sspai.com/post/33460)和 [Listary](https://sspai.com/post/52725)等（启动搜索也使用了 Wox 的开源代码），它们目前的困境是缺少足够数量的拓展（与之对比，可以看一下 macOS 上的 [Alfred](https://sspai.com/post/55098)和 [Launchbar](https://sspai.com/app/LaunchBar)的拓展数量）。微软如果能在之后允许用户自己制作拓展，相信会比第三方工具更容易吸引到开发者，这样才能让这个工具真正实用起来。

此次 PowerToys 更新带来的另一个新工具是键盘重映射。除了简单的改键之外，它还支持快捷键的重新映射，你可以根据自己的喜好来重新映射 Windows 上的各种快捷键，这对一些喜欢自己调整键盘的用户来说是个挺实用的小功能。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/492E7BBD-6E7D-40A3-A73E-3267F212CDEE.jpg)

PowerToys 里的其他小工具：

Windows Terminal 1.0：现代化的终端工具
-----------------------------

在经历了长时间的测试后，微软终于正式推出了现代化终端工具：Windows Terminal 的 1.0 版本。相比之前 Windows 平台的同类工具，它不仅开源免费，还拥有完整的字体字符渲染机制（包括 Emoji）、支持 GPU 加速，并且采用了更现代的 Fluent 设计风格。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/FE06E91C-90B2-48A4-B434-C96713B4DD0C.png)

这个工具自去年公布预览以来就受到广泛的关注，毕竟 Windows 系统此前一直都缺少一个真正称得上足够好用的终端，Windows Terminal 的出现算是解决了这个问题。

少数派之前对 Windows Terminal 也进行了详细的介绍，感兴趣的话不妨阅读一下：

> [新生代 Windows 终端：Windows Terminal 的全面自定义](https://sspai.com/post/59380)

你可以在微软商店下载 [Windows Terminal](https://www.microsoft.com/zh-cn/p/windows-terminal-preview/9n0dx20hk701?activetab=pivot:overviewtab)。

Windows Package Manager：一行代码搞定软件安装
----------------------------------

如果你有使用过 macOS 或者 Linux，应该对「包管理器」有一些印象。有了它，你只需要一行简单的代码，就能方便快捷、干净利落地管理设备上安装的软件，这种体验确实很爽。

Window 系统在这方面则相对要落后一些，目前大家使用的都是 [Scoop](https://sspai.com/post/52496)、[Chocolatey](https://sspai.com/post/55309)等第三方的包管理器。微软自然也看到了这一点，在 Build 2020，微软正式推出了自己的包管理器：Windows Package Manager（WinGet）。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/B66357CD-B94C-49B1-B448-C4E0AF70E1B9.png)

虽然目前的预览版还比较简单（甚至不支持卸载软件），在功能上也与第三方的包管理基本一致，但是作为官方的一个新尝试，这种态度还是非常值得鼓励的。

对普通用户而言，目前预览版的 WinGet 称不上好用，因此只推荐有尝鲜想法和一定动手能力的用户尝试。你可以在微软官方的 GitHub 仓库的 [Release](https://github.com/microsoft/winget-cli/releases)页面下载。

拓展阅读：[在 Windows 10 上安装软件，你现在可以用微软的包管理工具了](https://sspai.com/post/60592)

Microsoft Edge：加入搜索侧边栏
----------------------

自从去年 [更新 Chromium 内核](https://sspai.com/post/58490) 后，Microsoft Edge 就一直在加入各种新功能。本次 Build 2020 上，微软又为它带来了两个：

**搜索侧边栏**：浏览网页遇到一个不熟悉的词时，通常我们都会在地址栏输入关键词，跳转搜索，然后再回到网页进行浏览。此次 Edge 新加入了一个搜索侧边栏，当用户在网页上看到想搜索的词时，选中它并右键选择搜索，会直接右侧显示搜索结果，这样你就不需要来回在标签页里跳转了。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/3B3C53C7-5E0A-40BE-AA4B-86385A6B7A70.jpg)

**集锦支持 Pinterest 和 OneNote**：[集锦](https://sspai.com/post/60041) 是 Edge 内置的一个用来进行网页剪藏的工具，可以用来收集 URL 页面、图片或文本等信息，并统一进行保存。微软这次为它带来了导出到 Pinterest 和 OneNote 的支持。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/22A4B701-988D-400D-8BD6-AB53FA38643A.jpg)

Project Reunion：让 Win 32 与通用平台更近一步
----------------------------------

微软从 Windows 10 推出开始就一直希望推进通用 Windows 平台（UWP），来解决 Windows 软件在兼容性、升级维护、以及跨平台等多方面的问题。虽然后来 Windows 10 Mobile 的失败一度让这一计划蒙上了阴影，但微软并不打算停下推广 UWP 的脚步。

在今年的 Build 2020 上，微软提出了 [Project Reunion](https://blogs.windows.com/windowsdeveloper/2020/05/19/developing-for-all-1-billion-windows-10-devices-and-beyond/) 计划。该计划的核心就是让开发者只需要开发一个 Windows 应用程序，就能运行在所有安装 Windows 10 系统的设备上。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/8F125A1E-D125-4BEE-9D24-35FF3B9B738A.jpg)

要实现这一计划，微软需要整合现有的 Win32 与 UWP 的 api，为开发人员提供便利，使其在开发时不必担心旧版本是否兼容的问题。此外，微软还需要为应用开发提供更易用的工具，例如这次推出的 WinUI3 框架，它能够让程序支持自适应 UI 适配，来方便程序在不同形态的设备上使用。

除了适应各种形态的设备与系统，Project Reunion 对云端也做了一些优化。新的 WebView2 允许开发者在程序里嵌入基于 chromium 的 WebView，并不会受到 Windows 本身的限制。

不过，这个计划从目前来看只能说是一个愿景，当年微软也提出过让 iOS/Android 应用重新编译生成 UWP 应用的技术，但最后实际上开发者并没有足够的动力去这样做。具体这项计划是否能达到推进 UWP 的作用，可能最终还是要看开发者对于它的反馈。

WSL：将 Linux GUI 软件带到 Windows
----------------------------

广受好评的 [Windows Subsystem for Linux](https://sspai.com/post/43813) (WSL) 在此次 Build 2020 上得到了两个更新，其中最引人关注的便是微软宣布 WSL 将在未来支持 Linux GUI 软件。这意味着用户可以在 Windows 上轻松运行更多的 Linux 软件，为经常使用两个系统进行工作的用户提供了便利。

![](.evernote-content/79F2AD1C-7DD8-4DE0-ACB4-970EFC03DE59/849770BC-0A64-4FFF-B440-5D0A82576C64.png)

另一个更新是 WSL 现在支持了 GPU 计算，用户可以从 NVIDIA CUDA 和 DirectML 中选择自己需要使用的计算方案。此外，微软现在还为 WSL 提供了更方便的安装方式，你只需在命令行中输入 wsl.exe --install 就能完成安装，比之前要简单了不少。

拓展阅读：[具透 | Windows 10 五月更新来了，这 7 个变化值得关注](https://sspai.com/post/60509)

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e) ，了解更多实用 Windows 技巧

---

[🌐 原始链接](https://sspai.com/post/60618)

[📎 在印象笔记中打开](evernote:///view/207087/s1/eb7e03eb-ee0e-49e4-a624-9309333b5a7c/eb7e03eb-ee0e-49e4-a624-9309333b5a7c/)