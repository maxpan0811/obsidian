# 法律人的Claude Code教程（二）（教不会我吃民法典！）：十分钟掌握核心操作

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=MzkzMjg2NTcxNA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485775&idx=1&sn=ed1138eb730f4dc22440ed8ec360ae95&chksm=c2547a92f523f384ba66f9b9c08aaa33e635111d6c57cb31be92530c1e3704f1d62e6393a074&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQOTQC7QGX2OxbQpo/14tN0xLVAQIE97dBBAEAAAAAAMwrAKpvdtsAAAAOpnltbLcz9gKNyK89dVj04Z50mavMFuYGeqOBtbJ/I9oCKlnv2cdQfW/V2d5Eqz1sshttjEjIGNMnaEGTB4nDSKAyRN2MMjhNPRuj9CU7y4M+1ftOCOqDYLnXumQYkVSq4JvBI/jVBRQTX9Z7FIW1E3SsROWfG18wuKID8iOQNc+Rx2bklIujeg2KM4VF5pN7f/86F7Lmcs+bryHhHlNW9Y2ImLHOjiCiIWAZGIruwaptEHgAJyAqVkyIOcnFPA==&pass_ticket=YWvdUN0EleMbIM3UK608GOqpXbf/7agQIUoz4DdVjR5sssIB6xcUihWvxFoIYNYg&wx_header=3)

法律人的Claude Code教程（二）（教不会我吃民法典！）：十分钟掌握核心操作
=========================================

Original积成 智律积成

上一篇教程，我们一起把 Claude Code 装好了。

[法律人的Claude Code教程（一）（教不会我吃民法典！）：安装与配置](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485751&idx=1&sn=33d24ddf860b6bdfd0fb9211a4cb979c&scene=21#wechat_redirect)

但我猜，你现在可能正处于这样的状态：

* 打开终端，输入 `claude`，看到一堆信息就懵了
* 不知道在哪个文件夹启动才对
* 问了几个问题，但不知道怎么让它帮忙处理文件
* 想导出结果，但不知道用什么命令

***我都装好了，为什么还是不知道怎么用？***

说实话，这很正常。

**Claude Code 和你之前用过的任何 AI 工具都不一样——它不是网页，不是聊天框，而是一个真正能读写你电脑文件的"律师助理"。**

既然是助理，你得先学会怎么"指挥"它。

这篇教程就做一件事：**让你从"装好了"变成"会用了"。**

---

先搞清楚一件事：你在哪里启动，它就在哪里工作
----------------------

这可能是 Claude Code 最重要、也最容易被忽略的概念。

***工作目录 = 你打开的案件档案袋***

每个案子你都会有一个独立的文件夹：

📁 案件A - 张三诉李四借贷纠纷/
   ├── 起诉状草稿.md
   ├── 证据清单.xlsx
   └── 借条扫描件.pdf
📁 案件B - 公司合同审查/
   ├── 采购合同.docx
   └── 审查意见.md

你在案件 A 的文件夹里启动 Claude Code，它就只能处理案件 A 的材料。

这样设计很好理解：

* 不会把案件 A 的意见写进案件 B 的文件
* 不会误删其他案子的文件
* 每个案子的工作是隔离的

那怎么在指定文件夹启动呢？

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/9D41D1D1-D749-47C5-8C45-CBA9B01DA108.png)

**Mac 用户**：右键（或触摸板双指）- "新建位于文件夹位置的终端窗口"

**Windows 用户**：

* Windows 10：Shift + 右键 - "在此处打开 PowerShell 窗口"
* Windows 11：直接右键 - "在终端中打开"

然后在终端里输入 `claude`，工作目录就自动设置好了。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/E7D3172E-2F8D-4326-83FF-E4193F354048.png)

---

有更快的启动方式吗？
----------

如果你每次都要"打开文件夹 - 右键 - 打开终端 - 输入 claude"，确实有点烦。

我有个朋友，每次都把 "claude" 打成 "cluade"，后来他找了个更简单的方法：

**点击文件夹里的一个图标，直接进入 Claude Code**。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/703822B4-828D-4E1E-BEC1-37ED9A847754.png)

这个工具叫 "Claude Code Now"，橘子老师做的，在 claudecodenow.com 有详细的设置教程。

如果你每天都要用 Claude Code，这个工具确实能省不少时间。

当然，如果你习惯用 VS Code，也可以在里面装个 "Claude Code for VS Code" 插件，效果一样。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/42E8853A-996D-43A2-9205-08A5B1F7E101.png)

---

启动之后，怎么和它"说话"？
--------------

Claude Code 启动后，你会看到一个简洁的对话框，直接输入问题就行。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/CF25154D-1B5D-40E7-86BA-0E0F914511CC.png)

**有什么问题直接问，不用客气。**

民间借贷的诉讼时效是多久？

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/27ADCCDD-2896-4E8A-B268-7A412CFA55B8.png)

但真正让 Claude Code 发挥价值的，是三个特殊操作符：

| 操作符 | 名称 | 作用 | 示例 | 优先级 |
| --- | --- | --- | --- | --- |
| `/` | 斜杠命令 | 调用内置命令 | `/help`、`/clear` | ⭐⭐⭐ |
| `@` | 文件引用 | 让 Claude Code 读取文件 | `@合同.docx` | ⭐⭐⭐ |
| `!` | Bash 命令 | 执行系统命令 | `!ls`、`!pwd` | 知道就行 |

前两个必学，第三个可以不管。

`@`**引用文件**，这是你以后最常用的操作：

@样本合同.docx 审查违约责任条款

你也可以直接**拖拽文件**到 Claude Code 窗口，效果一样。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/A7A31A40-1E3D-4D5D-B7F8-1E911D4B6299.png)

`!`**执行命令**，有时候你想快速看看文件夹里有什么：

!ls# 查看当前目录有哪些文件
!pwd# 确认当前位置

***法律场景****：案件文件夹里有几十个文件，用*`!ls`*快速看看都有什么*

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/70CC5985-EBFF-4539-B84D-460E02CE4E5A.png)

---

问题很长，想分几行写？
-----------

有两种方法：

**方法一：反斜杠换行（所有终端通用）**

输入 `\` 然后按 `Enter`，既换行了又不会发送消息：

请帮我审查这份采购合同，重点检查：\
1. 付款条件是否对我方有利\
2. 违约责任是否对等\
3. 争议解决方式是否合适

写完后直接按 `Enter` 发送。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/8430A46D-25D1-4B77-ADE2-EB3BC7941273.png)

**方法二：Shift+Enter（部分终端）**

如果你用的是 iTerm2、WezTerm、Ghostty、Kitty，可以直接用 `Shift+Enter` 换行。

如果是其他终端（VS Code、Alacritty），先运行 `/terminal-setup` 安装绑定。

看不懂就不管，记住方法一就够了。

---

Claude Code 说太多了，怎么打断它？
-----------------------

按 `Esc` 键。

就像对实习生说"停，先不用说了"。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/645B15D7-4301-44FB-AA3F-31FD17CFA19E.png)

中断后你可以：

* 重新说清楚你的问题
* 转向其他话题
* 结束对话

---

最实用的功能：它能"看"图片
--------------

这对法律人太重要了——扫描件、截图、照片，统统能分析。

**Mac 用户**：

* 快捷键：`Ctrl+V`（大多数终端）或 `Cmd+V`（iTerm2）
* 截图：`Cmd+Shift+4` 选区截图
* 粘贴：在 Claude Code 里按 `Ctrl+V`

**Windows 用户**：

* 快捷键：`Alt+V`
* 截图：`Win+Shift+S`

**最简单的方法**：直接把图片文件**拖到 Claude Code 窗口**里。

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/939E9D80-9C1E-4DAE-A462-D07DF6B13C24.png)

***法律场景****：拿到一份扫描件合同，直接截图丢给 Claude Code 分析*

---

用图片还有这些技巧
---------

可以连续粘贴多张图片，Claude Code 会一起分析。

也可以同时发图片和文字说明，比如"这张图是合同第3页，帮我看违约金条款"。

截图快捷键记一下：Mac 用 `Cmd+Shift+4`，Windows 用 `Win+Shift+S`。

---

它的回答，怎么变成文件？
------------

有三种方法：

**方法一：直接让 Claude Code 生成文件（最推荐）**

直接告诉它"保存为文件"：

把这份审查意见保存为"合同审查意见.md"

把起诉状保存为"起诉状.docx"

Claude Code 会自动创建文件，你可以在工作目录找到它。

**方法二：/export 导出对话**

如果想保存完整的对话记录（包括你的问题和 Claude Code 的回答）：

| 命令 | 效果 |
| --- | --- |
| `/export` | 导出到剪贴板 |
| `/export 对话记录.md` | 导出到文件 |

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/0009572B-31DA-46E1-8766-D3E766327C80.png)

**使用场景**：保留与 Claude Code 的完整对话过程，方便后续查看或分享。

**方法三：直接复制**

最简单的方式——用鼠标选中文字，`Cmd+C` / `Ctrl+C` 复制。

---

几个必须记住的快捷键
----------

不用记太多，这 5 个就够用了：

| 快捷键 | 作用 | 什么时候用 | 优先级 |
| --- | --- | --- | --- |
| `Enter` | 发送消息 | 写完了，发出去 | ⭐⭐⭐ |
| `\` + `Enter` | 多行输入 | 问题很长，分几行写 | ⭐⭐⭐ |
| `Esc` | 中断生成 | Claude Code 说太多了，打断它 | ⭐⭐⭐ |
| `↑` / `↓` | 查看历史 | 重新编辑之前发的问题 | ⭐⭐⭐ |
| `Ctrl+L` | 清屏 | 屏幕太乱，清干净 | ⭐⭐ |

***说明****：*`Tab`*补全建议是 Claude Code 的智能提示，按了就接受，一般用不到。其他快捷键对法律人来说太程序员化，不用管。*

---

几个最常用的命令
--------

Claude Code 有一些内置命令，用 `/` 开头，就像微信的小程序入口。

**/help — 不会就问它**

忘记命令了？直接输入 `/help`，所有可用的命令都会列出来。

***法律场景****：你记得有个命令是关于导出的，但忘了具体是*`/export`*还是*`/save`*，打*`/help`*搜一下就知道了*

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/EB31A8A9-32AC-4CAA-A14D-96C43484A56E.png)

**/clear — 清空对话，重新开始**

有时候聊跑偏了，或者想换个新案子，直接清空对话历史。

***法律场景****：刚审完一份租赁合同，现在要审一份买卖合同，用*`/clear`*清空，避免上下文混淆*

**/compact — 对话太长？给它瘦身**

对话太长会影响响应速度和费用，`/compact` 会帮你压缩对话，保留关键信息。

***法律场景****：审一份 50 页的合同，来回聊了半天，对话变得很长。用*`/compact`*瘦身一下，让 Claude Code 聚焦在当前问题*

**/status — 看看当前状态**

查看你的账户、当前使用的模型、连接状态等信息。

***法律场景****：Claude Code 响应变慢了，不知道是网络问题还是模型问题，用*`/status`*检查一下*

**/model — 切换模型**

在不同的 AI 模型之间切换（如 Sonnet、Opus、Haiku）。

***法律场景****：*

* **Haiku**：简单快速问答，比如"诉讼时效是多久"
* **Sonnet**：日常合同审查、文书起草（推荐）
* **Opus**：复杂案情分析、疑难法律问题

**/resume — 找回上次没聊完的对话**

按 ID 或名称恢复之前的对话，不用重新说一遍背景。

***法律场景****：昨天下午在审一份并购协议，没聊完就下班了。今天用*`/resume`*找回昨天的对话，接着昨天的地方继续*

![](.evernote-content/D5F5F87A-8E56-4A35-B162-2FB41EA558F6/26313EED-1F9C-47F5-B63F-8D2F81B9F7D9.png)

---

一张速查表，贴在显示器旁边
-------------

打印出来，随用随查：

| 命令 | 作用 | 说明 |
| --- | --- | --- |
| `/help` | 查看帮助 | 不知道怎么用？先打这个 |
| `/clear` | 清空当前对话 | 对话太长、想重新开始时用 |
| `/compact` | 压缩上下文 | 对话太长快爆了？用这个瘦身 |
| `/status` | 查看状态 | 当前账户、模型、用量信息 |
| `/doctor` | 诊断问题 | Claude Code 出毛病了？让它自查 |
| `/model` | 切换模型 | 在不同模型之间切换 |
| `/resume` | 恢复对话 | 找回上次没聊完的对话 |
| `/init` | 初始化案件文件夹 | 在当前目录生成 CLAUDE.md 记录案件背景 |
| `/export` | 导出对话 | 保存对话记录到文件或剪贴板 |
| `/plan` | 进入规划模式 | 复杂任务先规划思路再执行 |
| `/rewind` | 回退对话/代码 | 改错了？回退到之前的状态 |
| `/stats` | 查看使用统计 | 看看自己的使用习惯和每日用量 |
| `/exit` | 退出 Claude Code | 用完了，退出程序 |
| `/config` | 配置设置 | 修改 Claude Code 的各项设置 |
| `Esc` | 中断生成 | Claude Code 说太多了？按 Esc 打断它 |
| `\` + `Enter` | 换行 | 输入多行内容时使用（通用方法） |

---

学会了这些，接下来做什么？
-------------

你现在已经掌握了 Claude Code 的核心操作：

* 在正确的文件夹启动它
* 用 `@` 引用文件，用 `/` 调用命令
* 用 `\` + `Enter` 换行，用 `Esc` 中断
* 粘贴图片让它分析扫描件
* 用 `/export` 导出对话记录

**但这只是开始。**

真正让 Claude Code 发挥价值的，是下一篇要讲的内容：**工作模式与权限管理**。

就像开车有 D 档、R 档、N 档，Claude Code 也有不同的"档位"——

* 什么时候该让它自动执行？
* 什么事必须让你确认？
* 复杂任务怎么先规划再动手？

掌握了这些，你才算真正把 Claude Code 用到了"律师助理"的程度。

---

很多法律人并不是不愿意用 AI，

而是：

* 不想反复折腾
* 不想每次都从零开始
* 不想把时间浪费在"重复说明"和"人工整理"上

Claude Code 的价值就在于：

***它让 AI 的使用方式，真正贴近了法律人的工作习惯。***

***下一篇，我们来聊聊"档位"的事。***

---

我也在持续分享更多法律 AI 的实践经验和工具，都会发布在公众号里。

如果你想一起交流、共建，

无论是使用、改进，还是自己动手做法律 AI 应用，都非常欢迎加入我们的群聊。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=MzkzMjg2NTcxNA==&mid=2247485775&idx=1&sn=ed1138eb730f4dc22440ed8ec360ae95&chksm=c2547a92f523f384ba66f9b9c08aaa33e635111d6c57cb31be92530c1e3704f1d62e6393a074&cur_album_id=4406622888632549382&scene=189&ascene=3&devicetype=iOS26.4.1&version=18004725&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQOTQC7QGX2OxbQpo/14tN0xLVAQIE97dBBAEAAAAAAMwrAKpvdtsAAAAOpnltbLcz9gKNyK89dVj04Z50mavMFuYGeqOBtbJ/I9oCKlnv2cdQfW/V2d5Eqz1sshttjEjIGNMnaEGTB4nDSKAyRN2MMjhNPRuj9CU7y4M+1ftOCOqDYLnXumQYkVSq4JvBI/jVBRQTX9Z7FIW1E3SsROWfG18wuKID8iOQNc+Rx2bklIujeg2KM4VF5pN7f/86F7Lmcs+bryHhHlNW9Y2ImLHOjiCiIWAZGIruwaptEHgAJyAqVkyIOcnFPA==&pass_ticket=YWvdUN0EleMbIM3UK608GOqpXbf/7agQIUoz4DdVjR5sssIB6xcUihWvxFoIYNYg&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/bc49fa3e-f559-4992-a579-741ea7deb29a/bc49fa3e-f559-4992-a579-741ea7deb29a/)