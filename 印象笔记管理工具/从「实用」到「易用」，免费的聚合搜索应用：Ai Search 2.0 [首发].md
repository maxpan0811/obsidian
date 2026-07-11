# 从「实用」到「易用」，免费的聚合搜索应用：Ai Search 2.0 [首发]

---

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/A7009A1D-26E4-4639-BE04-6AE22D8F9764.jpg)

如果说 1.6 版 Ai Search 是从「不好用」进阶为「实用」，2.0 则进一步将「实用」化为「易用」。聚合搜索应用 Ai Search 今日更新 2.0 版，除了新增 3D Touch 和原生 Safari 体验，以及许多细节的优化之外，开发者还宣布将应用完全免费。

这篇文章前半部分将着重介绍 2.0 新版的功能，后半部分是我们对 Ai Search 开发者 Todd 作的一次简单采访，谈及了 Ai Search 免费的原因及未来的规划。

3D Touch 让搜索更快捷
---------------

3D Touch 这一全新交互形式的引入，让许多应用在易用性上进了一大步，Ai Search 便是得益者之一。3D Touch 操作在新版 Ai Search 中主要体现在**两个方面**：

### 1. Peek 图标快捷搜索

在设置中点击「快捷动作标签」，可选择最多三个标签置于快捷菜单中。搜索时，轻按图标选择对应标签，即可进行对应搜索，无需输入标签名。对我这样的万年「百科」党来说，的确更方便了一些。且鉴于这一功能的加入，作为 1.6 版「鸡肋标杆」的 URL Scheme 带标签语句可以正式下岗，我也不用再纠结语句不支持中文这点破事。

此外，快捷菜单中原生的「搜索剪贴板」一项，基本可替代通知中心部件的功能，大屏用户不用伸着手指去下拉了。

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/19AA3B64-39DB-45CF-A4BB-B64DDC751326.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/3FC50F71-7D69-406C-A406-FF506785E9D7.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/40F3CCD2-BBBE-4C3A-8978-A5C5B5912C84.jpg)

### 2. Peek 预览 Pop 跳转 Safari

在浏览任意网页时，轻按其中链接可如 Safari 一样进行预览，当轻按转为重按时，则会跳转至 Safari 打开对应链接。由于 Peek 和 Pop 效果在这一控件中无法自定义，同为 3D Touch 操作，Pop 却会跳转至其它应用，在操作逻辑上并不十分顺畅。所幸 iOS 9 可以从左上角快速返回上一应用，虽然实用性感觉不如前者强，但还算是有用武之地。

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/24B3E0BF-24CF-4467-AF06-5A978A36E425.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/2B727DC4-8D49-40DF-B732-E51985D97CF6.jpg)

原生 Safari 浏览体验
--------------

Pop 跳转至 Safari 可以说是「无可奈何」，因为在大部分情况下你已无需跳转至 Safari 获取完整阅读体验了。只因 Ai Search 2.0 首次支持使用 Safari View Controller 浏览网页，只需点击右上角的按钮，大部分功能和分享插件都可自由调用，比如花样百出的内容拦截器。网站的登录状态也与 Safari 保持一致，无需重复登录。

除了新增 Safari View Controller 外，Ai Search 的原生浏览页功能也有所增强，比如现在长按链接可以将其拷贝或加入阅读列表，长按图片则可以保存到手机，不用再劳烦 Safari。

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/F4FE2D85-23DE-43F3-B59B-7F6DBA3F1F90.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/82E660F2-32CE-4933-BE09-B6417A01051E.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/0CC81C6C-4464-49A6-AD3C-7A070F19D0FD.jpg)

细节小修小补

有些更新或许并不如 3D Touch 这般新奇，也不如 Safari View Controller 这样明显，但它们却的的确确让 Ai Search 变得好用起来。比如搜索来源推荐，它藏在标签管理的左上角。但如果你不知去哪搜索，可以方便地从推荐中一键导入热门网站，无需再去学习打\*号的复杂方法。

而在搜索时，你无需再输入完整的标签，哪怕只输入一个字符，应用也会自动对应标签，点击即可标签名即可添加并进行搜索。

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/32048386-508B-47B6-98F7-0A72D32A614F.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/52744D56-0BE6-486B-BFF2-237CFF1353B8.jpg)

现在标签编辑也变得更易上手，长按标签名即可进入编辑模式，点击分组名还能对分组进行「批处理」操作。

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/59873029-753F-4FE7-8F72-13707607997E.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/E24CA52A-2910-4082-A079-F2D4FCD88053.jpg)

当然，还有一项不可忽略，Ai Search 2.0 支持将自己所有的搜索来源网站、分组和标签安全备份到云端，无论是误删应用还是换机，都不用担心数据丢失了。

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/5786D2E0-BDA8-4951-86B0-E17D689B8E38.jpg)

![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/8ECE606C-2227-4BFA-9D16-13F70C68F95F.jpg)

Ai Search 2.0 的更新日志长如白练。除了我文中提及的这些变化，2.0 版首次对 iPad 进行适配，支持 iOS 9 的同屏多任务处理，手持 iPad 的用户可以在大屏上搜索世界了。此外还有许多的优化和改进，就不一一赘述，没有什么能比上手体验更真实可感。

为什么免费？对话 Ai Search 开发者
----------------------

**sspai：**Ai Search 上架以来一直是付费 App，为什么会选择「永久免费」？

**Todd：**付费下载模式是预料之中的艰难。收入的艰难倒是其次，最大的问题是，不确定应用本身就小众，还是只是因为收费而将大多数人拒之门外。既然如此，不如免费，可以得到更多的反馈意见，帮助我们继续做的更好。之后可能会尝试内购，比如新增高级搜索服务的内购等。

**sspai：**那么之前已付费的用户呢？是否有补偿计划。

**Todd：**感谢所有付费购买 Ai Search 的用户一直以来的支持，在 Ai Search 存在种种问题，功能不够完善,  迭代缓慢的情况下依然陪伴我们，耐心地提供反馈和建议。

对于近期付费的用户，可以直接向我们申请退款，方式请留意微博 [@Ai\_Search](http://weibo.com/aisearhofficial)。

**sspai：**看起来这次 2.0 是 Ai Search 的一个转型，你们对未来是否有作规划？

**Todd：**以前一人独立开发的时候，描述联系方式总爱说「欢迎联系我们」， 说得好像真的有「我们」似的。😂 现在如愿以偿，有志同道合的小伙伴加入，未来 Ai Search 由工具升级为个性化的搜索引擎也不无可能，但「简单」「高效」「精准」的初衷不会变。

另外，在桌面端「搜索」依然有很大的需求，之后也许会尝试不同的平台，我们自己也很期待接下来会有哪些变化。

**sspai：**你自己平时是如何「搜索」的？和我们分享一下你的经验吧。

**Todd：**聪明人应该有更聪明的搜索方式。不管你使用的是何种搜索引擎或搜索工具，明确自己的需求，用最快的方式向它表明你的意图，养成习惯，能够极大地改善你的工作和生活。

iPhone 和 iPad 上，我会用 Ai Search + 科学上网进行搜索，主要解决一些临时遇到的问题。当找到可用的结果之后，会根据不同的结果类型，从 Ai Search 中分享到[印象笔记](http://sspai.com/tag/%E5%8D%B0%E8%B1%A1%E7%AC%94%E8%AE%B0)、[Instapaper](http://sspai.com/tag/Instapaper) 或 [OmniFocus](http://sspai.com/tag/OmniFocus) 中去，转到 Mac 上进行深入处理。

在桌面端，我查询特定的专业资料需求较多，一般会在浏览器标签栏固定常用的网站，如设计开发和科技方面需要查询对应资料时，直接在网站中搜索。 其它的不确定的直接用 Google，偶尔会使用搜索语法。

个人认为，搜索引擎按照网页、新闻、图片、学术等方式给结果分类，个人感觉并不符合直觉。很多时候，我也不确定想要的解决方案究竟是以什么样的数据类型出现，它也许是在某一篇新闻报道中，也许在某个微博的长图中。所以, 当在网页搜索中找不到结果的情况下，我可能会换个搜索类型，去社交媒体看看，或尝试使用英文关键词，会有意想不到的惊喜。

目前你可以在 [App Store](https://itunes.apple.com/cn/app/ai-search-smart-search-center/id936310061?uo=4&at=10lJSw) 免费下载 Ai Search 2.0。

文章来源 [少数派](http://sspai.com) ，原作者 [Snow](http://sspai.com/author/74) ，转载请注明原文链接

原文可获取应用下载链接：[从「实用」到「易用」，免费的聚合搜索应用：Ai Search 2.0 [首发]](http://sspai.com/32071)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/2E5F3943-34EE-4935-B469-F7281BC0CFBA/31AB0E4F-2C32-4C93-A810-E5C08DF6AF36.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:red/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fproduct-red%2F)

---

[🌐 原始链接](http://sspai.com/32071)

[📎 在印象笔记中打开](evernote:///view/207087/s1/81978c4b-97b9-457b-9aea-6ef0be96004b/81978c4b-97b9-457b-9aea-6ef0be96004b/)