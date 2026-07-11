---
title: AppleScript 入门：macOS 的台本
type: source
created: 2026-07-09
updated: 2026-07-09
source_path: 印象笔记管理工具/AppleScript 入门：macOS 的台本.md
tags: [印象笔记]
---

# AppleScript 入门：macOS 的台本

---

AppleScript 入门：macOS 的台本
========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

说起 macOS 上的自动化，我们可能可以想到不少知名的软件。然而，这些效率应用几乎无可避免地需要 macOS 原生脚本语言 AppleScript 的助力。事实上，许多第三方应用，可能只是把写好的 AppleScript 包装成一个按钮或一个快捷键。

除此之外，如果我们需要的某个功能，软件本身并没有提供给。我们也可以通过 AppleScript，在这些应用的基础上去自定义一些新功能。

AppleScript 被称为脚本「语言」，让不少本该掌握它的用户望而却步。但实际上，相较于其他脚本语言，它十分简单易学 —— 它涉及的知识点最少、语法也比较灵活，除此之外它最好的一点是所有资料都在 Mac 中预设好了，我们可以随用随查。

这篇文章，是一篇带领你入门 AppleScript 的文章，我们将先从它是什么说起，再谈谈如何去根据 Mac 中预设的文档，写出自己需要的脚本。

希望我可以解除你对 AppleScript 这一「语言」的畏惧，释放你 Mac 的自动化能力。

什么是 AppleScript？
----------------

AppleScript 这个词我们可以分解来看：

Apple，好理解，一看就表明是苹果自家的东西。

Script 呢？查词典的话 Script 的意思是「演员的台本、脚本」。按时间顺序，在什么场景下，使用什么道具，用什么神情和姿态去演绎什么台词，这些都可以是脚本的内容。

在计算机中，Script 则表示一类编程语言，称为「脚本语言」。脚本语言沿用了演员台本的基本特征。只不过这回计算机变成了演员，我们则成了编剧，你可以利用脚本语言告诉计算机，按时间顺序，在什么场景下，用什么姿态，做什么事。

脚本语言有很多种，你可能听说过的 Shell Script、Python 和 JavaScript，都是其中的代表。而 AppleScript 则是 macOS 下提供的系统级别的脚本语言。和前面几个相比，它出奇的简单，因为它：

1. **语法简单，并接近自然语言**：几乎没有标点符号，语法不像其他语言那样严格 1 ；
2. **语法查询十分方便**：系统原生提供 AppleScript 语法查询词典，支持关键词查询。

我们可以来看一个例子：往 OmniFocus 的购物清单里添加三项内容，鸡蛋、牛奶、面包，这个需求实际上是我和 macOS 的对话：

> 我：「你好 macOS，请添加几项内容到我 OmniFocus 的「购物清单」里！」
>
> macOS：「好的，您要添加哪些内容？」（弹出输入框）
>
> 我：「鸡蛋（换行）牛奶（换行）面包（回车）」
>
> macOS：（弹出通知）「已帮您添加 3 项内容到 OmniFocus 的「购物清单」！比心心！」

我们理解了这种逻辑，并按这种逻辑写好脚本，macOS 就会有条不紊地一句一句去演绎。

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/DDC5F763-752E-48E6-9D8B-D864BF2D013A.png)

用 AppleScript 让 Mac 去执行任务

我使用 AppleScript 的情境
-------------------

现在人们在电脑上办公学习的比重越来越大，如果你仔细体会可能会发现，有时自己会重复地进行同一个（或一系列）操作。如果这些单调费时的重复性操作让你十分抓狂，那么你就可以利用 AppleScript，让系统为你代劳。

拿我的使用场景举例的话，按使用频率粗略可分为以下三个使用 AppleScript 的情境：

1. **写入内容**：比如向 OmniFocus 收件箱添加一个项目，并对其设置项目名称，过期日期，标签等，而不需要打开 OmniFocus 应用本身；
2. **再软件间传输数据**：比如从邮件客户端抓取邮件内容到 OmniFocus；
3. **代替键鼠操作**：可以代替一些固定的键盘鼠标操作。

知道了它的使用情境后，我们来从易到难地，看看 AppleScript 的语法。

AppleScript 基础语法
----------------

作为入门级内容，本文不会全面介绍 AppleScript 语法，否则就成 Documentation 了。所以只列举出我最常用的几种，它们已经可以满足你的绝大多数需求。

### 告诉 xxx 做某事

AppleScript 的语法非常接近自然语言，希望一个应用（application）做某件事，只要直接「告诉」它就好了。

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/7B0611CD-4611-4002-898A-BCA247E8E975.png)

AppleScript 的语法结构

具体的例子：启动 Safari

```
tell application "Safari"
    activate
end tell 
```

「告诉 Safari 启动」，这是不是很接近英语的表达？

告诉 xxx 做某事具有俄罗斯套娃的结构，如果你要具体到 Safari 的当前页面，那么就要访问它的 `front document`（最前面的页面），代码上就是在 `tell application "Safari"` 结构里再嵌入一个 `tell front document`

```
tell application "Safari"
    tell front document
        -- 你希望应用 Safari 的当前页面做的事
        -- 比如获得当前页面的网页标题，直接用 name 就行
        name
    end tell
end tell
```

这里的 `activate` 和 `name` 分别是 AppleScript suite 里的类（command）和类的属性（property）。现在不理解别担心，下一节会专门介绍什么是 AppleScript suite，以及如何使用它。

以此类推，你可以无限 `tell` 下去，

```
tell application "Safari"
    tell front document
        tell something
            tell something
                tell something
                    -- macOS：你够了！
                end tell
            end tell
        end tell
    end tell
end tell
```

### 定义一个变量

```
set <变量名> to <类名称>
```

比如你想把剪贴板的内容放进一个变量中，方便后续使用，你可以这样做

```
set 我的变量 to clipboard
```

其中 `clipboard` 是 Standard suite 里提供的代表剪贴板的类。

或者，

```
tell application "Safari"
    tell front document
        set 标题 to name
    end tell
end tell
```

这段脚本把 Safari 当前页面的标题存入了名为「标题」的变量中。

至此相信你已经对 AppleScript 的语法，以及里面的「变量」、「类」等概念有了个简单的印象，不用追求完全理解，你只要能看懂最后一个例子就好。我们的认识会在学习和使用中逐步加深。

### 模拟键盘操作

模拟键盘操作是 AppleScript 的另一个特长，有两条命令可用于模拟键盘操作：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/8FDAB23B-7BE5-4E94-82ED-09B4F3B2C484.png)

同于模拟键盘操作的两条命令

1. `keystroke`: 主要用于输入一串任意字符，非 ASCII 字符也可以。  
   比如，

   ```
   keystroke "少数派"
   ```

   只要执行这段命令，系统就会直接键入「少数派」这一串字符。
2. `key code <code>`：主要用于单键模拟，适用于键盘上的任意按键，例如像 esc 这样的非字符按键，

   ```
   key code 53
   ```

   其中 `53` 是 esc 键的键位编码，完整的键位编码你可以在 [这里](https://eastmanreference.com/complete-list-of-applescript-key-codes/)找到。

此外 `key code` 还可以用来搭配修饰键 2 使用，像这样

```
key code 9 using {command down}
```

其中 9 是 `V` 键的键位编码，所以上面这条命令就模拟了粘贴快捷键 `⌘Command - V`。

注：键入操作必需在 System Events 内进行，比如我们要模拟敲 esc 的话，要这么写：

```
    tell application "System Events"
        key code 53
    end tell
```

### 模拟「鼠标」操作

这一小节与其说是介绍模拟「鼠标」操作，倒不如说是模拟「点击」操作。想想最原始的鼠标使用，无非就是「移动指针」和「点击」两种操作，「移动指针」也是为了移动鼠标到一个可点击区域，进行「点击」。

作为键盘党，鼠标可以「移动指针」的特性让我既爱又恨，爱它是因为它十分直观，恨的却是它效率的低下。试想如果我们无需移动鼠标，直接实现「点击」操作，那该有多棒！

而通过 AppleScript，就可以在**不需要「移动指针」的情况下实现「点击」操作**。

简单来介绍一下它的原理。一个运行中的系统界面下会存在很多个支持点击的界面元素，比如各式各样的按钮，还有许许多多的菜单项等等。系统会通过不同的「编号 xxx」来区分它们，避免混淆。因此我们就可以通过两个方式来点击它们：

1. 利用鼠标指针移动，进行点击操作；
2. 直接告诉电脑「请点击编号为 xxx 的 UI 元素」。

我们要通过 AppleScript 实现的，就是第二种方法。

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/B7C443AD-EA4D-4618-A8F5-37A158326585.png)

图形用户界面中的一些 UI 元素

下图演示了，一个无需利用鼠标，就能「点击」Finder 中的分享按钮中的 AirDrop 菜单项的效果（为了展示我没有通过移动鼠标点击，我不断地晃动我的鼠标，但你可以看到系统没有通过鼠标就完成了「通过 Airdrop 分享」的操作）：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/EA5FC19E-759A-4AF3-90BC-B3D03A9579CB.gif)

模拟点击

这样通过 AppleScript 来模拟「点击」操作专业术语叫做 GUI Scripting（图形用户界面脚本编写），再我之前的一篇文章《[手把手教你用 AppleScript 模拟鼠标键盘操作，实现 macOS 系统的自动化操作](https://sspai.com/post/43758)》中有更详细的说明。

### 小憩片刻

再运行 AppleScript 时，尤其是模拟键鼠操作时候，经常需要等待一个应用被打开、一个窗口弹出才能继续执行下一步操作，那就需要让运行中的脚本暂停片刻，用 `delay <秒数>` 命令就好，

```
delay 0.5   -- 暂停 0.5 秒
```

### 注释

在代码中插入一些不会被执行的注释用于解释代码内容，可以让别人（和自己）看自己写的代码时更好懂。AppleScript 中凡是双短线 `--` 和井号 `#` 后的内容都会被认为是注释，不会被执行。

```
    -- 这是一条注释
    # 这也是一条注释
```

AppleScript Suite
-----------------

接下来，我们要提高一些难度，来了解一下 AppleScript Suite。搞明白了它，在结合前面说明过的那些基础规则，我们就可以针对不同的软件，编写更复杂的脚本。

AppleScript Suite3 ，就是 AppleScript 类（class），及其元素（element）和属性（property）的集合。

一个类，可以是一个数据，比如 Safari HTML 文档（`document`）；也可以是一个函数，帮你完成一个特定功能，比如往 OmniFocus 里添加任务这个动作（`parse tasks into`）。

一个类中可能包含元素和属性，比如 `name` 是 `document` 的一个属性，代表 `document` 的名称。

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/587D3633-B5D3-4DDA-B73A-1B1539B9785A.png)

OmniFocus 中的「类」

**Suite 是按应用来分类的**

1. **Safari suite**：「Safari 浏览器」提供给你的 AppleScript 类的集合，只适用于「Safari 浏览器」；
2. **Finder suite**：「访达」提供的 AppleScript 类的集合，只适用于「访达」；
3. …

此外，你还能找到一个 Standard suite（标准脚本套件），它是系统的全局脚本套件，不局限于单个应用，可在任意场景下使用。

### 在哪里可以找到 AppleScript Suite 呢？

1. **系统原生的脚本词典**：打开「脚本编辑器」 → 新建一个脚本 → 用快捷键 ⌘⇧O 打开 AppleScript 字典（Dictionary），在这里你可以看到你 Mac 上所有支持 AppleScript 的应用的 suite。

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/29C8A657-B614-45CD-AB6F-7ABBE150E74F.png)

打开 AppleScript 字典

1. **学习和借鉴别人写好的脚本**：如果脚本词典里不好理解，你还可以到应用论坛（Forum）去学习别人做的脚本，比如 [Alfred](https://www.alfredforum.com/)、[OmniFocus](https://discourse.omnigroup.com/) 都有它们自己的论坛。
2. **善于提问**：可以去 [Stack Overflow](https://stackoverflow.com/questions/tagged/applescript) 的 AppleScript 板块下提问。

### 如何使用系统脚本词典

我们可以通过一个具体的例子来看如何使用脚本词典：以一定的格式发送当前的 Safari 页面到 OmniFocus。因为我利用 OmniFocus 来做「稍后阅读」，需要能以下面的格式发送当前 Safari 页面到 OmniFocus 中：将页面标题作为 OmniFocus 里一项任务的标题，并将页面网址作为这个任务的 Note，

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/08CD8DA4-91F9-4FD0-8425-058CB02C0F80.png)

添加一条 OmniFocus 任务

**第一步**：在 AppleScript suite 中查询有哪些类可供使用

我假设 AppleScript suite 一定提供了当前 Safari 页面的标题和网址的类，所以我打开词典在右上角的搜索框里首先搜索一下「title」（也就是标题）。它给出了以下结果：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/77DB7027-1B55-4A4E-81A3-906FBAF4D455.png)

「title」的搜索结果

这个关键词在 `add reading list item` 类下，说的是阅读列表，显然不是我们需要的，再尝试搜 `name` 看看，结果是：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/3CFCE08A-2EA8-40B2-B4E6-19656D77EB1F.png)

「name」的搜索结果

发现在 `document` 类下有一个 `name` 的属性，考虑到 Safari 页面是一个个的 HTML 文档（document），所以这应该就是我们需要的类。

**第二步**：在 Safari 里随便打开一个网站，然后在「脚本编辑器」里尝试一下：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/1F55E0B9-C19A-448F-AFC0-CF073BC4421C.png)

成功获得当前页面标题

**第三步**：通过类似的方法找到页面网址的类属性：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/B7AA98F0-3F1F-4EDF-9BCF-74CB55A8F37F.png)

成功获得当前页面网址

**第四步**：现在需要添加到 OmniFocus，先查查 OmniFocus suite 里哪个类可供使用，我先搜了一下 `add`，发现并没有什么好的结果：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/76507561-C650-46C0-A355-D00453B042A1.png)

add 的搜索结果

我又先后尝试了 `new`、`action` 等，都没找到需要的类，看来 OmniFocus suite 不按套路出牌呀。最笨但有效的方法是通读整个 OmniFocus suite，找到你需要的（也有可能找不到）。我的做法是，去 OmniFocus 论坛或 Stack Overflow 里搜看看别人是怎么做的，然后借鉴别人的代码。对于实现一些比较常用的功能，这些论坛里一般都有人分享过现成的解法。

于是我最终了解到 OmniFocus 快速添加任务类是 `parse tasks into`，在词典里搜索一下：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/A905DC22-D27F-40E1-9557-46829BAC3590.png)

「parse tasks into」的搜索结果

它的功能是把一段文字按 [Taskpaper](https://guide.taskpaper.com/getting-started/) 的格式添加到 OmniFocus 中。

**第五步**：在「脚本编辑器」里尝试一下

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/577622B2-9FE5-43A8-A530-6AF7947F3A63.gif)

尝试运行脚本

**完成**：目前你已经写出了一段可行的代码了，如果你之后希望经常使用它，可以通过 Automator 之类的软件，新建一个「服务」，然后把这段代码粘贴到相关的动作中。被设为「服务」后这个自动化流程就可以在快捷键设置中被赋予快捷键，所以从此之后你就可以通过快捷键直接调用这个脚本。

AppleScript suite 之外的解法：模拟键鼠
----------------------------

了解了 Suite 之后并不能处理所有问题，因为：

1. 应用的 AppleScript suite 不提供你需要的功能
2. 它虽然提供了，但你却找不到，或者不知道怎么找（比如上一节第四步中出现的情况）

那么你能做的，就是利用 AppleScript 来模拟键盘和鼠标操作，这一点我们已经在前面「AppleScript 基础语法」这一节介绍过了。

通过模拟键鼠来实现自动化操作，非常贴近我们平时在电脑上的操作习惯，所以非常直观。但我不建议用，如果能通过 suite 解决，请尽量用 suite！模拟键鼠只能作为在 suite 没办法时的变通方案之一。

举一个例子你就能理解，我有一个壁纸应用叫 Irvue，你可以通过它的菜单项「Change current wallpaper」来切换壁纸：

![](.evernote-content/9670504E-BA74-4725-8FB5-32FBB8BDD0B7/E3AD421B-EF4C-47F7-97C5-4E71D861B980.png)

用 Irvue 切换壁纸

如果通过模拟键鼠的方式，你需要模拟点击菜单中的 Irvue 图标，然后再模拟点击弹出菜单中的「Change current wallpaper」菜单项，这个过程大概会经历 0.5 秒的时间。

但这个方法的弊病是，在整个过程结束之前，你不能乱点你的鼠标 —— 比如菜单刚弹出来时，如果你不小心在这瞬间点击了一下其他地方，菜单消失了，脚本就会告诉你它找不到这个叫「Change current wallpaper」菜单项。所以这确实是比较妥协的方案。

注 1：其实 Irvue 是提供更改当前壁纸的类的。如果你查阅 Irvue 的 suite，你会发现它提供了一个名为「更改当前壁纸」的类，你直接调用它就能更换壁纸，这样就不会干扰你正常使用键盘和鼠标。

注 2：这种模拟点击的操作，不适用于那些不是通过 macOS 的 UI 编写的工具。比如说很多 Web 套壳工具的 macOS 客户端是用 [Electron](https://en.wikipedia.org/wiki/Electron_(software_framework)) 框架编写的，我们无法对其中的 UI 控件进行操作。4 

在我上文提到的文章《[手把手教你用 AppleScript 模拟鼠标键盘操作，实现 macOS 系统的自动化操作](https://sspai.com/post/43758)》中，提供了更多通过 AppleScript 模拟键鼠操作的例子，也都是很简单的代码。你可以根据那些具体例子的代码，进一步理解和学习 AppleScript。

尾巴
--

了解 AppleScript 的基础语法是掌握 AppleScript 自动化的第一步，在这之后应该理解 AppleScript Suite 的概念，以及如何使用它，因为它几乎是构成 AppleScript 的主要部分，只要 suite 能做到的，它就是最佳的 AppleScript 编写方案。如果遇上 suite 无法满足需求的情况下，模拟键鼠操作是一个非常有效（但有妥协性）的方案。

希望这篇文章让你对 AppleScript 有了一定的了解，在日后发现自己有重复操作时，不妨先想想可以如何通过 AppleScript 解决它。

1. [有些脚本语言每行的缩进不对都无法运行。↩](#)
2. [⌘Command、⇧Shift、⌥Option、⌃Control 等都称为修饰键。↩](#)
3. [翻译成脚本套件可能比较合适。↩](#)
4. [用 Accessibility Inspector（需安装 Xcode）可以查看一个界面下的 UI 可用性。↩](#)

[#macOS](https://sspai.com/tag/macOS)[#效率思维](https://sspai.com/tag/%E6%95%88%E7%8E%87%E6%80%9D%E7%BB%B4)

---

[🌐 原始链接](https://sspai.com/post/45368)

[📎 在印象笔记中打开](evernote:///view/207087/s1/468d4c68-e33b-4916-9e83-f53ecff2dc51/468d4c68-e33b-4916-9e83-f53ecff2dc51/)
