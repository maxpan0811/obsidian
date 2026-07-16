---
title: "Fusion Drive 是什么？"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Fusion Drive 是什么？.md
tags: [印象笔记]
---

# Fusion Drive 是什么？

# Fusion Drive 是什么？ --- [![](.evernote-content/EB94306A-85A0-465A-937B-DF184D451275/DEA2E7A5-AA0F-4A

---

# Fusion Drive 是什么？

---

[![](.evernote-content/EB94306A-85A0-465A-937B-DF184D451275/DEA2E7A5-AA0F-4A2C-A1EC-D4BFAE6AA776.jpg)](http://cdn.ifanr.cn/wp-content/uploads/2012/10/Fusion-Drive.jpg)

今天凌晨的发布会，苹果在宣布桌面电脑产品时，引入了闪存与传统硬盘相结合的 Fusion Drive，它能够“自动地管理数据，将使用频繁的 app、文档和照片以及其他文件存储在速度更快的闪存上，不常用的项目则移至硬盘。”

和许多苹果产品的设计思想一样，Fusion Drive 也具备“自动化”的特性，不必人工干预。它的工作方式是默默的，不会打扰你现在所做的事情。“随着系统逐渐了解你的工作方式，应用软件的启动和文件的存取访问将变得更快。”

Fusion Drive 很容易让人联想到几年前英特尔所提出的“迅盘”技术，同样利用闪存来提供硬盘的读写性能，提高系统响应速度。不过两者之间有细微的差别。笔记本电脑上的“迅盘”，其实是在内存与硬盘之间增加一块数据读写速度较高的闪存，利用它较高的读写性能，将它作为数据中转站，让 CPU 的性能得到尽情发挥，从而提高系统的响应速度。根据[联想官方](http://ask.lenovo.com.cn/index.php/detail/253374)的解释：

> 如果笔记本采用了迅盘闪存加速模块，数据读/写的方式将会有所不同。硬盘会一次性的批量读出大量数据，并暂时储存在迅盘中，供系统随时调用；同时需要写入的数据也先暂存在迅盘中，等积累到一定数量后再统一写入到硬盘中，这种随用随取的读/写机制对提高系统性能很有帮助。

而一年前，英特尔发展了“迅盘”技术，提出了 Rapid Storage Technology，为混合硬盘提供更多工作模式。其中一种被称为 Maximized，会让系统自行判断文件使用次数的频繁与否，然后将常用的文件放进读写速度更高的闪存中。——听上去，很像苹果所使用的 Fusion Drive。

不过，根据 [ArsTechnica](http://arstechnica.com/information-technology/2012/10/apple-fusion-drive-wait-what-how-does-this-work/) 的报道，Fusion Drive 更像是采用了企业常见的“自动分层储存技术（automatic tiering）”。这种技术会监控数据使用情况，频繁访问的数据会转移到高性能的 SSD、闪存等高速储存区中，而较少访问的转移到性能较低的机械硬盘等低速储存区中。

“自动分层储存”与英特尔的技术之间有关键的分别。后者实际上是统计频繁使用的文件，然后在 SSD、闪存中建立“镜像”，然后当系统读取相关文件的时候，就直接从闪存中读取。而“自动分层储存”则不然，当被频繁使用的数据迁移到高速储存区之后，原本放置于低速储存区的数据就被删除。

ArsTechnica 的推论有道理。根据 [AllThingsD](http://allthingsd.com/20121023/so-what-the-heck-is-an-apple-fusion-drive-anyway/?refcat=news) 的报道，IHS 一名内存市场分析师 Ryan Chien 称，“英特尔采用缓存机制（caching approach），而苹果则采用分层机制（tiering approach）。”

[AnandTech](http://www.anandtech.com/show/6406/understanding-apples-fusion-drive) 挖掘了 Fuison Drive 的更多细节。在 Mac OS X 中，128 GB SSD + 1 TB 的 Fusion Drive 的容量被识别为 1.1 TB，而换上了 128GB + 3 TB 的 Fusion Drive 的容量被识别为 3.1 TB；闪存与机械硬盘会分开显示；在系统设置中，没有相关图形设置界面。同时，Mac OS X 会自动在闪存上划出 4GB 的空间作为“写缓冲（write buffer）。”

[爱范儿 · Beats of Bits](http://www.ifanr.com/) | [原文链接](http://www.ifanr.com/179960) · [查看评论](http://www.ifanr.com/179960#comments) · [新浪微博](http://www.weibo.com/ifanr) · [订阅全文](http://www.ifanr.com/feed) · [微信订阅](https://www.ifanr.com/weixin) · [加入爱范社区！](http://bbs.ifanr.com/)

  

[![](.evernote-content/EB94306A-85A0-465A-937B-DF184D451275/0ECBABE4-468E-4459-9279-DCE31502148F.jpg)](http://www.ifanr.com/author/yibie)

**[陈一斌](http://www.ifanr.com/author/yibie)**

组织过软件汉化，写过时间管理文章，研究过个人知识管理。关注科技的发展，创投资讯、移动互联网。

邮箱 [Twitter](http://twitter.com/yibie) [Facebook](http://www.facebook.com/yibie) [新浪微博](http://weibo.com/yibie)

![](.evernote-content/EB94306A-85A0-465A-937B-DF184D451275/4012E98E-597E-467E-86B5-59756DF0B621.gif)  
  
[![](.evernote-content/EB94306A-85A0-465A-937B-DF184D451275/4012E98E-597E-467E-86B5-59756DF0B621.gif)](http://da.feedsportal.com/r/144540365956/u/362/f/642084/c/33866/s/179960/a2.htm)![](.evernote-content/EB94306A-85A0-465A-937B-DF184D451275/4012E98E-597E-467E-86B5-59756DF0B621.gif)

---

[🌐 原始链接](http://www.ifanr.com/179960)

[📎 在印象笔记中打开](evernote:///view/207087/s1/71a7e1e8-6bd9-48c8-8215-e3b0560cc066/71a7e1e8-6bd9-48c8-8215-e3b0560cc066/)