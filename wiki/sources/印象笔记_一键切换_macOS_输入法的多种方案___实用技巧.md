---
title: "一键切换 macOS 输入法的多种方案 _ 实用技巧"
type: source
created: 2026-07-15
updated: 2026-07-15
source_path: 印象笔记管理工具/一键切换 macOS 输入法的多种方案 _ 实用技巧.md
tags: [印象笔记]
---

# 一键切换 macOS 输入法的多种方案 _ 实用技巧

# 一键切换 macOS 输入法的多种方案 | 实用技巧 --- 一键切换 macOS 输入法的多种方案 | 实用技巧 ========================== | 本文为付费栏目文章，您

---

# 一键切换 macOS 输入法的多种方案 | 实用技巧

---

一键切换 macOS 输入法的多种方案 | 实用技巧
==========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

Windows 上的输入法大都可以使用 `⇧Shift` 来**切换中英文输入**，换到 Mac 却不怎么行得通，Mac 自带的中文输入法一直不能实现该功能。虽然苹果提供了类似的解决办法（使用 `⇪Caps Lock`，见下文），但是对于需要 Windows 和 Mac 一起用的用户来说，这多多少少有点不习惯。

恰巧前几天在 [Power+ 的 Slack 群里](https://sspai.com/article/51265?series_id=70)，看到有朋友提到了这方面的需求，所以本文就来解决这个问题。

除此之外，我想 Mac 输入法的另一个问题应该是**多个输入法间的切换**。由于 Mac 切换输入法只提供了「选择下一个输入法」和「选择上一个输入法」两个选项，而且输入法的顺序并不是固定的，而是根据最近使用来动态调整的，所以没办法靠肌肉记忆切换输入法。

如果使用了三个或以上的输入法，切换到我们想要的输入法时，有时需要两次按键，有时又只需要一次按键，并且每次切换时都要看一下右上角状态栏确认是否切换成功，实在太不友好。当然，也可以长按切换输入法快捷键，直到弹出键盘列表，但是我相信没有人愿意每次都等待那么长的时间。

对于多个输入法的情况，本文也会提供更便利的切换方法，让我们可以实现**精准切换**。

系统自带的中英文切换方案
------------

Mac 提供了使用 `⇪Caps Lock` 切换中英文的方案。我们要关注的是在「设置 – 键盘 – 输入法」选项卡中，「使用 Caps Lock 切换英文输入法」的选项。

没有勾选该选项时：

* 如果当前是中文输入：按下 `⇪Caps Lock`，仍然是中文输入法，但是切换到英文输入状态，再次按下回到中文输入。
* 如果当前是英文输入：按下 `⇪Caps Lock`，仍然是英文输入法，但是切换到大写锁定状态，再次按下回到小写状态。

虽然这个可以实现我们切换中英文的目的，但是由于仍然是中文输入法，所以我们无法通过状态栏的输入法图标，来判断目前的输入状态。

勾选该选项时，此时 `⇪Caps Lock` 相当于切换当前输入法和英文键盘的快捷键：

* 如果当前是中文输入：按下 `⇪Caps Lock`，切换到英文输入法，再次按下回到中文输入法，长按 `⇪Caps Lock` 切换到大写锁定状态。
* 如果当前是英文输入：按下 `⇪Caps Lock`，切换到英文输入法，再次按下回到中文输入法，长按 `⇪Caps Lock` 仍然是切换到大写锁定状态。

这种办法较好的实现快速切换中英文输入状态，并且可在状态栏快速查看到当前输入法状态，区别只是按键的不同。

使用 ⇧Shift 切换中英文
---------------

现在来看使用 `⇧Shift` 切换中英文的方案，我们需要用到 [Karabiner-Elements](https://pqrs.org/osx/karabiner/) 这款免费开源软件。Karabiner-Elements 是 Mac 上一款十分强大的改键软件，软件的详细介绍可以参考我之前写的《[macOS 改键利器：Karabiner-Elements 使用详解](https://sspai.com/article/46184?series_id=9)》（Power+ 1.0 文章），实现本文内容只需将提供的配置文件放入到指定目录。

⏬ **[点此下载配置文件](https://cdn.sspai.com/ee/%E4%BD%BF%E7%94%A8%20Shift%20%E5%88%87%E6%8D%A2%E4%B8%AD%E8%8B%B1%E6%96%87.zip)**

复制 `~/.config/karabiner/karabiner.json`，打开「访达」，在顶部状态栏点击「前往 - 前往文件夹」，粘贴路径前往后，使用下载好的 `karabiner.json` 文件替换掉默认的配置文件即可。

这时打开 Karabiner-Elements，在「Complex Modifications – Rules」选项卡下会有一条「Switching Keyboards Using Shift」的规则，代表我们已经成功了，大家可以随意按几下 `⇧Shift` 看一下效果。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/42AD5822-CEB6-45A7-9364-699EE7E6AF77.png)

已生效的规则

### 原理简介

配置文件可以使用文本编辑器打开，提供的配置文件只是在默认文件中的 `"rules": []` 添加了一些代码，结构如下：

```
{  
    "description": "Switching Keyboards Using Shift",  
    "manipulators": [  
        {…},  
        {…},  
        {…},  
        {…}  
    ]
}
```

`description` 显然就是规则名，重点是代码中有四个 `{…}`，这是为了清楚表示代码结构，将 `{}` 中的内容省略为了 `…`。虽然有四个 `{…}`，但是每个 `{…}` 中的内容只有细微差别，所以不必慌张，只要我们弄明白一个，所有的就都明白了。

我们想一下，按下 `⇧Shift` 切换中英文分为四种情况，分别是：

1. 按下左侧 `⇧Shift` 键，从中文切换到英文；
2. 按下左侧 `⇧Shift` 键，从英文切换到中文；
3. 按下右侧 `⇧Shift` 键，从中文切换到英文；
4. 按下右侧 `⇧Shift` 键，从英文切换到中文。

没错，这四个 `{…}` 分别对应这四种情况，从这四种情况也可以看出它们之间的差别并不大。现在我们以第 1 种情况为例，来看一下每个 `{…}` 的具体内容。

#### {…} 的具体内容

先来给出**按下左侧 `⇧Shift` 键，从中文切换到英文**的完整代码：

```
{  
    "conditions": [  
        {
            "input_sources": [  
                {
                    "language": "zh-Hans"  
                }
            ],  
            "type": "input_source_if"  
        }
    ],  
    "from": {  
        "key_code": "left_shift"  
    },  
    "to": [  
        {
            "key_code": "left_shift"  
        }
    ],  
    "to_if_alone": [  
        {
            "select_input_source": {  
                "input_source_id": "com.apple.keylayout.ABC"  
            }
        }  
    ],  
    "type": "basic"  
}
```

结构也很清楚：

1. `conditions` 部分：表示规则执行的条件
   * `input_sources` 部分：表示当前输入法的语言为 `zh-Hans`1
   * `type` 部分：`input_source_if` 表示肯定判断，结合 `input_sources` 部分即为如果当前输入法为中文时
2. `from` 部分：表示原始按键，如果按下左侧 `⇧Shift` 键时；
3. `to` 部分：表示目标按键，执行左侧 `⇧Shift` 键；
4. `to_if_alone` 部分：表示单独按下原始按键时，执行选择输入法操作，选择的输入法 ID 为 `com.apple.keylayout.ABC`2 ；
5. `type` 部分：总是 `basic`。

对照这部分代码，我们可以写出剩下的三种情况，以**按下左侧 `⇧Shift` 键，从英文切换到中文**为例，只需将 `conditions` 部分的 `zh-Hans` 改为 `en`，`to_if_alone` 部分的 ID 改为 `com.apple.inputmethod.SCIM.ITABC`。

```
{  
    "conditions": [  
        {
            "input_sources": [  
                {
                    "language": "en"  
                }
            ],  
            "type": "input_source_if"  
        }
    ],  
    "from": {  
        "key_code": "left_shift"  
    },  
    "to": [  
        {
            "key_code": "left_shift"  
        }
    ],  
    "to_if_alone": [  
        {
            "select_input_source": {  
                "input_source_id": "com.apple.inputmethod.SCIM.ITABC"  
            }
        }  
    ],  
    "type": "basic"  
}
```

至于按下右侧 `⇧Shift` 键的两种情况，只需将上述代码的 `from` 部分和 `to` 部分的 `left_shift` 改为 `right_shift` 即可。

#### 查找目标输入法的 ID

如果使用的不是系统自带的输入法，或是使用双拼输入法，同样可以实现一键切换。每一种输入法都有一个特定的 ID，我们可以通过这个 ID 来切换到该输入法，查找这个 ID 也很简单，利用安装 Karabiner-Elements 时附带的 EventViewer 就可快速查看。

打开 EventViewer 的 `「Variables」` 选项卡，在 `input_source` 中我们可以看到当前输入法的 `input_source_id` 和 `language`，分别表示其 ID 和语言。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/102E4F8F-9AFC-4B7B-A3D4-EC2C9840DD3D.gif)

查看当前输入法的 ID

找到 ID 后，只需将 `to_if_alone` 部分的 ID 更换为我们使用的输入法 ID 即可。

### 一些注意事项

上文我们提到每种情况都有 5 个部分，不过看起来我们只需要 `from`、`to_if_alone` 和 `type` 三部分就可以实现目的，那么 `conditions` 和 `to` 部分到底有什么用呢？

#### 使用 conditions 来细分情况

假如我们将 `conditions` 部分删除，那么我们当我们按下 `⇧Shift` 时，只能从中文输入法切换到英文，不能从英文切换到中文。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/71746045-5388-452A-9FCE-46C024492E19.gif)

只能从中文切换到英文，无法从英文切换到中文

这是因为 Karabiner-Elements 的逻辑，它默认从上往下执行，且只会执行第一个匹配到的情况。再删除 `conditions` 部分后，只要原始按键按下就匹配成功，所以无论按下哪侧 `⇧Shift` 时，第 2、4 种情况的代码根本没有机会运行，所以只会从中文切换到英文。

使用 `conditions` 后，我们为每种情况加入了一些限制条件，让它只在一定条件下满足。例如我们想要切换到英文输入法时，当前输入法应该是中文，这就是我们情况 1、3 的限制条件。当输入法为英文时，因为不匹配情况 1、3 的条件，所以继续测试情况 2、4，匹配成功，从英文切换到中文。

#### 使用 to 来保持修饰键的作用

如果将 `to` 部分删除，那么 `⇧Shift` 键就失去了作为修饰键的作用。这是由于我们只是告诉 Karabiner-Elements 按下 `⇧Shift` 时，切换输入法，并没有告诉它要执行什么按键，此时即使按下 `⇧Shift` 键也不会执行任何按键。

我们可以在 EventViewer 中测试一下，当我们按下 `⇧Shift` 时，可以看到确实切换了输入法，但是没有任何按键执行，自然无法再作为修饰键使用。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/3F3FC1D3-B913-449D-8B51-7A043B0A7D50.gif)

⇧Shift 只有切换输入法的作用

再加入 `to` 代码后，我们告诉了 Karabiner-Elements 按下哪侧 `⇧Shift` 后，执行相应的 `⇧Shift` 按键，于是修饰键的功能回来了。下图是加入 `to` 代码后 Eventviewer 的显示结果，可以发现除了输入法切换外，还监测到了相应的 `⇧Shift` 按键按下。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/C40C199A-17C3-4EF6-BEA2-00C983C8F55F.gif)

⇧Shift 恢复了修饰键的功能

多个输入法的精准切换
----------

现在我们以中日英三语键盘为例来看多个输入法的情况。我习惯使用键盘左侧的修饰键，很少用到右侧修饰键，所以我将右侧 `⌘Command`、`⌥Option` 和 `⇧Shift` 分别作为快速切换到中文，日文（平假名）和英文的快捷键，并仍保持它们的修饰键功能。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/6E5DC7F5-9B8E-41B6-9D3B-47D6521C8C5C.jpg)

用键盘右侧的修饰键来切换输入法

⏬ **[点此下载配置文件](https://cdn.sspai.com/ee/%E7%B2%BE%E5%87%86%E5%88%87%E6%8D%A2%E4%B8%AD%E6%97%A5%E8%8B%B1%E4%B8%89%E8%AF%AD%E9%94%AE%E7%9B%98.zip)**

同样只需替换掉 `~/.config/karabiner/karabiner.json` 路径下的原文件就可使用。

### 原理简介

这部分和使用 `⇧Shift` 切换中英文相似，也是在 `"rules": []` 中添加了相同结构的代码，只是 `{…}` 中的内容稍有不同，我们具体来看。

根据我们的想法，有三种情况：

1. 按下右侧 `⌘Command` 键，从非中文切换到中文；
2. 按下右侧 `⇧Shift` 键，从非英文切换到英文。
3. 按下右侧 `⌥Option` 键，从非日文切换到日文；

可以看出，与切换中英文最大的差别在于条件判断（即 `conditions` 部分）。在切换中英文时，我们使用的是肯定判断类型（`"type": "input_source_if"`），如果当前输入法是中文 / 英文时；现在我们需要使用否定判断类型（`"type": "input_source_unless"`），如果当前输入法不是中文 / 日文 / 英文时。

#### 每种情况的完整代码

首先来看情况 1，按下右侧 `⌘Command` 切换到中文：

```
{  
    "conditions": [  
        {
            "input_sources": [  
                {
                    "language": "zh-Hans"  
                }
            ],  
            "type": "input_source_unless"  
        }
    ],  
    "from": {  
        "key_code": "right_command"  
    },  
    "to": [  
        {
            "key_code": "right_command"  
        }
    ],  
    "to_if_alone": [  
        {
            "select_input_source": {  
                "input_source_id": "com.apple.inputmethod.SCIM.ITABC"  
            }
        }  
    ],  
    "type": "basic"  
}
```

同样是 5 个部分：

1. `conditions` 部分：表示规则执行的条件
   * `input_sources` 部分：表示当前输入法的语言为 `zh-Hans`
   * `type` 部分：`input_source_unless` 表示否定判断，结合 `input_sources` 部分即为如果当前输入法非中文时
2. `from` 部分：表示原始按键，如果按下右侧 `⌘Command` 键时；
3. `to` 部分：表示目标按键，执行右侧 `⌘Command` 键；
4. `to_if_alone` 部分：表示单独按下原始按键时，执行选择输入法操作，选择的输入法 ID 为 `com.apple.inputmethod.SCIM.ITABC`；
5. `type` 部分：总是 `basic`。

对比情况 1，我们可以很快写出情况 2、3 的内容。再以情况 3（按下右侧 `⌥Option` 切换到日文）为例，我们打开 EventViewer 确定日文（平假名）输入法的语言代码和 ID。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/AB81A0C3-73FD-4033-8CCB-6DBCFB631901.png)

日文输入法的语言代码和 ID

由图可以看出，语言代码为 `ja`，平假名键盘的 ID 为 `com.apple.inputmethod.Kotoeri.Japanese`，所以情况 3 的完整代码为：

```
{  
    "conditions": [  
        {
            "input_sources": [  
                {
                    "language": "ja"  
                }
            ],  
            "type": "input_source_unless"  
        }
    ],  
    "from": {  
        "key_code": "right_option"  
    },  
    "to": [  
        {
            "key_code": "right_option"  
        }
    ],  
    "to_if_alone": [  
        {
            "select_input_source": {  
                "input_source_id": "com.apple.inputmethod.Kotoeri.Japanese"  
            }
        }  
    ],  
    "type": "basic"  
}
```

自定义快速切换到指定输入法的快捷键
-----------------

如果三个输入法仍然满足不了你 ，Karabiner-Elements 还可以让我们自定义按键。只需要在 `from` 部分指定你想要的按键和修饰键，我们以使用 `⇧Shift-⌥Option-K` 切换到日语的片假名键盘为例。

`from` 部分代码为：

```
"from": {  
    "key_code": "k",  
    "modifiers": {  
        "mandatory": [  
            "shift",  
            "option"  
        ]
    }  
}
```

由于我们需要用到 `⇧Shift` 和 `⌥Option` 等修饰键，并且我们只需要切换输入法，不需要 Karabiner-Elements 执行任何按键，所以我们不再需要 `to_if_alone` 部分，只保留 `to` 部分，综上，`to` 部分代码为：

```
"to": [  
    {
        "select_input_source": {  
            "input_source_id": "com.apple.inputmethod.Kotoeri.Japanese.Katakana"  
        }
    }  
]
```

至于 `conditions` 部分和上面基本相同，不再赘述。需要说明的是，虽然本文全部以 `language` 作为 `conditions` 的条件，但是 Karabiner-Elements 并不局限于此，我们也可以使用输入法 ID（`input_source_id`）作为判断条件，来实现如果不是 A 输入法，则切换到 A 输入法的效果。

![](.evernote-content/FCD33084-5A06-4CA3-AE87-78BC57AC3743/13C3FB16-D1C9-4F3E-8868-60DB68EBF24E.gif)

使用自定义的快捷键切换输入法

可以看出，当我们按下 `⇧Shift` 和 `⌥Option` 键时，EventViewer 确实监测到了相应按键；再我们按下 `K` 键后，输入法切换成功，但是 EventViewer 没有监测到 `K` 键的按下，正是我们想要的效果。

结语
--

切换输入法看似是件小事，但是不顺手的切换方式却会破坏我们的输入体验。做好这件小事并不费力，只需一点点的时间就可以换来长久的畅快输入，何乐而不为。

虽然本文所举的例子都是系统输入法，但是鼠须管、搜狗之类的第三方输入法也是适用的，只需找到它们相应的 ID 即可。

优化切换方案时，我们首先要有个具体的想法，细分每种情况，对每种情况的条件是什么，原始按键是什么，执行动作是什么有一个明确的认识，清楚了这些，让 Karabiner-Elements 来实现就很简单了。

1. [表示中文，下文会介绍如何查找语言代码。↩](#)
2. [这个 ID 表示 Mac 的英文输入法，下文会介绍如何找到这个 ID。↩](#)

---

[🌐 原始链接](https://sspai.com/post/52964)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c9fd8527-4b79-4be6-95ab-83e1b7baf7fa/c9fd8527-4b79-4be6-95ab-83e1b7baf7fa/)