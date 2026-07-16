---
title: "Github 上最火的 Google 图片批量下载工具简明教程"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Github 上最火的 Google 图片批量下载工具简明教程.md
tags: [印象笔记]
---

# Github 上最火的 Google 图片批量下载工具简明教程

# Github 上最火的 Google 图片批量下载工具简明教程 --- Github 上最火的 Google 图片批量下载工具简明教程 ==============================

---

# Github 上最火的 Google 图片批量下载工具简明教程

---

Github 上最火的 Google 图片批量下载工具简明教程
===============================

07月21日

[![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/D1878CE8-A5C3-4BFE-B159-BF82F5120B49)](https://sspai.com/user/775063)

#### [玉树芝兰](https://sspai.com/user/775063)

#### 责编: [Hum](https://sspai.com/user/681230)

批量下载图片这种事儿，不管是谁可能都要遇上那么几回。作为一名信息管理与信息系统讲师，我经常需要大量图像来训练模型，这个需求也就更强烈。

一般来说，搜图时我们都会在 Google 图片中搜索我们想要的东西。比如键入「Walle」，就能搜到皮克斯制作的动画《瓦力》的主人公：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/3F317A80-D4BB-4921-8B43-5B1E80AD3E07)

搜索的结果，合乎我们的要求。Google 不但给了咱们图片，而且标记也已经做好了，下一步只要批量下载就行了。

可就是在批量下载这一步，很多人犯了难。和各位一样，我第一个想法也是看看有没有什么现成的 Chrome 插件能批量存图，结果却发现并没有一款从准确度和操作上都足够理想的工具。

山重水复的时候，我发现了一个特别棒的 Github 项目，叫做 [google-images-download](https://github.com/hardikvasa/google-images-download "google-images-download")

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/FEF2457D-EAD6-49B0-B0B1-D894B985CE79)

项目发布至今，只有短短 5 个月的时间，星标数量已经上了 2000，看来确实非常受欢迎。

`google-images-download` 是个 Python 脚本。但\*\*使用它却不需要什么代码知识——一条命令，就完成 Google 图片搜索和批量下载功能。而且，这工具还跨平台运行，Linux, Windows 和 macOS 都支持。简直是懒人福音。

安装
--

`google-images-download` 安装很简单。以 macOS 为例，只需要在终端下，执行以下命令：

```
pip install google_images_download
```

安装就算完成了。当然，这需要你系统里已经安装了 Python 环境。如果你还没有安装，或者对终端操作命令不太熟悉，可以参考我的《[如何安装 Python 运行环境 Anaconda？（视频教程）](https://www.jianshu.com/p/772740d57576 "如何安装 Python 运行环境 Anaconda？（视频教程）")》一文，学习如何下载安装 Anaconda ，和进行终端命令行操作。

运行
--

这次我们尝试下载什么图片呢？想起《我不是药神》里面有个叫谭卓的女演员，演的不错。可是我一开始，把她当成郝蕾了。咱们就尝试下载一些谭卓的图片吧。

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/BB14005F-057C-4472-BA00-8420504B47F4)

电影《我不是药神》海报

首先，我们先指定图片要下载的位置，我把它指定到了「下载（Download）」这个文件夹：

```
cd

~/Downloads
```

然后，在终端里执行即可：

```
googleimagesdownload -k

"谭卓"

-l

20
```

这行代码中：

* `googleimagesdownload` 是命令名，告诉系统我们现在要执行什么命令，现在我们要执行的就是「googleimagesdownload」这个命令。
* `-k` 指的是「关键词（Keyword）」，所以它的后面紧跟着关键词，在这里是 `"谭卓"`，注意关键词要用半角直双引号框起来。
* `-l` 指的是「限定（limit）」，指定下载图片的数量。本例中，我们下载了 20 张。

下面是执行过程：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/AF68119E-1FE1-4F04-A106-87F2D880C1F4)

最后的 `Error: 1` 说明， 下载过程中，发生了一个错误。但程序依然正常地将下载流程运行完毕。我们来看结果：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/C5B6A043-F652-400B-AE3E-3EF14A13222E)

我们发现，下载的图片已经都存放在 `~/Downloads/downloads/谭卓` 下面。`google-images-download` 非常贴心地，为我们建立子目录。

基本上，这一行命令就能帮我们解决正常情况下，批量下载图片的需求了。

进阶
--

然而，在有的情况下，我们需要下载的图片远远大于 20 张。比如说我看了半天照片，还是分不大清楚郝蕾和谭卓。那么为了彻底分清两位女演员，我打算再下载 200 张郝蕾的照片试试。

仿照刚才的命令，执行：

```
googleimagesdownload -k

"郝蕾"

-l

200
```

然后，你会发现报错了：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/04FA9131-454F-4029-9EF9-115F25476C68)

遇到问题，不要慌。你得认真看看错误提示。注意其中出现了一个关键词：`chromedriver`。这是个什么东西呢？

我们回到 `google-images-download` 的 [github 页面](https://github.com/hardikvasa/google-images-download "github 页面")，以 `chromedriver` 为关键词进行检索。你会立即找到如下结果：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/D861B021-41A3-4E6E-B0C4-CC7F40A41D04)

原来，当我们下载的图片数量超过 100 张时，程序就必须调用 `Selenium` 和 `chromedriver` 才行。不知道它俩是啥无所谓，要了咱装就行了。

Selenium 在我们安装 `google-images-download` 的时候，就已经同时安装好了。现在我们只需要下载 chromedriver 即可，它的下载链接在 [这里](https://sites.google.com/a/chromium.org/chromedriver/downloads "这里")。

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/A94B5012-D123-42B8-8DFE-E9F40ADDB924)

下载时请注意根据自己的系统类型选择合适的版本：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/831C1C35-619A-4E07-BBEA-B390A0FC5CEE)

我这里选的是 macOS 版本。下载后，压缩包里面只有一个文件，把它解压，然后放在 `~/Downloads` 目录下。

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/394A2F78-835B-4969-8524-6DBCF6578974)

接下来我们就可以批量下载超过 100 张图片了。执行以下命令：

```
googleimagesdownload -k

"郝蕾"

-l

200 --chromedriver=

"./chromedriver"
```

我们会发现多了一个 参数 `--chromedriver`。它是用来告诉 `google-images-download` 解压后 `chromedriver` 的所在路径。这回机器勤勤恳恳，帮我们下载郝蕾的照片了：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/A4878FDD-0DF8-452E-9AF1-C9E00016FFE9)

下载完毕后发现也有一些报错，部分图片没有正确下载。但这对总体结果没有太大影响。为了保险起见，建议你设置下载数量时，多设置一些。给自己留出安全边际嘛。

最后我们再打开下载后的目录 `~/Downloads/downloads/郝蕾` 看看：

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/E0CAFAEE-44CA-4D66-9796-92D678A6AFC2)

这回，你能分清楚她俩不？

更多参数介绍
------

评分这么高的 `google-images-download` ，自然不可能只有上例中这两三个参数选项。如果你对它感兴趣，可以用 [这个链接](https://github.com/hardikvasa/google-images-download#arguments "这个链接")查看全部可用参数列表。

![](.evernote-content/3941121A-5654-42D7-B11E-5E9FDD16DDC0/0D6D74E5-7E53-49C4-B256-D978EE00448A)

我数了一下，一共有39项。篇幅所限，这里就不一一展开罗列了。但是其中几个特色参数，我还是希望提示你一下，因为你在实际工作中，很可能会觉得它们有用处。

* `--format`: 选择图片格式，例如 `jpg`, `png`, `gif` 和 `svg` 等；
* `--usage_rights`：选择图片版权，例如 `labeled-for-nocommercial-reuse` 等。如果你希望建立自己发布内容用的图片素材库，可以用这个选项，避免踩到版权的坑上，被人家狮子大开口要钱；
* `--size`：选择图片大小。假如说你对于图片分辨率有要求，可以用 `>10MP` ，只下载像素数量超过 10M 的那些图片；
* `--type`：选择图片类型。例如只想要照片，可以用 `photo` ，只想要动漫形象，可以用 `animated` ；
* `--time`：选择图片被检索的时间。假如想要过去一周的图片，可以使用 `past-7-days`；
* `--specific_site`：指定图片存储网站。可以将搜索结果，限定在某个网站域名范围内；

最后还有一个参数，是 `---safe_search`，它的作用是启用安全搜索，来保证搜索结果中，不会出现不利于精神文明建设的内容。

---

[🌐 原始链接](https://sspai.com/post/45672)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c32d61d2-0f51-4e70-a6c5-d5b22537e20f/c32d61d2-0f51-4e70-a6c5-d5b22537e20f/)