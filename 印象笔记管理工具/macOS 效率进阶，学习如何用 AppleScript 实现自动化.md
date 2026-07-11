# macOS 效率进阶，学习如何用 AppleScript 实现自动化

---

听 [Yvesss](https://sspai.com/user/63) 老师的建议修改了标题，原标题：「快速上手 macOS GUI Scripting: 基于 UI 元素的系统自动化控制」。

GUI Scripting 可以帮助你实现如下图一样的效果：打开记账软件，并在其中进行复杂繁琐的自动化录入操作——几乎所有点击操作都在瞬间完成。过程中，我实际进行的操作只有：激活这个脚本、输入消费金额和消费内容而已。

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/6F0465D6-4F1F-4E27-B8D5-2C53902F9F3E.gif)在 Money Pro 中录入一次消费

GUI Scripting 的原理很简单，就是利用脚本语言模拟鼠标键盘操作，进而控制系统 UI 元素。比如说，点击窗口中的某个按钮、在某个文本框里输入信息、以及获取窗口内特定区域的文本等等。这些可能单调繁琐的工作，你都可以用 GUI Scripting 来解放双手，实现无延迟的自动化。

本文介绍的是 macOS 下的 GUI Scripting，macOS 系统中提供了现成的脚本语言 AppleScript，以及及其轻量化的原生 IDE 「脚本编辑器」，无需任何准备就能轻易上手。下面我就以动图中控制 Money Pro 为例，向你介绍 GUI Scripting 的基本方法。我相信读完文章后，你可以完全掌握常见 UI 元素的自动化控制。

扩展阅读：不仅是 macOS，Windows 下也有 GUI Scripting，在少数派的[这篇文章](https://sspai.com/post/43305)里有具体介绍。

AppleScript 基础
--------------

首先需要介绍几点 AppleScript 基础，它们太基本了，实在无法绕过，希望你可以耐心读完，如果有任何问题也可以在评论中提出，我会一一解答。这里介绍所有代码你均可在「脚本编辑器」里测试。

#### 1. 「告诉 xxx 做某事」的俄罗斯套娃结构

AppleScript 的语法非常接近自然语言，想要操控一个应用（application）做某件事，只要直接「告诉」它就好了。

```
tell application "Money Pro"
    activate -- 告诉 Money Pro，让它激活自己
end tell
```

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/D4CE2880-94F5-425C-8B89-6E96F2ED0239.png)UI 元素层级

然而，如果想要用 `tell` 访问某一个 UI 元素，必须按上图中的层级结构，一层一层按顺序进行访问：System Events 是最外围的框架 → Money Pro（具体某个应用）→ window 1（该应用的第1个窗口）→ button 1（窗口中的第1个按钮）。**理解和掌握这种层级关系，是进行 GUI Scripting 非常关键的一步。**

System Events 是系统应用（application），要「告诉」它做某事，AppleScript 要这么写，

```
tell application "System Events"
    -- 你希望应用 System Events 做的事
end tell
```

所有带 UI 结构的应用，都是 System Events 下的进程（process），包括 Money Pro。如果我要「告诉」Money Pro 做某事，因为它是套在 System Events 之内的，就要这么写

```
tell application "System Events"
    tell process "Money Pro"
        -- 你希望进程 Money Pro 做的事
    end tell
end tell
```

再进一步，我们要控制 Money Pro 的第一个窗口，就是

```
tell application "System Events"
    tell process "Money Pro"
        tell window 1
            -- 你希望 window 1 做的事
        end tell 
    end tell
end tell
```

以此类推，你可以无限 `tell` 下去，

```
tell application "System Events"
    tell process "Money Pro"
        tell window 1
            tell something
                tell something
                    tell something
                        -- System Events: 你他喵的够了
                    end tell
                end tell
            end tell
        end tell
    end tell
end tell
```

我们需要控制的 UI 元素一般藏在比较深的层级中，它们的完整描述都很长。拿下图中的「软件」菜单项举例，这个例子将会会贯穿全文。

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/21AF16EC-7561-4A80-B8AB-B02BC87F0136.png)「软件」菜单项

图中被选中的这个「软件」菜单项的完整描述是「Money Pro 应用中的第一个窗口中的第一个可滚动区域中的第一个表单中的第二列中的第一个 UI 元素中的第一个弹出菜单按钮的第一个弹出菜单中的菜单项“买买买”的第一个菜单中的“软件”菜单项」，在 AppleScript 中就是

```
menu item "软件" of menu 1 of menu item "买买买" of menu 1 of pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 of window 1 of process "Money Pro" of application "System Events"
```

其实这就是一句十分生硬、表示从属关系的英文，相比于中文「xxx中的xxx」，英文则是「of」，且关系倒置——子级在先，父级在后。至于我为什么知道是第 1 个按钮 button 1 而不是 button 2 或 button 3，这将作为重要内容在下一节详细说明。

#### 2. 小憩片刻

运行 AppleScript 时，如果你需要暂停片刻，那么就用

```
delay 0.5   -- 以秒为单位
```

#### 3. 注释

AppleScript 中凡是双短线 `--` 和井号 `#` 后的内容都会被认为是注释，不会被执行。

```
-- 这是一条注释
# 这也是一条注释
```

#### 4. 模拟键盘操作

键盘的模拟操作也需在 System Events 内进行。

你可以用 `keystroke` 来模拟键盘操作键入一串字符，

```
keystroke "一串字符"
```

也可以用 `key code` 来实现单键操作，比如利用

```
key code 53
```

来模拟点击键盘上的 Escape 键。完整的键位代码你可以在[这里](https://eastmanreference.com/complete-list-of-applescript-key-codes/)找到。

如何定位 UI 元素，获取它的完整描述
-------------------

这一节将重点说明如何去获取一个 UI 元素。紧接着上文 Money Pro 的例子——关于我����是如何获得那个「软件」菜单项的 AppleScript 完整描述。

对于毫无经验的我们，其策略就是，先获取整个应用内所有 UI 元素，然后缩小范围（比如该应用第 x 个窗口），再然后再凭直觉筛选出一些可能是目标元素的语句，逐个试验它们，最终定位目标 UI 元素。

#### 1. 获取一个区域内的所有 UI 元素

**任何一个 UI 元素，只有在软件当前的界面中存在，才能被获取和使用。一个获取失败的例子：没有被呼出的菜单里的内容，是无法被获取的。**

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/17A74616-76FB-48AF-9940-AF13516EDF89.png)右图中「软件」菜单项可以被获取和操作，而左图不行

用 AppleScript 获取某个区域内所有 UI 元素只需两个单词 `entire contents`。

例如，利用

```
tell application "System Events"
    tell process "Money Pro" -- 告诉 Money Pro
        entire contents -- 获取所有 UI 元素
    end tell
end tell
```

你就会得到 Money Pro 这整个应用所有的 UI 元素的**完整描述**，甚至是顶部菜单栏中的内容。UI 元素之间被逗号隔开。

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/7EBC1B7C-AEE9-4FC0-BB55-13BA7E3FEAE3.png)运行结果中数量多到令人窒息的 UI 元素

如果你需要进一步缩小范围，比如我不想看菜单栏的内容，那就再套一层 `tell window 1` 2 的语句：

```
tell application "System Events"
    tell process "Money Pro" -- 告诉 Money Pro
        tell window 1 -- 再告诉 Money Pro 的第一个窗口
            entire contents -- 获取所有 UI 元素
        end tell
    end tell
end tell
```

你就会得到内容比之前少一些，但同样很多的 UI 元素。

#### 2. 筛选可能是目标 UI 元素的内容

不同 UI 元素的筛选方法各不相同，似乎没有捷径。

如果这个元素有名称，比如菜单项显示的文字，那就直接查找这个文字！比如对于那个菜单项「软件」，如果你搜「软件」，直接就能定位到。

但并非所有开发者都会好好地给 UI 元素起名字，或者出于设计考虑，会刻意隐去名称，比如哪些`scroll area`就没有名字，而是用一个序号来标识 `scroll area 1`。在这种你搜不了名字的情况下，你还可以用这样一个经验性规律——脚本运行结果中的所有 UI 元素是按软件界面中**从上到下，从左到右的顺序排列**的。所以你可以查找它附近的元素，然后在这个元素前后用肉眼识别。

你还可能遇到不熟悉的 UI 元素类型（比如不确定一个按钮的类型该是 `button`，还是 `radio button`），你可以利用原生应用「Accessibility Inspector」去审查它，它长这个样子，Spotlight 一搜就能搜到：

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/16DC1B40-AE3B-48C6-8312-DCC56C744D59.png)Accessibility Inspector

点击上面那个「瞄准」按钮，就能用鼠标指针查看 99% UI 元素的信息，其中包含了 UI 元素的种类（Type）。

![](.evernote-content/71B116EB-B787-4021-AF70-35691264C237/474C81F8-D2A2-40F8-84E3-368045D70B4F.png)鼠标指向「2160p 4K」按钮后的效果

获取目标 UI 元素的过程看起来，复杂可怕，但只要敢于尝试，成功那么一两次，你就会变得经验老道了。

定位 UI 元素之后可以做什么？
----------------

#### 1. 如果是按钮或者菜单项，你可以在 AppleScript 里模拟点击 `click` 它，比如点击之前那个「软件」菜单项。

```
tell application "System Events"
    tell process "Money Pro"
        click menu item "软件" of menu 1 of menu item "买买买" of menu 1 of pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 of window 1 -- of process "Money Pro" of application "System Events"
    end tell
end tell
```

因为我们处在进程 Money Pro 的 `tell` 中，所以需要注释掉后面 `of process "Money Pro" of application "System Events"` 的部分。

#### 2. 如果是文本输入框，你可以设置文本框内容。

```
set value of text field 1 of ... to "一些文本内容"
```

也可以设置激活该输入框的光标，

```
set value of attribute "AXFocused" of text field 1 of ... to true
```

利用这些操作你可以逐个试验你定位到的元素，以最终确定哪一个是目标元素。由于篇幅限制，本篇文章无法涵盖所有 UI 元素的可控属性，需要了解更多请查阅 UI 元素的对应文档。但对我而言，能够实现图标点击、菜单项点击，文本框内容输入就完全足够了。

让我们来点击这个「软件」菜单项
---------------

前文说到，只有显示出来的 UI 元素才能被获取和操作，所以要想点击「软件」这个菜单项，我必须先让「软件」这个菜单项显示出来，于是我必须选中「买买买」这个菜单项。让「买买买」菜单项显出出来，我又必须点击「类别」按钮弹出类别菜单。「类别」按钮又是处在 Money Pro 新建面板中的。所以整个操作流程应该是

1. 打开 Money Pro 主窗口
2. 点击右上角的 + 号按钮，弹出新建面板
3. 点击面板上的「类别」按钮，弹出类别菜单
4. 选择「买买买」
5. 再选「软件」

从第 2 步开始每一步都是一次 UI 元素的操控命令。你必须先获取 + 号按钮的 AppleScript 描述，然后用 `click` 操作点击它；再获取「类别」按钮的描述，点击它；再获取「买买买」菜单项的描述，点击它，最后获取「软件」菜单项的描述，点击它。

完整的 AppleScript 脚本是

```
#激活 Money Pro
tell application "Money Pro" to activate

tell application "System Events"
    tell process "Money Pro"
        #点击 + 号按钮
        click button 2 of group 1 of group 1 of group 1 of window 1
        #暂停 0.3 秒，等待新建面板出现
        delay 0.3
        #点击「类别」按钮
        click pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 of window 1
        #选中「买买买」菜单项
        click menu item "买买买" of menu 1 of pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 of window 1
        #点击「软件」菜单项
        click menu item "软件" of menu 1 of menu item "买买买" of menu 1 of pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 of window 1
    end tell
end tell
```

值得一提的小事
-------

### 如何使用 UI 元素的描述语句，取决于所处层级

你可能已经注意到了，只要处于某个层级内部，对一个 UI 元素进行操作使用的并不是它的完整描述。

还是拿点击那个「软件」菜单项为例，我们是这样写的：

```
tell application "System Events"
    tell process "Money Pro"
        click menu item "软件" of menu 1 of menu item "买买买" of menu 1 of pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 of window 1 -- of process "Money Pro" of application "System Events"
    end tell
end tell
```

但你也可以这样写：

```
tell application "System Events"
    tell process "Money Pro"
        tell window 1
        click menu item "软件" of menu 1 of menu item "买买买" of menu 1 of pop up button 1 of UI element 1 of row 2 of table 1 of scroll area 1 -- of window 1 of process "Money Pro" of application "System Events"        end tell
    end tell
end tell
```

后者里，我多套了一个 `tell window 1` 的结构，所以 `click` 事件里就不必要把 `of window 1` 包括进去了，因为 `click` 事件已处于 window 1 的层级内了。

我这里提供一个最丧病的写法，可能可以促进理解，但实际编写时不具备参考价值

```
tell application "System Events"
  tell process "Money Pro"
    tell window 1
      tell scroll area 1
        tell table 1
          tell row 2
            tell UI element 1
              tell pop up button 1
                tell menu 1
                  tell menu item "买买买"
                    tell menu 1
                      tell menu item "软件"
                        click
                      end tell
                    end tell
                  end tell
                end tell
              end tell
            end tell
          end tell
        end tell
      end tell
    end tell
  end tell
end tell
```

### 两次 click 事件之间的延迟问题

正常情况下你无法快速点击两次菜单项——两次 `click` 事件之间会被强行插入一个 5 秒左右的延迟。这是 macOS 的保护机制，为了应用的 UI 反馈能够被成功接收。但是 5 秒的延迟太长太不讲道理了。

所幸的是，Stack Overflow 里的[这篇帖子](https://stackoverflow.com/questions/21270264/speed-up-applescript-ui-scripting?answertab=active#tab-top)提供了一个有效解决方案。

简言之就是先忽略第一次点击按钮后应用的 UI 反馈：

```
ignoring application responses
    -- 这里是你的第一次点击操作
    click button 1
end ignoring
```

然后在 System Events 的 `tell` 语句外面杀掉 System Events 进程：

```
delay 0.1
do shell script "killall System\ Events"
```

然后正常进行第二次点击操作。

完整语句是这样：

```
tell application "System Events"
    tell process "Reeder"
        ignoring application responses --忽略应用的反馈
            click button 1 of window "Day One 2"
        end ignoring
    end tell
end tell

-- 杀掉 System Events 应用
delay 0.1 --自定义 UI 反馈的等待时间为0.1 秒
do shell script "killall System\ Events"

tell application "System Events"
    tell process "Reeder"
        -- 第二次点击操作
    end tell
end tell
```

### \*检测屏幕内容2

一套自动化流程必定包含许多操作，这些操作之间会有不可避免的等待时间。比如，等待一个应用的主窗口打开。最简单的方法是自己估计所需的时间，然后用 `delay`语句让 AppleScript 暂停一会儿。然而为了 AppleScript 能够有效执行，等待时间需比实际时间要长，这样就不效率了！

更效率的方法，是让 AppleScript 自己知道什么时候主窗口出现了。

```
tell application "Safari" to activate --打开 Safari
tell application "System Events"
    tell process "Safari"
        repeat until window 1 exists
            -- 直到 Safari 应用的一个窗口存在之前，不停循环这段空语句
        end repeat
        -- 第一个窗口出现之后，继续要做的事……
    end tell
end tell
```

除了让 AppleScript 自己检测窗口的存在，你还可以检测应用的弹窗内容是不是符合一些特定条件。这就要你自己发挥想象力了。

### \*AppleScript 的封装

最后一步，你也可以借助一些支持 AppleScript 的第三方应用来封装你的脚本，比如 [Alfred](https://sspai.com/search/article?q=Alfred)、[Keyboard Maestro](https://sspai.com/search/article?q=Keyboard%20Maestro) 等，本文的第一幅动图中我把记账的录入 AppleScript 变成了 Keyboard Maestro 里的一个按钮，点击这个按钮就能执行该脚本。

### \*GUI Scripting 的一个优点

对 UI 元素进行控制时，并不要求该 UI 元素呈现在屏幕上，即使一个按钮被其他窗口挡住了，脚本里对它进行的点击操作也能顺利进行。所以，理论上执行 AppleScript 脚本时，你可以不受干扰地继续在电脑上做其他工作。

尾巴
--

欢迎评论指出文中未阐述清楚、产生混淆之处。

---

> 下载 [少数派 iOS 客户端](http://sspai.com/s/nqQk)、关注 [少数派公众号](http://sspai.com/s/KEPQ)，让智能设备更好用 💪

---

[🌐 原始链接](http://sspai.com/post/43758)

[📎 在印象笔记中打开](evernote:///view/207087/s1/e9c82db7-ab29-413c-ad89-3aba46dcfa51/e9c82db7-ab29-413c-ad89-3aba46dcfa51/)