---
title: 如何用 DeDRM 破解去除 AZW3 格式电子书 DRM 保护 – 书伴 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/如何用 DeDRM 破解去除 AZW3 格式电子书 DRM 保护 – 书伴 2.md
tags: [evernote, impression, yinxiang]
---

# 如何用 DeDRM 破解去除 AZW3 格式电子书 DRM 保护 – 书伴

---

如何用 DeDRM 破解去除 AZW3 格式电子书 DRM 保护
================================

更新时间：[2023年3月13日](https://bookfere.com/post/6.html)｜ 编辑：[书伴](https://bookfere.com/post/author/bookfere)｜ 分类：[辅助软件](https://bookfere.com/category/skills/software)｜ [56 条留言](https://bookfere.com/post/6.html#comments)

由于去除 Kindle 电子书的 DRM 保护需要用到 Kindle 设备序列号，因此请确保要下载到电子书时选择的是这台 Kindle 设备，本方法不适用于他人购买的或其它非自购来源的电子书。

“

目录

[一、什么是电子书的 DRM？](https://bookfere.com/post/6.html#rd1)

[二、为何要破解去除 DRM？](https://bookfere.com/post/6.html#rd2)

[三、去除 DRM 准备工作](https://bookfere.com/post/6.html#rd3)

[1、下载软件 DeDRM tools](https://bookfere.com/post/6.html#rd3_1)

[2、准备待移除 DRM 的电子书](https://bookfere.com/post/6.html#rd3_2)

[3、记下 Kindle 设备的序列号](https://bookfere.com/post/6.html#rd3_3)

[四、去除 DRM 详细步骤](https://bookfere.com/post/6.html#rd4)

[1、Calibre 插件版 DeDRM 操作步骤](https://bookfere.com/post/6.html#rd4_1)

[2、macOS 独立版 DeDRM 操作步骤](https://bookfere.com/post/6.html#rd4_2)

[3、Windows 独立版 DeDRM 操作步骤](https://bookfere.com/post/6.html#rd4_3)

[五、常见问答](https://bookfere.com/post/6.html#rd5)

[1、为何电子书移除 DRM 后不显示图片？](https://bookfere.com/post/6.html#rd5_1)

一、什么是电子书的 DRM？
--------------

DRM，全称 Digital Rights Management（数字版权管理），是随着电子音频视频节目在互联网上的广泛传播而发展起来的一种技术。出版者利用这些技术保护数字化内容（例如：软件、音乐、电影）以防止被非法复制，或者在一定程度上使复制很困难，使得最终用户必须得到授权后才能使用数字媒体。总的来说，DRM 是为了保护电子书版权而使用的一种限制性技术。[via](http://zh.wikipedia.org/wiki/%E6%95%B0%E5%AD%97%E7%89%88%E6%9D%83%E7%AE%A1%E7%90%86)

二、为何要破解去除 DRM？
--------------

先举个例子，我从亚马逊购买了一本电子书，尝试使用 Calibre 软件把这本电子书的 AZW 格式文件换成 mobi 格式时，会弹出如下图所示的错误提示，无法转换格式也无法阅读：

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/7CE276E3-1E90-499A-8838-D2A0B88D9239.png)

在美国亚马逊（美亚）或日本亚马逊（日亚）购买的 Kindle 设备（如 Kindle 4、Kindle 5）是无法绑定中国亚马逊账号的，这就导致在中国亚马逊购买的电子书不能通过正常推送渠道推送电子书，同样，在美亚日亚购买的电子书也无法推送到绑定中国亚马逊账号的Kindle中。

为了保护电子书的版权，亚马逊为其提供的 AZW 或 AZW3 格式电子书文件添加了 DRM，使得非购买者即便获取到这些电子书文件，也无法直接在其他阅读器或阅读设备上使用。比如你在亚马逊买到一本电子书，想要共享给自己的亲朋好友，或拷贝到另外一台 Kindle 设备，但由于 DRM 的存在，其它的 Kindle 设备就无法阅读了。为了突破这种限制就需要移除 DRM。

三、去除 DRM 准备工作
-------------

移除电子书文件的 DRM 保护，这里推荐使用 DeDRM Tools。首先，我们需要准备好相关软件、你购买的带 DRM 保护的电子书，以及绑定了亚马逊账号的 Kindle 设备的序列号。

#### 1、下载软件 DeDRM tools

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/EE1D6A85-5340-4969-9380-32ED3C468A5C.png)

将下载来下的压缩包 DeDRM\_tools-master.zip 解压备用。

* **DeDRM tools 分叉版**：[GitHub 发布页面](https://github.com/noDRM/DeDRM_tools/releases)
* **DeDRM tools 原始版**：[GitHub 发布页面](https://github.com/apprenticeharper/DeDRM_tools/releases)\* 已停止维护，Calibre 插件版仅适用于 5.0 以下的版本

DeDRM tools 的 macOS 和 Windows 独立版仅原始版的 [6.6.3](https://github.com/apprenticeharper/DeDRM_tools/releases/tag/v6.6.3) 及更老的版本提供。

**\* 提示**：在 Windows 系统中运行 DeDRM\_Drop\_Target.bat 时如果出现“找不到 Python”之类的提示，请务必确保您的系统安装了 [**Python**](https://www.python.org/downloads/) 和 [**PyCrypto**](https://pypi.org/project/pycrypto/)。

#### 2、准备待移除 DRM 的电子书

把需要破解的 AZW 或 AZW3 格式的电子书获取到本地，获取方式有以下几种：

**① 第一种获取电子书的方法：从亚马逊云端下载（推荐）**

进入亚马逊后台的 [我的内容](https://www.amazon.cn/mn/dcw/myx.html/ref=kinw_myk_redirect#/home/content/booksAll/dateDsc/)（用绑定 Kindle 的亚马逊账号登录），找到想要破解的那本书，点击电子书旁边的【**…**】按钮，在弹出的菜单中点击【**通过电脑下载 USB 传输**】，选择你的 Kindle 设备，点击【**下载**】按钮把电子书下载到电脑中，然后再按照本文的方法进行破解即可。

**② 第二种获取电子书方法：从 Kindle 阅读软件的目录中拷贝。**

这一种方法需要安装 Kindle 桌面客户端软件。如果没有安装请先在下面的列表中选择合适您的系统版本安装。安装完成后打开软件，用你的亚马逊账号登录，然后下载想要破解的电子书，再从相应电子书存放路径中找到它们（文件名类似于“B0080BKP1K\_EBOK.azw”这种），请将它们拷贝到如桌面等任意位置备用。

适用于 Windows 系统的 Kindle 阅读软件：

* **Kindle for Windows 版**：[官方下载](http://www.amazon.cn/kindlepcdownload) | [百度网盘](http://pan.baidu.com/s/1kTHqGg3)
* **电子书存放路径**：C:\Users\*[你的用户名]*\Documents\My Kindle Content

适用于 macOS 系统的 Kindle 阅读软件：

* **Kindle for Mac 版**：[官方下载](https://itunes.apple.com/cn/app/kindle-dian-zi-yue-du-qi-ke/id302584613?mt=8) | [百度网盘](http://pan.baidu.com/s/1hq1NLWC)
* **电子书存放路径**：/Users/*[你的用户名]*/Library/Application Support/Kindle/My Kindle Content

**③ 第三种获取电子书方法：直接从 Kindle 阅读器中拷贝。**

用USB线将 Kindle 连接到电脑，打开 Kindle 驱动器，在根目录里的 Documents 文件夹内找到 AZW 或 AZW3 格式的电子书文件将其拷贝出来。这种方法现在不建议使用，因为最新版本固件已经将下载到 Kindle 中的电子书中的图片抽离出去，导致用此方法复制的电子书缺失图片。

#### 3、记下 Kindle 设备的序列号

Kindle 序列号可以在包装盒或保修单上找到，没有包装盒或保修单的话也可以在系统里找到，具体方法可参考《[如何查看 Kindle 序列号以及查询 Kindle 设备的型号和批次](https://bookfere.com/post/200.html)》。

四、去除 DRM 详细步骤
-------------

做完以上准备工作就可以开始破解操作了。下面的操作步骤包含三个部分，分别是 Calibre 插件及适用于 macOS 系统和 Windows 系统的独立版软件，你可根据自己的喜好选择使用。

#### 1、Calibre 插件版 DeDRM 操作步骤

如果你习惯使用 [Calibre](https://bookfere.com/tools#calibre)）管理电子书，结合 DeDRM 插件移除 DRM 就更简单了，只需要在插件设置中填入你的 Kindle 序列号，就可以直接将 AZW 或 AZW3 格式的文件拖入 Calibre 即可自动移除 DRM。

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/470A874F-575B-415E-963F-4EB7CCEADFE3.png)

导入插件详细步骤：

1. 打开 Calibre，点击菜单中的【**首选项**】，在高级选项区域点击【**插件**】
2. 点击右下角的【**从文件加载插件**】，选择刚才解压的文件 DeDRM\_tools-master/DeDRM\_calibre\_plugin/**DeDRM\_plugin.zip**。
3. 再“文件类型 插件”中双击刚刚导入的插件，在弹出的窗口中点击【**eInk Kindle ebooks**】按钮，在新弹出的对话框中点击右侧的【**+**】按钮，在弹出的对话框中的【**EInk Kindle Serial Number**】一栏里输入你的 Kindle 序列号。然后一路确定、关闭、确定。
4. 应用更改后，重新启动 Calibre，插件即可生效，把带 DRM 的电子书拖入书库即可完成破解。

#### 2、macOS 独立版 DeDRM 操作步骤

打开刚才解压的 DeDRM\_tools-master 文件夹，进入 DeDRM\_Macintosh\_Application 目录，双击打开 DeDRM，界面如下图所示， 点击界面右下角【**Configure…**】

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/425B9D98-DF28-46D2-B5B0-22378010BB00.png)

在弹出的窗口中选中第一项【**eInk Kindle ebooks**】，然后点击【**Configure…**】（也可以双击【**eInk Kindle ebooks**】这一项）。

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/1AD8013B-D6FF-4874-B86A-F08C2D9D6834.png)

在弹出的窗口中输入你的 Kindle 序列号，点击【**Add**】按钮。

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/71D9B65A-36B4-47B2-89A0-2F0D5D010845.png)

返回主界面后，点击界面下方的【**Select Ebook**】，选择刚才拷贝的那个 AZW 或 AZW3 文件，点击确定即可完成破解。

#### 3、Windows 独立版 DeDRM 操作步骤

打开刚才解压的 DeDRM\_tools-master 文件夹，进入 DeDRM\_Windows\_Application\DeDRM\_App 目录，双击打开 DeDRM\_Drop\_Target.bat，出现如下界面：

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/76CC211B-640D-4E71-B416-2820E696C129.png)

在【**eInk Kindle Serial Number list**】一栏中填写你的 Kindle 序列号，然后点击下方的【Set Prefs】按钮保存。接下来，点击界面下面的【**Select an eBook to Process**】一栏后面的【**…**】按钮，选择电子书，点击【**Process eBook**】即可完成破解。

五、常见问答
------

#### 1、为何电子书移除 DRM 后不显示图片？

请检查一下未破解前的 AZW3 文件和破解后的 AZW3 文件大小是否相同，如果相同说明这并非破解导致的问题，而是在没破解前图片就已经不存在了。这这可能是因为亚马逊的新的处理机制的问题，推送到 Kindle 的电子书内容和图片被分离了，从而导致直接从 Kindle 中复制出来的 AZW3 文件不包含图片。如遇到此问题，请进入亚马逊后台的 [我的内容](https://www.amazon.cn/mn/dcw/myx.html/ref=kinw_myk_redirect#/home/content/booksAll/dateDsc/)（用绑定 Kindle 的亚马逊账号登录），找到想要破解的那本本书，点击电子书旁边的【**…**】按钮，在弹出的菜单中点击“**通过电脑下载USB传输**”把电子书下载到电脑中，再按照本文的方法进行破解即可。

![](.evernote-content/3679B3F6-63C1-4E12-8A6A-5F89C206D971/65C0E89B-1074-48AB-9095-1592AB628CE4.png)

© 「[书伴](https://bookfere.com/)」原创文章，转载请注明出处及原文链接：<https://bookfere.com/post/6.html>

—延伸阅读—
------

* [Ebook Translator：用 Calibre 翻译多语言多格式的电子书](https://bookfere.com/post/1057.html "Ebook Translator：用 Calibre 翻译多语言多格式的电子书")
* [[每周一书] 全面了解睡眠《我们为什么要睡觉》](https://bookfere.com/post/930.html "[每周一书] 全面了解睡眠《我们为什么要睡觉》")
* [[2021.03.17] Kindle Paperwhite 3 固件升级至 5.13.5](https://bookfere.com/post/890.html "[2021.03.17] Kindle Paperwhite 3 固件升级至 5.13.5")
* [ABBYY FineReader：把扫描版 PDF 转换成文本](https://bookfere.com/post/239.html "ABBYY FineReader：把扫描版 PDF 转换成文本")
* [亚马逊推出第三代 Kindle Oasis（KO3）可调节阅读灯色温](https://bookfere.com/post/761.html "亚马逊推出第三代 Kindle Oasis（KO3）可调节阅读灯色温")
* [[2018.06.06] Kindle 阅读器固件升级至 5.9.6](https://bookfere.com/post/654.html "[2018.06.06] Kindle 阅读器固件升级至 5.9.6")
* [中亚 2018 全民阅读报告：解读六大阅读行为趋势](https://bookfere.com/post/636.html "中亚 2018 全民阅读报告：解读六大阅读行为趋势")
* [[每周一书]《凤凰项目》写给 IT 从业者的项目管理故事](https://bookfere.com/post/740.html "[每周一书]《凤凰项目》写给 IT 从业者的项目管理故事")
* [Kindle 阅读器“生词本”功能详细使用说明](https://bookfere.com/post/465.html "Kindle 阅读器“生词本”功能详细使用说明")
* [三步搞定！Kindle Paperwhite 2 越狱教程](https://bookfere.com/post/33.html "三步搞定！Kindle Paperwhite 2 越狱教程")
* [[每周一书]《为什么读经典》卡尔维诺的阅读世界](https://bookfere.com/post/862.html "[每周一书]《为什么读经典》卡尔维诺的阅读世界")
* [让 Kindle 电子书下乡能消除城乡数字鸿沟吗？](https://bookfere.com/post/447.html "让 Kindle 电子书下乡能消除城乡数字鸿沟吗？")
* [[每周一书] 关于美的通识教育《艺术的故事》](https://bookfere.com/post/822.html "[每周一书] 关于美的通识教育《艺术的故事》")
* [[2016.02.13] Kindle 固件升级至修订版本 5.7.2.1](https://bookfere.com/post/309.html "[2016.02.13] Kindle 固件升级至修订版本 5.7.2.1")
* [百度与亚马逊中国合作，成 Kindle 默认搜索](https://bookfere.com/post/252.html "百度与亚马逊中国合作，成 Kindle 默认搜索")
* [[每周一书]《饱食穷民》泡沫经济时代的日本社会](https://bookfere.com/post/873.html "[每周一书]《饱食穷民》泡沫经济时代的日本社会")

[📎 在印象笔记中打开](evernote:///view/207087/s1/fc31486c-4cbf-4a40-a23a-885e9f80f07a/fc31486c-4cbf-4a40-a23a-885e9f80f07a/)
