---
title: iPhone 6s GPU性能为何能够有大幅提升？
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/iPhone 6s GPU性能为何能够有大幅提升？.html
tags: [印象笔记]
updated: 2026-06-27
---

---
title: "iPhone 6s GPU性能为何能够有大幅提升？"
source: evernote
type: note
export_date: 2026-06-27
guid: da89030d-1bc4-4c4a-ad2d-4e2fd122f8d0
---

# iPhone 6s GPU性能为何能够有大幅提升？

[![](attachments/2afbd4a6f5927923.jpg)](http://www.feng.com/iPhone/news/2015-11-04/Why-the-iPhone-6-s-GPU-performance-can-have-a-boost_629108.shtml)

　今年在iPhone 6s的A9芯片中苹果公司仍然非常重视提高GPU性能，而且和上一代相比A9的GPU性能确实提升不少。  
  
　从第一代iPhone 还有它们使用的三星开发的SoC来看，可以说苹果公司简直就是Imagination Technologies 及其PowerVR GPU最大的支持者。对于双方来说，他们达成了一种富有成效的关系，在A9中这一层关系依然牢固如旧。A9 GPU采用的是 PowerVR Rogue家族的另外一种设计——GT7600，这一点不足为奇。

![](attachments/f6c17459e0f67822.jpg)

简单说来，虽然苹果还是没有公开他们所使用的GPU，但是通过iOS Developer Library 我们可以知道苹果使用的是哪个GPU家族产品。苹果仍然使用基于tile渲染与延续象素着色架构的GPU（只有PowerVR 符合这种条件），所以现在唯一的问题就是苹果使用的是哪个家族产品，它有多少核心。

关于A8 和它的 GX6450，通过它支持 ASTC这一点我们就可以准确知道它属于哪个GPU家族，因为只有Series 6XT 和较新的GPU有这个特性。在A9上我们就没有找到类似非常确凿的证据，不过从Metal Feature表暗示它的很多底层特性，这足以说明它使用的是新版本的PowerVR Rogue。Imagination发布 PowerVR Series 7 已经快有一年的时间，而苹果公司完全有能力在一年的时间内使用这种新的PowerVR 设计，所以我们可以确定A9使用的是Series 7设计。

![](attachments/778918c2b020cb32.jpg)

至于配置，看过A9模具你就会知道答案了。在A9模具上一共有6个不同的GPU核心，一共分成三组，它们之间有一个共享的结构单元。所以和我此前预期相比，苹果可能还需要一年的时间，不过至少在A9中我们已经看到了iPhone 终于用上6核GPU设计。

![](attachments/4c17c2e99a2819cd.png)

从特性和设计的角度来说，GT7600和A7以及A8 SoC上的GPU并没有很大的差别，但是它还是有一些值得注意的提升，还有一些优化，有利于提升整体性能。相比GX6450它使用了一个几何镶嵌细工协处理器作为基础，这是只有Series6XT才可选的功能。可是看遍苹果公司的开发者文件，我们也没有发现Metal还是没增加支持镶嵌细工，所以假设目前苹果还没有去掉这个硬件，他们肯定没有针对它的API支持。

另外 Imagination想通过小幅的调整来提高Rogue 架构的整体销量。其中， Special Function Units如今已经可以原生支持FP16运行，SFU 运行和ALU 运行可同时进行，提升了性能。ertex Data Master（几何图形前端）、Compute Data Master 和Coarse Grain Scheduler 都有更新提升性能。

![](attachments/96d4aca4c5c582e7.png)

从整体上来说，在A8上苹果没有使用6核设计让很多人出乎意料，到了A9他们终于决定不再继续“吓人”了，而这样的选择意义重大。在高性能SoC上，GPU一直是内存带宽最大的消耗者，以至于在所有的平板级SoC上，苹果已经把存储器总线做到了128比特，为的就是满足GPU的“大胃口”。LPDDR的64比特设计造成的内存带宽限制会影响到GPU的设计。但是随着对LPDDR4 的使用，苹果的内存带宽增加了一倍，再加上更大的L3缓存，如今他们已经能够满足6核GPU的需求。

GPU核心数量增加50%，Imagination架构效率提升，还有苹果进行的优化，所以我相信GPU时钟频率会有所增加。苹果此前表示A9的GPU性能相比A8应该有90%的提升。而从我们的跑分测试来看，A9GPU相比A8的提升已经不止这个数。

![](attachments/c28f5af449680c03.png)

[阅读全文](http://www.feng.com/iPhone/news/2015-11-04/Why-the-iPhone-6-s-GPU-performance-can-have-a-boost_629108.shtml)
