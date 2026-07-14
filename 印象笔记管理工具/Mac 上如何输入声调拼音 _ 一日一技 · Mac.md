---
tags: [★★★★★]
---

# Mac 上如何输入声调拼音 | 一日一技 · Mac

---

Mac 上如何输入声调拼音 | 一日一技・Mac
========================

2016 年 05 月 09 日

文档编辑中，偶尔会需要给生僻字、多音字加拼音标注。作为孩子的家长，早教阅读时还需要给整篇文章添加拼音。

如果只是简单的几个拼音，用系统自带的汉语词典查询之后复制到文章里就可以，输入法输入稍微麻烦一点，需要安装输入源「ABC（扩展）」， iOS 键盘上输入拼音比 Mac 键盘要简单，原生的拼音输入法就行。

大篇幅的文章添加拼音，推荐使用 Word for Mac 来完成，Pages 中虽然也有「拼音指南文本」，不过效率要低很多，而且没有什么参数可以设置。

输入法输入声调拼音
---------

Mac 默认的英文键盘长按元音字母也会弹出包含声调的选单，但是这个选单是给英语音标用的，以元音 a 为例，选择项中只有 â ，没有 ǎ 。

完整的支持四声调的拼音首先需要添加并选择输入源「ABC（扩展）」。输入时先输入声调，然后输入元音字母（先声调再元音），例如：`` option + ` ``，再按 o，可得到 ò。

1、2、3、4 声调分别对应的组合按键是： `` option + a、e、v、 ` ``

* `option + a，再按 a，可得到 ā。`
* `option + e，再按 a，可得到 á。`
* `option + v，再按 a，可得到 ǎ。`
* `` option + `，再按 a，可得到 à。 ``

给「ü」添加声调略微麻烦一点，先键入「option + u」输入两点 ¨ 再键入 u，就能获得「 ü 」，然后将光标保持在「 ü 」后，按键「shift+option+A、E、V、~」添加声调，分别输出 “ǖ、ǘ、ǚ、ǜ”。「shift+option+A、E、V、~」的添加声调的方式其实也可以用在给已经输入的元音添加拼音声调，操作方法也是将光标定位到需要添加的元音字母后，然后按对应的组合键。

感谢 @Roger Shen 的补充：其实 ü 的打法不需要这么麻烦，只需要按照之前的声调按键，即 option＋a、e、v、～, 然后再接着按 v 就会默认是 u 了。

![](.evernote-content/07AFACBD-A253-424F-B578-E9F3DD719412/3DAB6BD2-1A62-4C7E-902D-96B81AE93869.png)

「鼠须管」输入法输入拼音声调就简单的多，直接输入 /a 的方式就可以调出候选项。

iOS 系统键盘输入声调拼音
--------------

iOS 键盘上输入带声调的拼音比 Mac 上简单，直接长按元音字母就可以，所以如果嫌在 Mac 上倒腾麻烦，可以在 iPhone 或 iPad 上输入再同步（可借助备忘录同步）到 Mac 上。

![](.evernote-content/07AFACBD-A253-424F-B578-E9F3DD719412/B73B4812-0E00-451F-A010-27A716BA9ECF.png)

Mac 和 iOS 的通讯录实际上是支持自动添加拼音的，不过首先需要添加拼音的字段，有拼音的字段后，当你输入联系人的姓氏和名字后，系统会自动在拼音字段中补齐带声调的拼音。

![](.evernote-content/07AFACBD-A253-424F-B578-E9F3DD719412/659BDE39-4AF7-4020-9467-0C422AD9A4D5.png)

应用程序里快速获得声调拼音
-------------

系统自带的词典中包含「汉语词典」，可以通过查询汉字或者词语的方式在释义中复制拼音。

![](.evernote-content/07AFACBD-A253-424F-B578-E9F3DD719412/3D641CD8-AA48-4CB8-9E2F-B665649116C1.png)

Pages 中的拼音指南文本（格式 — 拼音指南文本）比较简单，选中文本后由菜单选择操作即可。

![](.evernote-content/07AFACBD-A253-424F-B578-E9F3DD719412/70A2C92E-AE9D-4F5F-945B-4E1E63FEFE66.png)

Word 的「拼音指南」包括了更丰富的拼音设定项，可以用来控制拼音的字体、大小、和汉字之间的距离以及对齐方式。不过 Word 中每次最多只能选择两行进行拼音标注，遇到大篇幅的内容会让人很头疼。Mac 版的 Word 对宏的支持相对于 Windows 版的 Word 有些简化，所以从网上搜索到的宏需要简单调整一下才能给 Mac 版的 Word 使用。

![](.evernote-content/07AFACBD-A253-424F-B578-E9F3DD719412/DDBB09DF-1A9E-417C-9836-CDF7AAD586D7.png)

Word 视图菜单中打开宏，新建一个宏，并将下面的代码复制进去即可。运行时选择对应的宏点「运行」。代码中包含两个宏，「逐句拼音」，需要选中内容后再运行宏命令；「清除拼音」运行后会清除当前文本的所有拼音。

```
Sub 逐句拼音()

st = Selection.Start
ed = Selection.End

For sen = Selection.Sentences.Count To 1 Step -1

With Selection
.Start = st
.End = ed

End With

Selection.Sentences(sen).Select

Application.Run MacroName:="FormatPhoneticGuide"

ed = Selection.Start

Next sen

End Sub

Sub 清除拼音()

Selection.WholeStory

TextLength = Selection.Characters.Count

Selection.GoTo What:=wdGoToHeading, Which:=wdGoToAbsolute, Count:=1

For i = 0 To TextLength

   With Selection

   .Range.PhoneticGuide Text:="", Alignment:=wdPhoneticGuideAlignmentOneTwoOne, Raise:=11, FontSize:=8, FontName:="MS Gothic"

   End With

   Selection.MoveRight Unit:=wdCharacter, Count:=1

Next

Selection.WholeStory

End Sub
```

---

Measure

Measure

---

[🌐 原始链接](https://sspai.com/post/34146)

[📎 在印象笔记中打开](evernote:///view/207087/s1/1378e036-2b04-485f-a82f-01f9677dc4b4/1378e036-2b04-485f-a82f-01f9677dc4b4/)