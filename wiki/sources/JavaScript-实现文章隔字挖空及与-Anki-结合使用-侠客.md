---
title: JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客
type: source
created: 2026-06-20
updated: 2026-06-20
source: 印象笔记
source_path: 印象笔记管理工具/JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客.md
tags: [印象笔记]
updated: 2026-06-27
---

---
title: "JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客"
source: evernote
type: note
export_date: 2026-06-24
guid: 1d6a8bfb-26c0-4ae5-afd6-b9e0defd10a1
---

# JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客

# JavaScript 实现文章隔字挖空及与 Anki 结合使用 – 侠客

好久没写博客了，好开心。还是在自己的博客写文章更舒服。

不知不觉已经过去这么久了，我即将成为一名大二的学生，哈哈哈哈哈哈哈哈容我先笑一会儿。想想也很神奇，我竟然会去学 “数学与应用数学”。好久没写过代码了，其实我也没写过什么像样的代码。

### 文章隔字挖空

还是称其为 “隔字替换” 吧，就是每隔一个单词，把后面的单词替换为一个小方块，把标点符号留着。

我先实现了一个段落的隔字替换。html 示例像这样：

```
<p id="first">Our vicar is always raising money for one cause or another, but he has never managed to get enough money to have the church clock repaired. The big clock which used to strike the hours day and night was damaged many years ago and has been silent ever since.</p>
```

我在 js 里使用 document.getElementById (“first”).innerHTML 获取 p 标签的内容 (字符串)，并将其保存到 sen 变量中（sen 是 sentence 缩写），用 sen.length 获取字符串中的字符个数，使用 sen [i] 访问每个字符。在遍历 sen 中的每个字符时，判断该字符是不是空格或换行符，如果是，说明从下一个字符开始就是一个新单词。通过变量 second 的值在 0 和 1 之间的不断转换判断是否遇到要替换的单词。使用 str += sen [i]; 语句将字符追加到变量 str 之中（str 是 string 缩写），直到遇到空格或换行符，这时将 second 变量的值对换（0 或 1），如果遇到了要替换的单词，就使用 str += “□”; 语句将一个小方块追加到 str 中，并跳过其余普通字符，如果再遇到空格或换行符，就再次改变 second 的值……

```
var sen;
var str = "";
var second;
var i;

sen = document.getElementById("first").innerHTML;

second = 0;
for (i = 0; i < sen.length; i++) {
    if (sen[i] == ' ' || sen[i] == '\n') {
        str += sen[i];//原样输出空格或换行符
        if (second == 0) {
            second = 1;
            str += "□";
        } else {
            second = 0;
        }
    } else if (second == 0) {
        str += sen[i];
    }
}
document.getElementById("first").innerHTML = str;
alert("ok");
```

因为是否遇到了新单词是通过空格和换行符判断的，在英语当中，标点符号和单词之间有时候是没有间隔的，所以标点符号也会被视为单词的一部分，如果这时直接将 “单词” 替换为方块，那么标点符号就没有了，在背文章时会很不方便。所以，我又增加了一个判断，通过给 state 变量赋值 0 和 1 来标明是否遇到了标点符号。

```
var sen;
var str = "";
var second;
var i;
var state;

sen = document.getElementById("first").innerHTML;

second = 1;
state = 1;
for (i = 0; i < sen.length; i++) {
    if (sen[i] == ' ' || sen[i] == '\n') {
        str += sen[i];//原样输出空格或换行符
        if (second == 0) {
            second = 1;
            //str += "□";
        } else {
            second = 0;
            state = 1;//注意这里重新给 state 赋值 1
        }
    } else if (second == 0) {
        str += sen[i];
    } else if (second == 1) {
        if (sen[i] == '\"' || sen[i] == '\'' || sen[i] == ',' || sen[i] == '.' || sen[i] == '!' || sen[i] == '?' || sen[i] == ';' || sen[i] == ':') {
            str += sen[i];
            state = 1;
        } else if (state == 1) {
            str += "□";
            state = 0;
        }
    }
}
document.getElementById("first").innerHTML = str;
alert("ok");
```

接下来实现多个段落的间隔替换，html 示例像这样：

```
<p class="en">Our vicar is always raising money for one cause or another, but he has never managed to get enough money to have the church clock repaired. The big clock which used to strike the hours day and night was damaged many years ago and has been silent ever since.</p>
<p class="en">One night, however, our vicar woke up with a start: the clock was striking the hours! Looking at his watch, he saw that it was one o'clock, but the bell struck thirteen times before it stopped. Armed with a torch, the vicar went up into the clock tower to see what was going on. In the torchlight, he caught sight of a figure whom he immediately recognized as Bill Wilkins, our local grocer.</p>
<p class="en">'Whatever are you doing up here Bill?' asked the vicar in surprise.</p>
<p class="en">'I'm trying to repair the bell,' answered Bill. 'I've been coming up here night after night for weeks now. You see, I was hoping to give you a surprise.'</p>
<p class="en">'You certainly did give me a surprise!' said the vicar. 'You've probably woken up everyone in the village as well. Still, I'm glad the bell is working again.'</p>
<p class="en">'That's the trouble, vicar,' answered Bill. 'It's working all right, but I'm afraid that at one o'clock it will strike thirteen times and there's nothing I can do about it.'</p>
<p class="en">'We'll get used to that, Bill,' said the vicar. 'Thirteen is not as good as one, but it's better than nothing. Now let's go downstairs and have a cup of tea.'</p>
```

我使用 document.getElementsByClassName (“en”) 获取类名为 en 的标签，使用 document.getElementsByClassName (“en”).length 获取标签个数，使用 document.getElementsByClassName (“en”)[i] 语句通过下标访问各结点，使用 document.getElementsByClassName (“en”)[i].innerHTML 访问结点内容（字符串），使用 document.getElementsByClassName (“en”)[i].innerHTML.length 获取结点内字符串的字符个数，使用 document.getElementsByClassName (“en”)[i].innerHTML [j] 访问字符串中的各个字符。在原来的代码外面加了一层 for 循环，其余代码不变。修改后的代码像这样：

```
var sen;
var str;
var second;
var i, j;
var state;

sen = document.getElementsByClassName("en");
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
                str += "□";
                state = 0;
            }
        }
    }
    sen[i].innerHTML = str;
}
```

我曾把 document.getElementsByClassName (“en”)[i].innerHTML.length 错误地写成 document.getElementsByClassName (“en”)[i].length。document.getElementsByClassName (“en”)[i] 是结点对象，document.getElementsByClassName (“en”)[i].innerHTML 才是结点内的字符串内容。

代码到这里就算完成了，通过修改变量 second 的初值（0 和 1），可以控制偶数替换或奇数替换。在 anki 内使用需要进一步结合实际情形修改。现在的效果是这样的：

![](attachments/ea5e4f80390f5610.png)

### 与 Anki 结合

新概念英语的课文包含以下几部分：课文序号、课文标题、课文前的问题、课文内容。

我期望为添加的课文生成两张卡片，一张是给偶数单词挖空，一张是给奇数单词挖空，两张卡片结合起来是一篇完整的课文。所以我在卡片类型 “基础的（和相反的卡片）” 的基础上新建了一个新卡片类型 “文章填空 (和相反卡片)”。我把该种卡片类型的 “区域” 改成 “课文序号”、“文章标题”、“Question”、“文章内容”。

在卡片模板编辑里，分别是 “卡片 1” 和 “卡片 2” 的正、反面模板代码框，CSS 样式代码框，右边是卡片预览。基本的 html 代码是这样的：

```
<section id = "title">

Lesson {{课文序号}} {{文章标题}}

</section>

<section id = "question">{{Question}}</section>

<section id = "content">

{{文章内容}}

</section>
```

分别将以上代码填入正、反面卡片模板代码框里，课文就会在右面的预览框里显示了。现在我们将之前写好的 js 代码加入正面卡片模板中，这样一来，卡片正面显示的是挖空后的课文，卡片背面显示的是完整的课文。我们需要对代码做一些修改。

需要挖空的是 id 属性为 content 的标签里的内容，anki 会为里面的内容的不同段落加上  
div 标签，所以我们把语句 sen = document.getElementsByClassName (“en”); 改为语句 sen = document.getElementById (“content”).getElementsByTagName (“div”); 现在的 js 代码是这样的：

```
    var sen;
    var str;
    var second;
    var i, j;
    var state;

    sen = document.getElementById("content").getElementsByTagName("div");

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
                    str += "?";
                    state = 0;
                }
            }
        }
        sen[i].innerHTML = str;
    }
```

在 “卡片 1 正面模板” 代码框里填入上述 html 和 script 标签包裹的 js 代码，在 “卡片 1 反面模板” 里填入上述 html 代码，在右边的预览框里就能看到我们成功了。卡片正面预览框里显示挖空后的文章，卡片背面预览框里显示完整文章。

把刚才填入 “卡片 1 正面模板” 的代码拷贝一份粘贴到 “卡片 2 正面模板” 里，把变量 second 的初值由 0 改为 1，在右面的卡片正面预览框里就能看到奇数单词被挖空的效果了。在 “卡片 2 反面模板” 里也填入上述 html 代码，右面的卡片反面预览框就能正确显示完整文章了。

然后，我们点开卡片编辑界面底部的 “更多”，改一下 “浏览器外观”。卡片浏览器默认显示两列，分别是 “问题” 和 “答案”，但我的模板显然是不能正常显示的，因为我的卡片有好多条内容。在 “忽略正面模板” 里我填入 “Lesson {{课文序号}} {{文章标题}}”，在 “忽略背面模板” 里我填入 “{{文章内容}}”，花括号会被替换为所指示区域内容。效果就是在卡片浏览器里，左边一栏显示文章序号和标题，右边一栏显示文章内容。

功能代码写好了，下面该考虑外观了。我阅读英文文章时很喜欢带衬线字体，还有，我打算模仿英语旧报纸上的文章样式把第一段的第一个字母放大。另外，Anki 没有适配高分屏，在我的电脑上显示很糟糕，我把字体调得特别大，而且我使用了相对大小。我的 CSS 代码是这样的：

```
.card {
    font-family: "Times New Roman", Georgia, serif;
    font-size: 3em;
    color: black;
    line-height: 1.35em;
    text-align: left;
}

#title {
    text-align: center;
    font-size: 1.25em;
    font-weight: bold;
}

#question {
    margin-top: .8em;
}

#content div {
    margin-top: .6em;
    text-indent: 1em;
}

#content div:first-child {
    text-indent: 0;
}

#content div:first-child::first-letter {
    font-size: 2em;
    font-weight: bold;
    margin-right: 4px;
    float: left;
}
```

第一段第一个字母放大、加粗，其他段落首行缩进。

在 PC 版 Anki 上一切正常，但我将卡片导入手机 AnkiDroid App 后，卡片正面不显示，卡片背面 CSS 样式错位。

我不知道原因出在哪里，难道是 Anki 对 JavaScript 的支持不到位吗？我接着去看 Anki 的中文版帮助文档。上面有段话是这样的：

> 每个 Anki 客户端可能不同地实现卡片的显示， 所以需要通过各平台来测试其运行。 许多客户端通过保持一个长期运行的网页并动态更新其部分作为对卡片的检验， 所以 Javascript 需要更新文档的区段而不是像 document.write 函数那样运行。

难道说真的是 Anki 对 JavaScript 的支持不够完善造成的问题吗？我又去看了英文版的帮助文档。真想一口老血喷出来，里面同一段是这样写的：

> Each Anki client may implement card display differently, so you will need to test the behaviour across platforms. A number of clients are implemented by keeping a long running webpage and dynamically updating parts of it as cards are reviewed, so your Javascript will need to update sections of the document using things like document.getElementById() rather than doing things like document.write().

既然 document.getElementById () 可以用那就不应该出问题啊？！那是哪儿的问题呢？我突然想到 CSS 样式也不正常，我原本以为是 Anki 对 CSS 中的伪类支持也不好，现在看来并不是这样。又联想到在 AnkiDroid “编辑笔记” 界面的 “文章内容” 区域看到的 div 标签，我灵光一闪，该不会是 AnkiDroid 为卡片各区域多加了一个 div 标签吧？！于是我用 CSS 为 id 为 content 的标签内的第一个子 div 标签添加了一个背景色红色来验证我的推论，标签内的所有文本背景色都变成了红色（如果没有加额外的 div 标签，只有文章的第一段的背景色会变成红色），我的推论是正确的。

{{文章内容}} 会被替换为用 div 标签包裹的文章内容，在 PC 版 Anki 里就像这样：

```
<section id = "content">
    <div></div>
    <div></div>
    <div></div>
    ...
</section>
```

而在 AnkiDroid 里却是这样的：

```
<section id = "content">
    <div>
        <div></div>
        <div></div>
        <div></div>
        ...
    </div>
</section>
```

因为多了一层 div 标签，js 和 CSS 都不正常是很正常的了。

找到问题出现在哪里就很好解决了，把 “获取 id 属性为 content 的结点中的所有标签名为 div 的结点” 改为 “获取 id 属性为 content 的结点中的第一个标签名为 div 的结点中的所有标签名为 div 的结点”，即把语句 sen = document.getElementById (“content”).getElementsByTagName (“div”); 改为 sen = document.getElementById (“content”).getElementsByTagName (“div”)[0].getElementsByTagName (“div”); 。在 AnkiDroid 上果然正常了。怎么做到 PC 和 手机都正常显示呢？

我又在 js 代码中增加了一个函数，判断客户端是 PC 还是 手机，加载不同的代码。现在我的 js 代码变成了这样：

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
                str += "?";
                state = 0;
            }
        }
    }
    sen[i].innerHTML = str;
}
```

现在在 PC 和 手机 上 js 代码都正常了。但 CSS 也得改。我在 Anki 的帮助文档中看到，可以为不同平台的 Anki 使用不同的样式，所以，我把 CSS 改成了这样：

```
.card {
    font-family: "Times New Roman", Georgia, serif;
}

.win {/*.card*/
    font-size: 3em;
    color: black;
    line-height: 1.35em;
    text-align: justify;
}

.win #title {
    text-align: center;
    font-size: 1.25em;
    font-weight: bold;
}

.win #question {
    margin-top: .8em;
}

.win #content div {
    margin-top: .6em;
    text-indent: 1em;
}

.win #content div:first-child {
    text-indent: 0;
}

.win #content div:first-child::first-letter {
    font-size: 2em;
    font-weight: bold;
    margin-right: 4px;
    float: left;
}

.mobile {
    font-size: 1.35em;
    color: black;
    line-height: 2em;
    text-align: justify;
}

.mobile #title {
    text-align: center;
    font-size: 1.25em;
    font-weight: bold;
}

.mobile #question {
    margin-top: .8em;
    text-align: center;
}

.mobile #content div div {
    margin-top: .6em;
    text-indent: 1em;
}

.mobile #content div div:first-child {
    text-indent: 0;
}

.mobile #content div div:first-child::first-letter {
    font-size: 2em;
    font-weight: bold;
    margin-right: 4px;
    float: left;
}
```

我把文本对齐方式由 “左对齐” 改为了 “两端对齐”，更美观了。

来欣赏一下最后的成果吧：

![](attachments/c1d7af58a613c32e.jpg)

![](attachments/26c4b6779f206f90.jpg)

![](attachments/1a676d92c04eb215.png)

![](attachments/fb4d268d9568bc9e.png)

![](attachments/1e1b639beace5212.png)

这篇文章到这里就结束了。
