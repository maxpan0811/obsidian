---
title: 9 个 Yoink 实用技巧，提高你的 Mac 文件处理效率
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/9 个 Yoink 实用技巧，提高你的 Mac 文件处理效率.md
tags: [印象笔记]
---

# 9 个 Yoink 实用技巧，提高你的 Mac 文件处理效率

---

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/508BD3AE-A4E6-4245-9C4F-4A0B7DCF59C2.jpg)

Yoink 是 Mac 上一款临时文件暂存的工具类 App，它就像是一个「中转站」，让你能更轻松地把文件从一个窗口移动到另一个窗口。类似的软件在 Mac 上还有 [Dropshelf](https://itunes.apple.com/cn/app/id540404405?mt=12&uo=4&at=10lJSw) 和 [Unclutter](http://sspai.com/28798)，但相比之下，Yoink 更专注于「文件暂存」这个需求。

因为专注，看似简单的 Yoink 实际上有不少细节功能，可能很多长期在用 Yoink 的人都不一定知道，为此，开发者在官网有作一个技巧汇总页面，但可能也少有人发现。

为了让更多人更好使用 Yoink，我们将这些技巧整理编译出来，其中很可能就有可以帮你大大提高日常文件处理效率的方法。

如果你不了解 Yoink，可先阅读此前文章：[《OS X 上最临时的「临时文件夹」：Yoink》](http://sspai.com/30779)

技巧 1. 复制和移动操作
-------------

就像在 Finder 中一样，你可以将文件从 Yoink 复制到其他位置，而不仅仅是用 Yoink 移动文件。

**方法：**从 Yoink 面板拖拽出文件时，按住 Option 键 (⌥) ，你拖动的该文件会被复制到新的位置，而非移动。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/E3FD8C03-6EB5-45C4-B940-7E1180B2736C.gif)

技巧 2. 全选文件
----------

因为 Yoink 没有键盘焦点，所以不能使用 Command + A 来全选所有文件。

如果你在用 Force Touch 触控板的 Mac，你可以通过选中 Yoink 里任意一个文件用力按压触控板来全选所有文件。

如果你的触控板不具备 Force Touch，那么可以通过按住 Option 键 (⌥) 点击任意一个文件来全选所有文件。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/8A76837C-2D12-4B4B-A1DB-5C95D1EFB517.gif)

技巧 3. 使用快捷键来添加文件到 Yoink 中
-------------------------

安装 Yoink 后，我们就可以在任意文件的右键快捷菜单中选择「将文件添加到 Yoink」。

如果你嫌点选麻烦，其实可以通过快捷键（默认为 Control + Option + Command + X）来完成这一操作。如果觉得键位复杂，也可以在「系统偏好设置－键盘－快捷键－服务」中自行更改快捷键。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/8FBCFB84-B007-487F-A14A-94AA2DCF21CA.jpg)

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/27349B8F-D9A2-4C95-86AB-5EC6853BBC1C.jpg)

技巧 4. 在 Finder 中显示
------------------

你可以在 Yoink 中通过右键点击文件，以在 Finder 中显示。如果是堆叠的多个文件，也可以分别查看每个文件。

除此之外，当你按住 Option 键 (⌥) 再右键点击文件时，菜单中的 「在 Finder 中显示」会变成「拷贝文件路径」，你可以很方便地复制该文件在 Finder 的路径。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/BDCD32A1-0AD6-4B38-8DE0-7E6A3C3FDF2D.jpg)

技巧 5. 从终端添加文件到 Yoink
--------------------

如果要在终端将文件添加到 Yoink，你可以使用这条命令：

```
open -a Yoink /path/to/the/file
```

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/FB793192-02C6-41D7-8085-42E76B6E7B93.gif)

如果觉得命令太长，你也可以通过设置 alias 别名来简化输入：

```
alias yoink=“open -a Yoink”
```

如此一来，你只需要输入：

```
yoink /path/to/the/file
```

需要注意的是，这只是一条临时的 alias 命令，只对当前版本终端有效，如果你想使这条 alias 命令永久有效，可查阅这篇 [官方博文](https://eternalstorms.wordpress.com/2014/12/18/using-yoink-from-the-terminal-on-os-x/)。

技巧 6. 将 PDF 更方便地发送到 Yoink
-------------------------

如果你需要将机票行程单、电子发票存为 PDF 格式，然后快速保存或分享出去，那么可以将 Yoink 添加到 PDF 打印对话框，简化整个操作流程。

首先，在 Finder 中找到 Yoink 右键「制作替身」，然后将替身移动到`/Users/yourname/Library/PDF Services/` 路径下，就可以在打印对话框中，直接将 PDF 文件发送到 Yoink。

假如在上述路径中不存在 PDF Services 文件夹，可以手动创建一个。为了方便在菜单中辨认，你还可以将替身重命名为「Add PDF to Yoink」。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/3B162FEF-8E9D-4129-91CB-B023401AC6E4.jpg)

之后，在保存 PDF 时选择此项，你存下来的 PDF 文件就会直接放到 Yoink 中，方便你作下一步操作。

技巧 7. 从邮件中创建有标题的日历事件
--------------------

你可以从系统邮件 App 通过拖拽某一封邮件至 Yoink 以创建一个新事件，需要注意，在拖拽邮件时要按住 Option 键 (⌥)。

你也可以通过将放在 Yoink 中的邮件文件 (.eml 后缀) 拖拽到日历，来创建一个该内容的日历事件。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/A731E294-686F-4672-88CE-6771447300F9.jpg)

技巧 8. 将邮件附件添加到 Yoink
--------------------

通过使用 Mac 系统自带的自动化工具 Automator，你还可以将多封邮件中的多个附件直接添加到 Yoink，方便作后续操作。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/27AF01B4-8D1C-411E-98B0-D3B2ACE5D557.jpg)你可以直接下载已经做好的 [这个脚本](http://eternalstorms.at/yoink/workflows/YoinkAutomatorWorkflowMailAttachments.zip)，双击安装，然后在系统偏好设置中为这个 workflow 设置相应的快捷键即可。之后，你就可以通过设置的快捷键或从菜单栏使用这个脚本（如下图）。

如果你想了解这个脚本的实现方式，[这篇博文](https://eternalstorms.wordpress.com/2015/09/02/yoink-workflow-quickly-add-mail-attachments/) 作了具体解释。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/9C1A11C3-1F14-4548-A92E-3CE46E0A614C.jpg)

技巧 9. 将屏幕截图发送到 Yoink
--------------------

有人喜欢 Dropshelf 中使用当前剪贴板内容创建临时面板的功能，配合系统的 Shift+Control+Command+4 截图存至剪贴板的快捷键，可以把临时一用的截图无需存为本地文件就直接分享出去。这的确是一个存在的需求，借助 Automator，Yoink 其实也能做到。

下载安装 [这个脚本](http://eternalstorms.at/yoink/workflows/screencapture.zip)，在 Finder 的 ~/Documents 路径下（即中文的「文稿」）创建名为 Yoink 的文件夹，然后在系统设置里为该脚本创建一个快捷键即可（注意不要和系统快捷键冲突）。通过快捷键启用，会先让你选区截取屏幕，然后该截图会立刻出现在 Yoink 面板中，以便你可以直接分享这张截图。

当然，截图同时还会保存到你在文稿内创建的 Yoink 文件夹中。

如果你想要全屏截图而非区域截图，那么可以在 Automator 里打开这个脚本，将其中 AppleScript 的一段 `do shell script “screencapture -i ” & filePath` 替换为 `do shell script “screencapture “ & filePath`。

如果你想了解这个脚本的实现方式，可以阅读 [这篇博文](https://eternalstorms.wordpress.com/2015/01/15/capture-selective-screenshots-in-yoink/)。

![](.evernote-content/42B4718B-27F6-4335-981C-5D088B785A12/9957F796-E409-458C-94AF-AF251451E285.jpg)

你可以先在[官网免费下载](http://eternalstorms.at/Eternal_Storms_Software_-_Apps_for_Mac_OS_X_and_iOS/Eternal_Storms_Software_-_Apps_for_Mac_OS_X_and_iOS.html) Yoink 试用版，喜欢的话，可前往 [Mac App Store](https://itunes.apple.com/cn/app/yoink/id457622435?mt=12&uo=4&at=10lJSw) 下载 Yoink，售价 45 元。

文章来源 [少数派](http://sspai.com) ，原作者 [vanilla2w](http://sspai.com/author/666443) ，转载请注明原文链接

原文可获取应用下载链接：[9 个 Yoink 实用技巧，提高你的 Mac 文件处理效率](http://sspai.com/34048)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

---

[🌐 原始链接](http://sspai.com/34048)

[📎 在印象笔记中打开](evernote:///view/207087/s1/4c285de6-08bc-4d50-93bc-fa1cec95600b/4c285de6-08bc-4d50-93bc-fa1cec95600b/)
