# macOS 改键利器：Karabiner-Elements 使用详解

---

macOS 改键利器：Karabiner-Elements 使用详解
==================================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

键盘上总有一些按键是我们不常用的，比如说 `Caps Lock` 。但偏偏它还占据着键盘上非常好的位置，相比之下，更常用的 `Esc` 的位置却比较难够到。一直以来，注重效率的人，都会把这两个键调换位置。

不仅如此，为了设置一个和任何应用都不冲突的快捷键，大家往往会用 `⌃Control + ⌥Option + ⇧Shift + ⌘Command` 的组合，它也被称为 Hyper 键。虽然这个组合看起来很难按，但我们实际上可以用一个键代替这个组合。

要做到上面说的这两点，就需要**改键**。通过改键，我们不仅能分别做到这两点，我们还可以做到。当我们单次按下 `Caps Lock` 时，它的功能是 `Esc` 但是当我们按下 `Caps Lock` 并且再按其它键，也就是拿 `Caps Lock` 当作修饰键时，它又可以直接代替 `⌃Control + ⌥Option + ⇧Shift + ⌘Command` 的组合，称为 Hyper 键。

这篇文章将教会大家使用改键工具 Karabiner-Elements 做到这两点，并且为大家展示这个工具的其它核心功能。

Karabiner-Elements 适用于 macOS 10.12+，即 macOS Sierra 以及之后的系统。Sierra 之前的系统改键建议使用 Karabiner，参考 [潜水的科技猫](https://sspai.com/user/720817/posts) 的《[⌃Control + ⌥Option + ⇧Shift + ⌘Command：带你玩转 macOS 的修饰键](https://sspai.com/post/39331)》一文。

安装步骤
----

首先下载 [Karabiner-Elements](https://pqrs.org/osx/karabiner/files/Karabiner-Elements-12.1.0.dmg)，安装过程中会提示输入密码，键入密码后很快便完成安装。或者使用 [Homebrew](https://brew.sh/index_zh-cn)，在「终端」中输入 `brew cask install karabiner-elements` 命令即可。

安装完成后会出现两个应用，Karabiner-Elements（简称「KE」，下同）和 Karabiner-EventViewer（简称「EventViewer」，下同）。KE 是我们使用的主要应用；EventViewer 则是一个辅助应用，除了可以查看改键效果，还可以帮助我们确定**按键名称**（即下文代码中的 **`key_code`**）以及各种参数。

第一次打开 KE 会出现一个弹窗，提示我们系统阻止了 KE 的内核扩展。这是因为 KE 直接作用于底层硬件，所以需要我们手动允许。按照提示，点击「Open System Preferences - Security & Privacy」跳转到设置界面，再点击「允许」即可。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/F5B4DA60-254A-4C9D-8AF8-39E01C617497.png)

解除系统对 KE 内核扩展的阻止

继续回到 KE，这时会出现「键盘设置助理」，这是为了让 KE 识别我们使用的键盘类型，按照提示完成后，我们就可以开始使用 KE 了。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/8D386770-66B7-47AD-95B1-27783415FE64.png)

出现键盘设置助理

创建一个简单映射
--------

在这部分，我将为大家介绍如何使用 KE 将 `Caps Lock` 改为 `Esc`。

在开始介绍之前，为了避免引起歧义，我们来做一些约定：

* 将我们实际按下的按键称作**原始按键**；
* 将我们真正想执行的按键称作**目标按键**；
* 将原始按键改为目标按键这一用法，称为一条**映射**。

我们要将 `Caps Lock` 改为 `Esc`，那么称：

* `Caps Lock` 为原始按键；
* `Esc` 为目标按键；
* 这是一条将 `Caps Lock` 改为 `Esc` 的映射。

想要实现这条映射也很简单，打开 KE，在「Simple Modifications（简单映射）」下，点击左下角「Add item（添加映射）」，然后在「from key（即原始按键）」中选择 `Caps Lock`，在「to key（即目标按键）」中选择 `Esc`，我们的第一条映射就创建成功了。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/A12D5439-D29F-4665-BEB6-AF7548624ED7.png)

添加一个简单映射

选择好后，我们按一下 `Caps Lock`，用来指示 `Caps Lock` 状态的小绿灯不会亮起；再按一下 `Esc`，这次小绿灯亮了起来，证明我们改键成功。

简单映射里只能进行一些基础改键，并不能发挥出 KE 真正的实力，复杂映射才是 KE 的魅力所在。

创建一个复杂映射
--------

用 Mac 的人慢慢都会培养起快捷键的习惯，很多人刚接触 Mac 就会被 `⌘Command` 键吸引。也正因为如此，基本上容易按到的快捷键，都已经被各种软件使用了。

所以人们就在想，怎么样搞一个快捷键组合，能和谁都不冲突？一个终极答案就是拿 `⌃Control + ⌥Option + ⇧Shift + ⌘Command` 的组合键作为修饰键，不会和其他任何应用的快捷键冲突。

但我们也发现，同时按下这四个按键实在是太难了，所以我们需要用 KE 来帮助我们，把这 4 个键映射到 1 个键上。相当于我们按下这一个键，就相当于按下了这 4 个键。

### 导入复杂映射

这个做法和之前的简单映射有所不同，属于复杂映射。所以我们需要切换到「Complex Modifications（复杂映射）」选项卡，这里有两个选项卡，「Rules（映射 1 ）」和「Parameters（参数）」。我们暂时不看「参数」，先看「映射」。

界面左下角仍有「Add rule（添加映射）」，但点击后只能导入开发者制作好的映射，并不能让我们自由地添加映射。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/260BEA66-38DB-417D-AD7D-21ACF55812CA.png)

如何导入映射

图中黑色框中「Change caps\_lock to command+control+option+shift.」就是我们想要的映射。

因为现在我们要把 `Caps Lock` 改为 `Hyper` 键，和刚才把 `Caps Lock` 改为 `Esc` 的做法冲突，所以目前需要删除我们刚才在「简单映射」中创建的映射，再点击「Enable（启用）」启用这条映射。

### 使用 EventViewer 来检查效果

打开 EventViewer 后，我们随便敲几个字母，可以发现 EventViewer 会记录我们的每一次按键。比如我们依次按下 `Q`、`W`、`E` 键，结果如图。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/D62795B6-4260-4B38-8854-425D82B84A2F.png)

依次敲下 Q、W、E 键

然后我们按下 `Caps Lock`，结果如图。这就代表我们改键成功了。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/EC610EEE-4555-49F8-ADC7-D670FC088EB0.png)

按下 Caps Lock 实现组合键

创建一个进阶的复杂映射
-----------

现在，我们要把两者融合，做到：

* 单独按下 Caps Lock 时，让它作为 Esc 键。

* 按住 Caps Lock 并按其它键时，让它作为 Hyper 键，也就是 `⌃Control + ⌥Option + ⇧Shift + ⌘Command` 的组合。

要做到这点，就要进行更高的自定义，所以还是要先删除刚才的配置，把我们在「复杂映射」里启用的映射给删除。

### 修改 KE 配置文件

我们先来看一下创建自定义复杂映射的全过程，其中的代码解释我们在下一节中展开。

因为 KE 界面没有提供给我们自己创建映射的办法，所以我们通过修改 KE 配置文件实现我们的目标。

KE 配置文件是 `karabiner.json`，默认路径是 `~/.config/karabiner/karabiner.json`。复制好路径后，打开「访达」，在顶部状态栏点击「前往 - 前往文件夹」，粘贴路径前往后就找到了 KE 配置文件。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/170F5E0A-D0D2-4733-95E8-0866CE97C9EC.png)

配置文件位置

为避免直接修改原文件，我们将其拷贝到「下载」文件夹中，然后使用「文本编辑器」打开。虽然看起来很复杂，但其实我们需要关注的只是红色方框部分。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/8B99D008-0603-47FE-BFE9-A07C8A060B4A.png)

只需将代码粘贴在 [] 中即可

只需复制下文中提供的代码，粘贴到红色方框中方括号 `[]` 里，我们就完成了 KE 配置文件的修改。这里是修改后的配置文件 [karabiner.json](https://cl.ly/2m1t2d0t423q/download/karabiner.json)，大家可以参考，也可以拿来直接使用。

```
{  
    "description": "Change Caps Lock to Hyper",  
    "manipulators": [  
        {
            "from": {  
                "key_code": "caps_lock",  
                "modifiers": {  
                    "optional": [  
                        "any"  
                    ]
                }  
            },  
            "to_if_alone": [  
                {
                    "key_code": "escape"  
                }
            ],  
            "to_if_held_down": [  
                {
                    "key_code": "left_shift",  
                    "modifiers": [  
                        "left_command",  
                        "left_control",  
                        "left_option"  
                    ]
                }  
            ],  
            "type": "basic"  
        }
    ]  
}
```

复制修改后的 `karabiner.json`，前往 `~/.config/karabiner/karabiner.json`，替换原文件，至此，我们成功创建了自己的复杂映射。再次打开 KE，可以发现「映射」里多出了「Change Caps Lock to Hyper」映射，我们将其简称为映射 1。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/9CE3D1DD-FC68-4354-A723-C1A6C3E45624.png)

成功创建了 Caps Lock 到 Hyper 的映射

打开 EventViewer 后，首先短按 `Caps Lock` 键，最后长按 `Caps Lock` 键，结果如图。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/3AB9AF2F-4D53-40E5-9196-1F3BCA390434.png)

测试改键效果

### 通过「参数」优化体验

如果经过 EventViewer 的测试后，发现想要实现组合键时，需要长按很长时间，那么我们可以通过调整参数来优化体验。

切换到「复杂映射」下的「参数」选项卡，这里有四条参数，我们只需关注前两条参数。因为我们将按下 `Caps Lock` 键分为了短按和长按，所以我们需要告诉 KE 多长时间内是短按，超过多长时间是长按，这两条参数就是控制这些时间的。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/DF4741A2-B2A8-46FA-AD8F-E5527ECE04AA.png)

两条需要关注的参数

* `to_if_alone_timeout_milliseconds`：用来控制短按时间，按键时间在该数值以内属于短按；
* `to_if_held_down_threshold_milliseconds`：用来控制长按时间，按键时间在该数值以上属于长按。

这些参数默认单位都是毫秒，设置时只要保证短按时间小于等于长按时间即可。我习惯全部设置为 `200` 毫秒，大家可以利用 EventViewer 多做尝试，找到适合自己的阈值。

代码解释
----

在配置文件中，像 `parameters` 和 `rules` 这些字符两边必须添加 `""`，下文中为了写作方便不再添加。现在，我们来看一下，添加在配置文件中的代码究竟是什么。

### complex\_modifications 代码

再来看一下这张图片，在之前的基础上，我又添加了黄色方框和蓝色方框。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/BEEB6DA9-F912-4C9C-88E1-6B44B99FF6CA.jpg)

complex\_modifications 代码

蓝色方框标记的地方，即 `"complex_modifications": {}` 部分，正如名称所言，复杂映射中的所有内容，全部包含在这段代码中。

对照图片可以看出，`"complex_modifications": {}` 中代码分为两部分：

* **`"parameters": {}`**：图中用黄色方框标出；
* **`"rules": []`**：图中用红色方框标出。

显然，这和 KE 界面中，「复杂映射」下的「参数」和「映射」对应了起来。

既然黄色方框中 `"parameters": {}` 代码可以直接在「参数」选项卡里修改，那么我们只需关注红色方框中负责「映射」代码的 `"rules": []` 即可。

我们添加的所有映射，正是包含在 `"rules": []` 中。

### rules 代码

现在我们来看实际添加的代码。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/DB83E18A-9453-4459-BBEE-D11A7F539B33.png)

实际添加在配置文件中的代码

对照图片蓝色方框部分，我们可以看出，在 `rules: []` 中包含一段代码，对应我们添加的映射 1。

对照图片黄色方框部分，我们可以看出，映射 1 也有两部分，分别是：

* **`description`**：映射简介，用来描述映射作用。
* **`manipulators`**：映射内容，用来指定映射具体执行什么内容。

其中，`description` 中的内容会显示在「映射」选项卡下，帮助我们确定每一条映射是什么，可以简单的理解为，为我们的映射取个名字。我们的重点内容则是在 `manipulators` 下。

### manipulators 代码

对照图片红色方框部分，我们可以看出，在每段 `manipulators` 下有三个部分，分别是：

* **`from`**：输入部分，用来告诉 KE 监测哪些按键被按下，即我们的原始按键。
* **`to…`**：2 输出部分，用来告诉 KE 执行哪些按键，即我们的目标按键。
* **`type`**：映射类型，所有映射类型均为 `basic`。

我们使用到的 `to…` 代码有两种类型，分别是：

* **`to_if_alone`**：短按 3 原始按键时，KE 要执行的动作；
* **`to_if_held_down`**：长按原始按键时，KE 要执行的动作；

知道这些后，如何写代码告诉 KE 我们想要的效果，会有一个大致的思路。比如我们的映射 1，大致思路就是：

1. 利用 `from` 中代码告诉 KE 监测是否按下原始按键 `Caps Lock`；
2. 利用 `to_if_alone` 中代码告诉 KE 短按原始按键时输出目标按键 `Esc`；
3. 利用 `to_if_helf_down` 中代码告诉 KE 长按原始按键时输出目标按键组合键。

很简单对不对？剩下的问题就是如何让 KE 明白，我们的原始按键和目标按键是什么。这就是 `key_code` 和 `modifiers` 的作用。

### key\_code 代码

`key_code` 是按键名称，用来告诉 KE 要监测和执行的按键是什么。`key_code` 可以在 EventViewer 中查看。比如按下左侧 `⇧Shift`，EventViewer 中 name 一栏显示的 `left_shift` 就是左侧 `⇧Shift` 的 `key_code`。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/80451321-FAA5-4DE5-A82C-D3046979AA22.png)

左侧 ⇧Shift 的 key\_code

仍以映射 1 为例，确定了原始按键和目标按键以后，只需在 `from` 和 `to…` 中分别加入 `key_code` 即可。

* **原始按键**：在 `from` 中添加 `key_code: caps_lock`；
* **目标按键**：在 `to_if_alone` 中添加 `key_code: escape`。

  ```
  “from”: {  

   “key_code”: “caps_lock”,  

  },  

  “to_if_alone”: [  

   {
   “key_code”: “escape”  

   }
  ],
  ```

这时我们会发现一个问题，长按 `Caps Lock` 想要实现的组合键，该如何表示呢？这就需要 `modifiers` 了。

### modifiers 代码

`modifiers` 是修饰键，用来配合 `key_code`。如果只有 `key_code` 可用，那么 KE 只能监测或者输出一个按键，不能实现更多效果，就像我们的映射 1，但是配合上 `modifiers` 就不同了，我们一起来看。

#### from 中的修饰键

在 `from` 代码中，共有三种修饰键情况：

* **没有 `modifiers`** ：只有单独按下 `key_code` 才触发代码；
* **`mandatory` 选项**：只有该修饰键和 `key_code` 按下才触发代码；
* **`option` 选项**：该修饰键是可选的，有没有按下它不影响代码匹配情况。

比如我们只想监测 `⌥Option + Q` 的组合键，`Q` 单独按下时不做反应。这种情况下 `⌥Option` 是必须的，所以在 `from` 中的代码就应该是：

```
"key_code": "q",  
"modifiers": {  
    "mandatory": ["option"]  
}
```

另外，因为 q 有大小写之分（即打开 `Caps Lock` 时），我们想不论大小写都监测成功，那么我们还需添加上 `optional: caps_lock` 的选项：

```
"key_code": "q",  
"modifiers": {  
    "mandatory": ["option"],  
    "optional": ["caps_lock"]  
}
```

除了一般的按键名称外，`optional` 还有一个特殊值 `any`，`optional: [any]` 表示任何修饰键都是可选的。我们的映射 1 就添加了 `optional: [any]` 代码，用来扩大使用范围。

#### to… 中的修饰键

在 `to…` 代码中，`modifiers` 则很简单了，直接添加就可以。

这里有一个小细节，如果我们想要 `⌘Command` 作为修饰键，在 `modifiers` 中，我们不可以直接写 `command`，而是要随便指定为左侧或右侧 `⌘Command` 的 `key_code`。

比如映射 1 想要实现的组合键，就可以这样写。

```
"key_code": "left_shift",  
"modifiers": [  
    "left_command",  
    "left_control",  
    "left_option"  
]
```

### 复习代码

我们已经将使用到的所有代码学完了，现在我们总的来看一下映射 1 输入输出部分的代码，检查我们是否看得懂它在说什么。

```
"from": {  
    "key_code": "caps_lock",  
    "modifiers": {  
        "optional": [  
            "any"  
        ]
    }  
},  
"to_if_alone": [  
    {
        "key_code": "escape"  
    }
],  
"to_if_held_down": [  
    {
        "key_code": "left_shift",  
        "modifiers": [  
            "left_command",  
            "left_control",  
            "left_option"  
        ]
    }  
],
```

由输入部分看出，这条映射监测的是 `Caps Lock` 键，修饰键可以任意。

由输出部分看出，KE 分别监测 `Caps Lock` 的短按和长按行为。短按的话，执行 `Esc` 按键操作；长按的话，在左侧 `⌘Command`、`⌃Control`、`⌥Option` 的修饰下，执行左侧 `⇧Shift` 按键操作，即组合键。

映射的优先级
------

现在我们已经将 `Caps Lock` 改为 `Hyper` 键了，不过考虑到我们偶尔需要用到 `Caps Lock`，所以将 `Esc` 改为 `Caps Lock`。

这是一个简单映射，我们直接在「简单映射」里添加好后，打开 EventViewer 检验一下。当我们按下 `Esc` 时，出现的结果并不是我们期待的 `Caps Lock`，而是 `Esc`；当我们长按 `Esc` 时，发现却是组合键的效果。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/28C6F430-6A84-4034-BE45-0C70BB5228E2.png)

并不是我们想要的结果

这是因为 KE 并不会判断我们的目标按键究竟是什么，只会先运行「简单映射」，再运行「复杂映射」。所以当我们按下 `Esc` 时，「简单映射」首先起作用，将 `Esc` 改为 `Caps Lock`。但是 KE 并不是直接执行 `Caps Lock` 动作，而是将其继续发送到「复杂映射」中，这就相当于我们直接按下的是 `Caps Lock`，所以出现上图这种情况。

所以为避免带来不必要的麻烦，当「简单映射」和「复杂映射」中的按键存在某种联系时，不要在「简单映射」中添加映射，而是添加在「复杂映射」里。这同样很简单，只不过这次输出部分使用新的 `to` 4 代码而已。

下面给出将 `Esc` 改为 `Caps Lock` 的映射完整代码，简称为映射 2，相信大家都可以看明白。

```
{  
    "description": "Change Esc to Caps Lock",  
    "manipulators": [  
        {
            "from": {  
                "key_code": "escape",  
                "modifiers": {  
                    "optional": [  
                        "any"  
                    ]
                }  
            },  
            "to": [  
                {
                    "key_code": "caps_lock"  
                }
            ],  
            "type": "basic"  
        }
    ]  
}
```

进阶代码
----

看到这里，大家应该发现，「复杂映射」里并没有「目标设备」这一选项，如果我们想要针对某个设备来改键的话该怎么办呢？KE 仍然可以做到。

### 为复杂映射添加目标设备

我们以映射 2 为例，只想让它作用在我的外置键盘上。这相当于为映射 2 添加了一个条件，只有在条件满足的时候才起作用。

在 KE 代码中，条件是用 `conditions` 控制的。常用的 `conditions` 类型有 `device（设备）`、`variable（变量）` 等，这里我们使用设备变量。

`device` 条件结构包括两部分：

* **`type`**：类型，有两种，`device_if` 5 和 `device_unless`6 ；
* **`identifiers`**：设备需要满足的条件。

可以发现，我们只需要找到外置键盘的识别条件，然后填写在 `identifiers` 里，条件代码部分就完成了。

而我们想要的识别条件同样方便查找。连接好我们的外置键盘后，打开 KE 的「Devices（设备）」选项卡，KE 已经成功识别我们的设备。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/CE62F49F-DBA0-4017-9384-24062C845BBD.png)

找到 Vendor ID

在红色标记中找到外置键盘的 Vendor ID，图中为 3727，该数值，这就是我们要找的条件。一般情况下，我们只需要 Vendor ID 或者 Product ID 中的一个即可。

至于图中蓝色标记，如果勾中选项，那么设备连接到 Mac 后，Mac 内置键盘将不再起作用，只有靠外置键盘输入；将设备断开或者取消勾选后，Mac 键盘恢复。

我们已经找到了 `identifiers` 的内容，现在根据 `device` 的结构将整个代码写出。Vendor ID 的值不需要加 `""`。

```
"conditions": [  
    {
        "type": "device_if",  
        "identifiers": [  
            {
                "vendor_id": 3727  
            }
        ]  
    }
]
```

写好后，将这段代码添加在映射 2 输出部分的最后，另外，因为 JSON 的数据结构，需要在上一行结尾加一个英文逗号 `,`。这样，我们就为映射 2 添加了一个条件，使其只作用在外置键盘上。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/CB8BE030-1886-4D62-B467-216E0DE04929.png)

完整代码

### 实现双击按键

看过了 `device` 条件，我们再来看 `variable` 条件。我们以映射 3：双击右侧 `⇧Shift` 改为 `Mission Control` 7 为例。

`variable` 条件的结构有三部分：

* **`type`**：类型，有两种，`variable_if` 和 `variable_unless`；
* **`name`**：变量名，通过 `set _variable` 设置；
* **`value`**：变量值。

除此之外，我们还要学习一个新的输出动作，`to_delayed_action（延迟动作）`，它在原始按键按下 500 毫米 8 后开始执行，包括两种情况：

* **`to_if_invoked`**：除了原始按键，没有其他按键按下时执行的动作。
* **`to_if_canceled`**：按下其他按键时执行的动作。

我们对照映射 3 中，`manipulators` 的完整代码来学习，共分为两段代码。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/C03B7BAC-74AA-4484-889C-D7D6353A8BE9.png)

映射 3 代码部分

当第一次按右侧 `⇧Shift` 时，红色方框中代码，不满足变量 `right_shift pressed` 值为 1，所以不执行该段代码，转而开始进行蓝色方框中代码测试；满足蓝色方框，设定变量 `right_shift pressed` 值为 1，并输出一次右侧 `⇧Shift`。

此时，有两种情况，我们分别来看。

**立刻再次按下右侧 `⇧Shift` 时**

若 500 毫秒内再次按下右侧 `⇧Shift`，变量 `right_shift pressed` 值仍为 1，所以红色框中代码执行，输出 `misson_control` 键。500 毫秒后，`to_if_invoked` 动作执行，将变量 `right_shift pressed` 值清零。

**不按或者按下其他键时**

若 500 毫秒内按下其他按键，或者超过 500 毫秒后，`to_if_canceled` 动作执行，变量 `right_shift pressed` 值为 0，即使再次按下右侧 `⇧Shift`，也只是再次执行蓝色方框中代码。

KE 的应用界面
--------

KE 的应用界面一共有 7 个选项卡。常用的除了「简单映射」和「复杂映射」，还有「Profiles（配置）」和「Misc（杂项）」。

在「配置」里，我们可以创建多个配置，在每个配置里改键互不干扰。

比如创建游戏、办公两个配置。游戏配置里 `Caps Lock` 改为技能释放键 9 ，办公配置中则将 `Caps Lock` 改为 `Esc`。使用时可以通过状态栏快速切换到相应配置。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/71196E4F-677C-4C5C-8571-6A07CDD2D90F.png)

菜单栏切换配置

在「杂项」中，只需注意「System Default Configuration」。默认情况下，Karabiner-Elements 修改的键位只会作用在当前用户下，更改用户后仍然是系统默认键位。

![](.evernote-content/9976A7F0-0892-4C3B-B231-40BF4E87788E/F4904647-6111-4443-ACAB-2ACD671F47F2.png)

作用到该电脑的所有用户

点击「Copy the current configuration to the system default configuration」后，Karabiner-Elements 将作用在该电脑所有用户上。

结语
--

说起 Mac 上改键，有一个开发者是绕不开的，他就是 [@tekezo](https://github.com/tekezo)。

从最早开发的 KeyRemap4MacBook，到更名后的 Karabiner，每个都是精且专的改键利器。macOS Sierra 更新后，因为系统底层的变动使得 Karabiner 无法继续在新系统下工作，作者转而开始 Karabiner-Elements 的开发。

改键的需求并不会随着系统更新而减弱。在等待 Karabiner-Elements 开发的过程中，不少人开始寻找替代方案，不论是使用 Hammerspoon 还是 Keyboard Maestro 都比 Karabiner 少了点简洁。如今，不断开发的 Karabiner-Elements 已经足够强大，足以满足我们日常的改键需求，改键再次只需这一个软件。

虽然 Karabiner-Elements 只能通过配置文件来增添复杂映射，但实际代码并不复杂，需要我们掌握的只是 `from` 和 `to…` 部分。与其能带给我们的便利相比，花费一点点时间去掌握其写法是非常值得的。

最后在这里做一个简单总结，当我们想要创建一个复杂映射时：

1. 确定输入部分原始按键，修饰键；
2. 确定监控原始按键的哪些行为；
3. 根据行为确定输出部分共有几段；
4. 在每段行为里，写入目标按键。

完成这四步后，只需粘贴在配置文件中，Karabiner-Elements 便会立即按照我们的想法开始工作了。

1. [Rule 单词意思为规则，这里为避免歧义，引申为映射。↩](#)
2. [包括 to\_if\_alone、to\_if\_held\_down，这里用 to… 统称。↩](#)
3. [事实上，这条代码是当原始按键单独按下时，KE 要执行的动作。但因为这条代码有个很短的时间限制（即上文中的短按参数），超时后该代码将不再运行，所以我们利用它实现短按原始按键这种情况。↩](#)
4. [按下 —— 不论短按或是长按 —— 原始按键时，KE 要执行的动作。↩](#)
5. [只在该设备上工作。↩](#)
6. [不在该设备上工作。↩](#)
7. [即 F3 键。↩](#)
8. [可在「参数」里调节。↩](#)
9. [灵感来自 Minja《让键盘变成你想要的样子：改键利器 Karabiner-Elements》一文 https://sspai.com/post/42921↩](#)

[#使用详解](https://sspai.com/tag/%E4%BD%BF%E7%94%A8%E8%AF%A6%E8%A7%A3)[#键盘](https://sspai.com/tag/%E9%94%AE%E7%9B%98)

---

[🌐 原始链接](https://sspai.com/post/46184)

[📎 在印象笔记中打开](evernote:///view/207087/s1/2c23c083-efa4-4f81-92b1-cff7c3333515/2c23c083-efa4-4f81-92b1-cff7c3333515/)