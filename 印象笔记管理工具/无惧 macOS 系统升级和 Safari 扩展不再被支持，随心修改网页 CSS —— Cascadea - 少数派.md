# 无惧 macOS 系统升级和 Safari 扩展不再被支持，随心修改网页 CSS —— Cascadea - 少数派

---

无惧 macOS 系统升级和 Safari 扩展不再被支持，随心修改网页 CSS —— Cascadea
====================================================

### Matrix 精选

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

如果对一个网页的设计不满意怎么办？我们可以通过注入自定义 CSS 来进行更改。此前大名鼎鼎的 Stylish 就是一个修改网页 CSS 的浏览器插件，可惜最终因为窃取隐私数据被彻底人们抛弃。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/98401487-440A-4FA5-B452-13A643597368.jpg)

当时一直在使用 Stylish 的我，担心的却不是这个问题。Stylish「凉透」了，那我用什么来修改 Safari 网页的 CSS？虽然少数派后来有介绍过 Stylus，但对于我们这种 Safari 用户却「极不友好」—— 它只支持 Chrome、Firefox 和 Opera。

那么可能很多人会问，为什么不直接用 Chrome 呢？在我看来有两个原因。

第一是 iCloud 密码填充。这是阻碍我迁移到 Chrome 的最大阻力，因为我的 iCloud 已经保存了几百条的网站和 app 登录密码，并且实时和 iOS 设备同步。如果切换到 Chrome，就必须把这几百条数据全部迁移，工作量巨大。

第二是轻量省电。Safari 毕竟是苹果钦定的官方浏览器，在 macOS 和 iOS 上的体验肯定是坠好的。而且相对来说，Safari 占用的硬件资源更少，也更省电。有时候 Chrome 页面开多了，我 15 寸的 MacBook Pro 都顶不过来。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/D8729ABD-8583-467B-A6E3-3501C38E7059.png)

Chrome 不仅是内存杀手，还很吃 CPU......

所以，我也只能去寻找新的 Stylish 替代品。经过一段时间的努力之后，终于找到了一款能在 macOS High Sierra 和 macOS Mojave 下正常工作的网页 CSS 修改器 —— FreeStyler。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/76DC8A82-249F-48FD-AE94-6D0957A0422F.png)

但在使用 FreeStyler 之中也有一次「危机」，也就是从 macOS High Sierra 升级到 macOS Mojave 时，由于苹果增强了安全性，导致大批插件无法使用的情况。FreeStyler 很不幸在那一次也中枪了。好在后来开发者修复了这个问题，并重新上架了 Safari 扩展库。

然而今年，同样的故事也发生在了 macOS Catalina 上，我的油猴和 FreeStyler 再次因为 Safari 版本更新（13.0）和系统升级的原因无法使用了…… 而且，这一次的情况似乎还很严重：苹果直接关闭了 Safari 扩展的网页，而是把链接全部指向到了 App Store 的扩展商店内。这也就意味着，所有想要上架的插件，都必须经过苹果审核了。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/EC1A9C31-1452-4BA5-BC56-1B7BE5DD45A8.png)

所以，我对 FreeStyler 和油猴能不能上架，还是比较担心的。但是，想让我不改 CSS，那肯定也是不可能的！

但必须要承认的是，Safari 的生态真的太差了。为了寻找这样一个插件，浪费了我几个小时的时间。终于，功夫不负有心人，在漫长的搜索之后，还真让我找到了一款能在 macOS Catalina 下能完美使用的 Safari CSS 修改器 —— [Cascadea](https://apps.apple.com/cn/app/cascadea/id1432182561?mt=12)。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/C51437F6-23D6-4AE3-8EB9-53D9B76E5A41.png)

Cascadea 是一款直接上架在 App Store 上的应用，通过应用自带的扩展安装到 Safari 上，因此从某种程度来说绕过了 Safari 扩展商店的审核，也就保证了它不太可能会被系统更新和 Safari 升级所影响。只要 app 没有出现问题，那么 Cascadea 的 Safari 扩展大概率都不会出现被停用或不受支持的情况。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/D01E0352-A7A4-4EAB-9938-5342EA5EFFFF.png)

Cascadea 的使用方式也很简单。打开 app 后，只要点击左上角的「+」按钮，然后输入一个新的样式名称和适用的网页，再点击 Creat，就可以开始进行修改了。

值得一提的是，在「适用于以下网页」的选项上，Cascadea 提供了四个选择，分别是域名、地址、以某域名为起始的地址和正则表达式，几乎能够涵盖所有的网页。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/682E7B90-5B16-48E0-AA62-10F04BC5DC45.png)

进入到 CSS 编辑器后，就可以开始 CSS 代码的编写了。在编辑页面，Cascadea 支持多章节的 CSS 编写，更易于不同元素的管理。同时，你还可以在 Rules 中选择是否将 CSS 代码应用到多个网页，同样也支持域名、地址、以某域名为起始的地址和正则表达式的输入结构。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/8CEE759B-F94F-4BBA-81C1-12A3A76E349A.png)

除此之外，你还可以设定作者、版本、描述等内容，或者是将 CSS 单独保存为本地文件。

如果你平时在写代码时还是个不注意留白和换行的「随便党」，Cascadea 还给了你一个「一键格式化」的选项。当然，此「格式化」非彼「格式化」—— 点击上面的魔棒按钮，Cascadea 就会自动帮你整理和规范当前页面的代码，让代码更加符合留白和换行规范。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/229384AB-50A5-45FB-8D22-FDE98CED8D9A.png)

在 Cascadea 的偏好设置选项中，你也可以对编辑器进行调整，例如主题、是否显示行数、警告和错误、是否自动换行和自动填充。

不过在设置中的那个「Enable awesomeness detection」我倒是没发现哪里有用，大概是我代码写的太烂，根本不能触发吧。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/AA725D2D-D8B8-4966-9AB6-8679193ED290.png)

代码写完之后，直接按下 `⌘Command+S` 保存，就可以立即对需要修改的网页生效，不需要刷新。如果因为手抖出错，还可以直接 `⌘Command+Z` 进行回滚操作。因此比起之前那些直接在网页端进行修改的插件来说，Cascadea 的体验也更加优秀。

对了，Cascadea 还支持根据不同的系统显示模式（深色模式、浅色模式或全局），来选择是否对网页进行 CSS 修改。比如你可以针对经常访问的网页自己写一个「Dark Mode」的版本出来，并让它在系统开启深色模式时才生效，这样就能获得更佳的夜间网页浏览体验了。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/996B1775-6028-4490-8B8A-CB7E44221741.png)

妈妈再也不担心我被白色网页亮瞎了

此外，根据外国开发者的统计显示，Cascadea 还支持从 userstyles.org 安装 CSS 文件。

![](.evernote-content/81F6654B-5C7A-4282-BD69-0D0EB1A19FDA/1F9F0D28-60BB-4A1B-9C71-DA9BCCAB0E80.png)

Safari 的处境就是这么困难......

目前 Cascadea 可以在 Mac App Store 下载到，售价 18 元。至于值不值得掏这笔钱，就看你有没有强烈对 Safari 网页进行 CSS 修改的需求了，反正我觉得很值。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://beta.sspai.com/post/56909)

[📎 在印象笔记中打开](evernote:///view/207087/s1/088acc2d-7127-4567-905f-d6217571085c/088acc2d-7127-4567-905f-d6217571085c/)