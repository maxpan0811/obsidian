---
title: "用 Keyboard Maestro 托拽整理文件"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/用 Keyboard Maestro 托拽整理文件.md
tags: [印象笔记]
---

# 用 Keyboard Maestro 托拽整理文件

# 用 Keyboard Maestro 托拽整理文件 --- 用 Keyboard Maestro 托拽整理文件 ========================= | 本文为付费栏目文章，您已订阅

---

# 用 Keyboard Maestro 托拽整理文件

---

用 Keyboard Maestro 托拽整理文件
=========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

一般来说，在 PC 上，日常生成的文件，我们都会把它们放在「桌面」、「文档」之类文件夹，将它们作为一个临时收件箱。对于不少人来说，这个临时收件箱的整理，其实是个问题。

相信我们 Power+ 的读者都可以根据自己职业等特性，有一套「文件传输」的自动化系统，比如 Hum 分享过两个它的文章配图和 PDF 的自动化系统：

1. 《[苹果环境下半自动的文件处理流程思路](https://sspai.com/article/41865?series_id=9)》
2. 《[如何高效处理屏幕截图](https://sspai.com/article/42540?series_id=9)》

作为这类系统的实践者，我也会设置一些这样的自动化系统，但我也发现，这些系统并不能完全覆盖到所有需求，放置有些文件还是需要在 Finder 里打开一层一层的文件夹。

因此我就在想有没有办法，可以把「桌面」等「文件收件箱」中的文件，**直接拖到我们想要的文件夹里**？

经过一番折腾，我发现了通过 Keyboard Maestro 解决这个需求的办法。

通过 Keyboard Maestro 解决问题
------------------------

最新版本的 Keyboard Maestro 提供了「Dragged File」这一触发条件，我基于它做了一系列的 Macro（自动化动作），不用打开 Finder 中的文件夹，**直接把文件拖拽到 Keyboard Maestro 的 Palette（浮窗）上，就可以归档文件**：

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/22D082AF-D60E-49DE-A1EB-58C6A1CB74BC.gif)

托拽归档

* [> 动作下载（直接下载）](https://github.com/BlackwinMin/sspai-sample-script/blob/master/Keyboard%20Maestro/%E7%A7%BB%E5%8A%A8%E6%96%87%E4%BB%B6%20Macros.kmmacros.zip)
* [> 动作下载（GitHub）](https://cdn.sspai.com/2018-05-03/%E7%A7%BB%E5%8A%A8%E6%96%87%E4%BB%B6%20Macros.kmmacros.zip)

我提供的一系列 Macro 包含了图片、视频和文档等几个常用文件夹，你可以边试用这些 Macro 边阅读文章，制作出适合自己的 Macro。

基础知识：Palette

Palette 这个单词的意思是「调色盘」，即画家常常拿在手里的工具；在 Keyboard Maestro 里，Palette 就是几个 Macro 组合成的列表，它会像一个浮窗一样「漂」在屏幕上，可以随意拖动，方便我们像画家取用颜料一样方便地启动自动化动作。

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/ACD3E7F9-92E2-4C11-8D1C-F28ED8422931.gif)

Palette

制作单个 Macro
----------

我们先看看如何制作单个 Macro，学会之后，炮制其他 Macro 就只需修改一下目标文件夹的路径。

制作一个归档的 Macro 需要三大步。

以一个「归档到文档文件夹」的 Macro 为例，我们希望它仅在 Finder 中出现，而不要在其他应用里跑出来捣乱，那么步骤就是：

1. 让改 Macro 仅在 Finder 中生效。在 Keyboard Maestro 编辑界面创建一个 Macro 组（Group），将下图紫色部分所示的作用范围（Available in these applications）设置为「Finder」；  

   ![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/C7B124C1-05E3-49B0-AC20-B02B4F6A4A14.png)

   Finder 组
2. 设置触发条件。这个 Macro 需要两个触发条件，分别是：
   1. A file is dragged on to the macro：接下来能够处理被拖到这个 Macro 上的文件；
   2. The global macro palette entry is clicked：将在 Finder 内一直显示一个小号浮窗，当光标移到它上面，浮窗就会展开成一个 Palette，显示出我们要用的 Macro；  

      ![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/B761BFA8-C05C-4813-9B13-E54A0C1629EB.png)

      设置触发条件
3. 设置 Macro 动作内容：**For Each Item in a Collection Execute Actions**（黄色部分）。这个动作表示循环，它里面还需要套一个 **Move or Rename File**（红色部分）的动作来移动文件。如果你一次性拖了多个文件到 Macro 上，这组嵌套动作就能对每一个文件执行一次移动操作。其他参数如图填写：
   1. For each：**PATH**；
   2. 选 **The Finder’s Selection**；
   3. Move：**%Variable%Path%**；
   4. to：移动的目的地文件夹，例如 **~/Documentations**。  

      ![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/C4E257D9-0D1E-43D4-AB83-3C243D4D03B4.png)

      填写路径及其他参数

现在给这个 Macro 取个容易理解的名字（比如『归档文件到 文档』），保存并点击右上角的 ☑️ 来启用这个 Macro，切换到 Finder，你应该就能看到如下图左侧所示的小浮窗；如果没有，请点击菜单栏中 Keyboard Maestro 图标，并点选 **Show Global Macro Palette**。

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/2C739EBD-492E-4BBA-B1A0-9FAF1EA589B2.png)

显示 Palette

现在，试一试选一个文件拖到浮窗上，触发出 Palette 后继续拖动文件到「归档文件到 文档」这一 Macro 上，文件就会被移动到指定文件夹了。

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/22D082AF-D60E-49DE-A1EB-58C6A1CB74BC.gif)

移动文件

托拽多了，你还会形成肌肉记忆，每次「唰 ——」一下把文件拖到大致的位置，就能把它们放进想要的文件夹。我就把 Palette 挂在屏幕右上角，每次需要归档文件就拽住、往上一滑、松手，像投壶一样，把文件「投」进了文件夹。

为每个应用设置不同的 Macro
----------------

拖拽在 macOS 中很常见，除了 Finder，其他应用里也可以用拖拽来整理文件。通过上一节理解了 Macro 的工作原理之后，我们可以为每个应用设置不同的 Macro，显示出和这个应用关系最紧密的文件夹，例如：

* 用 Safari 浏览网页时，显示素材、摄影、插画等文件夹；
* 用 Ulysses 写作业时，显示民法、刑法、英语等文件夹；
* ……

操作也很简单，我们只需修改上一节中的第一步。譬如想为 Safari 设置一组专用的 Macro，就去 Keyboard Maestro 编辑界面创建一个 Macro 组，将下图紫色部分所示的作用范围设置为「Safari」。

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/70649A4E-9AFE-44E4-8858-F7B2839B10D9.png)

Safari 组合

再创建几个适用于 Safari 的 Macro。现在打开 Safari，就会看到它专用的 Macros 了：

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/61BC9CBE-FC28-4910-858F-7D67834914F2.gif)

Finder 和 Safari 都有各自专用的 Macro

下次浏览网页时看到好看的图片，就可以直接通过 Palette 放进对应文件夹，不用再打开 Finder 折腾。这种感觉很像去邮局寄信，你不用亲自跑到收件人那里，有邮差代劳；这个 Keyboard Maestro Macro 也是，它充当了「信差」的角色，帮你把文件放好，免去你手动打开 Finder 的麻烦。

用 Keyboard Maestro 的优势
----------------------

其实 macOS 上有一类「Shelf App（文件暂存应用」，它们也提供了类似 Palette 的「浮窗」，你可以把文件拖到这些浮窗上临时存放一下。这类 App 中的佼佼者 [Dropzone](https://aptonic.com/) 不仅支持直接把文件拖进预设文件夹，甚至还能对文件运行脚本，那为什么我还要使用 Keyboard Maestro 呢？

我们可以简单对比一下 Dropzone 和 Keyboard Maestro 在文件整理方面的功能：

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/57CA5C17-8A26-4291-B25C-C679FEE793CD.png)

Keyboard Maestro 和 Dropzone 的对比

从上表中能看出，Dropzone 关于文件整理的功能 Keyboard Maestro 基本可以实现，而且后者具有更大的灵活性，能够**为不同的 App 设置对应的 Macro**，这样在托拽文件时就不会出现不相干的选项。我用 Dropzone 时，偶尔会误把文件放进相邻的文件夹，事后找起来就比较麻烦了。

小结
--

在 macOS 上，拖托拽是非常符合直觉的一种操作，网页图片、Finder 里的文件，都可以拖到其他地方。

![](.evernote-content/43350AE6-864B-444D-A5B3-2DD11D568991/42D797A0-F955-4866-8578-ED53A12B624C.png)

各种托拽操作

我原先就在用托拽移动文件，但总是要在 Finder 里打开一层层的文件夹，或者委屈桌面充当「收件箱」，总是不够满意；正好 Keyboard Maestro 在上个月的更新里支持了托拽文件，就给我整理文件提供了一个捷径。

这种一托一放就能把文件放到指定文件夹的操作很讨人喜欢，就像在我们手边放了几个快捷入口，把文件投进去，它们就能如期出现在你预设的位置。当然，本文提供的只是「移动文件」这个基础操作，你可以配合 Hazel 等自动化工具来进行进阶的文件处理，这将放在今后的文章中再写。

[#文件管理](https://sspai.com/tag/%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86)[#macOS](https://sspai.com/tag/macOS)[#Keyboard Maestro](https://sspai.com/tag/Keyboard%20Maestro)

---

[🌐 原始链接](https://sspai.com/post/44429)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e7705abf-ad26-4a66-9004-41318ea3ccbb/e7705abf-ad26-4a66-9004-41318ea3ccbb/)