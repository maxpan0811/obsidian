---
title: 如何将从 Kindle 中国电子书商店购买的电子书备份到本地 – 书伴 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/如何将从 Kindle 中国电子书商店购买的电子书备份到本地 – 书伴 2.md
tags: [evernote, impression, yinxiang]
---

# 如何将从 Kindle 中国电子书商店购买的电子书备份到本地 – 书伴

---

如何将从 Kindle 中国电子书商店购买的电子书备份到本地
==============================

更新时间：[2023年3月11日](https://bookfere.com/post/983.html)｜ 编辑：[书伴](https://bookfere.com/post/author/bookfere)｜ 分类：[使用技巧](https://bookfere.com/category/skills)｜ [79 条留言](https://bookfere.com/post/983.html#comments)

![](.evernote-content/22430BD5-8D0D-4670-902F-0A29EE9D6A88/7E8DE37E-AE62-4217-80CE-99E0741384D2.png)

昨日亚马逊中国（amazon.cn）通过邮件向 Kindle 用户发送了关于“[Kindle 中国电子书店将于 2023 年 6 月 30 日停止运营](https://bookfere.com/post/982.html)”的业务调整通知，根据亚马逊的业务调整政策，用户需要在 2024 年 6 月 30 日之前，也就是在两年内，将自己购买的电子书下载到本地设备进行保存。

目录
--

1. [一、注意事项](https://bookfere.com/post/983.html#backup_1)
2. [二、手动下载](https://bookfere.com/post/983.html#backup_2)
3. [三、批量下载](https://bookfere.com/post/983.html#backup_3)
4. [四、移除 DRM](https://bookfere.com/post/983.html#backup_4)
5. [五、其它问题](https://bookfere.com/post/983.html#backup_5)

为确保小伙伴们的合法权益不受损害，书伴会在本文中介绍如何保全自己花钱购买的电子书。

一、注意事项
------

要备份在亚马逊中国 Kindle 电子书商店购买的电子书，最好的方式就是用网页浏览器访问亚马逊中国官网，进入“**管理我的内容和设备**”页面，通过电子书列表中提供的下载功能将电子书文件下载到本地，通常下载下来的文件是 AZW3 或 AZW 格式，含有书籍完整内容。

切忌通过 Kindle 设备直接下载电子书进行备份，这是因为 Kindle 为了优化电子书的阅读体验，会对通过此种方式下载电子书做额外处理，这会导致电子书的全部内容（如图片）不再存放在单个文件中，比如在 Kindle 的 documents 目录中常见到扩展名为 .kfx 的电子书文件。

二、手动下载
------

从亚马逊中国官方网站下载你所购买电子书的具体步骤如下图所示：

![](.evernote-content/22430BD5-8D0D-4670-902F-0A29EE9D6A88/F7DB9B8E-DA38-42FF-A44C-0EDB28812CE6.gif)

1. 访问网址 [**https://z.cn/myk**](https://z.cn/myk)，登录亚马逊中国账号；
2. 进入“**管理我的内容和设备**”页面的电子书列表；
3. 点击列表中电子书标题左侧的【…】按钮；
4. 在弹出的悬浮窗中点击“**通过电脑下载USB传输**”；
5. 选择要阅读此电子书的 Kindle 设备名称；
6. 最后点击【下载】按钮，即可将电子下载到本地。

通过上述方式下载电子书，有一个硬性条件，就是你所登录的账号名下必须有绑定的 Kindle 设备，手机、平板或电脑版 Kindle 应用都无法通过这种方式下载，只能在应用中下载电子书。

不同系统平台的 Kindle 应用存放电子书的位置不同，具体可参考以下列表：

* **Windows**：C:\Users\*YOURNAME*\Documents\My Kindle Content
* **macOS**：/Users/*YOURNAME*/Library/Application Support/Kindle/My Kindle Content/
* **Android**：/data/media/0/Android/data/com.amazon.kindle/files/

对于推送到个人文档的内容，亚马逊没有提供在线下载方式，你可以通过 Kindle 设备或应用下载个人文档，也可以通过下面提到的下载工具 Kindle\_download\_helper 批量下载个人文档。

三、批量下载
------

如果你嫌手动下载麻烦，可以尝试使用书伴为你编写的自动批量下载脚本。具体用法为：用鼠标将下面的链接拖放到网页浏览器的书签栏，访问 [http://z.cn/myk](https://z.cn/myk) 并登录你的账号，进入电子书列表，点击“**自动下载 Kindle 电子书**”书签即可。该脚本支持自动翻页，无需人工手动干预。

下载间隔 秒 ｜ 启用去重功能

[自动下载 Kindle 电子书](#)

↑ 请将此小书签拖放到浏览器书签栏使用 ↑

脚本会先等待电子书页面列表显示完整再下载，因此初次点击后需要等待一会儿，请勿重复点击。脚本默认每 20 秒下载一次，你可在拖放小书签之前通过上面的输入框修改“下载间隔”的数值，根据下载速度加大或减少间隔，以确保电子书能够下载成功。另外，你可以打开网页浏览器的开发者工具通过“控制台”（Console）查看下载详情。如果想中止下载，刷新一下页面即可。

注意，此脚本只是模拟了手动点击下载的操作，理想情况下，电子书应在设定的时间间隔内完成下载，如果网络不够通畅，加上浏览器对同时下载文件个数的限制，很可能会产生遗漏。遇到这种情况，可使用勾选了“启用去重功能”的小书签，这样运行脚本时会提示你选择已下载电子书所在的文件夹，从而在下载时检查文件夹中的电子书名，如果存在就会忽略，以达到去重功能。由于电子书列表页显示的书名和实际下载的文件名有出入，去重功能比较粗略。

![](.evernote-content/22430BD5-8D0D-4670-902F-0A29EE9D6A88/270B4890-2C81-4D7B-BCDA-FCA460019203.png)

▲ 在 Chrome 的开发者工具中查看自动下载详情

四、移除 DRM
--------

需要注意的是，亚马逊为 Kindle 电子书添加了 DRM[[1]](https://bookfere.com/post/983.html#footnote-1)，这会限制电子书的通用性，也就是说你所下载的电子书文件仅能在下载该电子书时所选择的 Kindle 设备中阅读，无法在其它电子书阅读器或电子书阅读软件阅读，即便是绑定在同一账号下的其它 Kindle 设备也是如此。

对于此问题，如果亚马逊中国持续提供内容的网络访问权，为电子书添加 DRM 的弊端还算不太明显，但是一旦出现停止网络服务这种极端情况，问题就显得比较尖锐了。由于电子书必须在某个特定设备才能阅读，如果将来你的 Kindle 设备故障失修，除非去除 DRM 保护，你将永远失去对这些你所购买的电子书的使用权限，这显然侵犯了 Kindle 用户作为消费者的权利。

Bookfere Supporter

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 24 16' data-evernote-id='38' class='js-evernote-checked'%3e%3cpath d='M10.90 4.69L10.90 5.57L3.17 5.57L3.17 7.22L3.17 7.22Q3.17 9.15 3.06 10.11L3.06 10.11L3.06 10.11Q2.95 11.07 2.58 11.92L2.58 11.92L2.58 11.92Q2.21 12.77 1.27 13.56L1.27 13.56L0.59 12.93L0.59 12.93Q2.29 11.82 2.29 8.66L2.29 8.66L2.29 4.69L6.11 4.69L6.11 2.95L7.00 2.95L7.00 4.69L10.90 4.69ZM23.00 7.34L23.00 8.22L12.80 8.22L12.80 7.34L17.55 7.34L17.55 5.53L15.12 5.53L15.12 5.53Q14.55 6.53 13.86 7.07L13.86 7.07L13.10 6.46L13.10 6.46Q14.44 5.46 14.95 3.33L14.95 3.33L15.84 3.55L15.84 3.55Q15.77 3.86 15.49 4.65L15.49 4.65L17.55 4.65L17.55 2.84L18.47 2.84L18.47 4.65L21.86 4.65L21.86 5.53L18.47 5.53L18.47 7.34L23.00 7.34ZM21.45 8.88L21.45 13.63L20.53 13.63L20.53 12.78L15.32 12.78L15.32 13.63L14.41 13.63L14.41 8.88L21.45 8.88ZM15.32 11.90L20.53 11.90L20.53 9.76L15.32 9.76L15.32 11.90Z'%3e%3c/path%3e%3c/svg%3e)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 15 15' data-evernote-id='41' class='js-evernote-checked'%3e%3cpath d='M3.25%2c3.25l8.5%2c8.5M11.75%2c3.25l-8.5%2c8.5'%3e%3c/path%3e%3c/svg%3e)

了解详情

重播

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='48' height='48' viewBox='0 0 48 48' fill='%23fff' data-evernote-id='46' class='js-evernote-checked'%3e%3cpath d='M-838-2232H562v3600H-838z' fill='none'%3e%3c/path%3e%3cpath d='M16 10v28l22-14z'%3e%3c/path%3e%3cpath d='M0 0h48v48H0z' fill='none'%3e%3c/path%3e%3c/svg%3e)

![](.evernote-content/22430BD5-8D0D-4670-902F-0A29EE9D6A88/6E4C1D2B-C839-4CEA-8AC7-B1F53EABEA9E.png)

了解详情

要去除电子书的 DRM 保护，这里推荐使用软件组合：**Calibre + DeDRM 插件**，即先安装 Calibre，再为 Calibre 安装 DeDRM 插件，即可利用 [Kindle 设备序列号](https://bookfere.com/post/200.html)为电子书移除 DRM（注意，如果你有多台 Kindle 设备，且不确定下载的电子书用的是哪一台，最好是将它们的序列号都添加到 DeDRM 的设置中。上面的电子书自动下载脚本使用的是默认选择的 Kindle 设备）。

* **下载 Calibre**：[官方下载页面](https://calibre-ebook.com/download) ｜ [Github 发布页](https://github.com/kovidgoyal/calibre/releases)
* **下载 DeDRM 插件**：[分叉版本](https://github.com/noDRM/DeDRM_tools/releases) ｜ [原始版本](https://github.com/apprenticeharper/DeDRM_tools/releases)（已停止维护）

\* 提示：用电脑或移动 Kindle 应用所下载电子书，去除 DRM 的方式有所不同，详情可参考 DeDRM 的 [Wiki 页面](https://github.com/apprenticeharper/DeDRM_tools/wiki/Exactly-how-to-remove-DRM)。

注意，移除 DRM 是为了维护自己的合法权益，为避免触犯版权方的权益，请勿分发到互联网上。为保护个人隐私及电子书文件不被外泄，建议避免使用任何在线形式的 DRM 去除工具。

五、其它问题
------

如果你没有 Kindle 设备，仅使用手机、平板或电脑版 Kindle 应用购买电子书，目前没有特别好的方法可以保全你所购买的电子书，在亚马逊中国停止服务后，你需要确保安装了 Kindle 应用的设备无恙，且没有误删 Kindle 应用。对于此类用户建议向亚马逊中国提出保全诉求。

1. [[1]](https://bookfere.com/post/983.html#footnote-1-back) DRM（Digital rights management），数字版权管理是对数字内容的合法访问的管理，常用来限制版权作品的使用。[via](https://en.wikipedia.org/wiki/Digital_rights_management)

© 「[书伴](https://bookfere.com/)」原创文章，转载请注明出处及原文链接：<https://bookfere.com/post/983.html>

—延伸阅读—
------

* [Ebook Translator：用 Calibre 翻译多语言多格式的电子书](https://bookfere.com/post/1057.html "Ebook Translator：用 Calibre 翻译多语言多格式的电子书")
* [读书三弊：细说三种不正确的读书方法和态度](https://bookfere.com/post/378.html "读书三弊：细说三种不正确的读书方法和态度")
* [[每周一书]《疾病的隐喻》揭露疾病的社会属性](https://bookfere.com/post/586.html "[每周一书]《疾病的隐喻》揭露疾病的社会属性")
* [[每周一书]《金融投资 400 年》群众心理与经验教训](https://bookfere.com/post/956.html "[每周一书]《金融投资 400 年》群众心理与经验教训")
* [在 Kindle 中阅读 EPUB 格式电子书的两种有效方法](https://bookfere.com/post/445.html "在 Kindle 中阅读 EPUB 格式电子书的两种有效方法")
* [鲁迅的读书态度：请教别人是大抵无用](https://bookfere.com/post/420.html "鲁迅的读书态度：请教别人是大抵无用")
* [[网友投稿]《效率脑科学》读书笔记：情绪的产生机制](https://bookfere.com/post/1027.html "[网友投稿]《效率脑科学》读书笔记：情绪的产生机制")
* [图解 Kindle Paperwhite 电子书阅读器工作原理](https://bookfere.com/post/592.html "图解 Kindle Paperwhite 电子书阅读器工作原理")
* [[每周一书]《敢问路在何方》杨洁的 30 年西游路](https://bookfere.com/post/526.html "[每周一书]《敢问路在何方》杨洁的 30 年西游路")
* [想读书却读不进去，如何重燃阅读的激情？](https://bookfere.com/post/259.html "想读书却读不进去，如何重燃阅读的激情？")
* [亚马逊中国总裁内部信：斥“收购”为荒谬的传言](https://bookfere.com/post/443.html "亚马逊中国总裁内部信：斥“收购”为荒谬的传言")
* [[每周一书]《稀缺》我们是如何陷入贫穷与忙碌的？](https://bookfere.com/post/381.html "[每周一书]《稀缺》我们是如何陷入贫穷与忙碌的？")
* [[2016.03.08] Kindle 阅读器固件升级至 5.7.3](https://bookfere.com/post/330.html "[2016.03.08] Kindle 阅读器固件升级至 5.7.3")
* [[每周一书]《大空头》讲述金融世界的游戏规则](https://bookfere.com/post/877.html "[每周一书]《大空头》讲述金融世界的游戏规则")
* [[2016.12.01] Kindle 阅读器固件升级至 5.8.7](https://bookfere.com/post/473.html "[2016.12.01] Kindle 阅读器固件升级至 5.8.7")
* [免越狱更换 Kindle Paperwhite 2 代屏保](https://bookfere.com/post/8.html "免越狱更换 Kindle Paperwhite 2 代屏保")

[📎 在印象笔记中打开](evernote:///view/207087/s1/97da07f2-3604-4ccc-b335-70166287bc52/97da07f2-3604-4ccc-b335-70166287bc52/)
