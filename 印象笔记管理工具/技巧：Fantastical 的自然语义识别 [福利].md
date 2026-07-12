# 技巧：Fantastical 的自然语义识别 [福利]

---

![](.evernote-content/027A5920-9D68-42A6-A2DF-C12DD99D7112/D42B4066-7650-4A5A-8B78-7F8FDA9E6C0D.jpg)

自然语义处理是 [Fantastical](http://sspai.com/tag/Fantastical) 的招牌功能之一，也是和 x-callback-URL 结合必不可少的部分，iOS 上的 Fantastical 的效率性的核心就在于这两个功能。在 Mac 上用 Fantastical 的自然语义识别可以让我们做到在绝大多数情况下不需要碰鼠标来建立事件。

这篇文章详细来说下 [Fantastical](http://sspai.com/tag/Fantastical) 的自然语义是如何使用的。

时间与日期
-----

### **设定日期**

类别中文例子自然语义提示普通日期 11 月 1 日 `11/1` 或 `11.1`   星期几 周一到周日 `Mon`/`Tue`/`Wed`/`Tur`/`Fri`/`Sat`/`Sun` 用缩写即可 特定的周几 下周三 `Next Mon`   若干天后 15 天后 `After 15 Days`   重复 每周二 `Every Tue`     每隔两周的周三 `Wed Every 2 weeks` 或 `Every 2 weeks on Wed`     7 月 1日到 8 月 1 日之间的每个周一周二和周五 `on Mons Tues Fris from 7/1 to 8/1` 注意有 `s`   每个月 2 号 `Every 2`

### **设定时间**

类别中文例子自然语义提示24 小时制 下午一点 `13`   12 小时制 上午一点 `1a` 可以用 `am/pm` 也可以用 `a/p`，字母与前面的数字之间可空格也可不空。   下午一点 `1p`   分钟 下午一点半 `13:30` 或 `1.30p` 用冒号或者点都可以。 其它时间戳 早上 8 点 `Morning` 可以直接用 `Morning-16.30` 这样的形式   中午 12 点 `Noon`     下午 5 点 `Evening`     晚上 8 点 `Night`     半夜 12 点 `Midnight`

### **设定时间区间**

类别中文例子自然语义提示几号到几号 12 月 17 日到次年 1 月 3 日是寒假 `寒假 12/17-1/3` 会自动跨年 几点到几点 下午 1 点 32 到晚上 7 点 47 `1.32~7.47` 波浪线 和横线都可以

### **标记提醒**

类别中文例子自然语义提示小时 提前 18 小时提醒 `alert 18 hours` 前面加 alert 就好 分钟 提前 45 分钟提醒 `alert 45 min`

URL
---

只要在合适的位置附上 URL 格式的文本，链接就会自动添加到日历的 URL 部分，比如 `会议前看资料 http://sspai.com/31500`。

切换日历
----

用 `/` 加上日历名就可以直接把事件发送到对应日历，中英文皆可，比如 `/个人` 或 `/Work`。

这里推荐用英文命名日历，因为 Fantastical 可以直接识别首字母，这样比如 `/Personal` 这样的长单词你可以直接用 `/p` 来代替。

同时也能保证整个输入过程只切一次输入法（事件名输入用输入法，其它全用英文）。

待办事项
----

日历界面中可以直接输入 `todo`、`task`、`Remind` 和 `Remind me to` 来**直接建立提醒事项**。比如 `Remind me to 扫描账单` 就能直接把 `扫描账单` 添加到默认的清单里，如果想改变清单，可以使用 `/` 来指名切换。

待办事项和日历的自然语义识别共通的部分是一样的，另外还有一些待办事项独有的：

类别中文含义自然语义提示截止 11 月 27 日晚上 7 点截至 `due 11/27 8p` 或 `until 11/27 8p` 看来待办事项把这俩词当一个意思了…… 紧急度 低/中/高 `!`/`!!`/`!!!` 放哪都行，前后不用空格。叹号可能本身就是为了表语气…超过三个叹号紧急程度都是高。

注意
--

**1.** Fantastical 的自然语义的默认顺序是正常用英文描述事件的顺序：

（`Task`）`事件` `with 人物` `at 地点` `on 日期与时间` `提醒` `URL 链接` `日历名`

违背了这个默认的顺序可能会造成读取失效，但由于我们并不是使用英文，而且用中文输入地点和人名肯定会识别不出，所以那些介词可以适当省略。但如果出现错误就得严格按照英文语法来一遍试试。

**2.** 我在本文为了好看而区分大小写，使用的时候可以无视大小写。

**3.** 本文所有范例我都试过，没有问题。如果出了问题可以先试着加减元素和调换顺序，不要死板，用法可以举一反三，希望大家找到用着顺手并省事儿的输入方法。

**4.** 有 [TextExpander](http://sspai.com/tag/TextExpander) 的一定结合 TextExpander 来用！

### *编注 & 福利*

Fantastical 有 iPhone、iPad 和 Mac 三个版本，你可[点此获取](http://sspai.com/tag/fantastical%202)下载地址，以及少数派此前 [关于 Fantastical 的数十篇文章](http://sspai.com/tag/fantastical%202)。

另外，今天少数派联合「数码荔枝」为大家带来 Fantastical for Mac 的国内正版首发，价格仅为官方售价的一半：**129 元**，少数派读者可再减 **5 元**（领券即可）。此前因高昂价格不忍收下的朋友，这次别错过。

* **领券：**[少数派专享优惠券（5 元）](http://sspai.com/su/zii)
* **购买：**[Fantastical for Mac 购买地址 >](http://lizhi.io/f)
* **转发：**[抽奖微博（送 3 份授权码） >](http://weibo.com/1914010467/D3b5v8ykc?ref=)
* **评论：**在文末围绕 Fantastical 进行的所有评论中，11.17 号挑选一条优秀评论，送 1 份授权码。

![](.evernote-content/027A5920-9D68-42A6-A2DF-C12DD99D7112/B655D312-BCED-4B12-8BA8-4A3A92EAC508.jpg)

文章来源 [少数派](http://sspai.com) ，原作者 [JailbreakHum](http://sspai.com/author/681230) ，转载请注明原文链接

原文可获取应用下载链接：[技巧：Fantastical 的自然语义识别 [福利]](http://sspai.com/31734)  
喜欢少数派？欢迎关注我们的微博：@少数派sspai ，微信公众号： sspaime  
少数派（ <http://sspai.com> ）

[![](.evernote-content/027A5920-9D68-42A6-A2DF-C12DD99D7112/893EDB74-0FA1-48D9-9568-FF3FB18B9A1C.jpg)](http://sspai.com/collection/photography)

---

[🌐 原始链接](http://sspai.com/31734)

[📎 在印象笔记中打开](evernote:///view/207087/s1/90c1c4a1-e6ca-487d-b4a6-da52b80ae0fc/90c1c4a1-e6ca-487d-b4a6-da52b80ae0fc/)