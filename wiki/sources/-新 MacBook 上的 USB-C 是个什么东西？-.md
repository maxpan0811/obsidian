---
title: "新 MacBook 上的 USB-C 是个什么东西？"
type: source
created: 2026-06-27
updated: 2026-06-27
source_path: 印象笔记管理工具/新 MacBook 上的 USB-C 是个什么东西？.md
tags: [evernote, impression]
---

---
title: "新 MacBook 上的 USB-C 是个什么东西？"
source: evernote
type: note
export_date: 2026-06-22
guid: d413fa31-6536-4cc4-bb9c-a705b0f41b99
---

# 新 MacBook 上的 USB-C 是个什么东西？

[![](attachments/e23935bb6caf8213.jpg)](http://cdnzz.ifanr.com/wp-content/uploads/2015/03/usbc.jpg)

4 年前，苹果引入 ThunderBolt，高速率传输以及支持多设备同时接入是它的特点。但 4 年过去，ThunderBolt 仍然无法触及主流大众用户，绝大部分 PC 依然使用 USB 接口。

所以，不要怪苹果为了让 MacBook 变得更薄，而直接放弃 ThunderBolt，而采用了体积上更小，可以正反插的 USB Type-C 接口（以下简称 USB-C）。——但是，在它到来之前，或许需要普及一些知识。

### 问题一：USB-C 与 Lightning 接口谁大谁小？

USB-C 接口与 Micro-USB 大小相近，8.4 mm x 2.6 mm。从图片上看，体积要比 Lightning 接口要稍微大一点，但相差也不远：

[![](attachments/1ddede8db51f2290.jpg)](http://cdnzz.ifanr.com/wp-content/uploads/2015/03/usb-c_sizecompare.jpg)

### 问题二：USB-C 中的 Type-C 是什么？

Type-C 是指 USB 接头的一种特定的规格。实际上，USB 的接头拥有多种规格，比如说以往我们常见的 USB 接头学名叫 USB Type-A，又比如 Android 手机上常见的 Micro-USB 也是 USB 接头的一种规格。

而令 MacBook 唯一的接口拥有高传输速率以及双向充电的特性，是最新的 USB 3.1 规范。该规范将 USB 接口传输速率提高到 10Gbit/s，而且支持三段电压 5V/12V/20V，最大供电 100W。——实际上，由于 USB 3.1 规定将向下兼容采用 USB 2.0/1.0 的设备，所以实际上如果其它采用 USB 3.1 规范的传统接头（Type-A），也可以直接与原来的 USB 设备相连。

实际上，MacBook 上的 USB 接口全名应该是 USB 3.1 Type-C。

一句话，USB 接头的规格决定 USB 的形状，而 USB 传输规范则决定它的性能与功能。

### 问题三：为什么 USB-C 可以取代 MageSafe 以及 ThunderBolt？

最关键的地方是 USB 3.1 规范规定，USB 3.1 接口可以支持 3 段电压，而且最高支持 100W 功率输出。而苹果笔记本电脑当中，对电源功率要求最高的是 Retina MacBook Pro 以及 15 寸和 17 寸 MacBook Pro，功率 85W。所以，USB-C 完全可以满足 MacBook 对电力的需求。

之前苹果看中 ThunderBolt 是因为它可以提供更高的传输速度，让苹果放开手脚开发更高分辨率，显示质量更好的显示器。而 USB 3.1 规范不光将传输速度提高到与 ThunderBolt 相等的 10Gbit/s，而且更重要的是，还支持 DisplayPort 1.2a 数字视频规范——苹果的显示器就采用 DisplayProt 标准来与电脑连接。

在未来，根据最新发布的 DisplayPort 1.3 规范，为了可以同时支持 2 部 4K 显示器，以及支持 5K 分辨率的显示器，它对带宽的要求提高到 8.1Gbit/s，而这并没有超过 USB 3.1 的性能极限。

### 问题四：USB-C 可以取代 iPhone 上的 Lightning 接口吗？

由于 USB-C 的纤细，很容易联想到，苹果是否会在 iPhone 上用它来取代 Lightning。但仔细研究之后，发现两者虽然外形相近，可以供电也可正反插，但实际上有很大的不同。

根据在 [TheiPhoneWiki](http://theiphonewiki.com/wiki/Lightning#Lightning_Digital_AV_Adapter) 上有一段匿名人士的解释，以及 Chipworks 对 Lightning 接头的拆解，苹果在 Lightning 线内安装了数控芯片，用来和其它 iPhone 外设进行交互。

[![](attachments/8deb06a348a1546d.jpg)](http://cdnzz.ifanr.com/wp-content/uploads/2015/03/chip-1.jpg)

右上方的芯片上印着 ARM 的 LOGO

一个有名的例子就是，[Panic](http://www.panic.com/blog/the-lightning-digital-av-adapter-surprise/#comment-16841) 在 iPhone 5 转 HDMI 转接头里发现了一颗 ARM SoC 芯片，而且还配备了 256MB 的 RAM。它的工作流程是，“解码后的视频信号经过压缩通过 Lightning 线来传输，然后最终通过 ARM 解码然后推送给 HDML 设备。”

换言之，如果只是换接口，UBS Type-C 和 iPhone 上的 Lightning 接口没有太大的差别。但 USB 线 与 Lightning 线的差别可太大了。

### 问题五：现在有多少设备支持 USB-C？

MacBook 是第一款支持 USB-C 的笔记本电脑。鉴于过去数年其它 PC 厂商对苹果笔记本电脑产品的不同程度的模仿，估计 USB-C 很快将在下一代 PC 笔记本上出现。

诺基亚的平板电脑 N1 是世界上第一款支持 USB-C 的平板电脑。

至于外设，SanDisk 以及 LaCie 各自推出了采用 USB-C 的外设产品，前者是 32GB 的 U 盘，后者是移动硬盘。

题图来自 [arstechnica](http://arstechnica.com/gadgets/2015/01/usb-3-1-and-type-c-the-only-stuff-at-ces-that-everyone-is-going-to-use/)

[![](attachments/08bc73505a87830c.png)](http://www.ifanr.com/author/yibie)

**[陈一斌](http://www.ifanr.com/author/yibie)**

爱范儿副主编，MindStore 社区联合负责人与总策划。于不可能处发现可能。

[邮箱](mailto:yibie@ifanr.com) [Twitter](http://twitter.com/yibie) [Facebook](http://www.facebook.com/yibie) [新浪微博](http://weibo.com/yibie)

#欢迎关注爱范儿认证微信公众号：AppSolution（微信号：appsolution），发现新酷精华应用。

![](attachments/325472601571f31e.gif)

[![](attachments/325472601571f31e.gif)](http://da.feedsportal.com/r/144540365956/u/362/f/642084/c/33866/s/500734/a2.htm)![](attachments/325472601571f31e.gif) [![](attachments/c5bbe5389daaf516.jpg)](http://mindstore.io/mind/2659/)

[爱范儿 · Beats of Bits](http://www.ifanr.com) | [原文链接](http://www.ifanr.com/500734) · [查看评论](http://www.ifanr.com/500734#comments) · [新浪微博](http://www.weibo.com/ifanr) · [微信订阅](http://www.ifanr.com/weixin) · [加入爱范社区！](http://bbs.ifanr.com/)


---

[🌐 原始链接](http://www.ifanr.com/500734?utm_source=rss&utm_medium=rss&utm_campaign=)
[📎 在印象笔记中打开](evernote:///view/207087/s1/d413fa31-6536-4cc4-bb9c-a705b0f41b99/d413fa31-6536-4cc4-bb9c-a705b0f41b99/)
