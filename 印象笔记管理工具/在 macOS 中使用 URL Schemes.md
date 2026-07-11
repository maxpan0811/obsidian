# 在 macOS 中使用 URL Schemes

---

在 macOS 中使用 URL Schemes
=======================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

在 iOS 上如果想完成一些跨 App 的自动化流程，可以使用 URL Schemes。随着 iOS 13 的发布，[新的系统级的快捷指令](https://developer.apple.com/siri/) 和 [SiriKit](https://developer.apple.com/documentation/sirikit) 变得前所未有的强大，但是 URL Schemes 的影响是不可磨灭的：一方面即使是使用快捷指令，也会时不时用到 URL Schemes；另一方面大部分 Power User 都会使用它，他们在处理自身的需求时首先想到的工具很可能也是它，URL Schemes 依旧是 Power User 的基础课，也依旧是判断一个 App 是否优秀的重要标准之一。

iOS 上 URL Schemes 能做什么和怎么用可以参考 [Hum](https://sspai.com/user/681230/updates) 的《[URL Schemes 使用详解](https://sspai.com/post/31500)》和《[入门 iOS 自动化：读懂 URL Schemes](https://sspai.com/post/44591)》这两篇文章。

而 macOS 上自动化手段和工具非常多，不是专业的效率 App 也可以通过支持 macOS 的自动化框架或命令行工具来提升自己的可自动化程度。尽管如此，许多 App 在 macOS 还是开发了对 URL Schemes 的支持，一是 iOS 平台的用户习惯影响深远；二是 URL Schemes 有其不可替代的使用场景。随着 Project Catalyst 的发布，macOS 将来会有越来越多的从 iPadOS 上移植来的 App，这些移植来的 iPad App 的 URL Schemes 依旧能在 macOS 上发光发热。

如何在 macOS 上使用 URL Schemes
-------------------------

URL Schemes 的用途主要有两个：

1. 在不同的 App 之间跳转，简化操作；
2. 将不同的应用串联起来，完成自动化流程。

在 iOS 平台上，常见的 URL Schemes 的用法有：

1. 直接在 Safari 地址栏中输入后跳转；
2. 点击一个指向 URL Schemes 的超链接；
3. 在 [Launch Center Pro](https://itunes.apple.com/us/app/launch-center-pro/id532016360?mt=8) 或 [Pin](https://itunes.apple.com/cn/app/pin-%E5%89%AA%E8%B4%B4%E6%9D%BF%E6%89%A9%E5%B1%95/id1039643846?mt=8) 这种启动器 App 中打开；
4. 在一段[快捷指令流程](https://support.apple.com/zh-cn/guide/shortcuts/welcome/ios)或一段 [JSBox 脚本](https://docs.xteko.com/#/README)、[Drafts Action](https://getdrafts.com/actions/) 中唤起。

在 macOS 平台上，URL Schemes 的用法与 iOS 基本相似，因为 URL Schemes 在 iOS 上的影响力远大于 macOS，所以接下来将会把 iOS 上的使用场景来与 macOS 上进行对比。

### 直接运行，用于快速跳转

在 Safari 地址栏中直接输入一段 URL Schemes 然后回车运行其实不是其最典型的使用场景，但是却是最直观的用法。

在编写一段 URL Schemes 免不了进行各种测试，在这个时候，相比较于 Safari 的地址栏，我更喜欢使用 LaunchBar 的链接模式，因为 LaunchBar  
无处不在，在任何地方都可以调出。调出 LaunchBar 后按 `⌘Command-L` 或 `.` 就会进入链接模式，然后通过 LaunchBar 唤起测试的 URL Schemes：

![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/13924290-EB60-426A-B20E-E200FB0E0CC4.png)

使用 LaunchBar 打开 URL Schemes

如果你是使用的 Alfred 则可以直接输入 URL Schemes：

![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/65A1503A-6C3F-4F9D-A91A-A4D83510D25E.png)

用 Alfred 打开 URL

上图中的 LaunchBar 部分：

```
x-fantastical2-register://oscarbulabula/ZHE-SHI-WO-XIA-BIAN-DE-YI-CHUAN-XU-LIE-HAO
```

是一段用于激活 Fantastical 2 的 URL Schemes，执行后 macOS 就会寻着协议名 `x-fantastical2-register` 找到 Fantastical，链接的后续部分包含了授权信息，Fantastical 处理后会完成激活操作。

在 iOS 上使用 URL Schemes 如果仅仅是启动某个 App，意义其实有限，所以我们一般是使用他们来打开一个特定视图或进入某个功能。在 macOS 也是类似的，如果仅仅是启动一个 App，何苦费力使用 URL Schemes，用 LaunchPad 或启动器要快的多。把具有特殊功能的 URL Schemes 放到自己熟悉的便于访问的位置才能最大化其效用。

我制作了一个 Keyboard Maestro [palette](https://wiki.keyboardmaestro.com/manual/Palettes) (指令面板)，包含了我在 Mac 上常用的一些有特定功能的 URL Schemes：

![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/B7A0448D-A6E8-436B-A62E-3C66314CFAF0.png)

包含了一些有特定功能的 URL Schemes 的 Keyboard Maestro palette

其分别是：

* 打开 Telegram 中的 Saved Message，即云存储界面，链接为：`tg://resolve?domain=ogeveryday`，其中 `ogeveryday` 是我的 Telegram 用户名
* 打开 2Do 中名为 Computer 的清单：

  ```
  twodo://x-callback-url/showList?name=Computer
  ```
* 打开 Spotify 中我收集的用于专注工作的歌单；
* 打开 Chrome 的 [OneTab](https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall) 插件的管理界面： 1

  ```
  chrome-extension://chphlpgkkbolifaimnlloiipkdnihall/onetab.html
  ```
* 打开 DEVONthink 中我的正则表达式的笔记：

  ```
  x-devonthink-item://63C03477-3CAC-4272-BD85-547A0707FBE4
  ```

契丹神童使用 LaunchBar 做了类似的事情，可以调用 OmniFocus 的各个功能，对应制作方法可以参考这篇文章：《[用 LaunchBar 调用 URL Schemess，直达 OmniFocus 的各个角落](https://sspai.com/post/41352)》

### 制作成超链接，串联不同 App

制作成超链接就是把一段 URL Schemes 放到文字里，如 [这个](https://sspai.com/post/55130mailto:feedback@sspai.com?subject=Test&body=Body%20text) 链接，其背后是：

```
mailto:feedback@sspai.com?subject=Test&body=Body%20text
```

这是一个 Email 链接，点击后系统就会调用邮件客户端撰写一个新的草稿 —— 收件人是「feedback@sspai.com」，标题是「test」，正文是「Body test」。

正如上文中所提到的，macOS 中的自动化手段非常多，我个人认为使用超链接唤起 URL Schemes 才是其在 macOS 平台上真正发光的 niche (称心的场景；合适的工作)。但凡是讨好进阶用户的 App，一般对自动化都十分友好，有各种各样的方法可以实现自身的需求，但是部分面向大众市场的 App 其自动化做的并不好，但是即使再不好，也是支持超链接的，所以有时我就会请出 URL Schemes 来达到我的目的。

在我的各种笔记中时常会遇到生词，直接在笔记的行文内详尽的记录其释意会导喧宾夺主，另一方面我也不愿舍弃我在[欧路词典](https://www.eudic.net/)中有的完整的生词学习方案。所以我会把对应词汇的 URL Schemes，如 `eudic://dict/example`，制作成超链接置于笔记中，点击单词直接跳转到欧路词典中的对应词条。2 

同样是记笔记时，有时我需要其他的的文档做参考，但是因为文件体积过大或其他顾虑，我并不想将这个文档导入至笔记中。Evernote 和 Ulysses 都不支持引用外部文件，二者对本地的文件路径：

```
/Users/Oscar/Downloads/JavaScript.pdf
```

或标准的文件 URI：

```
file://Users/Oscar/Downloads/JavaScript设计模式.pdf
```

处理的也不好。对于这种需求的处理方式是将文档存入 DEVONthink 中，然后将其 Item Link (形如：`x-devonthink-item://63EBF491-E901-458A-AB19-E580922AE2C1`) 放到关键词后。3 （后文进阶篇会介绍另一种处理方式。）

### 放在效率软件中

上面一种使用场景中有一个限制：URL Schemes 一旦制作好了便无法修改，也就是不能传入参数。在 iOS 上使用 Launch Center Pro 时可以用 [`[prompt]`](https://help.contrast.co/hc/en-us/articles/201915128-Input-Tags#prompt) 作为占位符，在每次运行时都可以导入不同的参数，在 macOS 中借助效率工具也可达到一样的效果。

最简单的方法就是使用 LaunchBar。以前面提到的欧陆词典为例，在 LaunchBar Index 中新建一个编码为 `Unicode UTF-8` 的 Search Template (搜索模板): `eudic://dict/*` 便完成了。

iOS 上有快捷指令，macOS 上有 [Keyboard Maestro](https://www.keyboardmaestro.com/)。作为最完备的 macOS 上的自动化工具，Keyboard Maestro 有着一系列处理 URL Schemes 的 Action (动作)，稍微复杂的需求自然要请出来他。

我的需求为：自动获取网页的标题和链接，添加新的任务至 Things 的「RSS Item」项目中。参考 Things 3 URL Schemes 的 [官方文档](https://support.culturedcode.com/customer/en/portal/articles/2803573)，使用 Keyboard Maestro 可以制作出 Macro：

![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/38EAAB77-F02A-4999-880F-70E8D0C04358.png)

这个 Macro 只需要两个 Actions 即可完成：

1. 第一个动作中包含的链接：

   ```
   things:///add?title=%ChromeTitle%&notes=%ChromeURL%&list=RSS Item
   ```

   就是查阅文档后按照「add」部分编写都 URL Scheme，其中 `%ChromeURL%` 和 `%ChromeTitle%` 都是 Keyboard Maestro 的 [Token](https://wiki.keyboardmaestro.com/Tokens)，也就是占位符，Keyboard Maestro 在执行到这个动作时会将二者分别替换为 Chrome 当前标签页的 URL 和标题。
2. 随后第一个 Action 会将得到的链接进行 [URL Encode](https://zh.wikipedia.org/zh-hans/%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81) (百分号编码), 也就是处理成格式标准的 URL Schemes。
3. 百分号编码过的 URL Schemes 会储存到变量 `URL` 中。
4. 第二个动作是使用默认程序打开变量 `URL` 中的链接。

如果想完善一些可以如添加激活时发出音效，完成后给出通知，最后销毁变量等 Action。效果如下，可以看到 Marco 运行后，Things 添加了一个新的任务到「RSS Item」项目中，任务名为当前 Chrome 的标签页的标题「Hacker News」，任务备注为其地址「https://news.ycombinator.com」。

### 放在脚本中

如果你足够「Pro」，习惯自己编写各种脚本，得益于 macOS 宽松的环境，URL Schemes 可以方便的融合至各种脚本中。

AppleScript，不用仔细说，一看就懂:

```
set theURL to "someApp://someaction"

open location theURL
```

Command line ：

```
 open 'someApp://someaction'
```

[`open`](https://ss64.com/osx/open.html) 是 macOS 独有的（相较于其他 \*nix）命令行工具，它发扬了很多 macOS 的特性，它可以打开文件或链接。`open` 的处理逻辑是与 macOS 的 [LaunchServices](https://developer.apple.com/documentation/coreservices/launch_services) 保持一致的， `-a` 可以通过名称指定处理的 App，`-g` 可以在后台打开，详情可以参考[文档](https://ss64.com/osx/open.html)。

macOS 上怎么找 URL Schemes？
-----------------------

在 macOS 上的 Apple Script 可以直接在 Script Editor 里查看字典获得，但是很不幸，与 iOS 上的 URL Schemes 现状差不多，macOS 上也没有一套统一的方法查询 URL Schemes，只能不厌其烦的 Google「App 名 URL Schemes」来获得。

URL Schemes 中占很大比例的一种是引用性质的，就是获得一篇文章、一份笔记、一个任务或一个事件等独一无二的链接，点击后就会直接导向这个对象。这类 URL Schemes 虽然在不同的 App 内名字不一样，但是获得方法基本上是一样的：

* 按住 `⌥Option` 在 Ulysses 的 Sheet 或 Library 上右键点按可获得「Callback URL」；

  ![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/30437418-2628-47D0-8AD5-5D519E01974B.png)

  Ulysses URL Schemes
* 在 DEVONthink 的文件上右键点按可获得「Item Link」；

  ![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/EE42F290-1A37-46F4-99A2-8682840C5BD8.png)

  DEVONthink Item Link
* 按住 `⌥Option` 在 Evernote 的笔记上右键点按可获得「Classic Note Link」；

  ![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/953504D1-C62B-4786-9DDE-D2FAE0ED4F14.jpg)

  Evernote Classic Link
* 按住 `⌥Option` 在 2Do 的任务上右键点按可获得「Shareable Link」；
* ……

其余的就只能自己搜索官方文档来自己摸索了。

进阶：制作自己的 URL Schemes
--------------------

对于刁钻的用户（如我）来说，这些还不够，在一些情况下我们可以制作自己的 URL Schemes。通过 Script Editor 或 Keyboard Maestro 都可以制作出自己的 URL Schemes。

### 使用 Script Editor

基本原理是：当一个软件被注册到 [LaunchServices](https://developer.apple.com/documentation/coreservices/launch_services)（通常是在 Finder 中查看 App 所在文件夹时），[LaunchServices](https://developer.apple.com/documentation/coreservices/launch_services) 会读取其 (info.plist 中) 声明的所支持的 URL 协议、文件类型以及 MIME 类型等信息并记录下来。在遇到这个记录的 URL 协议时就会传给这个 App 处理。一般这种程序被叫做 helper。

我们只要在 Script Editor 中将 Apple Script 代码保存为 Application 类型，然后修改其 Info.plist，在其中声明所能处理的 URL 类型，随后 LaunchServices  就会将我们的 App 记录在案。

#### 制作 App 并登记到 LaunchServices

打开 Script Editor，新建一个文档。要响应接受到的 URL Schemes，Apple Script 中必须要包含处理 `open location` 事件的代码：

```
on open location this_URL
```

然后测试一下，通过 `display dialog` 查看从 URL 传递来的参数：

```
display dialog "this URL: " & this_URL
```

在保存时 File Format 选择为 Application 类型，在右侧边栏里的 `BundleIdentifier` 中起一个名字：`org.oscar.opener`。然后点击小齿轮，选择在 Finder 中查看。

用文本编辑器修改 Info.plist 文件，添加下面字段并保存（注意复制完整）：

```
<key>CFBundleURLTypes</key>
<array>
	<dict>
		<key>CFBundleURLName</key>
		<string>Open File</string>
		<key>CFBundleURLSchemes</key>
		<array>
			<string>opener</string>
		</array>
	</dict>
</array>
```

如果按照我的写法，相当于告诉 macOS 将所有以 `opener://` 开头的名为 Open File 的 URL 全部交给 `org.oscar.opener` 也就是刚刚创建的这个 App 来处理。

现在要把他登记到 LaunchServices，最简单的方法是直接 `Command + O` 运行一下。登记完成后，使用 LaunchBar 打开一段 URL（⌘ L）试一下，可以看到已经成功了。我们的 App 显示出了传入的参数：`opener://OCR.py`

![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/E98DB730-598F-4A73-B0B5-41F3ED2F1140.png)

#### 解析处理参数

能够正确收到参数以后，下一步是解析参数。

在上文使用场景 — 制作成超链接中提到的需求，现在现在我们可以做一个小程序辅助解决这个问题。这么做还有一个好处是可以让 MAS App 绕过沙盒限制，不跳出 App 引用外部的文件。

假设一次只打开一个文件，即只传入一个参数：

```
set x to the offset of "://" in this_URL
-- 找到「://」位置并记录到变量 x 中

set the argument_string to text from (x + 3) to -1 of this_URL

-- 把 URL 中「://」后的所有字符保存为变量 argument_string
```

然后把获得的参数做一下 URL Decode 处理，把 POSIX 路径转换为 Apple Script 对象，最后使用 Finder 打开即可：

```
on open location this_URL
	
	set x to the offset of "://" in this_URL
	set the argument_string to text from (x + 3) to -1 of this_URL
	set decodedPath to urldecode(argument_string)
	
	set f to POSIX file decodedPath
	tell application "Finder" to open f
end open location
```

现在这个自定义 URL Scheme 就完成了。在 Ulysses 中添加 URL：

```
opener:///Users/Oscar/Desktop/Apple Script/1.png
```

点击后，macOS 会调用刚刚制作好的程序处理，引导 Finder 打开对应的文件。

效果如下：

你可以在 [这里](https://cl.ly/rEEp) 下载 opener.app。

不过这种制作方式也有弊端：Dock 上会有一个图标跳一下，下面介绍的方式可以避开这个问题。

### 使用 Keyboard Maestro

Keyboard Maestro 中所有的 Marco 除了指定的[触发方式](https://wiki.keyboardmaestro.com/Triggers)（最常见的是快捷键）之外，都可以通过 Scripts 或 URL Scheme 与 Keyboard Maestro 互动后触发。见 ：[trigger:Script](https://wiki.keyboardmaestro.com/trigger/Script) 和 [trigger:URL](https://wiki.keyboardmaestro.com/trigger/URL)，其中的 URL Trigger 是可以无限传参的！

Marco 的 URL Trigger 基本格式是可以是下面的任意一种：

* ```
   kmtrigger://macro=Prompt%20With%20List%20%40TEST&value=MyTriggerValue
  ```
* ```
   kmtrigger://macro=984A3DBF-5B70-4031-979F-5AD44E3B24A5&value=MyTriggerValue
  ```

也就是可以分别通过 Marco 名或 Marco 标识号来制作独一无二的 URL Scheme。

了解了原理后现在来解决一个实际的问题。在我的电脑上，不知道什么原因 Chrome 访问京东特别慢，一是加载慢，二是滑动也慢，但是 Safari 却没有这个问题，发现自己无法排除这个问题之后，我决定以后都用 Safari 访问京东。

一般来说访问京东不会是从其首页开始的，我都是直接使用 LaunchBar 直接搜索京东。 虽说可以制作一个 LaunchBar Action，通过这个 Action 调用 Safari，但是这里我使用 Keyboard Maestro。成品 Marco 如下图：

![](.evernote-content/835988B7-3BFC-4B80-A2EA-74B940A64DC7/CEF50BC4-87FC-4728-9504-DE1C3712BA83.jpg)

成品 Marco

这个 Marco 的处理流程是：

1. `%TriggerValue%` 在上文中提到了，是占位符，不过这里这个占位符在运行时会被替换成 [Marco 的触发值](https://wiki.keyboardmaestro.com/token/TriggerValue)，也就是 value 后等号后的字符串。
2. 随后会对这个字符串会进行百分号编码。编码后的结果会存到 Keyboard Maestro 变量 `SearchKeyword` 里。
3. 随后 Keyboard Maestro 会处理

   ```
   http://search.jd.com/Search?keyword=%Variable%SearchKeyword%&enc=utf-8&area=1
   ```

   这个 URL，把其中的 `%Variable%SearchKeyword%` 替换为变量值，也就是编码后的搜索关键词。
4. 最后 Keyboard Maestro 会调用 Safari 打开这个最终的 URL。
5. 清除变量。

这样 Keyboard Maestro 端的编写就完成了。点击「Or by script」下拉框，复制出「Or by URL」后的对应的 URL Schemes：

```
kmtrigger://macro=JD%20in%20Safari&value=Whatever
```

等号后替换成 LaunchBar 使用的占位符 `*` 就可以填到 LaunchBar 的自定义搜索模板里了。

最后效果如下：

结语
--

形如 `file:///home/username/sspai.pdf` 或 `https://sspai.com` 的这种由协议名、冒号、斜线和一串字母组成的链接叫做 [URI（统一资源标识符）](https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E6%A0%87%E5%BF%97%E7%AC%A6)，其本被设计为可用于定位资源或文件。而 URL Schemes 是 URI 的一个子集。

在 iOS 开发中，为了给开发者提供一个可以跳出沙盒的限制，从而在 App 外部引用 App 内资源的方法，[iOS 系统允许](https://developer.apple.com/documentation/uikit/core_app/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app?language=objc)开发者声明一个 Handler (处理程序) 处理特定的 URL Schemes (URL 方案)，从而实现功能如：

* 用户点击 Email 中的一个链接后，启动 App 同时进入特定的视图；
* App 运行一段 URL 后，触发其他的 App 的特定功能，如一个 App 调用支付宝完成付款。

URL Schemes 设计之初的本意并不是服务于自动化，只是囿于 iOS 的沙盒设计的限制，被聪明的开发者开拓出了自动化的用法。随着技术和平台的演进，一部分 iOS App 开始使用 [Universal Link](https://developer.apple.com/documentation/uikit/core_app/allowing_apps_and_websites_to_link_to_your_content?language=objc) 引用资源和内容；还有一部分转向了使用基于后端服务器的 API（应用程序接口）。不过 URL Schemes 在自动化方面的用法和习俗一直被保留了下来。

虽然可选择的其他自动化手段很多，URL Schemes 在 macOS 上依旧有其独到的使用之处。

通过最简单的直接运行的方式可以快速跳转到 App 特定功能中；制作成超链接则可以连接不同的 App；结合如 Keyboard Maestro 这种效率软件运行则可大大扩展其使用场景。最后，如果你的需求十分小众，自己定制一份 URL Schemes 也是可行的。

参考链接
----

1. [AppleScript: Launching Scripts From Links](http://www.macosautomation.com/applescript/linktrigger/index.html)
2. [Launching External Applications using Custom Protocols under OSX – Shotgun Support](https://support.shotgunsoftware.com/hc/en-us/community/posts/209485898-Launching-External-Applications-using-Custom-Protocols-under-OSX)
3. [在 macOS 中制作自己的 URL Schemes](https://sspai.com/post/44425)

1. [因为 Chrome 并没有在 macOS 中注册 URL handle，所以这个 macro 后续中设置为该 URL 指定通过 Chrome 打开。↩](#)
2. [我固然可以制作一个 Keyboard Maestro 的 Macro 来完成这个需求（事实上我也做了: https://cl.ly/26e27615e52f ），但是一是每次都要想办法唤起一个 Macro 太麻烦，二是欧陆词典的 URL Schemes iOS 和 macOS 是保持一致的，macOS 上编写的在 iOS 上也可以使用。↩](#)
3. [你可能会需要这个 Marco: https://cl.ly/40719e9d7047 使用时先将 URL Schemes 复制到剪贴板中，选中文字后执行。↩](#)

---

[🌐 原始链接](https://sspai.com/post/55130)

[📎 在印象笔记中打开](evernote:///view/207087/s1/36d30258-6bd2-4aa7-93bf-864467d0ced9/36d30258-6bd2-4aa7-93bf-864467d0ced9/)