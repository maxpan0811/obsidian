---
title: "用 App 记录自己的成长 _ Workflow 定制 002"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/用 App 记录自己的成长 _ Workflow 定制 002.md
tags: [印象笔记]
---

# 用 App 记录自己的成长 _ Workflow 定制 002

# 用 App 记录自己的成长 | Workflow 定制 002 --- 用 App 记录自己的成长 | Workflow 定制 002 ==============================

---

# 用 App 记录自己的成长 | Workflow 定制 002

---

用 App 记录自己的成长 | Workflow 定制 002
===============================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

#### **关于栏目**

Workflow 是一款自动化效率应用，而少数派拥有互联网上最好的 Workflow 中文教程。此栏目每期由读者提出想实现的 Workflow 需求，由我们来帮你定制。

[提交你的 Workflow 需求](https://jinshuju.net/f/rW8IdX)

---

Workflow 不能做什么（一）：用 URL Schemes 和 API 传输数据的区别
---------------------------------------------

**@JailbreakHum：**从开始写 Workflow 教程以来，就经常有人提出一些 Workflow 无法实现的需求。这个情况是正常的，而且反应出了基础用户对于一些概念的混淆。包括这次 Power+ 里诸位提出的需求里，也有类似的情况。所以我想趁着这个机会，每次跟大家梳理一下哪些东西 Workflow 是无能为力的。

这一期的 Workflow 定制，是一个读者希望在一个 App 里记录自己成长的需求。他希望每次把新的信息添加到同一份 Day One 的日记里。这个需求或者类似的需求有不少，我完全可以理解大家为什么想这么做，但是为什么这个需求针对 Day One 目前无法实现呢？原因有两点：

1. Day One 没有支持在同一个日记文件中「Append」内容的 URL Schemes；
2. Day One 虽然已经转为了网络服务形态，但并没有公开它的 API。

这里我顺便还想说一下 URL Schemes 和 API 的一个区别：URL Schemes 是用于**本地应用**间传输数据的，它最典型的一个特征就是，当你通过 URL Schemes 传输数据，就必然**会发生跳转**。但当我们通过 API 传输数据，它会把数据传到服务器（或者说云端），所以**不会发生跳转**。

也因此，没有网络的时候，你可以用 URL Schemes 或者内置的 Share Sheet 把文章存到 Evernote，但没有办法使用 Pocket 内置的发送到 Evernote 的动作去发送文章。

实现「把新的信息添加到同一份 Day One 的日记里」这个需求，我们最希望的是不用发生跳转 —— 通知中心拉出来，选择 Workflow，输入几个数字，发送，收回通知中心。这是最舒服的一个流程，所以我们最理想的解决方式就是通过 API。然后我们去查 Day One 的 API，发现它没有公开这部分的内容，所以我们只有退而求其次地选择 URL Schemes。

查找 [Day One 的 URL Schemes](http://help.dayoneapp.com/tips-and-tutorials/day-one-url-scheme) 我们会发现，它没有直接为同一条笔记附加内容的 URL Schemes（这其实也是有原因的，但是篇幅原因就不展开解释了）。没有越狱的 iOS 系统选择非常少，可以走的两条路都走不通，我们就可以宣布这个需求暂时不能解决。

但我们会发现如果把工具换成 Evernote，这个需求就可以很简单地解决。这就是 Evernote 强的地方，很多人只看到它交互糟糕那一面，从来没有认识到 Evernote 服务属性的完善程度。是这个服务属性的完善，让 Evernote 至今无可替代。

和 Dropbox 一样，只要和 Evernote 能关联上的第三方应用，都会去关联 Evernote。Workflow 也不例外。Workflow 内置了 5 个与 Evernote 有关的动作：

* Append to Note （附加内容到笔记）
* Delete Notes（删除笔记）
* Get Notes（获取笔记）
* Create New Note（创建新笔记）
* Get Note Link（获取笔记链接）

我们看到了 `Append to Note`，而这就是我们需要的。

所以「把新的信息添加到同一份日记里」这个需求，只要换为 Evernote，就可以轻松解决。

---

用 App 记录自己的成长
-------------

**@Aperper：**之前自己尝试制作了学习内容的 Workflow，比如我上午看了一本书看了多少页，我通过 Workflow 记录在了 Day One 中，下午听了英语听力，再运行一次在 Day One 是新的条目了，有没有一天的放在一个条目的可行性？或者说不使用 Day One，用另外一个 App 记录我一天的情况。总结一下就是，希望实现：一天的内容记录在一个条目。或者实现：同样的内容（书或者科目），每天不同的进度在一个条目。

**@文刀漢三：**Day One 本身很适合用来记录自己的成长，可惜做不到你想要的功能，它的 URL Scheme 或者 Workflow 动作中没有添加到同一个条目的选项。目前实现得比较好的方案是 Evernote（或印象笔记），Evernote 在 Workflow 里有一个叫「Append to Note」的动作，可以通过匹配条目名字，然后将内容附到结尾。Bear 和 Ulysses 也有类似的动作，但是都需要通过手动获取条目的 UUID，不能自动匹配，在你这个每天都需要创建一条新条目的需求里不实用。

这个 Evernote 的 Workflow 会自动判断今天是否有创建过条目，如果当天创建过，就添加到条目结尾，如果没创建过，则自动新建一条。

[> 下载 Evernote 动作](https://workflow.is/workflows/ead0281bd15c49adb1a0cae2c60410e3)

![](.evernote-content/3F5351E4-8B64-4266-819D-A519DECD000F/94CCF22A-8F95-474C-91F1-79B413DC6D5B.jpg)

我想到的另外一个解决方案是通过原生备忘录，因为备忘录的分享部件自带添加到同条目的功能。不过备忘录的缺点是每次都需要手动选择一次，考虑到它已经是很多人的主力笔记 app，你可以考虑一下是否选择这个折中方案。

[> 下载备忘录动作](https://workflow.is/workflows/b6b1ba64f2ee450b810625f280bd9969)

![](.evernote-content/3F5351E4-8B64-4266-819D-A519DECD000F/CB060E19-FA70-4DC5-8309-E1EC7272B95D.jpg)

最后一种方案是通过 Drafts，大概思路是每天先集中记录到 Drafts，到了晚上再一次性发送到 Day One。Drafts 有扩展键盘，可以实现快速插入日期时间、进行提问等操作，所以在输入时会相对方便一些。不过因为涉及的动作比较多，「到了晚上再一次性发送到 Day One」这件事还需要有一个闹钟来提醒你，因此操作成本比较高，你可以自己考量下是否要使用这种方法。

[#Workflow](https://sspai.com/tag/Workflow)[#Power+ 定制](https://sspai.com/tag/Power+%20%E5%AE%9A%E5%88%B6)

---

[🌐 原始链接](https://sspai.com/post/40879)

[📎 在印象笔记中打开](evernote:///view/207087/s1/105ddc78-a62a-4754-a3e6-60276047d968/105ddc78-a62a-4754-a3e6-60276047d968/)