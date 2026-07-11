# 【Karabiner 助力，让你的键盘操作快人一步】Karabiner 使用 JSON 作为配置文件配置繁琐且不易理解，有着不低的上手门槛。

---

【Karabiner 助力，让你的键盘操作快人一步】Karabiner 使用 JSON 作为配置文件配置繁琐且不易理解，有着不低的上手门槛。这篇文章教你玩转它。  (来自 @少数派sspai)

**Matrix 首页推荐**

[Matrix](https://sspai.com/matrix) 是少数派的写作社区，我们主张分享真实的产品体验，有实用价值的经验与思考。我们会不定期挑选 Matrix 最优质的文章，展示来自用户的最真实的体验和观点。

文章代表作者个人观点，少数派仅对标题和排版略作修改。

---

前言
--

Karabiner 全称 Karabiner-Elements，是 macOS 上的一款功能强劲的改键工具。它可以将键盘上的按键映射成其他一个或多个按键组合。然而，Karabiner 使用 JSON 作为配置文件，配置繁琐且不易理解，给上手带来了很高的门槛。

于是，有人专门为其制作了一个工具「Goku」，借助 Goku 可以方便地为 Karabiner 进行配置。

![](.evernote-content/385D43DB-D16B-4E74-B36A-A9E952DB6EE4/62A4B394-E85E-4F63-A749-7CAF798F8379.png)

上图展示了 Karabiner 中与 Goku 中，实现相同效果所需要的写法差异。

**准备工作：**

* Karabiner-Elements 可以从[官网](https://karabiner-elements.pqrs.org/)进行下载
* [Goku](https://github.com/yqrashawn/GokuRakuJoudo) 使用 Homebrew 进行安装：`brew install yqrashawn/goku/goku`
* 在 Karabiner 中确保配置文件 Profiles 选择默认的 Default
* 前往 `~/.config/`目录，创建名为 `karabiner.edn` 的 Goku 配置文件
* 参考下文进行配置文件的编辑，每次编辑完后在终端中执行 `goku` 使修改生效

将 Caps Lock 变为键盘功能的中枢
---------------------

通常，我们将 `⌃Control + ⌥Option + ⇧Shift + ⌘Command` 同时按下的组合称为 Hyper 键。通常程序内置的快捷键不会预设这么复杂的组合，因此使用 Hyper 键，能最大程度上避免与预设发生冲突。

大写锁定键 `Caps Lock` 位于键盘左侧中间，用起来很顺手，但我只用它切换输入法，输入大写字母靠 `⇧shift`，因此这里先对它下手，你也可以选择其他顺手且不常用的按键。

以下的 Goku 配置文件 `karabiner.edn` 写法，可以将大写锁定键修改为 Hyper 键，这时只需要按下这一个键，就等同于 `⌃Control + ⌥Option + ⇧Shift + ⌘Command` 同时按下的效果。

```
{
:main [
       {:des "caps_lock -> hyper"
         :rules [
                 [:##caps_lock :!CTOleft_shift]
                 ]}
       ]
}
```

然而，如果只是将 `Caps Lock` 转化为 Hyper 键，它会失去本身切换输入法的效果。幸好 Karabiner 支持在按键单独按下与组合按下时，为触发不同的效果。

以下写法可以让 `Caps Lock` 与其他键一同按下时触发 Hyper 键效果，单独按下时触发 `Control + Space` 切换输入法。

```
{
:main [
       {:des "caps_lock -> Ctrl+space(alone) and caps_lock -> hyper"
         :rules [
                 [:##caps_lock :!CTOleft_shift nil {:alone :!Tspacebar}]
                 ]}
       ]
}
```

以下是一些常用按键在 Goku 中的简化写法：

```
    ;; !  | means mandatory -   modifier(s) alone when pressend change behavior
    ;; #  | means optional  -   modifiers are optional (but at least one necessary)

    ;; :!Ca is keycode :a and prefix a with !C

    ;; C  | left_command
    ;; T  | left_control
    ;; O  | left_option
    ;; S  | left_shift
    ;; F  | fn
    ;; Q  | right_command
    ;; W  | right_control
    ;; E  | right_option
    ;; R  | right_shift

    ;; ## | optional any
    ;; !! | command + control + optional + shift (hyper)
```

要知道键盘上每个按键叫什么名字，可以使用 Karabiner 配套的 Karabiner-EventViewer 进行查看。

结合 Keyboard Maestro 实现快速搜索
--------------------------

单靠 Karabiner 只能发挥其一半的功力，要想发挥其全部实力，还是要与 Keyboard Maestro 或是 Alfred 这些支持自动化的工具搭档，才能强强联合。这里以 KM 为例，实现快速搜索选中内容的效果。

在 KM 中创建如下图的 Macro，为其指定 `Hyper + S` 的组合键，这样只需要选中想搜索的内容，按下快捷键即可使用 Google 进行搜索。

![](.evernote-content/385D43DB-D16B-4E74-B36A-A9E952DB6EE4/8544E1FB-C993-4033-B74D-29A288BB77F8.png)

同时，借助 KM 独特的冲突调色盘功能，当你为多个 Macro 设定了相同快捷键，按下快捷键后会触发选择界面，借此只需记忆一个快捷键，便可触发多种不同的搜索功能。

![](.evernote-content/385D43DB-D16B-4E74-B36A-A9E952DB6EE4/42246B1A-DF09-47D2-AA3D-D66D6E61930D.png)

Keyboard Maestro 的冲突调色盘

Hyper + 字母快速切换程序
----------------

日常使用时，经常要在不同的应用间来回切换。`Command + Tab` 虽然可行，但每次的应用顺序不固定，还要找到想切换到的程序，甚至因此诞生了一些专门为切换应用而生的工具。利用 Karabiner 搭配 Keyboard Maestro，即可实现 `Hyper + 字母` 一键切换应用。

在 Keyboard Maestro 中添加 Macro， 选择 `Activate a Specific Application` ，配置成下图所示，便可以在激活此 Macro 时切换到 Chrome。

![](.evernote-content/385D43DB-D16B-4E74-B36A-A9E952DB6EE4/7A3EC095-9633-49E7-8CCB-AECF6E1EF270.png)

这时，如果在 KM 中将 New Trigger 设置为按键的 `Hyper + C`，就可以开始使用了。

但这毕竟是一篇介绍 Karabiner 的文章，因此我演示一下如何在 Karabiner 的配置文件中，直接激活特定的 Macro。

以下配置文件可以实现 `Hyper + C` 切换到 Chrome 的效果。

```
{
:templates {:km "osascript -e 'tell application \"Keyboard Maestro Engine\" to do script \"%s\"'"
            }

:main [
       {:des "caps_lock -> Ctrl+space(alone) and caps_lock -> hyper"
         :rules [
                 [:##caps_lock :!CTOleft_shift nil {:alone :!Tspacebar}]

                 [:!!c [:km "open: chrome"] ] ;;caps+c open Chrome
                 
                 ]}
       ]
}
```

我在前面模板的基础上增加了两部分：

* 开头利用 `:templates` 创建了一个名为 `:km` 的脚本，可以快速激活 KM 中的 Macro
* 在 `:rules` 中新增加了一行规则，`:!!c` 表示 `Hyper + C` 的组合键，`:km "open: chrome"` 则表示调用前面创建的 `km` 脚本，并执行 `"open: chrome"` 这个 Macro

进阶，让每个键都能成为修饰键
--------------

`Hyper` 键只有一颗，用久了总有键位冲突不够用的那天，比如我既想用 `S` 键触发 Search，又想用它激活 Sorted 3。利用层（layer）的概念，可以让键盘上的每个键都能成为独一无二的修饰键。

所谓层，可以理解为按下某个键后，键盘上其他键的功能随之发生变化，例如下图就是按下 `option` 键后键盘的变化，我们可以称之为「option 层」。

![](.evernote-content/385D43DB-D16B-4E74-B36A-A9E952DB6EE4/F2A1A11E-C850-4334-BB39-91C320E32549.gif)

按下 `option` 后按键效果会整体发生变化

如下规则定义了一个称为「semicolon-mode」的层，在这里我将使用频率较低的分号`;`定义为触发按键：

```
{
:templates {:km "osascript -e 'tell application \"Keyboard Maestro Engine\" to do script \"%s\"'"
            }

:main [
       {:des "This is the semicolon-mode" 
         :rules [[:semicolon ["semicolon-mode" 1]  nil {:afterup ["semicolon-mode" 0] 
                                                 :alone :semicolon}] 

                [:hyphen [:km "insert: underline"] ["semicolon-mode" 1]]  
        ]}

       ]
}
```

* `:semicolon ["semicolon-mode" 1]` 指按下分号「semicolon」后，将变量 `semicolon-mode` 设置为 1，即进入「semicolon-mode」层
* `:afterup ["semicolon-mode" 0]` 指松开分号后，将变量 `semicolon-mode` 设置为 0，即退出「semicolon-mode」层
* 单独按下依然为分号本身 `:alone :semicolon`

在 `[:hyphen [:km "insert: underline"] ["semicolon-mode" 1]]` 这里，我定义了按下减号`-` ，触发 KM 中名为 `"insert: underline"` 的 Macro，输出一个下划线，这个规则只在`["semicolon-mode" 1]` 时（即按住分号时）才有效。

结语
--

> 花一些时间，折腾一点小东西，收获一个没多大用的成果，感到巨大的快乐。

这是我对摸鱼的定义。摸鱼摸得久了，总能折腾出些有意思的东西。现在我每天用这些快捷键输入一些常用短语，切换程序或是快速搜索，省下的时间可能没有多少，但是有种莫名的快乐，我觉得这就足够了。

相关文章
----

参考资料
----

**文章标题图片：**https://unsplash.com/photos/2xU7rYxsTiM

> 下载 [少数派 2.0 客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，解锁全新阅读体验 📰

> 实用、好用的 [正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

---

[🌐 原始链接](https://sspai.com/post/73827)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f15b205c-481b-408e-b98e-b812b1bdb4bf/f15b205c-481b-408e-b98e-b812b1bdb4bf/)