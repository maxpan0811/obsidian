---
title: Claude Fable 5最强深度实测！5个小时，我把想了很久的Mac App做出来了！
type: source
created: 2026-06-14
updated: 2026-06-14
source_path: 印象笔记管理工具/Claude Fable 5最强深度实测！5个小时，我把想了很久的Mac App做出来了！.md
tags: [印象笔记, AI/编程]
updated: 2026-06-27
---

---
title: "Claude Fable 5最强深度实测！5个小时，我把想了很久的Mac App做出来了！"
source: evernote
type: note
export_date: 2026-06-26
guid: 4d1ec351-3928-4787-a095-6d2090da968a
---

# Claude Fable 5最强深度实测！5个小时，我把想了很久的Mac App做出来了！

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg2OTA1OTAxNA==&mid=224749...](https://mp.weixin.qq.com/s?__biz=Mzg2OTA1OTAxNA==&mid=2247490708&idx=1&sn=788313f5ae32c48d4e8beeb12922e21a&chksm=cf568733fd006ca2d01d177ba5bd820ec41d1617713d778705023edef94017fe6eeaeef60e01&scene=90&xtrack=1&req_id=1781083050630724&sessionid=1781083059&subscene=93&clicktime=1781083068&enterid=1781083068&flutter_pos=1&biz_enter_id=4&ranksessionid=1781083050&jumppath=1001_1781083056205,1104_1781083060182,20020_1781083062923,1104_1781083064791&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8rG34xXKQD7f0wR804tPphLTAQIE97dBBAEAAAAAAJe9NsGmPisAAAAOpnltbLcz9gKNyK89dVj0wEzRbRBJLqcEW9JFZO/H4EKlxtrLjz0Ahz9ofbwFxH30V1Y/HtR5jEYS+/+S0wDjxdw1g2qsAYUiWqOpcwHvXaoQzSlPalJ+NJ6lF/ZdOWU2pwgWpJ0tJpRvb65215tg1+P4L1tJN36qPIEj9L4tMRKdCmkgB+AVXWJ9iNbzPHd9RRakKWEipMDcm7UHjLnkAcRttgbRlZ/Jc4Gdn16Rwu051p1be3+qWVoktxw=&pass_ticket=n0HgUph9hWNfs+tZuKFZ9lzLfwUtnZfIHKgOZR6E1G+RhiXOgoyAE6BtOH1GI2lM&wx_header=3)

Original花叔花叔

早上一觉醒来，Anthropic又又又发新模型了：Claude Fable 5。

Claude 5来了是挺好的，但是为什么特么又整出个Fable出来...Opus、Sonnet、Haiku这套名字还不够烦人么。

以及，为啥也不叫Mythos？？A社在这个细节上还真是挺有硅谷大公司瞎特么起名的风范的。

不过，吐槽归吐槽，这个模型确实够强的。一句话说清它是什么：**Fable 5，就是加了安全护栏的Mythos**。Mythos是Anthropic那个之前只开放给政府和受邀机构、外界只闻其名的模型，这次加上护栏，公开发售了。

以及你最该知道的是：**从现在到6月22日，Fable 5直接包含在Claude订阅里，Pro和Max用户免费用**。6月23日起它会从订阅额度里移除，想继续用得另外充值、按量计费。想白嫖的话，只有这两周窗口。

能力上看一张图就够了：

![](attachments/37126c56b7236755.jpg)

SWE-Bench Pro这个测试，是把真实开源项目里的bug丢给模型自己修。80.3%意思是十个真实bug它能独立修好八个，第二名被甩开11个百分点。官方公告还反复强调一句：**任务越长、越复杂，它的领先越大**。最有画面感的官方案例是Stripe：5000万行Ruby代码库迁移，团队原本评估要两个月，Fable 5一天跑完。

![](attachments/135ca520fbda22cc.jpg)

这篇文章前一半把这个模型讲清楚，后一半给你看一个别处看不到的实测：我用它把一个想了很久的App真的做了出来，从动手到打包好安装包，一天。

我大概用了5个小时后的感受是：**Fable 5写代码的稳定性比之前强了不少，只要你能把需求或者说你要解决的问题说清楚，基本上它就能给你一次性搞定。**

## Fable是什么来历

今年4月，Anthropic启动了一个叫Project Glasswing的项目，把Mythos开放给政府网络防御部门和关键基础设施提供方。只有受邀机构能用，外界只闻其名。

6月9日这次发布，其实是同时发了两个模型：Claude Mythos 5和Claude Fable 5。两者是同一个底层模型，区别只在安全分类器。这东西你可以理解成站在模型门口的安检员，检查进出的问题和回答，碰到生化武器、网络攻击这类危险话题直接拦下。Mythos 5安检松，继续只给受邀合作方；Fable 5安检严，公开发售。官方的定义很直接：a Mythos-class model made safe for general use。

名字也是配套的：Mythos是希腊语的「神话」，Fable是拉丁语里的「寓言」，一个希腊语一个拉丁语，都是讲故事。同一个故事，两种讲法，护栏的松紧直接写进了产品名里。

设计逻辑我看懂了，但还是想吐槽一句：Haiku、Sonnet、Opus这套大中小，用户好不容易才记住谁是谁，现在又冒出来Fable和Mythos两个新名字，模型选择器越来越像文学选修课。有情怀，但真没必要。老老实实叫Claude 5，天塌不下来。

几个指标顺手列一下：上下文窗口1M token，单次输出最高128K，思考模式强制开启、关都关不掉。这个「关不掉」后面还会提到，它和我的使用体感直接相关。

## 贵不贵？说说我今天的真实用量

API价格是讨论最多的地方：10/百万输入，10/百万输入，10/百万输入，50/百万输出，正好是Opus 4.8的两倍。目前在Claude Code中的消耗速度也会是Opus模型的2倍。

说说我自己的情况：我今天9点起床之后，一直同步在做2-3个项目，全程Fable 5，200美元的Max版本到现在没遇到限制。

不过有个前提，Anthropic在发布模型的时候把用量reset了一波，相当于给所有人发了张新卡。希望OpenAI赶紧特么参与竞争，让这种reset来得更猛一些。

至于6月23号之后，如果真按API价格收费的话，那确实会有点太贵了。所以我的态度是：这两周先往死里用，23号之后的事23号再说。

## 我手上正好压着一个想了很久的项目

模型讲完了。对我来说，判断一个模型好不好，标准只有一个：**能不能把我想做的东西真的做出来**。

事情是这样的：我从来不会写代码，所有产品都是AI写的。这种工作方式有个很具体的副作用：AI帮你一个下午起十个项目，但它们散落在各个文件夹里，名字认不出，agent改了什么也看不见。

具体到每天的场景，我的需求其实很朴素：agent起好的项目，我想轻松点开看；写作类的项目很多，稿子要反复改，我需要一个顺手的编辑器；绘图和设计类的任务，我得一张张查看agent的生成结果；agent做出来的东西出问题、不符合我预期的时候，我希望能更容易地截图、把参考文件拖进去投喂给它。

这些事没有一件是写代码，但每一件都卡在文件系统和agent中间：Finder看得见文件、不好喂agent，终端喂得了agent、看不见文件。所以我的日常就是在Finder、Cursor、浏览器三个窗口之间来回切，找一个昨天生成的文件要翻半天。

我一直想要的，是**文件系统和agent之间有真正的联动**：左边浏览和预览本机文件，右边一个真的终端跑coding agent，agent每改一个文件，左边当场亮起来。一个vibe coding的驾驶舱。

之前搭过一个网页版的雏形，一个本地文件浏览页，能搜能预览，仅此而已。真正想要的部分全卡在后面：内嵌真终端、文件监听、编辑器、打包签名，这是一个完整桌面App的工程量。以前不是做不了，主要是改起来太磨人，我提一个需求要来回拉扯很多轮，想想就先放下了。

Fable 5发布当天，我决定拿它试试。

## 一天，从想法到安装包

时间线是这样的：

6月9日下午我先拿Opus 4.8做了个基础的版本。Electron桌面壳、内嵌终端、文件×终端×预览三方联动。但是有些核心的体验一直没跑通。

6月10日早上，拿到Fable后开启大改：代码编辑器、Markdown所见即所得、图片标注编辑、整个布局重构。然后打包、签名，生成dmg安装包。

中间没有跳过验收。我给这个项目定的交付标准是：5个独立的AI subagent分别扮演重度vibe coder、原生审美设计师、零文档新用户、终端十年老兵、破坏性质量官，对着成品、真机截图和代码打分，**全部≥90分且无红线才算达标**。第一轮就被打回来了：审美踩红线、终端健壮性不够、数据安全有口子。修完再审，总共折腾了四轮，才算过关。

它不是demo，也不是原型。它装在我的Applications文件夹里，我写这篇文章的此刻，它就开着。

![](attachments/072ab942278dd0e2.jpg)

右下角终端里挂着的，正好是Fable 5的上线通知。

## 翻箱FanBox：它长什么样

App叫翻箱，英文名FanBox。你也可以把它读成一个**agent box**：一个更好地管理agent和文件系统的工具，把「找文件 → 跑agent → 看它改了什么」收进一个窗口。

设计目标是每种文件「长得像它自己」，不点开就知道是什么。

几个我自己最常用的能力：

**活的仪表盘**。agent每写一个文件，那张文件卡片当场荡开涟漪、按改动频率发光。多个项目并行跑agent的时候，agent写到哪，光就走到哪，「看AI干活」第一次有了现场感。

**会话回放**。变更面板里有个播放键，像刷视频一样拖时间轴，重现这段时间agent一步步改了哪些文件。agent跑了半小时长任务，回来拖一遍就知道它都干了什么。

**拖文件喂agent**。从文件列表把文件或文件夹拖进终端，路径自动插进输入行；在预览里选中一段文字，点一下就发到终端给agent当上下文。反过来，终端里出现的文件路径可以直接点击，在翻箱里打开。

**⌘K找回**。记得名字片段就能搜到文件和文件夹，文件夹卡片右上角自动标上node/web/py这些项目类型徽章，一下午起的十个项目一眼认出来。

**原地轻改**。代码和JSON用Monaco（VS Code同款内核），Markdown是Notion式所见即所得，图片可以直接标注、画箭头、打码。看到哪改到哪，不用再开一个编辑器。

这篇文章就是在翻箱里写的，左边预览草稿，右边终端挂着Claude Code：

![](attachments/cb419caca6b3c1a1.jpg)

下面这张是我自己堆满截图和录屏的桌面，不开启终端agent窗口的情况下和finder没太大区别：

![](attachments/bc707d2e01507139.jpg)

agent刚在一个文件夹里改了两处，那张卡片就这样亮起来：

![](attachments/ee403444571332e6.jpg)

顺便，它有三套皮肤，配色、字体、图标、代码高亮整体切换：荧光绿炭黑的终端风、奶油纸赤陶橙的档案风、黑白红的索引风。

![](attachments/e96467547132d07f.jpg)

我自己对这个产品定义的边界是：翻箱不跟Finder拼文件管理，不做插件不做调试，重活继续甩给IDE。它只把「找回 + 预览 + 轻改 + 指挥agent」这一条链路做到顺手。全部本地运行，零外网请求，数据不出本机。

不过呢，它现在还是个挺初级的版本，主要解决我自己的问题，审美和功能都按我自己的需要来，没打算讨好谁。我估计很长一段时间，它都会是我的一个简单的个人项目。

## 开发过程里，Fable 5给我的真实体感

回到模型本身。这次开发前一天用Opus 4.8打底，后一天用Fable 5大改，同一个项目前后脚换了两代模型，差别很具体：不是更快，是犯错更少，**一次就把问题解决**。

举个最典型的例子。翻箱的图片缩略图功能，初版在图多的文件夹里点击会卡好几秒。这种性能问题以前是最磨人的：模型猜一个原因，改一版，好一点但没解决，再猜再改，三四轮下来代码越来越乱。

这次我就描述了一句「图多的目录点击很卡」。它定位出来两个叠加的根因：缩略图在加载原图整个文件，以及每次点击都在重建整个文件网格。然后一次改完：加了一个带缓存的缩略图接口，点击改成只切换选中样式不重建。点击响应降到0.1秒内，肉眼无感。一轮，没有返工。

类似的还有终端里中文目录名乱码的问题。这涉及xterm.js的宽字符处理，挺冷门的。它直接指出要用unicode11这个addon，还提醒这是个实验性API需要显式开启。这种准确命中偏门问题的瞬间，一天里出现了很多次。

打包阶段更明显。Electron打包在国内网络环境下是个连环坑：二进制下载被挡、原生模块编译失败、新版node让构建工具直接挂掉。以前这种环境问题能耗掉一晚上，这次它一路换镜像、换编译方案、调整打包配置，把一串坑都绕过去了，我全程只负责看着。

为什么会这样？我猜答案就藏在前面那个「关不掉」里。Fable 5的思考模式是强制开启的，单个回复明显比Opus要等得久。慢和准很可能是同一枚硬币的两面：**动手之前想得久，猜错率就低，猜错率低，就不用返工**。它省掉的不是打字时间，是返工。

说句诚实的：我没拿同一个问题去喂旧模型做对照实验，上面这些是体感对比，不是同题实测。但「以前五轮拉锯、现在一轮解决」这种差别，大到不需要仪器。

后来我看到Claude Code的作者Boris Cherny对Fable 5的评价：「自Opus 4.5以来最大的一步」，他强调的也是判断力和debug能力。跟我的体感，完全对上了。

## 最后

翻箱的安装包已经打好了，并且，已开源发布，你也可以拿我的开源代码去改出一个更适合你自己的agent box来👇

https://github.com/alchaincyf/fanbox

![](attachments/a750cc38952d9db1.png)

至于Fable 5，我的建议很简单：如果你是Pro或Max订阅用户，**6月23日之前，在Claude Code里把模型切到Fable 5**，拿一个你一直想做但觉得「太麻烦」的项目喂给它。免费额度你也有，我做翻箱用的就是它。

还没上手过Claude Code的，可以从我的橙皮书《Claude Code: 从入门到精通》开始，微信读书就能看。

我想了很久的驾驶舱，从拿到Fable 5到完成MacOS应用打包，5个小时。

你那个搁置很久的项目，说不定也就差一个这样的周末。


---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg2OTA1OTAxNA==&mid=2247490708&idx=1&sn=788313f5ae32c48d4e8beeb12922e21a&chksm=cf568733fd006ca2d01d177ba5bd820ec41d1617713d778705023edef94017fe6eeaeef60e01&scene=90&xtrack=1&req_id=1781083050630724&sessionid=1781083059&subscene=93&clicktime=1781083068&enterid=1781083068&flutter_pos=1&biz_enter_id=4&ranksessionid=1781083050&jumppath=1001_1781083056205,1104_1781083060182,20020_1781083062923,1104_1781083064791&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004a2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQ8rG34xXKQD7f0wR804tPphLTAQIE97dBBAEAAAAAAJe9NsGmPisAAAAOpnltbLcz9gKNyK89dVj0wEzRbRBJLqcEW9JFZO/H4EKlxtrLjz0Ahz9ofbwFxH30V1Y/HtR5jEYS+/+S0wDjxdw1g2qsAYUiWqOpcwHvXaoQzSlPalJ+NJ6lF/ZdOWU2pwgWpJ0tJpRvb65215tg1+P4L1tJN36qPIEj9L4tMRKdCmkgB+AVXWJ9iNbzPHd9RRakKWEipMDcm7UHjLnkAcRttgbRlZ/Jc4Gdn16Rwu051p1be3+qWVoktxw=&pass_ticket=n0HgUph9hWNfs+tZuKFZ9lzLfwUtnZfIHKgOZR6E1G+RhiXOgoyAE6BtOH1GI2lM&wx_header=3)
[📎 在印象笔记中打开](evernote:///view/207087/s1/4d1ec351-3928-4787-a095-6d2090da968a/4d1ec351-3928-4787-a095-6d2090da968a/)
