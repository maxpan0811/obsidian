---
title: "如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF.md
tags: [印象笔记]
---

# 如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF

# 如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF --- 如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF ====================

---

# 如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF

---

如何在 macOS 上一键批量把 PPT 和 Word 文件转成 PDF
====================================

04月23日

[![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/B335FF51-F0C8-49C5-82AA-3542503F970A)](https://sspai.com/user/759132)

#### [joysisyphu](https://sspai.com/user/759132)

目录

相信不少人都有或曾经有过需要将多个 PPT/Word 文件转为 PDF 的需求，可能是一堆 PPT 课件为了方便批注，也可能是一些 Word 文档为了方便阅读。每次只能打开一个文档，选择「另存为」，选「PDF」，点「保存」，关掉，再打开下一个文档，文档数目一多，整个过程就会变得很令人沮丧。

最近我研究了一下这个磨人的问题，制作了一个动作可以在不到 2 秒的时间将多个 PPT/Word 文件转为 PDF（下图为 LaunchBar 版本的演示）。

![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/229C4532-F200-4FD4-8E81-384C3BA939F2.png)

视频中我剪掉了转换过程中等待的时间，可以看到，每转换完成一个文件都会有通知，全部转换完成之后也会有通知。

要实现这样批量转换的效果，请先下载 [LibreOffice](https://www.libreoffice.org/)，然后从下面两个自动化动作中下载一个适合你电脑的：

* [LaunchBar 动作下载](https://cdn.sspai.com/Convert%20to%20PDF.lbaction.zip)
* [Automator workflow 下载](https://cdn.sspai.com/converttopdf.workflow.zip)

两个动作的使用方式分别为：

* LaunchBar 版：双击安装下载的动作，选中文件，用快捷键呼出 Instant Send，输入 `convert to pdf` （一般只需要前几个字母），选中对应动作并回车（效果如上方视频所示）；
* Automator 版本：双击安装下载的 workflow，选中文件，右键，在「服务」里选择「convertoPDF」。

![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/FEB17B04-B081-4A6D-8EDE-CED646F7DF9C)

下载了[LibreOffice](https://www.libreoffice.org/)和任意一个动作就可以转换了，如果你想了解动作的制作过程，请继续往下看。

准备工作
----

想要进行批量转换，肯定要依赖于 Terminal 命令，然而 Microsoft Office 系列并不支持通过 Terminal 命令进行文件格式转换。经过一番搜索，找到了一个免费的开源软件 [LibreOffice](https://www.libreoffice.org/)。通过其 [官网](https://www.libreoffice.org/download/download/) 下载 dmg 的方式安装最新版即可。

通过查看其 manual 可知执行格式转换的命令如下：

```
soffice --convert-to pdf filename
```

其中 `filename` 为待转换的文件。

如果想要批量转换，只需要:

1. 将待转换文件放到一个文件夹

2. cd 到待转换的文件所在文件夹

3. 执行`soffice --convert-to pdf *.ppt` 或者`soffice --convert-to pdf *.doc`即可

![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/27790551-57A5-4AD2-A099-65CD90A5A7ED)

Terminal 命令

`*` 是通配符，代替零个、单个或多个字符，`*.ppt` 会匹配所有格式为 ppt 的文件，如果需要转换的文件中既有 ppt 又有 word 文件，可以通过 `soffice --convert-to pdf *` 来实现，`*` 会匹配当前目录下所有文件。

到此为止已经实现了批量转换文件到 PDF 的工作，但是每次都要打开 Terminal，`cd` 到对应文件夹，复制粘贴命令，也有些麻烦，于是我通过制作 LaunchBar 动作的方式进一步简化。

LaunchBar 版动作
-------------

LaunchBar 的 Instant Send 功能使得 LaunchBar 可以直接对选中的文件运行脚本，不需要打开 Terminal。

在 LaunchBar 中，按下快捷键 `⌥Option - ⌘Command - E`，新建一个动作，贴上如下脚本，这里脚本语言我选择的是 Python。

```
#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import subprocess as sp
import os
import json
import shutil

my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
# Note: The first argument is the script's path

for arg in sys.argv[1:]:
        fileFolder = os.path.dirname(arg)
        new_file= os.path.basename(arg)
        my_command = ["soffice", "--convert-to", "pdf", arg, "--outdir", fileFolder]
        sp.check_output(my_command, env=my_env)
        my_command = ["osascript", "notification.scpt", new_file, "Conversion Finished"]
        sp.check_output(my_command, env=my_env)

my_command = ["osascript", "done.scpt", "All Finished!"]
sp.check_output(my_command, env=my_env)
```

`for arg in sys.argv[1:]:` 之前的代码负责导入库和声明环境变量，`for arg in sys.argv[1:]:` 之后是针对选中的每一个文件进行如下操作。
值得注意的两条命令是：

* `my_command = ["soffice", "--convert-to", "pdf", arg, "--outdir", fileFolder]`
* `my_command = ["osascript", "notification.scpt", new_file, "Conversion Finished"]`

前者是格式转换的命令，注意这里加了 `"--outdir", fileFolder` 来指明输出的目录为所选文件所在目录，后者负责为每一个完成的文件发送通知。

这个动作到这里就制作完成了，操作起来也很简单：

1. 选中文件；
2. 长按 `⌘Command - 空格` 或其他你自定义的快捷键，通过 Instant Send 功能发送到 LaunchBar；
3. 输入 `convert to pdf`，选中对应动作，回车即可。

如文章开头视频中所展示的，整个过程不到 2 秒，可以将格式各异的 Office 文件统一转换为 PDF。

Automator 版动作
-------------

为了方便没有 LaunchBar 的人使用，在这里制作了同一动作的 Automator 版本，相比 LaunchBar 的动作，目前无法针对每一个文件发送完成通知，只能全部完成之后发送一个通知。

[下载](https://cdn.sspai.com/converttopdf.workflow.zip) 这个 Automator workflow 后，具体操作如下：

![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/D5980EF4-BC69-4115-80D7-321DF6F021B6)

新建 workflow

在Automatic中新建一个 workflow，这里选择 Service，以便于选中文件之后右键在服务中找到这个 workflow

![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/D7DBE137-98C4-433B-9EBF-22D313D25784)

逐一创建动作

接着按照图片里标记的顺序来创建这个动作：

1. 把「Service receives selected」这里改为「documents」，因为我们处理的对象是 office 文档；
2. 应用环境选择 Finder；
3. 添加一个动作「Get Selected Finder Items」，因为我们处理的对象是Finder里的文件；
4. 添加运行脚本动作「Run Shell Script」并将语言选择为 Python，把「Pass Input」改为「as arguments」；
5. 把下面的一段代码粘贴上去，注意这里的代码和上一节的完全一样，只是去掉了通知部分代码，因为我不清楚怎么把通知脚本内嵌到这个 workflow 里，只能采用别的方式弹出通知；
6. 添加弹出通知动作「Display Notification」，标题和副标题可以自己选择；
7. 保存 workflow，大功告成，我这里给这个 workflow 取的名字是「convertoPDF」。

```
#!/usr/bin/env python
#
import sys
import subprocess as sp
import os
import json
import shutil
my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
        fileFolder = os.path.dirname(arg)
        new_file= os.path.basename(arg)
        my_command = ["soffice", "--convert-to", "pdf", arg, "--outdir", fileFolder]
        sp.check_output(my_command, env=my_env)
```

使用起来也很简单，选中需要转换的 Office 文档，右键，在服务里选择「convertoPDF」即可。

![](.evernote-content/71E3D3E1-F4BE-4E14-A881-50952866AB2D/6CF9B208-8E4B-46D4-8B7A-D11E05AF3DEF)

Automator workflow 使用效果

最后
--

理论上任何针对文件的 Terminal 命令都可以通过制作 LaunchBar 或 Automator 动作的方式将其操作简化。

[LibreOffice](https://www.libreoffice.org/) 支持的文件格式转换还有很多，除了 PDF 之外还有 epub/html 等等，Libreoffice 的其他功能也很强大，有兴趣的可以自行研究。

注：本文借鉴了 @Minja 在 [Power+](https://sspai.com/series/9/list) 中的一篇文章《通吃常用格式，用 LaunchBar 快速无损压缩图片 | 工作日志》。

> 和高效率的生活，你只差这一步：订阅 [Power+](https://sspai.com/series/9) 专栏

---

[🌐 原始链接](https://sspai.com/post/44140)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bdaa1eb4-0666-4bb1-8ea0-72818c1857c3/bdaa1eb4-0666-4bb1-8ea0-72818c1857c3/)