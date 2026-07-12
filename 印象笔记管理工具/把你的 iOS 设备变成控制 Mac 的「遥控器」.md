# 把你的 iOS 设备变成控制 Mac 的「遥控器」

---

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/95FB2B33-4560-4F58-8F8C-CBC3B53DFA6E.jpg)

[![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/B8826DFD-766B-44A6-9771-65B34C6AAC4C.png)](http://matrix.sspai.com/user/681230)

这篇文章中谈到的方法并不是使用 [BetterTouchTool Remote](https://itunes.apple.com/us/app/btt-remote-mouse-trackpad/id561676304?mt=8&uo=4&at=10lJSw) 或类似的软件来控制 Mac，而是通过使用 Launch Center Pro 这样的 iOS App 来为自己的需求量身定做一个遥控器。与 BetterTouchTool Remote 或类似的软件相比，这种方法甚至不要求你的两个设备在同一个网络环境下，只要都连接在互联网上就能做到。

其实本文及类似文章里用到的方法实质上只有一个：发送内容到 Mac，触发 Mac 上预设好的规则，运行相应的 Applescript，然后再执行动作。

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/BDEAB776-3C1B-4F68-857C-8DF4F6BED658.jpg)

懂得原理的话工具是可以自己选择的，我个人偏好的工具是：

* **iOS 端发送工具：[Launch Center Pro](http://sspai.com/tag/Launch%20Center%20Pro)。**其实 Drafts、Workflow 都可以，但 Launch Center Pro 操作时可以凭借[肌肉记忆](http://sspai.com/34961)，根本不用看就能发送文本过去，更像遥控器的感觉。
* **Mac 端接收工具：Dropbox。**Launch Center Pro 支持 Dropbox 的接口，同时 Dropbox 在 Mac 上也拥有文件夹，可以触发 Hazel。
* **Mac 端触发条件的工具：[Hazel](http://sspai.com/tag/hazel)。**对于新手来说，Hazel 大概是这个流程里没办法替代的工具…… 所以配工具的时候可能要以 Hazel 为中心。

下面是四个我自己用的例子，用到了不同的工具组合。**最简单和懒省事的办法是例 4，而且例 4 基本可以满足大多数人的需求。**

* [例一：发送文章到 Mac 并用 Chrome 打开](http://sspai.com/35242#01)
* [例二：让 Mac 播放 Spotify 歌单](http://sspai.com/35242#02)
* [例三：让 Mac 屏幕睡眠（Shell 命令）](http://sspai.com/35242#03)
* [例四：让 Mac 播放 Apple Music 歌单（Keyboard Maestro）](http://sspai.com/35242#04)

例一：发送文章到 Mac 并用 Chrome 打开
-------------------------

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/D59B0DEF-A838-4D3D-B4FF-31001E39E375.jpg)

这是[《用 GTD 结束稍后读》](http://sspai.com/33933)里提到的例子，把适合在电脑上读的文章发到 Mac 上（比如这篇我感觉必须在 Mac 上读，在 iOS 上读一点用也没有）。使用情境是将自己看到的适合用电脑阅读的文章发送到电脑上打开，做到自己回家唤醒 Mac 就能直接看。除此之外另一个使用情境是收集素材，9.3.3 越狱刚出的时候我在坐电车，于是回家前只能用用 iPhone 看 [r/jailbreak](https://www.reddit.com/r/jailbreak/)，我想把我认为有价值的帖子和评论收集起来到家写文章的时候用，于是也用了这个 Workflow，效果很好。同理你可以在看 [Product Hunt](https://www.producthunt.com) 等产品网站的时候也把感兴趣的链接都发电脑上，虽然你也可以日后在自己的赞里一个一个点出来……日后找赞再点出来的方法除了比直接发到电脑上慢以外，关键是日后未必还能想得起来。打开电脑就能看见这个提示效果是惊人的，它也给了你一个必须马上执行的压力。

我使用 Chrome 的原因是因为它不是我的默认浏览器，我没有清默认浏览器 Tab 的习惯，如果直接发到 Safari 上，反而会造成阅读类的文章和之前打开的网页的混淆，所以要在这里专门用另外一款浏览器来打开文章。如果你习惯清 Safari，那把 Chrome 部分的 Applescript 改成 Safari 的就行了。

具体流程：

**第一步：**在 iOS 设备上看到一篇想要用 Mac 读的文章，通过 Workflow，把**链接**作为文本文档的内容，把 `ReadLaterURL.md` 作为文本文档的标题，发送到 Dropbox 的指定文件夹。

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/AD6EEDF9-AC9D-478F-8EA6-C13E7243965F.jpg)

*标题其实设为什么都行，但必须是文本格式的后缀名，比如 `.md` 或 `.txt`，而且要注意和之后写的几个例子里的名称有区分。*

* [Workflow​ 下载](https://cl.ly/hE18)（我的 Workflow 里标题就是 `ReadLaterURL.md`）

**第二步：**在 Hazel 里设置条件触发文件夹，这样发送到这个文件夹里的文件，如果满足条件，Hazel 就会作出你设定好的处理：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/EB4B135A-8CF8-4F0F-AFF0-771138294E8A.jpg)

**第三步：** Hazel 里的动作名称也就是 `Name` 这一栏可以是随意的，但剩下的要按要求来做。整体的结果是：当在指定文件夹中，发现名称为 `ReadLaterURL` 的文件，就执行两个动作：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/58C12306-1BB1-499F-BC02-5AFCC2446367.jpg)

*注意这里文件名不能带后缀名，因为 Hazel 会把文件名和后缀名区别对待，导致无法执行后续的任务。*

第一个动作是获取文本文档内容，作为链接在 Mac 上用 Chrome 打开。就是这一步需要用到 Applescript。**第二个动作**是前一个动作执行成功后删除文本文档。

**成功后删除**这一步很重要，类似的步骤都需要这一步，后面不再提了。

**第四步：**填入核心的 Applescript：

```
set the_file to "指定文件路径"
set theURL to (read the_file)
tell application "Google Chrome"
    if windows ≠ {} then
        make new tab at the end of window 1 with properties {URL:theURL}
    else
        make new window
        set URL of (active tab of window 1) to theURL
    end if
    activate
end tell
```

代码框中的指定文件夹路径必须是你在第二步 Hazel 里设置过的那个文件夹，文件名必须是你在 Workflow 里设置好的文件名，比如我的是：

```
/Users/Humsweet/Dropbox/Temporary/inbox/ReadLaterURL.md
```

*最后的 `.md` 这个后缀名，或者说格式，是你自定的，它也可以是 `.txt` 或者其它的文本格式，不过要和 Workflow 中设置的一致。因为这个动作整体是要把文章的链接作为文本内容发送到名为 ReadLaterURL 这个文本文件里，所以它的名称里必须有一个**文本类型**的拓展名。*

最终在 Hazel 里的 Applescript 应该是：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/9F0CF9F0-8C08-4979-8601-F3D01F1E1207.jpg)

例二：让 Mac 播放 Spotify 歌单
----------------------

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/AC1E51E3-A1A4-442A-86B3-B9EDA2DCB51C.jpg)

虽然我有了蓝牙音箱，但因为连接过的设备过多，每次连想连的设备都得靠运气决定音箱和谁配对儿，所以我还是会偶尔用 Mac 来单纯播放音乐。除此之外，用这个方法，**在屏幕睡眠的时候也可以直接开始播放**，这就像你有个遥控器，可以一键播放你想听的歌单。

这里用到的发送工具是 Launch Center Pro，因为「遥控器」这样的东西必须要做到的事，是可以让我们基于「肌肉记忆」来进行遥控。iPhone / iPad 这种基于触摸屏的设备上能满足这个要求的 App 寥寥无几，Launch Center Pro 就是体验最接近而且几乎每个 Power User 手中都有得 App。

**具体流程：**

**第一步：**在 Launch Center Pro 里可以直接添加`发送文件到 Dropbox` 的动作（需要提前在 Launch Center Pro 中关联 Dropbox）：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/1DD9CC3C-0C95-448A-A97E-E54C5BE44D1C.jpg)

最后 Launch Center Pro 里的代码应该是这样的：

> launch://dropbox/new?text=这里什么都行&path={{/Temporary/inbox}}&name={{PlayNew}}

*这次我指定文件名的时候没加后缀名，因为这次 Hazel 只需要识别文件名而不需要识别文件内容。*

设定 Hazel 动作的那几步可以直接参考例一，只是注意名称一定要和在 Launch Center Pro 里写好的文件名一致。

然后这个例子里比较复杂的地方是 Spotify 播放具体列表的 Applescript，下面是我写好的可用的 Applescript：

```
tell application "Spotify"
    activate
    delay 2
    play track "Spotify 播放列表链接"
    if repeating is false then
        set repeating to true
    end if
end tell
```

代码里的 `Spotify 播放列表链接`可以在 Mac 端里右键播放列表找到：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/57E1A63F-096B-4BBB-A410-3B43F714E278.jpg)

*`delay 2`是因为我的 Mac 直接将 Spotify activate 以后不会马上对命令有反应，得稍等个一两秒软件才有反应。你配置高的话也许不用 `delay`或者时间需要得短一些。另外我这段代码里也加入了判断是否开启了重复播放模式，如果没开启就开启，如果需要的话你也可以找找随机播放的代码然后加进去。*

最终的完成效果放在 Hazel 里应该是这样：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/6B084D2D-43F9-4E3E-8D03-E1C3B9E275F0.jpg)

如果你不用 Spotify，iTunes 里的音乐当然也是可以用这个方法做到的，具体的 Applescript 当作作业大家回去找一下吧。

例三：执行 Shell 命令
--------------

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/5CE4E17D-3021-4623-AE00-7592289FF5E4.jpg)

用 iOS 控制 Mac 的动作，支持 Applescript 的系统控制都可以做到。但是有可能比起 Applescript 你更熟悉 Shell 命令，而且有时候 Applescript 做不到的 Shell 命令可以做到，比如**仅让屏幕睡眠**，有时候我们用 Mac 放音乐的时候可能需要仅睡眠屏幕而不睡眠系统，这种情况下就可以用 Shell 命令。

这个例子第一步和例二一样，其它中间步骤和例一一样，所以都不再写。唯一不一样的也是 Applescript 部分。

用 Applescript 执行 Shell 命令的方法是：

```
do shell script "Shell 命令"
```

比如让屏幕睡眠（不是让系统睡眠）的 Shell 命令是：

```
pmset displaysleepnow
```

那在 Hazel 里的 Applescript 框里你只要填上：

```
do shell script "pmset displaysleepnow"
```

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/8EA73BD3-B631-42FB-A924-CFDF90D972B5.jpg)

就可以让屏幕睡眠而不让系统睡眠。

例四：触发 Keyboard Maestro 动作
-------------------------

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/C73EC5DD-6A67-41D7-9C4F-8DB62B6425D2.jpg)

如果你不熟悉 Applescript 也不熟悉 Shell 命令怎么办呢？如果你装有 [Keyboard Maestro](https://www.keyboardmaestro.com) 的话，有一个懒省事的办法——直接调用 Keyboard Maestro 的动作。这要比查 Applescript 简单不少。Keyboard Maestro 目前支持的系统动作目前有这些：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/63D998A0-3C5A-49DD-8D13-67202E8B8585.jpg)

当然我们真正可以使用的不止这些动作，比如前面留的作业，远程控制让 iTunes 播放你想听的播放列表，也可以用 Keyboard Maestro 来做。

前面的发送和接收以及 Hazel 文件夹设定这些步骤请参照例一和例二，我们直接从如何在 Hazel 接收文件后激活 Keyboard Mastro 动作开始看这个例子。

接收文件后让 Hazel 触发 Keyboard Maestro 动作的 Applescript 可以在 Keyboard Maestro 里找到：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/D64A328D-52CE-4476-8F9E-49A5FFD3F0C7.gif)

然后把选中部分复制到 Hazel 里即可：

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/FE3921C0-B9C8-4337-A303-1F748A642DDC.jpg)

把动作放到 Keyboard Maestro 里以后也可以用 [LaunchBar](http://sspai.com/tag/LaunchBar) 这样的快捷启动器来启动，一举两得。同时，用 Keyboard Maestro 你可以完成的不止一个动作，你也可以完成多个动作的组合，就看你的想象力和需求了。

结语
--

![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/CCE53D2F-C466-4B82-A268-7B563FE8FECF.jpg)

iOS 控制 Mac 对于很多人来说有两个多余感：一是本设备可以做为什么要用第二设备来做，二是为什么有的 App 本身就能用 iOS 上的 App 遥控，我还要再搞一个？

对于第一个多余，这一点其实跟智能电灯很像，大多时候，就算已经买了智能电灯，我们还是会用开关去控制电灯，但是总有些时候——比如进被窝早了懒得出来——你会特别想用意念把灯给关了。另外我偶尔会在看电影的时候睡着，过会儿又被吵醒，这时候就非常不想回到刺眼的屏幕下，敲几下键盘退出电影把系统睡眠，这时候就用得上睡眠或者静音这种命令了。你可能还没遇到这种情况，未必你永远不会遇到这种情况；你可能意志力很强大愿意冬天出被窝关灯或者在很困的时候爬起来敲键盘，那你就愿意吧，我不愿意，我愿意让我屋子里所有能发光的东西都能在手边儿就关上。

对于第二个多余，例子可以是用家庭共享控制 iTunes，或者是用 Spotify 的 App 通过 Airplay 在 Mac 上播放等等。但它们的问题是，不像遥控器，执行的过程不潇洒。你必须一步一步看一步一步点，因为它们的功能非常宽泛，就像支付宝的 App 一样，每个人都要其中的一两个功能，它就得把所有功能都做进去，对于一些追求简洁的人来说就乱，甚至难受。而通过 Launch Center Pro，你完全可以像使用遥控器一样，通过**[肌肉记忆](http://sspai.com/34961)**，执行你个人的需求。

给 Mac 配个遥控器没什么不好，尤其这遥控器还是自己为自己量身打造的。

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/BC6EF40F-D459-4D9B-A380-B1247B29CD6D/9441799B-737F-4FE8-ABA9-929DE697C8E6.jpg)](http://sspai.com/35108)

---

[🌐 原始链接](http://sspai.com/35242)

[📎 在印象笔记中打开](evernote:///view/207087/s1/66b8abfe-3d79-4a9b-9d28-4d62fab6c737/66b8abfe-3d79-4a9b-9d28-4d62fab6c737/)