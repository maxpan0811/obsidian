# macOS 隐藏的「注释」技巧，能帮你从凌乱中一步找到文件

---

为满足我们各方面的需求，每个人的电脑中都有一堆 App。其中有些可能并不常用，经常是为了解决临时遇到的问题，经过一番查找与对比后下载的 App。为了免去再次查找、下载的麻烦，这些 App 就留了下来。然而，在一段时间后再次打开 Launchpad 时，看着某些不怎么用过的 App 的图标，可能就会一脸茫然：「这货是干嘛的？」此外，看到一些优秀 App 的介绍后，也往往会下载备用，同样会造成这个问题。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/F9B2DCD2-F65D-4985-B9FA-52BDC5157BAD.png)

电脑在长期使用后，如果不是经常整理文件或着恪守命名与存放的原则，那么文件也可能杂乱无章。根据能否搜索内容，文件可分为两种。可搜索内容的，例如 Markdown、Txt 等文本格式的文件，再度寻找时，可以根据对于文件名和内容的印象进行搜索。而对于不可搜索内容的，例如图片、电影等，只靠文件名搜索，可能就无法如愿找到。

解决上述情况的一个好办法就是，为文件（软件也是文件的一种）添加注释，需要时通过搜索快速打开。例如，对于 [KeyCastr](https://sspai.com/post/41175 "KeyCastr") 这款实时显示按键的软件，可以加上「键盘 按键 显示 教程」等注释。我个人习惯于使用空格分隔的相关词语。其中的「教程」是考虑到这款软件常用于写教程。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/B44245C9-BB58-40D2-A8C3-2470A0C294BD.png)

另外，在为一些文件添加注释后，也能够达到聚合同类软件或文件的效果。例如：

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/F2F60E06-5A6A-4B4D-99F6-272DFABCFF9B.png)

对于有些名称不好记的软件，添加注释后也更加方便搜索。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/40B9948A-E79C-4760-B1A8-4E92D017666D.png)

可能有读者会问为什么不用标签呢？一般而言，标签是通用性的词语，比如「个人、工作、家庭」等。本文中，为文件添加的注释，是对其功能、用途或内容的概括。

添加注释
----

一般的方法为：

1. 选中文件后，右键菜单中打开**显示简介（Get Info）**或按下 `⌘Command-I` 快捷键。
2. 鼠标定位到注释框。
3. 输入注释。
4. 关闭：点击关闭按钮或按下 `⌘Command-W`。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/1668CB16-33DA-4331-8C44-C74C73819123.png)

可以看到，步骤有些麻烦。而且，多一步就多一份懒得用的可能。

所以，这里介绍下添加注释的快捷方法：

### 1. Finder 工具插件

下载 [AddCommentToFile](https://cl.ly/2K1s0g1Y3F0J "AddCommentToFile")，放置到一个你习惯的位置。我是放置在 iCloud/Apps/FinderPlugins文件夹中，方便同步。

在 Finder 工具栏上，右键点击并选择**自定工具栏**，将 AddCommentToFile 拖入工具栏中你喜欢的位置。需要注释时，点击 AddCommentToFile 图标，输入后回车即可。如果选中的文件原来就有注释，则输入框中包含，方便修改。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/68AE1147-F84C-4537-ABA4-14C2A4093244.gif)

对于桌面上的文件，需要在 Finder 中打开桌面文件夹，然后点击按钮添加注释，多了个步骤  
。但是我认为，一般而言，桌面上的文件都是近期文件、记忆清晰、直观可达，不怎么需要注释。如果确实需要，则可以使用下面的第二种方法。

AddCommentToFile 原理说明（可跳过）：这个 App 是在 Script Editor 中使用 AppleScript 编写的，可用 Script Editor 打开，其内容为（以 `--` 开头的是说明性文字）：

```
tell application "Finder"
    -- 获取当前选中文件列表
    set finderSelectionList to selection as alias list
    -- 判断是否有选中的文件
    if length of finderSelectionList = 0 then
        -- 如果没有，就弹出提示
        display alert "== Alert ==" message "Please select a file/folder !" as critical
    else
        -- 如果有，就获取第一个文件
        set theFile to (item 1 of finderSelectionList)
        -- 获取文件的注释
        set oldComment to comment of theFile
        -- 获取文件的名称
        set theFileName to name of theFile
        -- 生成对话框的信息
        set theMsg to "Enter comment for " & theFileName
        -- 弹出对话框
        set theResponse to display dialog theMsg default answer oldComment with icon note with title "Finder" buttons {"Cancel", "Continue"} default button "Continue"
        -- 设置新的注释
        set comment of theFile to (text returned of theResponse)
    end if
end tell
```

### 2. 使用 Alfred 添加

下载 AddCommentToFile 后，在 Alfred 中搜索，回车键运行。这个工具默认的操作对象是当前选中的文件。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/E52F36C4-82DB-4AC7-9DC3-510AC5B4B31F.gif)

灵活搜索
----

说完注释的添加，再来说下如何搜索。

### 1. Alfred 搜索

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/70684A64-F8FF-47A5-972D-6296AFF6D8F3.png)

在默认情况下，Alfred 只搜索 App、偏好设置和通讯录（上图中的第一个框，Essentials 部分）。Extras 部分（第二个框）包含了文件夹、文档、图片等，不建议勾选。如 Alfred 所提示的，在只勾选 Essentials 部分时，它最有效率。如果你需要搜索文件、文件夹等内容，只需要在唤出 Alfred 后，先按一下空格键再输入搜索词语即可。

因此，唤出 Alfred 后直接输入注释中的词语，就可以搜索相关 App。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/B44245C9-BB58-40D2-A8C3-2470A0C294BD.png)

唤出 Alfred 后先按一下空格键，再输入注释中的词语，搜索文件、文件夹等。输入框中的第一个字符 `'` 是按下空格键后自动生成的。

![](.evernote-content/13626016-4371-44B1-AC3B-71978D9067C0/14B9DCDA-2DE0-40E0-B7D5-5D74A9B85943.png)

另外，如果要搜索文件的内容，可以使用 `in 关键词` 的方式。

### 2. Spotlight 搜索

在 Spotlight 中搜索，个人感觉不如 Alfred 那么方便。如果直接在 Spotlight 中输入关键词，产生的结果十分混杂，往往得不到你想要的结果。这时候，需要使用一些搜索语法，以限定搜索范围。例如：

* `kind:app 关键词` 搜索 App
* `comment:关键词` 搜索注释

语法中的词语受系统语言影响，如搜索 App 在中文系统中为 `种类：应用 关键词`。更多的搜索语法可以看官方文档：

* [缩小在 Spotlight 和 Finder 中的搜索范围](https://support.apple.com/kb/PH25589?locale=zh_CN "缩小在 Spotlight 和 Finder 中的搜索范围")
* [Narrow your searches in Spotlight and Finder](https://support.apple.com/kb/PH25589?locale=en_US "Narrow your searches in Spotlight and Finder")

总结
--

使用注释有以下几个优点：

* 记住必要信息，避免看见软件或文件后不知道是干嘛的。
* 快捷搜索，不用去想文件名，直接输入描述你的需求的关键词。
* 避免记忆有些不好记忆的软件名，这相当于为软件加了个别名。
* 聚合同类软件或文件。

> 下载[少数派 iOS 客户端](http://sspai.com/s/nqQk "少数派 iOS 客户端")、关注[少数派公众号](http://sspai.com/s/KEPQ "少数派公众号")，让智能设备更好用 🖥

---

[🌐 原始链接](http://sspai.com/post/43673)

[📎 在印象笔记中打开](evernote:///view/207087/s1/84e19319-abe4-4a2b-8bd4-5d560724bdab/84e19319-abe4-4a2b-8bd4-5d560724bdab/)