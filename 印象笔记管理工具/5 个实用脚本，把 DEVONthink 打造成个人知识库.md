# 5 个实用脚本，把 DEVONthink 打造成个人知识库

---

[DEVONthink](https://www.devontechnologies.com/products/devonthink/overview.html) 给很多人的第一印象是「久闻盛名，无从下手」。

确实，DEVONthink 作为 Mac 平台上的一个文件管理应用，以高昂的售价、复杂的功能和缺乏中文支持让不少慕名前来者都望而却步。

但是历经多年后，DEVONthink 在使用者那里的口碑依旧无人能及。这是因为它集成了开放的「I/O]1 环境、拥有灵活的管理方式、还可搭配强大的人工智能和丰富的脚本支持。可以说，DEVONthink 在文件管理领域做到了极致。

那么在这个系列中，我将为大家介绍一些现成的 DEVONthink 上实用的脚本，帮助大家克服畏难情绪，更好地感受 DEVONthink 这个工具的强大。

准备工作
----

因为本文是该系列的第一期，所以我会先简单地介绍一下如何获取脚本、启用脚本以及更改脚本。

在 DEVONthink 的菜单栏中倒数第二个选项是一个「S」型的脚本图标，点开后就是 DEVONthink 的脚本菜单。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/68AE07C7-A65D-406A-A559-6D5F59122B32.jpg)

在脚本菜单中，我们可以看到不同主题的子菜单，里面就是 DEVONthink 内置的脚本，预先选中文件后点击即可使用；如果内置的脚本不能满足你的需求，你不妨点开「More Scripts…」看看，官方提供了更多的脚本供你下载使用，下载后的脚本同样会进入相应的子菜单中；当然你也可以创建自己的脚本文件，只要把它们放入 DEVONthink 的脚本文件中的子文件夹中即可，就能在子菜单中找到你 DIY 的脚本了。你也可以直接修改文件夹中的脚本文件，以达到你想要的效果，修改完保存即可。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/58B810E5-3D78-4919-9F39-07ECFFF07D5F.jpg)

一个小贴士：如果你不记得自己想要的脚本在哪个子菜单中，那么你可以在帮助菜单中直接搜索脚本名，出现结果后点击即可启用。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/14815999-00B2-47B9-AA26-48B06DA6DA4E.png)

脚本推荐
----

在 DEVONthink 中，应用内置的导入功能涵盖了许多第三方应用内容的导入。如果你想要导入的应用或者服务不在该范围内，你还可以通过强大的脚本工具来完成。那么本期，我将向大家展示 5 个用来导入第三方应用与服务内容的脚本，大家看完后可以试一试将自己在其他平台上的资料迁移过来，作为开始尝试 DEVONthink 的第一步。

### 导入 Pinboard 书签

[> 下载链接 🔗](http://7xne7k.com1.z0.glb.clouddn.com/2018-04-17Pinboard.scpt)

作为最负盛名的书签管理工具，Pinboard 拥有不少的拥趸，不过会员需要缴纳每年 11 美元的普通账户订阅费。如果你想获得书签的**离线存档和全文搜索功能**，你还需要额外升级到每年 25 美元的 Archival 账户，这些都是一笔不小的开支。如果你已经拥有了 DEVONthink，那么可以试试用它来代替 Pinboard，DEVONthink 强大的浏览器插件、离线保存特性和全文搜索功能可以帮你剩下 Pinboard 这笔订阅费。

在 DEVONthink 中的脚本菜单中启用「Pinboard」这个脚本，在弹出的窗口中填入你的 Pinboard 账号和密码，就可以自动导入你账户中的所有书签了。导入的时间取决于你账户中的书签数量。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/CF6970AF-2CC4-45F0-BDFE-557826951E2B.gif)

### 导入 Instapaper 文章

[> 下载链接 🔗](http://7xne7k.com1.z0.glb.clouddn.com/2018-04-17Import%20Instapaper%20CSV.scpt)

有很多人会使用 Instapaper 来作为它们稍后读的工具，但是 Instapaper 还是有不少缺点：

1. 基于文件夹的分类特点使得它在文章归档和管理上捉襟见肘
2. 无法抓取很多网站的文章；
3. 没有 Mac 客户端
4. 无法掌控文章离线的进度

那么，不妨试试用 DEVONthink 来做稍后读吧，它所支持的标签系统和智能文件夹可以让文章的归档和管理轻而易举，支持抓取所有网页的文章（除了特别做了防抓取机制的网站），并且可以做到真正的离线保存。

在开始迁移文章之前，你需要在 Instapaper 的网页版中登陆你的账户，然后在设置界面中下载一个 CSV 文件。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/2923D16B-1A80-4751-A0D0-E60FD9E710A3.png)

回到 DEVONthink 后，启用「Import from Instapaper」这个脚本读取这个 CSV 文件，接下来的工作交给 DEVONthink 就可以了，它会帮你**将 Instapaper 中的文章以 PDF 格式全部导入到 DEVONthink 中**。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/0B98E425-0AF0-459E-846B-18E1244DABD1.gif)

### 导入 RSS 内容

DEVONthink 支持导入 RSS 订阅源，可以像 Reeder 一样成为一个 RSS 阅读器，并且在归档和管理上更加方便。但是如果你只是一个 RSS 轻度用户，只是偶尔看一下 RSS 内容，那么 DEVONthink 也可以通过它的 RSS 脚本来解决你这个轻度需求。

以 Apple Hot News 为例，你只需通过内置的「**Feeds - Apple-Hot News**」这个脚本就能快速生成一个包含当天 RSS 信息流的 HTML 网页文件，不需要打开 RSS 阅读器，不需要从浏览器打开书签，在 DEVONthink 中即可快速浏览，看完即删，没有任何负担。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/D4306615-862B-403D-BBA3-36201FD6B37A.gif)

如果你想生成自己想看的 RSS 内容，只需将该脚本中相应部分的 URL 地址改成你想要的 RSS 地址即可。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/F86649BF-DD5E-47B9-89A6-763FF1C63EA3.jpg)

### 添加 Safari 当前所有标签页到 DEVONthink

如果你用 DEVONthink 来管理书签，或者用 DEVONthink 来做稍后读，那么经常会有把 Safari 当前所有的标签页都保存下来的需求。

通过 DEVONthink 的外部脚本，你不需要将标签页一个一个重复导入 DEVONthink，所有任务一键完成。

首先，你需要确保你在安装 DEVONthink 后安装了 Application Scripts，可以在菜单栏中的「Install Add-Ons…」确认。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/62FFBFA0-B373-412C-9D2C-ADBC72D05EBE.jpg)

安装后，你可以在 menubar 的右上角看到脚本工具的图标（如下图）。然后打开 Safari，确认需要保存所有标签页后，启动「Add tabs to DEVONthink」这个脚本，就可以将所有标签页以书签格式 webloc 添加到 DEVONthink 了。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/61392AFA-FB1E-4C19-A868-26C2CE181265.gif)

如果你想将这些网页离线存档，那么你可以用另一个脚本将它们批量转换为 webarchive 格式，也可以转换为 PDF 格式便于批注。这两个脚本将会在之后一期的文章中详细介绍。

### 制作 Safari/Chrome 标签页列表

[> Safari 版下载 🔗](http://veritrope.com/code/save-safari-tabs-to-devonthink/)

[> Chrome 版下载 🔗](http://veritrope.com/code/save-chrome-tabs-to-devonthink-pro/)

本期介绍的最后一个脚本与前面四个有所不同，需要借助 LaunchBar 和 Alfred 这类启动器来运行。

这个脚本的作用在于可以将浏览器中所有的标签页都抓取下来，在 DEVONthink 中**创建一个基于这些标签页的列表**。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/B10957BC-C521-49C6-8946-72B1AE1CEEB9.gif)

这个脚本实现的功能非常类似于 Chrome 上的插件 [Toby](https://chrome.google.com/webstore/detail/toby-for-chrome/hddnkoipeenegfoeaoibdmnaalmgkpip?utm_source=chrome-ntp-icon)，但是不同的是 Toby 适用于本地的临时保存，而这个脚本生成的列表非常适合与其他人分享。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/BC743BCA-7DF7-447F-A171-D8EAE4316067.png)

你可以一键将你浏览器中的网页全部抓取下来，在生成的 HTML 文件中，你可以直接删除不想要的网址，也可以直接用富文本为这些链接添加备注。

![](.evernote-content/AF1C3BBE-10E3-4614-B360-728F7D7B60CA/880A02E1-D4F9-4B49-B71B-7A2DCAC0C013.png)

---

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用 ⚡️

[📎 在印象笔记中打开](evernote:///view/207087/s1/94373a63-834f-4366-8d50-8e41e0ed8fd2/94373a63-834f-4366-8d50-8e41e0ed8fd2/)