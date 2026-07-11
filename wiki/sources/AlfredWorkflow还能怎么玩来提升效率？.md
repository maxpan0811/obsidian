---
title: AlfredWorkflow还能怎么玩来提升效率？
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/AlfredWorkflow还能怎么玩来提升效率？.md
tags: [印象笔记]
---

# AlfredWorkflow还能怎么玩来提升效率？

---

Alfred Workflow还能怎么玩来提升效率？
--------------------------

原创
*2015-05-15*
*5key*
Pinapps
Pinapps

**Pinapps**
![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/B8CD85CB-CAA8-4391-A398-CF539BF9D168.sgml)

Pinapps

我推荐的不仅是apps，更是一种态度!

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/40807499-3EB7-412B-8398-325D517626A6.jpg)

日常工作中处理某件事情时经常需要一组 apps 和文件来配合完成。如果将 apps 和文件挨个点开，很可惜，你浪费了太多时间；如果你使用 Alfred 来快速其启动应用，还不错，Alfred 没白装；如果你通过创建 Workflow 一键启动工作区呢？恭喜你，你正在使用 Alfred 最精髓的部分来提升工作效率。

以Pinapps 发布文章为例，我通常需要以下 apps 来配合完成：

> 1. Sketch，进行apps的截图整理；
> 2. Photobulk，进行图片缩放或加水印；
> 3. QR Factory，将下载地址生成二维码；
> 4. 打开微信公众号后台和知乎专栏后台；

如果每一个单独打开，即使使用 Alfred 快速启动也需要敲一些键盘加上鼠标点击。但如果使用 Workflow 来帮助完成，输入预设的字母回车就搞定了。不信你看！

还是以发布文章为例，首先进入 Alfred 的设置界面并切换到 Workflow 模块。点击下方「+」添加一个空白的 Workflow，填入 Workflow 的名称方便后续管理。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/69B184A6-6E55-4A28-BAD6-D24782354FF5.jpg)

在右边黑色区域点击「+」创建触发条件，选择「Input」-「Keyword」 通过输入关键词来触发。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/29097341-61C7-43D6-B331-24E92252645E.jpg)

完成后双击这个触发模块，在 「Keyword」 一栏填写你想使用的关键词，我在这里使用的是 「PP」 也就是 Pinapps Post 的缩写。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/DCAE8A2F-DE10-4970-86A5-A8FB86F4B486.jpg)

接下来我们开始添加触发后执行的操作。在 「Action」 中进行选择，这里需要使用到的是启动应用和打开 URL。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/41E13FA3-5F99-4279-8654-8A291A57BB5E.jpg)

将刚才提到的Sketch、Photobulk和 QR Factory 拖入兑换框并保存。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/52D90526-C9CC-46EC-9EE5-AC8E91DD5FAD.jpg)

接下来添加 「Open URL」 模块，分别添加微信公众号后台和知乎专栏后台的 URL。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/763D1AA1-95CE-4C6C-8D63-9C0595CC7E86.jpg)

如果需要，这里还可以指定打开浏览器。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/B3E3E086-041F-4334-8305-6DD4657E4C6D.jpg)

最后再添加执行后的反馈。选择 「Outputs」- 「Post Notification」，填写标题和显示文本。这里没有特别限定，按需求自行填写。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/6BAE3D16-492F-486B-98F7-8AF401ACA8B2.jpg)

最后拖动各个模块将他们连接起来这个快速启动的工作区就完成了。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/514E9C47-0366-4F5E-A195-4307F8B6EE16.jpg)

当我激活 Alfred 输入 「PP」，workflow 会自动帮我加载三款应用并在 Chrome 中打开两个网站，最后再推送给我一条执行成功的信息。

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/7F4B21EC-B03C-498A-85E7-D2CCB8CA30ED.jpg)

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/177C3A65-BE9B-466F-94A3-7ABD4F09F27D.jpg)

只需要简单的几步操作，一个专属的工作区快速启动就能完成。Workflow 中的 Action 模块支持应用加载、打开 URL、系统命令、Script 语言支持等众多操作，你可以根据习惯来为自己创建各种不同的工作区。

当然，这一切必须依靠 Powerpack 的支持。如果你还没有购买，可以考虑在 Pinapps 唯一合作的应用代购服务平台 Mou.li上来购买。

公众号回复 「power」获取购买链接。

**购买 Powerpack 后还能做哪些事情呢？可以看看这几篇介绍：**

> [八个不可错过的Alfred Workflow 第三季](http://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&amp;mid=205256129&amp;idx=1&amp;sn=a208820751bc8f2dacfba19057f99fc9&amp;scene=21#wechat_redirect)
>
> [八个不可错过的Alfred Workflow 第二季](http://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&amp;mid=204714642&amp;idx=1&amp;sn=7274784bcea2831bde853bf9da567bb7&amp;scene=21#wechat_redirect)
>
> [用Alfred大幅提升操作效率 - Workflow](http://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&amp;mid=204114681&amp;idx=1&amp;sn=7622e7c34ba3cb7a2b5fcb6373d76811&amp;scene=21#wechat_redirect)

![](.evernote-content/A69E7C0A-01BC-424E-94CE-AC11258B954C/812006EF-4146-4113-981F-0FB257E53F4A.png)

阅读

  
举报

[阅读原文](http://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&mid=205527616&idx=1&sn=9913fd9af10c8694f40638bbeac8d6cf&scene=1#rd)

---

[🌐 原始链接](http://mp.weixin.qq.com/s?__biz=MzA4NTMxOTgxNg==&amp;mid=205527616&amp;idx=1&amp;sn=9913fd9af10c8694f40638bbeac8d6cf&amp;scene=1#rd)

[📎 在印象笔记中打开](evernote:///view/207087/s1/72f162e9-964a-4fec-af42-87703040739f/72f162e9-964a-4fec-af42-87703040739f/)
