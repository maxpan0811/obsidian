---
title: "谷歌量子计算机Willow做了什么？大多数媒体都没说到点子上 _ 袁岚峰"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/谷歌量子计算机Willow做了什么？大多数媒体都没说到点子上 _ 袁岚峰.md
tags: [印象笔记]
---

# 谷歌量子计算机Willow做了什么？大多数媒体都没说到点子上 _ 袁岚峰

# 谷歌量子计算机Willow做了什么？大多数媒体都没说到点子上 | 袁岚峰 --- 速读摘要 即在某个数学问题上，量子计算机超越最强的经典计算机。顺便说一句，国内的报道中都没有翻译Willow这个词

---

# 谷歌量子计算机Willow做了什么？大多数媒体都没说到点子上 | 袁岚峰

---

速读摘要

即在某个数学问题上，量子计算机超越最强的经典计算机。顺便说一句，国内的报道中都没有翻译Willow这个词，大概是因为它有几个词义，柳树、球棒和纺织业中的威罗机，不知道该对应哪个。如果你能实现纠错，那你肯定能实现量子优越性，因为纠错意味着你对量子比特的操控已经达到了一个很高的水平。而如果你连量子优越性都做不到，那你当然不可能实现难度更高的纠错。那两个取样问题之所以能率先实现量子优越性，正是因为它们不需要纠错。

原文约4004 字|图片31张|建议阅读9分钟|[评价反馈](https://static.app.yinxiang.com/embedded-web/clipper/#/Evaluating?d=2024-12-25&nu=54744e0c-dcef-49ba-9946-c40bcbc9f062&fr=myyxbj&ud=328ef&v=2&sig=AD1B7306E6844A568E4A8026BD2A14BC)

原文链接: [http://mp.weixin.qq.com/s?\_\_biz=MzI0NzQzMjU3Ng==&mid=2247582...](http://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247582133&idx=1&sn=a35bd1190670a2baff534d66cfc780b3&chksm=e84575b7aa59d5636f873647509f34036365ea6dd6dd5418de6e0fde82180c0d44bffbb919fd&mpshare=1&scene=1&srcid=1225QbV6kG9p9KrQBLzurpU7&sharer_shareinfo=9ea35b7dff05c02fb26933c533a81030&sharer_shareinfo_first=9ea35b7dff05c02fb26933c533a81030#rd)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/D02B7D8B-9541-497E-9C69-BFE957F4A7E5.gif)

2024年12月中旬，谷歌的量子计算机Willow一下子在全球爆火。典型的报道标题像这样：《谷歌Willow量子芯片逆天出世！5分钟颠覆10亿亿亿计算极限，马斯克奥特曼惊叹》（https://www.thepaper.cn/newsDetail\_forward\_29604896）；《谷歌发布跨时代量子芯片Willow，5分钟顶超算1025年，马斯克、奥特曼点赞》（https://finance.sina.com.cn/tech/roll/2024-12-11/doc-inczawip0624279.shtml）。也有很多网友来问我，对此怎么看？

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/F28B6BE8-6D83-4990-8FAB-8C5BE774C251.png)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/4AADEE29-D1B8-4CC3-9603-0217042F18A1.png)

我的第一反应是，我对量子计算机“5分钟顶超算1025年”心中毫无波澜。因为这是早已实现的一类成就，叫做实现量子优越性（quantum advantage），即在某个数学问题上，量子计算机超越最强的经典计算机。

2019年谷歌的超导量子计算机“悬铃木”（Sycamore）第一次实现了量子优越性，相应的数学问题叫做“随机线路取样”（random circuit sampling）。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/67DA07C1-85CF-4391-929E-5BA44E1E176E.jpg)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/4581D492-4151-4470-A119-0808DFD6AD17.jpg)

2020年，中国科学技术大学潘建伟院士团队的量子计算机“九章”也用光学体系实现了量子优越性，相应的数学问题叫做“高斯玻色子取样”（Gaussian boson sampling）。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/AB21A85F-BCD3-4125-B6D9-A6D37D58600B.jpg)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/02EA5524-8A60-4FDD-A303-842E640D514E.jpg)

2021年，潘建伟团队的超导量子计算机“祖冲之二号”也实现了量子优越性，数学问题也是随机线路取样。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/BD770BE5-A9DD-4941-BB7D-57D1FEEB8D1E.png)

这类研究典型的成果，就是量子计算机处理某个数学问题的速度超过最强的超算好几个量级，如几分钟对几亿年。但这类研究也有个核心的局限性，就是这种优势只适用于某些数学问题，而这些数学问题还没有现实的应用。它们纯粹是为了实现量子优越性而设计出来的，好比先射箭，再画靶子。

量子计算机这个领域的一大基本状况，就是它目前还没有实用价值。它或者是对某些问题算得快，但这些问题本身尚无用处；或者是能处理一些有用的问题，但经典计算机对这些问题算得更快。总之，目前的量子计算机没有一个是有真正的实用价值的。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/CC940B32-1492-4131-91F9-3AF3895E3CBE.jpg)

因此，我的第一反应是，Willow只不过是把量子优越性的倍数进一步提高而已，并没有改变基本状况，所以这只是个量的改进，不是质的进步。顺便说一句，国内的报道中都没有翻译Willow这个词，大概是因为它有几个词义，柳树、球棒和纺织业中的威罗机，不知道该对应哪个。其实在我看来，既然谷歌的上一代超导量子计算机叫做悬铃木（Sycamore），那么十有八九，Willow应该指的是柳树，这个系列都以树木命名。正如IBM的超导量子计算机都以鸟类命名，鹰（Eagle）、鱼鹰（Osprey）和秃鹫（Condor）等等。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/84110C0B-D8F6-42BB-A44A-EF61E06682B7.jpg)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/E4070F13-946B-45CD-8CFC-37B8CF7E9BCF.jpg)

然而，我稍微有点空以后，去搜了相应的原始报道，就发现了一件令人吃惊的事。谷歌团队的论文是12月9日在线发表于《Nature》（https://www.nature.com/articles/s41586-024-08449-y），它的标题叫做《低于表面码阈值的量子纠错》（Quantum error correction below the surface code threshold），并没有提计算能力的进步。再看一下文章，更令人震惊的是，里边压根就没提5分钟对1025年！媒体热炒的这件事，论文里提都没提！

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/1D961ED8-0B82-462E-BF3E-78213F22FE42.png)

那么这个消息是从哪里来的呢？再仔细找找，出自谷歌的一个发布会，谷歌量子AI团队的领导人Hartmut Neven为此写了一篇报道（https://blog.google/technology/research/google-willow-quantum-chip）。也就是说，5分钟对1025年这个说法其实是谷歌自称的，还没有经过同行的审稿确认。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/78BD6D00-29A0-4D6C-81BB-F1668378F485.png)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/3945FC8F-A401-4F56-BA21-A13D7D0B130C.png)

当然，我并不是说这个算力的进步一定是错的，我只是说它并没有写在论文里，还需要一段时间来检验。这里真正的重点是，谷歌自己和业内专家都认为，这个工作的关键是纠错，而不是算力进步。我赶快咨询了我的几位量子计算专家朋友，对这件事的细节增加了很多了解。

实际上，《Nature》杂志为这个工作写了一篇评论文章（https://www.nature.com/articles/d41586-024-04028-3），标题就是引用我的一位科大同事说的“一个真正惊人的突破”（‘A truly remarkable breakthrough’: Google’s new quantum chip achieves accuracy milestone）。那么这个突破究竟惊人在哪里？简而言之，就是量子计算的纠错终于开始见效了。以前是越纠越错，现在是越纠越不错。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/C14DB3B5-C20B-4A3F-8458-CEE33D670789.png)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/22135A6F-8E97-4D0A-BC06-37BB5AFF4CD5.png)

我们来非常简略地解释一下，纠错是什么意思。由于受到环境的影响，计算机的存储和操作可能出错，例如0变成1，1变成0。曾经有人在玩《超级马里奥》的时候，发现马里奥突然出现在一个不可能的位置，后来分析可能就是因为一个宇宙线高能粒子打进来，导致一个比特出错。这还是经典计算机，它出错的概率相对较低。量子计算机的基本操作单元“量子比特”（qubit）对环境更敏感，出错的概率也就更大。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/EC1A2CB7-AEFB-48B7-B680-A46D0A390222.jpg)

所以无论是经典计算机还是量子计算机，都需要纠错。基本思想就是用多个比特来保一个比特，比如说把一个比特复制成三个一组。正常情况下它们应该是000或者111，假如我们有一天突然看见了001，这说明什么？有两种可能得到001，一种是一个0出错变成1，另一种是两个1出错变成0。显然第二种可能远低于第一种，于是我们少数服从多数，把那个1变成0，这就实现了纠错。

为了提高纠错的可靠性，还可以用更多的比特来保一个比特，例如用5个、用7个等等。所以有物理比特和逻辑比特之分，纠错就是用多个物理比特，来实现一个逻辑比特。

量子计算中的纠错，基本思想也是如此。只不过由于量子力学的特性，纠错方法设计起来更加复杂一些。这篇论文标题中提到的表面码（surface code），就是一种常用的纠错方法，它是用n × n的二维量子比特阵列，来实现一个逻辑量子比特。最小的1 × 1，就是没有纠错。3 × 3就是用9个物理量子比特，实现一个逻辑量子比特。5 × 5就是用25个物理量子比特，实现一个逻辑量子比特，如此等等。这里的n，称为码距（code distance）。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/E1696A7D-915F-47D8-8EC5-F2F9CB7A8A03.png)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/2020D5F0-CB36-476B-83D4-6267BAFB09B9.jpg)

“柳树”的量子比特布局图，见金贻荣《谷歌量子纠错取得重要突破：逻辑量子比特寿命大幅延长》（[谷歌量子纠错取得重要突破：逻辑量子比特寿命大幅延长](https://mp.weixin.qq.com/s?__biz=Mzg2MTUyODU2NA==&mid=2247617101&idx=1&sn=4c7756b36f1dfde15534298731077412&scene=21#wechat_redirect)）。其中黄色是数据比特，蓝色是测量比特，绿色是泄漏消除比特。红色、橙色、黑色框线分别标出码距为3、5、7的编码范围。可以看出，码距就是数据比特二维阵列的长度，如码距为3时，数据比特是3 × 3的阵列

乍看起来，码距越大，纠错的效果应该越好，对吧？但实际上，以前的实验结果都是越纠越错，即3 × 3的错误率比没有纠错还高，n越大错误率越高。这是为什么呢？因为纠错能生效的前提是，纠错前的正确率要超过某个阈值。假如没达到这个阈值，那么越纠错反而越糟糕。好比俗话说，三个臭皮匠顶个诸葛亮，但真能做到这一点的恐怕不是皮匠，至少也得是徐庶、程昱、郭嘉之流。如果都是王司徒这样的，恐怕是越多越添乱。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/02F89D73-486B-4505-841E-49C28AFC4615.png)

基于这些背景，就可以理解这篇文章的标题《低于表面码阈值的量子纠错》。它的意思是，通过很多方面的改进，终于让表面码纠错实现了正向效果。码距为3的优于码距为1即无纠错，码距为5的优于码距为3，码距为7的优于码距为5，每次基本上错误率下降一半。目前的实验就做到码距为7。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/615C2844-7799-4B96-A94F-D444FC7AC280.jpg)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/4980D934-7100-4BED-AEE2-AC988A610A37.png)

论文图1d，错误率随码距的增长指数下降

总之，这是个质的进步，而不只是量的进步。大多数媒体炒作的5分钟对1025年，其实并不是重点。量子纠错变得有用了，才是真正重大的进步。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/F1A2256A-FFD0-4A75-9EFE-656BA69FAAA2.png)

更具体而言，量子优越性跟纠错之间是什么关系呢？前者是后者的一个基础。如果你能实现纠错，那你肯定能实现量子优越性，因为纠错意味着你对量子比特的操控已经达到了一个很高的水平。而如果你连量子优越性都做不到，那你当然不可能实现难度更高的纠错。

有人可能会问，实现了纠错又有什么用？回答是，目前仍然没有实用价值。但沿着这条路发展下去，将来就可能造出真正有用的量子计算机。

谷歌在自己的报道中列出了一个六步走的量子计算路线图，量子优越性是第一步，纠错是第二步，第三步是长寿命的逻辑量子比特，第四步是逻辑门，第五步是工程扩展，最后一步是大规模的有纠错的量子计算机。2019年的悬铃木是实现了第一步，现在的柳树是实现了第二步。这一方面告诉我们，量子计算的发展仍然是路漫漫其修远兮，一方面也告诉我们，目前确实又迈出了坚实的一步，这是非常了不起的。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/DF8B232E-0442-4AF3-A043-524FB70D3E53.png)

实际上，我在跟专家们通话的时候，也立刻明白了一件事情。量子计算机之所以现在没用，很大程度上就是因为没有纠错。

其实量子计算在理论上有一些著名的应用，如因数分解，它可以用来破解RSA密码以及比特币。是的，比特币是可以被量子计算机破解的！但为什么目前还没有实现呢？因为大规模执行这样的算法需要很高水平的纠错。所以目前我们只能用量子计算机来分解一些很小的数，例如15 = 3 × 5，而不能分解密码中实际用的几百位上千位的数。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/BCB3793C-411C-4665-AC26-9AE6C39F1B4D.jpg)

量子因数分解算法的提出者、美国科学家Peter Shor

这就是为什么，实现量子优越性用的数学问题不是因数分解这种人人都能理解的问题，而是随机线路取样和高斯玻色子取样这两个奇怪的问题，普通人都听不懂它们是在干啥。那两个取样问题之所以能率先实现量子优越性，正是因为它们不需要纠错。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/99E57C7D-ABBB-4E86-9FAE-4331A8D73B26.jpg)

对玻色子取样的解释

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/8ABBABC9-7F7B-4CC7-A67F-20825C54ECA8.jpg)

玻色子取样的概率分布

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/1974723C-1E67-4B07-8824-03978D9B41CA.jpg)

玻色子取样的提出者、美国科学家Scott Aaronson

将来假如纠错的水平进一步提升，说不定就可以实打实地分解因数，破解密码。到那时量子计算的威力就是一目了然，任何人都不会有疑问了。当然这还需要艰苦的努力，不过至少已经露出了曙光。

最后，你可能想问，中国在量子纠错方面做得怎么样？我们又被落下了吗？我可以告诉大家的是，我的科大同事们一直在攻关。他们两年前率先演示了码距为3的纠错实验，现在正在做码距为7的实验，预计数月内完成实验。

[量子计算“华山论剑”，中美竞争态势胶着](https://mp.weixin.qq.com/s?__biz=MzI2NDIzMjYyMA==&mid=2247528767&idx=1&sn=aef11ceacc2d8adb609a7cd2caae548e&scene=21#wechat_redirect)

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/BA918FC3-84D4-48EB-B4F0-6FAB521C9819.jpg)

在本文录制的当天12月17日下午，我收到消息：祖冲之三号超导量子计算机已经上线，文章发在arXiv上，欢迎大家去看。

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/D6D101DE-B258-438F-94D6-4B5014AB8F5B.png)

**■****扩展阅读**

[九章三号如何遥遥领先？袁岚峰老师的解读来啦！](https://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247575486&idx=1&sn=339601c268a2d28f4897f4a8fda62fcc&scene=21#wechat_redirect)

[中国的量子跃迁 | 袁岚峰](https://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247541118&idx=1&sn=3222150be4e9fa438860bd77085a5085&scene=21#wechat_redirect)

[我国量子计算优越性研究取得重要进展 | 中国科学技术大学](https://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247535422&idx=2&sn=18804637587eb269da89e8f12b10275d&scene=21#wechat_redirect)

[量子计算“华山论剑”，中美竞争态势胶着](https://mp.weixin.qq.com/s?__biz=MzI2NDIzMjYyMA==&mid=2247528767&idx=1&sn=aef11ceacc2d8adb609a7cd2caae548e&scene=21#wechat_redirect)

[实用量子计算最具潜力候选者？中性原子阵列量子计算机前沿进展介绍 | 墨子沙龙](https://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247580291&idx=1&sn=6fe219609c9146b348eabdb5ec0c7d49&scene=21#wechat_redirect)

[谷歌量子计算机Willow做了什么？大多数媒体都没说到点子上 | 袁岚峰](https://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247581977&idx=1&sn=5384f921ba99186910efb97de88d2206&scene=21#wechat_redirect)

**■ 作者**

**袁岚峰**

中国科学技术大学科技传播系副主任

中国科学技术大学合肥微尺度物质科学国家研究中心副研究员

科技与战略风云学会会长

![](.evernote-content/8F69FEC9-50CA-49CF-B2D4-2364E4C30A8C/FAED8050-C6CA-4C5A-8447-02545C313D01.jpg)

**风云之声**

**科学 · 爱国 **· 价值****

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzI0NzQzMjU3Ng==&mid=2247582133&idx=1&sn=a35bd1190670a2baff534d66cfc780b3&chksm=e84575b7aa59d5636f873647509f34036365ea6dd6dd5418de6e0fde82180c0d44bffbb919fd&mpshare=1&scene=1&srcid=1225QbV6kG9p9KrQBLzurpU7&sharer_shareinfo=9ea35b7dff05c02fb26933c533a81030&sharer_shareinfo_first=9ea35b7dff05c02fb26933c533a81030#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9e629090-29f1-44ae-a85f-884f6f80f8e6/9e629090-29f1-44ae-a85f-884f6f80f8e6/)