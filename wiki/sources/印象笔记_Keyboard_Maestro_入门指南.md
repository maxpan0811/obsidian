---
title: "Keyboard Maestro 入门指南"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Keyboard Maestro 入门指南.md
tags: [印象笔记]
---

# Keyboard Maestro 入门指南

# Keyboard Maestro 入门指南 --- ![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/117CC453-124B

---

# Keyboard Maestro 入门指南

---

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/117CC453-124B-4BA5-8278-A82249B816C6.jpg)

[Jailbreakhum](http://matrix.sspai.com/user/681230) 在 [Workflow 教程 (一)](http://sspai.com/27733) 里提到：

> 想实现某个结果都有一定的流程，很多时候这些流程里的某些步骤是**重复**的。重复就会有两个弊端：第一是浪费时间，试想如果你能把某个常用的流程缩短了几步，那么每一次用这个流程你都省了一点儿时间，长久累积起来你能节省的时间就很可观了；第二个弊端是增加干扰，从锁屏就能看到的通知开始，智能设备里一切元素都是为了吸引你的注意力，步骤越多你受到的干扰就越多被打断的可能就越高，很多时候你想到一件事需要用手机完成，但是你拿出手机划了一会就忘了你当初为什么要拿出手机了。

这是之于智能手机，之于计算机同理。对大部分厌倦了低效、繁琐、重复操作的 Mac 用户，[Keyboard Maestro](http://sspai.com/tag/Keyboard%20Maestro) 和 [BetterTouchTool](http://sspai.com/tag/BetterTouchTool)、[Alfred](http://sspai.com/tag/Alfred) 都同列于必须尝试的软件，他甚至是很多 PC 用户切换到 Mac 的源动力。Keyboard Maestro 能将键盘的功能发挥到极致，同时还能代替很多软件，能够限制他用例的，只有你的想象力。

什么是 Keyboard Maestro
--------------------

> *Keyboard Maestro* is the leading software for Mac OS X automation. It will increase business productivity by using macros(or short cuts) with simple keystrokes.

这是 [官网](https://www.keyboardmaestro.com/main/) 上的介绍，简单来说，Keyboard Maestro 是通过一系列条件来触发一个个 Macro 藉此实现操作自动化的软件。

至于什么是 Marco，[维基百科](https://zh.wikipedia.org/zh-hans/%E5%B7%A8%E9%9B%86) 的解释是：

> **宏**（Macro，港澳台作**巨集**），是一种批量处理的称谓。
>
> 计算机科学里的宏是一种抽象（Abstraction），它根据一系列预定义的规则替换一定的文本模式。绝大多数情况下，**「宏」这个词的使用暗示着将小命令或动作转化为一系列指令。**

「宏」这个中文翻译其实并不能非常好的表明 Macro 的英文意思，所以在下文我会直接使用 Macro 这个词。

Macro 的触发条件可以是：按下的键盘按键、连接到了某个特定 SSID Wi-Fi、某个 App 被激活到了前台、剪贴板内容发生了某种变化……

而 Macro 可以执行的动作就更多了：控制浏览器、控制鼠标移动或点击、控制窗口大小、执行一段 AppleScript 脚本、进入特定 Finder 目录……

初探 Keyboard Maestro
-------------------

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/1CEDB036-C6C6-4AA4-A7C0-31CD8B076751.jpg)

Keyboard Maestro 程序体分为两部分，一部分是常驻 Menu Bar 的`Keyboard Maestro Engine` 一部分是运行时会在 Dock 上显示的 `Keyboard Maestro Editor`编辑器。其中，Keyboard Maestro Engine 除了显示一些状态信息，可以把一些不常用的 Macro 放在这里，进入 Debugging 捉虫（调试）模式的入口也在这里。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/116653CF-1011-4245-9980-AA56162DBBB6.jpg)

**创建第一个 Macro：**

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/D1A227D0-4216-410A-9146-9F318AAA85AC.jpg)

这里我们创建一个用于**将剪贴板内的文本粘贴为纯文本**的 Macro，虽然有很多 App 可以做到这一点，正如前文所说，Keyboard Maestro 可以替代很多 app，同时实现这个功能也非常简单。

创建后，首先给他起一个名字，这里名为「粘贴为纯文本」，再为他选择一个触发器（Trigger），即运行条件。macOS 默认粘贴动作快捷键为`⌘ + V`，在此基础上再另加一个修饰键`⌃`作为触发器，这是一个比较符合直觉的设定。选择触发器为`Hot Key Trigger`，快捷键触发器，并添加 `⌃ ⌘ V`。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/1B30DC24-3213-4C58-98E6-953FFD144313.jpg)

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/244D9548-2B95-4620-A924-621ED24153FB.jpg)

使用 Keyboard Maestro 内建的剪贴板相关的动作：`Fliter Clipboard`来去除掉剪贴板内容的样式使其变为纯文本。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/0E494095-82FA-4C11-9D4B-0B061F2C87C2.jpg)

通过第一个动作将剪贴板内容处理为纯文本后，再通过第二个动作`Type the Keystoke`使 Keyboard Maestro 模拟按下了`⌘ + V` ，将纯文本粘贴 App 内。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/A4300FF4-504A-4CF2-B448-FF0D1B78CECE.jpg)

完成了！现在到浏览器里复制一段一段有格式的文字，然后到 Word 里按下 `⌃ ⌘ V`看结果是不是纯文本？

很简单对吧，如果你有过使用 macOS 的 Automator 或者 iOS 上的 Workflow 经验的话，应该很容易就能明白 Keyboard Maestro 的基本逻辑。

如何像 Maestro 一样行事
----------------

Mac App Store 中充满了三万多个用于各式各样专有用途的 App，但是 Keyboard Maestro 却不是这种思维模式下的产物[1](http://sspai.com/36442#fn1)，取代的是，Keyboard Maestro 提供了极尽奢华的工具种类，甚至令人眼花缭乱、无从入手。

然而之所以会认为无从下手常常是因为梳理不出一个具体的、会经常重复的用例。

所以，我们要问自己：我在 Mac 上经常重复的事情是什么？有没有办法把它分解成一步步动作？这些动作有没有可能通过 Keyboard Maestro 来实现？

Keyboard Maestro 工具库
--------------------

下面来介绍一下 Keyboard Maestro 引以为傲的「弹药库」，如果你是初学者，现在只简单浏览一下有一个总体印象就可以。这部分更多是适合在你有一定基础以后，再回过头仔细看一遍。

### 触发器库

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/B9ED3A8C-5F0C-44C3-9B92-1302B27649E9.jpg)

**Hot Key Trigger**：我们刚刚已经使用过他了，他最容易理解，也是最经常使用的触发器——在按下特定快捷键组合时，运行 Action。

**Macro Palatte Trigger**：会在屏幕上显示一个「宏调色板触发器」，一个浮动的窗口。这个窗口只有在 Macro 可以执行的时候才会显示，然后用鼠标点击其中的 Macro 来触发。

**Status Menu Trigger**：在常驻 Menu Bar 的 Keyboard Maestro Engine 下拉菜单中添加一个项目。

**Typed String Trigger**：当某些字符被敲下时触发，与 HotKeyTrigger 不同的是，Typed String 敲下的字符不需要包含修饰键，同时这些按键不需要被同时按下。可以设置具体大小写敏感或者匹配某个正则表达式。（这个触发器在替代 [TextExpander](http://sspai.com/tag/TextExpander) 时经常使用）

**Application Trigger**：当某个应用程序处于某个状态时，触发。像 「Finder 从后台被激活到前台时（关闭其他窗口）」，「Chrome 被 `⌘ Q` 退出时（询问是否启动 Safari）」。

**Clipboard Trigger**：系统剪贴板内容发生变化时，触发。

**Engine Launch Trigger**：在 Keyboard Maestro Engine 启动时触发，一般情况来说，就是在 macOS 启动时，除非有你什么特殊目的重启了 Keyboard Maestro Engine。

**Focussed Window Trigger**： 焦点窗口改变时、标题改变时、焦点窗口的标题改变时、窗口框架改变时，触发。

**Folder Trigger**：这个触发器会关注某个特定文件夹，当这个文件夹添加了新文件，移除了文件，添加或移除了文件时，触发。（这个触发器在替代 [Hazel](http://sspai.com/tag/Hazel) 时常常用到）

**Login Trigger**：当 Keyboard Maestro Engine 随系统启动时，登陆到当前用户时，触发。大部分时候与 Engine Launch Trigger 没什么区别。

**MIDI Trigger**：当一个 MIDI 设备上的某个按键（note）被按下时触发。

**Mounted Volume Trigger**：任何设备或特定设备装载或弹出时，触发。

**Periodic Trigger**：用户登陆后，在一定时间间隔下，触发。这个触发器很适合用来执行一些周期性的（维护）工作，或追踪某些事件的进展。

**Public Web Trigger**：Keyboard Maestro 内建的 Web Server 激活，当有人连接到 Keyboard Maestro Web Server 时，触发。这个触发器需要一些更高阶的技巧，可以用于想从别处维护自己电脑时。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/59A8CD4E-67AF-42A4-8483-CFC5B38CD37B.jpg)

**Sleep Trigger**：当 Mac 睡眠时触发，这个触发器能够将 Mac 睡眠推迟最长大概 30s 用于执行相应的 Action。

**Time Trigger**：到达某一时间点时，触发。

**USB Devices Key Trigger**：某个 USB 设备上的按键被按下时，触发。如果你在用像 Razer Naga Chroma 这种按键特别多的设备，你会很喜欢这个触发器。

**USB Devices Trigger**：某个 USB 设备或拔出电脑时，触发。如果你是插画师，可以设定：「插入绘图板时，启动 Photoshop」这种 Macro。

**System Wake Trigger**：类似 Sleep Trigger，在 Mac 唤醒时触发。

**Wireless Network Trigger** ：连接到或离开特定网络时，触发。可以用于：插入以太网时关闭 WiFi；连接到公司 WiFi 时，取消 Surge 的 Proxy 设定。

### Action 库

了解了触发条件以后，再来认识一下 Macro 可以做什么。 Keyboard Maestro 提供了太多的 Action（[这里](https://wiki.keyboardmaestro.com/Actions)有官方的 Action Wiki），但是大致可以分为以下几类：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/3EDA5F9F-CB14-4D2E-A53A-3B2C93736593.jpg)

**Application Control**：这些动作可以用于激活、退出、隐藏、显示，上一个、下一个或具体某一个 App。

**Clipboard**：这些动作可以用于操纵系统剪贴板，进行像添加、删除、匹配格式、去除格式、过滤字符等。

**Control Flow**：提供了像 IF 语句、循环语句这种基本控制动作。这是高级 Macro 的立足之本。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/2150EE9E-567B-4665-8E6C-612E658D6CA3.jpg)

**Debugger**：在一个 Macro 执行的不尽人意时，这些动作能帮助你排错。

**Execute**：可以执行 JavaScript, Apple Script, Shell Script, Automator Workflow 脚本。

**File**：可以对文件或文件夹进行在 Finder 中显示、移动、重命名、删除、制作副本等动作。

**Google Chrome Control**：Chrome 这个舶来品在 macOS 生态下不是显的不是很温驯。这些动作可以用于控制 Chrome。

**Image**：可以捕获屏幕上的图像，或者用「计算机图形学」对图片进行旋转、镜像翻转、剪裁甚至更高阶的动作。

**Interface Control**：介面控制。这组动作可以对 UI 进行控制：模拟敲击按键、移动窗口、模拟点击鼠标、选择菜单栏上的某项 Item。

**iTunes Control**：播放，暂停、快进、回退等。

**Keyboard Maestro**：这是 meta action，用于操纵 Keyboard Maestro 自身。像在 Macro 中结合已经存在的其他 Macro，对某项 Action 添加注释，激活、取消某个 Macro 组等。

**Mail Control**：用来控制 macOS 内建的 Mail.app。

**Notifications**：给 Macro 的执行情况添加一个反馈，可以是一个通知，也可以一声「嘟嘟」、一段特定的音效，还可以是一个弹出窗口警告⚠️。

**Open**：打开特定的 [1Password](http://sspai.com/tag/1Password) 项目书签，一个文件或 App，一段 URL，或者在 Finder 中查找特定文件。

**Quicktime Player Control**：类似 iTunes Control，用来控制 QuickTime.app 。

**Safari Control**：类似 Google Chrome Control ，用来控制 Safari。

**Switchers**：Keyboard Maestro 内建了窗口管理器（⌘ ⇥），应用程序切换器，剪贴板历史记录器。这个动作组可以激活他们。（尽管有，但是我觉得并不好用，不美观另说，功能也非常初级）

**System Control**：这组动作用于控制电脑进入睡眠，注销或控制音量，亮度。

**Text** ：这组动作用于操作文本，像排序，应用特定格式等。

**Variables** 变量：这组动作用于使 Keyboard Maestro 储存或进行其他操作一个变量。

**Web**：打开一个 URL 或搜索特定内容。

### 通过「录制」制作 Macro

了解完了触发器和动作，感觉怎样？脑子乱也没关系，实际上你不需要记清 Keyboard Maestro 支持的每一个动作，制作的时候能想起来关键词去库里找就好。

就是考虑到了这种不知道该用哪个动作的情况，Keyboard Maestro 可以通过 recording 来记录你的动作，并从而制作 Macro：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/DD684D84-5907-4685-BA0B-86A0792765E5.jpg)

在右下方，有「记录」按钮，他会记录下此期间你的所有操作。

**但是通过这个方法制作的 Macro 应用环境比较窄，他要求执行时：系统的环境**（激活的 App、窗口位置、窗口中的内容等）**与录制时完全相同，否则执行结果就会与预期不符。**

几个用例
----

了解完库之后，现在通过几个例子来具体说明 Keyboard Maestro 是怎样工作的。

### 简单动作

#### 快速启动 App 和访问特定 Finder 目录

对每个人来说，App 基本上可以分为几种，下面以我的情况为例：

| 常驻后台的 App | 经常使用的 App | 偶尔打开的 App |

| :--------------------------------------: | :--------------------------------------: | :-------: |

| Chrome, Telegram, Sublime, iTerm, Finder | Tweetbot, Reeder, Quiver, Spotify, Evernote | 其他 App |

**对于常驻后台的 App：**

因为他们常驻后台，可以通过在 Dock 上固定位置通过光标切换，也可以通过 `⌘ ⇥`来切换。但是无论是点 Dock 还是按`⌘ ⇥`，都不够直觉，每次操作时候都需要眼睛辅助来定位，无法形成[肌肉记忆](http://sspai.com/34961)，可以通过 Keyboard Maestro 设定一个 `⌥ + 字母` 快捷键，精准定位到每个 App（这里替代了 [Manico](http://sspai.com/tag/Manico) 和 [Snap](https://itunes.apple.com/cn/app/snap/id418073146?l=en&mt=12&uo=4&at=10lJSw) 的功能），使用习惯后，快、准且不打断思路。

以 Sublime Text 为例，添加新 Macro 后，设定触发器 `Hot Key Trigger`，添加 Action `Activate a Specific Application` 下方选择 Sublime。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/04E77BB2-4E3D-456A-803D-09C6256C3E40.jpg)

**对于经常使用的 App：**

由于第二部分 App 是常用但不会常驻后台，我将其设定成了统一的快捷键 `⌘ ⌥ ⇧ ⌃ + L` （取 Launch 首字母）。添加一个新的 Macro Group，取名为「Launch Applications」，添加 Hotkey Trigger。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/FBC9E3C9-CAFC-4108-B290-B126761AEB50.jpg)

然后逐一添加类似第一类 App 的 Action，并且每个 App 可设定不同的字母对应。

之所以添加了`⌘ ⌥ ⇧ ⌃ + L` 来二次归类而不是统一都添加到 `⌥ + 字母`，是因为值得设定快捷键的 App 和动作实在是太多了，而键盘上的按键又远远不够，即使引入了`Hyper`键[2](http://sspai.com/36442#fn2)，也需要十分克制的分配按键，这同时有助于自己记忆。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/69F364EB-498A-4CAC-90A7-BA5B2272E914.gif)

**对其他 App：**直接用 Alfred 或 Spotlight 就好……

**打开特定的 Finder 目录：**

为了介绍更多 Keyboard Maestro 功能，这里使用另一种方法：Keyboard Maestro 的「Conflict Palette」是「冲突调色板」，他会在设定的快捷键有冲突时弹出。

新建一个名为「Finder」的 Macro Group，新建 Macro，设定 HotKey Trigger `⌘ ⌥ ⇧ ⌃ + G` （取义 Goto），添加 Action `Open a File , Folder or Application` Open 后填写 `/Users/你的用户名/Downloads` ，此时按下`⌘ ⌥ ⇧ ⌃ + G` 就打开了 Downloads 文件夹。

继续添加 Documents、Trash 等其他你常用的文件夹到该 Macro Group。

Ps. 如果你找不到 Trash 的路径的话，可以将 Action 改为`Execute Apple Script` 然后填入下面的 Apple Script：

```
apple script
tell application "Finder"
    open trash
    activate
end tell
```

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/46023445-0828-42CC-9587-B06BCF69A4D8.jpg)

因为都设定成了同一个 HotKey，在按下 `⌘ ⌥ ⇧ ⌃ + G` 时，Keyboard Maestro 就会调用「Conflict Palette」来询问具体是想打开哪个文件夹。

Conflict Palette 的样式可以在 `⌘ + ,` 内设置：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/2DF7423A-72FD-44C1-B3DF-45AFCF44A72A.jpg)![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/2470BE57-1284-4C56-966E-7CD7020A1C1F.gif)

#### 激活 OmniFocus 或 2Do 的同时执行同步

[OmniFocus](http://sspai.com/tag/OmniFocus) 和 [2Do](http://sspai.com/tag/2Do) 都是非常棒的 GTD 软件，但是他们默认仅仅会在软件启动时执行一次同步动作，有时在电脑上修改完成要出门时希望立即把任务同步到云端，可以通过 Keyboard Maestro 来使得每次打开 OmniFocus 和 2Do 时都进行同步。

有了制作快速启动 App 的 Macro，对 2Do 只需在此基础上添加一个随后动作：模拟按下 `⌘ S`，这是 2Do 的默认同步快捷键。这样，每次启动 2Do 时都会执行一次同步操作，而不是再去点那个小小的 Sync ♽ 图标了。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/B26AE40B-82B9-40A0-8B46-80369E10F05F.jpg)

之所以我还添加了模拟 `⌘ 0` ，是因为我比较喜欢以收件箱为主要入口来管理任务。

#### Command Q 防误触

对于一些 App 来说，按下 `⌘ Q` 会立即退出，不会有任何提示和做保存当前状态的工作（Duh，大部分是 Apple 自家的 App），有时候也可能只是想按 `⌘ W` 却误点到了 Q，对于这种情况，可以使用 Keyboard Maestro 使得在容易犯错的 App 内按下 `⌘ Q` 时，弹出一个提示。

创建一个新的 Macro，名字为「⌘ Q 拦截器」，添加 `IF` 中的 `Application Condition`，在特定 App 中，先弹出 Alert 警告窗口，询问是否退出，在其他 App 中，直接执行 `⌘ Q`。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/A0D12BF8-1B0B-45C1-BE7B-352388295200.jpg)

现在再在这几个 App 中误触，就会有提示了。

（注：灵感来自 [MacDrifter](http://www.macdrifter.com/2011/05/keyboard-maestro-and-the-dreaded-cmd-q.html)）

#### Duplicate（复制）当前行

在写代码和写文章时，经常需要把当前行复制一份，保留内容的同时进行一定的修改。Keyboard Maestro 没有 action 可以直接完成这个动作，但是会想一下我们平时进行这个操作时候的动作：

* 点击三下鼠标选中当前行
* `⌘ C` 复制
* 点击另一行
* `⌘ V` 粘贴

如何用键盘完成这个动作呢？抽象一下可以概括成：

* `⌘ ←` 移动到行首
* `⇧↓` 选中当前行
* `⌘ C`复制
* `↑`回到之前行的上一行
* `↓`回到之前行的行首
* `⌘ V`粘贴

制作成 Macro：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/A045546C-E5E3-4992-9892-9525504AC534.jpg)![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/39944E6C-E91D-4A23-94A9-6000CF8760F9.gif)

### 进阶动作

#### 控制 PopClip

[PopClip](http://sspai.com/tag/popclip) 是一个非常棒的 macOS 软件，他把 iOS 上复制粘贴样式带到了 Mac 同时还提供了强大的扩展能力。[这里](http://sspai.com/25483)有一篇他的介绍文章。

但是不知道是 PopClip 本身的问题，还是和我的其他剪贴板控制软件有冲突，日常使用中经常遇到无法唤出 PopClip 气泡的情况，有时还会导致我使用 `⌘ C` 复制失败；另外在使用键盘选择文字的时候， PopClip 是肯定不会被唤出的。可以使用 Keyboard Maestro 解决这个问题，同时不丧任何功能。

我的用法是将 PopClip 本身置于未激活状态：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/EBBC3C04-7D8B-4F44-AAAF-ABAD890EA2F9.jpg)

然后通过一小段 Apple Script：

```
tell application "PopClip" to appear
```

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/DF0CD57A-A729-4D6A-9DD2-12362EB428E4.jpg)

这样在 PopClip 就会「听话」的在任何我真正需要他的才会弹出。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/219023BF-B5DC-40EE-BC2E-4229DB4EE96C.gif)

#### 填充密码

在 macOS 使用时总有一些密码是要反复输入的：1Password 主密码，Apple ID 密码，Root Grant 密码。一遍遍的反复输入他们一点也不酷，可以通过 Keyboard Maestro 来快速输入。

设定一个快捷键：`⌃ ⌥ ⇧ ⌘ 1`，添加动作：`Insert text by typing`，通过打字来插入文字，填入 1Password 主密码，然后插入动作：`Simulate Keystore`，模拟按下了`↩︎`

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/5A27ACC8-CE29-46D0-83FE-224D502491CB.jpg)![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/2B176824-9C74-4A9E-9535-37AAC9BDB034.gif)

效果还可以 huh？但是不太安全，尽管触发的按键已经很复杂了，但是有人按到时候还是会直接暴露密码。

添加一个 `IF`，添加一个 `new condition`，选择 `Found Image Condition`，将 1Password 主程序和 1Password Mini 在锁定状态下的截图添加进来，捎捎向右拨动降低一点阈值，**这样更改后该 Macro 仅仅会在 1Password 锁定时执行**。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/17E55383-470A-4530-A6A2-DCBE429CA3B7.jpg)

但是，密码还是明文的！

想到了 Keychain Access 这个 macOS 内建的密码管理工具，将密码存在 Keychain 中就避免了明文存储，高兴的是 Keyboard Maestro 内建了能与 Keychain Access 互动的动作。

要在 Keyboard Maestro 中读取，首先在 Keychain 中建立新项目：`⌘ + N`。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/8B15B8D2-0E74-40C2-A865-B66A647BE255.jpg)

`Keychain Item Name`：是一会你将放到 Keyboard Maestro 的 item 名。

`Account Name`：是这个 item 的用户名，可以随意输入，但是如果不了解其机制的话，建议保持和你电脑的用户名相同。

**注意：新建的这个项目一定要放到 Login 中。**

然后回头修改 Macro，添加 Action `Set Keychain Password to Varaible`。将上一部中填入的内如依次填入：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/039F1579-D256-45FD-AE6F-80210AED9F1C.jpg)

这样一来，这个密码对大部分「muggle」😈 基本上是不可知的了，但是所做的这一切都是基于一个假设：**你是信任 Keyboard Maestro 开发者的，信任 Keyboard Maestro 得到 KeyChain 权限后不会「作恶」**，在相对的便捷和绝对的安全上，还是要做出自己的取舍。

Apple ID 密码和 macOS Root 密码可酌情做同样处理。

（注：此 Macro 参考了 Sayzlim 的 [这篇](https://sayzlim.net/secure-password-keyboard-maestro/) 文章和 Rico Yang 的 [这条](https://twitter.com/yxjxx/status/790930312717008900) Tweet）

#### 制作一个抬头信息窗

制作一个弹出的窗口，显示当前月历、时间、电池等信息，效果是这样：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/928CB1DC-3D3C-4485-B688-65D42DA61999.jpg)

首先在 [这里](http://mattgemmell.com/files/keyboard-maestro/heads-up-info-display-macro.zip) 下载这个 Macro。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/A0CD998B-5950-4837-AC34-C81D9E5FBFE5.jpg)

得到如图几个文件，双击 `Show heads-up info display.kmmacros` 导入到 Keyboard Maestro，其余的文件可以放到一个你比较习惯的位置，但是其中`battery-icons-svg`文件夹和 `battery.rb` 一定要放在同一路径下，三个「calendar」文件也要在同一路径下。

如果你的电脑没有 Ruby 环境的话，需要先安装 Ruby：

通过 Spotlight 搜索打开 `Terminal`, 复制粘贴进如下代码：

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

运行结束后，再执行：

```
brew install ruby
```

即可成功安装 Ruby。

然后将图示中的位置改为你存放这几个文件的位置。如果你不知道存放文件的路径是什么的话，将文件夹拖动到 Terminal 中就能得到。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/55021687-A6A1-454F-8CCD-8FAA51043F98.jpg)

改好后按下预设的快捷键`⌥ ⌃ -`，就会有一个简单的信息窗弹出来了。

通过这个 Macro 展示了 Keyboard Maestro 和 web 技术交互的能力。

（注：该 Macro 参考了 [这篇](http://mattgemmell.com/keyboard-maestro-macros/) 文章）

#### 取代 TextExpander

[TextExpander](http://sspai.com/tag/TextExpander) 在升级到版本 6 以后，收费方式从一次买断转变成了订阅制：个人用户年付 40 美元，团队用户年付 95 美元，价格大幅上升的同时功能上却并没有实质提升，有充足的理由使用 Keyboard Maestro 来代替他。

以把剪贴板中的 URL 转换成 MarkDown 格式并插入为例：

可以使用 `Typed String Trigger`，当按下预设的关键字：`[][]`时，就会自动扩展并将剪贴板粘贴内容和光标都放到对应的位置。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/F9697FE0-8AE8-4D15-B48C-9B0D64803DB1.jpg)![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/24467538-F84B-406C-9DE9-6F4FBDF0F188.gif)

对于一些稍复杂，需要在不同位置添加不同字符串的片段，可以通过添加变量和 `Prompt for user input` 动作解决，以制作快捷回复反馈邮件的片段为例：

首先使用 `Set Variabe to Text` 将需要用到的不同字符串分别设置成不同的变量，然后使用`Prompt for user input` 弹出对话框询问具体内容，最后把光标置于正文末尾以便于对不同的上下文添加不同的内容：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/F84AA6AE-A155-49E3-B997-E4A7DE9CC7B7.jpg)![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/AE8CEC03-3B5D-4CDE-A02C-EDFEA0CFA92E.gif)

在 `Prompt for user input` 后还可以接 `IF` 判断输入的内容，从而在下文粘贴不同的模板，这里不做展开。

一些 Tips
-------

### 查看节省的时间

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/673ED762-8CB9-4550-89FF-95766364F817.jpg)

在 Keyboard Maestro 编辑器的 About 项目下，可以看到 Keyboard Maestro 目前为止总共帮你节省的时间，其实节省的时间是小数目，避免的精力分散才是大数目。

### 保留一个方法来停止所有的 Macro

在编辑新的 Macro 或运行游戏时，设定一个全局快捷键来临时停止所有的 Macro 可以控制变量，避免不必要的干扰。

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/FC1A5D82-F2C6-4AF0-8C02-05F39E23C646.jpg)

### 通过 Alfred 或 LaunchBar 来启动 Macro

并不是所有的 Macro 都需要设定一个触发器，有时候可以把他放在 MenuBar 中的 Keyboard Maestro Engine 中来启动，或者干脆只通过 [Alfred](http://sspai.com/tag/Alfred) 或 [LaunchBar](http://sspai.com/tag/LaunchBar) 来启动。

如果你没有使用者两款启动器的话，可以通过这种方法来达到差不多的效果：

![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/CE4581E4-1865-49FE-B7EF-FBCA4A1409AC.jpg)

对于 Alfred，可以使用 [这个](https://github.com/iansinnott/alfred-maestro) 或 [这个](https://github.com/zhaocai/alfred2-keylue-workflow) Workflow 来启动 Macro；对于 LaunchBar，可以使用 [这个](https://github.com/mlinzner/LaunchBarActions/tree/master/actions/Keyboard%20Maestro) 方法。

### 善用通知

对于一些执行效果不明显的 Macro，像我有一个 Macro 是在启动 Safari 时，自动恢复上次关闭时的所有页面。在 action 的最后一步添加一个通知来指示 Macro 是否成功运行会很有帮助。

### 使用 Debug模式

Macro 执行结果不理想时，要利用好 Debugger，他会指示每一步的运行情况。同时，要会使用 `Pause` 暂停Action，很多时候 Macro 卡在了某一步可能是执行太快，添加一个微不足道的暂停会有奇效。

### 一个 Macro 只产生一个影响

可能你能够制作出很多很 Cool，在一个 Macro 完成很多事情。但是这不是好的 Macro 设计，不但混乱，而且不利于将来的管理。

拓展阅读
----

* [官方 WiKi](https://wiki.keyboardmaestro.com/User_Manual) 和 [官方文档](https://wiki.keyboardmaestro.com/doku.php) 永远是最好的资料。同时 [官方论坛](https://forum.keyboardmaestro.com) 里有很多有价值的讨论。
* [Ez Buttons](https://www.youtube.com/channel/UCIT95Ur12P5toN4FuYxVwLQ/videos) 做了一系列很不错的 Keyboard Maestro 视频教程。
* [Rocketink](https://www.google.com/search?sitesearch=http://rocketink.net&q=Keyboard+Maestro&sa=s) 有很多文章说明了 Keyboard Maestro 本身或者和其他 App 的结合。
* 一篇比较旧的 [文章](http://flipmartin.net/software/tips-and-tricks-for-keyboard-maestro)，讲述了一些进阶技巧。

尾声
--

Keyboard Maestro 是 macOS 上非常卓越的自动化 App，只要你使用得当可以极大的提升 Mac 使用效率。结合以上几个例子可以看出，Keyboard Maestro 只是一个平台，更高级的应用是少不了 Apple Script、Shell Script 加持的，学习并了解相关知识能极大的提升 Keyboard Maestro 应用范围。

祝你能够做出适合你自己的 Macro！

如果有什么反馈可以来 [Twitter](https://twitter.com/gongziheng1995) 或 [Telegram](https://telegram.me/OscarGong) 联系我。

1. 苹果的「自动化技术产品经理」( product manager for automation technologies ) Sal Soghoian 在 2016 年 11 月[离开](https://macosxautomation.com/about.html)了苹果，不管是 Sal 本人自己提议还是苹果的辞退，这都是一个标志——在苹果看来：「给一堆照片批量重命名要点鼠标点键盘好多次好烦哦？那就去 App Store 下一个 $9.99 的 App 吧，这才是未来！」不过这是另一个故事了。 [↩︎](http://sspai.com/36442#ffn1)
2. 这里之所以用了 `⌘ ⌥ ⇧ ⌃`这种看起来十分难按的修饰键，是因为我将 `CapsLock ⇪`更改为：长按按下时相当于同时按下了 `⌘ ⌥ ⇧ ⌃`，短按时为 `Esc ⎋︎`，同时把 CapsLock 这种新的用法称为 Hyper 键。如果你在使用 OSX 10.11 或更早的系统，可以参考[这篇文章](http://eamesliu.com/post/101419356939/caps-lock-key-to-hyper)来修改；如果你在使用 macOS Sierra，[这篇文章](https://sayzlim.net/remapping-hyper-key-macos-sierra/) 和 [这篇文章](http://brettterpstra.com/2016/09/29/a-better-hyper-key-hack-for-sierra/) 分别可以参考。 [↩︎](http://sspai.com/36442#ffn2)

文章来源 [少数派](http://sspai.com) ，原作者 [Oscar Gong](http://sspai.com/author/711608) ，转载请注明原文链接

原文可获取应用下载链接：[Keyboard Maestro 入门指南](http://sspai.com/36442)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/B5195342-3820-4F34-930B-DB5F86474B9C/0487B838-D7A5-4FC7-85A2-45FAA6D505F4.jpg)](http://sspai.com/36393)

---

[🌐 原始链接](http://sspai.com/36442)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c0740238-fa4c-4e83-a347-bd920299acff/c0740238-fa4c-4e83-a347-bd920299acff/)