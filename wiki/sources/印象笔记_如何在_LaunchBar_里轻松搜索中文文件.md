---
title: "如何在 LaunchBar 里轻松搜索中文文件"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在 LaunchBar 里轻松搜索中文文件.md
tags: [印象笔记]
---

# 如何在 LaunchBar 里轻松搜索中文文件

# 如何在 LaunchBar 里轻松搜索中文文件 --- 如何在 LaunchBar 里轻松搜索中文文件 ======================= | 本文为付费栏目文章，您已订阅，可阅读全文

---

# 如何在 LaunchBar 里轻松搜索中文文件

---

如何在 LaunchBar 里轻松搜索中文文件
=======================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

LaunchBar 缺失的最后一颗无限宝石
---------------------

在 LaunchBar 中可以通过简单的几个字母检索其包罗万象的各种功能，包括程序、动作、服务、文字片段、网络搜索模板等等。同样，在搜索以拉丁字母为文件名的文件时，LaunchBar 的表现也非常出色。然而，对于中文用户来说，LaunchBar 无法搜索中文文件名的文件，无疑是使用上一个巨大的痛点，这堪称 LaunchBar 的阿喀琉斯之踵。在少数派的 LaunchBar 教程评论区，以及在 Power+ 的 Slack 讨论组里，经常有朋友抱怨这个问题，这甚至成为他们拒绝尝试或者放弃使用 LaunchBar 的一个重要原因。

而 macOS 原生的搜索工具 Spotlight（中文译名 **聚焦**，但本文中统称 Spotlight）可以对各类文件进行全盘搜索，并迅速得到搜索结果。在搜索文件，尤其是文件名为中文的文件时，你可能会经常用到它。

本文提供了一个使 LaunchBar 集成 Spotlight 文件检索功能的方案，
使其可以直接搜索文件名为 **任何语言** 的文件，
以补齐 LaunchBar 这个 macOS 平台上的无限手套的最后一颗无限宝石。

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/6D714328-1907-4312-AFDF-115FB90D8BA9.gif)

在 LaunchBar 中借助 Spotlight 进行中文文件名的搜索

实现方案
----

这个功能通过如下两个动作实现，点击即可下载：

* [Search Files by Name](https://cdn.sspai.com/minja/search_files_by_name.zip)：根据文件名搜索文件；
* [Search Files by Contents](https://cdn.sspai.com/minja/search_files_by_contents.zip)：根据文件内容搜索文件。

### 基础使用方法

其使用方法比较简单，选定动作后直接输入关键词即可。其支持多个关键词，中间用空格隔开即可。例如，要搜索文件名中包含 `插图` 的 PNG 图片文件，则在动作 **Search Files by Name** 中直接输入 `插图 .png`。在列出的搜索结果中，可以进行进一步的操作。
例如下图中，筛选出名称中含有 `STU` 字样的图片，并用 Pixelmator 打开以进行编辑。

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/831365EA-CA31-4B80-851F-C51EED75BA2C.gif)

将搜索得到的图片文件用 Pixelmator 打开

同样，也可以把选中的文字通过 Instant Send 发送到这两个动作进行搜索，其效果见下节的两个实例。

### 进阶使用方法

同时，也可以使用 Spotlight 的搜索语法，即添加 **元数据属性** 1  条件来缩小搜索范围。例如，要搜索特定类型的文件：

* 如只搜索文件名包含「**插图**」的 **图片**，则在 **Search Files by Name** 中输入 `插图 kind:image`。  

  ![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/2967CAB7-AA8D-40FB-B9B8-64A3B43D27B4.gif)

  限定搜索图片

* 如只搜索文件内容中包含「**契丹**」的 **文档**，则在 **Search Files by Contents** 中输入 `契丹 kind:document`。  

  ![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/99554540-F615-49C1-9C57-7D072DE77576.gif)

  限定搜索文档

其它根据元数据的搜索实例请参见 Apple 官方的介绍：[缩小在 Spotlight 和 Finder 中的搜索范围](https://support.apple.com/kb/PH25589?locale=en_US&viewlocale=zh_CN)。

分配快捷键
-----

在 LaunchBar 中也能够为某些常用的功能设立独立的快捷键，如下图中所示的 **Search in Spotlight**（使用 Spotlight 搜索）、**Snippets**（片断）、**Emoji**、**Calculator**（计算器）、**Show clippboard history**（剪贴板历史）：

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/05BE8CED-35FA-47EE-855F-7D9605982FD3.png)

在 LaunchBar 设置中可以为其常用功能分配独立快捷键

搜索文件也是一个常用的功能，如果像上述动作一样，也为这个搜索文件的动作分配一个快捷键，无疑更加方便。下面列举两种常用的方法，可以从中选择一种进行配置。

### 借助 Automator 分配快捷键

可以通过系统原生的自动化应用 Automator（中文译名 **自动操作**）分配快捷键。步骤如下：

1. 启动 Automator，新建一个 **快速操作**（Quick Action）；
2. 如下图中左边的窗口所示，添加一个 **Perform Action**，其中填写 **Search Files by Name**，意即运行 LaunchBar 中的这个动作；
3. 直接保存，命名为 **Search Files by Name in LaunchBar**，退出；
4. 在系统设置的 **键盘** 中，依次选择 **快捷键** → **服务**，在右侧列表中的 **通用** 分类中可以看到刚刚建立的 **Search Files by Name in LaunchBar** 服务，为其分配快捷键，如 `⌃⌥⌘ 空格`，即可。  

   ![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/0CE886A1-0A86-4151-A224-63650BCBCA53.png)

   借助 Automator 为 LaunchBar 动作分配快捷键

### 借助 Keyboard Maestro 分配快捷键

我们也可以借助 Keyboard Maestro 来实现。在 Keyboard Maestro 中新建一个如下 Macro（宏）：

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/9A47A7B9-D1AC-4874-B3C7-260D16C2DB9D.png)

借助 Keyboard Maestro 为 LaunchBar 动作分配快捷键

这个 Macro 也只包含一个动作，即运行一小段 AppleScript 代码，其内容如下：

```
tell application "LaunchBar"
    perform action "Search Files by Name"
end tell
```

其含义一目了然，即「告诉应用程序 LaunchBar 运行名为 **Search Files by Name** 的动作」。

用相同的方法，亦可以为 **Search Files by Contents** 动作分配一个快捷键。

作为 SearchBar 应有的形态
------------------

至此，我们通过这两个动作拓展了 LaunchBar 的文件搜索能力，让它在文件搜索这个方面更接近了 [@Minja](https://sspai.com/user/731139) 在 Power+ 讨论组中谈到的「**SearchBar**」。

既然 Spotlight 就可以实现高效的文件搜索，那么我们为什么要把 Spotlight 的搜索功能集成到 LaunchBar 中呢？当我们在谈论用 LaunchBar 进行文件搜索时我们在谈论什么？

我们先回顾一下本文前面 **基础使用方法** 小节中描述的搜索文件的常见场景：当我们通过 LaunchBar 搜索到一批符合结果的文件后，可以直接对搜索结果进行进一步的检索筛选，之后，还可以把选中的若干文件按 `Tab` 键发送给某个软件进行进一步的处理（例如此例中将某张图片用 Pixelmator 打开以进行编辑）。

这个操作步骤中涉及到的 **二级检索** 和 **发送** 这两个功能可以说是 LaunchBar 众多强大的功能中最基础的两项：

* **二级检索** 是指在进行完一次检索后，在其所列出的结果中进行进一步的筛选检索。在进行 **全局检索** 时，选中的项目为蓝色高亮，二级检索时，选中的项目为橙色高亮。
* **发送** 是指在选中项目之后按 `Tab` 键将其发送给某个目录 / 程序 / 动作 / 服务 / 工作流 / 搜索模板等功能，如：
  + 将若干个文件发送（复制或剪切）至某个目录；
  + 将某个网址链接发送至 Chrome 以打开；
  + 将一段文字发送给翻译动作以进行翻译；
  + 将一个地址发送给谷歌地图以打开。

因此，当我们在谈论用 LaunchBar 进行文件搜索时，我们谈论的往往是快速找到目标文件并流畅地进行后续操作，这正是我们想把 LaunchBar 作为「SearchBar」的重要原因。

然而，由于 LaunchBar 原生不具备搜索中文文件名的能力，当需要使用 LaunchBar 对这些文件进行操作时，我们往往不得不先在 Finder 中按快捷键 `⌘ F` 搜索到所需的文件，再通过 **快速发送** （Instant Send）将搜索结果传递至 LaunchBar，以在 LaunchBar 中进行下一步的操作，这种割裂的操作方式打断了 LaunchBar 的流畅性。

其实，LaunchBar 中自带了一个 **Search in Spotlight** 的动作，可以使用 Spotlight 查找文件。但其使用效果是在 LaunchBar 中输入关键词后离开 LaunchBar，再在 Finder 中列出所搜索结果，与直接在 Finder 中搜索别无二致。因此使用这个动作的意义并不大。

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/1D5CBB9F-6FC8-40F1-BF67-9FAA55D254DA.png)

LaunchBar 中自带的 Search in Spotlight 的使用意义不大

所以 LaunchBar 中直接搜索中文文件名的功能，是保证这种流畅性的重要一环，本文为实现这一点提供了可能性。

制作思路
----

最后介绍一下这两个动作的制作思路。
这两个动作是借助 Spotlight 工作的。因此，要了解这两个动作的制作思路，有必要先了解一下 Spotlight 的工作原理与传统搜索方式的区别。传统的搜索方式是把整个搜索范围内的文件内容进行扫描；而 Spotlight 是使用扫描索引的方式，即为电脑中搜索范围内文件内容建立索引。
搜索的过程是在索引文件中进行搜索，因此速度相对更快。
当用户初次登入系统时，Spotlight 开始建立电脑硬盘上的文件的索引文件。初次建立索引时会持续一段时间，建立索引完成后，每当有文件发生变化，系统都会在后台持续地更新索引。在 Finder 中直接进行搜索也是进行了相同的过程。

macOS 中提供了一个命令行工具 `mdfind`，用以让用户在命令行中使用 Spotlight 的工作方式进行文件检索。
因此，Spotlight 的文件搜索功能、Finder 的文件搜索功能和 `mdfind`，是 macOS 上同一个功能的三张不同面孔，其本质的工作原理是一致的。
因此也可以说， `mdfind` 是运行在命令行中的 Spotlight。

`mdfind` 常用的使用方法如下：

* 按文件名搜索文件：

```
mdfind -name 关键词
```

* 按文件内容搜索文件：

```
mdfind 关键词
```

* 在特定的目录中按文件内容搜索文件：

```
mdfind -onlyin 目录路径 关键词
```

由于采用的是相同的工作原理，使用 `mdfind` 进行文件搜索得到的结果与在 Finder 中或使用 Spotlight 进行文件搜索的结果完全一致。

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/658B40FE-E9A5-4593-B20E-13622E2D131A.gif)

在命令行中运行 mdfind 的效果

同时，作为一个命令行工具，`mdfind` 最重要的价值，自然是它可以在 Shell 脚本中进行调用，以实现更为复杂的自动化工作。这就为各种自动化工具调用 Spotlight 进行搜索继并对搜索结果进行进一步的操作提供了可能性。

我们这两个 LaunchBar 的搜索动作就是通过调用 `mdfind` 实现的。
在 **Search Files by Name** 动作中，通过一个简单的 Python 脚本调用了上面提到的命令行语句 `mdfind -name 关键词`，并将其得到的搜索结果逐行地提取出来在 LaunchBar 中列出。其脚本内容如下：

![](.evernote-content/F3D872FF-D1A5-454D-AF28-5571F0D760B3/9160F92D-489C-4BE8-8931-525A404AABEE.png)

Search Files by Name 动作的 Python 脚本

其中各部分含义简要介绍如下：

* 6–9 行：引入用到的包；
* 11 行：获取运行命令行所需的环境变量；
* 12 行：声名要在 LaunchBar 中显示的搜索结果列表；
* 16–18 行：调用命令行 `mdfind -name 关键词`，并分解出得到的每一行文件的路径；
* 19–23 行：如果没有搜索结果，显示 **No result!**；
* 24–28 行：如果有搜索结果，将每一个文件的路径添加到要搜索结果列表；
* 30 行：最后，在 LaunchBar 中列出结果列表。

**Search Files by Contents** 动作的脚本中则调用了命令行语句 `mdfind 关键词`，其余内容与上面完全一致，故不赘述。

结语
--

本文介绍了一个在 LaunchBar 中实现搜索中文文件名的方案，并介绍了其使用方法和制作思路，亦讨论了在 LaunchBar 实现中文搜索的必要性。对于因为不支持中文文件名搜索而曾经拒绝尝试或是放弃使用 LaunchBar 的读者，希望这可以成为你开始喜爱或是重新爱上它的原因。

1. [文件的元数据用于描述文件内容、项目如何创建以及其他属性，我们可以在文件的信息窗口中查看。↩](#)

[#文件管理](https://sspai.com/tag/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86)[#macOS](https://sspai.com/tag/macOS)[#自动化](https://sspai.com/tag/%E8%87%AA%E5%8A%A8%E5%8C%96)

---

[🌐 原始链接](https://sspai.com/post/55233)

[📎 在印象笔记中打开](evernote:///view/207087/s1/5a3dc948-8b4c-421c-87da-dc9c16cf06e2/5a3dc948-8b4c-421c-87da-dc9c16cf06e2/)