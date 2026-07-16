---
title: "在 Alfred 上实现 Launchbar 的 Instant Send"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/在 Alfred 上实现 Launchbar 的 Instant Send.md
tags: [印象笔记]
---

# 在 Alfred 上实现 Launchbar 的 Instant Send

# 在 Alfred 上实现 Launchbar 的 Instant Send --- 在 Alfred 上实现 Launchbar 的 Instant Send ==================

---

# 在 Alfred 上实现 Launchbar 的 Instant Send

---

在 Alfred 上实现 Launchbar 的 Instant Send
=====================================

08月10日

[![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/8698C24B-014F-4D01-A2B5-B766BC4845AA)](https://sspai.com/user/728619)

#### [AFuture](https://sspai.com/user/728619)

在日常使用 Mac 时，把文字 / 文件从 A 应用发送到 B 应用是一个非常高频的操作。例如，浏览学术文档时，发现不熟悉的名词，你会打开浏览器，然后在搜索引擎里输入搜索一下；或者，查看照片时，如果想用 Photoshop 进行后期，你会打开 Photoshop，然后把照片从 Finder 里拖动到 Photoshop 里进行操作；对于开发者，调试网站时想把当前的网页换个浏览器测试，于是你会复制网址，然后在另一个浏览器里粘贴打开。

虽然「输入」「拖动」和「复制粘贴」都不是非常复杂的操作，但如果每天都要执行很多次的话，我们自然希望能有更高效的解决办法。macOS 上的效率启动器应用 Launchbar 里有一个名为 Instant Send 的功能，通过设置简单的快捷键，每次只需一次按键就能快速地把文字 / 文件发送到指定应用中打开，大大提高了操作效率。

![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/995BF74E-6975-4398-973F-29F3D316B031)

双击 Control 触发，然后直接将文件用 AirDrop 分享

除了 Launchbar，提到 macOS 上的效率启动器，Alfred 也是很多人的选择。遗憾的是，虽然 Alfred 拥有各种强大的功能和非常优秀的拓展性，但它并没有集成类似 Instant Send 这样的功能。在尝试了一段时间后，我找到了一个在 Alfred 实现 Instant Send 的方法。

（注：本文中提到的功能需要首先购买 Alfred 的 Powerpack。）

思路
--

在 Alfred 中达到 Instant Send 需要以下几个条件：

1. 能够通过快捷键触发 Alfred，打开启动器。
2. 触发 Alfred 的同时，Alfred 可以获取到我们选择的文本或文件；
3. 将文本 / 文件作为输出参数传递给 Alfred 的 Workflow 和 Action，进行下一步操作。

根据以上条件，我们可以通过制作一个 Workflow 来实现这些功能。

实现方法
----

查阅了官方的文档后，我找到了一个名为「Hotkey」的 Trigger（触发器） ，它能够获取选择的文本或者文件目录，并作为参数传到 Workflow 中。这正好对应了我们思路中提到的 3 点。我们可以围绕它来制作相应的 Workflow。

在 Alfred 中想要达到与 Instand Send 相同的效果需要分两步：第一步触发 Alfred、第二步执行操作或 Workflow。

### 触发 Alfred

首先新建一个名为 「Instant Send」的 Workflow ，接着在空白的 Workflow 配置中添加 Trigger。 依次**「鼠标右击 - Trigger - Hotkey」**，并按照以下条件配置：

* Hotkey：触发 Alfred 的快捷键组合。这里我设置了符合我自己的快捷键**「double tap ⇧」** 。
* Action：触发后的效果。可选的有「Show Alfred」和「Pass through to workflow」，由于需要显示启动器，那么我们就选择「Show Alfred」。
* Argument：参数类型。可选的有「None」「Selection in macOS」「macOS Clipboard contents」和「text」。根据条件 2，我们需要这个 Workflow 可以获取到我们选择的文本或文件，于是选择「Selection in macOS」。
* Prefix：在参数前添加的前缀字符，不需要填写。
* Cursor：展示启动器后光标出现的位置。为了方便输出动作，我们当然会选择「Left」而不是「Right」。

![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/090B2ECA-2E29-4106-8D6A-C50A607168F0)

配置参考图

至此，Instant Send 的基础部分就已经实现了。你现在就可以用它来试验一下，例如把你选择的文字发送到浏览器里进行搜索：

![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/F9A2C142-F6AA-4E4B-B34A-749A8798DCEC)

### 执行动作或 Workflow

上面我们已经实现了在 Alfred 里使用 Instant Send 的大部分功能。如果你只需要简单地进行文字发送，这个 Workflow 已经可以正常使用了，不需要额外地配置。

![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/6841C20A-E48D-407C-B428-3D8B39151BFE)

正常使用的场景

不过，为了能让它用起来更顺手，我们接下来可以继续完善这个 Workflow，需要配置的内容有：

* 无匹配结果后展示的默认动作
* 继续执行文件相关的操作

#### 设置默认动作

这个配置主要的目的是，当获取的信息输入到启动器时，如果没有可以执行的操作，则显示默认的一些动作用于快速访问。

在Alfred Preference 的 Features 中找到 Default Results，在右侧底部找到 Setup fallback results，然后添加新的动作。

非 Powerpack 用户只能使用「Web Search」这一个动作，Powerpack 用户可在 Workflow 中添加「Fallback Search」Trigger 来设置更多自定义的默认动作。

![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/F37641C5-AD40-4A97-8747-FA4976A1FC46)

#### 执行文件相关的操作

在之前制作的 Workflow 中，当选择文件触发时，Alfred 的启动器只能获取到文件的路径，如何才能进行和文件相关的操作呢？

答案是在「File Search」中设置动作触发按键。

在 Features 中找到 File Search，选择 Actions，在 Show Actions 中选择一个触发按键。你可以跟我一样使用 「Tab」 作为触发键，这样你可以使用 「←」和「→」作为文件导航键。

![](.evernote-content/BD1D4221-EE36-4AE4-B521-4B4AA5E0EFD9/EAA4D0BF-B4DD-4BE5-92FE-3937BDEDE55B)

与「默认动作」类似，非 Powerpack 用户只能使用已经含有的文件动作，如：打开、使用其它应用打开、在 Finder 中查看、复制文件名到剪切板等。Powerpack 用户可在 Workflow 中添加「File Action」Trigger 以设置更多自定义的文件动作。

下载少数派 [客户端](https://sspai.com/page/client "客户端")、关注[少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，了解更多效率工作的好方法

---

[🌐 原始链接](https://sspai.com/post/46088)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e5c4085f-4c76-4c3b-9bcf-33b3158136e4/e5c4085f-4c76-4c3b-9bcf-33b3158136e4/)