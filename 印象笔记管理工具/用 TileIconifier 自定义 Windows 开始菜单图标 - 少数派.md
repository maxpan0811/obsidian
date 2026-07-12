# 用 TileIconifier 自定义 Windows 开始菜单图标 - 少数派

---

用 TileIconifier 自定义 Windows 开始菜单图标
==================================

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/FADFE5ED-5D3D-4A8E-99D9-9ABF862A9302)

用 TileIconifier 自定义 Windows 开始菜单图标

### **Matrix 精选**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

Windows 开始菜单是我们大多数 Windows 用户使用 Windows 的起点。最近 Windows 10 除了在逐步更新一些 Windows 图标，使之匹配 Fluent Design 设计风格，还给我们提前看了一眼未来可能出现在正式版 Windows 系统中的开始菜单新设计。1

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/D4A59CB7-51A9-47BA-99A4-E5341757F5AA.jpg)

来自 Microsoft Design 的 Windows 10 开始菜单新设计

新开始菜单将经典的自定义 Windows 强调色剔除，统一了暗色和亮色的设计风格，确实令人眼前一新。不过，其实在现在的 Windows 系统里，我们用合适的工具为「Windows 开始菜单图标」填上一个背景颜色（比如纯白色、纯黑色），也能实现类似的效果，解解眼馋。

下载安装
----

本文使用的工具叫做：[TileIconifier](https://github.com/Jonno12345/TileIconifier)，一个可以自定义 Windows 开始菜单程序图标、背景颜色等设计元素的小工具。我们可以 [前往 TileIconifier 的 Release 页面](https://github.com/Jonno12345/TileIconifier/releases/latest) 下载，解压得到一个 exe 文件直接运行即可。虽然这一工具在 2018 年就停止了更新，但其功能并无任何缺失，可以继续使用。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/979236E4-09EE-4B2F-B308-10CE9485CA6F.png)

在 GitHub 上下载、运行 TileIconifie

使用 TileIconifier 对单个 Tile 进行修改
------------------------------

TileIconifier 是一个独立的 exe 应用程序，直接双击即可使用。给予 TileIconifier 权限之后，TileIconifier 即可自动识别出当前位于开始菜单中的所有应用程序的快捷方式（但不包括 Windows Store 安装的应用）。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/DC2D773C-F49A-4FBB-A7D8-365402407A53.png)

TileIconifier 自动列出开始菜单中的全部应用程序

我们可以在上方搜索框中搜索我们想要修改的应用图标，并在右侧「双击」进入图标选择。TileIconifier 会自动的将应用对应的图标默认图标找到，方便我们直接使用，当然我们也可以使用自己准备的图标。之后，我们调整「中号」和「小号」图标内 icon 尺寸（一般以中号 `16%`，小号 `7%` 为宜），并自己定义一个背景颜色，最后再将图标显示的文本名称颜色进行修改，点击「Tile Iconify!」就大功告成了！

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/CCD2D614-1143-43F1-AC21-47C2B85A2602.gif)

使用 TileIconifier 修改微信的图标

我一般都会用取色器选择原应用图标中的强调色（accent color），之后调整颜色的深浅为稍深一点的色调，这样搭配出来的 Windows Tile 比较好看。另外，如果你想要实现前文提到的新版 Windows 开始菜单的样子，也可以直接使用「浅色主题」并将所有的应用图标 Tile 的背景颜色调整为浅白色 `#fbfbfb`，虽然没有半透明磨砂的 Acrylic 效果，但是也相差无几了（如果你用「深色主题」，那么就将背景颜色调整为深灰色 `#2d2d30`）。

可以看到，TileIconifier 自定义图标是实时更新的，点击完成之后，Windows 的开始菜单会自动刷新，显示我们自定义的新图标。

使用 TileIconifier 生成自定义 Tile
---------------------------

除了在原有 Tile 的基础之上进行图标、背景颜色的更改，我们还可以用 TileIconifier 生成自定义的快捷方式，并用它们作为 Windows 开始菜单里的 Tile。我们点击工具栏中的「Utilities → Custom Shortcut Manager」，就可以开始进行自定义了。

TileIconifier 直接支持生成「进入特定文件夹」、「特定 Steam 游戏」、「特定 Chrome 应用（PWA 应用）」以及「打开特定 URL」、「执行特定命令」的快捷方式。（使用 TileIconifier 制作的 Windows Store 应用我个人没有成功，可能由于版本尚未支持。）

### 进入文件夹的快捷方式 Tile

TileIconifier 能够为我们直接生成进入文件资源管理器任意目录的快捷方式 Tile，同时还支持打开比如控制面板、应用程序文件夹、控制中心等等的特殊文件夹（可以在 Special Folder 中进行选择）。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/D278B8FB-BAE1-43BC-9B94-2607025C5AA2.png)

使用 TileIconifier 生成打开特定文件夹的快捷方式 Tile

我们还可以用 TileIconifier 自定义文件夹快捷方式的图标。推荐大家选用 Icons8 图标库提供的「文件夹图标」集合：[Color Icons of Folders - Icons8](https://icons8.com/icon/pack/folders/color)，虽然只能下载 96px 大小的图标，但是对于 Windows 开始菜单的显示也是绰绰有余的了。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/A54CF0A3-1934-4E35-BEB9-1D6492BA981D.png)

Color Icons of Folders - Icons

### 打开某个 URL 的快捷方式 Tile

我们还可以用 TileIconifier 来生成打开某个 URL 的快捷方式 Tile，这个 URL 不仅仅可以是网站的 URL 地址，还可以是如下图例子中所示的「Spotify 歌单 ID」、「邮件地址」等等。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/A7F20BAE-370C-4867-A65D-FD03447C9114.png)

使用 TileIconifier 生成打开少数派网址 URL 的快捷方式 Tile

### 执行特定命令的快捷方式 Tile

同时，TileIconifier 也可以为我们生成执行某个命令的快捷方式 Tile。这里我简单举一个例子 —— 使用 Windows Terminal 打开 Ubuntu WSL 环境：

```
wt.exe -p Ubuntu
```

我们实际上执行的就是上面这一命令。在 TileIconifier 中相应的进行设置，并设置好 Tile 的图标，就生成成功了。

**关联阅读：**[新生代 Windows 终端：Windows Terminal 的全面自定义](https://sspai.com/post/59380)

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/19ABF2CA-C8B0-4FF3-9D0B-532712341ABA.png)

使用 TileIconifier 生成执行特定命令的快捷方式 Tile

另外，TileIconifier 打开 Steam 游戏、Chrome App 等操作，也是自动识别的，原理和上面介绍一致，这里就不再赘述了。

### 微调生成的快捷方式 Tile

上面步骤中默认生成的快捷方式，都位于开始菜单的 `TileIconify` 文件夹里，我们需要手动将它们固定到「开始」屏幕。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/EB8CC7A2-049D-4C32-B3E9-3933B56CE871.png)

使用 TileIconifier 生成的快捷方式

在我们上一步生成好快捷方式之后，我们会看到在 TileIconifier 的 Custom Shortcut Manager 里以及出现有刚刚定义的所有快捷方式，我们可以任意选择，点击「Goto Selected Shortcut」开始对快捷方式进行相应的微调。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/9679D346-95FB-4C4F-9CBD-41101877FB69.png)

Custom Shortcut Manager

之后，我们就会在 TileIconifier 的主菜单中看到调整快捷方式 Tile 的图标、背景、大小的界面。这一界面和我们刚刚前面修改原有快捷方式的方法是一致的。

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/797880F3-2B17-445F-8AE8-D9D1905A7058.png)

调整自定义快捷方式的图标、背景和大小等

一切配置完成之后，我们现在就可以拥有像这样的独特且漂亮的开始菜单咯。2

![](.evernote-content/EC8050FF-F3DC-445F-A285-2D0C4A7940F8/D83D1213-51E7-4F00-9E1C-15E74434A6D8.png)

全部配置之后，我的开始菜单

小结
--

很遗憾的是，TileIconifier 目前仅支持静态图标的定义，不能直接生成 Windows 标志性的动态图标 ——Live Tiles。当然，看起来 Windows 更新过后，Live Tiles 可能也会换一种方式与我们见面。本文介绍到这里就结束了，希望这篇文章能帮助你自定义更好看养眼的 Windows 开始菜单。感谢阅读。

**拓展阅读：**

> 下载少数派  [客户端](https://sspai.com/page/client) 、关注  [少数派公众号](https://sspai.com/s/J71e) ，了解更精彩的 Windows 生活

---

[🌐 原始链接](https://sspai.com/post/59919)

[📎 在印象笔记中打开](evernote:///view/207087/s1/60849c05-b968-4456-b5c8-9f9049fee89c/60849c05-b968-4456-b5c8-9f9049fee89c/)