---
title: 奏折 35：Keyboard Maestro 9 发布、Launch Center Pro 新增图标生成器、PDF Expert 转订阅
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/奏折 35：Keyboard Maestro 9 发布、Launch Center Pro 新增图标生成器、PDF Expert 转订阅.md
tags: [印象笔记]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "奏折 35：Keyboard Maestro 9 发布、Launch Center Pro 新增图标生成器、PDF Expert 转订阅"
source: evernote
type: note
export_date: 2026-06-26
guid: 8084cee3-c187-43c4-9b81-a8d4a91e442b
---

# 奏折 35：Keyboard Maestro 9 发布、Launch Center Pro 新增图标生成器、PDF Expert 转订阅

# 奏折 35：Keyboard Maestro 9 发布、Launch Center Pro 新增图标生成器、PDF Expert 转订阅

| 本文为付费栏目文章，您已订阅，可阅读全文 |

作为 Power+ 的常客，Keyboard Maestro 几乎是 macOS power user 人手必备的自动化工具。本周，Keyboard Maestro 发布了 9.0 新版，新增了深色模式、OCR 功能（支持中文）、JSON 解析等功能，是非常值得入手的一次升级。

另一位 Power+ 常客 Launch Center Pro 也发布了新版，加入了高度自定义的图标生成器，不仅能提供直观的视觉效果和满足个性化需求，还能配合快捷指令（Shortcuts）一起使用，生成好看的图标放到手机桌面。

此外，本周还有 PDF Expert 转订阅制、两款 Setapp 新应用、Apple 限制第三方电池维修、百度又卖了我们的个人信息、Apple Card 讨论等内容。

## ⭐️ 重点关注

### Keyboard Maestro 9：深色模式、自带 OCR 以及更多特性

![](attachments/da904318b23d9829.png)

**Keyboard Maestro 9**

[下载链接](https://www.keyboardmaestro.com/main/)

#### 应用简介

Keyboard Maestro 是一款 macOS 平台的通用型自动化工具，可以通过快捷键、文本输入、文件变化等触发条件，进行一系列的自动化操作。

相关介绍：[Keyboard Maestro 入门指南](https://sspai.com/post/36442)

#### 更新重点

**@Minja：**对于 macOS Power User 来说，这周最重磅的消息就是 Keyboard Maestro 9 的发布。Keyboard Maestro 是 Mac 上最知名的自动化工具之一，涵盖了快捷键、鼠标、手势、文件自动整理等多个场景，几乎可以实现任何进阶操作。

Keyboard Maestro 9 无论在外观上还是功能上都提供了诸多新特性，值得 macOS 自动化玩家们注意：

- 适配 Mojave 的深色模式
- 原生支持解析 JSON
- 原生支持 OCR 光学字符识别
- 支持 Stream Deck 串流
- 增加更多新的触发机关（Triggers）
- 增加更多新动作
- 增加更多新变量
- ……

这里挑其中最受关注的几个特性和大家分享。

最明显的变动当然是界面。此前 Keyboard Maestro 用户经常揶揄 Keyboard Maestro 的界面「古板」，看上去像是 OS X 时代的文物。第九代终于适配了**深色模式**，从编辑界面到交互窗口都一下子时髦起来。

![](attachments/f63c5473ec20b474.png)

编辑窗口和悬浮菜单的深色界面

在美观之外，Keyboard Maestro 9 也加入了实用的**多窗口编辑**，可以同时编辑多个不同的动作。例如需要同时编辑多个动作（比如从一处拷贝代码到另一处）时，多窗口就可以减少很多来回切换的操作，让编辑工作轻松不少。

![](attachments/c84206c4fe83bc48.png)

多窗口同时编辑

不过 Keyboard Maestro 9 内置的动作图标仍然充满了拟物风格，看上去还是和当前的 macOS 系统不搭调，希望以后的更新可以有所改动。

至于 Keyboard Maestro 9 新增的各项功能，其中热度最高的可能就是 **OCR**（最近官方转发的 Twitter 用户反馈中这一关键词出境率相当高）。Keyboard Maestro 官方在 Twitter 上 [透露](https://twitter.com/keyboardmaestro/status/1161402039332569088)，Keyboard Maestro 9 使用的 OCR 引擎是 Tesseract。这一引擎我们在《[如何在 Mac 上提取屏幕任意区域的文字](https://sspai.com/post/53321)》一文中已经接触过，其中文识别率比不上百度、腾讯等本土商用服务，但日常使用也已经足够，而且经过 Keyboard Maestro 的调教，不需任何额外设置就能实现**中英文混合识别**。

![](attachments/6f100d357eb45bf8.gif)

OCR 动作

上图所示就是我在 Keyboard Maestro 9 发布会制作的第一个动作，借用新的 OCR 操作实现了截图 OCR，有需要的读者可以在 [这里](https://github.com/BlackwinMin/Keyboard-Maestro-gallery/tree/master/OCR%20Screen%20Capture.kmmacros.zip) 下载。OCR 是一个很酷的功能，但 macOS 上多数具有 OCR 功能的工具，要么需要交钱，要么需要用户自己安装组件、配置语言文件，Keyboard Maestro 虽然不能说是一个傻瓜式的工具，但相比需要使用命令行安装的工具已经简化了太多，也不需要考虑「为什么识别不了中文」「为什么识别出来有空格」等等琐碎问题。

![](attachments/cd2369e2c16f883e.png)

OCR 支持多国语言

对于有更高折腾能力的读者来说，Keyboard Maestro 9 增加的拓展正则表达式、追加到变量、色值变量同样可以细细研究。在我看来，Keyboard Maestro 的价值就在于**把原本需要脚本的复杂操作简化了**，只需要拖动模块、调整少量参数，就能够组合出可用的小工具。在 Keyboard Maestro 8 时代，我尚有一大批需要用到脚本的动作，到了 Keyboard Maestro 9 中，其中不少动作都会有更简单的实现方式。

### Launch Center Pro 3.1：高度自定义的图标生成器，还可配合快捷指令使用

![](attachments/c505c15b5fe0c5e5.png)

**Launch Center Pro 3.1**

[下载链接](https://apps.apple.com/cn/app/launch-center-pro/id532016360)

#### 应用简介

Launch Center Pro 是 iOS 上的元老级自动化工具之一，主要用途是启动器，用于快捷启动应用，或者执行自动化操作。Launch Center Pro 曾推进了 URL Schemes 的发展，是 iOS 自动化历史上不可以忽略的一款应用。

#### 更新重点

**@文刀漢三：**图像相比文字，有更直观的视觉区分效果，当我们快速浏览元素时，图像也更容易引起我们的注意 1。Launch Center Pro 3.1 推出了新版的**图标生成器**，可以让我们高度自定义动作图标，这不仅能满足个性化需求，也能辅助我们更快速地定位动作。

![](attachments/3c69c537755e0fb2.jpg)

Launch Center Pro 3.1 的新版图标生成器（来源：Contrast）

新版图标生成器有**非常充足的图标数量**，据 Launch Center Pro 应用内的数据，有**超过 5000 个**可选图标，其中还包含了 Emoji，并且可以通过搜索名称来找到图标。

![](attachments/6c9e25e8e053f9a3.png)

超过 5000 个可选图标

新版图标生成器的另一个特点，就是**可自定义元素非常多**，我们可以调整图标的形状、风格、颜色、大小、角标、角标位置、边框等元素。

![](attachments/317d7c458de6a950.png)

可调整的图标元素

其中新增的角标功能我认为是实用性最高的，可以通过角标来区分每个动作的作用，同时让主图案保持同类动作的标志元素。比如，我有一组 Ulysses 的动作，分别是创建新文稿、查看收藏列表、查看过去七天列表。我让这三个动作的主图案都维持了 Ulysses 元素，角标则标识了它们各自的用途。

![](attachments/f184a7243d78eda8.png)

用角标来标识动作用途

关于角标，Launch Center Pro 官方还有一种比较推荐的用法，用来标识打电话、发短信、发邮件等动作。因为这类动作我们常常会用联系人的头像作为主图标，因此角标就能起到很好的辅助作用。

![](attachments/884a49b8fd1d6100.jpg)

用于区分打电话和发短信等动作（来源：David Barnard）

这么灵活的图标生成器，除了提供直观的视觉区分效果和满足个性化需求，还有一个重要的用途是**配合快捷指令（Shortcuts）使用**，这也是官方推荐的另一种用法。

快捷指令一直以来都能将动作添加到主屏幕上，用于快速启动。但快捷指令应用自身提供的图标数量实在少得可怜，好在，Launch Center Pro 生成的图标可以提供给快捷指令使用。只需点击图标生成器右上角的分享按钮，就能将图标导出成图片，用在快捷指令中。

![](attachments/fb6a55f89998581e.jpg)

导出 Launch Center Pro 图标

Launch Center Pro 还提供了透明、白色、黑色三种图标底色，如果你的手机桌面使用的是纯黑或纯白壁纸，就能借助它生成圆形图标放到桌面上。

![](attachments/5517209d15432864.jpg)

生成圆形图标放到桌面上（来源：David Barnard）

## 新鲜工具

### Setapp 新上架：Beepify

![](attachments/b75b2d91ece89cb6.jpg)

**Beepify**

[SetApp 链接](https://setapp.com/apps/beepify)

#### 应用简介

**@沨沄极客：**这是一款 Macbook 防盗 App，听上去是不是很新奇？它的原理很简单，当你需要在咖啡厅、图书馆等公共场所短时间离开时，打开 Beepify。如果在这期间电源线被拔或是屏幕被合上，Beepify 就会发出警报声，让周围的人注意到你的电脑。

与此同时还会通过 Telegram、Facebook Message 向你的手机发送警报，让你及时回去检查电脑。

![](attachments/a80da1ffdb440781.png)

Beepify Bot 和 Mac 端设置

[Beepify](https://setapp.com/apps/beepify) 原价 19.99 美元，现已上架 SetApp。

### Setapp 新上架：PocketCAS

![](attachments/5e09e8f4a4466b06.jpg)

**PocketCAS**

[SetApp 链接](https://setapp.com/apps/pocketcas)

#### 应用简介

**@沨沄极客：**这是一款数学计算器工具，它可以解决从小学到微积分、代数、统计等多种问题。不仅能计算各种等式、方程组、常微分，能够计算极限、导数、积分、泰勒展开式，还能完成 2D、3D 的绘图工作。是一款合格的计算器工具。

作为一款 Mac 应用，PocketCAS 支持数据导入导出、专用的数学键盘、通过 iCloud 同步计算文档。所有的功能都可以在内置的参考文档中找到说明。目前 [PocketCAS](https://setapp.com/apps/pocketcas) 已上架 SetApp。

![](attachments/75b9e91d95ace50c.png)

PocketCAS

### 必备：工信部公布最新政务公务类短号码

**@Fairyex：**我们国家拥有许许多多政府部门，当我们遇到各种不同问题的时候需要求助不同的部门。联系这些部门最直接的方法当然是拨打他们的官方电话。

这些电话都是由工信部（工业和信息化部）核发管理的，为了让人民和政府间有更方便的交流渠道，也为了更现代的国家治理体系，最近工信部微博 [@工信微报](http://weibo.com/5149608258/I1TEagGqV)分享了近 80 个政务公务类短号码，涵盖了普通民众能遇到的方方面面问题。

![](attachments/ac81b51cd9fc7b42.png)

政务公务类短号码列表

大家可以打开上面的微博链接保存图片，也可以下载我制作好的 [CSV 文件](https://github.com/fairyex/Gov__short_phone_number)方便查看查找，推荐每个朋友都保存一份这个列表，在需要用到时就方便多了。不管什么时候，官方渠道永远是最有效，最快速的解决方法。

### 头条搜索：字节跳动上线搜索引擎

**@Fairyex：**我们经常听见的今日头条、抖音等头部应用都属于名为字节跳动的互联网公司，最近它偷偷上线了自己的搜索引擎 —— [头条搜索](https://m.toutiao.com/search)。

要注意上面给出的官方地址是移动端地址，虽然头条搜索也有电脑端网页，但那个是今日头条的站内搜索，这个才是真正的搜索引擎。

![](attachments/da63ffc585b3b547.jpg)

头条搜索首页与搜索结果页截图

头条搜索使用起来与其他搜索引擎非常相似，但有一个很特殊的卖点，那就是能够搜索抖音视频、西瓜视频、火山视频等短视频平台上面的短视频（因为这些都是字节跳动旗下的平台）。这是其他搜索引擎目前做不到的，如果你需要搜索全网特定的短视频，那么使用头条搜索就非常方便。

![](attachments/9c05fea5b66178d7.jpg)

使用头条搜索短视频

## ⚙️ 常规更新

### PDF Expert 7：转变订阅制，但不影响老用户

![](attachments/91bc336d43acffd8.png)

**PDF Expert 7**

[下载链接](https://apps.apple.com/cn/app/pdf-expert-7-by-readdle/id743974925)

#### 应用简介

由 Readdle 公司出品，集阅读、标注、编辑、文件管理等功能为一身，是一款功能全面的老牌 iOS PDF 阅读器应用。可配合 Readdle 家的文件管理应用 Documents 使用。

#### 值得注意的更新内容

**@ElijahLee：**著名的 PDF Expert iOS 版推出了 7.0 版本，加了订阅制让很多不明真相的群众「闻风丧胆」，纷纷发问寻找替代品。但实际上订阅制并不是过街老鼠，而且发展到现在，订阅制已经有很多种模式，PDF Expert 采用的是对用户最友好的方式。

首先，**所有 PDF Expert 6 的用户都可以继续使用之前的功能，不需要订阅**。看到这里我相信很多老用户就放心了，之前付费享受的功能还是可以继续使用，并**终身**可用。

Readdle 团队详细列示了 PDF Expert 7 各功能给新老用户的权限。如果你是已经内购的老用户，升级了之后发现「编辑 PDF」等功能无法使用，可以尝试「恢复购买」。

![](attachments/c686d578f57b6741.png)

PDF Expert 7 各功能给新老用户的权限

变为订阅制之后，PDF Expert 7 可以免费下载。订阅费用为 353 元 / 年，可以 7 天免费试用。个人而言，就目前这个时间点，这一订阅费用**对于已经内购的老用户**来说是偏高的，Pro 中的转换文档、压缩和自定义工具栏的作用可能有限。当然开发团队还表示未来会加入 OCR 识别、手写识别和扫描文档，老用户不妨在以后功能更加全面之后再按需订阅。

说完订阅制，我们来看看新版的变化。PDF Expert 7 一个明显的变化是设计了**全新的界面**。极简设计让应用看起来非常舒服，我个人比较喜欢这种白色界面。在 PDF 里标注、绘制等功能的图标也有重新设计，更加精致好看。

![](attachments/e4be3fbd826e3fb0.png)

PDF Expert 7 新设计

此外，PDF Expert 7 还新增了三项新功能：

1. **转换文档为 PDF：**可以把 Word、Excel 和 Pages 等文档转换为 PDF，而不需要跳转到相应的 App 中去。
2. **压缩 PDF：**可用于压缩 PDF 体积。
3. **自定义工具栏：**指的是把一些常用工具添加为收藏，而不需要在频繁更换工具时在不同类别里来回切换。

就我个人而言，PDF Expert 7 的推出并没有影响我使用 PDF Expert 看文档、标注和编辑的用途。之前内购解锁的功能已经完全够用，新推出的功能以及后续功能还有待观望。对于新用户，现在 iOS 版的 PDF 工具也有很多可以选择。PDF Expert 7、Adobe Acrobat、PDF Element 都可以尝试，根据自己实际需要选择最佳方案。

### Google 网页新增播客搜索功能，并且可搜到谈话内容

**@文刀漢三：**最近，Google 上线了播客搜索功能，可以通过关键词 `podcast 搜索内容` 搜到播客单集，并且点击后可**直接在网页播放**和**查看 show notes 信息**。

![](attachments/0fc84733524ba1b6.jpg)

搜索与苹果副总裁 Craig Federighi 相关的播客

根据 9to5Google 的[报道](https://9to5google.com/2019/08/08/google-podcast-search/)，Google 的播客搜索不仅能搜到播客标题和 show notes，还能借助 Google 的语音转录技术，搜到播客里的谈话内容。这无疑极大增强了播客这种基于音频内容的**可发现性**，以及**检索能力**。

## 观点 & 新闻

### Apple 将限制第三方电池维修

**@Minja：**手机使用了一两年后，如果没有其他毛病，换块电池继续用 —— 而且往往是街边找个实惠的维修点 —— 估计是不少人的选择。不过有人通过 [实验](https://www.vice.com/en_us/article/59nz3k/apple-is-locking-batteries-to-specific-iphones-a-nightmare-for-diy-repair) 发现，苹果会禁用非官方维修过的电池的部分功能，比如电池健康中的「最大容量」和「峰值性能容量」。iFixit 的 [实验](https://www.macrumors.com/2019/08/14/apple-responds-to-battery-locking-issue/) 也证实了相同的问题。即便使用原装电池，只要维修行为不是苹果进行或授权的，更换后的电池照样无法正确识别。某种程度上说，苹果的这一行为将限制第三方电池维修。

![](attachments/66663a78f366c4ce.jpg)

维修过的电池无法使用部分电池功能 图 / JUSTIN ASHFORD

随后（8 月 15 日），苹果在接受 The Verge 的 [采访](https://www.theverge.com/2019/8/14/20805744/apple-iphone-battery-replacements-ios-safety-statement-unauthorized) 时称，对于非官方电池的限制是为了保护客户安全。不过不满的声音并未就此消失。

多数人选择第三方维修服务往往是为了更低的价格。以 iPhone XS 为例，过保的机器需要支付 **513 元**才能 [在官方得到维修](https://support.apple.com/zh-cn/iphone/repair/service/pricing)，而去淘宝上换电池只需要**不到 200 元**。一般来说，电池容量下降到需要更换时，官方保修基本也已经过期，前往第三方维修并不会让我们损失保修机会，反而可以省下可观的一笔钱；而且去第三方也不需要预约，甚至可以享受「立等可取」的快捷服务。在保修到期的前提下，第三方维修在**价格**、**速度**上的优势显而易见。

Tim Cook 在上半年就 [宣称](https://www.vice.com/en_us/article/zmd9a5/tim-cook-to-investors-people-bought-fewer-new-iphones-because-they-repaired-their-old-ones) iPhone 销量下降的部分原因是用户选择维修旧机型，结合这次的电池功能禁用事件，很难不让人产生联想。一些花上一百块钱修修就能继续用的旧机器，偏偏要花几百块才能去官方更换电池 —— 而且屏幕稍有裂痕的话，根据保修条例必须先掏钱修完屏幕才给换电池 —— 在动辄几百上千的维修成本面前，相信会有人干脆购买新机。因为维修价格高昂而失去选择空间，正是我们不愉快的原因。

苹果在过去拒绝为经第三方维修过的机器提供保修，这已经是对于非官方维修的严格限制；这次再禁用部分电池相关功能，则是连同本就失去保修的机器一并限制，让用户的选择权变得更加无力。

### 新华社探秘骚扰电话产业链

**@Fairyex：**我写过一篇名为《[如何防范 3・15 晚会上曝光的人工智能骚扰电话？](https://sspai.com/post/53346)》的科普文章，从原理和流程讲述了骚扰电话产业如何利用科技的力量让骚扰电话的效率与杀伤力指数级提升。最近新华社记者也通过「卧底」骚扰电话源头企业发现了更多的新内幕。

在这篇新华社的《[记者 “卧底” 骚扰电话源头企业，内幕触目惊心](http://www.xinhuanet.com/local/2019-08/07/c_1124849387.htm)》报道中，我们能了解到骚扰电话是如何通过团队分工实现高效率；不同等级「首咨」（未被骚扰过的用户）和「公海」（被骚扰但没有成功的用户）两大类个人信息又是如何分配；如何给目标用户分类标记，并针对不同用户使用不同话术。

最重要的是报道还揭露，到底我们的个人信息都是被谁卖了。这部分当然少不了我们的老朋友百度公司，一条个人信息的进价只需要 100–150 元，还可以实现有新个人信息自动推送到客户。

![](attachments/eea1e24cd26bcd7c.png)

互联网公司是重要的泄露源头

文章地址：[记者 “卧底” 骚扰电话源头企业，内幕触目惊心](http://www.xinhuanet.com/local/2019-08/07/c_1124849387.htm)

## 推荐

### Apple Card 讨论：文章推荐 & 反方观点

**@沨沄极客：**苹果在上周开始逐渐放出 Apple Card 的注册权限，外媒 MacRumors 拿到了一张 Apple Card 并发布了一篇与 Apple Card 有关的详细指南：《[Apple Card: All the Details on Apple’s Credit Card](https://www.macrumors.com/guide/apple-card/)》，在这篇文章中，他们透露了许多关于 Apple Card 的细节，比如卡片的材质是钛金属，名字是激光蚀刻上去的，正反面没有卡号和 CVV 号。也给出了上手指南，包括它的奖励制度、信用额度、每日现金等功能。如果你正在国外并想获得一张 Apple Card，这篇文章会给出很多有用的信息。

如果身处国内无法注册，这篇文章中也放出了一个在线小工具供大家娱乐。可以生成一张带有自己名字的 Apple Card 预览图片。

![](attachments/b5cad7673702b2f2.png)

在 MacRumors 生成的 Apple Card 预览

当然，Apple Card 也并非是所有人都给出了好评。外媒 MacWorld 就发表了这样一篇观点文章：《[The Apple Card is not magic](https://www.macworld.com/article/3431637/the-apple-card-is-not-magic.html)》，表示 Apple Card 并不神奇，卡片本身并不具有革命性 ——「它只是另一张 MasterCard」。文章也指出 Apple Card 的软件支持是其他银行所不能比的，但它的数据仍然无法导出到其他应用。最后的观点是苹果并不想打破现有的信用卡市场，而是希望从信用卡市场中获得利润。

![](attachments/f09e3fd3469f1b06.jpg)

Apple Card / 来源 MacWorld

相关链接：

### 查看往期 App Store 推荐：AppFollow

[网址](https://appfollow.io/cn/featured/apps#country=cn&date=2019-08-11)

**@Minja：**常逛 App Store 的读者大多知道，应用商店每日会推出精选榜单和专题推荐。Power+ 在写文章时，也会把 App Store 的这些官方数据列为参考之一。不过 App Store 只会显示最近几期榜单，早先的数据除非提前收藏链接，不然就很难找到。

最近发现一个查看 App Store 往期榜单数据的好去处：**AppFollow**。

![](attachments/a16f7afd90bc6ca4.png)

AppFollow

AppFollow 是一个监控各大应用市场数据变动的服务（我也是通过应用开发者 @im61 知道 AppFollow 的），App Store 榜单历史记录就是其众多功能之一。AppFollow 允许通过日期和地区两种条件查找往期榜单，当然也包含了中国区 App Store 的数据。

![](attachments/d924a9c6c9ef8c8d.png)

日期和地区两种筛选条件

AppFollow 上的 App Store 榜单**无需注册、也不用付费**就能查看，对于写作者和开发者来说都是一个有价值的数据来源。

### 苹果推出 ASMR 系列视频

**@Fairyex：**自发性知觉高潮反应（英语：Autonomous sensory meridian response，缩写 ASMR），也称自发性知觉经络反应，是一种对于视觉、听觉、触觉、嗅觉等其他知觉，颅内、头皮、后背以及四肢等周边部位受到刺激而产生愉悦反应的感知现象，例如头颈部皮肤酥痒、起鸡皮疙瘩等反应，甚至能产生「颅内高潮」，**没试过的朋友可以带上耳机后，点开下面的演示影片感受一下**。

ASMR 演示视频（来源：维基百科 ASMR 词条）

不知道什么原因，苹果突然在它的 YouTube 频道上发布了四个 ASMR 类型的[视频](https://www.youtube.com/user/Apple/videos)（还用 Logo 替换了「A」）。

![](attachments/55edaca31cfc76a6.png)

视频列表

四个视频包含了不同的流行 ASMR 类型，包括窃窃私语、自然声音、木工声音、行走在不同道路上的脚步噪音等。建议感觉心情紧张的时候观看，极高的音质配上清晰的画面，让人能不由自主放松下来。

视频地址：[YouTube](https://www.youtube.com/user/Apple/videos)

### 书单推荐：谷歌设计师在读什么书？

[网站](https://www.fastcompany.com/90385380/google-has-a-secret-design-library-here-are-35-of-its-best-titles)

**@Minja：**大家常常调侃，Apple 的设计师是艺术家，Microsoft 的设计师是工程师。那么 Google，它的设计师则是一群神秘的 Geek。你可能也好奇过，这群创造出 Google Home 布艺拼接设计、也搞出过 Pixel 3 XL 「门牙」刘海的家伙，平时都在干什么？

Google 设计实验室领导者 Ivy Ross 最近公开的一份书单，可以帮你一窥这个神奇团队的侧面。设计实验室中的书籍都是设计师们推荐的，这份书单精选了其中的 35 本。不出意外，书单中有《设计心理学》《谁动了我的奶酪》等设计、商业类的经典畅销书；但是继续看下去，多数书籍对普通读者来说就比较陌生（很多甚至没有中译本）。虽说是设计师们推荐的书，单子上却不全是设计类书籍，还有不少哲学、社会相关的书，甚至**史奴比**和**丁丁历险记**漫画也有上榜，可见这群设计师的兴趣很是广阔（其实 Google Home 的布艺设计就源自北欧家具，也算是一个从不同领域汲取灵感的例子）。

[这里](https://www.topys.cn/article/29244.html) 有一份 TOPYS 节选、翻译的中文书目，有能力的读者也可以看看完整版 [英文书单](https://www.fastcompany.com/90385380/google-has-a-secret-design-library-here-are-35-of-its-best-titles)。

Measure

Measure


---

[🌐 原始链接](https://sspai.com/post/56241)
[📎 在印象笔记中打开](evernote:///view/207087/s1/8084cee3-c187-43c4-9b81-a8d4a91e442b/8084cee3-c187-43c4-9b81-a8d4a91e442b/)
