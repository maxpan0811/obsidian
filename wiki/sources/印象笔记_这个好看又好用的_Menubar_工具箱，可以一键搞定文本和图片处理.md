---
title: "这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理.md
tags: [印象笔记]
---

# 这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理

# 这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理 --- 这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理 ========================

---

# 这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理

---

这个好看又好用的 Menubar 工具箱，可以一键搞定文本和图片处理
==================================

macOS 上有很多第三方小工具，可以把原本需要好几个步骤的操作，简化为一两步，比如在菜单栏中提供一键开关各项功能的 [One Switch](https://fireball.studio/oneswitch/)，还有 macOS 上的文件中转站 [Yoink](https://www.sspai.com/post/30779) 等等。近日，[克拉壁纸](https://www.sspai.com/post/45356) 的开发团队推出了一款 macOS 小工具 [AnyDrop](https://yuanjoy.com/anydrop/)，它在菜单栏集成了文本处理动作和文件处理动作。让原本复杂的操作大大简化。

我们只要把文字或文件拖动到 AnyDrop 的菜单栏图标，应用会自动弹出动作抽屉，我们把目标拖拽到具体的动作卡片上，应用就会自动帮我们完成相应的操作，比如实现图片处理、识别文字、移动文件等操作。

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/F7211B21-644B-4096-8032-A91B2F717B93.gif)

文本动作，还能自定义 URL
--------------

AnyDrop 支持对文字进行 9 类处理，包括清除文本样式、翻译、繁简体转换等，不同的处理都还有不同的细节设置来实现更多功能。文本动作中最让我惊喜的是「转换为大写金额」操作，以前每次手写报销单我都要使用谷歌，现在只要把金额数字拖动到 AnyDrop，它就会在本地转换成大写，并添加「人民币」或「整」字，十分方便。

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/779FD423-1C54-416A-8E0D-3C7EF62292B8.gif)

当然萝卜白菜，各有所爱。AnyDrop 中默认的动作不一定符合你的口味，你可以在应用的偏好设置中添加或删减动作，以及调整它们的顺序（拖到动作卡片即可）。

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/FFFE74BE-9F6E-49C1-8239-A7FA1FFEE67D.png)

文本动作还支持打开自定义 URL，追求高效率的用户应该对 URL 跳转不会感到陌生。在 AnyDrop 设置中添加「打开自定义 URL」动作卡片，我们可以自行添加搜索、打开应用等操作。

* 在少数派中搜索文章的 URL： https://sspai.com/search/post/{test}，其中 {test} 为 AnyDrop 可识别的输入文本占位符（下同）；
* 在豆瓣电影中搜索电影的 URL：https://movie.douban.com/subject\_search?search\_text={text}；
* 以文本作为标题创建熊掌记笔记的 URL：bear://x-callback-url/create?title={text}，可以参考 [熊掌记的 URL 列表](https://bear.app/faq/X-callback-url%20Scheme%20documentation/) 创建更多动作；
* 以文本在 Things 中创建待办事项的 URL：things:///add?title={text}，可以参考 [Things 的 URL 列表](https://support.culturedcode.com/customer/en/portal/articles/2803573) 创建更多动作；

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/C0FB8449-2D82-43E0-A45A-E31B43ABCFA9.png)

文件动作，图片处理快人一步
-------------

AnyDrop 中的文件动作现在有 13 类，除了隔空投送和移动到文件夹外，图片处理应该是受众最广的应用。我们可以直接把本地图片或者 Safari 网页里的图片，拖动到 AnyDrop 进行处理，比如调整尺寸、压缩体积等。

又一个让我惊喜的动作是「识别图中文字」。以前我一直用 [iText](https://beta.sspai.com/app/iText) 来截图识别文字，现在 AnyDrop 也可以实现了。对于开发者来说，「上传到微博图床」和「上传到七牛云」两个动作，也很实用。

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/BB7900CC-F215-44E8-A960-3C18973C867E.png)

除了拖拽，还有快捷键支持
------------

AnyDrop 动作的触发方式有好几种。首先，拖拽是最直观明白的，把文字或文件拖到菜单栏图标，再拖动到动作卡片即可。

不过两次拖拽定位确实有点繁琐（不能像 Yoink 一样自定义接收区），那么你可以把第二次拖拽用快捷键来实现。当我们把目标拖到菜单栏图标，并弹出动作列表后，我们可以利用 `⌘Command - 数字`，直接触发列表里的动作。另外，AnyDrop 在菜单栏的动作列表也可以用快捷键打开，默认快捷键是 `⌘Command - D`。

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/E0897B2C-750A-442A-A8DE-732F956A01A7.png)

第三种方式是 AnyDrop 会抓取剪贴板中的内容，不管是文字还是图片。我们复制目标后，再点击 AnyDrop 菜单栏图标进行操作（或使用快捷键）。对于文本动作，还有一种触发方式，那就是在输入框中直接输入。

![](.evernote-content/28D5629A-4B68-4F3E-851E-CDAEC88C8D63/75CB2612-72E0-4A32-8980-26B9E9D61AAE.png)

小结
--

我个人使用 AnyDrop 感觉是，它内置的很多动作都动摇了我的 Mac 中部分应用的地位。图片压缩、调整尺寸干掉了 [Resize Master](https://apps.apple.com/cn/app/resize-master/id1025306797?mt=12)；URL 搜索豆瓣可以替代 Alfred 的相同功能；识别图中文字取代 iText；转换大写金额更是从无到有……[AnyDrop 的官网](https://yuanjoy.com/anydrop/) 还列示了许多未来将要加入的动作，以及像「快捷指令」那样可以创建多个连续动作。

因此我非常推荐 AnyDrop 这款聚合类工具，一方面 AnyDrop 满足了很多简单需求，并且不单单是把一些简单功能的叠加（有些动作还有参数设置），另一方面它又可以利用 URL 来实现更高阶的操作。拖拽触发、快捷键、高度自定义等特性都让它的使用体验相当舒畅。

你可以在 [官网](https://yuanjoy.com/anydrop/) 下载 AnyDrop，应用支持 7 天免费使试用，结束后需要付费购买，单台 Mac 激活需要 99 元 / 年， 两台为 186 元 / 年。

送码
--

在评论区说出你在使用 AnyDrop 后对这款产品的建议，我们将从中抽出 3 位读者各获得一枚 AnyDrop 的兑换码。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/56145)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6b1c8fd2-bcfd-45ca-bba9-cde92af38a4b/6b1c8fd2-bcfd-45ca-bba9-cde92af38a4b/)