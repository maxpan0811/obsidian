# 终极指南 - 怎样为iOS8应用制作预览视频 | Be For Web - 为网而生

---

[**Be**For Web](http://beforweb.com/ "首页") 为网而生 - 原创译文博客 - 关注移动应用及互联网产品、用户体验设计、前端开发
===================================================================================

* [**产品**product](http://beforweb.com/product)
* [**设计**design](http://beforweb.com/design)
* [**前端**front end](http://beforweb.com/front-end)

**终极指南 - 怎样为iOS8应用制作预览视频**

终极指南 - 怎样为iOS8应用制作预览视频
----------------------

C7210 发表于 2014-10-26 14:57

过去整整一周多的时间，每天到处是刺眼的阳光。天气也真是任性的很，我仍记得今年年初每天期盼出太阳的日子，而如今倒是期望一切不要都这么明晃晃的了。

上海的秋冬季节气候无常，但往往是不正常的热到一个峰值，然后温度一夜之间下降个10度左右，且伴有大风；接下来温度又一点点上升起来；如此往复，不亦乐乎。

文绉绉的呢。其实在看西游记。孙悟空被骗当了弼马温，还跟玉帝说“多谢了”。

说正经的吧；本周译文相当之推荐，关于iOS 8应用预览视频的话题，从设计、技术规范，到录屏、编辑工具，介绍的都比较详尽；建议收藏，在接下来用的到的时候作以参考。下面进入译文。

最近一两个月里，苹果的世界里出现了很多新东西，比如屏幕更大的iPhone 6，可穿戴设备Apple Watch，iOS8，以及旨在帮助用户更好的发现应用的App Store改版等等。

说到App Store的改版，最值得设计师、开发者和市场人员关注的大概就是视频预览功能了。官方将其称为“应用预览(App Previews)”，如今已经正式出现在iOS8的App Store当中。自然，已经有一大波设计师和开发者为他们的产品制作了预览视频并通过iTunes Connect上传。坦率的说，如果你也有自己的产品，那么也该开始考虑做这件事了。

### 来自官方的设计制作规范

与截屏图片一样，苹果针对应用预览视频提供了一些[官方的设计制作规范](https://developer.apple.com/app-store/app-previews/)。视频在上传之后同样需要接受苹果的审核，这就意味着如果你在预览视频方面破坏了规则，一样会被拒掉，所以建议你首先仔细阅读一下官方的规范。

### 技术规范

当前，我们可以为每个应用上传两段预览视频，其中一段用于iPhone，一段用于iPad。

从技术角度讲，你需要遵守以下这些规范：

* 长度在15至30秒之间
* 通过H.264 MPEG或ProRess 422(HQ)压缩
* 每秒30帧(30p)
* 最终文件不超过100MB
* 扩展名可以是.mov、.mp4或.m4v

分辨率规格如下（单位为像素）：

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/05C960ED-F5C7-4F76-99F4-FD50F0301531.png)](http://beforweb.com/sites/default/files/images/201410-3/01-ios-8-app-store-preview-video-design-development-guideline.png)

此外，上传视频需要基于以下平台及软件：

* 安装了OS X Yosemite的iMac或MacBook
* Safari浏览器

### 设计规范

规范当中的一些内容不大容易解释，因为它们更像是“建议”，而非“规则”。不过要记住，苹果官方会将这些“建议”作为评估的基础；遵守这些规范将能帮你避免遇到那些不必要的麻烦。

设计规范内容较多，我们不妨先来看下概要：

* 聚焦在最重要的三个卖点上
* 通过录屏演示产品体验
* 演示操作时不要让手挡住界面
* 不要通过编辑视频来造假
* 内容至少要适合4岁以上的人群
* 不要使用你不拥有版权的素材
* 不要依赖于文字介绍
* 瞄准目标用户群体及其语种
* 视频中不要涉及价格及运营商信息
* 不要使用有可能“过期”的内容或素材
* 从应用中录制实际音效
* 使用高品质的背景音乐及画外音
* 选择一张合适的封面

#### 聚焦在最重要的三个卖点上

当然，你不必严格按照字面上的意思强行挑出三个卖点进行演示；重点在于不要试图在30秒的视频中面面俱到，因为用户根本没法理解和记住那么多东西。

另一方面，虽然苹果允许你直接使用30秒的实际操作视频，但也不要将这30秒全部用来演示某一个功能流程，因为这会很无聊，而且可能使用户错过其他一些重要的东西。

用户通常会因为对产品当中一到三个卖点的关注而下载你的应用。卖点在设计上？或是某种新技术？还是对传统界面模式的优化改良？挑出那些最吸引人的亮点，在一段简单的蒙太奇当中展示出来；要做好这件事，你真的不需要拥有多么专业的视频制作能力。

此外，你并不一定需要去展示产品logo，应用图标，或是“Download on the App Store”标识。如果真的有必要，也尽量试着做出一些风格，例如通过某种形式的动画来展示logo和图标，给用户留下更积极的印象，强化品牌识别效应。甚至有[公司](http://animatid.com/)是专门提供这方面服务的。

#### 通过录屏演示产品体验

苹果真心不希望演示视频看上去像赤裸裸的广告。他们希望让你通过应用自身来更加“诚实”的进行展示。使用实际应用录屏，而不是展示人们拿着手机操作的样子，或是你从手机主屏一路点击进入应用的过程。

对于游戏来说，有取巧的可能，例如只放一些过场动画。苹果同样知道这一点，他们建议你还是尽量放些游戏进行过程中的录屏。

#### 演示操作时不要让手挡住界面

听上去很容易？但对于开发者来说，和苹果打交道就没有什么容易的事。演示视频中的应用界面不要被操作者的手指挡住，尽量通过前面说的录屏来演示；如果确实要展示交互方式，可以在录屏中加入视觉提示元素，例如通过逐渐淡出的圆环代表触摸点。

#### 不要通过编辑视频来造假

这是很严肃的事。不要通过欺骗的手段让人们觉得你的应用比实际的好。除了道德因素以外，这种手段更会为你的产品带来相当负面的评价，一星就是用户用来发泄愤慨的手段。

还要记得按照应用的实际分辨率来显示内容，不要放大。此外，不要把转场效果剪切的让用户误以为实际应用当中有这样的效果。

#### 内容至少要适合4岁以上的人群

任何人都可以访问App Store。我曾经见过3岁的小孩在iPad上通过各种复杂的手势操作应用，熟练的仿佛他在他妈的肚子里就已经开始使用这设备了一样。一旦了解有这种事情存在，你便知道为什么苹果会担心内容的适用人群了。

引用官方的话讲，你应该避免“令人反感的内容，暴力或成人主题，以及脏话。”

#### 不要使用你不拥有版权的素材

我猜这很容易理解。无论是在App Store还是其他地方，尊重版权和商标都是必须的。不要在视频中使用你不拥有版权的音乐、视频、商标、形象、人物形象等等。因为这方面的问题被App Store拒掉可是很蠢的。

苹果官方举了个例子：“如果你的应用可以访问iTunes Library，那么你只能在预览视频中使用自己创作的或是拥有特定授权的音乐。”

#### 不要依赖于文字介绍

至少目前，应用预览视频还不支持本地化，同一个视频会被全球的用户访问到。如果必须阅读视频中的文字才能了解产品功能，那么你就把全世界非英语用户挡在了门外。

如果一定要使用文字介绍，也要注意几点。世界上说英语的人不少。除非你的产品锁定在某个特定的国家或语种上，否则还是用英语的好。保持介绍文字的简短、易理解；因为文字是出现视频当中的，所以还要注意可读性，并确保其出现的时间足够长。

#### 瞄准目标用户群体及其语种

也许你的产品是一款游戏，在全球都有玩家，但最大的玩家群体在中国，而且其中多数是女性。如果这是你要瞄准的目标用户群，那么要对他们所习惯的广告形式及喜爱的功能进行研究，然后制作一段最能为中国女性玩家所接受的预览视频。

#### 视频中不要涉及价格及运营商信息

苹果希望你通过功能，而不是价格，来吸引用户下载应用。坦诚的说，在如今的App Store当中，单纯的免费或低价策略未必能带来多少关注，因为90%的下载都是集中在免费应用上的。况且，用户在你应用图标的下方就能直接看到价格信息，没必要在视频中累述。

你唯一有可能需要在视频中展示价格信息的地方就是关于应用内购买的描述；可以试着在视频中的免责声明部分或是结尾展示这些信息。此外，苹果建议对于包含订阅或账户登录功能的情况也要进行类似的处理。

如果不明确的展示这类信息又会怎样？无非是产品有可能被苹果拒掉。即使通过了审核，也很可能导致用户的差评。这些结果显然都不是你希望看到的。

不过，如果你家应用里有圣诞大促的话又当如何展示呢？其实多数用户不会因为你家宝贝有五折优惠就下载应用。说到这一点...

#### 不要使用有可能“过期”的内容或素材

制作优秀的预览视频是要花不少时间(和钱)的。那么，为什么要给它加上有效期呢？每个人都喜爱圣诞节，但仅限于12月份。如果某些用户在转年2月发现了你的应用，看到了一段圣诞主题的视频，那会有点荒唐吧？不仅如此，这会使用户认为你已经好几个月没有更新产品了。

除非你确定自己会在有特定意义的日期之后很快更新应用及视频，否则不要使用任何有可能过期的内容或素材。当然，如果你的应用本身就是关于圣诞或其他节日主题的，那例外。

#### 从应用中录制实际音效

正如前面所说，要避免在视频中通过手指操作来演示产品的交互特性，而要使用录屏。不过仅凭视觉上的呈现，也许会略显单薄。因此，操作过程中的实际音效对于演示交互反馈特性就变得更加重要了。

#### 使用高品质的背景音乐及画外音

虽说不是必需，但要找到一个合适的人来帮你做些简短的画外音解说，这也不是很困难的事。不过和前面提到的文字介绍性质相同，不要过分依赖于解说。当然有一点需要承认，如果做的够好，那么画外音可以给用户带来非常不错的第一印象。

你也可以自己做这件事，不过要在能够尽量隔绝噪音的地方使用高品质设备进行录制，而不是那种5美元的小麦克风。除非你在录音方面的确内行，否则还是建议你自己写好脚本然后交由外包。记得不要把画外音的风格搞得太像电视广告。

无论是否使用画外音进行解说，背景音乐总是你需要考虑的。如果你有原创的或是经过授权的歌曲，不妨一用。使用音乐配合视频，可以为产品奠定一种基调，让用户在下载前就对大致的体验风格有所感知。对于解说和音乐，要进行充分的效果测试，确保音质如水晶般清澈。

如果你不拥有原创音乐，那么在选择授权音乐的时候一定要考虑到风格是否适宜自己的产品。毕竟，哪怕拥有版权，[System of a Down乐队的“B.Y.O.B.”](http://www.xiami.com/song/2030077)也无法适用于小清新风格的购物应用。

#### 选择一张合适的封面

前文都是聚焦在视频本身上面，我们还忘记了一个小细节：视频不会自动播放，用户需要点击封面才可以观看。所以我们要确保他们有愿望去点击封面才是。

我们可以把这张图片称作封面，也可以叫做海报。它应当来自于视频当中，看上去就像带有一个播放按钮的截屏图片。

上传视频时，iTunes Connect会从视频里自动挑选一帧作为默认的封面，但你也可以自主选择。别忘了做这件事，它对于转化率的提升将起到重要的作用。如果你真的忘记了，而应用已经通过了审核，那么要做好准备重新上传一个新包，哪怕只是为了更换一张封面。

### 制作预览视频

看过上面所有这些技术与设计规范，是时候动手制作自己的预览视频了。

关于制作方式，苹果官方有做推荐，同时你也有很多其他选择。接下来，我会向各位展示我所探索到的所有的可行方法。无论是个人开发者，还是公司团体，都该试着为自己的产品制作预览视频。继续往下读吧，看看哪种制作方式最符合你们在时间及预算方面的具体情况。

### 预算较低

独立开发者和小工作室不该错过这场派对。你可能需要花些时间来学习相关的制作软件，但最终仍然可以凭借自己的力量制作出优秀的应用预览视频。

#### 使用苹果自家的软件录制屏幕

这大概是制作录屏的最简单的方法了。OS X Yosemite预置了一项全新的设备录制功能，目的就是帮助广大设计师和开发者制作应用预览视频。此外，你需要带有Lighting接口和Retina屏的iOS设备，系统是iOS 8；iPhone 5及之后的iPhone都可以满足条件。

下面是来自苹果官方的操作指南：

1. 使用Lighting连接线将你的iOS设备与Mac连接起来。
2. 在Mac上打开QuickTime播放器。
3. 选择“文件>新建屏幕录制“。
4. 在接下来出现的窗口中，选择你的iOS设备作为摄像头及麦克风输入源。

然后就可以开始录制了。

#### 使用第三方软件录制屏幕

另外一个比较简单易行的选择就是[TechSmith AppShow](http://appshow.techsmith.com/)。这款新软件也是专门针对应用预览视频的制作需求的，同样要求iOS 8硬件设备以及运行着Yosemite的Mac，当然，还有Lighting连接线。此外，这款软件自带一个简单的视频编辑工具，所以除了像使用Quicktime一样录制屏幕以外，你不需要再使用其它软件来编辑视频了。目前TechSmith AppShow还处于Beta测试阶段，你可以免费参加测试。

当然，你也可以使用市面上其它一些比较成熟的录屏软件。从前，它们的主要用途是从其它设备上录制视频，并在电视或网页上进行播放。

为什么要用这类工具？[Reflector](http://www.apptamin.com/blog/app-previews/)的团队告诉我们，通过AirPlay投射的屏幕视频质量更高，因为“通过USB连接的方式录制的视频帧数较低”。TechSmish和Apptamin也对此进行了验证，通过AirPlay投到Yosemite上的视频可以录制出更好的效果，包括iPhone 6和Plus都是这样。

那么这些第三方软件的工作原理是什么呢？他们本身相当于AirPlay接收器，可以将iOS设备的屏幕直接投到PC、Mac或Android上进行录制。确保这些设备在同一网络中，然后在你的iPhone或iPad中打开控制面板，激活AirPlay即可。

下面是一些比较有代表性的第三方软件：

![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/92FEF5F9-B948-404E-A986-AB928C491BF7.png)

#### 在Mac上直接录制iOS模拟器的屏幕

如果以上方法对你都不适用，还有一招：直接录制Mac的屏幕。不过同故宫这种方式录制的视频质量不是最佳的，帧数不够稳定，你可能需要通过后期编辑来改善。

具体方法就是在Xcode上加载并运行你的应用，然后通过下列软件录制iOS模拟器中的视频：

![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/2FFCA473-B570-4039-BC43-7BC55F60FAD7.png)

#### 编辑录屏视频

完成屏幕录制之后，你还需要进行编辑，剪掉没用的东西，把精华浓缩到30秒当中。在导出方面，要记得参考前文给到的技术规范。

你需要一些像样的工具来进行编辑工作，下面这些可供参考：

![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/FD4E20F5-4902-4531-8B5A-BDDDD62A8017.png)

如果你使用Final Cut Pro，可以看看苹果官方的教学视频。更多视频编辑工具可以参见[Mashable给出的列表](http://mashable.com/2013/07/24/best-video-editing-software/#_)。

其中一些软件，例如Camtasia，会内置一些编辑工具套装。如果使用这些软件，你需要留意一下这些工具在导出方面是否符合前文给到的技术规范当中的要求。

### 预算较高

如果钱不是问题，而时间和质量是你们最关注的，那么最好的方式就是外包。下面这些公司可以提供一站式服务，包括屏幕录制、视频编辑、解说等等，让你高枕无忧：

![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/80050D21-03F8-4C34-9401-A23E0A17C6A3.png)

### 小结

预览视频显然比截屏要难制作的多，但成本越高，所能带来的机遇也就越多。制作精良的预览视频可以成为一款优秀应用的又一个标准之一，用户也会越来越多的留意那些提供了预览视频的产品。

对于那些纠结于转化率的提升，或是渴望得到更多机会展示功能的产品来说，预览视频将成为好帮手。游戏类的产品很容易通过截屏来吸引用户的目光，因为它们本身就很炫酷；而对于生产力和效率类的应用来说，要做到吸引人就不那么容易了。花些心思打造一段预览视频将能帮你更好的展示产品。

接下来会有越来越多的设计师和开发者投入到预览视频的制作工作当中，千万别落后。当然，其他方面例如应用图标和静态截屏的优化也是要考虑到的，这些都是提升下载量的重要手段[。](http://beforweb.com/)

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/93809656-B76F-452F-98B2-42AADCF4968B.jpg)](http://www.amazon.cn/iOS%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97-%E4%BB%8E%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%88%B0App-Store%E4%B8%8A%E6%9E%B6-%E5%85%B3%E4%B8%9C%E5%8D%87/dp/B00E5M072K/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

#### [iOS开发指南:从零基础到App Store上架](http://www.amazon.cn/iOS%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97-%E4%BB%8E%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%88%B0App-Store%E4%B8%8A%E6%9E%B6-%E5%85%B3%E4%B8%9C%E5%8D%87/dp/B00E5M072K/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

[本书共4部分：基础篇，介绍了iOS的一些基础知识；网络篇，介绍了iOS网络开发相关的知识；进阶篇，介绍了iOS高级内容、商业思考等；实战篇，从无到有地介绍了两个真实的iOS应用...](http://www.amazon.cn/iOS%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97-%E4%BB%8E%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%88%B0App-Store%E4%B8%8A%E6%9E%B6-%E5%85%B3%E4%B8%9C%E5%8D%87/dp/B00E5M072K/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

相关书籍推荐

译文代表原作者观点。欢迎[发表评论](http://beforweb.com/node/581#comments)，或到[译者微博](http://weibo.com/c7210/)进一步交流探讨。

本站原创编译文章。如需转载，请注明：本文来自[Be For Web](http://beforweb.com/node/581)

英文原文:

[https://medium.com/app-store-optimization-aso/the-ultimate-guide-to-io...](https://medium.com/app-store-optimization-aso/the-ultimate-guide-to-ios-8-app-video-previews-f2e0cbfb0356)

译者信息: C7210 - UX玩家、交互设计师、猫奴、guitar fucker，现就职于腾讯ISUX(上海)

* [设计](http://beforweb.com/design)

* [用户体验](http://beforweb.com/taxonomy/term/14)
* [UX](http://beforweb.com/taxonomy/term/31)
* [UED](http://beforweb.com/taxonomy/term/32)
* [移动应用](http://beforweb.com/taxonomy/term/24)
* [iOS8](http://beforweb.com/taxonomy/term/174)
* [App Store](http://beforweb.com/taxonomy/term/76)
* [应用预览视频](http://beforweb.com/taxonomy/term/175)
* [原创翻译](http://beforweb.com/taxonomy/term/16)

相关阅读

* [十佳应用的故事(1) - 想法、产品定义与交互设计](http://beforweb.com/node/243)
* [iOS Wow体验 - 第三章 - 用户体验的差异化策略](http://beforweb.com/node/71)
* [让用户在输入密码时看到明文吧](http://beforweb.com/node/658)
* [为大屏手机而设计](http://beforweb.com/node/589)
* [汉堡包菜单在大屏设备上的可用性问题](http://beforweb.com/node/582)
* [汉堡包菜单与设计原则的突破](http://beforweb.com/node/552)
* [汉堡包菜单=地下室](http://beforweb.com/node/551)
* [以更好的方式引导用户为应用打分](http://beforweb.com/node/515)
* [通过有意义的动效解释应用的交互机制](http://beforweb.com/node/513)
* [案例学习 - 关于VSCO Cam的可用性测试](http://beforweb.com/node/498)

发表评论

称呼 \*

E-mail \*

邮箱不会被公开

主页 

网址以"http://"开头

评论 \*

有评论回复时提醒我

![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/4CD648FC-096E-42BC-A8C0-F14708FC52DB.jpg)

验证码 \*

输入图片中的字符

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/DA8915CB-B053-4DED-A23F-AED8AFF8ACA1.png)](http://beforweb.com/node/581 "阅读全文")

[在新浪微博上关注Be For Web](http://weibo.com/beforweb "在新浪微博上关注Be For Web")
[在微信上添加Be For Web](http://beforweb.com/sites/default/files/s/qrcode-beforweb.jpg "在微信上添加Be For Web")
[更多分享](http://www.jiathis.com/share)

Search form
-----------

Search

### 关于我

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/F66190CD-5F1E-4D66-9269-A4F720EA6542.png)](http://weibo.com/c7210 "我的新浪微博")

#### [C7210](http://weibo.com/c7210 "我的新浪微博")

UX玩家、交互设计师、猫奴、guitar fucker，现就职于腾讯ISUX(上海)

* [我的新浪微博](http://weibo.com/c7210 "我的新浪微博")
* [我的微信](http://beforweb.com/sites/default/files/s/c7210-weixin.jpg "我的微信")

### 本文相关书籍

* [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/8977383D-E8CB-489C-BE93-3862F4F9B689.jpg)](http://www.amazon.cn/%E8%8B%B9%E6%9E%9C%E7%9A%84%E4%BA%A7%E5%93%81%E8%AE%BE%E8%AE%A1%E4%B9%8B%E9%81%93-%E5%88%9B%E5%BB%BA%E4%BC%98%E7%A7%80%E4%BA%A7%E5%93%81-%E6%9C%8D%E5%8A%A1%E5%92%8C%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C%E7%9A%84%E4%B8%83%E4%B8%AA%E5%8E%9F%E5%88%99-%E5%9F%83%E5%BE%B7%E6%A3%AE/dp/B00E11HAKC/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  #### [苹果的产品设计之道](http://www.amazon.cn/%E8%8B%B9%E6%9E%9C%E7%9A%84%E4%BA%A7%E5%93%81%E8%AE%BE%E8%AE%A1%E4%B9%8B%E9%81%93-%E5%88%9B%E5%BB%BA%E4%BC%98%E7%A7%80%E4%BA%A7%E5%93%81-%E6%9C%8D%E5%8A%A1%E5%92%8C%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C%E7%9A%84%E4%B8%83%E4%B8%AA%E5%8E%9F%E5%88%99-%E5%9F%83%E5%BE%B7%E6%A3%AE/dp/B00E11HAKC/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  [国际知名设计公司LUNAR设计公司总裁John Edson结合自己多年的设计经验，深入苹果公司内部，对苹果公司的大量设计师和领导层进行了深度的采访，提炼和总结出了苹果公司在产品设计领域所遵循的七大原则...](http://www.amazon.cn/%E8%8B%B9%E6%9E%9C%E7%9A%84%E4%BA%A7%E5%93%81%E8%AE%BE%E8%AE%A1%E4%B9%8B%E9%81%93-%E5%88%9B%E5%BB%BA%E4%BC%98%E7%A7%80%E4%BA%A7%E5%93%81-%E6%9C%8D%E5%8A%A1%E5%92%8C%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C%E7%9A%84%E4%B8%83%E4%B8%AA%E5%8E%9F%E5%88%99-%E5%9F%83%E5%BE%B7%E6%A3%AE/dp/B00E11HAKC/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)
* [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/BA48EBA0-399C-4410-A4E0-1DEB1AFE5E97.jpg)](http://www.amazon.cn/iPhone%E5%BA%94%E7%94%A8%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C%E8%AE%BE%E8%AE%A1%E5%AE%9E%E8%B7%B5%E4%B8%8E%E6%A1%88%E4%BE%8B-%E9%87%91%E6%96%AF%E4%BC%AF%E6%A0%BC/dp/B0052HZC54/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  #### [iPhone应用用户体验设计实践与案例](http://www.amazon.cn/iPhone%E5%BA%94%E7%94%A8%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C%E8%AE%BE%E8%AE%A1%E5%AE%9E%E8%B7%B5%E4%B8%8E%E6%A1%88%E4%BE%8B-%E9%87%91%E6%96%AF%E4%BC%AF%E6%A0%BC/dp/B0052HZC54/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  [本书简述了iPhone硬件和应用风格，逐步介绍了如何进行前期的用户研究和竞争性分析，以及提升iPhone应用用户界面和视觉设计的最佳实践。全书通过13个案例分析展示了知名设计师的实践过程，为读者了解应用背后的设计过程提供了第一手资料...](http://www.amazon.cn/iPhone%E5%BA%94%E7%94%A8%E7%94%A8%E6%88%B7%E4%BD%93%E9%AA%8C%E8%AE%BE%E8%AE%A1%E5%AE%9E%E8%B7%B5%E4%B8%8E%E6%A1%88%E4%BE%8B-%E9%87%91%E6%96%AF%E4%BC%AF%E6%A0%BC/dp/B0052HZC54/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)
* [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/2D3285BA-600E-48B1-8BFF-CBEA40440348.jpg)](http://www.amazon.cn/%E8%87%B3%E5%85%B3%E9%87%8D%E8%A6%81%E7%9A%84%E8%AE%BE%E8%AE%A1-%E7%BD%97%E4%BC%AF%E7%89%B9%E2%80%A2%E5%B8%83%E4%BC%A6%E7%BA%B3/dp/B007HJ6TT8/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  #### [至关重要的设计](http://www.amazon.cn/%E8%87%B3%E5%85%B3%E9%87%8D%E8%A6%81%E7%9A%84%E8%AE%BE%E8%AE%A1-%E7%BD%97%E4%BC%AF%E7%89%B9%E2%80%A2%E5%B8%83%E4%BC%A6%E7%BA%B3/dp/B007HJ6TT8/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  [苹果公司前首席设计师罗伯特.布伦纳，乔纳森.艾维的伯乐，首度以“苹果人”内部视角揭示苹果设计之道。乔布斯设计团队中最有影响力的设计大师，精彩讲述伟大的设计如何成就伟大的企业。甄选全球企业经典案例，深度探寻苹果、宜家、星巴克、摩托罗拉等知名品牌的成败根源...](http://www.amazon.cn/%E8%87%B3%E5%85%B3%E9%87%8D%E8%A6%81%E7%9A%84%E8%AE%BE%E8%AE%A1-%E7%BD%97%E4%BC%AF%E7%89%B9%E2%80%A2%E5%B8%83%E4%BC%A6%E7%BA%B3/dp/B007HJ6TT8/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)
* [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/720CDE1A-6DC6-4449-959F-ADD2C237EB9A.jpg)](http://www.amazon.cn/%E8%8B%B9%E6%9E%9C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E4%B8%8E%E8%90%A5%E9%94%80-Dave-Wooldridge-Michael-Schneider/dp/B00817EV5O/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  #### [苹果应用开发与营销(第2版)](http://www.amazon.cn/%E8%8B%B9%E6%9E%9C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E4%B8%8E%E8%90%A5%E9%94%80-Dave-Wooldridge-Michael-Schneider/dp/B00817EV5O/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

  [本书介绍了从应用开发到应用上市销售等各个阶段需要进行的各种工作，包括分析应用创意和竞争力、确定目标受众、评估销售潜力；保护业务和知识产权、避免潜在的法律纠纷；将iOS应用转化为有力的营销工具...](http://www.amazon.cn/%E8%8B%B9%E6%9E%9C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E4%B8%8E%E8%90%A5%E9%94%80-Dave-Wooldridge-Michael-Schneider/dp/B00817EV5O/?_encoding=UTF8&camp=536&creative=3200&linkCode=ur2&tag=c7210-23)

### 推荐系列

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/D2CC24BE-260E-48A4-A90A-ABB0E7CBBC4C.png)](http://beforweb.com/node/596)

#### [Apple Watch Human Interface Guideline](http://beforweb.com/node/596)

[Apple Watch人机界面设计规范(预发布版本) 自发翻译 by C7210](http://beforweb.com/node/596)

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/106565DA-A68C-4FFC-877A-D0DC6569CE71.png)](http://beforweb.com/taxonomy/term/169)

#### [关于汉堡包菜单的二三言](http://beforweb.com/taxonomy/term/169)

[且探索、且思辨、且验证；盲从无益，解决问题才是最终目标](http://beforweb.com/taxonomy/term/169)

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/61E9C05B-1AA4-45E7-826B-B92072FF7E6D.png)](http://beforweb.com/taxonomy/term/151)

#### [那些小处见大的设计细节](http://beforweb.com/taxonomy/term/151)

[自下而上，精心构思，举手之劳，立竿见影，小处见大，令人心动](http://beforweb.com/taxonomy/term/151)

### 重点话题

* [Apple Watch](http://www.beforweb.com/taxonomy/term/171)
* [Sketch](http://www.beforweb.com/taxonomy/term/164)
* [交互设计](http://beforweb.com/taxonomy/term/36)

### 最新文章

* [念叨 - 关于Sketch、Origami、Swift及Apple Watch](http://beforweb.com/node/697)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/6C2C7B8A-3B14-4320-B830-D4362159484F.png)](http://beforweb.com/node/697)
* [(转) Apple Watch平台认知与产品设计](http://beforweb.com/node/695)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/5EE76E25-96BF-45E1-A247-4B3530ACD1B5.png)](http://beforweb.com/node/695)
* [在腕上](http://beforweb.com/node/693)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/FBF38C25-188B-44A1-AFC5-71F2702281B3.png)](http://beforweb.com/node/693)
* [Apple Watch - 放下你的手机，和世界更高效的沟通](http://beforweb.com/node/692)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/91134FF6-E4C3-4622-8456-91A6B39198E9.png)](http://beforweb.com/node/692)
* [Apple Watch的5个产品思路畅想](http://beforweb.com/node/689)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/5EE76E25-96BF-45E1-A247-4B3530ACD1B5.png)](http://beforweb.com/node/689)

### 随机文章

* [导读文摘111011(Google Dart,iPhone应用设计,轻邮件...)](http://beforweb.com/node/11) 

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/E4AF46EA-6C34-485B-BBA3-61C4293FF273.png)](http://beforweb.com/node/11)
* [设计师应该了解的Beacon基础知识 - 交互体验解析](http://beforweb.com/node/485)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/0E8EA8CE-BAC6-4CF3-8DE2-5F5B571A9834.png)](http://beforweb.com/node/485)
* [Apple Watch界面设计规范(21) - 菜单图标](http://beforweb.com/node/622)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/D2CC24BE-260E-48A4-A90A-ABB0E7CBBC4C.png)](http://beforweb.com/node/622)
* [那些小处见大的设计细节(3)](http://beforweb.com/node/378)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/61E9C05B-1AA4-45E7-826B-B92072FF7E6D.png)](http://beforweb.com/node/378)
* [应用推广站点的最佳设计实践及优秀范例](http://beforweb.com/node/177)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/228CE2E9-C9EB-4765-BA20-5398868251B5.png)](http://beforweb.com/node/177)
* [优雅之钻 - Sketch 3带来的新变化](http://beforweb.com/node/474)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/3DC055B8-F8F0-41B2-BE29-9E88A724A070.png)](http://beforweb.com/node/474)
* [Foodspotting创始人谈移动应用的体验设计](http://beforweb.com/node/233)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/8475763F-50A7-4DD7-A140-9F11C4A6B5ED.png)](http://beforweb.com/node/233)
* [易用性与转化率的提升 - 打造良好UI的32条建议(1)](http://beforweb.com/node/374)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/8846232F-4A98-4DC8-9F5D-62AB9B5AB6F2.png)](http://beforweb.com/node/374)
* [Apple Watch界面设计规范(16) - UI元素 - 滑块](http://beforweb.com/node/616)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/D2CC24BE-260E-48A4-A90A-ABB0E7CBBC4C.png)](http://beforweb.com/node/616)
* [Apple Watch界面设计规范(18) - UI元素 - 日期与计时器](http://beforweb.com/node/619)

  [![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/D2CC24BE-260E-48A4-A90A-ABB0E7CBBC4C.png)](http://beforweb.com/node/619)

### 热门话题

[用户体验](http://beforweb.com/taxonomy/term/14)
[UX](http://beforweb.com/taxonomy/term/31)
[UED](http://beforweb.com/taxonomy/term/32)
[原创翻译](http://beforweb.com/taxonomy/term/16)
[交互设计](http://beforweb.com/taxonomy/term/36)
[视觉设计](http://beforweb.com/taxonomy/term/115)
[移动应用](http://beforweb.com/taxonomy/term/24)
[UI](http://beforweb.com/taxonomy/term/43)
[iOS](http://beforweb.com/taxonomy/term/48)
[Apple Watch](http://beforweb.com/taxonomy/term/171)
[iOS7](http://beforweb.com/taxonomy/term/142)
[iPhone](http://beforweb.com/taxonomy/term/11)
[Apple Watch界面设计规范](http://beforweb.com/taxonomy/term/177)
[设计规范](http://beforweb.com/taxonomy/term/125)
[HIG](http://beforweb.com/taxonomy/term/79)
[设计模式](http://beforweb.com/taxonomy/term/68)
[情感化设计](http://beforweb.com/taxonomy/term/116)
[iPad](http://beforweb.com/taxonomy/term/12)
[可用性测试](http://beforweb.com/taxonomy/term/37)
[响应式Web设计](http://beforweb.com/taxonomy/term/7)
[引导](http://beforweb.com/taxonomy/term/73)
[用户研究](http://beforweb.com/taxonomy/term/54)
[反馈](http://beforweb.com/taxonomy/term/114)
[原型](http://beforweb.com/taxonomy/term/64)
[iOS Wow Factor](http://beforweb.com/taxonomy/term/78)
[Web应用](http://beforweb.com/taxonomy/term/44)
[小处见大的设计细节](http://beforweb.com/taxonomy/term/151)
[移动互联网](http://beforweb.com/taxonomy/term/42)
[Redesign](http://beforweb.com/taxonomy/term/145)
[移动设备](http://beforweb.com/taxonomy/term/10)
[线框原型](http://beforweb.com/taxonomy/term/38)
[触屏](http://beforweb.com/taxonomy/term/15)
[网站移动化](http://beforweb.com/taxonomy/term/46)
[汉堡包](http://beforweb.com/taxonomy/term/169)
[简约设计](http://beforweb.com/taxonomy/term/49)
[HTML5](http://beforweb.com/taxonomy/term/17)
[转化率](http://beforweb.com/taxonomy/term/56)
[拟物化](http://beforweb.com/taxonomy/term/130)
[可用性](http://beforweb.com/taxonomy/term/55)
[手势](http://beforweb.com/taxonomy/term/82)
[动画效果](http://beforweb.com/taxonomy/term/106)
[一致性](http://beforweb.com/taxonomy/term/109)
[CSS3](http://beforweb.com/taxonomy/term/8)
[Android](http://beforweb.com/taxonomy/term/51)
[Xcode](http://beforweb.com/taxonomy/term/122)
[App Store](http://beforweb.com/taxonomy/term/76)
[Sketch](http://beforweb.com/taxonomy/term/164)
[框架](http://beforweb.com/taxonomy/term/62)
[电子商务](http://beforweb.com/taxonomy/term/57)
[迭代](http://beforweb.com/taxonomy/term/119)
[最小化可行产品](http://beforweb.com/taxonomy/term/104)
[Google](http://beforweb.com/taxonomy/term/20)
[导读文摘](http://beforweb.com/taxonomy/term/25)
[扁平化](http://beforweb.com/taxonomy/term/129)
[智能手表](http://beforweb.com/taxonomy/term/148)
[iOS开发](http://beforweb.com/taxonomy/term/121)
[MVP](http://beforweb.com/taxonomy/term/105)
[交互模式](http://beforweb.com/taxonomy/term/113)
[情境](http://beforweb.com/taxonomy/term/137)
[差异化](http://beforweb.com/taxonomy/term/87)

[More](http://beforweb.com/tagadelic/chunk/1 "more tags")

### 最新评论

* PBB

  对:
  [念叨 - 关于Sketch、Origami、Swift及Apple Watch](http://beforweb.com/node/697)

  评论:
  [iTunes U 上有 Stanford 的公开课](http://beforweb.com/comment/3905#comment-3905)
* C7210

  对:
  [Apple Watch的5个产品思路畅想](http://beforweb.com/node/689)

  评论:
  [千万别用这词儿...谢了: )](http://beforweb.com/comment/3904#comment-3904)
* Sherry

  对:
  [Apple Watch的5个产品思路畅想](http://beforweb.com/node/689)

  评论:
  [生日快乐，男神！](http://beforweb.com/comment/3903#comment-3903)
* C7210

  对:
  [Apple Watch的5个产品思路畅想](http://beforweb.com/node/689)

  评论:
  [给评论点赞；我个人也是看够了从硬件产品角度的各种分析](http://beforweb.com/comment/3902#comment-3902)
* C7210

  对:
  [Apple Watch的5个产品思路畅想](http://beforweb.com/node/689)

  评论:
  [哈多谢: ) 可惜今天没力气等到1点看发布了，期待明天](http://beforweb.com/comment/3901#comment-3901)

[![](.evernote-content/0273C864-E913-483D-8473-2D71CCB830FA/C14D6572-CDC4-4713-BCCB-C48EE9213DAF.png)](http://creativecommons.org/licenses/by-nc/2.5/cn/)

* [关于Be For Web](http://beforweb.com/about)
* [站点地图](http://beforweb.com/sitemap)

A C7210's website. Copyright © 2015 [beforweb.com](http://beforweb.com/) . All rights reserved.

---

[🌐 原始链接](http://beforweb.com/node/581#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ac68fc7c-bda4-42be-a845-83455631df6e/ac68fc7c-bda4-42be-a845-83455631df6e/)