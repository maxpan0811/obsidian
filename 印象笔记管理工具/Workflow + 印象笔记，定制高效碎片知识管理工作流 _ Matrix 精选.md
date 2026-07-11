# Workflow + 印象笔记，定制高效碎片知识管理工作流 | Matrix 精选

---

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/0D2ACCA3-1134-4D93-9046-9178C5528F5B.jpg)

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/E2BA8EA5-53FC-449C-B5EE-0110C2918113.png)

[Matrix](http://matrix.sspai.com/) 是少数派的全新产品，一个纯净、小众的写作平台，我们主张分享真实的产品体验，有实用价值的互联网领域经验、思考。欢迎忠于写作，喜好分享的朋友[参与内测](http://matrix.sspai.com/apply)。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

本文作者借助 Workflow，制作了一个在 iOS 上非常方便地摘录文字信息至印象笔记的工作流，并详尽分享了他的制作过程和思路。文章内容仅代表作者本人观点，文章排版有略作修改，[原文链接](http://matrix.sspai.com/p/cdb08e20)。

写在前面
----

* 印象笔记：很多人都接触过 [印象笔记](http://sspai.com/tag/%E5%8D%B0%E8%B1%A1%E7%AC%94%E8%AE%B0)，这是一款用来收集整理的利器。作为一款众所周知的产品，相信大多数人都感受过它的强大。
* Workflow：这是一款手机端定制工作流的强大 App，不断扩展的组件库和系统 API 调用，让它可以拥有越来越强大的自动化处理能力。我们完全可以把自己日常生活中的一些繁琐的流程简化成一个工作流。如果看完本文章你对定制工作流感兴趣，推荐 [少数派Workflow 入门系列文章](http://sspai.com/27733)。

碎片知识收集为什么困难
-----------

想象一下，你在某篇公众号文章中发现了某段有价值的东西，如果你想收集起来，有时候不得不中断阅读的过程，打开某个可以收藏文字的 App（如印象笔记），新建一个文章粘贴保存。你也可以等到阅读完整篇文章再进行收集，但有的文章太长，极大可能你就不想再浏览一遍再专门进行收集了。

知识零散地分布在众多的平台，今天在微信，明天在知乎。这个牛逼的作者在豆瓣风声水起，那个大神却在简书里侃侃而谈。统一收集绝对是痛点，你可以分别在他们所在的平台收藏他们的文章，但不可避免地你需要管理多个平台的知识库。他们有很多经验与你分享，你当然很有必要收集起来，所以简化收集过程并将知识统一纳入我们惯用的空间进行储存是很重要的。

简要介绍这个 Workflow
---------------

### 特点

1. 任意地方收集你的知识
2. 通过下拉通知栏快捷操作
3. 几乎不影响阅读体验
4. 显示摘录时间
5. 印象笔记排版美观

### 使用方式一

1. 拷贝文章中某段某句
2. 点击下拉通知栏workflow收集项
3. 关闭通知栏继续阅读

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/F6D163A8-2DFC-45EF-8AEE-B8DB6777B79D.gif)

### 使用方式二

（感谢微信好友@聪聪 的补充）

1. 选中文章中某段某句
2. 点击共享
3. 选择 Run Workflow
4. 执行完毕自动返回继续阅读

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/65E0D8D9-23DE-43D2-AB08-FF65D05DF5C8.gif)

第一次使用方式二的时候，点击共享时需要按以下步骤配置出 Run Workflow 的选项：

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/5B214B38-2166-4C89-9170-47F53C8B7597.jpg)

扩展使用
----

上面仅仅只是演示了一个最简单的版本，Workflow 还可以做到更多，总结出属于自己的工作流使工作事半功倍。

如果基于上面的版本进行扩展，你会想到其他什么方案？

### 贴标签

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/68478956-E75F-464F-85CA-6A1D6DE074E7.gif)

### 加注释

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/91D07509-0144-4EB1-82C7-A15B034D0B1F.gif)

### 多文章存储

还有一种我已经实现的扩展是可以利用多个文章来分别存储，这种实现跟贴标签类似，只不过贴标签是在同一个文章里，有时候内容多了可能并不方便管理，多个文章也就相当于提前分好了类别。

最终效果图
-----

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/A1DE5DF2-2D7E-4F1E-A4E8-82DF4B3B9005.jpg)

制作过程
----

好了，看完了上面的演示，接下来讲下具体的制作过程，让更多喜欢折腾的人也能自己动起手来。如果突然发现这么一折腾，还能产生一些不错的想法，再一起交流促进，这样就再好不过了。

### 先讲下两者大概的分工

* Workflow：主要的工作是对文字内容进行各种组装，如格式化时间、自定义 Html 修饰文本、生成富文本等等。它最后输出一段富文本到印象笔记，传输到印象笔记的内容会按照两个参数来决定将内容添加到哪个文章末尾来进行储存，这个后面会详讲。
* 印象笔记：印象笔记其实并没有做太多的事情，它在这里最大的好处是可以在笔记内显示网页。当然，它庞大的用户基数和优良的体验也让它成为了知识整理存放的不二之选。

解析 Workflow 各个流程
----------------

在说清楚各个流程都具体干了哪些事情之前，先大概讲下 Workflow 这类工作流应用的工作理念。它原则上是给你提供了一系列动作（Action），主要分成两大类，一类是系统级别的各种开放式接口，一类是应用级别各个应用特殊开发的 URL Schemes，在 Workflow 中已经被封装成一个个动作，也配有专门的解释，不需要用户关心具体的 URL Schemes 代码是什么，图形化的界面方便更多用户使用。推荐大家阅读少数派这篇 [URL Schemes 使用详解](http://sspai.com/31500)。

通过这一系统的动作组合，往往就可以实现很多新奇的工作流。官方和很多第三方平台提供了许多定制好的工作流，只不过多数与我们自身并不十分相符，所以我更愿意尝试去总结出自己平常的一些操作。当然你并不能通过 Workflow 实现所有你想得到的 idea，但尝试去总结打造，过程仍然是相当有趣的。

### 1. 格式化时间显示

动作流程：

* 获取系统当前时间  >>>
* 自定义格式化  >>>
* 保存格式化后时间字符串  >>>

**![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/149591D8-A378-457A-AA8E-05E083EBB65D.jpg)**

这一步骤的重点，在自定义时间格式上，我们只需要分别对应上各个单位对应的英文字母，中间加上我们想显示的连接符就 OK 了。

经过这一步骤格式化之后，我们就可以获得需要的时间显示了。

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/5CB5D496-5B40-41B3-8091-96A619E513E6.jpg)

### 2. 添加注释处理

动作流程：

* 注释开关  >>>
* 判断是否进行该动作  >>>
* 获取用户输入  >>>
* 保存用户输入  >>>
* 拼接成HTML代码  >>>
* 保存拼接结果  >>>

<table style="font-size:11pt;margin-top:0.5em;">

<tbody>

<tr>

<td style="color:#a9a9a9;padding-right:0.5em;vertical-align:top;width:2px;">

注

</td>

<td style="padding-left:0.5em;width:10000px;vertical-align:top;color:#555555;border-left:1px solid #a9a9a9;">

这是一篇workflow评测文

</td>

</tr>

</tbody>

</table>

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/B4CFE61A-B085-4A01-9B10-A5A95EBC2974.jpg)

这里为了解析需要将所有操作都放在一起，所以特意添加多一个注释开关（将开关的输入改为 true 既可打开），我平时使用会将这注释与下文即将提到的贴标签等功能，分别独立成不同的 Workflow，因为有些操作需要中断阅读跳转到 Workflow 才能完成，比如添加注释。所以分成多个 Workflow 按需操作是种不错的选择。

### 3. 贴标签处理

动作流程：

* 标签开关  >>>
* 判断是否进行该动作  >>>
* 用户选择列表某一标签  >>>
* 保存该标签  >>>
* 拼接成HTML代码  >>>
* 保存拼接结果  >>>

<span style="padding: 1px 6px;border-radius: 10px;background-color: rgb(237,108,0);color: white;">

观点

</span>

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/CBF01F3D-BA9A-407B-A29F-C5C4CAE79501.jpg)

这里并没有太大的难点，标签列表需要提前添加好，目前暂没有提供多选标签的操作，想动动手的小伙伴们可以自己试试看。

### 4. 拼接成完整网页代码

将上述的时间，注释结果，标签结果拼接成一整块代码，对应生成到印象笔记效果图中的一项。以下是最终生成的网页代码，可以看到上面生成的片段代码都被拼凑到一起了。

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/97CAE3F5-8B61-4F99-9144-5F9ABC9D5EFB.jpg)

<div style="padding-top:1em; padding-bottom:1em;border-bottom:1px dotted #d3d3d3;">

<div style="font-size:10pt; margin-bottom:1em;padding-left: 8px;border-left: 5px solid rgb(237,108,0);color:#888888;">

16-08-25 16:15:16<span

style="padding: 1px 6px;border-radius: 10px;background-color: rgb(237,108,0);color: white;">精进</span></div>

<div style="font-size:12pt;">workflow+印象笔记，定制高效碎片知识管理工作流</div>

<table style="font-size:11pt;margin-top:0.5em;">

<tbody>

<tr>

<td style="color:#a9a9a9;padding-right:0.5em;vertical-align:top;width:2px;">注</td>

<td style="padding-left:0.5em;width:10000px;vertical-align:top;color:#555555;border-left:1px solid #a9a9a9;">

这是一篇workflow评测文

</td>

</tr>

</tbody>

</table>

</div>

### 5. 编译网页代码为富文本

上一步拼接好的完整代码会原原本本地传入这个动作中，这是一个重要的动作，将传入的网页代码转化为富文本，经过这一步转化，原来看起来很没有章法的代码就变成拥有漂亮格式的富文本了。

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/32D51F42-7466-4495-9CBD-80D67CE398D1.jpg)

看吧，这效果应该还是不错的，如果你是一名前端开发者，那就更有你的发挥空间了，你完全可以定制出自己喜欢的排版风格。不是专业的小伙伴可以评论出来，我会根据实际情况来帮你们实现。

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/AE182DA6-05AD-45CF-B1C1-D43345D4344E.jpg)

### 6. 添加至印象笔记指定文章

这一步应该说是整个 Workflow 的关键动作，这是印象笔记提供的一个可以在指定文章末尾添加内容的动作。第一个参数 Note Title 顾名思义就是指定文章的名称，第二个参数 In Notebook 是指定文章所在的笔记本名。

![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/41C91FA8-A3DB-4AF9-A9DA-E0681F391424.jpg)

注1：这里的指定文章和指定笔记本都是需要印象笔记或者国际版中实际存在的，两个参数都没有中英文限制，只要实际存在既可。

注2：这个动作是通过网络请求添加至印象笔记的，所以在使用过程中，你切换到了印象笔记有时候并不能马上看到结果，是因为这时候印象笔记还没来得及同步网络添加的笔记数据，这种情况下一般手动同步一下就可以看到了。

如何在你的 iOS 设备上体验该 Workflow
-------------------------

1. 从 App Store 下载 Workflow 应用，现价 18 元；
2. 在印象笔记建好一个名为 Note 的笔记本，并在该笔记本下新建一个 MainPanel 的笔记；
3. 点击下面的 Workflow 链接在 Safari 打开（会提示在 Workflow 应用内打开）；
4. 授权印象笔记后即可使用。

分享至印象笔记的 Workflow 下载
--------------------

* [标准版：单纯添加摘录内容至印象笔记](https://workflow.is/workflows/ffe340d09bb24cc1b951ce2774386301)
* [标签版：标准版+标签功能](https://workflow.is/workflows/b55b78f1a2d84a56b0052cdbd20303bf)
* [注释版：标准版+注释功能](https://workflow.is/workflows/f59254945a894d71bc931a4c0961462a)
* [组合版：如果你需要组合上述三种版本的话](https://workflow.is/workflows/72a952c8fc7d43809798f92d4bb86910)

#### 

写在结尾
----

作为一名喜欢瞎折腾的技术宅，平时实在没有太多的好料可以拿出来分享，懒是最主要一个原因，其次是不善于总结。保持输出是一个好的选择，也是一个好的习惯，希望自己可以保持每隔一段时间的输出，与诸君共勉。

文章来源 [少数派](http://sspai.com/) ，原作者 [weihong](http://sspai.com/author/707271) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime

少数派（ [http://sspai.com](http://sspai.com/) ）

[![](.evernote-content/9B9C48A8-3B62-449B-83AD-04A8F50B6D50/78C93D1A-761F-41D9-8010-D65E0F5054F2.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:BASE/destination:http://www.apple.com/cn/shop/product/HK2R2ZM/A/%E9%85%8D%E5%A4%87-smart-connector-%E7%9A%84-logi-base-%E5%85%85%E7%94%B5%E6%94%AF%E6%9E%B6-%E9%80%82%E7%94%A8%E4%BA%8E-ipad-pro?fnode=85)

---

[🌐 原始链接](http://sspai.com/35281)

[📎 在印象笔记中打开](evernote:///view/207087/s1/187b6af7-6ddf-4339-9dab-357d9c5b2691/187b6af7-6ddf-4339-9dab-357d9c5b2691/)