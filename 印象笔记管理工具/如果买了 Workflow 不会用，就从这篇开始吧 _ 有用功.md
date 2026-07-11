# 如果买了 Workflow 不会用，就从这篇开始吧 | 有用功

---

如果买了 Workflow 不会用，就从这篇开始吧 | 有用功
-------------------------------

原创 *2016-01-15* *应用推荐第一媒体*

![](.evernote-content/B46D5598-7C23-4DA7-A600-0C5D662E861D/6E3B2DB3-2C98-4D6B-B1C9-244585FD561E.jpg)

如果你尚未听过 Workflow，那么它是一款 iOS 平台的神级自动化流程应用。所谓「流程」，就是将各类任务（Actions）串联起来的流水线（Flow），就好比是一家工厂。这家工厂的任务可以有很多种，比如获取剪切板内容，或是打开 app，播放歌曲等。

若此时，我们以特定的触发条件和执行顺序，将这些单一的任务衔接起来，便可以组成形形色色的流水线。而一旦流水线装配完成后，你会惊奇地发现：任务们就像是被安置在了传送带上一样，流程们会自动地被传送至任意想到达的地点。

而 Workflow 就是其中这样一家大工厂，它不仅能帮助我们省去每次重复操作的过程，而且还能完成许多不可思议的任务。喂，你有意识到吗，这是一股「平民化」的编程浪潮！听上去很酷不？那就加入这支先锋队吧。

![](.evernote-content/B46D5598-7C23-4DA7-A600-0C5D662E861D/ADC3AB9E-03D5-4639-A3CB-3EEF146466CF.png)

首次打开应用，Workflow 会引导进入自带的一例入门教程 – 制作 GIF。该流程的制作过程包括：

* 拖拽「拍照」与「制作 GIF」这两个 Actions 至右侧流程
* 选取拍照的张数，并点击「播放键」运行流程

说到这儿，相信你会猛然明白 Workflow 其特有的鲜明之处了吧！

> 敲代码并不是人人都会，可作为智能手机用户，有谁不会拖拽和点击呢？

而且你得明白 iOS 平台可是一向以权限限制严格而著称，因此也只有像开发出 Workflow 这样的越狱天才才懂得如何用最精妙的方式，去在已有的规则下，完成不可思议之作。

以下，我们将从入门、进阶到最后罗列部分实例，来尝试覆盖 Workflow 一些常用或新奇的玩法。如果大家觉得不满足，可以提出建议和请求，我们后续也会有更新。但是请始终记住

> 入手 Workflow 后最重要的一件事，应该是将所有的 Actions 和它们对应的用法全浏览个遍。

因为今后，你所有的新奇想法全会从这些 Actions 中迸发出。OK，话不多说，把玩开始！

### **入门**

作为一款效率软件，如何使用 Workflow 因人而异，但总归也万变不离其宗 —— 目的是去解决一个具体问题。因而，你得很清楚地知道自己需要完成何种目标，然后才能去具象化 Workflow 流程。

好比现在，我想要找一些绝美的壁纸，如何通过 Workflow 实现呢？其中一个思路就是通过 Unsplash 的随机 API 来获取精美图片。整个过程可包括三个任务动作：

1. **URL** 中填入 https://source.unsplash.com/random （输入图片源）
2. **Get Contents of URL**（获取链接内容）
3. **Quick Look** & **Save to Photo Album**（预览并保存至相册）

其实在 **Quick Look** 执行时，我们也可选择点击右上角保存图片，不过我还是推荐建立一个独立 Unsplash 相簿，将这些照片分门别类到一起。此 Workflow 不需要任何变量或复杂的环路，算是简洁实用的一例。

### **稍进一阶**

首先请原谅，我们在这边并不会仔细讨论与 URL Scheme 和 x-callback-url 相关的玩法。因为针对大部分用户，添加判断、循环之类已属不易，更不谈去添加一大行的 URL 语法了。

对我而言，有时需要去从网页中拖取一段视频。比如说：我现在想将微博内的秒拍视频下载到本地。而作为零基础的我，该怎样一步一步写出此 Workflow 脚本呢？

首先，我们得清楚地知道获取视频的过程无非就是：获得网页内的源下载链接，并保存该链接所指向的文件。所以此流程包括如下关键的两步：

**1. 分析网页**

为了解析网页代码，我们可以使用 **Get Clipboard** 抓取微博内的分享链接，接着 **Get Contents of URL** 获取网页内容并 **Make HTML from Rich Text** 即转化为 HTML 源代码。

得到源代码后，为了找到对应的视频代码块（HTML Block），我们得暂时使用 **Quick Look** 稍加查看引号内的代码，并搜索定位至同时包含「http」和「mp4」的段落。而此链接就是我们最终需要的视频源链接。

**2. 流程语法**

以上的测试流程尚属比较简单，但若想将故事拼凑完整，我们还需要这两个利器：「判断 If」和「重复 Repeat」，而在第一步分析中，其实这两件事都是在我们的大脑内完成的，因而最终的流程中还需要以下几个子任务：

* **Split Text** with Quotation Mark 以引号将原网页代码分割成片段；
* **Repeat with Each** & **If** Control Flow by Keywords 重复所有的引号分割段，并通过关键字判断筛选出视频源链接；
* **Set as Variable** & **Get Contents of URL** 将视频源链接设置为变量，待重复完成后，调出此变量并下载此链接所包含的源视频。

需要注意的是，源网页内目标视频的代码片段中包含 Escape Chararcher – 反斜杠 ‘\’，因此上面的变量需要替换掉该字符。纵观以上，整个事件包含了：触发，流程，判断，执行以及反馈，是一套完整的 Workflow 流程。正所谓一通百通，如果我们想要得到其他网站内嵌的视频，这一套解决方案也是通用的。

### **实例**

对于那些不清楚自己想要些什么，或者只是想纯粹去体验 Workflow 各大奇葩功能的主们，通常除了在官方 Workflow Gallery 之外，还可于非官方的集合 和 以及 中找到一些实用的例子。

这里，我们将罗列出十个可能会常用到的流程，请大家用 Safari 浏览器打开以下链接，并尽可能地去造作它们。

> 随机显示 Unsplash 图片：http://tinyurl.com/ngk8grn
>
> 获取微博内视频：http://tinyurl.com/j854vq8
>
> 保存网页至 PDF：http://tinyurl.com/hkp35he
>
> 扫描二维码，若为网页则打开之：http://tinyurl.com/pgsla8p （@JailJT）
>
> 举报垃圾信息：http://tinyurl.com/hgtbrgh （@tianshilei1992 、 @文刀刀漢三 ）
>
> 保存 Instagram 图片：http://tinyurl.com/zurcfwv
>
> 获取设备当前公网 IP 地址：http://tinyurl.com/nk3c6y4
>
> 横向拼接图片：http://tinyurl.com/jds8p53
>
> 每日天文图：http://tinyurl.com/h68r7fl
>
> 搜索剪切板：http://tinyurl.com/qg295pz
>
> 来电号码检测： http://tinyurl.com/hrgp484

需求总是千变万化的，所以也恳请读者们尽可能地将自己的需求描述给我们听，而我们会尽可能的添加和完善 Workflow 分享社区（比如后面即将介绍给大家的 BitTorrent Sync 共享文件集）。

要知道，这个星球上从来都不缺乏创新，来自曼切斯特的 15 岁学生 @logandev22 两年前就开始了 iOS 应用的开发之路。@coolstarorg 今年 17 岁，他生活在 San Francisco，是一名地道的全平台开发者。而你，准备好用 Workflow 让手头的 iOS 设备闪闪发光了吗？

![](.evernote-content/B46D5598-7C23-4DA7-A600-0C5D662E861D/ADC3AB9E-03D5-4639-A3CB-3EEF146466CF.png)

Workflow 适用于 iOS 8.0+ 的 iPhone 和 iPad，大小 44.5 MB，售价 18 元。

推荐阅读：如何将 Action Launcher 打造成私人效率助手？| 有用功

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA==&amp;mid=401617398&amp;idx=1&amp;sn=95bb521c1ee889eae15fddedf2af1dc7&amp;scene=1&amp;srcid=01157BjMHvKhI380EvTOw4Tu#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4981a63b-3ebf-45f4-8d12-00cccda3e228/4981a63b-3ebf-45f4-8d12-00cccda3e228/)