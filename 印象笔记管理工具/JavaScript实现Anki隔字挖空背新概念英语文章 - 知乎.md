# JavaScript实现Anki隔字挖空背新概念英语文章 - 知乎

---

JavaScript 实现 Anki 隔字挖空背新概念英语文章
===============================

之前为了学好英语，在知乎浏览了很多人的回答、文章，看到

[@白诗诗](https://www.zhihu.com/people/55ff26531a113fd0e48dd0a0f0488f1f)

的一篇文章让我眼前一亮。我准备用

[@白诗诗](https://www.zhihu.com/people/55ff26531a113fd0e48dd0a0f0488f1f)

介绍的方法背《新概念英语・第三册》。这种记忆方式很简单，就是在要背的文章中每隔一个单词挖一个空，通过对空缺的单词的联想，很快地完成对整篇文章的记忆。就像这样：

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/1191F0A7-AE0F-401E-A71E-3634B8454EF4.jpg)

隔字挖空示例

白诗诗介绍这种方法的文章在知乎收获了很多的赞，更有人写了一个工具 “背个 X 啊” 来完成对单词的挖空，后来也出了 APP。但我觉得不够优雅，也不实用。不能多终端同步，背文章时还要自己手动去转换，如果文章中有单词拼写错误，需要在改正后再手动重新转换。最让我不能忍受的是，“背个 X 啊” 网页版工具是有 bug 的。我也曾私信过开发者

[@自定义](https://www.zhihu.com/people/18c3b4ccee8b519707a2ece4239af59f)

（下图），直到现在这个 bug 也没解决（后来出的 APP 版好像没这个 bug），所以我就自己写了一个，用 JavaScript 实现的。和 Anki 结合起来，不再需要手动转换文本，而且能够多终端同步，电脑手机都能用，还有网页版的 AnkiWeb，简直不要太方便。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/4C059F23-349B-4F50-A9BE-9947D289A738.jpg)

我和开发者 @自定义的知乎私信

确实，Anki 通常都用来记忆短小的知识点，但工具是死的、人是活的，当然是怎么方便怎么来。制作卡片时，会自动生成两个卡片，这两个卡片正面显示的文章是互补的。在 Anki 中储存的只有课文原文，并不会储存转换后的文本，文本转换过程是在卡片显示时进行的。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/423D58CD-E9E8-4AB8-9BC9-16FF3078351F.jpg)

用 Anki 背文章过程 - 卡片正面

单击 “显示答案” 后会显示完整的课文内容。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/CC712B02-5465-44B1-A7FB-00CD82D88929.jpg)

这是另一张卡片，正面挖空的单词正好是与另一张卡片相反的。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/3F5E3B28-4EDA-4F69-B52C-075AE4E84B23.jpg)

另一张卡片，正面挖空的单词与前一张相反

制作卡片时，只需要填写常规的 “课文编号、课文标题、段前问题、课文内容” 就可以。如果不小心拼错了什么单词，回过头来改正就行了，不会对转换后的文本产生任何错误影响，非常适合完美主义者。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/1078976A-83BF-4612-ACC3-D2CC90A79B37.jpg)

添加笔记制作卡片

不仅仅是《新概念英语》，你用来背其他的英文文章也可以。重点不是 Anki，而是我写的代码，我用 Anki 只是为了方便。代码是可以复用的。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/93BE2FB4-549E-4D53-BCF2-E58C050CA36F.jpg)

代码和卡片预览

每天背一篇课文我觉得是很合适的，不需要多。在选项里把每天的新卡片数量改成 2 就行了（一篇课文对应两张卡片）。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/D46697F1-EA24-4F87-857E-1313FD3D5513.jpg)

记忆库选项

因为 Anki 没有适配高分屏，而我的电脑是 Surface Pro 4，显示效果很糟糕，所以我把字体调得特别大，如果在你的电脑或手机上字体大小不合适，你改一下就行了，我在 CSS 样式代码里加了注释。卡片样式比较朴素，但对我来说已经很美观了，如果你喜欢可以自定义 CSS 样式。

在手机上的显示效果：

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/C3F63AF8-1914-4807-9E10-F2C53EB29C4C.jpg)

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/A559B148-910F-4FC0-A6EA-6997DECA772A.jpg)

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/E72C45DE-A6D8-4D52-8C27-9697A3900FA7.jpg)

卡片浏览器

下面给出具体代码。如果你没有时间去看代码，直接用我的模板就可以了，模板下载地址：

[https://pan.baidu.com/s/1dP\_vNOgEJFAxBLmddyCcSg](https://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1dP_vNOgEJFAxBLmddyCcSg)

在此吐槽某些人，如果你真的是想分享自己的成果，就大方一点，别藏着掖着、在评论区留下邮件地址才给下载链接，你这样做让我感觉怪怪的。没错我说的就是

[@堇力思](https://www.zhihu.com/people/10dcd559f567e168d68e40d69d8254de)

，一年前我在他的某篇文章下发表上述类似言论（具体我怎么说的不记得了，好像我还提到了百度贴吧）被他拉黑、评论折叠。我很生气。

下面是我本来想发给他的私信内容，但因为被拉黑没有发送成功。

![](.evernote-content/0A38D706-C0C2-4E03-86DA-7DBD0D762732/54626475-355B-4F84-9966-1456ED389AA8.jpg)

---

JavaScript 代码如下：

```
var sen;
var str;
var second;
var i, j;
var state;

function loadjs() {
    if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|wOSBrowser|BrowserNG|WebOS)/i))) {
        sen = document.getElementById("content").getElementsByTagName("div")[0].getElementsByTagName("div");
    } else {
        sen = document.getElementById("content").getElementsByTagName("div");
    }
}

loadjs();

for (i = 0; i < sen.length; i++) {
    str = "";
    second = 0;//控制奇数挖空或偶数挖空
    state = 1;
    for (j = 0; j < sen[i].innerHTML.length; j++) {
        if (sen[i].innerHTML[j] == ' ' || sen[i].innerHTML[j] == '\n') {
            str += sen[i].innerHTML[j];//原样输出空格或换行符
            if (second == 0) {
                second = 1;
            } else {
                second = 0;
                state = 1;
            }
        } else if (second == 0) {
            str += sen[i].innerHTML[j];
        } else if (second == 1) {
            if (sen[i].innerHTML[j] == '\"' || sen[i].innerHTML[j] == '\'' || sen[i].innerHTML[j] == ',' || sen[i].innerHTML[j] == '.' || sen[i].innerHTML[j] == '!' || sen[i].innerHTML[j] == '?' || sen[i].innerHTML[j] == ';' || sen[i].innerHTML[j] == ':') {
                str += sen[i].innerHTML[j];
                state = 1;
            } else if (state == 1) {
                str += "☐";
                state = 0;
            }
        }
    }
    sen[i].innerHTML = str;
}
```

代码是逐渐丰富的。一开始代码很简单，只是简单地判断是否遍历到第二个单词，是的话就在 str 字符串变量里增加一个小方块□，后来慢慢增加规则，就变成了现在这样子。

我本来是想从前到后写一下我的思考过程的，但文章现在已经很长了，那我一会儿再另外写一篇好了。不知道是知乎的编辑器的问题还是我的键盘的问题，我用拼音输入法打出来汉字后后面会出现一串英文字母，正好是汉字的拼音字母的反序，我猜是知乎的自动保存功能出的问题。

这是我在写这篇文章之前写的一些个人感想，本来是放在开头的，想了想还是放在文章末尾吧：

完成一件有挑战性的事情，会获得成就感，心情也会美美哒。好像很多人喜欢通过背书、背单词获得成就感，但是 “记忆” 真的能获得成就感吗？我很怀疑。在 2017 年我参加了扇贝的新年计划，每天打卡就跟完成任务似的，都是到最后一刻才很不情愿地打卡，好在最后完成了计划，打卡 300 天整。过一段时间看到自己的打卡天数时确实有成就感，但每天打卡我的确有一种敷衍的感觉，更别提成就感了。我的成就感，更多地来自 “解决或理解了一道自认为的数学难题”、“写了一个很有意思的程序”、“新学会了什么酷炫的轮滑动作”、“新学会了一首口琴曲” 这些有明确的终点的事情。如果让我在 “每天去背一些根本背不完的单词” 和 “做完《吉米多维奇数学分析习题集》” 之间选择，我肯定会选择后者。

“工欲善其事，必先利其器”，所以没必要去迁就 “器”。如果你有能力，就按照自己的需求去打造一套适合自己的工具，没有.... 就算了吧。年轻人逛知乎要学会独立思考，一些人自认为的 “优点” 恰恰是别人讨厌他的原因，而这些人总是喜欢在知乎上显露自己的 “优点”。用 Anki 不是什么有优越感的事情，也没必要神化 Anki，怎么方便怎么来，怎么适合自己的需求怎么来。

---

2018 年 7 月 22 日更新：我把思考过程写在了自己博客里，链接：

---

2019 年 4 月 9 日更新：

针对许多朋友反映的自己添加的卡片不能正常挖空的问题，我研究了一下，是 Anki 的内容储存结构改变导致的。我重写了代码，不仅解决了上述问题，更支持了中文短文挖空，也做到了不同设备加载代码的统一。新的代码我已上传至 GitHub 开源。详情和新卡片组的下载可以浏览下面这篇文章：

---

The end.

---

[🌐 原始链接](https://zhuanlan.zhihu.com/p/40219067)

[📎 在印象笔记中打开](evernote:///view/207087/s1/f01d1155-e1eb-43a7-b659-f732e6591804/f01d1155-e1eb-43a7-b659-f732e6591804/)