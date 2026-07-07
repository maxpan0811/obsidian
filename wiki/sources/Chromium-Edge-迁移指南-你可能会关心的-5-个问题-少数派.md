---
title: Chromium Edge 迁移指南：你可能会关心的 5 个问题 - 少数派
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/Chromium Edge 迁移指南：你可能会关心的 5 个问题 - 少数派.md
tags: [印象笔记]
updated: 2026-06-27
---

---
title: "Chromium Edge 迁移指南：你可能会关心的 5 个问题 - 少数派"
source: evernote
type: note
export_date: 2026-06-26
guid: ba8436c6-5917-406c-b70c-cfc2a854cc79
---

# Chromium Edge 迁移指南：你可能会关心的 5 个问题 - 少数派

# Chromium Edge 迁移指南：你可能会关心的 5 个问题

![](attachments/d6b861959d542fd9.png)

Chromium Edge 迁移指南：你可能会关心的 5 个问题

按照微软提供的 Edge 产品路线图，2020 年 1 月 15 日基于 Chromium 内核的稳定版 Edge 就将正式推出。此前我们已经介绍过提前「偷跑」的 Chromium Edge 稳定版的一些功能特色，但浏览器作为很多人日常使用频率最高的桌面应用之一，相比其他应用往往有着较高的用户粘性。因此很多人在新版 Edge 面前都会有些摇摆：迁移到 Chromium Edge 究竟有没有门槛，有哪些事情是切换浏览器过程中值得关心和需要注意的？

这篇文章就从安装与卸载、浏览器数据转移、扩展使用的注意事项、跨平台同步以及性能表现 5 个方面，为你带来最全面的 Chromium Edge 迁移指南。

**关联阅读：**[Windows 10 默认浏览器新选择：基于 Chromium 内核的 Edge 推出稳定版](https://sspai.com/post/57151)

## 安装和卸载

正如我们在上一篇文章中所介绍的那样，目前稳定通道基于 Chromium Edge 其实已经可以下载并正常安装，微软表示目前的稳定版本属于候选版本，功能基本稳定但并非最终版本。

而目前除了已经偷跑的稳定通道版本之外，考虑到需要一个逐渐熟悉以及适应的过程，微软在公布迁移计划的同时也正式上线了 Microsoft Edge Insider 网站，并且和 Chrome 版本发布类似，也提供了包括 Canary 渠道版本、Dev 渠道版本以及 Beta 渠道版本，而在现阶段，如果你希望在体验新版 Edge 的同时并保留旧版本 Edge，那么选择 Beta 渠道版本最为合适，且不会「替换」旧版本 Edge 浏览器。

![](attachments/5e8aedb50a0a379b.png)

安装过程

虽然早先偷跑的稳定版在安装后会完全覆盖掉 Windows 10 默认的 Edge 浏览器且无法回滚，但在之后候选版本更新中，微软已经加入了卸载选项。换句话说，如果你尝鲜体验了稳定版 Chromium Edge 后想要回到原版 Edge 浏览器，可以通过控制面板中的「程序和功能」将其卸载，卸载后即可还原成旧版 Edge。

事实上，安装基于 Chromium 内核的 Edge 并不会删除旧版 Edge 浏览器，之前的 Edge 浏览器只是被系统给隐藏了。

![](attachments/6dcde34664e88522.png)

## 哪些数据可以迁移

作为高频使用的桌面应用之一，切换浏览器同时也意味着使用习惯的迁移。在体验近似的前提下，平滑的数据迁移流程能够将浏览器平台切换带来的适应难度降至最低。

安装完成初次启动 Chromium Edge 后，设置向导专门提供了一个用于浏览器数据迁移的步骤，比如我此前的浏览器是 Chrome，那么设置向导就会提示是否要将其数据导入到 Edge 中。

![](attachments/63afa5db37dbf7d0.png)

数据迁移

下方的「更多设置选项」则详细说明了将会迁移哪些数据，包括**书签、保存的密码、地址信息、支付信息、浏览器历史、设置和打开的选项卡**，其中最为重要的应该就是「书签」了。值得注意的是「保存的密码」和「浏览器历史」都仅能将保存到本地的信息导入进来，如果你此前在多个平台上使用 Chrome，则是没办法将云端保存的数据同步过来的，所以在进行向 Chromium Edge 的数据迁移前，建议先在其它浏览器中将所有云端数据同步至本地。

![](attachments/905d69d1c7138a20.png)

不出意外，本机浏览器的大部分数据都可以全部导入 Edge 浏览器中，而这只是将原本使用习惯平滑迁移的第一步。

## 你的扩展怎么办

Chrome 强大并不是其本身功能丰富，而是其丰富的扩展将各种软件服务连接到了一起，而这也是微软最终选择转换 Edge 浏览器内核的原因，比起闭塞的旧版 Edge，基于 Chromium 的 Edge 的扩展和 Chrome 无缝兼容。

这也为我们浏览器使用习惯平滑迁移的第二步打下坚实基础。

当然，即便是内核已经完成迁移，微软还是为 Chromium 的 Edge 准备了官方的扩展应用商店，一些我们经常使用的扩展可以从中找到，比如说屏蔽网页广告的 ABP、印象笔记・剪藏以及密码管理工具 LastPass 等都已经列入其中，安装过程和在 Chrome 中安装扩展几乎一样。

![](attachments/6016ae415d2809c2.png)

不过或许是刚刚起步的原因，微软的 Edge 官方扩展商店中的扩展还是偏少，Chrome 中绝大多数的扩展都没有在此上架，因此通过 Chrome 商店安装扩展是个不错的选择，Edge 也提供了对应的选项：只需要在「扩展」中勾选上「允许来自其他应用商店的扩展」，然后打开 [Chrome 扩展商店](https://chrome.google.com/webstore/category/extensions?h1=zh) 就可以直接安装扩展了。

![](attachments/f8b310a2fe76a489.png)

对应的，你会在 Edge 的「已安装的扩展」中看到一个是来自 Microsoft Store 的扩展，而从 Chrome 网上应用商店安装的则被称之「来自其他源」。借助这样的组合安装方式，我将自己的 Chrome 扩展完整迁移了过来。

![](attachments/c3c01e5e9a32fdea.png)

还有个使用场景是离线安装扩展，如果你恰好有一个.crx 的扩展安装包，那么安装这个扩展方法其实和 Chrome 离线扩展安装方式差不多，首先在「扩展」中勾选「开发人员模式」。

![](attachments/46850956b9bb2804.png)

将.crx 的扩展用 7zip 等软件解压缩，之后在「扩展」中选择「加载解压缩的扩展」，选择之前解压缩的文件夹即可，这样离线的扩展就可以正常安装上了。

## 跨平台数据同步

相比此前 Edge 几乎半残的同步系统，采用 Chromium 内核的 Edge 真正引入了账户系统，并且得益于 Windows 10 的平台优势，新版 Edge 的账户系统和 Microsoft ID 高度整合。

也就是说，如果你有多台 Windows 10 设备，那么你的新版 Edge 的数据也会相互同步，就像是你在多个平台上使用 Chrome 浏览器一样。

**和 Chrome 相比，目前 Edge 浏览器可以同步的数据选项并不多。**在「设置 > 个人资料 > 同步」中，你可以看到目前可以同步的类别：收藏夹（书签）、浏览器设置、地址联系人信息以及密码，相比 Chrome 少了**扩展同步**以及**云历史记录**等同步信息，所以如果你有多台设备上运行了新版的 Edge 浏览器，那么你的扩展设置在现阶段必须手动进行二次设置。

![](attachments/67fddf4241ada398.png)

而如果有设备运行旧版的 Edge 浏览器，那么新版的 Edge 浏览器的数据是否会相互同步呢？我的试验结果是「No」，**或许因为两者同步系统现阶段完全独立，旧版的 Edge 浏览器的数据并不能互相同步**。

![](attachments/4c2d54133bbefab6.png)

而这一点差别也反映在了移动版 edge 浏览器上，和 Chrome 的跨平台浏览器方案相同的是，Edge 同样也提供了 iOS 以及 Android 版本，并且同样在 Android 上提供了 Chromium 内核版本，iOS 上提供的是「壳浏览器」。在同步数据方面则提供了两种数据源选项，一个是原来旧款 edge 浏览器的数据源，而要想将采用新内核的 edge 浏览器的数据同步到移动端，则需要在移动端的「同步设置」中选择「同步到 Microsoft Edge Insider」，并且微软也在说明中说明了两者的区别。

## 性能表现怎么样

从理论上来说，既然新版 Edge 浏览器采用了 Chromium 内核，那么基础性能乃至网站的兼容性将和 Chrome 无差。但真理总是实践出来的，为了消除大家的疑虑，我们来做一次 Chrome 浏览器和新版 Edge 浏览器的基准测试。

为了保证公平性，我模拟了我日常使用浏览器的习惯，在 Chrome 和 新版 Edge 上均安装了相同的扩展，均关闭「关闭浏览器后再后台运行」功能且开启了「硬件加速」。

- Google Chrome ：稳定通道，版本号： 78.0.3904.97 （64 位）

- Microsoft Edge：稳定通道（候选版本），版本号： 79.0.309.18 （64 位）

测试平台：Surface Laptop（i5 处理器），操作系统：Windows 10 专业版 v1909

测试项目： Kraken、JetStream、MotionMark、Speedometer、Basemark 3.0、WebXPRT

最终测试结果如下。

**Kraken ：**测试项目用来测试浏览器的 JavaScript 性能，得分为时间单位**，越小越好**

![](attachments/b5b5cb317b2a2140.png)

**Browserbench 系列测试：**该系列测试主要针对图形渲染、JavaScript 测试、循环 Dom 等进行压力测试**，得分越高越好**

![](attachments/d24c4036a716d880.png)

**Basemark 3.0 ：**该测试主要用来测试一些新的浏览器技术**，分数越高越好**

![](attachments/41e3d86a094de24e.png)

**WebXPRT：**该测试模拟一些浏览器日常使用操作，主要测试 html5 和 JavaScript 性能**，最终得分越高越好。**

![](attachments/04d3fbbbf7f87f84.png)

通过以上评分不难看出，两者实际上的跑分差距并不大。换言之，如果你将 Chrome 迁移到新内核 Edge 浏览器，那么无论是性能、兼容性还是使用习惯上并无大的影响。

## 结语

微软选择更换 Edge 浏览器的内核并采用和 Chrome 相同的 Chromium 内核，无论其背后的寓意和象征如何，最终我们还是需要去使用他。在此之前如果你依然纠结要不要从其它浏览器进行迁移，希望这篇解答文可以帮助你更好地进行选择。

你可以在 Chromium Edge [官方网站](https://www.microsoftedgeinsider.com/en-us/download/) 下载到它的各种版本，早前「偷跑」的稳定版依然需要通过搜索引擎搜索 [相关页面](https://go.microsoft.com/fwlink/?linkid=2069324&Channel=Stable&language=en) 后跳转下载。

**关联阅读：**

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure
