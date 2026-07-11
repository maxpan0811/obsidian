# 在 iOS 和 macOS 下更准确地统计文章字数

---

在 iOS 和 macOS 下更准确地统计文章字数
=========================

| 本文为付费栏目文章，您已订阅，可阅读全文 |

写作对于大多数人来说都是日常需要接触的活动。而对于一些略微特别的职业和样式，比如学生论文、有字数要求的文案等等，我们就会时不时地用到字数统计的功能。

对于写作者来说，统计字数则有着更多的意义：它不仅可以记录一个作者每日的工作量，还可以判断（按字结算的）稿费是否给足了（笑）。

统计字数的功能 Word 做的是最靠谱的，也是普遍的参考标准。但是，大多数愿意使用 Markdown 的人们正是对 Word 有着各种不满才使用了轻量的标记语言。单纯为了查字数去买 Word、或者任何一个编辑器，都会有牛鼎烹鸡之感。

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/E5F20DB2-69F5-4C42-8001-A654C2FA26C2.png)

Word 和 Ulysses 统计结果差距很大

为了更简单地了解写作情况，也为了不让字数统计限定我的写作工具，我通过一个简单的 js 脚本实现了让我满意的字数统计（下面是 LaunchBar 版本的效果）。

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/ED0C1D77-C22D-44FD-9C71-9A597B877302.png)

LaunchBar 版的统计效果

你可以下载适合自己的版本：

* [Automator 版下载](https://github.com/BlackwinMin/sspai-sample-script/blob/master/Automator/%E7%BB%9F%E8%AE%A1%E5%AD%97%E6%95%B0.workflow.zip)
* [LaunchBar 版下载](https://github.com/BlackwinMin/sspai-sample-script/blob/master/LaunchBar/Text%20Counter.lbaction.zip)
* [Drafts 版下载](https://drafts4-actions.agiletortoise.com/a/2Ob)（4、5 通用）

统计原理
----

一般我们统计字数都会以 [Word](https://support.office.com/en-us/article/show-the-word-count-and-more-3c9e6a11-a04d-43b4-977c-563a0e0d5da3) 为准，因为它可以在中英文混输的时候精确地区分英文单词、中文、标点符号等，作出精确统计。

但是遗憾的是，Word 统计字数的规则微软官方似乎没有公开。于是我根据我的思路制定了如下规则，比大多数其它工具统计字数更加可靠：

* 1 个汉字，比如 `派` 算 1 个字；
* 1 个英文**单词**，比如 `Power` 算 1 个字；
* 1 个**全角**标点，比如 `。` 算 1 个字；
* 2 个**半角**标点，比如 `.` 算 0.5 个字；
* 1 组数字，比如 `60` 算 1 个字；
* 空格不计。

Automator 版
-----------

利用原生的 Automator 来统计字数，是个不花钱的好办法。安装我提供的 Automator 服务后，就能在右键菜单中看见字数统计的选项。

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/6894EFF6-EA74-4294-BC05-2DCF33D4516A.gif)

Automator 版效果

下面来看看这个动作的制作。

1. 我们先新建一个 Automator 服务，把输入设为文本，适用于所有应用。Automator 自带一个字数统计，但是不适用于中文，遂自己动手。   

   ![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/0F618401-B145-4B70-B1E9-BDC5C49F3DBD.png)

   Automator 配置

     
   这样一来，不管是**编辑器里的文本**，还是**网页和应用中的文字**，都能交给 Automator 去处理了。
2. 添加一个「运行 JavaScript」的步骤，把下面的代码粘进去：

```
    function run(input) {
    
    var text = input.toString()
    
    var cn_re = /^[\u4E00-\uFA29]*$/
    var word_re = /\w+/g
    var num_re = /\d+/g
    var symbol_re1 = /[，。、？！（）［］｛｝《》〈〉％＊“”]/
    var symbol_re2 = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/
    
    var cn_count = 0
    var word_count = 0
    var num_count = 0
    var symbol_count1 = 0
    var symbol_count2 = 0
    
    //统计英文单词数
    var word_list = text.match(word_re)
    if (word_list != null){
    var word_add = word_list.length;
    word_count += word_add
    }
    
    //统计数字数
    var num_list = text.match(num_re)
    if (num_list != null){
    var num_add = num_list.length;
    num_count += num_add
    }
    
    for (var i = 0; i < text.length; ++i) {
      var character = text.charAt(i)
      
    //统计中文字数
      if (cn_re.test(character)) {
        ++cn_count
      }
    
    //统计全角标点符号数
     if (symbol_re1.test(character)) {
        ++symbol_count1
     }
    
    //统计半角标点符号数
     if (symbol_re2.test(character)) {
        ++symbol_count2
     }
    }
    
    //计算总字数
    var sum_count = cn_count + word_count + num_count + symbol_count1 + symbol_count2/2
    
    Title = "总字数：" + sum_count
    
    app = Application.currentApplication()
    app.includeStandardAdditions = true
    app.displayNotification('统计完成', { 
      withTitle: Title, 
      soundName: 'Sosumi'
    })
    
    }
```

它们的意思就是先统计英文单词和数字出现的次数，再把文本挨个确认一遍，记下中文字数和标点符号数，随后加在一起。最后的五行代码（不算括号），用处则是发送一条带声音提示的通知，告诉你统计结果。

现在把 Automator 服务保存起来，在任意一个应用里选中一块文字，运行一下这个服务试试：

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/6894EFF6-EA74-4294-BC05-2DCF33D4516A.gif)

Automator 统计效果

统计结果和 Word 一样，但是在我测试下来，发现我的动作和 Word 在处理代码、公式时的差距还是比较大的。只是想快速知道大致字数的话，这个动作是合格的，进一步的统计（如理工科论文）仍然需要专门的编辑器。

LaunchBar 版
-----------

如果你在使用 LaunchBar，查看字数就更方便，只需要通过快捷键发送到 LaunchBar，再启动统计字数的动作。代码部分几乎和 Automator 版是一样的，只是头尾负责输入、输出变量的部分略有区别，这里不细讲了。

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/66C55EC3-1D10-4B8A-94E6-95C77BB14554.gif)

LaunchBar 统计效果

Drafts 版
--------

Drafts 版的动作（Action）由两个步骤组成，它们是：

1. Script 脚本：统计字数、定义一个名为 `sum_count`（总字数）的标签；
2. Prompt 框：弹出提示框，显示字数。

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/FF5DF15D-536B-4374-9570-784525AEA873.png)

Drafts 步骤

其中统计字数的部分，只要懂了 Automator 版本的代码，套用起来就轻车熟路；而「定义标签」则用到了 Drafts 的专有语法：

```
drafts.defineTag("sum_count", sum_count)
```

这样定义过的标签就能在之后的步骤中用到，其值为刚刚统计好的字数。

第二步 Prompt 中，在 MESSAGE 里填入刚才定义的标签 `[[sum_count]]`（记得两端套上两层方括号），就能弹出带有统计结果的通知了。

运行一下试试：

![](.evernote-content/BC11B3B1-1385-4989-BD29-C61877A0F2A1/70D49A2C-CB2A-4FF4-B6E0-AA6E5646FB88.gif)

Drafts 统计效果

关于在 Drafts 中使用自定义标签、Prompt 的用法以及 JavaScript 的知识，可以看我以前写的两篇文章：

* [从 OmniFocus 认识 Drafts 的 Prompt 用法](https://sspai.com/article/42367?series_id=9)
* [iOS 文本处理中的 JavaScript](https://sspai.com/article/44253?series_id=9)

小结
--

了解文章的字数可以让我们对其篇幅、结构有一个清晰的概念。某次帮同学改论文，对方还想辩解「我的摘要已经很精简了」，我咔咔敲几下快捷键，「总计 450 字」的横幅一弹出来，到底是太长还是太短就一目了然 1 。

很多时候，把一个东西量化了，我们就能看出隐含在其背后的信息。自己写文章也好、读别人的文章也好，希望我这几个统计字数的小工具可以帮你更好地了解文章。

1. [文科本科论文摘要一般在 300 字以内↩](#)

[#macOS](https://sspai.com/tag/macOS)[#文字编辑](https://sspai.com/tag/%E6%96%87%E5%AD%97%E7%BC%96%E8%BE%91)[#iOS](https://sspai.com/tag/iOS)

---

[🌐 原始链接](https://sspai.com/post/44485)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f4bd52db-beef-4351-a56b-9b8a97a2b6d6/f4bd52db-beef-4351-a56b-9b8a97a2b6d6/)