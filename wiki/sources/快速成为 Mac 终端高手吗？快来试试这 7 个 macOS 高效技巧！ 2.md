---
title: 快速成为 Mac 终端高手吗？快来试试这 7 个 macOS 高效技巧！ 2
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/快速成为 Mac 终端高手吗？快来试试这 7 个 macOS 高效技巧！ 2.md
tags: [evernote, impression, yinxiang]
---

# 快速成为 Mac 终端高手吗？快来试试这 7 个 macOS 高效技巧！

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0MzU5NzQ4Mw==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247488941&idx=1&sn=98813c1f4d5096e64496ceb82c2c65be&chksm=c256a66c5bf8a17d95600288939ff6ff2b7305d98bdd50b73edb767ebda13362da9ba9e5f05d&scene=126&sessionid=1743733786&subscene=90&clicktime=1743738410&enterid=1743738410&ascene=3&devicetype=iOS18.3.2&version=1800392c&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAjURQ/dQi+NB6sE1BgQlPxLYAQIE97dBBAEAAAAAAK9sMZD9GgkAAAAOpnltbLcz9gKNyK89dVj0FSEb2pF7zhJIyNIQZbYl7GpfX7jHAmZnB6Z6l8DsGtKV+7JkIaLmJ+8AvaUMTBTfaofmnDNm6S9HpFmLUn/8OiwrKKJ9jCG99XWLndQ3ogrgXOspPVeGJkJI6m++q8zgITxxWBm9YxyZ8gBlRZ45/e2naYTxvO/UrqxGlvTR5w63eZXJ8Nxj8JCR4QAiKxeb/yNHJuhZRw65OKnKSv+zaqY4j9FsHYs/qTguRCbzbtEAnA==&pass_ticket=g00S07LRYretXocosRCuLE8ft8hWGvuUqnGeFkBsYmPlpGnn7oukFrxQDqBWGS9g&wx_header=3)

快速成为 Mac 终端高手吗？快来试试这 7 个 macOS 高效技巧！
====================================

原创 点蓝色字关注👉 程序员echo

所有的事情都有尽头。

在过去一年里，我分享了大量的 Mac Terminal 技巧，帮助你自动化繁琐的任务，让你忙碌的生活稍微轻松一些。

![](.evernote-content/CC0FA7C7-3582-4F76-9337-C6AF0E451EC5/B8770DE3-3AD9-4AA3-9EF6-0D6EDECDFF07.png)

这些（可能）是我目前为止最后的命令了——但别担心，它们绝对不会是最不重要的。我仍然会尽力收集并写下更多的命令。

以下是 11 条 Terminal 命令，帮助你更接近你梦想中的（工作）生活。

#### 1. 一次做大量的事情

好吧，这是你每天登录 Mac 时应该使用的神级命令。

它让你创建别名，以便只需一键打开应用（并带参数）。花 10 分钟设置好这些别名，我敢保证，你会节省一辈子很多时间。

首先，打开 Terminal 并运行 `touch aliases` 来创建一个别名文件在你的 Home 目录。你可以随便命名，但在本指南中我将用“aliases”。

然后输入 `open aliases` 来打开它。

现在，最酷的部分——添加你的别名。每个别名占一行。如果你创建了一个叫 `work` 的别名，只需在 Terminal 中输入 `work` 就能执行它。

你可以做的事情：

* 打开特定文件/文件夹：

  ```
  alias notes='open ~/Documents/notes.txt'  
  alias downloads='open ~/Downloads'
  ```
* 启动应用或用特定应用打开文件：

  ```
  alias zoom='open -a "Zoom"'  
  alias familypic='open -a "Preview" ~/Pictures/photo.jpg'  
  alias opentxt='open *.txt'
  ```
* 在浏览器中打开链接：

  ```
  alias apple='open https://www.apple.com'  
  alias google='open -a "Google Chrome" https://www.google.com'
  ```
* 在任意文件夹中打开 Terminal：

  ```
  alias termhere='open -a Terminal ~/Documents/Projects'
  ```
* 快速运行 Terminal 命令：

  ```
  alias brewupgrade='brew upgrade  --greedy'
  ```
* 跳转到系统偏好设置中的某个界面：

  ```
  alias displays='open "x-apple.systempreferences:com.apple.preference.displays"'  
  alias sound='open "x-apple.systempreferences:com.apple.preference.sound"'
  ```

  你可以在这里找到更多的 URL 方案。
* 将多个操作捆绑为一个别名：

  ```
  alias startday='open -a "Slack"; open -a "Google Chrome" https://calendar.google.com; open ~/Documents/Work'
  ```
* 将多个别名批量组合在一起：

  ```
  alias meet='files;slack;calendar'
  ```

添加完别名后，点击 `⌘S` 保存文件并输入 `source aliases` 来加载它（每个会话都需要这样做）。

试试看——输入 `startday`，看看 Slack、Google 日历和工作文件夹是否会瞬间打开。🫰

#### 2. 自动填充命令

谁愿意每次都输入 `source aliases`？那太麻烦了，天呐，已经是 2025 年了。

这里有个更快捷的方式。

打开 Terminal，按 `⌃R`。然后开始输入 `s. o. u…`，当你还没打完时——`source aliases` 就会自动显示出来。

只需要按回车，别名就会加载。

![](.evernote-content/CC0FA7C7-3582-4F76-9337-C6AF0E451EC5/8CFD0982-AEDF-4DC5-BC16-2E6B334F16FF.png)

实际发生了什么？`⌃R` 快捷键让你查找之前使用过的长命令。输入几个字母（不一定是开头字母），它会帮你拉出完整命令。

#### 3. 查看命令历史

想查看你执行过的每个命令吗？输入 `history`。

输入 `history -5` 查看最近 5 个命令。

输入 `history | grep git` 查看你之前执行过的 git 命令。 

输入 `history | grep "npm install"` 查看你安装过的 npm 工具。

假设你的历史记录是这样的：

```
rickastley@nggyu ~ % history   
1 pwd  
2 touch notes.txt  
3 cd Downloads  
...
```

如果你想再次运行 `touch notes.txt`，可以输入 `!2`。 另外，如果你想查看第 1967 条命令，可以使用 `!1967:p`。 

要运行最近的命令，输入 `!-1` 或 `!!`。 

要运行倒数第 20 条命令，使用 `!-20`。

要运行以 `cat` 开头的最后一个命令，使用 `!cat`。 要将历史记录导出为 txt 文件，可以使用 `history > print.txt`，文件会被创建在当前目录中。

#### 4. 展开 bit.ly 链接而不被 Rickrolled

在印度长大的时候，Rick Astley 和他的“Rickroll”梗对我们来说是全新的。直到某个同学给我们展示了这个梗，大家才明白并开始恶搞。

后来我们班有些人用 bit.ly 链接发给别人，说是答题卡或讲义下载链接，结果点开后就是 rickroll.us。

这倒是很有趣，但也很烦人。既然我总是在玩 Terminal，就写了这个命令来检查一个 bit.ly 链接是不是要把我们 Rickroll。

```
curl -s --head bit.ly/98K8eH |grep Location|awk '{print $2}'
```

如果输出中显示 `rickroll.us` 或 `youtu.be/dQw4w9WgXcQ`，那就说明你应该避免点击这个链接。这样，你就避免了被 Rickrolled。

该命令显示了 bit.ly 链接实际指向的原始链接，而无需点击它。

你可能会想——如果点击链接可能下载恶意软件呢？所以，先用这个命令检查 bit.ly 链接是个聪明的做法。

#### 5. 清除剪贴板

你知道 Windows 可以查看你复制的所有内容（⊞V）吗？但是 Mac 只记住你最近复制的那一项，而且当你重启后会清空。

如果你没有复制任何东西，剪贴板会在重启时清空。 如果你复制了“nothing”，你的剪贴板会立即清空。

那么，怎么复制“nothing”呢？

使用 `pbcopy < /dev/null`。这样你的 Mac 会复制空内容——在程序员术语中就是“nothing”。这会立即清空剪贴板。

#### 6. 打开应用时自动打开空白文档

假如你想快速创建一个 txt 文件、Word 文档或 PPT 文件。

![](.evernote-content/CC0FA7C7-3582-4F76-9337-C6AF0E451EC5/F81F39E7-542A-4773-BCCB-1150DD5213B5.png)

如果是我，我会点击 `⌘space`，输入 TextEdit、Word 或 PowerPoint 然后按回车，这样应用就会打开。

但等等——怎么回事？

我只想要一个空白文档来开始打字，为什么 TextEdit 会让我先选择保存的位置？（老实说，这让我有点怀念 Windows）。

![](.evernote-content/CC0FA7C7-3582-4F76-9337-C6AF0E451EC5/A2368ED0-AF6F-4FC6-AD93-1BA77DEE6346.png)

这里有两种解决方法（其中之一 ↓）

下载一个名为 **NewFolderFile** 的应用。

无论你在哪个文件夹，只需按 `⌘⇧N` 来创建新文件夹。然后把它命名为 `textfile.txt`、`myppt.pptx` 或 `doc.rtf`，根据你需要的文件类型来命名。使用自定义快捷键即可快速创建空白文件。

如果你讨厌第三方应用，可以尝试以下方法（2）。

要让 TextEdit 打开一个空白文档，你可以使用以下命令：

```
defaults write com.apple.TextEdit NSShowAppCentricOpenPanelInsteadOfUntitledFile -bool false
```

要将这个命令应用到其他应用，只需把应用名称改成那个应用的名称即可。

如果你不想任何应用出现保存/打开的对话框，可以使用这个命令：

```
defaults write -g NSShowAppCentricOpenPanelInsteadOfUntitledFile -bool false
```

#### 7. 加密 PDF

“Preview”应用已经提供了一种简单的方式来加密 PDF 文件。只需要选择 `File < Export < Permissions`，设置密码并保存即可。

这种加密适用于一般的机密 PDF 文件，比如商务或银行文件。

但是如果你是个 FBI 特工，要给 NY 警察局局长发送总统的下一步计划……你就需要更强大的加密方式了。

以下是 Terminal 中的命令：

```
openssl enc -aes-256-cbc -e -in PresidentVisit.pdf -out PVEncrypted.pdf
```

Terminal 会要求你输入密码。输入密码后，命令会将 `PresidentVisit.pdf` 加密成 `PVEncrypted.pdf`。 这些命令使用 AES-256-CBC 加密 — 这比预览版的加密要强得多。黑客更难通过暴力破解。

#### 备注：创建加密的 DMG

所以您刚刚学会了如何使用超级安全的 AES-256-CBS 加密 pdf 文件。但是如果您有多种不同类型的文件怎么办？

以下是需要采取的措施。

将所有文件放入一个文件夹中 - 我们称之为“新文件夹” - 然后在终端中运行：

```
hdiutil create -encryption AES -256 -srcfolder “新文件夹” -ov -格式UDBZ “EncryptedImage.dmg”
```

输入并确认您的密码。

您的文件夹旁边会弹出一个包含原始文件的加密 DMG 文件（磁盘映像）。任何试图访问其内容的人都需要密码。

你可能会想——为什么不直接制作一个加密的 zip 文件，而要制作一个 DMG 文件呢？因为有了 DMG，你就可以直接读取文件，而不必先解压它们。本期精彩分享到这了，下期我们再见！！！

![](.evernote-content/CC0FA7C7-3582-4F76-9337-C6AF0E451EC5/A27E2CE3-E152-4C5F-A05F-C80EB0AA808D.gif)

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0MzU5NzQ4Mw==&mid=2247488941&idx=1&sn=98813c1f4d5096e64496ceb82c2c65be&chksm=c256a66c5bf8a17d95600288939ff6ff2b7305d98bdd50b73edb767ebda13362da9ba9e5f05d&scene=126&sessionid=1743733786&subscene=90&clicktime=1743738410&enterid=1743738410&ascene=3&devicetype=iOS18.3.2&version=1800392c&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQAjURQ/dQi+NB6sE1BgQlPxLYAQIE97dBBAEAAAAAAK9sMZD9GgkAAAAOpnltbLcz9gKNyK89dVj0FSEb2pF7zhJIyNIQZbYl7GpfX7jHAmZnB6Z6l8DsGtKV+7JkIaLmJ+8AvaUMTBTfaofmnDNm6S9HpFmLUn/8OiwrKKJ9jCG99XWLndQ3ogrgXOspPVeGJkJI6m++q8zgITxxWBm9YxyZ8gBlRZ45/e2naYTxvO/UrqxGlvTR5w63eZXJ8Nxj8JCR4QAiKxeb/yNHJuhZRw65OKnKSv+zaqY4j9FsHYs/qTguRCbzbtEAnA==&pass_ticket=g00S07LRYretXocosRCuLE8ft8hWGvuUqnGeFkBsYmPlpGnn7oukFrxQDqBWGS9g&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f12b6852-5e37-4c65-974f-d960b653322b/f12b6852-5e37-4c65-974f-d960b653322b/)
