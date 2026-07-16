---
title: 才发现，Google Gemini 出了 Mac 版，居然可以读我的屏幕了
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/才发现，Google Gemini 出了 Mac 版，居然可以读我的屏幕了.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "才发现，Google Gemini 出了 Mac 版，居然可以读我的屏幕了"
source: evernote
type: note
export_date: 2026-06-27
guid: aa4d9e78-ebea-4e2d-8c15-5e81f65c5738
---

# 才发现，Google Gemini 出了 Mac 版，居然可以读我的屏幕了

**周五使用 Gemini 的时候，发现这货终于出了 Mac App，也就是 Gemini.app，这真是 Mac 党的福音啊，这个 AI 时代，对于 Mac 用户来说，几乎全是福音，太幸福了哈哈哈哈。**

![](attachments/894d063775be8c6b.png)

  

![](attachments/83ab8d39d3a1cc48.png)

  

把 App 拖入 Applications，安装完毕，打开就是 Gemini App 的 Mac 桌面版：

看到这个熟悉的界面或许你会脱口而出：这不就是套了个壳吗？你 Google 浓眉大眼的怎么也开始玩这一套了呢？

还真不是。这次 Google 最新推出的 Gemini 桌面端，原生架构，仅支持 Mac，下载地址是：gemini.google/mac

这次的桌面端是 100% 原生 Swift 应用，而非 Electron 套壳 Web。

![](attachments/8194de8ed2514ad9.png)

  

**Google CEO Sundar Pichai 在 X 上的原话是：“The team built this initial release with Antigravity, and it went from an idea to a native Swift app prototype in a few days.”**

**工程副总裁 Josh Woodward 明确表示："100+ features in less than 100 days. 100% native Swift. Lightning fast."**

![](attachments/affeb876a925a082.png)

  

也就是说，Gemini App 直接使用了 Apple 官方的 Swift 语言、基于 AppKit/SwiftUI 等 macOS 系统 API 构建的纯原生应用。

原生 Swift 让应用可以直接调用 macOS 的系统 API，比如 Option+Space 全局快捷键唤起、按应用粒度的屏幕共享权限，访问本地文件，以及 Apple 在最新系统中引入的 Liquid Glass（液态玻璃）界面设计语言。

有趣的是，现在 Anthropic 推出 Claude 设计工具，字节发布 SOLO 独立版，Google 开发 Gemini 桌面版，全部都是用自家 AI 工具实现，SOLO 93% 的代码都是 TRAE SOLO 写的，这次的 Gemin App，从想法到原生 Swift 应用的原型，Antigravity 只用了几天时间就完成了，随后，Antigravity 团队在不到 100 天里上线了 100 多个功能。

**其实我们看下 Claude 的发布节奏也就知道，不限量的 Token 和 Coding Agent 帮助这些顶尖大公司提高了多少效率。人是不可能做到一个月几十次发布的，从来没有过。**

目前 Antigravity 团队看起来更像是 Google 内部一个特别行动组，估计未来越来越多的公司会使用这种方式，小规模、高效、快速、不限量的 Token 使用。

在使用过程里也能感受产品的原生架构：只支持 Apple Silicon（M1 及以上）+ macOS Sequoia 15 及以上，磁盘占用 170M 左右，远低于典型 Electron 应用 300 MB+ 的基线水位。运行速度非常快。

**使用体验：有了 Mac App 和快捷键，我使用 Gemini 的频率明显增加了。**

我为 Gemini App 设置了快捷键：按两下 option 键呼出迷你对话框，有问题可以直接对话，也可以让 Gemini App 帮我读文件，感知屏幕，比如我把 B 站首页共享给 Gemini，就可以让它帮我总结和推荐视频。

![](attachments/041b98bb7bad4bba.png)

  

**Gemini App 可以直接读取和处理系统的本地文件，而不需要上传到云端。这个版本还不能通过文件地址访问 Mac 的文件夹，也没有激进到做 Agent 模式，直接像龙虾那样操控你的电脑，这一点倒是可以理解，毕竟 Google 太大了，过于激进也会出问题。**

![](attachments/25af309069a3acf1.png)

  

**从产品定位看，我预测 Gemini 会向这个方向发展，毕竟电脑才是最大的生产力。Google 把 Gemini 桌面端称作：一个真正个性化、主动且强大的桌面助手。做的就是类似 Spotlight/Siri 的“桌面智能助手”，甚至取而代之。我预计 Google 后续会在这个产品上增加更多依赖系统级能力的新功能。从这个方向上，Web 和原生 App 两者之间的差距只会越拉越大。**

那么，桌面端和 Web 端到底有哪些差异呢？我用龙虾做了张表，汇总了一下原生 App 和 Web 能力上的区别：

![](attachments/c18cbf32968e3ba8.png)

  

**注意：Web 版本还有一些功能没有移植到桌面端，比如“学习辅导”和笔记本“NotebookLM”，后者的多轮交互还得去 Web，不过迁移过来应该是指日可待的事情。**

对了，Gemin Web 端还新增了一个功能，就是导入记忆：

![](attachments/49f2b0e27d427733.png)

  

操作起来也很简单，比如我就把 GPT 的记忆导入进来了，两边互通友好，也许做个记忆共享的工具更有意思，Claude Mem 其实就是这个思路，现在我的龙虾和 Claude Code 就共享长期记忆了。

AI 的变化日新月异，李广密说，AI 取代的是不拥抱 AI 的人。我感觉拥抱了也悬，加油吧 😂

---

来源：<https://mp.weixin.qq.com/s/qEhZ2FKUOqWpsxd--kG10g>


---

[📎 在印象笔记中打开](evernote:///view/207087/s1/aa4d9e78-ebea-4e2d-8c15-5e81f65c5738/aa4d9e78-ebea-4e2d-8c15-5e81f65c5738/)
