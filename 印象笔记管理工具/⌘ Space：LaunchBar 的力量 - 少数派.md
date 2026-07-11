# ⌘ Space：LaunchBar 的力量 - 少数派

---

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/37944958-3338-4C7A-9488-8485566F942D.jpg)

⌘ Space：LaunchBar 的力量
=====================

[![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/DA1391F2-AFD5-4DB4-97DC-B79F99F97C97.png)](https://sspai.com/user/711608)[Oscar Gong](https://sspai.com/user/711608)1小时前 6 [2](#)

目录
:   1. [关于程序启动器](https://sspai.com/post/38526#ss-H2-1490597347840)
    2. [LaunchBar](https://sspai.com/post/38526#ss-2-1490584263224)
    3. [尾巴](https://sspai.com/post/38526#ss-2-1490584263229)

关于程序启动器
-------

当在 Mac 上想要运行一个 App 时候，你会怎么做？当你想打开一个文件或文件夹的时候，你又会怎么做？有一类 App 是专门做这个的。对于我来说，离开了这类 App 使用电脑，就像去朋友家做客时，夜里起床想穿过客厅去厕所，找不到灯的开关，磕磕绊绊中踢到了家具最后抱着脚流眼泪。

平均每天我会唤起 LaunchBar 使用它的各种功能 30 多次，在密集使用 Mac 进行生产力活动时，更是几乎每 10 分钟就有一次。从我使用 Mac 开始，最早使用的启动器是 Alfred，但是当我接触到并使用了一段时间 LaunchBar 后，就毫不犹豫的转换了过来，不仅是因为 LaunchBar 颜值更高，更是因为 LaunchBar 的设计思路更 macOS，能做到的事情也比 Alfred 更多。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/F2F7099F-2978-4D72-9068-404D8A4966D4.png)

虽然小标题为「程序启动器」但是启动器类 App 的用处不止于此：运行 AppleScript，执行一段临时起意的 Shell Script，直接在某个网站内搜索，打开一个浏览器书签，把一定金额的美元换算成人民币，获取剪贴板历史……这些功能还不是全部，无论 Alfred 还是 LaunchBar 都会随着你的使用变得越来越熟悉你，会学习你的使用习惯：提高你最经常使用的动作的优先度，会越用越顺手。

在 OS X 10.10 Yosemite 中，苹果把 Spotlight 的位置从屏幕右上角移动到了屏幕中间，些许地提升了一些 Spotlight 的「力量」。那么，这种「程序启动器」的应用点子是从哪里来的呢？

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/17D99FBF-6F1F-4387-B12F-1901B2953ACC.png)

⌘ Space 的历史

LaunchBar 始于 1995 年，运行在 OS X 的前身 NeXTSTEP 上。Norbert Heger，LaunchBar 的开发者，与 Derrick [讲述了](http://archive.oreilly.com/pub/a/mac/developer/2003/09/25/innovators.html) 这个软件的历史。在访谈中 Norbert 谈到：当你的文件系统是按照层级 (hierarchical) 来组织的时候，就很难快速定位到很深层目录下的某个文件；并且你把你的文件管理的越好、越井井有条，你找东西时候花费的时间就越多，为了解决这个问题，Norbert 开发了一个软件，只要把你想要的文件大概描述一下，剩下的寻找工作交给电脑来做，于是 LaunchBar 就诞生了。

最开始时 LaunchBar 只是一些 Shell 脚本的集合，但是随着 Norbert 和 [Objective Development](https://www.obdev.at/index.html)（LaunchBar 的开发商，同时还开发了 [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html)）团队使用 LaunchBar 使用的越来越多，他们意识到，这个软件有着非常广的用例，发布出来的话许多人都可以从中获益。于是，在 1996 年的时候 Objective Development 释出了 LaunchBar 公共测试版。

Norbert Heger：

> The very first “prototype” was not even an application. It all began with dozens of little shell scripts and a tiny Terminal window. … The Terminal window was placed in one of the screen corners, allowing us to bring it to the front quickly using the mouse. When we wanted to launch Interface Builder, for instance, we just had to click that screen corner, enter “IB” …
>
> As you can imagine, this approach was not really practical. We had to create a new shell script for each and every item that we wanted to access, so we thought, hey, there must be a simpler way to accomplish this.
>
> So we started developing a rating algorithm to determine the best matching item for a given abbreviation automatically.…. Even today, we're still trying to improve and optimize that technology in order to achieve even better search results.
>
> 在最早的原型阶段，LaunchBar 甚至不是一个完整的 App，只是一个保持在屏幕角落运行的 Terminal 窗口，当我想运行 Interface Builder 这个 App 时，我就点击屏幕角落，输入 "IB" 这个提前确定好的字符串。正如你猜到的，这么做很累人，需要给想访问的每个项目写一个新的脚本。于是我们花了两个月时间开发了一套算法，可以自动归纳项目的缩写。

然后我们熟悉的「Command 空格」也来了：

> Johannes “invented” the Command-Space hotkey back in 1995. In NEXTSTEP it was nearly impossible to implement a system wide hotkey, but Johannes found a way to patch the Display Postscript Server (also responsible for dispatching keyboard and mouse events), allowing us to activate LaunchBar with a single keystroke. Fortunately, these things became much easier to accomplish in Mac OS X.

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/C90A5287-A01E-4625-B3AA-E986434AB28E.png)

对于今天的 Mac 来说，LaunchBar 并不是唯一的「程序启动器」，一个 App 只要能够快速打开其它程序或文件、快速触发一个流程，都可以称为「程序启动器」，Spotlight 是，Launchpad 是，调教过的 Keyboard Maestro 也是。

当前来说，毫无疑问 Alfred 占据了 [绝大多数](http://www.threecentsapp.com/questions/71509087002675863/results) 这类软件使用者的桌面，向新手推荐 Alfred 是不会犯错的选择，功能强大的同时基础功能是免费使用的，当熟悉了基础功能以后还可以按需购买 Powerpack 增强包。但是对我个人来说我更喜欢 LaunchBar。

我青睐 Launchbar 的原因有几点：

1. LaunchBar 的 Instant Send、查看 App 最近打开的文件历史、剪贴板历史 [等等特点](https://www.obdev.at/products/launchbar/features.html)，利用尽了 macOS 的优势；
2. LaunchBar 有着 [20 多年](http://archive.oreilly.com/pub/a/mac/developer/2003/09/25/innovators.html) 的开发历史，而我又是特别喜欢这种端庄、正派物件的人。（[这里有一篇文章，整理了一些有着悠久开发历史的 macOS 软件](http://shawnblanc.net/2014/06/longstanding-mac-apps/)）

介绍 ⌘ Space 的历史或者说介绍 LaunchBar 的历史，是为了帮助理解： LaunchBar 与 Alfred 和 Spotlight 虽功能相似，但是在最初之时的设计理念就有所不同，Alfred 是一个站在系统旁边的「助手」，自己就能完成各种事；LaunchBar 本质上是一扎脚本的集合，对各种「变量」传入传出处理很好。

由于 Objective Development 是一家德国公司，LaunchBar 本身也只提供英文和德文的语言界面，中文下会有很多不便，建议在英文系统下使用，我也会在下文着重涉及一些母语为中文的人在 LaunchBar 中可能遇到的问题和一些应变方法。1

LaunchBar
---------

### 组成

使用 LaunchBar 除了启动器本体，LaunchBar 索引编辑器（⌥ ⌘ I）也要熟悉，未来有了制作自己的动作需求的时候，还会用的到动作编辑器（⌥ ⌘ E）。

### 

### 上手

对于之前的 Alfred 或者 Spotlight 用户来说，一开始使用 LaunchBar 最不适应的地方恐怕就是「Retype Delay」机制了。在 Alfred 和 Spotlight 中，按下回车之前，输入框中的内容是可以随便修改的；但是在 LaunchBar 中，只有在 retype delay 期间，输入的内容才可以修改（可以通过观察右边字符下面的下划线来得知，有下划线时可以修改），过了这段时间只能重新输入。

看起来不够友好？但是当你习惯了这个系统以后，效率是会提高的：因为在 LaunchBar 的自适应系统下，你不会经常需要微改输入了一半的指令，即使输入有小的错误也是可以到达预期的内容的；经常的情况是，输入途中突然变了主意，需要输入一条全新的，这个时候 LaunchBar 的设计就比按 n 次退格键方便很多。

[这里](https://vimeo.com/user40690351/videos)是 Objective Development 在 Vimeo 的频道，有着几个非常棒的 LaunchBar 功能介绍视频，一定要看一下。

#### Preferences 首选项

拿到手一个软件，第一时间要做的肯定是 ⌘ , 把各种设置翻一遍。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/8B29A346-C354-4EB3-933A-A5CFD60DD719.png)

* General Options：Retype Delay 在刚刚使用时可以适当调高一些，给自己多一些反应时间，老手觉得拖沓以后再调低。
* Appearance ：建议打开「Show All subtitles」，显示小标题。LaunchBar 的 Action 种类众多，有时甚至会出现名称一样但是是两个完全不同的动作的情况。
* Shotcuts:

+ 「Search in LaunchBar」就是唤起 LaunchBar 小黄条的快捷键。苹果在某一年把激活 Spotlight 的快捷键和切换输入源的快捷键对调了，在这里改成你习惯的那个就好。紧跟着的「Search in Spotlight」是调用的 Finder 中右上角的 Spotlight，而不是在屏幕居中显示的那个2。
+ 「Instant Send」为把当前选中的文字、文件、图片发送到 LaunchBar 为接下来处理做准备的快捷键，建议开启，我的设置是双击Fn键。还有另一种使用 Instant Send 的方式是长按 ⌘ Space，但是可能与 Sierra 中唤起 Siri 快捷键冲突，可在「系统偏好设置 - Siri - 快捷键」中更改。

* Clipboard：

+ 「Show clipboard history」为唤醒剪贴板历史的快捷键，我的习惯是 ⇧ ⌘ V。
+ 「Enable ClipMerge」勾选时，按两次 ⌘ C会把当前选中的内容附加到当前剪贴板后，开启后不仅仅可以附加其它 App 中的新内容，剪贴板历史本身的内容对 ClipMerge 也有效。

#### Adaptive Abbreviation Search 自适应简称搜索

LaunchBar 有着自己的一套自适应的缩写机制，自适应体现在：

* 像 System Preferences 系统偏好设置，SP 能搜到，SYS也能搜到。尽管 SYS 第一次搜索时，排在最前面的可能是 "System Info"，但是一旦通过 SYS 打开过系统偏好设置，下次再输入 SYS 时排在最前面的就变成了系统偏好设置。
* 不同于 Alfred 和 Spotlight，LaunchBar 可以为每一个动作分配你自己喜欢的快捷键。方法是用方向键移动到目标项目上，右击 LaunchBar 的这个部分：

  ![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/0B3CE0E1-72E1-4F95-93F5-0AAAAA854543.jpg)

  选择「Assign Abbreviation」或者直接使用快捷键 ⌥ ⌘ A。我用 Todoist 非常多，所以我分配了数字「2」键给 Todoist，输入 2 后排在最上面的就是 Todoist，比无论训练多少次的 TO 都要快。像优酷和百度网盘以及一小部分软件，不知道是 info.plist 的哪里写的不对还是其它原因，英文系统下的名字还是「优酷.app」，总之就是搜不到，我通过分配 YOUKU 给他解决了这部分软件的搜索问题。

基本上各个项目排列顺序可以归纳为：应用程序的权重最高、其次为文件夹、最后为动作，内建动作又高于自定义动作。

对于训练过的（分配过缩写）的项目，LaunchBar 在速度上更进一步，有一个小技巧叫「Instant Open」，对于我来说，打开 Todoist 的步骤可以从【⌘ Space → 2 → ↵】缩短成【⌘ Space → 2 (长按)】； System Preferences 这种缩写为两个字母的为【⌘ Space → S → P (长按)】，省去了按回车这一步，减少了手臂移动。

#### Sub-search 次层级搜索

LaunchBar 中有一个搜索状态的区别，可以通过下方候选项光标背景颜色来区分：蓝色为搜索大类（母类）；黄色为 Sub Search，搜索子类。当一个集合的内容较少时候，可以按空格键跳过集合下的小集合，直接浏览或「次层级搜索」这个集合的全部项目。

举个例子，LaunchBar 以特殊的文本片段 (Snippet) 形式有对 Emoji 的完整支持。输入EMJ 后，在蓝色背景下按方向键选择 Emoji 这个 Indexing Rule，Space 可以直接查看所有的 Emoji 表情（小项），也可以 → 或 Enter 查看「旗帜」啊「人物」啊的更细的分子类。

无论是直接查看所有项目，还是查看细分类，光标背景都变成了黄色，指示着此时处于 Sub Search 状态，这时再输入就是你选择的这个小范围中搜索，而不是整个 LaunchBar。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/82B0E3F9-D0E4-4F0B-ABB5-93E55E1282C2.png)

再举个例子，LaunchBar 可以直接进入 Chrome 内部[搜索](https://cl.ly/jefi) Chrome 中的历史记录、书签、当前打开的网页，大概整理如下，其中 Application 和 Indexing Rule 都可以直接在主层级搜索访问到。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/467D04CD-4B12-4EAA-8C86-6313096BB61C.png)

通过在 Index 中控制部分集合在 Sub Search 下显示，有助于保持搜索结果的精简。

#### Action 动作

「动作」是 LaunchBar 和核心，通过 Adaptive Abbreviation Search 只搜索到了内容但是无后续动作，那搜索就毫无意义。轻点回车或 Instant Open 打开是最简单的动作。

动作是贯穿整个 LaunchBar 的，大概可以分为：

* ⌘ Y 或空格使用 Quicklook 预览。
* ⌘ ↵ reveal（中文的翻译或许应为揭示、显示？我琢磨半天觉得都不太恰当）选中的项目。文件和文件夹会在 Finder 中展示；身份卡、邮件地址、电话号码等通讯录项目会在 Contact.app 中展示；1Password 项目会打开 1Password 中对应的位置等等。
* 左右箭头，在相关联的上下文或层级结构中导航。
* Tab 键，发送选中的项目。举个例子，我查找到了「VLC」后，Tab 发送，进入次层级搜索，UNNW 找到了「Uninstall with CleanMyMac」，回车确定，使用 CleanMyMac 卸载了 VLC。实际的操作中 LaunchBar 其实并没有把整个 VLC 软件都真的交给了 CleanMyMac，而是把 VLC 的路径：~/Applications/VLC.app 传递给了「Uninstall with CleanMyMac」的这个系统服务，即，填到了 Shell 脚本：open -a CleanMyMac\ 3.app {query} 中 query 部分。

  ![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/C20B8486-DFE3-40D8-B38A-E3F5A926268A.png)

  记住 Tab 键，你会用到它非常非常多次。
* ⌘ ⇧ I，在 LaunchBar Index 查看选中动作。
* Finder 相关：

+ ⌘ I 查看信息。
+ ⌘ T 在 Terminal 中定位到当前 Finder 位置。

### Browse 浏览

文件夹、书签的文件夹、联系人、联系人的分组、iTunes 库、应用程序的最近文件，都是集合，所有的集合都可以通过方向键左右箭头来导航浏览集合下的子项目。

LaunchBar 有着完整的文件系统导航功能，浏览、重命名（⇧⌘R）、创建新文件夹（⇧⌘N）一应俱全。

浏览功能是我非常喜欢的几个 LaunchBar 特点之一：

* 输入DWN 定位到我的 ~/Users/Downloads，使用 ⌘ → 查看文件夹的内容，并且使其按照修改日期排列——快速处理我刚刚下载的内容。
* 输入 TYP 定位到 Typora，我常用的 Markdown 编辑器，→ 查看最近几篇用 Typora 编辑过的文章，在背景为黄色，已经进入 Sub Search 状态时，⌘Y 或空格 QuickLook 文章内容（macOS 没有提供原生的 Markdown 预览，我安装了 [QLMarkdown](https://github.com/toland/qlmarkdown) 这个插件实现了这个功能），甚至更近一步继续 → 查看文档的 metadata 元信息：行数、创建日期、修改日期、大小等。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/21F55E51-18CE-4515-87CA-FB138043256D.png)

### Instant Send

Instant Send 是极其快速的把选中的文件或文字输入到 LaunchBar 的方法。可以通过快捷键（上文有提到）或把内容拖拽到 Dock 上的 LaunchBar 图标使用 Instant Send。

Instant Send 是我最喜欢的 LaunchBar 功能，用法非常多，几个我的用法：

* 在 Finder 中找到一张待处理的图片，双击 Fn 发送到 LaunchBar，⌘Y 预览，→ 查看下 Metadata 元信息，确定就是这张了，tab 使用 Pixelmator 或 Snagit 进行编辑、标注；我的默认文件浏览器是「预览」，但是预览如果不在打开时就选择多张图片，就无法在打开后查看上一张或下一张，Xee 可以。想想以前的流程：右击图片 - Open With - 选择使用 Xee 打开，在可以处理这种格式的软件很多时，要等待系统转圈加载，手还要在触摸板上进行小范围移动的精细操作，使用 Instant Send 把图片发送 Xee 打开，没等待过程，甚至全程不需要碰触摸板！
* macOS 上有个软件叫 [PopClip](https://pilotmoon.com/popclip/)，提供了一些蛮实用的小功能，但是这软件有一些小问题：经常无法弹出，还与部分剪贴板管理软件有冲突。[研究](https://github.com/pilotmoon/PopClip-Extensions)一下 PopClip 的动作，其实就是 URL Scheme 或者 AppleScript 嘛，把当前光标下选中的内容填到 URL 的某一部分，熟悉 [Launch Center Pro](https://contrast.co/launch-center-pro/) 的朋友一下子就能明白这个模式；或者作为传入值执行 AppleScript，完全可以用 Instant Send 完全代替掉 PopClip。在 Index 中添加一个 Custom Search Template:http://s.taobao.com/search?oe=utf-8&f=8&q=\*，一个淘宝搜索的动作就做好了，选中想搜索的文字，双击 Fn，Tab 就能使用淘宝搜索。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/ABE8B48B-FA00-40CA-BD0F-6818D2106B7C.png)

* 处理文件时候 Shift 和 Command 齐用选中了几个文件，Instant Send 使用 Keka 剔除掉类似 .DS\_Store 这种 Windows 用户看了一头雾水的文件后直接压缩；压缩后再次使用 Instant Send 传到到 Mail 直接发给接收文件的人。流程不要更舒爽……

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/062855E3-4D52-4A7D-B7FA-920F87902C7C.png)

* 在「自适应简称搜索」部分提到过「Instant Open」这个功能，Instant Send 也有类似的设计：发送到 LaunchBar 中的文字，可以直接长按动作缩写的最后一个字母直接调用相应动作处理。看到女朋友发来的「记得礼拜五晚上帮我去天猫抢资生堂的粉底液啊」，双击 Fn 发送到 LaunchBar 后，长按 2 就直接发送到了 Todoist 。🤦🏻‍♂️

本质上来说，Instant Send 只是一种把（输入的）文本、（Finder 中找到的）文件或文件夹，快捷的传入到 LaunchBar 中的方法，传入后的内容与手动在 LaunchBar 中一步步找到的内容在后续的处理方法（Action）上并没有什么区别，Instant Send 是最能体现我前文说到的「LaunchBar 设计思路更 macOS」的地方。

### 与其它程序的互动

像 Alfred 需用 Workflow 来提高与 Fantastical、Evernote 的互动能力不同，LaunchBar 本身就内置了与各种 App 联动的能力，加上更好的利用了 macOS 的「服务」这一特点，无需做多余工作就能融入现有的工作流。

Evernote：定位到 Evernote 后按空格即可搜索 Evernote 搜索内容，可以使用 [Evernote 高级搜索语法](https://help.evernote.com/hc/en-us/articles/208313828-How-to-use-Evernote-s-advanced-search-syntax)。因为在 LaunchBar 中搜索不像在 Evernote 右上角中输入会实时反馈搜索结果，我一般只用Tags:快速定位到几个标签。

日历：Calendar 下找到想添加的日历（账号）后，空格，可以使用（算是）自然语言（吧）直接添加日历项目，像这样：

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/35327F62-26ED-4503-BCC0-08AFEEC8512F.png)

Tab 可以快速输入 @ ，具体语法可以看[这里](https://www.obdev.at/resources/launchbar/help/index.php?chapter=WorkingWithCalendars)。 LaunchBar 自己设计的语法并不好用，所幸 LaunchBar 有 Fantastical、QuickCal 这种大家常用的日历软件的支持，调用他们使用真正的自然语言建日历项吧。

1Password : 需要在 1Password「设置 - 高级」中开启第三方 App 集成。LaunchBar 有着超赞的 1Password 的集成，书签密码、信用卡、软件许可一应俱全。回车直接查看，如果是密码的话则会直接用默认浏览器打开网站并自动填写密码；⌘↵ 会在 1Password 主程序中打开对应项目。有了 LaunchBar 我已经很久没使用 1Password Mini 了。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/B26FCA7D-9EFC-4DAB-ABB2-087D017B8D85.png)

Dash: 程序员朋友会经常用 Dash 来查看文档，与 Evernote 类似但又有所不同，LaunchBar 的 Dash 搜索有动态反馈。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/F69D7299-94B5-465A-9137-69828E8994A0.png)

其它的还有搜索 Mac App Store，Todoist、OmniFocus、2Do 添加任务，Twitter 发推，Tower 进行 Git 操作……都有很好的支持。

### LaunchBar 自己的动作

#### 程序切换

LaunchBar 提供了简单的应用程序切换器，可以从 ⌘ R 进入；或者在按下⌘ Space 后保持 ⌘ 不松开，继续点击空格来进入。但是我不使用它来切换应用程序，这明显不如系统自己的 ⌘ Tab 好用，更何况我用 [HyperSwitch](https://bahoom.com/hyperswitch) 把⌘ Tab 的逻辑进一步改进成了在打开的窗口之间切换。我使用这个功能来管理当前活跃的应用程序，在 LaunchBar 程序切换器中，⌘Q 退出、⌘H 隐藏、⌘⌥F 强制退出都是十分符合直觉的设计。在完成了手头的一个活的时候，Dock 上经常挤满了打开的各种软件，用这种方法可以快速清理出一个新的工作区。

#### 打开 URL

⌘ L 可以进入 URL 输入框，可以要多随意就有多随意的输网址，LaunchBar 会翻遍各个浏览器的历史记录和书签来补全，补全后可直接回车打开，也可以 Tab 进入发送：选择其它浏览器打开、使用 Downie 下载视频、使用 Flox 下载文件、使用我的自定义动作缩短成 bit.ly 短网址。

Alfred 有一点我诟病了很久，它的剪贴板历史功能与其它部分是隔开的，在 Alfred 中输入命令输入了一半时，查看剪贴板历史，会中断当前输入，即，无法把剪贴板历史插入到当前输入中。高兴的是 LaunchBar 在这个地方处理的很好。

#### 杂项

正如 LaunchBar 的 [Solgan](https://www.obdev.at/products/launchbar/features.html)，「1000+ Features, 1 Interface」，关机、休眠、重启；开启屏幕保护程序；清空废纸篓；弹出挂载中的驱动器；Base64 转码，LaunchBar 自己就能做到的小动作太多了，列举不完，翻一翻 Index 中 Actions 下的 Build-in Action 都是，熟悉熟悉在以后有需求了能想起来用就好。

### LaunchBar Index 索引编辑器

LaunchBar Index 里包含了所有会出现在 LaunchBar 中的搜索结果，基本上对 LaunchBar 的调教就是对 Index 的调教，Index 内的每项都值得研究。

像 Network Locations、User Accounts、Themes 等一些不会经常用到的集合，我都在 [Option] 中选择了 「Access items via sub-search only」，以保持 LaunchBar 候选项的简介、不混乱。

* Application：[Index] 中可以把一些死活没有英文的软件指定一个英文或拼音别名，要注意的是，指定别名 ≠ 分配快捷键，指定的别名无法在 Instant Open 中使用；[Option] 中建议更改为 Search Everywhere，因为不是所有的程序都存放在 ~/Applications 下，更改下以便于搜索到各个角落的 .app 文件。
* Actions 下的 Actions、Services、Workflows 有必要排着扫一遍，大概对所有动作有个印象，同时关掉直觉上就认为将来不会用到的动作。
* Contacts：

+ 这里我用到了一个 iOS 上的 App，[Phonetic Contacts](https://itunes.apple.com/cn/app/phonetic-contacts/id1078961574?l=en&mt=8) 来辅助。Phonetic Contacts 是一个可以在通讯录联系人中添加拼音字段的 App，有了拼音字段后，英文系统的 iOS 通讯录才能正确对中文名字联系人排序。
+ 在 Phonetic 中，开启「姓&名拼音」，「字段用于快速搜索」中开启「备注字段」部分，执行后待 iCloud 同步到 Mac 端。
+ LaunchBar Index - Contacts - [Option] 中勾选「Prefix with phonetic name」
+ 效果如图，可以直接输人名缩写，像「ZGLT」，或全拼的一部分，来定位联系人。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/5BA3B2D0-3422-4A3D-A89A-35B62C6A86CA.png)

* Web：可以看到 LaunchBar 已经有了两个内置的 Search Templates 搜索模板，不过 Encoding 编码不同，一个为 「ISO Latin 1」，一个为 「UTF-8」。简单来说，几乎所有网站都支持 ISO Latin 编码，但是他只支持西文字符，我把一些搜索词本来就为西文的模板放在这里，像 https://savedeo.com/download?url=\*，\* 处代替 Twitter 为链接，使用 Savdeo 下载 Twitter 中的视频；http://tinyurl.com/create.php?url=\* ，\* 代替为需要被 TinyUrl 缩短的长网址。UTF-8 编码支持范围更广，如中文，我新建了一个「Empty List of Search Templates」，设定为 UTF-8 后，常用的搜索模板都在这里面，像https://pinboard.in/search/?query=\*+&mine=Search+Mine，搜索 Pinboard 中我添加的内容；https://www.zhihu.com/search?type=content&q=\* 搜索知乎。
* Files & Folder：

+ Mounted Volumes 中我勾掉了 BootCamp，我的 Mac 上的 Windows 只是用来打 Overwatch 的，我不想在 Mac 上看到或处理任何 Windows 中的文件，即使我有安装 Paragon NTFS。
+ Home~ : 我的设置是 [Option] 中 「Search Scope」为两层子文件夹，搜索内容只为 Folder。同时添加 ~/Documents、~/Downloads、~/Pictures 搜索所有子文件夹的所有类型文件。实现在简洁和功能上的平衡。

### 问题和杂项

上文用了几千字讲了 LaunchBar 的优点，但是 LaunchBar 的问题也有不少。

#### 第三方 App 兼容

关于 Shell 脚本，LaunchBar 有「在 LaunchBar 中执行」、「在 Terminal 中执行」、「在 iTerm 中执行」共三种方法，前两种方法不受其它因素影响，但是第三种，在 iTerm 中执行，LaunchBar 的内置动作会寻找 iTerm 1，然而事实是 iTerm 已经升级到了版本 2，与版本 1 的 AppleScript 不再兼容，所以 LaunchBar 内置的在 iTerm 中打开 Shell 脚本的动作就失效了。[这里](https://cl.ly/jgP1)有一个自定义动作，可以在 iTerm 2 中运行 Shell 脚本，安装后在 Index 中把内置动作禁用掉吧。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/8D3359EF-5E82-4B08-A24F-D83368F105C1.png)

类似的问题还发生在 Evernote 和 Airmail 中：Evernote 目前是版本 6，LaunchBar 的内置动作还会寻找 Evernote 5；Airmail 现在的版本是 3，LaunchBar 还在坚持寻找 2。

虽然有解决办法，但是根本办法还是希望 Objective Development 的开发能更积极一些。

#### 滚动方向

Mac 的触摸板很好用，和 Windows 上大多数触摸板的滚动方向不一样，叫做「自然滚动」，是把当前屏幕上的内容想象成一个画布，而滚动是模拟手指在拖拉这个画布。在 LaunchBar 中使用触摸板滚动时，因为 LaunchBar 中没有「画布」，只有「光标」，所以「自然滚动」在 LaunchBar 是对光标而言的，如果你不习惯这种设计，可以在 Terminal 执行：

defaults write at.obdev.LaunchBar NaturalScrolling YES

更改成和其它软件中类似的逻辑。

开发者在[这里](https://blog.obdev.at//why-doesnt-launchbar-scroll-naturally/#more-627)一篇博文解释了这个问题。

#### 剪贴板管理

对于剪贴板中的图片和文字，在 Tab 发送出去时，LaunchBar 是把整个图片的内容和整个文字的内容发送的，而不是 image.jpg 或 text.txt 以文件的形式发送，然而能够接收处理图片内容的动作非常少，导致 LaunchBar 没办法直接特别好的把剪贴板中的内容做进一步处理。

当然可以理解的是 LaunchBar 这么设计是有着一致性的考虑，为了解决这部分需求，我使用 Keyboard Maestro 来实现直接对剪贴板内容处理。

### 动作的获取和制作

足够丰富的动作是一个启动器的立足之本，LaunchBar 有着丰富的资源。

* 首先是[这个](https://www.obdev.at/products/launchbar/actions-de.html) LaunchBar 官方动作示例库，其中的 Convert Currency 汇率转换和 Spotify 动作都非常值得一用。

![](.evernote-content/54B45B00-E8FE-451B-8101-D3C026D78A45/8ABF7F8F-E18E-4134-931C-EA9C41996E3E.png)

* [这是](https://forums.obdev.at/viewforum.php?f=24&sid=edac318ce0527502083a40fd1bc896e7)官方论坛，里面内容也不少，但是呈现做的不够好。我把他当成一个字典来用，做动作找不太到思路的时候会来这搜一下关键词，找找思路。
* [这里](https://atika.github.io/launchbar/)是一个又爱好者搭起来的网站，前文提到的 Run iTerm2 Command 就是来自这里，同时这还有一个不错的主题。
* [这个](https://github.com/hlissner/lb6-actions) Github 页面列举了非常多的动作，值得一看。最下面提到的其它网站也值得留意一下。

#### 编写自己的 Action

「自己动手，丰衣足食」，我曾在刚刚使用 Alfred 时，沉迷往返于各个论坛下载别人制作好的 Workflows 来用，其中有一些很是疯狂，像在 Alfred 中使用 Workflows 制作了一个 [aria2 管理器](https://cl.ly/jfj3)，但过了一阵后发现我下载下来的这些我用的其实并不多，真正多的是我自己亲手做的那部分。LaunchBar 的社区虽没有 Alfred 活跃（[市场份额差距](http://www.threecentsapp.com/questions/71509087002675863/results)在这里摆着），但是因为我会自己做动作，我之前的工作流可以完整的迁移过来。

如果你想制作 LaunchBar 动作，⌥ ⌘ E 打开 Action Editor，General 部分的动作图标、动作名称……这些信息按自己的需求填写就好，填写完成的这部分内容会和其它 macOS 上的 bundle 一样，生成一个 Info.plist 在 bundle 下。

#### LaunchBar 支持任何能在 Mac 上运行起来的语言，从简单的一小段 Shell Script，到 Python、Ruby 或 PHP 脚本语言，到 Objective-C 这种需要编译的语言。用哪种不重要，顺手就好。

* Default Script：通常情况下被执行的脚本。当动作被选择，用户按下回车时，或者按下右箭头时（适用于脚本有返回值，而且不需要有输入值就有返回值的情况）脚本被执行。每一个动作都要有一个 Default Script。
* Suggestions Script：只在输入过程中被执行。就像名字所预示的那样，这段脚本用于给用户建议可能想输入的内容。当用户完成输入，在建议的结果中选择了一个并按下回车后，把被选择的内容会传递到 Default Script 中。

要注意的是，如果你使用的是 JavaScript，那么你不能通过像其它脚本语言一样通过 [Shebang](http://www.wikiwand.com/en/Shebang_(Unix) 部分来指定解释器，LaunchBar 使用[JavaScriptCore Framework](https://developer.apple.com/reference/javascriptcore)提供了对 JavaScript 的原生支持，效果是 JavaScript 与 LaunchBar 结合的更好，可以实现像使用 LaunchBar 弹出警告这种使用其它语言做不到的功能。[这里](https://developer.obdev.at/launchbar-developer-documentation/#/javascript-reference)有详细的 LaunchBar JavaScript 文档。

在编写这部分我写的很粗糙，因为[官方文档](https://developer.obdev.at/launchbar-developer-documentation/#/welcome)十分详尽，我完全翻译一遍也没什么意义，按需自行查阅就好。

尾巴
--

因为我之前是 Alfred 用户，后来转来使用的 LaunchBar，文中处处充满了 Alfred 和 LaunchBar 的比较，但是我并没有贬低一者抬高另一者的意思，我还为 Alfred 保留了快捷键，以便使用一些用我不懂的语言编写、未能移植到 LaunchBar 的 Alfred Workflows。

Alfred 的开发和社区很活跃，容易上手，基础功能免费，毋庸置疑的是一个了不起的软件。但是如果你不尝试一下 LaunchBar 的话，You missed a lot！

1. [非英语使用者在赛博世界是二等公民的事实不是一天两天，在可以预测的未来里还会持续下去。改变世界还是改变自己? make your decision！](file:///Applications/%E5%8D%B0%E8%B1%A1%E7%AC%94%E8%AE%B0.app/Contents/Resources/common-editor-mac/uno-mac.html#)[↩](#)
2. [现在新款设备上统一成了 ⌃Space 切换输入源，⌘Space 唤出 Spotlight，iOS 上是没法改快捷键的，为了与 iPad 的统一体验，Mac 也改过来吧。](file:///Applications/%E5%8D%B0%E8%B1%A1%E7%AC%94%E8%AE%B0.app/Contents/Resources/common-editor-mac/uno-mac.html#)[↩](#)

[#](https://sspai.com/tag/macOS)macOS[#](https://sspai.com/tag/%E6%95%88%E7%8E%87)效率[#](https://sspai.com/tag/%E6%95%88%E7%8E%87%E5%B7%A5%E5%85%B7)效率工具

---

[🌐 原始链接](https://sspai.com/post/38526)

[📎 在印象笔记中打开](evernote:///view/207087/s1/6ebb6c6c-3942-4725-9e1b-7a40e6e56cd4/6ebb6c6c-3942-4725-9e1b-7a40e6e56cd4/)