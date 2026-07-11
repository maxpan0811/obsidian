# OmniFocus 的 URL Schemes 用法

---

![](.evernote-content/3963CFFF-9DC1-4552-BF0C-535D3803CF95/58448DA5-975A-45E5-8AD6-AEFF4E045FC1.jpg)

OmniFocus 在 iOS 上的 2.14 版对 Power User 来说是一次诚意十足的更新，简单来说，这次更新对 URL Schemes 进行了翻新，在已有基础上复杂 URL Schemes，还对 x-callback-URL 进行了支持。从而可以做到：直接从其他地方直接获取文件然后作为附件添加到 OmniFocus 里；从其它应用批量发送任务到 OmniFocus；以及把 OmniFocus 的任务添加到 Fantastical……

***本文导航***

（点击可快速跳转至对应章节）

* [对复杂 URL Schemes 的修改](http://sspai.com/33969#01)
* [使用例](http://sspai.com/33969#02)
  + [使用 Workflow 在 Share Sheet 为任务添加附件](http://sspai.com/33969#021)
  + [把 OmniFocus 的任务移动到 Fantastical](http://sspai.com/33969#022)
  + [使用 Launch Center Pro 快速添加提醒事项](http://sspai.com/33969#023)
  + [使用 Workflow 添加有预设目的的任务](http://sspai.com/33969#024)
  + [通过 Editorial 批量导出任务到](http://sspai.com/33969#025)
* [结语](http://sspai.com/33969#03)

对复杂 URL Schemes 的修改
-------------------

OmniFocus 的 URL Schemes 可以分为两部分：用于导航到具体界面和用于添加新任务。

在 2.14 之前 OmniFocus 就把导航部分的 URL Schemes 做的相当完整了：

**动作行为****URL Schemes**显示收件箱 OmniFocus:///inbox 显示具体文件夹 OmniFocus:///folder/`文件夹 ID` [[1]](http://sspai.com/33969#fn:1 "see footnote") 显示具体项目 OmniFocus:///task/`项目 ID` 显示具体情境 OmniFocus:///context/`情境 ID` 显示具体透视 OmniFocus:///perspective/`透视名` 显示检查 OmniFocus:///review 显示附近任务 OmniFocus:///nearby 显示旗标任务 OmniFocus:///flagged 显示截止日期为过去的任务 OmniFocus:///past 显示截止日期为今天的任务 OmniFocus:///today 显示截止日期为未来的任务 OmniFocus:///soon

注意：文件夹、项目、情境都是使用的 ID 而不是用户自己设定的名称，ID 的取得方法是在 Mac 端右键点击任一文件夹、项目或情境，然后选择`拷贝为链接`：

![](.evernote-content/3963CFFF-9DC1-4552-BF0C-535D3803CF95/A8076959-332C-43B1-96CB-B8DA180D4F5B.jpg)

 在 iOS 上可以使用 [这个 Workflow 动作](https://workflow.is/workflows/1140837eef764ed8a5c9d1b49a533f29) 来获取项目和任务 ID。

然后你会得到像这样 `omnifocus:///folder/mXBUhIF6qem` 的整段的链接，最末的 `mXBUhIF6qem` 为该项的 ID。

用于导航的 URL Schemes 虽然完整，用于添加任务的却一直十分简陋，只有两个：

1. **添加任务：**`omnifocus:///add?name=任务名`
2. **添加任务与备注：**`omnifocus:///add?name=任务名&note=备注内容`

也就是说，OmniFocus 里关于任务的其它备选项，比如项目、上下文、推迟到、结束时间、是否旗标等统统不能预先通过 URL Schemes 填好。像这样给又不给够的做法总是让人觉得鸡肋，我在添加任务的时候就经常会想到：既然我这么多重要的东西都不能直接通过 URL Schemes 填好，我还不如从一开始就打开 App 去添新任务。

2.14 之后的更新则改变了这一切，几乎所有 OmniFocus 中的关于任务的变量都可以通过 URL Schemes 直接填好：

```
omnifocus://x-callback-url/add?name=任务名&note=备注&estimate=延续时间&autocomplete=true&completed=预设完成日期&repeat-method=重复形式&repeat-rule=重复规则&parallel=true&flag=true&defer=推迟到…&due=何时到期&project=项目名&context=上下文&attachment-name=附件名&attachment=附件文件
```

* **name:** 任务标题、任务名。
* **note:**任务备注，在 LCP 中设为剪切板的话用起来比较方便，但在 OmniFocus 支持 Sharesheet 以后手动输备注用的越来越少。
* **estimate:**预估的延续时间，可以填写时间和简写，比如 3d 就是 3 天的意思。
* **autocomplete:** 自动完成，后面跟布尔值（`true` 或者 `false`）。这个大家可能不了解，自动完成代表到了过期时间会自动完成。这项适合那些你一定会做的周期性任务。
* **completed:** 后面跟具体时间点，思路和 autocomplete 类似，适用于非周期性的任务。
* **repeat-method:** OmniFocus 的重复形式分为三种，也就是说它后面**只能跟三个量**，`fixed` 定期重复、`start-after-completion` 完成后再次推迟、`due-after-completion` 完成后再次到期。这三个选项在新建任务时的重复选项里可以见到，理解了推迟和到期在 OmniFocus 的区别的话就不难理解后两个选项。
* **repeat-rule:** 这一项是重复的具体周期和次数，填写的内容要遵从 ICS 的语法，文档见 [RFC2445](http://www.ietf.org/rfc/rfc2445.txt)。[Omnigroup 论坛](https://discourse.omnigroup.com/t/implementation-details-for-OmniFocus-2-14-automation/24179?u=kcase)给出的例子是：`FREQ=WEEKLY;INTERVAL=1`（重复周期为一周，次数为一次）。
* **parallel:** 是否建立平行动作组[2](http://sspai.com/33969#fn:2 "see footnote")。后跟布尔值。单个的任务建立时和建立后都不会显示平行（parallel）这个选项，但是当你把其它任务拖到这个任务之下使之变成一个子任务[3](http://sspai.com/33969#fn:3 "see footnote")，主任务的平行属性就会生效。
* **flag:** 是否旗标，后跟布尔值。
* **defer:** 表示推迟到何时。OmniFocus 可以使用自然语义，比如 `2 days 14:00`，所以建议用用户词典自定义一些自己常用的推迟时间点。
* **due:** 截止日期，也可以使用自然语义。
* **project:** 项目名，但通过 URL Schemes 不能添加新项目，所以填写的必须是已有的项目名，建议在 Launch Center Pro 里做一个列表。
* **context:** 情境，具体使用规则同上。
* **attachment-name:** 附件名，很明显添加附件必须通过 Workflow 才能实现。
* **attachment:** 附件文件，需要进行编码。关于附件的两个变量，官网给出的这个  [Workflow 动作](https://workflow.is/workflows/15eb123f9611483f81c06103d8666962) 看懂了就自然明白怎么用了。

除此之外，你会发现在上面那段 URL Schemes 里有 `x-callback-url` 的字样，OmniFocus 在 2.14 版后正式支持了 x-callback-url，`x-success`、`x-cancel`、`x-error` 都支持。2.14 版本之前和之后的 URL Schemes，都可以举一反三的使用 x-callback-url 来跳转跳回。当然，在正常使用情况下，应该只有添加任务后跳回才有意义，打开具体界面类的动作跳过去再跳回来是图个啥……

使用例
---

### 使用 Workflow 在 Share Sheet 为任务添加附件

iOS 上一直没有能真正利用 Share Sheet 在各处都能保存附件的任务管理应用，2Do 虽然在 iCloud Drive 里有 Share Sheet 的动作，但是保存了的附件只是一个链接，可以说是不可用的。OmniFocus 这次更新之后，在 URL 中添加了两个关于附件的项：`attachment-name` 和 `attachment`，通过 [Workflow](http://sspai.com/tag/Workflow) 为这两个项赋值，就能非常理想地保存附件到 OmniFocus。

[下载该动作](https://workflow.is/workflows/15eb123f9611483f81c06103d8666962)

这个 Workflow 是个非常基础的动作，不需要弄明白就能使用。希望弄明白的话下载了好好看看应该也就能看懂了，它主要就是把文件和文件名、拓展名获取后插入 OmniFocus 的 URL Schemes 作为变量。

### 把 OmniFocus 的任务移动到 Fantastical

有计划地完成任务是有必要的，因为[拖延让我们经常错过最终期限](https://getpocket.com/@humsweet/share/571296)。我还读过一篇文章，名字就叫 [What doesn't get scheduled, doesn't get done](http://simplicitybliss.com/post/123996917217/scheduling-tasks-with-omnifocus)，讲的是把 OmniFocus 的任务部分地移到日历中去，现在你可以在 iOS 上效率地做到这一点了。

当然，这次我们又要用到 [Workflow](http://sspai.com/tag/Workflow) 了。你可以先下载 Omnigroup 官方做的[动作](https://workflow.is/workflows/d9cb2a8aa5c2426493bbfd4e18a0d4fe)（中文系统下没用），或者下载我汉化并改良了的[动作](https://workflow.is/workflows/752ed65766ea4ccc93a4b7b2031ab30d)。

从 OmniFocus 的 Share Sheet 运行该动作后，**首先**会检测该任务有没有起始时间，如果有就跳转 [Fantastical](http://sspai.com/tag/Fantastical) 的当天界面查看日历上已有的安排，如果没有就跳转到今天的界面。**查看完之后**你需要**手动**回到 OmniFocus，Workflow 则会继续运行，让你选择**任务开始时间**，**然后**把任务名、开始时间、持续时间、任务 ID 等东西全部填入 Fantastical，**最后**通过 Workflow 自动跳回到这个 OmniFocus 任务。

这个动作的实用性一般。首先，为什么说官方动作中文系统下没用，因为 Workflow 的时间格式会跟着系统变化，这里必须微调。其次英文系统下官方动作也有瑕疵，因为它不给你选择持续时间，动作本身虽然会获取 OmniFocus 任务的持续时间，但是如果该任务未设定持续时间，他也不给你选，而是使用 Fantastical 的默认持续时间，很明显这里不科学，我修改后的版本会让你自己填事件持续时间，需要用英文表示（只需要 min、hour 这俩单词，别怕啦）。

我只修改了这两个地方，在任何语言的系统下应该都可以用了，但我感觉可能还能改的更理想，留给喜欢折腾的人们玩。

### 使用 Launch Center Pro 快速添加提醒事项

说实话在这个版本之前我是不喜欢用 OmniFocus 的 URL Schemes 手动添加任务的，变量太局限了，只能预设任务名和备注，连提醒都不能设定。那对于一些杂项，要么可以用 [Due](http://sspai.com/tag/Due)，要么让 Siri 提醒我。但现在好了，有了 `Due` 这个变量和 x-callback-URL，我们在 [Launch Center Pro](http://sspai.com/tag/Launch%20Center%20Pro) 里建立一个 OmniFocus 的提醒事项就和 Due 一样简单快速了：

```
OmniFocus://x-callback-url/add?name=[prompt:Task]&due=[prompt:Due to…]&s-success={{launch:}}
```

* `x-callback-url`: 如果你想让 OmniFocus 执行 x-callback-URL 命令，或者说添加完任务以后跳转到其它 App（或者回到主屏幕[4](http://sspai.com/33969#fn:4 "see footnote")），那你就需要首先在 URL 中声明。如果不需要跳转，则不需要在 URL 中加上 x-callback-url。
* `add?name=[prompt:Task]`: `add` 是添加任务的命令，`name` 后面跟的是任务名，`[prompt:Task]` 是 Launch Center Pro 里专有的命令，代表打开一个标题为 `Task` 的输入框。
* `&due=[prompt:Due to...]`: URL 中的 `&` 符号用中文理解成「然后」我觉得是最合适的，你读的时候把这个符号都都成「然后」就好懂了。`=` 表示给变量赋值，左边是变量名，右边是你要赋的值。`due` 代表的是 OmniFocus 中的截止日期这一项。`[prompt:Due to...]` 和上面 `[prompt:Task]` 的理解一样。
* `&s-success={{launch:}}`: 很标准的 x-callback-URL 结尾，代表动作成功后跳转到 Launch Center Pro。

*[直接下载动作](http://cl.ly/fmPH)*

值得提醒的是，因为 Launch Center Pro 支持 [TextExpander](http://sspai.com/tag/TextExpander)，所以你可以设置一些你常用的截止日期的短语，比如用 [这篇文章里提到的技巧](http://www.worksmartandberemarkable.com/blog/2014/speed-deferring-OmniFocus-tasks)，可以让你在 iOS 和 Mac 上都更快地添加截止日期。

### 使用 Workflow 添加有预设目的的任务

在阅读 RSS 的时候人们会遇到一些电脑端软件的技巧或者教程，这些需要对照指示操作的文章，我在[《以 GTD 的方式处理稍后读》](http://sspai.com/33933)中提到过，最好发到任务管理软件，因为你在手机上看了也没用。利用 Workflow 和 OmniFocus 的 URL Schemes 就能快速做到这一点，而且还能跳回到你刚才正在阅读的文章。它所用的 URL Schemes 是：

```
OmniFocus://x-callback-url/add?name=文章名&note=文章链接&project=OmniFocus中的项目名&x-success=pocket://
```

*[Workflow 动作下载](http://cl.ly/fmeP)（注意，你需要修改项目名和你用于阅读的软件的 URL Scheme）*

这段 URL 里的文章名和文章链接，都可以通过 Workflow 直接获取，项目名你也可以预设好，所以你需要操作的只是在跳转后按一下完成，就又会自动从 OmniFocus 跳回你用于阅读的软件，我这里的阅读软件是 [Pocket](http://sspai.com/tag/Pocket)。

### 通过 Editorial 批量导出任务到 OmniFocus

能够支持 x-callback-url 了就具备了批量添加任务的条件，但还需要具体的工具，目前能在 x-callback-url 体系下做到这件事的只有 Workflow。[5](http://sspai.com/33969#fn:5 "see footnote")但是用 Workflow + x-callback-URl 做到这件事将是非常难看的，比如说你添加 12 个任务，那就得来回跳转 12 下，这跟 Clear 使用的用逗号分割多任务比起来就太不雅了[6](http://sspai.com/33969#fn:6 "see footnote")。但 Clear 能用逗号分割多任务是因为它任务属性太少，而 OmniFocus 有太多变量需要指定。于是，在 iOS 上，Omni 团队想到了用 [Editorial](http://sspai.com/tag/Editorial) 的动作来解决创建批量任务的问题。

使用这个动作需要对 Taskpaper 的格式有个了解，好在这很简单：

* 项目：一行字符后面跟一个**半角**冒号`:`
* 任务：一行字符前跟一个半角短横`-`和一个空格（就像 Markdown 的列表语法）
* 标签：一行字符前跟`@`

首先这个动作有两个形式，一种是单纯转换 [Taskpaper](https://www.taskpaper.com) 格式[7](http://sspai.com/33969#fn:7 "see footnote")的任务列表到 OmniFocus，就像这样：

![](.evernote-content/3963CFFF-9DC1-4552-BF0C-535D3803CF95/D14550CE-0DDD-48E8-BF7E-F179480F616F.jpg)

[下载用于单纯转换的 Editorial 动作](http://www.editorial-workflows.com/workflow/5794778264371200/ULWk7OZXqek)

下一种形式则更为复杂，但可以把前面介绍 URL Schemes 时提到的那些关于任务的各个后选项全部添加进来，但需要在 Editorial 中通过特殊字符标明这些是特殊项，好让 OmniFocus 在接受的时候把各个内容填写到应填写的位置。

官方论坛上给出的例子是这样的：

```
«project_name» @parallel(false) @due(«due»)  
      This task needs to be done at least 1 week before «project_name» is due @due(«due» –1w)  
      This task needs to be done at least 2 days before «project_name» is due @due(«due» –2d)
```

[官方动作](http://people.omnigroup.com/kc/editorial-template-project-workflow.html)中用`«»`包住的是变量，但是`«»`这个符号不是必须的，事实上这个半角书名号在 iOS 上还挺难找的，你可以在 Editorial 里将其把替换成你习惯的符号。考虑到要在 iPad 上使用外接键盘，加上我不用直角引号，我把它改为了`「」`（[下载修改过的动作](http://www.editorial-workflows.com/workflow/5790544366141440/bmxnQy_sSdY)）。变量在动作运行后会让你填写，比如前面代码框中的例子，在 Editorial 里填写后，会让你把 `project_name` 和 `due` 这两项填写了，然后会在 Omnifocus 出现这样的效果：

![](.evernote-content/3963CFFF-9DC1-4552-BF0C-535D3803CF95/1D868F88-5961-4C67-8490-C82581167BE0.jpg)

我写这篇文章的时间是 4 月 25 日（周一），所以中间那副图 Due 中的 `Next Sunday` 就是 5 月 1 日，也就是右图中的项目的截至时间。但因为，左图中，对不同的任务的截止时间通过加减进行了微调，`-1w` 表示减去一周，`-2d` 表示减去两天，所以右图中 OmniFocus 的输出结果里会有两个不同的截止日期，一个已经截至了，另一个还有几天才截至。

另外注意 `@parallel(false)` 这一句，这个前面读的仔细的人应该明白是什么意思，这是声明这个项目是否为平行项目。这里的小括号就像 URL Schemes 中的等号，特殊项的值在这里要添在小括号里。

这个简单的例子体现出 OmniFocus 可以通过 [Editorial](http://sspai.com/tag/Editorial) 做足够复杂的批量任务导入。

批量添加任务是个很基础的需求但是各大软件在 iOS 上的表现都很基础，OmniFocus 从 [Taskpaper](https://www.taskpaper.com) 那找到了灵感，通过 Editorial 绕道做到了这点。虽然需要多一款软件，但考虑到 Editorial 对在 iOS 既爱写字又爱折腾的人来说是名副其实的必备应用，入了还是不会亏的。

结语
--

这次的更新在我看来实际上是一次在 [2Do](http://sspai.com/tag/2Do) 和 [Taskpaper 3](https://www.taskpaper.com) 夹击下的防守。Omnifocus 这次建立了比 2Do 更完备的自动化支持，又在 Taskpaper 在 iOS 上力道不足时弥补了自身批量添加任务的不足。不过如此丰富的 URL Schemes 也确实让那个给我带来庄严感的 Omnifocus 年轻了起来，——我可以折腾和调教它了！

通过学习 [OmniFocus](http://sspai.com/tag/OmniFocus) 的 [URL Schemes](http://sspai.com/31500) 也可以让你对这款软件有更深的理解，你会知道一个任务在不同的情境下会有多少个维度，也会知道重复任务也不仅是简单的只有一种自动重复就足够了……所谓好的软件就是这样，在使用它的时候可以让你对它背后的概念更加熟悉，引导你走向更深的认识。

*注：除了文中提到的这些动作和方法，[官方论坛](https://discourse.omnigroup.com/t/automation-in-omnifocus-2-14-released-2016-04-26/23985)中还有不少的玩家在分享他们的动作和组合。*

1. 文件夹、项目、情境都是使用的 ID 而不是用户自己设定的名称，ID 的取得方法是在 Mac 端右键点击任一文件夹、项目或情境，然后选择`拷贝为链接`。然后你会得到像这样 `OmniFocus:///folder/mXBUhIF6qem` 的整段的链接，最末的 `mXBUhIF6qem` 为该项的 ID. [↩](http://sspai.com/33969#fnref:1 "return to article")
2. 在 OmniFocus 里，除了项目（Project）这种整理任务的方式，还有动作组的概念。 [↩](http://sspai.com/33969#fnref:2 "return to article")
3. 子任务（Subtask）: 把 任务 A 拖/移动到任务 B 下，A 就成为了 B 任务的 Subtask，B 本身成为一个拥有多任务的任务组，任务组和项目的区别见[官网文档](https://support.omnigroup.com/OmniFocus-ios-action-groups/)。 [↩](http://sspai.com/33969#fnref:3 "return to article")
4. 见我在越狱指南写的[《越狱后的 URL Schemes 详解》](http://jbguide.me/2016/01/23/url-schemes-after-jailbreak/)。 [↩](http://sspai.com/33969#fnref:4 "return to article")
5. 为什么 Launch Center Pro 跟 Drafts 不可以呢？Launch Center Pro 本身对多行分割无能为力，Drafts 可以用批量添加到 Fantastical 的机制添加多个任务到 OmniFocus，但是只能填写任务名，不能把每个项目填到相应的位置。 [↩](http://sspai.com/33969#fnref:5 "return to article")
6. Launch Center Pro 内置了 Clear 批量添加任务的动作，只要设好列表名，然后在填写任务的时候用半角逗号分割，就能一次性添加多个任务。 [↩](http://sspai.com/33969#fnref:6 "return to article")
7. 在 Taskpaper 中，一段文字是一条备注、一段文字后跟半角冒号则代表项目、一段文字前有半角短横与空格则表示任务。 [↩](http://sspai.com/33969#fnref:7 "return to article")

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[OmniFocus 的 URL Schemes 用法](http://sspai.com/33969)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/3963CFFF-9DC1-4552-BF0C-535D3803CF95/6FE4548D-1D19-4148-A6A3-9B3D603FAA9B.jpg)](http://aos.prf.hn/click/camref:111l75A/pubref:installment426/destination:http://www.apple.com/cn/shop/browse/finance/installment)

---

[🌐 原始链接](http://sspai.com/33969)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e957fa65-9d38-4a96-bebf-2d90a82fdb9b/e957fa65-9d38-4a96-bebf-2d90a82fdb9b/)