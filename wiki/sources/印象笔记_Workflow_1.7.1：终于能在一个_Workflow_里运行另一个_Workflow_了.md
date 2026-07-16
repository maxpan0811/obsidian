---
title: "Workflow 1.7.1：终于能在一个 Workflow 里运行另一个 Workflow 了"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/Workflow 1.7.1：终于能在一个 Workflow 里运行另一个 Workflow 了.md
tags: [印象笔记]
---

# Workflow 1.7.1：终于能在一个 Workflow 里运行另一个 Workflow 了

# Workflow 1.7.1：终于能在一个 Workflow 里运行另一个 Workflow 了 --- 我实在是服了 Workflow 的更新。这又是一次小版本号，又是一个大众期盼已久的功能。更

---

# Workflow 1.7.1：终于能在一个 Workflow 里运行另一个 Workflow 了

---

我实在是服了 Workflow 的更新。这又是一次小版本号，又是一个大众期盼已久的功能。更新邮件过来后，我看到第一句的前三个词时手机就差点扔地上：

> Run workflows inside your workflows with the new Run Workflow action...

是的，现在我们终于可以在一个 Workflow 里跑另一个 Workflow 了。

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/7356DDAA-1B5A-4F10-A406-A317B7578425.jpg)

Run Workflow

首先注意这个 Workflow 有一个选项，这个选项的意思是：被运行的 Workflow 是否展开。如果打开开关，那么这个 Workflow 在被运行的时候会展开；如果关闭开关，这个 Workflow 则会像 `Get Contents of URL` 这个动作下载东西一样读进度条。无论是打开还是关闭开关，当遇到需要对列表作出选择或者输入等情况，需要你选择和输入的项都会自动弹出，这里是没有区别的。

然后我们来看这个动作的使用情境。

两个使用情境
------

这个动作的第一种使用情境是一个母 Workflow 装多个功能完整的子 Workflow。母 Workflow 的作用只是做个选择。因为有不少 Workflow 本身就是用 Menu 这个动作组合了多种功能。比如之前有一个名为 Universal Download 的动作，这个动作拼接了下载各社交媒体上的视频的 Workflow，但是有的现在已经失效了。我感觉不会有人愿意修这么长的 Workflow。光拖动作都要拖到手酸，要是修完了试跑发现不好用，又忘了自己拖的动作都是啥，肯定一边骂娘一边果断删。

但现在，能在一个 Workflow 中跑其它的 Workflow 了，这种长得要命的聚合性 Workflow 就会变得容易做也容易修。

第二个使用情境是把一个辅 Workflow 作为主 Workflow 的一环来跑，这和我之前写的《[Workflow 思路教程](https://sspai.com/36359)》密切相关。有很多思路类或者类似于算法的 Workflow ，本身用处不大甚至可能就没啥用，比如「去掉重复项」、「倒序排列列表」这种动作。平时用来练手和锻炼思路会做这种 Workflow，但做成了就会放在那也没什么用，而这次，其中一个动作帮了大忙。

### 一、聚合多个 Workflow

聚合多个 Workflow 这个需求最强的情境大概是保存社交网络的视频到本地 [1]。很多人的 Workflow 里估计都装了这三个动作（如果没有的话还不赶紧下载）：

* 保存微博视频到本地（[下载](http://d.pr/1fPW4)，作者：[@Se7en\_YXS](https://twitter.com/se7en_yxs)）
* 保存 Twitter 视频到本地（[下载](http://d.pr/H4c7)，作者：同上，但修改自 [@Oscargong](https://twitter.com/oscargong1995) 的基础动作）
* 保存 Instagram 视频到本地（[下载](https://workflow.is/workflows/ca165ab0f458401c9b4f1a4256527b0a)，作者：不详）

要把这三个动作合并到一个动作里，需要在一个新的 Workflow 里先放一个的动作 `Menu`，再在每个选项下面接上更新出的 `Run Workflow`，在该动作里选择好你想跑的 Workflow 即可。

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/8EBFB568-AD77-4782-B8DA-762CBD7C9849.jpg)

选择要被执行的 Workflow

可以看出，在 `Run Workflow` 这个动作点开后会按首字母排列，同时 Workflow 也提供了一个搜索功能。

这个聚合社交网站视频下载的 Workflow 有一点特殊：对于大多数用户来说，微博和 Instagram 都用的是官方客户端，而这两个官方客户端是不能跑 Share Sheet（iOS 的系统分享菜单）的，所以你不能直接在应用内跑这个 Workflow，需要在通知中心运行 [2]。

这种情况，你可以把这个 Workflow 设两个属性：一个是 `Today Widget`，一个是 `Action Extension`。然后把 Workflow 做成，当通过 Share Sheet 获取链接时，就执行下载 Twitter 视频的动作，而通过 Share Sheet 没有获取链接时（比如直接在通知中心跑的时候），只提供下载 Instagram 视频和微博视频这两个选项。

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/1360B792-2F26-41B5-9ED9-DF2352B1C1B8.jpg)动作做法

但是要注意，当你要聚合的 Workflow 接受的数据种类比较杂的时候，要仔细处理好这里的数据。玩得不太转的，最好就只把那些不需要接收数据的，或者只需要接收同一种数据的 Workflow（比如在 App Store 里的 App 页跑的那些 Workflow）聚在一起就好。

### 二、作为其它 Workflow 运行过程中的一环

估计很多人都有一个待看电影的 List，大家可能各有各的实现方法，比如在豆瓣里弄个列表之类的。我想在自己的 Todoist 里做这个列表，一是待办这个事我倾向于放在同一个软件里，二是 Todoist 可以跟别人分享列表。

这个待看电影列表里的项目要有这些元素：电影名、链接、评分、导演、剧情简介、主演、剧照。

东西很全，所以加起任务来会非常麻烦。我手动加到第二个就觉得这么干实在是蠢得不行，肯定有什么快的方法，于是就通过豆瓣和 IMDB 的 API 分别实现了发送豆瓣电影的数据到 Todoist（[下载](http://cl.ly/jFEX)） 以及发送 IMDB 的数据到 Todoist（[下载](https://cl.ly/jFB1)）。[3]

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/36AE0A0E-C916-4D6A-AD89-15E5B5FFD392.jpg)最终效果

做完这个 Workflow，我突然又觉得，一个一个电影加也很蠢，能不能批量加多个电影？现在奥斯卡结束了，多少有几个自己没看过的，能一并加到 Todoist 岂不更好？

因为上面的两个动作，处理了各种你需要加电影的场景：

* 在豆瓣的网页或者应用
* 在 IMDB 的网页或者应用
* 直接在 Workflow 里输入电影名
* 直接在 Workflow 里输入 IMDB ID（后来我觉得没啥必要所以从豆瓣那个动作里去掉这个功能了）

这些场景并不是都能应对一对多这种情境的，只有后两个，你可以先在 Workflow 中做一个列表，然后再批量处理。所以这里我们需要把原来的 Workflow 拆开，把我们需要的部分单独取出来做成新的 Workflow。这里举输入电影名的例子好了。首先，因为我们只要用名称也就是字符来定位电影就行，所以可以删掉之前动作里获取网页的部分（最好复制一个新动作在新动作上修改，省得鸡飞蛋打），删掉以后把动作接受的内容从 `URL` 改为 `Text`，这个动作就改完了（建议自己亲自改一下动作，如果改不了的话可以直接[下载](https://cl.ly/jNWg)）：

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/1A0EB363-635B-45DC-B397-3CAFCD1D7AB1.jpg)

改完以后的动作的头部应该是这样

修改完动作以后这个动作就可以作为新动作的一环来运行，而新动作我们只要放一个 `Text` 文本框，输入我们想添加的电影名，然后用 `Split Text` 来制作列表。下面再用 `Repeat with Each` 包住 `Run Workflow`，就完成了。

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/ACE42866-B9A9-4971-864F-8675738E72C3.jpg)新动作

可以通过这个动图来看看批量添加的效果：

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/ADC78474-A3EC-493C-9B4A-27D4858E83E3.gif)批量添加

其实这个效果还可以变得更好，因为你会发现有一些电影候选项只有一个，这种情况我们明显可以不做选择直接让 Workflow 把它发到 Todoist 里。这个实现也非常简单，留给有能力的朋友练手。

做成这个 Workflow 以后我突然又想起之前刚好看过 [BBC 的 21 世纪百佳电影排名](http://www.bbc.com/culture/story/20160819-the-21st-centurys-100-greatest-films)，正好可以用这个 Workflow 一次性把前十加进去以后看 [4]。但是打开网页后我发现，这个排名是倒序的，也就是它不是 1–100 那么排的，它是 100–1 那么排的。那加到 Todoist 的顺序也自然会变成倒序，这让我觉得不舒服，我得把它倒过来。好在我有个留存已久的 [@三块五毛](https://sspai.com/post/weibo.com/steyuanxing) 做的用于逆序列表的 Workflow（[下载](https://cl.ly/jNLg)），这个 Workflow 就是把列表反过来用的，当时做这个 Workflow 是我们在玩思路，结果就在这派上用场了。

所以这个 Workflow 中运行了两个另外的 Workflow，一个用于把列表正过来，一个用于把电影加到 Todoist。

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/642EA060-C3D7-4A40-8909-42822CCADCFC.jpg)

一个 Workflow 中可以接两种 Workflow

### List 支持更加丰富的格式

`List` 这个动作一直是接收各种类型的文件但最后会输出文本。现在这个动作可以接受多种格式。如果你在下面接 `Choose from List`，结果会对文件类型进行显示，如果内容是图片的话还可以看到图片。

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/094D1D35-CF5B-4D4A-BFB4-414BFA2678E4.jpg)

显示文件格式与图片

### 健康数据支持 Duration 这个项

Workflow 很早就支持了获取健康数据，但是只是获取数据，并不对数据进行处理。所以有一个对大家都很重要的数据在 Workflow 里的处理一直很麻烦——睡眠时间。

它起初只支持获取 Start Date 和 End Date，而且 Workflow 里没有时间计算器这个东西，所以计算两天之间的睡眠情况就变得很复杂。现在 Workflow 添加了 `Duration` 这个项，你只要给它睡眠的起始和截至日期，它就会帮你获取那一天睡了几觉，每一觉睡了多久。如果你睡眠习惯好，一天只睡一次，那这个数据看起来会非常干净：

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/FB3B2733-67E7-468B-B0DA-1FCBC60C151F.jpg)请输入图片标题

### 增加了一些图标

在这次更新里 Workflow 还增加了不少图标，但是，还是没有 Evernote。🤷‍♂️

![](.evernote-content/FAFDFBAE-DEA3-4576-A183-D3BE015B0274/BE28E189-9DA5-4278-B3A3-3A6AD547731A.jpg)请输入图片标题

### 修复了拖动 End Repeat 时无限向下滚的 Bug

这是最后一个值得一说的变化，在之前的版本里，`Repeat` 这个动作的最后一步 `End Repeat` 在拖过一页以后就会自动往下跑，跑到最底部也不会固定位置，是个非常恼人的 Bug。在这个版本终于也予以修复。

可以做的期待
------

拿到 1.7.1 版本的第一个 Beta 的时候我就马上试用了 `Run Workflow` 这个动作，然后发现了两个问题：第一个是找动作难（第一版 Beta 还没支持搜索）；第二个问题是，当你把聚合类的 Workflow 放在通知中心部件的最顶部，那些被聚合的动作还是会在下面显示，也就是功能重复。所以我提了两个建议，第一个是在 `Run Workflow` 里加搜索，第二个是可不可以在通知中心隐藏那些被聚合过的动作。

前一个看起来是被接受了（当然提这个要求的肯定不止我一个），第二个要求作者则表示，也许会让一些用户困惑，但他又说，Workflow 的组织方式也着实需要做一些改变。所以在不远的未来，我们也许就能看到 Workflow 对动作实现更好的组织和管理方式。

---

[1]: 我个人的还有 App Store 相关、播客制作相关、Apple Music 相关等。

[2]: @Se7en\_YXS 的下载微博视频的动作倒是可以通过 Share Sheets 跑，但是需要用到能运行 Share Sheets 的第三方客户端。

[3]: 使用 2Do、Omnifocus、Things 的朋友也可以直接修改该动作的最后一步来做到把任务加到你想加到的应用里。但这些应用有两个不舒服的地方：一是需要跳转，二是不能直接添剧照。

[4]: 其实前几无所谓，100 个全加也不会用多久，只是在这里用 10 个来举例子。

---

[🌐 原始链接](https://sspai.com/post/37830)

[📎 在印象笔记中打开](evernote:///view/207087/s1/827bf9e1-9671-419b-aa39-ae66aa76ca3b/827bf9e1-9671-419b-aa39-ae66aa76ca3b/)