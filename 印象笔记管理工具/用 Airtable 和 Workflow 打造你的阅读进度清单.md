# 用 Airtable 和 Workflow 打造你的阅读进度清单

---

自从接触到了 [Airtable](https://airtable.com/) 和 [Workflow](https://itunes.apple.com/cn/app/workflow/id915249334?mt=8&at=10lJSw)，总觉得这两个要是结合起来会非常有用，但一直不知道怎么把两者结合。直到4月22日读到《[Airtable + Workflow = 效率？基础入门 | 新手问号](https://sspai.com/post/44207)》才知道结合二者的技术，于是萌生了利用 Airtable + Workflow 跟踪自己阅读的想法。

本文设计的 Workflow 的下载链接如下，你可以后一边查看 Workflow 步骤、一边阅读文章，效果更加。使用以下 Workflow 前需要配置填入 API key 和相应表格链接。

* [添加想读](https://workflow.is/workflows/33f5b0cef2654d89a770e29fca106361)
* [添加在读](https://workflow.is/workflows/bed9d5e973974da3a52a8a1755c56381)
* [添加已读](https://workflow.is/workflows/2ef56769f4e84784825d6cc1cc166054)

概述
--

虽然豆瓣本身就有跟踪自己的阅读书目的功能，但是还是更倾向于一个更加本地的，并且可以自己对数据进行操作的记录。在接触到 Airtable 之后觉得很适合，于是为自己建立了一个 Books I read 的表格，有三个 sheet，分别是 Books I want to read （想读）, Reading（在读）和 Books I read（读过）

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/93103F2C-755E-49D2-8366-314C610539B8.png)Books I read表格概览

想读（Books I read）中包含了

* 书名（Name）
* 作者（Author）
* 添加日期（Date added）
* 想读理由（Reading reason）
* 总结（Summary）
* 豆瓣链接（Douban link）

在读（Reading）表格在想读表格的基础上添加了

* 开始日期（Date started）

已读（Books I read）表格在在读表格的基础上添加了

* 结束日期（Date finished）
* 评分（Rating）
* 我的短总结（My short summary）
* 阅读笔记（Reading notes）

但是 Airtable 本身的输入方式并不是非常方便，尤其是在移动端上，连复制功能都没有，然而跟踪阅读书目中最常见的操作就是把一条记录从这一个 sheet 移到另一个 sheet。在看完《 Airtable + Workflow = 效率？基础入门 | 新手问号》之后，我决定采用利用 Workflow 自动输入的方式。另外，虽然不想在豆瓣上记录自己的数据，但不得不承认豆瓣上关于图书的数据库是很强大的，所以在添加书目的 Workflow 中我使用了从豆瓣上抓取书名，作者，简介的手段，减少输入成本。

Workflow 设计

我一共设计了三个 Workflow，分别是

* 添加想读：通过书名在豆瓣检索获得作者，简介等信息加入想读的 sheet，添加想读理由和时间戳
* 添加在读：选择在读的书名，将该记录从想读sheet移动到在读 sheet，并添加时间戳
* 添加已读：选择已读的书名，将该记录从在读sheet移动到已读 sheet，添加时间戳，自己的总结和读书笔记（可选）

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/EA3C3883-F260-4059-A935-CB3DED8BBA14.png)流程图

前期准备

这个 Workflow 是基于豆瓣和 Airtable 的 API，所以需要对 API 比较熟悉。API（应用程序接口）用于程序和其他软件的沟通，本质是一些预先设置好的函数。在豆瓣和 Airtable 的 API 实际使用中，可以简化理解为通过向服务器发送一个操作『链接』，服务器对记录进行操作（返回，添加，删除等等），其中记录储存格式主要是 JSON。

关于 Airtable 的 API 的使用在[《Airtable + Workflow = 效率？基础入门 | 新手问号》](https://sspai.com/post/44207)中有非常详尽的介绍，建议读者先移步这里。

关于豆瓣的 API，由于这里我主要参考的是 [搜索图书评分 Workflow](https://workflow.is/workflows/351d628833204674ac44a7a239b1c470) 中已有的操作，这里就不做赘述了。如果读者有需求添加自己的功能，请移步豆瓣 API 官方文档。

关键操作拆解
------

这三个 Workflow 中核心都是使用 Workflow 的 API 操作，包含的 API 操作主要是添加和删除，下面简要一下关键操作。

### 豆瓣搜索

如前所述，豆瓣搜索的部分我参考了少数派 Workflow Gallery中的 [搜索图书评分 Workflow](https://workflow.is/workflows/351d628833204674ac44a7a239b1c470)，并根据自己的需要加入了获取作品简介的功能，下面展示相关的Workflow操作：

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/381820A6-E302-46E4-96FC-72F2636C9BD7.jpg)豆瓣相关操作

这三个 Workflow 中核心都是使用 Workflow 的 API 操作，包含的 API 操作主要是添加和删除，下面简要一下关键操作。

### Airtable 操作

#### Airtable 记录添加

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/8566A3AD-43DD-4D91-AC26-9984C25B8D7A.jpg)Airtable记录添加相关操作

以上是 Airtable 记录添加的相关操作，设置好 URL（可从 Airtable 的官方文档获得），利用 Get Contents of URL，选择 POST 即可添加记录。添加的记录是 JSON 格式，名字叫 fields，设置如下图：

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/F09EDFA3-8DC5-4809-B3FB-3A4149695FBB.jpg)Airtable记录格式在Workflow中的设置

#### Airtable 记录检索

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/13CD78A2-0FC8-446F-AC39-A86B176A8438.jpg)Airtable记录检索相关操作

与记录添加类似，记录检索就是把 Get Contents of URL 中的 Method 设置为 GET，不需要设置 Request Body。返回的是一个 JSON 格式的记录，与前文的豆瓣返回结果类似，利用相似的操作，我们将其变为一个选择列表。

#### Airtable 记录删除

记录从一个表移入到另一个表其实是添加和删除两步，Airtable 记录删除的 Workflow 操作如下：

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/E7080965-FED9-408D-A1BC-C990B7B99A3F.jpg)Airtable记录删除

与前面很类似，我们只需要指定 URL，选择 Method 为 DELETE 即可。主义这次的 URL 需要包含需要删除的记录的 id 信息，有兴趣的读者可以参考 Airtable 的文档或者参看具体的 Workflow 动作（下载链接在文后）。

### 其他操作

设计中有很多获取记录并输出成选择列表的操作，在 Workflow 中这个功能实现有些复杂，在这里我参考的是豆瓣阅读中的相关操作，可以看出真的是很复杂……

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/12A09D6A-E83B-4599-9B1F-26E8FB0377B0.jpg)冗长的把记录变成输出列表的操作

演示视频
----

下面是三个 Workflow 的演示视频，可惜分辨率不高。

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/331D1BD9-0191-4D40-8652-7AF335943729.gif)添加想读演示

添加在读演示
------

添加已读演示
------

一点体会
----

这也是我第一次正式的做一个相对而言比较大的 Workflow，在感受到 Workflow 强大的同时，整个 DIY 过程也有些许体会。我平日工作很大一部分是编程，虽然 Workflow 在一定程度上是一种『编程』，但是其逻辑和 Python 之类的还是有一些不同，并且 Workflow 的调试也和一般的程序有所不同，需要一点时间适应。另外 Workflow 目前还不支持动作复制的功能，尤其在我这个有很多重复类似操作的设计中感觉还是有些繁琐。

相关链接
----

* [豆瓣 API 文档](https://developers.douban.com/wiki/?title=api_v2)
* Airtable 的 API 文档在每个 table 的 help 模块中，也可在此 [链接](https://airtable.com/api) 中获取

![](.evernote-content/C98E6FF3-2F69-4C05-93FB-30DB3BCA3C8C/F4B7C473-0428-4B52-BD26-B42060DA0EE3.png)Airtable API

* 本文的 Workflow 设计参考了基于[《Airtable + Workflow = 效率？基础入门 | 新手问号》](https://sspai.com/post/44207)by @小他还是他，另外根据小他在评论中的指路，也参考了[《技巧：利用 Workflow 记录书籍 / 影剧到 Airtable | Matrix 精选》](https://sspai.com/post/36100)by @Hughchanx

---

> 想知道关于 Workflow 的更多用法，请访问少数派的 Workflow 专题 🔥

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，读有趣的内容 🎉

---

[🌐 原始链接](http://sspai.com/post/44551)

[📎 在印象笔记中打开](evernote:///view/207087/s1/26f24967-ab02-48e9-8498-9026aa362eae/26f24967-ab02-48e9-8498-9026aa362eae/)