---
title: "一切为了让效率更进一步，Alfred 4.0 更新详解"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/一切为了让效率更进一步，Alfred 4.0 更新详解.md
tags: [印象笔记]
---

# 一切为了让效率更进一步，Alfred 4.0 更新详解

# 一切为了让效率更进一步，Alfred 4.0 更新详解 --- 一切为了让效率更进一步，Alfred 4.0 更新详解 =========================== 06 月 06 日 

---

# 一切为了让效率更进一步，Alfred 4.0 更新详解

---

一切为了让效率更进一步，Alfred 4.0 更新详解
===========================

06 月 06 日

[![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/20AA18EB-9F73-4994-8606-9EC1491AB3F8)](https://sspai.com/user/742287/updates) 

#### [涔 C](https://sspai.com/user/742287/updates)

macOS 上的效率应用五花八门、丰富异常，其中的 Alfred 位列许多用户的必备清单之首。应用与文件搜索、剪贴板管理、快捷短语输入，以及丰富全面的 Workflow 等功能都让用户享受到了便利和良好的使用体验。

近日，Alfred 迎来了时隔两年的 4.0 大版本更新，我们一起来看看吧。

深色模式与界面调整
---------

深色模式，毫无意外地出现在新版本中。Alfred 输入框、偏好设置界面都会随系统外观模式而自动变化。将系统切换至深色模式后，在 Alfred 偏好设置中选择的主题，就是 Alfred 的深色模式主题，简单直接。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/6F6FFF80-1D53-4437-B2D4-67CECD26B71A.png)

深色模式、界面布局

￼偏好设置界面中，面板标签由上方横排变为左侧竖排，与面板内的竖排布局相统一，交互更加一致。右上角添加了一个搜索框，可以搜索各项偏好设置，也可使用快捷键 `⌘Command-F` 激活搜索框。Features 面板中，常用的 Clipboard 与 Snippets 功能页面位置前移。并且，File Preview 功能独立出来，置于 Features 列表末尾，以方便直达该功能。

此外，macOS 中的效率应用难免都需要申请各种权限。Alfred 特地在 General 面板中加入 macOS 权限配置按钮「Permissions: Request Permissions…」，并配有启用权限的示意图片。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/1DCD1182-A272-425C-AB51-9ABD8B4C8650.png)

权限配置

￼深入内部的偏好设置搜索
------------

除了偏好设置界面的搜索框，我们还可以直接在 Alfred 输入框中使用 `?关键词` 搜索偏好设置。Features 中的每项功能、Snippets 中的每条片段、网络搜索的每个搜索引擎、以及每个 Workflow 中的所有对象，都可以搜索到，然后按下回车键直达。搜索结果列表的最后一项始终是在 Alfred Help 网站中搜索，方便用户快速访问帮助文档。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/D42A1293-3502-48B2-84A0-2C03588F5F3F.png)

偏好设置搜索

￼新版本对于 Workflow 的编辑流程用心做了优化。选择 `?关键词` 搜索结果中 Workflow 对象并回车，会打开偏好设置的 Workflow 界面并定位到该对象，按下回车就可以直接打开进行编辑。整个过程快捷顺畅，体验很棒。

此外，搜索 `?hotkey`、`?keyword` 可以列出所有的快捷键与动作关键词，包含 Alfred 内置功能和所有安装的 Workflow ，再也不用因为忘记它们而烦恼。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/169C2488-17AB-46DC-8B3F-EF4B7646BAA4.png)

Hotkey 搜索

￼更加省心的搜索引擎
----------

新版本在配置搜索引擎时，借助网站方面的 OpenSearch 与 SearchAction 协议实现自动化填写 Search URL。不再像以前那样需要自己寻找关键词参数位置，然后替换为 {query} 了。添加搜索引擎时，在 Search URL 文本框中填入网站的域名，然后点击右侧的「Lookup」就会自动分析并显示可用的搜索链接格式，接着点击「Use」就可以了。但遗憾的是，并非所有网站都支持 OpenSearch 或 SearchAction 协议。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/87C739CD-C95F-4E14-B7D9-1F3F18E5A7C6.png)

Lookup 功能

￼Alfred 同样优化了添加搜索引擎的整个流程，可以脱离鼠标进行全键盘操作，过程如下：

1. 快捷键唤出 Alfred，输入 `?Web search`，回车打开配置面板。
2. 按下 `⌘Command-N` 添加搜索引擎。
3. 直接输入网站域名（默认为 HTTPS），回车键运行「Lookup」。
4. 使用 `⌘Command-1/2` 选择可用的分析结果。
5. 光标自动移至 Keyword 输入框，输入后，按下回车就设置完毕了。

但美中不足的是，作为搜索时标题的 Title 一栏，使用的是形如 `https://www.pinterest.com` 的域名而非网站名称，不够美观。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/59A258FC-A910-4D72-825D-F41CB41BD919.png)

Alfred 中搜索引擎的标题栏

￼支持富文本的快捷短语
-----------

快捷短语功能 Snippets 在工作生活中非常有用，比如我就经常用来输入固定格式的时间日期，特定功能的 Google 搜索短语等。Alfred 能够胜任这些任务，但是基本上也仅限于此。新版本为之加入了富文本支持，对于编写邮件等日常事务很有帮助，进一步扩展了使用场景。附加的编辑菜单，支持字体、粗体 / 斜体 / 下划线、颜色、复制 / 粘贴格式等简单的调整选项。另外，还能够自动识别副本文中的链接文本。如果这些编辑功能不能满足要求，我们也可以在「文本编辑」应用中编辑后粘贴过来。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/B7020650-C792-4460-AE30-B90F6FC63FAB.png)

富文本 Snippet

￼其它方面：富文本 Snippet 会在列表中用 ✴️️ 加以标记；音效设置分割为可分别启用的 Snippet 短语和 Workflow 两种，可以选择系统音效，或拖拽加入自定义音乐文件。

加强的占位符语法
--------

主要用在 Snippets 中的占位符（Placeholder）功能也得到加强，除了之前就支持的当前日期、剪贴板等选项，还加入了随机值占位符 `{random}`，包含：

* 随机的通用唯一标识符 UUID： `{random:UUID}`，形如 `5FAF0AC6-B410-446C-A311-E41074205A05`
* 随机数字：`{random:1..10}`
* 列表中的随机项：`{random:苹果,香蕉,梨,葡萄,橙子}`

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/1DF69ED9-44FF-4033-A194-2264E76A8AFA.png)

占位符菜单

￼另外，新版本引入了形如 `{placeholder:variation.modifier}` 的占位符语法，可分为三部份：placeholder 占位符类别、variation 变种（可理解为参数或子类别）、modifier 修饰符。生成 1 到 10 之间随机数字的占位符 `{random:1..10}` 中 `random` 是 placeholder 占位符类别，`1..10` 部分是 variation 变种，而 modifier 修饰符部分，可以选择这些：

* `trim`：删去内容前后的换行、空格等空白字符。
* `reverse`：文本反转。
* `stripdiacritics`：去除重音标记，如 å 变为 a。
* `stripnonalphanumeric`：去除标点符号、Emoji 等非字母数字的字符。
* `uppercase`、`lowercase`、`capitalcase`：大写、小写、首字母大写转换。

这些修饰符同样可用于剪贴板占位符、Workflow 内的变量，例如 `{clipboard:3.reverse}` 代表反转第三条剪贴板历史的内容；`{var:result.trim.uppercase}` 代表将 result 变量的内容，删除前后空白字符后，再转换为大写。可以看到，修饰符部分支持复合连用。

得到完善的主题编辑器
----------

作为每天使用的应用，赏心悦目的主题十分必要，Alfred 此前的主题编辑器可用但不好用。新版本对编辑器的诸多细节做了优化。光标悬浮在界面元素上方，会使之高亮，指明正在设置的部分。编辑器界面下方显示当前编辑的元素名称与操作提示。并且，光标根据当前元素可执行的操作，变为上下拖动等动作标志。右键菜单中，列出当前主题内已经使用的颜色，以及已经使用字体的其他样式（粗体、斜体等），方便选择。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/5A0E5A37-64A3-4AA0-904E-3030BEE785D8.png)

主题编辑器

￼文件导航与文件缓存
----------

在 Alfred 中输入文件路径，或者使用快捷键 `⌘Command-⌥Option-/` 唤出，就会进入文件导航模式。左侧是文件列表，右侧是文件预览。新版本在右下角添加了一个配置菜单，点击 ⚙️️ 图标可以看到有这些选项：

* 排序方式：名称、创建日期、修改日期
* 文件夹置顶
* 逆序排列，快捷键 `⇧Shift- ⌘Command-S`
* 隐藏预览面板，快捷键 `⇧Shift- ⌘Command-I`

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/39CF0077-D824-41B8-94F8-028271FEB381.png)

文件导航模式

￼Alfred 中的文件缓存功能往往被用户忽略，但其实用来批量操作文件很好用。无论是直接搜索文件、文件导航模式中的文件列表，或者 Workflow 运行结果列表中的文件或文件夹，都可以用 `⌥Option-↑` 等快捷键缓存至输入框上方，然后按下 `⌥Option-→` 打开文件动作列表，进行批量操作。新版本中，为加入缓存的文件条目附上了专门的标记，以作区分。并且，光标移动至缓存区域，可以看到在原来名称、路径的基础上，工具提示又加入了快捷键说明 `⌥ Click to remove, ⌥⌫ to remove all, ⌥ → to action all`。看来新版本确实很为用户的记忆力担忧。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/7CCFACFC-6AB8-4BD6-AC63-60EE36670ECA.png)

￼此外，这里插播一则有趣的小改动。新版本中，默认禁止通过应用的关键词元数据进行搜索匹配。我们以 iOS 设备管理应用 iMazing 为例说明，打开 iMazing 的简介可以看到有一栏是关键词，后面跟着 `iOS, iPhone, iPad, iPod, Backup, Back up` 等几十个与其功能相关的词语。iMazing 在自身添加这些信息，就是为了用户在 Spotlight、Alfred、LaunchBar 等应用搜索这些词语时，匹配并显示出来。一方面，这确实可以带来一定的便利，但是另一方面也会扰乱搜索结果，所以 Alfred 新版本默认禁止了这种乱刷存在感的行为。不过，如果觉得用着还不错，我们可以在「偏好设置 - Features - Default Results」 功能界面最上方 「Applications Options」 中，勾选「Match Application’s keywords in default results」启用这个功能。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/91402C44-D047-401B-932B-D95EE2625B69.png)

￼更加全面的 Workflow
---------------

Workflow 作为 Alfred 的进阶功能，众多方便好用的 Workflow 正是吸引用户选择 Alfred 的重要方面。新版本进一步丰富 Workflow 对象库，添加了这几种：

* Utility > Conditional 条件选择工具，该对象相当于编程语言中的 `if else` 语句，可取代原有的 Filter Utility 过滤工具对象，用来判断情况做出选择。可选的条件判断方式有：等于、不等于、大于、小于和正则匹配。支持任意多个条件分支，每个分支后可连接一个其他对象。分支的排序可以通过拖拽调整。用户可以参考内置的 Workflow 样例「Examples > Simple To-Do List」中的用法。条件选择工具的加入，让编写 Workflow 更加简单，减少了对于代码的依赖，让普通用户也能够顺利上手。
* Utility > Split Arg to Vars 分隔工具，该对象可以将传入的文本分隔并保存为多个变量，传递到后续对象。其中，分隔符可自定义，默认为英文逗号。分隔后生成的变量可以自定义名称前缀，比如设置为 `name`，那么变量名称就是 `name1`、`name2` 等。
* Utility > Random 随机工具，与 Snippets 部分的随机值类似，可以生成随机的 UUID、指定范围的随机数字、列表中的随机项，后两者中可以使用传入值 {query} 和变量。
* Utility > Show Alfred 显示 Alfred 工具，显示 Alfred 输入框并输入指定的文本，可以选择光标位置。
* Action > Browse in Terminal 终端中打开指定路径，可以同时处理传入的多个路径。

新版本对于旧有的对象也做出了许多优化：

* Input > File Filter，新增 limit and sort 面板，可配置候选数量、排序方式、日期范围。Search Fields 可用变量占位符，从而更简单地创建动态搜索，之前需要借助 Json 配置工具。
* Input > keyword，去除必须设置 keyword 才能保存的限制。
* Input > Script Filter，输入 query 为空时，不再传递脚本参数。
* Trigger > Hotkey，增加 Find Pasteboard 参数选项。
* Utility > Replace，增加使用 Regex 时的多行、区分大小写选项。
* Output > Copy to Clipboard，支持富文本格式。
* Output > Play Sound，可以更方便地拖入音频文件，不再限制格式为 m4a、aif。
* Output > Large Type，可设置字体、颜色、对齐、淡入速度、背景填充等。

Workflow 对象之间的链接可以用复合修饰键了，如运行 Workflow 时按下 `⇧Shift + ⌘Command` 选择执行额外的操作。Workflow 导出时，显示配置表单，方便设置名称、环境变量、版本号、功能描述等必要信息。导入时，则是显示这些信息，方便配置环境变量，查看功能描述。

调试器（Debugger）对于制作 Workflow 是非常必要的工具，新版本同样优化了这方面。现在，可以使用快捷键 `⌘Command-D` 打开调试器。显示的调试信息，能够选择是对应当前 Workflow、或所有 Workflow。而且，点击不同的 Workflow 时，调试器窗口会保持显示，再也不用像以前那样每次切换都要重新打开调试器，极大地改善了调试多个 Workflow 的体验。调试信息中，涉及的对象名称会被高亮显示，而且点击就会在编辑器内被选中，直接按下回车键打开编辑。

版本升级与数据迁移
---------

版本升级过程中，数据备份与迁移是重中之重。下载新版本 Alfred 后运行，首先显示的是配置引导界面，点击「Begin Setup…」开始。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/64596134-79F3-4134-AFAB-CD2590600E89.png)

配置引导

￼第一步是激活 PowerPack 许可。按提示填写 Alfred 4 的许可邮箱、许可代码，然后点击「Activate Your Powerpack」激活。如果只有旧版本许可，可以填写后点击「Buy or Upgrade Powerpack」升级，或不填写直接点击购买。如果不打算使用 PowerPack 部分功能（含文件导航、剪贴板历史、通讯录、iTunes Mini 播放器以及 Workflow 等），那么可以直接点击右下角的「Continue without Powerpack」跳过该步骤。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/04FD27F3-6934-429B-8359-ACF8BAC1F0FF.png)

激活 PowerPack

￼第二步是备份与迁移配置数据。点击「Backup files above to tar.gz file」进行备份。然后根据自己的情况，选择下方配置迁移的选项，一般默认即可。而后点击右下角的「Begin Migration」开始迁移。如果之前没有使用 Alfred，那么此时会显示「No previous versions of Alfred found, continue without miagration」不需要迁移数据的信息。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/A6D337BA-2556-4164-B670-D70733D50D3B.png)

备份与迁移配置数据

￼第三步是授予权限。macOS 系统中的应用难免要申请各种权限，尤其是 Alfred 这种涉及系统各方面的效率应用。在第一次使用时就把权限配置好，会省去不少麻烦。依次点击界面上的三个按钮，在打开的 macOS 系统偏好设置中授予权限。**需要注意：**有时授予权限后，系统会提示需要「退出」Alfred 以生效，这时应该选择「稍后」。等到所有权限配置完毕后，再在 Alfred 界面中选择「Restart Alfred」以重启生效。

![](.evernote-content/4847FE0E-549F-4EB0-A707-7D977F453CBE/39294412-25CE-43D8-B795-4B09995B16B0.png)

授予权限

￼然后，就可以开始使用了。

价格方面
----

Mega Supporter 终身许可，以及在 2019 年购买单版本许可的用户可免费升级，其他用户可以付费 15 英镑或 25 英镑升级为新的单版本许可或终身许可。

总结
--

时隔两年的这次大更新，功能上，偏好设置搜索、富文本 Snippet、Workflow 增强等无一不是用户呼声已久的特性。使用体验方面，深色模式、主题编辑、搜索引擎添加流程、Workflow 编辑流程都得到了全力优化。扩展使用场景、贯通使用流程、降低用户门槛，新版本抓住了一款效率应用需要做好的重点。4.0 只是个开始，让我们拭目以待。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](http://sspai.com/s/KEPQ) ，了解更多有趣的应用

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

[#热门文章](https://sspai.com/tag/%E7%83%AD%E9%97%A8%E6%96%87%E7%AB%A0)[#应用推荐](https://sspai.com/tag/%E5%BA%94%E7%94%A8%E6%8E%A8%E8%8D%90)[#Alfred](https://sspai.com/tag/Alfred)[#效率](https://sspai.com/tag/%E6%95%88%E7%8E%87)

---

[🌐 原始链接](https://sspai.com/post/55098)

[📎 在印象笔记中打开](evernote:///view/207087/s1/46cbc4d4-6e87-4907-bdb0-0890b60a12e5/46cbc4d4-6e87-4907-bdb0-0890b60a12e5/)