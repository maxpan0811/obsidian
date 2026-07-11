# OS X 效率启动器 Alfred 的最佳伴侣：Alfred Remote for iOS 上手详解 - 少数派

---

**[Alfred](http://www.alfredapp.com/) 是什么？它是一款 OS X 效率启动类应用，旨在帮助用户以键盘的高效代替鼠标操作的繁冗。**对于非特殊/专业用户，（每天）用户一般可以在系统中进行上百次操作，可以是点击，也可以是拖拽，但相比之下，有一部分用户更离不开键盘，而非鼠标，所以前者的重要性可想而知，而 Alfred 就是一款极大提高键盘用户的操作效率的工具之一。笔者曾数次介绍过 Alfred 及其使用技巧，有兴趣的读者可 [点此阅读](http://sspai.com/search/alfred)。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/43F3EE93-8F57-422D-BABB-1E53C2BE2411.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/6db978a1d5cc68c3a7eaf330d225d56635b4e_mw_800_wm_1_wmp_3.jpg)

**[Alfred Remote](http://www.alfredapp.com/remote/) 是什么？它是为 Mac 端 Alfred 而诞生的 iOS 端辅助应用。让用户在 iOS 设备上也能便捷高效地操控 Mac、与 Mac 实现协作互通。**换句话说，就是 Alfred Remote 需要依附 Alfred 本身方可正常使用，就好比先前介绍过的 BetterTouchTool 的辅助应用 [BTT Remote](http://sspai.com/27105) 一样。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/E554AB32-5600-4BF0-ABFD-76A670EDB111.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/dfc31db8ad46548e950d0f6ac89b06fd35b50_mw_800_wm_1_wmp_3.jpg)

**使用 Alfred Remote 的理由是什么？**既然我们拥有了 Mac 电脑，也安装了 Alfred，再去购买 Alfred Remote for iOS 难道没觉得有些多此一举？这个观点看似合理，其实并无道理。打一比方，很多用 Macbook 的人还是会单独够买 Magic Trackpad 触摸板使用，因为它的面积更大，位置也可自由调整，而不是固定在笔记本的正中央。Alfred Remote 是为了让在 Mac 上使用 Alfred 的用户能有更高的操作效率、更自由的使用体验，而这样的多设备联动、多平台扩展的形式，让 Alfred 拥有了更广阔的想象空间。

首次使用的配置方法
---------

**目前，若要尝鲜体验到 Alfred Remote 的效果，需要在 Mac 上先将 Alfred 更新至 Pre-Release 版本。**具体来说，首先勾上「Alfred - 偏好设置 - Update」标签页里的「Automatically check for」选项，并在后面选择 pre-releases，最后重启一下偏好设置即可检查到更新。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/906863D3-5B16-4843-9831-D5EC99F8AFB1.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/d0d8c9eeaee3bc3efb26fc3f9a50b34935b52_mw_800_wm_1_wmp_3.jpg)

**其次，Alfred Remote 还要求与桌面端 Mac 保持在同一局域网环境下。**使用前，要先开启「Alfred - 偏好设置 - Remote」标签页下的「Enable Alfred Remote Server」选项，再点击右下角 Add iOS Remote 并打开 iOS 客户端，保持同一局域网环境，就能相互找到对方，输入随机验证码绑定后就可以正常控制了。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/1B0AFD0D-3886-4A63-97B2-0AFEF45F5014.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/fc9a4152506efa3c256babb1e45609c935b53_mw_800_wm_1_wmp_3.jpg)

注意，启用 Remote 功能并不必须购买 Alfred Powerpack 拓展包，但无法解锁高级功能。**什么是 Powerpack 拓展包？这是 Alfred 功能上的一个附加内容，主要用于解锁 Alfred Workflows 和 Remote 等高级功能。**当然，若只想实现基本的快速启动功能的话，用户可以直接选择免费版。但要想让 Alfred 做更多事情，还是非常值得购买它，而下文也将围绕 Powerpack 的高级功能展开。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/429502B6-D7B9-4019-A7C9-925348F62AAB.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/7b25d52f74473b02bfe19ccfc8c2922b35b54_mw_800_wm_1_wmp_3.jpg)

以下 Alfred Remote 功能需要依靠 Powerpack 扩展包：

* 控制 iTunes
* 剪切板快捷短语
* 运行脚本
* 运行 Applescript 脚本
* 运行终端指令（Terminal Command）
* 触发扩展

Alfred Remote 使用基础
------------------

Alfred Remote 的操作习惯与桌面端 Alfred 有本质上的不同，前者在 iOS 设备上大多都是依靠手指点击实现 & 完成，比较简单；后者在 Mac 上则是将重点放在键盘和速度上，需要用户牢记快捷键和特殊操作方式。在功能方面，Alfred Remote 中共包括了六个区域划分，依次是：

* System Commands 系统命令
* Applications 快速启动应用程序
* Preferences 偏好设置
* Folders & Files 文件夹及文件系统
* Bookmarks 书签及收藏夹
* iTunes Control 音乐播放控制

每个区域都有共同的特点，即用户界面与 iOS 系统雷同，既支持大屏 iPad 设备，也支持小屏 iPhone 设备，最下方 Dock 为分类总览，其上方的每个「格子」皆为单独项目，轻按即可运行，且所有项目都是通过 Mac 端进行设置的，可按照分类自由定义，亦可通过左下角「加号键 - Blank Page」创建新分类。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/D0BF0A45-714B-4F9F-86D3-D7FECE1711B2.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/5548ffacc8339e2d45a49e8219dac8f635b55_mw_800_wm_1_wmp_3.jpg)

在选定功能分类后，点选格子中的图标并右键，可以查看相关的操作方式，例如基本的：设置、剪切、拷贝、删除等。拖拽可以移动位置，可惜目前不支持覆盖移动，所以重新排版的时候比较麻烦。点击「空格子」区域会出现一个菜单，其中包括所有可以实现的功能。读者不妨先自行琢磨着体验一把，接下来我们着重来介绍「实例」技巧。

### 注意事项

Alfred Remote 默认使用 49689 端口进行通讯，若你发现自己的 Remote 客户端无法成功与 Mac 连接，有一定可能是由于端口冲突导致的，手动修改为另一 Port 即可解决。同时，该界面下也允许用户手动勾选「通知」方面的服务，为保护电脑不被在未知情况下受控，建议全部开启。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/F207927B-B490-4054-B424-DB746129816D.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/c844edb8a200811f6c516d6d3ad95eab35b58_mw_800_wm_1_wmp_3.jpg)

在左侧「总览区」中，每个分类项目都拥有单独的图标、标题和副标题，殊不知其「功能编辑区」的右键菜单中，Configure 功能还能让我们自定义文字及背景的颜色。如果你看默认配色方案不爽，那这个功能算是发挥其作用了。万一出错了，轻击 Default 还原。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/00723147-DC99-42B4-AF3F-9892CB263C5A.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/f80d4f187004495f089acf3e070a82b935b5a_mw_800_wm_1_wmp_3.jpg)

快捷短语 Snippets
-------------

快捷短语功能即 Snippets，它可帮助用户以组合键或其它便捷的方式，快速输入固定短语或带有「变量」的语句，专注 Snippets 的应用有 [TextExpander](http://sspai.com/tag/TextExpander)。Alfred Remote 也加入了这一功能，目前我们可以通过「创建 Clipboard Snippets 分类」或「添加 Clipboard Snippet 功能」建立。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/1E7888D0-EB23-4F15-8DA5-38502DBFC16F.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/53a2913fbcaba9f46faa152c4322aae635b5b_mw_800_wm_1_wmp_3.jpg)

语法方面，我们可以先看一眼自带的范例（见下图）。这是一个关于 Dates（时间 & 日期）的 Snippet，固定的内容为纯文本语句，那带有 {} 符号的文本则为变量。目前 Alfred Remote 支持的主体语法变量包括三种（最下方灰色字体有标明）：{time} 表示时间、{date} 表示日期、{clipboard} 表示剪贴板。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/CF985FB6-8C22-4F91-B83B-99443F63DBA5.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/dfaba4a9d9ddd24dd353ef3efca45c3735b5f_mw_800_wm_1_wmp_3.jpg)

Date 类的分部语法格式包括：{date:short} 短日期、{date:medium} 偏长日期、{date:long} 长日期、{date:full} 全长日期。其它分类的语法中也有对应的格式，具体请大家参考余下的范例。目前 Snippets 只支持纯文本，富文本和多媒体文件暂不确定将来是否会加入，期待开发商能有这方面的考虑。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/A3861BB2-9CCD-4EA1-BE96-622B58B8EF9E.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/83d634317da9e6facbb206b52937abc335b60_mw_800_wm_1_wmp_3.jpg)

还要提一下，Snippets 功能不一定是直接输入至 Mac 端的，也可以先拷贝至其剪贴板，再经由该设备主动地进行粘贴。若要实现这一效果，须在创建 Snippets 的同时，将状态由默认的「Paste text to active app in OS X」改为「Place text in OS X clipboard」方可。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/F8172588-4F5B-41F0-B485-A6F1A065BD0D.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/4399406daccfd372eebf5887d42d8b7335b61_mw_800_wm_1_wmp_3.jpg)

扩展触发 Workflows Trigger
----------------------

若要在 iOS 设备上实现 Alfred 扩展的直接或间接执行，有两种方法：生成针对 Remote 开发的扩展、通过 Trigger 定位至已经安装了的扩展并间接触发。笔者自认为能力不足，无法向读者解释具体的 Alfred 扩展开发步骤，因此，接下来主要谈谈 Trigger 引用的方法。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/19C9AE20-E1D7-4AF0-8914-C643CEF92CCC.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/23849928de6fa6d2d7d593687998983835b62_mw_800_wm_1_wmp_3.jpg)

拿一个简单的 Relaunch  扩展举例吧。首先要做的，就是在 Alfred 扩展的标签页下找到它。接着，点击右上角「加号键 - Triggers - Remote」生成一个新的 Remote Trigger，在 Identifier 处为其命名，并在左侧 UI 界面里填入描述。最后将 Trigger 与触发点拼接即可。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/65BD8383-7F4E-4380-88B4-EDC8E07B7879.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/396e7970b19705db5196ae114260553935b63_mw_800_wm_1_wmp_3.jpg)

到这里只是完成了扩展方面的操作步骤，接下来还要为 iOS 端添加这一 Trigger，如何实现？点击空白空格上的「加号键」选择「Run Workflow Trigger」，在其中找到我们刚才编辑好的 Relaunch 扩展，轻敲就能完成添加。这时可以发现，iOS 端已经添加了这一 Trigger，点击就能直接激活 Relaunch 功能，很不错吧？

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/9BBFCD4B-6531-4A4D-B0C1-FB23D350783D.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/6ed7c487767aee36277e77864115cbc635b64_mw_800_wm_1_wmp_3.jpg)

简单的演示差不多就这样，感兴趣的小伙伴可以在扩展（Workflows）标签的左下角，添加由开发商为 Remote Trigger 量身订制的扩展（见下图）。各位可自行琢磨，笔者这里暂时不打算详细分解介绍，或许会留在「进阶篇」中叙述，望读者保持关注！

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/92928252-EB41-4467-A564-5EADC89C2A96.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/11ccb0d1626f7bcd868507f4d01790dc35b66_mw_800_wm_1_wmp_3.jpg)

写在最后
----

Alfred 在 Mac 平台自一开始就以其高质量、高效率而倍受关注，新生的 Alfred Remote 同样如此。在开发商发布 iOS 客户端之初，笔者就火急火燎地为大家带来这篇还算全面的体验详解，但这并不代表最终效果，因为开头说过，该版本的 Alfred 只是 Pre-release，因此本文更多地是给想尝鲜但又犹豫不决的读者一个初步的上手详解。

[![](.evernote-content/C0A347F5-E8C6-4702-84C6-5CAA4FB102AA/C39689A5-9629-4271-BD0D-D83E6F86B4D0.jpg)](http://cdn.sspai.com/attachment/thumbnail/2015/01/28/cd439a295407d46eca42d34fca8c8f6235b65_mw_800_wm_1_wmp_3.jpg)

作为新开发的功能，谁都不保证 Alfred 与 Remote 能有非常稳定的运行效果。鉴于要迎合大众的需求，笔者建议各位在遇到问题时积极向开发商反馈，或前往 [帮助页面](http://support.alfredapp.com/remote:connection-troubleshooting) 获取解决方案。最后，欢迎有能力的读者在 [微博](http://weibo.com/sspaime/) 或 [社区](http://sspai.com/t) 与我们分享交流更多自己制作的 Remote Trigger。

各位目前可前往 [App Store 下载](https://itunes.apple.com/app/alfred-remote/id927944141?mt=8&uo=4&uo=4&at=10lJSw) Alfred Remote，售价 ￥30 元人民币，若你已在 Mac 上使用 Alfred，建议首选考虑。

---

[🌐 原始链接](http://sspai.com/28137)

[📎 在印象笔记中打开](evernote:///view/207087/s1/b18f2143-1dd0-44df-a638-6045e63b7e75/b18f2143-1dd0-44df-a638-6045e63b7e75/)