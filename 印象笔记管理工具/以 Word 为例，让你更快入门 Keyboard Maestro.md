# 以 Word 为例，让你更快入门 Keyboard Maestro

---

以 Word 为例，让你更快入门 Keyboard Maestro
=================================

04月14日

[![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/4C718B14-50F1-4996-9DF9-10AEE36C66B2)](https://sspai.com/user/735387)

#### [Janner Chang](https://sspai.com/user/735387)

目录

前言
==

[Keyboard Maestro](https://www.keyboardmaestro.com/) 是 macOS 下的强大的自动化工具，这个无须过多的介绍，但是还是有很多朋友对该工具一头雾水，不知从何入手，可能是有些文章介绍的过于详细，技巧过于高级所致 ，其实对于这种功能丰富而强大的 app，我们先从最基本的功能用起就好。

> Mac 版的 Office 遭到很多人的唾弃 ，但是有了 Keyboard Maestro 等自动化工具，用起来可能比 Windows 版还要快捷。本篇文章将围绕对 Word 的各种操作，来展示 Keyboard Maestro 的基础应用。

正题
--

在 Word 中使用 Keyboard Maestro 主要目的是消灭重复乏味的操作。

对于 Word ，我主要集中在三个方面使用 Keyboard Maestro：

1. 对菜单的操作
2. 对文字的操作
3. 使用 AppleScript 操作

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/837BD5F1-8656-4F67-A0D5-6677390E61C7)

Keyboard Maestro 的 Palette 功能

为了减少大脑的记忆，我还是喜欢用 Palette 来执行 Keyboard Maestro 的 Macro。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/BB0514BE-439E-4EB1-93F4-79D03E452CF9)

创建组，如图设置成「Word」激活时显示 Palette 即可。

### 对菜单的操作

对于大部分 macOS app 来说，Keyboard Maestro 都可以直接调用你的菜单，不知道是不是使用了 macOS 标准开发所致，在 Keyboard Maestro 里可以模拟你对菜单项的选择，进而运行该菜单项。

比如「100%」、「200%」这两个 Macro，目的是快速将视图缩放至 100% 和 200%，不用 Keyboard Maestro 的话你需要在菜单里选择「视图 - 缩放 - 100% or 200%」或者在底部功能区拖动滑块或点「+、-」来调整。

如果我们有了 Keyboard Maestro 制作好 Macro 放到 Palette 里，一次点击就直接切换，岂不快哉。

创建 Macro，按 `⌘Command-K` 或 菜单「Actions - Show Actions」 呼出动作库，将「Interface Control」里的「Select or Show a Menu Item」动作拖入到 Macro 里。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/6980AE78-5134-49F0-A92B-6372AF52B2E0)

在「Select menu in」里选择「Microsoft Word」如果不是正在运行的 App 可以选择「More」。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/99FC3E52-9111-4F58-84DA-87CC3C23C398)

在「Menu」里选择你想选择的菜单项即可。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/16863F09-7F67-4A6E-8111-903594729D28)

当然对于需要连续选择菜单的操作也是可以的，再加个 Action 就行，比如对「页眉」的操作，这个操作是针对有的文档会在页眉处显示一个横杠，将页眉样式改成正文就能彻底解决。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/099E5278-15CC-43CE-80FD-F13B35E575C6)

Keyboard Maestro 对菜单的操作是非常快的，完全看不到菜单展开的过程，直接就是运行你需要的菜单项。

以上就可以用 Keyboard Maestro 操作所有可操作的 App 的菜单，对于某些经常选择的菜单项来说还是非常快捷的，完全不需要编程。

### 对文字的操作

对于我们常书写的文书中，有大量制式但又存在个案差异的情况，需要大量的复制粘贴，又要对部分文字进行修改，在我们刚开始使用的智审系统里，它会将这些固定的信息填写好，目的是减少我们书写的工作量，但实际操作中会存在非常多的错误，会大大加大校对的难度和出错率，所以求人不如求己，直接促使我使用 Keyboard Maestro 来强化本部分的操作了 。

> 对于我这种复制粘贴的文字操作，我主要是先复制到剪贴板，然后对剪贴板进行处理，再粘贴到需要的地方。

#### 当事人信息处理

二审文书中当事人主要有两个地位，上诉人和被上诉人，但是对应的原审地位就不确定了，有可能是「上诉人（原审原告）」也有可能是「上诉人（原审被告）」，以前是直接复制当事人的信息，然后手动填上「上诉人（原审XX）」「被上诉人（原审XX）」，虽说也不是很麻烦的事儿，但是偶尔碰见十几个当事人的时候也是个力气活 。

如图设置：

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/F06B64C8-D579-4E0E-BEDB-0EC3F37B3670)

1. 我们首先添加「Clipboard - Filter」Action，「with」这里设置成「Remove Styles」去除剪贴板里文字的格式；
2. 再添加「Clipboard - Search and Replace」，「for」选择「Regular Expression」利用正则表达式匹配你需要替换的关键词。

这样你在 Word 里选择部分当事人，然后点击 「上诉人、被上诉人」，就会根据原审地位生成二审地位，这种操作也能避免一些疏漏。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/AFA5CA4F-B45E-437D-8E61-A0F500CEF2DC)

#### 删除身份证号

对于有些不必要显示的当事人信息，如身份证号等，利用 Keyboard Maestro 批量删除也是一键的事儿。同样是「去剪贴板格式 - 利用正则表达式替换剪贴板中的文字」。

如图设置：

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/9580F1B5-23BC-4912-ABF7-0C853D2A104C)

效果如下：

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/0B0C0B33-FEAD-44DE-A317-355E39BE3D19)

#### 加顿号

这个操作是配合 Popclip 的 Append 动作的，通过 Popclip 复制的多条文本是分多行显示的，这个 Macro 是将多行文本用顿号分割，变成单行文本。

如图设置：

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/C3C568E6-B24E-4231-8685-520750E0D6C0)

效果如图：

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/64C7D0C9-1CE9-4970-92C8-E16FA63A866A)

#### 替换一审法院认为

不详细介绍了，设置都是一样，用不同的正则表达式替换不同的信息而已。

Keyboard Maestro 的正则表达式调试非常直观，还能将匹配出的不同文本分别赋给不同的变量。

### 使用 AppleScript 操作

该部分的操作主要在我之前的文章[《Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活》](https://sspai.com/post/44091)里有介绍，这里不再重复了。

结语
--

对于 Keyboard Maestro 这样的工具来说，他人的操作只是一个抛砖引玉的作用，真正要让工具为自己服务，尽量自己先提个需求，再看工具能否满足，用惯了 Keyboard Maestro，一般在有些重复操作的时候都会想 Keyboard Maestro 是不是能做，这个操作以后会不会经常重复，慢慢你的 Macro 就越积累越多，祝各位朋友都能用各种工具提高自己的效率，节省下来的时间可以做自己喜欢的事儿啦 。

![](.evernote-content/52E16576-419D-4CB0-84EA-7DF8D4C4FC0E/CCA6FC7C-C4C1-4634-9EEE-76FB2AEE663F)

* *Ulysses 编写，QuickTime 录屏，GIF Brewery 3 转 Gif*
* *[JannerChang 的知识库](http://jannerchang.bitcron.com/)*

---

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用

---

[🌐 原始链接](https://sspai.com/post/44091)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bf9abe51-76f9-4e9c-9de2-daf053c28076/bf9abe51-76f9-4e9c-9de2-daf053c28076/)