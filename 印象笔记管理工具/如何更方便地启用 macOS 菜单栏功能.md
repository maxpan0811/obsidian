# 如何更方便地启用 macOS 菜单栏功能

---

如何更方便地启用 macOS 菜单栏功能
====================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

Finder 压缩文件的快捷键是什么？Safari 固定标签页的快捷键是什么？怎样快速把 Pages 文件导出成 doc 格式？

这些功能，虽然常用，但是能快速找到它们在哪儿的人不会太多。至于使用率再低一些的功能，估计就更没多少人知道了。找不到功能的位置、记不住快捷键，不是你的错，因为**应用的功能往往都挤在 macOS 的菜单栏里**，有的干脆连快捷键也不给你（比如 Pages 的导出功能）。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/EB70ED6A-3775-4E2C-98BB-50A14276C6E8.png)

Pixelmator Pro 的菜单栏非常冗长

这种把功能一股脑往菜单栏里塞的设计，最早可以追溯到 1984 年的 System 1.0，不过那年头的应用，功能都不多，全塞进菜单栏也问题不大。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/4BCD0781-0068-4E2E-8496-180168C6B5B2.png)

System 1.0 中的菜单栏

不过到了今天，即使是最简陋的文本编辑器也有近 100 个功能选项，**显然菜单栏「摊大饼」般的呈现方式已经不符合我们的使用习惯，带来了很多问题：**

* **不好找：**像「压缩文件」这类使用频率较高的功能，每次却要去菜单里翻找，多走一步。
* **不好记：**Photoshop、Pixelmator Pro 等专业工具，菜单栏层级非常多，记都记不住某个选项在哪里。

好在我们有不少方法，**来更轻松地启用菜单栏中的功能**，而无需层层翻找、手动点击。这篇文章里，我们将从简单到高级分 3 个层次来优化 macOS 的菜单栏功能体验：

* 简单版：用系统设置给菜单选项添加快捷键
* 进阶版：用 Keyboard Maestro 制作精简版菜单栏
* 自动化：用 Keyboard Maestro 实现特殊场景下自动点击菜单选项

基础方案：通过系统设置自定义快捷键
-----------------

**给常用功能绑定一个快捷键**，是最直接的思路。这个需求不需要第三方工具就能实现。比较会折腾 Mac 的人，可能已经知道一个**通过快捷键启动菜单栏项目的技巧**。

这个原生技巧操作起来不难：

1. 在系统设置中打开「键盘 - 快捷键」，点击左栏的「应用快捷键」；  

   ![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/7F7D135E-2181-4630-9575-E88A0AE2E0B8.png)

   自定义快捷键
2. 点击下方的加号 `+` 按钮，新建一个自定义快捷键；
3. 在弹出的界面中选择菜单选项所在的**应用程序**（默认是所有应用），输入**菜单选项标题**和**想要的快捷键**，就完成设置了。注意菜单栏标题不能填错，不然快捷键不起作用。  

   ![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/44E9EEBA-8BB7-43FC-AAA5-97AF4C13EC05.png)

   设置快捷键

如上图所示，我们已经为「压缩文件（Compress）」绑定了快捷键 `⌥Option - ⌘Command - Z`。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/A04C0951-88B3-44B4-AA2A-C5353A275F03.gif)

通过快捷键快速压缩文件

**自定义快捷键可以是全局的，也可以为特定应用专门设置，避免冲突。**我的任务管理工具 TaskPaper 有一个「Jump to」功能，类似 Evernote、Slack 的全局跳转，我想把这类跳转功能的快捷键都统一成 `⌘Command - J`，于是就专门为 TaskPaper 设置了下面的快捷键。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/A92980B1-1EF7-4737-A1DC-8B0E9FA83C8A.gif)

通过快捷键实现快速跳转

如果你遇到快捷键不起作用的情况，可以试试重启应用，要是仍然不奏效，很大概率是和已有的快捷键冲突了，需要你另设一组。

不过，自定义快捷键多了，你会慢慢遇到下面的问题：

* 每次必须手工输入菜单栏项目的完整名称
* 不能临时禁用某个快捷键，只能直接删除
* 不能保存配置文件，换电脑时要重新手动设置
* ……

这些问题，我们将引入 Keyboard Maestro 来解决。

进阶方案：用 Keyboard Maestro 自定义菜单选项
-------------------------------

Keyboard Maestro 不仅可以实现系统快捷键设置的全部功能，还有更高级的玩法，能够突破快捷键的限制，比如：

* 快捷键太多记不过来？自制一个精简版菜单栏
* 不想每次手动按快捷键？可以根据触发条件自动点击菜单选项

我们先从最简单的单个快捷键设置开始。

### 简单的快捷键

总体上说，在 Keyboard Maestro 里设置一个快捷键也是分两步走。以「为 Safari 的 Pin 功能设置 `⌥Option - ⌘Command - P` 快捷键」为例：

1. 设置 Hot Key Trigger `⌥Option - ⌘Command - P`
2. 添加「Select or Show a Menu Item」步骤，选择需要的 App 和菜单栏选项

![](https://cdn.sspai.com/minja/2018-08-15-%E7%94%A8%20Keyboard%20Maestro%20%E8%AE%BE%E7%BD%AE%E5%BF%AB%E6%8D%B7%E9%94%AE.png)

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/D6B80525-44C3-4F1C-BF22-5DCD126BE9B4.gif)

开启 Safari 的 Pin 功能

用过系统自带应用快捷键后再用 Keyboard Maestro，给人的第一感觉就是「Keyboard Maestro 的设置过程简直是享受」：**不需要手动输入完整的菜单栏选项，直接点选就能选中想要的功能。**

![](https://cdn.sspai.com/minja/2018-08-15-%E7%9B%B4%E6%8E%A5%E7%82%B9%E9%80%89%E8%8F%9C%E5%8D%95%E6%A0%8F%E9%80%89%E9%A1%B9%EF%BC%8C%E6%97%A0%E9%9C%80%E6%89%8B%E6%89%93%E5%90%8D%E7%A7%B0.png)

而在使用中，Keyboard Maestro 的两个细节也让人觉得很舒服：

* 可以随时禁用和开启某个快捷键
* 可以自动备份配置文件，也能导出后和别人分享。想用上面这个 Pin 快捷键？直接下载 [这个](https://cdn.sspai.com/Pin.kmmacros.zip) 文件拖进 Keyboard Maestro 就行。

有了这些在编辑和使用中的优点，Keyboard Maestro 已经能在实现系统应用快捷键全部功能的同时，提供更人性化的体验。

### 打造一个精简版菜单栏

当你绑定的快捷键越来越多，难免遇到两个问题：

* 新快捷键很容易与现有快捷键发生冲突
* 快捷键太多，不好记

我们不妨换一个思路，不必在快捷键这条道上走到黑。下面就介绍 Keyboard Maestro 的一个特色功能：**Palette（调色盘），借助它，可以打造出一个精简版的菜单栏，里面放着最常用的功能，按数字键就可以启用，而无需记住一堆快捷键。**

我最终实现的效果是，在任意应用里按下快捷键 `⌃Control - ⌥Option - ⌘Command - P`（P 表示 Palette），都能打开对应的精简版菜单栏，接着直接按选项后面对应的数字就能启用该功能，比如在 Sketch 里打开 Palette、再按一下 `2` 就可以把图片翻转过来。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/253DAED1-8758-4918-9C6D-E3F5AB7827F3.gif)

快速启用翻转功能

制作这样的 Palette 的步骤也不复杂：

1. 在 Keyboard Maestro 里新建一个 Group；
2. 如图，为这个 Group 设置好应用、窗口和快捷键；  

   ![](https://cdn.sspai.com/minja/2018-08-15-%E4%B8%BA%20Sketch%20%E5%88%B6%E4%BD%9C%20Palette.png)
3. 做 Group 中照上一节的方法为菜单栏选项设置 Hot Key Tigger，但是不用设置像 `⌥Option - ⌘Command - P` 这样长长一串的快捷键，直接设置数字快捷键即可。

事实上，Palette 也用到了快捷键，不过**我们能够从成堆的快捷键里解放出来**， 只记住一个开启 Palette 的快捷键，剩下的功能，直接按数字键就能迅速启用。

对于 Office 套件、Photoshop、Pixelmator Pro 等菜单栏繁复的专业工具来说，Palette 是一个简化菜单栏的好办法。在《[3 种方法调教工具栏，让最常用的 Office 功能触手可及](https://sspai.com/post/45560)》中，Adventure 就展示了他用 Keyboard Maestro 自制的精简版 Office 菜单栏，把常用功能都集中在了一起。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/DFFCE305-239B-4FB0-997A-D56FBAA11E80.png)

用 Palette 自制 Office 菜单栏 图 / Adventure

高级方案：用 Keyboard Maestro 自动点击菜单栏
-------------------------------

有些情况下，即使有快捷键我们都不想按，更自然的解决方案是**让 Keyboard Maestro 根据触发条件自动帮我们点击菜单栏**。比如：

* 开启 Chrome，自动进入隐身模式；
* 离开 IINA 视频播放界面，自动开启画中画模式；
* 打开 GitHub，自动点击「Pull」同步数据；
* ……

我们就取前两个场景，来看看 Keyboard Maestro 是怎样实现的。

### 自动点击：自动进入 Chrome 隐身模式

Safari 是我的主力浏览器，但是我也会用 Chrome 来应对一些 Safari 看不了的网站，比如部分学校的官网、仍未启用 Flash 的古董级资源站点。我一般不希望在 Chrome 上留下这些网站的浏览痕迹，所以每次都会用隐身模式来浏览网页。

Windows 上的 Chrome 可以用启动选项让 Chrome 默认以隐身模式打开，但是 macOS 版则需要通过 shell 脚本来启动，不是很方便。其实，可以用 Keyboard Maestro 让 Mac 版的 Chrome **自动进入隐身模式**。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/2FAE597A-CC41-4B6D-A279-E56BE2D5022A.gif)

自动进入 Chrome 隐身模式

[> 动作下载](https://cdn.sspai.com/%E8%BF%9B%E5%85%A5%20Chrome%20%E9%9A%90%E8%BA%AB%E6%A8%A1%E5%BC%8F.kmmacros.zip)

这个 Macro 主要有三步：

1. 触发条件：Chrome 启动（This application, Google Chrome, Launches）；
2. 第 1 个动作：暂停 1 秒，等 Chrome 完全启动，不然下一步会失败；
3. 第 2 个动作：点击 Chrome 菜单栏中的「File, New Incognito Window」选项。

![](https://cdn.sspai.com/minja/2018-08-15-%E8%87%AA%E5%8A%A8%E8%BF%9B%E5%85%A5%20Chrome%20%E9%9A%90%E8%BA%AB%E6%A8%A1%E5%BC%8F%E7%9A%84%20Marco.png)

当然，你也可以把这个自动进入隐身模式的技巧用到 Safari 上。

在应用启动等时刻自动启用菜单选项，可以帮我们节省很多力气，除了前文介绍过的 GitHub 客户端自动 Pull 技巧，下面这些用法也值得参考：

* 打开 Mac App Store 后，自动跳到应用升级界面；
* 打开 Sketch 后，自动创建一个新的空白画布；
* 连上自家 Wi-Fi 时，就把网络位置切换到「家」；
* ……

### 后台自动点击：IINA 自动开关画中画

IINA 是我在 Mac 上的主力视频播放器，很重要一个原因就是**它支持用画中画播放几乎任意格式的视频**，追剧遇到一个梗、看电影碰到不懂的概念想 Google 一下也不用错过视频，直接开个小窗口继续播放就行。

开关画中画的次数多了，我开始觉得这样手动操作并不自然，于是通过 Keyboard Maestro 来实现**离开 IINA 播放界面自动开启画中画、回到播放界面自动退出画中画**的效果。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/B955F4D2-AB3C-4281-98EA-542F84DB678D.gif)

自动开关画中画

[> 动作下载](https://cdn.sspai.com/Video%20Macros.kmmacros.zip)

这个效果要通过两个 Macro 来实现，实际上就是根据 IINA 窗口是否处于激活状态来点击菜单栏中进入 / 退出画中画的选项。

![](.evernote-content/F5C6720C-5435-494D-9837-F9E71052D06B/A073CA65-8F2F-4B53-9AB3-B3001518A7E4.png)

控制 IINA 开关画中画

两个 Macro 的触发条件分别是：

* 进入画中画的 Macro：IINA，Deactivates
* 退出画中画的 Macro：IINA，Activates

所要触发的动作都是模拟快捷键 `⌃Control - ⌘Command - P`，这是 IINA 自带的快捷键，用于触发菜单栏中进出画中画的选项。需要注意的是，**要在 Type Keystroke 步骤右上角的设置中选择将快捷键发送（Send To）给 IINA**，才能准确控制 IINA 的菜单栏选项，而不会在离开 IINA 窗口时影响到其他应用。

![](https://cdn.sspai.com/minja/2018-08-15-Send%20To%20IINA.png)

结语
--

面对 macOS 上应用菜单栏太繁复的问题，我们从系统自动的功能出发，先尝试用快捷键来启动最常用的功能；但原生应用快捷键的体验还不够完善，何况绑了过多快捷键反而会记不住。所以我们又引入了 Keyboard Maestro 来简化菜单栏。最后，我们还借助 Keyboard Maestro 的自动化操作，在特定场景下自动帮我们点击菜单栏选项。

这种「**先试试系统原生功能，再引入第三方工具，最后看看有没有自动化解决方案**」的思路，在许多场景下都很有用。优化 macOS 菜单栏使用体验只是一个例子，大家可以在别的地方多多尝试这类由简入繁的解决思路。

[#Keyboard Maestro](https://sspai.com/tag/Keyboard%20Maestro)[#macOS](https://sspai.com/tag/macOS)

---

[🌐 原始链接](https://sspai.com/post/46169)

[📎 在印象笔记中打开](evernote:///view/207087/s1/ba69c783-a337-4d34-a29f-f9e461f5d6d8/ba69c783-a337-4d34-a29f-f9e461f5d6d8/)