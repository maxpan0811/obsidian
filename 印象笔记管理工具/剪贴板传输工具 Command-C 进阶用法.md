# 剪贴板传输工具 Command-C 进阶用法

---

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/650CA47E-4F89-4F41-A2D1-502DFF7C94B3.jpg)

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/6359F5C8-CAF5-4B9A-B8C8-521B7EE293A9.png)

Command-C 最打动我的是对少数需求的支持。它的各个功能都可以用 x-callback-URL 来做到，Mac 上有全面可自定义的快捷键，甚至支持了 AppleScript。最近入了 iPad Pro 后，我又发现这个小众工具竟然这么快就支持了最大的 iOS 尺寸……

因为 Command-C 容易上手，所以我并不打算介绍它的基本功能，这篇文章主要讲解的是它在 iOS 和 Mac 上的进阶功能——如何使用它的 URl Schemes 和 AppleScript——从而让你在此类工具的选择和使用方面一步到位，不再存疑。顺利的话，你应该还能学会一些关于制作 Popclip 插件的东西。

iOS 上的进阶用法
----------

首先说下 Command-C 的基本 URL Schemes[1](http://sspai.com/32293#fn1): `command-c:`

其次，Command-C 已经在 2.0 版本中使用 UUID[2](http://sspai.com/32293#fn2) 代替了之前通过设备名或者设备的匹配顺序来定位设备，所以之前的 URL Schemes 已经都不能用了。现在想用 Command-C 的 URL Schemes，就需要用到自己的设备在 Command-C 中的 UUID。

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/8BEDDE93-D5A1-4300-8145-DE5CA32A3E2B.jpg)

在 Command-C 的设置界面的设备列表中，进入各个设备的界面就能复制该设备的 UUID。

以上两步是准备工作，下面正式开始折腾。

Command-C 的 x-callback-URL 分为以下三个类别：直接发送剪贴板内容、直接发送文本和发送链接并在目标设备打开该链接。

### 1. 直接发送剪贴板内容

这是最常用的动作：

> command-c://x-callback-url/share?deviceUUID=`你设备的 UUID`

上面这条 URL 做到的事是：把目前的剪贴板内容直接发送到另一台**装有并运行[3](http://sspai.com/32293#fn3)**了 Command-C 的设备。**这时候，目标设备的剪贴板会直接被替换，你只要在你想粘贴的地方执行粘贴的操作即可**。如果你有多个设备，还有 Launch Center Pro，那么你可以使用 List 来制作列表，在使用的时候通过列表选择目标设备。

这个动作的制作很简单：

假设你有一台 iPhone 和一台 iPad（任意型号），那么在 Launch Center Pro 中，使用 List 的这个动作的 URL 应该是这样：

```
command-c://x-callback-url/share?deviceUUID=[list: Choose a device|iPhone=UUID|iPad=UUID]
```

如果再多的话就按照格式，在最后的中括号前面添加 `|Macbook Pro=UUID` 即可。*注意不同的设备要用不同的 UUID。*

如果，你想在发送完剪贴板内容后自动回到上一个 App 或者接下一个动作，可以用：

> command-c://x-callback-url/share?x-source=`SourceApp`&x-success={{`sourceapp`://}}&x-error={{`sourceapp`://}}&deviceUUID=`你设备的 UUID`

这里面有三个 `sourceapp`，你可以直接把第一个替换为你想跳转的 App 的 App 名，比如 `Launch Center Pro`。后面的两个`sourceapp` 你要将它们替换为对应的 App 的基本 URL，`Launch Center Pro` 的基本 URL 是 `launch:`。

### 2. 直接发送文本

这个并不常用，我也想不出使用情境。除非你有一些字符需要经常在各个设备间传输，但这个功能用系统的`文本替换`也完全可以做到。它的 URL Schemes 是这样：

> command-c://x-callback-url/shareText?text=`文本`&deviceUUID=`你设备的 UUID`

文本的部分需要编码，当然，你也可以用 Launch Center Pro 来临时输入文本，因为 Launch Center Pro 会自动为编码，你会省下编码这一步。

和直接发送剪贴板内容一样，直接发送文本的操作也有相应的 x-callback-URL:

> command-c://x-callback-url/shareText?x-source=`SourceApp`&x-success={{`sourceapp`://}}&x-error={{`sourceapp`://}}&deviceUUID=`你设备的 UUID`&text=`文本`

两者的读法也没有什么区别。

### 3. 发送链接并在目标设备打开

这一步可以用 Handsoff 完成，所以我也并不使用，硬要用的话，可以把一些其它 App 的 URL Schemes 发送到其他设备，然后直接在目标设备执行操作。所以你甚至可以通过 Command-C，用 Mac 发送一些 URL Schemes 到 iOS 设备上，直接让相应的 App 执行动作。

发送链接并在目标设备打开的 URL Schemes 是：

> command-c://x-callback-url/shareAndOpenURL?url=`链接`&deviceUUID=`你设备的 UUID`

按照惯例，这里也有一个 x-callback-URL:

> command-c://x-callback-url/shareAndOpenURL?x-source=`SourceApp`&x-success={{`sourceapp`://}}&x-error={{`sourceapp`://}}&deviceUUID=`你设备的 UUID`&url=`{{http://}}`

同样格式的 URL 看三遍应该就看得懂了，如果看不懂，用最简单的那个试一下就能搞清楚。URL Schemes 这样的东西，都是跑一下就知道能不能行。不行了就排错，排完了就全明白了。

以上就是 Command-C 在 iOS 上的进阶用法，简单来说，就是活用几段格式一样的 URL Schemes，结合 Launch Center Pro 的 List 来做一个动作会更加高效。

Mac 上的进阶用法
----------

Command-C 在 Mac 上的进阶用法是利用对 AppleScript 和 x-callback-URL 的支持做一些东西，比如 Popclip 的插件、Alfred 的 Workflow 或是 Launcher 的 Action。但是如果是以效率而不是以折腾为目的的话，Alfred 的 Workflow 和 Launcher 的 Action 在这里是不必要的。因为 Command-C 的快捷键系统非常全面，可以先整体设置一个快捷键，然后用方向键选择设备：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/2B0D56AD-CA86-4F0C-A3E4-1971504E262F.jpg)

也可以直接给单个设备设置快捷键。

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/EE698ED5-188B-4C5B-B75D-DC8F7F13DE1D.jpg)

所以已经不需要再耗费时间专门为 Alfred 和 Launchbar 再做动作。这里主要介绍一下 Popclip 的插件，这个是与快捷键不同甚至比快捷键更快的方法。因为无论是快捷键还是 Alfred 和 Launchbar 的方法，都要先选中文字，再用快捷键复制，再用快捷键发送。但是，通过Command-C 的 Popclip 的插件可以做到选中一段文字，在弹出的菜单中选择自己的设备，然后直接发送出去。省去了**复制**这一步，并且考虑到你鼠标光标的位置离弹出菜单并不会太远，所以这个方法应该是最快的。

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/8B22582B-5391-472C-A861-AAE9BE0F5312.jpg)

[@饺子如何是好](http://weibo.com/u/3183472515) 曾经写了 Command-C 的 Popclip 的[插件](https://github.com/Howisdumpling/Popclip-Extension-for-Command-C-on-Mac)，并且写了[详细的教程](http://sspai.com/26154)。但是如前文所说，2.0 改变了定位设备的方法，所以原来的教程和插件需要进行稍微的修改才能使用。

### 自制 Popclip 插件

首先先下载我做好的[插件模板](http://cl.ly/e1n9/download/Command-C.popclipext.zip)。你要知道这个插件你是肯定要手动修改的，因为我们的设备数量未必相同，UUID 必定不同。所以这里没有近路了，下载完压缩文件，先不要安装，耐心地折腾一会儿，如果想只做到功能而不求甚解，那一点儿不难。想即弄清楚功能又搞懂原理，也不难。

这个[插件模板](http://cl.ly/e1n9/download/Command-C.popclipext.zip)对应了我的四个设备（如前文中的图例所示，有 iPhone, iPad Mini, iPad Pro 和 iMac），但一般来说大家设备不会这么多，所以我们先从修改设备数量说起。

#### 1. 单设备为 iPhone 的情况

**第一步：**解压缩文件，然后右键后缀名为 `popclipext` 的文件，选择「显示包内容」，再用 `Xcode` 打开 `Config.plist` 文件，展开所有层级，你应该看到的是：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/034A8B6F-8D4C-4984-8DE8-478EA0447658.jpg)

**第二步：** **不需要懂里面都是什么**，先把你没有的设备所在的 `item` 都删除了，比如你只有 iPhone，那你就把除了 `item 0` 以外的所有其它 `item` 都删了：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/05E9637F-87ED-4908-826D-2DAB68091520.jpg)

如果你只有一台设备，任务就算基本完成了，你现在可以双击 `popclipext` 文件安装插件，然后会看到这样的情况：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/F781A740-3310-4BC3-9308-CD528EFE2C1C.jpg)

你只需要**把你的 UUID 粘贴进去**，下次再选中文字，就会直接弹出一个 iPhone 的标志：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/F0DAF531-6CEE-4172-90B2-738101C56CDF.jpg)

选择这个 iPhone 标志，就能把内容发送到你的设备上啦。

总结起来总共只有两步：第一步，用 Xcode 打开文件；第二步，删了不带 iPhone 的 `item`。然后你就可以安装了，安装以后修改一下 UUID 就可以，就这么简单。

#### 2. 单设备，且模板里没有你的设备

现在让我们回到**第二步**，你发现了一个问题：你只有一个设备，但不是 iPhone，比如说是个 iPod Touch，咋办？

也不难。

这时候你要做的**第一步**：是把 `Config.plist` 里的 `iphone` 全改成 `ipodtouch`，而 `iPhone` 你可以改为 `iPod Touch`，注意两者有什么区别，改完以后大概是这样：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/7F3AD507-E427-4CFF-B2CC-1EE46D57AB10.jpg)

**第二步：**回到 `Config.plist` 所在的文件夹，你要把 `iphone.png` 改成 `ipodtouch.png`。

**第三步：**回到 `Config.plist` 所在的文件夹，把 `iphone.applescript` 改成 `ipodtouch.applescript`。

**第四步：**打开 `ipodtouch.applescript`，把里面的 `iphoneuuid` 改成 `ipodtouchuuid`。

然后你就可以关闭文件夹，双击 `popclipext` 文件安装插件，然后会看到熟悉的让你替换 UUID 的界面。

#### 3. 多设备，想搞懂原理

前面是为了让大家减少压力，快速上手，所以没有讲清楚。我觉得这种东西都是 Learning by doing, 一定要做，做着做着就明白了。在这一步我准备详细讲一下这个 Popclip 的插件是怎么做的，让大家对这个插件知其所以然。

**第一步**还是要下载模板压缩文件、解压缩然后右键「显示包内容」，但是现在我们要观察这个文件夹里的东西了：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/5E7B8E92-54B2-45E4-A057-A25EA43AACF9.jpg)

1. 图片：这些图片要是 `.png` 格式的，因为它们将会是每一个动作的图标，`.png` 格式的图片的特性是可以背景留白，你可以在 [Noun Project 的网站](https://thenounproject.com/)上找到高质量的图标。你也可以不用图片，这样动作将没有图标，相应位置会是个黑块儿。
2. AppleScript 文件：这里面就是一句 Command-C 的 Applescript 命令。
3. Config.plist 文件：它是 Popclip 插件的核心文件，事情都是在这里做的。

我们从 Config.plist 开始：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/54E79FA6-514C-4E1D-B486-079A219EE38C.jpg)

以发送剪贴板到 iPhone 的插件为例，我们需要在乎部分的有图上三个。

* 橙色部分有两个选项：
  + `Extension Name`: 这是这个插件的名字，最终会显示在 **Popclip 的下拉菜单里。**
  + `Extension Image File`: 这是这个插件的图标，图标文件放在**插件文件夹**中，最终显示在 **Popclip 的下拉菜单里**。
  + 这两个部分用我的模板就可以，**不用折腾**。
* 蓝色部分中，我们要在乎的有以下三个选项：
  + `AppleScript File`: 这项用于关联插件文件夹中的 Applescript 的文件，所以这里的名字和文件夹中相关的 Applescript 文件名一定要一致。
  + `Image File`: 这是此动作在弹出菜单中显示的**动作图标**，就是在选中文字后显示的设备图标，**跟上面的插件图标不同**。它后面的字符关联了文件夹中的图片文件，所以名字同样不能出错。
  + `Title`: 这是**动作名称**，在弹出菜单中，鼠标悬停在动作上就会看到看到该动作的名称。显示出来的就是后面的字符，以图中动作为例，显示出的将是 `Send to iPhone`。
* 红色部分其实是个可选项，它存在的价值在于让这个动作变得更灵活，我们稍后说 Apple Script 部分的时候会详细说明原因。在这部分，我们需要注意的只有三个选项：
  + `Option Default Value`: 这后面的字符储存的是该设备 UUID，但是这是可以在安装后随时改动的，所以并不用太介意。当然，在这里都改好的话，安装插件的时候比较省心。
  + `Option Identifier`: 这是这个动作的身份，和外面的 Applescript 文件相关。在蓝色部分指定的 Applescript 文件，在动作运行时会获取这个身份，然后再读取上面的 `Option Default Value`。
  + `Option Label`：这个是你在安装过动作后，让你修改 UUID 时显示出来的文字。

然后再看 Applescript 文件，以 `iphone.applescirpt` 为例，你如果打开它，会发现它非常简单，就是一句 Command-C 默认的：

```
tell application "Command-C"
    shareClipboard to "{popclip option iphoneuuid}"
end tell
```

关键在于花括号中的 `{popclip option iphoneuuid}`，这里面的这个 `iphoneuuid`，就是我们前面在红色部分中设定好的`Option Identifier` 的字符。而它的默认值，`Option Default Value`，也就是 `63BDD57E-5F25-4C97-83F8-F4BB80FF0CD2`这一串字符。

它工作的方式就是，每当运行这个动作，`iphone.applescript` 文件会先去找 `Option Identifier` 的字符，找到是`iphoneuuid` 以后，会继续找它的默认值 `Option Default Value`，最后读取出 `63BDD57E-5F25-4C97-83F8-F4BB80FF0CD2`，也就是我 iPhone 的 UUID。

所以这里可以解释前面为什么说红色的部分不是必要的了，因为这个部分整个是为了你日后便于修改设备的 UUID 的，所以它把 UUID 设为了一个变量，你随时可以修改：

![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/EBA0BA22-3074-423B-A6D8-50FB98239413.jpg)

尤其是当你要把设备分享给别人的时候，为了方便，可以让对方直接在安装后就修改 UUID 来使用。

但如果你是自用，那么完全可以把红色部分全部删除，然后在 `AppleScirpt` 文件中，把 UUID 写死，给对应的设备写上对应的 UUID，比如我的 iPhone，就可以写成：

```
tell application "Command-C"
    shareClipboard to "63BDD57E-5F25-4C97-83F8-F4BB80FF0CD2"
end tell
```

那么整个动作就会简单一大半儿了。

现在，你应该会读模板了，也应该知道要修改模板的哪里来制作自己的动作了，相信不管是一个还是多个设备，做 Command-C 的 Popclip 的插件从此就难不住你了。

1. 基本 URL Schemes 就是打开 App 的 URL Schemes。详细介绍见：[URL Schemes 使用详解的基本 URL Schemes 部分](http://sspai.com/31500#04)。 [↩︎](http://sspai.com/32293#ffn1)
2. UUID 是在电子设备中很常见的概念，它是 Universally Unique Identifier 的缩写，中文翻译是通用唯一识别码。简单说，就是硬件或者软件为确定设备使用的一个名字，保证这个设备不会和其他设备重名。 [↩︎](http://sspai.com/32293#ffn2)
3. 从 iOS 发送到 Mac 理论上是不会失败的，但是 iOS 之间和 Mac 传输到 iOS 是有失败的可能的，这要看 iOS 是否因超时或者内存不足而中止了 Command-C，如果失败，只要在 iOS 上临时再打开就好。当然，如果你有清后台的习惯，就是每次你都要把所有的 App 都退出才安心。那么你每次用 Command-C 都要重新打开它一次。所以清后台是个很落后的习惯。 [↩︎](http://sspai.com/32293#ffn3)

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[剪贴板传输工具 Command-C 进阶用法](http://sspai.com/32293)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/08D4D358-AAA3-404F-AC5B-2A2892CFE96E/76420E44-7276-412E-A72F-C3EE333D4D66.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:gif/destination:http%3A%2F%2Fwww.apple.com%2Fcn%2Fgifts%2Ffor-gamers%2F)

---

[🌐 原始链接](http://sspai.com/32293)

[📎 在印象笔记中打开](evernote:///view/207087/s1/9a6ea490-9b5c-4752-8587-16b26c41c470/9a6ea490-9b5c-4752-8587-16b26c41c470/)