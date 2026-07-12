# 新生代 Windows 终端：Windows Terminal 的全面自定义 - 少数派

---

新生代 Windows 终端：Windows Terminal 的全面自定义
======================================

新晋 Windows 终端模拟器：[Windows Terminal](https://www.microsoft.com/zh-cn/p/windows-terminal-preview/9n0dx20hk701)，自发布以来就备受开发者的喜爱，并与 [WSL](https://sspai.com/post/43813) 一起，让不少先前非 Linux 不用的开发者朋友们向 Windows 倾斜。Windows Terminal 不仅开源免费，还拥有现代化的界面、完整的字体字符渲染机制（包括 Emoji）、GPU 加速和 Fluent 设计风格。这些都让 Windows Terminal 成为 Windows 平台最先进的终端模拟器，力压一众第三方终端以及 Windows 自带的默认终端。

**推荐阅读：**[告别 Windows 终端的难看难用，从改造 PowerShell 的外观开始](https://sspai.com/post/52868)

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/DD9FF0ED-7725-4DD9-9D73-4D49F02EC7F0.png)

现代化 UI、丰富的自定义功能与设计的 Windows Terminal

事实上，Windows Terminal 不仅速度快、设计美，还有众多可自定义的 UI 元素、快捷键与实用功能。这篇文章中，我希望在 Windows Terminal 1.0 发布的前夕，详细介绍一下 Windows Terminal 的设置与自定义方法，并和大家分享一些让 Windows Terminal 实用且美丽起来的小技巧。

Windows Terminal 的配置文件
----------------------

首先，我们进入 Windows Terminal 的设置文件。在 Windows Terminal 的下拉菜单中，选择 Settings（或使用快捷键 `Ctrl + ,`），这一操作会使用你系统默认的文本编辑器打开 Windows Terminal 的配置文件。

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/1D52324A-A4FB-4541-BAC5-A1F2DC4880B7.png)

点击 Settings 进入 Windows Terminal 的设置

Windows Terminal 的配置文件是一个 JSON 格式的文件，我们会在其中定义全部 Windows Terminal 的属性。简单来讲，这个配置文件包含了如下的几个部分：

* **全局属性**：位于 JSON 最外侧，包含有设置亮暗主题、默认 Profile 等项目的配置。
* **环境入口 `profiles`**：一个列表，其中包含有 Windows Terminal 下拉菜单中唤起的各种环境（比如打开 PowerShell 环境、WSL 环境或 SSH 至远程服务器的环境……）与各种环境里 Windows Terminal 的显示方案（比如字体、背景、色彩方案等）。
* **配色主题 `schemes`**：一个配色方案列表，其中包含有 Windows Terminal 在上一项「环境入口」中可以调用的「色彩主题」。
* **快捷键绑定 `keybindings`**：自定义快捷键。

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/30BF1EB0-F35A-48D9-9671-B9BED2F6D96F.png)

Windows Terminal: profiles.json 配置文件的格式

熟悉了 Windows Terminal 配置文件的各项含义之后，我们即可开始对 Windows Terminal 的各项属性进行配置。

在配置文件中对 Windows Terminal 进行自定义
------------------------------

### 全局属性的配置

设置 Windows Terminal 从设置其全局属性开始，也就是它的配置文件 `profiles.json` 里面最开始的部分。在这里我们可以定义：

* Terminal 亮暗主题设置 `"requestedTheme"`：可以为 `"system"`（跟随系统）、`"light"` 或 `"dark"`
* Terminal 初始大小：`"initialCols"` 和 `"initialRows"`
* Terminal 的默认配置文件：设置打开自动进入的环境（通过 GUID 唯一标识码来识别环境）
* ……

之后，就是三个包含二级设置项目：「环境入口」、「配色主题」和「快捷键绑定」的设置。我们依次进行介绍。

### 设置 Windows Terminal 的环境入口

下拉菜单是 Windows Terminal 唤起各个环境的入口。我们通过点击「下拉菜单」的各个选项，即可唤起不同的 Windows Terminal 环境。

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/D8209A10-9185-4822-999A-8F485CC9BA8C.png)

下拉菜单中的环境入口

默认情况下，Windows Terminal 已经为我们配置了本机安装的全部命令行环境：包括 PowerShell 环境、cmd 环境以及自家云服务 Azure Cloud Shell 入口。如果你安装了 WSL（Windows Subsystem for Linux），那么 Windows Terminal 也同样将这一环境自动探测并添加。这些环境，就是 Windows Terminal 配置文件中 `"profiles"` 属性列表里面的内容，我们同样可以在这一列表中：

* 自定义某一环境的性质
* 添加我们自己的环境或命令

#### 自定义某一个环境的配置

Windows Terminal 的环境配置中可以设置其调用命令（`commandline`）、字体（`fontFace`）、颜色方案（`colorScheme`）、背景颜色（`background`）与背景图片（`backgroundImage`）等等。这里我想重点介绍一下为 Windows Terminal 一个特定环境的背景进行设置的方法。

Windows Terminal 的背景可以是一个纯色，**也可以是一张高清壁纸、GIF 动图等等**。如果是纯色的背景，在未经设置的情况下这一颜色与你环境所定义的配色方案的颜色一致，你也可以通过控制 `background` 这一属性来更换颜色。比如这里我想让 PowerShell 的背景带有一抹独特的「蓝色」，即可这一进行设置：

```
// "profiles": [ ... ] 项目中 PowerShell 环境的配置
{
    "background": "#013456",
    "acrylicOpacity": 0.8,
    "useAcrylic": true,
}
```

其中：

* `"background"` 与后面的 HEX 颜色即定义了背景颜色
* `"useAcrylic"` 表示我们背景会添加 Windows Fluent 设计风格的亚克力着色
* `"acrylicOpacity"` 定义了亚克力效果的透明度

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/0B894131-5FAF-4ACE-BF12-04000C2E443F.png)

带有 PowerShell 特色蓝与亚克力透明效果的背景设置

当然，背景的设置不止步于此，我们可以直接一张图片作为 Windows Terminal 的背景，不仅可以用于装饰，还可以用于提醒我们当前所在环境。

首先我们需要进入 Windows Terminal 的素材文件夹，也就是 Windows Terminal 安装目录 `C:\Users\{用户名}\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe` 里面的 **`RoamingState` 这一文件夹**，将挑选好的「壁纸」背景放入其中，并记下其文件名。比如，这里我挑选了一张非常有 Windows 特色的壁纸（下载：[Untitled Goose Wallpaper](https://wallpaperhub.app/wallpapers/6277)），将之命名为 `goose.png`：

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/2F85E520-693D-41F5-BC84-3C9C186BCCD8.png)

Windows 特色桌面壁纸

之后，在 Windows Terminal PowerShell 的配置模块，我们加入如下的内容，依次定义：

* `"backgroundImage"`：设置背景图片为 `goose.png`，具体素材路径的语法格式为 `ms-appdata:///roaming/{图片名}`
* `"backgroundImageStretchMode"`：设置背景图片伸缩模式为「按比例放大」
* `"backgroundImageOpacity"`：设置背景图片透明度为 0.6

```
{
    "backgroundImage": "ms-appdata:///roaming/goose.png",
    "backgroundImageStretchMode": "uniformToFill",
    "backgroundImageOpacity": 0.6
}
```

  
  

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/EBA8FD50-CF98-4EE1-B7D6-40E5EB1944DD.png)

PowerShell 环境背景设置

这样，我们就得到了一个非常 Windows 风格的 PowerShell 终端环境：

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/29DBC4FC-1501-4DF1-80C3-5BA43BA7CD65.png)

Windows 极了！

当然，我们同样可以为其他环境配置相应的背景图案。为 Windows Terminal 的环境设置背景，还可以提示我们当前所处的位置，防止在生产环境做出错误的操作等。

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/EBD9A9EB-AF1D-493B-A460-0474FE160325.png)

WSL - Ubuntu 环境 / Windows 环境

#### 启动环境时自动运行命令

Windows Terminal 唤起环境时，实际上是通过执行环境入口配置里面 `commandline` 这一属性所定义的命令，来进入相应的环境。**那么，我们可以在点击 Windows Terminal 下拉菜单唤起一个环境时，执行我们自定义的一个命令。**这一命令可以是 SSH 登录远程服务器，可以是调用其他系统环境（比如 Anaconda 环境）等等。我们以 SSH 远程登录为例子，具体介绍如何利用 `commandline` 这一属性。

默认最简单的环境就是 Windows Terminal 的 cmd 环境了，其 profile 定义为：

```
{
    // Make changes here to the cmd.exe profile
    "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
    "name": "cmd",
    "commandline": "cmd.exe"
}
```

可以看到，事实上这一环境仅定义了 `"commandline": "cmd.exe"`，也就是在 Windows Terminal 唤起环境时执行 `cmd.exe` 这一命令，从而自动进入 cmd 环境。于是，我们只要添加一个执行 SSH 登录服务器的命令的环境配置，即可自动进入远程服务器环境。比如，我们登录服务器的命令是非常简单的：

```
ssh root@10.0.0.1
```

即：在 PowerShell 环境下，执行上述命令，以 root 身份登录内网 IP 为 10.0.0.12 的服务器（手动输入密码）。那么我们即可这样添加执行这一命令的 Windows Terminal 环境入口：

* 使用 [在线 UUID 生成器](https://www.uuidgenerator.net/) 生成独一无二的 UUID：

  ![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/702811E2-600D-4D56-95DB-BD323C69BA80.png)

  生成 UUID
* 在 `"profiles"` 列表中新建一个最简的环境入口配置，填写 UUID、环境名称、以及具体命令（注意这里我们需要指定用 `powershell.exe`，否则可能默认使用 cmd 环境）：

  ```
  {
    "guid": "{a060905f-d089-43d9-9422-cd748e7f0230}",
    "name": "SSH",
    "commandline": "powershell.exe ssh root@10.0.0.1"
  }
  ```
* 为了更加美观实用，我们还可以添加一个图标。我事先准备了一个 GPU 的图标并将之命名为 `gpu.png`（因为我这台内网服务器是学校训练用的 GPU 服务器），将图标同样放置在 Windows Terminal 素材文件夹 `RoamingState` 里，并向刚刚创建的环境入口配置中填入图标的定义：

  ```
  {
    "icon": "ms-appdata:///roaming/gpu.png"
  }
  ```

    
    

  ![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/A21FF8F7-4336-41E8-844D-08E5B1A9580E.png)

  自定义 profile 与对应图标

这样，我们就可以直接唤起这一命令，执行 SSH 登录，进入远程服务器环境。

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/628A5030-4E50-4921-83D1-17A97ACD5B24.gif)

直接点击标签页即可执行相应的登录命令

想要寻找更多图标的同学，可以在 [icons8](https://icons8.com/)、[iconfont](https://www.iconfont.cn/) 等网站上进行搜索，特别是 icons8 的图标，非常精致，且同一类别风格一致，96px 的尺寸也足够用于 Windows Terminal 上，推荐大家使用！

另外，如果你日常使用的环境是 WSL 环境并使用 mosh 进行 SSH 登录（因为 mosh 并不支持 Windows），你同样可以在 `commandline` 一处将命令设置为：

```
{
    "commandline": "wsl.exe mosh root@10.0.0.1"
}
```

这样依然可以正常执行相应的操作：进入 WSL 环境 » 执行 Linux 独占工具。

### 添加额外的配色主题

Windows Terminal 的色彩主题同样是 JSON 文件，我们可以在上文介绍的 `profiles.json` 文件的 `schemes` 属性处，添加自定义的色彩主题。可能是全网最丰富的终端配色方案集合：[iTerm2 Color Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)，就包含有为 Windows Terminal 提供的 200 余中色彩方案，位于 [`windowsterminal`](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/windowsterminal) 文件夹中。（主题的样式预览可以在 [iTerm2 Color Scheme 的官网](https://iterm2colorschemes.com/) 查看。）

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/E21FD22D-E12A-4053-8BF5-6A5E9EF35298.png)

iTerm2 Color Scheme 中 Windows Terminal 色彩主题

iTerm2 Color Scheme 项目中的 Windows Terminal 主题均为独立的 JSON 文件，我们挑选好想要添加的主题之后，点击打开对应的主题文件，复制整个 JSON 文件的内容，并粘贴到 Windows Terminal 的配置文件的 `schemes` 主题文件列表之中，即可使用这一色彩主题。

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/5925FDB4-0576-4468-BA04-329440E74917.png)

将色彩主题的 JSON 内容粘贴到 schemes 属性之中

之后，我们在 Windows Terminal 配置文件里各个环境入口的配置中，定义使用相应的「色彩主题」，即可让这一环境的配色方案生效：

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/737787C0-FE88-4CAF-B936-94E9312D3C90.png)

定义一个 profile 使用的配色主题

### 自定义 Windows Terminal 的快捷键

在 Windows Terminal 的配置文件末尾，我们可以在 `"keybindings": []` 里定义其快捷键绑定。默认的 Windows Terminal 快捷键实际上就非常好用，可以用来快速开启某个环境、实施分屏操作等。这里举几个比较典型的、无需设置即可使用的例子：

* `Ctrl + Shift + T` 打开新标签页
* `Ctrl + Shift + 1` 进入配置文件中定义的第一个环境（`Ctrl + Shift + 2` 进入第二个，以此类推）
* `Alt + Shift + -` 横向分屏；`Alt + Shift + +` 纵向分屏
* `Ctrl + +` 放大、`Ctrl + -` 缩小、`Ctrl + 0` 恢复默认缩放比例
* ……

我们可以在按住 `Alt` 的时候，点击 Windows Terminal 下拉菜单的「设置」，进入 Windows Terminal 自动生成的默认配置文件（不要更改这一文件，更改也不会有用的！）。在文件的最后，有 Windows Terminal 默认快捷键绑定可以参考：

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/97016FB3-6227-4023-A2CD-30854A48AAC9.png)

Windows Terminal 默认快捷键绑定

如何更快地进入工作环境
-----------

从 [Windows Terminal v0.9](https://devblogs.microsoft.com/commandline/windows-terminal-preview-v0-9-release/) 版本开始，Windows Terminal 支持了「命令行参数」。也就是说，我们现在可以用 `wt -xxx` 的命令来唤起 Windows Terminal 打开不同的环境、进入特定的目录，设置直接设置分屏、同时打开多个标签页等。

举几个比较常用的「命令行参数」的例子：

* 在当前路径下进入默认的 Windows Terminal 环境：

  ```
  wt -d .
  ```
* 使用名为 `Ubuntu` 的 WSL 环境打开当前路径：

  ```
  wt -p "Ubuntu" -d .
  ```
* 垂直分屏打开 PowerShell 与 WSL 环境：

  ```
  wt -p "Windows PowerShell" -d . ; split-pane -V -p "Ubuntu" -d .
  ```

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/847EDD4B-32F8-458E-8EC7-EC9D52293516.gif)

使用「命令行参数」唤起 Windows Terminal 的特定环境

注：完整的 Windows Terminal 命令行参数文档位于 [Using the `wt.exe` Commandline](https://github.com/microsoft/terminal/blob/master/doc/user-docs/UsingCommandlineArguments.md)

你可能也发现了，上面的命令有时候并不简单，进入一个环境可能需要重复手动输入复杂的指令。那么，如何才能更快速的唤起某个 Windows Terminal 状态呢？

我们都知道 Windows「右键菜单」的快捷之处：快速在 Windows 自带终端中打开当前目录、快速创建文件夹、快速批量压缩文件……Windows 终极效率利器 Quicker，就是利用「右键菜单」的思想，设计了「全局右键菜单」。

**关联阅读：**[Windows 平台的快捷指令：Quicker 使用详解](https://sspai.com/post/55382)

利用 Quicker，我们就可以**把 Windows Terminal 命令放进右键菜单里**。下面我以「在当前目录下打开 Windows Terminal 的默认环境」这个动作为例子，为大家介绍如何使用 Quicker 自定义打开 Windows Terminal 的方式。

实际上，从 Quicker 唤起 Windows Terminal 就是使用 Quicker 在当前文件夹下执行这一命令：

```
wt -d .
```

默认情况下，如果我们直接用 Quicker 的「执行动作」这一简单动作直接运行 `wt -d .`，由于 Quicker 尚未获取到当前命令的执行环境，因此它会按其默认环境执行这一命令，我们也就只能进入默认的 Windows 根目录下。**我们需要先获取到当前资源管理器所在路径，之后将这一路径传递给「运行或打开」，将动作的「工作路径」进行设置，才能正确执行命令。**

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/B69265AC-FEFD-41E2-A9DD-DC96B6E9DF5B.png)

使用 Quicker 自定义组合动作在当前文件夹下唤起 Windows Termina

使用这一动作，我们可以达到类似下面演示的效果：

![](.evernote-content/0DEA2D9E-271F-4733-AA8D-A5674CD6128E/869454D8-7442-4DAF-9F2F-025E2175C1B1.gif)

Quicker 动作：在当前文件夹下打开 Windows Termina

这一动作我已经发布在 Quicker 的动作库中了：[WT Here](https://getquicker.net/Sharedaction?code=4e7abb0c-f213-4ee4-39f5-08d7bfff7792)，感兴趣的同学可以前往添加下载。发布的动作中我还设置了一个 `args` 变量，方便你配置自己的命令行参数。你也可以直接根据我的思路，自行进行动作制作。我觉得使用 Quicker 进行「右键菜单」的定义，**比直接修改「注册表」来添加右键菜单的动作要方便得多，且更加安全。**

小结
--

Windows Terminal 当属 Windows 上第一个兼顾速度、界面与可定制性的终端模拟器。作为微软自家出品的 Windows 终端软件，「亲儿子」的待遇和体验就是不一般。Windows Terminal 的出现可以说是直接拯救了多年来糟糕的 Windows 命令行体验，让 Windows 在命令行环境下的操作感受能够和他 UNIX 的朋友们比一比。相信，在接下来的版本迭代中，Windows Terminal 会随着设置 UI 界面化、插件系统的加入…… 而越来越强大。希望这篇文章能够让你重新体验到 Windows 命令行环境的强大，提升在 Windows 上的工作、开发效率。感谢阅读。

> 下载少数派 [客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，了解更多 Windows 技巧 ⚙️

> 特惠、好用的硬件产品，尽在 [少数派 sspai 官方店铺](https://shop549593764.taobao.com/?spm=a230r.7195193.1997079397.2.2ddc7e0bPqKQHc)

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/59380)

[📎 在印象笔记中打开](evernote:///view/207087/s1/a015bbd9-2eee-49d4-bcd8-c9e86c464307/a015bbd9-2eee-49d4-bcd8-c9e86c464307/)